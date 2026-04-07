---
title: "NVIDIA Vera Rubin NVL72 Enters Full Production — 5x Blackwell Performance Per Rack"
summary: "NVIDIA's next-generation Vera Rubin NVL72 AI supercomputer has entered full production ahead of its originally guided H2 2026 schedule. The rack-scale system delivers 3.6 exaflops of inference compute and up to 5x greater inference performance and 10x lower cost per token compared to Blackwell, with AWS, Google Cloud, Microsoft Azure, and CoreWeave among the first deployment wave."
category: "hardware"
publishedAt: 2026-04-07
lang: "en"
featured: false
trending: true
sources:
  - name: "NVIDIA Newsroom: Rubin Platform AI Supercomputer"
    url: "https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer"
  - name: "Microsoft Azure Blog: Strategic AI Datacenter Planning with NVIDIA Rubin"
    url: "https://azure.microsoft.com/en-us/blog/microsofts-strategic-ai-datacenter-planning-enables-seamless-large-scale-nvidia-rubin-deployments/"
  - name: "Tom's Hardware: NVIDIA Vera Rubin NVL72 AI Supercomputer"
    url: "https://www.tomshardware.com/pc-components/gpus/nvidia-launches-vera-rubin-nvl72-ai-supercomputer-at-ces-promises-up-to-5x-greater-inference-performance-and-10x-lower-cost-per-token-than-blackwell-coming-2h-2026"
tags:
  - "NVIDIA"
  - "Vera Rubin"
  - "GPU"
  - "AI infrastructure"
  - "data centers"
  - "cloud computing"
relatedSlugs:
  - "2026-04-03-nvidia-blackwell-supply-en"
  - "2026-04-05-nvidia-marvell-nvlink-fusion-en"
  - "2026-04-04-amd-mi300x-enterprise-en"
---

# NVIDIA Vera Rubin NVL72 Enters Full Production — 5x Blackwell Performance Per Rack

NVIDIA's Vera Rubin NVL72, the company's most powerful AI supercomputer to date, has entered full production — ahead of the H2 2026 timeline CEO Jensen Huang originally announced at CES 2026. The news marks a significant inflection point in the AI infrastructure arms race, as hyperscalers and cloud providers rush to secure rack allocations for a system that NVIDIA claims delivers **5x greater inference performance** and **10x lower cost per token** than its predecessor, the Blackwell platform.

The Vera Rubin generation had been the subject of intense industry anticipation since its announcement. Confirmation that production has commenced ahead of schedule — at a time when AI compute demand continues to outstrip supply — represents both a technical and supply chain achievement for NVIDIA and its manufacturing partners.

## What's Inside the NVL72

The NVL72 is a rack-scale system, meaning the fundamental unit of deployment is an entire rack rather than a discrete GPU or server blade. Each rack integrates:

- **72 Rubin GPUs** — NVIDIA's next-generation data center GPU, built on a new architecture optimized for transformer inference workloads
- **36 Vera CPUs** — NVIDIA's in-house ARM-based CPU, making Vera Rubin the company's first rack system to ship without reliance on third-party processors from AMD or Intel
- **ConnectX-9 SuperNICs** — the latest generation of NVIDIA's high-performance networking adapters
- **BlueField-4 DPUs** — data processing units that offload networking, storage, and security tasks from the GPUs

Together, the system delivers **3.6 exaflops (EFLOPS) for inference** and **2.5 EFLOPS for training** per rack — roughly equivalent to what would have required multiple Blackwell server halls just 18 months ago.

The Vera CPU integration is particularly notable. By designing its own processor, NVIDIA gains tighter integration between the CPU and GPU memory subsystems, reducing the latency penalties that have historically plagued heterogeneous compute architectures. It also gives NVIDIA a vertically integrated AI compute stack — silicon, networking, and software — that mirrors the model Apple has pursued in consumer silicon.

## The Inference Economics

The headline claim of **10x lower cost per token** versus Blackwell deserves scrutiny, and NVIDIA has published workload-specific figures to support it. The gains come from three compounding factors:

1. **Higher arithmetic intensity**: Rubin GPUs feature a new generation of Tensor Core that delivers significantly higher FLOPS per watt on FP8 and INT4 precision formats — the workloads that dominate production inference.
2. **NVLink bandwidth scaling**: The NVL72's all-to-all GPU connectivity eliminates inter-node communication bottlenecks that emerge when running large models across multiple servers, reducing model-parallel overhead.
3. **Memory hierarchy redesign**: Rubin introduces a much larger on-chip L2 cache and high-bandwidth memory configuration, reducing trips to slower DRAM and improving batch processing efficiency for long-context requests.

