---
title: "Amazon's Custom Chip Business Crosses $20B Annual Run Rate—and CEO Jassy Says the Real Value Could Be $50B"
summary: "Amazon's in-house silicon portfolio—spanning Graviton processors, Trainium AI accelerators, and Nitro networking chips—has surpassed a $20 billion annual revenue run rate with triple-digit year-over-year growth. CEO Andy Jassy says that if the business were standalone and sold chips to third parties, its annual revenue run rate would be $50 billion."
category: "hardware"
publishedAt: 2026-06-30
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "Let's Data Science – Amazon's Custom Chips Reach $20B Run Rate"
    url: "https://letsdatascience.com/news/amazons-custom-chips-reach-a-20b-run-rate-9c98d68a"
  - name: "TIKR – Amazon Beat Q1 2026 Earnings; The Bigger Story Is the Chip Business"
    url: "https://www.tikr.com/blog/amazon-beat-q1-2026-earnings-on-every-line-the-bigger-story-is-the-chip-business-inside-aws"
  - name: "The Next Web – Amazon Custom Chips: Jassy Hints at $50B External Value"
    url: "https://thenextweb.com/news/amazon-custom-chips-jassy-letter-fifty-billion-trainium"
  - name: "About Amazon – AWS Trainium and Graviton Explained"
    url: "https://www.aboutamazon.com/news/aws/aws-trainium-graviton-ai-chips-explained"
tags:
  - "Amazon"
  - "AWS"
  - "Trainium"
  - "Graviton"
  - "AI chips"
  - "hardware"
  - "semiconductor"
relatedSlugs:
  - "2026-06-29-openai-jalapeno-broadcom-inference-chip-en"
  - "2026-06-29-ai-chip-stock-selloff-june-2026-en"
---

Andy Jassy disclosed, in Amazon's shareholder letter and again on its Q1 2026 earnings call, that the company's custom silicon business had crossed a **$20 billion annual revenue run rate**, growing at triple-digit rates year-over-year. But the bigger figure came next: if Amazon's chip business were a standalone business and sold chips to AWS and other third parties as other leading chip companies do, Jassy said, the annual revenue run rate would be **$50 billion**.

That hypothetical valuation—which Jassy laid out in Amazon's shareholder letter and repeated on the earnings call—frames what may be the most underappreciated strategic asset in technology today. Amazon has quietly built a vertically integrated silicon stack that spans training accelerators, inference processors, CPU clusters, and data-plane networking chips, all tuned specifically for the AI workloads that are now the primary driver of cloud infrastructure investment.

## Three Chip Lines, One Coherent Strategy

Amazon's custom silicon portfolio breaks into three product families: Graviton, Trainium and Nitro.

**Graviton** processors power CPU-bound workloads across AWS. The chip runs the operating system layer, application servers, inference preprocessing, and data pipeline tasks that bookend every AI model call. Graviton is already used by 98% of the top 1,000 AWS EC2 customers.

**Trainium** is Amazon's AI training and inference accelerator, designed to compete with Nvidia's data center GPUs. Trainium3, Amazon's first chip built on a 3nm process node, began shipping to customers in early 2026 and is described as "nearly fully subscribed," according to AWS briefings—meaning demand already matches or exceeds production capacity. Trainium4, still roughly 18 months from broad availability, has already been significantly reserved.

**Nitro** chips handle the data-plane infrastructure that makes AWS's virtualization, networking, and storage systems run. Less visible to end users than Graviton or Trainium, Nitro is nonetheless foundational—it offloads the overhead that would otherwise consume significant CPU cycles on every server in Amazon's fleet, and it enables the high-bandwidth networking that AI model inference at scale requires.

## The Anchor Customers That Changed Everything

The inflection point for Trainium came when two of the world's largest AI model developers agreed to commit their training workloads to Amazon's silicon.

**Anthropic** committed up to **5 gigawatts** of Trainium capacity under a long-term agreement, paired with Amazon's $25 billion investment commitment in the company. That arrangement transforms Trainium from an interesting competitor to Nvidia into an essential piece of Anthropic's training infrastructure—a customer relationship that locks in both compute revenue and model development alignment for years.

When the two dominant model providers in the industry choose your silicon for training runs, it validates both the chip's technical capability and the cost-per-compute-unit competitiveness that matters most to organizations burning through billions in training budgets.

## What $50 Billion Means

Jassy's hypothetical $50 billion market-rate valuation deserves scrutiny. The $50 billion figure is Jassy's estimate of the annual revenue run rate the chip business would have if it were a standalone company selling chips to AWS and third parties, versus the more than $20 billion run rate today. Nvidia's data center GPU chips carry significant margin above manufacturing cost. If Amazon sold Trainium and Graviton units at comparable market pricing rather than internalizing them into AWS infrastructure costs, the business would appear dramatically larger.

This matters for several reasons. First, it suggests that AWS's reported margins significantly understate the strategic value of its silicon investment, because the chips are priced into AWS services rather than reported as standalone chip sales. Second, and more practically, it positions Amazon to potentially enter the external chip market—selling Trainium to non-AWS customers who want an alternative to Nvidia's near-monopoly on AI training hardware.

Jassy has signaled this direction, writing that it is "quite possible we'll sell racks of them to third parties in the future." Amazon currently monetizes its chips through EC2 instances, so selling them directly would mark a fundamental shift toward competing in the chip merchant market.

## The Broader Context: Nvidia's Moat Under Pressure

The significance of Amazon's $20 billion run rate extends beyond Amazon itself. It represents one of the clearest data points yet that the AI silicon market is beginning to fragment away from Nvidia's overwhelming dominance.

Nvidia captured roughly 80% of AI training accelerator revenue in 2025. But in 2026, the composition of the remaining 20% has changed substantially. Amazon, Google (with its TPU line), and Microsoft (with the Maia 2 chip powering Azure AI workloads) are each operating custom silicon programs at a scale that was unimaginable five years ago. Combined, the hyperscaler internal chip programs now represent an estimated $60–70 billion in annual compute value that simply does not flow through Nvidia's revenue line.

That dynamic is already visible in Nvidia's forward guidance. While the company continues to project extraordinary revenue growth through 2027, its CEO Jensen Huang has acknowledged that hyperscaler custom silicon represents a structural shift in the market, not a temporary blip.

For Amazon, the $20 billion milestone is as much a signal to the market as a financial report. It tells AI developers that AWS is building for the long-term silicon race, that Trainium is a credible alternative to Nvidia's H-series for serious training workloads, and that the company has the scale and customer commitment to keep investing through multiple chip generations. Whether that translates into the full $50 billion hypothetical Jassy described—on the open market, as a standalone business—remains an open question. But the direction of travel is unmistakable.

*Correction (November 15, 2026): 12 sentences were corrected or removed to match the sources listed on this page.*
