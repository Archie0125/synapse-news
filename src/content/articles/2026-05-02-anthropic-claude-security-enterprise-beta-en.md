---
title: "Anthropic Launches Claude Security in Public Beta, Partnered with CrowdStrike and Five Cybersecurity Giants"
summary: "Anthropic has opened Claude Security to public beta for enterprise customers — an AI-powered tool that reasons over entire codebases to find vulnerabilities and auto-generate patches. Backed by six major security platform partners including CrowdStrike and Palo Alto Networks, the launch signals Anthropic's entry into a market where AI-generated code is now creating an unprecedented wave of exploitable flaws."
category: "products"
publishedAt: 2026-05-02
lang: "en"
featured: true
trending: true
sources:
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/04/30/anthropic-announces-claude-security-public-beta-find-fix-software-vulnerabilities/"
  - name: "Business Standard"
    url: "https://www.business-standard.com/technology/tech-news/anthropic-announces-claude-security-beta-for-enterprise-customers-126050100019_1.html"
  - name: "SecurityWeek"
    url: "https://www.securityweek.com/anthropic-unveils-claude-security-to-counter-ai-powered-exploit-surge/"
  - name: "CrowdStrike"
    url: "https://www.crowdstrike.com/en-us/press-releases/crowdstrike-puts-claude-opus-4-7-to-work-across-falcon-platform-project-quiltworks/"
tags:
  - "anthropic"
  - "claude"
  - "cybersecurity"
  - "enterprise"
  - "vulnerabilities"
  - "ai-security"
relatedSlugs:
  - "2026-04-24-anthropic-19b-arr-claude-code-growth-en"
  - "2026-04-17-claude-opus-47-release-en"
  - "2026-04-12-anthropic-mythos-cybersecurity-model-en"
---

For months, security researchers have been sounding the same alarm: AI coding assistants are shipping code faster than human reviewers can audit it, and the result is a growing backlog of vulnerabilities baked directly into production systems. On April 30, Anthropic made its answer to that problem official. Claude Security is now available in public beta to Claude Enterprise customers — and the company arrived with an impressive roster of partners in tow.

## From Research Preview to Enterprise Product

Claude Security isn't entirely new. Anthropic first released the capability in February 2026 under the name Claude Code Security, initially as a limited research preview accessible to a narrow group of enterprise developers. The public beta represents a meaningful expansion: any organization on a Claude Enterprise plan can now apply for access, and Anthropic says it will roll the product out broadly over the coming weeks.

The core pitch is straightforward. Claude Security is designed to find what traditional static analysis tools miss. Where conventional scanners pattern-match against known vulnerability signatures — looking for SQL injection templates, buffer overflow patterns, or known CVEs — Claude Security reasons over the full codebase the way a senior security engineer would. It traces data flows across file boundaries, examines how components interact at runtime, and synthesizes a holistic picture of how an attacker might chain together otherwise low-severity issues into a critical exploit path.

Before any finding reaches an analyst's dashboard, the model assigns a confidence rating, effectively self-auditing its own reasoning. Anthropic says this filtering step is what makes the system practical at enterprise scale: the goal is a tool that security teams will actually trust, not one that floods queues with noise.

## Six Partners at Launch — Including CrowdStrike's New Coalition

The partner announcement is arguably the most strategically significant aspect of the launch. Anthropic has signed integrations with CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, TrendAI, and Wiz. Each is embedding Claude Opus 4.7 — Anthropic's flagship model — directly into their existing security platforms.

The CrowdStrike relationship goes beyond a standard integration. Alongside the Claude Security announcement, CrowdStrike unveiled Project QuiltWorks, an industry-wide coalition it is convening to tackle what the company calls the "AI vulnerability surge." The coalition draws on frontier models from both Anthropic and OpenAI, and its stated mission is to build shared tooling and practices for continuously discovering and remediating the vulnerabilities that AI-generated code is now producing at scale.

The framing matters. CrowdStrike is not merely adding a new feature to Falcon — it is positioning itself at the center of a new sub-industry, one that exists entirely because AI coding tools have changed the economics of software production. CrowdStrike CEO George Kurtz called AI-generated code "the single largest expansion of the enterprise attack surface in a decade," a direct acknowledgment that the very tools enterprises are adopting to write software faster are simultaneously creating security debt faster than traditional methods can retire it.

## The Market Problem Claude Security Is Designed to Solve

Understanding why Anthropic is launching this product now requires a look at the broader security landscape of mid-2026. According to data cited by Anthropic, the volume of newly discovered vulnerabilities in AI-assisted codebases has grown roughly three times faster over the past 18 months than in the preceding three years. Security teams have not grown proportionally.

The proximate cause is obvious: when a developer can go from a rough prompt to a working pull request in minutes, the rate of new code entering a codebase accelerates dramatically. What's less obvious is that AI-generated code tends to fail in different ways than human-written code. It frequently produces plausible-looking, syntactically valid code that compiles cleanly and passes basic tests, but carries subtle logic errors — incorrect assumptions about authentication state, improperly validated trust boundaries, or race conditions in concurrent operations — that only manifest under specific conditions or at scale.

Standard static analysis tools were trained, both figuratively and literally, on the patterns of human programmers. They are poorly calibrated for this new category of flaw. Claude Security's bet is that a large language model reasoning contextually over an entire repository is better positioned to catch these "AI-native" vulnerabilities than pattern-based scanners.

## Pricing and Access

Anthropic has not released granular pricing details beyond confirming that Claude Security is available to existing Claude Enterprise subscribers. The company appears to be positioning it as an add-on capability rather than a standalone product, which makes sense given that many of the partner integrations (CrowdStrike Falcon, Wiz Cloud Security, Microsoft Defender) are themselves priced per seat or per workload on enterprise contracts.

For security-focused teams already on the Claude Enterprise plan, the path to access is an application form that Anthropic says it will process on a rolling basis throughout May.

## Anthropic's Expanding Enterprise Surface

The Claude Security launch is the latest signal that Anthropic is deliberately broadening its enterprise footprint beyond its origins as a model provider. Over the past six months, the company has launched Claude for Word (integrating into Microsoft Office workflows), Claude Code for developer tooling, and now Claude Security for the security operations center. Each product addresses a distinct professional workflow, and each has been accompanied by partnerships that embed Anthropic's models within platforms its customers are already paying for.

That distribution strategy reflects a hard lesson from the enterprise software market: organizations rarely abandon their existing tool stacks. Winning in the enterprise means showing up inside the tools that already have budget allocations and organizational buy-in — which is precisely what the CrowdStrike, Palo Alto, and Wiz partnerships deliver.

## What Comes Next

With Anthropic's annualized revenue approaching $19 billion as of late April 2026, the company has the runway to build out a full enterprise product suite at a measured pace. Claude Security joins a portfolio that is increasingly difficult to characterize as "just an AI model company."

The deeper question is whether AI-powered security tools will keep pace with AI-powered threats. CrowdStrike's Project QuiltWorks implicitly acknowledges that this is now an arms race: the same models that help developers write code faster also help attackers find and exploit the vulnerabilities that code contains. Claude Security, at its core, is Anthropic's bid to be on the right side of that race.

For enterprises currently grappling with the security implications of their own AI-assisted development workflows, the public beta landing at this moment is something between a relief and a recognition of just how quickly the ground has shifted.
