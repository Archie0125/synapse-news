---
title: "Qualcomm in Advanced Talks to Acquire Tenstorrent for Up to $10 Billion in RISC-V Power Play"
summary: "Qualcomm is in advanced acquisition talks with AI chip startup Tenstorrent, valuing Jim Keller's company at $8 to $10 billion—a 3x jump from its valuation just one year ago. The deal would give Qualcomm a full AI silicon stack alongside its recent Modular compiler acquisition, mounting the most credible open-architecture challenge to NVIDIA's dominance yet."
category: "hardware"
publishedAt: 2026-06-26
lang: "en"
featured: false
trending: true
sources:
  - name: "The Register"
    url: "https://www.theregister.com/systems/2026/06/16/qualcomm-said-to-be-circling-ai-chip-biz-tenstorrent-in-10b-risc-v-power-play/5256084"
  - name: "Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/qualcomm-considers-acquiring-ai-chip-firm-tenstorrent/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/319017/20260624/qualcomm-bets-14-billion-cracking-nvidias-ai-monopoly-risc-v-open-compiler.htm"
  - name: "AI Unfiltered"
    url: "https://www.arturmarkus.com/qualcomm-in-talks-to-acquire-tenstorrent-for-8-10-billion-jim-kellers-risc-v-ai-chip-startup-valuation-triples-in-one-year/"
tags:
  - "qualcomm"
  - "tenstorrent"
  - "RISC-V"
  - "ai chips"
  - "acquisition"
  - "jim keller"
  - "hardware"
relatedSlugs:
  - "2026-06-24-qualcomm-modular-4b-acquisition-nvidia-moat-en"
  - "2026-06-25-nvidia-vera-rubin-nvl72-78m-rack-memory-cost-en"
---

The AI chip industry may be on the verge of its biggest acquisition in years. Qualcomm is in advanced negotiations to acquire Tenstorrent, the RISC-V-based AI accelerator startup led by semiconductor legend Jim Keller, for between $8 billion and $10 billion — a valuation that has tripled in roughly twelve months.

The deal, first reported by Reuters on June 15, 2026, and independently confirmed by multiple publications, would represent one of the largest AI hardware acquisitions in history. If it closes, it would also mark Qualcomm's most aggressive move yet in its campaign to challenge NVIDIA's commanding grip on the AI infrastructure market.

## Who Is Tenstorrent?

Founded in 2016, Tenstorrent has been building AI accelerator hardware based on RISC-V, the open-source instruction set architecture that has become a rallying point for companies seeking an alternative to Arm-licensed and x86 designs. The company operates in a market where NVIDIA and AMD compete on proprietary silicon ecosystems, and Tenstorrent has carved a distinct position by betting that the open architecture model — widely successful in software through Linux and open-source frameworks — can work in hardware too.

The man behind that bet is Jim Keller, one of the most storied chip architects in Silicon Valley history. Keller designed AMD's K8 processor, the chip that introduced 64-bit computing to x86 and nearly bankrupted Intel in the mid-2000s. He architected Apple's A4 and A5 processors, launching the era of in-house ARM chips that made iPhone the world's most profitable product line. He designed AMD's Zen architecture, which resurrected the company from near-irrelevance to genuine competitiveness with Intel. He built Tesla's Full Self-Driving chip. And he served as Intel's SVP of Silicon Engineering before departing in 2020 to join Tenstorrent as CEO.

Tenstorrent's flagship product, the **Galaxy Blackhole** platform — launched earlier in 2026 — packs 32 AI accelerators into a single 6U data center enclosure. Each accelerator contains 768 RISC-V cores, yielding massive parallelism for both inference and mid-scale training workloads. The platform is designed to give enterprises an alternative to NVIDIA's H-series GPUs without paying NVIDIA's premium or accepting its proprietary software lock-in.

## A Valuation That Tripled in Twelve Months

The numbers make clear how dramatically the AI chip landscape shifted over the past year. Just twelve months ago, Tenstorrent was seeking approximately $800 million in a funding round at a $3.2 billion post-money valuation. The company had shipped hardware, attracted engineering talent, and built customer pipeline — but was still a mid-stage startup by AI infrastructure standards.

In the intervening period, the AI hardware shortage intensified, RISC-V gained credibility with major deployments, Galaxy Blackhole shipped, and the market's appetite for any credible alternative to NVIDIA expanded dramatically. Now Qualcomm is reportedly willing to pay up to $10 billion — a 3.1x premium over last year's fundraising valuation, and roughly 12.5x what Tenstorrent sought to raise in that round.

