---
title: "Google Unveils Ironwood TPU and Splits Its Eighth-Gen Chip Roadmap Into Training and Inference at Cloud Next 2026"
summary: "Google made its seventh-generation Ironwood TPU generally available at Cloud Next 2026, delivering 4.6 petaFLOPS per chip and 42.5 exaFLOPS at pod scale — a 10× leap over TPU v5p. The company simultaneously previewed its eighth-generation split architecture: a Broadcom-designed training chip and a MediaTek-designed inference chip, both on TSMC's 2nm process, targeting 2027. A $750 million partner fund and expanded A2A agent protocol round out Google's most comprehensive challenge yet to Nvidia's AI infrastructure dominance."
category: "hardware"
publishedAt: 2026-04-23
lang: "en"
featured: false
trending: true
sources:
  - name: "Google Cloud Blog — Ironwood TPU"
    url: "https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads/"
  - name: "Google Blog — Ironwood: The First TPU for the Age of Inference"
    url: "https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/"
  - name: "TechCrunch — Google Cloud launches two new AI chips"
    url: "https://techcrunch.com/2026/04/22/google-cloud-next-new-tpu-ai-chips-compete-with-nvidia/"
  - name: "The Next Web — Ironwood TPU inference coverage"
    url: "https://thenextweb.com/news/google-ironwood-tpu-inference-cloud-next"
  - name: "HyperFrame Research — TPU 8t and 8i analysis"
    url: "https://hyperframeresearch.com/2026/04/22/google-cloud-next-2026-google-cloud-bifurcates-the-ai-future-specialized-tpu-8t-and-8i-architectures-signal-the-end-of-general-purpose-silicon/"
tags:
  - "Google"
  - "TPU"
  - "Ironwood"
  - "AI chips"
  - "Nvidia"
  - "Cloud Next"
  - "infrastructure"
  - "Gemini"
relatedSlugs:
  - "2026-04-11-rebellions-400m-rebelrack-nvidia-inference-en"
  - "2026-04-17-nvidia-ising-quantum-ai-models-en"
  - "2026-04-10-google-gemini-31-flash-live-en"
---

Google used its biggest annual customer conference to fire its most direct salvo yet against Nvidia's dominance of the AI chip market. At Google Cloud Next 2026 in Las Vegas on April 22, the company made its seventh-generation Tensor Processing Unit — Ironwood — generally available, while simultaneously previewing a split eighth-generation architecture that divides AI workloads between dedicated training and inference silicon. The announcements, alongside a $750 million agentic AI partner fund and major updates to Google's agent interoperability protocol, signal a company that is no longer content to play a supporting role in AI infrastructure.

## Ironwood: Designed for Inference at Scale

The name carries intent. Google describes Ironwood as "the first TPU for the age of inference," reflecting a fundamental shift in where AI compute is actually being consumed. In the early deep learning era, training dominated GPU demand. Now, with frontier models largely trained and deployed to hundreds of millions of users, serving predictions in real time — inference — is consuming a rapidly growing share of every data center's compute budget.

Each Ironwood chip delivers 4.6 petaFLOPS of compute and 192 gigabytes of high-bandwidth memory. At pod scale, a 9,216-chip Ironwood superpod delivers 42.5 exaFLOPS of aggregate performance. Google claims a 10× peak performance improvement over the TPU v5p and more than 4× better performance per chip compared to the v6e Trillium, the prior generation released less than two years ago. Both training and inference workloads benefit from the improvement, but the architecture is optimized for inference throughput in ways that earlier generations were not.

One of Ironwood's key design choices is a disaggregated memory architecture: compute and memory can be scaled independently, which matters enormously when running millions of simultaneous inference requests. In those workloads, memory bandwidth often becomes the bottleneck before raw compute does. Google also redesigned Ironwood's inter-chip interconnect to let pods share a unified high-bandwidth memory pool rather than copying data between chips — a direct optimization for long-context inference, where models like Gemini need to process hundreds of thousands of tokens in a single pass without repeated memory transfers inflating latency.

Ironwood is available immediately on Google Cloud, meaning customers can now provision it on demand alongside H100 and GB200 instances from competing providers — a significant change from the era when Google's TPUs were largely reserved for internal workloads.

