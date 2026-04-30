---
title: "AWS Posts Fastest Growth in 15 Quarters as Amazon's Custom Silicon Crosses $20B Revenue Run Rate"
summary: "Amazon's Q1 2026 results revealed two intertwined stories: AWS grew 28% to $37.6 billion — its fastest pace in nearly four years — while the company's custom chip business (Trainium, Graviton, Nitro) quietly crossed a $20 billion annual revenue run rate growing at triple-digit rates. CEO Andy Jassy hinted the business could eventually sell chips externally, at a potential $50B valuation."
category: "hardware"
publishedAt: 2026-04-30
lang: "en"
featured: false
trending: true
sources:
  - name: "Amazon Q1 2026 Earnings — CNBC"
    url: "https://www.cnbc.com/2026/04/29/amazon-amzn-q1-earnings-report-2026.html"
  - name: "AWS Q1 2026 — CNBC"
    url: "https://www.cnbc.com/2026/04/29/aws-earnings-q1-2026.html"
  - name: "Amazon's chips become a $20B business — The Register"
    url: "https://www.theregister.com/2026/04/29/amazon_chips_20b_business/"
  - name: "Amazon Q1 2026 Earnings Transcript — Motley Fool"
    url: "https://www.fool.com/earnings/call-transcripts/2026/04/29/amazon-amzn-q1-2026-earnings-call-transcript/"
  - name: "Amazon Earnings Q1 2026 — About Amazon"
    url: "https://www.aboutamazon.com/news/company-news/amazon-earnings-q1-2026-report"
tags:
  - "Amazon"
  - "AWS"
  - "Trainium"
  - "Graviton"
  - "AI chips"
  - "custom silicon"
  - "cloud computing"
  - "earnings"
relatedSlugs:
  - "2026-04-30-alphabet-q1-2026-cloud-compute-constrained-en"
  - "2026-04-30-microsoft-q3-fy2026-ai-revenue-azure-en"
  - "2026-04-27-hyperscaler-custom-silicon-nvidia-decoupling-en"
---

When Amazon reported Q1 2026 earnings on April 29, the headline was an AWS growth reacceleration that surprised even the bullish end of analyst estimates. But buried inside the results was a business development story that could reshape the semiconductor competitive landscape: Amazon's homegrown chip portfolio — Trainium for AI training, Graviton for general compute, Nitro for security and networking — crossed a $20 billion annual revenue run rate in the quarter, growing at triple-digit percentages year-over-year.

For context: a standalone chip company doing $20 billion annually would rank among the most valuable in the world. AWS CEO Andy Jassy didn't just report the number — he teased an even bigger possibility.

## The Numbers

Amazon's total Q1 2026 net sales reached $181.5 billion, up 17% year-over-year from $155.7 billion, easily beating the $177.3 billion analyst consensus. Diluted EPS came in at $2.78, more than 70% above the $1.64 estimate.

But the number most relevant to the AI arms race was the AWS figure: $37.59 billion in revenue, up 28% year-over-year from $29.27 billion. The AWS operating income of $14.16 billion beat StreetAccount's $12.84 billion consensus. Crucially, this 28% growth rate marks AWS's fastest expansion in 15 quarters — an acceleration from 24% the previous quarter, snapping what had been a gradual deceleration narrative.

Advertising revenue also jumped 24% year-over-year to $17.24 billion, above expectations, further illustrating the breadth of Amazon's AI-driven monetization across business lines.

Q2 2026 guidance was set at net sales of $194 billion to $199 billion, representing 16% to 19% year-over-year growth.

## The $20 Billion Chip Business No One Was Talking About

The custom silicon disclosure was the most forward-looking element of the earnings call. Amazon's chip business — comprising Graviton processors, Trainium AI training chips, and Nitro security controllers — exceeded a $20 billion annual revenue run rate in Q1, growing at "triple-digit percentages" year-over-year, according to Jassy.

