---
title: "PrismML Releases Bonsai 27B, a 27-Billion-Parameter AI Model Built to Run on an iPhone"
summary: "PrismML, a company founded by Caltech researchers and backed by Khosla Ventures, Cerberus, and Google, has released Bonsai 27B, a 27-billion-parameter model whose smaller variant is about 3.9GB and, per PrismML's white paper, generates about 11 tokens per second on an iPhone 17 Pro Max. The weights are available under Apache 2.0, and that variant keeps about 90% of the original model's performance in PrismML's own evaluation."
category: "developer-tools"
publishedAt: 2026-07-17
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "9to5Mac"
    url: "https://9to5mac.com/2026/07/14/prismml-releases-bonsai-27b-claiming-first-major-ai-model-of-its-size-fit-for-iphone/"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/07/14/prismml-releases-bonsai-27b-1-bit-and-ternary-builds-of-qwen3-6-27b-that-run-on-laptops-and-phones/"
  - name: "The Decoder"
    url: "https://the-decoder.com/bonsai-27b-is-a-full-open-reasoning-model-that-fits-on-an-iphone/"
  - name: "CryptoBriefing"
    url: "https://cryptobriefing.com/bonsai-27b-ai-model-mobile-devices/"
tags:
  - "on-device-ai"
  - "prismml"
  - "bonsai-27b"
  - "mobile-ai"
  - "open-source"
  - "quantization"
  - "iphone"
relatedSlugs:
  - "2026-07-17-moonshot-kimi-k3-open-weight-model-en"
---

The story of AI moving from the cloud to the edge has been building for years. PrismML, a company founded by Caltech researchers, has released Bonsai 27B, a 27-billion-parameter model whose smaller variant takes up about 3.9 gigabytes and, according to PrismML's white paper, generates about 11 tokens per second on an iPhone 17 Pro Max.

The model, based on Alibaba's Qwen3.6 27B foundation but rebuilt from the ground up using extreme quantization techniques, is available immediately under the Apache 2.0 license. The model weights are available under the Apache 2.0 license, and PrismML also offers a free, limited-time developer preview API. A developer can pull Bonsai 27B today, run it entirely on a consumer device, and ship an application that processes text, images, and documents without a single API call to a cloud server.

That's a genuinely different world from where on-device AI was even twelve months ago.

## How You Fit 27 Billion Parameters Into a Phone

The technical challenge is stark. A model of this size typically takes up about 54 gigabytes of storage, while a 12 GB iPhone makes only about 6 GB available to a single app. Getting to 3.9 gigabytes requires a compression ratio of approximately 14:1 without catastrophic performance loss. That's the problem PrismML spent the past year solving.

The company's approach uses two quantization variants shipped simultaneously. The **1-bit variant**, in which each weight has only two states, is the smaller one at about 3.9 GB and is the version meant for the iPhone. The **ternary variant** uses three states per weight, is the larger, quality-focused version at about 5.9 GB, and is meant for laptops.

Both variants build on research from the 1.58-bit BitNet paper tradition, but PrismML's implementation introduces several proprietary optimizations for inference on ARM and Apple Silicon architectures that the company says account for most of the practical speedup. In PrismML's own evaluation across 15 benchmarks, the smaller variant keeps about 90% of the original model's performance, and PrismML says math and coding stayed "virtually unaffected."

The vision tower — which enables the model to process images, screenshots, and camera input — ships in compact 4-bit form rather than being dropped entirely, preserving multimodal capability within the phone's memory budget.

## Speculative Decoding Compounds the Advantage

Bonsai 27B ships with a built-in speculative decoding implementation, a technique where a smaller "draft" model rapidly proposes likely next tokens, which the main model then verifies in parallel. On compatible hardware, this compounds the 11-tokens-per-second baseline throughput with additional speedup in practice — the company says 15-17 tokens per second is achievable on continuous prose generation workloads on the latest iPhone hardware.

The 262,000-token context window is another headline figure. For a model running locally on a phone, 262K tokens means the ability to process a 200-page PDF, a full codebase, or an extended multi-turn conversation without chunking or retrieval workarounds. Prior on-device models in the sub-10B parameter range typically maxed out at 8,000-32,000 tokens. Bonsai 27B's context window is a step-function improvement that changes what kinds of applications are practical to build locally.

## Who Built This and Who's Backing It

PrismML is a company founded by a team of Caltech researchers. The company was founded with backing from Khosla Ventures, Cerberus, and Google, and Samsung continues to support it.

Samsung's involvement is particularly notable. The company ships hundreds of millions of Android devices annually and has been building out its own on-device AI platform (Galaxy AI) for the past two years. Bonsai 27B offers Samsung a 27B-class model that could run on Galaxy hardware without Samsung paying per-inference cloud fees — a strong incentive for the Samsung venture arm to support its development.

Google's involvement is more ambiguous. On one hand, on-device inference at scale reduces the number of queries that hit Google Cloud and Vertex AI. On the other, Google has been investing heavily in its own on-device model series (Gemma Nano) and likely views PrismML as a potential acqui-hire target or a useful benchmark for its own compression research.

## The Developer Opportunity

From a developer perspective, Bonsai 27B opens a set of application categories that have been practically inaccessible until now.

**Privacy-first applications**: Document processing, note-taking, journaling, and health-monitoring apps where users don't want their data leaving the device. A 27B-class model running locally can process and reason over personal data with capability that was previously only available through cloud APIs.

**Offline-first enterprise tools**: Field workers, medical professionals, and military applications where reliable internet connectivity cannot be assumed. The ability to run a frontier-tier model from a phone's internal storage, with no network dependency, changes the architecture of a large category of enterprise software.

**Low-latency consumer experiences**: Cloud round-trip times, even on fast networks, introduce hundreds of milliseconds of latency. On-device inference eliminates that entirely. For real-time applications — live translation, accessibility tools, coding assistants — this is a qualitative difference in user experience.

**Emerging market accessibility**: In regions where cloud inference costs are prohibitive or internet infrastructure is unreliable, a powerful model that runs entirely offline changes who can access capable AI tooling.

## The "DeepSeek Moment" Framing

Several outlets covering the Bonsai 27B release used the phrase "DeepSeek moment" — invoking the January 2026 release of DeepSeek R1 that demonstrated frontier-tier reasoning at dramatically lower cost than assumed possible, sending a shockwave through the AI infrastructure investment thesis. The comparison captures something real: both events involve a dramatically cheaper path to a capability that had been assumed to require expensive resources.

The parallel isn't perfect — DeepSeek R1's cost efficiency was achieved at training time, while Bonsai 27B's efficiency is at inference time on specific hardware. But the underlying point holds: the assumption that 27B-parameter-class intelligence requires cloud infrastructure has just been falsified, with open weights and an Apache license attached.

For AI developers, that's worth sitting with. The architecture of a significant portion of the AI application stack was designed around the assumption that models of this size live in the cloud. Bonsai 27B — and the category of models it represents — suggests that assumption needs revisiting.

The weights are available now at the PrismML GitHub repository. According to PrismML, a 12 GB iPhone makes only about 6 GB available to a single app, split between the model and the cache. iPhone 17 Pro, iPhone 17 Pro Max, and recent iPad Pro models all qualify.

*Correction (November 15, 2026): 11 sentences were corrected or removed to match the sources listed on this page.*
