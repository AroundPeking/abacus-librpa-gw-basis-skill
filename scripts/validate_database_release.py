#!/usr/bin/env python3
"""Validate mirrored basis payloads against a checked-out database release index."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess


SHA256 = re.compile(r"^[0-9a-f]{64}$")
COMMIT = re.compile(r"^[0-9a-f]{40}$|^[0-9a-f]{64}$")


def _portable(root: Path, value: object, label: str) -> Path:
    if not isinstance(value, str):
        raise ValueError(f"{label}: expected a repository-relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{label}: expected a repository-relative path")
    full = root.joinpath(*path.parts).resolve()
    try:
        full.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"{label}: path escapes repository") from exc
    return full


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_release_index(database_root: Path) -> dict[str, dict]:
    index_path = database_root / "data/release-index.json"
    if not index_path.is_file():
        raise ValueError("database release index is missing; run build_indexes.py --write")
    data = json.loads(index_path.read_text(encoding="utf-8"))
    entries = data.get("sets")
    if not isinstance(entries, list):
        raise ValueError("database release index has no sets list")
    return {entry["set_id"]: entry for entry in entries}


def validate_release(database_root: Path, manifest: dict, mirror_root: Path | None = None) -> list[str]:
    """Return an empty list for a valid mirror, or raise on a contract error."""
    if manifest.get("schema_version") != 1:
        raise ValueError("manifest schema_version must be 1")
    pinned = manifest.get("database_commit")
    if not isinstance(pinned, str) or not COMMIT.fullmatch(pinned):
        raise ValueError("manifest database_commit must be a full commit")
    git_dir = database_root / ".git"
    if git_dir.exists():
        try:
            actual = subprocess.check_output(["git", "-C", str(database_root), "rev-parse", "HEAD"], text=True).strip()
        except (OSError, subprocess.CalledProcessError) as exc:
            raise ValueError("could not resolve the database checkout commit") from exc
        if actual != pinned:
            raise ValueError(f"database checkout is {actual}, manifest pins {pinned}")
    entries = _load_release_index(database_root)
    mirror_root = mirror_root or Path(__file__).resolve().parents[1]
    seen = set()
    for number, item in enumerate(manifest.get("sets", [])):
        label = f"sets[{number}]"
        if not isinstance(item, dict) or not isinstance(item.get("set_id"), str):
            raise ValueError(f"{label}: expected set_id")
        set_id = item["set_id"]
        if set_id in seen:
            raise ValueError(f"{label}: duplicate set_id")
        seen.add(set_id)
        if set_id not in entries:
            raise ValueError(f"{label}: set is not publishable in database")
        database_entry = entries[set_id]
        if sorted(item.get("calculation_ids", [])) != sorted(database_entry.get("calculation_ids", [])):
            raise ValueError(f"{label}: calculation_ids do not match database")
        source_files = {(f.get("role"), f.get("path")): f for f in database_entry.get("files", [])}
        mirror_files = item.get("files")
        if not isinstance(mirror_files, list) or not mirror_files:
            raise ValueError(f"{label}: files must be a non-empty list")
        for file_number, mirror in enumerate(mirror_files):
            file_label = f"{label}.files[{file_number}]"
            key = (mirror.get("role"), mirror.get("database_path", mirror.get("source_path")))
            source = source_files.get(key)
            if source is None:
                # A compact manifest may use the database path directly as path.
                key = (mirror.get("role"), mirror.get("path"))
                source = source_files.get(key)
            if source is None:
                raise ValueError(f"{file_label}: file is not in the database release")
            if mirror.get("sha256") != source.get("sha256"):
                raise ValueError(f"{file_label}: SHA-256 does not match database")
            target = _portable(mirror_root, mirror.get("path"), file_label)
            if not target.is_file():
                raise ValueError(f"{file_label}: mirrored payload is missing")
            if not SHA256.fullmatch(str(mirror.get("sha256", ""))) or _digest(target) != mirror["sha256"]:
                raise ValueError(f"{file_label}: SHA-256 does not match mirrored payload")
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, default=Path("data/release-manifest.json"))
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    validate_release(args.database_root, manifest, Path(__file__).resolve().parents[1])
    print(f"database release OK: {args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
