# ABACUS + LibRPA GW basis skill

## [打开网页版 / Open web database](https://aroundpeking.github.io/abacus-librpa-gw-database/database/)

Browse the live materials and basis catalog, including archived input previews
and downloads. No installation or GitHub sign-in is needed to use the website.
The source repository and this agent skill remain separate from the web UI.

This public skill explains how to obtain or generate a matched
pseudopotential (PP), physical numerical atomic orbital (NAO), and localized
auxiliary basis (ABF) for ABACUS + LibRPA RPA/GW calculations. The actual
hash-addressed PP/NAO/ABF files and calculation evidence live in the separate
[ABACUS + LibRPA GW database](https://github.com/AroundPeking/abacus-librpa-gw-database).
The database is split into `2d` and `3d` so that a two-dimensional Coulomb and
band-path result is not silently treated as a bulk benchmark.

Scientific status is deliberately conservative: a file-integrity pass, an
atomic radial check, a PBE check, a completed producer run, and a physical GW
acceptance are different statuses. Every copied data file records its hashes
and any redaction or other transformation in the database repository.

## Use

Copy this repository into the skill directory of the target agent, or pass the
repository URL to an agent that supports public skills. Browse the companion
database repository for actual assets, hashes, inputs, logs, figures, and
results. Its `database/data.json` is machine-readable and its `database/`
directory is a static searchable catalog. Open a calculation's **Input files**
section to preview or download its archived inputs, and **Pseudopotentials &
basis** to inspect the exact asset bindings. An **Inputs not archived** message
means those inputs are absent; candidate assets do not fill that gap.

The database preserves hash-addressed files while showing readable names.
Recorded filenames and calculation aliases are used when supported by the
metadata; a descriptive alias is explicitly labelled when the original name
is unknown. Always compare the full SHA-256 and calculation-specific names
before reuse. Archive downloads are separate from the validated direct-use
mirror described below.

To add a new element set or calculation, follow the contribution protocol in
the database repository and use a new immutable set ID when any payload
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

The direct-use mirror is governed by `data/release-manifest.json` and is
checked against a pinned database checkout with:

```bash
python scripts/validate_database_release.py --database-root ../abacus-librpa-gw-database
```

The first release intentionally contains no mirrored payloads: the imported
historical records are searchable in the database, but none yet has the full
public input/output and code-commit evidence required for direct distribution.
When a database set becomes `publishable`, copy its PP, physical NAO, optional
`for_aux` orbital, and ABF into `data/payloads/<set-id>/` and add reciprocal
hash entries to the manifest.

Native ABACUS/LibRPA builds and scientific runs belong on the user's approved
Linux/HPC environment. The included checks are static and dependency-free.
The scripts require Python 3.8 or newer and use only the standard library.

## Public sources

- ABACUS: https://github.com/abacusmodeling/abacus-develop
- ABACUS orbitals: https://github.com/abacusmodeling/ABACUS-orbitals
- LibRPA: https://github.com/AESM-Group/LibRPA
- PseudoDojo: https://www.pseudo-dojo.org/
- SG15/ONCV: http://www.quantum-simulation.org/potentials/sg15_oncv/
- [Separate basis and calculation database](https://github.com/AroundPeking/abacus-librpa-gw-database)

The detailed source and licensing notes are in
`references/public-assets.md`. The database's current inventory and its
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
under the MIT License. Third-party software and scientific data in the
companion database keep their own licenses and reuse conditions.
