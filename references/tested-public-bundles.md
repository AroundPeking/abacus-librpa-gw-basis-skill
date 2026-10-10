# Public calculation bundle index

The public case lists are split by dimensionality so new 2D pseudopotential
and basis contributions can be added without mixing them with the 3D bulk
benchmarks:

- [2D materials and basis assets](tested-public-bundles-2d.md)
- [3D bulk cases and basis assets](tested-public-bundles-3d.md)

Both lists point to the published
[ABACUS + LibRPA GW calculation-data repository](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks).
Its [`MANIFEST.tsv`](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/MANIFEST.tsv)
records SHA-256 hashes for retained files. The current upstream repository has
no declared GitHub license, so do not mirror or redistribute its assets until
their reuse terms are confirmed.

These are reproducibility records for the calculations they document. A
published GW output or a matching hash does not prove that a basis is
converged for another material, observable, mesh, or code version. Check each
case's inputs, outputs, and validation evidence before reuse.

- [Download the upstream data repository as ZIP](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/archive/refs/heads/main.zip)
- [Upstream README and publication context](https://github.com/AESM-Group/abacus-librpa-g0w0-nao-pp-benchmarks/blob/main/README.md)
