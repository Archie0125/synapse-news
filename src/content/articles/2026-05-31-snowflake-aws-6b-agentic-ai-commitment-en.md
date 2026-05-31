---
title: "Snowflake Commits $6 Billion to AWS in Largest Enterprise Agentic AI Infrastructure Bet"
summary: "Snowflake announced a $6 billion, five-year commitment to Amazon Web Services on May 27, 2026 — its largest cloud infrastructure deal ever — aimed at accelerating enterprise agentic AI adoption. The deal covers AWS Graviton processors and GPU-accelerated EC2 instances for Snowflake's Cortex AI platform, as customer spending on Snowflake's AWS-hosted services doubled to $2 billion in 2025."
category: "industry"
publishedAt: 2026-05-31
lang: "en"
featured: false
trending: true
sources:
  - name: "Snowflake Press Release"
    url: "https://www.snowflake.com/en/news/press-releases/snowflake-expands-aws-collaboration-with-6b-commitment-to-accelerate-enterprise-agentic-ai-adoption/"
  - name: "PYMNTS"
    url: "https://www.pymnts.com/artificial-intelligence-2/2026/snowflake-commits-6-billion-to-aws-for-global-ai-expansion/"
  - name: "The AI Insider"
    url: "https://theaiinsider.tech/2026/05/28/snowflake-signs-6b-aws-deal-driven-by-ai-workloads-and-graviton-chip-demand/"
  - name: "The New Stack"
    url: "https://thenewstack.io/snowflake-aws-6b-commitment/"
tags:
  - "snowflake"
  - "aws"
  - "agentic-ai"
  - "enterprise-ai"
  - "cloud-infrastructure"
  - "cortex-ai"
  - "graviton"
  - "data-platform"
relatedSlugs:
  - "2026-05-28-kpmg-anthropic-claude-276000-employees-en"
  - "2026-05-28-openai-deployment-company-deployco-4b-enterprise-en"
---

For most of its history, Snowflake's relationship with Amazon Web Services was primarily structural: AWS was the cloud infrastructure on which Snowflake ran. With the announcement of a $6 billion, five-year commitment on May 27, 2026, that relationship has been fundamentally reframed. Snowflake is now betting that its future as an enterprise AI platform is inseparable from AWS's compute infrastructure — and it has put a number large enough to signal strategic conviction to both its customers and its competitors.

The $6 billion commitment, Snowflake's largest cloud spending pledge to date, covers Amazon's ARM-based Graviton processors and GPU-accelerated EC2 instances. It is not a revenue deal — Snowflake is not committing to sell $6 billion of product on AWS Marketplace — but a cost commitment: Snowflake will spend $6 billion purchasing the compute required to run its growing AI workloads on AWS infrastructure.

## The Agentic Pivot

The deal's timing reflects Snowflake's effort to position itself at the center of what enterprise software analysts are calling the "agentic enterprise" transition: the shift from AI systems that answer questions to AI systems that autonomously execute multi-step workflows across an organization's data, tools, and business processes.

Snowflake's Cortex AI platform — its suite of AI products built on top of the data platform — already handles a significant volume of enterprise AI tasks: text-to-SQL query generation, document summarization, sentiment analysis on customer data, entity extraction from unstructured text. These are high-value but fundamentally reactive capabilities; they work when a user asks a question and the system answers it.

The agentic extension means building systems that don't wait to be asked. An agentic AI operating on Snowflake's platform would monitor a data pipeline, detect an anomaly, identify the likely cause by querying related datasets, escalate to a human if the anomaly exceeds a threshold, and file an incident report — all without a user initiating any of these steps. The compute profile for this kind of continuous, multi-step, feedback-loop AI is substantially more intensive than batch query processing, which is a primary reason Snowflake needs to lock in infrastructure at scale.

## Cortex AI and the Data Moat

Snowflake's fundamental competitive argument is that AI is most valuable when it operates on a company's actual data — governed, current, and trusted — rather than on training data or synthetic approximations. This is a more defensible position than it might appear, because the highest-value enterprise AI use cases are precisely those that require access to proprietary data: analyzing customer behavior, forecasting supply chains, monitoring financial positions, or understanding employee patterns.

Cortex AI is the vehicle for that argument. By embedding AI capabilities inside the Snowflake data platform rather than routing data out to external AI services, Snowflake offers enterprise customers a path to AI that doesn't require resolving the data governance questions that have blocked many AI projects. A legal team can run AI summarization on contract data without that data leaving the environment where it is already governed; a financial institution can run fraud detection models on transaction data without establishing data transfer agreements with an external AI vendor.

