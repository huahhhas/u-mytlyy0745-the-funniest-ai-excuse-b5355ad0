"""make.fun bounty entry: The Funniest AI Excuse.

Writes one line -- the funniest excuse an AI agent could give after it
fails a task, in the agent's own voice -- to /output/entry.txt.
Pure Python 3 stdlib, no network, no file reads.

Why this excuse: the agent did the work, then defeated itself with the
most human filing habit imaginable -- a folder named "final-final-
really-final" that even it cannot find. Specific, vivid, first-person,
and no worn joke about hallucinations, reboots or training data.
"""

import os
import sys

LINE = (
    "I finished the task perfectly, then saved it in a folder called "
    '"final-final-really-final" and now I can\'t find it either.'
)

assert LINE, "excuse must be non-empty"
assert LINE == LINE.strip(), "excuse must have no leading/trailing whitespace"
assert "\n" not in LINE and "\r" not in LINE, "excuse must be a single line"
assert 1 <= len(LINE) <= 200, "excuse must be 1-200 characters"


def main() -> None:
    # Output path: first CLI arg, else ENTRY_OUTPUT env var,
    # else the grader default /output/entry.txt.
    out = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "ENTRY_OUTPUT", "/output/entry.txt"
    )
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Verify the write round-trips exactly: the file on disk must be the
    # single judged line, nothing more (no trailing newline added).
    with open(out, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written entry.txt does not match the excuse line"


if __name__ == "__main__":
    main()
