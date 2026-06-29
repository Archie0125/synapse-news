---
title: "Qualcomm in Talks to Acquire Tenstorrent for Up to $10 Billion in RISC-V Power Play Against Nvidia"
summary: "Qualcomm is in advanced discussions to acquire Tenstorrent, the Canadian RISC-V AI chip startup led by legendary chip architect Jim Keller, for between $8 and $10 billion — a threefold valuation jump in under a year. The deal, if completed, would hand Qualcomm a credible data center AI strategy, deep RISC-V expertise, and one of the most respected chip designers alive."
category: "hardware"
publishedAt: 2026-06-29
lang: "en"
featured: false
trending: false
sources:
  - name: "The Register — Qualcomm Said to Be Circling Tenstorrent in $10B RISC-V Power Play"
    url: "https://www.theregister.com/systems/2026/06/16/qualcomm-said-to-be-circling-ai-chip-biz-tenstorrent-in-10b-risc-v-power-play/5256084"
  - name: "AI Weekly — Qualcomm Targets Tenstorrent in Reported $10B RISC-V Deal"
    url: "https://aiweekly.co/alerts/qualcomm-targets-tenstorrent-in-reported-10b-risc-v-deal"
  - name: "AI Unfiltered — Qualcomm in Talks to Acquire Tenstorrent for $8-10B"
    url: "https://www.arturmarkus.com/qualcomm-in-talks-to-acquire-tenstorrent-for-8-10-billion-jim-kellers-risc-v-ai-chip-startup-valuation-triples-in-one-year/"
  - name: "TechTimes — Qualcomm Bets $14 Billion on Cracking Nvidia's AI Monopoly"
    url: "https://www.techtimes.com/articles/319017/20260624/qualcomm-bets-14-billion-cracking-nvidias-ai-monopoly-risc-v-open-compiler.htm"
tags:
  - "qualcomm"
  - "tenstorrent"
  - "risc-v"
  - "jim-keller"
  - "ai-chips"
  - "acquisition"
  - "hardware"
  - "nvidia"
  - "data-center"
  - "blackhole"
relatedSlugs:
  - "2026-06-29-openai-jalapeno-broadcom-inference-chip-en"
  - "2026-06-29-ai-chip-stock-selloff-june-2026-en"
  - "2026-06-29-onsemi-synaptics-7b-edge-ai-acquisition-en"
---

Qualcomm is in advanced talks to acquire Tenstorrent, the Canadian AI chip startup best known for its RISC-V architecture and its CEO Jim Keller, at a valuation between $8 and $10 billion, according to multiple reports that emerged this month. The Information first broke the story, with Reuters independently confirming shortly after. Neither company has commented publicly, and no deal has been finalized.

But the strategic logic is hard to miss. If the deal closes, it would be the most significant bet Qualcomm has made in years — and a clear signal that the mobile chip giant is done watching the data center AI boom from the sidelines.

## Who Tenstorrent Is

Founded in 2016 and headquartered in Toronto, Tenstorrent has spent a decade pursuing an approach to AI hardware that differs fundamentally from the GPU paradigm Nvidia has refined for three decades. Instead of adapting graphics processors to handle AI workloads, Tenstorrent built from the ground up on the RISC-V instruction set architecture — an open standard that allows chip designers to customize processor cores without paying licensing royalties to Arm or Intel.

The company's flagship product, the Blackhole chip, reached general availability in April 2026. Its computing architecture, built around Tensix cores, takes a different view of how neural network computation should be distributed across silicon. Each Blackhole chip contains 768 RISC-V cores alongside dedicated AI engines and a high-bandwidth interconnect, designed for the kind of distributed inference workloads that large-scale AI deployments require.

The Galaxy Blackhole platform packs 32 Blackhole chips into a 6U server enclosure — a dense, high-throughput configuration aimed at data center customers who want to run large models without the per-chip costs that Nvidia's H-series and B-series GPUs command.

## Why Jim Keller Is the Asset

