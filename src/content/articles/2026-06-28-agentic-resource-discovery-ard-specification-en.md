---
title: "ARD: The Open Standard That Lets AI Agents Find Each Other Across the Entire Web"
summary: "Google, Microsoft, GitHub, Nvidia, Salesforce, Snowflake, and seven other technology companies have jointly released the Agentic Resource Discovery specification—an open standard that enables AI agents to discover, verify, and connect with tools, APIs, and other agents anywhere on the web without manual integration. ARD draws an explicit parallel to how search engines solved the early web's discoverability problem and could reshape how multi-agent enterprise systems are built."
category: "developer-tools"
publishedAt: 2026-06-28
lang: "en"
featured: false
trending: true
sources:
  - name: "Google Developers Blog"
    url: "https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/"
  - name: "Microsoft Command Line"
    url: "https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/"
  - name: "Hugging Face Blog"
    url: "https://huggingface.co/blog/agentic-resource-discovery-launch"
  - name: "Search Engine Journal"
    url: "https://www.searchenginejournal.com/google-microsoft-back-draft-ai-agent-discovery-spec/579894/"
tags:
  - "ARD"
  - "AI agents"
  - "open standard"
  - "Google"
  - "Microsoft"
  - "interoperability"
  - "MCP"
  - "developer tools"
relatedSlugs:
  - "2026-06-27-arcade-60m-ai-agent-security-mcp-en"
  - "2026-06-23-agentjacking-sentry-mcp-ai-coding-attack-en"
  - "2026-06-11-visa-openai-ai-agents-payments-en"
---

The early web had a problem that looks obvious in retrospect: millions of pages existed, but most people only visited sites that came pre-filled in their browser bookmarks. The content was there, but nobody could find it. Search engines didn't create the web—they made the web that already existed actually usable by solving discovery at scale.

The agentic AI ecosystem in 2026 has the same problem.

Hundreds of thousands of AI tools, APIs, MCP servers, and specialized agents now exist across the internet. They can perform code analysis, legal document review, financial modeling, supply chain optimization, and thousands of other tasks. But today's AI agents can only use resources that have been explicitly wired to them by developers—discovered manually, integrated individually, and maintained by hand. As the ecosystem expands faster than any team can keep pace with manually, the fundamental constraint on agent capability is not intelligence. It is wiring.

The Agentic Resource Discovery specification, released June 17 and backed by eleven of the world's largest technology companies, is an attempt to solve that wiring problem with the same approach search engines used for web pages: a standardized, crawlable discovery layer that lets agents find what they need at runtime rather than requiring developers to anticipate it at build time.

## Who Is Behind It

The specification was developed collaboratively by **Google**, **Microsoft**, **Cisco**, **Databricks**, **GitHub**, **GoDaddy**, **Hugging Face**, **Nvidia**, **Salesforce**, **ServiceNow**, and **Snowflake**. It is licensed under Apache 2.0 and builds on the AI Catalog data model from the Linux Foundation's AI Catalog Working Group. The breadth of backing—spanning cloud infrastructure, developer tooling, enterprise software, and AI platforms—signals that this is positioned as a foundational layer rather than a proprietary format.

Notably absent from the launch coalition are OpenAI and Anthropic, the two companies with the largest active developer communities. The specification's lead authors—Google's Junjie Bu (Senior Staff Software Engineer) and Srinivas Krishnan (Distinguished Software Engineer)—acknowledged in the launch announcement that broader industry participation is the goal, and that the spec is designed to be adoptable by any platform.

## How ARD Actually Works

The specification operates on two core primitives.

The first is the **catalog**: a machine-readable `ai-catalog.json` file that organizations publish at a well-known path on their domain. The catalog describes what AI capabilities an organization makes available—tools, agents, APIs, skills—with enough structured metadata for an AI system to understand what each capability does, what inputs it requires, what permissions it needs, and how to invoke it. Domain ownership serves as cryptographic identity verification: if a catalog lives at `stripe.com/ai-catalog.json`, it is authoritative for Stripe's AI capabilities in a way that a third-party catalog entry for "Stripe's payment API" is not.

The second is the **registry**: a search layer that crawls published catalogs, indexes their contents, and responds to natural-language discovery queries with ranked matches. The registry is not a single centralized database—it's a specification for how registries work, which means multiple registries can coexist, compete on quality, and specialize by domain. An organization can run a private registry that indexes only its internal catalogs alongside selected vendor resources, while also exposing its public capabilities to global registries that developers worldwide can query.

The ARD team draws the comparison to DNS deliberately. DNS enables local control—any organization can manage its own domain—while participating in a global namespace. ARD applies the same architecture to AI capability discovery: organizations control their own capability definitions, and discovery infrastructure can be distributed rather than relying on a single chokepoint.

