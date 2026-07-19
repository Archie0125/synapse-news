---
title: "Mira Murati's Thinking Machines Releases Inkling: A 975B-Parameter Open-Weight Challenger"
summary: "Former OpenAI CTO Mira Murati's Thinking Machines Lab has launched Inkling, a 975-billion-parameter mixture-of-experts model released open-weight under Apache 2.0. The multimodal model, built in just nine months with a 200-person team, directly challenges the closed-model paradigm with controllable reasoning, a 1M-token context window, and a fine-tuning platform designed to let enterprises train proprietary AI without licensing fees."
category: "ai-ml"
publishedAt: 2026-07-19
lang: "en"
featured: true
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/"
  - name: "Fortune"
    url: "https://fortune.com/2026/07/15/what-is-mira-murati-thinking-machines-first-ai-model-inkling/"
  - name: "Thinking Machines Lab"
    url: "https://thinkingmachines.ai/news/introducing-inkling/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/thinking-machines-open-sources-first-multimodal-language-model-inkling-focused-on-low-cost-and-resistance-to-censorship"
  - name: "gHacks"
    url: "https://www.ghacks.net/2026/07/16/thinking-machines-lab-releases-inkling-a-975-billion-parameter-open-weights-ai-model-under-apache-2-0/"
tags:
  - "Thinking Machines"
  - "Mira Murati"
  - "open-weight"
  - "LLM"
  - "AI models"
  - "multimodal"
  - "open source"
relatedSlugs:
  - "2026-07-17-moonshot-kimi-k3-open-weight-model-en"
  - "2026-07-07-deepseek-custom-ai-chip-inference-en"
  - "2026-04-04-open-source-llm-race-en"
---

When Mira Murati left OpenAI in October 2023 to found Thinking Machines Lab, the AI industry was curious but skeptical. Starting a frontier AI lab from scratch, nine months later producing a model capable of competing with the best open-weight systems on the market — that was the kind of timeline that would have seemed fantastical even two years ago. On July 15, 2026, Thinking Machines proved the skeptics wrong by releasing Inkling, a 975-billion-parameter mixture-of-experts model available to anyone under an Apache 2.0 license.

The launch reframes what the open-weight AI ecosystem can look like at the frontier tier, and arrives at a moment when enterprises are increasingly questioning the economics and strategic risks of depending entirely on proprietary models.

## What Inkling Is — and What It Isn't

Thinking Machines has been unusually direct about Inkling's positioning. The company's announcement states plainly that "Inkling is not the strongest overall model available today, open or closed." That kind of candor is rare in a field where every model launch comes with a cascade of cherry-picked benchmarks.

What Inkling offers instead is a carefully calibrated package: breadth, efficiency, and customizability. The architecture is a sparse mixture-of-experts system with 975 billion total parameters but only approximately 41 billion active during any given inference pass. That activation sparsity makes Inkling dramatically cheaper to run than dense models of equivalent total parameter count — a core requirement for enterprises that want to deploy AI at scale without inference costs that compound across millions of daily requests.

The model was trained on 45 trillion tokens spanning text, images, audio, and video, making it a native multimodal system. Current outputs are limited to text and code, but the underlying representation is cross-modal, meaning future fine-tuned variants could generate or interpret audio and video directly.

The context window extends to 1 million tokens — matching the largest windows available from closed frontier models — with a key practical feature: token efficiency. Independent benchmarks show Inkling completing comparable coding tasks using roughly one-third the tokens of Nvidia's Nemotron 3 Ultra, the previous leading open-weight coding model. At scale, that efficiency gap translates directly into infrastructure cost savings.

## Controllable Reasoning: A Novel Interface Primitive

Perhaps the most technically interesting feature is what Thinking Machines calls "controllable thinking effort." Rather than a binary on/off reasoning mode — the toggle OpenAI popularized with its o-series models — Inkling exposes a continuous dial from 0.2 to 0.99. Developers can programmatically adjust how much compute the model spends reasoning before generating an output.

