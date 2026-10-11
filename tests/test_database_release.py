"""Tests for the database-to-skill release contract."""

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/validate_database_release.py"


class DatabaseReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("release", SCRIPT)
        cls.release = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.release)

    def test_empty_release_is_valid_when_database_has_no_publishable_sets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data").mkdir()
            (root / "data/release-index.json").write_text(
                json.dumps({"schema_version": 1, "sets": []}), encoding="utf-8"
            )
            manifest = {"schema_version": 1, "database_commit": "a" * 40, "sets": []}
            self.assertEqual(self.release.validate_release(root, manifest, root), [])

    def test_mirror_requires_publishable_database_set_and_matching_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data/elements/Si/sets/Si-x").mkdir(parents=True)
            payload = b"basis\n"
            payload_path = root / "data/elements/Si/orbitals/test.orb"
            payload_path.parent.mkdir(parents=True)
            payload_path.write_bytes(payload)
            digest = hashlib.sha256(payload).hexdigest()
            set_record = {
                "id": "Si-x", "element": "Si",
                "publication": {"status": "publishable", "calculation_ids": ["si-1"]},
                "files": [{"role": "nao", "path": "data/elements/Si/orbitals/test.orb", "sha256": digest}],
            }
            (root / "data/elements/Si/sets/Si-x/set.json").write_text(json.dumps(set_record), encoding="utf-8")
            (root / "data/release-index.json").write_text(json.dumps({"schema_version": 1, "sets": [{
                "set_id": "Si-x", "element": "Si", "calculation_ids": ["si-1"],
                "files": [{"role": "nao", "path": payload_path.relative_to(root).as_posix(), "sha256": digest}]
            }]}), encoding="utf-8")
            manifest = {"schema_version": 1, "database_commit": "a" * 40, "sets": [{
                "set_id": "Si-x", "calculation_ids": ["si-1"],
                "files": [{"role": "nao", "database_path": payload_path.relative_to(root).as_posix(),
                           "path": "payloads/Si-x/test.orb", "sha256": digest}]
            }]}
            (root / "payloads/Si-x").mkdir(parents=True)
            (root / "payloads/Si-x/test.orb").write_bytes(payload)
            self.assertEqual(self.release.validate_release(root, manifest, root), [])
            (root / "payloads/Si-x/test.orb").write_bytes(b"changed\n")
            with self.assertRaisesRegex(ValueError, "SHA-256"):
                self.release.validate_release(root, manifest, root)


if __name__ == "__main__":
    unittest.main()
