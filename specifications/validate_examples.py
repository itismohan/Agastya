#!/usr/bin/env python3
"""Validate canonical specification examples against the JSON Schema."""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit(
        "The jsonschema package is required. Install it with: sudo pip3 install jsonschema"
    ) from exc

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "schemas" / "agastya-canonical-specification.schema.json"
EXAMPLE_DIR = ROOT / "examples"
INSTANCE_DIR = ROOT / "instances"


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    paths = sorted(EXAMPLE_DIR.glob("*.json")) + sorted(INSTANCE_DIR.glob("*.json"))
    if not paths:
        print("No specification documents found.")
        return 1

    valid = True
    for path in paths:
        document = load_json(path)
        errors = sorted(validator.iter_errors(document), key=lambda error: list(error.absolute_path))
        if errors:
            valid = False
            print(f"INVALID  {path.relative_to(ROOT)}")
            for error in errors:
                location = "/" + "/".join(str(segment) for segment in error.absolute_path)
                print(f"  {location or '/'}: {error.message}")
        else:
            print(f"VALID    {path.relative_to(ROOT)}")

    return 0 if valid else 1


if __name__ == "__main__":
    sys.exit(main())
