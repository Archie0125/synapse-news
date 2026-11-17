---
title: "US Government Orders Anthropic to Cut Off Foreign Nationals from Fable 5 — Anthropic Complies, Pushes Back"
summary: "The US government issued an export control directive ordering Anthropic to suspend access to Fable 5 and Mythos 5 for all foreign nationals. Anthropic disabled both models for all customers to ensure compliance, while publicly disagreeing with the decision."
category: "policy"
publishedAt: 2026-06-29
modifiedAt: 2026-11-15T00:00:00Z
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

At 5:21 PM Eastern Time on June 12, 2026, Anthropic received a letter from the US government. The directive, citing national security authorities, ordered the company to suspend all access to Fable 5 and Mythos 5 for any foreign national, whether inside or outside the United States, including foreign national Anthropic employees.

By the time most of the world woke up on June 13, both of Anthropic's most capable models were dark.

## The Directive and the Jailbreak

The letter did not provide specific details of the government's national security concern, but Anthropic understood it to center on a reported jailbreak. According to Anthropic, its understanding is that the government believes it became aware of a method of bypassing, or "jailbreaking," Fable 5. Cybersecurity Dive reported that the directive came after Amazon researchers were reportedly able to circumvent some of Fable 5's guardrails.

The specific technique was, by Anthropic's own description, strikingly mundane: asking the model "to read a specific codebase and fix any software flaws." When invoked in a particular sequence, this apparently prompted Fable 5 to surface vulnerability information that its safety filters were designed to suppress.

Anthropic engineers reviewed the technique and reached a different conclusion than the government did. They characterized it as a "narrow, non-universal jailbreak" that exposed "a small number of previously known, minor vulnerabilities." More pointedly, the company said the level of capability displayed is widely available from other models, including OpenAI's GPT-5.5.

"We disagree that the finding of a narrow potential jailbreak should be cause for recalling a commercial model deployed to hundreds of millions of people," Anthropic wrote in its public statement.

## Why Global Shutdown, Not Just Geofencing

The specific mechanism of the directive created an unusual compliance problem. Restricting access to "all foreign nationals" sounds like a geofencing challenge — block IP addresses from other countries — but the legal reality was more complex.

Verifying whether a user inside the United States is a foreign national is not something Anthropic's systems were designed to do. Without robust, real-time citizenship verification across its entire user base — a technical and privacy minefield — the only legally defensible interpretation of the directive was to shut down Fable 5 and Mythos 5 for all customers globally.

Access to all other Anthropic models, including Opus 4.8, was not affected. But Fable 5, which had been released just that week, was disabled for all customers.

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

*Access to Claude Fable 5 and Mythos 5 remains suspended as of publication. Anthropic has said it is working to restore access as soon as possible.*

*Correction (November 15, 2026): 10 sentences were corrected or removed to match the sources listed on this page.*
