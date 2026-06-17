---
title: "Qualcomm in Talks to Acquire AI Chip Startup Tenstorrent for Up to $10 Billion"
summary: "Qualcomm is in advanced negotiations to buy Tenstorrent, the AI chip startup led by legendary chip designer Jim Keller, in a deal that could value the company at $8–10 billion. The potential acquisition would mark Qualcomm's most aggressive move yet into the datacenter AI acceleration market and hand the RISC-V ecosystem its most consequential corporate win to date."
category: "hardware"
publishedAt: 2026-06-17
lang: "en"
featured: true
trending: true
sources:
  - name: "The Register"
    url: "https://www.theregister.com/systems/2026/06/16/qualcomm-said-to-be-circling-ai-chip-biz-tenstorrent-in-10b-risc-v-power-play/5256084"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-mulls-taking-over-jim-kellers-tenstorrent-report-claims-deal-for-ai-chipmaker-would-value-the-company-at-between-usd8-billion-and-usd10-billion"
  - name: "GuruFocus"
    url: "https://www.gurufocus.com/news/8918836/qualcomm-qcom-explores-8b10b-acquisition-of-ai-chip-startup-tenstorrent"
  - name: "Invezz"
    url: "https://invezz.com/news/2026/06/16/qualcomm-stock-rises-on-ai-chip-push-tenstorrent-deal-speculation/"
tags:
  - "Qualcomm"
  - "Tenstorrent"
  - "Jim Keller"
  - "RISC-V"
  - "AI chips"
  - "semiconductors"
  - "datacenter"
  - "NVIDIA alternative"
relatedSlugs:
  - "2026-06-14-nvidia-sk-hynix-ai-memory-partnership-en"
  - "2026-04-03-riscv-ai-accelerators-en"
  - "2026-04-03-nvidia-blackwell-supply-en"
---

On a Monday that saw Qualcomm's stock jump more than four percent in premarket trading, news emerged that the San Diego chipmaker is in advanced negotiations to acquire Tenstorrent — the Canadian AI chip startup founded and led by Jim Keller, one of the most storied hardware engineers in Silicon Valley history. The deal, first reported by The Information, would value Tenstorrent at between $8 billion and $10 billion, making it one of the largest AI chip acquisitions ever attempted.

Neither company has confirmed the talks. Qualcomm's next scheduled public event is its Investor Day on June 24, which is widely seen as the likely venue for a formal announcement if negotiations succeed.

## Who Is Tenstorrent?

Founded in 2016 and headquartered in Santa Clara with major engineering operations in Toronto, Tenstorrent has spent a decade quietly building what it calls a fundamentally different approach to AI compute. Unlike NVIDIA's GPU-based architecture or Google's TPUs, Tenstorrent builds its accelerators entirely on the RISC-V instruction set architecture — a freely licensed, open standard that any company can implement without paying royalties to a proprietary licensor.

The company's current flagship product, the Galaxy Blackhole AI compute platform, packs 32 accelerators into a 6U rack enclosure, with each accelerator containing 768 RISC-V cores. The design philosophy prioritizes flexibility and programmability over raw throughput — a deliberate bet that the next generation of AI workloads will require more nuanced, task-specific compute rather than brute-force matrix multiplication.

What makes Tenstorrent genuinely unusual in the crowded AI chip space is its software stack. The company has invested heavily in compilers and tooling that allow its hardware to run models without the CUDA ecosystem that effectively locks most AI practitioners into NVIDIA's platform. This has been a meaningful differentiator: several hyperscalers and defense contractors have tested Tenstorrent's systems precisely because they want a credible path off NVIDIA dependency.

## The Jim Keller Factor

Jim Keller has an engineering biography that few in the industry can match. He architected AMD's K7 and K8 processor families — the designs that briefly put AMD ahead of Intel in the early 2000s. He then moved to Apple, where he led the team that built the A4 and A5 chips that powered the original iPhone and iPad. He joined Tesla from 2016 to 2018 to lead Autopilot hardware development, then spent two years as Intel's Senior Vice President of Silicon Engineering before joining Tenstorrent as CEO.

