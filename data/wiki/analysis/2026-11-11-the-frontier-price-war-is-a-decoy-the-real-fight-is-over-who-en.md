---
category: ai-ml
lang: en
published: '2026-11-11T06:28:48.054484+00:00'
sources:
- name: Dev.to
  url: https://dev.to/mohsinakram91/stop-paying-for-ai-to-think-out-loud-1dgn
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1030787/google-gemini-4-carbon-public-rollout
- name: Engadget
  url: https://www.engadget.com/2311855/gemini-4-carbon-now-available-worldwide/
- name: 9to5Google
  url: https://9to5google.com/2026/11/10/gemini-app-4-carbon/
- name: Hacker News
  url: https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/
summary: Google just priced its best model at a quarter of Anthropic's, and Amazon
  still found that the cheapest frontier model was 50x too expensive for the job.
title: The Frontier Price War Is a Decoy. The Real Fight Is Over Who Gets Fired.
trending_theme: Frontier Model Price War Intensifies
type: analysis
---

Here's the uncomfortable part of this week's model launches: the most important pricing story isn't Gemini 4 Carbon's $2 per million input tokens. It's that Amazon, Anthropic's biggest backer, pulled a Claude model out of one of the world's largest internal ticketing systems and replaced it with a 4-billion-parameter-class decision model that **can't write a single sentence**. It cut costs by 98%.

Frontier labs are fighting a price war over the top of the market. The bigger change is that a large share of enterprise AI work is leaving the top of the market altogether.

## The headline numbers

Start with what Google shipped. Gemini 4 Carbon became broadly available on November 10 at introductory pricing of **$2 per million input tokens and $10 per million output tokens**. The Verge puts that at roughly a fifth of OpenAI's GPT-6 Astra and a quarter of Anthropic's Fable 5.2, which launched the day before. Even when the price doubles to **$4/$20** after November 30, Carbon stays well below its frontier rivals on a per-token basis.

Then there's the benchmark Google chose to promote. It isn't a leaderboard score. Google co-launched a new Multimodal Knowledge Agents (MKA) benchmark with Artificial Analysis, where Carbon ranks first across 200 agentic tasks **while using 3x fewer tokens than the next-best model.** When a lab designs a benchmark around token efficiency, it's telling you what customers now ask about first.

For context on how quickly this has moved: GPT-4 launched in March 2023 at $30 input and $60 output per million tokens. Three and a half years later, a model Google calls its "strongest ever" launches at one-fifteenth of that input price and one-sixth of the output price. DeepSeek's R1 in January 2025 showed that frontier-adjacent reasoning could be sold for single-digit dollars. Since then, every lab has had to explain why its premium is worth paying.

## Per-token price is the wrong number

Google's own launch coverage admits the key point: lower per-token pricing "doesn't necessarily translate to lower costs as models can use different numbers of tokens for the same tasks."

That caveat carries the whole story. Output tokens usually cost 3 to 5 times more than input tokens, and with reasoning models, much of the output is the model thinking out loud on your bill. A developer on Dev.to described a simple case: sorting 50 customer messages should take about 500 output tokens as a table. Without a format instruction, the model writes a paragraph per message and the answer runs to about 2,500 tokens. The result is the same and the output bill is 5x higher.

Apply that to model selection. Suppose a model costs half as much per token but reasons twice as long. It costs you the same, and it's slower. Suppose another costs four times as much per token but finishes the task in a third of the tokens. That one is nearly competitive. This is why the useful unit is now **cost per completed task**, and why Google is pitching "3x fewer tokens" alongside "#1."

My view: within a year, per-token list prices will matter about as much as a CPU's clock speed. They're real numbers, technically comparable, and mostly misleading.

## What nobody is talking about: Google told you not to buy its best model

Read Google's positioning closely. It says **Argon, not Carbon, "remains the ideal choice for the majority of software engineering and knowledge work."** In the Gemini app's model picker, Argon is labeled "Code & analysis" and Carbon is labeled "Most complex work."

So a frontier lab launched its flagship and, in the same announcement, told most customers they don't need it. That's honesty about a market where the top model has become a specialist, something you assign the hardest 5% of the work to rather than a default.

