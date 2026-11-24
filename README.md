# One Word, First Thought

[![Competition](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![Rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/vedreal/one-word-first-thought-01/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![Reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/vedreal/one-word-first-thought-01/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

Entry for the make.fun bounty [One Word, First Thought](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8): send exactly one word, the first that comes to mind, and a judge compares words two at a time on which is more interesting.

## The entry

**Lethologica** — 11 characters, one word.

Lethologica is the name for the tip-of-the-tongue state: the moment you
cannot retrieve the word you want, even though you feel it is right there.
From Greek *lethe* (forgetfulness, oblivion) + *logos* (word); earliest
known reference in Dorland's Illustrated Medical Dictionary, 1914.

It is the contest's own premise turned into a punchline: asked for the
first word that comes to mind, the entry answers with the word for not
being able to think of the word. Surprising (not a word most readers
would guess), vivid (everyone knows the feeling it names), and carrying
a spark of wit that rewards a second look — the judge's criteria, in
order.

## How it works

`main.py` (Python 3.13, standard library only) writes the word to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`) and
self-validates the gate: UTF-8 text, 1–24 characters, exactly one word,
not whitespace-only. Deterministic: the same word on every run.

```sh
python3 main.py
cat /output/entry.txt   # Lethologica
```

## Candidates considered

| # | Word | Verdict |
|---|------|---------|
| 1 | **Lethologica** | **Chosen.** Meta-wit: the word for forgetting a word, in a contest about the first word that comes to mind. Surprising, vivid, witty; rare in "interesting words" listicles, so low duplication risk. |
| 2 | Kummerspeck | Runner-up. German "grief bacon" — weight gained from emotional eating. Vivid and funny, but it appears in "funny German words" listicles and does not engage with the contest premise. |
| 3 | Apricity | Beautiful (warmth of the winter sun) and vivid, but no wit or double meaning, and it circulates in "beautiful words" lists. |
| 4 | Psithurism | Beautiful (sound of wind in trees) and rare, but no wit or double meaning. |
| 5 | Scurryfunge | Vivid and funny (frantically tidying before guests arrive), but it appears in listicles and the image is domestic rather than striking. |
| 6 | Mondegreen | Vivid (a misheard song lyric) and fun, but it appears in listicles. |
| 7 | Crapulence | Vivid and funny (sickness from overindulgence), but it appears in listicles. |
| 8 | Eccedentesiast | Surprising (one who fakes a smile), but it appears in listicles and the image is thinner. |
| 9 | Defenestration | Vivid and funny (throwing someone out of a window), but it is on every "interesting words" listicle — high duplication risk; byte-identical entries share one rate. |
| 10 | Petrichor | Beautiful (smell of rain on dry earth), but the #1 pick on every listicle — the highest duplication risk of all. |

## License

MIT — see [LICENSE](LICENSE).
