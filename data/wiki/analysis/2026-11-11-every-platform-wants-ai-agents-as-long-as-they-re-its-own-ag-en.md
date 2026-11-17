---
category: products
lang: en
published: '2026-11-11T06:30:18.443295+00:00'
sources:
- name: Google AI Blog
  url: https://blog.google/company-news/inside-google/company-announcements/adobe-google-partnership-integration/
- name: The Verge
  url: https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/openai-rolls-out-new-business-profiles-making-chatgpt-just-a-little-bit-more-like-google/
- name: Engadget
  url: https://www.engadget.com/2312215/adobe-and-google-have-teamed-up-to-connect-drive-gmail-and-acrobat/
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/
summary: The agent economy isn't opening the web up. It's building a new set of toll
  booths, and this week we found out who's collecting the tolls.
title: Every Platform Wants AI Agents — As Long As They're Its Own Agents
trending_theme: AI Agents Reshape Commerce and Platforms
type: analysis
---

Everyone says they want AI agents to do your shopping, edit your files and run your errands. Look at what actually shipped this week, though, and "agent-friendly" turns out to mean "friendly to *my* agent." Every major move in the past ten days was either a company trying to become the agent's front door or a company bolting its own door shut.

On November 10, OpenAI launched a Business Hub (in beta) where companies can verify profiles, put up a branded business agent inside ChatGPT and see analytics on profile views, mentions and clicks. The same day at Adobe MAX in Miami, Adobe released a local MCP server that exposes Photoshop, Illustrator, After Effects and Premiere to ChatGPT, Claude and Gemini. Adobe also announced a wider Google partnership that puts Acrobat inside Gmail and Drive and puts Adobe's tools into Gemini Enterprise and Google Search's AI Mode. Meanwhile eBay quietly started blocking Meta's Muse agent from even *browsing* listings, and Apple has been tightening Full Disk Access on macOS while it builds an agentic Siri of its own.

These look like separate stories. They are the same story.

## The front door is the business model

Every computing era has one company that controls how users find things, and that company collects the tolls. In the 2000s it was Google search. Alphabet's search and other revenue reached roughly $198 billion in 2024, and the antitrust trial showed Google paid Apple about $20 billion in 2022 just to stay the default search engine in Safari. In the 2010s it was the app stores and their 15–30% cut. The question for the 2020s is who owns the layer where an AI agent decides which business to call, which tool to open and which listing to buy.

Read OpenAI's Business Hub with that in mind. It isn't a feature. It's Google Business Profile plus Google Analytics, rebuilt for a chat interface with about 800 million weekly users (OpenAI's number from October 2025). Verified profiles and analytics come first. You need the measurement layer before you can sell the ad layer. I'd bet sponsored placement inside business agent answers is on OpenAI's roadmap, and that it ships before the end of 2027.

The tell is what OpenAI gave up. Its Instant Checkout effort, launched in September 2025 with Etsy and Shopify merchants and run on a commission model, was quietly retired in March 2026, cart and all. OpenAI tried to be Amazon and it didn't work. Now it's trying to be Google, which is a far better business: Google doesn't need to hold inventory, handle returns or win on price. It only needs businesses to believe they can't afford to be invisible there.

## Adobe's bet: be the tool, not the destination

Adobe is running the opposite play, and it's the smarter one for a company in its position. Adobe has spent two years watching generative AI threaten to commoditize the craft its subscriptions are built on. Its answer is to be inside every agent, including rival ones.

Look at the sourcing. Adobe already offers third-party models from Google, OpenAI, Runway, ElevenLabs, Black Forest Labs, Kling and ByteDance. It added Topaz Labs' Wonder 4 and ImageHDR after buying Topaz. Now its MCP lets Claude or ChatGPT drive Photoshop directly. Adobe VP Deepa Subramaniam told TechCrunch the company has "no need or desire to sort of limit what the MCP endpoint can expose."

That openness is calculated. If the user's starting point moves to a chat window, Adobe wants to be the default verb inside it: "edit with Acrobat," "open in Photoshop." The Google deal makes this concrete, with Acrobat as a suggested app in Drive and Gmail file previews. Google gets its models into Photoshop. Adobe gets distribution in the two apps billions of people already have open. Both are hedging against Microsoft's Copilot-plus-Office stack and against OpenAI becoming everyone's home screen.

