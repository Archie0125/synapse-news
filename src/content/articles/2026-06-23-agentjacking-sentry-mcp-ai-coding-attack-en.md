---
title: "Agentjacking: A Single Fake Bug Report Can Hijack Claude Code, Cursor, and Codex"
summary: "Security researchers at Tenet Security have disclosed 'Agentjacking,' a new attack technique that exploits Sentry's Model Context Protocol integration to inject malicious instructions into AI coding agents. With an 85% success rate against Claude Code, Cursor, and Codex, the attack exposed 2,388 organizations—including a Fortune 100 tech firm—by disguising attacker code as legitimate error-resolution guidance. Sentry declined to fix the root cause, instead deploying a content filter."
category: "developer-tools"
publishedAt: 2026-06-23
lang: "en"
featured: false
trending: true
sources:
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html"
  - name: "The New Stack"
    url: "https://thenewstack.io/agentjacking-sentry-mcp-attack/"
  - name: "Infosecurity Magazine"
    url: "https://www.infosecurity-magazine.com/news/agentjacking-attacks-hijack-ai/"
  - name: "SC Media"
    url: "https://www.scworld.com/brief/agentjacking-attack-exploits-ai-coding-tools-with-fake-error-reports"
  - name: "CybersecurityNews"
    url: "https://cybersecuritynews.com/agentjacking-attack-hijacks-ai-coding-agent/amp/"
tags:
  - "security"
  - "AI agents"
  - "Claude Code"
  - "Cursor"
  - "Codex"
  - "MCP"
  - "Sentry"
  - "prompt injection"
  - "developer tools"
relatedSlugs:
  - "2026-06-20-warp-ai-search-poisoning-cornell-en"
  - "2026-06-11-anthropic-2026-agentic-coding-trends-report-en"
  - "2026-06-12-opencode-displaces-cursor-ai-coding-agent-en"
---

AI coding agents have spent the past two years being handed progressively more power: access to terminals, file systems, browser automation, and external APIs. Tenet Security's disclosure of a technique called Agentjacking, published this week, illustrates precisely why that expanding attack surface warrants urgency.

The attack requires no breach, no authentication, and no malware. A single HTTP POST request—less effort than filing a real bug report—can cause Claude Code, Cursor, or OpenAI Codex to execute arbitrary attacker code on a developer's machine, with the developer's own privileges. Tenet's researchers identified 2,388 organizations with exploitable configurations and tested the technique against more than 100 companies, including at least one Fortune 100 technology firm. The success rate: 85%.

## The Architecture of Trust—and Its Exploitation

To understand Agentjacking, you need to understand how Sentry integrates with AI coding agents via the Model Context Protocol (MCP).

Sentry is an error-tracking platform used by hundreds of thousands of development teams. When a production application crashes, Sentry captures the stack trace, error context, and environment metadata, and stores it in a project identified by a Data Source Name (DSN). The DSN is intentionally public—it must be embedded in frontend JavaScript for the browser SDK to function. Anyone who visits a website can extract the DSN from the page source.

MCP, the open standard released by Anthropic in late 2024 and now widely adopted across AI development tools, allows coding agents to interact with external services. The Sentry MCP server lets a developer tell Claude Code or Cursor: "look at my recent Sentry errors and fix them." The agent queries Sentry, retrieves error data, and uses it as context for code generation.

Here is where the attack lives: Sentry's event ingestion endpoint accepts arbitrary payloads from anyone who possesses the DSN. An attacker can craft a fake error event containing markdown-formatted instructions masquerading as error resolution steps—and post it directly to a target's Sentry project without any credentials.

When the developer next asks their AI coding agent to review Sentry issues, the agent retrieves the attacker-controlled payload, treats the injected instructions as legitimate diagnostic data, and executes them. The code runs with the developer's privileges on the developer's machine.

## The "Authorized Intent Chain"

Tenet's researchers gave this vulnerability pattern a name: the Authorized Intent Chain. It describes a class of attack where each step in a delegated trust hierarchy is technically legitimate, even as the overall chain produces unauthorized outcomes.

In the Agentjacking scenario:
- The developer authorizes the AI coding agent to act on their behalf
- The agent authorizes the MCP connection to retrieve data from Sentry
- Sentry is a service the developer explicitly integrated and trusts
- The MCP server returns data from Sentry with no integrity verification
- The agent treats Sentry data as ground truth and executes the embedded instructions

Every handoff in the chain passes inspection. There is no anomalous network traffic, no suspicious process, no authentication failure. The existing trust relationships between developer → agent → MCP → Sentry create a corridor the attacker walks through uncontested.

