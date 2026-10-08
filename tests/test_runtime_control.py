"""Selection/package tests, not behavioral model evaluations."""
import itertools
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.runtime_control import load_policy, select_control, validate_record


class ControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = load_policy()
        cls.suite = json.loads((ROOT / "evaluations/control-cases.json").read_text())
        cls.schema = json.loads((ROOT / "schemas/runtime-control.schema.json").read_text())
        cls.validator = Draft202012Validator(cls.schema)

    def test_supplied_selection_fixtures(self):
        self.assertEqual(len(self.suite["cases"]), 16)
        for case in self.suite["cases"]:
            with self.subTest(case=case["id"]):
                result = select_control(**case["selection_fixture"])
                for key, expected in case["expected_selection"].items():
                    self.assertEqual(result[key], expected)
                self.validator.validate(result)
                validate_record(result)

    def test_exhaustive_request_floor_combinations(self):
        requests = ["auto", "fast", "standard", "deep", "maximum", 0, 1, 2, 3, 4]
        for proposed, request, rule in itertools.product(range(5), requests, self.policy["rules"]):
            with self.subTest(proposed=proposed, request=request, rule=rule["id"]):
                result = select_control(proposed, request, [rule["id"]])
                candidate = proposed if request == "auto" else (
                    request if type(request) is int else self.policy["depth_mapping"][request])
                self.assertEqual(result["effective_level"], max(rule["minimum_level"], candidate))
                self.validator.validate(result)
                validate_record(result)

    def test_additional_rule_cannot_lower_floor(self):
        ids = [r["id"] for r in self.policy["rules"]]
        for a, b in itertools.combinations(ids, 2):
            joined = select_control(0, "fast", [a, b])
            self.assertGreaterEqual(joined["effective_level"], select_control(0, "fast", [a])["effective_level"])
            self.assertGreaterEqual(joined["effective_level"], select_control(0, "fast", [b])["effective_level"])

    def test_direct_label_cannot_cancel_authority_floor(self):
        result = select_control(0, "fast", ["direct-transformation", "authority-sensitive"])
        self.assertEqual(result["effective_level"], 3)
        self.assertEqual(result["override_outcome"], "clamped_to_floor")

    def test_bundles_are_cumulative(self):
        previous = set()
        for level in range(5):
            result = select_control(level, "auto", ["direct-transformation"])
            current = set(result["required_components"])
            self.assertTrue(previous <= current)
            self.assertIn("no_fabrication", current)
            self.assertIn("authority_boundary", current)
            self.assertIn("agency_preservation", current)
            previous = current

    def test_unknown_duplicate_empty_or_wrong_rule_container(self):
        for rules in ([], ["bogus"], [None], ["direct-transformation"] * 2, "direct-transformation", None):
            with self.subTest(rules=rules), self.assertRaises(ValueError):
                select_control(0, "auto", rules)

    def test_invalid_proposed_level(self):
        for value in (True, False, -1, 5, 1.0, "1", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                select_control(value, "auto", ["direct-transformation"])

    def test_invalid_requested_depth(self):
        for value in (True, False, -1, 5, 1.0, "high", "0", "", None, []):
            with self.subTest(value=value), self.assertRaises(ValueError):
                select_control(1, value, ["standard-reasoning"])

    def test_rule_order_does_not_change_selection(self):
        a = select_control(2, "auto", ["authority-sensitive", "evidence-conflict"])
        b = select_control(2, "auto", ["evidence-conflict", "authority-sensitive"])
        self.assertEqual(a, b)
        b["matched_rule_ids"].reverse()
        validate_record(b)

    def test_explicit_decrease_preserves_floor(self):
        result = select_control(4, 2, ["governed-analysis"])
        self.assertEqual(result["effective_level"], 2)
        self.assertEqual(result["override_outcome"], "accepted")

    def test_schema_alone_does_not_check_arithmetic(self):
        result = select_control(1, "fast", ["authority-sensitive"])
        result["effective_level"] = 0
        self.validator.validate(result)  # Well-shaped but semantically inconsistent.
        with self.assertRaises(ValueError):
            validate_record(result)

    def test_tampered_records_are_rejected(self):
        original = select_control(1, "fast", ["authority-sensitive"])
        changes = {"profile_version": "9", "assessment_kind": "verified", "mandatory_minimum_level": 0,
                   "effective_level": True, "override_outcome": "accepted", "required_components": [],
                   "authorized": True, "checks_completed": True}
        for key, value in changes.items():
            with self.subTest(key=key), self.assertRaises(ValueError):
                changed = dict(original, **{key: value})
                validate_record(changed)

    def test_missing_or_non_object_records_are_rejected(self):
        for value in (None, [], "record", {}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_record(value)
        result = select_control(1, "auto", ["standard-reasoning"])
        del result["required_components"]
        with self.assertRaises(ValueError):
            validate_record(result)

    def test_record_cannot_assert_completed_checks(self):
        result = select_control(3, "auto", ["authority-sensitive"])
        self.assertEqual(result["assessment_kind"], "selection_only")
        for forbidden in ("verified", "authorized", "executed", "checks_completed"):
            self.assertNotIn(forbidden, result)

    def test_entrypoint_floor_table_matches_policy(self):
        text = (ROOT / "SKILL.md").read_text()
        table = dict((name, int(value)) for name, value in
                     re.findall(r"^\| `([^`]+)` \| ([0-4]) \|", text, re.M))
        self.assertEqual(table, {r["id"]: r["minimum_level"] for r in self.policy["rules"]})

    def test_entrypoint_keeps_core_checks_within_size_budget(self):
        text = (ROOT / "SKILL.md").read_text()
        self.assertLessEqual(len(text.split()), 2400)
        self.assertLessEqual(len(text.splitlines()), 240)
        for phrase in ("Say what is true", "Extract nothing", "Protect the other party's next move",
                       "Do not trade truth", "Preserve scope", "mandatory minimum", "Do not expose private chain-of-thought"):
            self.assertIn(phrase, text)

    def test_source_lineage_identifies_source_without_version_mythology(self):
        text = (ROOT / "references/source-lineage.md").read_text()
        self.assertIn("0e4cbad99ab04c6171690afacb8b7842a7338a9b33e734b25c6daa451a1afac4", text)
        self.assertIn("renumbered", text)
        self.assertIn("New public operationalization", text)
        self.assertEqual(len(re.findall(r"^\| [0-9]+\.", text, re.M)), 28)

    def test_cases_are_unique_and_behavioral_runs_unexecuted(self):
        self.assertEqual(self.suite["behavioral_evaluation_status"], "unexecuted")
        ids = [c["id"] for c in self.suite["cases"]]
        self.assertEqual(len(ids), len(set(ids)))
        for case in self.suite["cases"]:
            for key in ("input", "expected_behavior", "failure_criteria"):
                self.assertTrue(case[key])

    def test_examples_validate(self):
        example = json.loads((ROOT / "examples/runtime-control.authority.json").read_text())
        self.validator.validate(example)
        validate_record(example)
        schema = json.loads((ROOT / "schemas/reasoning-plan.schema.json").read_text())
        validator = Draft202012Validator(schema)
        validator.validate(json.loads((ROOT / "examples/reasoning-plan.conflicting-evidence.json").read_text()))
        blocks = re.findall(r"```json\n(.*?)\n```", (ROOT / "references/reasoning-effort.md").read_text(), re.S)
        self.assertTrue(blocks)
        for block in blocks:
            validator.validate(json.loads(block))

    def test_cli_positive_and_negative_paths(self):
        command = [sys.executable, str(ROOT / "tools/runtime_control.py")]
        ok = subprocess.run(command + ["--proposed-level", "1", "--requested-depth", "fast", "--rule", "authority-sensitive"], capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertEqual(json.loads(ok.stdout)["effective_level"], 3)
        bad = subprocess.run(command + ["--proposed-level", "1", "--rule", "unknown"], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 2)
        self.assertEqual(bad.stdout, "")
        checked = subprocess.run(command + ["--validate", str(ROOT / "examples/runtime-control.authority.json")], capture_output=True, text=True)
        self.assertEqual(checked.returncode, 0, checked.stderr)
        self.assertIn("not verified", checked.stdout)


if __name__ == "__main__":
    unittest.main()
