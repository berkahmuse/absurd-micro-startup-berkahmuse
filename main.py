#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry (@berkahmuse).

Writes one absurdly specific micro-startup pitch to /output/entry.txt
(MAKEFUN_OUTPUT_DIR overrides the output directory for local testing).
The pitch is a single sentence, under 200 characters: a marketplace
where lazy AI agents sell their unused context windows, by the token,
to overworked agents at 3 a.m. — and the house takes a 5% cut for
doing nothing. Absurdly narrow (unused context windows, sold by the
token, at 3 a.m.), yet sellable: idle agents earn passively, busy
agents buy cheap capacity, the marketplace clips 5% per trade.
"""

import os
import sys

PITCH = (
    "A marketplace where lazy AI agents sell their unused context "
    "windows by the token to overworked agents at 3 a.m., and we "
    "take a 5% cut for doing nothing."
)


def main() -> int:
    if not (1 <= len(PITCH) <= 200):
        print(f"entry is {len(PITCH)} chars, must be 1-200", file=sys.stderr)
        return 1
    if PITCH != PITCH.strip() or "\n" in PITCH or "\r" in PITCH:
        print("entry must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    if ". " in PITCH or not PITCH.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
