# Calibration of the audit (Codex, high reasoning effort, blind)

30 audited articles drawn at random (seed 20261114). For each: every sentence Sonnet called a hard error, plus 2 random sentences it called supported, shuffled and shown to Codex without Sonnet's labels, with the same readable source texts.

| Sonnet said | Codex: contradicted | Codex: not in sources | Codex: supported | Codex: opinion |
|---|---|---|---|---|
| hard error (144) | 66 (46%) | 64 (44%) | 13 (9%) | 1 |
| supported (52) | 4 (8%) | 15 (29%) | 30 (58%) | 3 |

- Articles where both judges agree on at least one hard error: **23 of 30 (77%, Wilson 95% CI 59%–88%)**. The decision threshold (lower bound ≥ 20%) is met even on this stricter two-judge count.
- Sonnet over-calls "contradicted" where Codex sees "not in the sources" (44% of its hard errors), and misses problems in sentences it calls supported (37%). Neither judge is ground truth; agreement is not accuracy.
- An earlier calibration of the 10-article pilot ran Codex at its configured low reasoning effort and is superseded by this one.
