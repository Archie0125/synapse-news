---
title: "Google Bets the Enterprise on AI Agents: Ironwood TPU, 8th-Gen Chips, and the Gemini Platform"
summary: "At Google Cloud Next 2026, Google introduced two purpose-built eighth-generation TPUs for training and inference, and rebranded Vertex AI as the Gemini Enterprise Agent Platform, part of a full-stack push to own the agentic enterprise era."
category: "ai-ml"
publishedAt: 2026-04-26
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: true
trending: true
sources:
  - name: "Google Cloud Blog: Next '26 Day 1 Recap"
    url: "https://cloud.google.com/blog/topics/google-cloud-next/next26-day-1-recap"
  - name: "Google Blog: 8th Generation TPUs"
    url: "https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/"
  - name: "Google Cloud: Ironwood TPU"
    url: "https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era"
  - name: "Computer Weekly"
    url: "https://www.computerweekly.com/news/366641999/Google-launches-Gemini-Agent-Platform-eighth-generation-TPUs"
tags:
  - "Google"
  - "TPU"
  - "AI agents"
  - "enterprise AI"
  - "cloud computing"
  - "Gemini"
  - "Google Cloud"
relatedSlugs:
  - "2026-04-24-anthropic-19b-arr-claude-code-growth-en"
  - "2026-04-24-cambridge-neuromorphic-chip-ai-energy-en"
  - "2026-04-25-google-anthropic-40b-investment-en"
---

Las Vegas — Google arrived at its annual Cloud Next conference this week with a message it has been building toward for years: the agentic enterprise era is here, and Google intends to own every layer of it. From custom silicon to frontier models to a unified software platform, the company made its most sweeping set of enterprise AI announcements to date, challenging not just Amazon Web Services and Microsoft Azure, but OpenAI and Anthropic on their own turf.

## Ironwood Goes Generally Available

The centerpiece infrastructure announcement was the general availability of Ironwood, Google's seventh-generation Tensor Processing Unit (TPU) — and the first the company has explicitly designed for the age of inference rather than training. Each Ironwood chip delivers peak compute of 4,614 TFLOPs, backed by 192 gigabytes of HBM, 6x that of Trillium, at 7.37 terabytes per second of bandwidth.

At scale, pods of 9,216 Ironwood chips deliver 42.5 exaflops of compute, more than 24x the compute power of El Capitan, the world's largest supercomputer. Anthropic has committed to up to one million Ironwood units.

## The Next Generation: TPU 8t and TPU 8i

But Ironwood was almost a footnote to the day's hardware headline. Google simultaneously introduced its eighth-generation TPU, split for the first time into two purpose-built chips for training and inference.

The **TPU 8t** targets training. A single superpod hosts 9,600 chips connected by a redesigned Inter-Chip Interconnect (ICI), delivering 121 exaflops of compute and two petabytes of shared high-bandwidth memory — three times the processing power of Ironwood and up to double its performance per watt. For the first time, a single Google pod can hold a model entirely in shared memory during training, eliminating the inter-node communication overhead that has traditionally bottlenecked large-model development.

The **TPU 8i** is built for inference at agent scale. Using a new "Boardfly" topology, the TPU 8i directly connects 1,152 chips in a single pod, features three times more on-chip SRAM than the previous generation, and integrates an on-chip Collectives Acceleration Engine. The result: 80% better performance per dollar for inference workloads compared to the prior generation, and the latency profile needed to run millions of concurrent AI agents cost-effectively.

"A thing of beauty," said Amin, describing the eighth-generation TPU on stage.

Both chips were designed in partnership with Google DeepMind and are expected to be generally available later this year.

## The Gemini Enterprise Agent Platform

On the software side, Google introduced the **Gemini Enterprise Agent Platform**, the evolution of Vertex AI. The rebranding is more than cosmetic. The unified platform covers the full lifecycle of enterprise agents across four capability pillars: build, scale, govern, and optimize.

The **Build** layer introduces Agent Studio — a low-code, visual interface for non-engineers — alongside the Agent Development Kit (ADK), a code-first environment with AI-native coding tools. The **Scale** layer features a re-engineered Agent Runtime capable of maintaining agent state for days, paired with a persistent Memory Bank for long-term context storage across sessions.

