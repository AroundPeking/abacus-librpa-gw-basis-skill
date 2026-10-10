#!/usr/bin/env python3
"""Validate a public ABACUS + LibRPA basis manifest using stdlib only."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")
PLACEHOLDER = "CHANGE_ME"


def fail(message: str) -> None:
    raise ValueError(message)


def check_url(value: object, label: str, allow_placeholders: bool) -> None:
    if allow_placeholders and value == "https://example.org/structure":
        return
    if not isinstance(value, str) or urlparse(value).scheme not in {"http", "https"}:
        fail(f"{label}: expected an http(s) URL")


def check_text(value: object, label: str, allow_placeholders: bool) -> None:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label}: expected a non-empty string")
    if not allow_placeholders and (value == PLACEHOLDER or "replace-with-" in value):
        fail(f"{label}: placeholder remains")


def check_filename(value: object, label: str, allow_placeholders: bool) -> None:
    check_text(value, label, allow_placeholders)
    if not isinstance(value, str):
        return
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        fail(f"{label}: expected a portable filename, not an absolute or parent path")


def check_hash(value: object, label: str, allow_placeholders: bool) -> None:
    if allow_placeholders and value == PLACEHOLDER:
        return
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        fail(f"{label}: expected a 64-character SHA-256")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--allow-placeholders", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))

    for key in ("schema_version", "case_id", "target", "software", "species", "validation"):
        if key not in data:
            fail(f"missing top-level key: {key}")
    check_text(data["case_id"], "case_id", args.allow_placeholders)
    target = data["target"]
    check_text(target["observable"], "target.observable", args.allow_placeholders)
    check_text(target["xc"], "target.xc", args.allow_placeholders)
    check_url(target["structure_source_url"], "target.structure_source_url", args.allow_placeholders)
    check_hash(target["structure_sha256"], "target.structure_sha256", args.allow_placeholders)

    for name in ("abacus", "librpa"):
        item = data["software"].get(name)
        if not isinstance(item, dict):
            fail(f"software.{name}: expected object")
        check_url(item.get("source_url"), f"software.{name}.source_url", args.allow_placeholders)
        check_text(item.get("commit"), f"software.{name}.commit", args.allow_placeholders)

    if not isinstance(data["species"], list) or not data["species"]:
        fail("species: expected a non-empty list")
    for index, species in enumerate(data["species"]):
        prefix = f"species[{index}]"
        check_text(species.get("element"), f"{prefix}.element", args.allow_placeholders)
        for section in ("pseudopotential", "physical_nao", "auxiliary_abf"):
            item = species.get(section)
            if not isinstance(item, dict):
                fail(f"{prefix}.{section}: expected object")
            check_url(item.get("source_url"), f"{prefix}.{section}.source_url", args.allow_placeholders)
            # ABACUS consumes the configured path; the suffix is a naming
            # convention, not a file-format guarantee.
            check_filename(item.get("filename"), f"{prefix}.{section}.filename", args.allow_placeholders)
            check_hash(item.get("sha256"), f"{prefix}.{section}.sha256", args.allow_placeholders)
        check_text(species["pseudopotential"].get("relativistic"), f"{prefix}.pseudopotential.relativistic", args.allow_placeholders)
        if species["auxiliary_abf"].get("for_aux_only") is not True:
            fail(f"{prefix}.auxiliary_abf.for_aux_only: must be true")

    if not isinstance(data["validation"], dict):
        fail("validation: expected object")
    allowed = {"pass", "fail", "pending", "not_run"}
    for key, value in data["validation"].items():
        if key != "evidence_urls_or_paths" and value not in allowed:
            fail(f"validation.{key}: expected one of {sorted(allowed)}")
    print(f"manifest OK: {args.manifest}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"manifest ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
