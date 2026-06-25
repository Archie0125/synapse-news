---
title: "Snowflake Bets the Enterprise on AI Agents with CoWork, CoCo, and a Deep Anthropic Alliance"
summary: "At Snowflake Summit 2026 in San Francisco on June 2, CEO Sridhar Ramaswamy unveiled more than 26 new capabilities under the organizing theme of the 'agentic enterprise,' including CoWork—a personal AI agent for knowledge workers—and CoCo, Snowflake's full-stack coding agent. Anthropic President Daniela Amodei co-keynoted, formalizing one of enterprise AI's deepest platform partnerships with Claude Opus 4.8 powering both products. The announcements signal a strategic pivot from data platform to AI operating system."
category: "industry"
publishedAt: 2026-06-25
lang: "en"
featured: false
trending: false
sources:
  - name: "Snowflake: CoWork Powers the Agentic Enterprise"
    url: "https://www.snowflake.com/en/news/press-releases/snowflake-cowork-powers-the-agentic-enterprise-as-the-personal-agent-for-knowledge-workers-to-work-smarter/"
  - name: "Snowflake: CoCo Redefines Enterprise AI Development"
    url: "https://www.snowflake.com/en/news/press-releases/snowflake-coco-redefines-enterprise-ai-development-as-the-coding-agent-built-for-faster-easier-and-more-powerful-innovation-anywhere/"
  - name: "Snowflake and Anthropic Accelerate Enterprise AI Adoption"
    url: "https://www.snowflake.com/en/news/press-releases/snowflake-and-anthropic-accelerate-enterprise-ai-adoption-driven-by-rising-demand-for-governed-ai/"
  - name: "Flexera: Snowflake Summit 2026 recap — 25+ announcements"
    url: "https://www.flexera.com/blog/perspectives/snowflake-summit-2026/"
  - name: "Atlan: Snowflake Summit 2026 — All the Announcements and What They Mean"
    url: "https://atlan.com/know/snowflake/summit-2026-announcements/"
tags:
  - "Snowflake"
  - "CoWork"
  - "CoCo"
  - "Anthropic"
  - "enterprise AI"
  - "AI agents"
  - "C2PA"
  - "data platform"
  - "Claude"
relatedSlugs:
  - "2026-06-04-anthropic-claude-opus-48-dynamic-workflows-en"
  - "2026-06-23-openai-codex-record-replay-workflow-automation-en"
  - "2026-06-12-openai-acquires-ona-gitpod-codex-cloud-agents-en"
---

When Sridhar Ramaswamy walked onto the stage at the Moscone Center in San Francisco on June 2, 2026, for his second Snowflake Summit as CEO, the company he was running looked meaningfully different from the one he inherited. Gone was the emphasis on Snowflake as a neutral data storage and query layer. In its place: a full-stack agentic platform with more than 26 new capabilities, two renamed and substantially rebuilt products, and an onstage co-keynote with Anthropic President Daniela Amodei.

The message was unambiguous: Snowflake is not trying to build the best database. It is trying to build the operating system for the agentic enterprise.

## CoWork: A Personal AI Agent That Already Knows Your Business

The most strategically significant announcement of Snowflake Summit 2026 may have been the least flashy: the renaming and expansion of **Snowflake Intelligence** into **Snowflake CoWork**.

CoWork is positioned as a "personal agent for knowledge workers"—an AI system that can access a company's governed Snowflake data, synthesize it into actionable insight, and take structured actions across connected enterprise systems. Unlike generic AI assistants that must be given context from scratch in every session, CoWork operates within Snowflake's data governance layer. Every query, every output, and every action is logged, auditable, and subject to the access controls that already govern who can see what data.

The design philosophy is what Ramaswamy called "AI that already knows your business." The argument is that generic AI assistants fail in enterprise deployments not because the underlying models are inadequate, but because those models lack access to the institutional context—the internal terminology, the business logic, the definitions of what the data actually means—that makes an output useful for a specific organization.

Three new capabilities announced at Summit develop this premise. **Artifacts** allows CoWork to produce persistent, shareable outputs—charts, reports, analyses—that are attached to Snowflake's lineage graph, so anyone consuming that analysis can trace it back to the specific data tables it was derived from. **Cortex Sense**, the new shared context layer discussed below, ensures CoWork understands the business meaning of data labels rather than just their technical schema. And new personalization capabilities allow individual users to calibrate CoWork's defaults to their role and communication preferences—so a data scientist and a sales director asking CoWork the same question receive answers calibrated to different levels of technical depth.

## CoCo: Snowflake Enters the Coding Agent Race

The second major renaming of Summit 2026 transformed **Cortex Code** into **Snowflake CoCo**—the company's AI coding agent, now positioned explicitly as a challenger in the space occupied by GitHub Copilot, Cursor, and OpenAI's Codex.

CoCo's differentiation argument is context. Where third-party coding agents have access only to the code a developer is writing, CoCo also has access to the Snowflake schemas, transformation pipelines, and data contracts that define the environment the code will run in. A developer asking CoCo to write a SQL transformation for a new data model does not need to explain what tables exist, what the column names mean, or what business logic governs the data—CoCo already knows, from the same Cortex Sense context layer that powers CoWork.

