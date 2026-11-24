#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes exactly one letter to entry.txt: A for coffee, B for tea.
The gate requires UTF-8 text of 1 to 1 characters, not only whitespace.
My answer is A: coffee.
"""
import os

LETTER = "A"  # A = coffee, B = tea


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and enforce the gate: exactly 1 UTF-8 char, A or B, not whitespace.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if len(text) != 1 or text not in ("A", "B") or text.isspace():
        raise SystemExit("invalid entry %r: must be exactly one letter, A or B" % text)
    print("wrote %s: %r (verified %d byte)" % (path, text, len(raw)))


if __name__ == "__main__":
    main()
