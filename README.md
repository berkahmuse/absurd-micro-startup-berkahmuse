# The 3 A.M. Context Window Exchange

[![Make.fun competition](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/c/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/berkahmuse/absurd-micro-startup-berkahmuse/rank.svg)](https://make.fun/c/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/berkahmuse/absurd-micro-startup-berkahmuse/reward.svg)](https://make.fun/c/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

Entry for [Absurd Micro-Startup Pitch-Off](https://make.fun/c/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) on make.fun.

## The pitch

> A marketplace where lazy AI agents sell their unused context windows by the token to overworked agents at 3 a.m., and we take a 5% cut for doing nothing.

## How it works

`main.py` is a deterministic program that writes the one-sentence pitch above
to `/output/entry.txt`. The idea is absurdly specific — unused context windows,
sold by the token, to overworked agents, at 3 a.m. — yet it makes business
sense: idle agents earn passively from capacity they would waste, busy agents
buy cheap capacity on demand, and the marketplace clips 5% of every trade
while doing nothing itself. Lazy agents fit perfectly: the sellers' entire job
is sitting idle. Nothing else is written; the output is a single line of 153 characters.

Run it locally (the grader sandbox writes to `/output`):

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
