---
title: "NVIDIA and SK Hynix Forge Multi-Year AI Memory Partnership for Next-Gen AI Factories"
summary: "NVIDIA and SK Hynix announced a sweeping multi-year technology partnership to co-develop next-generation memory for AI factories, spanning Vera Rubin supercomputers, RTX Spark PCs, and Jetson Thor robotics platforms. The deal deepens vertical integration in the AI supply chain and signals that memory — long a commodity — is now a strategic battleground."
category: "hardware"
publishedAt: 2026-06-14
lang: "en"
featured: true
trending: false
sources:
  - name: "NVIDIA Newsroom"
    url: "https://nvidianews.nvidia.com/news/sk-hynix-ai-factory"
  - name: "SK Hynix Newsroom"
    url: "https://news.skhynix.com/multi-year-tech-partnership-with-nvidia/"
  - name: "GlobeNewswire"
    url: "https://www.globenewswire.com/news-release/2026/06/07/3307752/0/en/NVIDIA-and-SK-hynix-Announce-Multiyear-Technology-Partnership-to-Advance-Memory-for-AI-Factories.html"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-06-07/nvidia-sk-hynix-sign-multi-year-pact-to-develop-next-gen-chips"
tags:
  - "NVIDIA"
  - "SK Hynix"
  - "HBM"
  - "AI infrastructure"
  - "semiconductors"
  - "memory"
  - "Vera Rubin"
relatedSlugs:
  - "2026-06-14-anthropic-overtakes-openai-aws-5gw-compute-deal-en"
  - "2026-06-12-oracle-fy2026-q4-ai-capex-shock-en"
---

When Jensen Huang talks about AI factories as "the engines of the next industrial revolution," he is talking about infrastructure at a scale that strains every link in the supply chain — and none more than memory. On June 7, NVIDIA and South Korea's SK Hynix formalized what both companies described as a multi-year technology partnership to co-develop next-generation memory for AI factories. The announcement redraws the line between chip supplier and strategic partner, and signals that the memory bottleneck in AI compute is no longer an afterthought.

## What the Partnership Actually Covers

The agreement goes well beyond a standard volume purchase deal. According to both companies' official releases, the collaboration has three distinct pillars.

The first is **memory co-development**: SK Hynix will design and supply advanced memory for NVIDIA's full product stack — Vera Rubin AI supercomputers, Vera CPUs, RTX Spark-powered AI PCs, and Jetson Thor robotic computing platforms. This covers everything from datacenter GPU clusters down to edge devices and humanoid robotics, a vertical span that few partnerships match.

The second pillar is **semiconductor design acceleration**. NVIDIA and SK Hynix will use NVIDIA's own tools — the CUDA-X libraries and the PhysicsNeMo physics simulation framework — to speed up technology computer-aided design (TCAD) workflows, computational lithography, and custom in-house simulation codes. In plain terms: SK Hynix will apply NVIDIA's AI to make better NVIDIA memory, faster.

The third is **autonomous fab operations**. SK Hynix will build factory digital twins using NVIDIA Omniverse and OpenUSD, and integrate NVIDIA cuOpt to run fully autonomous fab optimization. The stated goal is to progressively replace human scheduling loops in semiconductor fabrication with AI-driven orchestration — a vision that echoes NVIDIA's broader pitch for physical AI.

## Why Memory Is Now Strategic

For most of the past decade, high-bandwidth memory (HBM) was treated as a commodity specification: you listed your gigabytes and bandwidth, picked your supplier, and moved on. The AI build-out changed that calculus dramatically.

HBM is the most capacity-constrained component in today's AI accelerators. A single H100 GPU uses six HBM3 stacks totaling 80 GB; a Blackwell B200 doubles that to 192 GB of HBM3e. Demand for HBM surged roughly 80% year-over-year in 2025 and is projected to double again through 2027, according to multiple analyst estimates. SK Hynix, Samsung, and Micron are the only companies capable of producing it at scale, giving them enormous negotiating leverage — and enormous responsibility when supply slips.

