---
title: "Anthropic Acquires Stainless, Cutting Off the SDK Tool Used by OpenAI and Google"
summary: "Anthropic has acquired Stainless, a New York-based developer tools startup whose SDK-generation platform was widely used by rival AI labs including OpenAI, Google, and Cloudflare. Anthropic didn't disclose terms, though the deal was reported at over $300 million, and the company plans to wind down Stainless's hosted products."
category: "developer-tools"
publishedAt: 2026-05-24
modifiedAt: 2026-11-15T00:00:00Z
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

Anthropic announced on May 18 that it has acquired Stainless, a New York-based startup that automated the creation and maintenance of software development kits for API-driven products. Anthropic didn't disclose terms, but The Information reported the company was in talks to pay more than $300 million, and the deal is noteworthy for a reason that goes well beyond the price tag: Stainless had become a shared piece of infrastructure for AI labs that are otherwise fierce competitors. Its customers included OpenAI, Google, Cloudflare, and Runway — meaning Anthropic has just bought a key infrastructure supplier its rivals used.

## What Stainless Actually Does

Founded in 2022 by Alex Rattray, a former Stripe engineer, Stainless solves a problem that is tedious, repetitive, and critically important: keeping SDK libraries in sync with a rapidly evolving API.

When an AI company ships a new model, endpoint, or parameter, every SDK that developers use to call that API — Python, TypeScript, Go, Kotlin, Java — needs to be updated accordingly. Doing this by hand is error-prone and time-consuming. Rattray's insight was to treat the API specification as the source of truth and automate the rest: Stainless takes an OpenAPI spec, generates production-quality SDKs across all target languages, and continues to regenerate them automatically as the spec changes.

The result was a platform that dramatically reduced the maintenance burden for any company that runs a public API. This was particularly valuable to companies building AI agents that connect to external software. Google and Cloudflare were also among the companies that used the platform.

## The Competitive Fallout

Anthropic's announcement was direct: the company plans to wind down all hosted Stainless products, including its SDK generator. Existing customers will retain full ownership and rights to the SDKs they've generated to date, and can modify or extend them independently — but the automated maintenance pipeline that kept those SDKs current is going away.

For OpenAI and Google, this creates a genuine, if manageable, operational headache. Both companies will need to either build their own SDK generation infrastructure, contract with a new vendor, or absorb the manual maintenance burden in-house. None of those options are catastrophic for organizations with engineering resources of that scale — but all of them take time and money that would otherwise go to product development.

In an ecosystem where developer experience is often a decisive factor in API adoption, losing a reliable SDK maintenance platform at a critical growth stage is a real setback.

## Why Anthropic Bought a B2B Tool Startup

At first glance, a reported $300 million-plus for a developer productivity tool looks expensive. But Anthropic is clearly buying strategic advantage as much as technology.

The most obvious rationale is defensive consolidation. As Anthropic's API business scales, the quality and reliability of developer tooling around the Claude API becomes a meaningful competitive factor. By bringing Stainless in-house, Anthropic can direct the platform's full capability toward its own SDK ecosystem: faster updates, better language coverage, tighter integration with Claude's evolving feature set.

There is also a talent angle. Rattray and the Stainless team built what is arguably the most sophisticated API SDK generation platform in the industry. That expertise applied to Anthropic's own developer relations and API infrastructure is worth something independent of the product itself.

The third rationale — and the most strategically uncomfortable for Anthropic's competitors — is disruption. Whether or not Anthropic intends it primarily as a competitive weapon, acquiring and winding down a platform that OpenAI and Google depend on is a real disruption to their developer ecosystems. In a market where developer mindshare compounds over time, every friction point in a competitor's SDK workflow is a small edge for Anthropic.

## Developer Ecosystem as a Moat

The acquisition reflects a broader pattern in the AI industry's current phase: frontier model performance is converging fast enough that complementary developer experience is becoming a primary battleground. When GPT-5, Gemini 3.5 Flash, and Claude 4 are all capable of handling the same enterprise tasks, the decision about which API to build on increasingly comes down to documentation quality, SDK reliability, support responsiveness, and ecosystem depth.

Anthropic created the Model Context Protocol (MCP) to make agent connectivity possible, and Stainless has powered every official Anthropic SDK since the earliest days of its API. The Stainless acquisition fits into that pattern: methodically improving every layer of the developer experience stack.

## What Comes Next

Anthropic has said it will wind down all hosted Stainless products, though sources do not give a precise shutdown date. Customers will need to decide whether exported SDKs, local tooling, or a replacement vendor give them enough automation.

For the broader developer ecosystem, the episode is a reminder that shared infrastructure in competitive markets carries hidden risks. A tool that is "neutral" because multiple competing companies use it can become a weapon the moment one of those companies acquires it.

Anthropic says it is bringing the Stainless team into the company. Stainless's tools will only be available to Anthropic going forward, not its competitors.

The Stainless chapter of AI infrastructure history is over. The next chapter is Anthropic's to write.

*Correction (November 15, 2026): 20 sentences were corrected or removed to match the sources listed on this page.*
