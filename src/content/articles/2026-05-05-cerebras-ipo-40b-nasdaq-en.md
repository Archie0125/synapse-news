---
title: "Cerebras Files for $40 Billion IPO on Nasdaq, Backed by OpenAI's $10B Compute Deal"
summary: "AI chipmaker Cerebras Systems has refiled its IPO prospectus targeting a $4 billion raise at a $40 billion valuation, underpinned by a landmark inference compute agreement with OpenAI worth over $10 billion through 2028. With $510 million in 2025 revenue and a $24.6 billion backlog, the Nasdaq listing could become the largest AI chip IPO in U.S. history."
category: "hardware"
publishedAt: 2026-05-05
lang: "en"
featured: true
trending: true
sources:
  - name: "The Next Web"
    url: "https://thenextweb.com/news/cerebras-ipo-4-billion-40-billion-valuation"
  - name: "Seeking Alpha"
    url: "https://seekingalpha.com/article/4898002-wall-street-lunch-ai-chipmaker-seeks-3-5b-in-ipo-eyes-26-5b-valuation"
  - name: "Winbuzzer"
    url: "https://winbuzzer.com/2026/05/04/cerebras-refiles-ipo-40-billion-valuation-xcxwbn/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/04/openais-cozy-partner-cerebras-is-on-track-for-a-blockbuster-ipo/"
tags:
  - "Cerebras"
  - "IPO"
  - "AI chips"
  - "OpenAI"
  - "Nasdaq"
  - "semiconductor"
  - "wafer-scale"
relatedSlugs:
  - "2026-04-17-openai-cerebras-20b-chip-deal-en"
  - "2026-05-05-whitehouse-ai-model-prerelease-review-en"
  - "2026-04-24-sk-hynix-q1-2026-record-earnings-hbm-en"
---

When Cerebras Systems filed its original IPO prospectus last autumn, skeptics had a field day. The company makes chips the size of dinner plates — literally wafer-scale silicon, each device spanning the entire surface of a semiconductor wafer — and had built its entire commercial thesis around inference workloads at a time when the industry was still obsessed with training. The initial S-1 priced shares at $115 to $125, implying a $26.6 billion valuation. Ambitious, but investors weren't convinced the company deserved Nvidia-like multiples without Nvidia-like scale.

That conversation has changed dramatically. On Monday, Cerebras refiled its prospectus targeting a $4 billion raise at a $40 billion valuation on Nasdaq under the ticker CBRS, a number that would rank the listing among the largest AI chip IPOs in American history. The primary catalyst: a series of landmark agreements with OpenAI that have transformed the company from an interesting hardware alternative into a critical piece of the world's most valuable AI infrastructure.

## The OpenAI Linchpin

No aspect of Cerebras's revised story commands more investor attention than its relationship with OpenAI. In January 2026, the two companies announced an agreement under which Cerebras will supply OpenAI with up to 750 megawatts of AI inference capacity through 2028. The total value of the commitment exceeds $10 billion over the term according to the updated S-1 — with some analyst estimates placing the full contractual value closer to $20 billion when all provisions are accounted for.

The structure of the relationship is unusual even by the baroque standards of contemporary AI deal-making. OpenAI also loaned Cerebras $1 billion in December 2025, a facility secured by warrants that would allow OpenAI to acquire more than 33 million Cerebras shares. That means the company that is simultaneously Cerebras's largest customer and its primary source of forward revenue is also, through those warrants, a potential major shareholder. Bulls call this alignment of incentives; governance observers call it a concentration risk.

The financial reality this creates is striking. Cerebras disclosed a $24.6 billion revenue backlog at year-end 2025, with management guiding investors to expect roughly 15 percent of that to be recognized across 2026 and 2027. Against full-year 2025 revenue of $510 million — nearly double the annualized run rate of $272 million from the first half of 2024 — the backlog represents a level of forward visibility that is genuinely rare in the semiconductor industry.

## Architecture as Differentiation

