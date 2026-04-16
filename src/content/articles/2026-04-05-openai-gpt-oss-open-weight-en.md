---
title: "OpenAI Releases First Open-Weight Models in Seven Years, Challenging Meta's Llama Dominance"
summary: "OpenAI has released two open-weight models — gpt-oss-20b and gpt-oss-120b — under the Apache 2.0 license, ending a seven-year absence from open-source AI. The models target agentic workflows and directly compete with Meta's Llama series on both performance and permissive licensing."
category: "ai-ml"
publishedAt: 2026-04-05T10:15:00Z
lang: "en"
featured: true
trending: true
sources:
  - name: "OpenAI Blog"
    url: "https://openai.com/index/introducing-gpt-oss/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/ai/openai-returns-to-open-source-roots-with-new-models-gpt-oss-120b-and-gpt-oss-20b"
  - name: "Hugging Face Blog"
    url: "https://huggingface.co/blog/welcome-openai-gpt-oss"
tags:
  - "openai"
  - "open-source"
  - "llm"
  - "apache-2.0"
  - "mixture-of-experts"
  - "llama"
relatedSlugs:
  - "2026-04-05-google-turboquant-kv-cache-en"
  - "2026-04-05-noah-labs-fda-voice-heart-failure-en"
---

Seven years after releasing GPT-2 in 2019, OpenAI has broken its silence on open-weight AI models. On April 4, 2026, the company published two fully open models — `gpt-oss-20b` and `gpt-oss-120b` — under the Apache 2.0 license, one of the most permissive in software. The release marks a dramatic philosophical reversal for the organization that literally coined the term "open AI" before slowly retreating behind closed APIs and a for-profit restructuring.

## The Models, By the Numbers

`gpt-oss-120b` is a Mixture-of-Experts (MoE) architecture with 117 billion total parameters, but only activates approximately 5.1 billion per forward pass — making it far cheaper to run than a comparably-sized dense model. Its smaller sibling, `gpt-oss-20b`, totals 21 billion parameters and activates roughly 3.6 billion at inference time.

Both models are text-only in this initial release, with no multimodal capabilities. OpenAI positioned them as purpose-built for **agentic workflows**: tool use (web search, Python code execution), long multi-turn reasoning chains, and instruction following. They are natively compatible with OpenAI's Responses API — meaning developers can switch between the open-weight models and proprietary GPT-4o/o3 endpoints with minimal code changes.

The release landed simultaneously on Hugging Face and with deployment support baked in from AWS, Azure, Together AI, Vercel, Cloudflare, and Databricks. Ollama compatibility means any developer with a modern laptop can run `gpt-oss-20b` locally without a cloud dependency.

## Apache 2.0: The Boldest Licensing Move in AI This Year

The choice of Apache 2.0 is not subtle. While Meta releases Llama models under a custom license that restricts commercial use at scale (triggering a licensing conversation for apps with over 700 million monthly active users), OpenAI went further toward freedom than Meta has ever been willing to. Apache 2.0 permits unrestricted commercial use, fine-tuning, redistribution, and integration into proprietary products.

This is the same license that underpins Linux kernel derivatives and major enterprise open-source projects. By adopting it, OpenAI is signaling that these models are a genuine developer resource, not a marketing exercise with fine print.

Hugging Face CEO Clem Delangue called the release "a watershed moment for the ecosystem," noting that having a well-resourced lab with OpenAI's safety research infrastructure commit to open weights under this license changes the baseline expectation for what "open" means in AI.

## Why Now? The Competitive Logic

OpenAI's pivot is legible against the backdrop of 2025's open-model explosion. Meta's Llama 3.1 405B posted benchmark numbers competitive with GPT-4-era models. Google's Gemma 2 27B became a popular fine-tuning base. Mistral, Qwen, DeepSeek, and a long tail of open models gave developers credible alternatives to OpenAI's API. The developer community — historically OpenAI's most loyal constituency — began migrating inference workloads to open infrastructure that offered more control, lower costs, and no vendor lock-in.

At the same time, OpenAI has been under sustained pressure from regulators, former employees, and the AI safety community over its shift away from its original nonprofit mission. Releasing open-weight models is both a competitive move and a narrative one — a way to reclaim the identity encoded in the company's own name.

There is also a strategic dimension that goes beyond ideology. OpenAI earns significant revenue from API-layer services: fine-tuning, safety evaluation, the Responses API, and enterprise tooling. Open-weight base models can serve as top-of-funnel for that stack, especially if developers find it easier to fine-tune `gpt-oss-120b` and then deploy through OpenAI's managed infrastructure than to operate it themselves.

## Benchmark Performance: Competitive, Not Dominant

OpenAI released evaluation results showing `gpt-oss-120b` outperforming Llama 3.1 405B on MMLU, GPQA-Diamond, and LiveCodeBench, while trading blows with DeepSeek-V3 on several coding benchmarks. Independent evaluations from the Hugging Face Open LLM Leaderboard, posted within hours of the model's release, broadly confirmed OpenAI's numbers.

That said, the models land below the company's own frontier products. `gpt-oss-120b` is not a match for GPT-4o, let alone o3. OpenAI was explicit about this positioning: these are not distillations of their state-of-the-art systems, but purpose-built open models intended to be genuinely useful and deployable at reasonable cost.

At 3.6B active parameters per token, `gpt-oss-20b` runs efficiently on a single A100 GPU, and early testers report it handles tool-calling and structured output tasks with notably better reliability than prior open models in its compute class.

## The Llama Question

The elephant in the room is Meta. Llama 4 Scout, released just weeks earlier, had established new benchmarks for efficiency-per-parameter in the open ecosystem. OpenAI's release now gives developers a direct apples-to-apples comparison from a lab with a different safety research methodology and a different fine-tuning philosophy.

The competitive dynamics are moving fast. Both labs have significant reasons to keep open weights flowing: Meta to maintain developer platform relevance independent of its consumer apps, OpenAI to reclaim narrative territory and build top-of-funnel for its API ecosystem. The real beneficiary is the developer community, which now has a richer set of well-maintained, commercially usable models to build on.

## What's Next

OpenAI indicated that multimodal versions — supporting images and audio — are on the roadmap but gave no timeline. The company also hinted at a structured fine-tuning program that would let enterprises submit domain-specific data to receive customized variants, with the resulting models remaining under Apache 2.0 for the fine-tuned weights.

For now, the release validates a view that has been gaining traction across the industry: the frontier of AI capability is gradually separating from the frontier of AI openness, and smart labs can compete on both axes simultaneously without one cannibalizing the other. Whether OpenAI can sustain this commitment — or whether competitive pressure will eventually push it back toward closed weights — is the question worth watching over the next 12 months.
