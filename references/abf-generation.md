# Auxiliary basis functions for LRI

## Role and separation

The ABF expands products of physical NAOs in the localized resolution-of-identity
(LRI) approximation. ABFs are not physical orbitals and do not replace the
`.orb` file. Generate them from the same physical NAO and PP used by the final
ABACUS producer.

ABACUS workflows can construct product ABFs internally or consume explicit
auxiliary orbital files through `ABFS_ORBITAL`. These are distinct workflows:
an internal PCA setting does not by itself prove that a reusable `.abfs` file
was exported. First decide whether the pinned producer expects generated files
or constructs the basis at runtime, then follow that version's documented
route. In `STRU`, map one auxiliary file to each species in the same order as
`ATOMIC_SPECIES`; keep `ABFS_ORBITAL` in the consuming calculation, not in an
input whose purpose is to generate those files.

Keep these controls distinct because they act at different stages:

- generator-side product-basis PCA or retained-spectrum threshold;
- Coulomb-metric inversion or eigenvalue cutoff used to form LRI coefficients;
- LibRPA/ABACUS runtime shrink threshold for the production ABF;
- any frequency, q-grid, Coulomb-truncation, or head/wing settings.

The exact keyword names and availability change with the ABACUS branch. Verify
them against the source branch used for the run. Do not copy a threshold from a
different branch and call it a default.

## Generic generation recipe

1. Start from the final PP and physical `.orb` files. Freeze their hashes.
2. Create a clean, one-species generation case when the generator requires it;
   use a minimal k-point input and omit production-only `ABFS_ORBITAL` entries.
   Use the exact PP and physical `.orb` used by the later production case.
3. Choose auxiliary angular channels to cover products. As a starting rule,
   add only channels beyond the physical maximum angular momentum (for example,
   auxiliary `f`/`g` when the physical set stops at `d`), then test alternatives.
   This is a search strategy, not a universal recipe.
4. Record the generator commit, input, radial channels, PCA threshold, Coulomb
   metric settings, retained dimensions, and output hashes.
5. Map the generated ABF files back to the final `STRU` in the exact species
   order. Do not use a generation-only `for_aux` basis as the physical NAO.

### Explicit ABFS export route

