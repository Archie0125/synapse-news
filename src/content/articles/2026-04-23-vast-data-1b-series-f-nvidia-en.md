---
title: "Nvidia-Backed Vast Data Raises $1 Billion at $30 Billion Valuation, Tripling Its Worth as AI Data Infrastructure Booms"
summary: "Vast Data closed a $1 billion Series F round led by Drive Capital and Access Industries, with Nvidia, Fidelity, and NEA participating, valuing the AI data infrastructure company at $30 billion — more than triple its $9.1 billion valuation from 2023. The company reports over $500 million in committed annual recurring revenue, more than $100 million in cash generated per quarter, and $4 billion in cumulative bookings. Vast Data's platform sits between GPU clusters and AI models, handling the data management layer that determines how fast those systems can actually move."
category: "startups"
publishedAt: 2026-04-23
lang: "en"
featured: false
trending: true
sources:
  - name: "Bloomberg — Nvidia-Backed Vast Data Raises $1 Billion"
    url: "https://www.bloomberg.com/news/articles/2026-04-22/nvidia-backed-vast-data-raises-1-billion-triples-valuation-to-30-billion"
  - name: "CNBC — Nvidia backs AI company Vast Data at $30 billion valuation"
    url: "https://www.cnbc.com/2026/04/22/nvidia-backs-ai-company-vast-data.html"
  - name: "The Next Web — Vast Data $1B raise at $30B valuation"
    url: "https://thenextweb.com/news/vast-data-1b-raise-30b-valuation-nvidia-ai-storage"
  - name: "Quartz — Nvidia backed AI data company Vast Data"
    url: "https://qz.com/nvidia-vast-data-series-f-billion-valuation-042226"
tags:
  - "Vast Data"
  - "AI infrastructure"
  - "Nvidia"
  - "startup funding"
  - "data storage"
  - "Series F"
  - "AI investment"
relatedSlugs:
  - "2026-04-13-q1-2026-vc-funding-record-en"
  - "2026-04-08-semiconductor-sales-record-2026-en"
  - "2026-04-11-rebellions-400m-rebelrack-nvidia-inference-en"
---

The AI infrastructure boom has now produced a $30 billion storage company. Vast Data, the New York-based data infrastructure startup that has spent nearly a decade building storage and data management systems for AI workloads, announced on April 22 that it has raised $1 billion in a Series F funding round that triples its valuation from $9.1 billion in 2023 to $30 billion — one of the most dramatic valuation jumps for any technology company over that period.

Drive Capital and Access Industries led the round, with Nvidia, Fidelity Management and Research Co., and NEA joining as participants. The structure of the round is notable: more than $500 million of the $1 billion total is secondary capital, allowing early investors and employees to sell existing shares rather than the full amount going onto Vast Data's balance sheet. The primary portion gives the company fresh capital to invest in product development and sales; the secondary component provides an early liquidity pathway without the complexity of an IPO.

## What Vast Data Does

Vast Data occupies a layer of the AI stack that receives less public attention than the GPU clusters above it and the models above those, but that determines much of the practical performance of both. The company builds distributed storage and data management infrastructure specifically engineered for the access patterns that large-scale AI training and inference create.

Traditional enterprise storage systems — built for transactional databases, file servers, and backup — were designed around workloads where relatively small amounts of data are read and written frequently, with low latency requirements for individual operations. AI training inverts those assumptions: it involves reading enormous quantities of data at very high throughput, often non-sequentially, in tightly synchronized patterns across thousands of GPU cores that must all receive their next batch of training samples within nanoseconds of each other to avoid idle waiting.

Vast Data's architecture was designed from the ground up for this profile. The company uses a disaggregated storage model in which compute and storage are separated and connected over high-speed networks — a design that allows customers to scale each independently based on workload needs and that eliminates the storage bottlenecks that often throttle GPU utilization in naive AI training setups. Its Vast Universal Storage platform exposes data through a unified namespace, eliminating the file/object/block storage distinctions that create management complexity in traditional infrastructure.

