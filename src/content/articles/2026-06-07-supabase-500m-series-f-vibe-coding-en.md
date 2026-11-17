---
title: "Supabase Raises $500M at $10.5B Valuation as AI Coding Tools Rewrite the Database Market"
summary: "The open-source Firebase alternative raised $500 million in a round led by Singapore's GIC, roughly doubling its valuation since October. Claude Code is now the largest contributor of databases on Supabase in 2026, according to its CEO."
category: "developer-tools"
publishedAt: 2026-06-07
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: true
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/04/database-startup-supabase-raises-500-million-10point5-billion-valuation.html"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/06/04/supabase-raises-500m-ai-coding-tools-drive-phenomenal-growth/"
  - name: "TechStartups"
    url: "https://techstartups.com/2026/06/05/supabase-hits-10-5b-valuation-after-500m-funding-round-as-vibe-coding-drives-explosive-growth/"
tags:
  - "supabase"
  - "database"
  - "developer-tools"
  - "vibe-coding"
  - "AI-coding"
  - "startup-funding"
  - "series-f"
relatedSlugs:
  - "2026-06-01-github-copilot-ai-credits-billing-change-en"
  - "2026-04-04-cursor-devin-war-en"
  - "2026-04-04-mcp-protocol-explosion-en"
---

When Supabase CEO Paul Copplestone described his company's growth, he pointed to a striking data point: AI coding tools are now responsible for the majority of databases on his platform. According to Copplestone, AI coding assistants now account for most of the databases created on Supabase. More specifically, Anthropic's Claude Code has emerged as the largest contributor in 2026.

That data point sits behind a $500 million funding round announced on Thursday, valuing Supabase at $10.5 billion. The round was led by Singapore's sovereign wealth fund GIC and joined by Accel, Y Combinator, Craft Ventures, Felicis, Coatue, and—notably—Stripe, the payments giant that increasingly stakes out territory in the developer infrastructure stack. The valuation represents a near-doubling from Supabase's $5 billion figure just eight months earlier, in October 2025.

## The Vibe Coding Windfall

The phrase "vibe coding" has evolved from a glib meme into a legitimate market category. AI coding tools now allow developers—and increasingly non-developers—to build software using simple text prompts, with tools like Claude Code and OpenAI's Codex among the most popular. Supabase sits directly in the critical path: when an AI agent scaffolds a new application, it almost invariably needs a backend database, authentication, and storage layer. Supabase has become the default answer.

Accel partner Arun Mathew said of the growth: "We haven't seen a company grow at this pace, certainly in the database layer, ever, ever before."" Supabase now counts over 250,000 customers and employs approximately 350 people—a lean headcount for a company at this valuation, reflecting the automation-first culture the company embodies.

Founded in 2020 by Copplestone and CTO Ant Wilson, Supabase was built as an open-source alternative to Google's Firebase. Where Firebase locks developers into Google's proprietary ecosystem, Supabase runs on PostgreSQL, the gold-standard open-source relational database. That architectural choice has helped: Supabase uses the pgvector tool to add support for the AI embeddings that Postgres alone handles poorly.

## What the Money Buys

Supabase previewed **Multigres**, a new tool meant to help companies building on its platform scale "up to the size of OpenAI or even larger," according to Copplestone.

As AI applications proliferate, the need to store and retrieve high-dimensional vector embeddings—the numerical representations that power semantic search, RAG pipelines, and recommendation systems—has become a core database workload rather than a niche one. Supabase's Postgres-native pgvector support gives it an advantage over dedicated vector databases that lack the broader relational capabilities most applications still require.

Authentication and storage remain competitive moats as well. When an AI agent builds an application end-to-end, it typically reaches for a single vendor that can handle all three pillars of backend infrastructure—data, auth, and files—without requiring configuration of separate services. Supabase's integrated approach has made it the path of least resistance.

## A New Kind of Infrastructure Company

The Supabase round illustrates a broader dynamic reshaping the enterprise software market: AI agents are becoming a new and enormous class of customer. Traditional developer-tool companies grew by persuading individual engineers or engineering teams to adopt their product. The sales motion was human-centric—developer relations, conference sponsorships, documentation quality, Hacker News sentiment.

That model still matters, but it is now layered with a second growth vector: winning the default recommendation slot in AI coding tools. When Claude Code decides which database to spin up, that decision is shaped by the training data the model has seen, the tools it has been given, and the documentation quality of competing providers. Supabase has apparently won that competition decisively in the current generation, with Claude Code being its largest single source of new databases.

This creates a feedback loop with significant compounding potential. More AI-created databases mean more data about usage patterns, more developer mindshare, and more reason for AI model providers to continue recommending Supabase. It also creates risk: if a future generation of AI coding tools shifts preference toward a competitor—say, PlanetScale, Neon, or a fully-managed Postgres offering from a hyperscaler—Supabase's growth could be disrupted as suddenly as it accelerated.

The company's open-source foundation provides some insurance against this risk. With 250,000 customers and a stack that covers the full backend surface area, the switching cost for human-built applications remains high.

## The Broader Ecosystem Signal

Stripe's participation in the round deserves particular attention. Investing in Supabase, the default backend for AI-generated apps, is a strategic alignment rather than a purely financial bet.

For investors, the round signals continued conviction that the database and backend-infrastructure layer will capture significant value even as AI commoditizes application logic. If AI agents write most application code, the margins on application software compress—but the infrastructure the agents depend on maintains pricing power as long as switching costs remain.

The $10.5 billion valuation puts Supabase in the same tier as mature infrastructure companies with much longer track records. Whether that valuation is justified depends on how quickly Multigres and the vector database roadmap can expand average revenue per customer and how durable the AI coding tool tailwind proves to be. What's not in dispute is that the vibe coding era has created a new category of infrastructure winner—and Supabase is currently its clearest example.

*Correction (November 15, 2026): 14 sentences were corrected or removed to match the sources listed on this page.*
