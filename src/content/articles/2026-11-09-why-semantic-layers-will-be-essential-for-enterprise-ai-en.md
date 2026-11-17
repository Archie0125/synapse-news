---
category: ai-ml
faqs:
- answer: Semantic layers encode what business terms actually mean at a specific company,
    such as how "pipeline" is defined by sales stages and qualification rules. Without
    that layer, AI agents can retrieve the right data and still answer the wrong question.
  question: What problem do semantic layers solve for enterprise AI?
- answer: Standards like MCP give agents access to systems such as CRMs, warehouses
    and ERPs, but access is not understanding. An agent connected to everything can
    still misread business rules that were never written down.
  question: Why isn't MCP enough on its own?
- answer: They should invest in codifying business definitions and rules, not only
    in connecting more data sources. The article argues that if the agent layer doesn't
    understand the business, the systems underneath it don't matter.
  question: What should enterprises prioritize when deploying agents?
featured: false
lang: en
publishedAt: '2026-11-09T15:00:00+00:00'
relatedSlugs: []
sources:
- name: The New Stack
  url: https://thenewstack.io/semantic-layers-enterprise-ai/
summary: MCP solved how AI agents reach enterprise data, not whether they understand
  it, and the semantic layer is where enterprise AI succeeds or fails.
tags:
- ai-ml
- developer-tools
- industry
title: Why semantic layers will be essential for enterprise AI
trending: false
type: news
---

# Why semantic layers will be essential for enterprise AI

