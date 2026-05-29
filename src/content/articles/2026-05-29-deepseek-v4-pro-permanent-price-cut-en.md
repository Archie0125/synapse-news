---
title: "DeepSeek Makes Its 75% Price Cut on V4-Pro Permanent, Ratcheting Up the Global AI Pricing War"
summary: "DeepSeek has made the 75% promotional discount on its flagship V4-Pro model the permanent list price, dropping input costs to $0.435 per million tokens — roughly 100x cheaper than Claude Opus 4.7 on comparable tasks. The move arrives as four Chinese labs released competing open-weight coding models within a 12-day window, signaling a structural acceleration in the race to commoditize inference."
category: "ai-ml"
publishedAt: 2026-05-29
lang: "en"
featured: false
trending: true
sources:
  - name: "The Next Web"
    url: "https://thenextweb.com/news/deepseek-v4-pro-price-cut-75-percent"
  - name: "InfoWorld"
    url: "https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html"
  - name: "US News & World Report"
    url: "https://money.usnews.com/investing/news/articles/2026-05-23/chinas-deepseek-to-make-permanent-75-price-cut-on-flagship-v4-pro-ai-model"
  - name: "DeepSeek API Docs"
    url: "https://api-docs.deepseek.com/quick_start/pricing"
tags:
  - "deepseek"
  - "ai-pricing"
  - "llm"
  - "api"
  - "china"
  - "inference"
  - "developer-tools"
relatedSlugs:
  - "2026-05-26-cursor-composer-25-kimi-k25-coding-agent-en"
  - "2026-05-27-open-weight-ai-guardrails-heretic-abliteration-en"
  - "2026-05-23-openai-q1-2026-revenue-57b-codex-losses-en"
---

On May 22, 2026, DeepSeek announced that the 75% promotional discount on its DeepSeek-V4-Pro API — originally scheduled to expire on May 31 — would not roll back. What began as a developer acquisition play has become the company's permanent pricing strategy, and the implications for the global AI inference market are significant.

The new permanent rates: **$0.435 per million input tokens**, **$0.87 per million output tokens**, and **$0.003625 per million cached tokens** — the last figure representing a tenth of previous cache pricing across DeepSeek's entire API suite. Compare those numbers to Claude Opus 4.7's $5/$25 per million input/output tokens, or GPT-5's mid-tier pricing, and the order-of-magnitude gap is not a rounding error. For cost-sensitive workloads running at scale — legal document review, code analysis pipelines, enterprise data extraction — developers are being offered frontier-class capability at prices that would have seemed satirical eighteen months ago.

## What V4-Pro Actually Is

To understand what the pricing cut means, you need to understand the model. DeepSeek-V4-Pro is a **1.6 trillion parameter Mixture-of-Experts (MoE) architecture** that activates approximately 49 billion parameters per forward pass. That distinction matters enormously for inference economics: the model carries the knowledge capacity of a 1.6T parameter network but burns compute like a much smaller 49B dense model on most queries.

The context window is **one million tokens by default** — a critical differentiator for enterprise use cases involving large codebases, lengthy legal contracts, or extensive document repositories. DeepSeek achieved this long-context capability through a novel combination of Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA), which requires only 27% of the per-token FLOPs that its predecessor DeepSeek-V3.2 needed at 1M context length, and 10% of the KV-cache memory.

On benchmarks, V4-Pro posts **80.6% on SWE-bench Verified** (the software engineering evaluation considered the most reliable proxy for real-world coding tasks) and **93.5 on LiveCodeBench**. For retrieval in very long contexts, V4-Pro-Max scores 83.5% on MRCR 1M, surpassing Gemini 3.1-Pro on that specific long-context benchmark. Independent NIST CAISI evaluations characterize V4-Pro's capabilities as lagging the frontier by approximately 8 months — but also note that it is more cost-efficient than comparable U.S. models on 5 of 7 evaluated benchmarks.

That combination — near-frontier coding capability, 1M context, MoE inference efficiency — is precisely why the 75% price cut lands differently than generic price competition.

## The 12-Day Chinese Model Surge

