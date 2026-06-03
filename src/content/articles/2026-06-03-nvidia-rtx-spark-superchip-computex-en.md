---
title: "Nvidia RTX Spark: The Arm+Blackwell Superchip That Wants to Make Windows an AI OS"
summary: "Nvidia unveiled the RTX Spark Superchip at Computex 2026 — a 70-billion-transistor, TSMC 3nm SoC fusing a 20-core Grace Arm CPU with a Blackwell GPU, 128GB of unified LPDDR5X memory, and 1 petaFLOP of FP4 AI compute in a laptop form factor. Shipping this fall from Dell, HP, Lenovo, ASUS, MSI and Microsoft's Surface Laptop Ultra, it represents Nvidia's most ambitious push into personal computing yet."
category: "hardware"
publishedAt: 2026-06-03
lang: "en"
featured: false
trending: true
sources:
  - name: "Tom's Hardware — RTX Spark Unveil"
    url: "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory"
  - name: "Tom's Hardware — RTX Spark Roadmap"
    url: "https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman"
  - name: "Nvidia GeForce — Computex 2026"
    url: "https://www.nvidia.com/en-us/geforce/news/computex-2026-nvidia-geforce-rtx-announcements/"
  - name: "StorageReview"
    url: "https://www.storagereview.com/news/nvidia-computex-2026-keynote-the-rtx-spark-pc-family-dgx-station-and-physical-ai"
  - name: "HP Newsroom"
    url: "https://www.hp.com/us-en/newsroom/press-releases/2026/computex.html"
tags:
  - "Nvidia"
  - "RTX Spark"
  - "Computex 2026"
  - "Blackwell"
  - "Arm"
  - "laptop"
  - "AI PC"
  - "on-device AI"
relatedSlugs:
  - "2026-06-01-nvidia-n1x-computex-arm-laptop-launch-en"
  - "2026-06-02-intel-crescent-island-ai-gpu-computex-en"
  - "2026-06-02-amd-computex-2026-x3d-rx9070gre-consumer-en"
---

Jensen Huang took the Computex 2026 stage in Taipei wearing his signature leather jacket and carrying what Nvidia is positioning as the most significant PC architecture shift since the GPU itself. The RTX Spark Superchip — formally unveiled during Huang's keynote — is a single system-on-chip that combines a 20-core Grace Arm CPU with a Blackwell GPU, 128 gigabytes of unified memory, and enough AI compute to run 120-billion-parameter reasoning models locally on a device thin enough to fit in a laptop bag.

The announcement lands at a pivotal moment for the PC industry. Intel and AMD have spent the past two years trying to define the "AI PC" category through NPU acceleration bolted onto conventional x86 architectures. Nvidia is proposing something more radical: abandon x86 entirely, unify CPU and GPU memory on a single substrate, and build a machine that treats agentic AI workflows as the primary workload rather than a secondary feature.

## The Silicon

At its core, RTX Spark is a 70-billion-transistor part manufactured on TSMC's 3nm process. The architecture fuses two chiplets — a 20-core Grace CPU and a Blackwell GPU with 6,144 CUDA cores — connected via NVLink-C2C at 600 GB/s, a bandwidth figure that dwarfs the PCI Express lanes connecting discrete GPUs in conventional laptops. The unified memory pool sits at 128GB of LPDDR5X with 300 GB/s of aggregate bandwidth.

The AI performance headline is 1 petaFLOP (1,000 teraFLOPs) of FP4 compute. To put that in context, the M4 Max in Apple's top MacBook Pro delivers approximately 38 TOPS of Neural Engine throughput — a different metric, but the order-of-magnitude difference illustrates the gap between purpose-built AI silicon and general-purpose accelerators. Nvidia is positioning RTX Spark as a competitor to Apple Silicon's integrated memory architecture, a comparison that would have seemed implausible eighteen months ago.

The chip is capable of running models up to 120 billion parameters with context windows stretching to one million tokens — locally, without a network connection. That means a developer or researcher can run a model roughly equivalent to GPT-4's parameter count as a background process on a laptop, something currently possible only on cloud infrastructure or purpose-built workstations costing upwards of $10,000.

## The Ecosystem

