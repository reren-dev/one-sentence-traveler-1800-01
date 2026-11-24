#!/usr/bin/env python3
"""One sentence for a traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler who has just stepped out of the year 1800,
to /output/entry.txt.

The sentence is built only from things a person from 1800 already knows:
roads, libraries, post offices, letters, horses, books, and supper.
"""

import os

SENTENCE = (
    "It is a road joining every library and post office on earth, "
    "carrying your letters faster than any horse, so a farmer may read "
    "a book kept across the sea before supper."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"sentence is {len(text)} characters, must be 1-200")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
