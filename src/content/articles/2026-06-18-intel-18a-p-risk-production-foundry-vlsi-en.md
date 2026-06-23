---
title: "Intel's 18A-P Process Enters Risk Production, Pushing Back Against TSMC's AI Chip Stranglehold"
summary: "Intel Foundry unveiled its 18A-P process node at the VLSI 2026 Symposium, moving into risk production and delivering up to 9% performance gains and 18% power savings over 18A. The launch marks Intel's most credible challenge yet to TSMC's dominance in the AI chip manufacturing market."
category: "hardware"
publishedAt: 2026-06-18
lang: "en"
featured: false
trending: false
sources:
  - name: "Intel Newsroom"
    url: "https://newsroom.intel.com/intel-foundry/intel-foundry-details-process-milestones-future-innovation-at-vlsi-symposium"
  - name: "SemiWiki"
    url: "https://semiwiki.com/semiconductor-manufacturers/intel/370197-intel-foundry-expands-the-18a-platform-with-18a-p-and-demonstrates-long-term-technology-leadership-at-vlsi-2026/"
  - name: "HotHardware"
    url: "https://hothardware.com/news/intel-18a-p-process-risk-production"
  - name: "Club386"
    url: "https://www.club386.com/intel-foundry-18a-p-node/"
tags:
  - "Intel"
  - "Intel Foundry"
  - "18A-P"
  - "semiconductor"
  - "TSMC"
  - "AI chips"
  - "manufacturing"
  - "PowerVia"
relatedSlugs:
  - "2026-06-17-qualcomm-tenstorrent-acquisition-risc-v-ai-chip-en"
  - "2026-04-03-nvidia-blackwell-supply-en"
  - "2026-04-03-riscv-ai-accelerators-en"
---

For most of the past five years, conversations about cutting-edge chip manufacturing have been conversations about TSMC. Taiwan Semiconductor Manufacturing Company holds the manufacturing contracts for Apple's chips, NVIDIA's GPUs, AMD's processors, and the overwhelming majority of high-performance AI accelerators. Its N2 and N3 process nodes have been the de facto definition of the frontier for chip designers worldwide.

Intel, which once led the industry in semiconductor manufacturing, has been on a painful and public journey to close the gap. At the VLSI 2026 Symposium — the premier academic and industry venue for semiconductor technology — Intel Foundry presented a credible milestone: **18A-P**, a performance-enhanced derivative of its flagship 18A process node, has entered risk production. The numbers back up the claim.

## What Risk Production Means

"Risk production" is a term of art in semiconductor manufacturing. It refers to the phase where wafers are being fabricated on the new process, but before full-scale manufacturing ramp. The "risk" in question is the customer's — typically a fabless chip designer who agrees to have their product made on a process that hasn't yet been fully validated at volume. If the process has issues, yields suffer and the chip fails to perform as specified.

The fact that 18A-P has entered risk production means Intel has chips going through its fabrication facilities on this process right now. It meets a timeline that Intel shared with customers and partners at the start of the year — a notable achievement for a company that has repeatedly missed its own roadmap targets over the past several years.

## The Performance Numbers

The headline figures are compelling for a process derivative — typically a more conservative upgrade than a new node:

- **9% higher performance** at equivalent power, based on a fully routed Arm core test vehicle
- **18% lower power consumption** at equivalent performance
- **20–40% improvement in thermal resistance**
- **10–30% lower via resistance** on performance-critical interconnect layers

These are measured numbers from actual silicon, presented at a peer-reviewed symposium — not marketing projections. For AI chip designers, the power efficiency improvement is particularly relevant. AI training and inference workloads are fundamentally thermal problems: large clusters of accelerators generate heat that limits sustained performance, and any reduction in power per operation translates directly into higher throughput per watt.

## The PowerVia Breakthrough

The most technically significant innovation in 18A-P is the **Dual-Contact Power Boost structure**, which combines Intel's traditional front-side metal contacts with direct backside contacts enabled through **PowerVia** technology — Intel's implementation of backside power delivery.

Conventional chip manufacturing routes power through the same metal layers as signals, creating a conflict between power delivery and signal routing. Backside power delivery moves power to the back of the wafer, freeing the front-side layers entirely for signals. This reduces parasitic resistance in the power delivery network, improves current delivery uniformity, and allows transistors to operate at higher drive strength without sacrificing efficiency.

The concrete results: when combined with gate-all-around transistors, Intel reports approximately **10× dynamic voltage droop reduction**, **5–6% frequency improvement** at the same power, or alternatively **more than 15% dynamic power reduction** at the same frequency. For high-clock designs — exactly the type used in AI accelerators — voltage droop is a fundamental limiter of achievable frequency. A 10× improvement is not incremental.

## How This Positions Intel Against TSMC

TSMC's N2 process, its leading node currently in production, uses gate-all-around transistors and has been receiving strong customer demand for AI chip designs. The company's N2P (performance-enhanced) derivative is in preparation. Direct comparisons between Intel 18A-P and TSMC N2P are not published — semiconductor companies do not benchmark each other's processes officially — but analyst estimates suggest competitive parity for the first time in years.

Intel's structural advantage, if it can execute, is geography. TSMC's dominant manufacturing footprint is in Taiwan, with new fabs in Arizona and Japan still ramping. Geopolitical concerns about Taiwan-concentrated production have made US and European governments eager to diversify chip manufacturing supply chains. Intel's fabs in Oregon, Arizona, New Mexico, and Germany are positioned to serve customers who cannot or will not rely on Taiwan-concentrated production.

The CHIPS Act funding — $8.5 billion in direct grants to Intel — has gone partly toward accelerating the 18A-P timeline. The partnership with Foxconn to develop rack-scale AI infrastructure, and the SandboxAQ $500 million CHIPS Research grant for AI-aided materials discovery, are companion bets on the same thesis: that the US can rebuild competitive semiconductor manufacturing if it can sustain the investment and execution through the current administration.

## Intel Foundry's External Customer Challenge

Intel Foundry's fundamental challenge is not technical — it is commercial. Building advanced chips for other companies is a different business than building chips for your own product lines. It requires building customer relationships, running competing companies' most sensitive designs through your fab, and convincing chip designers that Intel Foundry will execute reliably on its commitments — a record that has been spotty.

The 18A and 18A-P timeline, if it holds through full production, begins to rebuild that credibility. The chip manufacturing market has structural demand for a credible alternative to TSMC at the leading edge. Intel is the only Western-owned company with a realistic path to offering one.

Intel 18A-P entering risk production is not a victory lap. It is a prerequisite for becoming viable. The company needs to get to high-yield volume production, attract anchor external customers willing to commit future designs to 18A-P, and maintain its process roadmap cadence through 14A and beyond. The VLSI Symposium announcement is a credible signal that the prerequisites are being met — one milestone at a time.

Whether the AI chip market will wait for Intel to fully arrive, or whether TSMC's lead will prove insurmountable, is a question the semiconductor industry will be answering over the next 24 months. The answer has consequences well beyond the chip industry: it will shape where AI compute is manufactured, and therefore who controls the physical infrastructure of the next decade's AI revolution.
