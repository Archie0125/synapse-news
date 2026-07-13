---
title: "Meta's Iris AI Chip Clears Testing, Enters Mass Production in September"
summary: "Meta's fourth-generation MTIA chip, code-named Iris, passed its bug-testing phase in just six weeks and is slated for mass production this September. Designed with Broadcom and manufactured by TSMC, Iris is the centerpiece of Meta's $125–$145 billion capital expenditure plan to double its AI computing capacity to 14 gigawatts by 2027."
category: "hardware"
publishedAt: 2026-07-13
lang: "en"
featured: false
trending: true
sources:
  - name: "Reuters / US News"
    url: "https://money.usnews.com/investing/news/articles/2026-07-09/exclusive-meta-to-put-ai-chip-into-production-in-september-as-it-looks-to-double-computing-capacity-memo-shows"
  - name: "MLQ News"
    url: "https://mlq.ai/news/meta-to-begin-manufacturing-in-house-iris-ai-chip-in-september/"
  - name: "Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/meta-could-start-production-of-iris-ai-chip-in-september-report/"
tags:
  - "Meta"
  - "AI chips"
  - "MTIA"
  - "hardware"
  - "Broadcom"
  - "TSMC"
  - "custom silicon"
relatedSlugs:
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-en"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-en"
  - "2026-07-11-sambanova-1b-series-f-ai-chip-en"
---

Meta Platforms is moving decisively from GPU dependence to in-house silicon. An internal company memo reviewed by Reuters revealed that Iris—the fourth generation of Meta's Meta Training and Inference Accelerators (MTIA) program—cleared its bug-testing phase in roughly six weeks without uncovering significant problems and is set to begin mass production in September 2026. The milestone marks a critical inflection point in big tech's race to own every layer of the AI stack.

## What Iris Is—and What It Isn't

Iris is not a GPU replacement in the style of Google's TPU or Amazon's Trainium. Instead, it is purpose-built for the inference workloads that dominate Meta's production environment: ranking and recommendation signals for Facebook and Instagram feeds, generative image and video inference, and increasingly, on-platform AI features like Llama-powered chat assistants.

The MTIA lineup now covers four variants with roughly six-month release cadences—approximately double the pace of comparable industry programs:

- **MTIA 300**: Already in production, powering recommendation and ranking tasks across Meta's social platforms
- **Iris (MTIA 400-series)**: Entering production September 2026, targeting generative AI inference
- **MTIA 450 and 500**: Planned through 2027, targeting increasingly complex generative image and video workloads

Newer MTIA generations are expected to use TSMC's 2-nanometer process node, which offers significant power efficiency improvements over current production nodes. Broadcom serves as design partner under an agreement that runs through 2029 and covers multiple chip generations.

## The Strategic Imperative: Breaking Nvidia's Hold

Meta's 2026 capital expenditure guidance runs to $125–$145 billion, with nearly all of it directed at data centers, GPUs, and custom silicon. That figure is larger than the GDP of roughly 100 countries. The scale reflects a fundamental tension the company is trying to resolve: its AI ambitions are growing faster than Nvidia can profitably supply it with H100s and B200s.

"We need more compute than the market can easily provide at reasonable cost," Meta's infrastructure team stated in the memo. Iris directly addresses that constraint. While the chip will not fully replace third-party GPUs—analysts expect it to absorb growth in inference workloads rather than displace existing Nvidia training clusters—it gives Meta pricing leverage in supplier negotiations and removes a significant portion of inference cost from Nvidia's margin stack.

By the numbers, Meta is targeting:
- **7 gigawatts** of total computing capacity operational by end of 2026
- **14 gigawatts** by end of 2027—a doubling in twelve months

To put that in perspective, 14 gigawatts is roughly equivalent to the entire output of twelve large nuclear reactors running continuously.

## How Iris Fits the Broader Custom Silicon Wave

Meta joins a growing cohort of hyperscalers developing inference-specific silicon to hedge against what industry analysts have started calling "chipflation"—the compounding cost pressure of training and inference workloads scaling faster than GPU supply. Google has run its TPU program since 2016. Amazon's Trainium and Inferentia chips power a growing share of AWS's AI services. Microsoft is developing its Maia AI accelerator. Apple's Neural Engine is deeply embedded in on-device inference.

What distinguishes Meta's approach is the scale of the inference problem it is trying to solve. At roughly 3.3 billion daily active users across Facebook, Instagram, WhatsApp, and Threads, the recommendation and ranking models that Meta runs are among the most computationally demanding in the world—and they run continuously, 24 hours a day. Even marginal improvements in inference efficiency translate to hundreds of millions of dollars in cost savings annually.

The Iris chip also has supply-chain depth that most custom silicon programs lack. Meta has secured memory supply agreements with Samsung, flash storage with SanDisk, and fiber-optic interconnect equipment with Sumitomo Electric—the kind of multi-tier supply chain management that historically only Nvidia and Intel have operated at scale.

## Competitive and Market Implications

For Nvidia, Iris represents not an existential threat but a meaningful revenue headwind. Meta is currently one of Nvidia's largest customers, and a successful Iris deployment that absorbs even 15–20% of Meta's inference demand would reduce annual GPU purchases by several billion dollars. Multiplied across Google, Amazon, Microsoft, and Apple running similar programs, the aggregate effect on Nvidia's data-center revenue growth trajectory is material.

For TSMC and Broadcom, the news is unambiguously positive. TSMC lands the Iris fabrication contract, extending its lead as the preferred foundry for leading-edge custom silicon. Broadcom's chip design partnership with Meta through 2029 gives it a predictable revenue stream in the custom ASIC market that it has also been developing with Google (TPU supply partnership) and ByteDance.

For the broader AI ecosystem, Iris signals that the inference infrastructure layer is becoming as strategically contested as the training layer. Companies that can run inference cheaply and at scale will have a structural cost advantage in deploying AI features across their products—an advantage that compounds over time as model complexity grows.

## What Comes Next

The September production start means Iris chips should be appearing in Meta's data centers before the end of 2026. The company is expected to publish performance benchmarks and deployment metrics once the rollout is far enough along to be meaningful—likely in Q4 2026 or with the release of its fourth-quarter earnings.

For developers and researchers, the MTIA program's rapid cadence suggests Meta is serious about catching up to Google's TPU maturity curve. Whether Iris performs well enough in production to justify the massive capital commitment—and whether the 14-gigawatt target by 2027 is achievable given global power grid constraints—will determine whether this represents a genuine shift in AI infrastructure or an expensive experiment in hardware sovereignty.
