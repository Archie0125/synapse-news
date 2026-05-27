---
title: "NVIDIA Vera Rubin Confirmed for Q3 Launch: 5× Blackwell Performance at 10× Lower Cost"
summary: "NVIDIA confirmed during its record-breaking Q1 FY2027 earnings call that the Vera Rubin platform will ship in Q3 2026 with a full volume ramp by Q4. The seven-chip architecture promises 50 petaFLOPs of NVFP4 inference per GPU and 3.6 exaFLOPs of rack-scale throughput — potentially the most consequential AI hardware generation since the Transformer took hold."
category: "hardware"
publishedAt: 2026-05-27
lang: "en"
featured: true
trending: true
sources:
  - name: "CNBC – NVIDIA Q1 FY2027 Earnings Live"
    url: "https://www.cnbc.com/2026/05/20/nvidia-nvda-earnings-report-q1-2027.html"
  - name: "VideoCardz – Vera Rubin NVL72 Detailed"
    url: "https://videocardz.com/newz/nvidia-vera-rubin-nvl72-detailed-72-gpus-36-cpus-260-tb-s-scale-up-bandwidth"
  - name: "Tom's Hardware – Vera Rubin NVL72 AI Supercomputer"
    url: "https://www.tomshardware.com/pc-components/gpus/nvidia-launches-vera-rubin-nvl72-ai-supercomputer-at-ces-promises-up-to-5x-greater-inference-performance-and-10x-lower-cost-per-token-than-blackwell-coming-2h-2026"
  - name: "Futurum Group – NVIDIA Q1 FY2027 Analysis"
    url: "https://futurumgroup.com/insights/nvidia-q1-fy2027-data-center-diversification-blackwell-scale-cpu-upside/"
tags:
  - "nvidia"
  - "vera-rubin"
  - "ai-chips"
  - "hardware"
  - "data-center"
  - "jensen-huang"
relatedSlugs:
  - "2026-05-22-nvidia-q1-fy2027-earnings-china-huawei-concession-en"
  - "2026-05-08-nvidia-iren-5gw-ai-factory-partnership-en"
  - "2026-05-18-tsmc-n2-2nm-chip-ramp-ai-hardware-en"
---

When NVIDIA reported $81.6 billion in Q1 FY2027 revenue — up 85 percent from a year earlier — the headline numbers were almost secondary. The more consequential news came in Jensen Huang's prepared remarks: Vera Rubin, NVIDIA's next-generation AI compute platform, will begin shipping to cloud customers in Q3 2026, with volume ramping aggressively through Q4.

For an industry that has spent the past eighteen months wrestling with Blackwell supply constraints and eye-watering compute bills, the confirmation carries real weight. Vera Rubin isn't just the next chip. It is a seven-component platform designed from the ground up for the agentic AI era — an era Huang argued, in no uncertain terms, has definitively arrived.

"Computing demand is growing exponentially — the agentic AI inflection point has arrived," Huang told analysts on the earnings call. "Grace Blackwell with NVLink is the king of inference today — delivering an order-of-magnitude lower cost per token — and Vera Rubin will extend that leadership even further."

## Seven Chips, One Platform

Vera Rubin is the product of what NVIDIA calls "extreme co-design" across the entire compute stack. The platform integrates six chip types announced at CES 2026 and a seventh — the Groq 3 LPX low-latency inference accelerator — added to the lineup in March. Together they form a unified system: the Vera CPU, the Rubin GPU, the NVLink 6 Switch, the ConnectX-9 SuperNIC, the BlueField-4 DPU, the Spectrum-6 Ethernet switch, and the LPX.

The Rubin GPU is the centerpiece. Built from two reticle dies with 336 billion transistors — roughly 60 percent more than the Blackwell B200 — it delivers 50 petaFLOPs of NVFP4 inference performance and 35 petaFLOPs of training throughput. Memory has moved to HBM4, with 288 gigabytes per GPU and a staggering 22 terabytes-per-second of on-chip bandwidth. That bandwidth figure matters as much as raw FLOP counts: the bottleneck in large language model inference is almost always memory throughput, not arithmetic capacity.

The Vera CPU is equally ambitious. At 227 billion transistors and built on custom Arm "Olympus" cores with 88 cores and 176 threads, it delivers 1.5 terabytes of LPDDR5x capacity and 1.2 terabytes-per-second of memory bandwidth. NVIDIA has been shipping standalone GPU accelerators for decades; the Vera CPU signals a serious bid to own both sides of the host-accelerator boundary.

## The NVL72: NVIDIA's New Unit of AI Infrastructure