Founded in 2016 by Andrew Feldman and Gary Lauterbach, Cerebras built its name on a conviction that the GPU-cluster model dominant in AI training was the wrong architecture for inference. Rather than connecting multiple accelerator dies across a circuit board — Nvidia's approach — Cerebras fabricates its Wafer Scale Engine as a single monolithic chip across an entire silicon wafer. The WSC-3, the current generation, measures approximately 46,225 square millimeters and integrates 4 trillion transistors, with no inter-chip communication bottlenecks that slow down memory-intensive operations.

The tradeoff is manufacturing complexity. Producing defect-tolerant chips at wafer scale requires TSMC's most advanced processes and engineering redundancy that keeps per-chip yields commercially viable. Production costs are substantially higher than for tiled GPU architectures, and manufacturing scalability is constrained. But for inference — the act of running a trained model to generate outputs for actual users — the architecture delivers exceptional per-token latency at a price point that Cerebras argues is increasingly competitive.

The OpenAI deal is structured around inference capacity rather than training. This matters: it validates the thesis that wafer-scale silicon can win premium contracts in the inference economy even if it never displaces Nvidia in the training data centers where the big models are built.

## Navigating the Nvidia Shadow

Every Cerebras IPO analysis must eventually reckon with Nvidia, whose market capitalization touched a record $5.26 trillion in April as the company's H100 and H200 GPUs remained the unchallenged default for enterprise AI training. Nvidia has not been passive: its Rubin platform entered full production at the end of April and the company claims a tenfold reduction in inference token cost versus its prior Blackwell generation — exactly the performance dimension Cerebras has built its pitch around.

Cerebras's response is not to contest Nvidia's dominance broadly, but to win in corners of the inference market where single-chip memory bandwidth and ultra-low per-token latency outweigh raw throughput and ecosystem compatibility. The OpenAI deal suggests at least one major buyer has decided that corner is real and large enough to warrant locking in hundreds of megawatts of capacity.

Still, the customer concentration risk disclosed in the S-1 is significant. If OpenAI were to slow its consumption commitments — through model architecture changes that required less inference compute, a pivot to competing architectures, or financial distress of its own — Cerebras's backlog picture would change materially. Underwriters Goldman Sachs, Morgan Stanley, and Citigroup have presumably stress-tested these scenarios with institutional accounts during early roadshow conversations.

## Market Context and Timing

Cerebras is targeting a mid-May 2026 Nasdaq listing, with roadshows expected to begin this week. The timing is calculated: the first-quarter earnings season just concluded with Amazon, Microsoft, and Alphabet all reaffirming enormous capital expenditure commitments to AI data center buildout, pushing AI infrastructure stocks broadly higher. The institutional appetite for anything in the direct path of hyperscaler GPU spending has rarely been stronger.

At $40 billion, Cerebras would trade at roughly 78 times its 2025 revenue of $510 million — a multiple that reflects expected growth rather than current scale. For context, Nvidia trades at approximately 25 times trailing revenue, though that comparison elides the difference in absolute revenue scale, gross margin profile, and market position.

The more relevant question is whether public market investors will continue to price AI infrastructure companies on growth expectations as aggressively as private markets have. The data center spending cycle has proven more durable than many predicted entering 2026, and the Cerebras backlog — if it holds — provides visible cash flow that distinguishes it from pure-growth AI software plays.

## What This Means for the AI Chip Ecosystem

The Cerebras IPO is, in the broadest sense, a test of whether the AI chip ecosystem can support multiple architectures at scale. Nvidia has proven that AI semiconductor demand is real and enormous; Cerebras is attempting to prove that specific inference workloads create durable value for alternative silicon approaches.

The timing also coincides with renewed attention on the geopolitics of AI compute. Huawei's Ascend 950PR is aggressively capturing Chinese inference deployments that Nvidia can no longer serve under export controls. In the United States, policymakers increasingly view domestic AI chip capacity as a strategic asset. A successful Cerebras IPO would add a second significant public company to that infrastructure, with a manufacturing base anchored at TSMC's Arizona fabs.

Mid-May's pricing date cannot come soon enough for a market hungry for answers about which alternatives to Nvidia will survive their public debuts.
