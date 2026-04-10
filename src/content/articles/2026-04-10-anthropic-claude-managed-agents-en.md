---
title: "Anthropic Launches Claude Managed Agents: A Fully Hosted Platform to Run AI Agents at Scale"
summary: "Anthropic has launched Claude Managed Agents, a cloud-hosted service that handles all production infrastructure for AI agents—including sandboxed execution, state management, credential handling, permissions, and end-to-end tracing. Priced at $0.08 per runtime hour, the platform is already live with enterprise customers including Notion, Rakuten, and Asana."
category: "developer-tools"
publishedAt: 2026-04-10
lang: "en"
featured: false
trending: true
sources:
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/"
  - name: "The New Stack"
    url: "https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/"
  - name: "9to5Mac"
    url: "https://9to5mac.com/2026/04/09/anthropic-scales-up-with-enterprise-features-for-claude-cowork-and-managed-agents/"
  - name: "Help Net Security"
    url: "https://www.helpnetsecurity.com/2026/04/09/claude-managed-agents-bring-execution-and-control-to-ai-agent-workflows/"
  - name: "The Register"
    url: "https://www.theregister.com/2026/04/09/anthropic_offers_to_host_ai/"
tags:
  - "Anthropic"
  - "Claude"
  - "AI agents"
  - "developer tools"
  - "agentic AI"
  - "enterprise AI"
  - "cloud infrastructure"
relatedSlugs:
  - "2026-04-06-agentic-ai-foundation-en"
  - "2026-04-09-anthropic-project-glasswing-en"
  - "2026-04-04-mcp-protocol-explosion-en"
---

Building production AI agents has never been harder—not because the models aren't capable, but because deploying them reliably involves a daunting amount of infrastructure work that has nothing to do with the actual intelligence. State management, sandboxed code execution, credential vaulting, permission scoping, checkpointing, observability tooling, loop-breaking logic—the list of plumbing required before an agent actually does anything useful in production is long, expensive, and technically risky.

Anthropic's answer, unveiled on April 8th, is Claude Managed Agents: a fully hosted cloud service that absorbs all of that infrastructure complexity, letting developers focus on agent logic and business outcomes. The service entered public beta on the Claude Platform as of April 9th.

## What Managed Agents Actually Does

Claude Managed Agents is described by Anthropic as "a suite of composable APIs for building and deploying cloud-hosted agents at scale." In practice, it provides a managed runtime environment where developers deploy Claude-powered agents and Anthropic handles everything behind the scenes: provisioning sandboxed execution environments, maintaining agent state across long-running tasks, managing secure credential storage, enforcing scoped permissions, providing checkpointing so agents can resume from failures, and offering end-to-end distributed tracing for debugging.

The platform also ships with a built-in agent harness—a pre-configured loop optimized for Claude's architecture—which means developers don't need to write their own agent orchestration from scratch or retool it every time Anthropic releases a new model version. Model upgrades within the platform are handled transparently.

"Until now, building agents meant spending development cycles on secure infrastructure, state management, permissioning, and reworking your agent loops for every model upgrade," Anthropic's announcement stated. "Managed Agents pairs an agent harness tuned for performance with production infrastructure to go from prototype to launch in days rather than months."

## The Pricing Structure

Anthropic priced the service at $0.08 per runtime hour, on top of standard Claude model token costs. An agent running continuously would cost approximately $58 per month in runtime fees alone, before accounting for the inference costs that scale with usage. For intermittent or task-based workloads—the majority of enterprise use cases—costs will be substantially lower.

The pricing is designed to position Managed Agents as significantly cheaper than the engineering overhead of building equivalent infrastructure in-house. At current market rates for senior backend engineers, even a modest internal agent infrastructure project would cost multiples of what Anthropic is charging.

## Early Adopters and Use Cases

Anthropic launched with a roster of high-profile design partners. Notion is using Claude Managed Agents to power in-product AI workflows that help users accomplish complex document and knowledge-management tasks. Rakuten is deploying agents across e-commerce and logistics operations. Asana is integrating agents into project management workflows for HR and finance automation. Vibecode and Sentry, both developer-focused companies, are using the platform for code automation—writing, reviewing, and debugging code at scale.

The breadth of early customers signals that Managed Agents is not narrowly focused on a single vertical. Instead, it appears designed to be the lowest-friction path for any enterprise that wants to deploy Claude in persistent, autonomous workflows without standing up dedicated AI infrastructure teams.

## Why This Is a Strategic Pivot for Anthropic

For most of its existence, Anthropic has sold access to Claude models—essentially the intelligence layer—through an API, leaving the infrastructure problem to customers and third-party orchestration frameworks like LangChain, CrewAI, and Mastra. Managed Agents represents a deliberate move up the stack: Anthropic is now selling not just the model, but the runtime that runs the model in production.

This has significant competitive implications. OpenAI has made similar moves with its Assistants API and, more recently, with various agent-hosting features in its enterprise platform. Microsoft Azure has agent orchestration through Azure AI Agent Service. Google offers Vertex AI Agent Builder. Anthropic's differentiator is the tight coupling between the agent harness and Claude's specific capabilities—prompting patterns, tool-use behavior, and safety guardrails are tuned specifically for the Claude model family.

The move also deepens Anthropic's relationship with enterprise customers in a stickier way than API access alone. An enterprise that has built critical workflows on Claude Managed Agents is more deeply embedded in Anthropic's ecosystem than one that simply calls the Claude API through a third-party framework.

## The Infrastructure Layer Becomes a Moat

The broader trend here—hyperscalers and foundation model companies racing to own the agent runtime layer—reflects a recognition that the infrastructure problem is becoming as important as the intelligence problem. Raw model capability is increasingly commoditized; the differentiated value lies in who can make it reliably deployable at enterprise scale.

Anthropic's timing is notable. The company recently surpassed a $30 billion annual recurring revenue milestone, and the launch of Managed Agents provides a new, recurring revenue stream that is directly correlated with customer usage rather than flat API subscriptions. As agents proliferate across enterprise environments, runtime fees compound in a way that pure API pricing does not.

Claude Managed Agents is currently in public beta, available to developers through the Claude Platform. Anthropic has indicated that additional composable features—including enhanced multi-agent coordination tools and expanded tracing dashboards—are on the roadmap for later in 2026.

The practical message to enterprise AI teams is clear: you no longer have to build the scaffold. Anthropic will hold the agents while you teach them what to do.
