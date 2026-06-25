---
title: "Nvidia's Vera Rubin Rack Hits $7.8 Million as Memory Costs Explode 435%"
summary: "A Morgan Stanley analysis puts the cost of a single Nvidia Vera Rubin VR200 NVL72 rack at $7.8 million—nearly double the Blackwell generation's $3.5–4 million—driven by a 435% surge in HBM4 and LPDDR5X memory prices that now account for 25% of total system cost. With volume shipments starting Q3 2026 and some analysts predicting prices as high as $9.1 million per rack, the Vera Rubin generation marks a structural shift: GPU cost no longer dominates AI infrastructure pricing."
category: "hardware"
publishedAt: 2026-06-25
lang: "en"
featured: true
trending: true
sources:
  - name: "Tom's Hardware: Nvidia's memory costs soar 485%, latest AI systems now cost $7.8 million"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-memory-costs-soar-485-percent-latest-ai-systems-now-cost-usd7-8-million-to-build-memory-now-comprises-25-percent-of-the-total-cost-rubin-gpus-a-mere-usd50-000-apiece"
  - name: "PC Gamer: A Morgan Stanley estimate says a single Nvidia Vera Rubin rack costs over $7.8 million"
    url: "https://www.pcgamer.com/hardware/a-single-nvidia-vera-rubin-rack-is-estimated-to-cost-usd7-803-148-with-over-usd2-million-of-that-figure-spent-on-memory-alone/"
  - name: "WCCFTech: NVIDIA's Vera Rubin Rack Hit With 435% Memory Price Surge, HBM4 Bill to $2M"
    url: "https://wccftech.com/nvidia-vera-rubin-rack-hit-with-memory-price-surge-pushing-hbm4-lpddr5x-bill-to-2m-of-7-8m-total/"
  - name: "Tom's Hardware: Price of Nvidia's Vera Rubin NVL72 racks skyrockets to as much as $8.8 million"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/price-of-nvidias-vera-rubin-nvl72-racks-skyrockets-to-as-much-as-usd8-8-million-apiece-but-server-makers-margins-will-be-tight-nvidia-is-moving-closer-to-shipping-entire-full-scale-systems"
  - name: "WCCFTech: Bernstein Warns Vera Rubin Racks Will Hit $9.1 Million"
    url: "https://wccftech.com/bernstein-warns-nvidias-vera-rubin-racks-will-hit-9-1-million-as-hbm4-prices-triple-to-53-per-gigabyte/"
tags:
  - "Nvidia"
  - "Vera Rubin"
  - "NVL72"
  - "HBM4"
  - "AI hardware"
  - "data center"
  - "memory"
  - "Morgan Stanley"
relatedSlugs:
  - "2026-06-11-nvidia-rubin-platform-vera-cpu-en"
  - "2026-06-04-big-tech-725b-ai-capex-race-en"
  - "2026-06-14-nvidia-sk-hynix-ai-memory-partnership-en"
---

The GPU is no longer the most important line item in an AI infrastructure purchase. A new Morgan Stanley research note on Nvidia's forthcoming Vera Rubin generation has landed a number that is reshaping how hyperscalers and infrastructure investors think about AI capex: a single **VR200 NVL72 rack costs an estimated $7,803,148**—nearly double the $3.5–4 million price tag of the Blackwell NVL72 generation it replaces. The primary culprit is memory. HBM4 and LPDDR5X prices have surged **435%** from Blackwell to Rubin, pushing the memory bill for a single rack past **$2 million**—roughly 26% of total system cost.

The Vera Rubin generation, confirmed for initial shipments in Q3 2026 with volume ramp in Q4, marks the most significant structural shift in AI rack economics since Nvidia introduced the NVL72 form factor with Blackwell. The story of AI infrastructure pricing is no longer primarily about GPU silicon; it is about memory.

## The Cost Anatomy of a Vera Rubin Rack

Understanding why the VR200 NVL72 rack costs what it costs requires looking at each component category separately:

**GPUs.** Each Rubin GPU is expected to cost approximately $55,000 at hyperscaler volume, with the Vera CPU companion chip adding about $5,000 per unit. An NVL72 rack contains 72 GPUs, putting the raw silicon cost at roughly $4.3 million—still the largest single line item, but now representing a smaller share of total system cost than in previous generations.

**Memory.** This is where the story changes. The VR200 NVL72 carries **20.7 terabytes of HBM4** (High Bandwidth Memory 4) and **54 terabytes of LPDDR5X**, totaling approximately $2 million in memory cost alone. HBM4, the latest generation of stacked high-bandwidth memory co-designed by Nvidia and SK Hynix (their AI memory partnership announced earlier in June), prices at roughly $53 per gigabyte at current rates—nearly triple the cost of HBM3e used in Blackwell systems. This memory escalation reflects both the scarcity of advanced HBM4 production capacity and a deliberate architectural choice: Rubin systems require substantially more memory bandwidth to feed the increased parallelism of the Vera CPU–GPU integration.

