---
category: ai-ml
featured: true
lang: en
publishedAt: '2026-11-11T06:25:46.061594+00:00'
relatedSlugs: []
sources:
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/all-7-anthropic-founders-will-each-cash-out-about-250m-in-ipo/
- name: SaaStr
  url: https://www.saastr.com/anthropics-ipo-puts-216-billion-in-employee-hands-another-160-billion-is-reserved-for-the-next-hires/
- name: Engadget
  url: https://www.engadget.com/2312177/anthropic-takes-on-google-and-microsoft-with-claude-sheets/
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/anthropic-sets-ipo-price-range-of-70-to-78-per-share-to-reach-an-implied-valuation-of-1-404-trillion/
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1030709/anthropic-has-its-own-ai-powered-office-suite-now
summary: Anthropic wants $64 billion from public investors, no real vote for them,
  and a seat in your spreadsheet.
tags: []
title: Anthropic's $1.4T IPO Is Really a Bet on Your Spreadsheet, Not AGI
trending: true
type: analysis
---

Anthropic is about to sell $64 billion of stock that comes with almost no say over the company. It picked the same week to launch a spreadsheet app. Those two things are connected.

The amended S-1 is out. It covers 825 million Class A shares at $70 to $78, under the ticker ANT on Nasdaq, with trading expected around November 19. At the top of the range Anthropic is worth $1.404 trillion fully diluted. Add the $26 billion private placement and the underwriters' greenshoe, and net proceeds land between $84.6 billion and $93.7 billion. For scale, Saudi Aramco's record 2019 IPO raised about $25.6 billion. Anthropic's public offering alone is roughly 2.5 times that.

Most coverage stops at the size. The more interesting question is what Anthropic is asking public investors to believe, and what it is careful not to give them in return.

## The governance fine print

Here is how control works. Each of the seven co-founders (Dario Amodei, Daniela Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah) gets one share of Class F stock with supervoting rights. Together those votes are about 51% of the total. The Long-Term Benefit Trust also elects a board majority. Amazon, Google and the new strategic buyers hold nonvoting Class N shares. If you buy ANT on day one, you get economic exposure and little else.

Dual-class structures are nothing new. Google did it in 2004, Facebook in 2012, and Snap went further in 2017 by selling public shares with zero votes. Anthropic stacks two layers on top: a founder voting bloc and a trust that picks the board. Founder-controlled companies are common. A company whose board is chosen by a body outside the shareholder base is far less common at trillion-dollar scale.

I think this is defensible. A safety-focused lab whose board could be replaced by activist hedge funds after one bad quarter wouldn't be much of a safety-focused lab. But investors should be clear about the deal. Retail is promised up to 20% of the allocation, and those buyers are funding a public benefit corporation that has written into its charter that their interests come second.

The founder selling is mostly a distraction. Each founder sells 3,378,378 shares, about $250 million at the $74 midpoint and roughly $1.75 billion across all seven. That is under 3% of the offering. After the sale each founder still owns about 3.2% of Class A. When people sell this small a slice, it reads as diversification, not an exit.

## Why the office suite launched now

The timing of the launch event makes sense once you look at the revenue. Anthropic says run-rate revenue hit $81 billion at the end of October, up about $10 billion from September's level. At $1.404 trillion, that is around 17x run-rate revenue. That is expensive for a utility, cheap for a company still growing at this pace, and entirely dependent on the growth continuing.

The growth so far came mostly from developers and enterprises: API usage, Claude Code, and agentic coding seats. Anthropic's own product lead, Nicholas Lin, told *The Verge* that Claude Code "changed how engineers work a year ago" and that non-developers are "the gap we're hoping to close." There are perhaps 30 million professional developers worldwide. There are hundreds of millions of people who spend their days in Excel, Google Sheets, Zoom, and meeting notes. The S-1 story depends on reaching that second group.

So we get:
- **Claude Sheets** (beta, all paid plans): collaborative spreadsheets with tabs and formulas, Claude's edits tracked, Excel export, and support for Anthropic's Google Workspace plugin.
- **Claude Meetings** (beta, Team and Enterprise): a note-taking agent that starts in Google Meet. It will not join calls with outside guests without admin approval.
- **Claude Whiteboards** (beta, all paid plans): brainstorming that groups ideas by theme and drafts action items for each person.
- **Claude Data** (renamed from Dashboards): now generally available.
- **Deeper connectors** to HubSpot, Adobe and Atlassian, sitting on top of an MCP marketplace that now has more than 9,000 plugins.

