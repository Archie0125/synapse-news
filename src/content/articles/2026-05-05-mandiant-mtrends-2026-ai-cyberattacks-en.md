---
title: "2026 Is the Year AI Became the Hacker's Best Weapon — Mandiant's Annual Report Lays Out the Damage"
summary: "Google's Mandiant has released its M-Trends 2026 report, drawing on 450,000 hours of incident response work to document a threat landscape reshaped by AI. Attack handoff times have collapsed from eight hours in 2022 to just 22 seconds; 28.3% of CVEs are now exploited within 24 hours of disclosure; and AI-powered malware families are querying LLMs mid-execution to evade detection."
category: "ai-ml"
publishedAt: 2026-05-05
lang: "en"
featured: false
trending: false
sources:
  - name: "Google Cloud Blog"
    url: "https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026"
  - name: "SecurityWeek"
    url: "https://www.securityweek.com/m-trends-2026-initial-access-handoff-shrinks-from-hours-to-22-seconds/"
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html"
  - name: "Help Net Security"
    url: "https://www.helpnetsecurity.com/2026/03/24/mandiant-m-trends-2026-report/"
tags:
  - "cybersecurity"
  - "Mandiant"
  - "M-Trends"
  - "AI attacks"
  - "threat intelligence"
  - "CVE"
  - "zero-day"
relatedSlugs:
  - "2026-04-15-openai-gpt54-cyber-model-en"
  - "2026-05-02-anthropic-claude-security-enterprise-beta-en"
  - "2026-05-05-whitehouse-ai-model-prerelease-review-en"
---

There has never been a shortage of annual cybersecurity threat reports, but Google's Mandiant M-Trends series occupies a particular position: it is built entirely from real incident response data, not vendor surveys or threat modeling exercises. The M-Trends 2026 edition, drawing on more than 450,000 hours of Mandiant investigations worldwide, documents a threat landscape in which AI has moved from a theoretical force multiplier to a measurable operational reality for attackers — and not yet for defenders to the same degree.

The headline number that has circulated most widely since the report's release is 22 seconds — the current median time between initial network access being established and that access being handed off to a second-stage threat actor. In 2022, the equivalent figure was more than eight hours. In 2023, it had fallen to under two hours. The collapse is not gradual; it is exponential, driven by the industrialization of attack infrastructure and, increasingly, by AI tools that automate the steps between initial foothold and lateral movement.

## The Patch Gap Has Become Untenable

The 22-second handoff statistic captures how fast attacks move once they are inside a network. Equally alarming is the data on how fast attackers are getting inside in the first place.

M-Trends 2026 reports that 28.3 percent of disclosed CVEs are now exploited within 24 hours of their public disclosure — a number that has roughly doubled in two years. A meaningful fraction of exploits arrive before a patch exists at all: Mandiant classified a substantial portion of initial access techniques in 2025 investigations as zero-day exploits, meaning the vulnerability had no available fix at the time it was used.

The implications for enterprise security practice are brutal. The conventional wisdom of "patch within 30 days" — still embedded in many corporate security policy frameworks — is not a defense against 24-hour exploitation cycles. The organizations that avoided compromise in Mandiant's 2025 case work overwhelmingly had either (a) deployed compensating controls at the network layer that reduced exposure regardless of patch status, or (b) caught attacker activity in the initial access phase before lateral movement occurred — which requires detection tooling far faster than most SOCs currently operate.

## AI Is Now a Component of the Malware Stack

The most technically novel findings in M-Trends 2026 concern AI-native malware — code designed not merely to run on a victim's machine, but to actively leverage AI capabilities during execution.

Mandiant's research teams documented two malware families in particular. PROMPTFLUX is an information stealer that, during execution, constructs queries to external LLM APIs based on what it finds on the infected machine — dynamically adapting its data exfiltration strategy based on AI-assisted analysis of the victim's environment rather than following a hard-coded ruleset. PROMPTSTEAL operates similarly, using LLM calls to generate more convincing spear-phishing content for subsequent target expansion after an initial breach.

