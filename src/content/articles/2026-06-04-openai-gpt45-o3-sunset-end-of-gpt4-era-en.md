---
title: "OpenAI Retires GPT-4.5 and o3, Closing the Book on the GPT-4 Generation"
summary: "OpenAI has confirmed it will retire GPT-4.5 on June 27 and o3 on August 26, 2026, ending the last standing members of the GPT-4 model family. GPT-4.5, launched in February, lasted only four months — one of the shortest model lifespans in OpenAI's history — superseded by a GPT-5 lineup that has proven decisively superior on every major benchmark. The retirements mark a genuine generational inflection point in the commercial AI stack."
category: "ai-ml"
publishedAt: 2026-06-04
lang: "en"
featured: false
trending: true
sources:
  - name: "gHacks Tech News"
    url: "https://www.ghacks.net/2026/06/03/openai-upgrades-gpt-5-5-instant-and-confirms-retirement-of-o3-and-gpt-4-5-models/"
  - name: "BleepingComputer"
    url: "https://www.bleepingcomputer.com/news/artificial-intelligence/openai-upgrades-gpt-55-as-it-plans-to-retire-legacy-chatgpt-models/"
  - name: "TechRadar"
    url: "https://www.techradar.com/ai-platforms-assistants/chatgpt/openai-just-quietly-retired-the-last-of-the-gpt-4-models-and-it-feels-like-the-end-of-an-ai-era"
  - name: "OpenAI API Deprecations"
    url: "https://developers.openai.com/api/docs/deprecations"
tags:
  - "OpenAI"
  - "GPT-4.5"
  - "o3"
  - "model retirement"
  - "GPT-5.5"
  - "AI models"
  - "developer tools"
relatedSlugs:
  - "2026-04-11-openai-spud-gpt55-pretraining-complete-en"
  - "2026-05-10-openai-gpt55-instant-chatgpt-default-en"
  - "2026-04-05-openai-gpt4o-retirement-en"
---

In the technology industry, version numbers tend to accumulate like sediment. Old models pile up in API documentation, get quietly deprecated, and slowly drain off usage. What OpenAI announced this week is different in character: the simultaneous retirement of GPT-4.5 and o3 represents not just model turnover but the formal closure of an architectural and commercial era — the GPT-4 generation — that reshaped how the world thought about artificial intelligence.

GPT-4.5 will be removed from ChatGPT and the API on June 27, 2026. The o3 reasoning model will follow on August 26, 2026. Both are being retired in favor of GPT-5.5 Instant, which has been upgraded this week with quality improvements, and the broader GPT-5 family.

## The Unusually Short Life of GPT-4.5

When OpenAI launched GPT-4.5 in February 2026, it positioned the model as its "most knowledgeable" at the time — the culmination of everything the company had learned about pre-training and fine-tuning through the GPT-4 lineage. Four months later, it is being retired. That is an extraordinarily short commercial lifespan, even by the accelerated standards of frontier AI development.

The speed of retirement reflects the pace at which the GPT-5 family has matured. GPT-5 launched in early 2026, followed by a rapid succession of refinements: GPT-5.2, GPT-5.3-Codex, GPT-5.4, and the GPT-5.5 series. On every benchmark that enterprise customers care about — reasoning accuracy, code generation quality, instruction following, agentic task completion — the GPT-5 models outperform GPT-4.5 comprehensively. Running two high-quality model families in parallel is operationally expensive and strategically confusing. OpenAI chose to rationalize.

The retirement is more emotionally charged than it might appear. GPT-4.5 had a behavioral profile that many users found distinctly appealing: its responses were warmer in tone and closer in character to the conversational GPT-4o that millions of people had come to rely on for day-to-day interaction. Several power users specifically preferred GPT-4.5 for creative writing, long-form drafting, and nuanced conversation tasks, citing a quality of voice that felt more distinctly human than the more analytically precise GPT-5 models. Those users will need to adapt to a new default.

## o3: A Reasoning Pioneer Without a Long-Term Audience

The retirement of o3 is less contentious but no less symbolically significant. Introduced in late 2024 as OpenAI's first dedicated reasoning model — capable of multi-step chain-of-thought problem solving across mathematics, science, and code — o3 was a genuine technical breakthrough. It set new standards on competition math, advanced programming benchmarks, and PhD-level scientific reasoning tasks.

