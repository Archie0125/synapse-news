---
title: "Apple Confirms iOS 26.5 Brings End-to-End Encrypted RCS Messaging (Beta) Between iPhone and Android"
summary: "Apple has released the iOS 26.5 release candidate, confirming that end-to-end encrypted RCS messaging (beta) is coming to the Messages app, with supported carriers. The update also includes Suggested Places in Maps and a Pride Luminance wallpaper."
category: "products"
publishedAt: 2026-05-06
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "9to5Mac"
    url: "https://9to5mac.com/2026/05/04/apple-confirms-ios-26-5-messages-app-adds-rcs-end-to-end-encryption/"
  - name: "MacRumors"
    url: "https://www.macrumors.com/2026/05/05/ios-26-5-three-new-iphone-features/"
  - name: "Privacy Guides"
    url: "https://www.privacyguides.org/news/2026/05/05/apple-confirms-rcs-e2ee-will-ship-with-ios-26-5/"
  - name: "Geeky Gadgets"
    url: "https://www.geeky-gadgets.com/ios-26-5-rc-released/"
tags:
  - "Apple"
  - "iOS 26.5"
  - "RCS"
  - "end-to-end encryption"
  - "messaging"
  - "privacy"
  - "Android"
relatedSlugs:
  - "2026-05-05-wwdc-2026-preview-ios27-siri-gemini-en"
---

Apple has released the iOS 26.5 release candidate, and its release notes confirm a feature the privacy community has waited years to see: end-to-end encryption for RCS messages exchanged between iPhone and Android devices.

The update is expected to be released next week. It is modest in scope compared to major iOS releases, but it marks a turning point in how the world's billion-plus iPhone users communicate with the other half of the smartphone market.

## What RCS E2EE Actually Means

Apple added RCS (Rich Communication Services) support to the Messages app in iOS 18, replacing the aging SMS protocol for conversations between iPhones and Android phones. RCS brought read receipts, typing indicators, higher-quality media sharing, and reaction support — the features that iMessage users had taken for granted for years. What it did not bring was privacy.

Standard RCS messages — unlike iMessage between two iPhones — were not end-to-end encrypted. That meant carriers and, in principle, anyone who intercepted the transmission could read the content. Apple's Messages app displayed those conversations with green bubbles, and the lack of encryption was a meaningful privacy gap between blue-bubble (iMessage) and green-bubble (RCS) chats.

iOS 26.5 changes that. According to Apple's confirmation and the RC release notes, end-to-end encrypted RCS is being rolled out in beta through supported carriers, with a broader rollout to follow over time. When the feature is active, a lock icon will appear in the conversation, consistent with iMessage's encryption indicator.

The GSMA announced Universal Profile 3.0 in March 2025, and with it RCS E2EE based on the MLS standard, though it is not yet clear which specific features Apple will support. This matters because the standard is not Apple-proprietary. Google Messages uses its own in-house encryption based on the Signal protocol, and carriers also need to support the new encryption for it to work. A message sent from an iPhone running iOS 26.5 to an Android phone running Google Messages, where both support the standard, will be protected end-to-end.

## Why It Took This Long

The delay was not technical reluctance on Apple's part. RCS E2EE required the GSMA to finalize the cross-platform standard, carriers to update their infrastructure to route encrypted traffic, and handset makers on both sides to implement compatible clients. Apple has been actively involved in the GSMA working groups that produced the standard.

The carrier dependency is why iOS 26.5 notes that the feature will "roll out over time" — not every carrier has completed infrastructure upgrades, and in markets where carriers lag, the encryption simply will not be available until they do. Apple is expected to prominently display which conversations are and are not encrypted, giving users transparency about their actual security posture.

## New Features: Maps, EU Notifications, and Android Migration

Beyond the headline RCS update, iOS 26.5 includes two other features highlighted in Apple's release notes:

**Suggested Places in Maps**: The Maps app displays recommendations based on what is trending nearby and the user's recent searches. Ads are set to start appearing in this section in the U.S. and Canada later this year. Apple's implementation draws on its own crowd-sourced data, keeping the recommendations on-device where possible to limit privacy exposure.

**EU-Exclusive Notification Forwarding**: In a concession to European digital market regulations, iOS 26.5 adds the ability to forward notifications to third-party devices, including non-Apple smartwatches. This means Galaxy Watch, Garmin, and other wearable users in the EU can receive iPhone notifications without needing an Apple Watch — a meaningful expansion of iPhone compatibility in Europe. Users outside the EU will not see this feature in the initial rollout.

**Android Message Transfer**: Users switching from iPhone to Android can now transfer their iMessage history as part of the device migration process. This is Apple acknowledging that some customers do leave, and making the process less punishing. For years, the lack of an easy message transfer was an implicit lock-in mechanism; removing that barrier reflects both regulatory pressure and Apple's confidence that its ecosystem advantages are sufficient to retain users without friction.

## The Broader Privacy Narrative

iOS 26.5 arrives at a moment when encrypted messaging has become a mainstream concern rather than a niche one. The ongoing Musk v. Altman trial has put questions of data control and AI training on front pages; policymakers globally are debating what access governments should have to communications; and AI-generated phishing, according to recent Mandiant research, is outperforming human red teams.

End-to-end encryption for cross-platform RCS does not address all of those concerns, but it meaningfully raises the floor for the average person's messaging security. When a grandmother texts her Android-using grandchild, that conversation can be encrypted so that Apple or any third party cannot intercept and read it, provided both devices and carriers support the feature.

Apple has been the standard-bearer for consumer privacy marketing. iOS 26.5 is a case where the marketing is backed by a genuine technical commitment. The green bubbles are getting a lot more private.

## What to Expect After the RC

The iOS 26.5 release candidate typically precedes the public release by approximately one week. Barring unexpected issues discovered during the RC phase, users can expect the update to arrive the week of May 11, 2026. The RCS E2EE feature is labeled a beta and will roll out over time with supported carriers.

Ahead of WWDC 2026 in June, iOS 26.5 represents the last significant iOS update before the iOS 27 preview — keeping Apple's release cadence on track for a fall announcement cycle that, according to earlier reporting, will center heavily on deeper AI integration through a next-generation Siri powered by a multimodal model.

*Correction (November 15, 2026): 10 sentences were corrected or removed to match the sources listed on this page.*
