---
title: "China's Moonshot AI Drops Kimi K3: The World's Largest Open-Weight Model at 2.8 Trillion Parameters"
summary: "Moonshot AI has released Kimi K3, a 2.8-trillion-parameter open-weight Mixture-of-Experts model that rivals GPT-5.5 and Claude Opus 4.8, with a 1-million-token context window and full weights shipping July 27. It is the largest open-source AI model ever released, marking a major milestone for China's AI industry and the global open-source community."
category: "ai-ml"
publishedAt: 2026-07-17
lang: "en"
featured: true
trending: true
sources:
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html"
  - name: "Fortune"
    url: "https://fortune.com/2026/07/16/moonshots-kimi-k3-pushes-chinese-ai-into-fable-level-territory/"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/07/16/moonshot-ai-releases-kimi-k3-a-2-8-trillion-parameter-open-moe-model-with-kimi-delta-attention-and-1m-context/"
tags:
  - "open-source"
  - "moonshot-ai"
  - "kimi-k3"
  - "mixture-of-experts"
  - "china-ai"
  - "large-language-models"
relatedSlugs:
  - "2026-07-16-google-gemini-35-pro-launch-en"
  - "2026-07-05-meta-watermelon-model-gpt55-parity-en"
---

On July 16, 2026, Beijing-based Moonshot AI quietly reshuffled the global frontier AI leaderboard. The company released Kimi K3 — a 2.8-trillion-total-parameter open-weight Mixture-of-Experts model with a 1-million-token context window — and announced that the full model weights will be made publicly available on July 27 under a permissive open license. Independent benchmarks from Artificial Analysis place its performance squarely alongside OpenAI's GPT-5.5 and Anthropic's Claude Opus 4.8, particularly on complex multi-step reasoning and agentic workflows.

For anyone tracking where the AI frontier actually lives, this is a landmark moment. No open-weight model has come close to this scale before, and no Chinese AI lab has ever shipped something that independent evaluators place in the same tier as the best American closed models.

## What Kimi K3 Actually Is

Kimi K3 is a sparse Mixture-of-Experts architecture built on two novel components Moonshot developed internally. The first is Kimi Delta Attention, which the company's researchers describe as a memory-efficient variant of standard multi-head attention that reduces the quadratic cost of processing long contexts by computing attention only on changes between token representations rather than on all tokens simultaneously. The second is Attention Residuals, a technique that blends attention outputs across transformer layers so information can shortcut to later stages without passing through all intermediate computation — reducing depth without sacrificing model quality on long-horizon tasks.

In concrete terms: the model has 2.8 trillion total parameters arranged across 896 experts, of which 16 are activated per token during inference. This is the same fundamental trade-off that makes MoE models computationally feasible — you build a huge model but only use a slice of it for any given input, keeping actual compute costs manageable. The 1-million-token context window is the longest in any production-ready open-weight model by a significant margin.

Two variants shipped at launch. K3 Max is optimized for single-user chat and standard agentic tasks. K3 Swarm Max is designed for large-scale parallel processing — running many agents simultaneously against different parts of a problem — which Moonshot envisions as the architecture for complex enterprise workflows like code refactoring across large repositories or multi-step scientific literature review.

## Performance at the Top of the Open Leaderboard

The benchmarks tell a specific story. On MMLU-Pro, GPQA Diamond, and LiveCodeBench — the evaluations most commonly used to separate frontier models — Kimi K3 lands within one to two percentage points of GPT-5.5 and Claude Opus 4.8. It outperforms both on certain long-document reasoning tasks, which is consistent with its architectural emphasis on efficient attention over million-token inputs.

Moonshot's own internal testing shows K3 achieving 76.4 on GPQA Diamond (compared to GPT-5.5's reported 77.1), 85.2 on MATH-500, and a 67.8 on SWE-bench Verified — a widely watched coding benchmark that measures a model's ability to resolve real GitHub issues. That last number places it roughly on par with Claude Sonnet 5 on agentic coding, though still below Claude's best-performing coding-specialist configurations.

What the numbers don't capture is the qualitative shift: this is the first time a fully open-weight model can credibly claim to participate in the same conversation as the closed frontier. That changes what developers, researchers, and enterprises can actually build without signing terms-of-service agreements or routing data through third-party APIs.

## API First, Weights Later

Kimi K3 launched on the Kimi Code developer platform and inside the Kimi consumer app on July 16, with API pricing set at $3 per million input tokens and $15 per million output tokens — slightly higher than Claude Sonnet-tier pricing but below Opus 4.8. Web search grounding is billed at $0.015 per call. The pricing puts it in premium-but-accessible territory for developers building agents that need long-context reasoning.

The full open weights arrive July 27. That two-week gap between API availability and weight release is deliberate: Moonshot wants to establish the API as the primary commercial surface before the open-source community begins running the model on private infrastructure. Once weights ship, the calculus changes — enterprises and researchers can deploy Kimi K3 on their own hardware, train derivative models, and integrate it into pipelines without API dependency.

The weights are being released under a permissive license, though Moonshot has not specified the exact terms beyond confirming that commercial use will be allowed.

## Why This Matters for the Competitive Landscape

DeepSeek's V3 and R2 releases earlier in 2026 established that Chinese AI labs could match American frontier models on certain tasks while open-sourcing the result. Kimi K3 extends that pattern in a different direction: pure scale. Where DeepSeek competed on cost efficiency and mathematical reasoning, Moonshot is competing on capability breadth and context length.

The strategic logic for Moonshot is clear. The company generates revenue from the Kimi consumer app and Kimi Code developer platform, both of which run on proprietary infrastructure. Open-sourcing the weights builds a developer community, drives API adoption, and establishes Kimi K3 as a default baseline for enterprise AI teams evaluating frontier models — particularly in markets where data sovereignty concerns make American closed models difficult to adopt.

For the broader industry, this represents a maturation of the open-weight ecosystem that few expected to arrive this quickly. Eighteen months ago, the gap between open-weight and closed frontier models was widely assumed to be structural — a function of the resource advantages that only a handful of companies could marshal. Kimi K3's release challenges that assumption in a concrete way that previous open-weight releases didn't.

## The Geopolitical Subtext

The timing — the same week as the 2026 World Artificial Intelligence Conference in Shanghai, where President Xi Jinping personally attended and called AI "a symphony of global cooperation" — is unlikely to be coincidental. Moonshot AI is Beijing-based, founder Yang Zhilin trained at Carnegie Mellon and was a Google researcher before returning to China, and Kimi K3 is now cited by China's state media as evidence that domestic AI development has reached parity with American systems.

The US export control regime has, to date, restricted China's access to the highest-end training chips. Moonshot has not disclosed the specific hardware stack used to train K3, but the company has operated within the constraints of available domestic and older-generation NVIDIA silicon. If the benchmarks hold under independent scrutiny — and the early signs suggest they will — the policy argument that chip restrictions prevent China from reaching frontier AI capability will need serious revision.

For Western AI labs, the immediate practical question is what Kimi K3 means for the open-weight competitive landscape when its weights are fully available on July 27. The answer is almost certainly: a significant acceleration of fine-tuning, distillation, and derivative model development, concentrated in the research and enterprise communities that most directly compete with closed-model providers.

The model is available now via the Kimi API, and developers should expect a busy two weeks until the weights land.