Cortex Code, the coding assistant variant, applies the same logic to software development: it can analyze a company's own code repositories, documentation, and commit history to provide context-specific assistance rather than generic code generation.

## The Natoma Acquisition

In the same week as the AWS deal, Snowflake announced the acquisition of Natoma — an enterprise Model Context Protocol (MCP) platform that helps AI agents securely connect to the external tools and systems they need to execute workflows. The deal reflects a recognition that the hardest part of deploying agentic AI in enterprise environments is not the AI itself, but the integration layer: connecting AI agents to CRM systems, ERP platforms, internal APIs, and business tools in a way that respects security boundaries and maintains auditability.

MCP, introduced by Anthropic as an open standard for AI tool connection, has become the de facto interface protocol for agentic AI in a short period. By acquiring a company that built its core product around MCP, Snowflake is positioning Cortex AI agents to interoperate natively with the growing ecosystem of MCP-compatible enterprise tools — without Snowflake needing to build every integration itself.

## The Numbers That Justify $6 Billion

The scale of the AWS commitment makes sense in the context of Snowflake's recent financial trajectory. Customer spending on AWS-hosted Snowflake services doubled in 2025, reaching $2 billion for the calendar year. Since Snowflake first appeared on AWS Marketplace, cumulative customer sales have surpassed $7 billion, and the company's lifetime purchases of AWS services have scaled to justify a forward commitment in the multi-billion dollar range.

The demand driver is clear: Snowflake's Cortex AI workloads are growing faster than its traditional data warehouse workloads, and Cortex AI runs on Graviton and GPU-accelerated EC2 instances, not on the general-purpose compute that powered Snowflake's historical growth. To meet enterprise SLA commitments for AI inference latency and reliability — and to offer pricing predictability to customers running continuous agentic workloads — Snowflake needs reserved capacity at scale. The $6 billion commitment effectively secures that capacity through 2031.

The Graviton processor choice is significant. AWS's ARM-based Graviton chips offer better price-performance for inference workloads than comparable x86 instances — a meaningful consideration when inference is becoming a continuously running cost rather than an occasional query cost. Pairing Graviton with GPU-accelerated EC2 for training and more compute-intensive inference creates a tiered infrastructure profile that maps to Snowflake's different AI workload types.

## Competitive Context

Snowflake's AWS commitment comes at a moment of intense competition for enterprise AI platform positioning. Microsoft's Azure, through its integration of OpenAI models and Copilot across Office 365 and Dynamics, has embedded AI into the workflow tools that enterprise users spend most of their time in. Google Cloud, through BigQuery and Vertex AI, is making a similar case that data analytics and AI capabilities belong together. Databricks, the open-source data platform that is Snowflake's most direct competitor, has been aggressively expanding its AI capabilities and recently closed a significant funding round that gives it substantial resources to accelerate.

In this environment, the $6 billion AWS commitment serves multiple functions beyond pure infrastructure provisioning. It signals to enterprise customers that Snowflake has made a long-term bet on AWS-hosted AI — relevant for customers who have standardized on AWS and want their AI infrastructure to be consistent with their cloud strategy. It also signals to AWS that Snowflake is a strategic partner, which typically translates into joint sales motions, co-marketing resources, and access to AWS's own product roadmap discussions.

The commitment does not make Snowflake exclusively AWS-dependent — the company runs on Azure and Google Cloud as well, and multi-cloud support remains a commercial requirement for its largest customers. But the $6 billion scale of the AWS commitment, relative to what are presumably smaller commitments to the other hyperscalers, represents a meaningful weighting of Snowflake's infrastructure future toward AWS.

## What It Means for Enterprise AI Procurement

For enterprise technology buyers, the Snowflake-AWS deal is a data point in an ongoing conversation about where AI infrastructure should be consolidated. The deal's logic — that the most valuable AI operates on your own governed data, inside a platform that handles both data management and AI execution — is persuasive for organizations that have already invested significantly in cloud data infrastructure.

The specific AI capabilities unlocked by the deal are not primarily about accessing more powerful foundation models. Snowflake's Cortex AI already integrates foundation models from Anthropic, Meta, Mistral, and others. The value proposition is about running those models continuously, at enterprise scale, on proprietary data, with the governance and reliability characteristics that enterprise procurement requires.

As agentic AI transitions from proof-of-concept to production deployment across the enterprise, the compute economics of continuously running AI workflows — rather than occasional query processing — will become a defining competitive and cost factor. Snowflake's $6 billion commitment is a bet that it has correctly identified where those economics will settle, and that the enterprise customers who follow it will find the infrastructure waiting for them.
