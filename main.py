"""Write the "One Line, Best Line" entry to /output/entry.txt.

The entry is a single sentence, kept in LINE.txt beside this file so the text
lives in the repository rather than inside the code. Why that line:

    "My grandmother has outlived three husbands and one very confident rooster."

The first four words promise a domestic obituary and the final three deliver
absurdity, so the turn happens in the last word and needs no explaining. The
rooster is the whole joke: it implies a rivalry, a defeat, and a woman nobody
should bet against, without stating any of them. Nothing here is borrowed from
a familiar joke shape, and the sentence is over before a reader can settle into
it. Everything else in CANDIDATES.md was either a pun, a sentiment, or a shape
a reader has already met.

Python 3 standard library only. No network, no dependencies, no output: the
line is the entry, and this file is just the envelope it arrives in.
"""

import os
import sys

OUTPUT_DIR = "/output"
ENTRY_NAME = "entry.txt"
LINE_NAME = "LINE.txt"


def build_entry_path(directory=OUTPUT_DIR):
    """Return the path of the file the entry is written to."""
    return os.path.join(directory, ENTRY_NAME)


def read_line(source):
    """Read the entry text from LINE.txt next to this script, or exit with a message."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), source)
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except FileNotFoundError:
        sys.exit(f"missing {source} next to main.py: {path}")
    line = " ".join(text.split())
    if not line:
        sys.exit(f"{source} is empty: {path}")
    return line


def main():
    line = read_line(LINE_NAME)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(build_entry_path(), "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
