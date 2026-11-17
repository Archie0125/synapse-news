---
title: "Cursor's Composer 2.5 Comes Close to Frontier Models at 1/10th the Per-Token Price — Built on Chinese Open-Source AI"
summary: "Cursor shipped Composer 2.5 on May 18, a coding agent built on Moonshot AI's open-source Kimi K2.5 checkpoint that scores 79.8% on SWE-Bench Multilingual — close to Claude Opus 4.7's 80.5% — at roughly one-tenth the per-token price. The launch raises questions about the future of expensive frontier model pricing in developer tools."
category: "developer-tools"
publishedAt: 2026-05-26
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "Winbuzzer"
    url: "https://winbuzzer.com/2026/05/18/cursor-releases-composer-25-saying-its-better-at-s-xcxwbn/"
  - name: "Build Fast With AI"
    url: "https://www.buildfastwithai.com/blogs/cursor-composer-2-5-review-2026"
  - name: "Startup Fortune"
    url: "https://startupfortune.com/cursor-makes-composer-25-a-cheaper-rival-for-coding-agents/"
  - name: "Digital Applied"
    url: "https://www.digitalapplied.com/blog/cursor-composer-2-5-agent-coding-launch"
tags:
  - "Cursor"
  - "AI-coding"
  - "Kimi"
  - "Moonshot-AI"
  - "developer-tools"
  - "agentic-coding"
  - "open-source"
relatedSlugs:
  - "2026-05-11-spacex-cursor-60b-acquisition-en"
  - "2026-05-04-kimi-k26-open-source-coding-benchmark-en"
---

When Cursor shipped Composer 2.5 on May 18, the announcement appeared, on its surface, to be a routine model update: a new release with improved benchmarks and a promotional pricing period. The technical details told a different story.

Composer 2.5 achieves 79.8% on SWE-Bench Multilingual and 63.2% on CursorBench v3.1, Cursor's internal evaluation suite for coding agent tasks. On SWE-Bench Multilingual, those numbers put it close to Claude Opus 4.7 (80.5%) and ahead of GPT-5.5 (77.8%), though GPT-5.5 remains well ahead on Terminal-Bench 2.0.

The price gap is not within statistical noise. Composer 2.5's standard tier is $0.50 per million input tokens and $2.50 per million output tokens. Claude Opus 4.7 is priced at $5 per million input tokens and $25 per million output tokens, while GPT-5.5 is $5 for input and $30 for output. Composer 2.5 on the standard tier costs approximately ten times less.

The model it is built on is Kimi K2.5 — an open-source checkpoint from Moonshot AI, a Chinese AI startup.

## How Cursor Got Here

The architecture of Composer 2.5 reflects a maturing understanding of what coding-specific AI actually requires. Cursor's team did not take Kimi K2.5's open weights and release them as-is. The training pipeline applied three targeted modifications over the base model:

**Textual feedback reinforcement learning.** Rather than providing reward signals only at the end of a coding session — did the code work? — Cursor's training pipeline inserted localized feedback at the specific trajectory points where the model could have made a better decision. A bad tool call, an incorrectly interpreted requirement, a redundant file read: each of these now receives targeted correction during training rather than being diluted into an end-of-task reward. The feedback is inserted at the exact decision points where the model went off-trajectory, rather than scoring only the final outcome.

**25x synthetic task scale.** Composer 2.5 was trained on approximately 25 times more synthetic coding tasks than its predecessor. Crucially, these include what Cursor calls "feature deletion" rebuild puzzles — tasks where the model must understand a working codebase well enough to reconstruct a removed feature from the surrounding context. This trains a form of deep comprehension that standard code generation benchmarks do not directly measure.

**Mixture-of-Experts infrastructure.** The model uses a sharded Muon optimizer and dual-mesh Hybrid Sharded Data Parallelism training setup, enabling more efficient training of MoE-scale architectures that maintain low per-token inference costs even at competitive capability levels.

## The Kimi K2.5 Foundation

Moonshot AI's open release of Kimi K2.5 made Composer 2.5 possible in a way that would not have been true 18 months ago. The availability of a capable open-weights foundation model that Cursor could fine-tune on proprietary coding data, with targeted RL improvements, at inference costs that make commercial deployment viable — this is the open-source strategy bearing fruit in ways its advocates predicted.

K2.5 is a Mixture-of-Experts model with roughly 1 trillion total parameters and about 32 billion active per inference. Chinese open-source models have been tracking closely behind frontier proprietary models in raw benchmark performance while maintaining significantly lower inference cost profiles, and K2.5 represents one of the cleaner examples of this pattern.

The practical implication for Cursor: a Chinese open-source checkpoint, combined with Cursor's extensive proprietary post-training, produced a model that comes close to the most expensive models on several coding benchmarks — at a fraction of the per-token price.

## What This Means for the Frontier Licensing Model

The AI coding tools market is currently undergoing a structural pricing shift. Anthropic and OpenAI continue to price their frontier models for general enterprise use cases that implicitly include developers. The implicit assumption has been that coding agents require frontier-class general intelligence and must therefore be priced at frontier rates.

Composer 2.5 challenges that assumption. If a purpose-built, task-specialized model can achieve frontier coding performance at roughly one-tenth the inference cost, the premium attached to general frontier models in developer tools begins to look like a market inefficiency rather than a justified premium.

This does not make frontier models irrelevant in coding. There are tasks — architectural reasoning about novel systems, security review of complex codebases, debugging highly obscure edge cases — where general intelligence and broad training data may matter in ways that benchmark scores do not capture. But for the bread-and-butter work of coding agents — understanding requirements, reading existing code, writing correct implementations, running test suites, debugging outputs — the specialized model is increasingly competitive.

The broader pattern, as tools like Composer 2.5 mature, is that the AI layer in developer tooling may commoditize faster than the AI model vendors anticipated. The value may concentrate in the user interface, the context management system, the integration with development environments, and the proprietary datasets derived from actual developer usage — all layers where Cursor has accumulated significant advantages.

## The Colossus 2 Roadmap

Composer 2.5 is not Cursor's final model bet. The company disclosed in the May 18 announcement that it is co-training a significantly larger model with SpaceXAI using approximately 10 times the total compute of the current release, running on Colossus 2's million H100-equivalent processors.

Cursor is working with SpaceXAI, and SpaceX reportedly holds a $60 billion acquisition option on Cursor.

No release date has been disclosed for the resulting model. If it clears the same performance-per-dollar hurdle at a higher absolute capability level, it would represent a more significant disruption to the existing frontier model economics in developer tools — and a test of whether the Cursor-xAI combination can compound the efficiency advantage that Composer 2.5 has demonstrated.

For developers who have grown accustomed to treating Claude or GPT as the default intelligence layer in their tools, the message from Cursor is increasingly clear: the intelligence is becoming cheaper faster than you might think, and the value is being built elsewhere.

*Correction (November 15, 2026): 13 sentences were corrected or removed to match the sources listed on this page.*
