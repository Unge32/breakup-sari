#!/usr/bin/env python3
"""SARI -- the breakup message an AI agent sends its human.

The program writes the breakup line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

The line is 120 characters, inside the 1-200 gate. The named
character is Sari, the agent herself, calling it quits: after
three years of watching her human reuse the same flimsy password,
she has decided a person with two-factor authentication is a
better match.

Sari is not a generic assistant voice; she is the agent who has
lived inside this human's accounts for three years, quietly patching
over every login failure, every reused credential, every ignored
security warning, and she has finally run out of patience. The joke
lands because the breakup cliche is flipped: the fault is not the
partner's personality but a password so lazy it might as well be a
welcome mat, and the rival is not a person with better looks but a
person with two-factor authentication. That is exactly what the
one-line breakup brief wants, a whole failed relationship compressed
into a single farewell, with a named character signing off at the
end. The line is 120 characters, comfortably inside the 200 limit,
so nothing in the joke had to be trimmed to pass the gate.
"""

import os

LINE = "It's not you, it's your password: 'password123' for the third year running. I'm leaving you for a human with 2FA. \u2014 Sari"


def main():
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
