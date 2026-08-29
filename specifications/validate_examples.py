#!/usr/bin/env python3
"""Validate AGASTYA canonical specifications and repository cross-references."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit(
        "The jsonschema package is required. Install it with: python -m pip install jsonschema"
    ) from exc

ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = ROOT.parent
SCHEMA_PATH = ROOT / "schemas" / "agastya-canonical-specification.schema.json"
EXAMPLE_DIR = ROOT / "examples"
INSTANCE_DIR = ROOT / "instances"
SPEC_DOC_PATTERN = "SPEC-PLATFORM-*.md"
SPEC_TOKEN = re.compile(r"\bSPEC-PLATFORM-\d{3}\b")
MARKER_PATTERN = re.compile(r"\[\.\.\.\]|file truncated for brevity|TODO|FIXME", re.IGNORECASE)
LOCAL_LINK_PATTERN = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")
EXPECTED_IDS = {f"SPEC-PLATFORM-{index:03d}" for index in range(1, 13)}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def relative(path: Path) -> str:
    return path.relative_to(REPOSITORY_ROOT).as_posix()


def iter_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from iter_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_strings(child)


def check_schema_documents(schema: dict[str, Any]) -> tuple[bool, set[str]]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    paths = sorted(EXAMPLE_DIR.glob("*.json")) + sorted(INSTANCE_DIR.glob("*.json"))
    if not paths:
        print("ERROR  No specification JSON documents found.")
        return False, set()

    valid = True
    instance_ids: set[str] = set()
    example_ids: set[str] = set()
    required = set(schema.get("required", []))

    for path in paths:
        try:
            document = load_json(path)
        except (OSError, json.JSONDecodeError) as error:
            print(f"INVALID  {relative(path)}: {error}")
            valid = False
            continue

        errors = sorted(validator.iter_errors(document), key=lambda error: list(error.absolute_path))
        if errors:
            valid = False
            print(f"INVALID  {relative(path)}")
            for error in errors:
                location = "/" + "/".join(str(segment) for segment in error.absolute_path)
                print(f"  {location or '/'}: {error.message}")
        else:
            print(f"VALID    {relative(path)}")

        if isinstance(document, dict):
            spec_id = document.get("id")
            if isinstance(spec_id, str):
                if path.parent == INSTANCE_DIR:
                    if spec_id in instance_ids:
                        print(f"ERROR  Duplicate canonical instance id: {spec_id}")
                        valid = False
                    instance_ids.add(spec_id)
                elif path.parent == EXAMPLE_DIR:
                    example_ids.add(spec_id)
                if path.parent in (INSTANCE_DIR, EXAMPLE_DIR):
                    missing = sorted(required - document.keys())
                    if missing:
                        print(f"INCOMPLETE  {relative(path)} missing root fields: {', '.join(missing)}")
                        valid = False

    available_ids = instance_ids | example_ids
    missing_ids = EXPECTED_IDS - available_ids
    unexpected_ids = available_ids - EXPECTED_IDS
    if missing_ids:
        print(f"INCOMPLETE  Missing canonical documents: {', '.join(sorted(missing_ids))}")
        valid = False
    if unexpected_ids:
        print(f"ERROR  Unexpected canonical ids: {', '.join(sorted(unexpected_ids))}")
        valid = False
    return valid, available_ids


def check_markdown_completeness() -> bool:
    valid = True
    documents = sorted(ROOT.glob(SPEC_DOC_PATTERN))
    found_ids: set[str] = set()
    if not documents:
        print("ERROR  No platform specification Markdown documents found.")
        return False

    for path in documents:
        text = path.read_text(encoding="utf-8")
        matches = SPEC_TOKEN.findall(text)
        expected = path.stem
        if expected not in matches:
            print(f"INCOMPLETE  {relative(path)} does not identify itself as {expected}")
            valid = False
        found_ids.add(expected)
        if len(text.strip()) < 500 or text.count("\n## ") < 3:
            print(f"INCOMPLETE  {relative(path)} lacks the minimum specification structure")
            valid = False
        marker = MARKER_PATTERN.search(text)
        if marker:
            print(f"INCOMPLETE  {relative(path)} contains placeholder/truncation marker: {marker.group(0)}")
            valid = False

        for link in LOCAL_LINK_PATTERN.findall(text):
            if "://" in link or link.startswith("#"):
                continue
            target = (path.parent / link).resolve()
            if not target.exists():
                print(f"BROKEN-REF  {relative(path)} -> {link}")
                valid = False

    missing = EXPECTED_IDS - found_ids
    if missing:
        print(f"INCOMPLETE  Missing platform specification documents: {', '.join(sorted(missing))}")
        valid = False
    return valid


def check_cross_references(instance_ids: set[str]) -> bool:
    valid = True
    referenced: dict[str, set[str]] = {}
    paths = sorted(ROOT.rglob("*.md")) + sorted(ROOT.rglob("*.json"))
    for path in paths:
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        tokens = set(SPEC_TOKEN.findall(text))
        referenced[relative(path)] = tokens
        unknown = sorted(tokens - EXPECTED_IDS)
        if unknown:
            print(f"BROKEN-REF  {relative(path)} references unknown ids: {', '.join(unknown)}")
            valid = False

    if not instance_ids.issuperset(EXPECTED_IDS):
        print("BROKEN-REF  Cross-reference validation is blocked by missing canonical instances")
        return False

    total_refs = sum(len(tokens) for tokens in referenced.values())
    print(f"CROSS-REF  Checked {len(referenced)} repository documents and {total_refs} specification references")
    return valid


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cross-references",
        action="store_true",
        help="also check specification completeness, local Markdown links, and cross-references",
    )
    args = parser.parse_args()

    schema = load_json(SCHEMA_PATH)
    valid, instance_ids = check_schema_documents(schema)
    if args.cross_references:
        valid = check_markdown_completeness() and valid
        valid = check_cross_references(instance_ids) and valid

    if valid:
        print("PASS   Specification validation completed successfully.")
        return 0
    print("FAIL   Specification validation found errors.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
