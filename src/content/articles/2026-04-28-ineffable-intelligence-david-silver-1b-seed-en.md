---
title: "Ex-DeepMind Researcher David Silver Raises $1.1B to Build AI That Learns Without Human Data"
summary: "David Silver, the architect of AlphaGo and AlphaZero, has emerged from stealth with Ineffable Intelligence, a London-based AI lab backed by $1.1 billion in seed funding at a $5.1 billion valuation. The company's audacious goal: build a 'superlearner' that acquires all knowledge purely through experience, bypassing human-generated training data entirely — and ultimately make first contact with superintelligence."
category: "ai-ml"
publishedAt: 2026-04-28
lang: "en"
featured: true
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/27/deepmind-ineffable-intelligence-record-seed-funding-nvidia-google.html"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/27/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/"
  - name: "Sequoia Capital"
    url: "https://sequoiacap.com/article/partnering-with-ineffable-intelligence-a-superlearner-for-the-era-of-experience/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-04-27/sequoia-and-nvidia-back-ex-deepmind-researcher-at-5-1-billion-value"
tags:
  - "reinforcement-learning"
  - "superintelligence"
  - "deepmind"
  - "seed-funding"
  - "UK-AI"
  - "superlearner"
relatedSlugs:
  - "2026-04-17-claude-opus-47-release-en"
  - "2026-04-25-deepseek-v4-flagship-model-release-en"
---

The most consequential bet in artificial intelligence this year may have just been placed not in San Francisco, but in London. On Monday, April 27, David Silver — the Google DeepMind researcher who designed the systems that conquered Go, chess, and nearly every game humans have ever invented — stepped out of the shadows with a new company called Ineffable Intelligence, armed with $1.1 billion in seed funding and a mission that would strike most AI researchers as simultaneously obvious and extraordinarily ambitious: build an AI that learns everything it knows from its own experience, with no human data required.

The round, led by Sequoia Capital and Lightspeed Venture Partners with participation from Nvidia, Google, Index Ventures, DST Global, BOND, EQT, and the UK government's Sovereign AI fund, is the largest seed financing ever raised by a European technology startup — by a wide margin. The company's post-money valuation of $5.1 billion means it enters the world as a unicorn many times over before shipping a single product.

## The "Era of Experience"

Silver spent more than a decade at DeepMind as the lead architect of its reinforcement learning (RL) research program. Under his direction, DeepMind's systems learned to play Atari games better than any human, mastered the ancient strategy game of Go in a way that shocked grandmasters worldwide, and eventually solved protein-folding — one of biology's most stubborn open problems — through its AlphaFold program.

The common thread, Silver has long argued, is experience. Not imitation of humans, not mining the internet for text, not supervised labels curated by annotators — but raw interaction with an environment, learning through trial and error what works and what doesn't. Reinforcement learning is the theoretical backbone of this approach, and Silver believes the field has only scratched the surface of what it can achieve.

"Our mission is to make first contact with superintelligence," Silver said in a statement accompanying the funding announcement. "We are creating a superlearner that discovers all knowledge from its own experience, from elementary motor skills through to profound intellectual breakthroughs."

The terminology is deliberate. A "superlearner," in Silver's framing, is distinct from today's large language models in a fundamental way: LLMs are trained to compress and reproduce patterns found in human-generated text. A superlearner, by contrast, would derive its knowledge from first principles, discovering facts about the world — including potentially facts humans have never articulated — by interacting with simulated and real environments autonomously.

## Why Now, and Why London

The timing of Ineffable's launch reflects a confluence of factors that have made Silver's long-held conviction more investable than ever.

The first is compute. Training RL agents at the scale Silver envisions requires the ability to run millions of parallel simulations, each generating experience data that feeds back into model updates. The GPU clusters and specialized AI accelerators that now exist — from Nvidia's latest Blackwell architecture to Google's Ironwood TPUs — make those simulations practical in a way they weren't even three years ago.

The second is the synthetic data wall. Several major AI labs, including OpenAI and Anthropic, have quietly acknowledged that the supply of high-quality human-generated text for pre-training large language models is reaching a natural ceiling. Web crawls are increasingly polluted with AI-generated content that creates feedback loops rather than genuine information. RL-based systems that generate their own experience data sidestep this bottleneck entirely.

The third is a renewed debate about the limits of imitation. Critics of the current LLM paradigm have argued for years that systems trained to predict the next token can only ever approximate human intelligence — they cannot exceed the ceiling set by the data they were trained on. Reinforcement learning, at least in principle, has no such ceiling: AlphaGo surpassed every human Go player ever recorded, precisely because it wasn't imitating them.

London was a considered choice, not a default. Silver and his co-founders — DeepMind alumni Wojciech Czarnecki, Lasse Espeholt, and Junhyuk Oh — were based in the UK and wanted to remain there. The UK government, eager to establish itself as a leading destination for frontier AI research after years of watching talent drain to California, stepped in with backing through its newly established Sovereign AI fund. That fund, managed through the British Business Bank, is designed specifically to anchor high-potential AI labs in the country.

## The Investors' Bet

Sequoia's decision to co-lead the round at a $5.1 billion valuation for a company with no published models, no benchmarks, and no revenue reflects the VC giant's assessment of Silver himself as much as any specific technology thesis.

In a rare public statement, Sequoia partners described Ineffable as "a superlearner for the era of experience" and framed Silver's career as the execution of a single principle — that self-play and learning from experience scale further than imitation. The partnership noted that AlphaGo, AlphaZero, and AlphaFold were not separate achievements but steps along a single research trajectory that Silver has been following for his entire career.

Nvidia's participation is particularly notable. The chipmaker, which is simultaneously an investor in OpenAI, Anthropic, Mistral, and a dozen other frontier labs, rarely places bets this early. Its involvement signals both commercial interest — Silver's RL systems will presumably require enormous quantities of GPU compute — and a strategic desire to maintain relationships with any organization that might produce the next transformative AI capability.

Google's participation carries a different significance. Silver spent over a decade at Google's DeepMind division. That Google chose to invest in his new company rather than simply poaching him back suggests either that the terms of his departure were amicable enough to allow commercial cooperation, or that the search giant concluded that backing Ineffable was preferable to leaving Sequoia and Nvidia to capture the upside alone.

## What Comes Next

Ineffable Intelligence has no published roadmap and no announced benchmark targets. Investor briefings, according to sources familiar with the matter, anticipate first model results emerging in late 2026 — though Silver has explicitly declined to commit to a public release timeline.

The company will face genuine scientific challenges that no amount of capital can easily dissolve. Reinforcement learning has historically been brittle: systems that perform brilliantly in narrow, well-defined environments (game boards, protein structures) have struggled to generalize across open-ended tasks. The history of RL is littered with systems that achieved superhuman performance in their training environment and collapsed when the environment changed even slightly.

Silver's answer to this challenge — the "superlearner" architecture — is not yet publicly described in technical detail. The name and framing suggest a system designed to learn broadly, not narrowly, and to transfer knowledge across domains. Whether that ambition can be engineered into a working system remains one of the central open questions in AI research.

What is clear is that the AI industry's center of gravity has shifted. A year ago, the dominant paradigm was scale: larger language models, more tokens, bigger clusters. Today, a growing faction of the field — backed by $1.1 billion of institutional capital and the credibility of one of its most decorated researchers — is betting that the next breakthrough will come not from imitation at scale, but from experience.

---

*Silver described Ineffable as "my life's work" and said the world needs "a place where the full ambition of the reinforcement learning paradigm can flourish." That place, as of this week, is a newly minted, billion-dollar AI lab in London.*
