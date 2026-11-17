---
title: "Anthropic's 'Claude Mythos' Leaked: The Most Powerful AI Model Yet — and a Cybersecurity Threat"
summary: "A CMS misconfiguration exposed Anthropic's secret model codenamed 'Mythos', positioned above Opus in a new 'Capybara' tier. The company is now privately briefing US officials about its unprecedented cybersecurity risks while conducting limited early access testing."
category: "ai-ml"
publishedAt: 2026-04-05T09:05:00Z
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: true
trending: false
sources:
  - name: "Fortune"
    url: "https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/"
  - name: "Axios"
    url: "https://www.axios.com/2026/03/29/claude-mythos-anthropic-cyberattack-ai-agents"
  - name: "Dataconomy"
    url: "https://dataconomy.com/2026/04/02/anthropic-tests-claude-mythos-as-its-most-powerful-ai-model/"
tags:
  - "Anthropic"
  - "Claude Mythos"
  - "AI safety"
  - "cybersecurity"
  - "foundation models"
  - "AI agents"
relatedSlugs:
  - "2026-04-05-openai-gpt4o-retirement-en"
  - "2026-04-04-openai-gpt5-leak-en"
---

A configuration error at Anthropic's content management system inadvertently revealed something the company had been keeping under wraps: a new AI model of unprecedented capability, codenamed "Mythos." The accidental exposure, which left close to 3,000 previously unpublished assets linked to Anthropic's blog publicly accessible, led the company to confirm that it is developing and testing the new model.

## The Leak That Wasn't Supposed to Happen

The CMS misconfiguration left a cache of unpublished material publicly accessible, including a draft blog post about the new model and a PDF about an invite-only CEO retreat. Among those materials was evidence of a model operating in a product tier codenamed "Capybara" — positioned above the company's current flagship Claude Opus 4.6 in the product hierarchy.

Anthropic moved quickly to contain the exposure, but security researchers and journalists had already captured enough to piece together a picture of what Mythos is — and what it's capable of. After Fortune reported on the leak, Anthropic confirmed it is developing and testing the model, calling it "a step change" and "the most capable we've built to date." A leaked draft blog post had described it as "by far the most powerful AI model we've ever developed."

That's a notable statement from a company whose Opus 4.6 already sits at or near the top of most independent AI benchmarks. But Mythos, according to Anthropic, doesn't just incrementally advance the state of the art: a spokesperson called it "a step change."

## Dramatically Superior Benchmarks

The leaked data shows Mythos dramatically outperforming Claude Opus 4.6 across three core domains: coding, academic reasoning, and cybersecurity. On SWE-bench Verified — the gold standard for autonomous software engineering capability — Mythos reportedly scores significantly above any currently released model. On advanced academic benchmarks like GPQA Diamond and AIME 2025, the performance gaps are described as "substantial" in internal materials.

But it's the cybersecurity benchmarks that have attracted the most attention, and the most concern.

Mythos is described as capable of identifying and exploiting vulnerabilities at a scale that "far outpaces the efforts of defenders." In internal red-teaming exercises, the model demonstrated the ability to autonomously chain multiple steps of a cyberattack — reconnaissance, vulnerability identification, exploitation, and lateral movement — without requiring human prompting at each stage.

This reflects Mythos's core design philosophy: it is an agentic model by default, built to plan and execute multi-step task sequences end-to-end. Where Claude Opus 4.6 benefits from agentic scaffolding but was fundamentally designed as a conversational assistant, Mythos is architected from the ground up to operate autonomously across extended task horizons.

## Briefing Washington Before Launch

What makes the Mythos situation unusual — even by frontier AI standards — is the step Anthropic took before announcing general availability or even a release date: private briefings with senior US government officials.

According to reporting from Axios, Anthropic has been quietly briefing officials in the intelligence community and relevant congressional committees about Mythos's potential for offensive cybersecurity applications. The company is framing this proactively, positioning itself as a responsible actor flagging dual-use risks before the model reaches broad deployment.

It's a playbook that reflects Anthropic's safety-first brand positioning, but also the genuine unease that senior staff reportedly feel about releasing a model with these capabilities into a world where adversarial actors — state-sponsored and otherwise — are actively looking for AI-powered offensive tools.

The briefings also carry a practical dimension: Anthropic is reportedly interested in positioning Mythos for classified government work, particularly in cyber defense applications. The company already has existing relationships with DARPA and the intelligence community through its broader research partnerships.

## Cybersecurity Partners Get First Access

Rather than a broad public launch, Anthropic is currently working with a small group of early access customers to test Mythos, with a release plan the draft blog said would focus on cyber defenders. This group includes a small number of vetted organizations working on defensive AI applications — intrusion detection, vulnerability assessment, threat intelligence — where Mythos's capabilities can be applied in controlled, monitored environments.

This approach mirrors how OpenAI handled its own most sensitive model releases, creating tiered access structures that allow the company to gather real-world capability data while limiting exposure of the most dangerous capabilities to vetted actors.

Notably, no general release date has been announced. This is itself unusual: Anthropic typically pre-announces model releases with some lead time to prepare the developer ecosystem. The absence of a public timeline for Mythos suggests either that safety testing is still ongoing, or that the company is navigating a more complex policy and legal landscape than it has for previous releases.

## A New Pricing Tier and the Economics of Frontier AI

According to the leaked draft blog post, Capybara is a new tier of model larger than Opus, and Capybara and Mythos appear to refer to the same underlying model. The draft blog described Capybara as more expensive than Opus.

The business logic is clear: as the gap between frontier AI and the open-source alternatives continues to widen on the most demanding tasks, the willingness of enterprise customers to pay premium prices for genuine capability advantages grows as well. Mythos appears designed to be the offering that justifies a price point that no current AI product can claim.

This also has implications for Anthropic's competitive posture. The company has been in an uncomfortable position in early 2026 — Claude Opus 4.6 remains highly regarded, but Google's Gemini 3.1 Pro has been leading on many benchmarks, and OpenAI's GPT-5.x series has successfully completed its transition away from GPT-4o. Mythos, if it performs as internal data suggests, would re-establish Anthropic at the technical frontier in a way that changes the competitive calculus for the entire industry.

## The Dual-Use Problem at Unprecedented Scale

The deeper issue that Mythos raises — one that industry observers are beginning to grapple with — is what it means for the safety and policy ecosystem when a model is powerful enough that its offense-defense balance tips meaningfully toward offense.

Previous AI capabilities — coding assistants, image generation, even earlier agentic systems — presented manageable dual-use concerns. Regulatory and industry frameworks developed quickly enough to keep pace. Mythos, as described in the leaked materials, is different in degree to a point where it might be different in kind.

An AI system that can autonomously chain cyberattack steps at scale doesn't just make individual bad actors more effective — it potentially changes the economics of state-sponsored cyber operations, lowers the bar for sophisticated attacks to a level where much smaller actors can mount them, and creates novel attack surfaces that existing detection systems weren't designed to identify.

Anthropic's decision to brief government officials before launch is recognition of this reality. The question the broader industry is now asking is whether that recognition is enough — or whether Mythos represents the moment when AI capabilities require a fundamentally different governance framework than we currently have.

For now, Anthropic is proceeding carefully. But the existence of Mythos — however accidentally revealed — means that a new threshold in AI capability has already been crossed, whether or not the model is yet in anyone's hands.

*Correction (November 15, 2026): 7 sentences were corrected or removed to match the sources listed on this page.*
