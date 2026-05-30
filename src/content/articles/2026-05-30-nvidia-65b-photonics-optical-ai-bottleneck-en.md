---
title: "Nvidia's $6.5 Billion Photonics Bet: How Light Will Replace Copper at the Heart of AI Infrastructure"
summary: "Nvidia has quietly assembled a $6.5 billion-plus investment portfolio in photonics and optical interconnect companies — Lumentum, Coherent, Marvell, Corning, and Ayar Labs — in a strategic campaign to replace the copper cables and electrical signals that currently link GPU clusters with light-based alternatives. The push addresses a fundamental energy and bandwidth bottleneck that threatens to constrain AI scale-out before silicon itself does."
category: "hardware"
publishedAt: 2026-05-30
lang: "en"
featured: false
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/05/29/nvidia-photonics-investment-ai.html"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/nvidia-photonics-investment-copper-bottleneck-ai-data-centre"
  - name: "NVIDIA Newsroom (Lumentum)"
    url: "https://nvidianews.nvidia.com/news/nvidia-announces-strategic-partnership-with-lumentum-to-develop-state-of-the-art-optics-technology"
  - name: "NVIDIA Newsroom (Coherent)"
    url: "https://nvidianews.nvidia.com/news/nvidia-and-coherent-announce-strategic-partnership-to-develop-optics-technology-to-scale-next-generation-data-center-architecture"
  - name: "Photonics Spectra"
    url: "https://www.photonics.com/Articles/NVIDIA-Invests-4B-in-Coherent-Lumentum/a72014"
tags:
  - "Nvidia"
  - "photonics"
  - "optical interconnects"
  - "AI infrastructure"
  - "data centers"
  - "hardware"
relatedSlugs:
  - "2026-05-10-nvidia-corning-us-manufacturing-optical-en"
  - "2026-05-27-nvidia-vera-rubin-q3-launch-5x-blackwell-en"
  - "2026-05-22-nvidia-q1-fy2027-earnings-china-huawei-concession-en"
---

Jensen Huang has spent the past year talking about AI factories — data centers so dense with GPU compute that they function as single industrial machines. What he has been quietly building in parallel is the optical plumbing those factories will require.

Since early March, Nvidia has committed more than $6.5 billion across five strategic investments in photonics and optical connectivity companies: $2 billion each into Lumentum and Coherent, up to $3.2 billion into Corning, $2 billion into Marvell for optical networking chips, and a participation in optics startup Ayar Labs' $500 million Series E. Taken together, the investments represent one of the most focused infrastructure bets in Nvidia's history — not on silicon, but on the light-based interconnects that will replace the copper cables holding its GPU clusters together.

A CNBC analysis published on May 29 drew the full arc of the strategy into focus for the first time, describing what analysts are calling a deliberate effort to solve a problem that Nvidia cannot fix with faster chips alone.

## The Copper Bottleneck Nobody Is Talking About

Most public discussion of AI infrastructure constraints focuses on silicon: GPU supply, HBM memory availability, chip yield, or TSMC's production capacity. The copper bottleneck is less visible but increasingly consequential.

AI training clusters link tens of thousands of GPU accelerators together using high-speed interconnects — copper cables and electrical transceivers that pass data between chips, nodes, and racks. As clusters scale from thousands to hundreds of thousands of GPUs, these electrical interconnects hit physical limits. Copper cables attenuate high-frequency signals over distance, requiring repeaters that add latency. Electrical transceivers consume substantial power — power that shows up in data center electricity budgets before it produces any computation. And the bandwidth ceiling of copper interconnects is approaching the rate at which frontier model training jobs need to move data between accelerators.

"Photonics represents a way for Nvidia to scale their AI infrastructure without the energy costs that staying with electrical and copper will incur," one analyst told CNBC. As data centers begin measuring their power consumption in gigawatts rather than megawatts, the efficiency gap between optical and copper interconnects becomes a billion-dollar consideration.

## The Investment Portfolio in Detail

Nvidia's photonics commitment unfolded across several months.