## The Eighth Generation: Splitting the Stack

More strategically striking than Ironwood's launch was the roadmap Google laid out for its eighth-generation chips, which will be the first time the company has deliberately designed separate chips for training and inference rather than a single general-purpose processor.

TPU 8t, codenamed "Sunfish," is co-designed with Broadcom and targets training workloads. It will scale to 9,600 chips in a single superpod, backed by two petabytes of shared high-bandwidth memory, and is projected to deliver three times the processing power of Ironwood. Both Sunfish and its inference counterpart are built on TSMC's 2nm process and are expected to reach production in late 2027.

TPU 8i, codenamed "Zebrafish," is co-designed with MediaTek — an unusual partnership that illustrates how broadly Google is distributing its silicon design work — and targets inference exclusively. Zebrafish uses a new "Boardfly" topology to directly connect 1,152 chips in a single pod, carries 3× more on-chip SRAM than previous generations to keep KV caches entirely on silicon rather than in slower off-chip memory, and integrates a specialized Collectives Acceleration Engine. Google projects 80% better performance per dollar for inference versus the prior generation.

The decision to bifurcate the eighth generation is a philosophical break from the general-purpose GPU paradigm that Nvidia has built its $3 trillion business around. It is a bet that by 2027, training and inference will be sufficiently different in their memory access patterns, parallelism requirements, and power profiles that optimizing a single chip for both is an unacceptable engineering compromise.

HyperFrame Research called the TPU 8t/8i split "the most direct architectural rejection of the GPU paradigm from any hyperscaler to date," noting that if Google hits its 2027 production targets, enterprise procurement decisions for the next wave of AI infrastructure will look substantially different from those made over the past three years.

## The Agent Stack: $750 Million and the A2A Protocol

Cloud Next 2026 was not purely a silicon story. Google committed $750 million to an agentic AI partner fund aimed at helping enterprises across its 120,000-member ecosystem build, prototype, and deploy autonomous agent systems. The fund includes direct engineering support from Google forward-deployed engineers, infrastructure credits, upskilling programs, and prototyping resources.

Central to the conference's software narrative was the expansion of Google's Agent-to-Agent (A2A) protocol, which lets Gemini-native agents communicate with third-party agents from ServiceNow, Salesforce, Atlassian, SAP, and others without custom integration code. The practical effect is significant: a Salesforce Agentforce agent can hand a task mid-workflow to a Vertex AI agent, which can query a ServiceNow system for IT asset data — all over A2A, with no bespoke connectors. Deloitte announced it is building cross-platform agent workflows for enterprise clients using this mechanism. Merck announced a partnership to deploy Gemini Enterprise across its R&D workflows and manufacturing automation.

Google also announced Agent Gateway, a centralized policy enforcement layer for multi-agent systems that speaks MCP, A2A, and proprietary protocols simultaneously. The gateway enables visibility into agent-to-agent calls, rate limiting, compliance logging, and access controls — infrastructure that enterprises need before they can responsibly run autonomous agent networks in regulated industries.

## Competitive Context

The timing is deliberate. Nvidia's GB200 NVL72 systems remain the performance benchmark for dense AI training, and Nvidia's software ecosystem and customer relationships represent a moat that years of competing attempts have failed to erode. But the competitive environment has shifted. Supply constraints on Nvidia hardware have pushed major AI labs — Anthropic, Meta, and as reported separately today, Mira Murati's Thinking Machines Lab — to sign multi-billion dollar commitments to Google's compute roadmap.

Anthropic's arrangement with Google is expanding to 3.5 gigawatts of compute capacity in 2027, making it the anchor customer for both Ironwood and the eighth-generation platform. That scale of commitment gives Google the utilization guarantees it needs to justify the capital expenditure of Ironwood's production ramp, while giving Anthropic a credible alternative supply chain as it grows toward and beyond $3 billion in annualized revenue.

For Nvidia, the most significant development at Cloud Next 2026 is not any single chip specification but the emerging reality that the largest frontier AI labs are no longer treating GPU access as their only strategic infrastructure option. Google has not yet out-engineered Nvidia on raw throughput. But it has made a credible case that by 2028, the AI hardware market will be meaningfully more plural than it is today.
