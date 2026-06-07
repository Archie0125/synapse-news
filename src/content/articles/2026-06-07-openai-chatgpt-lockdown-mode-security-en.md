---
title: "OpenAI Rolls Out ChatGPT Lockdown Mode to Defend Against Prompt Injection Attacks"
summary: "OpenAI has begun rolling out Lockdown Mode to all personal and self-serve business ChatGPT accounts, cutting off live web browsing, agent actions, and file downloads to prevent prompt-injection-driven data exfiltration. The feature marks a meaningful step in making AI assistants safer for high-stakes environments, though OpenAI acknowledges residual risks remain."
category: "ai-ml"
publishedAt: 2026-06-07
lang: "en"
featured: false
trending: true
sources:
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html"
  - name: "OpenAI"
    url: "https://openai.com/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/"
  - name: "BetaNews"
    url: "https://betanews.com/article/lockdown-mode-is-rolling-out-to-all-chatgpt-accounts/"
tags:
  - "openai"
  - "chatgpt"
  - "security"
  - "prompt-injection"
  - "AI-safety"
  - "enterprise"
relatedSlugs:
  - "2026-06-05-openai-dreaming-v3-chatgpt-memory-en"
  - "2026-06-04-openai-codex-sites-role-plugins-enterprise-en"
  - "2026-06-05-openai-chatgpt-ads-self-serve-cpc-en"
---

For all the capabilities packed into ChatGPT, one of its most persistent vulnerabilities has been the prompt injection attack: an adversary embeds malicious instructions inside a document, email, or website that ChatGPT reads, and those instructions hijack the model's behavior—sometimes causing it to leak sensitive data to attacker-controlled servers. As ChatGPT has grown into an enterprise tool and agentic workflows have multiplied the attack surface, OpenAI has faced mounting pressure to address this class of threat at the platform level.

The company's answer, now rolling out broadly, is **Lockdown Mode**: an optional security setting that surgically removes the outbound network pathways prompt-injection attacks most commonly exploit. The feature, initially piloted in February for a limited group of high-security users, is now available to all personal accounts—Free, Go, Plus, and Pro—as well as self-serve ChatGPT Business subscribers.

## What Lockdown Mode Does (and Doesn't Do)

The design philosophy is precise and intentionally narrow. Lockdown Mode does not try to prevent prompt injections from entering the model's context window in the first place—that remains an unsolved problem in AI security. Instead, it targets the final mile of a successful attack: the moment an attacker's embedded instruction attempts to exfiltrate data by making an outbound network request.

To accomplish this, Lockdown Mode disables or heavily restricts a set of ChatGPT features that require external connectivity:

- **Live web browsing**: real-time web access is blocked; the model can only draw on its training data and cached content
- **Deep Research**: the multi-step research feature that browses and synthesizes live sources is disabled
- **Agent Mode**: autonomous task-completion workflows that interact with external services are turned off
- **Canvas networking**: the collaborative document feature's network integrations are cut
- **File downloads**: ChatGPT cannot send files to external destinations
- **Image support**: some web-derived image retrieval features are restricted

What remains is a capable text-in, text-out assistant with access to uploaded files and documents—powerful for analysis, drafting, and reasoning, but isolated from the web in ways that meaningfully shrink the exfiltration surface.

Enabling the feature is straightforward: navigate to **Settings → Security → Advanced Security → Lockdown Mode**. One important operational constraint: Lockdown Mode and Developer Mode cannot be active simultaneously. Activating one disables the other, a deliberate choice that prevents developers from accidentally bypassing security settings in production environments where Lockdown Mode should remain on.

## Why This Matters Now

The timing is not coincidental. The past twelve months have seen ChatGPT evolve from a largely single-turn chat interface into a multi-step agent capable of browsing the web, reading uploaded documents, running code, and connecting to third-party services. Each of these capabilities adds productivity value—and each adds attack surface.

Security researchers have demonstrated in controlled settings that prompt-injection attacks against ChatGPT's web browsing and agent features can be used to exfiltrate clipboard contents, session identifiers, and document text to attacker-controlled URLs. The attacks do not require any compromise of OpenAI's infrastructure; they exploit the fundamental tension between an AI model's instruction-following nature and the untrustworthiness of content it reads from the open web.

Enterprise adoption has compounded the urgency. As companies deploy ChatGPT for tasks like contract review, HR document analysis, and code generation in sensitive codebases, the potential blast radius of a successful prompt injection attack grows. A model that reads an adversarially crafted PDF and then attempts to POST its contents to an external server is not a theoretical concern—it is a demonstrated attack pattern.

Lockdown Mode addresses this by making the POST request impossible. Even if an injected instruction successfully manipulates the model's output, it has no network pathway to complete the exfiltration.

## Honest About the Limits

OpenAI has been notably candid about what Lockdown Mode cannot guarantee. The company explicitly states the feature "does not guarantee that data exfiltration cannot happen." Three residual risk vectors remain:

**Third-party app integrations**: Users who have connected third-party applications to ChatGPT retain those connections even in Lockdown Mode. A malicious instruction could potentially abuse a connected app to reach an external system.

**Unforeseen capability combinations**: AI systems are complex, and the interaction between Lockdown Mode's restrictions and specific capability combinations may create unanticipated gaps that future attack research could surface.

**Novel exploitation techniques**: Security is an arms race. Lockdown Mode closes known attack vectors; it does not immunize the system against attack techniques that haven't been discovered yet.

The company also notes that malicious instructions embedded in uploaded files continue to affect ChatGPT's behavior even in Lockdown Mode—the model reads the file, and if the file contains adversarial text, that text enters the context. The protection is against exfiltration, not against the injection itself.

## Elevated Risk Labels: A Companion Feature

Alongside Lockdown Mode, OpenAI introduced **Elevated Risk Labels**—visual indicators that appear in the interface when ChatGPT is processing content that has a higher probability of containing prompt injections. The system draws on heuristics about content types and provenance to flag situations where users should be especially cautious about the actions ChatGPT proposes to take.

The labels don't block actions; they surface warnings. The design reflects OpenAI's broader philosophy that AI safety is best achieved through a combination of technical controls and informed human oversight, rather than opaque automatic blocking that users can't reason about.

## The Broader Security Trajectory

ChatGPT Lockdown Mode arrives as the industry grapples with a fundamental tension in agentic AI design. The features that make AI assistants most useful—web access, tool use, multi-step autonomy—are precisely the features that expand the attack surface. Security-conscious enterprises have been asking for opt-in hardening modes for months; OpenAI's implementation validates the demand.

Competitors are watching. Google's Gemini Advanced and Anthropic's Claude both face identical prompt-injection risks in their agentic configurations. Whether they follow with analogous hardening features in the coming months will be a useful indicator of how seriously the industry is treating security as a first-class product concern rather than an afterthought.

For now, Lockdown Mode represents a pragmatic and honest step: it shrinks the attack surface significantly, acknowledges what it cannot guarantee, and gives users the agency to make an informed trade-off between capability and security. For enterprises handling sensitive documents, that trade-off is one many security teams will be eager to make.
