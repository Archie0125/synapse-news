---
title: "Grok 4.3 Lands on Amazon Bedrock as xAI Makes Its Enterprise Push"
summary: "xAI's Grok 4.3 is now generally available on Amazon Bedrock, making the startup the third major independent AI lab on the platform alongside Anthropic and OpenAI. At $1.25 input and $2.50 output per million tokens for requests under 200,000 tokens, it is the cheapest US-lab frontier reasoning model on Bedrock, backed by a 1-million-token context window, configurable reasoning effort, and xAI's claim of the lowest hallucination rate among frontier models. The deployment uses a new 'Mantle' inference engine, requiring developers to update their SDK integration."
category: "developer-tools"
publishedAt: 2026-06-25
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "AWS: Grok 4.3 from xAI now available in Amazon Bedrock"
    url: "https://aws.amazon.com/about-aws/whats-new/2026/06/grok-amazon-bedrock/"
  - name: "AWS Blog: AWS Weekly Roundup June 22, 2026 — Grok 4.3 in Bedrock"
    url: "https://aws.amazon.com/blogs/aws/aws-weekly-roundup-ny-summit-recap-local-zone-in-hanoi-grok-4-3-in-bedrock-price-reductions-and-more-june-22-2026/"
  - name: "xAI: Grok on Amazon Bedrock"
    url: "https://x.ai/news/grok-amazon-bedrock"
  - name: "Digital Applied: Grok 4.3 on Amazon Bedrock Enterprise Launch 2026"
    url: "https://www.digitalapplied.com/blog/grok-4-3-amazon-bedrock-enterprise-launch-2026-guide"
tags:
  - "xAI"
  - "Grok"
  - "Amazon Bedrock"
  - "AWS"
  - "enterprise AI"
  - "developer tools"
  - "reasoning models"
  - "Mantle"
relatedSlugs:
  - "2026-06-02-xai-grok-41-fast-enterprise-api-grok5-roadmap-en"
  - "2026-06-06-openai-gpt55-codex-aws-bedrock-en"
  - "2026-06-01-amazon-trainium-20b-custom-silicon-en"
---

Amazon Bedrock just added its third major independent AI lab. Starting June 15, 2026, **Grok 4.3 from xAI** is generally available on the platform, putting xAI alongside Anthropic and OpenAI as the third major independent lab on AWS's managed AI service. The deployment comes with a pricing structure that is likely to generate immediate developer attention: **$1.25 per million input tokens and $2.50 per million output tokens**, making it the cheapest US-lab frontier reasoning model on Bedrock by a significant margin.

## What Grok 4.3 Brings

The model ships with a set of capabilities designed specifically for enterprise production workloads:

**1-million-token context window.** Grok 4.3 can process up to 1 million tokens in a single request, though requests above 200,000 tokens are billed at a higher tier where the per-token rate doubles. For enterprise use cases involving lengthy legal documents, large codebases, or complex multi-document analysis, this is now table stakes rather than a differentiator.

**Configurable reasoning effort.** xAI's most distinctive feature in the enterprise context is the ability to dial reasoning intensity across four levels: none, low, medium, and high. Grok 4.3's configurable effort lets developers trade off latency and cost against reasoning depth on a per-request basis, which is valuable for applications where some queries need deep analysis and others just need fast responses.

**Lowest hallucination rate claim.** xAI claims Grok 4.3 achieves the lowest hallucination rate among frontier models. Customer support, legal research, and financial document Q&A are domains where accuracy matters, so the claim will get scrutiny.

**Tool calling, structured output, streaming.** All three are supported on Mantle.

## The Mantle Difference

The deployment architecture is notable and worth understanding before building on it. Grok 4.3 on Bedrock runs on **Mantle**, a new inference engine in Amazon Bedrock, not on the standard Bedrock Runtime used by Claude and other models. This means existing Bedrock SDK code will not work with Grok 4.3 unchanged.

Developers must use the `bedrock-mantle` endpoint rather than `bedrock-runtime`, and the API path uses an OpenAI-compatible structure rather than the Converse or InvokeModel APIs that most Bedrock integrations rely on. The practical implication: dropping Grok 4.3 into an existing Bedrock application requires code changes, not just a model ID swap.

AWS describes Mantle as designed for price performance, with support for tool calling, structured output, and response streaming. Whether Mantle evolves into a general inference infrastructure layer for Bedrock's more performance-demanding models, or remains xAI-specific, has significant implications for how developers architect against the platform.

## The Pricing Math

At $1.25/$2.50 per million tokens, Grok 4.3 is substantially cheaper than its nearest Bedrock competitors in the reasoning model tier:

- **Claude Sonnet 4.6** runs at $3.00/$15.00 per million tokens on Bedrock
- **GPT-5.4 via Bedrock** runs at roughly $2.50/$15.00
- **Grok 4.3** at $1.25/$2.50 is less than half the Claude Sonnet 4.6 price on input ($3.00) and well under a fifth on output ($15.00)

For high-volume enterprise workloads—where token usage is measured in billions per month, not millions—the cost differential compounds dramatically.

This pricing pressure is not just good news for developers. It also reflects the intensifying competition in the managed model market, where providers are under growing pressure to differentiate on price as model quality converges across frontier labs. This pricing pressure is not just good news for developers; it also reflects the intensifying competition in the managed model market.

## xAI's Enterprise Trajectory

Grok 4.3 on Bedrock is the clearest signal yet that xAI is executing a deliberate enterprise distribution strategy rather than relying solely on Grok's consumer presence through X Premium and the grok.com interface.

For Grok to succeed in enterprise, the Bedrock channel matters more than almost any other distribution decision xAI could make. Teams that already build on Bedrock can evaluate Grok 4.3 through the Mantle endpoint, compare it against other models on their own workloads, and switch if the price-quality ratio holds up. That is a far faster evaluation cycle than convincing enterprise procurement teams to onboard a new AI vendor from scratch.

## What Developers Should Know

For teams evaluating Grok 4.3 on Bedrock, the practical guidance:

The model is best suited to **document-heavy, cost-sensitive workloads** where configurable reasoning effort can reduce per-request costs for simpler queries. Customer support, web development, case law research, and financial document Q&A are the workloads AWS highlights as especially well suited.

The **Mantle endpoint** requires SDK updates. Teams should test their existing Bedrock integrations before assuming compatibility.

**Hallucination claims** from xAI should be validated against each team's specific domain before relying on them for compliance-sensitive applications.

The enterprise AI model market is converging on a structure where three or four frontier models compete aggressively on both capability and price through managed platforms. Grok 4.3 on Bedrock is the most significant move yet toward that convergence.

*Correction (November 15, 2026): 21 sentences were corrected or removed to match the sources listed on this page.*
