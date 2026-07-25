---
title: "Nvidia's RTX Spark Superchip Puts AI Agents on Your Desktop, Challenging Intel, AMD, and Qualcomm"
summary: "At Computex 2026, Nvidia unveiled the RTX Spark, its first self-developed AI PC superchip, alongside a three-generation roadmap targeting the $200 billion PC processor market. Co-developed with MediaTek and backed by Microsoft, Dell, and HP, the move marks Nvidia's most aggressive push yet beyond data centers into personal computing."
category: "hardware"
publishedAt: 2026-07-25
lang: "en"
featured: false
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/02/nvidias-new-pc-chips-are-ceos-bid-to-own-every-part-of-ai-stack.html"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/01/nvidia-chases-200b-cpu-market-with-ai-agent-pcs-from-microsoft-dell-and-hp/"
  - name: "Nvidia Investor Relations"
    url: "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Microsoft-Reinvent-Windows-PCs-for-the-Age-of-Personal-AI/default.aspx"
  - name: "Fortune"
    url: "https://fortune.com/2026/06/01/jensen-huang-nvidia-pc-reinvention-ai-chips/"
tags:
  - "Nvidia"
  - "RTX Spark"
  - "AI PC"
  - "Jensen Huang"
  - "Microsoft"
  - "PC chips"
  - "hardware"
relatedSlugs:
  - "2026-07-25-intel-q2-2026-earnings-comeback-en"
---

For two decades, Nvidia has been the company that made the chips *inside* computers do extraordinary things. Now Jensen Huang wants Nvidia to be the company that makes the chip that *is* the computer.

At Computex 2026 in Taipei, Nvidia unveiled the **RTX Spark**, a system-on-chip superchip co-developed with MediaTek that marks the company's first foray into designing the primary processor for Windows PCs. The announcement — flanked by executive appearances from Microsoft, Dell, and HP — signals that the world's most valuable semiconductor company is preparing a direct assault on the $200 billion PC processor market currently shared among Intel, AMD, Apple, and Qualcomm.

## The RTX Spark: What It Is

The RTX Spark is not a discrete GPU slotted into a desktop tower. It is an integrated system-on-chip — CPU, GPU, NPU, and memory — designed to power an entire PC on a single die. Huang called it the centerpiece of Nvidia's vision for "agentic PCs": computers capable of running AI agents locally, without relying on cloud infrastructure.

The chip is built on a 3nm process node and delivers what Nvidia claims is 200 TOPS (trillion operations per second) of AI performance on-device — roughly double the highest-performing AI PCs currently shipping with AMD and Qualcomm silicon. Unlike cloud inference, which incurs latency and per-call costs, the RTX Spark is designed to run agents continuously in the background, monitoring applications, drafting responses, and executing multi-step workflows without an internet connection.

Nvidia's partnership with **MediaTek** for the chip's CPU cores is a notable design choice. Rather than building CPU cores from scratch — a multi-year undertaking — Nvidia licensed MediaTek's Arm-based CPU architecture, combining it with its own GPU and AI accelerator IP. The result is a hybrid design that lets Nvidia move fast without compromising on the GPU and NPU performance that defines its brand.

## A Three-Generation Roadmap

At Computex, Huang unveiled a chip roadmap that had clearly been in preparation for years. The sequence:

- **N1X** (2026): Entry-level AI PC chip, targeting thin-and-light laptops
- **N2X** (2027): Mid-range chip with higher NPU throughput, targeting workstations
- **N3X** (2028): High-performance chip for professional AI workstations and "personal supercomputers"

The RTX Spark sits alongside the N1X as part of the initial launch wave. The roadmap cadence matches Apple's annual Silicon release cycle and mirrors Intel's historical tick-tock model — sending a clear message that Nvidia intends to be a recurring presence in the PC market, not a one-off experiment.

"We've been preparing AI PCs with Microsoft for three years," Huang told reporters after his keynote. "This is not a detour. This is the center of gravity shifting."

