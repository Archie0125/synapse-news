---
title: "Claude Opus 4.7 Retakes the AI Crown With a Vision Leap and Agentic Gains"
summary: "Anthropic released Claude Opus 4.7 on April 16, pushing the model past GPT-5.4 and Gemini 3.1 Pro on virtually every major benchmark. SWE-bench Verified climbed to 87.6%, vision accuracy surged from 54.5% to 98.5%, and a new 'xhigh' effort level enables sustained reasoning across multi-hour autonomous workflows — all at the same price as its predecessor."
category: "ai-ml"
publishedAt: 2026-04-17
lang: "en"
featured: true
trending: true
sources:
  - name: "Anthropic"
    url: "https://www.anthropic.com/news/claude-opus-4-7"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/anthropic-claude-opus-4-7-coding-agentic-benchmarks-release"
  - name: "GitHub Changelog"
    url: "https://github.blog/changelog/2026-04-16-claude-opus-4-7-is-generally-available/"
tags:
  - "Claude"
  - "Anthropic"
  - "AI models"
  - "benchmarks"
  - "agentic AI"
  - "vision AI"
relatedSlugs:
  - "2026-04-17-openai-cerebras-20b-chip-deal-en"
  - "2026-04-15-anthropic-30b-revenue-google-broadcom-en"
  - "2026-04-10-anthropic-claude-managed-agents-en"
---

# Claude Opus 4.7 Retakes the AI Crown With a Vision Leap and Agentic Gains

Anthropic released Claude Opus 4.7 on Wednesday, delivering the most substantial single-generation capability jump the company has produced since the original Opus 4 launch. The new model tops leaderboards across coding, agentic reasoning, and vision tasks—beating OpenAI's GPT-5.4 and Google's Gemini 3.1 Pro on nearly every metric that enterprise developers track—while shipping at identical pricing to its predecessor.

The release is well-timed. Anthropic disclosed a $30 billion annualized revenue run rate just ten days ago, and competition for the frontier AI crown has never been more compressed. GPT-5.4 launched in early March 2026. Gemini 3.1 Pro followed in February. Opus 4.7 now restores the margin that Anthropic held until earlier this year.

## The Benchmark Picture

The numbers are hard to minimize. On SWE-bench Verified—the industry's most widely cited software engineering evaluation—Opus 4.7 scores 87.6%, up from 80.8% on Opus 4.6. That is a nearly 7-point gain in a single generation, in a benchmark where the difference between 80% and 90% represents the gap between a model that can handle most real-world tickets and one that can handle almost all of them.

SWE-bench Pro, a harder variant released late last year with less training-set contamination, showed an even steeper gain: from 53.4% to 64.3%. CursorBench, which simulates multi-step code editing in realistic IDE sessions, jumped from 58% to 70%. GPT-5.4 Thinking, OpenAI's current flagship, scores 58% and 62% on those same benchmarks, respectively.

On financial analysis tasks—a vertical that accounts for a significant portion of Anthropic's enterprise revenue—Opus 4.7 scored 78.4%, compared to 69.1% for GPT-5.4 Thinking and 72.2% for Gemini 3.1 Pro. Cursor pushed a blog post within hours of the launch highlighting the coding gains; GitHub has scheduled a benchmark response for next week.

The one area where GPT-5.4 Thinking still holds its own is math-heavy evaluations such as MATH-500 and competition-level theorem proving, where OpenAI's model matches or edges past Opus 4.7. For most developers, however, those benchmarks are less decision-relevant than the coding and agentic suites.

## Vision, Rebuilt

The most dramatic improvement in Opus 4.7 is in visual understanding—and the numbers border on the implausible until you examine the methodology. The model now accepts images up to 2,576 pixels on the long edge, more than three times the resolution ceiling of previous Claude versions. Anthropic describes the visual encoding stack as fundamentally redesigned, not iteratively improved.

