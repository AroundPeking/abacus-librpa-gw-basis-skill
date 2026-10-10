# Published 2D and 3D calculation bundles

These links point to public ABACUS + LibRPA calculation data that include
matched pseudopotentials, physical numerical orbitals, auxiliary bases, and
completed KS/EXX/GW outputs. Download the upstream repository or individual
case directories and verify file hashes against its
[`MANIFEST.tsv`](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/MANIFEST.tsv).

The bundles are reproducibility records for their stated calculations. Their
presence does not mean every included basis is converged for every observable,
material, mesh, or code version. Read each case's inputs and logs before reuse.

## 2D: MoS2/WS2

The published [MoS2/WS2 case](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/FIG/Fig_10_MoS2_WS2)
contains the producer and band inputs, GTH-PBE pseudopotentials, physical
`.orb` files, exported `.abfs` files, `librpa.in`/`librpa.out`, and final
`KS_band_spin_1.dat`, `EXX_band_spin_1.dat`, and `GW_band_spin_1.dat` files.
The element assets are:

| Element | Physical NAO | Pseudopotential | Exported ABF |
| --- | --- | --- | --- |
| Mo | `4s2p2d1f` | [GTH-PBE Mo](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/FIG/Fig_10_MoS2_WS2/ABACUS_producer_input/assets/Mo-GTH-PBE-q14-cp2k-default-grid.upf) | [foraux, PCA 1e-5, 319 functions](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/FIG/Fig_10_MoS2_WS2/ABACUS_producer_input/assets/Mo_GTH-PBE_foraux_1g_pca1e-5_naux319.abfs) |
| S | `2s2p2d1f` | [GTH-PBE S](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/FIG/Fig_10_MoS2_WS2/ABACUS_producer_input/assets/S-GTH-PBE-q6-cp2k-default-grid.upf) | [foraux, PCA 1e-5, 328 functions](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/FIG/Fig_10_MoS2_WS2/ABACUS_producer_input/assets/S_GTH-PBE_foraux_1g_pca1e-5_naux328.abfs) |
| W | `6s3p3d2f` | [GTH-PBE W](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/FIG/Fig_10_MoS2_WS2/ABACUS_producer_input/assets/W-GTH-PBE-q14-cp2k-default-grid.upf) | [foraux, PCA 1e-5, 584 functions](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/FIG/Fig_10_MoS2_WS2/ABACUS_producer_input/assets/W_GTH-PBE_foraux_1g_pca1e-5_naux584.abfs) |

The matched physical orbitals are [Mo](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/FIG/Fig_10_MoS2_WS2/ABACUS_producer_input/assets/Mo_gga_10au_100Ry_4s2p2d1f.orb), [S](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/FIG/Fig_10_MoS2_WS2/ABACUS_producer_input/assets/S_gga_10au_100Ry_2s2p2d1f.orb), and [W](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/FIG/Fig_10_MoS2_WS2/ABACUS_producer_input/assets/W_gga_10au_100Ry_6s3p3d2f.orb). The GW output files are in the linked `LibRPA_GW` folder.

The labels and dimensions identify the published files; they are not general
defaults for new materials or ABACUS/LibRPA versions.

## 3D: GW comparison cases

The published [Table 04 GW comparison](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison)
contains the following material cases. Each linked folder has the associated
GW result record. PP and physical-NAO files are not co-located in five folders
(AlAs, AlP, BAs, BP, and NaCl); do not treat those folders alone as complete
reusable basis bundles. Check the manifest for the exact files included in each
case and use the complete-asset cases or a verified companion source when
reusing a basis.

| Material | GW case | PP/NAO in this folder |
| --- | --- | --- |
| AlAs | [AlAs__src_paper](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/AlAs__src_paper) | No |
| AlP | [AlP__src_k8_shrink_wing](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/AlP__src_k8_shrink_wing) | No |
| AlSb | [AlSb__src_gw_gth_modspencer](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/AlSb__src_gw_gth_modspencer) | Yes |
| BAs | [BAs__src_k8_shrink_wing](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/BAs__src_k8_shrink_wing) | No |
| BN | [BN__src_sg15](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/BN__src_sg15) | Yes |
| BP | [BP__src_k8_shrink_wing](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/BP__src_k8_shrink_wing) | No |
| C | [C__src_sg15_cs1e-5](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/C__src_sg15_cs1e-5) | Yes |
| CaO | [CaO__src_24freq](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/CaO__src_24freq) | Yes |
| CdS | [CdS__src_debug](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/CdS__src_debug) | Yes |
| GaAs | [GaAs__src_gw_xsoc_1e-10](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/GaAs__src_gw_xsoc_1e-10) | Yes |
| GaN | [GaN__src_pca1e-6](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/GaN__src_pca1e-6) | Yes |
| GaP | [GaP__src_gw_shrink_chi](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/GaP__src_gw_shrink_chi) | Yes |
| LiF | [LiF__src_jy](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/LiF__src_jy) | Yes |
| MgO | [MgO__src_fix_gap](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/MgO__src_fix_gap) | Yes |
| NaCl | [NaCl__src_sg15](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/NaCl__src_sg15) | No |
| SiC | [SiC__src_pca1e-6](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/SiC__src_pca1e-6) | Yes |
| Si | [Si__src_all_kpath](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison/Si__src_all_kpath) | Yes |

Supplementary reference folders include [GaAs 13e/5e and 21e/15e PP cases](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_01_pseudopotential_metrics), [ABF-compression comparisons](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_02_ABF_compression), and [VASP comparison cases](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_03_VASP_benchmark).

## Download and reuse

- [Download the complete data repository as ZIP](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/archive/refs/heads/main.zip).
- The [upstream README](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/README.md) describes the retained files and publication context.
- The data repository currently declares no GitHub license. Treat its files as reference downloads; do not mirror or redistribute its PP, NAO, ABF, inputs, or outputs until their reuse terms are confirmed.
- Recompute SHA-256 values from downloaded files and compare them with `MANIFEST.tsv`. A matching hash establishes file identity, not physical suitability for a different protocol.