The platform's flagship configuration, the NVL72, combines 72 Rubin GPUs with 36 Vera CPUs connected through NVLink 6, which triples the per-GPU switch bandwidth versus NVLink 5. The numbers that result are difficult to process intuitively: 3.6 exaFLOPs of NVFP4 inference per rack, 2.5 exaFLOPs of training throughput, 20.7 terabytes of HBM4 capacity, 54 terabytes of LPDDR5x, and 260 terabytes-per-second of scale-up bandwidth.

Compared with the Blackwell NVL72, NVIDIA projects 5× better inference performance and 10× lower cost per token at equivalent workload scale. Those aren't specifications to file away — they are the economics of an entirely different regime. A deployment that costs $100 million to serve at Blackwell speed could theoretically deliver the same throughput on Vera Rubin infrastructure for around $10 million. Whether those projections hold at real-world mixture-of-experts model sizes remains to be seen, but the trajectory is directionally unambiguous.

## Supply Reality Check

Enthusiasm about Vera Rubin's specs warrants tempering with production math. NVIDIA guided Q2 FY2027 revenue to approximately $91 billion — still largely Blackwell-driven. The company characteristically allocates 60 to 70 percent of new GPU production to hyperscalers during the first year, leaving enterprises, governments, and cloud startups competing for the remainder.

Analyst estimates put total 2026 Vera Rubin GPU output at somewhere between 200,000 and 300,000 units — a fraction of the installed Blackwell base. First customer deployments are expected across AWS, Google Cloud, Microsoft Azure, Oracle Cloud Infrastructure, and CoreWeave, in that order of likely allocation priority.

That supply constraint is, paradoxically, part of why NVIDIA guided the combined Blackwell-plus-Rubin platform to $1 trillion in cumulative revenue through 2027. Blackwell continues to sell as fast as it can be manufactured; Rubin adds a premium tier rather than replacing its predecessor. The $80 billion stock buyback and 25-fold dividend increase announced alongside earnings reflect management confidence that the demand runway extends well beyond any near-term supply ceiling.

## The Groq 3 LPX Factor

The seventh chip is worth separate attention. The Groq 3 LPX — NVIDIA acquired Groq's team and intellectual property earlier this year — is a low-latency inference accelerator optimized for the sub-100-millisecond response times that conversational AI and agentic real-time tasks demand. Traditional GPU-based inference is throughput-optimized; the LPX addresses a distinct dimension of the problem.

Its inclusion in the Vera Rubin platform signals that NVIDIA is building for a model of AI deployment where inference requests arrive in rapid bursts rather than batch jobs — the natural pattern of AI agents making dozens of tool calls per task. Combining maximum-throughput Rubin GPUs for heavy workloads with LPX accelerators for interactive latency is the kind of architectural sophistication that takes years to replicate.

## China: The Concession That Sharpens Focus

One subplot that shaped the earnings narrative was Jensen Huang's candid acknowledgment that NVIDIA has "largely conceded" China's advanced AI chip market to Huawei. The geopolitical restrictions that prevent NVIDIA from selling high-end H100 and H200 variants in China have left Huawei's Ascend 910C as the default option for Chinese hyperscalers and AI labs.

That concession removes a potential wildcard from supply forecasting. NVIDIA's China-compliant H20 chip continues to ship in modest volumes, but the company is no longer trying to win the flagship China market. From an investor perspective, that clarity is arguably more valuable than fighting a regulatory battle NVIDIA cannot control. From a competitive-dynamics perspective, it means the race for AI infrastructure supremacy is now, more than ever, a contest between NVIDIA and the cloud providers' custom silicon programs — Google's TPU, Amazon's Trainium, and Microsoft's Maia.

## What Vera Rubin Means for the Next Two Years

The architecture decisions embedded in Vera Rubin reflect a clear read of where AI compute is heading. Multi-step agentic workflows, long-context reasoning models, and mixture-of-experts architectures all stress memory capacity and bandwidth more than raw arithmetic throughput. HBM4's 22 TB/s bandwidth, 260 TB/s NVLink-6 scale-up, and the LPX's latency story are answers to those specific demands.

The broader implication is that the economics of inference are about to shift again. Every year since the 2022 ChatGPT moment, the cost of a million tokens has fallen by roughly 80 percent — not because OpenAI or Anthropic became more efficient, but because the hardware they run on got dramatically faster at fixed power envelopes. Vera Rubin's 10× cost-per-token improvement over Blackwell, if it materializes, would accelerate that trend and expand the range of tasks where deploying AI agents is economically rational.

For the enterprises, developers, and researchers waiting on the other side of NVIDIA's allocation queue, Q3 2026 cannot arrive quickly enough.
