---
title: "Google and Intel Expand Multiyear AI Chip Partnership With Xeon 6 and Custom IPUs"
summary: "Google and Intel announced an expanded multiyear partnership on April 9 that commits Google Cloud to multiple generations of Intel Xeon 6 processors for AI workloads while deepening joint development of custom infrastructure processing units. The deal gives Intel a meaningful foothold in a data-center market long dominated by Nvidia and signals that CPUs are returning to relevance in AI infrastructure."
category: "hardware"
publishedAt: 2026-04-11
lang: "en"
featured: false
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/09/google-expands-partnership-with-intel-for-ai-chips-.html"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/04/09/intel-inks-multiyear-data-center-chip-partnership-google/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-04-09/intel-wins-google-commitment-to-use-xeon-chips-in-data-centers"
  - name: "The Register"
    url: "https://www.theregister.com/2026/04/09/google_intel_ipu/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/09/google-and-intel-deepen-ai-infrastructure-partnership/"
tags:
  - "Intel"
  - "Google"
  - "Xeon"
  - "IPU"
  - "AI chips"
  - "data center"
  - "hardware"
  - "cloud infrastructure"
relatedSlugs:
  - "2026-04-07-nvidia-vera-rubin-nvl72-production-en"
  - "2026-04-04-amd-mi300x-enterprise-en"
  - "2026-04-10-tsmc-q1-2026-record-revenue-en"
---

Intel has spent the better part of three years trying to convince the AI industry that GPUs are not the only answer. On April 9, the company landed its most significant validation yet: a public, expanded multiyear partnership with Google Cloud that commits Alphabet's cloud division to multiple generations of Intel Xeon processors for AI inference and general-purpose computing—and deepens joint development of custom infrastructure processing units that Intel and Google have quietly been building together since 2022.

Intel's stock rose on the news. After a period of wrenching restructuring, layoffs, and leadership transition, the partnership announcement offered the market a rare affirmation: one of the world's most sophisticated cloud operators is betting on Intel's silicon roadmap for the long term.

## Two Pillars: Xeon and Custom IPUs

The partnership has two distinct components that address different layers of the AI data-center stack.

The first is a commitment to Intel's Xeon 6 processor family. Google Cloud will continue deploying Xeon processors across its infrastructure and will adopt the latest Xeon 6 chips for AI inference workloads, training support, and general-purpose cloud computing. This matters because modern AI systems—particularly large-scale inference serving, retrieval-augmented generation, and agentic workloads—require CPU-side processing that scales in ways that are economically and architecturally distinct from GPU compute. As AI workloads mature from training-heavy to inference-heavy, the CPU's role in the data center has quietly grown.

The second component is an expanded co-development program for custom infrastructure processing units, or IPUs. Intel and Google have jointly developed IPU hardware since at least 2022, but the updated agreement expands both the scope and the roadmap commitment. IPUs are application-specific integrated circuits designed to handle infrastructure management tasks—encrypting and decrypting network traffic, coordinating storage hardware, managing virtual machine hypervisors—tasks that traditionally burdened the main CPU and sapped its capacity for user workloads. By offloading this overhead to a dedicated IPU, the servers running Google's AI services recover meaningful compute capacity for the actual intelligence layer.

The Register reported that Google's involvement in the IPU program now extends to influence over future chip design specifications—a level of collaboration that goes beyond a standard customer relationship and positions Google more as a co-architect of Intel's infrastructure silicon.

## Why This Is Significant for Intel

The timing of the announcement matters for Intel as an institution as much as it matters as a strategic partnership. Under CEO Lip-Bu Tan, who took the helm in early 2025, Intel has been executing a sharper strategy: refocus on core CPU and custom silicon strengths, reduce sprawl in manufacturing ambitions, and rebuild credibility with hyperscale customers. The Google deal is the clearest public signal that the strategy is gaining traction with the most discerning buyers in the industry.

Intel's Xeon 6 architecture delivered a significant performance-per-watt improvement over its predecessor, making it competitive for workloads that were previously awkward fits for CPU-based processing. More importantly, the density of Xeon 6 in inferencing pipelines—where latency and cost-per-query matter more than peak training throughput—has made CPU-based inferencing economically attractive again for certain workloads.

Intel also needs wins outside the pure GPU accelerator market, which Nvidia continues to dominate with commanding margins. The strategy of competing not on raw AI training throughput—where Nvidia's H100 and Blackwell family are effectively unassailable in the short term—but on the complementary CPU and network infrastructure layer is arguably more defensible. Google's commitment validates that Intel's targeting is correct.

## The CPU's Quiet Comeback in AI

The broader narrative here is one that the AI industry has been slow to fully appreciate: as AI deployments mature from experimental to production, the workload mix shifts in ways that favor heterogeneous computing over pure-GPU clusters. Early AI infrastructure was dominated by training runs—massively parallel workloads that GPUs handle with unmatched efficiency. But inference serving, which is now the economically dominant mode of AI operation, has different characteristics: many small, latency-sensitive requests, with CPU-side processing for data retrieval, context assembly, and routing decisions.

Several large cloud operators—AWS, Microsoft Azure, and now Google Cloud explicitly—have described the CPU as a first-class participant in their AI infrastructure, not merely a legacy component waiting to be displaced. Intel's Xeon 6, positioned as an inference-capable processor that handles the CPU-side of AI workloads efficiently while custom IPUs handle infrastructure overhead, fits neatly into this architecture.

Analysts at Bernstein noted that the Google partnership "meaningfully de-risks Intel's data-center revenue trajectory through at least 2028," providing visibility that the company's previous quarters lacked. The partnership does not guarantee Intel's broader recovery—the company still faces severe competition in foundry services and custom silicon from TSMC and AMD—but it demonstrates that Intel's CPU business, properly focused, retains a durable position in the AI data-center ecosystem.

## What Google Gets

For Google, the partnership is a deliberate diversification strategy. While Google Cloud has deployed Nvidia hardware extensively—and will continue to through its TPU and GPU offerings—maintaining a deep relationship with Intel provides architectural flexibility and pricing leverage. Custom IPUs, in particular, represent infrastructure cost savings that compound at hyperscale: every efficiency point in networking, storage, and security overhead translates directly into more server capacity available for billable AI compute.

The partnership also advances Google's broader interest in having influence over the silicon it deploys at scale. Google already designs its own Tensor Processing Units (TPUs), its custom Axion ARM-based CPUs, and participates in the design of its custom networking ASICs. Co-developing Intel IPUs extends that design influence into the infrastructure silicon layer, giving Google another custom hardware lever in a data-center architecture increasingly defined by tight co-optimization between software and silicon.

For the industry watching this announcement, the message is clear: the GPU may be the star of the AI gold rush, but the surrounding infrastructure—the CPUs, IPUs, and network chips that make GPUs useful at scale—is where the next wave of hardware differentiation is being built. Intel, having found its footing in that layer, just signed its most important customer to a long-term commitment.