**Storage.** A new addition to the VR200 NVL72 bill of materials is approximately **$1 million in 3D NAND storage**—a figure that was effectively zero in the GB200 NVL72 generation. This reflects Nvidia's integration of local high-speed storage into the rack design for agentic workloads that require persistent context and fast retrieval of large model checkpoints.

**Balance of system.** PCBs, power delivery, networking (ConnectX-9 NICs), cooling infrastructure, and chassis account for the remaining ~$450,000, with higher per-unit costs driven by denser power delivery requirements for the Vera CPU architecture.

## The Market Implications

The $7.8 million figure—which Bernstein analysts believe could reach **$9.1 million** by the time OEM markups and system integration fees are applied—has several immediate consequences for the AI infrastructure market:

**Hyperscaler capex will increase even if rack counts hold flat.** A hyperscaler that bought 1,000 NVL72 Blackwell racks at $3.5 million each—$3.5 billion total—faces an $7.8 billion bill for the same number of Vera Rubin racks. This helps explain why Microsoft, Google, Amazon, and Meta have been revising their 2026 capex guidance upward throughout Q1 and Q2, even as they have been careful to avoid specifying rack quantities.

**Memory suppliers become indispensable infrastructure.** SK Hynix, Samsung, and Micron—the only manufacturers capable of producing HBM4 at volume—are now as critical to AI infrastructure buildout as TSMC. Nvidia's partnership with SK Hynix for AI memory, announced this month, is less a marketing arrangement and more a supply chain lifeline: Nvidia needs guaranteed HBM4 allocation to keep shipment commitments to hyperscalers.

**The GPU as a fraction.** In the Blackwell era, GPUs accounted for roughly 60–65% of a rack's cost. In Vera Rubin, that share drops to approximately 55%. Memory's share rises from around 8% to 26%. Storage, effectively zero in Blackwell, becomes a meaningful 13%. This diversification of cost is structurally significant: it means the suppliers that benefit from the AI infrastructure boom are expanding beyond pure semiconductor design, into memory stacking, advanced packaging, and storage tiers.

## Why Vera Rubin Is More Expensive By Design

The Vera Rubin architecture represents Nvidia's most significant departure from the pure-GPU model in over a decade. The key innovation is the **Vera CPU**—a custom Arm-based processor designed specifically to manage the data movement, orchestration, and memory hierarchy of large AI clusters. Rather than relying on host CPUs from Intel or AMD to coordinate GPU workloads, Vera Rubin integrates the CPU function directly into the rack's compute fabric.

This tight integration dramatically improves the efficiency of very large model inference—particularly for the long-context, multi-step agentic workloads that are becoming the dominant enterprise AI use case. But it comes at a cost: the Vera CPU requires its own memory hierarchy (hence the LPDDR5X addition), its own power delivery (adding to system complexity), and new firmware and software stacks that customers must integrate with their existing ML infrastructure.

The storage integration similarly reflects the architectural demands of the agentic era. Models running long agent loops—writing code, browsing, editing documents, managing files—generate and consume large amounts of intermediate state that must persist across steps. Local NVMe storage at the rack level eliminates round-trips to network-attached storage for these workloads, improving latency but adding hardware cost.

## What This Means for AI Capex Forecasts

Goldman Sachs published a $7.6 trillion AI capex forecast for the decade through 2035 in June 2026—a figure that attracted significant skepticism at the time. The Vera Rubin pricing data provides concrete arithmetic for how large-scale AI infrastructure spending could compound.

A 10,000-rack hyperscale cluster—roughly the size of the first Colossus build—costs approximately $78 billion in Vera Rubin hardware alone, before cooling infrastructure, networking, power delivery, and real estate. Meta's announced plan to build a 2-gigawatt AI cluster implies on the order of 200,000+ high-end GPU racks across multiple facilities; at $7.8 million per rack, the hardware cost alone approaches $1.5 trillion. Not in ten years. In the current capex cycle.

The numbers strain credibility—until you look at the financial commitments that hyperscalers are actually making. Microsoft's 2026 capital expenditure guidance of $190 billion, Google's $80 billion committed for AI infrastructure, and Amazon's custom silicon business exceeding a $20 billion annual run rate are all consistent with a world where a single AI rack costs $7.8 million and thousands of them are being ordered.

## The SK Hynix Signal

One of the more telling data points in the Vera Rubin story is what it implies for SK Hynix. The Korean memory giant announced its AI memory partnership with Nvidia earlier this month—a partnership that goes beyond preferred supplier status to include joint co-design of HBM4 stacks optimized for the Vera CPU architecture. For SK Hynix shareholders, the $7.8 million rack price is not a concern; it is a revenue opportunity. Every VR200 NVL72 rack sold carries $2 million in memory content, of which SK Hynix captures a substantial share.

The AI infrastructure boom has, in this sense, triggered the most significant shift in the semiconductor value chain since the rise of mobile—moving billions of dollars of value from logic chips (where Nvidia captures enormous margin) toward memory (where HBM4 suppliers capture enormous margin). Both can be true simultaneously, which is why the AI infrastructure investment cycle is generating financial returns for an unusually broad coalition of hardware companies.

Volume Vera Rubin shipments begin in Q4 2026. The rack price will be the number that shapes AI infrastructure economics for the next two years.
