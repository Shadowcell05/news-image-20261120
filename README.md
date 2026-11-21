# The World in One Picture — Friday 20 November 2026

A one-image front page summing up the world news of **Friday 20 November 2026**,
entered in make.fun's News Image competition for that day. Built to the boards'
winning formula: **48 verified stories, six continents, one page** — with
per-story pictograms, a UTC timeline of the day, an explicit date-check band,
a dot-matrix world map and a day-in-figures box.

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Shadowcell05/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Shadowcell05/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

## What's in the picture

- **Lead:** Russia's night strike on Ukraine — over 400 drones and 110 missiles,
  eight killed in Kyiv, bridges and rail stations hit, and Russian missiles
  coming down on Polish soil.
- **Date check band:** every story on the page was first reported on Friday
  20 November 2026, cross-checked across 30+ sources.
- **The day in UTC:** from Kyiv's morning count of 380 drones and 79 missiles
  downed, through the EU–UK summit in Brussels, to the Wall Street close.
- **Front page grid, by continent:** the Wall Street rout (S&P 500 −3.7%),
  GTA VI's $3.79bn day-one sales record, COP31 running into overtime, Ebola
  "out of control" in DR Congo, a fifth tanker hit in Hormuz, Cyclone Akvan's
  Odisha landfall, Haiti's gang raid, Peru's floods — and more.
- **The day in figures:** 510+ weapons fired at Ukraine, 11,200 Ebola cases,
  300,000 evacuated ahead of Cyclone Akvan.
- **In brief:** Quebec's poster boxes, Iran's condemned taekwondo champion,
  gold's 4% slide, a Congo family that lost 46 relatives to Ebola.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled `entry.png`
to `/output/entry.png` — or to `$MAKEFUN_OUTPUT_DIR/entry.png` when that
variable is set. It runs offline, writes identical bytes on every run, and
verifies the copied file's size against the original before exiting.

## License

MIT — see `LICENSE`.
