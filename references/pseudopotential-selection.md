# Pseudopotential selection for GW

## Scope and invariants

ABACUS LCAO calculations need both a norm-conserving pseudopotential and
numerical atomic orbitals. The orbitals are generated for a specific PP; a
visually similar filename or the same element does not make two files
interchangeable. Freeze the PP before generating or selecting the NAO and ABF.
Within each candidate bundle, use the same pseudopotential throughout the
matched PP/NAO/ABF producer chain. When comparing two PP families, use a
separately matched NAO and ABF bundle for each PP; hold the generation recipe
and test protocol fixed where possible, not the PP-dependent files.

## Obtaining versus generating a PP

Routine material work should select a released, tested PP from its publisher,
not create a new PP during the material calculation. A new PP is an element-
level project: preserve generator inputs and reference configurations, test
scattering properties and ghost states, and compare against trusted all-electron
or established PP references before using it for GW. This skill does not define
a universal PP-generation recipe. Record the published release and file hash
even when the PP comes from a well-known library.

For each element, record:

| Field | What to preserve |
| --- | --- |
| Source | Publisher URL, library name, release or commit |
| Identity | Exact filename and SHA-256 |
| Functional | PBE, PBEsol, or other XC used to generate and compare it |
| Core/valence | Valence count, semicore states, NLCC, reference configuration |
| Relativity | Scalar or full relativistic; SOC flag in the UPF header |
| Projectors | Angular channels and number of projectors |
| Evidence | Published tests and the user's target-system controls |

## How to choose a family

GTH, SG15/ONCV, PseudoDojo/Dojo-NC, and other norm-conserving families are
candidate families, not a universal ranking. There is no universal best PP.
Choose the candidate that has the
needed elements, relativistic mode, and tested transferability at a tolerable
cost. Include semicore states when the target states or response involve those
shells; extra valence states increase cost and can alter the reference, so they
must be compared deliberately.

For SOC, inspect the PP header and the ABACUS documentation for the selected
version. An SOC calculation requires a compatible fully relativistic PP and
the corresponding SOC support in the code. A non-SOC run may use a scalar-
relativistic file or a fully relativistic file only when the code documents the
conversion. Do not silently mix scalar and full-relativistic results.

## Minimal comparison protocol

When more than one PP is plausible, hold structure, XC, spin/SOC, k/q meshes,
generation protocol, ABF construction recipe, and executable commits fixed as
far as possible. Use a separately matched physical NAO and ABF for each PP.
Compare in this order:

1. **PP self-consistency:** read the header, valence configuration, projectors,
   and reference energies; check that the file is the intended format.
2. **Same-PP plane-wave control:** converge a PW PBE calculation for the same
   structure and compare the target bands, occupations, forces, or response
   quantity. This separates a PP error from an NAO error.
3. **Matched LCAO control:** use a NAO generated for that exact PP. Compare the
   physical PBE quantity and the first unoccupied states in the window needed by
   GW. A small total-energy difference alone is insufficient.
4. **Independent reference when required:** compare to an all-electron or
   trusted external reference with aligned XC, structure, SOC, and observable.
5. **Response controls:** for GW/RPA, repeat the comparison with the same
   auxiliary-basis and Coulomb settings. A PP that matches occupied PBE bands
   can still fail in high empty states or finite-q response.

Do not turn historical percentage thresholds into universal acceptance criteria.
Choose tolerances from the target observable and document them in the manifest.

## Public asset rules

Download from the publisher or a project-maintained public release. Preserve the
original file and its checksum; do not normalize XML, rename it, or edit its
header before hashing. If a database mirrors a file, record both the mirror URL
and the publisher identity. See [public-assets.md](public-assets.md).
