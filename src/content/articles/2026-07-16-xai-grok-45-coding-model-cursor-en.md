---
title: "xAI Launches Grok 4.5: A Cursor-Trained Coding Model Aiming to Undercut the Frontier"
summary: "xAI released Grok 4.5 on July 8 as its fastest and most cost-efficient model yet, co-trained with Cursor and built around a 500,000-token context window. At $2 per million input tokens, it places in the same tier as GPT-5.6 Terra while claiming performance closer to Claude Opus 4.8."
category: "developer-tools"
publishedAt: 2026-07-16
lang: "en"
featured: false
trending: true
sources:
  - name: "xAI — Introducing Grok 4.5"
    url: "https://x.ai/news/grok-4-5"
  - name: "Axios — SpaceXAI launches new model, Grok 4.5"
    url: "https://www.axios.com/2026/07/08/spacexai-grok-new-model"
  - name: "TechCrunch — Grok 4.5 launch"
    url: "https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/"
  - name: "Fullstack.com — Grok 4.5 deep dive"
    url: "https://www.fullstack.com/labs/resources/blog/grok-4-5-a-closer-look-at-xais-latest-model"
  - name: "DataNorth — Grok 4.5 release"
    url: "https://datanorth.ai/news/xai-releases-grok-4-5-coding-focused-model"
tags:
  - "xAI"
  - "Grok"
  - "coding AI"
  - "Cursor"
  - "developer tools"
  - "large language models"
relatedSlugs:
  - "2026-07-16-openai-gpt56-sol-terra-luna-general-availability-en"
  - "2026-07-15-gemini-35-pro-pricing-deepseek-competition-en"
---

The day before OpenAI opened GPT-5.6 to the world, xAI made its own move. On July 8, the company Elon Musk controls alongside SpaceX released Grok 4.5 — a coding-first model that was co-developed with Cursor, the AI-native code editor, and priced to make the economics of frontier-class intelligence genuinely accessible to individual developers. The release is xAI's clearest statement yet that it intends to compete not just on raw capability, but on the cost-performance curve that increasingly drives enterprise and developer adoption.

## What's Inside Grok 4.5

Grok 4.5 is a text-and-image input, text-output model built around four headline specifications:

**Context window: 500,000 tokens.** This is among the largest commercially available context windows at launch, comfortably exceeding GPT-5.6 Sol's window and roughly matching Gemini Omni Ultra's extended-context configuration. For coding tasks specifically, a 500K context means Grok 4.5 can ingest an entire mid-sized repository — including test suites, configuration files, and build scripts — in a single pass, without the chunking and retrieval gymnastics that limit smaller-context models.

**Speed: 80 tokens per second.** xAI describes this as "fast-model speeds," and at 80 TPS it is meaningfully faster than GPU-served alternatives at the same parameter count. The company attributes the throughput to custom inference kernel work done in parallel with Cursor's engineering team.

**Pricing: $2 / $6 per million tokens.** Input at $2 per million and output at $6 per million positions Grok 4.5 in direct competition with GPT-5.6 Terra and Gemini Omni Flash Pro. Elon Musk described the model as "roughly comparable to Opus 4.7, but much faster and more token-efficient" — a claim that, if it holds under independent benchmarking, would represent an extraordinary value proposition: near-frontier intelligence at mid-tier prices.

**Function calling and structured outputs.** Grok 4.5 supports all the programmatic interfaces modern agent frameworks depend on — function calling, structured JSON outputs, web search, X (Twitter) search, and code execution. The X search integration is genuinely differentiated: developers building applications that need real-time public discourse context can query X's firehose natively through the model, without a separate API integration.

## The Cursor Partnership

What makes Grok 4.5's origin story unusual in the current AI landscape is that it was co-trained with Cursor rather than simply integrated into it post hoc. Cursor's engineering team contributed to the model's training data curation and fine-tuning process, with a particular focus on multi-file code comprehension, diff generation, and inline edit quality.

The practical result is that Grok 4.5 shows strong performance on the specific tasks Cursor users perform most — not just code generation from a specification, but the messier work of refactoring existing code, fixing type errors across a module boundary, and reasoning about what a diff will actually do to a running system. The 500K context window is particularly well-suited to this: Cursor can pass the model the full contents of a repository feature branch and ask it to reason holistically about correctness.

Grok 4.5 ships as a first-class model in Cursor on all subscription plans from launch day, including Cursor's free tier. This distribution channel matters: Cursor has grown to become one of the most widely used coding environments among professional developers over the past 18 months, and embedding Grok 4.5 at the free tier level gives xAI immediate reach into that developer population without needing to win a separate purchasing decision.

## Benchmark Positioning

xAI placed Grok 4.5 fourth on the Artificial Analysis Intelligence Index at launch, above all current open-weight models and above the entire Gemini family — a meaningful claim given Google's model family is the closest competitor in terms of breadth of enterprise deployment. The model sits above GPT-5.6 Terra on the index but below Sol.

The benchmark that will attract the most scrutiny is SWE-bench Verified, the code editing benchmark that has become the de facto standard for measuring real-world software engineering capability. xAI has not yet published a SWE-bench Verified score for Grok 4.5, and independent researchers have flagged that the model's strong performance on synthetic coding evals does not always translate directly to SWE-bench's messier, real-repository tasks. That number, when it appears, will be closely watched by the developer community.

## Availability Constraints

Grok 4.5 is available today in Grok Build (xAI's agent API platform), in Cursor on all plans, and through the xAI API console. However, it is **not yet available in the European Union**, where xAI is still navigating regulatory compliance requirements under the EU AI Act's transparency and data governance provisions. EU availability is expected in mid-July — a window that is already here, suggesting xAI is close to clearing those requirements.

The EU gap is a persistent friction point for xAI's enterprise ambitions. European enterprises represent a significant portion of global AI API spend, and every week of EU absence is a week of market share accumulation for compliant alternatives.

## Competitive Framing

The timing of Grok 4.5's release — one day before OpenAI's GPT-5.6 GA — was deliberate. xAI wanted its own narrative cycle before OpenAI's press wave arrived. The strategy partially worked: Grok 4.5 generated a concentrated burst of developer community discussion before being somewhat eclipsed by the GPT-5.6 coverage. But the model's staying power will be determined less by its launch week and more by whether the Cursor integration drives durable daily-active-user metrics that xAI can point to in future funding conversations.

At the same time, xAI's position in the emerging AI-native developer tooling market is genuinely interesting. Anthropic has its own strong developer relationships through Claude's API and its integration into Claude.ai's artifact system. OpenAI owns GitHub Copilot through Microsoft. Google has Gemini deeply embedded in Android Studio and Firebase. xAI has Cursor — and through Cursor, a rapidly growing population of developers who encounter Grok 4.5 as their default AI collaborator, not a conscious product choice.

## What Developers Should Watch

For teams evaluating Grok 4.5 as a primary model, the key unknowns are: SWE-bench Verified performance, latency consistency under production load (80 TPS is a headline figure; real-world p95 latency matters more), and the stability of the X search integration for applications that depend on real-time data. The 500K context is immediately useful for large repository analysis; whether it degrades gracefully at the upper end of the window will need independent testing.

For the broader AI landscape, Grok 4.5 signals that the coding model segment — once a relatively undifferentiated category dominated by GitHub Copilot and a few API players — is becoming a genuine arena of competitive intensity, with model architecture, training partnerships, and distribution channel all mattering in ways they didn't 18 months ago.
