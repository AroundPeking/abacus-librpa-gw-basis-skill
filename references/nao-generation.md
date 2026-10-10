# Physical numerical atomic orbitals

## What is being generated

The physical NAO expands the one-particle KS states in ABACUS LCAO. It is
different from an auxiliary basis used to fit products of two NAOs. It must be
generated for the exact PP and target XC; an ABF generator cannot repair an
incompatible physical NAO.

ABACUS orbital blocks are organized by species and atom, then angular momentum,
zeta, and magnetic component. Count functions with the angular degeneracy
$2l+1$: `s=1`, `p=3`, `d=5`, `f=7`, and so on. Include spin doubling only when
the ABACUS/LibRPA contract actually stores spinor components.

## Generation inputs

For SIAB, ABACUS ORBGEN, or another public generator, preserve:

- exact PP file and SHA-256;
- generator URL, commit/release, executable or script version, backend, and
  random seed where applicable;
- element reference configuration and shell ladder;
- radial cutoff, smoothing, confinement, grid, and optimization controls;
- training geometries (atom, dimer, crystal, or other target environments),
  k-point/occupation window, state weights, and empty-state policy;
- spillage history, final coefficients, actual output shell counts, and the hash
  of the generated `.orb` file.

`auto` weights derived from occupations are different from uniform weights; a
`fix` mode that freezes imported coefficients is different from an optimization.
Keep electronic broadening parameters distinct from radial smoothing parameters.

## Practical generation sequence

1. Freeze the PP and its valence/reference configuration. Search the public
   ABACUS orbital library for an exact matched file before starting a new
   optimization.
2. Define the target state window and an initial shell ladder. Include radial
   flexibility for semicore shells when they are in the PP valence, but do not
   multiply every shell by the same number of zeta functions solely because the
   electron count increased.
3. Prepare reference plane-wave calculations for the isolated atom and a small
   set of representative bonded environments. Include enough bands to cover
   the intended occupied and empty-state window. Save structures, occupations,
   spin, k points, PP hash, and converged inputs/outputs.
4. Configure the optimizer using the syntax of the SIAB or ORBGEN release in
   use. Record each effective level input, seed, restart/frozen coefficients,
   nonzero state weights, stopping condition, and the full spillage history.
   Do not assume that all calculated empty bands enter an occupation-derived
   objective with equal weight.
5. Export the `.orb`, hash it, inspect the actual shell counts and radial
   functions, then run the same-PP plane-wave versus LCAO PBE control before
   building an ABF from it.

The exact optimizer input schema changes across releases. Treat a GUI label,
top-level recipe name, or archived metadata summary as insufficient evidence
of the effective settings; retain the inputs actually read by each optimizer
level.

The public ABACUS-orbitals repository supplies a runnable SIAB example and
stores the corresponding `INPUT` and `ORBITAL_RESULTS.txt` beside released
`.orb` files. `templates/SIAB_INPUT.example` is a sanitized schematic of that
interface. Replace placeholders with public paths and run the SIAB command
documented by the pinned release; do not copy a scheduler or module setup from
another site.

For the repository's example layout, the documented invocation is:

```bash
cd ABACUS-orbitals/SIAB/example_Si
python3 ../SIAB.py SIAB_INPUT
```

Use the pinned public repository commit and its stated dependencies. The
example's Si geometry, numerical settings, and shell ladder are not defaults
for another element or material.

## Selection ladder

Start with a public matched set such as a documented DZP/TZDP family. Increase
zeta, angular channels, or cutoffs only when a controlled PBE/response test
identifies the missing subspace. More functions can worsen overlap conditioning
or expose high-state artifacts; size alone is not an accuracy certificate.

For each candidate:

1. Check radial endpoints, normalization, continuity, and finite overlap norms.
2. Run the same-PP (same pseudopotential) PW versus LCAO PBE control on the
   target structure. In this document, “same PP” means the exact same file and
   hash, not merely the same family label.
3. Inspect the occupied-to-empty window needed by GW, including ordering at
   high-symmetry points and the first unoccupied bands.
4. Check the overlap spectrum and condition number on the production k mesh.
5. Only after the physical NAO passes, generate or select its ABF and continue
   to RI/EXX/GW tests.

The spillage objective measures representation of the chosen training states. It
does not certify empty-state completeness, RI completeness, or GW convergence.

## Reuse versus regeneration

Reuse a public `.orb` when its PP, generator provenance, species ordering, and
hash are known and its physical controls pass. A changed PP, SOC mode, XC, or
target window requires a new compatibility check; regenerate only when the
matched file is absent or a controlled test shows it is inadequate. A generator
version change alone does not invalidate a previously validated file. Do not
regenerate only to make filenames or cutoff labels look consistent.
