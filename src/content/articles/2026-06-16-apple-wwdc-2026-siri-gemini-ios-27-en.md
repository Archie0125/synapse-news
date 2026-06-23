---
title: "Apple Pays Google $1B/Year to Run Siri: Inside WWDC 2026's Defining Moment"
summary: "At WWDC 2026, Apple unveiled a completely rebuilt Siri powered by Google Gemini's 1.2-trillion-parameter model, paying approximately $1 billion per year for the partnership. iOS 27 brings a three-tier AI routing architecture, multi-chatbot extensions including Claude and ChatGPT, and drops device support for iPhone 11. Tim Cook delivered his final WWDC keynote before transitioning to executive chairman."
category: "products"
publishedAt: 2026-06-16
lang: "en"
featured: false
trending: true
sources:
  - name: "TechRadar — Apple WWDC 2026 Live"
    url: "https://www.techradar.com/news/live/apple-wwdc-2026-live"
  - name: "Tom's Guide — WWDC 2026 Recap"
    url: "https://www.tomsguide.com/news/live/wwdc-2026-live-news-updates"
  - name: "MacRumors — Everything Announced at WWDC 2026"
    url: "https://www.macrumors.com/2026/06/08/wwdc-2026-recap/"
  - name: "9to5Mac — iOS 27 Multi-AI Extensions Report"
    url: "https://9to5mac.com/2026/05/05/ios-27-will-let-you-choose-between-gemini-claude-and-more-for-ai-features-report/"
  - name: "TechJournal — WWDC 2026 Siri Gemini iOS 27"
    url: "https://techjournal.org/wwdc-2026-siri-gemini-ios-27"
  - name: "The Next Web — Apple Siri Extensions"
    url: "https://thenextweb.com/news/apple-siri-extensions-third-party-ai-missing-wwdc"
tags:
  - "Apple"
  - "WWDC 2026"
  - "Siri"
  - "Google Gemini"
  - "iOS 27"
  - "Apple Intelligence"
  - "Tim Cook"
relatedSlugs:
  - "2026-06-15-google-gemini-35-pro-imminent-launch-en"
  - "2026-06-14-anthropic-overtakes-openai-aws-5gw-compute-deal-en"
---

On June 8, 2026, Tim Cook took the stage at Apple Park for what would be his final WWDC keynote as CEO. What he announced marked a historic break from the company's foundational strategy: Apple, the company that pioneered the principle of owning the full stack from silicon to software, is now paying Google approximately $1 billion per year to power its AI assistant.

The new Siri is not incrementally improved. It has been rebuilt from scratch, running on a custom version of Google Gemini with a reported 1.2 trillion parameters. It is the most significant third-party infrastructure decision Apple has made in a generation — and a frank admission from Tim Cook's team that the company could not build competitive cloud AI at scale on its own.

## The Architecture Behind the New Siri

The rebuilt Siri operates on a three-tier routing system that Apple engineers spent years designing to balance privacy, capability, and cost.

Simple queries — setting timers, launching apps, reading weather — stay entirely on-device, handled by a compact Apple-trained model running in the Neural Engine. This preserves the privacy guarantees Apple has built its brand around for the past decade: that data never leaves your iPhone for routine tasks.

Mid-level requests — drafting emails, summarizing documents, managing calendar conflicts — route to Apple's Private Cloud Compute infrastructure, a system of Apple Silicon servers designed specifically to process cloud AI workloads without storing user data or making it visible to Apple employees.

Complex queries — open-ended research, multi-step planning, creative generation — route to Gemini's cloud infrastructure under the custom $1 billion agreement. This tier is where the 1.2 trillion-parameter model operates. Apple specifies in the updated privacy documentation that these queries are processed under strict data handling terms, but critics have noted that the fundamental privacy calculus changes when Google's servers are handling some portion of what users ask Siri.

The new Siri features a standalone chatbot-style app with full text input support, multi-step command chaining, on-screen awareness (the ability to respond to content currently visible on your display), and personal context drawn from your emails, photos, and files. When the assistant is uncertain whether to route a query on-device or to the cloud, it signals this to the user — a design choice Apple is positioning as transparency about AI decision-making.

## Claude and ChatGPT Join the Ecosystem — Quietly

