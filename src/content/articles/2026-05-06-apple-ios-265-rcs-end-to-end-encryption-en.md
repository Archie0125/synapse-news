---
title: "Apple Confirms iOS 26.5 Brings End-to-End Encrypted RCS Messaging Between iPhone and Android"
summary: "Apple has released the iOS 26.5 release candidate, confirming that end-to-end encrypted RCS messaging will arrive for the first time on iPhone — allowing encrypted cross-platform chats with Android users without relying on iMessage. The update also introduces EU-exclusive notification forwarding to third-party wearables, Suggested Places in Maps, and full message history transfer when switching to Android, making iOS 26.5 Apple's most significant cross-platform privacy update in years."
category: "products"
publishedAt: 2026-05-06
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

Apple has seeded the release candidate for iOS 26.5 to developers and public beta testers, and buried inside the release notes is a feature announcement that the privacy community has waited years to see: end-to-end encryption for RCS messages exchanged between iPhone and Android devices.

The update is expected to reach all users by mid-May 2026. It is modest in scope compared to major iOS releases, but it marks a turning point in how the world's billion-plus iPhone users communicate with the other half of the smartphone market.

## What RCS E2EE Actually Means

Apple added RCS (Rich Communication Services) support to the Messages app in iOS 18, replacing the aging SMS protocol for conversations between iPhones and Android phones. RCS brought read receipts, typing indicators, higher-quality media sharing, and reaction support — the features that iMessage users had taken for granted for years. What it did not bring was privacy.

Standard RCS messages — unlike iMessage between two iPhones — were not end-to-end encrypted. That meant carriers and, in principle, anyone who intercepted the transmission could read the content. Apple's Messages app displayed those conversations with green bubbles, and the lack of encryption was a meaningful privacy gap between blue-bubble (iMessage) and green-bubble (RCS) chats.

iOS 26.5 changes that. According to Apple's confirmation and the RC release notes, end-to-end encrypted RCS is being rolled out in beta through supported carriers, with a broader rollout to follow over time. When the feature is active, a lock icon will appear in the conversation, consistent with iMessage's encryption indicator.

The implementation follows the GSMA's Universal Profile standard for RCS E2EE, which the industry consortium finalized in late 2025. This matters because it means the encryption is not Apple-proprietary — it can, in principle, interoperate with Android's implementation in Google Messages, which already supports the same standard. A message sent from an iPhone running iOS 26.5 to an Android phone running Google Messages, where both support the standard, will be protected end-to-end.

## Why It Took This Long

The delay was not technical reluctance on Apple's part. RCS E2EE required the GSMA to finalize the cross-platform standard, carriers to update their infrastructure to route encrypted traffic, and handset makers on both sides to implement compatible clients. Apple has been actively involved in the GSMA working groups that produced the standard.

The carrier dependency is why iOS 26.5 notes that the feature will "roll out over time" — not every carrier has completed infrastructure upgrades, and in markets where carriers lag, the encryption simply will not be available until they do. Apple is expected to prominently display which conversations are and are not encrypted, giving users transparency about their actual security posture.

## New Features: Maps, EU Notifications, and Android Migration

Beyond the headline RCS update, iOS 26.5 introduces three additional features highlighted in Apple's announcement:

**Suggested Places in Maps**: The Maps app now displays location recommendations based on what is trending nearby and the user's recent searches — a contextual discovery layer similar to what Google Maps has offered for years. Apple's implementation draws on its own crowd-sourced data, keeping the recommendations on-device where possible to limit privacy exposure.

**EU-Exclusive Notification Forwarding**: In a concession to European digital market regulations, iOS 26.5 adds the ability to forward notifications to third-party devices, including non-Apple smartwatches. This means Galaxy Watch, Garmin, and other wearable users in the EU can receive iPhone notifications without needing an Apple Watch — a meaningful expansion of iPhone compatibility in Europe. Users outside the EU will not see this feature in the initial rollout.

**Android Message Transfer**: Users switching from iPhone to Android can now transfer their iMessage history as part of the device migration process. This is Apple acknowledging that some customers do leave, and making the process less punishing. For years, the lack of an easy message transfer was an implicit lock-in mechanism; removing that barrier reflects both regulatory pressure and Apple's confidence that its ecosystem advantages are sufficient to retain users without friction.

## The Broader Privacy Narrative

iOS 26.5 arrives at a moment when encrypted messaging has become a mainstream concern rather than a niche one. The ongoing Musk v. Altman trial has put questions of data control and AI training on front pages; policymakers globally are debating what access governments should have to communications; and AI-generated phishing, according to recent Mandiant research, is outperforming human red teams.

End-to-end encryption for cross-platform RCS does not address all of those concerns, but it meaningfully raises the floor for the average person's messaging security. When a grandmother texts her Android-using grandchild, that conversation will, for the first time, have a layer of cryptographic protection that neither Apple nor the carrier can pierce — provided both devices and carriers support the standard.

Apple has been the standard-bearer for consumer privacy marketing. iOS 26.5 is a case where the marketing is backed by a genuine technical commitment. The green bubbles are getting a lot more private.

## What to Expect After the RC

The iOS 26.5 release candidate typically precedes the public release by approximately one week. Barring unexpected issues discovered during the RC phase, users can expect the update to arrive the week of May 11, 2026. The RCS E2EE feature will be enabled by default on supported carrier networks, with a clear in-app indicator for users to verify the status of individual conversations.

Ahead of WWDC 2026 in June, iOS 26.5 represents the last significant iOS update before the iOS 27 preview — keeping Apple's release cadence on track for a fall announcement cycle that, according to earlier reporting, will center heavily on deeper AI integration through a next-generation Siri powered by a multimodal model.
