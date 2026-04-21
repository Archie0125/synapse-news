---
title: "Google in Talks With Marvell to Co-Develop Two AI Chips, Reshaping the Custom Silicon Race"
summary: "Google is negotiating a deal with Marvell Technology to jointly develop two new AI chips: a memory processing unit designed to eliminate inference bottlenecks alongside its existing TPUs, and a cheaper, more efficient inference-optimized TPU. The talks add Marvell as a third custom chip design partner alongside Broadcom and MediaTek, and sent Marvell shares surging while Broadcom stock fell sharply."
category: "hardware"
publishedAt: 2026-04-21
lang: "en"
featured: false
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/20/marvell-stock-google-custom-ai-chips.html"
  - name: "BNN Bloomberg"
    url: "https://www.bnnbloomberg.ca/investing/2026/04/20/marvell-shares-gain-on-report-of-deal-talks-with-google-to-develop-two-ai-chips/"
  - name: "WCCFTech"
    url: "https://wccftech.com/google-pulls-marvell-into-a-two-chip-tpu-plan-reshaping-ai-inference-for-asics/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/google-marvell-ai-chips-inference-tpu-broadcom"
tags:
  - "google"
  - "marvell"
  - "tpu"
  - "ai-chips"
  - "custom-silicon"
  - "inference"
  - "hardware"
relatedSlugs:
  - "2026-04-15-meta-broadcom-mtia-chip-deal-en"
  - "2026-04-10-tsmc-q1-2026-record-revenue-en"
  - "2026-04-08-semiconductor-sales-record-2026-en"
---

Google's strategy for reducing its dependence on Nvidia just took a significant new turn. According to reporting by The Information, Alphabet is in active talks with Marvell Technology to co-develop two distinct AI chips — an arrangement that would add Marvell as a third custom silicon design partner alongside Broadcom and MediaTek, and signal a deliberate push to diversify its AI infrastructure supply chain as inference costs become the dominant variable in AI deployment economics.

The news sent Marvell shares climbing more than five percent in pre-market trading on April 20, extending a year-to-date gain that now stands at approximately 84% from its December 31 close of $80.46. Broadcom — which currently designs Google's Tensor Processing Units under a long-term supply agreement — saw its shares fall sharply on the announcement, a sign that investors read the move as a partial realignment of Google's custom chip strategy.

## The Two Chips Google Wants Marvell to Build

The reported collaboration covers two separate chips with distinct roles in Google's AI infrastructure stack:

**A Memory Processing Unit (MPU)**: The first chip would function as a complement to Google's existing fleet of Tensor Processing Units. TPUs are optimized for the matrix multiplication workloads that dominate model training and large-scale inference, but they increasingly face a bottleneck at the memory interface — the speed at which data can be moved into and out of the processing cores. The proposed MPU would address this constraint directly, sitting adjacent to the TPU and managing memory operations with specialized hardware to reduce the latency penalty that currently limits throughput on large model workloads.

Google and Marvell reportedly plan to finalize the MPU design over the next year before entering trial production, with initial manufacturing targets in the range of two million units.

**An Inference-Optimized TPU**: The second chip would be an entirely new TPU architecture purpose-built for inference — the phase where trained models serve actual user requests rather than learn from data. This chip would be designed to be cheaper to produce and more power-efficient per inference operation than the current TPU generation, which was architected with training workloads in mind. As AI applications scale from thousands to hundreds of millions of daily active users, inference costs — not training costs — have become the primary operating expense for AI companies.

## Why This Matters: Inference Is Now the Battleground

The shift in emphasis from training to inference reflects a fundamental change in how the AI industry operates in 2026. In 2022 and 2023, the most compute-intensive workloads were pre-training runs for frontier models — enormous one-time jobs that required the largest GPU clusters on earth for months at a time. Today, those training runs still happen, but the continuous cost of serving billions of queries per day across ChatGPT, Gemini, Claude, and their enterprise API customers has grown to dwarf training costs in aggregate.

Google's internal economics follow the same pattern. Serving Gemini queries in Search, Workspace, and the consumer app requires inference capacity that runs continuously at scale, and optimizing the cost-per-token of those workloads has become a first-order engineering priority. A cheaper, more efficient inference-specialized TPU would meaningfully reduce the operating cost of every Gemini API call.

The custom ASIC market — which includes Google's TPUs, Meta's MTIA, Amazon's Inferentia, and Microsoft's Maia — is projected to grow 45% in 2026 and reach $118 billion by 2033, according to market research cited in recent reports. The underlying driver is exactly this shift: hyperscalers are discovering that general-purpose GPUs are not the most economical tool for steady-state inference at their scale.

## Marvell's Position in the AI Chip Ecosystem

Marvell is not a household name in the consumer technology industry, but it occupies a strategically critical position in the semiconductor supply chain. The company has deep expertise in custom ASIC design, networking silicon, and high-speed interconnects — exactly the capabilities that hyperscalers need when designing bespoke chips at scale.

Marvell already designs custom chips for Amazon Web Services and Microsoft Azure, giving it a playbook for the kind of long-term, high-volume relationship that Google is proposing. Adding Google to that client roster would cement Marvell's position as the preferred custom silicon design partner for the major cloud providers, a niche that is growing rapidly as the Big Three hyperscalers collectively spend hundreds of billions of dollars on AI infrastructure.

The company's stock rally this year reflects investor recognition of this positioning. Marvell's 84% year-to-date gain compares favorably to Nvidia's roughly 30% gain over the same period — a sign that custom ASIC vendors are increasingly viewed as structural beneficiaries of AI capex even as direct GPU competition intensifies.

## The Broadcom Complication

The optics of the Marvell talks are complicated by Broadcom's existing relationship with Google. Broadcom has been Google's primary TPU design partner for years, and earlier in April the two companies reportedly locked in a new agreement running through 2031 that covers the current TPU roadmap. Broadcom CEO Hock Tan has positioned AI custom silicon as the company's core growth driver, and has discussed it extensively with investors as a multi-year revenue tailwind.

Google's simultaneous negotiation with Marvell does not necessarily mean it is preparing to exit the Broadcom relationship — the two chips under discussion would serve different functions than Broadcom's existing TPUs. But the signal to Broadcom is clear: Google is not content with a single-vendor approach to custom silicon, and it is actively developing the organizational capability to manage multiple chip design relationships concurrently.

That diversification makes strategic sense. As AI infrastructure costs have become a defining variable in competitive positioning, hyperscalers have strong incentives to maintain optionality in their silicon supply chains, avoiding the kind of single-point dependency that would give any one vendor pricing leverage over a critical input.

## What Comes Next

The discussions between Google and Marvell have not yet produced a signed contract, and both companies declined to comment on the reported talks. Chip development timelines are long — from initial design specification to volume production, a new custom ASIC typically requires two to three years — so any chips emerging from this partnership would likely enter deployment in 2028 or 2029.

In the near term, the market reaction tells most of the story: investors are treating the report as evidence that the custom AI chip market is expanding faster than expected, and that Marvell is positioned to capture a meaningful share of that expansion. For Nvidia, which continues to command the market for general-purpose AI compute, the proliferation of custom ASIC programs by hyperscalers represents a slow but steady erosion of addressable market at the margin.

The silicon war is not binary. It will be won and lost across dozens of specialized workloads, and every chip that a hyperscaler designs in-house is one that Nvidia does not sell.