Nvidia has secured launch partners across every tier of the PC market. Dell, HP, Lenovo, ASUS, and MSI will all ship RTX Spark laptops starting this fall. The highest-profile device is the Microsoft Surface Laptop Ultra — a collaboration that underscores how central Microsoft's Windows AI strategy has become to Nvidia's plans. The Surface Ultra wields RTX Spark with the full 128GB memory configuration and a co-designed thermal solution that Nvidia describes as enabling "sustained AI workloads" rather than burst-and-throttle operation.

ASUS's ProArt P14 and P16 target creative professionals and AI researchers who want to run local inference for image generation, audio processing, and document understanding without sending data to the cloud. HP's configuration skews toward enterprise deployments where data sovereignty and compliance requirements make cloud-hosted AI legally or contractually problematic.

The GPU performance in gaming workloads is said to be equivalent to a discrete RTX 5070, which at roughly $599 currently represents the mainstream-enthusiast tier of Nvidia's GPU lineup. That parity claim would make RTX Spark laptops genuinely competitive with traditional gaming laptops while adding capabilities those machines cannot match.

## The Platform Play

RTX Spark is not just a chip — it is a platform, and Nvidia's ambitions are architectural. The company is working with Microsoft to position Windows as what Huang called an "agentic AI OS": an operating system where local AI models can orchestrate file management, application control, background research, and multi-agent task delegation without cloud dependencies.

This vision aligns with Microsoft's own Aion 1.0 announcement at Build 2026, which ships a 14-billion parameter reasoning model in-box with Windows. The combination of Aion 1.0 running on RTX Spark hardware creates a device that can, in theory, plan and execute multi-step tasks autonomously using only local compute. Whether the software ecosystem — applications designed to expose the right tool interfaces to a local model — will mature quickly enough to realize that vision is a separate question.

Nvidia also announced DLSS 4.5, its latest AI-upscaling technology, which runs on RTX Spark to deliver what the company claims is native-equivalent visual quality at significantly lower rendering cost. For gaming workloads, DLSS 4.5 on a unified memory architecture offers different performance characteristics than discrete GPU implementations, potentially enabling high-fidelity gaming on fanless or near-fanless form factors.

## The Three-Generation Roadmap

In a move that signals long-term commitment to the platform, Nvidia outlined three generations of RTX Spark silicon:

**Grace Blackwell (Current)** — The chip announced at Computex, shipping fall 2026 with LPDDR5X memory.

**Vera Rubin Spark (Second Generation)** — A newly designed Vera CPU paired with a Rubin-generation GPU and LPDDR6 memory, expected to roughly double AI compute performance. No launch date announced.

**Rosa Feynman Spark (Third Generation)** — A Rosa CPU with stacked Feynman GPUs. Nvidia described Feynman as utilizing vertical 3D stacking for GPU chiplets, a manufacturing approach that would allow memory-bandwidth scaling beyond what planar architectures can achieve.

Providing a three-generation roadmap at a product launch is a deliberate signal to OEM partners and enterprise buyers: this is not an experiment. Nvidia is committing to the Arm CPU architecture for personal computing devices in the same way it committed to the Hopper-Blackwell-Rubin cadence for data center products.

## The Competitive Context

RTX Spark enters a market where Apple Silicon has held an unchallenged performance-per-watt lead for five years. The M4 Ultra in Apple's Mac Studio already demonstrates what unified memory architecture can do for AI inference, and Apple's developer ecosystem has had years to optimize for it. Nvidia's advantage is the installed base of CUDA software, the breadth of its gaming ecosystem, and crucially, Windows — a platform that represents roughly 90% of global PC shipments and has essentially zero addressable market for Apple's hardware.

Qualcomm's Snapdragon X Elite had positioned Windows-on-Arm as an efficiency story; RTX Spark repositions it as a performance story. Whether that distinction translates into commercial success depends on whether the productivity and AI software ecosystem for Windows on Arm can close the compatibility gap with legacy x86 applications — a problem that has undermined every previous Windows-on-Arm attempt, from the original Surface RT to Qualcomm's early Snapdragon laptops.

Nvidia's bet is that this time, the AI workload is compelling enough that developers will follow the hardware rather than waiting for the hardware to follow the software.

Devices ship fall 2026. Pricing has not been announced.
