# Validation gates

Use the following order. Record `pass`, `fail`, or `pending` with evidence and
the exact input/output hash. Do not collapse all of them into “the job passed.”

## Gate 0: provenance

- PP, physical `.orb`, and `.abfs` files exist and have recorded SHA-256 hashes.
- Species order, XC, SOC/relativity, generator commits, and ABACUS/LibRPA commits
  are explicit.
- The source and license permit the planned redistribution or download.

## Gate 1: file and radial checks

- UPF header is readable and agrees with the intended valence, NLCC, and
  relativistic mode.
- Orbital and ABF headers, radial grids, endpoints, normalization, and shell
  counts are finite and internally consistent.

This gate only proves file integrity. It does not establish a usable basis.

## Gate 2: physical PBE and overlap

- Same-PP PW and LCAO calculations use the same structure, XC, spin/SOC, and
  target k mesh.
- Occupations converge; no false plateau or unexpected band reordering appears
  at the target window.
- The NAO overlap spectrum is finite and sufficiently conditioned for the
  intended solver and product space.

Stop before ABF/GW if the physical PBE gate fails.

## Gate 3: RI and Coulomb metric

- Product-space rank and condition numbers are finite and documented.
- RI residuals are measured with a stated norm and q/grid sampling.
- Full and shrunk Coulomb matrices are Hermitian/finite; positive-semidefinite
  behavior is checked in the representation where it is expected.
- For strict-2D or other special Coulomb conventions, head, wings, body, and
  normalization are tested under that exact contract.

## Gate 4: EXX/RPA producer control

- A same-producer positive control gives finite exchange/RPA output.
- Raw band indices and occupation boundaries are retained; do not globally sort
  across occupied and empty manifolds to hide a kink.
- Results are stable under the documented q-grid, ABF subset, and shrink control.

## Gate 5: GW readiness

- The complete producer handoff is present and reader-compatible.
- Empty-state count and frequency/q settings cover the declared observable.
- A controlled convergence comparison exists for the reported quantity.

When a gate is not run, label it `pending`; do not infer it from another gate.
