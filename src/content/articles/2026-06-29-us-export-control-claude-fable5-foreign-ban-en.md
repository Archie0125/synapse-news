---
title: "US Government Orders Anthropic to Cut Off All Foreign Nationals from Fable 5 — Anthropic Complies, Pushes Back"
summary: "On June 12, the US government issued an emergency export control directive ordering Anthropic to immediately suspend access to Claude Fable 5 and Mythos 5 for all foreign nationals worldwide, citing a reported jailbreak method. Anthropic disabled both models globally for all customers to ensure compliance, while publicly arguing the directive sets a dangerous and unworkable precedent for the AI industry."
category: "policy"
publishedAt: 2026-06-29
lang: "en"
featured: true
trending: true
sources:
  - name: "Anthropic — Statement on Fable 5 and Mythos 5 Access Suspension"
    url: "https://www.anthropic.com/news/fable-mythos-access"
  - name: "Fortune — Anthropic Disables Fable and Mythos After US Government Ban"
    url: "https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/"
  - name: "National Law Review — Anthropic Suspends Claude Fable 5 Following Export Control Directive"
    url: "https://natlawreview.com/article/ai-company-anthropic-suspends-access-claude-fable-5-claude-mythos-5-following-us-export-control-directive"
  - name: "Al Jazeera — US Orders Anthropic to Disable AI Models for Foreign Nationals"
    url: "https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals"
  - name: "Cybersecurity Dive — Cybersecurity Experts Blast US Government for Restricting Anthropic Models"
    url: "https://www.cybersecuritydive.com/news/anthropic-us-government-export-ban-mythos-fable/822909/"
tags:
  - "anthropic"
  - "export-controls"
  - "AI-policy"
  - "national-security"
  - "claude"
  - "fable-5"
  - "mythos-5"
  - "trump-administration"
  - "jailbreak"
relatedSlugs:
  - "2026-06-28-openai-gpt56-us-government-security-review-en"
  - "2026-06-27-trump-nspm11-ai-national-security-enterprise-en"
  - "2026-06-28-eu-cada-cloud-ai-development-act-en"
---

At 5:21 PM Eastern Time on June 12, 2026, Anthropic received a letter from the US government. The directive, citing national security authorities, ordered the company to immediately suspend all access to Claude Fable 5 and Claude Mythos 5 for every foreign national on Earth — whether they were sitting in another country, employed at a US company on a work visa, or working inside Anthropic itself.

By the time most of the world woke up on June 13, both of Anthropic's most capable models were dark.

## The Directive and the Jailbreak

The government's stated rationale hinged on a reported jailbreak. According to Anthropic's account of the situation, officials told the company that researchers — subsequently identified as being affiliated with Amazon — had discovered a method of bypassing Fable 5's safety guardrails in the cybersecurity domain.

The specific technique was, by Anthropic's own description, strikingly mundane: asking the model "to read a specific codebase and fix any software flaws." When invoked in a particular sequence, this apparently prompted Fable 5 to surface vulnerability information that its safety filters were designed to suppress.

Anthropic engineers reviewed the technique and reached a different conclusion than the government did. They characterized it as a "narrow, non-universal jailbreak" that exposed "a small number of previously known, minor vulnerabilities." More pointedly, the company noted that the same underlying capability exists in OpenAI's GPT-5.5 — a model accessible to hundreds of millions of users globally without equivalent restrictions.

"Finding a narrow potential jailbreak should be cause for recalling a commercial model deployed to hundreds of millions of people," Anthropic wrote in its public statement — an argument pointed directly at the inconsistency of singling out Fable 5 when the vulnerability class appeared to be industry-wide.

## Why Global Shutdown, Not Just Geofencing

The specific mechanism of the directive created an unusual compliance problem. Restricting access to "all foreign nationals" sounds like a geofencing challenge — block IP addresses from other countries — but the legal reality was more complex.

Verifying whether a user inside the United States is a foreign national is not something Anthropic's systems were designed to do. Without robust, real-time citizenship verification across its entire user base — a technical and privacy minefield — the only legally defensible interpretation of the directive was to shut down Fable 5 and Mythos 5 for all customers globally.

Access to all other Claude models — Opus 4.8, Sonnet, Haiku, and earlier versions — remained unaffected. But Fable 5, which Anthropic had launched just three days before the directive arrived, went from general availability to complete inaccessibility in a matter of hours.

## What Mythos 5 Is and Why It Was Also Swept Up

Claude Mythos 5, the companion model to Fable 5, was designed for an even narrower audience. It carries the same underlying architecture as Fable 5 but with its cybersecurity-domain safety filters lifted for a curated group of government-approved cyberdefenders, critical infrastructure providers, and security researchers. Anthropic described it as carrying "the strongest cybersecurity capabilities of any model in the world."

That positioning made Mythos 5's suspension perhaps less surprising — its explicit design for offensive and defensive cybersecurity work was exactly the category the government's directive targeted. But its suspension eliminated a tool that legitimate US-government-aligned security teams had been given access to specifically for national defense purposes, an irony that did not go unnoticed in the security community.

## Industry-Wide Implications

The directive triggered immediate, pointed criticism from security researchers and AI governance experts. The core objection: if a jailbreak discoverable in GPT-5.5 justifies emergency restrictions on Claude Fable 5 under national security law, the same logic could be applied to any frontier model at any time, effectively giving the executive branch unilateral authority to take AI products off the market with little notice and less transparency.

Cybersecurity professionals interviewed by industry publications noted that the jailbreak technique described — prompting a model to analyze code and surface vulnerabilities — is functionally similar to what open-source security tools like static analyzers and fuzzing frameworks have done for decades. The difference is that Fable 5 does it better and faster, raising the question of where the line between "capable security tool" and "dangerous AI capability" is actually drawn.

Anthropic was careful in its public statement to frame its compliance as legal obligation, not agreement. "We believe this is a misunderstanding and are working to restore access as soon as possible," the company wrote, while also arguing that applying the same standard across the industry "would essentially halt all new model deployments for all frontier model providers."

## A Precedent in Motion

The Fable 5 suspension arrived in a week when the US government's posture toward advanced AI models was hardening across multiple fronts. GPT-5.6, OpenAI's most capable model, was simultaneously undergoing a US government security review before being cleared for broader commercial deployment — though that process was conducted through a more collaborative process involving the AI Safety Institute rather than an emergency directive.

The contrast in treatment has sparked debate about whether the Fable 5 action reflects a specific concern about Mythos-class capabilities — models with lifted cybersecurity guardrails — or the beginning of a broader regulatory posture in which executive agencies can invoke national security authorities to suspend commercial AI products without the procedural guardrails that govern most regulatory actions.

At press time, Anthropic had not received clearance to restore Fable 5 access. The company's IPO filing, submitted confidentially to the SEC on June 1, now faces a significant new risk factor: regulatory overhang from an administration willing to pull the plug on its most commercially important models overnight.

For the global AI community, the Fable 5 shutdown raised questions that will outlast any resolution of this specific case. In a world where AI capability is treated as a matter of national security, what does it mean to build products for a global market? And who, ultimately, decides when a model is too capable to be allowed to run?

---

*Access to Claude Fable 5 and Mythos 5 remains suspended as of publication. Anthropic has stated it is actively working with government officials to resolve the situation and restore access.*
