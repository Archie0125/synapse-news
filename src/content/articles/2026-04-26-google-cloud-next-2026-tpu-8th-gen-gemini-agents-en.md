---
title: "Google Bets the Enterprise on AI Agents: Ironwood TPU, 8th-Gen Chips, and the Gemini Platform"
summary: "At Google Cloud Next 2026 in Las Vegas, Google unveiled its seventh-generation Ironwood TPU now generally available, previewed two purpose-built eighth-generation chips for training and inference, and rebranded its entire enterprise AI stack as the Gemini Enterprise Agent Platform — the company's most ambitious full-stack bet to own the agentic enterprise era."
category: "ai-ml"
publishedAt: 2026-04-26
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

The centerpiece infrastructure announcement was the general availability of Ironwood, Google's seventh-generation Tensor Processing Unit (TPU) — and the first the company has explicitly designed for the age of inference rather than training. Each Ironwood chip delivers 4.6 petaFLOPS of peak FP8 compute, roughly four times the performance of its predecessor Trillium, backed by 192 gigabytes of HBM3e memory running at 7.37 terabytes per second of bandwidth.

At scale, clusters of 9,216 Ironwood chips deliver 42.5 exaflops of aggregate compute, a figure that exceeds any existing publicly announced supercomputer. Anthropic is already the highest-profile customer: under its expanded deal with Google, the AI safety company will gain access to up to one million TPU chips and more than a gigawatt of capacity in 2026, with an initial phase covering 400,000 Ironwood units — a contract estimated at roughly $10 billion in finished rack value.

## The Next Generation: TPU 8t and TPU 8i

But Ironwood was almost a footnote to the day's hardware headline. Google simultaneously previewed its eighth-generation TPU architecture, split for the first time into two purpose-built chips designed for distinct workloads.

The **TPU 8t** targets training. A single superpod hosts 9,600 chips connected by a redesigned Inter-Chip Interconnect (ICI), delivering 121 exaflops of compute and two petabytes of shared high-bandwidth memory — three times the processing power of Ironwood and up to double its performance per watt. For the first time, a single Google pod can hold a model entirely in shared memory during training, eliminating the inter-node communication overhead that has traditionally bottlenecked large-model development.

The **TPU 8i** is built for inference at agent scale. Using a new "Boardfly" topology, it directly connects 1,152 chips in a single pod, features three times more on-chip SRAM than its predecessor — large enough to cache KV stores entirely on-silicon without touching HBM — and integrates a dedicated Collectives Acceleration Engine. The result: 80% better performance per dollar for inference workloads compared to the prior generation, and the latency profile needed to run millions of concurrent AI agents cost-effectively.

"A thing of beauty," said Amin Vadhat, Google's SVP of AI and Infrastructure, describing the 8th-gen architecture on stage.

Both chips were co-designed with Google DeepMind and are expected to enter customer availability in late 2026 through the AI Hypercomputer reservation program.

## The Gemini Enterprise Agent Platform

On the software side, Google consolidated Vertex AI and Agentspace into a single product: the **Gemini Enterprise Agent Platform**. The rebranding is more than cosmetic. The unified platform covers the full lifecycle of enterprise agents across four capability pillars: build, scale, govern, and optimize.

The **Build** layer introduces Agent Studio — a low-code, visual interface for non-engineers — alongside the Agent Development Kit (ADK), a code-first environment with AI-native coding tools. The **Scale** layer features a re-engineered Agent Runtime capable of maintaining agent state for days, paired with a persistent Memory Bank for long-term context storage across sessions.

The **Govern** layer addresses the enterprise's deepest anxiety about agents: control. Agent Identity, Agent Registry, and Agent Gateway together form a centralized governance fabric — letting IT teams know exactly which agents are running, what they have access to, and what they did. The **Optimize** layer then closes the loop with Agent Simulation for pre-deployment testing, Agent Evaluation for benchmarking, and Agent Observability providing full execution traces and real-time reasoning visibility.

### The A2A Protocol Expansion

