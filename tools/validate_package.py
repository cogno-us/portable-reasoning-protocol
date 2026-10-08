"""Offline structural checks; not model-efficacy or IP-clearance certification."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.runtime_control import validate_record


def main() -> int:
    errors = []
    json_count = yaml_count = link_count = 0
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"\A---\n(.*?)\n---", skill, re.S)
    if not front:
        errors.append("SKILL.md: missing frontmatter")
    else:
        metadata = yaml.safe_load(front.group(1))
        if set(metadata) != {"name", "description"}:
            errors.append("SKILL.md: unexpected frontmatter fields")
        if metadata.get("name") != "portable-reasoning-protocol":
            errors.append("SKILL.md: changed Skill identity")
        if not isinstance(metadata.get("description"), str) or len(metadata["description"]) > 1024:
            errors.append("SKILL.md: invalid description")
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix == ".json":
            try:
                data = json.loads(path.read_text(encoding="utf-8")); json_count += 1
                if path.name.endswith(".schema.json"):
                    Draft202012Validator.check_schema(data)
            except Exception as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")
        elif path.suffix in {".yaml", ".yml"}:
            try:
                yaml.safe_load(path.read_text(encoding="utf-8")); yaml_count += 1
            except Exception as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")
        elif path.suffix == ".md":
            text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
            for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", text):
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue  # No remote HTTP availability claim.
                dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
                if not dest.is_relative_to(ROOT.resolve()) or not dest.exists():
                    errors.append(f"{path.relative_to(ROOT)}: missing/escaping target {target}")
                    continue
                link_count += 1
                if parsed.fragment and dest.suffix == ".md":
                    headings = re.findall(r"^#+\s+(.+)$", dest.read_text(encoding="utf-8"), re.M)
                    anchors = {re.sub(r"[^a-z0-9_ -]", "", h.lower()).replace(" ", "-") for h in headings}
                    if unquote(parsed.fragment) not in anchors:
                        errors.append(f"{path.relative_to(ROOT)}: missing anchor {target}")
    try:
        schema = json.loads((ROOT / "schemas/reasoning-plan.schema.json").read_text())
        validator = Draft202012Validator(schema)
        validator.validate(json.loads((ROOT / "examples/reasoning-plan.conflicting-evidence.json").read_text()))
        for block in re.findall(r"```json\n(.*?)\n```", (ROOT / "references/reasoning-effort.md").read_text(), re.S):
            validator.validate(json.loads(block))
        control = json.loads((ROOT / "examples/runtime-control.authority.json").read_text())
        control_schema = json.loads((ROOT / "schemas/runtime-control.schema.json").read_text())
        Draft202012Validator(control_schema).validate(control)
        validate_record(control)
    except Exception as exc:
        errors.append(f"Example validation: {exc}")
    for path in ("LICENSE", "NOTICE"):
        if not (ROOT / path).is_file():
            errors.append(f"Missing {path}")
    if errors:
        print("FAIL\n" + "\n".join(errors))
        return 1
    print(f"PASS: {json_count} JSON, {yaml_count} YAML, {link_count} local Markdown links/anchors; examples and frontmatter")
    print("Static checks only. No model evaluations, source truth or authorization verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
