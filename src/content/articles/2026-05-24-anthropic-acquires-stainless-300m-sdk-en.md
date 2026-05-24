---
title: "Anthropic Buys Stainless for $300M+, Cutting Off the SDK Tool That Powered OpenAI and Google"
summary: "Anthropic has acquired Stainless, a New York-based developer tools startup whose SDK-generation platform was widely used by rival AI labs including OpenAI, Google, and Cloudflare. The deal, reported at over $300 million, immediately raises competitive questions: Anthropic plans to wind down Stainless's hosted products, leaving rivals scrambling to rebuild or migrate a key piece of their developer infrastructure."
category: "developer-tools"
publishedAt: 2026-05-24
lang: "en"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/"
  - name: "Anthropic Blog"
    url: "https://www.anthropic.com/news/anthropic-acquires-stainless"
  - name: "The AI Insider"
    url: "https://theaiinsider.tech/2026/05/19/anthropic-acquires-sdk-startup-stainless-for-over-300m-cutting-off-key-tool-used-by-openai-and-google/"
  - name: "Winbuzzer"
    url: "https://winbuzzer.com/2026/05/19/anthropic-buys-stainless-ends-hosted-sdk-tools-xcxwbn/"
tags:
  - "Anthropic"
  - "Stainless"
  - "developer tools"
  - "SDK"
  - "acquisition"
  - "OpenAI"
  - "Google"
relatedSlugs:
  - "2026-05-23-karpathy-anthropic-pretraining-claude-en"
  - "2026-05-23-anthropic-milan-emea-expansion-9x-revenue-en"
  - "2026-05-22-anthropic-first-profit-q2-revenue-109b-en"
---

Anthropic announced on May 18 that it has acquired Stainless, a New York-based startup that automated the creation and maintenance of software development kits for API-driven products. The deal, confirmed by The Information to be worth more than $300 million, is noteworthy for a reason that goes well beyond the price tag: Stainless had become a shared piece of infrastructure for AI labs that are otherwise fierce competitors. Its biggest customers included OpenAI, Google, Cloudflare, and Merge — meaning Anthropic has just bought the plumbing that its rivals depend on to keep their developer ecosystems running.

The competitive implications of that fact are landing hard across the developer tools community.

## What Stainless Actually Does

Founded in 2022 by Alex Rattray, a former Stripe engineer, Stainless solves a problem that is tedious, repetitive, and critically important: keeping SDK libraries in sync with a rapidly evolving API.

When an AI company ships a new model, endpoint, or parameter, every SDK that developers use to call that API — Python, TypeScript, Go, Kotlin, Java — needs to be updated accordingly. Doing this by hand is error-prone and time-consuming. Rattray's insight was to treat the API specification as the source of truth and automate the rest: Stainless takes an OpenAPI spec, generates production-quality SDKs across all target languages, and continues to regenerate them automatically as the spec changes.

The result was a platform that dramatically reduced the maintenance burden for any company that runs a public API. For AI labs shipping new model versions every few weeks, this was particularly valuable. OpenAI's Python and TypeScript libraries — two of the most-downloaded libraries in the entire AI ecosystem — were built and maintained using Stainless. Google's AI SDK infrastructure and Cloudflare's developer offerings were similarly dependent on the platform.

## The Competitive Fallout

Anthropic's announcement was direct: the company plans to wind down all hosted Stainless products, including its SDK generator. Existing customers will retain full ownership and rights to the SDKs they've generated to date, and can modify or extend them independently — but the automated maintenance pipeline that kept those SDKs current is going away.

For OpenAI and Google, this creates a genuine, if manageable, operational headache. Both companies will need to either build their own SDK generation infrastructure, contract with a new vendor, or absorb the manual maintenance burden in-house. None of those options are catastrophic for organizations with engineering resources of that scale — but all of them take time and money that would otherwise go to product development.

The more meaningful disruption is at the margin: smaller AI startups that relied on Stainless because they couldn't afford to build their own SDK tooling now need to find alternatives quickly. In an ecosystem where developer experience is often a decisive factor in API adoption, losing a reliable SDK maintenance platform at a critical growth stage is a real setback.

## Why Anthropic Paid $300M for a B2B Tool Startup

At first glance, $300 million-plus for a developer productivity tool looks expensive. Stainless was not a revenue-generating juggernaut by AI startup standards. But Anthropic is clearly buying strategic advantage as much as technology.

The most obvious rationale is defensive consolidation. As Anthropic's API business scales — the company just reported its first profitable quarter with $10.9 billion in Q2 revenue — the quality and reliability of developer tooling around the Claude API becomes a meaningful competitive factor. By bringing Stainless in-house, Anthropic can direct the platform's full capability toward its own SDK ecosystem: faster updates, better language coverage, tighter integration with Claude's evolving feature set.

There is also a talent angle. Rattray and the Stainless team built what is arguably the most sophisticated API SDK generation platform in the industry. That expertise applied to Anthropic's own developer relations and API infrastructure is worth something independent of the product itself.

The third rationale — and the most strategically uncomfortable for Anthropic's competitors — is disruption. Whether or not Anthropic intends it primarily as a competitive weapon, acquiring and winding down a platform that OpenAI and Google depend on is a real disruption to their developer ecosystems. In a market where developer mindshare compounds over time, every friction point in a competitor's SDK workflow is a small edge for Anthropic.

## Developer Ecosystem as a Moat

The acquisition reflects a broader pattern in the AI industry's current phase: frontier model performance is converging fast enough that complementary developer experience is becoming a primary battleground. When GPT-5, Gemini 3.5 Flash, and Claude 4 are all capable of handling the same enterprise tasks, the decision about which API to build on increasingly comes down to documentation quality, SDK reliability, support responsiveness, and ecosystem depth.

Anthropic has been investing in this dimension for roughly 18 months — shipping a dramatically improved developer portal, launching the Model Context Protocol (MCP) which spawned an ecosystem of third-party integrations, and now hiring Andrej Karpathy as a research advisor. The Stainless acquisition fits into that pattern: methodically improving every layer of the developer experience stack.

The announcement also comes as Anthropic reportedly approaches a new funding round that could value the company at $900 billion — a figure that would make it the most valuable private company in history. At that scale, the company can afford to pay $300 million to control infrastructure that its competitors cannot.

## What Comes Next

Stainless customers that aren't Anthropic have 90 days to prepare for service discontinuation, according to sources familiar with the terms. Most are expected to migrate to internal solutions or emerging alternatives, of which several have already signaled plans to fill the gap.

For the broader developer ecosystem, the episode is a reminder that shared infrastructure in competitive markets carries hidden risks. A tool that is "neutral" because multiple competing companies use it can become a weapon the moment one of those companies acquires it.

Rattray and the core Stainless team will join Anthropic's developer experience organization. The SDK generator technology, stripped of its hosted service, will be retooled into internal tooling that Anthropic uses to maintain its own client libraries — with no plans to make it available externally again.

The Stainless chapter of AI infrastructure history is over. The next chapter is Anthropic's to write.
