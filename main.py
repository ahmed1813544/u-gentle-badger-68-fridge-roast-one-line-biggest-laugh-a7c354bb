"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast of a smart fridge to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python 3.13 standard library only. Fully deterministic: the same
line is written on every run.
"""

import os
from pathlib import Path

# The roast: a smart fridge so smart it forgot its one job.
LINE = "My fridge updated its firmware last night and forgot how to be cold until it restarts."


def main() -> None:
    # The gate allows 1-200 characters; never ship a line that breaks it.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
