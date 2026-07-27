---
title: "DeepSeek V4 Hits General Availability, Setting an Open-Source Price Floor at $0.87 Per Million Tokens"
summary: "After a three-month preview period, DeepSeek V4 has reached full general availability with 80.6% SWE-bench performance at pricing 28x cheaper than Claude Opus 4.8. Combined with Kimi K3's open-weight release, the final week of July marks the most consequential stretch for open-source AI in 2026."
category: "ai-ml"
publishedAt: 2026-07-27
lang: "en"
featured: false
trending: true
sources:
  - name: "DeepSeek V4 Benchmarks — BenchLM"
    url: "https://benchlm.ai/models/deepseek-v4-pro"
  - name: "DeepSeek V4 Complete Guide"
    url: "https://codersera.com/blog/deepseek-v4-complete-guide-2026/"
  - name: "DeepSeek V4 General Availability"
    url: "https://tech-insider.org/au/deepseek-v4-general-availability-2026/"
  - name: "DataCamp DeepSeek V4"
    url: "https://www.datacamp.com/blog/deepseek-v4"
tags:
  - "deepseek"
  - "open-source"
  - "llm"
  - "benchmarks"
  - "pricing"
  - "swe-bench"
  - "inference"
relatedSlugs:
  - "2026-07-10-deepseek-v4-api-migration-july24-deadline-en"
  - "2026-07-26-kimi-k3-open-weights-self-hosting-en"
  - "2026-07-20-deepseek-71b-valuation-ipo-2026-en"
---

Three months after its preview launch, DeepSeek V4 has reached full general availability—and with it, the Chinese AI lab has established a pricing floor that will force every frontier model provider to justify their rates anew. The timing, coinciding almost exactly with Moonshot's release of Kimi K3's open weights on July 27, makes the final week of July the most consequential stretch for open-source AI in 2026.

## What V4 Brings to the Table

DeepSeek V4 comes in two variants built around mixture-of-experts architecture. V4-Pro uses 1.6 trillion total parameters, of which only 49 billion are active at inference time—the sparse activation is what makes the model computationally tractable despite its enormous theoretical scale. V4-Flash, the lighter option, totals 284 billion parameters with 13 billion active. Both models support a 1-million-token context window with a maximum output of 384,000 tokens.

On benchmarks, V4-Pro's highest-performing configuration—V4-Pro-Max—achieves 80.6% on SWE-bench Verified, the software engineering task suite that has become one of the most credible proxies for real-world coding ability. That score ties Gemini 3.1 Pro for the top position among open-weights models, and meaningfully exceeds the 75% range typically associated with strong GPT-4-class systems. The leap from the previous DeepSeek generation to V4 on this benchmark is roughly 7 to 8 percentage points—a significant single-generation gain.

## The Price Floor

Pricing is where V4 makes its most aggressive argument to the market. V4-Pro via DeepSeek's API costs $0.435 per million input tokens and $0.87 per million output tokens. V4-Flash costs $0.14 input and $0.28 output per million tokens. By comparison, Claude Opus 4.8—before Claude Opus 5 replaced it—was priced at approximately $15 input and $75 output. V4-Pro is 28.7 times cheaper per output token than Opus 4.8, and more than 86 times cheaper than Opus 4.8 on output.

These are not small differences. For enterprises running at scale—legal document review, code generation, data extraction, customer service automation—the cost gap between a V4-Pro deployment and a Claude or GPT-4-class deployment can run to millions of dollars annually. V4 pricing creates a forcing function: API providers serving cost-sensitive workloads must either match these rates, specialize their offerings in ways that justify a premium, or watch enterprise budget holders choose the cheaper option.

The old DeepSeek API endpoints—running on prior model generations—were shut down on July 24 as part of the official migration to V4. Users who had not yet migrated faced brief service interruptions, which produced short-lived complaints on developer forums before the transition completed. The migration deadline had been announced two weeks earlier, giving developers adequate warning.

## The Three-Month Journey to GA

DeepSeek released V4's preview on April 24, 2026, as a technical preview with limited capacity and some availability constraints. During the three-month preview period, the company gathered real usage data, tuned safety filters for production workloads, resolved reliability issues under genuine load, and validated that the inference infrastructure could handle the volume required for enterprise SLA commitments.

The GA transition in the July 20-24 window brought full production-level SLA commitments—the kind of uptime guarantees that enterprise procurement teams require before they can put a model in a production pipeline. It also brought the stable API endpoint naming that allows customers to integrate once and not worry about version migrations breaking their code, and expanded capacity across DeepSeek's inference infrastructure.

## A Week That Rewrites the Map

The simultaneous nature of V4's GA arrival and Kimi K3's open-weight release has created an unusual market moment. In the same week:

- DeepSeek V4-Pro-Max achieves 80.6% SWE-bench at $0.87 per million output tokens via hosted API
- Kimi K3's 2.8-trillion-parameter weights are freely downloadable for self-hosting at no per-token cost
- Claude Opus 5 holds the FrontierBench v0.1 lead at 43.3% at $25 per million output tokens in standard mode
- GPT-5.6 Sol offers OpenAI's benchmark story at comparable premium pricing

The market is now showing developers four distinct choices at four distinct price and capability points, with the open-source and open-weight options now viable for production use at scale. This bifurcation—top frontier models at premium prices for maximum-effort tasks, and efficient open-weight or API-accessible models for cost-sensitive workloads—is the AI infrastructure structure that was predicted but has now arrived.

What is notable is not just the price gap but the performance convergence. When V4-Pro-Max achieves 80.6% on SWE-bench while Claude Opus 5 and GPT-5.6 occupy the high-$20s-to-mid-$40s range on different benchmarks, the question enterprises are asking is no longer "can open-source compete?" but "for which specific workloads does the premium still make sense?" That is a fundamentally different question, and it benefits buyers.

## The Broader Context: DeepSeek's Complicated Moment

V4's GA comes as DeepSeek itself navigates significant competing pressures. The company is reportedly pursuing a $71 billion valuation for a domestic Shanghai STAR Market listing, capitalizing on the brand recognition that V3 and V4 have built globally. Its aggressive API pricing strategy has drawn scrutiny from U.S. policymakers who view it as potentially subsidized competition, though no formal action has been taken.

The Treasury Department has reportedly reviewed whether Kimi K3's performance on Anthropic-trained benchmarks suggests unauthorized model distillation—a concern that has extended to review of DeepSeek's training process as well. Neither company has commented publicly on the investigations.

None of that scrutiny has slowed V4's adoption. Developer community data across GitHub, Hugging Face, and key AI developer forums suggests V4 is now the default choice for cost-sensitive enterprise workloads where model accuracy at the 80% SWE-bench range is sufficient for the task—which, for most production applications, it is. The benchmark gap between V4 and the frontier flagships exists, but the price gap between them is an order of magnitude larger.

## What Happens Next

DeepSeek's roadmap beyond V4 is opaque—the company discloses very little publicly about development timelines. What is clear is that V4's GA marks the stabilization of a generation that has fundamentally altered enterprise AI economics.

For developers: V4 is now production-grade, stable, and cheap enough to run inference at scales that would have required dedicated hardware or enterprise contracts just two years ago. The democratization of high-performance AI inference is not a future event; it arrived this week.

For frontier model providers: every model priced above $0.87 per million output tokens needs a clear differentiation story for each customer segment it targets. Capability alone—particularly capability at the 43% FrontierBench level—is no longer sufficient justification for a 28x price premium in competitive enterprise negotiations.

The open-source price floor is now set. The race to the next level has begun.
