---
title: "DeepSeek Quietly Building Its Own AI Chip to Escape Dependence on Nvidia and Huawei"
summary: "A Reuters exclusive published July 7 reveals that Chinese AI startup DeepSeek has been secretly developing a custom inference chip for about a year, hiring semiconductor engineers and approaching foundry partners. The move would make DeepSeek the latest major AI lab to vertically integrate into silicon — and could reshape China's AI hardware landscape."
category: "hardware"
publishedAt: 2026-07-07
lang: "en"
featured: true
trending: false
sources:
  - name: "Reuters via US News"
    url: "https://www.usnews.com/news/top-news/articles/2026-07-07/exclusive-chinas-deepseek-developing-its-own-ai-chip-sources-say"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-07-07/chinese-ai-startup-deepseek-developing-own-ai-chip-reuters-says"
  - name: "Engadget"
    url: "https://www.engadget.com/2209378/deepseek-reportedly-developing-ai-chips/"
tags:
  - "deepseek"
  - "ai-chip"
  - "semiconductor"
  - "china"
  - "inference"
  - "nvidia"
relatedSlugs:
  - "2026-07-07-chinese-ai-models-openrouter-60-percent-dominance-en"
  - "2026-07-05-meituan-longcat-2-china-domestic-chips-en"
---

In an industry where compute is power, DeepSeek wants to control its own destiny.

Reuters reported on July 7, 2026, citing three people familiar with the matter, that the Chinese AI startup behind the globally popular DeepSeek-R1 and V3 reasoning models has been quietly working on a custom AI chip for approximately one year. The chip targets **inference** — the computationally intensive process of generating model responses for users — rather than training, where building competitive silicon is an even more daunting engineering challenge.

DeepSeek did not respond to Reuters' request for comment, and the effort is described as early-stage. But the report's confirmation from multiple independent sources marks a significant moment: the company that redefined what was possible with constrained compute is now working to constrain that constraint itself.

## Why Now, Why Inference

The timing reflects both ambition and necessity. DeepSeek has built an extraordinary reputation for training highly capable models with far fewer GPUs than Western competitors — R1's release in early 2025 sent shockwaves through the industry precisely because it achieved frontier reasoning performance at a fraction of the expected compute cost. But every successful inference query still runs on Nvidia A100s and H800s or Huawei's Ascend chips, and both supply lines carry serious strategic risk.

Nvidia's H100 and H200 series remain under strict U.S. export controls. Separate restrictions on high-bandwidth memory (HBM) — a component critical to AI inference — further complicate China's access to the hardware stack. Huawei's Ascend 910C has partially filled the gap, but supply remains constrained and performance lags behind Nvidia's latest Blackwell offerings.

A purpose-built inference chip would let DeepSeek sidestep both constraints for the workloads that actually generate revenue. Inference is also more technically tractable than training silicon: the required memory bandwidth and precision requirements, while still demanding, are more achievable within China's current domestic manufacturing capabilities.

## The Manufacturing Challenge

DeepSeek's effort involves privately hiring chip-design engineers and holding discussions with foundry and memory partners. But the path to a competitive chip is steep.

U.S. export controls prevent Chinese chip designers from accessing TSMC's most advanced nodes — currently 3nm. China's leading foundry, SMIC, currently offers mature 7nm production and limited 5nm-equivalent processes, meaning any chip DeepSeek produces in the near term would face a meaningful performance gap relative to Nvidia's latest silicon.

Separate restrictions on HBM exports are potentially even more limiting. AI inference is fundamentally memory-bandwidth-bound — models need to shuttle billions of parameters from memory to compute units at extreme speed. Without access to competitive HBM from SK Hynix, Samsung, or Micron, a domestically designed inference chip would need to compensate with novel architectural choices or accept throughput limitations.

These are not insurmountable problems — DeepSeek has demonstrated a remarkable capacity for unconventional engineering under constraint — but they are real ones that will determine whether the chip can actually compete at scale.

## A Crowded Field of In-House Silicon

DeepSeek would not be alone in making this bet. OpenAI last month unveiled Jalapeno, its first custom inference chip co-developed with Broadcom, signaling that even the dominant commercial AI lab sees proprietary silicon as a strategic priority. Anthropic has separately been reported to be evaluating its own chip roadmap. Google's TPU v5 and Amazon's Trainium 2 are already in production at scale, and Meta's MTIA accelerators handle a significant portion of Facebook and Instagram's AI workloads.

The difference for DeepSeek is the geopolitical context. Western AI labs building custom silicon are optimizing for cost efficiency and performance differentiation within an abundant supply chain. DeepSeek is building partly out of constraint — and potentially as a template for how Chinese AI companies survive in a world of sustained, and potentially intensifying, export controls.

## What This Signals for China's AI Ecosystem

If DeepSeek succeeds in shipping a competitive inference chip, the implications extend well beyond the company itself. It would validate the feasibility of a vertically integrated AI stack within China's domestic semiconductor ecosystem and potentially provide a blueprint for Baidu, ByteDance, Alibaba, and other large operators of AI infrastructure.

It would also pose new competition for Huawei, which has positioned its Ascend line as the de facto inference backbone for Chinese AI companies. A DeepSeek chip — tuned specifically for DeepSeek models and potentially made available to the broader ecosystem — could significantly complicate Huawei's semiconductor ambitions and accelerate the fragmentation of China's AI hardware supply chain.

For Nvidia, the risk is more distant: China already accounts for a fraction of its legal addressable market under current export controls, and a domestically fabbed chip is unlikely to match Blackwell performance in the near term. But every successful alternative chip reduces Chinese AI companies' dependence on the CUDA software ecosystem — and that long-term erosion of CUDA lock-in matters more than any single competitor's market share.

## The Broader Pattern

The chip announcement confirms a trend that is accelerating across the global AI industry: every frontier AI lab is moving to control its own silicon. The era of AI companies as pure software enterprises, entirely dependent on commodity hardware from a handful of suppliers, is ending. DeepSeek's entry into chip design — even in its early stages — is the latest evidence that this vertical integration imperative has crossed geopolitical lines.

The company that shocked the world with R1's efficiency has demonstrated that unconventional engineering approaches can produce remarkable results under constraint. Whether that same ingenuity can crack custom silicon within China's manufacturing limitations remains to be seen. But that DeepSeek is trying at all is itself a signal about where the industry is heading.
