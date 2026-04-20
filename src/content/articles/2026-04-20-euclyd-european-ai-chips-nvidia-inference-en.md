---
title: "European AI Chip Startups Target Nvidia's Inference Dominance With $100M+ Fundraises"
summary: "A wave of European AI chip startups — led by Dutch company Euclyd, backed by ex-ASML CEO Peter Wennink — are raising $100 million or more each, targeting what they say is a 100x power efficiency gap in Nvidia's inference stack. As AI inference workloads scale globally, a new generation of purpose-built silicon is emerging to challenge GPU supremacy."
category: "hardware"
publishedAt: 2026-04-20
lang: "en"
featured: false
trending: true
sources:
  - name: "CNBC — Nvidia rival tells CNBC it's seeking at least $100 million in funding"
    url: "https://www.cnbc.com/2026/04/17/nvidia-rivals-chip-market-funding-ai-asml-euclyd.html"
  - name: "NL Times — Eindhoven-based Euclyd targets €100 million funding round"
    url: "https://nltimes.nl/2026/04/17/eindhoven-based-euclyd-targets-eu100-million-funding-round-ai-chip-expansion"
  - name: "EE News Europe — Euclyd Unveils CRAFTWERK: Exascale Inference Architecture"
    url: "https://www.eenewseurope.com/en/euclyd-unveils-craftwerk-exascale-inference-architecture-targets-agentic-ai-at-record-efficiency/"
  - name: "Tech Startups — AI chip startups raise billions to challenge Nvidia's dominance"
    url: "https://techstartups.com/2026/04/17/ai-chip-startups-raise-billions-to-challenge-nvidias-dominance-in-inference-race/"
tags:
  - "AI-chips"
  - "Nvidia"
  - "Euclyd"
  - "Europe"
  - "inference"
  - "semiconductors"
relatedSlugs:
  - "2026-04-07-nvidia-vera-rubin-nvl72-production-en"
  - "2026-04-19-huawei-ascend-950pr-china-ai-chip-en"
  - "2026-04-05-cognichip-ai-chip-design-en"
---

Nvidia's grip on AI infrastructure spending has looked unassailable for years — but a cluster of European hardware startups is betting that the economics of inference will fracture the market wide open, and they are raising serious capital to prove it.

Leading the charge is Euclyd, a Dutch startup based in Eindhoven that announced this week it is actively seeking a funding round of at least €100 million ($118 million). The company's pitch rests on a striking claim: its purpose-built inference chip system can deliver 100 times higher power efficiency than Nvidia's latest Vera Rubin generation for inference workloads. Euclyd is not alone — UK-based Fractile, photonics startup Optalysys, and German firm Arago are all reported to be seeking rounds of similar scale, signaling a coordinated surge of European hardware ambition aimed squarely at Nvidia's most lucrative market segment.

## What Euclyd Is Building

Euclyd was founded in 2024 by former ASML director Kas Kastrup, with a pedigree that carries significant weight in European semiconductor circles. The startup counts Peter Wennink — the longtime CEO who built ASML into the world's most strategically critical semiconductor equipment company — as an advisor and early investor. For a company that launched barely 18 months ago, that network access to the European chip supply chain ecosystem is unusual.

The company's flagship product is CRAFTWERK, which Euclyd describes as an "exascale inference architecture" targeting agentic AI workloads. The technical approach diverges significantly from the GPU paradigm. Where graphics processing units — including Nvidia's Vera Rubin and its predecessors — work by moving data from memory to compute cores for processing, then writing results back to memory, Euclyd's chips are designed to process data closer to where it is stored. This "compute-near-memory" or "near-memory computing" approach dramatically reduces the energy and time spent on data movement, which has emerged as one of the dominant bottlenecks in large language model inference at scale.

In modeled performance figures for Llama 4 Maverick — the multimodal open-weight model Meta released in April 2025 — Euclyd's CWS 32 multi-chiplet system projects 7.68 million tokens per second at just 125 kilowatts of power consumption. The company frames this as a 100x improvement in power efficiency and cost per token compared to leading GPU alternatives at equivalent token throughput. The critical caveat is that these remain modeled projections, not yet demonstrated at scale in real-world customer deployments.

