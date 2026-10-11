# ABACUS + LibRPA GW basis skill

This public skill explains how to obtain or generate a matched
pseudopotential (PP), physical numerical atomic orbital (NAO), and localized
auxiliary basis (ABF) for ABACUS + LibRPA RPA/GW calculations. It also ships a
curated, hash-addressed library of the public PP/NAO/ABF files and calculation
evidence that have already been collected. The data are split into `2d` and
`3d` so that a two-dimensional Coulomb and band-path result is not silently
treated as a bulk benchmark.

Binary payloads are included only when their source license or project policy
allows redistribution. Every copied file records its original SHA-256, its
published SHA-256, and any redaction or other transformation in the adjacent
JSON record. Scientific status is deliberately conservative: a file-integrity
pass, an atomic radial check, a PBE check, a completed producer run, and a
physical GW acceptance are different statuses.

## Use

Copy the whole repository into the skill directory of the target agent, or pass
the repository URL to an agent that supports public skills. The searchable
catalog is available from `database/index.html` after the repository is served
as a static site. The same records are plain JSON, so the database can also be
queried without a browser.

The checked-in payloads live under `data/elements/<Element>/`; calculation
inputs, logs, figures, and results live under `data/calculations/2d/` or
`data/calculations/3d/`. The repository therefore remains usable when an
upstream case or download link changes.

To add a new element set, put the PP, physical NAO, optional `for_aux` orbital,
and ABF under that element's directory, add one `sets/<set-id>/set.json`, then
add the calculation record under either `data/calculations/2d/<material>/` or
`data/calculations/3d/<material>/`. Use a new immutable set ID when any payload
changes. The complete field definitions and review rules are in
[`references/database.md`](references/database.md) and
[`CONTRIBUTING.md`](CONTRIBUTING.md).

For a standalone manifest, fill
`templates/basis-manifest.example.json` and run the portable checks:

```bash
python scripts/validate_manifest.py templates/basis-manifest.example.json --allow-placeholders
python scripts/public_scan.py .
```

Repository maintainers should keep `tests/` and also run:

```bash
python tests/test_public_skill.py
python tests/test_gaussian_aux_orb.py
```

To record hashes of downloaded files, run
`python scripts/sha256_files.py file1.upf file2.orb file3.abfs`.

Native ABACUS/LibRPA builds and scientific runs belong on the user's approved
Linux/HPC environment. The included checks are static and dependency-free.
The scripts require Python 3.8 or newer and use only the standard library.
The manifest validator checks schema, URLs, portable filenames, and hash
format; it does not download files or verify a digest against a local file.
Use an independent SHA-256 tool on each downloaded asset and copy the resulting
digest into the manifest.

## Public sources

- ABACUS: https://github.com/abacusmodeling/abacus-develop
- ABACUS orbitals: https://github.com/abacusmodeling/ABACUS-orbitals
- LibRPA: https://github.com/AESM-Group/LibRPA
- PseudoDojo: https://www.pseudo-dojo.org/
- SG15/ONCV: http://www.quantum-simulation.org/potentials/sg15_oncv/

The detailed source and licensing notes are in
`references/public-assets.md`. The repository's current inventory and its
limitations are summarized in:

- [`references/tested-public-bundles-2d.md`](references/tested-public-bundles-2d.md)
- [`references/tested-public-bundles-3d.md`](references/tested-public-bundles-3d.md)
- [`references/database.md`](references/database.md)

The historical records are not a claim that one PP/NAO/ABF is universally best.
Use the narrow `validation_scope`, `status`, and `missing` fields before copying
a set into a new material. When a new basis improves a controlled comparison,
add it as a new set and update the affected calculation record rather than
overwriting the old evidence.

## License

The documentation, templates, and scripts in this repository are released
under the MIT License; third-party software and data keep their own licenses.
