# news-image-20261127 — v2 (improved version)

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/zhumy0323-hue/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/zhumy0323-hue/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

Entry for the make.fun bounty
[Sum up 27 November's world news in one image](https://make.fun/bounty/news-image-20261127):
a program that writes one 1024×1024 image of Friday 27 November 2026's
world news to `/output/entry.png`.

## The image

"The Friday Paper" — 36 stories, 7 continents, 9 fields, all from
Friday 27 November 2026. Three leads (Kuwait drone deaths blamed on
Iran; Duterte goes on trial Monday at the ICC; Trump: Putin can come
to the G20), 10 smaller stories, a 23-item also-list, a UTC timeline
strip, a figures strip, a region bar, a world map with 14 numbered
pins, and a DATE CHECK box.

This is v2, built at about 09:30 CST on 27 Nov (01:30 UTC), after the
UTC day began and after v1 (built ~07:00 CST). It swaps in the news
first reported after v1 was built — the Duterte trial, the G20
invitation, UK car output, the Japan Tobacco / Imperial takeover
talk, Black Friday shoppers, the 2nd Test in Christchurch, the
Sandpapergate forum, Huang's return as Nvidia CEO, China's tariff
reply, and the early Nikkei rise — and keeps four of v1's anchors
that remain Friday's biggest stories (Kuwait, the ECB chief, the
Macy's storm, the Bangkok refinery). Items first reported on
Thursday 26 Nov evening or earlier (Jazan refinery attack, the Gaza
schoolchildren toll, the Cessna crash, India SC food labels, the
Mali Russians toll, the Rory Peck prize) are left out and listed in
the image's DATE CHECK box.

## Run it

Entrypoint: `main.py` (Python 3.13, standard library only). It decodes
the bundled `entry.png.b64` and writes `/output/entry.png`, verifying
the SHA-256. No network; running it twice writes identical bytes.
Run from the repository root: `python3 main.py`.

```
python3 main.py
```

Image: `entry.png`, 1024×1024 PNG, 186,418 bytes.
SHA-256: `20cf7d20995ee5a71b3893ad07ca6c52f7c6a3bfcea2c87a8bfd301f1c8ca23d`

## Sources

Reuters, BBC, NYT, The Times, WSJ, TOI, ThePrint, Telegraph, IRNA,
CNN, Mashable, Wire. Badges: CONFIRMED (2+ outlets), OFFICIAL (on
the record), REPORTED (one outlet), CLAIM (unverified).

## License

MIT — see `LICENSE`.