The use of external API calls to LLMs during malware execution represents an architectural shift: instead of encoding attack logic statically in the binary, threat actors are outsourcing reasoning to foundation models in real time. This makes malware substantially harder to detect with signature-based methods, since the "intelligence" is not present in the sample itself.

A third indicator in the report, QUIETVAULT, is a credential stealer that specifically checks infected machines for locally installed AI command-line tools — targeting the API keys and session tokens that developers commonly store in plaintext configuration files for Claude, GPT, and open-source model interfaces. The exploitation of AI developer toolchains as an attack surface is a direct consequence of the AI developer ecosystem expanding faster than security hygiene practices.

## Nation-State and Criminal Actors Converge on AI Tooling

M-Trends 2026 documents AI adoption across both nation-state threat groups and financially motivated criminal organizations, with the use cases diverging along predictable lines.

State-sponsored groups — particularly those attributed by Mandiant to China, Russia, and Iran — are using AI primarily in the reconnaissance and pre-intrusion phases: generating highly targeted spear-phishing content, synthesizing publicly available information about targets into operational intelligence profiles, and automating the identification of network perimeter vulnerabilities at scales that previously required large human analyst teams. The goal is reducing the human labor required for the early stages of long-duration espionage campaigns.

Financially motivated threat actors — ransomware groups, initial access brokers, and fraud organizations — are focusing AI use on two different problems: social engineering and evasion. On the social engineering side, the report documents a shift from mass email campaigns toward highly personalized rapport-building interactions conducted at scale by AI, with individual targets receiving months of low-intensity, seemingly legitimate contact before a malicious payload is delivered. On the evasion side, AI-assisted obfuscation tools are generating polymorphic code variants that defeat endpoint detection products trained on historical malware patterns.

## The Defender Asymmetry Problem

The most uncomfortable finding in M-Trends 2026 is the asymmetry: AI has improved attacker capabilities more dramatically than defender capabilities, at least as measured by actual incident outcome data. Mandiant's overall breach dwell time — the median duration between initial compromise and detection — has improved modestly over the past two years, from 16 days in 2023 to 11 days in 2025. But the attack-side improvements are larger in magnitude: faster handoffs, faster exploitation, and now AI-enhanced evasion.

The gap exists for structural reasons. Attackers are unconstrained optimizers — they can adopt any AI tool that improves their success rate without worrying about vendor relationships, procurement cycles, or regulatory approval for AI use in security systems. Defenders operate under institutional constraints: AI-based security products require vendor evaluation, legal review, and IT deployment cycles measured in months. By the time a defensive AI capability is widely deployed, the offensive community has iterated past it.

This is not a counsel of despair. Mandiant's report also documents organizations where AI-assisted detection and response has materially shortened the window between initial compromise and containment — some measured in hours rather than the 11-day median. But those organizations cluster in sectors with the resources and security maturity to move fast: financial services, defense contractors, and major cloud providers. The median enterprise is still fighting the last war.

## What Security Teams Should Do Now

The prescriptive section of M-Trends 2026 focuses on three operational priorities derived from the year's breach data.

First, privileged access management cannot wait. The majority of cases where an initial foothold became a catastrophic breach involved attackers obtaining privileged credentials within the first 24 hours. Zero-trust architecture and privileged access workstations for administrative functions are no longer aspirational; they are the structural difference between a contained incident and a ransomware deployment.

Second, detection must move to the access layer, not just the endpoint. Signature-based EDR cannot detect PROMPTFLUX-style AI-assisted malware by design. Behavioral monitoring of network traffic, identity activity, and API call patterns — the things that change when an attacker is operating, regardless of what code they are running — is where detection capability needs to grow.

Third, AI developer assets need to be treated as crown jewels. The QUIETVAULT finding reflects a broader attack surface that security teams have been slow to classify: every developer with LLM API keys in their home directory, every CI/CD pipeline with model API credentials, is a potential entry point for attackers seeking to abuse AI compute resources or pivot into adjacent systems. The AI security hygiene gap is 2026's version of the cloud credential hygiene gap that produced the major cloud breaches of 2019 to 2022.

The adversaries, as M-Trends 2026 makes clear, have already done this analysis.
