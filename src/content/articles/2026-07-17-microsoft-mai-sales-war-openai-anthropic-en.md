---
title: "Microsoft Declares Internal War on OpenAI and Anthropic, Training Sales Teams to Bury Former Partners"
summary: "Microsoft held an internal FY2027 strategy session in mid-July where executives trained sales teams to explicitly compete against OpenAI, Anthropic, and Google — calling Claude 'slower and less accurate' — while simultaneously migrating Excel and Outlook from third-party AI models to its own proprietary MAI stack. The move signals the definitive end of Microsoft's era as a neutral AI distributor."
category: "industry"
publishedAt: 2026-07-17
lang: "en"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/15/microsoft-is-reportedly-training-salespeople-to-talk-down-openai-and-anthropic/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-07-07/microsoft-replaces-openai-anthropic-with-own-ai-in-some-apps"
  - name: "CryptoBriefing"
    url: "https://cryptobriefing.com/microsoft-sales-teams-compete-openai-anthropic-google/"
  - name: "Benzinga"
    url: "https://www.benzinga.com/markets/tech/26/07/60490610/microsoft-wants-sales-team-to-push-its-own-ai-models-instead-of-rivals-openai-google-and-anthropic-report"
tags:
  - "microsoft"
  - "openai"
  - "anthropic"
  - "mai-models"
  - "enterprise-ai"
  - "competitive-strategy"
relatedSlugs:
  - "2026-07-07-microsoft-mai-thinking-1-code-1-flash-launch-en"
  - "2026-07-13-anthropic-overtakes-openai-revenue-47b-en"
---

Something fundamental changed at Microsoft this week. In an internal planning session held July 14-15 to kick off fiscal year 2027, the company's senior leadership trained its global sales force to do something that would have been unthinkable eighteen months ago: explicitly position Microsoft's own AI models as superior to those of OpenAI, Anthropic, and Google — and to say so directly to enterprise customers.

The session, first reported by Bloomberg and confirmed by multiple sources familiar with the briefing, was not a subtle shift in emphasis. Copilot Executive Vice President Jacob Andreou reportedly characterized Anthropic's Claude model as "slower and less accurate" when used inside Microsoft Office applications. That kind of specific, named criticism of a partner company's product — in an internal corporate training — is extraordinary in the enterprise software world, where strategic relationships are normally handled with more care.

## The Strategy: Stop Selling Parts, Start Selling the Whole System

Executive Vice President Jay Parikh, one of the primary architects of Microsoft's internal AI strategy, framed the new fiscal year pitch around a deceptively simple idea: Microsoft sells the full end-to-end AI system. Rivals — including OpenAI, which Microsoft has invested roughly $13 billion in, and Anthropic, which its own hardware ecosystem hosts — sell only components.

The logic is coherent on its face. Microsoft has Azure (the cloud), Copilot (the application layer), Microsoft 365 (the productivity surface), GitHub Copilot (the developer surface), and now the MAI model family (the intelligence layer). An enterprise that buys into the Microsoft stack gets all of these integrated. An enterprise that buys a Claude or GPT-5 API subscription gets a model — and then has to build the rest themselves.

What's new is that Microsoft is now actively selling against the model vendors rather than treating them as complementary. The internal session reportedly included specific competitive talk tracks comparing MAI performance and cost against named competitors. Salespeople were reportedly told to lead with the security and compliance advantages of keeping AI inference inside Microsoft's own infrastructure, rather than routing to Anthropic's or OpenAI's external API endpoints.

## The Technical Ground Shift Already Underway

This competitive pivot didn't arrive from nowhere. Since July 7, Microsoft has been actively migrating selected Microsoft 365 applications — starting with Excel and Outlook — from OpenAI and Anthropic model backends to its own MAI stack. The company's MAI models (Thinking 1, Code 1, and Flash, announced in early July) handle "tens of thousands" of AI-assisted prompts per week across these applications, according to figures cited internally.

