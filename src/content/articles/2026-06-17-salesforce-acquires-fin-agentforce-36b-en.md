---
title: "Salesforce Acquires AI Customer Service Platform Fin for $3.6 Billion"
summary: "Salesforce announced a $3.6 billion deal to acquire Fin, the AI customer service company formerly known as Intercom, in its largest acquisition since buying Slack for $27.7 billion in 2021. The deal brings Fin's proprietary Apex model and its network of enterprise customers into Salesforce's Agentforce platform, as Marc Benioff bets that autonomous AI agents — not seats-based software — will define the next decade of enterprise CRM."
category: "products"
publishedAt: 2026-06-17
lang: "en"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/15/salesforce-acquires-ai-customer-service-platform-fin-for-3-6b/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/15/salesforce-ai-customer-service-fin-acquistion.html"
  - name: "Salesforce Press Release"
    url: "https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/"
  - name: "CMSWire"
    url: "https://www.cmswire.com/customer-experience/salesforce-acquires-fin/"
tags:
  - "Salesforce"
  - "Fin"
  - "Intercom"
  - "Agentforce"
  - "AI agents"
  - "customer service AI"
  - "enterprise software"
  - "Marc Benioff"
  - "Eoghan McCabe"
relatedSlugs:
  - "2026-04-03-vertical-ai-saas-en"
  - "2026-04-04-cursor-devin-war-en"
---

On Monday morning, Salesforce CEO Marc Benioff announced a definitive agreement to acquire Fin — the company formerly known as Intercom — for $3.6 billion in cash and stock. The deal is Salesforce's most significant acquisition in five years, and its timing makes its strategic intent unmistakable: Benioff is betting that the enterprise software company he built over 25 years on the concept of "no software" must now reinvent itself around a new concept — "no humans required."

The transaction is expected to close in the fourth quarter of Salesforce's fiscal year 2027, which runs through early calendar 2027, subject to regulatory approval.

## What Fin Actually Does

Fin launched as Intercom in 2011, founded by Eoghan McCabe along with Des Traynor, Ciaran Lee, and David Barrett. For most of its existence, Intercom was a customer messaging platform — a smarter, more conversational alternative to traditional helpdesk ticketing systems. Companies embedded Intercom's chat widget on their websites to handle customer questions, support tickets, and sales conversations.

The rebranding to Fin in 2024 was more than cosmetic. The company had pivoted its core product around a single ambition: an AI agent that could resolve customer issues entirely autonomously, without routing to a human agent. The new name reflected the new product: Fin AI Agent, powered by Apex, a proprietary model the company says was purpose-built for customer support use cases.

Apex is a notable technical achievement in a narrow domain. According to Fin's benchmarks, the model outperforms frontier models from OpenAI and Anthropic when measured by resolution rate — the percentage of customer inquiries it can resolve without human escalation. The claim is credible: support resolution is a highly structured task with narrow intent categories, where a purpose-built model with access to company knowledge bases can outperform a general-purpose frontier model without the full breadth of general reasoning.

Fin's AI Agent operates across every channel an enterprise customer service operation runs: live chat, email, WhatsApp, SMS, phone calls, and Slack. It uses a combination of retrieval from internal documentation and knowledge bases, workflow automation for resolution steps like issuing refunds or updating account information, and escalation to human agents when confidence falls below threshold.

The company also developed an internal tool called Operator — an AI agent framework for building more complex automated workflows within the Fin ecosystem. Operator represents Fin's bet that customer service orchestration, not just individual query resolution, is where the real enterprise value sits.

## The Agentforce Angle

For Salesforce, Fin is a strategic acquisition that addresses a specific gap in Agentforce.

Agentforce, launched publicly in late 2024, is Salesforce's platform for building, deploying, and managing AI agents across enterprise workflows. It is Benioff's declared answer to the question of what Salesforce does in a world where AI agents can perform the tasks that CRM software historically tracked and organized. Instead of managing records of what salespeople and customer service agents did, Agentforce is meant to be the operating system for AI agents that do the work themselves.

The challenge Agentforce has faced is the same one confronting every enterprise platform trying to sell AI agents: trust. Enterprise buyers want to see proven resolution rates, auditable decision trails, and clear accountability when an agent makes a mistake. Building that trust track record from scratch, inside a platform that has never done autonomous resolution before, takes years.

Fin removes that problem by acquisition. The company has a live production network of enterprise customers — including major retailers, SaaS companies, and financial services firms — who are already running Fin AI Agent at scale. Their resolution rates, their edge case taxonomies, and their failure modes are production data, not lab benchmarks. Integrating that knowledge and that customer trust into Agentforce compresses years of market development into a single deal.

Benioff framed the strategic logic directly in the announcement: the acquisition will help companies "accelerate time to value with trusted agents that deliver measurable outcomes." The key word is "trusted" — it signals that Salesforce understands the barrier to enterprise AI agent adoption is not model capability but proven reliability.

## The Intercom Transformation Story

The acquisition is also a remarkable company narrative. Intercom was founded in Dublin in 2011 and spent more than a decade as one of the most successful B2B SaaS companies of its generation. It raised over $240 million in venture capital, achieved unicorn status in 2018, and was widely expected to IPO. The company had over 30,000 customers at its peak and $400+ million in annual revenue.

Then OpenAI released GPT-3.5, and Eoghan McCabe made a decision that most incumbent SaaS CEOs were unable or unwilling to make: he bet the company on the pivot.

"We were existentially threatened," McCabe said in a 2024 interview. "Every customer was asking us whether they still needed us. The answer was: if we don't rebuild around AI resolution, they don't."

The rebranding from Intercom to Fin was the culmination of that pivot. The company rebuilt its core product around autonomous AI resolution, launched Apex, and reoriented its sales motion around resolution rate — a metric that traditional SaaS companies never tracked because their software didn't claim to resolve anything. Fin now bills on outcomes (resolved queries) rather than seats (licensed users), a pricing model that aligns perfectly with Salesforce's Agentforce pricing philosophy.

McCabe confirmed he will remain as CEO of the Fin division within Salesforce, with R&D leadership staying in place. He described the deal as "a chance to bring autonomous support to every company in the world, with the distribution and trust that Salesforce brings."

## Competitive Context

The acquisition is part of a broader consolidation pattern in enterprise AI agents. ServiceNow acquired AI workflow startup Moveworks in 2025. Microsoft's Copilot Studio absorbed multiple agentic tools from its ecosystem. Zendesk has been aggressively integrating AI resolution features into its platform.

The common thread: established enterprise software companies are racing to acquire the customer trust and production track records that their legacy platforms cannot develop organically fast enough to matter. AI-native startups that have spent two to three years building real resolution track records with enterprise customers are enormously valuable precisely because they have something that money alone cannot quickly replicate.

At $3.6 billion, Fin commands a substantial premium to revenue — probably eight to ten times revenue on current run rate estimates. The market implied by that valuation is not Fin's current customer base but the share of Salesforce's 150,000+ customer installed base that could be migrated to autonomous AI customer service operations. If even 20% of Salesforce enterprise customers replace human-staffed support tiers with Fin-powered agents, the economic logic of the acquisition becomes obvious.

For enterprise software observers, the Fin acquisition is a signal about where the next five years are heading. The CRM category was built on the premise that software helps humans do their jobs better. The Agentforce-plus-Fin bet is that software is about to do many of those jobs itself.