The **Govern** layer addresses the enterprise's deepest anxiety about agents: control. Agent Identity, Agent Registry, and Agent Gateway together form a centralized governance fabric — letting IT teams know exactly which agents are running, what they have access to, and what they did. The **Optimize** layer then closes the loop with Agent Simulation for pre-deployment testing, Agent Evaluation for benchmarking, and Agent Observability providing full execution traces and real-time reasoning visibility.

### The A2A Protocol Expansion

For enterprises already running fragmented agent ecosystems, A2A could become the lingua franca of multi-agent orchestration, letting products from competing vendors collaborate on shared tasks.

## Workspace Goes Agentic

The Workspace announcements centered on Workspace Intelligence and new AI features across Docs, Gmail, Drive and Chat. **Ask Gemini in Google Chat** can now synthesize information from across Workspace, surface insights, and deliver proactive daily briefings. **AI Inbox and AI Overviews in Gmail** create a personal, proactive inbox assistant with Gemini. **Google Drive Projects** instantly organizes files and emails around workflow needs.

Google also introduced **Workspace Intelligence** — a semantic layer that learns an organization's voice, style, and brand, then applies it automatically to content creation tasks. The company added Microsoft 365 interoperability through Canvas, letting Workspace users export documents to Office formats natively, a direct acknowledgment of where much of its enterprise competition still lives.

## Security: Wiz Integration and the AI-BOM

Google's $32 billion acquisition of cloud security firm Wiz closed earlier in 2026, and Next showcased the first fully integrated product outcomes. Among the new Wiz items is the **AI Bill of Materials (AI-BOM)** — an automatic inventory of AI frameworks, models, and IDE extensions across an organization's environment. As enterprises accelerate AI adoption through "vibe coding" and third-party agent procurement, the attack surface is ballooning; AI-BOM provides a mechanism to track what's actually running.

Google Security Operations also introduced three new agents: a **Threat Hunting agent** that proactively hunts for novel attack patterns (in preview), a **Detection Engineering agent** that identifies coverage gaps and creates new detections (in preview), and a **Third-Party Context agent** that enriches workflows with contextual data from third-party content (coming soon to preview). These are tasks that have historically required senior security engineers working for hours.

The Agentic Data Cloud received its own announcements as well: a **Knowledge Catalog** serving as a unified, dynamic context graph of entire business data; a **Lightning Engine for Apache Spark** delivering up to 4.5x faster performance than open-source alternatives and 2x better price-performance against leading competitors; and a **Cross-Cloud Lakehouse** built on Apache Iceberg that lets enterprises query data stored in AWS or Azure without copying it.

## Google's Full-Stack Argument

CEO Thomas Kurian framed these announcements around a unified stack, with chips, models, agents and applications built together; the pitch is that Google owns all four layers: custom silicon (TPUs), frontier models (Gemini), the cloud platform (now Gemini Enterprise Agent Platform), and enterprise distribution (Workspace).

"Chips that are designed for models, models that are grounded in your data, agents and applications that are built with those models," Kurian said on stage, describing what he called the integrated bet against the market.

That bet is explicitly aimed at OpenAI and Anthropic as much as at Microsoft and AWS. By building the Gemini Enterprise Agent Platform as a direct competitor to Microsoft Copilot and OpenAI's enterprise offerings — while simultaneously providing Anthropic's models through its infrastructure — Google is playing a multi-layered competitive game that few companies have the asset base to attempt.

"A big focus of ours is to always be customer zero for our own technologies," Pichai said in his opening remarks.

## What Comes Next

Both eighth-generation TPUs are expected to be generally available later this year. The Gemini Enterprise Agent Platform is available now, replacing prior access paths through Vertex AI and Agentspace. The A2A protocol expansions with enterprise SaaS partners are rolling out through Q2 2026.

Whether Google's full-stack approach can translate into durable enterprise revenue — against Microsoft's dominant installed base and OpenAI's brand gravity in the developer community — will likely define the company's cloud business for the next several years. Cloud Next 2026 was the clearest articulation yet of how Google intends to try.

*Correction (November 15, 2026): 19 sentences were corrected or removed to match the sources listed on this page.*
