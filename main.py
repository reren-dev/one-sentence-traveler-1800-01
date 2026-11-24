#!/usr/bin/env python3
"""One sentence for a traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler who has just stepped out of the year 1800,
to /output/entry.txt.

The sentence is built only from things a person from 1800 already knows:
roads, libraries, post offices, letters, ink, books, and shelves.
No word in it was coined after the traveler's time: the program checks
the sentence against a small list of modern words and refuses to write
it if one slips in.
"""

import os

# Words coined after 1800 that must never appear in the sentence.
MODERN_WORDS = (
    "internet", "computer", "online", "website", "email", "e-mail",
    "screen", "digital", "phone", "television", "radio", "wireless",
    "download", "upload", "browser", "server", "software", "data",
)

SENTENCE = (
    "Imagine a single road joining every library and post office on "
    "earth, so a letter you send arrives before the ink dries, and "
    "the books of every land wait upon your own shelf."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"sentence is {len(text)} characters, must be 1-200")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    lowered = text.lower()
    for word in MODERN_WORDS:
        if word in lowered:
            raise SystemExit(f"modern word slipped into the sentence: {word}")
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