Fable 5.2 shipped in the same window with a price cut and a separate, gated Mythos model. That pairing tells you the pricing strategy. The workhorse model gets cheaper so it can run inside every spreadsheet cell and meeting transcript. The most capable model stays restricted, which keeps it scarce, keeps the safety story intact, and keeps it as the premium tier that justifies the multiple. It is the same approach Nvidia has taken with gaming GPUs and data-center GPUs.

## The part nobody is talking about: the cap table has a conflict

Look at who bought the $26 billion private placement: AMD, Broadcom, Google, Micron, Microsoft, Nvidia, and TSMC. Google and Nvidia put in $10 billion each.

Two things follow. First, five of the seven are suppliers in Anthropic's compute chain. Much of that $26 billion will go back to them as chip, memory, and foundry orders. Calling it partly a prepaid purchase agreement is fair. That isn't fraud, but public investors should discount the "strategic validation" pitch accordingly.

Second, Google and Microsoft are now shareholders in a company that just launched spreadsheets and meeting agents aimed at Google Workspace and Microsoft 365. Claude Meetings launches inside Google Meet, which already has Gemini taking notes. Claude Sheets exports to Excel, where Copilot already lives. Anthropic is building its consumer and white-collar business on its investors' platforms while competing with their products. That arrangement holds as long as both sides need each other. Google needs Anthropic as a large TPU customer, and Microsoft needs model diversity beyond OpenAI. If either decides it needs Anthropic less, the distribution Anthropic depends on can be throttled through an API policy change.

There is a second hidden number in the SaaStr analysis of the filing. Current employees and option holders hold about **$216 billion** of net equity value at $78, roughly $41 million per head across about 5,300 employees. Another **$160 billion** of shares is reserved for future grants. Headcount rose from about 940 at the end of 2024 to 5,300 now. That $160 billion reserve is a recruiting budget large enough to strain the talent market for every other AI company and every B2B SaaS company for the next three years. A startup offering a senior engineer $400,000 in options is competing with a liquid ticker and a reserve worth more than most of the S&P 500.

## The bear case, taken seriously

Run-rate revenue is not profit, and the filing hints that Q4 GAAP results will look bad. It shows about $32.3 billion of unrecognized RSU expense, and RSU expense rises in the quarter the offering closes. Expect the first earnings report to show a very large GAAP loss.

The valuation trend is also less exciting than the headline. Anthropic was reportedly aiming for $2 trillion a couple of months ago. It is now at $1.4 trillion, against a $965 billion private round in May. TechCrunch notes the company is going ahead "despite shakier markets and the broader pullback from AI investing." Falling short of a $2 trillion target by $600 billion means investors already negotiated the price down.

Finally, office suites are hard to win. Microsoft has kept Office on top for three decades despite Google Docs, Notion, Airtable, and Quip, which Salesforce bought for $750 million. Strong AI features don't automatically overcome entrenched workflows, IT procurement rules, and the habits of an accounting team that has used the same Excel shortcuts since 2009.

I'm still more bullish than bearish. The difference this time is that Claude doesn't have to replace Excel. It only has to become where the work starts, with Excel as the export format. Its MCP connectors exist to make the host app interchangeable.

## What to Watch

1. **The IPO prices above $78.** Reed Hastings alone wants $300 million through his donor-advised fund. I expect a final price of $82 or higher and a first-day pop above 20%, partly because of the retail allocation.
2. **Microsoft and Google respond on price within 90 days.** Expect Copilot and Gemini meeting and spreadsheet features to be bundled more aggressively or cut in price by Q1 2027. Fable 5.2's price cut was the first move in that fight.
3. **Claude Meetings comes to Zoom and Microsoft Teams by mid-2027.** Starting only on Google Meet is a beta limitation, not a strategy. Whether Microsoft cooperates on Teams access will show how far the investor relationship really goes.
4. **Mythos becomes an enterprise upsell, not a public model.** Gated access will turn into a price tier, probably bundled with Enterprise seats and compliance commitments.
5. **The lockup expiry is the real stress test.** Roughly six months after listing, around May 2027, a large share of that $216 billion in employee equity becomes sellable. If run-rate growth slows before then, ANT could fall sharply even if the business is fine.
6. **OpenAI speeds up its own listing.** Once a pure-play frontier lab trades publicly, every competitor gets a public valuation benchmark it has to answer to.