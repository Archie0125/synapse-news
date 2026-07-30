---
title: "ChipAgents Raises $60M and Deepens Nvidia Tie-Up to Automate Semiconductor Design"
summary: "ChipAgents, a Santa Clara startup that deploys AI agents to automate the most time-intensive phases of chip design, has raised $60 million in Series A2 funding led by B Capital, bringing its total Series A haul to $134 million. The round accompanies an expanded partnership with Nvidia to develop a specialized AI model for semiconductor design, as ChipAgents reports 6x annualized revenue growth and deployments at more than 120 chip companies."
category: "hardware"
publishedAt: 2026-07-30
lang: "en"
featured: false
trending: true
sources:
  - name: "Yahoo Finance – Nvidia Partner ChipAgents Raises $60 Million to Accelerate Chip Design with AI Agents"
    url: "https://finance.yahoo.com/technology/ai/articles/nvidia-partner-chipagents-raises-60-114953354.html"
  - name: "The Next Web – Nvidia Partner ChipAgents Raises $60M for Agentic Chip Design"
    url: "https://thenextweb.com/news/nvidia-partner-chipagents-raises-60m-for-agentic-chip-design"
  - name: "Quartz – ChipAgents Was Raising $60 Million as It Expanded Its Partnership With Nvidia"
    url: "https://qz.com/chipagents-series-a2-funding-nvidia-partnership-072926"
  - name: "MarketScreener – Nvidia Partner ChipAgents Raises $60 Million to Accelerate Chip Design with AI Agents"
    url: "https://www.marketscreener.com/news/nvidia-partner-chipagents-raises-60-million-to-accelerate-chip-design-with-ai-agents-ce7f51d2d18eff23"
tags:
  - "ChipAgents"
  - "Nvidia"
  - "semiconductor"
  - "chip design"
  - "AI agents"
  - "EDA"
  - "B Capital"
  - "hardware"
  - "funding"
relatedSlugs:
  - "2026-07-05-oxmiq-raja-koduri-35m-series-a-gpu-architecture-en"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-en"
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-en"
---

Building a modern semiconductor is one of the most labor-intensive engineering challenges that exists. A single advanced chip can require billions of transistors arranged with nanometer precision, designed by teams of hundreds of engineers over two to four years, verified against millions of test cases before a single wafer is ever cut. The verification phase alone—checking that the chip actually does what the specification says it should do—can consume more than 70% of total design time and budget.

ChipAgents thinks AI agents can change that equation. On July 29, the Santa Clara-based startup announced $60 million in new Series A2 funding, bringing its total Series A financing to $134 million. The round was led by B Capital and included existing investors Bessemer Venture Partners, Micron, MediaTek, and Ericsson. Simultaneously, ChipAgents expanded its technical partnership with Nvidia to develop a specialized AI model focused on semiconductor design—a collaboration that places Nvidia's model capabilities in service of the very industry that makes Nvidia's chips possible.

## What ChipAgents Actually Does

Electronic design automation (EDA) is the software category that governs chip design. Companies like Cadence Design Systems and Synopsys have dominated the space for decades, providing the tools engineers use to lay out transistors, simulate circuit behavior, and verify that designs are correct before committing to expensive fabrication.

ChipAgents enters this space with a different architectural bet: rather than augmenting existing EDA tools with AI features, it builds autonomous AI agents that operate those tools on engineers' behalf. The agents can read a chip specification, generate test cases, execute them in simulation, analyze failures, and iterate—all with minimal human direction.

CEO William Wang describes the core promise as eliminating the busywork that currently occupies the majority of a verification engineer's day: "A big part of what we do is actually making sure there are no bugs," Wang said in an interview. "But today, the way that happens is humans writing thousands of test cases, running simulations, reading logs. That can change."

The technology targets chip verification specifically—the phase where engineers confirm that the logical design of a chip behaves correctly before it goes to manufacturing. A bug discovered at this stage can be fixed in software. The same bug discovered after fabrication can render an entire wafer run worthless, at a cost that can reach tens of millions of dollars.

## The Funding Trajectory

