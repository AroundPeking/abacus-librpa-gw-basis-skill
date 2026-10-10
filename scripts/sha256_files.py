#!/usr/bin/env python3
"""Print SHA-256 digests for downloaded pseudopotential and basis files."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Dict, Union


def digest(path: Path) -> Dict[str, Union[str, int]]:
    hasher = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            hasher.update(chunk)
            size += len(chunk)
    return {"file": path.name, "sha256": hasher.hexdigest(), "size_bytes": size}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps([digest(path) for path in args.files], indent=2))
    except OSError as exc:
        print(f"hash ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