On March 2, the company simultaneously announced $2 billion investments in both Lumentum and Coherent — the two dominant US suppliers of the laser components and optical transceivers used in high-speed data center networking. Both deals include not just equity investment but multi-billion-dollar purchase commitments and future capacity access rights, meaning Nvidia is securing supply chain priority for the optical components it expects to need at scale.

The Lumentum deal includes funding for a new US-based semiconductor fab dedicated to laser components — a significant manufacturing commitment that echoes the domestic chip production priorities that have become central to US technology policy. Coherent received similar terms, with the investment structured to support US-based manufacturing buildout for advanced optical networking products.

In May, Nvidia formalized a partnership with Corning — the glass giant that manufactures the fiber optic cables that form the backbone of telecommunications and data center connectivity — with an investment commitment of up to $3.2 billion. Corning will increase its US optical fiber capacity by more than 50% and open new manufacturing facilities in North Carolina and Texas. The scale of that commitment reflects Nvidia's expectation that AI data centers will require vastly more fiber than the current telecommunications-grade infrastructure provides.

The Ayar Labs investment rounds out the portfolio with a bet on a more radical approach: co-packaged optics, which integrates photonic transceivers directly into the same package as the GPU or networking chip, eliminating the electrical signal path between chip and optical transceiver entirely. Ayar Labs is developing technology that would allow light to enter and exit the processor package directly — potentially the longest-term but highest-leverage solution to the interconnect problem.

## Why Now

The timing of Nvidia's photonics push aligns with a specific transition in AI cluster architecture.

The current generation of Nvidia's AI infrastructure — based on NVLink switches and InfiniBand networking — relies heavily on copper-based high-speed interconnects at the within-rack and between-rack scale. For clusters of the size that hyperscalers operate today — tens of thousands of H100 or H200 GPUs — copper solutions are workable, if power-hungry.

But Nvidia's roadmap points toward clusters that are qualitatively larger. The Vera Rubin architecture, targeting Q3 2026 volume production, is designed for deployment in configurations that previous GPU generations could not achieve. Future clusters of 100,000 or 1 million GPUs — described by Huang as the architecture of AI factories — require interconnect solutions that copper simply cannot provide at acceptable power and cost.

Optical interconnects move data using light rather than electrons, which travels through fiber or silicon waveguides with minimal signal degradation over distance and at a fraction of the electrical power. For the intra-cluster connections where latency and bandwidth are most critical — the links between GPUs within a training job — optical solutions offer the path to scaling that copper cannot.

## Supply Chain Strategy and Geopolitical Dimensions

Nvidia's insistence on US-based manufacturing for these investments is not accidental.

Every major optical investment — Lumentum's new fab, Coherent's manufacturing expansion, Corning's fiber capacity increase — is explicitly tied to domestic production. This reflects both the supply chain diversification lessons of the semiconductor shortage era and the political environment created by export controls, CHIPS Act incentives, and the broader push to bring critical technology manufacturing back to the United States.

For Nvidia, having US-based supply chains for its optical components also reduces the export control exposure that has complicated its GPU sales in China. Optical components for data center interconnects are not currently subject to the same restriction frameworks as AI accelerators, but the company appears to be structuring its supply chain to minimize dependencies that could become regulatory vulnerabilities.

## What It Means for the AI Infrastructure Landscape

Nvidia's photonics portfolio positions it not merely as a chip company that sells into AI data centers, but as a vertically integrated architect of the entire AI factory — from silicon to interconnect to optical fiber.

For competitors, the implications are significant. AMD, which offers its own GPU accelerators and networking products for AI training clusters, does not have an equivalent optical interconnect investment portfolio. Custom silicon programs at hyperscalers like Google (TPUs) and Amazon (Trainium) operate within data center architectures largely defined by the networking and interconnect infrastructure that Nvidia is now shaping.

The $6.5 billion in photonics commitments also signals Nvidia's view that optical interconnects will become a standard component of AI infrastructure within the next two to three years — not a future research direction, but an engineering deliverable with specific production timelines. For a company that generated $81.6 billion in revenue in its most recent fiscal year, $6.5 billion is a meaningful supply chain bet, but not an exploratory one.

In Jensen Huang's framing, the AI factory is a single machine. Copper was always a temporary material for that machine. Nvidia is now building the light-based nervous system it always intended.
