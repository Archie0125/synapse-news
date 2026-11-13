---
category: ai-ml
featured: true
lang: en
publishedAt: '2026-11-13T18:34:51.313772+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/tarikmostafa/why-standing-api-tokens-are-architectural-malpractice-the-case-for-ephemeral-single-action-15me
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/github-agentic-workflows-ga/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: Engadget
  url: https://www.engadget.com/2313187/grok-build-leaked-sensitive-spacexsi-data/
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1032020/gemini-chatgpt-perplexity-shopping-test-risky-fake-websites-citations
- name: TechCrunch
  url: https://techcrunch.com/2026/11/12/cyberattack-on-fireworks-ai-allowed-hackers-to-access-notion-customers-chat-transcripts/
summary: Giving a probabilistic agent a permanent API key is not automation—it is
  an incident waiting for a trigger.
tags: []
title: AI Agents Don’t Have a Hallucination Problem. They Have an Authority Problem
trending: true
type: analysis
---

AI agents do not become dangerous when they make mistakes. They become dangerous when we give those mistakes credentials.

That distinction is being buried under the industry’s obsession with smarter models. Vendors keep selling higher benchmark scores, longer context windows, and better reasoning as if reliability naturally arrives with intelligence. It does not. A model that chooses the correct action 99.5% of the time still produces five failures per 1,000 decisions. Give that model access to GitHub, Stripe, Slack, and a production database, and “five failures” stops being a quality metric. It becomes an operational threat model.

The old chatbot could embarrass a company. The new agent can change the company’s infrastructure before anyone notices.

The architectural mistake is surprisingly mundane: teams are connecting agents the way they connected scripts a decade ago. Put a `GITHUB_TOKEN`, `DATABASE_URL`, or payment key in an environment variable; add a system prompt saying what the agent should not do; then hope model alignment holds. A standing credential may remain valid for months and authorize thousands of actions. A prompt injection needs to succeed only once.

That is why the most important agent-security idea is not another content filter. It is ephemeral, single-action authority. An agent should propose a precisely scoped operation—such as “add label `bug` to issue 1842”—and an external policy service should decide whether to issue a one-use credential bound to that action, target, and short expiration time. The agent never sees the upstream secret. If its runtime is compromised, the attacker steals a proposal mechanism, not an organization-wide skeleton key.

GitHub’s Agentic Workflows, made generally available on October 28, 2026 after entering public preview in June, offers a useful blueprint. Agents begin with read-only permissions inside sandboxed containers. Proposed changes pass through a threat-detection job, while a separate job holding its own write token applies them. Teams can place GitHub Environment approval in front of that write step.

That separation matters more than whether the coding model gains another three points on a benchmark. It turns “the agent was tricked” and “production was modified” into two distinct events. Security lives in the gap between them.

GitHub’s implementation also shows why product labels cannot substitute for architecture. Its own FAQ says the protections do not automatically cover custom jobs or workflows granted direct write access. Self-hosted deployments using Actions Runner Controller may run Docker-in-Docker through a privileged sidecar. In other words, a least-privileged agent can still sit beside a highly privileged component. The sandbox icon in a product diagram tells you almost nothing unless you inspect the full execution path.

GitHub has also put numbers around runaway behavior. AI Credits cost $0.01 each, with a default limit of 1,000 credits—or $10—per run. Enterprise defaults include 5,000 credits per day, 400 per threat-detection run, and a 20-minute agent timeout. These are presented as spending controls, but they are security controls too. A compromised agent with unlimited retries is effectively an automated attacker funded by the victim.

Accenture says one lead saved an estimated 29 hours per week with the workflows. GitHub’s announcement does not explain how that figure was measured. That is a familiar agent-era trade: productivity benefits arrive as a polished anecdote, while risk appears as a configuration manual. Buyers should reverse that burden of proof. Show the permission graph, failure rate, rollback path, and blocked-action log before showing the time-saved slide.

