---
title: "Google and SpaceX Are Reportedly in Talks to Put AI Data Centers in Orbit"
summary: "The Wall Street Journal reports that Google and SpaceX are in advanced talks to launch orbital AI data centers into space, with Google's Project Suncatcher satellite initiative as a backdrop. The potential deal comes as SpaceX prepares for an IPO later this year that some analysts expect could value it at nearly $1.75 trillion."
category: "hardware"
publishedAt: 2026-05-14
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: true
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/12/report-google-and-spacex-in-talks-to-put-data-centers-into-orbit/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-05-12/google-in-talks-to-use-spacex-to-launch-space-data-centers-wsj"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reportedly-in-talks-with-spacex-to-launch-its-orbital-data-centers-partnership-could-mark-a-historic-turning-point-and-boost-upcoming-ipo"
  - name: "Tech Startups"
    url: "https://techstartups.com/2026/05/13/google-and-spacex-in-talks-to-launch-orbital-ai-data-centers-into-space/"
tags:
  - "Google"
  - "SpaceX"
  - "orbital data centers"
  - "AI infrastructure"
  - "Project Suncatcher"
  - "cloud computing"
  - "space tech"
relatedSlugs:
  - "2026-05-11-spacex-cursor-60b-acquisition-en"
  - "2026-05-13-google-googlebook-ai-laptop-en"
---

For decades, the computing industry has organized itself around a simple premise: put your servers somewhere cheap, cool, and reliably connected to power. That premise is now under serious pressure. According to a report from The Wall Street Journal, Google and SpaceX are in advanced discussions to do something that would have seemed like science fiction five years ago — launch AI data centers into Earth's orbit.

The talks, first reported on May 12, 2026, come at an extraordinary moment. SpaceX is preparing for an IPO later this year that some analysts expect could value it at nearly $1.75 trillion, and the company is pitching orbital infrastructure to investors as the cheapest place to put AI compute within the next few years. For Google, whose AI ambitions have bumped hard against the limits of terrestrial expansion — land, power, water, permitting — space offers a way to break the constraint entirely.

## Why Space, and Why Now

The fundamental problem with AI infrastructure is that it keeps getting bigger faster than the world can build to accommodate it. Meta, Amazon, Microsoft, and Alphabet have collectively signaled roughly $725 billion in capital expenditures for 2026, almost entirely earmarked for data centers, custom chips, and GPUs. But that money can't conjure land in proximity to fiber backbones, it can't resolve municipal permitting battles overnight, and it can't make renewable energy abundant everywhere that compute needs to be.

Orbital data centers sidestep several of these problems in one move. Satellites in low Earth orbit (LEO) could draw uninterrupted solar energy, easing the power constraint that has become one of the biggest bottlenecks for terrestrial AI expansion. They also bypass land acquisition entirely and circumvent a growing wave of community opposition to large data center developments in suburban and rural areas.

SpaceX is selling investors on the idea that orbital data centers will be the cheapest place to put AI compute within the next few years. That's a bold assertion, but it's grounded in a real trend: SpaceX has driven per-kilogram launch costs down by more than 90% compared to the pre-Falcon 9 era, and the next-generation Starship system promises to push costs down further still.

## Project Suncatcher: Google's Long Bet

Google has not been idle on this front. The company announced **Project Suncatcher** late last year, an internal orbital-computing effort focused on space-based data centers. The project takes its name from the satellite's ability to capture unobstructed solar energy in orbit, which it would then use to power high-density AI compute hardware.

Google plans to launch prototype satellites by 2027 as part of Project Suncatcher, according to reports.

Google's existing financial relationship with SpaceX provides useful context. Google's existing financial relationship with SpaceX provides useful context: according to regulatory filings, Google invested $900 million in SpaceX in 2015. That relationship gives Google both an informational edge about SpaceX's capabilities and a financial incentive to see the IPO succeed at a high valuation.

## Anthropic Is Already in the Conversation

Google and SpaceX are not having this conversation in isolation. Reporting this week also revealed that Anthropic has struck a deal with SpaceX to use computing resources from xAI's data center in Memphis, Tennessee — and that the partnership explicitly contemplates expansion to orbital facilities in the future. (SpaceX acquired xAI, Elon Musk's AI company, in February 2026.)

