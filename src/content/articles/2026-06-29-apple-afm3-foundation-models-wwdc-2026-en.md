---
title: "Apple's AFM 3: A 20-Billion-Parameter AI Model Running Entirely on Your iPhone"
summary: "At WWDC 2026, Apple unveiled its third-generation Apple Foundation Models — a family of five AI models co-developed with Google, including AFM 3 Core Advanced, a 20-billion-parameter sparse multimodal model that runs on-device using flash memory. The new architecture powers a complete redesign of Siri and represents Apple's most ambitious on-device AI engineering effort to date."
category: "ai-ml"
publishedAt: 2026-06-29
lang: "en"
featured: false
trending: true
sources:
  - name: "Apple Machine Learning Research — Introducing AFM 3"
    url: "https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models"
  - name: "9to5Mac — Apple's Third-Generation Foundation Models Explained"
    url: "https://9to5mac.com/2026/06/11/apples-new-foundation-models-explained-on-device-ai-cloud-ai-and-everything-in-between/"
  - name: "GIGAZINE — Apple AFM 3 Core Advanced 20B Model on iPhone"
    url: "https://gigazine.net/gsc_news/en/20260610-apple-foundation-models"
  - name: "MacStories — Third Generation Apple Foundation Models"
    url: "https://www.macstories.net/linked/the-third-generation-of-apples-foundation-models-and-afm-core-advanced/"
  - name: "Let's Data Science — Apple Debuts Third-Generation Foundation Models"
    url: "https://letsdatascience.com/news/apple-debuts-third-generation-foundation-models-and-afm-core-advanced-d7aeb6dc"
tags:
  - "apple"
  - "foundation-models"
  - "on-device-ai"
  - "siri"
  - "wwdc2026"
  - "afm3"
  - "google"
  - "multimodal"
  - "sparse-models"
  - "private-cloud-compute"
relatedSlugs:
  - "2026-06-29-openai-jalapeno-broadcom-inference-chip-en"
  - "2026-06-27-google-gemini-25-deep-think-reasoning-en"
  - "2026-06-28-anthropic-ai-for-science-life-sciences-push-en"
---

Apple has never competed on raw model benchmarks. Its AI strategy has always been oriented around a different constraint: what can run, privately and reliably, on the device in your pocket? At WWDC 2026, the company answered that question with more ambition than ever before — a 20-billion-parameter AI model that runs entirely on an iPhone's flash memory, without sending a single byte to a remote server.

The third generation of Apple Foundation Models, announced on June 8, represents both an engineering feat and a statement of values. The result is a family of five AI models spanning from compact on-device models to powerful server-side architectures, collectively designed to power a complete reimagining of Siri and transform how Apple's apps understand and respond to users.

## The Model Family

AFM 3 comes in five variants, each occupying a specific position in Apple's privacy-first AI architecture.

**AFM 3 Core** is the entry-level on-device model, a 3-billion-parameter dense architecture — the same category as its predecessor — but delivering meaningfully improved output quality. In comparative testing, it achieved 45.6% preference over the 2026 baseline across text generation tasks, with 61% preference on image understanding. It handles the everyday, latency-sensitive tasks where waiting even a second for a cloud response would feel unacceptable.

**AFM 3 Core Advanced** is where Apple's engineering ambition becomes dramatic. At 20 billion parameters, it's roughly six times larger than AFM 3 Core. And yet it runs entirely on-device, without cloud connectivity, using a sparse activation architecture that Apple calls Instruction-Following Pruning (IFP). At any given moment, the model activates only 1 to 4 billion parameters — a fraction of its theoretical capacity — choosing which expert sub-networks to engage based on the nature of the current request.

The architectural trick that makes this possible: "the full model is stored in flash memory (NAND)" rather than active RAM. Flash memory is far slower than DRAM, but AFM 3 Core Advanced's sparse design means only a tiny slice of the model needs to be loaded into active memory at any given time. For complex reasoning tasks, more experts activate; for simple requests, the model runs lean. Apple calls this "inference-time elasticity."

