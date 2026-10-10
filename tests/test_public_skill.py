#!/usr/bin/env python3
"""Pressure test for the public ABACUS + LibRPA GW skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = " ".join((ROOT / path).read_text(encoding="utf-8").split())
    for needle in needles:
        assert needle in text, f"{path} is missing required text: {needle!r}"


def main() -> int:
    require(
        "SKILL.md",
        (
            "name: abacus-librpa-gw-basis",
            "Use when",
            "pseudopotential",
            "physical numerical atomic orbital",
            "auxiliary basis",
            "pseudopotential -> physical NAO -> ABF",
            "GW",
            "SHA-256",
            "results",
            "gates",
            "assumptions",
            "pending",
        ),
    )
    require(
        "references/pseudopotential-selection.md",
        ("same pseudopotential", "semicore", "SOC", "plane-wave", "no universal"),
    )
    require(
        "references/nao-generation.md",
        ("SIAB", "spillage", "training", "empty-state", "same PP"),
    )
    require(
        "references/abf-generation.md",
        ("ABF", "for_aux", "PCA", "Coulomb", "EXX"),
    )
    require(
        "references/gw-handoff.md",
        ("reader", "STRU", ".orb", ".upf", ".abfs", "nbands"),
    )
    require("templates/basis-manifest.example.json", ("sha256", "source_url"))
    require("templates/validation-report.example.json", ("gates", "pending"))
    require("templates/SIAB_INPUT.example", ("Pseudo_name", "Level1", "Save3"))
    require("templates/INPUT.abf-generation.example", ("rpa", "exx_pca_threshold"))
    require("templates/STRU.abfs.example", ("NUMERICAL_ORBITAL", "ABFS_ORBITAL"))
    require("templates/STRU.abf-generation.example", ("X_pbe_for_aux.orb", "ATOMIC_POSITIONS"))
    require("templates/KPT.gamma.example", ("1 1 1 0 0 0",))
    require(
        "references/abf-generation.md",
        ("exx_cs_inv_thr", "for_aux", "gen_opt_abfs", "exit(0)", "806cde132cbf98c25809e1a6f51a700ca97ce10c"),
    )

    forbidden = re.compile(
        r"(?:/" + r"Users/|/home/" + r"(?:[A-Za-z0-9_.-]+)|ssh:" + r"//|SLURM_" + r"JOB_ID)"
    )
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        assert not forbidden.search(text), f"private path or host leak in {path}"
    return 0


if __name__ == "__main__":
    sys.exit(main())
