---
title: "Amazon's Custom Chip Business Hits $20B Run Rate With $225B Backlog — Nvidia's Toughest Challenger Yet"
summary: "Amazon's Q1 2026 earnings revealed its Trainium custom silicon business has surpassed a $20 billion annual revenue run rate, growing at triple-digit percentages year-over-year, with $225 billion in committed backlog from customers including OpenAI and Anthropic. CEO Andy Jassy called it one of the top three data center chip businesses in the world — and said the real value is twice that if sold externally."
category: "hardware"
publishedAt: 2026-05-25
lang: "en"
featured: true
trending: true
sources:
  - name: "Amazon Q1 2026 Earnings Call — Motley Fool Transcript"
    url: "https://www.fool.com/earnings/call-transcripts/2026/04/29/amazon-amzn-q1-2026-earnings-call-transcript/"
  - name: "The Register: Amazon chips become a $20B business"
    url: "https://www.theregister.com/2026/04/29/amazon_chips_20b_business/"
  - name: "Motley Fool: Amazon's $225B Trainium Backlog"
    url: "https://www.fool.com/investing/2026/05/11/amazons-ai-chip-backlog-stands-at-a-massive-225-bi/"
  - name: "About Amazon: Andy Jassy on chips"
    url: "https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-amazon-chips-business-q1-2026-earnings"
tags:
  - "Amazon"
  - "AWS"
  - "Trainium"
  - "custom silicon"
  - "AI chips"
  - "Nvidia"
  - "data center"
  - "cloud computing"
relatedSlugs:
  - "2026-05-22-nvidia-q1-fy2027-earnings-china-huawei-concession-en"
  - "2026-05-18-tsmc-n2-2nm-chip-ramp-ai-hardware-en"
  - "2026-05-24-anthropic-acquires-stainless-300m-sdk-en"
---

For years, the custom chip ambitions of the hyperscalers were treated as a footnote to Nvidia's dominance. Amazon's Trainium line was technically impressive but commercially marginal — used mostly to trim internal AWS costs, with limited appeal to third parties who preferred the ecosystem of CUDA and the reliability of the H100. That narrative has now conclusively collapsed.

Amazon's first-quarter 2026 earnings call, held April 29, contained a data point that the semiconductor industry is still processing: the company's custom silicon business has surpassed a $20 billion annual revenue run rate, growing at triple-digit percentages year-over-year. More striking still, committed customer backlog for Trainium has reached $225 billion — a figure that exceeds Nvidia's total revenue for fiscal year 2026 by a wide margin.

## The Numbers Behind the Headline

CEO Andy Jassy was characteristically methodical in walking through what these numbers mean. The $20 billion run rate covers external chip revenue — sales to customers other than Amazon's own internal workloads. But Jassy offered a more expansive framing: if Amazon's chip business were counted the way traditional semiconductor companies count revenue — including the chips it manufactures for its own AWS infrastructure — the annual run rate would be approximately $50 billion.

"We are now one of the top three datacenter chip businesses in the world," Jassy said. "That's not a statement we make lightly."

That assertion is credible by most measures. Nvidia's data center segment generated roughly $110 billion in its most recent fiscal year, firmly in first place. AMD's data center chip revenue was approximately $12 billion annually as of early 2026, before its landmark $100 billion deal with Meta was announced in February. Amazon, at a $20 billion external run rate with a $225 billion backlog, now sits firmly in conversation with AMD for second place — and has a structural advantage: it is simultaneously the customer, the cloud provider, and the chip vendor, an integration that no pure-play semiconductor company can replicate.

## Trainium3: The Generation That Changed the Conversation

Trainium2, Amazon's previous generation, offered roughly 30% better price-performance than comparable GPU-based cloud instances — significant, but not the kind of advantage that convinces customers to abandon Nvidia's mature software ecosystem. Trainium3, which began shipping to customers at the start of 2026, is a different proposition.

