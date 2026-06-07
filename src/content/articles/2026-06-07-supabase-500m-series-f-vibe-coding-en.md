---
title: "Supabase Raises $500M at $10.5B Valuation as AI Coding Tools Rewrite the Database Market"
summary: "The open-source Firebase alternative closed a $500 million Series F led by Singapore's GIC, doubling its valuation in eight months. Claude Code now accounts for more database creation on Supabase than any human developer, signaling a structural shift in how software infrastructure companies grow."
category: "developer-tools"
publishedAt: 2026-06-07
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

When Supabase CEO Paul Copplestone sat down to describe his company's growth in the first half of 2026, he reached for an unusual frame: most of the databases being spun up on his platform are no longer created by human developers. "AI coding assistants now account for most of the databases created on Supabase," Copplestone told investors. More specifically, Anthropic's Claude Code has emerged as the single largest contributor—surpassing every individual human customer.

That extraordinary data point is the engine behind a $500 million Series F funding round announced on June 4, valuing Supabase at $10.5 billion post-money. The round was led by Singapore's sovereign wealth fund GIC and joined by Accel, Y Combinator, Craft Ventures, Felicis, Coatue, and—notably—Stripe, the payments giant that increasingly stakes out territory in the developer infrastructure stack. The valuation represents a near-doubling from Supabase's $5 billion figure just eight months earlier, in October 2025.

## The Vibe Coding Windfall

The phrase "vibe coding" has evolved from a glib meme into a legitimate market category. AI coding tools now allow developers—and increasingly non-developers—to build functional software by describing intent in natural language, with agents like Claude Code, OpenAI's Codex, and GitHub Copilot generating everything from front-end components to database schemas. Supabase sits directly in the critical path: when an AI agent scaffolds a new application, it almost invariably needs a backend database, authentication, and storage layer. Supabase has become the default answer.

The result has been, in the words of Accel partner Rich Wong, growth that is "unprecedented in the database layer, ever before." Supabase now counts over 250,000 customers and employs approximately 350 people—a lean headcount for a company at this valuation, reflecting the automation-first culture the company embodies.

Founded in 2020 by Copplestone and CTO Ant Wilson, Supabase was built as an open-source alternative to Google's Firebase. Where Firebase locks developers into Google's proprietary ecosystem, Supabase runs on PostgreSQL, the gold-standard open-source relational database. That architectural choice has paid enormous dividends: PostgreSQL's extension ecosystem, including the pgvector extension for storing AI embeddings, positioned Supabase perfectly for the generative AI wave before most startups saw it coming.

## What the Money Buys

The new capital will accelerate several strategic bets. Most prominently, Supabase previewed **Multigres**, a new architecture designed to help applications scale beyond the boundaries that typically force startups onto more complex distributed database systems. The challenge is real: Supabase's success with AI-generated apps means it now hosts workloads that grow from zero to significant scale far faster than traditionally human-built applications.

The company is also investing in its vector database capabilities. As AI applications proliferate, the need to store and retrieve high-dimensional vector embeddings—the numerical representations that power semantic search, RAG pipelines, and recommendation systems—has become a core database workload rather than a niche one. Supabase's Postgres-native pgvector support gives it an advantage over dedicated vector databases that lack the broader relational capabilities most applications still require.

Authentication and storage remain competitive moats as well. When an AI agent builds an application end-to-end, it typically reaches for a single vendor that can handle all three pillars of backend infrastructure—data, auth, and files—without requiring configuration of separate services. Supabase's integrated approach has made it the path of least resistance.

## A New Kind of Infrastructure Company

The Supabase round illustrates a broader dynamic reshaping the enterprise software market: AI agents are becoming a new and enormous class of customer. Traditional developer-tool companies grew by persuading individual engineers or engineering teams to adopt their product. The sales motion was human-centric—developer relations, conference sponsorships, documentation quality, Hacker News sentiment.

That model still matters, but it is now layered with a second growth vector: winning the default recommendation slot in AI coding tools. When Claude Code decides which database to spin up, that decision is shaped by the training data the model has seen, the tools it has been given, and the documentation quality of competing providers. Supabase has apparently won that competition decisively in the current generation, with Claude Code being its largest single source of new databases.

This creates a feedback loop with significant compounding potential. More AI-created databases mean more data about usage patterns, more developer mindshare, and more reason for AI model providers to continue recommending Supabase. It also creates risk: if a future generation of AI coding tools shifts preference toward a competitor—say, PlanetScale, Neon, or a fully-managed Postgres offering from a hyperscaler—Supabase's growth could be disrupted as suddenly as it accelerated.

The company's open-source foundation provides some insurance against this risk. Because Supabase can be self-hosted, it maintains a grassroots developer community that generates organic word-of-mouth and documentation contributions independent of any AI model's recommendations. With 250,000 customers and a stack that covers the full backend surface area, the switching cost for human-built applications remains high.

## The Broader Ecosystem Signal

Stripe's participation in the round deserves particular attention. The payments company has been quietly building a developer ecosystem play—Stripe's new AI foundational models product and its push into agentic commerce suggest it sees the AI-native application layer as its next frontier. Investing in Supabase, the default backend for AI-generated apps, is a strategic alignment rather than a purely financial bet.

For investors, the round signals continued conviction that the database and backend-infrastructure layer will capture significant value even as AI commoditizes application logic. If AI agents write most application code, the margins on application software compress—but the infrastructure the agents depend on maintains pricing power as long as switching costs remain.

The $10.5 billion valuation puts Supabase in the same tier as mature infrastructure companies with much longer track records. Whether that valuation is justified depends on how quickly Multigres and the vector database roadmap can expand average revenue per customer and how durable the AI coding tool tailwind proves to be. What's not in dispute is that the vibe coding era has created a new category of infrastructure winner—and Supabase is currently its clearest example.
