---
title: "Apple Pays $1B a Year to Remake Siri with Google Gemini — WWDC 2026 Recap"
summary: "At WWDC 2026, Apple unveiled a completely rebuilt Siri powered by a custom 1.2-trillion-parameter Google Gemini model in a deal reportedly worth $1 billion annually. iOS 27 and macOS 27 'Golden Gate' ship deep AI integration across every core app, marking Apple's boldest AI strategy pivot yet."
category: "ai-ml"
publishedAt: 2026-06-18
lang: "en"
featured: true
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/09/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/"
  - name: "MacRumors"
    url: "https://www.macrumors.com/roundup/wwdc/"
  - name: "Let's Data Science"
    url: "https://letsdatascience.com/news/apple-unveils-gemini-powered-siri-and-ios-27-at-wwdc-2026-b757953c"
  - name: "Redshark News"
    url: "https://www.redsharknews.com/apple-wwdc-2026-siri-gemini-ios-27"
tags:
  - "Apple"
  - "Siri"
  - "Google Gemini"
  - "iOS 27"
  - "WWDC 2026"
  - "AI assistants"
relatedSlugs:
  - "2026-06-18-apple-wwdc-2026-siri-gemini-ios-27-zh"
  - "2026-06-17-android-17-gemini-omni-pixel-launch-en"
  - "2026-06-18-openai-gpt56-imminent-june-launch-en"
---

When Apple CEO Tim Cook took the stage at Apple Park on June 9, the opening act was not a new iPhone, a new chip, or a new product category. It was the most consequential software partnership in Apple's history: a reported $1 billion-per-year deal with Google to put a custom Gemini AI model at the core of Siri.

For nearly two decades, Siri has been a reliable punchline — the assistant that searched the web when you wanted an answer, the voice in your pocket that failed to set a timer on the first try. WWDC 2026 was Apple's declaration that the joke is over.

## The $1 Billion Bet

Apple licensed a custom 1.2-trillion-parameter version of Google's Gemini model — roughly eight times larger than the biggest cloud model Apple had ever built in-house — under an arrangement reportedly worth approximately $1 billion per year. That price tag secures Apple a dedicated, customized deployment of Gemini's most powerful inference infrastructure, fine-tuned for the tasks Siri users actually perform.

"We believe privacy in AI is non-negotiable," SVP Craig Federighi told the audience, framing the announcement with characteristic care. Apple was not abandoning its privacy identity, he argued — it was engineering around it.

The result is a three-tier routing architecture that Federighi described in unusual technical depth:

- **On-device Apple models** handle simple, low-latency requests — timers, messages, music playback — with no data leaving the device.
- **Private Cloud Compute** routes mid-complexity tasks through Apple's own servers, where cryptographic guarantees are meant to prevent even Apple's engineers from accessing user data.
- **Gemini cloud** handles only the heaviest queries: long-horizon planning, complex document analysis, cross-app reasoning tasks where raw model scale matters most.

Whether this privacy architecture holds under real-world scrutiny is a question for regulators and security researchers. As a system design, it is genuinely novel — and it gives Apple a credible narrative for why licensing a competitor's model is not a contradiction of its brand values.

## A New Siri, Inside and Out

The visual identity of Siri has been rebuilt from scratch. The familiar pulsing orb is gone. In its place is a standalone Siri app — dark-themed, conversation-forward, more reminiscent of Claude or ChatGPT than any previous version of Apple's assistant.

Opening the app reveals an "Ask Siri" bar that accepts text or voice, with a paperclip attachment icon for images, PDFs, and documents. Siri now maintains full conversation history across sessions, can follow up on previous queries, and draws context from emails, messages, files, and photos to complete tasks that would previously have defeated it.

On-screen awareness is perhaps the most immediately useful new capability. Point your camera at a restaurant menu and ask whether there is anything suitable for a dairy-free guest; Siri reasons over what the camera sees. Pull up a screenshot of a festival schedule, describe which three performances interest you, and Siri adds them to your calendar directly without requiring you to touch the screen again.

iOS 27 also adds **Extensions**, a framework letting users designate Claude or Gemini as their default AI assistant system-wide, replacing Siri in supported apps. Apple's willingness to enshrine competitors as first-class citizens of its operating system is a striking signal — either of confidence in the overall experience, or of pragmatic recognition that some users have strong model allegiances Apple cannot override.

## iOS 27 and macOS 27 'Golden Gate': AI at Every Layer

The operating system updates that ship alongside the new Siri represent the most thorough AI integration Apple has ever attempted.

In **Photos**, new editing tools include "Reframe" for spatial perspective adjustments and "Extend" for generating new image content at the edges of a frame — capabilities that migrate professional-grade editing into everyday use. An improved "Cleanup" feature makes object removal significantly more reliable.

In **Messages**, AI-powered reply suggestions move beyond the three-word quick responses of previous years. The system reads full thread context and drafts substantive replies that users review before sending.

In **Phone**, mid-call context awareness surfaces relevant information from Mail and Messages while a call is in progress — pulling up project details a client is asking about without requiring the user to put them on hold and search manually.

**Shortcuts** has been rebuilt around natural language: describe in plain English the workflow you want to automate, and iOS 27 attempts to construct the shortcut. A system-wide dictation engine corrects spelling, punctuation, and capitalization on the fly.

The update reaches back to iPhone 11, representing Apple's broadest iOS compatibility in the platform's history — a signal that Apple wants as many devices as possible running these AI features as quickly as possible.

macOS 27 "Golden Gate" carries the same intelligence stack to the desktop, with additional power in the search layer — Spotlight, Photos, and Mail search have been rebuilt on new foundations that understand natural language queries rather than requiring exact-match keyword input.

## The Competitive Calculus

Apple's WWDC 2026 lands in an AI landscape that has reshuffled dramatically in the past eighteen months. Google's Gemini 2.5 Ultra leads on coding and reasoning benchmarks; Anthropic's Claude 4 dominates in long-form analysis and safety evaluations; and OpenAI's GPT-5 series continues a sub-60-day iteration cycle, with GPT-5.6 widely expected before month's end.

For Apple, the risk of continued underperformance was existential for the assistant category. The company's in-house AI team had produced capable, efficient on-device models — genuinely impressive given the power envelope constraints of a phone — but inadequate for the open-ended reasoning tasks users increasingly expect.

The Gemini licensing deal effectively buys time: time to scale Apple's own research organization, time to expand Private Cloud Compute capacity, and time for the market to reveal which AI capabilities actually drive user loyalty.

For Google, the calculus is subtler. The deal delivers guaranteed revenue and, more importantly, places Gemini at the center of over a billion active devices. The inference feedback signal generated by that scale — understanding how real users phrase real questions in a privacy-safe aggregate — could prove more strategically valuable over time than the licensing fees themselves.

## What to Watch

Developer betas of iOS 27, iPadOS 27, macOS 27, watchOS 27, and visionOS 27 are available today. Public releases are expected to ship alongside new iPhone hardware in September 2026.

WWDC 2026 was conspicuously hardware-free — no new Mac, no updated iPad, no Vision Pro announcement. That silence is deliberate: Apple is saving its product stage for the fall, and likely for a fall in which the AI capabilities demonstrated this week will be a central part of every pitch.

For the first time since Siri's 2011 debut, Apple's AI assistant is genuinely competitive. Whether the $1 billion-per-year bet on Google's infrastructure turns out to be a bridge to a stronger in-house position — or a permanent strategic dependency — is the question that will define Apple's AI decade.
