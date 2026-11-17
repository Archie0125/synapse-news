---
category: ai-ml
lang: en
published: '2026-11-09T06:26:57.589330+00:00'
sources:
- name: Hacker News
  url: https://hunch.net/?p=13764006
- name: SaaStr
  url: https://www.saastr.com/gartner-sees-software-growing-14-6-to-1-68-trillion-in-2027-models-at-117-ai-app-platforms-at-39-and-price-increases-doing-a-lot-of-the-work/
- name: Hacker News
  url: https://247wallst.com/investing/2026/11/07/openai-just-raised-11-billion-at-a-1-25-trillion-valuation-below-the-1-4-trillion-it-first-sought/
- name: Hacker News
  url: https://matteoraso.github.io/im-not-convinced-the-ai-bubble-exists.html#im-not-convinced-the-ai-bubble-exists
- name: SaaStr
  url: https://www.saastr.com/jasons-takes-on-this-weeks-20vc-a-72-cost-drop-on-our-own-app-the-100m-acquisition-bar-and-doordashs-third-competitor/
summary: OpenAI wanted $30 billion and got $11 billion, and the cause isn't weak AI
  demand. Cheap AI is wrecking the revenue stories behind trillion-dollar valuations.
title: OpenAI's $11B Round Isn't a Bubble Popping. It's AI Labs Pricing Like Utilities
trending_theme: AI Funding Fatigue Signals
type: analysis
---

Look at the size of the cheque, not the valuation. OpenAI has closed $11 billion at a $1.25 trillion pre-money valuation. Reports said it first set out to raise $30 billion or more at $1.4 trillion, and two investors put the opening ask at $1.5 trillion. CFO Sarah Friar says that $1.5 trillion figure started with a media report, not with OpenAI. Either way, the company closed about 37% of its target. The rest may arrive later. Up to another $9 billion could bring the total to roughly $20 billion, but that tranche has not closed, and no one has said who is leading it.

Then compare March. Eight months ago OpenAI raised $122 billion at $852 billion. The new price is about 47% higher. In a normal market that's a strong step-up. Here, investors were offered a trillion-dollar story and put in a fraction of the money.

I don't think this is a bubble popping. I think frontier labs are slowly finding out they sell a product whose price keeps falling. That is a very different problem, and investors are pricing it in now.

## The deflation problem nobody wants to model

Start with a real invoice. SaaStr's Jason Lemkin moved the company's AI recruiting app, SaaStr Connect, onto Haiku 5.5 and a cheaper mix of models. Total cost for the same workflow fell 72%. The app also got faster and produced better output. He added that since early 2025, despite all the falling token prices, nothing his team ran with agents had gotten cheaper per use. This was the first time he saw the drop in his own bill.

That's good news for a customer. For the supplier, it means a workload that used to bring in $100 now brings in $28. The model provider has to sell close to 3.6 times as many tokens to stay level.

This matches the pattern in Ramp's corporate card data: enterprise AI spending is flattening while token usage keeps rising. Usage is not falling. Each unit of usage costs less. Anthropic's revenue shows what that looks like. GAAP revenue went from roughly $5 billion in Q1 to $11 billion in Q2 to $17 billion in Q3. You can tell that two ways:

- **Bear version:** quarter-over-quarter growth fell from 100% to 50% in one quarter.
- **Bull version:** Anthropic added about $6 billion each quarter and is still on pace for roughly 5x year-over-year growth.

Both are true. Markets choose the version that fits their mood, and the mood has turned. Investors now put Anthropic at about $1.5 trillion ahead of its mid-November Nasdaq listing, down from roughly $2 trillion in earlier expectations.

## The 30% discount problem

Lemkin's explanation for Anthropic's slowdown is pricing, not demand, and I agree. He says OpenAI is selling roughly equivalent products at 30% off, while open-weight models pull prices down from below. A 30% discount from a competitor is enough to halve a growth rate, because the incumbent has to win a lot more deals to make up the difference.

**Here's what nobody is talking about: switching costs in this market are close to zero.** Lemkin re-platformed a production app and got a 72% saving with no migration project. In the database era, moving off Oracle took years and consultants. In the SaaS era, moving off Salesforce meant retraining a sales team. Moving between model providers is an API change plus a weekend of evals. Most lab valuations quietly assume something like cloud-style lock-in. AWS, Azure and Google Cloud earned their margins because data has gravity, and moving it costs money. Prompts move easily.

