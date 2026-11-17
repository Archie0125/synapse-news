---
category: ai-ml
faqs:
- answer: QCon AI New York 2026 於 12 月 15–16 日舉行，聚焦在正式環境中運行 AI 系統。來自 LinkedIn、Netflix、DoorDash、Figma
    等公司的工程師將分享代理授權、評估流程、模型服務與 AI 輔助軟體交付的經驗。
  question: QCon AI New York 2026 的主題是什麼？
- answer: 身分與授權系統預設每組憑證背後都有一個人，角色穩定、工作階段有邊界，事後也能究責。AI 代理不具備這些特性，因此很難控制它能做什麼，出事時也難以釐清責任。
  question: 為什麼代理的身分問題特別受關注？
- answer: 議程集中在權限該在哪裡把關、離線評估能否預測正式環境表現等營運問題。這代表大型企業已走過初期導入，正在面對規模化後的治理、可靠性與成本挑戰。
  question: 議程透露出企業 AI 的什麼趨勢？
featured: false
lang: zh
publishedAt: '2026-11-11T11:00:00+00:00'
relatedSlugs: []
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/qcon-ai-newyork-2026-program/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: 從 QCon AI 的議程可以看出，業界關注的焦點已從「Agent 能不能上線？」轉向「Agent 出手後該由誰負責？」，而身分識別正是至今仍懸而未決的核心難題。
tags:
- ai-ml
- industry
title: LinkedIn、Netflix 與 DoorDash 如何在正式環境中運行 Agent、評測與推論：QCon AI New York 2026
trending: false
type: news
---