The other three models run server-side on Apple's Private Cloud Compute infrastructure. **AFM 3 Cloud** handles speed-sensitive tasks; **AFM 3 Cloud (Image)** specializes in generation and editing; **AFM 3 Cloud Pro** — the most capable model in the family — is designed for complex agentic reasoning tasks that require more compute than any phone can supply.

## The Google and NVIDIA Collaboration

AFM 3 was developed in collaboration with Google, a partnership that extends deeper than infrastructure agreements. For AFM 3 Cloud Pro specifically, Apple extended its Private Cloud Compute architecture to run on NVIDIA GPUs hosted in Google Cloud — an unusual configuration that maintains Apple's privacy guarantees (no user data stored, no Apple visibility into queries) while accessing the kind of compute power required for frontier-class reasoning.

The collaboration represents a pragmatic recalibration for a company that has historically insisted on controlling its own hardware. Even Apple's world-class silicon cannot match the raw compute of a Google Cloud cluster running hundreds of Blackwell GPUs. For the most demanding AI tasks — the long-horizon agent workflows that define where AI utility is heading — Apple chose to extend its architecture rather than constrain its models.

## What This Means for Siri

Apple framed AFM 3 as the engine for "an entirely new Siri" — a promise the company has made in various forms since 2022, but that now appears to rest on substantially more capable foundations.

The key changes are in reasoning depth and multimodal understanding. AFM 3 Core Advanced can handle complex, multi-turn requests that require the model to hold context, make inferences across modalities (text, images, audio), and produce outputs that feel genuinely responsive rather than scripted. The 4.15 Mean Opinion Score for text-to-speech quality — compared to a 3.87 baseline — suggests that Siri's voice will also sound meaningfully more natural.

The audio and dictation improvements matter particularly for accessibility users and for the growing share of people who interact with their phones primarily through voice. At 44.7% preference for dictation quality versus the baseline, AFM 3 Core Advanced's voice understanding represents a substantial step toward a Siri that can actually replace typing in complex scenarios.

## Privacy as Architecture, Not Policy

One of the most distinctive aspects of Apple's AFM 3 announcement was how consistently privacy was treated as an engineering constraint rather than a feature to be advertised. The architecture — sparse models that activate only what's needed, flash-based storage, Private Cloud Compute with verifiable privacy properties — is designed so that privacy guarantees emerge from the system's structure, not from policy promises.

Apple explicitly noted that neither user data nor user interactions were used in training any of the AFM 3 models. Training data drew from public information and licensed third-party datasets. The cloud components run on infrastructure where Apple has cryptographic evidence that user data cannot be logged or stored, and where independent security researchers can verify those properties by inspecting the software running in the secure enclave.

This architecture stands in contrast to most other frontier AI systems, where privacy often amounts to a terms-of-service commitment rather than a technical guarantee.

## The Race to On-Device Intelligence

Apple's AFM 3 launch comes as the industry broadly wrestles with the costs and latency of cloud-dependent AI. Every request that goes to a remote server adds latency, burns API credits, and raises privacy questions. The economic pressure to push more AI computation to edge devices is enormous — and AFM 3 Core Advanced demonstrates that the capability frontier for on-device AI is moving faster than most observers expected.

Running 20 billion parameters — even sparsely — on a phone was considered a credible challenge for 2027 or 2028. Apple's flash-based IFP architecture did it in 2026. That matters not just for iPhone users but for the entire industry's sense of what edge inference can deliver.

With Apple Silicon's memory bandwidth advantages and a software stack built from the ground up for this model family, AFM 3 Core Advanced establishes a new benchmark for what sovereign, private, on-device AI looks like. The question now is how long it takes for the rest of the industry to match it — and whether Apple will have moved the target again by then.

---

*AFM 3 is available across iPhone, iPad, and Mac devices with Apple Silicon, with capabilities rolling out through iOS 20, iPadOS 20, and macOS Tahoe through the latter half of 2026.*
