---
title: "Google Scraps Gemini 3.5 Pro Architecture Entirely, Targets July 17 With Full Rebuild"
summary: "Google DeepMind has abandoned the existing Gemini 2.5 Pro architecture mid-development and launched an entirely new pre-training run for Gemini 3.5 Pro, targeting a July 17 launch. The scrapped architecture hit performance ceilings in multi-step mathematical reasoning and SVG scene generation, prompting an unprecedented engineering pivot that DeepMind is betting will produce a model competitive with GPT-5.6 Sol and Anthropic's Fable 5."
category: "ai-ml"
publishedAt: 2026-07-11
lang: "en"
featured: false
trending: false
sources:
  - name: "BigGo Finance"
    url: "https://finance.biggo.com/news/6f0c6bb2-795f-4c57-9d09-6db691d7638a"
  - name: "HackerNoon"
    url: "https://hackernoon.com/google-delays-gemini-35-pro-to-july-17-the-strategic-play-behind-the-scrapped-base-model"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/319877/20260708/gemini-35-pro-targets-july-17-deepseeks-july-24-deadline-hits-developers-now.htm"
  - name: "Bind AI Blog"
    url: "https://blog.getbind.co/gemini-3-5-pro-slips-to-july-and-four-senior-google-researchers-just-left-for-anthropic/"
tags:
  - "Google"
  - "Gemini"
  - "DeepMind"
  - "AI models"
  - "large language models"
  - "model training"
relatedSlugs:
  - "2026-07-01-google-gemini-35-pro-july-launch-delayed-en"
  - "2026-07-04-google-deepmind-brain-drain-shazeer-jumper-en"
---

The story of Google's Gemini 3.5 Pro has taken a more dramatic turn than originally reported. What began as a delay announcement earlier this month — attributed at the time to standard quality checks — has resolved into something significantly larger: Google DeepMind pulled the plug on the existing Gemini 3.5 Pro architecture entirely, just days before its planned deployment, and launched a fresh pre-training run from scratch. The new target launch date is July 17.

## What Actually Happened to the Original Architecture

According to reporting from multiple sources close to the project, DeepMind engineers reached a conclusion that the Gemini 3.5 model trained on the 2.5 Pro base architecture had hit performance ceilings that could not be resolved through fine-tuning or post-training interventions. Two capability areas were identified as the critical failure modes:

**Multi-step mathematical reasoning**: The model consistently underperformed on complex chained mathematical derivations — the kind of extended, multi-stage proofs that are a primary use case for frontier models in academic, engineering, and scientific contexts. Internal benchmarks reportedly showed degradation in long-horizon reasoning chains, with the model losing track of intermediate steps in ways that could not be patched post-training.

**SVG scene generation**: The model struggled to produce accurate, well-structured Scalable Vector Graphics, a capability that has become increasingly important as enterprises use AI for UI design, data visualization, and technical diagram generation. Performance on SVG tasks fell below the bar DeepMind considered competitive with OpenAI's GPT-5.6 and Anthropic's Fable 5 at equivalent or higher cost.

Rather than ship a model with known limitations — and risk the kind of public benchmark-versus-reality gap that has damaged competitors — DeepMind made the decision to scrap the architecture and start over.

## The Scale of the Pivot

Scrapping a near-deployment-ready foundation model and launching a new pre-training run is not a routine engineering decision. Pre-training runs for frontier-class models consume tens to hundreds of millions of dollars in compute, require weeks to months of wall-clock time depending on cluster scale, and involve model architecture decisions that are difficult to reverse mid-run.

The decision to pull the model "just days before its targeted deployment," as one source described the timeline, suggests that DeepMind's internal evaluation process identified critical deficiencies only in late-stage testing — either because the full capability ceiling was not visible until the model was pushed through comprehensive holdout evaluations, or because competitive intelligence about GPT-5.6's actual capabilities reset DeepMind's performance threshold.

Sundar Pichai had referenced Gemini 3.5 Pro during the Google I/O keynote as a "next-month" release, giving the project a public commitment that the architecture scrapping has now made considerably more expensive to walk back cleanly.

## The Rebuilt Architecture's Specifications

The rebuilt Gemini 3.5 Pro targets several capability areas that the scrapped version fell short on, along with new features that DeepMind is positioning as competitive differentiators:

- A **2 million token context window**, substantially larger than the 1 million token context Gemini 2.5 Pro offered, and designed to accommodate full enterprise codebases, long-form document analysis, and extended research workflows
- A **Deep Think Reasoning Layer** for complex problem-solving — a refinement of the Deep Think mode introduced with Gemini 2.5 Pro that applies extended inference time selectively to high-difficulty problems rather than uniformly, reducing cost on routine queries
- **Autonomous workflow capabilities**, bringing Gemini 3.5 Pro into alignment with the agentic execution features that OpenAI and Anthropic have been shipping since early 2026

## The Talent Context

The architecture decision does not exist in isolation. DeepMind has lost several senior researchers in rapid succession in recent weeks, including two figures instrumental to Gemini's multimodal architecture and one senior researcher who had worked on the reasoning scaling pipeline. These departures, reported earlier this week, have raised questions about whether DeepMind's internal talent base remains intact enough to execute at frontier pace.

The architecture scrapping and the talent losses together create a perception problem for Google, even if neither is definitively causal. From the outside, the picture of a company that delayed its flagship model, then scrapped its architecture, while losing key researchers, reads as evidence of internal turbulence — regardless of whether the full restart is, in fact, the strategically correct move.

## What July 17 Actually Means

The July 17 target date is three days away from DeepSeek's V4 API migration deadline on July 24 — creating a narrow window in which developers weighing Chinese model alternatives will also be evaluating whether a rebuilt Gemini 3.5 Pro changes their calculations. That juxtaposition is unlikely to be accidental in DeepMind's release planning.

If the rebuilt Gemini 3.5 Pro delivers on its specifications — particularly the 2M context window and the improved math reasoning — it would meaningfully close the gap between Google and the current leaders on the tasks that enterprise buyers care most about. The question is whether a model that went through an unprecedented architecture restart in the past two weeks is ready for the kind of scrutiny that a flagship release from a major lab invites.

July 17 will tell us whether the decision to restart was brilliant urgency or manufactured confidence.