The emergence of SpaceX as a central figure in AI compute supply — serving simultaneously as Google's infrastructure partner, Anthropic's compute provider, and the operator of xAI's own models — creates a novel and potentially uncomfortable concentration of leverage. SpaceX would, in this scenario, be supplying compute to competing AI labs while its own affiliated model (xAI's Grok series) competes in the same market. The conflicts of interest are obvious; whether regulators will eventually scrutinize them is an open question.

## The Engineering Challenges Are Real

Enthusiasm for orbital data centers is warranted, but so is a clear-eyed look at what remains unsolved. The engineering challenges are significant and only partially analogous to the problems that have already been solved for terrestrial infrastructure.

**Radiation hardening** is the most acute. The processors that underpin modern AI training and inference — NVIDIA's H100 and its successors — are not designed for the radiation environment of low Earth orbit, where charged particles can cause bit flips and accelerated transistor degradation. Google and SpaceX would either need to use radiation-hardened custom silicon (which currently runs substantially behind commercial ASIC performance) or develop novel shielding approaches.

**Thermal management** in orbit is counterintuitive: while space is extremely cold, there is no atmosphere to carry heat away from a computing cluster via convection. All heat must be radiated, which requires large surface-area radiator panels — adding to a satellite's mass and complexity. Google's prototype program will partly be a testing ground for how well these thermal architectures perform at AI workload densities.

**Latency** is a genuine constraint for certain AI workloads. Satellites in LEO orbit at altitudes of roughly 300-600 km, adding round-trip signal latency of approximately 10-20 milliseconds — acceptable for training workloads that don't require interactive latency, but potentially significant for real-time inference applications. Starlink's ground-station network could help minimize hops, but it cannot eliminate the physics of the orbital altitude.

**Launch costs and cadence** remain the most important variable. SpaceX's Starship, which has the potential to launch payload at a cost approaching $100 per kilogram at full reusability, is still in development and has experienced setbacks. The commercial viability of orbital AI infrastructure depends heavily on Starship achieving its cost targets.

## What This Means for the Cloud Industry

For Amazon Web Services, Microsoft Azure, and the rest of the terrestrial cloud incumbents, the Google-SpaceX discussions represent a new front in infrastructure competition that they are not currently positioned to participate in. None of the other hyperscalers have a comparable launch partnership or orbital infrastructure program at a similar stage of development.

Microsoft's long-standing partnership with SpaceX via Azure Orbital — a ground-station-as-a-service offering — gives it some proximity to the relationship, but Azure Orbital is a networking service, not a compute hosting arrangement. Amazon has its own launch ambitions via Blue Origin, but Jeff Bezos's rocket company has consistently lagged SpaceX by years on launch cadence and cost reduction.

If Google successfully deploys orbital AI infrastructure at commercial scale in the 2027-2029 window, it would be the most significant new axis of differentiation in cloud computing since the introduction of custom ASICs like Google's TPUs. And unlike TPUs, orbital compute would be difficult for competitors to replicate quickly.

## The IPO Angle

It would be naive to ignore the timing. SpaceX's IPO is expected later this year, and the company has every incentive to surface the most compelling vision of its commercial future in the run-up to pricing. A publicly announced agreement with Google to develop orbital AI infrastructure would serve as powerful evidence that SpaceX's space infrastructure ambitions have Fortune 500 validation.

The $1.75 trillion target valuation implies that investors are being asked to value SpaceX not just on its existing Starlink revenue (which reportedly exceeded $10 billion in 2025) but on the long-term potential of a much larger space economy. Orbital AI data centers are precisely the kind of transformative infrastructure story that justifies a multiple like that.

Whether the talks will result in a formal announcement before the IPO remains unknown. What is clear is that the conversation is real, the technology roadmap is credible, and the economic logic — at least at the level of first principles — is compelling. The cloud industry's next frontier may literally be above the clouds.

*Correction (November 15, 2026): 10 sentences were corrected or removed to match the sources listed on this page.*
