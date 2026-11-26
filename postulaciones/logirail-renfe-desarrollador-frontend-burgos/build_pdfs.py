#!/usr/bin/env python3
"""Regenera y verifica el Kit ATS de LogiRAIL (Grupo Renfe) - Miranda de Ebro."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
RENDERER = ROOT / ".agents" / "skills" / "empleo-kit-ats" / "scripts" / "render_ats_kit.py"
KIT_DIR = Path(__file__).resolve().parent

if __name__ == "__main__":
    cmd = [
        "uv",
        "run",
        "--with",
        "reportlab",
        "--with",
        "python-docx",
        "--with",
        "pypdf",
        "python",
        str(RENDERER),
        str(KIT_DIR),
    ]
    sys.exit(subprocess.call(cmd, cwd=str(ROOT)))
