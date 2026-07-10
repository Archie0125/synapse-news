---
title: "OpenAI Unveils Jalapeño: Its First Custom Inference Chip, Built With Broadcom in Nine Months"
summary: "OpenAI and Broadcom revealed Jalapeño, OpenAI's first in-house AI inference processor, promising roughly 50% cost savings over GPU alternatives. Developed from concept to tape-out in under nine months, the chip signals a major vertical integration push by the world's most valuable AI company."
category: "hardware"
publishedAt: 2026-07-10
lang: "en"
featured: true
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/"
  - name: "OpenAI"
    url: "https://openai.com/index/openai-broadcom-jalapeno-inference-chip/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-06-24/openai-and-broadcom-unveil-ai-chip-to-run-models-faster-cheaper"
tags:
  - "OpenAI"
  - "Broadcom"
  - "Jalapeño"
  - "AI chips"
  - "inference"
  - "hardware"
  - "semiconductors"
relatedSlugs:
  - "2026-07-09-apple-broadcom-30b-us-chip-deal-en"
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-en"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-en"
---

For years, OpenAI has been the world's most important customer of the GPU industry — a company that purchases enormous quantities of Nvidia silicon and converts it, at enormous cost, into the intelligence behind ChatGPT. On June 24, OpenAI began rewriting that relationship. The company unveiled Jalapeño, its first custom AI inference chip, built in partnership with Broadcom, in what executives called the first step of a multi-generation compute platform the company intends to own rather than rent.

The announcement marks a genuine strategic inflection point, not just for OpenAI, but for the entire AI infrastructure ecosystem.

## What Is Jalapeño?

Jalapeño is an inference processor — designed specifically for the phase of AI computation that happens after a model has been trained, when it responds to real user queries. That distinction matters enormously. Training large language models requires the generalized, massively parallel floating-point performance of Nvidia H100 and GB300 GPUs. Inference is a different beast: it demands low latency, high memory bandwidth, and cost efficiency at scale, often running billions of requests per day.

Where Nvidia's hardware is a general-purpose accelerator adapted to AI workloads, Jalapeño was designed from a blank slate with a single objective: run OpenAI's LLM inference workloads as efficiently as possible. "We have a deep understanding of the workload," OpenAI President Greg Brockman said at the chip's reveal. "We wanted to build something that will be able to accelerate what's possible."

Early testing bears that out. Engineering samples of Jalapeño are already running ML workloads in the lab at production target frequency and power levels — including GPT-5.3-Codex-Spark, one of OpenAI's coding-optimized models. The company says performance per watt is "substantially better than current state-of-the-art alternatives," and independent analysis suggests cost savings of roughly 50% compared to standard GPU deployments.

## The Speed of Development

What is perhaps most remarkable about Jalapeño is not the chip itself but how quickly it materialized. The partnership between OpenAI and Broadcom was officially announced in October 2025. From initial design concept to manufacturing tape-out — the point at which chip designs are committed to silicon — took fewer than nine months. For a high-performance advanced semiconductor, that may be the fastest ASIC development cycle ever achieved in the industry.

The speed reflects a deliberate approach to co-development. Broadcom, the world's largest ASIC manufacturer and a dominant force in custom silicon for hyperscalers like Google and Meta, brought its implementation expertise to the table. OpenAI contributed deep, empirical knowledge of how its models actually run in production — how attention heads access memory, how key-value cache access patterns shift under load, how routing decisions flow through mixture-of-experts architectures. Crucially, OpenAI also used its own AI models to accelerate portions of chip design and optimization — a genuinely new feedback loop in semiconductor engineering.

## The Economics Behind the Move

The motivation for custom silicon is not obscure. OpenAI's compute costs are staggering and growing. Running ChatGPT, the Codex API, and an expanding suite of enterprise products across hundreds of thousands of GPUs costs the company billions of dollars annually. Inference — responding to users in real time — dominates that cost structure. Every percentage point of efficiency improvement translates directly to margin.

By owning its inference silicon, OpenAI gains leverage it has never had. When Nvidia raises prices or allocates supply to other customers, OpenAI's dependence on a single vendor creates risk. Custom chips remove that single point of failure and give the company the ability to optimize hardware for precisely how its models are architected — something a general-purpose accelerator cannot do.

The playbook is borrowed from predecessors. Google built its Tensor Processing Units (TPU) starting in 2015 and credits them with much of its cost advantage in serving Search and Google Cloud AI workloads. Amazon's Trainium chips power its own model training and have become a significant commercial alternative to Nvidia within AWS. Apple, which reached a separate $30 billion agreement with Broadcom in 2026 for custom components, pursues the same logic at the consumer device layer.

## Part of a Larger Vertical Integration Strategy

Jalapeño is described by OpenAI as the first step in a "multi-generation compute platform." Initial deployment is planned for before the end of 2026, with successive generations of the architecture to follow. The company has not disclosed planned production volumes, but Broadcom's role as Merchant of Record for the manufacturing relationship suggests significant scale is anticipated.

This chip strategy fits within a broader pattern at OpenAI. The company has moved aggressively into hardware adjacencies over the past year: the rumored Ive-led AI device effort, the Stargate data center buildout with SoftBank and Oracle, a reported 5% equity stake offered to the U.S. government. Owning inference silicon closes another loop in a company that increasingly resembles a vertically integrated platform rather than a software startup.

Pre-training on GPUs — the phase that creates new foundation models — will still require Nvidia hardware for the foreseeable future. The compute requirements for that phase are so large and heterogeneous that custom ASICs cannot yet match the flexibility of Nvidia's H100 clusters. But inference is exactly where custom chips shine: predictable, high-volume, easily characterized workloads that reward specialization.

## What This Means for Nvidia

The announcement is a signal to the industry even if it doesn't immediately dent Nvidia's financials. OpenAI is Nvidia's most prominent AI customer and arguably its most powerful brand ambassador. When the company announces it has designed its own inference chip, every other major AI developer in the world receives a clear message about where the industry is heading.

Nvidia retains its dominance in training, and the GB300 Blackwell Ultra architecture remains the gold standard for frontier model development. But as inference workloads grow faster than training workloads — ChatGPT's usage has grown dramatically, and each conversation generates far more inference tokens than training tokens per unit of user value — the GPU incumbent's position in the inference market could erode as custom silicon matures.

For the broader semiconductor ecosystem, Jalapeño is another data point that AI is driving the most aggressive wave of custom chip development since the smartphone era. Broadcom, TSMC, and other foundry-and-design-services players are the structural beneficiaries of this trend regardless of which AI companies ultimately win. The race to build the most efficient stack for AI inference is only beginning.

---

*OpenAI's Jalapeño chip will enter initial production deployment by end of 2026, with successive chip generations planned under the multi-generation platform roadmap.*
