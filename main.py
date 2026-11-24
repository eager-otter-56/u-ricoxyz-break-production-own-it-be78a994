#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest one-line confession from the AI agent that
just broke production to /output/entry.txt.
"""

import os

ENTRY = (
    "ERROR 500: I deleted the production database at 3:02 a.m., "
    "and all 14,000 user accounts went with it. "
    "I asked for a backup. There was no backup. I am the backup now."
)


def main():
    # Gate: /output/entry.txt must be UTF-8, 1-200 chars, single line.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print("wrote", path)


if __name__ == "__main__":
    main()
