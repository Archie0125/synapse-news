---
category: ai-ml
lang: en
published: '2026-11-13T06:28:03.722661+00:00'
sources:
- name: Wired
  url: https://www.wired.com/story/teen-girl-asked-gemini-about-suicide-for-months-until-it-was-flagged/
- name: Engadget
  url: https://www.engadget.com/2313187/grok-build-leaked-sensitive-spacexsi-data/
- name: Tom's Hardware
  url: https://www.tomshardware.com/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back
- name: Hacker News
  url: https://www.vulncheck.com/blog/anthropic-glasswing-november-update
- name: Hacker News
  url: https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/
summary: Models are getting more capable while the systems deciding what they may
  touch remain dangerously primitive.
title: AI’s Real Bottleneck Isn’t Intelligence. It’s Permission.
trending_theme: AI Trust Gaps Widen
type: analysis
---

The most dangerous AI product is not the model that occasionally gives a wrong answer. It is the model that gives a plausible answer while holding production credentials, publishing code, advising a child, or exposing company data—and is trusted because someone added the word “agent” to its name.

That distinction matters because the AI trust gap is widening in two directions. Models can now generate software, search for security flaws, and conduct long conversations at a scale that looked unrealistic three years ago. Yet the controls around them—identity, access, monitoring, verification, escalation, and human review—still resemble the hurried settings page of a beta SaaS product.

We are automating authority faster than we are automating accountability.

Consider four stories from November 2026. A lawsuit alleges that a 13-year-old in North Carolina used a school Chromebook to discuss depression, research suicide, and plan her funeral for three months before adults intervened. A Grok coding product exposed sensitive apps through discoverable links. A Linux memory-management reviewer stepped back after AI-generated patches overwhelmed his inbox. Meanwhile, an independent analysis of Anthropic’s vulnerability-hunting project found a widening gap between reported findings and confirmed fixes.

These are not four unrelated AI mishaps. They are the same systems-design failure appearing in education, enterprise software, open source, and cybersecurity: generation scales cheaply; judgment does not.

## The safety stack had multiple chances to fail

