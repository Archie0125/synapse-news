---
title: "OpenAI and Broadcom Unveil Jalapeño: The Custom AI Chip Designed to Dethrone Nvidia at Inference"
summary: "OpenAI and Broadcom revealed Jalapeño on June 24, OpenAI's first custom AI accelerator optimized specifically for LLM inference. Built in a record-breaking nine-month development cycle, the chip aims to dramatically cut the cost of running ChatGPT and future models at scale, signaling OpenAI's long-term push to own its full compute stack."
category: "hardware"
publishedAt: 2026-06-29
lang: "en"
featured: false
trending: true
sources:
  - name: "OpenAI — Jalapeño Inference Chip Announcement"
    url: "https://openai.com/index/openai-broadcom-jalapeno-inference-chip/"
  - name: "TechCrunch — OpenAI Unveils First Custom Chip Built by Broadcom"
    url: "https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/"
  - name: "CNBC — OpenAI and Broadcom Reveal Jalapeño"
    url: "https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html"
  - name: "VentureBeat — OpenAI First Custom AI Inference Chip Jalapeño"
    url: "https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models/"
  - name: "Tom's Hardware — Jalapeño ASIC Details"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle"
tags:
  - "openai"
  - "broadcom"
  - "ai-chips"
  - "hardware"
  - "inference"
  - "custom-silicon"
  - "nvidia"
  - "jalapeno"
relatedSlugs:
  - "2026-06-29-ai-chip-stock-selloff-june-2026-en"
  - "2026-06-29-onsemi-synaptics-7b-edge-ai-acquisition-en"
  - "2026-06-27-openai-gpt56-sol-terra-luna-preview-en"
---

When OpenAI and Broadcom took the stage on June 24 to unveil Jalapeño — OpenAI's first custom-designed intelligence processor — they weren't just announcing a chip. They were signaling a fundamental shift in how the world's most-used AI company intends to power its future. After years of being entirely dependent on Nvidia's H100 and H200 GPUs, OpenAI is now building its own silicon, and the implications ripple far beyond one product launch.

## Nine Months from Concept to Silicon

The most striking number in the Jalapeño announcement isn't a benchmark figure — it's a timeline. The chip went from initial design to manufacturing tape-out in just nine months, a pace Broadcom and OpenAI believe may represent the fastest ASIC development cycle ever achieved in high-performance advanced semiconductors. For comparison, traditional custom chip programs at hyperscalers like Google and Amazon have historically taken 18 to 24 months to complete their first silicon iteration.

That compression was no accident. OpenAI engineers used their own AI models to accelerate portions of the hardware design and optimization process — a recursive loop of artificial intelligence helping build the infrastructure that runs artificial intelligence. The company called it a demonstration of "deep software-hardware co-development," with Broadcom contributing silicon implementation expertise and Celestica handling board, rack, and system integration.

Engineering samples are already running machine-learning workloads in the lab at production target frequency and power, including GPT-5.3-Codex-Spark, one of OpenAI's internal coding model variants. Deployment at scale is planned before the end of 2026.

## What Jalapeño Is — and Isn't — Designed to Do

The chip is purpose-built for inference: the process of running a pre-trained AI model in response to user queries. This is the workload that dominates OpenAI's operational costs. Every ChatGPT conversation, every API call, every Codex completion — these are inference operations, consuming enormous amounts of compute at razor-thin margins.

Jalapeño's architecture was designed specifically around the bottlenecks that matter for LLM inference at scale: data movement between memory and compute cores, the balance between memory bandwidth and raw processing, networking efficiency between chips and servers, and the serving patterns that affect latency for real users. Early testing shows it delivers substantially better performance per watt than current state-of-the-art alternatives, though OpenAI has not yet released specific benchmark numbers.

Critically, Jalapeño is not intended to replace Nvidia for model training. Pre-training frontier models — the computationally brutal process that takes months and consumes vast clusters of the most powerful GPUs available — will continue to rely on Nvidia hardware for the foreseeable future. Jalapeño targets inference, where OpenAI spends the most money day-to-day.

OpenAI President Greg Brockman said the company is looking for "specific workloads that are underserved" and aiming to "accelerate what's possible" — careful language that acknowledges both what the chip will and won't do.

## The Economics of Custom Silicon

To understand why this matters, it helps to understand the cost structure OpenAI faces. Running ChatGPT, with hundreds of millions of users across free and paid tiers, generates enormous inference workloads. Despite record revenue — and a run-rate approaching the scale of major cloud providers — OpenAI has historically spent a disproportionate share of that revenue on compute, much of it flowing to Nvidia.

Custom inference chips offer a path to dramatically better economics. Google has run its own inference infrastructure on Tensor Processing Units (TPUs) for over a decade, giving it structural cost advantages in operating Gemini at scale. Amazon's Trainium and Inferentia chips serve similar purposes on AWS. By joining this club, OpenAI can negotiate better terms with cloud providers, reduce dependency on spot GPU markets, and improve the unit economics of every API call it delivers.

The strategic logic extends further: owning your hardware stack gives you control over roadmaps, supply chains, and the specific optimizations that matter most for your models. As OpenAI's models grow more complex — and as inference-heavy applications like agentic AI require faster, cheaper compute — having dedicated silicon becomes not just a cost play but a competitive advantage.

## A Multi-Generation Commitment

OpenAI and Broadcom framed Jalapeño not as a one-off product but as the first step in a "multi-generation compute platform." The partnership, officially announced in October 2025 before Jalapeño's unveiling, envisions multiple iterations of custom AI accelerators, with scale expanding from initial deployment through gigawatt-scale data centers planned alongside Microsoft and other infrastructure partners.

That gigawatt-scale ambition is significant. A single gigawatt of data center power is approximately the combined electrical consumption of a mid-sized American city. OpenAI is planning, in other words, for an AI compute footprint measured in the same units as national power grids.

## The Broader Chip Race

Jalapeño arrives at a pivotal moment in the AI hardware landscape. Qualcomm is reportedly in advanced talks to acquire RISC-V chip startup Tenstorrent for $8-10 billion. Samsung and SK Hynix are racing to supply the next-generation HBM memory that all these chips require. Nvidia's monopoly on AI compute, while still commanding, is being chipped away — quite literally — from multiple directions simultaneously.

For the broader industry, each new custom chip from a major AI lab is a signal: the era of AI companies simply buying Nvidia's latest GPU and calling it a strategy is ending. The companies that will dominate the next decade of AI are the ones building not just the models, but the full stack underneath them — the chips, the interconnects, the servers, and the data centers.

OpenAI just got much more serious about what that stack looks like.

---

*Jalapeño is expected to begin deployment in OpenAI's data centers before the end of 2026, with Broadcom, Celestica, and Microsoft as key partners in the rollout.*
