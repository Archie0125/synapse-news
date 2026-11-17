---
title: "Chinese AI Models Held 61% of Top-10 OpenRouter Token Volume in One Week as US Share Fell from 70% to 30%"
summary: "Chinese-origin models accounted for roughly 61% of token volume among OpenRouter's top 10 models in one February 2026 week, up from under 2% in late 2024. Separately, US providers' share of OpenRouter tokens fell from about 70% in June 2025 to about 30% in June 2026. The shift is attributed to lower pricing, open-weight availability, and coding benchmark performance that rivals closed US models."
category: "industry"
publishedAt: 2026-07-07
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "ChatForest — Chinese AI Models Now Own 60% of Global API Traffic"
    url: "https://chatforest.com/reviews/chinese-ai-models-openrouter-dominance-deepseek-kimi-minimax-glm-2026/"
  - name: "TechTimes — DeepSeek Hits 541 Million Visits, Fifth Worldwide"
    url: "https://www.techtimes.com/articles/318181/20260610/deepseek-hits-541-million-visits-fifth-worldwidechina-ai-price-war-tests-us-bills-data.htm"
  - name: "TechTimes — Chinese AI Models Lead OpenRouter Traffic: Coding Gains Come With China Data Risk"
    url: "https://www.techtimes.com/articles/317352/20260529/chinese-ai-models-lead-openrouter-traffic-coding-gains-come-china-data-risk.htm"
  - name: "OfficeChai — Share Of US Models Being Used On OpenRouter Has Collapsed From 70% To 30%"
    url: "https://officechai.com/ai/share-of-us-models-being-used-on-openrouter-has-collapsed-from-70-to-30-over-the-past-year/"
  - name: "Data Gravity — China's Open-Weight Takeover"
    url: "https://www.datagravity.dev/p/chinas-open-weight-takeover"
tags:
  - "chinese-AI"
  - "DeepSeek"
  - "OpenRouter"
  - "AI-market-share"
  - "geopolitics"
  - "open-source"
relatedSlugs:
  - "2026-07-05-meituan-longcat-2-china-domestic-chips-en"
  - "2026-07-02-taiwan-super-micro-nvidia-chip-smuggling-probe-en"
---

In June 2025, US AI providers — Google, OpenAI, and Anthropic — collectively accounted for roughly 70% of all token consumption routed through OpenRouter, the largest public API routing platform for AI models. One year later, that share has collapsed to approximately 30%.

The inverse of that decline has been captured by Chinese providers. Chinese-origin models, including those from DeepSeek, MiniMax, Moonshot AI (Kimi), Zhipu AI (GLM), and Xiaomi, accounted for roughly 61% of token volume among OpenRouter's ten most-used models in the week of February 24, 2026, though other measures put the Chinese share lower. That is up from less than 2% in early 2025 — a structural market shift of extraordinary speed and scale.

## The Numbers Behind the Shift

The scale of individual Chinese providers on the platform is striking. MiniMax's M2.5 model led OpenRouter's weekly ranking for the week of February 24, 2026 with 2.45 trillion tokens. Xiaomi, which entered the AI model market relatively recently, is processing 4.21 trillion tokens weekly — implying a monthly volume that dwarfs both competitors.

DeepSeek V3.2 and V4 collectively hold approximately 17.6% of total platform share as of June 2026. To put that in context: DeepSeek's share outranks every US lab on the platform, including Anthropic at about 15.4%, and sits well above Google and OpenAI. Zhipu's GLM-5.1 rounds out the top tier.

The composition of usage matters as much as the volume. Programming tasks now account for over 50% of all OpenRouter traffic, up from 11% in early 2025. Chinese models have specifically optimized for this use case, and their benchmark performance on software engineering tasks has reached parity or superiority with US closed-weight alternatives at dramatically lower price points.

## Why Chinese Models Are Winning

The competitive thesis for Chinese AI providers rests on four interlocking advantages.