DeepSeek's pricing announcement didn't land in isolation. In the twelve days straddling the May 22 announcement, four Chinese labs released competing open-weight frontier coding models: Z.ai's GLM-5.1, MiniMax's M2.7, Moonshot AI's Kimi K2.6, and DeepSeek V4 itself. All four hit roughly the same capability ceiling on agentic engineering benchmarks while offering inference costs meaningfully below Western frontier models.

This coordinated — or rather convergent — release wave represents a structural shift in how Chinese AI labs are competing. Where the original DeepSeek-V3 release in January 2025 felt like a surprise attack, the current pattern looks more like a sustained industrial strategy: parallel teams racing to the capability frontier with efficiency optimization as a differentiator, compressing pricing to drive API adoption before revenue monetization of enterprise accounts.

The model quality gap between the Chinese frontier and Western frontier has narrowed substantially. V4-Pro at 80.6% SWE-bench sits below Claude Opus 4.7 and GPT-5 on the same benchmark, but close enough that for the 90% of real-world coding tasks that don't require absolute state-of-the-art reasoning, the cost differential matters more than the benchmark differential.

## What This Does to Western Labs' Business Models

The permanent price cut lands at a genuinely awkward moment for Anthropic, OpenAI, and Google. All three have built revenue forecasts on an implicit assumption that enterprise AI pricing could sustain current levels long enough to fund the next generation of model training. DeepSeek's move challenges that assumption in two ways.

First, it directly compresses the addressable market for high-volume, cost-sensitive inference workloads that Western labs have been pricing at levels roughly comparable to their compute costs plus a margin. Enterprise developers with mature production pipelines evaluating their Q3 API costs have new options that were not available six months ago.

Second, it accelerates the commoditization narrative that is structurally uncomfortable for any business model built on selling intelligence-as-a-service. If inference prices continue declining at the rate of the past 18 months — roughly a 70-80% annual decline in cost per token on comparable capability — the sustainable moats will increasingly be about proprietary data, unique integrations, and trust rather than raw model capability.

Anthropic's position in this dynamic is nuanced. The company's revenue growth ($45B+ annualized) suggests it is successfully selling something beyond raw inference at commodity rates — its enterprise integrations, Constitutional AI trust advantages, and managed agent orchestration capabilities all command premiums that pure API pricing comparisons miss. OpenAI faces similar dynamics but with a larger portion of its revenue tied to consumer ChatGPT subscriptions, which are partly insulated from raw API pricing pressure.

## The Cache Hit Footnote That Deserves More Attention

The most underreported element of DeepSeek's announcement is the permanent reduction in cache-hit pricing across its entire API suite to **one-tenth of previous levels**. Cache hits matter because in production AI applications — conversational systems that maintain context across sessions, RAG pipelines that repeatedly access the same knowledge base chunks, coding assistants that operate over the same codebase — a large fraction of inference volume is served from cache rather than computed from scratch.

At $0.003625 per million cached tokens, DeepSeek is effectively making cached inference nearly free. For production applications with high cache-hit rates — which experienced developers design for explicitly — effective per-query costs drop dramatically below even the headline input price. A developer running a coding assistant over a 500,000-token codebase context who achieves 70% cache hit rate is paying per-query economics that would have been impossible to budget at any Western provider's prices.

## The Regulatory Complexity

No analysis of DeepSeek pricing can ignore the regulatory dimension. The NIST CAISI evaluation framework has reviewed V4-Pro, and the model is currently available to U.S. developers without restriction. But the China AI talent export controls that became visible in May 2026 — and the broader context of U.S.-China technology decoupling — create a long-term availability risk that any enterprise architect building critical infrastructure on DeepSeek's API must factor into their roadmap.

Some enterprises are already responding by running open-weight versions of DeepSeek models on their own infrastructure — either on-premise or in U.S.-based cloud — rather than using the hosted API. DeepSeek releases its models with weights publicly available, which means the pricing signal is about hosted API competition while the technology itself is accessible regardless of geopolitical developments.

For the broader AI industry, the permanent 75% price cut is less a pricing event than a market structure event. It establishes a new floor that competitors cannot ignore, and it does so at a capability level that makes the floor credible for a substantial portion of real enterprise workloads. The pricing war Satya Nadella and Sam Altman both alluded to in various earnings calls over the past year is no longer a future scenario. It is the present reality.