For a cloud provider running a frontier language model at scale, even a 2-3x improvement in tokens-per-dollar is transformative. A 10x improvement — if borne out in production — would be seismic, enabling providers to substantially cut API prices while improving margins, or to run dramatically larger models within the same capex envelope.

## Who Gets the First Racks

NVIDIA has confirmed that the initial production allocation is going to a first wave of infrastructure partners:

- **Microsoft Azure**: Already integrating Rubin NVL72 across its AI superfactory buildouts in Wisconsin, Atlanta, and the planned Fairwater campus
- **Amazon Web Services**: Part of the first deployment wave, with timelines aligned to H2 2026 launches
- **Google Cloud**: A significant early customer, though details on specific deployment regions remain embargoed
- **Oracle Cloud Infrastructure (OCI)**: Expanding its AI infrastructure partnership with NVIDIA
- **CoreWeave**: The AI-specialized cloud provider, which has been among NVIDIA's most aggressive early adopters, is in the first wave
- **Lambda Labs, Nebius, and Nscale**: Emerging cloud providers specializing in AI compute are also confirmed

The allocation reflects both financial commitments and strategic partnerships. Microsoft's relationship with NVIDIA extends to deep Azure stack integrations, while CoreWeave's entire business model is predicated on having the latest NVIDIA silicon before competitors.

Notably absent from early announcements: any mention of Meta or Apple receiving early allocations, though both companies are known to have substantial GPU procurement operations that operate through different channels.

## The Broader Infrastructure Context

The Rubin NVL72's production timing lands at a moment of extraordinary capital intensity in AI infrastructure. A **1.2-gigawatt data center** that OpenAI is building in Abilene, Texas — reportedly in partnership with Microsoft — is under construction and expected to come online later this year. The facility is widely assumed to be a primary destination for Rubin-class hardware.

Meanwhile, NVIDIA's supply chain for the Rubin generation has been reorganized following hard lessons from the Blackwell ramp, which experienced delays related to thermal management issues in high-density rack configurations. The company worked closely with its Taiwan-based manufacturing partners — TSMC for the dies, Hon Hai (Foxconn) for rack assembly — to validate the NVL72's thermal and power delivery systems before committing to production.

The Rubin GPU itself is manufactured on TSMC's **N3 process node**, with a chip-on-wafer-on-substrate (CoWoS) advanced packaging configuration that allows the GPU die to be paired with high-bandwidth memory stacks. TSMC's CoWoS capacity, which was a significant bottleneck during the Hopper-to-Blackwell transition, has been substantially expanded through 2025 investments at facilities in Hsinchu and Taichung.

## What This Means for the Competition

AMD's MI350X accelerators and Intel's Gaudi 4 are both expected to ramp in H2 2026, but neither has claimed performance benchmarks in the same tier as the Rubin NVL72 for frontier inference workloads. The gap may be closing — AMD has made significant architectural improvements across successive generations — but NVIDIA's combination of hardware leadership and CUDA ecosystem lock-in remains formidable.

The more interesting competitive dynamic is at the system level. Google's own TPU v7 infrastructure and Amazon's Trainium3 chips are both designed to reduce dependence on NVIDIA for internal workloads, while being deployed alongside NVIDIA hardware in customer-facing cloud offerings. Neither Google nor Amazon has indicated plans to exit the NVIDIA supply chain; the proprietary silicon is cost optimization at scale, not a full replacement.

For startups and enterprises making infrastructure decisions today, the Rubin NVL72's production status changes the calculus. Leasing Blackwell-generation capacity at current market prices is now a short-term hedge, with the expectation that Rubin-class pricing will reset the economics within 12-18 months. The question for buyers is whether to lock in multi-year Blackwell contracts now or wait for Rubin availability to broaden — a bet on when exactly NVIDIA's production ramp translates into accessible cloud pricing.

## Jensen Huang's Bet on the Rack

The Vera Rubin NVL72 represents the culmination of a multi-year strategic bet Jensen Huang made when he decided NVIDIA needed to own the full rack — silicon, networking, cooling, and software — rather than selling components to ODMs. That bet now appears to be paying off: the NVL72 is a product no competitor can replicate simply by licensing NVIDIA's chip designs, because the competitive advantage lives in the integration.

Whether that 10x token cost claim survives contact with production workloads remains to be seen. But the arrival of Vera Rubin in full production, ahead of schedule, is a signal that NVIDIA's engineering and supply chain organization is operating at peak intensity — and that the AI infrastructure cycle is accelerating, not slowing.
