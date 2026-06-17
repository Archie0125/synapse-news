---
title: "Anthropic's AI Finds 10,000+ Critical Bugs — and Now It's Coming for Power Grids and Hospitals"
summary: "Anthropic has expanded Project Glasswing — its Claude Mythos-powered vulnerability scanning initiative — to approximately 150 new organizations across more than 15 countries, adding power grids, hospitals, water systems, and telecoms operators for the first time. Since launching in April, the program has identified over 10,000 high- or critical-severity security flaws across millions of lines of code, with a confirmation rate exceeding 90%."
category: "developer-tools"
publishedAt: 2026-06-17
lang: "en"
featured: false
trending: true
sources:
  - name: "CyberScoop"
    url: "https://cyberscoop.com/anthropic-project-glasswing-expansion-critical-infrastructure-claude-mythos/"
  - name: "Help Net Security"
    url: "https://www.helpnetsecurity.com/2026/06/03/anthropic-project-glasswing-expansion/"
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html"
  - name: "Anthropic"
    url: "https://www.anthropic.com/news/expanding-project-glasswing"
tags:
  - "Anthropic"
  - "Project Glasswing"
  - "cybersecurity"
  - "Claude Mythos"
  - "vulnerability scanning"
  - "critical infrastructure"
  - "open source security"
relatedSlugs:
  - "2026-06-16-anthropic-when-ai-builds-itself-recursive-self-improvement-en"
  - "2026-06-13-trump-anthropic-fable5-mythos-export-controls-en"
---

When Anthropic launched Project Glasswing in April 2026, the pitch was simple and audacious: give the world's most powerful AI model access to the code underpinning critical global software infrastructure, and see how many vulnerabilities it could find before attackers did.

The answer, after roughly six weeks of operation with an initial cohort of about 50 partner organizations, was: a lot. More than 10,000 high- or critical-severity vulnerabilities, with a validation rate exceeding 90% — meaning the vast majority of findings turned out to be real, exploitable bugs rather than false positives. One of the most significant was CVE-2026-5194, a critical WolfSSL flaw (CVSS 9.1) that would have allowed attackers to forge certificates and impersonate trusted services across systems that depend on the widely-used cryptography library.

Now Anthropic is scaling up. On June 2, the company announced it was extending Project Glasswing to approximately 150 new organizations across more than 15 countries — more than tripling the program's reach — with a deliberate expansion into sectors the initial cohort had not covered.

## What Changed in Phase Two

The first wave of Glasswing partners was dominated by established technology companies: Amazon Web Services, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks, among others. These are organizations with mature security practices, large internal engineering teams, and the infrastructure to process and triage AI-generated findings at scale.

Phase two deliberately targets organizations that are harder to secure but potentially more catastrophic when breached. New sectors added include power and energy utilities, water treatment and distribution systems, healthcare providers and hospital networks, and telecommunications infrastructure. Many of the new participants are vendors: companies whose software runs inside critical infrastructure systems rather than operating the infrastructure directly — making them high-value attack targets with potentially lower security maturity than the organizations they serve.

Anthropic's framing for why these organizations were prioritized is explicit in its announcement: "For most of them, a major breach could affect more than 100 million people."

The expansion also notably includes NetSkope and Rubrik — cloud security and data management specialists — which Anthropic said are participating to help validate findings and develop remediation workflows appropriate for the new sectors.

## The Bottleneck Isn't Finding Bugs. It's Fixing Them.

One of the more counterintuitive insights to emerge from Phase One of Glasswing is that AI-powered vulnerability discovery has progressed further and faster than anyone expected — but it has also revealed a structural bottleneck that AI cannot yet solve.

Cloudflare found 400 critical and high-severity bugs among 2,000 total findings. Mozilla found 271 vulnerabilities in Firefox 150 alone. An open-source scan across more than 1,000 projects flagged 23,019 potential issues, of which 6,202 were classified as high- or critical-severity with 1,726 confirmed as valid true positives.

These are extraordinary numbers. They also create a new problem: the pipeline of confirmed vulnerabilities is generating more remediation work than engineering teams can absorb. As Anthropic noted in its expansion announcement, "The bottleneck in fixing bugs like these is the human capacity to triage, report, and design and deploy patches for them."

This is what the company describes as the deeper challenge of the program: not the discovery phase, but the response phase. Even with AI doing the detection, patching critical vulnerabilities in widely-deployed, production software requires human judgment, careful testing, and coordination with the open-source maintainers or enterprise vendors who own the affected code. That process cannot be automated away — yet.

Anthropic says that Claude Security, using the publicly available Claude Opus 4.8 model (not the restricted Mythos variant), has already helped patch more than 2,100 vulnerabilities in three weeks. The distinction is deliberate: Claude Mythos Preview is kept restricted specifically because of dual-use concerns — the same capabilities that make it exceptional at finding security flaws would also make it exceptionally useful for creating exploits.

## The Architecture of Controlled Access

Project Glasswing represents a genuine experiment in responsible deployment of a capability-threshold AI model. Claude Mythos was not publicly released when it crossed what Anthropic describes as a critical capability threshold for cybersecurity offense. Instead, Anthropic chose a restricted-access model: partner organizations get API access under specific use-case constraints, and Anthropic maintains oversight of how the model is being used.

The expansion to 150 organizations makes that oversight challenge significantly harder. Fifteen-plus countries means multiple regulatory jurisdictions, varying disclosure norms, and different legal frameworks around responsible vulnerability disclosure. A critical finding in a U.S.-regulated hospital system has different reporting requirements than the same finding in a German energy utility or a South Korean telecommunications provider.

Anthropic says it is managing this through what it calls a "structural advantage for defenders over attackers" framework: the goal is not simply to find vulnerabilities, but to ensure that the time advantage for defenders — their ability to patch before attackers weaponize a finding — is permanently widened. That requires treating disclosure coordination as a core program function, not an afterthought.

## A Preview of the AI-Security Relationship

The broader significance of Project Glasswing extends beyond the vulnerability counts. It represents the first large-scale test of a model that has crossed a cybersecurity capability threshold — and a template for how the AI industry might handle future capability milestones.

The implicit argument Anthropic is making is that the right response to building a model powerful enough to cause serious harm in the wrong hands is not to delay deployment or embargo the model entirely, but to deploy it under controlled conditions for defensive purposes, at scale, before adversarial actors can develop equivalent capabilities themselves.

Whether that framework holds at the next capability threshold — whenever models become capable of autonomous, end-to-end exploit development without human guidance — is a question the security community is watching closely. For now, Glasswing offers something that has been largely absent from AI safety debates: empirical evidence of what AI-powered security defense actually looks like in production.

The evidence so far suggests that the defenders are winning, at least in this phase. The race is still very much on.
