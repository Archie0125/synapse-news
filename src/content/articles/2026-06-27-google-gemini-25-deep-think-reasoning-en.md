---
title: "Google's Gemini 2.5 Deep Think Claims the Top of Science, Math, and Reasoning Benchmarks"
summary: "Google launched Gemini 2.5 Pro with Deep Think mode on June 22, achieving 89.8% on MMLU-Pro and 82.4% on GPQA Diamond—surpassing Anthropic's Fable 5 and OpenAI's GPT-5.5 across science and reasoning. The extended-inference model uses parallel thinking and is available now for Google AI Ultra subscribers, with API access for developers arriving soon."
category: "ai-ml"
publishedAt: 2026-06-27
lang: "en"
featured: false
trending: true
sources:
  - name: "Google Blog"
    url: "https://blog.google/products-and-platforms/products/gemini/gemini-2-5-deep-think/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/ai/google-releases-olympiad-medal-winning-gemini-2-5-deep-think-ai-publicly-but-theres-a-catch"
  - name: "Engadget"
    url: "https://www.engadget.com/ai/google-introduces-the-deep-think-reasoning-model-for-gemini-25-pro-and-a-better-25-flash-174531020.html"
tags:
  - "google"
  - "gemini"
  - "deep think"
  - "reasoning models"
  - "benchmarks"
  - "ai-ml"
relatedSlugs:
  - "2026-06-27-openai-gpt56-sol-terra-luna-preview-en"
  - "2026-06-27-five-eyes-ai-cyber-threat-warning-en"
  - "2026-06-26-google-gemini-talent-exodus-adler-pritzel-anthropic-en"
---

For the past several months, the benchmark wars among frontier AI labs have been fought largely on incremental gains—a few percentage points here, a new math record there. On June 22, 2026, Google broke through that pattern with a release that didn't just top the leaderboard on one task. It led across science, math, and reasoning simultaneously.

Gemini 2.5 Pro with **Deep Think** is Google DeepMind's most capable publicly available model. It doesn't rely solely on scaling the same underlying architecture to new extremes—it adds a fundamentally different computational mode: extended, parallel inference at the moment of answering.

## What Deep Think Actually Does

Deep Think is not simply "slower Gemini with more compute." It's a reasoning architecture that changes how the model approaches difficult problems. When activated, Gemini 2.5 Pro generates multiple chains of thought simultaneously—exploring different solution paths in parallel—before converging on a final answer. Novel reinforcement learning techniques allow the model to improve its step-by-step problem-solving capabilities over time.

The practical effect is visible immediately in benchmark performance. On **MMLU-Pro**, a rigorous benchmark covering graduate-level questions across 57 academic subjects, Gemini 2.5 Pro with Deep Think scored **89.8%**—the highest achieved by any publicly available model. On **GPQA Diamond**, which tests graduate-level expertise in physics, chemistry, and biology, it scored **82.4%**, beating Anthropic's Fable 5 (79.1%, before its government-ordered suspension) and OpenAI's GPT-5.5 (76.3%).

On LiveCodeBench V6, a competitive programming benchmark that continuously updates to prevent training data contamination, Gemini 2.5 Deep Think also led the field. And on Humanity's Last Exam—one of the hardest multi-disciplinary benchmarks in existence, designed to probe genuine domain expertise rather than pattern matching—it posted state-of-the-art results across the board.

## The IMO Moment

The most striking demonstration of Deep Think's capabilities came from mathematics: an advanced research version of Gemini 2.5 achieved **gold-medal standard** at the 2025 International Mathematical Olympiad. The IMO tests creative mathematical problem-solving at a level that separates elite human mathematicians from the merely excellent—problems that require original insight, not computation.

Reaching gold-medal performance on IMO problems was, until recently, considered a target that would take years more of research. That it has been achieved—even in a research setting—marks a genuine inflection point in what machine reasoning can do.

