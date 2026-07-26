---
title: "Kimi K3 Open Weights Drop Sunday: World's Largest Open-Weight Model at 2.8 Trillion Parameters"
summary: "Moonshot AI releases the full weights of Kimi K3 on July 27 under a Modified MIT license — making the 2.8-trillion-parameter model the largest open-weight release in history. For enterprises wary of routing sensitive data through a Chinese API, self-hosting now becomes a technically viable, if hardware-intensive, option."
category: "ai-ml"
publishedAt: 2026-07-26
lang: "en"
featured: false
trending: true
sources:
  - name: "Kimi Blog"
    url: "https://www.kimi.com/blog/kimi-k3"
  - name: "Labellerr"
    url: "https://www.labellerr.com/blog/kimi-k3-world-first-open-2-8t-ai-model/"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/321551/20260725/kimi-k3-open-weights-arrive-sunday-self-hosting-cuts-china-data-risk-api-never-can.htm"
tags:
  - "Kimi K3"
  - "Moonshot AI"
  - "open weights"
  - "LLM"
  - "open source"
  - "China AI"
  - "self-hosting"
  - "mixture of experts"
relatedSlugs:
  - "2026-07-17-moonshot-kimi-k3-open-weight-model-en"
  - "2026-07-24-moonshot-ai-kimi-k3-treasury-sanctions-anthropic-distillation-en"
  - "2026-07-07-chinese-ai-models-openrouter-60-percent-dominance-en"
---

At midnight UTC on July 27 — 8:00 PM Eastern on Sunday — Moonshot AI will publish the full weights of Kimi K3 on Hugging Face, making available for inspection, modification, and self-deployment the largest open-weight model ever released: 2.8 trillion parameters, nearly triple the size of its predecessor Kimi K2.6.

The release is the culmination of a model that has generated sustained industry attention since its API launch on July 16. K3 topped the Frontend Code Arena benchmark with 1,679 points, besting Claude Fable 5 (1,631), GPT-5.6 Sol (1,618), and Zhipu's GLM-5.2 (1,587). On GPQA Diamond — the graduate-level science reasoning benchmark — K3 scored 93.5%, the strongest open-weight result at launch. BrowseComp, which tests web research capability, came in at 91.2%, the best published score for any model as of the release date.

But benchmarks are only part of the story. The open weights release introduces a fundamentally different deployment calculus for any organization that has been using K3's API while quietly worrying about what happens to their data when it flows through servers in Beijing.

## What Makes K3's Architecture Different

K3 is a Mixture of Experts (MoE) model, but not a conventional one. Out of 896 total experts, only 16 are activated per token — a 1.8% activation rate that keeps per-token compute tractable despite the trillion-parameter count. Three architectural innovations differentiate K3 from previous large MoE releases.

**Kimi Delta Attention (KDA)**: A hybrid linear attention mechanism that enables up to 6.3x faster decoding for million-token contexts. Practical long-context processing has historically required massive compute budgets; KDA makes it competitive at inference time.

**Attention Residuals (AttnRes)**: Boosts training efficiency by approximately 25% while adding less than 2% computational overhead. This is primarily a training efficiency story, but it allows Moonshot to pack more training signal into the same compute envelope.

**Stable LatentMoE**: The expert routing mechanism that achieves the 1.8% activation rate with claimed load balancing stability — routing collapse has been a persistent failure mode in large MoE models, and Moonshot's approach here appears to have addressed it.

The model also natively handles vision inputs and provides a one-million-token context window — meaningful for enterprise document processing and codebase analysis workflows.

## The Self-Hosting Value Proposition (and Its Hardware Reality)

The candid case for self-hosting K3 comes down to data residency. When you call the Kimi API, your prompts — potentially including proprietary code, internal documents, or sensitive customer data — route through Moonshot's infrastructure in China. That exposure is acceptable for many use cases. It is not acceptable for regulated industries, government contractors, defense-adjacent applications, or any organization that has received legal advice about Chinese data handling.

Self-hosting K3 eliminates that routing entirely. The weights are yours to run on your own compute, inspect for modifications, and audit. Under the Modified MIT license, commercial use is permitted without royalty, subject to attribution requirements and prohibitions on misrepresentation.

The hardware reality is less comfortable. Moonshot recommends production deployment on configurations with 64 or more accelerators. In Q4 MXFP4 quantization — the practical format for deployment — K3 requires approximately 1.4 terabytes of storage and 18 NVIDIA H100 80GB GPUs at minimum for inferencing, according to third-party analysis. That is approximately $2.5-3 million in GPU hardware at current market prices, plus substantial networking and cooling infrastructure.

For most teams, this rules out on-premises deployment. The practical middle path is running K3 on a hosted inference provider — Fireworks AI, Together AI, Baseten, or similar — which gives you contractual data residency guarantees under U.S. or EU law without requiring you to own the hardware. Several of these providers have confirmed they will offer K3 hosting by end of July.

## China's Open-Weight Strategy

K3's release is strategically timed. Moonshot is pursuing a Hong Kong IPO at a $50 billion valuation, with the weights release designed to maximize community mindshare and benchmark visibility before the roadshow. DeepSeek is pursuing a separate Shanghai listing at a $71 billion valuation; the open-weight model race has become intertwined with Chinese AI companies' capital market ambitions.

There is also a geopolitical dimension. Since Treasury sanctions targeted Kimi K3 in late July — prompted by evidence of Anthropic Claude training data distillation — the API has been restricted for U.S.-headquartered entities. Open weights create a legal workaround: the weights themselves are not yet sanctioned, and running an open-weight model locally does not constitute accessing a sanctioned service. Lawyers will debate the edge cases, but the practical reality is that K3 weights may remain accessible to U.S. developers even as the API becomes off-limits.

## How K3 Compares to the Open-Weight Landscape

Before K3, the largest open-weight model was DeepSeek V4 (671 billion parameters) and Meta's Llama 4 series. K3 at 2.8 trillion total parameters — 49 billion active per token — is in a different weight class. The nearest comparable in terms of benchmark performance is Mistral's LeanStral 1.5 and Meta's Watermelon model, both of which trail K3 on coding and research benchmarks.

For developers who need near-frontier performance without commercial API lock-in, K3 is the clearest option available as of today. DeepSeek V4-Flash maintains pricing pressure at $0.14 input / $0.28 output per million tokens, but K3's architecture advantages on long-context and coding tasks are significant enough that the higher API cost ($3.00 input / $15.00 output per million tokens) is defensible for production workloads.

## What to Watch After the Drop

The weights release will trigger an immediate community response. Fine-tuning experiments — particularly on coding, mathematics, and instruction-following — will begin within hours. The absence of a published hallucination rate benchmark is a gap that independent evaluators will move quickly to fill; Moonshot has disclosed strong accuracy scores but has not published a systematic false positive rate for factual claims.

The Modified MIT license terms are permissive enough that commercial fine-tunes and custom derivatives are expected to proliferate rapidly. Whether any of those derivatives are subject to Treasury sanctions if they incorporate K3 as a foundation remains legally uncertain and is already being actively discussed in legal and compliance communities.

The release arrives at a moment when the open-source AI ecosystem is undergoing structural change. The community is watching to see whether a 2.8 trillion parameter model is genuinely usable at the frontier — or whether it simply marks a parameter-count record while remaining impractical for the majority of deployment scenarios.