The public [ABACUS auxiliary-basis generator fork](https://github.com/AroundPeking/abacus_abf_gen/tree/806cde132cbf98c25809e1a6f51a700ca97ce10c)
contains an explicit export path at commit
`806cde132cbf98c25809e1a6f51a700ca97ce10c`. In that source revision,
`Exx_LRI` constructs the same-atom product basis, writes one `.abfs` file per
species, and then calls `exit(0)`. The normal `rpa 1` route is therefore used
as a one-shot exporter: the zero exit status means the export path returned,
not that an SCF or RPA calculation completed. Do not use this exporter run as
the production LibRPA handoff.

For this route, prepare `INPUT`, `KPT`, and a single-species `STRU` using the
exact PP and auxiliary-only `.orb`; omit `ABFS_ORBITAL` while generating. Use
the pinned branch's documented RPA trigger and set `exx_pca_threshold`
explicitly. Run the compiled ABACUS executable under the site's normal
Linux/HPC policy; LibRPA is not run in this step. The expected product is an
`.abfs` file named from the element/orbital label. Check the log, file count,
header, and SHA-256. If no file is written, stop and verify the executable,
commit, and branch-specific export path; do not treat the exit code alone as
success.

This implementation is old and branch-specific. Pin its immutable commit,
confirm compatibility with the ABACUS inputs and LibRPA reader being used, and
prefer a maintained exporter if one becomes available. Standard ABACUS builds
may construct ABFs internally without exporting reusable `.abfs` files.

An auxiliary-only `for_aux` orbital is a separate input variant for generators
that need extra angular channels to construct products. Keep the production
`.orb` unchanged. One candidate hierarchy for a physical basis ending at `d`
is `d -> d+f -> d+f+g`; for a basis ending at `f`, test `f+g`. These are
candidate ladders, not defaults. Hold PP, physical NAO, radial rules, generator
version, and PCA settings fixed while comparing the angular candidates. The
`for_aux` file must never be placed in the production `NUMERICAL_ORBITAL`
section.

## Version-specific ABACUS controls

Check the source and documentation for the pinned ABACUS branch before setting
these controls. They act at different stages:

| Control | Meaning to verify | Not equivalent to |
| --- | --- | --- |
| `exx_pca_threshold` | Product-basis/PCA reduction in the selected LRI route; determine whether it changes an exported file or a runtime basis | Coulomb inversion or LibRPA shrink |
| `exx_cs_inv_thr` | Local Coulomb-metric inversion/eigenvalue handling in versions that provide it | Generator PCA threshold |
| `shrink_abfs_pca_thr` | Runtime auxiliary-basis shrink where supported | The original unshrunk ABF file |
| `calculation = gen_opt_abfs` and `exx_opt_orb_*` | The separate optimized-ABF mode documented by some ABACUS versions | A promise that `ABFS_ORBITAL` files were exported |

Keyword names, defaults, build requirements, and output behavior can change.
Record the exact version and effective value; do not promote a documented
example value into a general recommendation.

`templates/INPUT.abf-generation.example`, `templates/STRU.abf-generation.example`,
and `templates/KPT.gamma.example` are a schematic starting point for a
single-species generation case. `templates/STRU.abfs.example` shows the
consuming `ABFS_ORBITAL` mapping. Generation and consumption may need different
`STRU` sections; keep the two manifests separate when the selected branch
requires that distinction. The angle-bracket fields are placeholders and must
be replaced before running ABACUS.

## Acceptance before GW

An ABF candidate must pass the producer/material gate, not just a file parser:

- finite retained Coulomb spectrum with documented rank and conditioning;
- finite, bounded coefficients in the full and any shrunk basis;
- RI fitting residual or an equivalent product-space error measure;
- a same-producer EXX or RPA positive control with stable energy and band
  ordering;
- material full-q checks (and the analytic head/wing contract when applicable).

PCA stability can be non-monotonic. If a threshold gives pathological
coefficients or exchange energy, compare neighboring retained subsets and a
hash-frozen positive control, then reject the candidate before PyATB, NSCF, EXX,
or GW. A finite file and a successful job exit do not pass this gate.

## Public reporting

Report unshrunk and shrunk dimensions separately. Include the exact `Cs`/Coulomb
metric provenance, q-grid and head/wing convention, residual definition, and
the reason for any removed channel. Never hide an unstable candidate by
silently clipping coefficients or reordering bands.

## Optional smooth high-angular-momentum helper

When an auxiliary-only `f/g` candidate is needed, the repository includes
`scripts/generate_gaussian_aux_orb.py`. It reads a public ABACUS `.orb`, locates
the outermost-zeta peak of the highest existing channel, appends a normalized
smooth Gaussian `f` and/or `g` channel, and prints the chosen radii and
exponents as JSON. The `single` mode is the constrained one-primitive starting
point; `extend` adds a broader same-sign primitive. This is a candidate
construction tool, not a proof that the resulting ABF is converged.

For a physical basis ending at `d`, generate and test the hierarchy in two
steps so the `f` and `g` contributions can be distinguished:

```bash
python scripts/generate_gaussian_aux_orb.py --input X_d.orb --output X_df_for_aux.orb --add-channels f
python scripts/generate_gaussian_aux_orb.py --input X_df_for_aux.orb --output X_dfg_for_aux.orb --add-channels g
```

For a physical basis that already ends at `f`, add only `g`:

```bash
python scripts/generate_gaussian_aux_orb.py --input X_f.orb --output X_fg_for_aux.orb --add-channels g
```

For a single Gaussian primitive, the radial channel is
`R_l(r) = r^l exp(-alpha*r^2)` with peak at
`r_peak = sqrt(l/(2*alpha))`. The helper starts with `r_f = 1.10*r_ref` and
`r_g = 1.25*r_f`, where `r_ref` is the peak radius of the highest existing
channel. It multiplies the radial function by a quintic smooth cutoff from
`0.85*Rcut` to `Rcut`, then normalizes it. These scale factors and the cutoff
window are candidate parameters; change them only in a controlled comparison.
The optional `extend` mode adds a broader same-sign primitive with one-quarter
the main exponent and configurable weight.

Use it only on a copy of the physical `.orb`, keep the output labelled
`for_aux`, and run the full producer/material acceptance gates above. The
algorithm is intentionally generic: verify the `.orb` header format, radial
mesh, cutoff, normalization convention, and ABACUS version before using it.
