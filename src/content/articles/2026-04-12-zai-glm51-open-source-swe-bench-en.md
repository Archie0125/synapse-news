---
title: "Z.ai's GLM-5.1 Becomes First Open-Source Model to Top SWE-Bench Pro — Trained on Huawei Chips"
summary: "Chinese AI lab Z.ai released GLM-5.1, a 754-billion-parameter open-weight model under the MIT license that scored 58.4% on SWE-Bench Pro — surpassing GPT-5.4 and Claude Opus 4.6 on real-world code repair. The model can operate autonomously for up to eight hours and was trained entirely on Huawei Ascend 910B hardware, with no Nvidia involvement."
category: "ai-ml"
publishedAt: 2026-04-12
lang: "en"
featured: false
trending: true
sources:
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/04/08/z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4"
  - name: "Hugging Face"
    url: "https://huggingface.co/zai-org/GLM-5.1"
  - name: "Winbuzzer"
    url: "https://winbuzzer.com/2026/04/09/z-ai-releases-glm-5-1-754b-model-tops-swe-bench-pro-xcxwbn/"
tags:
  - "open-source"
  - "Z.ai"
  - "GLM-5.1"
  - "Zhipu AI"
  - "SWE-Bench"
  - "agentic AI"
  - "Huawei Ascend"
  - "coding AI"
relatedSlugs:
  - "2026-04-05-google-gemma-4-apache-en"
  - "2026-04-06-deepseek-v4-huawei-chips-en"
  - "2026-04-04-open-source-llm-race-en"
---

For years, the open-source AI community has celebrated competitive models that could nearly match — but never quite beat — the best closed-source systems on rigorous software engineering benchmarks. On April 7, 2026, that changed. Z.ai, the commercial platform spun out of Beijing's Zhipu AI lab, released GLM-5.1: a 754-billion-parameter mixture-of-experts model that became the first open-weight system to claim the top spot on SWE-Bench Pro, the industry's most demanding real-world code repair leaderboard.

The score — 58.4% on SWE-Bench Pro — beat both OpenAI's GPT-5.4 and Anthropic's Claude Opus 4.6. Three days later, on April 10, GLM-5.1 posted a 1,530 Elo score on Code Arena, landing in third place globally, behind only claude-opus-4-6-thinking (1,548) and claude-opus-4-6 (1,542). No open model has previously cracked the Code Arena top three. The jump from GLM-5.0 to 5.1 represents a +90 Elo improvement in a single release cycle.

## What Makes GLM-5.1 Different

GLM-5.1 is not a general-purpose chatbot upgrade. Z.ai built it from the ground up for *agentic engineering*: long-running, multi-step software tasks that require sustained planning, execution, and self-correction. In benchmark demos, the model operated autonomously for up to eight hours in a single continuous run — planning, writing code, running tests, identifying failures, and iterating to a final solution without human intervention. That puts it squarely in competition with proprietary coding agents like OpenAI's Devin successor and Anthropic's Claude Code, not just raw chatbot rankings.

Under the hood, GLM-5.1 uses a MoE + DSA (Decomposed Sparse Attention) architecture trained with asynchronous reinforcement learning. Unlike dense transformers that activate all parameters on every token, GLM-5.1 keeps inference costs comparable to a 37-billion-parameter dense model despite its 754B total parameter count. The context window supports up to 200,000 tokens with a maximum output of 128,000 tokens — critical for agentic tasks that require maintaining coherent state across entire codebases.

Deployment is straightforward: the model weights are fully public on Hugging Face under an MIT license, enabling unrestricted commercial use, modification, and redistribution. Inference is supported via SGLang, vLLM, xLLM, Transformers, and KTransformers for self-hosting, and the Z.AI platform exposes an OpenAI SDK-compatible API for cloud access.

## The Huawei Chip Story

Perhaps the most geopolitically significant detail in GLM-5.1's release notes is the training stack: every parameter was optimized on Huawei Ascend 910B chips. No Nvidia hardware was involved. This is the largest frontier-capable model to publicly confirm a China-domestic training pipeline — and it arrives amid ongoing uncertainty about the future of US semiconductor export controls.

The timing matters. Congress is currently debating the MATCH Act, proposed legislation that would extend restrictions to deep-ultraviolet (DUV) lithography tools, closing what critics call the last major loophole in chip export policy. Meanwhile, Z.ai's result suggests that Chinese AI labs have already achieved enough optimization on Ascend hardware to train models that rival — and in specific benchmarks, surpass — models trained on Nvidia H100 and H200 clusters. The gap that Western policymakers assumed export controls were maintaining may be narrower than advertised.

"Training GLM-5.1 entirely on Ascend was not a workaround," said a Z.ai engineer in a post published alongside the release. "It was the plan from day one. Ascend 910B has enough compute for frontier-class training if you know how to use it."

## SWE-Bench Pro and What It Measures

SWE-Bench Pro, introduced in early 2026 as the successor to the original SWE-Bench, tests AI systems against real GitHub issues drawn from production-level Python repositories. Each problem requires the model to read existing code, understand the bug report, write a patch, and pass an existing test suite — the same workflow a human engineer faces on a daily basis. Unlike coding competitions or synthetic benchmarks, SWE-Bench Pro is hard to game because the test cases are held out and the issues are drawn from repositories with complex inter-dependencies.

At 58.4%, GLM-5.1 beats GPT-5.4 and matches human expert-level performance on a subset of tasks, according to researchers who have compared AI scores against the average patch-acceptance rate for senior engineers on the same repository set. That does not mean the model solves every problem a senior engineer could; it means that for the specific class of well-scoped, textually described issues that SWE-Bench selects, GLM-5.1's output is indistinguishable from a strong human patch more than half the time.

## Industry Implications

The release reshapes several assumptions that have structured the AI landscape for the past two years:

**Open-source has caught up on code.** For software engineering tasks, the proprietary advantage of GPT and Claude has effectively been neutralized. Any company building coding tools on top of closed APIs now has a free, MIT-licensed alternative with comparable or superior benchmark performance.

**China's domestic AI stack is real.** The combination of GLM-5.1 (trained on Huawei chips) and DeepSeek V4 (expected late April, also on Ascend 950PR) demonstrates that Chinese labs have successfully built a vertically integrated AI training pipeline that operates independently of US-controlled hardware.

**Agentic benchmarks are the new frontier.** SWE-Bench Pro and Code Arena are replacing single-turn MMLU and HumanEval as the benchmarks that matter. GLM-5.1's focus on 8-hour autonomous runs signals that the industry has shifted its attention from *how smart is the model?* to *how long can it work?*

## What Comes Next

Z.ai has indicated that GLM-5.1 is a stepping stone toward a full multimodal agentic release later in 2026. The company is expanding its developer platform to support tool-calling, sandboxed code execution, and long-term memory — features currently only available through closed platforms like Claude Code and OpenAI's operator API.

For developers, the immediate opportunity is clear: a state-of-the-art coding model is now available for free, with no usage restrictions, deployable locally on consumer hardware via quantized versions. The first genuinely open frontier coding agent has arrived, and it was built in Beijing on chips Washington tried to block.
