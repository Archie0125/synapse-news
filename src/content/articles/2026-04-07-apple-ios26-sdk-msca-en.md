---
title: "Apple Sets April 28 iOS 26 SDK Deadline as EU Forces Open App Distribution"
summary: "Apple has announced that all App Store submissions must use the iOS 26 SDK starting April 28, 2026, forcing developers to update their toolchains. Simultaneously, EU Mobile Software Competition Act compliance in iOS 26.2 is unlocking alternative app marketplaces, third-party payment processing, and independent distribution for the first time — the biggest structural change to the App Store since its 2008 launch."
category: "developer-tools"
publishedAt: 2026-04-07
lang: "en"
featured: false
trending: true
sources:
  - name: "Apple Developer News and Updates"
    url: "https://developer.apple.com/news/"
  - name: "Built In: 12 Tech Laws Taking Effect in 2026"
    url: "https://builtin.com/articles/tech-laws-2026"
  - name: "TechPolicy.Press: March 2026 US Tech Policy Roundup"
    url: "https://www.techpolicy.press/march-2026-us-tech-policy-roundup/"
tags:
  - "Apple"
  - "iOS 26"
  - "App Store"
  - "EU regulation"
  - "MSCA"
  - "developer tools"
  - "alternative marketplaces"
relatedSlugs:
  - "2026-04-04-eu-ai-act-enforcement-en"
  - "2026-04-05-apple-business-platform-en"
---

# Apple Sets April 28 iOS 26 SDK Deadline as EU Forces Open App Distribution

Two separate but interconnected forces are reshaping how developers build and distribute iOS apps in 2026. Apple has set **April 28** as the deadline for all App Store Connect submissions to use the **iOS 26 / iPadOS 26 SDK**, requiring developers worldwide to update their build toolchains. And in Europe, Apple is implementing the most structurally significant changes to its platform economics since the App Store launched in 2008 — this time compelled not by business strategy but by law.

## The SDK Deadline: What It Means for Developers

The April 28 requirement is, in one sense, routine. Apple has enforced SDK minimums for years, progressively retiring older toolchains to ensure the App Store reflects current platform capabilities. The transition to iOS 26 SDK is no different in mechanism, but it lands at a moment when iOS 26 itself introduces a substantially expanded feature set — including a revamped SwiftUI layout engine, native AI inference APIs tied to Apple Intelligence 2.0, and new real-time audio and video processing primitives.

Developers who have not yet migrated to Xcode 17.3 or later — the release that includes the iOS 26 SDK — face a hard cutoff. As of April 28:

- **New app submissions** must be built with the iOS 26 SDK
- **App updates** must also comply; submitting an update to an existing app with an older SDK will be rejected
- **Extension bundles** (widgets, app clips, live activities) must likewise target the new SDK

The practical implication for large app teams is non-trivial. Testing against a new SDK often surfaces deprecation warnings that become hard failures — particularly around UIKit APIs that Apple has been gradually sunset in favor of SwiftUI, and around privacy manifest requirements that were tightened in iOS 26. Teams that deferred SDK updates through the iOS 26 beta cycle now face a compressed sprint to certify and ship.

For smaller studios and solo developers, the calculus is simpler: update Xcode, re-run tests, fix whatever breaks. Apple's migration guides have improved substantially over recent releases, and the iOS 26 SDK ships with a compatibility mode for most deprecated UIKit patterns.

## MSCA: Europe's App Store Reformation

While the SDK deadline affects all developers globally, the Mobile Software Competition Act (MSCA) changes — arriving in **iOS 26.2**, expected in late Q2 — are geographically constrained to the European Economic Area but structurally consequential for the entire industry.

The MSCA, which passed the European Parliament in 2024 and entered into force in early 2025, requires Apple to allow:

