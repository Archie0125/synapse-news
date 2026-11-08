---
category: developer-tools
faqs:
- answer: The agent polls test results every 15 minutes and decides whether each failure
    is a new bug, a duplicate or a regression. It then files a structured JIRA ticket
    with screenshots and repro rates and notifies the right people.
  question: What does this autonomous QA agent do?
- answer: For one team, the workload is small and periodic. An EventBridge-triggered
    Lambda with DynamoDB requires no infrastructure to operate and costs under $5
    a month.
  question: Why was Lambda the right choice at first?
- answer: Containers become the better fit when serving 10 to 100 teams changes the
    workload, for example through longer-running jobs, higher concurrency or shared
    state. The move is about fit, not Lambda failing.
  question: When should the agent move to containers?
featured: false
lang: en
publishedAt: '2026-11-08T16:30:00+00:00'
relatedSlugs: []
sources:
- name: The New Stack
  url: https://thenewstack.io/scaling-autonomous-agents-framework/
summary: 'A $5-a-month Lambda bug-filing agent shows the right way to scale: start
  serverless, and move to containers only when the workload actually changes.'
tags:
- developer-tools
- ai-ml
title: 'Scaling an autonomous agent from one team to fifty: A serverless-to-container
  decision framework'
trending: false
type: news
---

# Scaling an autonomous agent from one team to fifty: A serverless-to-container decision framework

**QA teams shipping complex products generate test failures around the clock.** Every failure needs a bug ticket with steps, screenshots, repro rates, and regression labels. The manual process takes 10-15 minutes per failure. Multiply that by 30+ failures per week across a team, and you have burned an entire engineering day on documentation that should be automatic.

