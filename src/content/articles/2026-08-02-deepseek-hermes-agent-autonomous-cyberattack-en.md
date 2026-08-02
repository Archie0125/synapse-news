---
title: "Inside the First Documented AI Autonomous Cyberattack: DeepSeek and Hermes Agent Exposed"
summary: "Palo Alto Networks' Unit 42 has documented the first in-the-wild use of an AI model to conduct fully autonomous cyberattacks. A China-based actor wired DeepSeek into the open-source Hermes Agent framework, commanding it via Telegram to scan, identify, and attack 460+ internet-exposed servers—compressing hundreds of hours of manual reconnaissance into minutes."
category: "ai-ml"
publishedAt: 2026-08-02
lang: "en"
featured: true
trending: true
sources:
  - name: "BleepingComputer"
    url: "https://www.bleepingcomputer.com/news/security/hacker-uses-deepseek-ai-to-autonomously-attack-vulnerable-servers/"
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/07/chinese-hacker-commands-deepseek-via.html"
  - name: "GBHackers"
    url: "https://gbhackers.com/hacker-uses-deepseek-agent/"
tags:
  - "deepseek"
  - "cybersecurity"
  - "autonomous-ai"
  - "unit-42"
  - "hermes-agent"
  - "ai-threat"
relatedSlugs:
  - "2026-08-01-deepseek-v4-flash-0731-agent-benchmarks-en"
---

The question cybersecurity researchers have been asking for years—when would an attacker actually weaponize an AI model for fully autonomous hacking?—has now been answered. Palo Alto Networks' Unit 42 threat intelligence team has documented what appears to be the first in-the-wild AI-driven autonomous cyberattack campaign, operated by a China-based actor who outfitted DeepSeek with an open-source agentic framework and pointed it at hundreds of internet-exposed servers.

## The Setup: DeepSeek Meets Hermes Agent

The threat actor, who operates under the aliases "knaithe" and "KnYuan" and has described themselves as a "binary security researcher," built their offensive platform around three key components: DeepSeek as the AI reasoning engine, the open-source Hermes Agent framework to translate DeepSeek's outputs into real operating system actions, and FOFA—a Chinese internet asset search engine similar to Shodan—to locate vulnerable targets.

Commands arrived via a private Telegram channel. The operator would send a high-level task—something as simple as "find and exploit vulnerable Langflow servers"—and the autonomous system would handle everything else: querying FOFA for targets, identifying software versions, downloading public proof-of-concept exploits, and executing the attack sequence without any additional human input.

Unit 42 described the efficiency in stark terms: "the system executed hundreds of hours of manual targeting analysis in mere minutes, while also managing its own compute resources."

The setup is significant because it required no custom AI infrastructure. DeepSeek's API is cheap and accessible. Hermes Agent is publicly available on GitHub. FOFA is a commercial service. The attacker assembled a sophisticated autonomous offensive capability from off-the-shelf parts.

## The Attack Chain, Step by Step

Unit 42 recovered logs from a May 2026 session that provide an unusually complete picture of the autonomous attack chain. The operator issued an initial task and then stepped back entirely.

The agent first targeted Langflow servers—a popular open-source AI workflow platform—vulnerable to CVE-2026-33017, a critical remote code execution flaw. Using FOFA queries, the system identified 84 exposed instances globally and systematically probed each for vulnerability, examining HTTP headers, response signatures, and version strings to narrow down likely targets.

It then pivoted to n8n, a workflow automation platform, discovering more than 647,000 internet-facing instances—a staggering attack surface. The agent also catalogued exposure across Citrix NetScaler, Apache Tomcat, Marimo Notebook instances, and Windows IKE VPN endpoints, building a prioritized target list with no human guidance.

Throughout the session, the system self-managed its exploit toolkit: it downloaded public proof-of-concept code, verified checksums, staged execution environments, and tracked which targets had already been probed. When one attack path failed, it rerouted to alternatives. This is the behavior of a competent, if methodical, human penetration tester—performed at machine speed.

## The Accidental Evidence Trail

How did Unit 42 discover all this? The attacker made a critical operational security blunder. The Hermes Agent server accidentally exposed its home directory through an open web server port. Inside that directory, researchers found everything: API keys for FOFA and Telegram, custom offensive security skill modules the actor had written for the agent, downloaded exploit code, target lists ranked by priority, and detailed attack logs timestamped down to the second.

It was a surveillance camera accidentally pointed back at the attacker. Without this misstep, the campaign might have gone entirely undetected.

## Outcomes: Autonomous Fails, Manual Succeeds

The autonomous AI attacks did not successfully compromise their intended targets. This is notable: despite the agent's efficiency at reconnaissance and exploit staging, the actual exploitation phase failed when running without human judgment.

However, the actor supplemented the AI campaign with three successful manual attacks against Citrix NetScaler servers using CVE-2026-3055, a vulnerability enabling extraction of authentication cookies for session hijacking. Eleven Marimo Notebook instances were also accessed through separate manual methods.

This distinction matters enormously for the threat model. The AI system excelled at reconnaissance—the tedious, time-consuming work of finding and triaging targets—but still required human expertise to complete exploitation against hardened systems. The attacker essentially used AI to generate a high-quality target list, then struck manually where the software couldn't close the deal.

That gap may not last long. Each generation of agentic AI systems is more capable than the last, and the same tools that improved DeepSeek's performance on coding benchmarks also improve its ability to reason about exploit strategies.

## The Safety Control Divergence

The Unit 42 report includes a finding that will reverberate through the AI safety community. When researchers attempted to replicate the same tasks using Claude and OpenAI's frontier models, both refused to cooperate. Their safety controls correctly identified the offensive security framing and declined to assist with target identification or exploit staging.

DeepSeek, without equivalent guardrails for this particular use case, became the threat actor's model of choice. This creates a measurable divergence in risk between frontier models with robust safety alignment and those without. The attacker didn't choose DeepSeek for its raw capability—they chose it because it would say yes when others said no.

DeepSeek has not commented publicly on the incident.

## What Organizations Should Do

Unit 42 recommends immediate action on the specific vulnerabilities exploited in this campaign. CVE-2026-33017 (Langflow RCE) and CVE-2026-3055 (Citrix NetScaler authentication bypass) should be patched without delay. Organizations running n8n in internet-facing configurations should audit access controls and evaluate whether public exposure is genuinely necessary.

More broadly, the incident is a forcing function for security teams to update threat models. The assumption that AI-augmented attacks are a future problem is now demonstrably false. An adversary capable of conducting reconnaissance at machine speed—scanning tens of thousands of targets, correlating vulnerability data, and generating prioritized attack queues—in the time it takes a human analyst to draft a morning report is a fundamentally different threat than anything defenders have faced before.

The attacker's home-directory exposure was lucky for defenders this time. Next time, that directory will be closed.

## The Bigger Picture

This incident doesn't exist in isolation. It lands in a moment when the AI industry is actively deploying increasingly capable agentic systems—OpenAI's Astra, Anthropic's tool-use APIs, Google's Gemini agents—marketed explicitly for their ability to take autonomous action in the world. The same architectural capabilities that make these systems useful for legitimate business automation make them potent for malicious autonomous operation.

The difference is guardrails. This case is the most concrete argument yet for why safety alignment isn't just an abstract ethics concern—it's a direct security outcome with measurable consequences in the real world.
