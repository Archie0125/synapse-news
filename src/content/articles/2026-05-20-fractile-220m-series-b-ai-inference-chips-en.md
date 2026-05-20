---
title: "UK Startup Fractile Raises $220M to Solve AI's Inference Bottleneck with In-Memory Chips"
summary: "London-based Fractile has raised $220 million in a Series B round led by Accel, Factorial Funds, and Founders Fund, hitting a $1 billion post-money valuation. The company is building inference chips that co-locate memory and compute on a single die — eliminating the expensive DRAM bottleneck that slows and inflates the cost of running frontier AI models. Anthropic is reportedly in early talks to become a customer."
category: "hardware"
publishedAt: 2026-05-20
lang: "en"
featured: false
trending: true
sources:
  - name: "Tech.eu"
    url: "https://tech.eu/2026/05/13/uk-ai-chip-startup-fractile-raises-220m-to-tackle-the-growing-inference-bottleneck/"
  - name: "Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/fractile-raises-220m-to-accelerate-development-of-ai-inference-chips/"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-in-early-talks-to-buy-inference-chips-from-uk-startup-fractile"
  - name: "Fractile"
    url: "https://www.fractile.ai/news/fractile-raises-220m-to-build-the-next-generation-of-inference-hardware"
tags:
  - "Fractile"
  - "AI chips"
  - "inference"
  - "hardware"
  - "UK startups"
  - "semiconductors"
  - "Series B"
  - "Anthropic"
relatedSlugs:
  - "2026-05-18-tsmc-n2-2nm-chip-ramp-ai-hardware-en"
  - "2026-05-05-cerebras-ipo-40b-nasdaq-en"
  - "2026-04-03-riscv-ai-accelerators-en"
---

The AI industry's spending problem has two faces. Training new models demands massive compute clusters and months of GPU time — a cost that gets most of the headlines. But inference, the act of running trained models to generate actual responses, is fast becoming the larger and more persistent expense. Every ChatGPT query, every Gemini API call, every Claude conversation — all of it runs on inference infrastructure, and the cost is compounding as usage scales.

London-based **Fractile** has raised **$220 million** in a Series B funding round to address exactly this problem. The round, announced on May 13, 2026, was led by Accel, Factorial Funds, and Founders Fund, with participation from Conviction, Felicis, 8VC, Gigascale, O1A, Buckley Ventures, Kindred Capital, NATO Innovation Fund, and Oxford Science Enterprises. The round values Fractile at $1 billion post-money.

## The Technical Problem Fractile Is Solving

Today's AI inference hardware is dominated by Nvidia GPUs, which are powerful but architecturally designed for a different era. They rely on separate, external DRAM (dynamic random-access memory) to hold the model weights and intermediate state required to run inference. Every time the chip needs to access a weight — which happens constantly during token generation — it has to fetch that data from DRAM across a high-bandwidth memory bus.

This back-and-forth between processor and memory is the inference bottleneck. It consumes energy, introduces latency, and limits the speed at which tokens can be generated. As models grow larger — frontier models now exceed hundreds of billions of parameters — the memory bandwidth requirement grows proportionally, and the cost of satisfying it with high-capacity DRAM explodes.

Fractile's approach is to eliminate this separation entirely. The company is building chips based on **in-memory compute**: the calculation happens directly inside the memory itself, using SRAM (static random-access memory) that is co-located with the processing logic on the same silicon die. Instead of shuttling data between a GPU and external DRAM, the data stays put and the computation comes to it.

"We want to radically accelerate frontier model inference," said CEO Walter Goodwin in the company's fundraise announcement. "The memory wall is the fundamental constraint in running large models economically at scale, and our architecture is designed to remove it."

## The Founders and Their Pedigrees

Fractile was founded in 2022 by **Walter Goodwin** and **Yuhang Song**. Goodwin, who serves as CEO, was completing a PhD at the University of Oxford's Robotics Institute when he founded the company. The Oxford connection runs deep in Fractile's investor roster: Oxford Science Enterprises is among the Series B backers, and former Acorn Computers and Arm executive **Stan Boland** — one of the architects of the architecture that now runs inside virtually every mobile device on earth — invested personally. **Hermann Hauser**, the co-founder of Arm, also appears on the cap table.

