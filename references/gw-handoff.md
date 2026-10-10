# ABACUS to LibRPA GW handoff

## Bundle contents

Keep these artifacts in one case manifest or an immutable archive:

- `INPUT`, `KPT`, and `STRU` with the species order used for every file;
- exact `.upf`, physical `.orb`, and `.abfs` files;
- ABACUS SCF/NSCF/preprocess outputs and the producer commit;
- response, Coulomb, LRI, shrink, eigenvector, and band metadata files required
  by the selected LibRPA reader contract;
- `librpa.in`, frequency-grid file, q-grid description, and final KS/EXX/GW data;
- validation report with hashes and gate status.

Do not substitute a Coulomb or eigenvector file from a different PP, NAO, ABF,
species order, k/q mesh, or producer commit. A reader parser can accept such a
file while the physics is inconsistent.

For ABACUS versions that support `ABFS_ORBITAL`, list one auxiliary filename
per species, in the same order as `ATOMIC_SPECIES`:

```text
ATOMIC_SPECIES
X 1.0 X.upf

NUMERICAL_ORBITAL
X.orb

ABFS_ORBITAL
X.abfs
```

The suffix is a naming convention; the consuming code reads the path. Confirm
the section and its runtime requirements in the pinned version's source or
documentation. For multiple elements, preserve the species order in all three
sections.

## Periodic route

The usual periodic chain is:

`SCF -> optional full-grid response preparation -> NSCF/preprocess -> LibRPA`.

The optional stage may be PyATB or another documented producer, but it must use
the same physical NAO and ABF contract. A molecular or gamma-only case can use a
shorter route only when its reader contract explicitly supports it.

## `nbands` and dimensions

Compute the complete AO dimension from the actual shell list and angular
degeneracies, not from a filename such as `TZDP`. For a full-basis control, the
KS state count should be checked against that dimension. A reduced-state GW test
must state exactly which states were removed and retain a complete producer
handoff; it is not automatically equivalent to the full-basis calculation.

Include enough empty states for the declared self-energy/frequency window and
converge that window independently. Record spin/SOC factors explicitly rather
than applying a blanket factor of two.

## Reader/version contract

LibRPA interfaces are under active development. Pin the LibRPA source URL and
commit, identify the reader contract (for example, a versioned file-based
contract), and run the matching static input checks. If a keyword or filename is
branch-specific, link the branch documentation in the manifest rather than
silently translating it.