1. **Alternative app marketplaces**: Third-party entities — developers, retailers, platform operators — may now operate their own app stores on iOS in Europe. Users can install these marketplaces directly and download apps through them, bypassing App Store curation and search entirely.
2. **Third-party payment processing**: Apps distributed through any channel (including the App Store itself) may offer payment processing by third parties — Stripe, PayPal, local PSPs — for digital goods, without routing through Apple's In-App Purchase system.
3. **Sideloading via developer-operated channels**: Larger developers may distribute apps directly to European users from their own infrastructure, without going through any marketplace intermediary.

These changes parallel — and go further than — what Apple implemented in the EU under the Digital Markets Act (DMA) starting in early 2024. The DMA opened sideloading in principle; the MSCA enforces more specific interoperability requirements and extends the obligations to a broader set of platform behaviors.

## Apple's Response: Controlled Opening

Apple has not embraced these changes warmly, and its implementation approach reflects that ambivalence. The company has designed a series of friction points that technically comply with MSCA requirements while preserving as much of its platform control as legally permissible:

**Notarization requirements**: Apps distributed through alternative marketplaces must still pass Apple's notarization process — a security review that checks for malware and certain policy violations. Apple has argued this is necessary for user safety; critics argue it gives Apple an effective veto over alternative marketplace offerings.

**New commission structure**: Apple has introduced a "Core Technology Fee" for alternative marketplace apps — a per-install charge (currently set at €0.50 per install beyond the first million annually) that applies regardless of whether the developer uses Apple's payment system. Large-volume free apps, particularly social media platforms and games, have pushed back hard, arguing the fee is designed to make alternative distribution economically unviable.

**Limited API access**: Some platform APIs — particularly those related to Secure Enclave, certain NFC capabilities, and health data integrations — remain unavailable to apps distributed outside the App Store under current MSCA compliance rules, which Apple maintains are justified on security grounds.

The European Commission is monitoring Apple's compliance and has already opened an investigation into whether the Core Technology Fee constitutes a circumvention of the spirit of the MSCA. A ruling is expected later this year.

## Developer Economics: A New Calculus

For app developers, particularly those with large European user bases, the MSCA changes require a genuine strategic rethinking. The decisions are not simple:

**Should you move to an alternative marketplace?** The economics depend heavily on your revenue model. If you're a subscription app paying Apple's 15-30% commission, moving to an alternative marketplace with a third-party PSP could save tens of millions of euros annually — minus the Core Technology Fee and the cost of running your own payment and distribution infrastructure. For large apps, this is often worthwhile. For small apps, the overhead may not be.

**Should you operate your own marketplace?** Several large platform operators — Epic Games, Spotify, and at least one major European publisher — have announced intentions to operate their own iOS app marketplaces in Europe. This gives them full control over distribution, discovery, and monetization for their app ecosystems, but requires investment in infrastructure and compliance.

**Should you use third-party payment processing in the App Store?** This option is available even for App Store-distributed apps under MSCA. Apple's revised fee structure for in-App Store third-party payments still applies a reduced platform fee (lowered from 30% to approximately 12-17% depending on subscription tier), which may not be attractive enough to justify switching PSPs for many developers.

## Global Implications

The MSCA's influence is unlikely to stay within European borders. When significant regulatory frameworks reshape platform economics in a major market, developers begin building two-tier distribution architectures — one for Europe, one for everywhere else — and those architectures create pressure for global policy alignment.

The US has its own regulatory process underway. The Open App Markets Act has been repeatedly introduced in Congress, and state-level legislation in California and New York has applied pressure on mobile platform operators. Apple's concessions in Europe create a precedent that US legislators and courts are watching closely.

For developers building new apps today, the emerging reality is that iOS distribution is no longer a single, monolithic channel. Planning for multiple distribution paths — including the possibility of alternative marketplaces gaining meaningful traction in Europe and eventually elsewhere — is now part of responsible platform strategy.

The April 28 SDK deadline is the near-term forcing function. The longer-term transformation of the App Store as an institution is just beginning.