One of the conference's most technically significant announcements was the expansion of Google's **Agent-to-Agent (A2A) protocol**, now enabling Gemini-native agents to communicate with third-party agents from ServiceNow, Salesforce, Atlassian, SAP, and other enterprise vendors — without custom integration code. For enterprises already running fragmented agent ecosystems, A2A could become the lingua franca of multi-agent orchestration, letting products from competing vendors collaborate on shared tasks.

## Workspace Goes Agentic

The Workspace announcements targeted the more than 300 million business users who live in Google Docs, Gmail, and Drive daily. **Ask Gemini in Google Chat** can now synthesize information across an organization's entire data estate, surface insights, and deliver proactive daily briefings. **AI Inbox and AI Overviews in Gmail** function as a personal assistant that triages messages and drafts responses. **Google Drive Projects** instantly organizes files and emails around workflow needs.

Google also introduced **Workspace Intelligence** — a semantic layer that learns an organization's voice, style, and brand, then applies it automatically to content creation tasks. The company added Microsoft 365 interoperability through Canvas, letting Workspace users export documents to Office formats natively, a direct acknowledgment of where much of its enterprise competition still lives.

## Security: Wiz Integration and the AI-BOM

Google's $32 billion acquisition of cloud security firm Wiz closed earlier in 2026, and Next showcased the first fully integrated product outcomes. The highlight is the **AI Bill of Materials (AI-BOM)** — an automatic inventory of every AI framework, model, and IDE extension deployed inside an organization's environment. As enterprises accelerate AI adoption through "vibe coding" and third-party agent procurement, the attack surface is ballooning; AI-BOM provides a mechanism to track what's actually running.

Google Security Operations also previewed three new agentic defenders in preview: a **Threat Hunting agent** that proactively searches for novel attack patterns, a **Detection Engineering agent** that identifies coverage gaps and writes new detection rules, and a **Third-Party Context agent** that enriches security workflows with external intelligence. These are tasks that have historically required senior security engineers working for hours.

The Agentic Data Cloud received its own announcements as well: a **Knowledge Catalog** serving as a unified, dynamic context graph of entire business data; a **Lightning Engine for Apache Spark** delivering up to 4.5x faster performance than open-source alternatives and 2x better price-performance against leading competitors; and a **Cross-Cloud Lakehouse** built on Apache Iceberg that lets enterprises query data stored in AWS or Azure without copying it.

## Google's Full-Stack Argument

CEO Thomas Kurian framed all of these announcements around a single strategic thesis: Google is the only company that owns all four layers of the modern AI stack — custom silicon (TPUs), frontier models (Gemini), the cloud platform (now Gemini Enterprise Agent Platform), and enterprise distribution (Workspace's three billion users).

"Chips that are designed for models, models that are grounded in your data, agents and applications that are built with those models," Kurian said on stage, describing what he called the integrated bet against the market.

That bet is explicitly aimed at OpenAI and Anthropic as much as at Microsoft and AWS. By building the Gemini Enterprise Agent Platform as a direct competitor to Microsoft Copilot and OpenAI's enterprise offerings — while simultaneously providing Anthropic's models through its infrastructure — Google is playing a multi-layered competitive game that few companies have the asset base to attempt.

Alphabet CEO Sundar Pichai described AI agents replacing pilots across entire enterprises as the central challenge of 2026. "A big focus of ours is to always be customer zero for our own technologies," he told attendees, in a nod to Google's internal deployment of the same agent infrastructure it is selling externally.

## What Comes Next

The 8th-generation TPUs enter customer availability in late 2026 through the AI Hypercomputer reservation program. The Gemini Enterprise Agent Platform is available now, replacing prior access paths through Vertex AI and Agentspace. The A2A protocol expansions with enterprise SaaS partners are rolling out through Q2 2026.

Whether Google's full-stack approach can translate into durable enterprise revenue — against Microsoft's dominant installed base and OpenAI's brand gravity in the developer community — will likely define the company's cloud business for the next several years. Cloud Next 2026 was the clearest articulation yet of how Google intends to try.
