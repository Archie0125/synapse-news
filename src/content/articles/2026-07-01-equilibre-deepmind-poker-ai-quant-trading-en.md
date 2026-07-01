---
title: "DeepMind's Poker AI Creators Are Now Beating Markets With the Same Reinforcement Learning"
summary: "EquiLibre Technologies, founded by the three researchers who built DeepStack — the first AI to defeat professional poker players — has raised a Series A at a $500 million valuation. Their Prague-based lab is applying the same reinforcement learning techniques to stock and crypto markets, reporting zero negative months since inception in partnership with quant firm Tower Research Capital."
category: "startups"
publishedAt: 2026-07-01
lang: "en"
featured: false
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/30/the-deepmind-trio-who-built-a-poker-ai-are-now-making-money-for-quant-hedge-funds/"
  - name: "Futurum Group"
    url: "https://futurumgroup.com/insights/ex-deepmind-researchers-launch-equilibre-to-give-stock-and-crypto-traders-an-edge-using-ai/"
  - name: "Mezha"
    url: "https://mezha.net/eng/bukvy/dbb81e5d_ex-deepmind_researchers_apply/"
tags:
  - "deepmind"
  - "reinforcement-learning"
  - "fintech"
  - "quant-trading"
  - "startups"
  - "ai"
relatedSlugs:
  - "2026-07-01-equilibre-deepmind-poker-ai-quant-trading-zh"
---

In 2017, three visiting PhD students at DeepMind's Edmonton research office published a paper that changed the history of game-playing AI. Their system, DeepStack, became the first artificial intelligence to defeat professional players at no-limit Texas hold 'em poker — a game of imperfect information, bluffing, and probabilistic reasoning that had long resisted the approaches that conquered chess and Go.

Nearly a decade later, those same three researchers have turned DeepStack's core ideas toward a different game with much larger stakes: financial markets. Their company, EquiLibre Technologies, has raised a Series A led by Creandum — the largest single investment the Swedish VC firm has ever made — at a reported $500 million valuation. The Prague-based startup says its algorithms have maintained a perfect record of zero negative months since deployment, trading billions in daily volume across the S&P 500 and Nasdaq in partnership with quant giant Tower Research Capital.

## The Team Behind DeepStack

Martin Schmid (CEO), Rudolf Kadlec (CTO), and Matej Moravcik (CSO) built DeepStack while visiting DeepMind's first international AI research outpost in Edmonton, Alberta. The lab, which Alphabet shut down in 2023, was at the time one of the world's most concentrated nodes of AI talent. The trio's poker AI achievement was published in *Science* in 2017 and instantly elevated them to the front rank of reinforcement learning researchers.

The connection between poker and financial trading is more than metaphorical. Both involve sequential decision-making under uncertainty, incomplete information about opponents' positions, and reward signals that are unambiguous but delayed. In poker, the score is chips won or lost per session. In trading, as Schmid puts it: "The nice thing about trading and markets is that the scoring is super simple: how much money did the agent make?"

This directness of reward signal is precisely what makes financial markets an attractive domain for reinforcement learning. Unlike supervised learning applications, where you need labeled training data, RL agents learn by doing — they take actions, observe outcomes, and update their strategies. The poker research demonstrated that RL agents trained through self-play could develop strategies that outperformed human intuition in complex, adversarial, imperfect-information environments. Markets are exactly that.

## From Poker Tables to Trading Desks

EquiLibre's algorithms were initially deployed in cryptocurrency markets in 2025, where liquidity conditions, 24/7 operation, and data richness made them an ideal proving ground. The track record built in crypto — zero negative months since inception — gave Tower Research Capital the confidence to extend the partnership to equity markets.

Tower Research Capital is one of the world's largest and most sophisticated quantitative trading firms, responsible for significant daily volume across global exchanges. The firm's willingness to integrate EquiLibre's RL-based agents into live equity trading — managing "billions in daily volume" across the S&P 500 and Nasdaq — is itself a significant institutional endorsement. Tower doesn't experiment with unproven technology on live capital at that scale.

The specific strategies EquiLibre employs are not publicly disclosed, as is standard in quantitative trading. The firm's competitive advantage lies in the approach — self-learning models motivated by financial reward signals, applying the imperfect-information game theory developed for poker to the perpetual adversarial game of price discovery — rather than any single trade or algorithm.

## The Business Case for Reinforcement Learning in Finance

Traditional quantitative trading relies heavily on statistical arbitrage: identifying price discrepancies across assets or time periods based on historical patterns and exploiting them before they close. These strategies are subject to alpha decay as more capital chases the same signals, and they require constant recalibration as market microstructure evolves.

Reinforcement learning offers a different paradigm. Rather than encoding human-identified patterns, RL agents develop their own representations of market dynamics through interaction. They can adapt to changing conditions — market regime shifts, new participants, policy changes — in ways that static models cannot. And because they're trained through self-play and interaction rather than historical data alone, they're potentially less exposed to the overfitting that plagues backtested quant strategies.

The poker analogy holds at the competitive level too. Markets are not solved games; like poker, they have persistent exploitable inefficiencies because participants have bounded rationality and varying objectives. An RL agent that can model counterparty behavior and adapt its strategy dynamically has a structural advantage over agents relying on fixed rules.

## $500M Valuation and the Series A

EquiLibre's funding history reflects the trajectory of a high-conviction bet on a novel research approach. A seed round of $10 million, led by Blossom Capital at a $140 million valuation, gave the founders runway to prove out the crypto trading thesis. The Series A — led by Creandum and described as the largest single investment in the firm's history — represents a major conviction upgrade.

The $500 million valuation for a 25-person Prague-based lab may raise eyebrows in traditional finance circles, but it maps logically onto the asset management opportunity. A quant strategy that generates consistent uncorrelated returns at scale is worth enormous multiples of its technology cost, because the underlying business is managing capital at fees, not selling software licenses.

The firm's 25 employees are based in Prague, where it has leveraged a Czech diaspora network from Google and other tech firms to recruit. The city's deep ties to European research institutions and its cost structure relative to London or New York give EquiLibre a talent advantage at its current scale.

## The Broader Trajectory

EquiLibre sits at the intersection of two powerful trends: the professionalization of AI research talent into high-value commercial applications, and the maturation of reinforcement learning from academic curiosity to production-grade technology.

The DeepMind talent exodus — which has been running for years and accelerated through 2025 and 2026 as Alphabet's AI standing came under pressure — has seeded a generation of exceptionally capable researchers into startups and commercial ventures. EquiLibre is one of the more technically distinctive products of that diaspora: a founding team who used their DeepMind tenure to solve a canonical imperfect-information problem and are now applying that solution to the largest imperfect-information game in the world.

Whether RL-based trading can sustain its edge as the strategies become more widely known — and as market participants adapt to them — is the central unanswered question. Poker AIs eventually plateaued against each other in self-play, converging on Nash equilibria that left no edge. Markets may be more complex and less bounded. If EquiLibre has found a durable structural approach rather than a temporary alpha, it is building something worth multiples of its current valuation. If not, it is the most sophisticated example yet of the quant strategy lifecycle playing out at AI speed.

The zero negative months record will be tested. The more interesting question is how it holds when it is.