Other notable individual investors include **Amar Shah**, co-founder of Wayve (the autonomous driving startup that raised over $1 billion from Nvidia and SoftBank in 2024), and **Pat Gelsinger**, the former Intel CEO who spent four years attempting to revive Intel's manufacturing operations before his departure in late 2024.

The presence of Gelsinger and Boland is more than symbolic. These are engineers who built generations of computing architecture and understand at a molecular level what it takes to design, manufacture, and bring to market a chip that can compete with established incumbents. Their investment signals belief in the technical viability of Fractile's approach.

## Why SRAM Over DRAM?

SRAM is faster and more energy-efficient than DRAM for active computation — but it's also larger and more expensive per bit. The conventional wisdom has been that it's impractical to put enough SRAM on-die to hold the weights of a large frontier model. Fractile's bet is that advances in chip density, aggressive model compression techniques, and architectural innovations in how weights are managed can make SRAM-based inference not just viable but economically superior at the inference scale AI labs now require.

A report from Tom's Hardware noted that **Anthropic** has held early discussions with Fractile about purchasing the startup's chips for inference workloads when they become available, which the company is targeting for 2027. If accurate, this would be significant: Anthropic's Claude 3.5 models are among the most computationally demanding inference workloads in production, and an endorsement from Anthropic would signal that Fractile's architecture can operate at frontier scale, not just in lab conditions.

## The Competitive Landscape

Fractile enters a market that is both more open and more crowded than it was two years ago. Nvidia's inference dominance remains massive — its H100 and H200 chips power the majority of production AI inference globally. But the inference-specific chip category has attracted a wave of new entrants:

- **Cerebras**, which went public on Nasdaq in May 2026, uses a wafer-scale chip architecture to achieve extreme memory bandwidth for inference.
- **Groq**, the inference-only chip company, has focused on extreme token generation speed using a deterministic SIMD architecture.
- **Rebellions** (South Korea) raised $400 million in March 2026 for its AI inference chips targeting data center deployments.
- **d-Matrix** and **Etched** have each built silicon around specific transformer inference optimization bets.

What differentiates Fractile is the in-memory compute approach itself. None of the other major inference chip startups are pursuing the same fundamental architecture, which means Fractile is making a harder bet with a potentially larger payoff. If SRAM-based in-memory compute proves economically viable at the scale frontier AI demands, Fractile could achieve performance and energy efficiency advantages that conventional architectures — whether Nvidia's or the other startups' — cannot match structurally.

## UK Silicon as a Strategic Asset

Fractile's fundraise is part of a broader moment for European semiconductor startups. The geopolitical tension around advanced chip supply — US export controls on high-end chips to China, the concentration of TSMC capacity in Taiwan, and growing European anxiety about dependence on US-controlled AI infrastructure — has created investor appetite for sovereign and geographically diversified chip development.

Fractile has offices in London, Bristol, San Francisco, and Taipei, reflecting both its UK roots and the practical necessity of access to Taiwanese advanced node manufacturing. The NATO Innovation Fund's participation in this round is particularly notable: it is one of the few venture funds backed by a military alliance, and its investment in a chip company focused on AI inference reflects the recognition that AI infrastructure is now explicitly treated as a national security concern.

The company is hiring aggressively across all four locations, with particular emphasis on chip design engineers — a talent pool that remains globally scarce despite the AI investment wave.

## The Road to 2027

Fractile's chips are not yet in production. The company's stated timeline targets hardware availability in 2027, which means the $220 million in Series B funding is runway for continued R&D, tape-out costs for prototype silicon, and the long, expensive process of working with foundry partners to bring a novel chip architecture to manufacturable reality.

The inference chip market will look different in 2027 than it does today. Nvidia will have new architectures. Several of the current inference startups will have either succeeded or failed. Demand will continue to grow as AI models become more integrated into enterprise and consumer software.

What won't change is the underlying physics: moving data between separate memory and processor chips costs energy and time. If Fractile's in-memory compute architecture works as designed, it will address a constraint that every other inference chip — including Nvidia's — is fighting against. That's the kind of technical differentiation that, if proven out, tends to attract not just investment but customers.