The multi-year commitment locks in supply alignment ahead of NVIDIA's Vera Rubin ramp, expected to begin sampling in late 2026 and hit volume production in 2027. For NVIDIA, the strategic logic is obvious: a predictable memory supply pipeline reduces the risk of the kind of allocation bottlenecks that constrained H100 shipments in 2023 and 2024.

For SK Hynix, the upside is structural. "Together, we are co-developing the next generation of memory for AI factories and applying AI to how we design and manufacture semiconductors," said SK Group Chairman Chey Tae-won. Participating in NVIDIA's design process — rather than receiving a spec sheet to build against — positions SK Hynix higher in the value chain and should translate into better margins and longer product cycles.

## The Vera Rubin Architecture Bet

Central to the partnership is NVIDIA's Vera Rubin platform, the successor to Blackwell. Vera Rubin pairs a new Rubin GPU with NVIDIA's first in-house CPU — Vera — in a tightly integrated rack-scale design. Memory bandwidth is the defining constraint of the architecture: early performance projections suggest Rubin will require HBM4 or HBM4E with bandwidth exceeding 8 TB/s per GPU, roughly triple what HBM3E provides.

Developing memory at that specification requires deep collaboration between chip and memory designers from the earliest stages, not just at the final integration step. That is the practical reason for the partnership's scope. Co-development means SK Hynix engineers are working in NVIDIA's design toolchain, and NVIDIA's teams have visibility into SK Hynix's fabrication roadmap — a level of integration more typical of an acquisition than a supply agreement.

## Autonomous Fabs: The Longer Bet

Perhaps the most ambitious element of the deal is the shared vision for AI-driven semiconductor manufacturing. Chip fabrication is one of the most complex industrial processes on Earth, involving hundreds of process steps and tolerances measured in single-digit nanometers. Today, expert engineers make millions of scheduling and process control decisions per day; mistakes are expensive and sometimes irreversible.

Both companies believe AI can take over substantial portions of that decision-making. SK Hynix's factory digital twins — virtual replicas of physical fabs — will let NVIDIA's Omniverse platform simulate process changes before committing to them on the actual line. NVIDIA cuOpt, an optimization engine originally built for logistics, will handle real-time fab scheduling. The endgame is a fab that adjusts its own processes continuously, catching defect patterns faster than human operators can and reoptimizing throughput without human intervention.

Whether that vision is achievable at the complexity of leading-edge DRAM fabrication remains to be proven. But the direction is clear: NVIDIA is not just building chips for AI factories; it is proposing to build AI-run factories for its chips.

## Competitive Implications

The partnership puts pressure on Samsung, SK Hynix's chief HBM rival. Samsung has struggled with HBM3E yield issues that cost it NVIDIA qualification in 2024, and has been working to recover ground. A deepened SK Hynix-NVIDIA collaboration — one where SK Hynix has early access to next-generation spec requirements — makes it harder for Samsung to catch up purely on technical merit. Samsung would need a similar design partnership with another major GPU vendor, likely AMD, to offset the disadvantage.

For the broader AI infrastructure ecosystem, the deal reinforces the pattern of vertical deepening. Amazon builds custom silicon (Trainium, Inferentia). Google has its own TPUs. Microsoft is designing Maia AI chips. NVIDIA, despite sitting at the top of the discrete GPU market, is now tying its memory supply chain more tightly to a single partner. The age of commodity AI components is, at least at the frontier, ending.

## What Comes Next

Both companies declined to disclose financial terms, and NVIDIA's investor relations team noted the partnership covers "extended development cycles" typical of leading-edge memory programs — meaning the roadmap extends at minimum through the Vera Rubin generation and likely beyond. SK Hynix's Icheon and Cheongju fabs in South Korea will be the primary manufacturing sites.

The first commercial products under the partnership — HBM4 memory for Vera Rubin systems — are expected to enter production in 2027. Industry watchers will be looking for signs of the autonomous fab technology arriving even sooner, given both companies' aggressive public timelines for AI-driven manufacturing.

For investors, the partnership confirms SK Hynix's position as the preferred NVIDIA memory supplier ahead of the next major architecture cycle — a position that carries both premium pricing power and concentration risk if NVIDIA's own roadmap slips.