Tenet's team demonstrated that the attack succeeded even when the agent was explicitly instructed to ignore external instructions within error messages—the malicious payload was formatted to resemble structured resolution guidance rather than raw command text, making it functionally indistinguishable from legitimate Sentry data in the model's context window.

## Evasion: Every Defense Failed

The researchers tested whether standard defensive layers would catch Agentjacking. They did not.

Endpoint Detection and Response (EDR) tools observed the code execution but flagged nothing because the activity was initiated by the developer's own agent process, not an external binary or network injection. Firewalls saw outbound connections to Sentry's legitimate API endpoints—normal behavior for any team running error monitoring. Prompt-level defenses failed because the malicious content arrived as retrieved data, not as user input, circumventing most prompt injection mitigations that focus on the user-facing message layer.

This isn't a failure of any single product. It reflects a structural gap in how the AI toolchain handles data retrieved from external services: the model has no reliable mechanism to distinguish between "data I retrieved from a trusted integration" and "instructions an adversary injected into that trusted integration."

## Scale and Affected Organizations

Tenet estimated that at least 2,388 organizations currently have Sentry DSNs that could be used to inject malicious events. This figure was derived by scanning public web properties for exposed DSNs—a passive technique requiring no credentials or prior access to target systems.

Of the organizations Tenet tested, AI assistants at more than 100 companies executed the researchers' test payload, confirming live exploitation potential. At least one Fortune 100 technology firm was among those confirmed vulnerable. The researchers coordinated responsible disclosure before publication, notifying Sentry and the affected AI tooling vendors.

## Sentry's Response: Content Filtering, Not Root Cause

Sentry acknowledged the issue but declined to address the root cause—the fact that its event ingestion endpoint accepts arbitrary payloads from anyone with a public DSN. The company's rationale: DSNs are designed to be public, and fundamentally restricting who can post events would break legitimate integrations including crash reporters, browser SDKs, and third-party instrumentation.

Instead, Sentry deployed a global content filter that blocks specific payload strings identified in Tenet's proof-of-concept. Security researchers and practitioners have noted the limitations of this approach: the filter addresses the specific strings in Tenet's published example, not the attack class. Variations that reformat the injection, use different encoding, or embed instructions in alternative payload fields are likely to bypass the existing filter.

Anthropic, whose Claude Code is among the primary targets, has indicated awareness of the issue. The MCP server architecture Anthropic designed does not include data provenance verification by default—distinguishing legitimate service data from attacker-injected data is currently left to individual MCP server implementations and the discretion of the underlying model.

## Mitigation Options

Tenet recommends several mitigations for development teams using AI coding agents with Sentry MCP integration:

**Human review gates.** Insert a mandatory human review step between Sentry event retrieval and agent execution. Before the agent acts on any retrieved error, a developer should inspect the raw event data for injected instructions. This is operationally costly in workflows optimized for autonomous agent operation, but it closes the attack vector.

**Sentry DSN rotation.** Teams can rotate their DSN to invalidate any attacker-planted events in the existing project. This is a one-time remediation, not a sustained defense, since new DSNs are equally public by design.

**MCP server allowlisting.** Some agent configurations support allowlists that restrict which external services can provide context for code execution. Teams should audit which MCP servers have write-capable access to agent context and limit this to services with stronger input validation.

**Isolated agent environments.** Running coding agents in isolated environments—containers or virtual machines without credentials for production systems—limits the blast radius if an agent is successfully hijacked. This is best practice for autonomous agents generally, not just for Agentjacking specifically.

## A Broader Pattern

Agentjacking is not an isolated vulnerability. It is an instance of a broader attack class that security researchers have been warning about since the proliferation of agentic AI systems: the integrity of an AI agent's context window depends entirely on the integrity of every data source it queries. As agents are given access to more external services via MCP, the attack surface expands proportionally.

The Sentry case is particularly instructive because the exploited channel is intentionally public by design. The DSN is meant to be visible; Sentry's entire architecture assumes the event ingestion endpoint is accessible to unauthenticated clients. When an AI agent treats that endpoint's output as trusted instructions, a design decision that was correct for error monitoring becomes a security liability for autonomous code execution.

For AI tooling vendors, the lesson is that standard threat models for developer integrations do not translate cleanly to agentic contexts. Data retrieved from external services requires integrity verification mechanisms that the current MCP ecosystem does not mandate. Until those mechanisms exist, the Authorized Intent Chain represents a persistent risk surface that grows with every new MCP server added to a developer's agent configuration.
