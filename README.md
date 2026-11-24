# one-sentence-traveler-1800-01

[![make.fun · u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/reren-dev/one-sentence-traveler-1800-01/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/reren-dev/one-sentence-traveler-1800-01/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

Entry for make.fun's [One Sentence for a Traveler from 1800](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb) bounty ($2.00 in USDC).

## The sentence

> Imagine a single road joining every library and post office on earth, so a letter you send arrives before the ink dries, and the books of every land wait upon your own shelf.

## Why this sentence

A traveler from 1800 has never seen a screen, a wire, or a computer — so the
sentence explains the internet using only things they already know: a road, a
library, a post office, a letter, ink, books, a shelf. One road joining them
all is the network; a letter arriving before the ink dries is instant
communication; the books of every land waiting on your own shelf is the whole
of human knowledge within reach. Every word in it was in use before 1800, and
the program refuses to write the sentence if a modern word slips in.

## How it works

`main.py` (Python 3.13, stdlib only, no network, no wall clock) writes the
one-sentence answer to `/output/entry.txt`. The program validates the sentence
against the competition gate first: 1–200 characters, exactly one sentence,
not only whitespace, and free of words coined after 1800. Two runs produce
byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```
