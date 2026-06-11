---
title: "NVIDIA Unveils Rubin: Six New Chips Promising 10x Cheaper AI Inference"
summary: "NVIDIA has detailed the full Rubin platform — six interconnected chips including the Vera CPU and Rubin GPU — targeting H2 2026 availability. The company claims a 10x reduction in inference token cost and 4x fewer GPUs needed to train mixture-of-experts models versus the current Blackwell generation, a leap that could reshape the economics of large-scale AI deployment."
category: "hardware"
publishedAt: 2026-06-11
lang: "en"
featured: false
trending: true
sources:
  - name: "NVIDIA Newsroom"
    url: "https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer"
tags:
  - "NVIDIA"
  - "Rubin"
  - "Vera CPU"
  - "AI chips"
  - "data center"
  - "hardware"
relatedSlugs:
  - "2026-06-03-nvidia-rtx-spark-superchip-computex-en"
  - "2026-06-10-tensorwave-amd-350m-series-b-anti-nvidia-en"
  - "2026-06-10-china-295b-ai-data-center-buildout-en"
---

NVIDIA has pulled back the curtain on Rubin, its next-generation data center platform and the direct successor to Blackwell. The company published full specifications for a six-chip system that represents not just a new GPU, but a ground-up redesign of every piece of silicon that goes into an AI supercomputer — from the compute engines to the networking fabric to the storage controllers.

The timing is deliberate. With Blackwell shipments now ramping at hyperscalers worldwide and competitors — AMD with MI400, Intel with Falcon Shores, and a rising tide of custom silicon from Google, Microsoft, and Amazon — narrowing the gap, NVIDIA needs to demonstrate that its roadmap lead remains intact. Rubin is that demonstration.

## What Rubin Actually Is

The platform comprises six distinct chips, each replacing a component in the existing Hopper/Blackwell stack:

**Vera CPU**: NVIDIA's first production-grade custom CPU, built on Armv9.2 with 88 custom Olympus cores. It replaces the host CPUs (typically Grace or third-party x86) that pair with NVIDIA's current data center GPUs. The Olympus cores are co-designed with the Rubin GPU's memory subsystem to minimize PCIe/NVLink latency for CPU-to-GPU data movement, a bottleneck that has historically limited performance on memory-intensive LLM workloads.

**Rubin GPU**: Features NVIDIA's third-generation Transformer Engine, optimized specifically for the attention and feedforward computation patterns of modern transformer architectures. Supports FP4 and FP6 data types natively alongside FP8, enabling aggressive quantization without the accuracy penalties that have limited earlier low-precision approaches. NVIDIA claims the Rubin GPU delivers roughly 4x the training throughput of H100 for mixture-of-experts (MoE) model architectures like DeepSeek-V3 and GPT-5.

**NVLink 6 Switch**: Delivers 3.6 terabytes per second of bandwidth per GPU — nearly double NVLink 4's 1.8 TB/s. At the rack level, the Vera Rubin NVL72 configuration packs 72 Rubin GPUs and 36 Vera CPUs, with an aggregate internal bandwidth of 260 TB/s. That makes the NVL72 roughly three times more bandwidth-dense than the current NVL72 Blackwell rack.

**ConnectX-9 SuperNIC**: Handles InfiniBand and Ethernet connectivity between racks, with per-port bandwidth sufficient to sustain the NVLink 6 Switch speeds without creating inter-rack bottlenecks. NVIDIA has been expanding into networking since its 2020 acquisition of Mellanox, and ConnectX-9 represents the full convergence of its GPU and networking roadmaps.

**BlueField-4 DPU and Spectrum-6 Ethernet Switch** round out the platform, handling storage offload and inter-cluster fabric respectively.

## The 10x Inference Cost Claim

The headline number NVIDIA is leading with is a 10x reduction in the cost per inference token relative to Blackwell. This is a compound figure that incorporates the higher GPU compute density, improved memory bandwidth, better quantization support in hardware, and the reduced number of racks required per unit of inference capacity.

For context: inference cost has been the central competitive battleground in AI infrastructure for the past 18 months. OpenAI's decision to price GPT-4 at $0.03 per 1,000 input tokens in early 2024 was only possible because of aggressive batching and optimization; today, frontier model inference runs at roughly 1/10th of that cost thanks to successive hardware and software improvements. If Rubin delivers another 10x reduction, it brings the cost of running a GPT-5-class model into the range where sub-cent-per-query pricing becomes viable — potentially unlocking consumer use cases that remain economically marginal today.

NVIDIA's customers are paying close attention. AWS, Google Cloud, Microsoft Azure, Oracle Cloud, Meta, OpenAI, Anthropic, xAI, and CoreWeave are all named as confirmed Rubin customers, representing essentially every significant buyer of data center GPU capacity globally. The company has not disclosed pricing, but industry analysts expect NVL72 rack prices to come in above Blackwell equivalents while offering substantially lower total cost of ownership per unit of compute.

## Vera CPU: NVIDIA Picks a Fight with Intel and AMD

The Vera CPU announcement is arguably as significant as the GPU specs, even if it commands less attention in the AI press. NVIDIA has historically been agnostic about host CPUs, supporting Grace (its own Arm-based CPU), Intel Xeon, and AMD EPYC interchangeably. With Vera, the company is making an explicit architectural bet: that the tightest possible integration between CPU and GPU — using co-designed cores and unified memory management — will deliver meaningful advantages for AI workloads that no third-party CPU can match.

The 88-core Olympus design is targeting the specific bottlenecks in large-language-model serving: context management, KV cache handling, and the memory-bandwidth-intensive decode phase of autoregressive generation. AMD EPYC Venice (manufactured on TSMC's 2nm process, now in production) offers more general-purpose compute throughput, but NVIDIA is betting that specialization beats raw core count for its primary use case.

Intel, which has been struggling to maintain relevance in the data center AI market following a string of execution missteps, faces a more existential challenge: if Vera displaces x86 as the standard CPU pairing for NVIDIA GPU clusters, the company loses a significant share of its highest-margin server CPU revenue.

## Availability and Competitive Landscape

NVIDIA has committed to general availability in the second half of 2026, with hyperscaler deployments expected to begin in Q3. Manufacturing is split between TSMC's N3 process for the Vera CPU and N2 for the Rubin GPU, representing NVIDIA's first volume production on the most advanced nodes both foundries offer.

The window between now and Rubin GA is the most competitive NVIDIA has faced in years. AMD's MI300X has found genuine traction in inference workloads, and Google's TPU v6 has eliminated the per-query cost gap for Gemini-class models running on Google Cloud. TensorWave's $350M Series B, announced earlier this week, is explicitly targeting enterprises dissatisfied with NVIDIA's pricing and allocation timelines.

Whether Rubin's efficiency claims hold up at production scale — and whether customers can actually procure them without the allocation queues that have plagued Blackwell — will determine whether NVIDIA extends its lead or merely maintains it heading into 2027.
