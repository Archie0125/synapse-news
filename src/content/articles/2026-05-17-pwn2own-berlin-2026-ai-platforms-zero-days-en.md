---
title: "Pwn2Own Berlin 2026: AI Platforms Join Windows and Edge as Prime Hacking Targets"
summary: "Security researchers earned $908,750 for 39 unique zero-day vulnerabilities over the first two days of Pwn2Own Berlin 2026, with AI targets such as LiteLLM and Cursor among those exploited."
category: "developer-tools"
publishedAt: 2026-05-17
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "Security Affairs"
    url: "https://securityaffairs.com/192183/hacking/pwn2own-berlin-2026-day-one-523000-paid-out-ai-products-fall.html"
  - name: "Zero Day Initiative"
    url: "https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results"
  - name: "BleepingComputer"
    url: "https://www.bleepingcomputer.com/news/security/windows-11-and-microsoft-edge-hacked-on-first-day-of-pwn2own-berlin-2026/"
  - name: "CybersecurityNews"
    url: "https://cybersecuritynews.com/microsoft-exchange-windows-11-and-cursor-zero-days-exploited-pwn2own/"
tags:
  - "cybersecurity"
  - "Pwn2Own"
  - "zero-day"
  - "LiteLLM"
  - "Cursor"
  - "AI security"
  - "Windows 11"
  - "Microsoft Edge"
relatedSlugs:
  - "2026-04-05-anthropic-claude-code-source-leak-en"
  - "2026-05-13-anthropic-mythos-autonomous-exploit-en"
---

Pwn2Own is a hacking competition where security researchers demonstrate previously unknown vulnerabilities in fully patched software. This year's Berlin edition focused on enterprise technologies and artificial intelligence, with targets including AI databases, coding agents and local inference.

The results were sobering.

After the first two days of the event, with one day still remaining, researchers had collectively earned $908,750 by demonstrating 39 unique zero-day vulnerabilities. Windows 11 fell three times. Microsoft Edge collapsed to a multi-bug sandbox escape worth $175,000. And LiteLLM was fully compromised by k3vg3n, who chained three bugs including server-side request forgery and code injection.

That enrollment overflow speaks volumes about where the security research community has focused its attention.

## The Day-One Headline: $523,000 and 24 Zero-Days

Twenty-four unique vulnerabilities were demonstrated, earning researchers $523,000 — an average of nearly $22,000 per bug.

The most dramatic single performance came from Orange Tsai and the DEVCORE Research Team, who claimed $175,000 for a Microsoft Edge sandbox escape. Their attack chained four separate logic vulnerabilities.

Windows 11 was compromised three times on day one, by separate researchers demonstrating privilege escalation zero-days. Two sources report $30,000 for each of the three, though the Zero Day Initiative's own listing shows $30,000 for the first and $15,000 each for the other two. The fact that three independent teams found distinct paths to the same privilege escalation class suggests the surface is broader than Microsoft's internal security teams had mapped.

Day two extended the results. Microsoft Exchange, historically a rich target for enterprise attack research, fell to a fresh zero-day. More notable for the AI industry: the Cursor code editor was successfully exploited twice by different teams on day two.

## The AI Security Wake-Up Call

The LiteLLM and Cursor exploits are the most strategically significant results of the event, even if their individual prize amounts were smaller than the Edge finding.

LiteLLM is infrastructure-level software. A successful attack on LiteLLM doesn't just compromise one application — it can give an attacker access to every AI interaction flowing through an enterprise's deployment. The exploit demonstrated at Pwn2Own chained three bugs, including SSRF and code injection, to take down LiteLLM.

Cursor's compromise is a different category of concern. Code editors with AI features have access to an unusually sensitive slice of developer activity: they see source code, authentication tokens stored in config files, environment variables, and often have direct integration with cloud deployment pipelines. A zero-day in Cursor could theoretically be weaponized to silently exfiltrate proprietary code or inject malicious code into a software project without a developer noticing.

## Why This Year Felt Different

AI tooling is new, rapidly deployed, often not subjected to the same rigorous security review as traditional enterprise software, and increasingly running with elevated access to sensitive systems.

Meanwhile, the traditional targets remain as vulnerable as ever. Windows 11, Edge, and Exchange have been hardened through years of attacker scrutiny and Microsoft's own extensive security investment. Windows 11 and Edge fell on day one, and Exchange followed on day two. That combination — a mature attack surface still yielding high-value bugs, plus a new AI-specific attack surface barely scrutinized at all — made this Berlin edition uniquely dense in consequential findings.

## The Enterprise Implications

The vulnerabilities demonstrated at Pwn2Own are responsibly disclosed. Vendors receive private notification and have a fixed window — typically 90 days — to patch before public disclosure. Vendors have 90 days to release fixes for the zero-days demonstrated at the contest.

But responsible disclosure doesn't mean the findings are irrelevant in the interim. Every zero-day demonstrated at Pwn2Own represents a class of vulnerability that independent threat actors may have already found and been quietly exploiting. The contest doesn't create the risk; it surfaces what was already there.

For enterprise security teams, the Berlin results come with several concrete action items. Deployments of LiteLLM and similar AI proxy frameworks should be reviewed for network segmentation and input validation controls. Code editors with AI integration should be subject to the same endpoint security scrutiny as other development tools. And the broader principle — that AI software needs to be treated as security-critical infrastructure rather than productivity software — needs to accelerate its way into procurement and governance processes.

The AI industry has spent the past three years arguing about model safety. Pwn2Own Berlin 2026 is a reminder that the stack below the model — the APIs, the proxies, the editors, the orchestration layers — deserves at least as much attention.

*Correction (November 15, 2026): 21 sentences were corrected or removed to match the sources listed on this page.*