The deal structure reportedly includes performance milestone payments tied to roadmap execution — a standard mechanism for chip startup acquisitions where technical promises must eventually translate to shipping, deployed silicon.

## Qualcomm's Two-Part Strategy Against NVIDIA

The strategic logic of the Tenstorrent acquisition becomes significantly clearer when viewed alongside Qualcomm's other recent moves.

In June 2026, Qualcomm announced a **$4 billion acquisition of Modular Inc.**, a compiler technology company that owns key MLIR-based toolchain infrastructure sitting between AI frameworks (PyTorch, JAX) and chip hardware. Modular's compiler technology is what enables developers to target multiple hardware backends from a single codebase — a critical piece of infrastructure for any ecosystem hoping to displace NVIDIA's CUDA.

Tenstorrent would give Qualcomm the chip itself. Together, a Qualcomm that owns both Modular and Tenstorrent would control an end-to-end AI silicon stack: the compiler that translates models into hardware instructions, and the accelerator that executes them. It's the same vertical integration strategy that made NVIDIA so hard to displace — CUDA, cuDNN, TensorRT, and GPU hardware all developed in tandem.

"RISC-V is Nvidia's blind spot," one analyst told The Register. "They've built their moat on proprietary everything — CUDA, NVLink, the memory subsystem. RISC-V by definition can't be proprietary, and companies like Qualcomm see that as an opportunity to build an ecosystem rather than just a product."

The RISC-V angle also has geopolitical dimensions. Because RISC-V is an open standard not subject to US export license requirements in the same way that Arm-licensed designs are, RISC-V accelerators have become increasingly attractive in non-US markets — particularly China, where Alibaba, Huawei, and various state-backed institutes have been building RISC-V competency aggressively. A Qualcomm-Tenstorrent combination could serve both Western enterprise markets and, through appropriate channels, markets where US architectural IP restrictions create friction.

## Intel in the Wings

The acquisition isn't a simple bilateral deal. Bloomberg reported in May 2026 that Intel had separately approached Tenstorrent as an acquisition target, creating competitive bidding dynamics that almost certainly helped push the asking price toward $10 billion.

For Intel, a Tenstorrent acquisition would serve different strategic purposes. Intel is in the middle of an expensive foundry turnaround, and acquiring a prominent RISC-V AI chip startup would demonstrate that its process nodes can attract marquee custom chip customers — while also potentially integrating with Intel's existing Gaudi AI accelerator line.

But Intel's financial position is considerably more constrained than Qualcomm's right now. The company is managing billions in restructuring costs, and a $10 billion acquisition would face intense scrutiny from its board and investors already questioning the pace of its turnaround. Qualcomm, by contrast, has strong free cash flow and a balance sheet that can absorb this deal.

## What Happens to Jim Keller?

Perhaps the most intriguing open question is what a Qualcomm acquisition would mean for Keller himself. His tenure at companies tends to follow a recognizable pattern: design the architecture, oversee the key milestones, and eventually move on. He stayed at Apple through the A5. He left AMD after Zen shipped. He departed Intel within two years.

Keller hasn't commented publicly on the acquisition talks. Deal structures for founder-led technology companies often include retention agreements that commit key technical leadership for two to four years post-acquisition. Whether those golden handcuffs would hold someone with Keller's track record and optionality is a separate question.

If he stays, Qualcomm gets one of the most productive chip architects alive at the helm of its most important new business. If he leaves, it inherits a strong team, a coherent roadmap, and a customer pipeline — but loses the creative vision that built them.

## What It Would Mean for NVIDIA

Neither Qualcomm nor Tenstorrent has confirmed the deal, and acquisition talks at this stage frequently fall through. But the semiconductor industry is watching closely, because the implications of a completed deal would be significant.

NVIDIA's dominance in AI compute rests on three mutually reinforcing factors: hardware performance, software ecosystem (CUDA), and supply chain relationships built over two decades. Individually, none of these advantages is permanent. Collectively, they've proven nearly impossible to attack.

A Qualcomm that owns both the best open-architecture AI chip company (Tenstorrent) and the best cross-platform AI compiler stack (Modular) would be taking aim at all three simultaneously: competing on hardware performance, offering a software-defined alternative to CUDA lock-in, and leveraging Qualcomm's existing relationships with hyperscalers, OEMs, and telecommunications customers to build a distribution channel NVIDIA doesn't naturally own.

That's a credible strategy. Whether it's a winning one depends on execution — and on how much of Jim Keller's talent travels with the deal.
