---
title: "Amazon's Custom Chip Business Hits $20B Run Rate With $225B in Committed Orders"
summary: "Amazon CEO Andy Jassy disclosed that the company's custom silicon business — Trainium AI accelerators, Graviton processors, and Nitro security chips — has crossed $20 billion in annual revenue, growing triple digits year-over-year. With $225 billion in multi-year order commitments tied almost entirely to Trainium, Amazon is now positioned as the third-largest datacenter chipmaker on the planet, with a credible path to $50 billion."
category: "hardware"
publishedAt: 2026-07-20
lang: "en"
featured: false
trending: false
sources:
  - name: "Crypto Briefing"
    url: "https://cryptobriefing.com/amazon-trainium-chip-20b-revenue/"
  - name: "The Motley Fool"
    url: "https://www.fool.com/investing/2026/07/16/andy-jassy-says-amazons-chip-business-already-has/"
  - name: "The Globe and Mail"
    url: "https://www.theglobeandmail.com/investing/markets/stocks/AMZN/pressreleases/3328399/andy-jassy-says-amazons-chip-business-already-has-225-billion-in-commitments/"
  - name: "Let's Data Science"
    url: "https://letsdatascience.com/news/amazons-custom-chips-reach-a-20b-run-rate-9c98d68a"
tags:
  - "Amazon"
  - "Trainium"
  - "AWS"
  - "custom silicon"
  - "AI chips"
  - "Graviton"
  - "hardware"
relatedSlugs:
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-en"
  - "2026-07-10-openai-jalapeno-broadcom-inference-chip-en"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-en"
---

When Andy Jassy disclosed Amazon's custom chip revenue during the company's Q1 2026 earnings call in late April, the number was eye-catching: the business had crossed $20 billion in annual revenue run rate, growing at triple-digit rates year-over-year. But the more significant figure was the one sitting behind it — $225 billion in multi-year order commitments, tied almost entirely to Trainium AI training accelerators, representing contracted demand that stretches years into the future.

Those two numbers, taken together, tell a story about how quickly the competitive landscape in AI infrastructure hardware has shifted — and how Amazon has moved from a laggard in custom silicon to a company with a credible claim to be among the top three datacenter chipmakers in the world.

## The Three-Chip Portfolio

Amazon's custom silicon strategy rests on three distinct families of chips, each addressing a different layer of the cloud infrastructure stack.

**Graviton** is Amazon's ARM-based general-purpose processor, now in its fourth generation. Graviton4, released on TSMC's 3nm process, offers significant performance-per-dollar improvements over comparable x86 instances for cloud workloads that don't require GPU acceleration — things like web serving, data processing, and application backends. AWS reports that more than a third of all EC2 instances launched globally now run on Graviton, a penetration rate that would have seemed impossible three years ago.

**Trainium** is the crown jewel and the driver of the $225 billion commitment number. Trainium2, launched in 2024, delivered about 30% better price-performance than comparable Nvidia H100 instances for large language model training workloads — a margin that proved sufficient to shift spending at scale. Trainium3, which began shipping in early 2026, is already nearly fully subscribed despite being brand new to market. The chip is built specifically for the tensor operations that dominate transformer model training, and AWS has invested heavily in the software stack — the Neuron compiler and runtime — needed to make models written for Nvidia's CUDA ecosystem portable to Trainium.

**Nitro** is less visible but strategically important: it's the security and virtualization chip embedded in every AWS server that handles isolation between tenants, networking, and storage access. Nitro allows AWS to deliver bare-metal-equivalent performance on virtualized infrastructure, and it reduces the CPU overhead of cloud operations substantially — a compounding efficiency advantage that accumulates at AWS's scale.

## The $225 Billion Bet

The $225 billion in order commitments deserves careful unpacking. Jassy framed it as contracted demand — customers who have made multi-year commitments to consume Trainium capacity, with contracts structured as take-or-pay arrangements that provide Amazon with revenue visibility and customers with capacity guarantees in a constrained market.

The two largest commitments are from OpenAI and Anthropic. OpenAI has committed to consume approximately two gigawatts of Trainium capacity beginning in 2027 — a scale of commitment that implies OpenAI is treating Trainium as a genuine alternative to its primary Nvidia infrastructure, not just a hedge. Anthropic, which has a deeper existing relationship with AWS and has received significant Amazon investment, has committed to up to five gigawatts of current and future Trainium generations. Given that a single H100 GPU cluster of 10,000 chips draws roughly 15-20 megawatts, five gigawatts represents a staggering scale of potential deployment.

The existence of these commitments answers a question that has dogged Trainium since its early days: can Amazon convince frontier AI labs to move workloads from Nvidia's CUDA ecosystem to Amazon's Neuron stack? The answer appears to be yes — at least for a meaningful fraction of their total compute needs, at prices and availability terms that Nvidia cannot match during a period of acute GPU supply constraints.

## The Standalone Valuation Exercise

Jassy made a point during the earnings call that is worth sitting with. He said that if Amazon's custom silicon business operated as a standalone semiconductor company — selling chips to AWS and third parties alike, as Nvidia does — its annual revenue run rate would approach $50 billion, placing it among the largest chipmakers in the world.

The exercise is partly hypothetical: most of Amazon's chip revenue is currently internal, with AWS "buying" Trainium and Graviton at transfer prices. A standalone entity selling externally would face different pricing dynamics. But the point stands directionally: Amazon is building chip scale that is meaningful on an absolute basis, not just as a fraction of its cloud business.

This matters for competitive dynamics. Nvidia's data center GPU business generated roughly $120 billion in revenue in FY2026, and AMD's Instinct MI-series business is growing rapidly but from a smaller base. Amazon's $20 billion run rate puts it in the same conversation as AMD as the number-two or number-three player in AI-specific datacenter compute, with significantly more contracted future demand than either.

## Why This Matters Beyond the Financials

The Trainium story is significant not just as a financial achievement but as an indicator of how the AI infrastructure layer is consolidating. The conventional wisdom through 2024 was that Nvidia's CUDA ecosystem was an effectively unassailable competitive moat — that the software ecosystem was too deeply entrenched for any competing platform to reach viable scale. Trainium's adoption among frontier AI labs is the most concrete evidence to date that this moat has limits.

It's worth noting what Trainium is not: it is not a general-purpose GPU with a broad software ecosystem available for anyone to buy. It is deeply integrated into the AWS cloud, accessible only as a managed service through EC2 instances. This limits adoption to customers willing to run workloads on AWS — it does not threaten Nvidia's on-premise or competitor-cloud business. But within the AWS-managed training context, the competitive displacement is real.

The harder question is whether Amazon can extend Trainium's reach beyond training into inference. Inference — running trained models to serve predictions to end users — is increasingly the larger share of total AI compute spending as production deployments scale. Amazon has historically positioned Inferentia as its inference chip, but Inferentia has seen slower adoption than Trainium. Whether the $225 billion commitment translates into equally dominant inference revenue will depend on workload economics that are still evolving.

For now, the milestone is clear: Amazon has moved from being a chip consumer to a chip manufacturer with a credible, large-scale position in the highest-growth segment of the semiconductor market. The implications for Nvidia, AWS's hyperscaler competitors, and the economics of AI model training will play out over the next several years.
