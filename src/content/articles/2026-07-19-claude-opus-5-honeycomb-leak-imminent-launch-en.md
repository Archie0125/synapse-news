---
title: "Claude 'Honeycomb' Leaked in Cursor — Anthropic's Opus 5 Is Almost Here"
summary: "A mystery model called 'Claude Honeycomb EAP' briefly appeared in Cursor's production model picker on July 8, revealing a 1-million-token context window and an 'xhigh' reasoning tier. As Fable 5's free subscription window closes today, all signs point to Anthropic's next frontier model being days away."
category: "ai-ml"
publishedAt: 2026-07-19
lang: "en"
featured: true
trending: true
sources:
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/320265/20260712/fable-5-free-through-july-19-anthropic-blinks-again-opus-5-leak-surfaces-cursor.htm"
  - name: "The New Stack"
    url: "https://thenewstack.io/fable-5-honeycomb-opus/"
  - name: "WinCentral"
    url: "https://thewincentral.com/claude-opus-5-leak-1m-context-window-launch/"
  - name: "Valletta Software"
    url: "https://vallettasoftware.com/blog/post/claude-opus-5-release-date"
  - name: "KuCoin"
    url: "https://www.kucoin.com/news/flash/anthropic-preparing-claude-opus-5-for-potential-release-this-week"
  - name: "AIToolsRecap"
    url: "https://aitoolsrecap.com/Blog/claude-honeycomb-eap-opus-5-anthropic-2026"
tags:
  - "Anthropic"
  - "Claude Opus 5"
  - "Honeycomb"
  - "AI Models"
  - "Frontier AI"
  - "Cursor"
relatedSlugs:
  - "2026-07-07-anthropic-fable5-exits-subscriptions-billing-change-en"
  - "2026-07-17-anthropic-blackstone-ode-ai-implementation-en"
  - "2026-07-18-anthropic-ipo-roadshow-october-2026-en"
---

For eleven days, the AI developer community has been dissecting a screenshot that lasted less than an hour. On July 8, a developer going by @chetaslua posted to X what looked like a routine screenshot of Cursor's model picker — except one of the models was labeled "Claude Honeycomb EAP." Within hours, the string was gone. Anthropic said nothing. But the AI industry spent the next week doing what it always does: reading every pixel for signal.

Today, July 19, Fable 5's free subscription access expires at 11:59 PM Pacific Time. Whatever Anthropic does next — launch Opus 5, extend free access a fourth time, or convert users to credits — happens within hours. The Honeycomb leak didn't just tease a model name. It may have told us exactly what that model is.

## What the Cursor Leak Actually Showed

Three facts about the Honeycomb EAP model are corroborated by multiple independent screenshots and developer accounts. First, the context window appeared to be 1 million tokens, matching the 2-million-token figure Anthropic introduced with Fable 5 for the extended-context tier while sitting below it at the standard level. Second, the model supported an "xhigh" effort setting — a reasoning tier one step above the "high" setting available in Claude's API today, suggesting a chain-of-thought depth significantly beyond current Opus 4.8 behavior. Third, when a safety trigger was hit during testing, the fallback model was Claude Opus 4.8, not Fable 5 — an architectural choice that implies Honeycomb is positioned between Opus 4.8 and Fable 5 in the product lineup, which is exactly where Opus 5 would slot.

The "EAP" designation — Early Access Program — is the same tag Anthropic used internally for Claude Sonnet 5 before its public announcement on June 30. The model string does not appear in any of Anthropic's public API documentation, the claude.ai interface, or the Claude Code CLI, which is consistent with a pre-announcement engineering preview that slipped into a production endpoint through a deployment mistake.

## Three Extensions and a Pattern

Anthropic's handling of the Fable 5 subscription window has been unusual by any measure. When Claude Fable 5 launched June 9 alongside Claude Mythos 5 as Anthropic's most capable publicly released model, the pricing plan included a time-limited free trial period. The original cutoff was July 7. Then July 12. Then July 19. Each extension came with minimal explanation — "community feedback" and "transition support" — but each also coincided precisely with a moment when a new competitor model arrived or when Anthropic's own release timeline appeared to shift.

Industry observers note that the extensions look less like generosity and more like schedule management. When GPT-5.6 Sol launched July 9 at OpenAI, Fable 5 free access appeared to be extended as a direct competitive response. The July 19 deadline is now the hard wall, and Anthropic appears to have nothing to extend toward: either the next model ships, or subscribers accept the credit-based billing that follows.

Prediction markets on Metaculus and Manifold Markets had, as of July 17, placed late July to early August as the most likely window for an Anthropic frontier model release — not Fable 5 level, but the next tier up. The Honeycomb name, which does not appear in any prior Anthropic communications, aligns with the company's pattern of using organic-sounding internal codenames during development before switching to the more formal Claude [tier] [version] naming convention at release.

## Why Opus 5 Would Matter

The current frontier model landscape after July's releases has grown exceptionally crowded. OpenAI's GPT-5.6 Sol, which became generally available July 9, demonstrated strong performance on long-horizon agentic benchmarks and is priced aggressively at $1 per million input tokens for the base tier. xAI's Grok 4.5, released around the same time, showed particular strength on code generation. Moonshot AI's Kimi K3, an open-weight model that arrived July 17, topped the Frontend Code Arena leaderboard hours after release — a milestone for open-weight models and a shock to the incumbent providers.

Against this backdrop, Claude Fable 5, which Anthropic launched as its most capable model, finds itself in an unusual position: it remains best-in-class on several benchmarks, particularly long-form reasoning and safety alignment, but the competitive gap has narrowed materially in less than six weeks. An Opus 5 release would reset that gap, at least on benchmarks, and signal to enterprise customers — many of whom signed contracts based on Anthropic's roadmap — that the company's research velocity remains on track.

More importantly, the leaked xhigh reasoning tier hints that Opus 5 may be Anthropic's answer to the extended-thinking trend pioneered by OpenAI's o-series and Google's Deep Think mode. Claude Fable 5's parallel reasoning approach was a significant architectural innovation, but if Honeycomb adds a sustained multi-step deliberation mode above what Fable 5 currently supports, the practical gap between Claude and its competitors on complex, multi-day agentic tasks could widen considerably.

## What to Watch

Anthropic has offered no public comment on Honeycomb. The company's practice has been to announce models on its newsroom and via API documentation simultaneously, with no pre-announcement period — which makes any timeline speculation inherently uncertain. What is certain is the product calendar: Fable 5 free access ends today, and whatever follows begins tonight.

For developers, the most relevant question is whether Honeycomb will debut as a limited EAP or as a full API release. The July 8 appearance in Cursor's production picker — a partner integration rather than Anthropic's own interface — suggests the model may be farther along in external testing than Anthropic typically acknowledges before a launch. Cursor's tight integration with Anthropic, following the deal to give Cursor users access to extended Sonnet 5 capacity, makes it the natural first surface for an EAP leak.

If Honeycomb does ship this week, it will enter a market that has changed substantially since Anthropic's last major frontier release. The open-weight offensive from Kimi K3 and the coming DeepSeek V4 weights on July 24 mean that a closed frontier model now needs to demonstrate not just benchmark superiority but a practical value proposition — something users cannot get by running a local model. Anthropic's bet, implicit in the Fable 5 architecture and likely amplified in Opus 5, is that alignment quality, long-context coherence, and agentic reliability are the dimensions that matter most to enterprise buyers. Whether that bet holds in a world where $0/month open-weight models top coding arenas is the question the next few days may begin to answer.