Within the chip industry, Keller occupies a category usually reserved for musicians or athletes: the rare designer who can demonstrably change the trajectory of an organization's products. Companies hire him when they need transformational chip design, not incremental improvement.

That track record is a significant part of what Qualcomm would be paying for. Tenstorrent's patent portfolio and its assembled engineering team — drawn from AMD, Apple, Intel, Tesla, and others — represent exactly the kind of concentrated talent that cannot be replicated by hiring in the open market.

## Qualcomm's Strategic Logic

Qualcomm derives the overwhelming majority of its revenue from Snapdragon processors for smartphones and increasingly for Windows PCs. That market is mature, competitive, and increasingly under pressure from Apple's M-series silicon on the high end and commoditized ARM designs on the low end. The AI PC wave has been a meaningful tailwind, but it does not, by itself, justify a $10 billion acquisition.

What Qualcomm actually wants is a credible story in the datacenter AI acceleration market — the segment currently dominated by NVIDIA with over 80% market share, where the top seven hyperscalers are collectively spending more than $200 billion on AI infrastructure this year alone. Qualcomm CEO Cristiano Amon has been publicly bullish on AI silicon for two years, but the company has lacked a competitive datacenter product.

Tenstorrent provides that product. More importantly, it provides it on RISC-V, which aligns with a second strategic objective: reducing Qualcomm's dependence on ARM Holdings. Qualcomm and ARM have been embroiled in a protracted licensing dispute that has cast uncertainty over Qualcomm's architecture roadmap. Acquiring Tenstorrent would accelerate Qualcomm's ability to pivot toward an open-architecture future where it controls its own instruction set destiny.

There is also a market timing argument. The AI chip market is entering what analysts call a "NVIDIA alternative trade" — a period in which hyperscalers, governments, and large enterprises are actively seeking to diversify their supply chains away from a single dominant vendor. Qualcomm, with its manufacturing relationships, global sales infrastructure, and brand recognition, is better positioned than almost any other non-NVIDIA vendor to capitalize on that demand — but only if it has compelling silicon to sell.

## The RISC-V Power Play

The most significant structural consequence of this acquisition, if it closes, would be for the RISC-V ecosystem rather than for Qualcomm itself.

RISC-V has been growing rapidly as an instruction set architecture — particularly in embedded systems, edge devices, and sovereign compute initiatives (China's homegrown chip efforts, India's national semiconductor program, and the EU's chips ambitions all have significant RISC-V components). But it has lacked a flagship success story in high-performance AI compute.

A Qualcomm-backed Tenstorrent with access to the world's most advanced semiconductor fabrication relationships and a global enterprise sales network would be the RISC-V ecosystem's most powerful commercial proof point. It would signal, concretely, that RISC-V can compete at the top of the AI inference market — not just in constrained edge devices.

The Register described the deal as "a $10B RISC-V power play," and that framing may prove more accurate in the long run than the headline about Qualcomm's datacenter ambitions.

## What Comes Next

The talks are described as advanced but not finalized. Deals at this scale and complexity routinely fall apart over valuation disagreements, regulatory concerns, or simply the difficulty of aligning two organizations with very different cultures. Qualcomm has a history of ambitious M&A attempts — most famously its failed $44 billion bid for NXP Semiconductors — that ultimately did not close.

Antitrust scrutiny is also a legitimate question. While Tenstorrent does not hold dominant market positions that would obviously trigger horizontal competition concerns, the Biden-era regulatory approach to chip industry consolidation was aggressive, and the current regulatory environment remains unpredictable.

If the deal does close, it will almost certainly be announced at Qualcomm's Investor Day on June 24. The market will be watching whether Qualcomm presents Tenstorrent as a datacenter play, a RISC-V platform, or — most ambitiously — both. The price tag implies it believes the answer is both.

For an industry watching NVIDIA's H100 and B200 backorders stretch into 2027, the prospect of a well-capitalized, enterprise-ready RISC-V AI accelerator backed by a $40 billion company is not a marginal story. It may be the most consequential chip deal of the decade.