Built on TSMC's 3-nanometer process, Trainium3 delivers 30–40% better price-performance than Trainium2 — meaning roughly 70% better than comparable Nvidia GPU instances on a cost-per-token basis for inference workloads. More importantly, AWS reports that Trainium3 capacity is "nearly fully subscribed" despite having only recently entered production, suggesting that hyperscale customers are now willing to lock in multi-year Trainium commitments at volumes that rival Nvidia H100/Blackwell deployments.

The generational roadmap is extending the advantage further. Trainium4, still approximately 18 months from broad availability, has already been substantially reserved by customers. "Customers are committing to future generations before they've seen them perform," one AWS infrastructure analyst noted. "That reflects a level of confidence in the roadmap that we haven't seen with custom silicon before."

## The Anchor Customers: OpenAI, Anthropic, and Beyond

The $225 billion backlog is not diffuse — it is anchored by a handful of enormous, multi-year commitments. The two most significant are OpenAI and Anthropic.

In an expanded agreement announced in parallel with Q1 earnings, OpenAI committed to an $138 billion partnership with AWS — an expansion of an existing $38 billion multi-year agreement. The terms call for OpenAI to consume approximately 2 gigawatts of Trainium capacity through AWS infrastructure over eight years, with AWS becoming the exclusive cloud distributor for OpenAI's Frontier enterprise platform.

Anthropic went further still. On April 20, Amazon announced an additional investment of up to $25 billion in Anthropic — bringing its cumulative investment to $33 billion — alongside a Anthropic commitment to spend more than $100 billion on AWS services over ten years. The compute element of that commitment secures up to 5 gigawatts of Trainium capacity across Trainium2, Trainium3, and Trainium4 generations, with nearly 1 GW expected to come online by year-end 2026.

The strategic logic for both companies is similar: Trainium offers significantly lower cost-per-token for inference than Nvidia, and AWS's vertical integration — networking, storage, Graviton CPUs, and Trainium all designed to work together — provides efficiency advantages that accrue over multi-year deployments. For AI labs burning billions of dollars per year on compute, even a 20% cost reduction on inference translates to hundreds of millions in savings annually.

## What This Means for Nvidia

Nvidia's grip on AI compute remains extraordinarily strong. Its CUDA software ecosystem, built over two decades, has become the de facto standard for AI training — the layer where researcher intuition, existing code, and tooling all converge. That moat is not easily replaced, and neither OpenAI nor Anthropic has abandoned Nvidia entirely. Both companies maintain diversified compute strategies that include Nvidia Blackwell alongside Trainium.

But the direction of travel is unambiguous. Every dollar committed to a Trainium multi-year deal is a dollar that does not go to Nvidia. And the scale of commitments — $225 billion in Trainium backlog alone — suggests that the custom silicon transition is not a future scenario; it is already underway.

The pressure is compounded by parallel moves from Google, which is deploying its TPU v6 (Trillium) generation at scale across Alphabet's AI infrastructure, and Meta, which committed to up to $100 billion in AMD MI-series GPU purchases in February. Nvidia is not losing its dominant position, but the cloud giants have collectively decided that dependence on a single chip vendor is a strategic risk they are unwilling to maintain at these capex levels.

## The AWS Flywheel

What Amazon has built goes beyond a chip business. Trainium is the anchor of a compute flywheel: customers who commit to Trainium capacity become deeply integrated with the broader AWS platform — Bedrock, SageMaker, Graviton, and now the AgentCore agentic infrastructure layer announced last week. Each layer of integration makes switching costs higher and makes the Amazon AI stack more attractive to the next enterprise customer evaluating where to build.

"We're not trying to be a chip company," Jassy said on the earnings call. "We're trying to be the infrastructure layer that makes AI economically viable at scale. The chips are one part of that."

With $225 billion in backlog and Trainium4 already substantially reserved, Amazon has demonstrated that custom silicon can escape the gravitational pull of Nvidia's ecosystem — provided the price performance advantage is large enough and the software tooling matures sufficiently. Both conditions now appear to be met.

The semiconductor industry's trillion-dollar question is no longer whether Amazon's chip business is real. It is how much of Nvidia's future growth it will absorb.
