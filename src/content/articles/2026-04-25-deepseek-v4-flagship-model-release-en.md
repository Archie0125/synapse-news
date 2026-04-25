---
title: "DeepSeek V4 Arrives: 1.6 Trillion Parameters, $0.28 Output Tokens, and a Direct Challenge to the West"
summary: "China's DeepSeek has released its most powerful AI model yet — V4 — in two variants: a flagship Pro model with 1.6 trillion total parameters and a lean Flash variant priced at just $0.28 per million output tokens. The release marks one year since DeepSeek first shocked Silicon Valley, and signals that Chinese AI development has not slowed."
category: "ai-ml"
publishedAt: 2026-04-25
lang: "en"
featured: true
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/24/deepseek-v4-llm-preview-open-source-ai-competition-china.html"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-04-24/deepseek-unveils-newest-flagship-a-year-after-ai-breakthrough"
  - name: "Fortune"
    url: "https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/"
  - name: "MIT Technology Review"
    url: "https://www.technologyreview.com/2026/04/24/1136422/why-deepseeks-v4-matters/"
  - name: "DeepSeek API Docs"
    url: "https://api-docs.deepseek.com/news/news260424"
tags:
  - "DeepSeek"
  - "LLM"
  - "open-source"
  - "China AI"
  - "Mixture of Experts"
  - "Huawei"
relatedSlugs:
  - "2026-04-25-cohere-aleph-alpha-merger-sovereign-ai-en"
  - "2026-04-25-openai-25b-revenue-ipo-plans-en"
  - "2026-04-24-openai-gpt-5-5-agentic-model-en"
---

Exactly one year after DeepSeek's R1 reasoning model sent shockwaves through Silicon Valley — triggering a $600 billion single-day wipeout in Nvidia's market cap — the Chinese AI startup has returned with its most capable model to date. DeepSeek V4, released in preview on April 24, 2026, arrives in two variants and reasserts the company's position at or near the frontier of large language model development.

The release carries competitive weight far beyond its benchmarks. In a global AI race where the United States has imposed sweeping chip export restrictions on China and European governments are rethinking AI sovereignty, DeepSeek's continued progress on a fraction of Western compute budgets is a direct challenge to the assumption that frontier AI requires frontier hardware spending.

## Two Models, One Architecture

DeepSeek V4 ships as two distinct models. **V4-Pro** is the flagship: a 1.6 trillion total-parameter Mixture of Experts (MoE) architecture with 49 billion parameters active per inference pass. **V4-Flash** is a smaller, faster variant at 284 billion total parameters with 13 billion active, designed for latency-sensitive and cost-sensitive applications.

Both models share a 1,048,576-token context window — one million tokens — allowing entire codebases, lengthy legal contracts, or multi-volume research corpora to be processed in a single prompt. That context length matches or exceeds what OpenAI and Anthropic currently offer at full quality levels.

The headline architectural innovation is what DeepSeek calls the **Hybrid Attention Architecture** (HAA). Traditional transformer attention scales poorly across extremely long contexts, creating a well-known performance degradation problem. HAA addresses this by alternating between different attention mechanisms at different layers, allowing the model to maintain coherent recall across its full context window without the quadratic compute cost of pure dense attention. The result, according to DeepSeek's technical documentation, is meaningfully better long-context memory — particularly relevant for coding agents and document analysis workflows that need to track state across many thousands of lines.

## Pricing That Resets Expectations

DeepSeek has again used pricing as a weapon. V4-Pro costs **$3.48 per million output tokens** via the DeepSeek API. V4-Flash costs just **$0.28 per million output tokens**. For comparison, OpenAI's o3 model runs at roughly $60 per million output tokens for its full reasoning mode, and even GPT-4.1 sits at $8 per million. Anthropic's Claude Sonnet 4.6 is priced at $15 per million output tokens.

At $0.28 per million tokens, V4-Flash is cheaper than sending a postcard. For developers building high-throughput applications — customer service bots, document processors, code review pipelines — the economics are transformative. Even V4-Pro at $3.48 undercuts most comparable Western frontier models by a factor of two to five.

DeepSeek achieves these prices through the MoE architecture, which dramatically reduces active compute per token, and through what appears to be exceptionally efficient training runs. The company has not disclosed its training costs for V4, but its prior models have been trained for a fraction of what comparable U.S. labs spend.

## Open Source and Huawei Integration

Both V4 variants are released as open-weight models, available for download and fine-tuning on Hugging Face. This continues DeepSeek's tradition of open releases that have repeatedly seeded new research and derivative models across the global AI community.

More geopolitically notable is the model's close integration with **Huawei's Ascend AI chips**. U.S. export controls have effectively cut off Chinese AI labs from NVIDIA H100 and H200 GPUs. Rather than stalling, DeepSeek appears to have adapted — optimizing V4 for Huawei's domestic alternative. The Ascend 910C, Huawei's current flagship AI accelerator, still trails NVIDIA's best hardware on raw throughput, but V4's efficiency-focused architecture narrows that gap considerably.

This detail matters beyond DeepSeek itself. It demonstrates that U.S. chip restrictions, while impactful, have not succeeded in preventing frontier model development in China — they have instead accelerated domestic chip optimization.

## Benchmark Performance

DeepSeek has positioned V4-Pro as near-frontier on coding, mathematics, and reasoning tasks. On internal benchmarks, the company claims V4-Pro outperforms GPT-4.1 on several coding evaluations and matches or exceeds Gemini 3.1 Pro on multi-step reasoning tasks. Independent evaluators on platforms like Chatbot Arena have begun placing V4-Pro in the top five globally, though comprehensive third-party benchmark results are still emerging.

V4-Flash, despite its dramatically smaller active parameter count, reportedly performs comparably to GPT-4o-mini and Gemini 3.1 Flash on most standard evaluations — a ratio of price-to-performance that will be difficult for Western providers to match.

## The Geopolitical Subtext

This release lands in a charged context. Chinese regulators have recently been scrutinizing foreign investment in domestic AI companies including Moonshot AI, StepFun, and ByteDance. Meanwhile, U.S. policymakers are debating further tightening of the chip export regime. DeepSeek operates in this environment as something of an anomaly: a Chinese AI lab that remains largely open, internationally accessible, and technologically credible.

The one-year anniversary framing is deliberate. When DeepSeek R1 dropped in January 2025, the immediate assumption in Western AI circles was that it represented a one-time disruption — clever engineering of an existing paradigm, not a sustained capability trajectory. V4's release challenges that assumption. The company has shipped V2, V3, R1, and now V4 in roughly eighteen months, each meaningfully more capable than the last.

## What This Means for Enterprise Adopters

For CTOs and AI leads evaluating model providers, V4's release opens practical questions. V4-Flash's price point makes it compelling for any application currently using GPT-4o-mini or Gemini Flash — the cost savings are too large to ignore. V4-Pro enters serious consideration for workloads where model quality is paramount and data residency requirements permit use of DeepSeek's API.

The persistent concern is reliability and enterprise support. DeepSeek's API infrastructure, while significantly more robust than it was a year ago, still has occasional availability issues under peak demand. For mission-critical enterprise deployments, many organizations will want to run open-weight versions on their own infrastructure — which the open-source release makes possible.

The message from Hangzhou is clear: the AI race remains wide open, the cost curve is still dropping, and Western providers cannot take their lead for granted.