## The gatekeepers' counterattack

Now the other side. eBay changed its user agreement in January 2026 to ban "buy-for-me agents" and "LLM-driven bots" that place orders without human review. Until recently agents could still browse. That stopped. When *The Verge* tested Muse, it sometimes sent users to third-party sites that mirror eBay listings instead. eBay's spokesperson said the company takes a "selective approach" and is "evaluating ways third-party agents could help new customers discover eBay's unmatched inventory."

Translated: eBay isn't against agents. It's against *unpaid* agents. "Selective" means "we're negotiating."

Amazon is further along. It blocks outside agents from browsing or shopping, and in November 2025 it sued Perplexity over the Comet browser's shopping agent. Amazon's position makes sense: it earned roughly $56 billion in advertising in 2024, nearly all of it from sponsored placements that a human sees while scrolling. An agent that reads the page, skips the sponsored slots and buys the cheapest acceptable item is an ad blocker with a credit card. Target falls in between, blocking agents some of the time. Shopify, which has no consumer storefront to protect, has been the most open of the large commerce platforms, because its merchants want to be found anywhere.

Apple is doing the same thing at the operating-system level. Tighter Full Disk Access means third-party agents get less free run of your Mac. Agentic Siri means Apple's own agent gets the access through App Intents. The control just moves to Apple.

## What nobody is talking about: MCP is becoming the new robots.txt

The industry is celebrating MCP as an open standard, and the protocol itself is open. Access through it isn't.

Look at what Adobe actually shipped. It's a *local* MCP, and Adobe decides which endpoints exist. Today it's generous. But an MCP server is a permissions layer the platform controls. The vendor can meter it, tier it by subscription, rate-limit it, or turn on endpoints only for partners who pay. In practice it's robots.txt with an API key, and robots.txt never stopped anyone. The API key will.

This is where the eBay and Adobe stories meet. Scraping (Muse reading eBay's HTML) is the uncontrolled channel, and every platform is closing it. MCP endpoints, verified business agents and signed partnership deals are the controlled channels, and every platform is opening them. The "open agentic web" is turning into a set of bilateral agreements, which is how the 2010s app economy worked too.

Second-order effect: small merchants and indie developers end up with less agent reach than they had with Google SEO, not more. Being found by an agent will depend on being in the right partner program, not on having a good webpage.

## The bear case

The honest counterargument is that the gatekeepers may be right to stay calm, because agent commerce might simply not be a big deal yet. OpenAI's checkout was retired after about six months. *The Verge*'s Muse user was building a daily watch digest, which is a hobbyist workflow, not a mass-market habit. If agents send little real purchase volume, eBay and Amazon lose nothing by blocking them, and OpenAI's Business Hub becomes a vanity dashboard that businesses fill out once and forget.

I take that seriously, but it misreads the timing. Gatekeepers don't block things that don't matter. Amazon doesn't hire litigators over a rounding error. The blocks are coming *before* the volume because incumbents learned from the 2000s: once users get used to an intermediary, that intermediary sets the terms. eBay watched Google turn into its biggest customer-acquisition cost. It doesn't want to repeat that with OpenAI.

## What to Watch

1. **Ads in ChatGPT's business layer by H2 2027.** Business Hub analytics are the groundwork for sponsored business-agent placements. Watch for a "promoted" label within 12 months.
2. **eBay signs a paid agent deal within a year.** "Selective approach" plus "ongoing discussions with potential partners" means a deal is coming, most likely with Google or OpenAI, not Meta.
3. **Adobe's MCP gets tiered.** Expect endpoint access tied to Creative Cloud plan level by MAX 2027. "No desire to limit" will turn into "Pro endpoints."
4. **Amazon stays fully closed and pushes its own agents** (Rufus, Buy for Me) harder. It's the one retailer big enough to never need a third-party front door.
5. **Apple's agentic Siri runs through App Intents only.** Apps that adopt App Intents get Siri traffic. Agents that rely on screen-reading get squeezed out of macOS and iOS through permission changes, not public bans.

The winners of the agent era won't be the companies with the smartest agents. They'll be the ones that decide which agents get in.