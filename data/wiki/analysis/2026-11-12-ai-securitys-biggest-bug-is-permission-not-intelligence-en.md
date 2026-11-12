---
category: industry
lang: en
published: '2026-11-12T18:40:46.516312+00:00'
sources:
- name: Dev.to
  url: https://dev.to/tarikmostafa/why-standing-api-tokens-are-architectural-malpractice-the-case-for-ephemeral-single-action-15me
- name: Engadget
  url: https://www.engadget.com/2313187/grok-build-leaked-sensitive-spacexsi-data/
- name: Wired
  url: https://www.wired.com/story/security-flaws-across-uk-government-sites-exposed-god-tier-information/
- name: Hacker News
  url: https://www.vulncheck.com/blog/anthropic-glasswing-november-update
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1032020/gemini-chatgpt-perplexity-shopping-test-risky-fake-websites-citations
summary: The dangerous AI agent is not the smartest one—it is the one holding a permanent
  credential.
title: AI Security’s Biggest Bug Is Permission, Not Intelligence
trending_theme: AI Security and Reliability Gaps
type: analysis
---

The AI security debate is staring at the wrong screen. Researchers obsess over whether models can invent bioweapons or escape their sandboxes, while companies are already handing probabilistic software permanent database passwords, billing privileges, and production write access. The immediate danger is not artificial superintelligence. It is ordinary automation carrying extraordinary authority.

This is a familiar engineering mistake wearing an AI badge. Teams configure agents much as they configured cron jobs in 2016: place a `DATABASE_URL`, `STRIPE_SECRET_KEY`, or organization-wide `GITHUB_TOKEN` in the runtime, add a prompt saying “only modify approved records,” and assume the instruction limits the credential. It does not. A prompt describes preferred behavior; a token defines actual power.

The distinction matters because agents consume untrusted material by design. They read emails, webpages, support tickets, repositories, documents, and tool responses. Any one of those can contain a prompt injection, malicious dependency, poisoned instruction, or simply ambiguous text. When the same process also holds a long-lived secret, one parsing mistake can become a cross-system incident.

The better architecture is almost boring: the agent proposes one action, an external policy service checks the action and target, and the service issues a short-lived, single-use grant. A token authorizing “refund order 4821 for US$29.50 within 30 seconds” is fundamentally safer than a Stripe key authorizing every refund indefinitely. The agent should never see the upstream master credential. A consumed nonce, narrow scope, expiration time, and signed action receipt turn a runaway loop from a company-wide event into one bounded mistake.

This is not a new security insight. Saltzer and Schroeder described least privilege in 1975. What has changed is the frequency with which software now decides what action to take. Traditional applications expose predetermined paths written by developers. Agents assemble paths dynamically, often across GitHub, Slack, Salesforce, cloud storage, and payment systems. That flexibility multiplies the number of places where identity, policy, and context can disagree.

