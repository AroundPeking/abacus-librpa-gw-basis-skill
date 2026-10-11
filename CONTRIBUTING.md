# Contributing a PP/NAO/ABF or GW result

Contributions are welcome for both dimensions. Keep 2D and 3D records in their
separate directories and preserve the files needed to reproduce the stated
observable.

## Before adding files

Confirm that the PP, NAO, and ABF may be redistributed. Check the upstream
license and retain its source URL in the set record. Do not add private paths,
hostnames, scheduler output, credentials, or binaries whose redistribution is
not authorized. If a text log contains such information, redact it and record
the transformation and both hashes.

## Add an element set

1. Put the byte-preserved payloads in `data/elements/<Element>/` under its
   `pseudopotentials/`,
   `orbitals/`, `for_aux/`, or `auxiliary/` directory. Use the SHA-256 as the
   filename stem.
2. Create `sets/<set-id>/set.json` with the exact roles, hashes, dimensions,
   generator inputs, validation scope, and source license information.
   Record the lowercase `sha256` of every committed payload.
3. Use a new set ID for every changed payload or changed PP/NAO/ABF binding.
   Never edit an old set to point at a new file.

## Add a calculation

Create `data/calculations/2d/<material>/<case-id>/` or
`data/calculations/3d/<material>/<case-id>/`. Add portable `inputs`, `results`,
`logs`, and `figures` files as available. In `record.json`, bind exact set IDs
only when the source audit proves the production association. Otherwise leave
`species` empty and explain the missing linkage in `missing`.

If a set is useful for follow-up testing but its exact production binding is
not proven, add it under `basis_candidates` with an explicit scope instead of
putting it in `species`.

Use `gw_validated` only for the exact target observable and protocol whose
physical gates are documented. Keep completed but incomplete or anomalous runs
as `gw_diagnostic`, `path_diagnostic`, or `failed`; do not delete them to make a
table look cleaner.

## Local checks

```bash
python3 scripts/library.py --write-catalog
python3 scripts/public_scan.py .
python3 tests/test_library.py
python3 tests/test_public_skill.py
git diff --check
```

These checks are a static public scan and do not compile ABACUS or LibRPA. A reviewer should
also inspect the exact PP/NAO/ABF association, the producer and LibRPA commit
identity, and the physical gate evidence before calling a result validated.
