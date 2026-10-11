# Contributing a PP/NAO/ABF or GW result

Contributions are welcome for both dimensions. Add data to the separate
[ABACUS + LibRPA GW database](https://github.com/AroundPeking/abacus-librpa-gw-database),
keeping 2D and 3D records in their separate directories and preserving the
files needed to reproduce the stated observable.

## Before adding files

Confirm that the PP, NAO, and ABF may be redistributed. Check the upstream
license and retain its source URL in the set record. Do not add private paths,
hostnames, scheduler output, credentials, or binaries whose redistribution is
not authorized. If a text log contains such information, redact it and record
the transformation and both hashes.

The database repository's `CONTRIBUTING.md` contains the element-set and
calculation-record steps, including `basis_candidates`, `sha256`, and status
meanings.

## Local checks

```bash
python3 scripts/public_scan.py .
python3 tests/test_public_skill.py
python3 tests/test_gaussian_aux_orb.py
git diff --check
```

These checks are a static public scan and do not compile ABACUS or LibRPA. A reviewer should
also inspect the exact PP/NAO/ABF association, the producer and LibRPA commit
identity, and the physical gate evidence before calling a result validated.
