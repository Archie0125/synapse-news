---
title: "OpenAI Launches GPT-5.5: A New Class of Autonomous AI That Plans, Codes, and Executes"
summary: "OpenAI released GPT-5.5 on April 23, its most capable agentic model yet, scoring 82.7% on Terminal-Bench 2.0 and 84.9% on the GDPval occupational benchmark. Priced at $5/$30 per million tokens, the model runs on NVIDIA GB200 NVL72 infrastructure and powers Codex for over 10,000 NVIDIA employees already."
category: "ai-ml"
publishedAt: 2026-04-24
lang: "en"
featured: true
trending: true
sources:
  - name: "OpenAI Blog"
    url: "https://openai.com/index/introducing-gpt-5-5/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/"
  - name: "NVIDIA Blog"
    url: "https://blogs.nvidia.com/blog/openai-codex-gpt-5-5-ai-agents/"
  - name: "The Decoder"
    url: "https://the-decoder.com/openai-unveils-gpt-5-5-claims-a-new-class-of-intelligence-at-double-the-api-price/"
  - name: "Artificial Analysis"
    url: "https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model"
tags:
  - "OpenAI"
  - "GPT-5.5"
  - "AI agents"
  - "agentic AI"
  - "Codex"
  - "NVIDIA"
  - "large language models"
relatedSlugs:
  - "2026-04-23-meta-model-capability-initiative-tracking-en"
  - "2026-04-23-thinking-machines-lab-google-cloud-deal-en"
---

OpenAI shipped GPT-5.5 on April 23, a fully retrained model the company calls its "smartest and most intuitive" release to date — and the benchmark numbers make a strong case. The model tops the Artificial Analysis Intelligence Index with a score of 60, three points ahead of the next best competitors: Claude Opus 4.7 and Gemini 3.1 Pro Preview, both sitting at 57.

The release is not just an incremental upgrade. GPT-5.5 represents a deliberate architectural bet on agentic work: give the model a complex, multi-part task, and it will plan, use tools, check its own work, navigate ambiguity, and keep going until finished. That positions it squarely as infrastructure for autonomous AI "digital workers," not just a better chatbot.

## Benchmark Dominance Across Agentic Tasks

OpenAI published a broad scorecard that reinforces GPT-5.5's claim to best-in-class status across the metrics that matter most for real-world deployment:

- **Terminal-Bench 2.0** (complex command-line workflows requiring planning, iteration, and tool coordination): **82.7%**, up from 75.1% for GPT-5.4 — a 7.6-point jump.
- **SWE-Bench Pro** (real-world GitHub issue resolution): **58.6%**, solving more tasks end-to-end in a single pass than any previous model.
- **GDPval** (agent performance across 44 professional occupations, from legal research to financial analysis): **84.9%**.
- **OSWorld-Verified** (operating real computer environments autonomously): **78.7%**.
- **Tau2-bench Telecom** (complex customer-service workflow automation): **98.0%** without prompt tuning.
- **Expert-SWE** (OpenAI's internal coding evaluation): **73.1%**, versus 68.5% for GPT-5.4.

The cumulative picture is of a model that has crossed a meaningful threshold in agentic capability — not merely generating text about tasks, but reliably completing them across diverse, high-stakes domains.

## Codex Gets GPT-5.5 — and NVIDIA Is Already Running It at Scale

The most concrete deployment signal came from NVIDIA. GPT-5.5 now powers Codex, OpenAI's agentic coding application, running on NVIDIA's GB200 NVL72 rack-scale systems. According to NVIDIA, more than 10,000 of its employees — spanning engineering, product, legal, marketing, finance, sales, HR, and operations — are already using GPT-5.5-powered Codex in their daily work.

That is a notable proof-of-concept for enterprise-wide agentic AI adoption, and the hardware context matters: NVIDIA's GB200 NVL72 systems deliver 35x lower cost per million tokens and 50x higher token throughput per second per megawatt compared to prior-generation infrastructure. GPT-5.5 was co-designed for and trained on GB200 and GB300 NVL72 systems, making it one of the first frontier models with deep architectural co-optimization alongside the hardware it runs on.

Internally, OpenAI reportedly codenamed the model "Spud" — a contrast to the grandeur of its public positioning, but consistent with the company's tradition of understated internal project names.

## What Changes in Practice

For developers and enterprise users, the most important shift is behavioral, not just numerical. GPT-5.5 understands user intent faster and carries more of the execution itself. Previous models in this generation required careful step-by-step orchestration to handle complex tasks reliably. GPT-5.5 is designed to accept messy, underspecified instructions and produce clean, verified outputs.

In practical terms, this means a user can hand the model a disorganized research brief, a multi-file codebase with ambiguous requirements, or a complex customer service workflow and expect the model to make reasonable inferences, use tools appropriately, double-check its output, and complete the task — rather than stalling or requiring constant guidance.

OpenAI frames this as a shift toward what it calls "digital workers": AI agents that don't just assist humans but take on entire workstreams autonomously. GPT-5.5 excels specifically at writing and debugging code, conducting online research, analyzing data, creating documents and spreadsheets, operating software interfaces, and chaining across multiple tools in sequence.

## Pricing: Double the Cost, Fewer Tokens Required

For API developers, GPT-5.5 arrives with a meaningful price increase: **$5 per million input tokens and $30 per million output tokens** — exactly double the cost of GPT-5.4's $2.50/$15 pricing. The Pro tier for heavy agentic use cases runs at $30/$180 per million tokens.

OpenAI and independent benchmarking firm Artificial Analysis both note that GPT-5.5 uses approximately 40% fewer tokens on equivalent agentic tasks than its predecessor, which absorbs much of the per-token price hike in practice. The net cost increase for real-world workloads is estimated at roughly 20% — significant, but manageable for applications where output quality justifies the spend.

Availability rolled out immediately to ChatGPT Plus, Pro, Business, and Enterprise subscribers on April 23. API access opened simultaneously.

## The Competitive Landscape Shifts Again

The release resets the competitive benchmarks at the top of the frontier. Claude Opus 4.7, released by Anthropic just days earlier, had briefly held the Intelligence Index lead; GPT-5.5 displaces it within a week. The speed of leapfrogging at the frontier has accelerated dramatically in 2026, with major releases from Anthropic, Google, xAI, and now OpenAI arriving in rapid succession.

For enterprises evaluating which foundation model to build on, the volatility creates both opportunity and risk. GPT-5.5's strong agentic benchmarks make it the obvious choice for autonomous workflow automation today — but the gap between top models is narrowing, and the table may look very different in another month.

What is clear is that the industry has moved past debating whether AI can handle complex tasks autonomously. The question now is which model handles them most reliably, at what cost, and with what governance controls in place. GPT-5.5 makes a compelling first-mover argument for 2026's agentic AI wave — but the competition is watching closely.
