---
title: "Apple Pays Google $1B/Year to Run Siri: Inside WWDC 2026's Defining Moment"
summary: "At WWDC 2026, Apple unveiled a rebuilt Siri powered by a custom Google Gemini model, reportedly around 1.2 trillion parameters, at a reported cost of about $1 billion per year. iOS 27 brings a three-tier AI routing architecture and is expected to drop support for iPhone 11, while an Extensions framework for third-party chatbots sits in the beta but was not announced. Tim Cook delivered his final WWDC keynote before transitioning to executive chairman."
category: "products"
publishedAt: 2026-06-16
modifiedAt: 2026-11-15T00:00:00Z
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

The new Siri is not incrementally improved. It has been rebuilt, with its heaviest queries running on a custom version of Google Gemini with a reported 1.2 trillion parameters. It is the most significant third-party infrastructure decision Apple has made in a generation — and a frank admission from Tim Cook's team that the company could not build competitive cloud AI at scale on its own.

## The Architecture Behind the New Siri

The rebuilt Siri operates on a three-tier routing system that Apple engineers spent years designing to balance privacy, capability, and cost.

Simple queries — setting timers, launching apps, reading weather — stay entirely on-device, handled by a compact Apple-trained model running in the Neural Engine. This preserves the privacy guarantees Apple has built its brand around for the past decade: that data never leaves your iPhone for routine tasks.

Mid-level requests — drafting emails, summarizing documents, managing calendar conflicts — route to Apple's Private Cloud Compute infrastructure, a system of Apple Silicon servers designed specifically to process cloud AI workloads without storing user data or making it visible to Apple employees.

Complex queries — open-ended research, multi-step planning, creative generation — route to Gemini's cloud infrastructure under the custom $1 billion agreement. This tier is where the 1.2 trillion-parameter model operates. Apple specifies in the updated privacy documentation that these queries are processed under strict data handling terms, but critics have noted that the fundamental privacy calculus changes when Google's servers are handling some portion of what users ask Siri.

The new Siri features a standalone chatbot-style app with full text input support, multi-step command chaining, on-screen awareness (the ability to respond to content currently visible on your display), and personal context drawn from your emails, photos, and files. When the assistant is uncertain whether to route a query on-device or to the cloud, it signals this to the user — a design choice Apple is positioning as transparency about AI decision-making.

## Claude and ChatGPT Join the Ecosystem — Quietly

Apple's iOS 27 developer beta contains underlying support for an Extensions framework that would let users swap between ChatGPT, Claude and Gemini inside Siri, though its settings panel and App Store section are reportedly toggled off. Bloomberg has reported that iOS 27 will let users hear a different voice for Siri responses powered by external models than for Apple's own system.

Notably, this Extensions system was absent from the June 8 keynote itself. Apple demoed the new Gemini-powered Siri extensively but made no mention of Claude or ChatGPT on stage. The feature surfaced in the iOS 27 developer beta code rather than at the keynote, and Apple has not publicly confirmed whether Extensions will ship with iOS 27 this fall.

The architecture represents a meaningful shift for Anthropic and OpenAI. If Extensions ships, Claude and ChatGPT being accessible inside Siri would give those models a distribution channel to a very large base of active Apple devices. Whether users will actually invoke these alternatives in meaningful numbers, or whether the default Gemini-powered experience will capture the vast majority of queries, is an open question.

## iOS 27: What Changes for Users

All Apple operating systems jumped to version 27 with this release: iOS 27, iPadOS 27, macOS Golden Gate, watchOS 27, tvOS 27, and visionOS 27. The version number itself is a statement — Apple aligning all its platforms to a common numeral echoes the software coherence push that began with the 2019 catalyst program.

For iPhone users, iOS 27 is expected to run on iPhone 12 and newer. iPhone 11 is expected to lose support, so owners may need to upgrade; Apple's official compatibility list should confirm this. The new Gemini-powered Siri and Apple Intelligence features require iPhone 15 Pro or newer — a hardware segmentation that sets a clear incentive structure for upgrading.

Notable iOS 27 features beyond the AI overhaul include redesigned CarPlay support for automotive OEM integration, an upgraded Apple Maps with Flyover visual enhancements, perimenopause and menopause tracking added to the Health app, and system-wide performance optimizations that Apple is promising will make iPhone 12-era hardware feel significantly faster despite running newer software.

Developer betas went live immediately after the keynote. Public betas are expected in mid-July. The full public release is scheduled for September 2026, alongside the iPhone 18 lineup.

## Tim Cook's Last Dance

WWDC 2026 was Tim Cook's fifteenth as CEO and, by Apple's own account, his final keynote in that role. Cook is set to transition to executive chairman, handing the chief executive role to John Ternus.

The Gemini deal is Cook's parting gift and, in a sense, his most honest acknowledgment of where the AI race stands. After years of arguing that Apple's vertical integration — building its own chips, its own frameworks, its own AI models — was a structural advantage, Cook is departing having admitted that cloud AI is one area where building alone is not enough.

The $1 billion annual payment to Google is not just a line item. It is a strategic admission: for all of Apple's investments in on-device AI through the A-series and M-series chips, the frontier of large-scale reasoning remains in the cloud, and the cloud leader in AI is Google. Building on top of that, rather than competing with it, is the calculation Cook has made.

## What This Means for the AI Landscape

Apple's Gemini integration shifts the competitive dynamics of the foundation model market. Google now has two of the world's most valuable distribution relationships: its own search and assistant surfaces, and Apple's billion-plus user base.

For developers, the Extensions framework in the iOS 27 beta points to possible new integration paths, though Apple has not confirmed it will ship. Apple has held discussions with OpenAI, Anthropic and Google about granting entitlements for the framework, according to Bloomberg.

For users, the new Siri is materially more capable than anything Apple has shipped before. Whether that capability justifies the privacy implications of Google's cloud handling a subset of your most complex queries is a personal calculus. Apple has spent years building the argument that you shouldn't have to make that tradeoff. With iOS 27, the company has quietly decided that, at least for the most demanding tasks, you will.

*Correction (November 15, 2026): 14 sentences were corrected or removed to match the sources listed on this page.*