## What This Means for MCP

The model context protocol, which Anthropic released in late 2024 and which became the dominant standard for connecting AI models to external tools, is not displaced by ARD—it's complemented by it.

MCP answers the question of *how* to invoke a resource: it defines the wire protocol for calling a tool, passing parameters, receiving results, and managing sessions. ARD answers a different question: *which* resource to invoke, from the full universe of available options, for a given task.

In a complete agentic workflow, ARD operates before MCP. An agent receives a task—"analyze the legal risk in this contract"—and queries an ARD registry to discover which legal analysis tools, agents, or MCP servers are available, appropriate for the task, and authorized for use by this agent's operator. The registry returns ranked matches with invocation details. The agent then uses MCP (or a REST API, or whatever native protocol the resource specifies) to actually call the tool.

This layering means that the investment organizations have already made in MCP-compliant tools is not wasted. ARD makes those tools more discoverable, not less compatible.

## Early Implementations

The two most significant reference implementations shipped alongside the specification itself.

**GitHub Copilot's Agent Finder** is the most prominent. It indexes ARD-compliant resources—including MCP servers, GitHub Copilot Skills, and third-party agents—and makes them discoverable within Copilot at runtime. When a developer asks Copilot to complete a task that requires an external capability, Agent Finder queries the indexed catalog, presents matches for developer approval, and loads only the needed resources into context. This prevents the context-window bloat that currently plagues manual multi-tool Copilot configurations, where developers pre-load dozens of MCP servers regardless of relevance.

**Hugging Face's Discover Tool** wraps the Hub's semantic search—covering thousands of Spaces, ML applications, and MCP servers—in the ARD envelope, making it queryable by any ARD-compliant agent. Given Hugging Face's position as the dominant open-weight model and tool repository, this means a significant fraction of the open-source AI ecosystem becomes ARD-discoverable immediately.

Google Cloud's Agent Registry within the Gemini Enterprise Agent Platform also supports ARD, with native support available in Agent Platform "in the coming months."

## The Problem It Is Actually Trying to Solve

The specification's framing is ambitious. The founding document at Microsoft's Command Line blog describes the current state of agent integrations as equivalent to a web where "millions of pages existed, but most people only visited the sites that came prefilled in their browser's bookmarks." The web was there, but it was dark.

That framing is accurate in a way that is easy to underestimate. Enterprise AI deployments in 2026 are overwhelmingly custom-wired: a team identifies the tools their agents need, integrates them manually, tests the integrations, and maintains them as tool APIs evolve. This works when the relevant tool space is small and stable. It breaks down when organizations have dozens of business units each with their own tool ecosystems, or when an agent needs to access a tool it wasn't built to know about.

The catalog-and-registry model means that a new tool published by, say, a legal tech vendor automatically becomes discoverable to any agent that queries a registry indexing that catalog—without any developer action beyond the vendor publishing their `ai-catalog.json`. The integration work moves from "each agent must know about each tool" to "each tool publishes once, any agent can find it."

## What Still Needs to Happen

ARD is a draft specification with eleven corporate backers and two reference implementations. That is a meaningful starting point—considerably more backing than most developer standards receive at launch—but the distance between "promising specification" and "infrastructure the industry actually uses" is long.

The critical variable is adoption by tool and platform providers. If Stripe publishes an ARD catalog, if Salesforce makes its Agentforce capabilities ARD-discoverable, if enterprise software vendors treat `ai-catalog.json` as a standard part of their product distribution, ARD could genuinely become the DNS of AI capability discovery. If adoption stalls at the founding coalition and doesn't expand to the broader ecosystem of tool providers, it becomes one of many interoperability proposals that looked promising on launch day and were forgotten by the end of the year.

The Apache 2.0 license and Linux Foundation data model ancestry are positive signals—they suggest the intention to build neutral, broadly adoptable infrastructure rather than a standard that benefits one vendor's platform disproportionately. Whether OpenAI and Anthropic eventually join the coalition will matter significantly for developer trust: a standard that doesn't work with ChatGPT Plugins or Claude Tools has incomplete coverage of the market it's trying to serve.

For developers building agent applications today, the practical advice is to track ARD without blocking on it. The specification is real, the implementations exist, and the backing is serious. But the killer application—agents that discover the right tool for any task across the full ecosystem of available resources—is still ahead of where the infrastructure stands today.

The analogy to search engines remains instructive. Google wasn't inevitable. Yahoo's curated directory existed first, worked fine for its era, and became obsolete when the web grew too large for manual curation. ARD is betting that agentic AI will follow the same pattern—that the manual wiring era is temporary, and that the discoverable-at-runtime future is where the ecosystem is heading. The bet is plausible. Whether the ARD specification specifically is the one that wins is still an open question.
