# Design: ABACUS + LibRPA GW basis and pseudopotential skill

## Goal

Provide a portable skill that teaches a new user how to obtain, generate, select,
validate, and hand off pseudopotentials, physical numerical atomic orbitals
(NAOs), and localized auxiliary basis functions (ABFs) for ABACUS + LibRPA GW.
The package must be useful without access to any private workstation, cluster,
calculation directory, or unpublished binary asset.

## Public contract

- Every external asset is referenced by an official public URL, immutable release
  or commit when available, and SHA-256 when a concrete file is used.
- The skill distinguishes a file-format check from a physical acceptance gate.
- It keeps pseudopotential, physical NAO, and ABF provenance linked by species,
  version, hash, exchange-correlation functional, and relativistic treatment.
- It separates results, gates, assumptions, and pending checks.
- It never presents one PP family, orbital size, or PCA threshold as universal.
- It describes remote native execution generically and contains no personal paths,
  host aliases, scheduler partitions, job IDs, or private repository URLs.

## Package shape

- `SKILL.md`: trigger conditions and the short end-to-end procedure.
- `references/`: detailed PP selection, NAO/SIAB generation, ABF generation,
  validation, and GW handoff guidance.
- `templates/`: a hash/provenance manifest and a validation report template.
- `scripts/`: dependency-free manifest, public-content, and hash checks, plus an
  optional Gaussian high-angular-momentum candidate generator for `for_aux`.
- `tests/`: pressure tests that make the publication contract executable.
- `README.md`: public usage, scope, citations, and download links.

## Safety boundaries

The repository ships only those third-party PP/NAO/ABF payloads whose source
terms or project policy permit this redistribution, and records the source,
license note, original hash, published hash, and any text redaction. Other
assets remain links or are marked missing until their reuse terms are clear.
Native ABACUS/LibRPA compilation and large calculations are left to the user's
approved Linux/HPC environment; local static checks do not claim scientific
acceptance.
