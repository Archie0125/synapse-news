---
title: "DeepSeek V4-Flash Beats Its Own Pro Model on Agent Benchmarks at One-Third the Price"
summary: "DeepSeek released V4-Flash-0731 on July 31, with its 284B mixture-of-experts model outscoring V4-Pro-Preview on every agentic test — including a 645% leap on DeepSWE — while charging just $0.28 per million output tokens. The MIT-licensed release redraws the cost-performance frontier for autonomous coding and tool-calling agents."
category: "ai-ml"
publishedAt: 2026-08-01
lang: "en"
featured: true
trending: true
sources:
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/322513/20260731/deepseek-retrained-v4-flash-beats-its-flagship-pro-nine-agent-benchmarks.htm"
  - name: "Caixin Global"
    url: "https://www.caixinglobal.com/2026-08-01/deepseek-releases-official-v4-flash-model-as-chinas-ai-race-intensifies-102470292.html"
  - name: "Digital Applied"
    url: "https://www.digitalapplied.com/blog/deepseek-v4-flash-0731-official-release-agent-benchmarks"
tags:
  - "DeepSeek"
  - "AI models"
  - "agentic AI"
  - "open-weight"
  - "LLM benchmarks"
  - "China AI"
relatedSlugs:
  - "2026-07-31-openai-gpt56-luna-80-percent-price-cut-en"
  - "2026-08-01-xai-grok-46-47-rapid-release-roadmap-en"
---

When DeepSeek published its V4-Flash-0731 changelog on the last day of July, the numbers looked almost too good to be true. A model that had been polling developers for weeks as the most-used on OpenRouter suddenly posted agent benchmark scores that beat DeepSeek's own Pro-grade flagship — at a price point one-third as expensive. Within hours, AI engineers were stress-testing the claims and rebuilding pipelines around the new build.

## What Changed — And What Didn't

The headline reveal is what DeepSeek explicitly chose *not* to change. V4-Flash-0731 carries the identical 284-billion-parameter, mixture-of-experts architecture that shipped in April's preview build: one shared expert plus 256 routed experts per layer, with six routed experts firing on any given token, activating just 13 billion parameters at inference time. The context window stays at one million tokens. Pricing is unchanged at $0.14 per million input tokens on a cache miss and $0.28 per million output tokens.

What changed is everything that comes after the architecture: the post-training stack. DeepSeek ran a new round of reinforcement learning and supervised fine-tuning specifically targeting tool-calling loops, multi-step reasoning, and long-horizon coding tasks. The company did not disclose the training compute used, the dataset composition, or whether any external human-preference data was involved — a pattern consistent with its approach since V3.

The result is a model that, by DeepSeek's own measurements, is now substantially better than the version it replaced, and better still than V4-Pro-Preview, the company's more expensive research-focused build.

## The Benchmark Numbers

DeepSeek published a four-benchmark comparison across three variants: V4-Flash Preview (April), V4-Flash-0731, and V4-Pro-Preview.

On **Terminal Bench 2.1**, a test measuring a model's ability to drive command-line workflows autonomously, V4-Flash-0731 scored 82.7 against V4-Pro-Preview's 72.1 and the previous Flash build's 61.8. That is a 34% improvement over the Pro variant on an externally-developed benchmark that tests genuine agentic behavior rather than question-answering.

On **DeepSWE** — a software-engineering agent evaluation that asks models to resolve real GitHub issues — the jump is staggering: from 7.3 in the April Flash Preview to 54.4 in the new build. V4-Pro-Preview sat at 12.8, making the Flash model now 4.25× better than the Pro on one of the most demanding open agent evaluations available. The company also reported **Cybergym** scores of 76.7 (vs. 52.7 for Pro) and **NL2Repo** at 54.2 (vs. 38.5 for Pro).

The caveats are real. All four benchmarks were run on DeepSeek's internal evaluation harness, which has not been released publicly. DSBench-FullStack and DSBench-Hard — two others mentioned in the technical blog — are entirely proprietary. As of the model's release date, no independent AI safety lab or external research group had reproduced any of these numbers. The company's track record on self-reported benchmarks has been solid, but audited verification is a different bar.

## Responses API and Codex Integration

Beyond raw task performance, V4-Flash-0731 ships with native support for the Responses API format that OpenAI standardized, along with specific adaptations designed for Codex-style agent loops. Developers can enable DSpark speculative decoding — DeepSeek's proprietary draft module that adds 20 billion parameters of draft inference capacity — with a single vLLM configuration flag, delivering measurably higher throughput on long-context outputs.

The model also unlocks up to 384,000 output tokens at high or maximum reasoning effort, relevant for agentic tasks that require generating extensive code, documentation, or multi-file diffs within a single call.

## Deployment Options and Licensing

DeepSeek has maintained an MIT license on V4-Flash, meaning commercial deployment — including building products on top of the weights — requires no royalties or usage agreements beyond standard API terms. For teams that want to self-host: the model needs approximately 110 gigabytes of memory in 3-bit quantization, or a cluster of four GB300 nodes at full BF16 precision. That hardware threshold is within reach of well-funded startups and enterprise infrastructure teams, but still out of range for individual researchers working on consumer hardware.

The API concurrency limit is set at 2,500 parallel requests — substantially higher than the preview build, a signal that DeepSeek has provisioned production-grade capacity for this release.

## Context: Company Trajectory

DeepSeek's timing here is notable. Just weeks before this release, Caixin Global confirmed that the Hangzhou-based lab had closed a funding round of approximately $7.4 billion, valuing it at 350 billion yuan (roughly $48 billion USD) with participation from Tencent and NetEase — the largest disclosed raise for a Chinese AI lab this cycle. The company has announced plans to double headcount and shift its product roadmap squarely toward AI agents rather than general-purpose assistants.

That strategic pivot explains the emphasis on agentic benchmarks in this release. DeepSeek isn't competing on raw reasoning scores against GPT-5.6 Sol or Claude Mythos; it's competing on the ability to run extended tool-calling workflows cheaply and at scale. At $0.28 per million output tokens, a developer can run tens of thousands of agent turns for the same budget that would buy a few hundred on top-tier models from OpenAI or Anthropic.

The model also arrives at a moment when Chinese AI labs face rising export uncertainty. Reuters reported last month that Beijing held consultations with Alibaba, ByteDance, and Z.ai about restricting overseas access to their most advanced models. DeepSeek's open-weight, MIT-licensed approach sidesteps that policy surface entirely: once the weights are downloadable, no export restriction can easily pull them back.

## What Developers Should Watch

The community response in the first 24 hours has been enthusiastic but measured. Several engineering teams have independently confirmed that the model's tool-calling reliability improved substantially from the April preview in informal evaluations, even if they haven't run the formal benchmarks DeepSeek published. The DeepSWE number, if it holds under independent audit, would represent a meaningful step change in what open-weight models can do on real software tasks.

V4-Pro remains available for teams whose workflows benefit from its longer chain-of-thought reasoning traces. But for agentic pipelines where throughput and cost matter — automated code review, CI-integrated agents, large-scale data extraction — V4-Flash-0731 has now become the default recommendation across several developer communities.

DeepSeek has not committed to a release timeline for V4-Pro's official version, which the company originally planned to launch alongside Flash. That upgrade is now expected in September or October 2026.