## Microsoft, Dell, and HP at Launch

The launch lineup underscores how seriously the industry's largest OEMs are taking Nvidia's PC ambitions. Microsoft confirmed that Windows 12 will include deep platform support for RTX Spark, including native integration with Copilot agents, local model execution APIs, and a new "Agentic PC" certification program. Dell and HP are the first hardware partners, with AI-optimized PCs based on RTX Spark expected to ship before the end of 2026.

The Microsoft relationship is particularly significant. Huang described three years of co-development on both the chip architecture and the software stack — a degree of partnership that suggests Microsoft sees Nvidia's PC chip as a serious long-term bet, not a hedging experiment. Critically, RTX Spark PCs will run Windows 12 natively on Arm, ending the compatibility compromises that have hampered earlier Arm-based Windows devices.

## What This Means for Intel, AMD, and Qualcomm

The competitive implications are significant, if still unfolding.

**Intel** is the most exposed. The PC chip market has long been Intel's home turf, and the company has spent years building its AI PC narrative around its Lunar Lake and Arrow Lake architectures. Nvidia entering the PC SoC market with Microsoft's explicit backing represents a credibility threat that numbers alone don't capture. Intel stock slid 3.2% in the session following the Computex announcement.

**AMD** faces a similar narrative risk. Its Ryzen AI series has been gaining traction in AI PC deployments, but Nvidia's brand recognition in AI acceleration — earned in data centers — gives RTX Spark a marketing advantage that is difficult to counter.

**Qualcomm** may be the most complicated case. The company's Snapdragon X Elite has been the leading Arm-based Windows chip, and Qualcomm has invested heavily in its software ecosystem and OEM relationships. Nvidia's entry validates the Arm-on-Windows thesis while simultaneously threatening Qualcomm's first-mover advantage. Several analysts expect Qualcomm to accelerate its next-generation chip timeline in response.

Apple, which designs its own Silicon for a closed ecosystem, is largely insulated from direct competition, though Nvidia's push into efficient on-device AI clearly benchmarks against Apple's M-series performance.

## The "Local AI Agent" Thesis

Central to Nvidia's PC strategy is a bet that the future of AI is not purely cloud-based. Huang argued at Computex that the next era of AI will be dominated by "personal AI agents" — software that knows your files, your calendar, your workflows, and your preferences, and acts on your behalf autonomously. Running such agents in the cloud raises latency, privacy, and cost concerns that on-device processing can resolve.

"AI agents need to be with you, on your device, responding in milliseconds," Huang said. "The cloud will do what the cloud does best. But your personal AI needs to be personal."

This framing conveniently positions RTX Spark in a market segment where Nvidia's GPU heritage is an advantage rather than an afterthought. AI PC chips from Intel and AMD have been shaped largely by CPU-first architectures that added neural processing capability incrementally. RTX Spark inverts the priority stack, treating GPU and NPU compute as primary and treating CPU capability as necessary but secondary.

## Early Benchmarks and Developer Reception

Nvidia has shared preliminary benchmark data showing RTX Spark outperforming current AI PCs on transformer model inference tasks by 2.5x to 3x at equivalent power draw. Independent labs have not yet validated these figures, and production silicon samples have not shipped at press time.

Developer reception has been cautiously optimistic. Several application developers told TechCrunch they were excited about the prospect of running local multimodal agents — combining vision, language, and tool-use — without cloud dependencies, but noted that the software ecosystem would need time to mature. Nvidia's CUDA ecosystem, dominant in data centers, does not automatically translate to PC workloads, and the company will need to demonstrate that its developer tools adapt to the on-device context.

A beta version of Nvidia's Agent Toolkit for PC — a developer framework for building agentic applications on RTX Spark — is expected to be available to select partners later this year, with a public release alongside N1X hardware in early 2027.

The PC chip market has not seen a genuinely new entrant in years. Whether RTX Spark disrupts the status quo or becomes a high-profile stumble remains to be seen — but Nvidia has rarely arrived late to a market it intended to own.