**AI can find your data. It can’t read your mind.** AI agents can already reach into your CRM, your warehouse, and your ERP, and with [standards like MCP](https://thenewstack.io/mcp-release-candidate-rewrite/), that list keeps growing. Access is solved. Understanding is not. An agent can retrieve every record in your pipeline and still give your CRO the wrong answer, not because the data is bad, but because it doesn’t know what *you* mean by “pipeline.” Agents without semantics don’t fail loudly. They deliver confident answers to the wrong question.

## “Pipeline” means something different at every company

Ask an executive, “How is pipeline looking this quarter?” and it sounds like a simple request. It isn’t. The answer depends on your sales stages, your forecasting methodology, your territory structure, and your qualification criteria, which are business rules that evolved over years, often without ever being written down. Two companies can use the same word and mean entirely different things. Businesses don’t run on raw data. They run on shared meaning, and humans carry that meaning around in their heads. Agents don’t have heads. They have whatever we give them.

## From systems of record to systems of agency

That matters more as the way we work changes. For decades, employees logged into the CRM, the BI tool, or the ERP and supplied the judgment themselves, because they knew which dashboard to trust and which field was never quite right. Now they state intent, and an agent figures out the rest.

The systems of record stay where they are, but a new layer sits between people and technology: a system of agency. In my experience, leaders spend a lot of time asking whether that layer can connect to everything and far less time asking whether it understands anything. If that layer doesn’t understand your business, nothing underneath it matters.

## Catalogs helped people find data. Semantic layers help AI understand it.

For the last decade, we invested in governance, integration, quality, and catalogs, and those investments still matter because trusted data is the prerequisite. But a catalog tells people where the data lives. A semantic layer tells AI what it means. It captures what your best people carry in their heads:

- Business definitions, such as what counts as “pipeline,” “churn,” or “active customer”
- Policies that govern how data can be used
- Relationships between products, customers, contracts, and outcomes
- Rules that determine how decisions get made

“A catalog tells people where the data lives. A semantic layer tells AI what it means.”


Put that in a form both humans and machines can consume, and agents stop guessing. This isn’t a nice-to-have. It’s the difference between an agent that is technically capable and one that is operationally reliable.

## Relationships are where the value lives

Definitions are only half the story, because business decisions rarely live in a single dataset. They depend on how concepts connect. Take an AI-powered quoting process, where the agent needs products, contracts, customer history, usage patterns, approval structures, and pricing rules all at once, and each lives in a different system. Retrieving them is the easy part.

Reasoning across them is the hard part, and when the agent gets it wrong, it won’t throw an error. It will produce a plausible quote with the wrong discount and send it to a real customer. That’s where knowledge graphs and context graphs earn their place. They treat information as [connected business knowledge](https://thenewstack.io/your-ai-is-working-with-half-a-brain-you-need-the-other-half/) rather than isolated facts, so instead of piecing together a customer’s story from scattered records, the agent gets a map of how your business fits together.

## Meaning is also an efficiency play

Without encoded context, agents spend compute rediscovering relationships and re-inferring meaning your organization already understands, so every query becomes a small act of reconstruction. Define it once, and every agent reasons from the same source. That means more consistent answers, fewer contradictions between teams, and lower cost as usage scales. Consistency is underrated. If sales, finance, and operations each get a different answer to the same question from the same AI, you haven’t built intelligence. You’ve built an argument.

## Anyone can build now. Not everything should scale.

Generative AI has finally delivered on the citizen developer promise. Employees can describe a workflow in plain language and get a working prototype back, which means good ideas can now come from anywhere. That’s the opportunity.

“If sales, finance, and operations each get a different answer to the same question from the same AI, you haven’t built intelligence. You’ve built an argument.”


The risk is that a tool that helps one person is a convenience, while the same tool deployed across departments is a liability if no one validated it, governed it, or owns it. Organizations need a path from experiment to enterprise asset. I think of it as a graduation factory: identify the promising prototypes, test them, apply governance, and promote the ones that earn it. Innovation should be easy to start and hard to scale carelessly.

The same foundations apply here. Only 12% of organizations say their [data is AI-ready](https://thenewstack.io/how-precog-adds-business-context-to-make-enterprise-data-ai-ready/), and only 31% can tie their AI initiatives to clear KPIs. Semantics and governance are how you close that gap.

## Where I’d start

You don’t need a multi-year program to make progress. Start small and prove it:

1. Pick the five terms your executives argue about most, and define them.
2. Assign a business owner to each definition.
3. Expose those definitions to your agents through a governed layer, then measure whether the answers improve.

Meaning, like data, has to be managed. Someone has to own it.

## The bottom line

Connecting AI to your data is table stakes. Everyone will do it, so it won’t differentiate you. Trusted data is the prerequisite. Shared meaning is the multiplier. Connect your agents to everything, and you’ve built access. Teach them how your business thinks, and you’ve built an advantage.

			
				[YOUTUBE.COM/THENEWSTACK
			
			
				Tech moves fast, don't miss an episode. Subscribe to our YouTube 
				channel to stream all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)

## Summary

**TLDR:** MCP solved how AI agents reach enterprise data, not whether they understand it, and the semantic layer is where enterprise AI succeeds or fails.

- Standards like MCP let agents connect to CRMs, warehouses and ERPs, so access is largely solved.
- Business terms like "pipeline" mean different things at each company, based on unwritten rules about stages, territories and qualification.
- Agents without semantics don't fail loudly; they give confident answers to the wrong question.
- A new "system of agency" layer is forming between people and systems of record, and it needs codified business meaning.
- Leaders focus on connectivity over comprehension, which is the wrong priority for agent deployments.

## 摘要

**重點摘要：** MCP 解決了 AI 代理「拿得到」企業資料的問題，卻沒解決「看得懂」，企業 AI 的成敗就落在語意層。

- MCP 等標準讓 AI 代理能接上 CRM、資料倉儲和 ERP，「取用」這關基本上已經過了。
- 像「pipeline」這樣的商業用語，每家公司的定義都不同，背後是銷售階段、業務區域、資格標準等多年沒寫下來的規則。
- 缺乏語意的代理不會明顯出錯，而是很有自信地回答一個錯誤的問題。
- 人與紀錄系統之間正在出現一層新的「代理系統」，它需要被明確寫下的商業語意。
- 主管們太在意「能不能連」，太少問「懂不懂」，這是導入代理時的錯誤優先順序。