So when Friar says demand for AI is real, she's right, and it doesn't settle the question. Demand for long-distance calls was real in 1999 too. The issue was never demand. It was who captures the margin when the unit price collapses.

## Where the money is actually going

Gartner's October 21 forecast shows the split clearly:

- **Total IT spending:** $7.35 trillion in 2027, up 15%.
- **Data center systems:** from $879 billion to $1.366 trillion, adding $487 billion in one year. That's about half of all new IT spending.
- **Data centers' share of IT spending:** from 13.8% to 18.6% in a single year.
- **Software:** up 14.6% to $1.68 trillion, while its share stays flat at about 23%.
- **GenAI models inside software:** projected to grow 117% in 2026, so a handful of labs are fighting over most of the new software spend.

Gartner also says a meaningful share of software growth is price increases: the same seats sold for more, plus AI add-ons. Enterprises are mostly buying embedded AI features from vendors they already use, such as the AI SKU on Salesforce, ServiceNow or Microsoft 365, rather than building on raw model APIs.

The second-order effect: model labs carry the infrastructure bill, while incumbent app vendors capture much of the pricing power. Those vendors buy tokens wholesale at falling prices and sell AI features at rising ones. The labs hold the commodity side of the trade.

## The bear case on my bear case

The strongest counterargument comes from Anthropic's S-1. The company earns $2.08 for every $1 of compute. It has also started earning more than its compute and infrastructure investment combined. That's not a WeWork-style unit-economics problem. Skeptics also point out that roughly $3 trillion in spending commitments and about $1.9 trillion already spent are mostly one-time construction costs. Once the data centers are built, the argument goes, spending falls sharply and margins jump.

OpenAI's operating numbers are strong too: 70% quarter-over-quarter growth in Q3, enterprise business doubled, 1.2 billion weekly ChatGPT users, and a $1 billion ads run rate by August. That's not a company running out of customers.

I'll grant all of that. But the $2.08 ratio is measured at today's prices. If competitors keep cutting 30% and customers keep re-benchmarking every time a small model ships, that ratio compresses. The idea that training spending is a one-time cost assumes the frontier race ends at some point. No lab can stop training without becoming the next 30%-off option. The capex is not one-time. It recurs and is called "staying relevant."

## The quiet tell from Redmond

One signal didn't make the funding headlines. Microsoft Research's AI Frontiers group, about 50 people, was folded into Microsoft AI in early September. The group built the AutoGen agent framework and the Fara computer-use model, and researched new training objectives and architectures. John Langford's post-mortem reads like what happens when a company stops paying for optionality and starts paying for products.

Microsoft cutting exploratory research while it holds a large OpenAI stake that now runs through GAAP earnings is not a coincidence. When capital tightens, the first thing cut is the work that doesn't ship this year. Expect the same pattern at other big tech companies.

## What to Watch

1. **Anthropic's IPO becomes the price check for every private lab.** I expect it to price at or below the $1.5 trillion reference. If it trades below its offer price within 60 days, OpenAI's undisclosed follow-on tranche will close well below the full $9 billion, or slip into 2027.
2. **Another round of price cuts by Q1 2027.** At least one of OpenAI, Anthropic or Google will cut flagship model API prices by 30% or more within the next two quarters. Whoever cuts first wins share and loses growth rate.
3. **Labs will start reporting net new revenue in dollars, not growth rates.** Watch whether Anthropic's first earnings call leads with dollar figures. If it does, management has accepted that percentage growth is now a liability.
4. **More corporate AI research groups get folded into product teams.** Microsoft's AI Frontiers won't be the last. I'd bet at least one more big-tech research group of 50+ people is reorganized into a product org by mid-2027.
5. **The margin shifts to the incumbent app layer.** Gartner's projection of 39% growth for AI app development platforms, alongside rising software prices, says the winners of 2027 are the companies reselling cheap tokens at premium prices, not the companies making them.

AI demand is not slowing. What's slowing is investors' willingness to pay trillion-dollar prices for companies whose main product gets about 70% cheaper every time a new small model ships.