**Pricing.** The most immediate driver is cost. Chinese models are roughly 60 to 90% cheaper than leading US alternatives for comparable workloads, though the advantage is not uniform across the Chinese lineup. DeepSeek V4, for example, offers a 1M-token default context window and prices output at $0.87 per million tokens, a fraction of the cost of leading US models. For cost-sensitive developers building high-volume applications, the math is not difficult.

**Open-weight availability.** Several leading Chinese models are released as open weights, meaning organizations can download and run them on their own infrastructure with no per-token fees whatsoever. This makes them attractive not only to budget-constrained startups but to enterprises with data sovereignty requirements, large-context batch processing needs, or a preference for infrastructure independence. The self-hosting option effectively removes the per-query cost ceiling entirely.

**Context window engineering.** Chinese AI development efforts have focused heavily on extending context windows and optimizing for long-document and multi-file tasks. MiniMax M2.5 is a mixture-of-experts model tuned for long-context tasks.

**Coding specialization.** The shift of OpenRouter usage toward programming tasks played directly into the strengths that Chinese labs have prioritized.

## The Regulatory and Security Dimension

The OpenRouter data tells a market story. But it lands in a geopolitical context that makes its implications more complex than a simple competitive analysis.

Directing production traffic to Chinese-controlled AI providers raises questions that go beyond cost optimization. Data processed by Chinese AI models — including potentially proprietary business logic, source code, customer data, and strategic communications — may be subject to Chinese data governance laws that require cooperation with government authorities. The legal frameworks governing Chinese technology companies' data handling obligations differ materially from the standards applied to US or EU providers.

US legislators have noticed the shift. The Trump administration postponed a planned AI oversight executive order in May 2026, leaving at that time no formal US framework governing how frontier models are evaluated before release; a revised order setting a 30-day review window was signed on June 2, 2026. That regulatory gap has effectively allowed market forces to drive adoption decisions that have national security implications.

For commercial enterprises outside the government sphere, the guidance is less clear. The security considerations are real but manageable with proper architecture: data can be classified, routing decisions can be task-specific, and hybrid deployments can use Chinese models exclusively for non-sensitive batch tasks while reserving US models for anything involving confidential information.

## What This Means for US AI Labs

The competitive implications for OpenAI, Anthropic, and Google are real but context-dependent. OpenRouter is not the entire AI market — it is a routing layer predominantly used by developers, AI startups, and technically sophisticated enterprises building on top of foundation models. The enterprise procurement landscape, which drives a disproportionate share of AI revenue, still skews toward US providers due to compliance requirements, established vendor relationships, and risk tolerance.

But OpenRouter is a leading indicator. The developer community that drives enterprise adoption cycles builds with what is cheapest and most capable first, and then advocates for organizational adoption. A developer community that has shifted heavily toward Chinese model usage is a community that, when asked to recommend AI infrastructure for their employer, may frequently cite Chinese providers.

But the pricing asymmetry may be structural rather than marginal: some Chinese providers can sustain lower prices because their models serve strategic goals beyond direct monetization, though the long-term economics are not verifiable from public data.

The deeper structural response is differentiation. The argument is that the highest-value AI workloads are better suited to frontier US models even at premium pricing. That argument is defensible. It is less convincing to the cost-sensitive majority of developers who are routing the traffic that shows up in OpenRouter's statistics.

## The View From Asia-Pacific

For readers in Taiwan and the broader Asia-Pacific region, the OpenRouter data is a particularly relevant data point.

Taiwanese enterprises and developers navigating this landscape face a choice with no easy answer. Chinese AI models offer compelling cost and capability profiles. US AI models offer more predictable regulatory compliance and alignment with Taiwan's strategic relationships. The appropriate answer, for most organizations, is a deliberate hybrid strategy rather than a default to either pole.

The OpenRouter data is a market signal about what the global developer community, unconstrained by compliance requirements, has found most economically rational. The question for organizations in Taiwan and beyond is how much of that rationality they can act on, and where the constraints make the cost premium for US models the right trade.

*Correction (November 15, 2026): 19 sentences were corrected or removed to match the sources listed on this page.*