The migration is both strategic and financial. Every prompt routed through the MAI stack instead of an OpenAI or Anthropic API call is a cost Microsoft keeps rather than paying to a partner. At scale — across hundreds of millions of Microsoft 365 users — the economics become massive. Analysts estimate that at mid-tier API pricing, even routing 5% of Office AI workloads to internal models could save Microsoft several billion dollars annually in API costs, while simultaneously generating data that improves its own models.

The product quality bar for internal models also appears to have cleared a threshold that gives Microsoft confidence to make this move. Code 1, Microsoft's coding model, has been evaluated by internal benchmarks against Claude Sonnet 5 and GPT-5.6 Sol — and while it doesn't beat either across the board, it performs comparably on the specific task distributions most common in Office applications: document summarization, formula generation, email drafting, and data analysis.

## What This Means for OpenAI

The OpenAI relationship is the most complicated piece. Microsoft is simultaneously OpenAI's largest investor ($13 billion), its primary cloud provider, and now its explicit sales competitor. OpenAI's enterprise products — ChatGPT Work, the GPT-5.6 API, operator tiers — compete directly with Microsoft Copilot for the same enterprise buyers. And those buyers are now being briefed by Microsoft sales teams on why they should choose Copilot over ChatGPT Work.

The relationship has been fracturing for months. Microsoft's early 2026 decision to launch its own MAI model family was the first public signal that the partnership had limits. The July strategy session makes those limits explicit: Microsoft will continue to offer OpenAI models as an option in Azure (it still makes money from that), but its sales organization is now oriented around winning the enterprise AI platform war against everyone, including its biggest AI investment.

For OpenAI, which is targeting an IPO as early as September at a valuation north of $700 billion, this is not a trivial complication. Enterprise revenue is a critical part of the IPO story, and having Microsoft's sales force explicitly pitch against your products changes the competitive dynamics in a market where Microsoft has extraordinary incumbent leverage.

## What This Means for Anthropic

Anthropic finds itself in an interesting position. Its revenue has grown dramatically — it recently overtook OpenAI in annualized run rate, approaching $47 billion — driven primarily by Claude Code adoption and enterprise API contracts. But a meaningful portion of that enterprise deployment happens through Microsoft Azure, which hosts Claude models via its AI marketplace.

If Microsoft sales teams are now characterizing Claude as "slower and less accurate" in Office contexts, the immediate threat is to the subset of enterprise customers who might have chosen Claude-via-Azure for Microsoft 365 integration specifically. Anthropic's direct API business, and its partnerships with Amazon, Google Cloud, and Salesforce, are unaffected. But the Azure channel — which had been a significant distribution lever — now operates in an environment where the channel owner is actively hostile.

Anthropic has not publicly commented on the Microsoft session.

## Google Gets Hit Too

The briefing apparently didn't spare Google. Gemini-via-Azure and Gemini-on-Google-Cloud are now competing for the same enterprise budgets that Microsoft Copilot targets. Google's own enterprise AI push — centered on the newly launched Gemini 3.5 Pro and its Gemini Enterprise Agent Platform — puts it in direct competition with Microsoft in the same market segment. The Microsoft sales session reportedly included competitive materials positioning MAI as more cost-effective and less latency-prone than Gemini for Office-integrated workflows.

## The Larger Pattern

Zoom out and what you're watching is the inevitable endpoint of a phase that began in 2022 when Microsoft made its landmark OpenAI investment. The partnership model — Microsoft provides cloud, OpenAI provides intelligence, both win — worked beautifully while AI capabilities were nascent and the market was expanding fast enough for everyone to grow. By mid-2026, with a defined set of enterprise AI budgets and a maturing set of capable models across multiple providers, the partnership has become a competitive constraint for Microsoft.

The company's move to build its own models, train its sales force to sell against its former partners, and migrate its highest-volume applications to internal infrastructure is classic vertical integration strategy — the same playbook Microsoft has run in operating systems, browsers, and productivity software across three decades. What's different this time is the speed, the stakes, and the fact that its "former partner" is simultaneously its most prominent AI investment and, probably, its most capable external model provider.

The enterprise AI platform market is worth, by various estimates, $200-400 billion in annual spend by 2028. Microsoft is not content to be the cloud that others win that market on. It wants to win it directly.