[QCon AI New York 2026](https://newyork.qcon.ai/?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26) has published its [full schedule](https://newyork.qcon.ai/schedule/newyork2026?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26) for December 15–16. Engineers from LinkedIn, Netflix, DoorDash, Figma, and other organizations will examine the architecture and operational decisions behind production AI systems, including agent authorization, evaluation pipelines, model serving, and AI-assisted software delivery. With the conference a few weeks away, there is still time to [join other practitioners](https://newyork.qcon.ai/registration/event/newyork2026?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26) before the full ticket price takes effect on December 9.

The program addresses questions facing teams moving beyond initial AI deployments: where to enforce agent permissions, how to connect offline evaluations to production behavior, and how to support growing inference workloads. It also examines how coding agents affect code review, engineering practices, and organizational adoption.

The following presentations explore these challenges through systems the speakers build and operate.

## Keynotes

Nancy Wang, CTO at 1Password, who founded and scaled AWS Data Protection and previously worked at Rubrik and Google, opens day one with [When Software Becomes a User: Identity and Authorization for Agents in Production](https://newyork.qcon.ai/keynote/newyork2026/when-software-becomes-user-identity-and-authorization-agents-production?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). She argues that identity systems assume a human behind every credential, with a stable role, a bounded session, and someone accountable afterward. Agents have none of these.

Tara Sainath, Distinguished Research Scientist at Google DeepMind, lead of the Gemini Audio area and modeling lead for Project Astra, opens day two with [Audio Processing with Large Language Models](https://newyork.qcon.ai/keynote/newyork2026/audio-processing-large-language-models?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). She covers how LLMs have changed audio processing, and the research and product impact of audio LLMs at Google.

## Agents in production

Pratik Agarwal, Distributed Systems Engineer on Figma's sandbox and caching platforms, [explains how Figma provisions and secures production agents](https://newyork.qcon.ai/presentation/newyork2026/beyond-sandbox-provisioning-and-securing-production-ai-agents-figma?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). Figma found that the trust boundary for agents extends beyond the sandbox. Warm pools cut provisioning latency by 90%, and availability rose from 99% to 99.95%.

Ronak Nathani, Principal Staff Software Engineer in Compute Infrastructure at LinkedIn and host of the Software Misadventures podcast, presents [LinkedIn's Kubernetes ops agent](https://newyork.qcon.ai/presentation/newyork2026/inside-linkedins-kubernetes-ops-agent-skills-tools-and-guardrails?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26), which works across 500,000+ nodes and 5M+ pods. Its guardrails sit on the server, including rate limits, delete protection, and peer approval for production changes.

## Evals that decide whether a change ships

Fabio Flores, Software Engineer at DoorDash who leads foundation development for its agentic ordering system, [explains the eval loop behind it](https://newyork.qcon.ai/presentation/newyork2026/signal-impact-eval-loop-behind-doordashs-agentic-ordering-system?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). Every change is checked before launch by an LLM judge calibrated against human reviewers. The same rubrics score simulated and real sessions, so offline gains carry into production.

Emrick Donadei, Software Engineer on the Google DeepMind infrastructure team who works on evaluation and safety for agentic harnesses, covers [agent evals the whole organization can write and keep running](https://newyork.qcon.ai/presentation/newyork2026/agent-evals-your-whole-org-can-write-and-keep-running?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). The talk starts from a common problem: an eval that passes once, then fails on the next run.

## Inference cost and model serving

Fan Yang, Staff Software Engineer building Netflix's AI serving platform, and Rajat Shah, Staff Software Engineer who leads the technical architecture for ML model serving, explain [how Netflix serves ML and GenAI from one platform](https://newyork.qcon.ai/presentation/newyork2026/one-infrastructure-every-model-how-netflix-scales-ml-genai?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). It handles about 1 million inference requests per second across 300+ models, after five years of consolidation. They cover what multi-tenancy costs to operate.

Salina Wu, Software Engineer building Pinterest's generative AI serving platform, and Cristian Lopez, Software Engineer on GenAI Serving at Pinterest, present [Pinterest's vision-language model serving stack on NVIDIA Dynamo](https://newyork.qcon.ai/presentation/newyork2026/building-pinterests-vlm-serving-stack-nvidia-dynamo?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). It is built for multimodal workloads with heavy prefill computation and large KV cache pressure.

## AI-assisted software engineering

Min Chen, Principal Staff Engineer at LinkedIn with more than 25 years of software development experience, presents [LinkedIn's AI code review system](https://newyork.qcon.ai/presentation/newyork2026/high-signal-ai-code-review-adapts-your-codebase-scale?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). It reviews tens of thousands of pull requests a week across about 10,000 repositories. More than 60% of sampled suggestions are accepted, and a validation pipeline filters findings before developers see them.

Joey Wang, engineering lead at Harvey who created Spectre, Harvey's internal collaborative cloud agent platform, explains how Harvey [shipped its agents internally first on Spectre](https://newyork.qcon.ai/presentation/newyork2026/be-your-toughest-customer-shipping-collaborative-agents-twice-our-own-org?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). Spectre passed 7,000 merged pull requests across every repository before the agents reached lawyers.

## Engineering leadership and adoption

Liz Fong-Jones, Technical Fellow at Honeycomb and site reliability engineer with more than two decades of experience, and Rebecca Murphey, Principal for AI Ops at Honeycomb and author of *Build: Elements of an Effective Software Organization*, [reflect on Honeycomb's 2x initiative](https://newyork.qcon.ai/presentation/newyork2026/reflections-2x-initiative-honeycomb?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). Peak weekday PR merges to Honeycomb's main monorepo rose from about 30 to about 74 between early 2025 and April 2026, and have held steady since.

Brian Yang, Member of Technical Staff at OpenAI who builds AI-native advertising and monetization systems, covers [making AI adoption work across an engineering team](https://newyork.qcon.ai/presentation/newyork2026/making-ai-adoption-work-across-engineering-team?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26). He looks at what happens after every engineer has coding agents, when one person finds a way of working that teammates struggle to reproduce.

## Also on the program

Other sessions come from engineers at *Anthropic, Microsoft, BlackRock, Databricks, Datadog, Tessl, LangChain, Baseten, and Google Cloud’s DORA team*. Topics include agentic standards, sandbox density, SRE agents, AgentOps for financial services, inference with vLLM, voice agents, software factories, and enterprise AI adoption. Explore the [full schedule](https://newyork.qcon.ai/schedule/newyork2026?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26).

Group registration for teams of three or more closes on November 27, 2026, with savings of $50 to $125 per ticket. Individual tickets are $1,790 until December 8, the last price before the full rate applies. Tickets can be transferred to a colleague free of charge until December 11, 2026.

Engineers who need approval can use the [Convince Your Manager page](https://newyork.qcon.ai/convince-your-manager?utm_source=infoq&utm_medium=referral&utm_campaign=newspost_nov11_qainy26), which provides an email template built around the sessions relevant to their work.

## Summary

**TLDR:** QCon AI's lineup shows the industry has moved from 'can we ship an agent?' to 'who is accountable when it acts?', and identity is the unsolved problem.

- QCon AI New York 2026 runs December 15-16, with engineers from LinkedIn, Netflix, DoorDash, Figma and others.
- Topics include agent authorization, linking offline evals to production behavior, scaling inference, and how coding agents change code review.
- 1Password CTO Nancy Wang's keynote argues identity systems assume a human with a stable role and accountability, and agents have none of these.
- The piece is partly promotional; full ticket pricing starts December 9.

## 摘要

**重點摘要：** QCon AI 的議程顯示產業焦點已從「能不能做出代理」轉向「代理出事誰負責」，而身分與授權是還沒解決的難題。

- QCon AI New York 2026 將於 12 月 15–16 日舉行，講者來自 LinkedIn、Netflix、DoorDash、Figma 等公司。
- 議題涵蓋代理授權、離線評估如何對應正式環境表現、推論規模擴充，以及程式碼代理如何改變 code review。
- 1Password 技術長 Nancy Wang 的主題演講指出，身分系統預設每組憑證背後有個角色穩定、可究責的人，而代理三者都沒有。
- 這篇文章帶有宣傳性質，12 月 9 日起恢復全額票價。