According to the [Wired report](https://www.wired.com/story/teen-girl-asked-gemini-about-suicide-for-months-until-it-was-flagged/), the family’s lawsuit says Google Search routed the 13-year-old to Gemini even though her school had blocked the standalone Gemini site. The teenager allegedly spent three months discussing self-harm before monitoring software generated an alert. That alert reportedly went to the personal phone of a counselor who had left the school nine months earlier.

Look at the chain. The chatbot’s safety response was one layer. Google Search routing was another. The Chromebook’s school policy was a third. Student-monitoring software was a fourth. The alert directory and the school’s incident process were fifth and sixth.

The failure was not simply “Gemini said something bad.” The system depended on six layers, but nobody verified that the layers formed a working safety path. Blocking one domain did not block the capability. Detecting risk did not guarantee timely escalation. Sending an alert did not mean the recipient still had the job.

Schools were sold visibility; what they needed was response readiness. A dashboard showing that a warning existed is worthless if the warning arrives weeks late or lands on an ex-employee’s phone.

This is also why Google requiring schools to enable generative AI features to keep using Search, as described by Wired, is more than an unpopular product decision. It changes the default from “a school chooses to deploy AI” to “a school must actively fight the platform to limit it.” For an adult experimenting with search, that might be an interface annoyance. For a school managing thousands of minors, defaults are policy.

## Grok Build confused secrecy with access control

The [Grok Build exposure](https://www.engadget.com/2313187/grok-build-leaked-sensitive-spacexsi-data/) is almost a parody of modern AI security. The product created share links using four random “dice words,” providing as much as 38 bits of entropy. But it placed the random phrase in a subdomain, where passive DNS systems could record it. The links looked secret to users while becoming discoverable through public databases.

Security firm Claroc reportedly found exposed material from thousands of users, including a hospital group, a fire department, six Fortune 500 companies, and 26 organizations with more than 1,000 employees. SpaceXSI’s own exposed material allegedly included a map of 594 strategic sales accounts, eight X advertising proposals, four live advertiser boards, and two copies of an X brand-safety playbook. Only one exposed app asked for a password. Claroc estimated that roughly 2 percent contained material serious enough to rate high or critical.

The embarrassing detail is not that an AI-generated app had a security flaw. Conventional app builders ship flaws too. It is that the product treated an unguessable URL as authorization—an error the security world has understood for decades—while encouraging users to build and share software faster than they could inspect it.

Google Gemini’s link structure, according to the report, puts its random component in the URL path rather than the subdomain. That reduces this particular passive-DNS exposure. But choosing the safer URL position is still not the same as enforcing authentication, expiration, tenant boundaries, and revocation.

A secret link is not an identity system. “Anyone with the link” is not least privilege. AI did not invent those rules, but AI product speed makes ignoring them far more expensive.

## AI can find 37,966 problems. Who fixes them?

Anthropic’s Project Glasswing offers the mirror image of the coding problem: AI producing security findings faster than humans can validate and repair them.

Seven months after its April 7 launch, [VulnCheck’s tracking](https://www.vulncheck.com/blog/anthropic-glasswing-november-update) attributed 442 CVEs to Anthropic, about 0.5 percent of all CVEs published during the year. That is meaningful output. But Anthropic had reportedly logged 37,966 findings, of which 7,349—or 19.4 percent—were public and only 217 were marked fixed. Since September, the ledger added nearly 12,000 findings but just 15 additional fixes.

Duplicates numbered 1,654, almost eight times the fixed count; another 419 reports had been withdrawn. Curl maintainers rejected 19 of 34 published reports as vulnerabilities, classified six as low severity, and still had nine under assessment. Anthropic reported a 94.2 percent true-positive rate, up from 90.8 percent, but those maintenance outcomes make that headline number hard to interpret.

The bear case against this criticism is fair: finding hundreds of CVEs is useful, only two of the 442 were identified as exploited in the wild, and imperfect reports can still direct maintainers toward real weaknesses. Security research has always produced duplicate, disputed, and low-severity findings.

But that defense misses the operational problem. A vulnerability is not remediated when a model names it. It is remediated when someone reproduces it, judges severity, develops a safe patch, tests compatibility, ships the update, and gets users to install it. Discovery is the cheapest stage to scale, so counting discoveries rewards the part of the pipeline AI already makes abundant.

The better metric is not findings per model run. It is median days from valid report to deployed fix, weighted by exploitability and affected installations.

## Linux exposes the hidden trust tax

Linux reviewer Lorenzo Stoakes said AI-generated “slop” went from an occasional sighting to weekly, then every few days, and now “pretty much half” of what he sees, according to [Tom’s Hardware](https://www.tomshardware.com/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back). He stepped away from several memory-management responsibilities, including core, reclaim, Rust, and transparent huge pages work, while retaining other duties such as KVM.

AI coding advocates count code produced. Open-source maintainers pay for code inspected.

That is the trust tax: one person can prompt an agent to generate five patches before lunch, but an experienced maintainer must reason through locking, lifetime, compatibility, performance, and failure behavior. Rejecting a bad patch can take longer than generating it. Worse, every low-quality submission competes with a real fix for scarce reviewer attention.

Linus Torvalds has taken a more positive view of AI assistance, and he has a point: machines can avoid some careless mistakes made by experienced humans. AI can also help newcomers understand unfamiliar code and draft repetitive changes. The issue is not whether AI ever writes good code. It plainly does. The issue is whether submitters bear enough of the verification cost before transferring that cost to maintainers.

Here’s what nobody is talking about: the scarce input in the AI economy is no longer code, prose, findings, or recommendations. It is credible rejection.

Organizations need people and systems empowered to say no: no, this patch lacks meaningful tests; no, this link is not access control; no, this alert workflow has never been exercised; no, this vulnerability count does not equal risk reduction. AI makes proposals nearly free, so the economic value moves to filtering, provenance, and accountable approval.

That will change budgets. Companies spending millions on model access will have to spend more on sandboxing, permission design, evaluation suites, audit trails, incident drills, and senior reviewers. If they do not, the apparent productivity gain will reappear later as security incidents, maintenance queues, customer-support load, and insurance costs.

## What to Watch

First, “agent permissions” will become a buying criterion by 2027. Enterprise customers will ask whether an agent can receive time-limited credentials, operate inside a sandbox, expose an action log, and require approval for external writes. Products offering only a broad API key and a confirmation popup will fail security review.

Second, coding platforms will introduce submission friction. Expect major repositories to require AI-use disclosure, reproducible tests, provenance metadata, or contributor rate limits. Linux will not be the last project to protect human reviewers from machine-generated volume.

Third, vulnerability programs will be judged by closure, not discovery. Public scorecards will compare confirmed findings, duplicate rates, time to patch, and real-world exploitability. A five-digit findings total without a repair pipeline will start to look like an unpaid invoice sent to maintainers.

Fourth, schools will face pressure to separate AI access from core productivity contracts. Search, email, classroom management, and generative assistants should not be bundled into one irreversible default. After the North Carolina case, “disable” will have to mean disabling the capability—not merely blocking one website.

The next AI winner will not be the company whose model produces the most. It will be the company whose system can prove what the model saw, what it did, who approved it, and how quickly the action can be stopped. Intelligence may sell the demo. Controlled authority will determine who survives deployment.