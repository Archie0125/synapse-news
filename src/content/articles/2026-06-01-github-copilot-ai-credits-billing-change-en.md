---
title: "GitHub Copilot's Flat-Rate Era Ends Today: AI Credits Replace Premium Request Units"
summary: "GitHub's AI coding assistant has switched to usage-based billing as of June 1, retiring Premium Request Units in favor of 'GitHub AI Credits' tied directly to token consumption. Plan prices are unchanged, but agentic workflows and code review now draw from a monthly credit pool — and once it's gone, organizations decide whether to let the meter run or cut developers off."
category: "developer-tools"
publishedAt: 2026-06-01
lang: "en"
featured: false
trending: true
sources:
  - name: "GitHub Blog"
    url: "https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/"
  - name: "GitHub Docs"
    url: "https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises"
  - name: "Visual Studio Magazine"
    url: "https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx"
  - name: "Enterprise DNA"
    url: "https://enterprisedna.co/resources/news/github-copilot-usage-based-billing-enterprise-2026/"
tags:
  - "GitHub Copilot"
  - "AI Credits"
  - "developer tools"
  - "Microsoft"
  - "pricing"
  - "agentic AI"
  - "billing"
relatedSlugs:
  - "2026-06-01-microsoft-build-2026-mai-coding-models-en"
  - "2026-04-04-cursor-devin-war-en"
---

For the millions of developers who have come to rely on GitHub Copilot as a daily coding companion, today marks a quiet but consequential shift in the terms of that relationship. As of June 1, 2026, GitHub has officially transitioned its AI assistant away from flat-rate billing — and toward a metered system built around a new virtual currency called GitHub AI Credits.

The change has been telegraphed since April, when GitHub announced the restructuring in a community post. But now that the migration is live, the implications are coming into sharper focus for enterprises and individual subscribers alike.

## Out with PRUs, In with Credits

The previous system granted paying Copilot users a monthly allotment of "Premium Request Units" (PRUs) — a fixed budget tied to usage of advanced AI features like Copilot Chat with GPT-4o, multi-file edits, and code review. PRUs acted as a soft ceiling: once exhausted, users were downgraded to weaker model responses until the monthly clock reset.

GitHub AI Credits work differently in important ways. One AI Credit equals $0.01 USD, and credits are consumed based on actual token usage across input, output, and cached context, priced according to the published API rates for each underlying model. Credit consumption scales with workload complexity and model choice — using Claude Sonnet for a complex multi-file refactor will cost more than running a quick inline completion through a lighter model.

Crucially, what stays free: basic code completions and Next Edit Suggestions, the bread-and-butter inline autocomplete that most developers use every minute of the day, remain fully included in all plans with no credit deduction. The billing clock only starts ticking when developers engage features that make substantive model calls — Copilot Chat with frontier models, multi-file agentic workflows, pull request code review, and similar functions.

## Pricing Tiers: Unchanged and Unchanged

GitHub has been careful to emphasize that monthly plan prices are not moving. The three commercial tiers are:

- **Copilot Pro+** — $39/month, includes $39 in monthly AI Credits
- **Copilot Business** — $19/user/month, includes $19 in monthly AI Credits  
- **Copilot Enterprise** — $39/user/month, includes $39 in monthly AI Credits

In each case, the included credit allotment is numerically equal to the subscription price, which means each dollar paid converts directly to $1 in credit. Additional usage beyond the included pool is available at published API rates, which organizations can opt into or cap by policy.

The math is not as straightforward as it looks. Under the old PRU system, a heavy agentic user might have had their usage throttled after exhausting their premium allotment, but they would never see an overage charge — the plan simply degraded gracefully. Under AI Credits, an enterprise running automated code review pipelines or agentic refactoring bots at scale can now generate real overage costs unless admins actively configure spending limits.

## The Developer Reaction

Developer response has been mixed, trending toward skeptical. Visual Studio Magazine ran a community survey after the April announcement, with the headline quote — "You will get less, but pay the same price" — capturing the dominant sentiment. The concern is that while the nominal plan price is identical, the effective value received by power users has decreased: a $39/month subscriber who used to run complex agentic workflows freely now has a metered budget that can be exhausted mid-month.

GitHub has countered this framing by pointing to the addition of budget controls and the claim that typical developers who use Copilot primarily for completions and occasional chat will see no effective change. "For the vast majority of our users, this change is invisible," one GitHub spokesperson said. "Code completions — the thing people use most — are not touching credits at all."

For enterprise customers, the picture is more nuanced. Admins now have granular budget controls: they can set spending ceilings at the enterprise, cost center, team, and individual user levels. When the included pool runs dry, organizations can choose to allow additional usage at metered rates or enforce a hard cap that disables premium features until the next billing cycle. This level of governance is new and welcome for IT procurement teams who have struggled to predict Copilot's total cost of ownership as agentic use cases proliferated.

## The Broader Context: AI Becomes Infrastructure

The switch from PRUs to AI Credits is not just a billing adjustment — it reflects a fundamental shift in how GitHub thinks about what Copilot is becoming. When Copilot launched in 2021, it was a code autocomplete tool. In 2026, it is increasingly an agentic platform capable of planning and executing multi-step development tasks: writing tests, opening pull requests, reviewing changes, and orchestrating actions across repositories.

Metered pricing is the natural infrastructure model for that kind of compute. Cloud services like AWS Lambda and Azure Functions have always charged per invocation rather than per month precisely because their cost profile is nonlinear. GitHub is applying the same logic to AI workloads.

The timing is also competitive. Cursor raised $2 billion at a $50 billion valuation in April on the strength of its per-request model, which developers have embraced for its transparency. Devin, JetBrains AI, and a new wave of agentic coding tools are all experimenting with usage-based pricing. GitHub's move aligns Copilot with the market's direction, even as it risks friction with users accustomed to thinking of Copilot as an always-available utility.

## What Should Developers Do Now

For individual subscribers on Copilot Pro+, the practical advice is to monitor the new credit usage dashboard — GitHub has added a real-time spend tracker to the Copilot settings panel — and pay attention to which features are consuming the most credits. The biggest credit consumers are typically long agentic sessions with frontier models, not conversational chat.

For enterprises, the transition is a good forcing function to audit how Copilot is actually being used. Many organizations deployed Copilot broadly but have limited visibility into which teams are generating the most model traffic. The new cost center reporting makes that visible for the first time.

The bottom line: GitHub Copilot is still one of the most cost-effective AI productivity tools available, and for developers who primarily use completions and light chat, today's change is a non-event. For power users building automation on top of Copilot's agentic capabilities, the metered future has arrived — and the bill is about to become more legible.
