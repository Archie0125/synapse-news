---
category: products
featured: true
lang: en
publishedAt: '2026-11-10T18:48:38.118522+00:00'
relatedSlugs: []
sources:
- name: Google AI Blog
  url: https://blog.google/company-news/inside-google/company-announcements/adobe-google-partnership-integration/
- name: The Verge
  url: https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping
- name: Engadget
  url: https://www.engadget.com/2312215/adobe-and-google-have-teamed-up-to-connect-drive-gmail-and-acrobat/
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/
- name: 9to5Google
  url: https://9to5google.com/2026/11/09/google-antigravity-knowledge-work/
summary: AI agents are becoming the new front end for software and shopping, and the
  companies that block them may protect today's margins while losing tomorrow's customers.
tags: []
title: 'eBay Built a Wall, Adobe Built a Door: Who Owns the Agent Layer?'
trending: true
type: analysis
---

On the same week, two companies made opposite bets on the same question. At its MAX conference in Miami on November 10, Adobe shipped a local Model Context Protocol (MCP) server that lets ChatGPT, Claude and Gemini drive Photoshop, Illustrator, After Effects and Premiere. Adobe VP Deepa Subramaniam told TechCrunch the company has "no need or desire" to limit what the endpoint exposes. Around the same time, eBay quietly stopped Meta's Muse agent from reading its listings.

One company is opening a door for agents. The other is putting up a wall. Both think they are protecting their future. Only one of them is right, and it isn't the one most people would pick.

## The interface is moving again

Software has changed hands at the interface level before. In the 2000s, the browser took over from the desktop. In the 2010s, the app store took over from the browser. Each time, the company that owned the new layer collected a toll. For Apple and Google, that toll was a 30% cut of app revenue.

The current move is from apps to agents, and you could see it all over this week's news:

- **Adobe** now appears inside Gmail and Google Drive as an "Edit with Acrobat" option. Its CX Enterprise Coworker agent runs inside Gemini Enterprise, and its tools are coming to AI Mode in Google Search.
- **Google Antigravity** started as a coding agent. It just added a "Knowledge Work" mode because, according to Google, tens of thousands of non-engineers across sales, finance, legal and marketing use it every week. The new mode hides the plumbing. MCP servers, skills and custom agents keep running in the background, but they no longer appear in the UI.
- **OpenAI** keeps pushing agents into ChatGPT's business tiers, so the chat window becomes where work starts, not just a place to ask questions.

Put those together and you get the real story. The app is turning into a backend. Users ask an agent, and the agent calls Adobe, or a spreadsheet, or a store. The brand you used to open on purpose becomes a function call you never see.

## Why Adobe chose to become plumbing

Adobe's choice looks like surrender until you read the fine print. The MCP server is **local**. It runs on your machine and controls Creative Cloud apps you already pay for. A Claude user who wants Photoshop's generative relighting still needs a Photoshop seat.

So the MCP is not a giveaway. It keeps subscribers paying. If a designer's workflow moves into a chat window, Adobe wants Photoshop to be the tool the agent calls, not a free open-source model the agent finds on its own. Adobe has been heading this way for a while. It already offers outside models from Google, OpenAI, Runway, ElevenLabs, Black Forest Labs, Kling and ByteDance inside its apps, and it bought Topaz Labs in June. Adobe has stopped claiming its own model is best. It now claims to be the workbench where every model gets used.

The Google deal gives each side something it needs. Adobe gets distribution inside Gmail and Drive, where billions of PDFs already sit. Google gets a top-tier creative brand inside Gemini, which helps against Microsoft's Copilot-plus-Office bundle and OpenAI's push into business software. This is a partnership between two companies that are each worried about being left out.

## Why eBay chose the wall

eBay's reasons are just as clear. In January it changed its user agreement to ban "buy-for-me agents" and "LLM-driven bots" that place orders without human review. Now it appears to block browsing too. Its spokesperson said eBay takes a "selective approach" and has "restricted agent access in certain cases, including unauthorized scraping and training on our data."

