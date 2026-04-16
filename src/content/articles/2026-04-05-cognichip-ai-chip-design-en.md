---
title: "Cognichip Raises $60M to Let AI Design the Next Generation of Chips — Intel CEO Joins Board"
summary: "Cognichip, a San Francisco startup using physics-informed AI models to radically cut chip design costs and timelines, raised a $60M Series A led by Seligman Ventures. The company claims 75% cost reduction and 50% timeline compression. Intel CEO Lip-Bu Tan's board seat sends a pointed signal about where the semiconductor industry thinks custom silicon design is heading."
category: "startups"
publishedAt: 2026-04-05T09:15:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/01/cognichip-wants-ai-to-design-the-chips-that-power-ai-and-just-raised-60m-to-try/"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/04/01/cognichip-raises-60m-reinvent-chip-design-physics-inspired-ai-models/"
  - name: "Unite.AI"
    url: "https://www.unite.ai/cognichip-raises-60m-series-a-to-rebuild-chip-design-around-ai/"
tags:
  - "chip-design"
  - "EDA"
  - "ai-for-hardware"
  - "startups"
  - "semiconductor"
  - "cognichip"
relatedSlugs:
  - "2026-04-05-intel-fab34-buyback-en"
  - "2026-04-03-riscv-ai-accelerators-en"
---

Chip design has long been one of the last great redoubts of human expertise in engineering. While AI has transformed software development, drug discovery, material science, and protein folding, the process of designing a modern semiconductor — months of painstaking work by teams of hundreds of specialized engineers using billion-dollar EDA (electronic design automation) software — has remained largely resistant to automation.

Cognichip is betting that ends now.

The San Francisco startup, founded in 2024, announced on April 1 that it has raised a $60 million Series A led by Seligman Ventures, bringing its total funding to $93 million. The round's most notable element is not the capital but the board appointment: Intel CEO Lip-Bu Tan has joined Cognichip's board, a move that signals serious institutional validation from the head of the world's largest chip manufacturer.

## The Technology: Physics-Informed AI for Silicon

Cognichip's platform — which the company calls Artificial Chip Intelligence, or ACI — is built around a class of AI model called physics-informed neural networks (PINNs). Unlike general-purpose large language models that learn from text or code, PINNs incorporate the fundamental physics equations governing semiconductor behavior directly into the model architecture.

This matters because chip design is ultimately a physics problem. Transistor switching characteristics, heat dissipation, signal propagation, electron tunneling at sub-nanometer scales — these are governed by equations that don't change based on training data. By baking the physics in, Cognichip's models can make reliable predictions about how a circuit will behave without needing to simulate every possible configuration from scratch.

The result, according to Cognichip's claims (unverified by independent benchmarking): a 75%+ reduction in chip development costs and a 50%+ reduction in design-to-tape-out timeline compared to conventional EDA workflows. For context, tape-out — the point at which a chip design is finalized and sent to fabrication — typically takes 18 to 36 months for a complex SoC. A 50% reduction would bring that to 9 to 18 months, a transformation that would fundamentally change competitive dynamics in the chip industry.

## The EDA Market Context

The existing EDA software market is dominated by three players: Synopsys, Cadence Design Systems, and Siemens EDA (formerly Mentor Graphics). These companies provide the tools that every major semiconductor design team uses, and their software suites cost tens to hundreds of millions of dollars per year for large chipmakers.

Both Synopsys and Cadence have been integrating AI into their platforms — Cadence's Cerebrus and Synopsys' DSO.ai both use reinforcement learning to optimize circuit placement and routing. But these are incremental improvements to existing EDA workflows, not replacements for them.

Cognichip is positioning as a different kind of disruption: not a better tool within the existing workflow, but an alternative workflow built ground-up on AI. This is the same pattern that has played out in other domains where AI disrupted established software platforms — the question is always whether the new paradigm is good enough to displace the incumbent, or whether the incumbent simply integrates the new approach.

## The Lip-Bu Tan Signal

Intel CEO Lip-Bu Tan's board seat at Cognichip is significant precisely because of who Lip-Bu Tan is. Before joining Intel, Tan spent over a decade as CEO of Cadence Design Systems — the second-largest EDA software company in the world. He arguably knows the chip design workflow better than anyone in the industry.

Tan's decision to take a board seat at a company whose explicit mission is to disrupt the EDA-centric chip design workflow he spent his career building reads as a signal that he believes the disruption is real and coming. For Intel, the strategic interest is clear: if Cognichip's platform works, it could significantly expand the market of companies that can afford to design custom chips — and those custom chip designers would need a foundry to manufacture them.

An Intel CEO on the board of a startup that democratizes chip design is, in essence, a bet on demand creation for Intel's foundry services. It is also a hedge: if AI-driven chip design is coming regardless, Intel would prefer to be close to it.

## The 30+ Design Partners

Cognichip reports that it is working with 30+ semiconductor design companies, including unnamed "industry's biggest players" in production testing workflows. At this stage, the company has not shipped a chip that was designed primarily through its platform, and revenue figures have not been disclosed.

The production testing phase is critical. Semiconductor design tools must be validated against tape-out results — the only thing that matters is whether the chip that comes back from the fab matches what the simulator predicted. Any discrepancy between Cognichip's physics-informed predictions and actual silicon behavior would be disqualifying.

The unnamed "industry's biggest players" in testing suggests that at least some tier-1 chipmakers are running parallel validation — using Cognichip's ACI platform alongside conventional EDA workflows and comparing results. If those validations are positive, formal partnerships and customer announcements are likely to follow in the next twelve months.

## The Bigger Bet

Cognichip sits at the intersection of two powerful trends: AI automating knowledge work at every level of the engineering stack, and the semiconductor industry facing an urgent need to reduce the cost and timeline of custom chip development as AI hardware requirements evolve faster than traditional design cycles can accommodate.

The hardware-software co-design imperative — the idea that next-generation AI models require custom chips designed specifically for their compute patterns, rather than adapted from general-purpose GPU architectures — is increasingly well-understood in the industry. But the cost and timeline of custom chip design has historically limited this co-design opportunity to the very largest companies.

If Cognichip can deliver on its 75% cost reduction claim in production, it would bring custom silicon within reach of a much larger population of AI companies — enabling the kind of hardware-software co-optimization at the system level that currently only a handful of hyperscalers can afford. That would be a genuinely transformative development for the AI industry, and a $93 million bet with Intel's CEO on the board is the industry's early read that it might just be possible.