Apple's iOS 27 beta contains an Extensions framework that allows users to route Siri queries to Claude, ChatGPT, and other third-party AI providers via gesture controls. When an outside model handles a request, it responds in a distinct voice from Apple's system, so users know which AI is answering.

Notably, this Extensions system was absent from the June 8 keynote itself. Apple demoed the new Gemini-powered Siri extensively but made no mention of Claude or ChatGPT on stage. The feature surfaced in the developer beta documentation that went live immediately after the keynote — a quiet launch that has drawn speculation about whether Apple is still finalizing the commercial arrangements with Anthropic and OpenAI, or whether it wanted to avoid attention on the feature in a keynote focused on the Gemini partnership.

The architecture represents a meaningful shift for Anthropic and OpenAI. Claude and ChatGPT being accessible inside Siri — even as secondary options — gives those models a distribution channel of over a billion active iPhone users. Whether users will actually invoke these alternatives in meaningful numbers, or whether the default Gemini-powered experience will capture the vast majority of queries, is an open question.

## iOS 27: What Changes for Users

All Apple operating systems jumped to version 27 with this release: iOS 27, iPadOS 27, macOS Golden Gate, watchOS 27, tvOS 27, and visionOS 27. The version number itself is a statement — Apple aligning all its platforms to a common numeral echoes the software coherence push that began with the 2019 catalyst program.

For iPhone users, iOS 27 runs on iPhone 12 and newer. iPhone 11 loses software update support, affecting tens of millions of users who will need to upgrade to continue receiving security patches. The new Gemini-powered Siri and full Apple Intelligence feature set require iPhone 15 Pro or newer — a hardware segmentation that sets a clear incentive structure for upgrading.

Notable iOS 27 features beyond the AI overhaul include redesigned CarPlay support for automotive OEM integration, an upgraded Apple Maps with Flyover visual enhancements, perimenopause and menopause tracking added to the Health app, and system-wide performance optimizations that Apple is promising will make iPhone 12-era hardware feel significantly faster despite running newer software.

Developer betas went live immediately after the keynote. Public betas are expected in mid-July. The full public release is scheduled for September 2026, alongside what the rumor mill is positioning as a significant iPhone 17 Pro hardware refresh.

## Tim Cook's Last Dance

WWDC 2026 was Tim Cook's fifteenth as CEO and, by Apple's own account, his final keynote in that role. Cook has been signaling his transition to executive chairman for several quarters, with succession planning reported to be centered on Chief Operating Officer Sabih Khan or a rotation of senior vice presidents depending on the strategic priorities of the moment.

The Gemini deal is Cook's parting gift and, in a sense, his most honest acknowledgment of where the AI race stands. After years of arguing that Apple's vertical integration — building its own chips, its own frameworks, its own AI models — was a structural advantage, Cook is departing having admitted that cloud AI is one area where building alone is not enough.

The $1 billion annual payment to Google is not just a line item. It is a strategic admission: for all of Apple's investments in on-device AI through the A-series and M-series chips, the frontier of large-scale reasoning remains in the cloud, and the cloud leader in AI is Google. Building on top of that, rather than competing with it, is the calculation Cook has made.

## What This Means for the AI Landscape

Apple's Gemini integration shifts the competitive dynamics of the foundation model market. Google now has two of the world's most valuable distribution relationships: its own search and assistant surfaces, and Apple's billion-plus user base. For OpenAI, which had previously secured the ChatGPT integration with Apple Intelligence announced at WWDC 2024, the new architecture represents a demotion — ChatGPT remains available through Extensions, but Gemini is now the default for the new Siri's most sophisticated queries.

For developers, iOS 27 opens up new integration paths through the Extensions framework. Apps that have built on Claude, ChatGPT, or other models could potentially surface inside Siri with the right entitlements — though the technical details of that pathway remain to be worked out through the beta period.

For users, the new Siri is materially more capable than anything Apple has shipped before. Whether that capability justifies the privacy implications of Google's cloud handling a subset of your most complex queries is a personal calculus. Apple has spent years building the argument that you shouldn't have to make that tradeoff. With iOS 27, the company has quietly decided that, at least for the most demanding tasks, you will.