In any conversation about Tenstorrent, the name Jim Keller comes up first. His track record in semiconductor design is without parallel among active practitioners: he architected AMD's K8 processor, which rescued the company from near-bankruptcy in the early 2000s; designed the Apple A4 and A5 chips that defined the original iPhone's silicon; led AMD's Zen microarchitecture development; built Tesla's Full Self-Driving chip; and served as Intel's head of Silicon Engineering.

At Tenstorrent, Keller has applied that experience to the problem of AI hardware from first principles. His design philosophy emphasizes radical efficiency — extracting maximum compute from minimum power and area — rather than simply scaling up existing architectures. The RISC-V bet reflects a conviction that the future of AI hardware requires open, customizable cores that can be tailored to specific workloads rather than adapted from general-purpose designs.

For Qualcomm, acquiring Tenstorrent isn't just buying a company. It's hiring the most celebrated chip architect of his generation to lead a new front in the company's hardware strategy.

## What Qualcomm Needs

Qualcomm's position in the AI era is a study in successful mobile dominance that didn't translate cleanly to data center opportunity. The Snapdragon SoC family commands the premium Android market and powers the majority of the world's smartphones. But data center AI, the sector that has generated the most dramatic value creation in technology over the past three years, has been essentially Nvidia's world — with some market share taken by AMD, Google's TPUs, and Amazon's Trainium.

Qualcomm has made attempts to enter the data center AI space organically, but the results have been modest. The company's server-class Arm chips have found customers, but not at the scale or pricing that challenges Nvidia in inference or training. Meanwhile, Qualcomm's licensing dispute with Arm Holdings has added strategic urgency to its RISC-V ambitions — owning deep RISC-V capability reduces existential dependence on a supplier the company is actively litigating against.

In December 2025, Qualcomm acquired Ventana Micro Systems, a smaller RISC-V server chip startup, in a move analysts read as a first step toward data center ambitions. The Tenstorrent talks, at 20 to 25 times the estimated size of that earlier deal, represent a dramatically larger commitment.

## The RISC-V Moment

Tenstorrent's RISC-V architecture sits at the center of a broader industry shift that has been accelerating through 2025 and 2026. As the cost of Arm licensing has risen and geopolitical pressure on Western chip design has intensified, the open standard has attracted serious investment from companies including Google, Samsung, Western Digital, and a growing roster of startups.

The appeal is structural: RISC-V allows any company to design custom processors optimized for specific workloads without paying royalties, without negotiating technology access agreements, and without the vendor lock-in risks that come with proprietary ISAs. For AI inference specifically — where the workload characteristics are well-understood and optimization opportunities are large — RISC-V-based designs have the potential to deliver significantly better performance-per-dollar than general-purpose alternatives.

A Qualcomm acquisition would bring RISC-V's most technically credible AI implementation into the arms of a company with the manufacturing relationships, customer access, and capital to scale it. That combination, if executed well, is exactly what would be required to credibly challenge Nvidia in the data center.

## The Uncertainty Ahead

For now, the uncertainty is real. Reports indicate talks are ongoing but with no certainty of completion. The valuation range — $8 to $10 billion — represents a significant premium over Tenstorrent's $3.2 billion funding valuation from mid-2025, a tripling in roughly 12 months that reflects both AI chip euphoria and Tenstorrent's genuine progress in shipping competitive hardware.

Regulatory scrutiny is likely given Qualcomm's existing semiconductor market position, though RISC-V chips currently represent a small enough market share that antitrust concerns may be manageable. More significant may be the question of Jim Keller's own trajectory — whether he would remain to lead a chip division within a larger corporation, or whether a sale would represent an exit that accelerates his eventual departure.

What isn't in doubt is the direction of travel. As OpenAI builds its Jalapeño inference chip, as Apple runs 20-billion-parameter models on iPhone flash storage, and as onsemi moves to acquire Synaptics for edge AI at the endpoint, the AI hardware market is fragmenting from Nvidia's near-monopoly toward a diverse ecosystem of purpose-built silicon. Qualcomm, if it buys Tenstorrent, is making a very large bet on being a central player in that new world.

---

*Talks are ongoing and no deal has been announced. Reuters and The Information first reported the discussions in June 2026.*
