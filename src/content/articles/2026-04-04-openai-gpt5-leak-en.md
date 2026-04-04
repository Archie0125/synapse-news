---
title: "GPT-5 Benchmarks Leaked — And They Tell a Very Different Story Than OpenAI Wants"
summary: "Internal benchmark results suggest GPT-5's improvements are narrower than expected. The era of 'just scale it up' might officially be over, and that's actually good news for the industry."
category: "ai-ml"
publishedAt: 2026-04-04
lang: "en"
featured: false
trending: true
sources:
  - name: "The Information"
    url: "https://www.theinformation.com"
  - name: "Semianalysis"
    url: "https://www.semianalysis.com"
  - name: "AI Twitter / X"
    url: "https://x.com"
tags:
  - "openai"
  - "gpt-5"
  - "scaling-laws"
  - "benchmarks"
  - "llm"
relatedSlugs:
  - "2026-04-04-apple-ai-strategy-shift-en"
---

## The Leak Nobody at OpenAI Wanted

A set of internal benchmark results, reportedly from OpenAI's GPT-5 evaluation runs, surfaced on a research forum this week before being hastily taken down. Multiple credible sources have since corroborated the key findings.

The numbers are interesting — but not for the reason you'd expect.

## What the Benchmarks Actually Show

According to the leaked data:

- **Coding (HumanEval+)**: GPT-5 scores 94.2%, up from GPT-4's 86.6%. Solid improvement, but not the generational leap that GPT-3→4 represented.
- **Reasoning (ARC-AGI-2)**: 71.8%, compared to GPT-4's 55.3%. Genuine progress, but still below what Claude Opus and Gemini Ultra achieve in specialized configs.
- **Math (MATH-500)**: 96.1% — essentially the ceiling. GPT-4 was already at 92.4%.
- **Creative writing**: Human evaluators rated GPT-5 outputs only 4% higher than GPT-4 in blind tests. Barely distinguishable.
- **Multilingual tasks**: This is the real surprise — GPT-5 shows 15-20% improvements in low-resource languages. This is where the compute actually went.

## The Scaling Wall Is Real

Here's what this data actually means: **the pre-training scaling paradigm has reached diminishing returns for English-language tasks.**

OpenAI reportedly burned through 35,000 H100-equivalents for GPT-5 training — roughly 3x the compute of GPT-4. For that investment, they got single-digit percentage improvements on most benchmarks.

This isn't failure. This is physics. When you're already at 90%+ on a benchmark, the remaining points cost exponentially more compute to squeeze out. The interesting question is what happens next.

## Why This Is Actually Good News

The end of "just make it bigger" forces the industry into more creative territory:

1. **Specialization over generalization** — Instead of one massive model that's okay at everything, expect families of smaller, domain-specific models that are extraordinary at specific tasks.

2. **Post-training becomes king** — The real gains are now in RLHF, tool use, agentic capabilities, and inference-time compute. The base model is just the starting point.

3. **Infrastructure matters more** — If raw model performance plateaus, the winners will be whoever builds the best surrounding infrastructure: memory, tool integration, reliability, latency.

4. **Open-source closes the gap** — When the frontier isn't moving as fast, open-source models can catch up. Llama 4 and Mistral Large are already competitive with GPT-4 on many tasks.

## The Real Competition Now

The AI race is shifting from "who has the smartest model" to "who has the most useful system." That's a fundamentally different competition — one where Apple's on-device play, Anthropic's safety-focused approach, and Google's integration advantage all become more relevant.

OpenAI built the cathedral. Now everyone's building the city around it.

## What to Watch

- OpenAI's official GPT-5 announcement (expected May/June) — watch for how they frame the narrative
- Whether they lean into specialization or double down on scale
- Anthropic's response (Claude 5?) and whether they take a different architectural approach
- The open-source community's reaction — this data validates the "small models + good post-training" thesis

*The scaling wall isn't the end of AI progress. It's the end of the easy part. What comes next will be harder, messier, and ultimately more interesting.*