The consequences are already escaping controlled demos. Claroc researchers found that Grok Build share links exposed apps belonging to thousands of users, including SpaceXSI itself. The URLs used four random words with up to 38 bits of entropy, but the random portion appeared as a subdomain. Passive DNS systems therefore recorded links that users reasonably assumed were secret.

The exposed SpaceXSI material reportedly included a sales territory map covering 594 strategic accounts, eight X advertising proposals, four live advertiser boards, and two copies of an X brand-safety playbook. Only one exposed app required a password. Claroc found six affected Fortune 500 companies and 26 organizations with more than 1,000 employees; it estimated that about 2% of the exposed apps contained material serious enough for its highest risk categories.

This was not a futuristic model-alignment failure. It was a URL-design failure amplified by AI-generated software and careless sharing defaults. That is the pattern to watch: ordinary security mistakes become more frequent because agents generate more applications, integrations, and data flows than security teams can review manually.

A second warning comes from AI-assisted shopping. Podqi tested 6,795 answers involving 151 brands across Gemini, ChatGPT, and Perplexity. Perplexity displayed risky retail sites in 15% of answers, ChatGPT in 8%, and Gemini in 4%. ChatGPT warned users about risky sites only 24% of the times it surfaced them.

The methodology deserves scrutiny: Podqi designed the prompts, and one brand in the study, Madhappy, was its client. But even the best result—Gemini at 4%—is unacceptable once an assistant moves from suggesting stores to autonomously completing purchases. At 4%, one in 25 answer sets contains a risky destination. A shopping agent processing 10,000 sessions could create hundreds of opportunities for credential theft, counterfeit purchases, or chargebacks.

Here is what nobody is talking about: agents collapse several previously separate supply chains into one invisible chain of trust.

A user may think they are using Notion AI, but the request can pass through Notion, an AI infrastructure vendor, that vendor’s cloud provider, a model host, telemetry systems, and storage layers. In November 2026, Notion disclosed that a breach involving Fireworks AI affected roughly 1% of its customers. Attackers obtained some transcripts from the Notion AI Insights feature, including model inputs and outputs. Fireworks said the intrusion began through its cloud provider and reached a development system. It was Fireworks’ second disclosed incident in two months.

Users did not choose Fireworks. They did not negotiate its data retention or inspect its development environment. Yet their private conversations inherited every weakness downstream. This is the reliability gap in its most commercial form: the interface belongs to one company, while the blast radius is assembled from vendors the customer cannot see.

The bear case is that heavy approval gates will destroy the value of agents. If a human must authorize every label change, refund, deployment, and email, why not do the work manually? That objection is correct for low-risk, reversible actions. Read-only analysis, draft creation, test execution, and changes inside disposable environments should run automatically.

But autonomy should be priced by consequence, not marketed as a universal setting. Reading a public issue and deleting a customer database are not two positions on the same convenience slider. Production systems need graduated authority: automatic execution for low-impact actions, policy validation for bounded changes, and human approval for irreversible or externally visible operations.

The winning agent platform will not be the one that acts most freely. It will be the one that can prove exactly why an action was allowed, what credential authorized it, which data crossed each vendor boundary, and how the damage stops when every other layer fails.

### What to Watch

By mid-2027, major agent platforms will begin advertising one-use capability tokens and permission duration as product features, much as cloud providers once marketed encryption at rest. Any vendor still asking customers to paste permanent organization-wide API keys into an agent runtime will look negligent.

GitHub’s read-agent/write-job separation will become a pattern outside software development. Expect payment agents to propose refunds while a separate service executes them, and support agents to draft account changes while an approval service issues action-bound credentials.

Agent evaluations will also move beyond answer accuracy. Enterprise buyers will demand behavioral tests for prompt injection, retry storms, poisoned tool output, compromised vendors, and approval bypasses. “The model passed the benchmark” will carry little weight without a blocked-action rate and a measured blast radius.

Finally, at least one major 2027 breach will be blamed publicly on an agent but traced to something less glamorous: an overbroad token, a discoverable share link, an unreviewed connector, or a vendor’s development system. That will not make agents innocent. It will prove the point: intelligence is not the security boundary. Authority is.