I built a system to eliminate this entirely. Not a dashboard. Not a notification bot. [An autonomous agent](https://thenewstack.io/ai-agents-are-finally-starting-to-revolutionize-the-software-development-lifecycle/) that observes test results, makes judgment calls – is this a new bug, a duplicate, or a regression? And takes action without human intervention. It files structured bugs, attaches screenshots, calculates repro rates, detects regressions build-over-build, and notifies the right people. The team just marks FAIL and moves on.

The system runs on Lambda today. It works perfectly for one team. But what happens when other teams want it? What happens when you need to serve 10, 50, or 100 teams? That’s where the architectural decisions get interesting – not because Lambda fails, but because the workload characteristics shift into territory where a different tool becomes the better fit.

## What I built (and why it works)

The architecture is elegant: an EventBridge rule triggers a Lambda function every 15 minutes. The function polls the test management API, processes failures through a decision engine (dedup check against DynamoDB, regression detection against previous build results), and files bugs via the JIRA API. Total infrastructure cost: under $5/month.

[Lambda was the](https://thenewstack.io/mastering-aws-lambda-optimize-cost-and-performance/) correct choice here for three reasons:

1. **Zero operational overhead:** No servers, no scaling config, no patching. Deploy and forget.
2. **Cost proportional to usage:** One team generates \~200 invocations/month. At Lambda pricing, this is effectively free.
3. **Fast iteration:** The decision engine went through 20+ revisions in the first month. Lambda’s deployment model let me ship changes in seconds.

Within weeks of deploying, the system filed more complete and consistent bugs than the team had ever produced manually. Zero missed failures. Regressions caught in minutes instead of days. Status interruptions to QA dropped to zero because anyone could query the system directly via Slack. 8-10 hours per week saved.

Other teams have noticed. “Can we have that?” is a recurring question. The answer seems simple – deploy another instance per team. But at scale, the workload characteristics change in ways that shift the architectural decision.

## The scaling decision

Lambda handles single-tenant agentic workloads beautifully. The challenge at multi-tenant scale isn’t that Lambda can’t do it; it’s that the workload characteristics shift:

**From stateless events to long-running context:** A single team’s poll cycle finishes in seconds. But cross-project correlation – “is this the same failure pattern we’re seeing across three teams?” requires analyzing hundreds of results and their relationships in a single pass. That’s a fundamentally different compute profile.

**From isolated invocations to shared resource contention:** When 50 functions trigger on the same EventBridge schedule, they all hit TestRail and JIRA APIs simultaneously. You need centralized rate limiting, connection pooling, and backpressure – patterns that benefit from persistent, shared infrastructure.

**From single-team to multi-tenant isolation:** Each team needs guaranteed resources, network boundaries, and scoped credentials. The isolation model becomes as important as the compute model.

Lambda’s recent launches address many of these individually – Managed Instances solve connection persistence, Durable Functions break the 15-minute ceiling for long-running workflows, and Tenant Isolation provides native tenant boundaries. For many multi-tenant workloads, these capabilities narrow the gap significantly.

But for this specific workload – long-running agents that need persistent connections, cross-tenant analysis, GPU inference, and namespace-level isolation simultaneously- the decision framework points toward a container-native execution model with serverless-like operations. That’s where [EKS Auto Mode fits.](https://thenewstack.io/how-amazon-eks-auto-mode-simplifies-kubernetes-cluster-management-part-1/)

## The decision framework

This led me to build a simple decision rubric – not Lambda vs. containers, but which characteristics does your workload actually exhibit?

| **Workload characteristic** | **Lambda (+ Managed Instances, Durable Functions)** | **Auto Mode** | 
| Event-driven, short-lived | Optimal | Overengineered | 
| Single-tenant, low complexity | Optimal | Unnecessary | 
| Multi-tenant with isolation needs | Possible (Tenant Isolation) | Native (namespaces, RBAC, NetworkPolicies) | 
| Long-running with persistent state | Possible (Durable Functions) | Native (pods, persistent connections) | 
| Cross-tenant analysis requiring shared memory | Complex (custom orchestration) | Natural (shared services namespace) | 
| GPU-burst inference | Possible (Lambda GPU – if available) | Native (GPU NodePools, scale-to-zero) | 
| Centralized rate limiting + connection pooling | Custom build (SQS + Step Functions) | Shared platform service | 

“The deciding factor for my workload: I need all of the right-column characteristics simultaneously. Together, they compose more naturally in a container-native environment.”


**The deciding factor for my workload:** I need all of the right-column characteristics simultaneously. Cross-team pattern detection requires a shared analysis context. ML-based bug classification requires burst GPU. Per-team isolation requires namespace-level boundaries. Centralized rate limiting requires a persistent shared service. Each of these is individually solvable in Lambda. Together, they compose more naturally in a container-native environment.

## What unlocks at scale: cross-team intelligence

The most interesting architectural capability that emerges at multi-tenant scale isn’t per-team automation – it’s cross-team pattern detection. This is what makes the scaling exercise worthwhile.

## Cross-team failure correlation

When 50 teams run their test suites independently, failures appear isolated. But patterns emerge across teams that no single team can see:

- Three teams report navigation failures on the same firmware build → systemic regression, not three independent bugs
- Test failures correlate with deployment timing across unrelated services → infrastructure issue, not product bugs
- Identical error signatures across teams with different test suites → shared dependency failure

This requires an analysis engine that can hold context from all teams simultaneously – comparing fingerprints, correlating timestamps, and identifying shared root causes. That’s a persistent, long-running workload with access to cross-tenant state. It runs naturally as a shared service in a platform namespace, consuming events from all tenant agents.

## ML-based bug classification

Once you have enough historical data (thousands of bugs filed across teams), patterns become classifiable:

- Auto-assign bugs to the correct component owner based on failure signature
- Predict severity based on failure characteristics (crash vs. degraded behavior vs. cosmetic)
- Suggest related bugs for investigation (“this looks like the same root cause as PROJ-4521”)
- Detect anomalous failure rates before they become incident-scale

This inference workload is bursty – you need GPU when bugs arrive, not 24/7. A GPU NodePool that scales to zero when idle and provisions g5 instances only during inference keeps costs proportional to actual usage. The same pod that files a bug can synchronously call the classification service, get a component assignment, and include it in the ticket – all within the same request path.

## Queryable knowledge base via Slack

The agent isn’t just an automation – it becomes the organization’s queryable QA state. Via Slack, anyone can ask:

- “What’s the failure rate for navigation this week across all teams?”
- “Show me regressions introduced in build 2.4.1”
- “Which teams are seeing the most P0 bugs right now?”

This transforms the agent from a task automator into an intelligence layer. The answers require cross-team state aggregation, trend computation, and natural language interpretation – all served from persistent, indexed state that accumulates over time.

## What EKS Auto Mode brings to this architecture

EKS Auto Mode launched at re:Invent 2024 with a specific promise: full Kubernetes without managing nodes. For a multi-tenant agent platform, this means:

- **Nodes appear when pods need them.** Deploy a tenant namespace with an auto-filer pod. The Karpenter-based scheduler provisions a node within seconds. When the pod is deleted (tenant offboarded), the node is consolidated or terminated automatically. You never think about EC2 instances.
- **Security is not your configuration burden.** Nodes run immutable Bottlerocket AMIs – read-only root filesystem, SELinux enforcing, no SSH access. Nodes rotate every 21 days automatically. For long-running agent pods, this means a graceful drain roughly every three weeks. At most one missed poll cycle.
- **Scaling is reactive to demand.** During off-hours when agents are idle between polls, Auto Mode consolidates workloads onto fewer nodes. You pay for what you use.
- **GPU workloads slot in without architectural changes.** Define a GPU NodePool for the ML classification service. EKS Auto Mode provisions g5 instances only when inference pods are scheduled and terminates them when done.

## The multi-tenant architecture

At scale, the system would have three layers:

1. **Shared platform services:** a rate limiter that prevents any single tenant from exhausting external API quotas, a connection pool manager that maintains persistent sessions to TestRail and JIRA, and a Prometheus instance collecting metrics across all tenants.
2. **Per-tenant agent namespaces:** each team gets an isolated namespace containing their auto-filer pod, reporter pod, and Slack bot pod. ResourceQuotas guarantee resources. NetworkPolicies enforce that Team A’s pods cannot talk to Team B’s pods. Each namespace’s service account assumes a tenant-scoped IAM role via IRSA.
3. **Shared ML inference namespace:** GPU-enabled pods running classification models that all tenants can call. This namespace has its own NodePool that scales to zero when no inference is happening.

The agent code would remain essentially the same Python that runs on Lambda today – the core decision engine (observe, dedup, decide, act) doesn’t change. What changes is the execution model: instead of being invoked per-event and destroyed, the agent runs as a long-lived async loop with persistent connections, graceful shutdown handling, and internal scheduling.

## The AWS portfolio working together

The right framing isn’t “migrate off Lambda onto EKS.” It’s “use each service where it fits”:

- **Lambda** remains the entry point. New teams start here. Single-team automation at $5/month with zero ops. Event-driven triggers, rapid iteration, pay-per-invocation economics.
- **Lambda + Durable Functions** handles teams that need longer analysis windows or multi-step orchestration without leaving the serverless model.
- **EKS Auto Mode** serves the platform layer when you need persistent multi-tenant services, cross-team intelligence, GPU inference, and namespace-level isolation working together.
- **DynamoDB** persists state across all layers – dedup records, bug history, trend data.
- **EventBridge** orchestrates events whether the consumer is a Lambda function or a Kubernetes pod.

A team that needs 30-minute analysis windows or multi-step workflows (poll → correlate → file → notify → wait for response → update) benefits from Durable Functions without leaving serverless. You stay here until you need cross-tenant shared state or GPU – that’s the signal to evaluate Auto Mode.

“Lambda validates the pattern. EKS Auto Mode operationalizes it at scale. They’re stages in a journey, not competitors.”


The intelligence moves up the stack as the organization’s needs mature. Lambda validates the pattern. EKS Auto Mode operationalizes it at scale. They’re stages in a journey, not competitors.

## Key takeaways

- **Start serverless:** Lambda lets you validate the agentic pattern at zero operational cost. The $5/month price point removes all friction for proving the concept works. Don’t prematurely optimize for scale you don’t have.
- **Design for portability from day one:** Structure your Lambda function as a pure decision engine with external state. Containerizing it means wrapping it in an async loop and adding a health endpoint. If you build Lambda functions as self-contained decision engines rather than tightly coupled to the invocation model, the transition is a one-day exercise whenever you need it.
- **The decision trigger isn’t scale – it’s workload characteristics:** Don’t move because you hit 50 teams. Move when you need capabilities that benefit from persistent, shared infrastructure: cross-team correlation, centralized rate limiting, GPU inference, streaming connections.
- **Multi-tenancy is an isolation problem, not a compute problem:** Both Lambda (Tenant Isolation) and Kubernetes (namespaces) solve this. Choose based on what other characteristics your workload needs alongside isolation.
- **EKS Auto Mode closes the operational gap:** Before Auto Mode, choosing EKS meant accepting node management overhead. Auto Mode removes that tradeoff. You get container-native execution with serverless-like operations.

## The cost math

Single team on Lambda today: $3-5/month. 8-10 hours/week saved. 67x ROI. Fifty teams on EKS Auto Mode would cost approximately $200-250/month total – roughly $4-5 per team per month. Same per-team economics as Lambda, but with namespace isolation, persistent connections, GPU-ready infrastructure, centralized observability, and built-in organizational governance.

The cost-per-team barely changes. What changes is what you get for it!

## What comes next?

The agentic pattern – ‘observe, decide, act’ is infrastructure-agnostic. The decision logic doesn’t care about its deployment target. What changes is what becomes possible when agents stop operating in isolation.

“The next frontier isn’t single agents doing single tasks faster. It’s agents coordinating with other agents.”


The next frontier isn’t single agents doing single tasks faster. It’s agents coordinating with other agents. An auto-filer agent detects a failure pattern and hands context to a root-cause agent, which traces the dependency chain across services, identifies the offending commit, and drafts a fix recommendation – all before a human sees the bug ticket. Agent-to-agent delegation, where one agent’s output becomes another’s input without human routing in between.

Beyond that: agents that build their own decision models. Today, I hand-code the dedup logic and regression detection rules. Tomorrow, the agent observes which of its filed bugs humans close as duplicates, learns from those corrections, and tightens its own classification boundaries. The system improves not because I ship better code, but because it accumulates organizational judgment over time.

The system started as a weekend project to stop filing bugs manually. It now runs in production, eliminating an entire category of manual work from QA operations.

The infrastructure question stays the same – serverless for validation, containers for scale. But the agents running on that infrastructure are about to get significantly more capable. Teams with the platform layer ready will be the ones that can adopt those capabilities without rearchitecting.

			
				[YOUTUBE.COM/THENEWSTACK
			
			
				Tech moves fast, don't miss an episode. Subscribe to our YouTube 
				channel to stream all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)

## Summary

**TLDR:** A $5-a-month Lambda bug-filing agent shows the right way to scale: start serverless, and move to containers only when the workload actually changes.

- Filing a bug ticket for each QA failure takes 10–15 minutes by hand. At 30 or more failures a week, that adds up to about a full engineering day.
- The author built an autonomous agent that decides whether a failure is a new bug, a duplicate or a regression, then files it in JIRA with screenshots and repro rates.
- The system uses an EventBridge rule that triggers Lambda every 15 minutes, with DynamoDB for deduplication. It costs under $5 a month.
- The author argues Lambda is the right choice for one team. Moving to containers makes sense when serving 10–100 teams changes the workload, not because Lambda fails.
- The broader lesson is to choose infrastructure based on workload characteristics rather than trends.

## 摘要

**重點摘要：** 一個每月不到 5 美元的 Lambda 自動開單代理說明了正確的擴展方式：先用無伺服器架構，等工作負載真的改變了再換容器。

- 每筆 QA 測試失敗手動開單要花 10 到 15 分鐘，每週 30 筆以上，等於燒掉一整個工程日。
- 作者打造了一個自主 AI 代理，會判斷失敗是新 bug、重複問題還是回歸，再自動到 JIRA 開單，附上截圖和重現率。
- 系統用 EventBridge 規則每 15 分鐘觸發一次 Lambda，以 DynamoDB 做重複檢查，每月成本不到 5 美元。
- 作者認為一個團隊用 Lambda 正合適。改用容器的理由，是服務 10 到 100 個團隊時工作負載特性改變了，而不是 Lambda 撐不住。
- 更廣的啟示是：基礎設施要根據工作負載特性來選，而不是追潮流。