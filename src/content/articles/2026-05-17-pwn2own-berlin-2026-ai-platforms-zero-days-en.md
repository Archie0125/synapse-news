---
title: "Pwn2Own Berlin 2026: AI Platforms Join Windows and Edge as Prime Hacking Targets"
summary: "Security researchers earned over $900,000 for 39 unique zero-day vulnerabilities at Pwn2Own Berlin 2026, with AI orchestration tools like LiteLLM and the Cursor code editor making their debut as contest targets. The event sold out for the first time in its 19-year history, reflecting the explosion of interest in AI-system security research."
category: "developer-tools"
publishedAt: 2026-05-17
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

For 19 years, Pwn2Own has been the world's most prestigious hacking competition — a place where elite security researchers demonstrate previously unknown vulnerabilities in the most-hardened software on the planet. This year's Berlin edition added a category that would have seemed almost science fiction just two years ago: AI platforms.

The results were sobering.

By the end of a two-day event that ran from May 13–14, researchers had collectively earned $908,750 by demonstrating 39 unique zero-day vulnerabilities. Windows 11 fell three times. Microsoft Edge collapsed to a multi-bug sandbox escape worth $175,000. And LiteLLM — a popular open-source AI model routing framework used by enterprises to manage connections to models from OpenAI, Anthropic, and dozens of other providers — was fully compromised through a chained exploit that combined server-side request forgery with remote code injection.

For the first time in the contest's history, the organizers had to turn away over 150 researchers due to capacity limits. That enrollment overflow speaks volumes about where the security research community has focused its attention.

## The Day-One Headline: $523,000 and 24 Zero-Days

The first day alone set a record pace. Twenty-four unique vulnerabilities were demonstrated, earning researchers $523,000 — an average of nearly $22,000 per bug.

The most dramatic single performance came from Orange Tsai and the DEVCORE Research Team, who claimed $175,000 for a Microsoft Edge sandbox escape. Their attack chained four separate logic vulnerabilities — a technique that has become something of a signature for DEVCORE, which has historically excelled at identifying how individually mild-looking bugs can be combined into devastating exploit chains.

Windows 11 was the most-targeted platform on day one, compromised by three separate research teams demonstrating privilege escalation zero-days. Each earned $30,000 — the standard award for that class of vulnerability. The fact that three independent teams found distinct paths to the same privilege escalation class suggests the surface is broader than Microsoft's internal security teams had mapped.

Day two extended the carnage. Microsoft Exchange, historically a rich target for enterprise attack research, fell to a fresh zero-day. More notable for the AI industry: the Cursor code editor — one of the most widely adopted AI-native development environments with an estimated user base in the millions — was also compromised through a previously unknown vulnerability.

## The AI Security Wake-Up Call

The LiteLLM and Cursor exploits are the most strategically significant results of the event, even if their individual prize amounts were smaller than the Edge finding.

LiteLLM is infrastructure-level software. It sits between an enterprise's internal systems and the AI models those systems call, handling authentication, routing, rate limiting, and logging. A successful attack on LiteLLM doesn't just compromise one application — it can give an attacker access to every AI interaction flowing through an enterprise's deployment. The exploit demonstrated at Pwn2Own used SSRF to make LiteLLM issue requests to internal network services, then leveraged a code injection flaw to achieve full system takeover.

Cursor's compromise is a different category of concern. Code editors with AI features have access to an unusually sensitive slice of developer activity: they see source code, authentication tokens stored in config files, environment variables, and often have direct integration with cloud deployment pipelines. A zero-day in Cursor could theoretically be weaponized to silently exfiltrate proprietary code or inject malicious code into a software project without a developer noticing.

The Trend Micro Zero Day Initiative (ZDI), which organizes Pwn2Own, formally introduced AI platforms as a contest category this year following industry lobbying from enterprise security teams who argued that AI-specific tooling had matured to the point where its vulnerability surface deserved systematic research attention.

"AI ecosystems and core enterprise technologies are increasingly exposed to complex, chained attacks," ZDI noted in its event summary — language that has a very different weight when you consider that LiteLLM and similar frameworks are now embedded in the workflows of banks, law firms, healthcare systems, and government agencies.

## Why This Year Felt Different

Pwn2Own Berlin 2026 sold out. That has never happened before.

The overflow of researchers — more than 150 turned away after contest slots filled — reflects a structural shift in where the cybersecurity community sees opportunity and impact. AI tooling is new, rapidly deployed, often not subjected to the same rigorous security review as traditional enterprise software, and increasingly running with elevated access to sensitive systems.

Meanwhile, the traditional targets remain as vulnerable as ever. Windows 11, Edge, and Exchange have been hardened through years of attacker scrutiny and Microsoft's own extensive security investment. Yet they still fell on day one. That combination — a mature attack surface still yielding high-value bugs, plus a new AI-specific attack surface barely scrutinized at all — made this Berlin edition uniquely dense in consequential findings.

## The Enterprise Implications

The vulnerabilities demonstrated at Pwn2Own are responsibly disclosed. Vendors receive private notification and have a fixed window — typically 90 days — to patch before public disclosure. Microsoft, the LiteLLM maintainers, Anysphere (the company behind Cursor), and others affected have all been notified and are working on fixes.

But responsible disclosure doesn't mean the findings are irrelevant in the interim. Every zero-day demonstrated at Pwn2Own represents a class of vulnerability that independent threat actors may have already found and been quietly exploiting. The contest doesn't create the risk; it surfaces what was already there.

For enterprise security teams, the Berlin results come with several concrete action items. Deployments of LiteLLM and similar AI proxy frameworks should be reviewed for network segmentation and input validation controls. Code editors with AI integration should be subject to the same endpoint security scrutiny as other development tools. And the broader principle — that AI software needs to be treated as security-critical infrastructure rather than productivity software — needs to accelerate its way into procurement and governance processes.

The AI industry has spent the past three years arguing about model safety. Pwn2Own Berlin 2026 is a reminder that the stack below the model — the APIs, the proxies, the editors, the orchestration layers — deserves at least as much attention.
