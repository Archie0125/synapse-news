---
title: "NVIDIA and SK Hynix Lock In Multiyear HBM4 Partnership for Vera Rubin AI Factories"
summary: "NVIDIA and SK Hynix announced a multiyear co-development agreement on June 7-8 spanning HBM4 memory, Vera Rubin supercomputers, Vera CPUs, and Jetson Thor robotics platforms — a deal that brings the memory supplier into silicon definition discussions before chips are taped out, a first for the industry."
category: "hardware"
publishedAt: 2026-07-08
lang: "en"
featured: false
trending: true
sources:
  - name: "NVIDIA Newsroom"
    url: "https://nvidianews.nvidia.com/news/sk-hynix-ai-factory"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317994/20260608/nvidia-sk-hynix-sign-multiyear-memory-pact-why-your-next-pcs-ram-just-got-more-expensive-build.htm"
  - name: "AI Magazine"
    url: "https://aimagazine.com/news/nvidia-sk-hynix-partner-on-next-gen-memory-for-ai"
  - name: "TrendForce"
    url: "https://www.trendforce.com/news/2026/06/08/news-sk-hynix-to-supply-memory-for-nvidia-vera-cpu-as-partnership-deepens-samsung-meeting-on-june-8-in-spotlight/"
tags:
  - "NVIDIA"
  - "SK Hynix"
  - "HBM4"
  - "Vera Rubin"
  - "memory"
  - "AI chips"
  - "hardware"
  - "data centers"
relatedSlugs:
  - "2026-04-03-nvidia-blackwell-supply-en"
  - "2026-07-08-south-korea-880b-ai-chip-plan-en"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-en"
---

When NVIDIA and SK Hynix announced a multiyear technology partnership on June 7-8, 2026, it looked at first like a straightforward supply agreement: the world's dominant AI chip designer locking in memory from one of the world's dominant HBM suppliers. Dig deeper and the partnership represents something more structurally significant — a fundamental shift in how AI chip architecture gets defined, and a preview of what AI hardware economics will look like in the Vera Rubin era.

## More Than a Supply Deal

The conventional model for chip and memory development has always been sequential: a processor company designs its chip, specifies its memory interface, and then memory suppliers build to that spec. NVIDIA and SK Hynix are explicitly breaking that model.

Under the partnership, SK Hynix engineers will collaborate with NVIDIA's chip architects **during the silicon definition phase** — before tape-out, before specifications are finalized, before silicon is even committed. The goal is to eliminate "last-mile inefficiencies" that arise when memory designers and processor designers work in isolation, each optimizing for their own component without full visibility into how the other half of the equation behaves.

This early co-design approach is not unprecedented — Apple has done something similar with its DRAM suppliers for years — but it is a first for hyperscale AI accelerators at this level of integration. The implication is that future Vera Rubin successor architectures may be as much the product of joint NVIDIA-SK Hynix engineering as they are of NVIDIA's in-house GPU teams.

## What the Partnership Covers

The agreement extends across NVIDIA's full hardware roadmap:

- **Vera Rubin NVL72 supercomputers**: The immediate focus, with SK Hynix as a confirmed HBM4 supplier alongside Samsung and Micron. Each VR200 NVL72 rack costs hyperscale cloud providers approximately $7.8 million. Memory alone accounts for roughly 25% of that figure — around $2 million per rack — making memory the single largest cost component aside from the compute dies themselves.
- **Vera CPUs**: Jensen Huang confirmed that Vera CPUs — NVIDIA's first in-house general-purpose processor, designed to replace x86 CPUs in AI servers — will use SK Hynix memory, extending the partnership beyond the GPU stack.
- **RTX Spark PCs**: The next generation of NVIDIA's consumer and workstation AI PCs, bringing the co-development relationship into products that will reach individual developers and researchers.
- **Jetson Thor robotics platforms**: NVIDIA's robotics compute module, used in humanoid robots and autonomous systems, will also draw on SK Hynix memory under the agreement.

The breadth is striking. NVIDIA is not simply diversifying its HBM supply risk — it is weaving SK Hynix into the design process across every product tier.