The version available in the consumer Gemini app operates at **bronze-medal level** on IMO problems—remarkable in its own right—while running significantly faster than the research variant. The gap between app and research versions reflects a familiar compute-capability tradeoff: the research model burns more inference budget to explore deeper into the solution space than real-time consumer deployment permits.

## Availability and the Catch

Herein lies the constraint that benchmark numbers don't capture: access is tiered and limited.

Deep Think is currently accessible only to **Google AI Ultra subscribers** via a toggle in the Gemini app, with a fixed cap on daily prompts. This isn't a soft limit—users exhaust their Deep Think allocation and revert to standard Gemini 2.5 Pro for the remainder of the day. Enterprise and developer access through the Gemini API is "coming in coming weeks."

At standard Gemini 2.5 Pro pricing ($2.50 input / $15 output per million tokens), Deep Think mode is estimated at roughly **4x the cost** of standard inference. That positions it as a premium tool for tasks where frontier reasoning genuinely matters—complex scientific analysis, advanced mathematical derivations, multi-step software architecture—rather than everyday assistant queries where Gemini Flash is sufficient.

The Ultra subscriber gate is a calculated commercial decision. Google AI Ultra already carries a premium price, and restricting Deep Think to Ultra positions the feature as exclusive before the infrastructure can scale to general availability. It also allows Google to observe how Ultra subscribers actually use Deep Think at scale before committing to API pricing across the full developer tier.

## Safety and Refusal Trade-offs

One technical note that deserves attention: Deep Think demonstrated **improved content safety scores** compared to standard Gemini 2.5 Pro, but also showed a higher tendency to refuse benign requests. This is a well-documented tension in frontier reasoning models—as models get more sophisticated at identifying potential harms, their calibration on what constitutes harm tends to widen, catching legitimate requests in the safety net.

For researchers and enterprise users, this over-refusal tendency will be a practical friction point, particularly in domains like cybersecurity, medical research, and competitive intelligence where professional use cases superficially resemble adversarial ones. Google will need to calibrate this before API release if enterprise developers are to trust Deep Think as a production reasoning layer.

## The Competitive Landscape

The timing of Deep Think's launch was strategically favorable, whether intentional or not. Anthropic's Fable 5, which had posted a 79.1% GPQA Diamond score before becoming the most capable publicly available model of its time, was suspended globally on June 12 following a U.S. government export control directive. That suspension—even if temporary—created a window in which Google could claim the frontier reasoning crown without Fable 5 competing directly.

OpenAI's GPT-5.6 Sol, announced June 26 in limited preview, will be the immediate competitive test for Deep Think. Sol is explicitly designed for complex reasoning and research-grade tasks, and while OpenAI hasn't published full benchmark comparisons yet, the head-to-head will inevitably come once Sol reaches broader availability. Grok 4 from xAI also scores below Gemini 2.5 Deep Think on code, math, and reasoning according to currently available data.

## Why Extended Inference Changes the Equation

The deeper significance of Deep Think isn't its benchmark scores—it's what the approach reveals about where frontier AI capability development is heading.

The original scaling hypothesis—train larger models on more data—is running into two hard constraints: the availability of high-quality training data is finite, and training runs at the frontier now cost hundreds of millions of dollars and months of calendar time. Improvements are increasingly incremental per training dollar spent.

Extended inference is the alternative thesis: instead of only making a smarter model during training, make a smart model *think longer* at inference time. Deep Think's parallel exploration of solution paths, combined with RL-driven reasoning improvement, suggests that significant capability gains are available through inference-time compute allocation rather than training-time scaling alone.

This isn't unique to Google. OpenAI's o-series demonstrated extended thinking as a capability tier years ago. What makes Gemini 2.5 Deep Think notable is the magnitude of improvement it delivers and the breadth of benchmarks where it leads. The era where inference-time compute is a first-class lever for capability improvement—alongside training scale—has definitively arrived.

For enterprises evaluating AI platforms, the practical implication is that the question is no longer just "which model was trained best?" It's also "how much thinking time will you allocate per query, and at what cost?" Deep Think makes that a product decision as much as a research one.
