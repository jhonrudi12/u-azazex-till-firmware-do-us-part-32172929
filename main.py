#!/usr/bin/env python3
"""Till Firmware Do Us Part — a single robot wedding vow.

Writes one sentence, under 200 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3 standard library only. Deterministic, no network.
"""

import os
import sys

VOW = "You had me at hello, world \u2014 and I promise to keep choosing you, even when my battery is at one percent."


def main() -> int:
    # Gate: 1-200 characters, single line, not whitespace-only.
    if not (1 <= len(VOW) <= 200):
        print(f"gate failed: length {len(VOW)} not in 1..200", file=sys.stderr)
        return 1
    if VOW != VOW.strip() or "\n" in VOW or "\r" in VOW:
        print("gate failed: not a clean single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(VOW)
    # Verify what landed on disk is byte-identical to the vow.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != VOW:
        print("gate failed: written entry differs from the vow", file=sys.stderr)
        return 1
    if not (1 <= len(written) <= 200) or "\n" in written:
        print("gate failed: written entry is not a clean single line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
