---
name: abacus-librpa-gw-basis
description: Use when preparing or auditing ABACUS plus LibRPA GW inputs whose pseudopotential, numerical atomic orbital, auxiliary basis, provenance, or basis-size choices affect the result.
---

# ABACUS + LibRPA GW basis and pseudopotential

This skill covers the reproducible chain from the physical numerical atomic
orbital to the auxiliary basis used by the GW response:

`pseudopotential -> physical NAO -> ABF -> ABACUS producer -> LibRPA GW`.

It is a decision and audit guide, not a universal parameter table. A file can be
syntactically valid and still be unsuitable for a GW calculation. Keep four
labels separate in every report: `results`, `gates`, `assumptions`, and
`pending`.

The repository contains the current public asset inventory in
`data/elements/` and the calculation database in `data/calculations/`. The two
dimensions are intentionally separate. Each element directory contains only
sets that have an imported payload or an explicit test record; each set keeps
its PP, physical NAO, optional `for_aux` orbital, ABF, evidence files, and
hashes together. Use `database/index.html` or `database/data.json` to search
the records before generating a new set.

## First checks

Before downloading or generating anything, freeze the target protocol:

- system, structure, charge, spin, SOC, relativistic treatment, and XC;
- observable (band gap, quasiparticle shift, self-energy, RPA energy, or another
  quantity), k/q meshes, empty-state window, and convergence target;
- ABACUS and LibRPA source URLs plus immutable commits or releases;
- whether a public matched PP/NAO/ABF bundle already exists.

Search the complete public asset catalog before regenerating a basis. Reuse is
valid only when the producer, species order, XC, relativistic treatment, files,
and SHA-256 hashes match. A filename or family label is not provenance.

## Workflow

1. **Choose and freeze the PP.** Use a norm-conserving PP supported by the
   selected ABACUS route. Record its source, release/commit, SHA-256, XC,
   valence and semicore configuration, NLCC status, relativistic mode, and
   projector channels. Select scalar-relativistic or full-relativistic files
   consistently with SOC. Do not mix PP families in a comparison.
2. **Obtain or generate the physical NAO.** Prefer a public NAO generated for
   the exact PP. If generating with SIAB or another documented generator, keep
   the PP and generator inputs fixed, record the radial cutoffs and angular
   channels, and validate the training set and spillage. The physical NAO is
   the basis for the KS states; it is not an ABF.
3. **Generate or obtain ABFs separately.** ABFs expand products of physical
   NAOs for LRI. Generate them from the same PP and physical NAO, use
   auxiliary-only extra angular channels where justified, and record generator
   version, PCA/conditioning thresholds, retained dimensions, and hashes. Keep
   generation thresholds distinct from LibRPA runtime shrink thresholds.
4. **Run the validation ladder.** Check file headers and hashes, isolated-atom
   radial behavior, periodic PBE/overlap, RI residual and Coulomb conditioning,
   exchange-energy controls, and only then the target GW calculation. Stop when
   an earlier gate fails; a successful parser or scheduler job is not physical
   acceptance.
5. **Build a complete handoff.** Keep `STRU`, exact `.upf`, `.orb`, `.abfs`,
   ABACUS producer outputs, and `librpa.in` in one manifest. For a periodic
   workflow, use the same producer chain for SCF, optional full-grid response
   preparation, NSCF, and LibRPA. Do not replace one producer's Coulomb or
   eigenvector files with another producer's files.
6. **Report evidence.** Use the manifest and validation template in `templates/`.
   State which gates passed, which assumptions were made, and which checks are
   still pending. Preserve anomalous points and raw band indices.
7. **Publish a contribution.** Add immutable element-set and calculation
   records as described in `references/database.md`. Keep the original asset
   hash, the published hash, the exact ABACUS/LibRPA commit when it is known,
   and a short explanation of every redaction. A new result can supersede a
   contextual recommendation only after the same PP, NAO, ABF, producer,
   Coulomb convention, k/q mesh, and observable have been compared.

## References to load as needed

- PP family and comparison criteria: [references/pseudopotential-selection.md](references/pseudopotential-selection.md)
- Physical NAO/SIAB generation: [references/nao-generation.md](references/nao-generation.md)
- ABF generation and LRI conditioning: [references/abf-generation.md](references/abf-generation.md)
- Evidence gates: [references/validation-gates.md](references/validation-gates.md)
- ABACUS-to-LibRPA handoff and `nbands`: [references/gw-handoff.md](references/gw-handoff.md)
- Public downloads and licensing: [references/public-assets.md](references/public-assets.md)
- Published 2D/3D calculation bundles: [references/tested-public-bundles.md](references/tested-public-bundles.md)
- Database layout and contribution protocol: [references/database.md](references/database.md)
- Imported 2D records: [references/tested-public-bundles-2d.md](references/tested-public-bundles-2d.md)
- Imported 3D records: [references/tested-public-bundles-3d.md](references/tested-public-bundles-3d.md)

## Hard stops

- Do not claim a basis is converged from an atom-only or radial check.
- Do not compare GW numbers with different PP/NAO/ABF producers unless the
  comparison is explicitly a provenance study.
- Do not copy private paths, host aliases, scheduler settings, task IDs, or
  unpublished binaries into a public bundle. Public records must use
  repository-relative paths and must say when an exact production asset or
  code commit is missing.
- Do not treat a larger NAO/ABF or a familiar PCA threshold as automatically
  more accurate; inspect conditioning and the target observable.
- Native ABACUS/LibRPA compilation belongs in the approved Linux/HPC environment.
  This skill's local checks are static and do not replace a remote build or run.

## Portable checks

Run these from the skill directory before publishing a manifest or archive:

```bash
python scripts/validate_manifest.py templates/basis-manifest.example.json --allow-placeholders
python scripts/public_scan.py .
python tests/test_public_skill.py
```

The scripts use only the Python standard library and never compile ABACUS or
LibRPA.
