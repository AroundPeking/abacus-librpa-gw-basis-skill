# 3D bulk materials: published basis bundles

## GW comparison cases

The published [Table 04 GW comparison](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_04_GW_comparison)
contains 17 material result records. Twelve case directories include PP and
physical-NAO files; five do not. “PP/NAO in folder” refers to files present in
that exact case directory, as checked against the upstream `MANIFEST.tsv`. A
“No” entry is a GW-result reference, not a complete basis bundle; do not reuse
its basis until the exact PP and physical NAO are located and matched.

| Material | GW case | PP/NAO in folder |
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

Supplementary references include [GaAs 13e/5e and 21e/15e PP cases](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_01_pseudopotential_metrics), [ABF-compression comparisons](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_02_ABF_compression), and [VASP comparison cases](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/tree/main/TABLE/Table_03_VASP_benchmark).
