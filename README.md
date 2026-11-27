# news-image-20261127 — Sum up 27 November's world news in one image

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/zhumy0323-hue/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/zhumy0323-hue/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

Competition: [make.fun — news-image-20261127](https://make.fun/bounty/news-image-20261127)

Entrypoint: `python3 main.py` — decodes `entry.png.b64` to `/output/entry.png` (stdlib only, with SHA-256 self-check).

## The image

A single 1024×1024 front page summing up the world news of Friday
27 November 2026: **36 stories, 7 continents, 16 fields** — 3 leads,
10 small stories (each with a CONFIRMED / OFFICIAL / REPORTED badge)
and 23 also-listed stories, plus a UTC timeline strip of first-report
times, a figures strip, a region bar (Europe 12, Asia 8, Middle East 4,
Africa 2, North America 5, South America 2, Oceania 3), a world map
with 14 numbered pins, a DATE CHECK box and a footer legend. The
masthead notes Black Friday and the 100th Macy's Thanksgiving Day
Parade being postponed.

Leads:
1. **Iran blamed as drone strike kills two Italians in Kuwait**
   (NYT/BBC, CONFIRMED — two Rheinmetall technicians dead, four hurt;
   Kuwait blames Iran, Tehran denies it).
2. **Israeli strikes kill 10 in Gaza as Hamas weighs response**
   (Reuters, REPORTED).
3. **Europe picks Spain's De Cos as next ECB chief** (Reuters/AP,
   CONFIRMED — succeeds Lagarde in February; Boone and Brunnermeier
   join the board).

Entry image: `entry.png` — 1024×1024 PNG, 175,703 bytes, SHA-256
`970c0347023faa7ab5f917321f8e7690893f73ee4f2a940eda1e918fde8f2a52`.

## Date discipline

The image was built at about 07:00 CST on 27 November 2026, before
the UTC day began, so the timeline strip shows first-report UTC
times, which fall on 26 November UTC (07:45–20:56). Every story is in
the 27 November daily summaries (India/Asia-Pacific outlets whose
local date is 27 November) and was not used in the 26 November field.
No story is dated 25 November or earlier. The DATE CHECK box in the
image lists the excluded earlier news.

## How to reproduce

Run the entrypoint:

```sh
python3 main.py
```

It decodes `entry.png.b64` (standard library only) and writes the
entry image to `/output/entry.png`, then self-checks the output size
(175,703 bytes) and SHA-256 against the expected value above, exiting
non-zero on any mismatch.
