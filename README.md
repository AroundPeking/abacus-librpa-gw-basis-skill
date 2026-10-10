# ABACUS + LibRPA GW basis skill

This public skill explains how to obtain or generate a matched
pseudopotential, physical numerical atomic orbital, and localized auxiliary
basis for ABACUS + LibRPA GW calculations. It separates file checks from
physical gates and keeps provenance explicit.

The repository contains no private calculation directories, host settings,
scheduler jobs, or third-party binary assets. Download PP/NAO/ABF files from
their publisher, check the license, and record the source URL plus SHA-256 in
the manifest.

## Use

Copy the whole repository into the skill directory of the target agent, or pass
the repository URL to an agent that supports public skills. At minimum keep
`SKILL.md`, `references/`, `templates/`, and `scripts/`. Fill
`templates/basis-manifest.example.json` for each case and run the portable
checks:

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
`references/public-assets.md`.

For published 2D and 3D ABACUS + LibRPA cases, including downloadable PP,
NAO, ABF, inputs, and GW outputs where present, see
[`references/tested-public-bundles.md`](references/tested-public-bundles.md).
The linked data repository provides its own `MANIFEST.tsv` with SHA-256 hashes;
this skill links to the data instead of duplicating its files.

## License

The documentation, templates, and scripts in this repository are released
under the MIT License; third-party software and data keep their own licenses.