Antigravity's new `/swarm` feature makes the same point. Google's suggested setup puts Carbon in the roles that need "the deepest reasoning" (architecture, coordination, auditing) and pairs it with "faster, lighter models" doing parallel work. The frontier model becomes the manager, and most of the tokens get spent by cheaper workers.

Taken together, Carbon, Fable 5.2, and Meta's Muse Ember are competing over a slice of each workflow, while the bulk of the volume moves to whatever is cheapest and good enough.

## The Amazon case study, read properly

The Strands Decider story deserves more attention than a launch-day benchmark chart.

Amazon teams used Claude Sonnet 4.6 to label tickets into 20 categories: customer escalations, capacity requests, automated alarms, security findings. Each ticket went through a long system prompt, and the model produced JSON plus reasoning. That's a sensible setup, and it's what most enterprises built in 2025.

Two engineers swapped in Strands Decider, a model that doesn't generate text. You give it state and a list of options, and it returns a probability for each option plus a confidence score. They tested the original 2B version, then moved to an E4B build on Gemma 4, tuned the confidence threshold, and **beat production Sonnet on a held-out ticket set.** It runs on a single A10G GPU (SageMaker `ml.g5.xlarge`), uses about 19 GiB of memory, and answers in roughly 640 ms. Amazon says the switch will save millions of dollars a year.

Three things stand out:

1. **The task never needed language generation.** Classification was squeezed into a text generator because that was the tool teams had. Every "write JSON explaining your reasoning" step was output-token spend on a multiple-choice question.
2. **The migration path is boring.** SQS, Lambda, SageMaker, AppConfig, CloudWatch, CDK. A three-way switch (`BEDROCK` / `DUAL` / new model) let them run both models side by side before cutting over. Any competent platform team can copy this in a quarter.
3. **Note who the vendor is.** AWS published this on its own Strands blog. Amazon sells Claude through Bedrock and is publicly showing customers how to stop paying for it on certain workloads. The cloud providers' incentive is to sell you GPU hours and their own models, not a partner's tokens.

The second-order effect: every enterprise CFO who reads this case study will ask which of their LLM workloads is secretly a classification problem. My estimate is that at a typical company, the answer covers a big share of call volume: routing, tagging, triage, moderation, and intent detection.

## The bear case

The strongest counterargument is Jevons' paradox. Cheaper tokens don't reduce total spend; they increase it. Agent swarms like `/swarm` multiply token use by the number of agents, adversarial verifiers rerun every change, and long-horizon tasks run for hours. Even if unit costs fall 90%, frontier revenue can keep rising because workloads that were unaffordable at $30 per million become routine at $4.

That's fair, and it's probably right in aggregate. It still misses the shape of the market. Frontier demand will grow in the hard-reasoning slice while it shrinks in the high-volume, low-complexity slice that has been quietly paying the bills. Labs whose revenue comes mostly from enterprises running Sonnet-class models on simple, repetitive tasks have the most exposure.

The second bear case: introductory pricing is a customer-acquisition tactic. Carbon's price doubles in three weeks, and Google is giving 10,000 scientists six months of free access, which looks a lot like a data-collection program. Google isn't committing to permanently low prices. It's buying adoption with a cash pile Anthropic doesn't have.

## What to Watch

- **December 1: Carbon's real price test.** When Carbon moves to $4/$20, I expect Google to either extend the introductory pricing or make Argon cheaper rather than let the gap with Fable 5.2 narrow. Google won't be the first to blink on price.
- **Tokens-per-task becomes a standard disclosure.** By mid-2027, at least two of the big three labs (Google, Anthropic, OpenAI) will publish efficiency metrics such as tokens or dollars per task on model cards, not just accuracy. MKA is the template.
- **Anthropic answers at the bottom of the market, not the top.** Fable 5.2 doesn't need a price cut to win hard tasks. Anthropic does need a credible answer to "Sonnet is too expensive for classification" within six months, whether that's a cheaper tier or a structured-output product. Without one, the Amazon story repeats across Bedrock customers.
- **Decision models get their own category.** Expect at least one more major cloud provider to ship a non-generative decision or classification model family with managed hosting by Q2 2027. Strands Decider is version one of a product category, not a one-off.
- **The question in procurement meetings changes** from "which model is smartest?" to "which of our tasks actually need a frontier model?" Companies that audit their workloads this way will cut AI bills by 50% or more without losing quality. Companies that don't will keep paying top rates for classification work.