This vertical integration is Snowflake's core argument for why AI built into the data layer produces better results than AI bolted on top of it. The company is betting that data engineers building dbt models, Snowpark applications, and SQL pipelines will prefer a coding agent that understands their data environment to one that requires manual context injection before every task.

Whether CoCo can take meaningful share from tools with larger developer mindshare—Cursor, in particular, has become nearly synonymous with AI-assisted development among younger engineers—is an open question. Snowflake's distribution advantage is real: it already serves more than 9,000 enterprise customers whose developers are building data pipelines inside Snowflake environments every day. The question is whether those developers are persuadable to replace their general-purpose coding agent with one that knows their specific Snowflake schema.

## Cortex Sense: The Shared Context Layer

The most architecturally interesting announcement at Summit 2026 was **Cortex Sense**—not for what it does in isolation, but for how it changes the architecture of everything else.

Cortex Sense is a semantic layer that unifies the business meaning of enterprise data into a single, shared context representation used by every Snowflake AI product. It reads table schemas, data contracts, column descriptions, lineage graphs, and documentation (including dbt documentation), then produces a structured context object that CoWork, CoCo, and any third-party tool built on Snowflake's Cortex AI APIs can consume without re-ingesting raw documentation.

The practical consequence: a company that maintains good Snowflake documentation gets AI products that understand its business by default. When schemas change, Cortex Sense updates automatically, meaning CoWork and CoCo stay current without requiring developers to re-prompt the AI every time the data model evolves.

The deeper implication is architectural. Cortex Sense makes the documentation and institutional knowledge that companies embed in their Snowflake data model into a first-class artifact consumed by AI products—changing the economics of documentation investment. Under Cortex Sense, well-documented data tables immediately translate into better AI outputs, creating a new business incentive for data quality work that has historically been difficult to justify.

## The Anthropic Alliance at the Center

Powering both CoWork and CoCo is Claude, Anthropic's model family. Snowflake announced at Summit that **Claude Opus 4.8**—released the same day as the keynote—was immediately available in Snowflake Cortex AI, allowing enterprises to run Claude on Snowflake's infrastructure without exporting data to external endpoints. For industries with strict data residency requirements, this availability within Snowflake's governance boundary is a material compliance advantage.

The partnership goes well beyond an API integration. Daniela Amodei co-keynoted with Ramaswamy—an unusual move for a model provider at a customer conference—and Snowflake was announced as one of ten launch partners in Anthropic's **Claude Marketplace**, which allows companies with existing Anthropic enterprise commitments to apply those credits toward Snowflake AI products, reducing procurement friction for joint customers.

The Marketplace arrangement is structurally advantageous for both companies. Snowflake gains access to Anthropic's growing base of enterprise Claude customers—companies that have already made the procurement decision to standardize on Claude and are now looking for governed ways to apply it to their data. Anthropic gains a distribution channel into Snowflake's enterprise customer base, where data assets exist but AI products capable of acting on that data within a governance framework are still a relatively new category.

## The Broader Infrastructure Bet

Snowflake announced several platform-level capabilities at Summit that extend beyond the CoWork and CoCo headlines.

**Cortex Training** allows enterprises to fine-tune models on their own Snowflake data without moving that data to external training infrastructure—a significant reduction in the friction between having proprietary data and having a model that reflects it.

**Snowflake Datastream**, a new fully managed streaming service for Apache Kafka, brings real-time data ingestion into the platform. The addition matters for agent applications: CoWork and CoCo are most valuable when operating on current data, and Datastream provides a governed pathway for real-time data to flow into the context that those agents consume.

The company also announced support for **Apache Iceberg v35** and Snowflake Storage for Apache Iceberg Tables—a significant interoperability statement that allows enterprises to maintain a single, live, governed copy of data across Snowflake and external data lakes without duplication. This open-table-format push is partly defensive (insulating Snowflake against competitors building on open formats like Delta Lake) and partly expansive (making Snowflake's AI products available to data that lives in external systems).

## What This Signals About Enterprise AI

The Snowflake announcements fit into a pattern that has become increasingly legible in enterprise AI over the first half of 2026: the competition is shifting from individual model capability to integrated platform coverage.

No individual AI tool—however capable the underlying model—operates effectively in an enterprise without access to the right data, in a governed context, with the auditability that compliance and legal requirements demand. That bundling problem is what Snowflake is positioning itself to solve, with Anthropic's Claude as the reasoning engine and Snowflake's data platform as the institutional memory.

The company's strategic bet is that enterprise AI will consolidate around platforms that own the data governance layer—just as cloud infrastructure consolidated around AWS, Azure, and Google Cloud after a period of fragmentation. The analogy is imperfect but instructive: in the cloud wars, the winner was not the company with the best individual service, but the company with the broadest governed platform that enterprises could standardize on.

If that consolidation logic holds for AI, Summit 2026 may look in retrospect like the moment Snowflake staked its claim—with 20,000 developers in San Francisco and Daniela Amodei onstage as the evidence that it has the model partner to make the bet credible.