## The HBM4 Bottleneck and Why It Matters

High-bandwidth memory has been the critical constraint in AI hardware since the Hopper generation. Training large language models and running inference on frontier AI systems requires moving enormous amounts of data between the compute die and memory at extraordinary speeds. HBM stacks chips vertically to maximize bandwidth while minimizing latency — but the physics of stacking more dies, at higher bandwidth, with lower power consumption, is extraordinarily difficult.

HBM4, the generation being co-developed under this partnership, targets bandwidth of around 1.5 terabytes per second per stack — roughly double HBM3E's capacity. At those speeds, even tiny inefficiencies in the interface between the GPU and the memory become significant. The co-development model is precisely designed to address this: if SK Hynix and NVIDIA are designing the interface together, they can optimize parameters that a purely sequential approach would treat as fixed constraints.

For the hyperscalers ordering Vera Rubin systems, HBM4 supply is the primary constraint on how quickly they can build out AI capacity. NVIDIA has approved Samsung, SK Hynix, and Micron as HBM4 suppliers — but SK Hynix is the market leader, accounting for roughly half of global HBM output in 2026. The multiyear co-development agreement is, among other things, a signal to the market that SK Hynix supply is not at risk of being displaced by Samsung or Micron on strategic NVIDIA platforms.

## AI Applied to Chipmaking Itself

One underreported dimension of the partnership is its software component. The two companies will apply NVIDIA's AI tools — specifically CUDA-X libraries and NVIDIA PhysicsNeMo — to semiconductor chip design and manufacturing processes at SK Hynix's facilities. This includes accelerating semiconductor simulations, Technology Computer-Aided Design (TCAD) workflows, and internal engineering codes that model how materials and devices behave at nanoscale.

This is part of a broader trend NVIDIA has been pushing under its "AI for Every Industry" strategy: using its AI infrastructure to accelerate the industries that produce AI infrastructure. TSMC has deployed NVIDIA systems internally for similar purposes. The implication is that future generations of HBM chips may be designed, simulated, and refined using AI tools running on the very same architecture the chips will eventually power — a recursive loop that could meaningfully compress development timelines.

## Reading the Competitive Signals

The partnership carries several implicit messages for the rest of the industry.

For **Samsung**, which competes directly with SK Hynix in HBM and which is also a confirmed HBM4 supplier, the news is a warning: SK Hynix is not merely a vendor, but a design partner with visibility into NVIDIA's roadmap. That relationship depth is difficult to replicate by simply offering better pricing or faster delivery.

For **Micron**, the third HBM4 supplier, the message is similar. Micron has been working aggressively to catch SK Hynix in HBM market share, with its HBM3E achieving competitive performance in testing. But market share in components is different from co-design participation in architecture.

For **AMD**, which competes with NVIDIA in the AI accelerator market, the announcement highlights a growing asymmetry: NVIDIA's relationships with its supply chain are not just commercial, they are technical. AMD has its own memory partnerships, but the public signal from NVIDIA and SK Hynix — a joint announcement from both CEOs, an NVIDIA Newsroom feature — is a deliberate demonstration of depth.

For **hyperscalers** building AI infrastructure, the partnership is reassuring: NVIDIA and its primary HBM supplier are aligned on a multiyear roadmap, reducing the risk of the supply disruptions that plagued H100 builds in 2023 and H200 builds in 2024.

## The $7.8 Million Question

The Vera Rubin NVL72 rack price — approximately $7.8 million per unit at hyperscaler volume pricing — frames the stakes. With Microsoft, Google, Amazon, and Meta each ordering tens of thousands of these systems in 2026, the total addressable market for HBM4 alone runs into the hundreds of billions of dollars.

SK Hynix's position as NVIDIA's co-design partner, rather than simply a qualified component vendor, gives it structural advantages in the pricing and allocation of that market. The multiyear agreement locks that relationship in over the period when HBM4 demand will be at its peak — and begins co-development of the HBM5 generation that will define AI hardware economics in the late 2020s.

That is what makes the June partnership more significant than it appeared on announcement day: it is not just a supply deal, it is an architectural alliance.