The practical implications are significant. A customer service chatbot answering simple product questions doesn't need the same reasoning depth as a model auditing a financial model or debugging a distributed systems race condition. With controllable thinking effort, a single deployment can scale reasoning resources dynamically based on query complexity — reducing cost on simple tasks while preserving quality on hard ones. No other major model currently exposes this interface.

## Benchmark Context

Thinking Machines published a comprehensive benchmark suite alongside the launch. On the Humanity's Last Exam (HLE), Inkling scores 29.7% in pure text mode — meaningfully below leading closed models — rising to 46.0% when tool use is enabled. On AIME 2026, the advanced mathematics competition benchmark, Inkling scores 97.1%. On GPQA Diamond, a graduate-level science reasoning test, it achieves 87.2%. For software engineering, SWE-bench Verified comes in at 77.6%.

These numbers put Inkling comfortably ahead of other open-weight alternatives on most dimensions, while clearly trailing GPT-5.6 Sol and Claude Fable 5 on aggregate capability. The tradeoff Thinking Machines is making explicit: customizability and deployment economics beat peak benchmark performance for the majority of real-world enterprise applications.

The Bridgewater Associates case study in the announcement provides a concrete illustration. Bridgewater's quantitative team fine-tuned Inkling on financial reasoning tasks using the Tinker platform and achieved 84.7% accuracy on an internal financial reasoning test — beating proprietary closed models on that specific task while running at approximately one-fourteenth the inference cost.

## The Tinker Platform and Revenue Model

Unlike closed-model companies that charge for API access, Thinking Machines generates revenue through Tinker, its model customization platform. Because Inkling's weights are freely downloadable from Hugging Face, the company doesn't collect model licensing fees. Instead, Tinker provides the infrastructure to fine-tune, evaluate, and deploy custom Inkling variants, with pricing tied to compute consumption rather than model access.

This architecture aligns Thinking Machines' incentives with enterprises building proprietary AI rather than with general public adoption — a meaningful distinction. A company that fine-tunes Inkling on its internal knowledge base doesn't leak that knowledge to a shared model serving millions of users, addressing one of the core data sovereignty objections to proprietary AI deployment.

The model ships with broad inference engine compatibility at launch: vLLM, SGLang, Miles, TokenSpeed, and Llama.cpp are all supported, giving engineering teams flexibility in how they host and scale deployments.

## The Bigger Industry Signal

The Inkling launch is most significant not for what the model can do today but for what its existence signals about the frontier AI competitive landscape. Thinking Machines built a model that competes meaningfully with the world's best open-weight alternatives in approximately nine months with roughly 200 employees. OpenAI's first GPT-4-class model took the company five years and thousands of people.

The compression of development timelines is not a Thinking Machines anomaly — it's a structural shift driven by the compound effects of better training infrastructure, larger pools of synthetic training data, and the accumulated research that has flowed into the open literature since 2022. The consequence is that the barrier to entering the frontier AI model market is falling, faster than most established players anticipated.

Microsoft CEO Satya Nadella's recent observation that enterprises effectively "pay twice" when using proprietary models — once through subscription fees and again through implicit knowledge transfer as their usage patterns inform model improvements — has found wide resonance in enterprise AI procurement teams. Inkling's Apache 2.0 license directly addresses that concern: the model can be deployed entirely within a customer's own infrastructure, with no data leaving their control.

Whether Thinking Machines can sustain a viable business model on Tinker revenue alone remains to be tested. The company reportedly paused a $50 billion fundraising round earlier this year amid market uncertainty. But the Inkling launch demonstrates that the lab has produced a technically credible product in a compressed timeframe — a meaningful proof point regardless of how the financing situation ultimately resolves.

For the broader market, Inkling's arrival makes the summer of 2026 officially the most competitive open-weight landscape the AI industry has seen. Meta's Llama 4, Moonshot's Kimi K3, DeepSeek V4, and now Inkling are all competing for developer mindshare within a matter of weeks — forcing engineers to develop genuine model selection discipline rather than defaulting to whichever frontier name they already know.
