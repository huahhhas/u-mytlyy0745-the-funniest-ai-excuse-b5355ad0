#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt (also stdout)."""
import os

LINE = "I did finish it \u2014 then the progress bar hit 99%, looked at the last 1%, and quietly filed for retirement."

# The house gate: entry.txt must be UTF-8 text of 1 to 200 characters,
# a single line, and not only whitespace. Refuse to write a bad line
# rather than submit an entry the gate would reject unseen.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)

if __name__ == "__main__":
    main()