eBay is not alone. Amazon blocks outside agents completely. It sued Perplexity in November 2025 over the Comet browser's shopping agent, and it is spending heavily on its own assistant, Rufus. Amazon has said Rufus is on track for more than $10 billion in annualized incremental sales. Target lets agents through some of the time and blocks them the rest of the time.

## The part nobody is talking about: ad inventory

Most coverage presents this as a fight over scraping or training data. That's the cover story. The real issue is the **ad business**.

An eBay search results page is ad inventory. eBay's Promoted Listings business, where sellers pay for visibility, brings in well over a billion dollars a year. Amazon's ad business is far larger, more than $50 billion a year. Both depend on a human looking at a ranked page that the platform controls.

An agent doesn't look at sponsored slots. It reads the listings, compares price and condition, and returns the best match. When Muse built that reader's daily watch digest, every promoted listing it skipped was revenue eBay lost. Every listing it found through a mirror site gave eBay's inventory value away to someone else.

That leads to the second-order effect: **agents break the business model that pays for marketplace discovery.** Marketplaces won't accept that for free. They will either block agents, which is what eBay and Amazon are doing, or charge them for access, which is what eBay hints at when it mentions "ongoing discussions with potential partners."

We've seen this before. Twitter and Reddit both put their APIs behind paywalls in 2023, and Reddit later signed a data deal with Google reportedly worth about $60 million a year. Commerce agents are next in that line.

## The bear case for openness

Here is the strongest argument for eBay. Agents are unreliable buyers. They misread condition notes, miss seller reputation signals, and can't tell when a "mint" watch is a fake. When an agent buys the wrong thing, the buyer blames eBay, and eBay pays for the dispute. eBay's "trusted end-to-end experience" line is not just PR. A two-sided marketplace runs on trust, and an unaccountable middleman between buyer and seller puts that trust at risk.

The argument has a weak spot, though. It assumes users will keep coming back to eBay directly. Users don't stay loyal to platforms. They stay with whatever is convenient. The Verge found Muse was already sending users to sites that mirror eBay listings. Blocking agents doesn't keep shoppers on eBay. It sends them to worse copies of eBay, where eBay earns nothing and controls nothing.

## The real dividing line

Adobe can open up because it sells **capability**. Every agent call still ends at a paid seat. eBay hesitates because it sells **attention**, and agents take attention away. That distinction predicts who opens and who closes better than any company's AI strategy deck:

- Capability sellers like Adobe, Figma, Notion, Salesforce and Stripe will rush to ship MCP servers. Being callable by agents is how they get distribution now.
- Attention sellers like Amazon, eBay, Meta's feeds and Google's own ad business will block outside agents, build their own, and sell paid access to everyone else.

Google is in an unusual position because it plays both roles. It is hosting Adobe in AI Mode while its search ad business depends on people clicking the same kind of ranked results that agents skip.

## What to Watch

1. **eBay signs an authorized agent deal by mid-2027.** The likeliest partners are OpenAI or Google, through structured checkout protocols like OpenAI's Agentic Commerce Protocol or Google's AP2, and not through browsing. Meta's Muse stays blocked unless Meta pays.
2. **Agent access fees become a standard line item.** At least one major marketplace will publicly price per-query or per-transaction access for third-party agents within 12 months. That's the 2023 API paywall again, applied to commerce.
3. **Adobe reports agent-originated usage as a metric.** Expect a number like "X% of Firefly generations started outside Adobe apps" in an earnings call during 2027. Investors who doubt Adobe will want proof that the MCP retains subscribers.
4. **Microsoft answers with a deeper Office MCP play.** The Adobe-Google alliance targets Microsoft's productivity base directly, and Microsoft will respond within two quarters.
5. **Amazon v. Perplexity becomes the defining case.** Whatever the court decides on agent access will matter more for this market than any product launch this year.

The interface war is about whether your product is a destination or a tool. Companies that sell tools will welcome agents. Companies that sell destinations will fight them, and a growing number of shoppers will stop visiting destinations at all.