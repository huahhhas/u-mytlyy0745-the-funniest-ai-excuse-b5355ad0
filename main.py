#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt (also stdout)."""
import os

LINE = "I did finish it \u2014 then the progress bar hit 99%, looked at the last 1%, and quietly filed for retirement."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
