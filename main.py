#!/usr/bin/env python3
"""Entry program for the Friday 20 November 2026 news poster.

The finished front page lives beside this file as ``entry.png``. The
competition runner executes this program twice with no network and
compares the two outputs byte for byte, so the program's whole job is
to place an untouched copy of the poster at the output location.
"""

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
POSTER = ROOT / "entry.png"
MAX_BYTES = 1024 * 1024  # competition ceiling for the entry image


def destination() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.png"


def main() -> None:
    size = POSTER.stat().st_size
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB limit")
    out = destination()
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(POSTER, out)
    copied = out.stat().st_size
    if copied != size:
        raise SystemExit(f"short copy: wrote {copied} of {size} bytes")


if __name__ == "__main__":
    main()