ChipAgents was founded in 2024 as a spinout from Alpha Design AI in San Jose. Its funding history reflects a rapid escalation of investor confidence: it closed a $21 million Series A in October 2025, added $50 million in February 2026, and now brings the total to $134 million in less than a year of Series A activity. B Capital's decision to lead the latest round, alongside chipmaker-investors Micron and MediaTek, signals that the customers are also believers.

The company now has approximately 64 employees and deployments at more than 120 semiconductor companies. Its annualized recurring revenue grew 6x in the first half of 2026—a growth rate that, if sustained, would put ChipAgents among the fastest-growing enterprise software companies in the sector. The company has not disclosed absolute revenue figures.

## The Nvidia Partnership: A Specialized Model for Chips

The most strategically significant element of the announcement is not the money—it is the deepened relationship with Nvidia. The two companies will collaborate on developing an AI model specifically trained for semiconductor design tasks: understanding hardware description language (HDL) code, interpreting specifications, predicting verification coverage gaps, and proposing test strategies.

This kind of domain-specific model is substantially different from general-purpose code models that have been applied to hardware design with limited success. Writing RTL (Register Transfer Level) code for a chip requires understanding timing constraints, power budgets, and fabrication process rules in ways that a model trained primarily on software code handles poorly. A model trained on the specific corpus of hardware design artifacts—specification documents, RTL code, verification testbenches, simulation logs, silicon failure analysis—would represent a qualitative improvement.

Wang declined to confirm whether Nvidia has taken an equity stake in the company alongside the technical partnership. Nvidia's motivation is apparent regardless: accelerating chip design software directly shortens the time-to-market for next-generation hardware, reducing the cycle time between when Nvidia's own chips are designed and when customers can design new chips that use them.

## The Market and the Competition

The EDA market is large, deeply entrenched, and consolidating. Cadence and Synopsys have both integrated AI features into their flagship design environments over the past two years, and both have launched agent-based products that compete with ChipAgents' core offering. The incumbents have something ChipAgents does not: decades of trust relationships with chip design teams and deep integration into established workflows.

What ChipAgents has is architectural purity—its agents are built from the ground up to operate autonomously, rather than being AI features bolted onto tools designed for human interaction—and the momentum of a market that is desperately looking for ways to reduce the cost and time of chip development.

The pressure to design faster has never been higher. The AI infrastructure buildout has created insatiable demand for new chip architectures: more efficient attention processors, custom inference chips, memory controllers optimized for transformer workloads, and interconnects that can move data fast enough to feed GPU clusters. Every six months of delay in bringing a new chip to market is revenue and competitive advantage lost.

If ChipAgents can demonstrably compress verification cycles—even by 20 or 30 percent—the ROI case is obvious. A 30% reduction in verification time on a chip program that would otherwise take two years is six months of accelerated time-to-market, worth far more than any software subscription.

## The Trust Problem

The challenge ChipAgents and every other company in agentic EDA will face is trust. Chip fabrication is irreversible. When TSMC or Samsung prints a wafer, any design flaw embedded in that silicon is permanent—there is no software patch that can fix a transistor that is in the wrong place. The humans who currently sign off on verification results do so with the full weight of that consequence in mind.

Convincing a verification team to delegate meaningful portions of their workflow to autonomous agents requires not just demonstrating that the agents are fast, but that they are reliably correct in ways that can be audited and understood. An AI agent that passes 99% of test cases but misses a class of timing violations in a specific corner case is worse than useless—it provides false confidence in a process where false confidence has catastrophic consequences.

The Nvidia partnership may help here. A model trained on Nvidia's internal design artifacts and validated against Nvidia's own silicon outcomes would carry credibility that no general-purpose model can claim. If ChipAgents can point to Nvidia designs that went to fabrication successfully after agent-assisted verification, that is a reference that the rest of the industry will take seriously.

The race to automate chip design is early. ChipAgents has positioned itself at the most impactful phase of that workflow, raised the capital to compete at scale, and secured the most credible possible partner to anchor its model development. The next two years will determine whether the industry is ready to trust an agent to find bugs before the wafer is poured.
