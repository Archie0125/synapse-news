---
title: "Anthropic's Claude Mythos: The Leaked 'Step-Change' Model Rewriting AI Safety Calculus"
summary: "Anthropic has accidentally confirmed the existence of Claude Mythos — which it calls its most capable model to date, revealed through a misconfigured content management system. A leaked draft blog post describes a new tier beyond Opus and warns of unprecedented cybersecurity risks."
category: "ai-ml"
publishedAt: 2026-04-06T09:05:00Z
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "Fortune"
    url: "https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/"
  - name: "CNN Business"
    url: "https://www.cnn.com/2026/04/03/tech/anthropic-mythos-ai-cybersecurity"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/03/27/anthropic-launch-new-claude-mythos-model-advanced-reasoning-features/"
  - name: "Euronews"
    url: "https://www.euronews.com/next/2026/03/30/what-is-anthropics-mythos-the-leaked-ai-model-that-poses-unprecedented-cybersecurity-risks"
  - name: "Futurism"
    url: "https://futurism.com/artificial-intelligence/anthropic-step-change-new-model-claude-mythos"
tags:
  - "anthropic"
  - "claude"
  - "mythos"
  - "AI-safety"
  - "cybersecurity"
  - "frontier-models"
  - "LLM"
relatedSlugs:
  - "2026-04-04-openai-gpt5-leak-en"
  - "2026-04-04-open-source-llm-race-en"
  - "2026-04-06-microsoft-mai-models-independence-en"
---

## The Leak That Wasn't Supposed to Happen

Anthropic has spent four years building a reputation as the "safety-first" AI lab — the company founded by former OpenAI researchers who believed their former employer was moving too fast. The irony, then, is almost painful: the existence of Anthropic's most powerful model ever was revealed not by a press release, but by a misconfigured content management system that left an unpublished blog post publicly searchable.

Fortune reviewed the leaked material, which had also been located separately by security researchers, and reported it in late March 2026. Anthropic confirmed it shortly after, attributing the exposure to "human error" in their CMS configuration. In doing so, they confirmed details they hadn't planned to announce publicly: the model is real, it's called Claude Mythos, and an Anthropic spokesperson described it as "a step change" and "the most capable we've built to date."

That phrase — "step-change" — carries significant weight in the AI industry. It means something qualitatively different, not just quantitatively larger. It's the language used to describe the jumps between generations that actually alter what AI systems can do. Anthropic has used this term sparingly.

## What Is Claude Mythos?

The model naming is somewhat complex. "Mythos" is the name of the new model, which the draft blog post calls Claude Mythos. "Capybara" is the name the draft blog post gives to a new tier of model, and Capybara and Mythos appear to refer to the same underlying model. According to the draft, the new tier sits above the current Opus tier: "larger and more intelligent than our Opus models — which were, until now, our most powerful."

What can it do that current models cannot? Anthropic has been measured in its disclosures, but the contours are becoming clear from the early-access customer reports and the inadvertently published draft:

**Reasoning at scale.** Mythos shows significantly improved performance on complex, multi-step reasoning tasks that require maintaining coherent chains of logic across very long contexts. Early testers working in scientific research describe it as the first AI model capable of independently navigating literature reviews without losing thread — synthesizing contradictory papers and generating novel hypotheses with a degree of rigor that approaches expert human performance.

**Advanced coding.** The model's coding capabilities are described as a meaningful jump from Claude Opus 4.6. In internal testing, Mythos reportedly completes large-scale refactoring tasks that previously required multiple rounds of human correction in a single pass. It can reason about an entire codebase's architecture, not just isolated functions.

**Cybersecurity.** This is where Anthropic's communications have been most careful — and most revealing. The company is working with a small group of early access customers to test the model, and the draft blog says it is releasing it in early access to organizations to give cyber defenders a head start. The draft blog post says the model poses "unprecedented cybersecurity risks," and Anthropic says it wants to understand the near-term risks and share the results to help cyber defenders prepare.

## The Safety Paradox

The cybersecurity focus is Anthropic's acknowledgment of a tension at the heart of frontier AI development: the more capable a model becomes at understanding and reasoning about complex systems, the more capable it becomes at attacking them.

Anthropic's approach is to lean into controlled, supervised deployment in the cybersecurity vertical before broader release — accumulating evidence about how the model behaves in the wild with expert operators before democratizing access. This is the "responsible scaling" playbook, and it's been Anthropic's differentiating narrative.

But critics in the security research community have noted the obvious limitation: a model capable of producing "unprecedented" cybersecurity insights in the hands of a vetted enterprise client is, architecturally, the same model that could produce unprecedented attack capabilities in the hands of a less scrupulous user. The difference between a vulnerability report and an exploit is often syntactic.

CNN's reporting adds texture to this concern. Cybersecurity experts interviewed for the piece described Mythos as potentially the first model capable of autonomously developing novel zero-day exploits — not just cataloguing known vulnerabilities, but reasoning from first principles about where gaps in a given system's defenses might exist. That's a qualitative capability shift that the current generation of models, including Claude Opus 4.6 and GPT-5.4, does not clearly exhibit.

## The Release Strategy

Mythos is not launching publicly. As of early April, Anthropic has distributed access to "a small group of early access customers selected by Anthropic," with an explicit initial focus on cybersecurity applications. The company says it is "slowly expanding access to Claude Mythos to more customers using the Claude API over the coming weeks."

The caveat is significant: the draft blog notes that Mythos is expensive to run and not yet ready for general release." Anthropic is working to make it more efficient before any general release. This is consistent with the history of other frontier models — GPT-4 was initially expensive and capacity-constrained at launch, and its pricing fell by roughly 97% over 18 months as infrastructure improved and smaller distilled variants emerged.

The current expectation among Claude API customers is a limited beta through Q2 2026, with broader availability potentially tied to the release of a more efficient Mythos variant — internally called something other than Capybara, which presumably represents the maximum-compute configuration — in H2 2026.

## What Anthropic Signaled, Even Inadvertently

The leak, embarrassing as it was operationally, may have served a useful function for Anthropic. In a competitive market where OpenAI just raised $122 billion at an $852 billion valuation and Microsoft shipped independent frontier models, Anthropic needed a signal that it remains at the capability frontier.

Mythos provides that signal — and the cybersecurity framing provides the safety narrative that differentiates Anthropic from its rivals. The message is: we have the most powerful model, we know it's dangerous, and we're handling it more carefully than anyone else would.

Whether the safety-first approach proves durable — or whether competitive pressure eventually forces faster, broader rollout — will define Anthropic's next chapter. For now, Claude Mythos is the most anticipated model no one is allowed to use.

That might be exactly the point.

*Correction (November 15, 2026): 9 sentences were corrected or removed to match the sources listed on this page.*