To understand why this matters, consider the trajectory. Graviton has been shipping since 2018 and is now in its fourth generation, with AWS claiming it offers better price-performance than equivalent x86 instances from AMD and Intel. Graviton4 instances have become the default recommendation for general-purpose cloud workloads at AWS, giving Amazon a meaningful structural cost advantage relative to competitors running on third-party silicon.

Trainium is the bigger story for the AI era. Trainium2, now widely available, offers approximately 30% better price-performance than comparable GPU instances and has largely sold out. Trainium3, which began shipping in early 2026, is 30-40% more price-performant than Trainium2, and is already nearly fully subscribed despite being less than a year into production. Trainium4 — not yet shipping — has had much of its capacity pre-reserved by customers.

The demand picture is staggering: Jassy disclosed that Amazon has received "very large, multi-year, multi-gigawatt training commitments" from Anthropic and OpenAI, and that cumulative revenue commitments for Trainium now exceed $225 billion. That figure, if it materializes on the indicated timelines, would dwarf the current annual revenue run rate many times over.

## "Could Be Worth $50 Billion" — Jassy's External Sales Hint

The most eyebrow-raising moment of the earnings call came when Jassy addressed the possibility of selling Amazon's custom chips externally — not just using them internally within AWS.

"If we were to sell the chips we produce this year externally, the run rate would be approximately $50 billion," Jassy said, adding that the company is "actively considering" whether external chip sales make strategic sense. He stopped short of announcing a product launch, but the disclosure was deliberate: Amazon is signaling to the market that its silicon ambitions extend beyond internal cost optimization.

An external chip business of that scale would position Amazon as a direct competitor to Nvidia in the AI accelerator market — a consequence that would have seemed far-fetched as recently as two years ago. The more immediate question is whether hyperscaler customers beyond Amazon's own AWS would be willing to buy Trainium systems, and whether Amazon would be willing to build the external sales infrastructure (support, developer tooling, ecosystem partnerships) that chip sales at scale require.

For now, it remains a stated consideration rather than a product announcement. But Jassy is not known for off-the-cuff remarks on earnings calls.

## Meta's Graviton Bet and the CPU Surge

One data point that adds texture to the custom silicon story: Meta announced earlier in April that it is deploying Amazon Graviton chips at significant scale across its infrastructure. The deal was described as a "billion-dollar bet" — notable because Meta has historically developed its own custom silicon (MTIA) for AI inference workloads.

The explanation is the rise of the AI agent era. General-purpose CPU workloads — running inference at modest scale, orchestrating multi-agent pipelines, handling the non-matrix-multiply portions of AI workloads — are growing faster than the GPU-centric training and large-scale inference tasks that capture most headlines. Graviton's price-performance advantage in general compute makes it an attractive substrate for the long tail of AI agent infrastructure.

This dynamic, if it extends beyond Meta, represents a second revenue stream for Amazon's custom silicon alongside the Trainium GPU-alternative story.

## The Broader Context: AWS as the AI Infrastructure Backbone

The AWS growth reacceleration comes against a backdrop in which Amazon has committed approximately $200 billion in capital expenditure for 2026 — the single largest AI infrastructure commitment of any company globally. Critics had questioned whether the investment was outpacing the addressable revenue opportunity. Q1's 28% growth rate, the fastest in 15 quarters, is the most direct rebuttal yet.

The $225 billion in Trainium revenue commitments, combined with AWS's overall cloud growth, suggest that the bet is being validated at the customer commitment level. Enterprises aren't just signing up for AWS because of brand inertia — they are making multi-year, multi-gigawatt training commitments because they believe Amazon's silicon trajectory and data center capacity will deliver the economics they need to run frontier AI workloads.

Whether AWS can sustain 28% growth through the back half of 2026 is an open question; the comparison period becomes more demanding as prior-year numbers reflect an AWS that had already begun to reaccelerate. But for one quarter, Amazon produced the clearest evidence yet that its $200 billion AI infrastructure bet is paying off — and that the chip business it almost no one was watching may quietly become a $50 billion business in its own right.