But o3 always existed in a transitional zone. It was powerful enough to be impressive, but specialized enough that only a subset of users needed its particular flavor of extended deliberation. As the GPT-5 family incorporated reasoning capabilities natively — culminating in GPT-5.4's first-generation native computer-use capabilities and GPT-5.5's dramatic improvements in factual accuracy — the dedicated o3 use case became narrower. OpenAI reports that o3 saw meaningfully lower ongoing demand than GPT-4.5, and the 90-day sunset period (versus 30 days for GPT-4.5) reflects a recognition that its residual user base needs more migration time.

## GPT-5.5 Instant: The New Floor

The model taking the place of o3 and GPT-4.5 as ChatGPT's default and primary API offering is GPT-5.5 Instant, which received a significant quality upgrade this week. The numbers OpenAI has disclosed are meaningful: GPT-5.5 Instant produces 52.5% fewer hallucinated claims than its predecessor GPT-5.3 Instant on high-stakes prompts covering medicine, law, and finance. Inaccurate claims dropped by 37.3% on especially challenging conversations that users had flagged for factual errors.

Beyond raw accuracy improvements, the June update has changed GPT-5.5 Instant's stylistic behavior. Responses are now more naturally paced, with fewer of the long bullet-point lists that made AI output feel robotic in earlier model generations. The upgrade introduces a more conversational register for everyday interactions while maintaining analytical precision for technical tasks — a balance that previous model versions struggled to achieve simultaneously.

New structural features include writing blocks and code blocks rendered directly in chat responses, giving users cleaner visual separation between prose, structured data, and executable code without needing external tools.

## Migration Implications for Developers

For API users, the practical impact of GPT-4.5's retirement on June 27 is real. Applications built with the `gpt-4.5` model identifier will stop functioning. OpenAI's migration recommendation is to move to `gpt-5` or `gpt-5.3-codex` depending on whether the application prioritizes general intelligence or coding tasks. The GPT-5 pricing is different from GPT-4.5 — generally higher per token for output, though significantly more capable — so cost modeling will need to be revisited.

Enterprise customers on Azure OpenAI will face slightly different timelines through Microsoft Foundry's model lifecycle policy, which typically provides extended support windows. But the directional signal is identical: the GPT-4 era is over, and the entire OpenAI ecosystem is now GPT-5 native.

## What the Retirement Tells Us About OpenAI's Velocity

Reading OpenAI's model retirement cadence backward is instructive. GPT-4o was retired earlier this year. GPT-4.5 lasted four months. o3 is being phased out within roughly eighteen months of its debut. The interval between "state-of-the-art" and "deprecated" has compressed to less than a year.

This is partly a function of technical progress — the company is genuinely shipping better models faster than it ever has. But it is also a function of strategic clarity. OpenAI is simplifying its model portfolio aggressively, moving toward a world where most users interact with GPT-5.5 Instant as a universal default, GPT-5 or GPT-5.4 for professional and agentic tasks, and the upcoming GPT-5.6 at the frontier.

The architecture behind that simplification is significant: GPT-5.4 was the first model to natively merge general-purpose intelligence, reasoning, and computer-use capabilities into a single model, eliminating the need for separate reasoning-specialist models like o3. That consolidation is what makes the retirement of specialized models possible without leaving capability gaps.

## An AI Era in the Rearview Mirror

For anyone who has followed language AI since GPT-3 in 2020 or GPT-4 in March 2023, the retirement of these models carries a particular weight. GPT-4 catalyzed the current wave of enterprise AI adoption. GPT-4o made it accessible to hundreds of millions of casual users. GPT-4.5, brief as its tenure was, represented the final refinement of that lineage before the generational leap.

The transition to GPT-5 is not merely a version number increment. The models are architecturally different — trained on far more data, with native multimodality, extended context windows, and agentic capabilities that the GPT-4 family could not approach. That gap is why the retirements are happening as rapidly as they are, and why the industry should treat this moment not as routine deprecation but as the end of a chapter.

The next chapter has better tools. But the previous one is worth acknowledging.