The practical result is that Vast Data's customers can run their GPU clusters closer to full utilization — a significant economic advantage when GPU time costs hundreds of dollars per hour and storage-induced idle time is pure waste.

## The Business Case: Revenue and Margin at Scale

Vast Data's fundraising announcement came with unusual transparency about its financial metrics, reflecting confidence in a story that investors can evaluate rigorously rather than on pure potential.

The company reports more than $4 billion in cumulative bookings since its founding in 2016 — a figure that encompasses total contract value committed by customers over its history rather than revenue recognized. More directly comparable to revenue is its committed annual recurring revenue figure: over $500 million as of the end of fiscal year 2026, a number that represents what Vast Data's contracted customer base has agreed to pay over the next twelve months.

Crucially, the company reports generating more than $100 million in cash per quarter and describes itself as both free cash flow positive and operating margin positive. In the current venture environment, where many high-valuation infrastructure companies remain cash-consuming despite years of operation, those metrics place Vast Data in a category that could credibly support an IPO at scale without requiring immediate external capital.

The $1 billion raise appears designed to accelerate rather than sustain: with Nvidia as both customer and investor and AI data center construction running at historically unprecedented pace, Vast Data is betting that the window for capturing long-term relationships with the world's largest AI training operators is open now and will not stay open indefinitely.

## Nvidia's Stake: More Than a Financial Bet

Nvidia's participation in the round deserves separate analysis. Nvidia is already the hyperscaler of AI compute, selling GPUs to every major cloud provider, frontier AI lab, and enterprise data center that matters. Its decision to take an equity position in Vast Data signals something more specific than generic interest in the AI infrastructure space.

GPU utilization is a direct lever on Nvidia's business. A storage bottleneck that keeps a cluster of H100s waiting for data is lost revenue for Nvidia's customers and reputational drag on Nvidia's own products. By backing Vast Data, Nvidia is investing in a company whose success is literally measured by how efficiently data flows to Nvidia's chips. The relationship is symbiotic in a way that makes the investment strategically coherent even if the financial return were marginal.

Nvidia has made similar investments across the AI infrastructure stack — in networking companies, chip packaging specialists, and software tooling — as part of a broader strategy of ensuring that the ecosystem surrounding its GPUs is robust enough that customers can buy Nvidia hardware at scale without hitting bottlenecks elsewhere that undercut the value of that hardware. Vast Data fits squarely in that thesis.

## The Broader Infrastructure Funding Wave

Vast Data's raise is the latest in a series of landmark rounds for companies addressing the infrastructure layers of AI that are neither hardware manufacturers nor model developers. The pattern reflects a maturing investment thesis: that the value chain of AI is long, that bottlenecks exist at multiple layers, and that companies solving real infrastructure problems for customers who are spending billions on AI can build durable, high-margin businesses without needing to develop foundation models of their own.

The capital flowing into this category — networking, storage, data management, inference optimization — has accelerated sharply in 2025 and 2026 as it became clear that the demand for AI compute was not a temporary wave but a structural shift in how enterprises operate. Vast Data's $30 billion valuation is a data point in that thesis: a company that was valued at $9.1 billion at a moment when AI infrastructure investment was already growing rapidly has more than tripled in roughly two years as that growth accelerated further.

For Vast Data's founders and early investors, the secondary component of the round offers meaningful liquidity at a moment when the IPO market for technology companies remains selective and the path from private company to public listing can take years longer than optimistic projections suggest. The structure allows the company to maintain its growth trajectory without the distraction of an IPO process while still rewarding the long-duration bets that its earliest backers made.

Whether Vast Data eventually goes public, gets acquired by a hyperscaler, or remains private while growing into its $30 billion valuation is an open question. What the round establishes is that the company has the financial metrics, the customer relationships, and the Nvidia endorsement to make any of those outcomes viable. In an era where AI infrastructure spending is measured in hundreds of billions of dollars annually, a $30 billion data company that generates $100 million in cash per quarter looks less like a richly valued startup and more like the early stages of a durable enterprise infrastructure franchise.
