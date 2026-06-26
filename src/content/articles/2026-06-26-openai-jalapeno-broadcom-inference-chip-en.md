---
title: "OpenAI and Broadcom Unveil Jalapeño: ChatGPT's Maker Enters the Silicon Race"
summary: "OpenAI revealed its first custom AI inference chip, co-developed with Broadcom, called Jalapeño. Built from concept to tape-out in just nine months—a record for high-performance ASICs—the chip targets the inference workloads that power ChatGPT and OpenAI's enterprise products, promising significantly better performance-per-watt than current NVIDIA alternatives."
category: "hardware"
publishedAt: 2026-06-26
lang: "en"
featured: true
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/"
  - name: "OpenAI Blog"
    url: "https://openai.com/index/openai-broadcom-jalapeno-inference-chip/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models/"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle"
tags:
  - "openai"
  - "broadcom"
  - "ai chips"
  - "hardware"
  - "inference"
  - "silicon"
relatedSlugs:
  - "2026-06-25-nvidia-vera-rubin-nvl72-78m-rack-memory-cost-en"
---

For years, the AI industry ran on a single silicon dependency: NVIDIA. Training GPT-4, Gemini, Claude — all of it consumed H100s and A100s by the tens of thousands. But on June 24, 2026, OpenAI announced a step toward breaking that dependency, at least for one critical part of the stack.

The company unveiled **Jalapeño**, its first custom AI inference chip, co-developed with Broadcom. The announcement marks a pivotal moment in AI's infrastructure evolution — not because OpenAI is replacing NVIDIA for training, but because it's now building dedicated silicon for the other half of the equation: *serving* its models to hundreds of millions of users.

## What Is Jalapeño?

Jalapeño is what the chip industry calls an ASIC — Application-Specific Integrated Circuit — built from the ground up for one purpose: running OpenAI's large language model inference workloads. Unlike a GPU, which is a general-purpose parallel processor, Jalapeño is hardwired for the specific mathematical operations that make LLMs respond to user queries.

It's a reticle-sized chip, meaning it occupies the maximum area possible on the silicon wafer given the lithography constraints of the fabrication process — a design choice that maximizes compute density. Early testing shows it delivers "performance per watt substantially better than current state-of-the-art," according to OpenAI, though the company has not yet published full benchmark numbers.

"We have a deep understanding of the workload," said Greg Brockman, OpenAI's President, in a statement accompanying the launch. "We've really been looking for specific workloads that are underserved, [and asking] how can we build something that will be able to accelerate what's possible?"

## A Nine-Month ASIC: AI Designing AI Silicon

What makes Jalapeño as technically impressive as the chip itself is how fast it was built. The partnership between OpenAI and Broadcom was announced in October 2025. From that initial design kick-off to manufacturing tape-out — the final step before a chip goes into production — took just **nine months**.

That's remarkable. Typical ASIC development cycles for high-performance, production-ready silicon run 18 to 24 months. Cutting that timeline in half required two things: Broadcom's deep expertise in custom silicon implementation, and something genuinely novel — OpenAI's own models were used to accelerate parts of the chip's design and optimization process.

It's a recursive achievement: AI helping design the chips that will run AI. Engineers used OpenAI models to explore design spaces, verify timing constraints, and optimize circuit layouts that would have taken human teams months longer to complete manually.

## Inference vs. Training: Why This Matters

The distinction between training and inference chips is crucial to understanding why Jalapeño matters.

Training is where raw computational brute force wins. You're running gradient descent across trillions of parameters with massive memory bandwidth requirements. NVIDIA's H100 and H200 GPUs, with their enormous HBM3 memory and NVLink interconnects, remain unmatched for this workload. OpenAI will continue using NVIDIA hardware for training its frontier models.

Inference is a different beast. When you type a message into ChatGPT, a model runs forward pass computations in milliseconds, generating one token at a time until the response completes. This workload is high-frequency, latency-sensitive, and runs at scale across millions of simultaneous users. The cost profile is also different: inference is where OpenAI spends the bulk of its compute dollars *per day*.

Custom inference silicon — like Google's TPU v5, Amazon's Inferentia, and Microsoft's Maia — can be optimized specifically for the batch sizes, precision formats (INT8, FP8, FP4), and memory access patterns that production LLM serving actually uses. GPUs are flexible but inefficient for these workloads because they carry hardware optimized for use cases OpenAI simply doesn't need.

By deploying Jalapeño, OpenAI can dramatically reduce its per-token inference cost, improve latency, and — critically — reduce its operational exposure to NVIDIA's pricing and supply constraints.

## Strategic Context: The Silicon Sovereignty Race

OpenAI isn't alone in this move. Every major AI hyperscaler has realized the same thing: if you're spending billions on compute, you want to own the silicon.

Google has been deploying TPUs since 2016. Amazon's Trainium 2 handles training for its own models and powers Bedrock. Microsoft Maia 100 runs Copilot inference internally. Meta's MTIA chip handles recommendation system inference at massive scale.

What's notable is how *late* OpenAI arrived to this game relative to the models it built. The company has been spending billions per year on NVIDIA GPU rentals to serve ChatGPT — a dependency that has made it simultaneously the world's most important NVIDIA customer and one of its most vulnerable to pricing leverage.

Broadcom was the right partner to compress the development timeline. The company is the world's top custom ASIC designer, with deep relationships with hyperscalers including Google (whose TPUs Broadcom helped design) and Meta. For Broadcom, the OpenAI deal validates and extends its AI custom silicon business, which it projected to generate $12 billion in revenue in 2026 alone.

The fact that OpenAI used its own models to speed up chip design also opens a compelling product flywheel: better models help design better chips, which enable faster and cheaper inference, which generates more revenue to train even better models.

## The Jalapeño Architecture

While OpenAI hasn't disclosed full technical specifications — common for pre-deployment ASIC announcements — several details have emerged. Jalapeño is described as a "reticle-sized" design, placing it in the same size category as NVIDIA's H100 die, which means it's pushing the physical limits of what a single piece of silicon can contain given current lithography constraints.

The chip is optimized for inference rather than training, which implies a different memory architecture than training-oriented GPUs. Training chips need enormous high-bandwidth memory for storing intermediate gradients and activations. Inference chips prioritize low-latency memory access for KV-cache lookups (the cached attention states that enable efficient multi-turn conversations) and high-throughput tensor math for forward passes.

The "performance per watt substantially better than state-of-the-art" claim is significant: in a data center running millions of ChatGPT queries per day, watt-efficiency translates directly into operational costs. A 30% efficiency improvement over NVIDIA H-series hardware at OpenAI's inference scale would save hundreds of millions of dollars annually.

## What Comes Next

Jalapeño is expected to begin initial deployment at OpenAI data centers by end of 2026, "expanding in the years ahead." That's a careful hedge — initial deployments of new ASICs almost always encounter integration challenges, and OpenAI is clearly leaving itself room to absorb early-iteration lessons before full-scale rollout.

The implications extend beyond cost savings. Custom silicon gives OpenAI the ability to co-optimize models and hardware together — a capability previously available only to Google. Future OpenAI models may be designed with Jalapeño's specific memory hierarchy, precision support, and interconnect characteristics in mind, creating performance advantages that pure software optimization can't replicate.

Nvidia's stock dipped 3.2% on the announcement day before recovering — a market signal that Wall Street understands the long-term implication. The inference market is vast and growing. Every billion queries per day that OpenAI routes through Jalapeño instead of NVIDIA GPUs is a direct hit to NVIDIA's service revenue.

The AI infrastructure race is no longer just about model size. It's about who controls the silicon underneath.
