---
title: "Raja Koduri's Oxmiq Labs Raises $35M to Make Custom AI Silicon Accessible to Any Chipmaker"
summary: "Oxmiq Labs, founded by former Intel and AMD chip architect Raja Koduri, has closed a $35 million Series A to scale its licensable GPU and AI architecture platform OxCore. The startup is betting that the real bottleneck in the AI chip race is not fabrication capacity but design cost — and that a licensable architecture can open custom AI silicon to companies that couldn't afford to build it from scratch."
category: "hardware"
publishedAt: 2026-07-05
lang: "en"
featured: false
trending: false
sources:
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/07/01/raja-koduris-oxmiq-labs-raises-35m-lower-design-cost-custom-ai-silicon/"
  - name: "Tech Startups"
    url: "https://techstartups.com/2026/07/01/raja-koduris-ai-startup-oxmiq-raises-35m-to-build-ai-chip-architecture-that-cuts-the-cost-of-custom-ai-silicon/"
  - name: "HPCwire"
    url: "https://www.hpcwire.com/off-the-wire/oxmiq-raises-35m-to-scale-oxcoretm-architecture/"
  - name: "Yahoo Finance"
    url: "https://finance.yahoo.com/technology/ai/articles/oxmiq-raises-35-million-scale-131500901.html"
tags:
  - "Oxmiq"
  - "Raja Koduri"
  - "GPU architecture"
  - "custom silicon"
  - "AI chip"
  - "Series A"
  - "Samsung Catalyst Fund"
  - "MediaTek"
  - "OxCore"
relatedSlugs:
  - "2026-07-05-anthropic-samsung-custom-ai-chip-talks-en"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-en"
  - "2026-07-01-etched-5b-valuation-1b-sales-inference-chip-en"
---

Raja Koduri has spent his career inside the largest chip companies in the world — first as a key graphics architect at AMD, then as Chief Architect and Executive Vice President at Intel, where he led the company's ambitions to re-enter the discrete GPU market. Now, with his startup Oxmiq Labs, he is betting that the most important gap in the AI chip industry is not at the manufacturing layer but at the design layer — and that a licensable GPU architecture can lower the barrier to custom AI silicon dramatically.

Oxmiq announced on July 1, 2026 that it has closed a $35 million Series A round, bringing total capital raised to $60 million since the company's founding. The round was co-led by Fundomo and Samsung Catalyst Fund, with strategic participation from MediaTek, AM Intelligence Labs, Pegatron Venture Capital, CDIB-TEN, Darwin Ventures, and Morgan Creek Digital.

## The Problem Oxmiq Is Solving

Building a custom AI chip from scratch is extraordinarily expensive. The design cost alone — before taping out a single wafer — routinely runs into the hundreds of millions of dollars when factoring in engineering headcount, EDA software licenses, IP licensing fees, and the iterative design cycles required to reach production quality. That cost is why custom AI silicon has historically been the domain of hyperscalers: companies like Google (TPU), Amazon (Trainium/Inferentia), Microsoft (Maia), and now OpenAI, whose scale makes the multi-year investment economically rational.

Everyone else — semiconductor companies, enterprise AI infrastructure providers, national defense programs, regional cloud operators — has faced a choice between paying Nvidia's prices or undertaking a prohibitively expensive design program. Oxmiq's thesis is that there is a third path: license a proven, production-tested GPU architecture and build from there.

OxCore is Oxmiq's answer to that gap. It consolidates three traditionally separate components — GPUs, central processing units, and a custom tensor engine optimized for AI matrix operations — into a single licensable intellectual property block. Companies that license OxCore can build custom chips tailored to their specific workloads without designing the foundational architecture from scratch, dramatically compressing both the cost and the time-to-market.

## OxQuilt and the Software Layer

Oxmiq's approach extends beyond the core architecture. The company has also developed OxQuilt, a computing fabric that combines heterogeneous chiplets and memory into a single integrated package, with configuration tools that allow designers to adapt the design to different supply chains and manufacturing constraints. This is particularly relevant in the current environment, where supply chain resilience has become a design requirement, not an afterthought.

The software story is equally important. One of the deepest moats Nvidia has built over the past decade is not its hardware — it's CUDA, the programming model that has attracted millions of developers and locked an enormous amount of AI workload code to Nvidia's ecosystem. Oxmiq's OxPython is a direct attempt to address this lock-in: it allows existing CUDA and PyTorch code to run on OxCore-based hardware without modification, lowering the migration barrier for developers and potential customers.

OxCapsule, the orchestration layer, handles deployment and management across distributed OxCore-based clusters — the infrastructure plumbing that enterprise customers need before they can realistically evaluate switching from established platforms.

## Why the Investor Mix Matters

The composition of Oxmiq's Series A investor syndicate tells a strategic story. Samsung Catalyst Fund — Samsung's corporate venture arm — is a lead investor, and Samsung's foundry operations are a natural manufacturing partner for any company that licenses OxCore and wants to produce chips at scale. MediaTek, the Taiwanese semiconductor company that produces chips for smartphones, automotive, and increasingly AI edge applications, brings both a potential customer and an insight into what licensable architecture economics look like in practice.

Pegatron Venture Capital represents Taiwan's hardware manufacturing ecosystem directly. Pegatron, the contract manufacturer responsible for assembling a large share of the world's consumer electronics, has been actively investing in AI chip infrastructure as part of a strategic push to move up the value chain from assembly toward components. For Oxmiq, Pegatron's involvement opens potential pathways to customers across the Asian hardware supply chain.

The combination of a foundry partner (Samsung), a logic chip customer (MediaTek), and a contract manufacturer (Pegatron) suggests that Oxmiq is building toward an ecosystem, not just a product. The strategic goal appears to be positioning OxCore as the ARM of AI silicon — a licensable architecture that sits beneath many different end-products rather than competing directly with any of them.

## Koduri's Bet Against the GPU Monopoly

Raja Koduri has thought about this market for a very long time. At AMD, he led the team that brought Radeon graphics to competitive parity with Nvidia across multiple generations. At Intel, he was given enormous resources to build the Arc GPU line and was tasked with breaking Nvidia's stranglehold on professional graphics and AI compute. Neither effort succeeded as fully as hoped — and Koduri departed Intel in late 2023 with a clear-eyed understanding of what makes Nvidia's position so difficult to displace.

His conclusion appears to be that competing head-on with Nvidia at the high end is a losing game for most players. The better play is to expand the market — to make custom AI silicon accessible to the companies that currently have no viable alternative to paying Nvidia — and to position Oxmiq's intellectual property at the center of that expansion.

"By bringing that cost down, you widen who gets to build with it," Koduri said in announcing the funding round. The ambition is not to replace Nvidia but to build the infrastructure that enables the next generation of competitors to exist.

## The Market Timing

Oxmiq's Series A closes at a moment when the custom AI silicon market is moving faster than at any previous point. Anthropic just entered preliminary chip talks with Samsung. Etched, another AI chip startup, recently achieved a $5 billion valuation on $1 billion in reported sales. Qualcomm is reportedly in talks to acquire RISC-V chip startup Tenstorrent for up to $10 billion.

Against that backdrop, a $35 million Series A for a licensable architecture company is a relatively modest bet with an unusually asymmetric upside profile. If OxCore gains adoption even among a small fraction of the companies currently planning custom AI chips, the licensing revenue at scale could be substantial — and Koduri's expertise in both the technical and commercial sides of chip architecture gives Oxmiq credibility that most early-stage hardware startups simply cannot claim.

The AI chip wars are widening. Oxmiq is betting that democratizing chip design will eventually prove more durable than winning any single design competition.
