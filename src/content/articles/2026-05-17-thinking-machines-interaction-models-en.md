---
title: "Mira Murati's Thinking Machines Lab Unveils Interaction Models: Full-Duplex AI at 0.4 Seconds"
summary: "Thinking Machines Lab, the startup founded by former OpenAI CTO Mira Murati, has previewed its debut product: Interaction Models, a native multimodal AI architecture built from scratch for real-time human conversation. The flagship TML-Interaction-Small model responds in 0.4 seconds — matching natural conversational speed — and runs as a 276B-parameter Mixture-of-Experts system with only 12B parameters active at inference."
category: "ai-ml"
publishedAt: 2026-05-17
lang: "en"
featured: false
trending: true
sources:
  - name: "Semafor — Mira Murati's Thinking Machines previews interaction models"
    url: "https://www.semafor.com/article/05/13/2026/mira-muratis-thinking-machines-previews-interaction-models"
  - name: "The AI Insider — Thinking Machines Lab Unveils Full-Duplex AI"
    url: "https://theaiinsider.tech/2026/05/12/mira-muratis-thinking-machines-lab-unveils-full-duplex-ai-that-responds-in-0-4-seconds/"
  - name: "MarkTechPost — Thinking Machines introduces Interaction Models"
    url: "https://www.marktechpost.com/2026/05/13/mira-muratis-thinking-machines-lab-introduces-interaction-models-a-native-multimodal-architecture-for-real-time-human-ai-collaboration/"
  - name: "CNBC — Mira Murati 2026 Changemaker"
    url: "https://www.cnbc.com/mira-murati-2026-changemaker/"
  - name: "TechFunding News — Thinking Machines Lab $2B seed round"
    url: "https://techfundingnews.com/thinking-machines-lab-ai-seed-round-record/"
tags:
  - "Mira Murati"
  - "Thinking Machines Lab"
  - "multimodal AI"
  - "voice AI"
  - "AI models"
  - "real-time AI"
  - "startups"
relatedSlugs:
  - "2026-04-23-thinking-machines-lab-google-cloud-deal-en"
---

Mira Murati spent seven years at OpenAI helping build the technology that reshaped the industry. Since leaving as CTO in late 2024, she has been unusually quiet for someone who raised a record $2 billion seed round before writing a single line of product code. On May 11, the silence broke. Thinking Machines Lab previewed its first product: Interaction Models, an approach to AI that Murati argues is not an iteration on existing voice-mode technology but a ground-up rethink of what it means for a machine to converse.

## The Latency Problem, Solved by Architecture

Every AI lab with a consumer voice product has been wrestling with the same problem: natural human conversation operates at roughly 200 to 400 milliseconds of response latency. Current best-in-class systems — including GPT-4o's voice mode and Google Gemini Live — hover around 400 to 700 milliseconds on a good day, and significantly higher during peak load. The perceptible gap is small, but it is enough to make conversations feel slightly off, like talking to someone on a bad satellite call.

TML-Interaction-Small, the model at the center of Thinking Machines' preview, claims a response latency of 0.40 seconds. That number, if it holds at scale and across diverse conversational contexts, would place it at the low end of the range that human listeners perceive as natural. The company did not reveal precise benchmark methodology, and the system is not yet publicly accessible, so independent verification remains pending.

The architectural choice that enables this is a Mixture-of-Experts (MoE) design scaled to 276 billion total parameters, with only approximately 12 billion parameters active during any single inference pass. MoE architectures have become the dominant paradigm for balancing capability and efficiency among frontier labs — Meta's Llama 4, Google's Gemini models, and OpenAI's GPT-4o all use variants of the approach. What Thinking Machines claims is different is that its model was trained from scratch specifically for continuous, full-duplex interaction rather than adapted from a text-first foundation model.

## Full-Duplex: The Overlooked Dimension

Most AI voice interfaces are, architecturally, turn-based: the user speaks, the model transcribes, processes, and responds, then waits for the next input. Full-duplex communication — where both parties can speak, listen, and interrupt simultaneously, as happens in human conversation — requires the model to maintain a persistent representation of the interaction state while processing incoming audio in real time. It is a substantially harder engineering problem than low-latency turn-based response.

Thinking Machines describes TML-Interaction-Small as natively full-duplex, built to handle interruptions, topic pivots, and overlapping speech without losing context or requiring a reset. In the preview demonstrations, the model reportedly handles mid-sentence corrections and conversational backchannel signals — the "mm-hmm" and "right, right" that signal comprehension in human dialogue — without interpreting them as new input prompts.

This design choice has significant implications for enterprise use cases. Customer service agents, tutoring applications, and medical intake workflows have long been constrained by the turn-based interaction paradigm, which creates unnatural pauses and makes users feel they are operating a tool rather than having a conversation. Full-duplex architecture, if it works reliably at scale, removes that constraint.

## Seventeen Months, $2 Billion, and a Product

The timeline of Thinking Machines Lab is worth appreciating. Murati left OpenAI in late 2024. By July 2025 — less than nine months after founding — the company had completed a $2 billion seed round at a $12 billion valuation, with participation from Andreessen Horowitz, Nvidia, AMD, Cisco, and Jane Street. In March 2026, the company announced a multi-year strategic partnership with Nvidia for one gigawatt of Vera Rubin computing capacity. In April 2026, a multi-billion dollar Google Cloud infrastructure deal followed.

The capital and compute commitments assembled by a company with no public product represent a bet on Murati's credibility and the team she recruited — a cohort that reportedly includes senior researchers from OpenAI, Google DeepMind, and Meta AI. The Interaction Models preview, released seventeen months after the company's founding, is the first public evidence of what that credibility has been building toward.

Limited access to TML-Interaction-Small is being rolled out over the coming months through a waitlist. The company has not announced pricing. A broader public release is expected in the second half of 2026.

## The Competitive Context

Thinking Machines enters a voice AI market that is more crowded in 2026 than it was even a year ago. ElevenLabs raised $500 million in March to expand its voice synthesis and conversational AI platform. Hume AI and Sesame AI have been demonstrating emotionally aware voice interaction. OpenAI's GPT Realtime API version 2 shipped last month with significantly improved latency and multilingual support. Google is expected to announce Gemini voice enhancements at I/O 2026 next Tuesday.

What separates Thinking Machines' positioning from these competitors is the insistence on full-duplex native architecture rather than system-level latency optimization applied to an existing model. Whether that architectural difference translates to a meaningful product advantage at scale is the question the Interaction Models preview raises but does not yet answer.

The more intriguing question is what Murati's team does next. The $12 billion valuation and the infrastructure deals in place suggest they are not building a voice assistant. They are building infrastructure for a new generation of human-AI interaction, with voice as the first surface. The model's name — TML-Interaction-Small — implies a larger sibling is in development. For a company that has been this quiet for this long, the "small" in the name feels like a deliberate understatement.