Euclyd has built a working inference chip and is developing the full multi-chiplet system with a target of production-ready silicon by 2028. The company says it is in discussions with four potential first customers. The €100 million raise is intended to fund that product development sprint to first deliveries.

## Why Inference Is the Battleground

The strategic logic of challenging Nvidia specifically on inference rather than training is well-grounded in market economics. Training large models is an intensive but episodic activity, performed by a relatively small number of frontier labs with massive budgets and high tolerance for cost. Inference — running those trained models to serve billions of user queries — is continuous, scales with every new user, and is performed by every enterprise, startup, and application developer that builds on top of AI.

As model deployment has matured, inference has become the dominant share of total AI compute spending for most organizations. Analysts at Dealroom estimate that AI chip startups globally raised $8.3 billion in 2026, with inference-focused architectures attracting an increasingly large portion of that capital. Nvidia's Vera Rubin platform has extended its training dominance into inference, but the power efficiency and per-token cost arguments for purpose-built inference silicon are becoming harder to dismiss as workloads scale.

The agentic AI shift amplifies this dynamic. A single user interaction that triggers an AI agent capable of taking dozens or hundreds of sequential inference steps multiplies compute requirements dramatically compared to a simple chatbot response. Euclyd's CRAFTWERK is specifically positioned for this "agentic AI" use case — high-throughput, sustained inference rather than bursty request-response patterns.

## Fractile, Optalysys, and the European Cluster

Euclyd is the most visible of several European chip challengers currently in fundraising mode. Fractile, a UK startup, has separately confirmed it is seeking a round of approximately £160 million ($200 million) to develop transformer-specific inference silicon. The company received an early-stage investment from the NATO Innovation Fund — a signal that European defense and security considerations are being woven into AI chip investment alongside commercial motivations.

Optalysys is pursuing a photonics-based approach, using optical computing to perform AI matrix multiplication at the speed of light rather than through silicon transistors. The company claims orders-of-magnitude energy efficiency advantages for specific inference workloads, though photonic computing faces its own maturation challenges in scaling to practical deployment.

Arago, the German entrant, is focused on the software-hardware co-design layer, building inference acceleration systems that are optimized in conjunction with the model architecture rather than treating the model as a fixed input.

The geographic concentration of these efforts in Europe reflects several factors: the proximity of the Dutch-German-UK corridor to ASML's supply chain and semiconductor equipment expertise; supportive EU industrial policy through the European Chips Act; and the presence of engineering talent from Arm, ASML, and Qualcomm's European research centers that has been seeding startups at an accelerating pace.

## Nvidia's Position and the Path for Challengers

None of this implies that Nvidia is in immediate danger. The company's data center revenue reached $62.31 billion in Q4 FY2026, up 75% year over year, with Q1 FY2027 guidance calling for approximately $78 billion. Its software ecosystem — CUDA, cuDNN, the NIM inference microservice platform, and deep integrations with every major cloud provider — represents a moat that pure silicon efficiency claims cannot overcome overnight.

Historically, challenger chip companies have found a narrow but real path to market by targeting specific inference workloads where the incumbent's general-purpose architecture is genuinely inefficient, building a beachhead customer base, and using that revenue and credibility to gradually expand. Cerebras Systems followed this path with wafer-scale chips for large models; Groq has done it with deterministic inference latency for real-time applications. The European startups are betting the agentic inference era creates a new opening.

The 2028 production target that Euclyd has set is realistic for a chip development timeline, but it also means the company will need to demonstrate performance against whatever generation of Nvidia silicon is current at that time — not today's Vera Rubin, but potentially the successor architecture that follows it. The AI hardware ladder moves quickly.

What is clear from this week's fundraising signals is that the inference market's scale and energy cost are large enough to attract serious capital and serious talent into the challenge. Whether Euclyd, Fractile, or any of their European peers can translate engineering efficiency claims into sustained commercial traction is a question that the next 24 months will begin to answer.