The [Grok Build exposure](https://www.engadget.com/2313187/grok-build-leaked-sensitive-spacexsi-data/) demonstrates how little sophistication an incident may require. Its shared apps used four random “dice words,” reportedly providing up to 38 bits of entropy. But the random portion appeared to the left of the domain, where passive DNS systems could record it, instead of inside a URL path. The links looked secret to users while remaining discoverable through public infrastructure.

Claroc reportedly found exposed material belonging to thousands of users, including a hospital group, a fire department, six Fortune 500 companies, and 26 organizations with more than 1,000 employees. SpaceXSI’s own exposed material included a sales map covering 594 strategic accounts, four live advertiser boards, eight X advertising proposals, and two copies of a brand-safety playbook. Only one exposed app requested a password, and Claroc estimated that about 2% of the material deserved a high or critical rating.

That 2% figure is the important number. Consumer AI products encourage people to create hundreds or thousands of small apps, summaries, dashboards, and workflows. Most contain nothing consequential, so weak defaults appear harmless during testing. At scale, however, even a 2% serious-exposure rate becomes an incident factory. SpaceXSI removed 24 of its own exposed apps after public escalation, according to Claroc, but other users’ apps reportedly remained available. A platform cannot call a sharing model safe when remediation depends on every customer noticing the same design error.

Old-fashioned credential hygiene is failing too. A researcher using Claude Opus and Sonnet found [more than 100 serious vulnerabilities in publicly available UK government code](https://www.wired.com/story/security-flaws-across-uk-government-sites-exposed-god-tier-information/). The worst case involved Microsoft Entra ID credentials committed to GitHub and not fully revoked. They allegedly offered read-and-write access across SharePoint, private employee OneDrive accounts, HR records, and evidence held for statutory planning cases—access the researcher described as “god-tier.”

The Planning Inspectorate said monitoring detected the activity, the problem was fixed within 20 minutes of the report, and no breach occurred. That is a meaningful defense. It is also an indictment of everything before detection: broad credentials, incomplete revocation, public source exposure, and insufficient maintenance. Claude helped locate the weakness, but the defect itself was not futuristic. AI is accelerating the discovery of security debt that basic health checks should already have found.

Discovery, however, is not the same as security. Seven months into Anthropic’s Project Glasswing, [VulnCheck tracked 37,966 reported findings](https://www.vulncheck.com/blog/anthropic-glasswing-november-update), of which 7,349—or 19.4%—had become public and only 217 were marked fixed. Since September, the project reportedly added almost 12,000 findings but just 15 additional fixes. It also accumulated 1,654 duplicates and 419 withdrawn reports. Curl maintainers rejected 19 of 34 published reports as vulnerabilities, rated six as low severity, and still had nine awaiting assessment.

The bear case is obvious: only 442 CVEs had been attributed to Anthropic, roughly 0.5% of that year’s published CVEs, and only two were known to be exploited in the wild. Podqi’s shopping study also used researcher-written prompts rather than real conversations, and one tested brand, Madhappy, was a client. Those limitations matter. They show why a claimed 94.2% true-positive rate should not be treated as ground truth.

But the skeptical reading does not rescue today’s AI products. It exposes the second reliability gap: models can generate alerts, links, and recommendations faster than humans can validate them. A scanner that produces 12,000 new findings while recording 15 fixes may increase maintainer exhaustion faster than it reduces risk. Security teams do not need a larger inbox. They need reproducible evidence, deduplication, severity calibration, ownership, and patch capacity.

The same verification failure reaches consumers. In [6,795 shopping answers tested by Podqi](https://www.theverge.com/ai-artificial-intelligence/1032020/gemini-chatgpt-perplexity-shopping-test-risky-fake-websites-citations), Perplexity displayed risky URLs in 15% of answers, ChatGPT in 8%, and Gemini in 4%. The sites included impersonators, counterfeit sellers, abandoned domains re-registered by new owners, and dead domains available for purchase. ChatGPT warned users about risky sites only 24% of the times it surfaced them.

Here is what nobody is talking about: AI answers are becoming an identity layer for the web without assuming the responsibilities of one. A search result presents provenance signals, domain names, multiple alternatives, and often reputation warnings. A conversational answer compresses those clues into a confident recommendation. Once an agent can also open the site, enter an address, or complete a purchase, a citation error stops being bad information and becomes an executed transaction.

This changes the economics of fraud. Criminals no longer need to rank first for millions of human searches. They need a poisoned domain, convincing product data, and enough presence in the sources models retrieve. Smaller brands were about twice as likely as large ones to receive risky-site mentions in Podqi’s testing, making obscure regional retailers the softest targets. AI shopping could unintentionally become an affiliate channel for counterfeiters.

The security standard for agents therefore cannot be “the model usually behaves.” Every consequential action needs a verifiable target, minimal authority, explicit limits, and a receipt recording who proposed it, which policy approved it, what credential was issued, and what actually happened. If a company cannot reconstruct that chain after an incident, it has deployed an unaccountable employee with machine speed.

## What to Watch

- **Permanent agent credentials will become an audit failure.** By the end of 2027, major enterprise buyers will begin requiring action-scoped tokens, expiration measured in minutes, and out-of-process policy enforcement in procurement reviews.

- **Vulnerability counts will lose marketing value.** Projects such as Glasswing will be judged by validated fixes, median remediation time, duplicate rate, and maintainer acceptance—not the number of generated findings.

- **AI shopping products will add domain verification.** ChatGPT, Gemini, and Perplexity will need verified-brand registries, domain-age checks, ownership-change alerts, and warnings before sending users to unfamiliar sellers. Citations alone are not protection.

- **The first defining agent-security lawsuits will concern ordinary permissions.** Expect disputes over an agent using an authorized credential for an unauthorized purpose—not a model “breaking free.” The companies with single-action grants and auditable receipts will have a defensible story. The others will have prompts.