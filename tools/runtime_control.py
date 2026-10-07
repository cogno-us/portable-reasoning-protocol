"""Offline PRP selection arithmetic over supplied rule matches; no model calls.

Passing this check establishes record consistency only. It does not establish
correct task classification, performed verification, authority or model behavior.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "policies/runtime-control.v1.json"


def _level(value: Any, label: str) -> int:
    # bool is an int subclass in Python, but is not a valid level.
    if type(value) is not int or not 0 <= value <= 4:
        raise ValueError(f"{label} must be an integer from 0 through 4")
    return value


def load_policy() -> dict[str, Any]:
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    if policy.get("profile_version") != "1.0.0":
        raise ValueError("Unsupported control profile")
    ids = [r["id"] for r in policy["rules"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate policy rule ID")
    for rule in policy["rules"]:
        _level(rule["minimum_level"], "policy minimum")
    return policy


def select_control(proposed_level: int, requested_depth: str | int,
                   matched_rule_ids: list[str]) -> dict[str, Any]:
    """Calculate selection only; the caller must identify applicable rules."""
    proposed = _level(proposed_level, "proposed_level")
    policy = load_policy()
    rules = {r["id"]: r["minimum_level"] for r in policy["rules"]}
    if not isinstance(matched_rule_ids, list) or not matched_rule_ids:
        raise ValueError("Supply a nonempty list of matched rule IDs")
    if any(not isinstance(r, str) or r not in rules for r in matched_rule_ids):
        raise ValueError("Unknown or non-string rule ID")
    if len(matched_rule_ids) != len(set(matched_rule_ids)):
        raise ValueError("Duplicate matched rule IDs")
    matched = sorted(matched_rule_ids)
    floor = max(rules[r] for r in matched)
    if type(requested_depth) is int:
        candidate = _level(requested_depth, "requested_depth")
    elif isinstance(requested_depth, str) and requested_depth == "auto":
        candidate = proposed
    elif isinstance(requested_depth, str) and requested_depth in policy["depth_mapping"]:
        candidate = policy["depth_mapping"][requested_depth]
    else:
        raise ValueError("requested_depth must be auto/fast/standard/deep/maximum or integer 0-4")
    effective = max(floor, candidate)
    if requested_depth == "auto":
        outcome = "not_requested"
    elif candidate < floor:
        outcome = "clamped_to_floor"
    elif candidate == proposed:
        outcome = "unchanged"
    else:
        outcome = "accepted"
    components = [c for level in range(effective + 1)
                  for c in policy["level_additions"][str(level)]]
    return {
        "profile_version": policy["profile_version"],
        "assessment_kind": "selection_only",
        "proposed_level": proposed,
        "requested_depth": requested_depth,
        "mandatory_minimum_level": floor,
        "effective_level": effective,
        "matched_rule_ids": matched,
        "override_outcome": outcome,
        "required_components": components,
    }


def validate_record(record: Any) -> None:
    """Reject structurally or arithmetically inconsistent selection records."""
    if not isinstance(record, dict):
        raise ValueError("Record must be an object")
    try:
        expected = select_control(record["proposed_level"], record["requested_depth"],
                                  record["matched_rule_ids"])
    except KeyError as exc:
        raise ValueError(f"Missing field: {exc.args[0]}") from exc
    if set(record) != set(expected):
        raise ValueError("Record fields do not match the selection-only profile")
    _level(record["mandatory_minimum_level"], "mandatory_minimum_level")
    _level(record["effective_level"], "effective_level")
    # IDs are a set; calculator output sorts them for reproducibility.
    normalized = dict(record, matched_rule_ids=sorted(record["matched_rule_ids"]))
    if normalized != expected:
        raise ValueError("Inconsistent profile, floor, effective level, override or component bundle")


def _request(text: str) -> str | int:
    return int(text) if text in {"0", "1", "2", "3", "4"} else text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", type=Path, help="Validate an existing selection record")
    parser.add_argument("--proposed-level", type=int)
    parser.add_argument("--requested-depth", default="auto", type=_request)
    parser.add_argument("--rule", action="append", dest="rules")
    args = parser.parse_args()
    try:
        if args.validate:
            if args.proposed_level is not None or args.rules or args.requested_depth != "auto":
                raise ValueError("Do not combine --validate with selection arguments")
            record = json.loads(args.validate.read_text(encoding="utf-8"))
            validate_record(record)
            print("PASS: selection record is consistent; behavior and authority are not verified")
        else:
            record = select_control(args.proposed_level, args.requested_depth, args.rules)
            print(json.dumps(record, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
