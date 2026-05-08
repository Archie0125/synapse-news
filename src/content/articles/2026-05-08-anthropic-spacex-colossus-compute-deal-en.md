---
title: "Anthropic Signs SpaceX's Colossus 1 for 220,000 GPUs, Doubles Claude Code Rate Limits"
summary: "Anthropic announced on May 6 that it has secured the entire computing capacity of SpaceX's Colossus 1 data center — originally built to run xAI's Grok — giving the AI safety company access to over 300 megawatts and 220,000 Nvidia GPUs within a month. The deal prompted Anthropic to immediately double Claude Code's rate limits and remove peak-hour caps, while the company revealed it is also exploring space-based AI compute with SpaceX."
category: "ai-ml"
publishedAt: 2026-05-08
lang: "en"
featured: true
trending: true
sources:
  - name: "Anthropic Blog"
    url: "https://www.anthropic.com/news/higher-limits-spacex"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html"
  - name: "Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/anthropic-to-use-all-of-spacex-xais-colossus-1-data-center-compute/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-05-06/anthropic-inks-computing-deal-with-spacex-to-meet-ai-demand"
tags:
  - "Anthropic"
  - "SpaceX"
  - "Claude"
  - "Claude Code"
  - "Colossus"
  - "GPU compute"
  - "AI infrastructure"
relatedSlugs:
  - "2026-05-07-anthropic-44b-arr-claude-code-growth-en"
  - "2026-05-07-anthropic-goldman-blackstone-enterprise-ai-en"
---

Sometime in the past six months, Claude Code became something that Anthropic's own infrastructure could no longer keep up with. On May 6, 2026, the AI safety company announced an unusual fix: it has secured the full computing capacity of Colossus 1, a data center built and owned by SpaceX that was originally constructed to power xAI's Grok models, and will use it to dramatically expand the compute available to Claude users. The deal is a reminder that in the current AI era, the infrastructure constraints are often more binding than the models themselves.

## What Colossus 1 Brings

The numbers are striking. Colossus 1 gives Anthropic access to more than 300 megawatts of power capacity across more than 220,000 Nvidia GPUs, all expected to come online for Anthropic's workloads within a month of the announcement. For context, that is roughly comparable to a mid-sized hyperscaler's dedicated AI training cluster — handed to a company that, until recently, was primarily known for running lean on compute relative to its rivals.

The deal is structured through SpaceX rather than xAI directly, reflecting SpaceX's role as the owner and operator of the Colossus 1 physical facility. The arrangement also has a forward-looking component: Anthropic disclosed it has "expressed interest" in working with SpaceX to explore multiple gigawatts of compute capacity deployed in space — an ambitious framing that signals the relationship extends well beyond an emergency capacity arrangement.

## Immediate Impact: Rate Limits Doubled

Anthropic moved fast to translate the new capacity into user-facing benefits. Alongside the infrastructure announcement, the company confirmed it is doubling Claude Code's rate limits across all paid subscription tiers — Pro, Max, Team, and Enterprise — and removing the peak-hour usage caps that had frustrated developers working within the tool's previous constraints.

The peak-hour cap removal is particularly meaningful. Claude Code had been experiencing the kind of demand spike characteristic of genuinely viral developer adoption: rapid enough that even periods of moderate global usage could bump users into rate limits during peak hours in certain regions. Removing that ceiling, even temporarily, signals that Anthropic now has enough compute headroom to operate Claude Code more like an always-on infrastructure service rather than a usage-rationed API.

This matters commercially. Claude Code's explosive growth has been the primary driver of Anthropic's revenue acceleration, with the tool's annualized revenue contribution reportedly crossing significant milestones in early 2026. Every rate limit hit is a lost customer moment; doubling limits and removing peak-hour caps directly addresses the friction most likely to drive enterprise customers toward alternative tools.

## A Competitor's Compute

The most striking aspect of the deal is its counterintuitive structure. Anthropic is, broadly speaking, a competitor to xAI — both companies are racing to build frontier AI models, and both are vying for enterprise customers, developer mindshare, and capital. Colossus 1 was built by SpaceX specifically to power xAI's training runs.

The fact that Anthropic is now running its workloads through that same facility is a reminder that the AI infrastructure market has not yet consolidated around ideological boundaries. Compute is fungible, and available capacity is scarce. SpaceX, as the facility's owner and operator, has every incentive to monetize Colossus 1's capacity productively, regardless of which AI company is writing the checks.

There is also a structural logic: xAI's Grok development cadence fluctuates, creating windows of underutilization at Colossus 1. Leasing that idle capacity to Anthropic generates revenue for SpaceX from infrastructure that would otherwise sit partially idle. For Anthropic, it solves an urgent supply problem without the 18-to-24-month lead time required to build equivalent owned infrastructure from scratch.

## Layering on Top of AWS

The SpaceX deal is the latest addition to an increasingly diversified compute strategy at Anthropic. In April 2026, the company announced an expanded partnership with Amazon Web Services for up to 5 gigawatts of AI infrastructure capacity, including nearly 1 gigawatt of AWS Trainium 2 compute expected to be available by the end of 2026.

The multi-provider approach makes strategic sense. AWS gives Anthropic access to Trainium, Amazon's custom AI training chip, reducing dependency on Nvidia GPU allocations for certain workloads. SpaceX's Colossus 1 provides immediate Nvidia GPU capacity for inference-heavy workloads like Claude Code. And Anthropic continues to pursue its own preferred cloud partnerships for specific product lines.

This architecture hedges against the single-provider concentration risk that has created operational vulnerability for other AI companies during demand spikes. It also gives Anthropic negotiating leverage: no single infrastructure partner can hold the company hostage on pricing or availability.

## The Space Compute Angle

The mention of potential space-based compute is easy to dismiss as futurism, but deserves careful reading. SpaceX is uniquely positioned to explore this thesis: the company operates the world's most advanced commercial launch capability and has already deployed thousands of Starlink satellites that process significant data loads in orbit.

Moving AI compute to space would theoretically solve several significant constraints: real estate for data centers, the environmental impact of terrestrial power consumption, and — in theory — global latency by routing inference through satellites in low Earth orbit. None of these benefits are close to realization at the infrastructure scale required for frontier AI, but the partnership creates a natural R&D pathway to explore the concept seriously.

For Anthropic, expressing interest in space compute serves a secondary purpose beyond pure technical exploration: it signals the company's intent to stay ahead of infrastructure constraints over a longer time horizon, even as the near-term focus remains on scaling terrestrial capacity as fast as humanly possible.

## What This Signals for the AI Compute Market

The Anthropic-SpaceX deal highlights a dynamic that is reshaping how AI companies think about infrastructure strategy. The frontier AI race has moved so quickly that no single company — including the hyperscalers — can build capacity fast enough purely through owned infrastructure. The result is a market where unusual partnerships form across what would historically have been competitor lines, and where underutilized capacity at one company becomes a strategic asset for another.

For developers and enterprises relying on Claude Code, the immediate takeaway is simple: the compute ceiling that was throttling productivity has been substantially raised, and the peak-hour frustrations that punctuated the prior several months should ease significantly within weeks.

The longer-term implication is more structural. Anthropic, having crossed $44 billion in annualized revenue and accelerating, is now constructing an infrastructure stack commensurate with its ambitions — one that mixes owned capacity, hyperscaler partnerships, competitor facility leases, and potentially orbital compute in a configuration that no one would have predicted a year ago.
