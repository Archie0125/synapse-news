---
title: "Baseten Raises $1.5B at $13B Valuation as AI Inference Becomes Its Own Infrastructure War"
summary: "Baseten closed a $1.5 billion Series F led by Altimeter Capital, vaulting its valuation from $5 billion to $13 billion in under five months. The San Francisco startup now processes over one billion AI inference calls daily across 87 global clusters, with revenue growing 20x year-over-year as enterprises shift 30–50% of model spend toward custom post-trained models."
category: "startups"
publishedAt: 2026-07-04
lang: "en"
featured: false
trending: true
sources:
  - name: "Business Wire"
    url: "https://www.businesswire.com/news/home/20260622645563/en/Baseten-Raises-%241.5-Billion-to-Power-the-Next-Era-of-AI-Inference"
  - name: "Startup Fortune"
    url: "https://startupfortune.com/baseten-raises-15-billion-at-a-13-billion-valuation-as-inference-becomes-ais-most-contested-infrastructure-layer/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/18/ai-inference-startup-baseten-reportedly-raising-1-5b-months-after-its-last-mega-round/"
tags:
  - "Baseten"
  - "AI inference"
  - "Series F"
  - "infrastructure"
  - "post-training"
  - "developer tools"
relatedSlugs:
  - "2026-07-01-etched-5b-valuation-1b-sales-inference-chip-en"
  - "2026-07-03-together-ai-800m-series-c-open-source-cloud-en"
---

Baseten has closed a $1.5 billion Series F financing that values the San Francisco AI inference company at $13 billion — a 160 percent leap from the $5 billion valuation attached to its $300 million Series E just five months ago. The round was led by Altimeter Capital, Conviction, and Spark Capital, with Sands Capital and Wellington Management serving as co-leads, and a roster of institutional investors including IVP, Greylock, 01A, Blackbird, Durable Capital Partners, Verified Capital, Battery Ventures, and D. E. Shaw Ventures also participating. Baseten's total capital raised now exceeds $2 billion.

The numbers behind the raise are striking. The company processes more than one billion AI inference calls per day, runs 87 clusters across 18 cloud providers worldwide, and has grown revenue approximately 20x year-over-year. Its annualized revenue run rate climbed from roughly $200 million in December 2025 to approximately $600 million by March 2026 — a pace that, if sustained, would put Baseten in the company of venture-backed software businesses that almost never exist outside of spreadsheets.

## Why Inference Has Become Its Own Infrastructure Layer

For most of AI's history as a commercial category, the prevailing assumption was that inference was a solved problem: buy compute, pick a model, run it. Training was where the hard technical and capital challenges lived. That view is rapidly obsolescing.

As AI workloads have moved from internal tools and experiments into customer-facing, latency-sensitive production systems, the operational complexity of inference has exploded. A company running a single frontier model in a single region with predictable load can still manage inference on generic cloud infrastructure. A company running ten models across a multi-region architecture, handling traffic spikes measured in millions of requests per minute, orchestrating fine-tuned variants against cold-start constraints on GPU clusters — that company needs specialized infrastructure software, not a general-purpose cloud console.

Baseten CEO Tuhin Srivastava has been direct about what is driving the business: "Post-training has become existential for companies building on their own data." The insight is that the era of foundation model commoditization has arrived faster than most predicted. Post-trained, domain-specialized open-source models now deliver frontier-level performance at a fraction of the cost on many commercially relevant tasks. Leading application-layer companies are increasingly allocating 30 to 50 percent of their total model spending toward custom and post-trained models rather than paying premium rates for frontier API access.

That shift creates a structural need for what Baseten provides. Running a post-trained or fine-tuned model at production scale requires GPU lifecycle management, autoscaling across heterogeneous hardware, observability pipelines, billing integration, and developer tooling — all of which Baseten has spent years engineering. Customers can get inference from a dozen providers. They can get production-grade inference infrastructure from a much shorter list.

## The Customer List as a Market Map

Baseten's customer base reads like a directory of the AI application layer's most technically demanding operators. Cursor, the AI-powered code editor that has become the de facto productivity platform for software engineers, runs inference through Baseten. So does Abridge, which builds AI-powered clinical documentation tools for healthcare systems, and Mercor, the AI-native hiring platform. Clay, the AI sales intelligence company, and Lovable, the AI-powered web development tool, also rely on Baseten's infrastructure. OpenEvidence, which applies LLMs to medical research synthesis, rounds out a customer roster that spans healthcare, developer tooling, sales intelligence, and software creation.

The common thread is not sector or revenue stage. It is the requirement for multi-model inference at production speeds, where reliability and latency directly affect whether the product works for end users. These companies are not running inference as a background job. They are running it as the critical path of their product.

## Funding Velocity as a Signal

The capital trajectory is worth examining independently of the business metrics. Baseten raised a $150 million Series D, followed by a $300 million Series E at $5 billion nine months later, followed by a $1.5 billion Series F at $13 billion just five months after that. Total capital deployed into the company in roughly fourteen months: approximately $1.95 billion.

This velocity is not simply a function of investor exuberance toward anything AI-adjacent. It reflects a rational response to a structural supply constraint. Building production AI inference infrastructure requires pre-committed GPU capacity — contracts signed months in advance for hardware that, in constrained supply markets, is not available on demand. Companies in this space that want to guarantee capacity for the next year must pay for it now, whether the demand exists yet or not. Baseten's repeated large rounds are partly about funding growth and partly about securing the physical infrastructure pipeline necessary to serve customers who will commit to it only after it exists.

The investor list reveals something about where institutional money currently believes the value in AI infrastructure will concentrate. Altimeter Capital has been one of the most consistent large-scale investors in public-market cloud infrastructure companies. Its lead in this round signals that Baseten is being underwritten not as an AI venture bet but as an infrastructure business with durable revenue characteristics.

## The Inference Infrastructure Competition

Baseten does not operate in a vacuum. The inference infrastructure market includes Together AI, which this week announced its own $800 million Series C at an $8.3 billion valuation, focusing primarily on open-source model hosting and GPU cloud. It includes Fireworks AI, Replicate, and Modal, all targeting overlapping segments of the developer and enterprise inference market. It includes the hyperscalers themselves — AWS, Azure, and Google Cloud — which offer managed inference services as part of their broader AI platform portfolios.

What differentiates Baseten's positioning is its emphasis on the systems software layer above raw compute. The company does not primarily sell GPU-hours; it sells the operational infrastructure that makes GPU-hours usable in production. That distinction matters increasingly as the market matures. In the early years of cloud computing, buying compute was the purchase. As cloud matured, the value migrated toward managed services, databases, queues, and observability tools — the software that made compute reliable and operable at scale. The inference infrastructure market appears to be following a similar arc, compressing what once took years in cloud into a much shorter window.

At $13 billion and $600 million annualized run rate, Baseten is being valued at roughly 22 times revenue — a premium multiple that implies investors expect the company to either sustain its extraordinary growth rate or expand into adjacent markets as the inference infrastructure layer consolidates. Both scenarios require execution that the company has so far demonstrated it can deliver.
