---
title: "Google Unveils Ironwood TPU and Splits Its Eighth-Gen Chip Roadmap Into Training and Inference"
summary: "Google made its seventh-generation Ironwood TPU generally available at Cloud Next 2026, with 4.6 petaFLOPS per chip and 42.5 exaFLOPS in a 9,216-chip superpod, and previewed an eighth-generation split architecture: a Broadcom-designed training chip and a MediaTek-designed inference chip, both targeting TSMC's 2nm process."
category: "hardware"
publishedAt: 2026-04-23
modifiedAt: 2026-11-15T00:00:00Z
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

Google used its biggest annual customer conference to fire its most direct salvo yet against Nvidia's dominance of the AI chip market. At Google Cloud Next 2026 in Las Vegas, the company made its seventh-generation Tensor Processing Unit — Ironwood — generally available, while simultaneously previewing a split eighth-generation architecture that divides AI workloads between dedicated training and inference silicon. The announcements signal a company that is no longer content to play a supporting role in AI infrastructure.

## Ironwood: Designed for Inference at Scale

The name carries intent. Google describes Ironwood as "the first Google TPU for the age of inference," reflecting a fundamental shift in where AI compute is actually being consumed. In the early deep learning era, training dominated GPU demand. Now, with frontier models largely trained and deployed to hundreds of millions of users, serving predictions in real time — inference — is consuming a rapidly growing share of every data center's compute budget.

Each Ironwood chip delivers 4.6 petaFLOPS of compute and 192 gigabytes of high-bandwidth memory. At pod scale, a 9,216-chip Ironwood superpod delivers 42.5 exaFLOPS of aggregate performance. Google claims a 10× peak performance improvement over the TPU v5p and more than 4× better performance per chip compared to the v6e Trillium, the prior generation. Both training and inference workloads benefit from the improvement, and Google describes Ironwood as the first TPU designed specifically for inference.

In those workloads, memory bandwidth often becomes the bottleneck before raw compute does. Google's materials describe Ironwood superpods linked by Inter-Chip Interconnect networking that gives chips access to a shared pool of 1.77 petabytes of high-bandwidth memory.

Ironwood is now generally available to Google Cloud customers.

## The Eighth Generation: Splitting the Stack

More strategically striking than Ironwood's launch was the roadmap Google laid out for its eighth-generation chips, which will be the first time the company has deliberately designed separate chips for training and inference rather than a single general-purpose processor.

TPU 8t, codenamed "Sunfish," is co-designed with Broadcom and targets training workloads. It will scale to 9,600 chips in a single superpod, backed by two petabytes of shared high-bandwidth memory, and is designed to deliver up to 2.8x better training price-performance than Ironwood. Both Sunfish and its inference counterpart are slated to be built on TSMC's 2nm process and are targeted for late 2027.

TPU 8i, codenamed "Zebrafish," is co-designed with MediaTek — an unusual partnership that illustrates how broadly Google is distributing its silicon design work — and targets inference exclusively. Zebrafish uses a new "Boardfly" topology to directly connect 1,152 chips in a single pod, carries 3× more on-chip SRAM than previous generations to keep KV caches entirely on silicon rather than in slower off-chip memory, and integrates a specialized Collectives Acceleration Engine. Google projects 80% better performance per dollar for inference versus the prior generation.

The decision to bifurcate the eighth generation is a philosophical break from the general-purpose GPU paradigm that Nvidia has built its business, now valued at nearly $5 trillion, around. It is a bet that by 2027, training and inference will be sufficiently different in their memory access patterns, parallelism requirements, and power profiles that optimizing a single chip for both is an unacceptable engineering compromise.

## The Agent Stack: $750 Million and the A2A Protocol

Cloud Next 2026 was not purely a silicon story.

## Competitive Context

The timing is deliberate. But the competitive environment has shifted.

Anthropic's arrangement with Google is expanding to 3.5 gigawatts of compute capacity in 2027, making it the anchor customer for both Ironwood and the eighth-generation platform. That scale of commitment gives Anthropic a credible alternative supply chain as its run-rate revenue has surpassed $30 billion.

For Nvidia, the most significant development at Cloud Next 2026 is not any single chip specification but the emerging reality that the largest frontier AI labs are no longer treating GPU access as their only strategic infrastructure option. Google has not yet out-engineered Nvidia on raw throughput. But it has made a credible case that by 2028, the AI hardware market will be meaningfully more plural than it is today.

*Correction (November 15, 2026): 25 sentences were corrected or removed to match the sources listed on this page.*
