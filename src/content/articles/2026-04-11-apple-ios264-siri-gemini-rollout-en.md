---
title: "Apple's Gemini-Powered Siri Features Are Not in iOS 26.4, and It Is Unclear When They Will Arrive"
summary: "The new Siri features from Apple's Google Gemini partnership are not in iOS 26.4. Apple has reportedly shifted its target to iOS 26.5 and iOS 27, and it is not yet known which features will arrive in which release."
category: "products"
publishedAt: 2026-04-11T09:00:00Z
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "9to5Mac"
    url: "https://9to5mac.com/2026/03/20/apples-gemini-powered-siri-upgrade-could-still-arrive-this-month/"
  - name: "MacRumors"
    url: "https://www.macrumors.com/2026/01/25/siri-google-gemini-release-date/"
  - name: "Geeky Gadgets"
    url: "https://www.geeky-gadgets.com/ios-26-4-siri-2-0-gemini/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html"
  - name: "Apple Insider"
    url: "https://appleinsider.com/articles/26/01/25/new-siri-expected-to-finally-debut-in-ios-264-beta-shortly"
tags:
  - "Apple"
  - "Siri"
  - "Google Gemini"
  - "iOS 26.4"
  - "Apple Intelligence"
  - "AI"
  - "mobile"
relatedSlugs:
  - "2026-04-07-apple-ios26-sdk-msca-en"
  - "2026-04-05-apple-business-platform-en"
  - "2026-04-09-apple-baltra-ai-server-chip-en"
---

For five years, Apple's most consistent AI story was an embarrassing one: Siri, the world's most distributed voice assistant by installed base, was consistently outclassed by competitors with a fraction of Apple's resources. Last January's announcement that Apple had partnered with Google to replace the AI engine behind Siri with a custom version of Gemini — at a reported cost of $1 billion per year — was the company's clearest acknowledgment yet that building a competitive large language model in-house had been a strategic failure.

iOS 26.4 turned out to be feature-packed, but the new Siri features from that partnership are not in it. But if you were expecting Siri to feel fundamentally different overnight, the reality is more complicated — and in some ways, more honest about the difficulty of rebuilding a decade-old voice assistant from the inside.

## What's Actually in iOS 26.4

These are the building blocks of the agentic Siri experience that Apple has been describing since the original Apple Intelligence announcement in 2024.

## The Gap Between Promise and Delivery

The frustration is not that iOS 26.4 is bad — the Phase 1 features represent a real and meaningful improvement over the Siri that preceded them. The frustration is the distance between what Apple announced in January and what is actually shipping now.

The January 12 announcement, framed as a joint statement from Apple and Google, said the next generation of Apple Foundation Models would be based on Gemini models and cloud technology, helping power future Apple Intelligence features, including a more personalized Siri coming this year, while maintaining "Apple's industry-leading privacy standards."" The custom Gemini model at the center of the deal is reportedly eight times larger than Apple's existing cloud AI models — a 1.2 trillion parameter system purpose-built for Apple's specific requirements.

The new Siri features are not part of iOS 26.4. According to Bloomberg's Mark Gurman, Apple would instead target iOS 26.5 and iOS 27 for the new Siri features, though it is not yet known which features will make which release. The reason most frequently cited is integration complexity: routing Gemini's inference through Apple's Private Cloud Compute architecture, while maintaining the privacy guarantees Apple has committed to, required more engineering work than the original timeline anticipated.

## The Privacy Architecture Challenge

The privacy engineering problem deserves more than a dismissive note. Apple's Private Cloud Compute is genuinely novel infrastructure — a system that allows on-device and cloud AI inference to be performed in a way that Apple itself cannot access the user's data, verified through cryptographic attestation that security researchers have audited publicly. Integrating a model as large as the custom 1.2 trillion parameter Gemini into this framework is not a trivial API integration.

The engineering challenge is that Gemini's conversational capabilities — particularly its memory and long-context reasoning — depend on infrastructure that assumes the model can maintain state and access broad context. Apple's privacy architecture is designed precisely to prevent that kind of persistent access to user data. Reconciling these two design philosophies, without compromising either Gemini's capabilities or Apple's privacy guarantees, is the problem that pushed Phase 2 to a later release.

When it ships, Phase 2 is intended to enable a Siri that can synthesize across a user's entire data footprint — messages, emails, photos, health data, calendar, and third-party apps — with the conversational fluency of Gemini, while running through the same Private Cloud Compute attestation model. The privacy story, if Apple executes it, would be unprecedented: a trillion-parameter conversational AI that operates at frontier capability levels with zero-knowledge guarantees for the AI provider.

## The Commercial Consequences

For Apple, the stakes of getting Siri right extend beyond product embarrassment. The company's primary hardware premium — the argument that iPhone and Mac command higher prices than Android alternatives — has historically rested on software quality and ecosystem integration. As AI assistants become increasingly central to how people interact with their devices, a Siri that demonstrably lags Gemini on Google's own Android devices, or ChatGPT on iPhones where users download OpenAI's app, erodes the core value proposition.

The $1 billion annual payment to Google is an extraordinary commitment — larger than most AI companies' entire annual revenue — and reflects Apple's calculation that the cost of licensing Gemini is lower than the reputational cost of shipping another generation of mediocre Siri features. But licensing alone does not guarantee successful integration. The Phase 2 delays are a reminder that the hard work is not acquiring access to capable AI, but weaving it into a product experience that feels seamless.

Early adopters who have installed iOS 26.4 describe the Phase 1 Siri improvements as "noticeably better, not transformationally better" — a verdict that is probably fair. The real test will come in September, when iOS 27 ships with the full Phase 2 capabilities. If Apple delivers on what it promised in January, the narrative shifts from "Apple's AI embarrassment continues" to "Apple solved the privacy problem no one else attempted." If Phase 2 slips again, the $1 billion annual Gemini deal will look like an expensive acknowledgment of a competitive deficit that Apple still cannot close on its own timeline.

The history of Apple product cycles suggests that first-generation shipping is rarely the full story. But its users have been waiting for a Siri upgrade for years. Their patience, like the Phase 2 rollout, has a deadline.

*Correction (November 15, 2026): 15 sentences were corrected or removed to match the sources listed on this page.*
