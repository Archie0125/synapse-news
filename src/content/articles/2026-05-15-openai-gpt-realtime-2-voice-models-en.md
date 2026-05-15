---
title: "OpenAI Launches GPT-Realtime-2: Voice AI That Can Actually Think"
summary: "OpenAI has released three new real-time audio models through its API — GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper — bringing GPT-5-class reasoning to live voice interactions and targeting a rapid displacement of traditional call center and transcription infrastructure."
category: "products"
publishedAt: 2026-05-15
lang: "en"
featured: false
trending: true
sources:
  - name: "OpenAI"
    url: "https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/07/openai-launches-new-voice-intelligence-features-in-its-api/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/openai-gpt-realtime-2-voice-models"
  - name: "Dataconomy"
    url: "https://dataconomy.com/2026/05/08/gpt-realtime-2-expands-openais-voice-intelligence-capabilities/"
tags:
  - "OpenAI"
  - "voice-AI"
  - "API"
  - "real-time-audio"
  - "GPT-Realtime-2"
relatedSlugs:
  - "2026-05-13-elevenlabs-500m-series-d-voice-ai-en"
  - "2026-05-14-openai-daybreak-cybersecurity-gpt55-en"
---

The problem with voice AI has never been the voice. It has been the thinking behind the voice — the long pause before an answer, the failure to track context across a long call, the inability to recover gracefully when the user interrupts or changes course. OpenAI's latest release takes direct aim at that gap.

On May 7, 2026, OpenAI released three new models through its Realtime API: GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper. Together, they represent the most significant upgrade to voice AI infrastructure since OpenAI first launched the Realtime API in late 2024 — and the first time that GPT-5-class reasoning has been coupled with a low-latency voice interface.

## GPT-Realtime-2: When Voice Gets a Brain

The flagship model in the release is GPT-Realtime-2, which OpenAI describes as its "most advanced voice reasoning model." The headline capability is the integration of GPT-5-class reasoning directly into a model optimized for live voice interactions. Previous voice models ran reasoning and audio on separate pipelines, introducing latency and context degradation at the seam. GPT-Realtime-2 handles both natively.

The context window has expanded dramatically — from 32,000 tokens in the previous generation to 128,000 tokens, allowing voice agents to maintain much longer conversational histories without losing earlier context. In a customer service deployment, that means an agent can reference information shared 45 minutes earlier in the same call without being explicitly reminded.

Benchmarks show the model scoring 96.6% on Big Bench Audio Intelligence, a composite evaluation of comprehension, reasoning, and coherence across spoken interactions. That is 15.2% higher than its predecessor, GPT-Realtime-1.5, on the same benchmark.

The model is also built to handle real-world conversational friction. It can process simultaneous speech from multiple speakers, manage interruptions without losing its place, and gracefully incorporate corrections in mid-sentence. These are the exact failure modes that have made the current generation of AI phone agents feel robotic — the tendency to restart rather than adapt.

Pricing is set at $32 per million audio input tokens and $64 per million audio output tokens, with a significantly discounted rate of $0.40 per million for cached input tokens. For context, a typical 10-minute customer support call generates roughly 15,000–20,000 tokens. At that usage level, the per-call cost is well under $0.01 for audio input — substantially cheaper than maintaining human agents for routine queries.

## GPT-Realtime-Translate: 70 Languages, Live

The second model, GPT-Realtime-Translate, addresses the real-time multilingual translation market that companies like Interpreter.ai and KUDO have been building toward for the past several years.

The model accepts audio input in more than 70 languages and translates it into 13 output languages while keeping pace with a live speaker — a capability that previous systems could only approximate with noticeable lag. The key technical challenge is that human speech arrives with natural pauses, fillers, and sentence fragments; a model that waits for a complete sentence before translating introduces perceptible delay, while one that translates incrementally risks generating incorrect output when the speaker changes direction mid-thought.

OpenAI's approach uses a streaming architecture that generates provisional translations and updates them in real time as more context arrives, rather than waiting for sentence boundaries or speaking in discrete chunks. The result, based on demos shared with developers in early access, is near-simultaneous translation that sounds more natural than the two-beat rhythm of traditional interpretation systems.

Pricing is $0.034 per minute — significantly cheaper than live human interpretation services, which typically cost $2–$4 per minute for professional interpreters.

## GPT-Realtime-Whisper: Faster Than You Can Type

The third model, GPT-Realtime-Whisper, is positioned as a live transcription and captioning engine for meetings, legal proceedings, media production, and accessibility applications.

The company claims the model transcribes faster than most humans can type, maintaining low word error rates even in noisy environments or with speakers who have strong accents or non-standard prosody. Unlike batch transcription APIs that process audio files after the fact, GPT-Realtime-Whisper is designed for streaming, with sub-300ms latency from speech to displayed text.

For accessibility use cases — automatic captions for the deaf and hard-of-hearing — this latency difference is significant. A 300ms delay reads as nearly synchronous to human perception; the 1.5–3 second delays common in older real-time captioning systems are noticeably disjointed from the speaker.

## The Market Opportunity

The release is explicitly aimed at the call center and contact center market, which OpenAI estimates runs over 15 million agent seats globally. The combination of GPT-5-class reasoning and low-latency audio means that for the first time, AI voice agents can handle genuinely complex queries — not just routing callers or answering FAQs, but explaining a disputed insurance claim, walking a customer through a technical troubleshooting sequence, or negotiating a payment plan.

ElevenLabs, which raised $500 million at a $5 billion valuation in May, is likely to feel the most direct competitive pressure. Its voice synthesis technology is best-in-class, but GPT-Realtime-2's reasoning capability combined with OpenAI's model distribution gives developers a strong reason to consolidate on a single API rather than stitching together OpenAI reasoning with ElevenLabs speech.

Smaller players in the live translation market — Interprefy, Kudo, Wordly — face a similar dynamic. Their per-minute rates cannot match GPT-Realtime-Translate at $0.034/min without equivalent accuracy, and their enterprise contracts are now under renewal pressure.

## What Comes Next

OpenAI confirmed at launch that GPT-Realtime-2 is already being used by GPT-5.5 to handle voice-mode interactions in ChatGPT, replacing the previous voice pipeline. The company has also said that workspace agents — its enterprise automation product — will be able to receive voice instructions via GPT-Realtime-2, making it possible to trigger multi-step automated workflows entirely through spoken commands.

That means the vision is not just a smarter phone agent. It is a voice interface for the agentic AI era: one where speaking to your AI assistant is not merely a convenience, but the primary way humans direct complex, multi-step automated work.