The benchmark consequence is stark: vision task accuracy jumped from 54.5% to 98.5% in Anthropic's internal evaluations. External developers who tested the model before launch corroborated the improvement. One engineer testing the model on detailed PCB schematics reported that Opus 4.7 could accurately identify individual component labels and trace signal paths that Opus 4.6 "essentially made up." Another testing on dense financial tables noted that the model could correctly parse and reason over multi-column data at a resolution that previously caused systematic errors.

For agentic applications—where models must read screenshots, interpret UI states, and take responsive actions—this vision upgrade has transformational implications. Computer-use tasks that previously required multiple observation-correction cycles can now, in many cases, be completed in a single pass. Anthropic's internal computer-use benchmark showed a 34% improvement in single-pass task completion, rising from 51% to 85%.

## The xhigh Effort Level

Anthropic also introduced a new compute tier called xhigh, slotting between the existing high and max effort settings. The company recommends starting with high or xhigh for most coding and agentic use cases, and Claude Code now defaults to xhigh for all subscription plans.

The reasoning behind the new tier reflects something non-obvious about how frontier models actually perform. Large models allocate reasoning compute dynamically, and in long agentic conversations—where context is dense and the model must integrate many prior tool calls before acting—there is a tendency for effective reasoning depth to taper off relative to the model's theoretical maximum. The xhigh setting is engineered to sustain elevated reasoning throughout multi-hour workflows rather than letting it degrade as conversation length grows.

In Anthropic's benchmarks, xhigh-setting completions for 10-turn tool-use scenarios showed a 12% higher task completion rate than high-setting equivalents, at approximately 30% greater compute cost. For production agentic applications—customer support automation, autonomous code review, financial document processing—that tradeoff is likely worth it in the majority of deployment contexts.

## Safety and Cybersecurity Controls

Opus 4.7 ships with built-in cybersecurity safeguards: automatic detection and blocking of requests that indicate prohibited or high-risk security uses. Anthropic has not disclosed technical details of the implementation, describing it broadly as an evolution of its Constitutional AI approach.

The timing is pointed. OpenAI launched GPT-5.4 Cyber last week—a specialized variant tuned for offensive security research—to immediate controversy over its ability to generate working exploit code. Anthropic is taking the opposite positioning: a general-purpose model with safety baked in, rather than a bifurcated offering with a separately managed security version.

This distinction will matter to enterprise buyers whose legal and compliance teams are increasingly scrutinizing AI vendor practices. Several Fortune 500 procurement officers have told reporters that "dual-version" AI offerings—where a more capable but less constrained model exists in parallel—complicate internal governance.

## Pricing and Availability

Opus 4.7 is priced identically to its predecessor: $5 per million input tokens and $25 per million output tokens through the Anthropic API. The model is available immediately across Claude.ai on all subscription tiers, the Anthropic API, Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Azure AI Foundry.

For developers currently running Opus 4.6 in production, Anthropic's migration documentation recommends testing agentic prompts first. Because the model's stronger intermediate reasoning can change the order and content of tool calls even when final outputs are equivalent, automated regression testing against expected outputs may produce false failures. Testing against task-completion outcomes rather than exact output strings is the recommended approach.

## The Competitive Moment

The release reinstates Anthropic at the top of the frontier model leaderboard after a period when OpenAI's GPT-5.4 Thinking and Turbo variants had narrowed the gap. The margin is not decisive—both companies sit within a few percentage points of each other across most benchmarks—but the breadth of Anthropic's improvement, spanning coding, vision, and agentic tasks simultaneously, represents a more comprehensive advance than its rivals delivered in their most recent releases.

The deeper competitive pattern worth watching is cadence. GPT-5.4 launched in March. Gemini 3.1 Pro in February. Opus 4.7 in April. Frontier model releases that once came annually now arrive quarterly, with each generation delivering double-digit benchmark gains. For enterprises evaluating which AI platform to standardize on, that pace makes heavy platform lock-in a risky bet—and helps explain why Anthropic, OpenAI, and Google are all racing to deepen workflow integrations and API stickiness alongside raw model capability.

Opus 4.7 is Anthropic's strongest answer yet to the question of whether it can sustain its technical lead as it scales commercially. At $30 billion in annualized revenue and growing, the company now has the resources to keep answering it.
