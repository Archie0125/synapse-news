---
category: developer-tools
faqs:
- answer: Kiro bots 是 AWS Kiro 開發環境中有名字、長時間運作的 AI agent，由開發者針對特定任務定義與客製。每個 bot 都有自己的長期記憶，可以接手委派的工作流程。
  question: Kiro bots 是什麼？
- answer: Kiro Crew 於 2026 年 8 月推出，是能跨 session 保留記憶的開源工作區。Kiro bots 更進一步，讓每個 agent
    都擁有自己獨立的記憶。
  question: Kiro bots 和 Kiro Crew 有什麼不同？
- answer: 開發者平行執行的複雜任務越來越多，逐步監督反而成為瓶頸。AWS 押注具備獨立記憶的專責 agent，能在較少人工介入下完成委派的工作。
  question: AWS 為什麼要讓開發者不再「盯場」agent？
featured: false
lang: zh
publishedAt: '2026-11-07T15:30:00+00:00'
relatedSlugs: []
sources:
- name: The New Stack
  url: https://thenewstack.io/kiro-bots-agent-memory/
summary: AWS 推出的 Kiro 機器人讓每個 AI 代理都擁有各自的持久記憶。AWS 押注未來開發者不再只和單一代理對話，而是改為管理一整支代理團隊。
tags:
- developer-tools
- ai-ml
- products
title: AWS 為何希望開發者別再當 AI 代理的保母
trending: false
type: news
---

Join our community of software engineering leaders and aspirational developers. Always
stay in-the-know by getting the most important news and exclusive content delivered
fresh to your inbox to learn more about at-scale software development.

REQUIRED

It seems that you've previously unsubscribed from our newsletter
in the past. Click the button below to open the re-subscribe form
in a new tab. When you're done, simply close that tab and continue
with this form to complete your subscription.

The New Stack does not sell your information or share it with
unaffiliated third parties. By continuing, you agree to our
Terms of Use and
Privacy Policy.

Welcome and thank you for joining The New Stack community!

Please answer a few simple questions to help us deliver the news and resources you are interested in.

REQUIRED

REQUIRED

REQUIRED

REQUIRED

REQUIRED

Great to meet you!

Tell us a bit about your job so we can cover the topics you find most relevant.

REQUIRED

REQUIRED

REQUIRED

REQUIRED

REQUIRED

Welcome!

We’re so glad you’re here. You can expect all the best TNS content to arrive
Monday through Friday to keep you on top of the news and at the top of your game.

What’s next?

Check your inbox for a confirmation email where you can adjust your preferences
and even join additional groups.

Follow TNS on your favorite social media networks.

AWS first introduced Kiro, its agentic, spec-driven development environment, in July 2025. It also introduced Kiro Crewin August of this year, its persistent, open-source development workspace that remembers context. Now, to help developers juggle more complex tasks executed in parallel, AWS introduced Kiro bots on Thursday, adding persistent agent memory and delegated workflow management to the toolset. Kiro Crew already carried memory across sessions; bots give each agent its own.

Described as a “named, long-running agent that you define and customize for a specific part of your work” (such as reading new issues in a ticket queue), Kiro bots retain their own memory and start with only the tools provided to them at creation.

The bot function also runs its own sessions (by which AWS means parallel worker sessions the bot launches and monitors), so software engineers don’t have to track them one by one or weave them together.

According to AWS, the arrival of Kiro bots heralds the shift from delegating tasks to delegating processes.

Babysitting vs. bots building better

AWS Agentic AI director of engineering Kathy Kam tells The New Stack that agents are only useful when developers can trust them to act on their own, but when a session ends, nobody owns the work anymore.

“Developers end up as the go-between, carrying context from one session to the next. Kiro bots take that job off their plate, so developers can now spend the day deciding what’s worth building instead of babysitting sessions,” Kam says.

“Developers can now spend the day deciding what’s worth building, instead of babysitting sessions.”

Up to now, if this babysitting to carefully shepherd agents from one point to the next with more durable memory isn’t there, then the negative consequences show up pretty fast.

“You get what a lot of developers now call context rot, which can make it feel like nagging an agent to redo what you told it yesterday,” Kam explains. “It spreads fast when parallel tasks each hold their own drifting version of reality. So we gave every Kiro bot its own durable memory, with a notes \[.md\] file it reads and writes, and that developers can edit directly. Fix a mistake once – and it stays fixed, instead of resurfacing across every task in flight.”

Each Kiro bot works with only the tools and permissions its job needs.

For example, a research bot can search the web and read files, but it can’t change them. A deployment bot can run deployment scripts and ask for approval before each change. A bot can ask developers for more tools, but nothing changes until the software engineer actually approves the request. Because each bot has its own memory, what the deployment bot learns about the release process does not mix with what the research bot learns. Separate lessons keep each bot aligned to its own responsibility, as judged by the developer at the outset.

Trust comes from track record

If this feels like bots and agents are developing more of their own personalities and being anthropomorphized into some sort of hierarchy, with some acting in a more senior capacity than others, then AWS’s Kam says that’s the wrong way to think about it.

“A hierarchy of agents based purely on IQ is the wrong measure. What matters is what an agent is allowed to touch, and a Kiro bot earns trust by building a track record,” underlines Kam.

“A hierarchy of agents based purely on IQ is the wrong measure. What matters is what an agent is allowed to touch, and a Kiro bot earns trust by building a track record.”

No anthropomorphization as yet, but still, each Kiro bot has a name, an avatar, its own memory, and one ongoing chat channel where developers set its direction and come back for results.

Behind that chat, the bot starts sessions in parallel and monitors them. It can redirect a session that drifts from the plan and combine the results when the sessions finish. If one task needs a human decision, the bot can ask the engineer while it keeps working on parts that don’t depend on an answer. Developers can set up routines in the chat, so a bot can investigate overnight build failures before the coding team even starts its day.

Yes, AWS, but what if…?

There still feels like a lot of yes, but what if… questions to surface here. What happens when bots are instructed to wait for human developer decisions, but the bot and wider agent framework already has enough institutional or historical knowledge to tell it the human doesn’t need to be involved? Doesn’t this mean the human coder should be overridden with an automation to reduce time-wasting?

“As more companies shift toward software factories, agents can end up remembering more information and context across a team than an individual developer, but that doesn’t put the agent in charge,” clarifies AWS’ Kam. “The human is still the one accountable, while the agent is responsible for executing the work. The software engineer sets how much access each Kiro bot gets for its job, so a deployment bot can require approval before every change while a research bot runs with fewer checkpoints.”

Kam further notes that a Kiro bot can “ask for more authority, but it can never take it” unmanaged. However, as already emphasized, while it waits for an answer, it keeps moving on everything that doesn’t need the human-in-the-loop.

Each Kiro bot understands its specialty, outcome, trade-offs, limits & decisions

In its official launch blog, AWS said developers using Kiro bots will find the direction given to the bot stays visible and revisable. It is set through ongoing conversation and feedback, and Kiro Crew’s learning builds within each bot. This lets the developer hand off an ongoing responsibility, not a single task. Each bot understands, for its specialty, the outcome it should aim for, the reason behind a trade-off, the limits around a change, and decisions already made.

One Kiro bot can own issue intake while another owns release readiness, and each follows the rules set for that work. AWS noted that taken together, each developer’s “crew of bots” supports the programmer’s unique approach to development and work requirements without flattening into one generic workflow.

“Bots can’t delegate work to other bots — and that’s by design to prevent context rot and ensure Kiro bots can remain independent.”

“Bots can’t delegate work to other bots — and that’s by design to prevent context rot and ensure Kiro bots can remain independent,” highlights Kam. “A Kiro bot splits big jobs across its own parallel workstreams and pulls the results into one recommendation. Developers stay the one defining each’s boundaries and connecting Kiro bots to each other, so no decision that you want to provide input on moves between them without you being involved.”

AWS also explained that over time, a developer’s bot crew “reflects how you actually develop”, because each bot carries the requirements and boundaries for its part of the work needed. The software engineer still decides how those processes change and where judgment belongs.

To get started, AWS has encouraged developers to open the bots workspace in the Kiro Crew sidebar, add a bot, and choose the default or a custom agent as its base. A custom agent supplies the prompt, model, tools, and skills, so users can build on a setup they already use without changing existing chats. In summary, with all the autonomy swirling around here, we might suggest that AWS isn’t asking developers to give up the steering wheel, but perhaps it’s asking them to sit further away from the passenger seat when AI is doing the driving.

## Summary

**TLDR:** AWS's Kiro bots give each agent its own persistent memory, and the bet is that developers will manage teams of agents rather than chat with one.

- AWS introduced Kiro bots, adding persistent per-agent memory and delegated workflow management to its Kiro toolset.
- Bots are named, long-running agents that developers define and customize for a specific job.
- Kiro launched in July 2025 as a spec-driven agentic development environment; Kiro Crew, an open-source persistent workspace, followed in August 2026.
- Kiro Crew already carried memory across sessions; bots extend that memory to each individual agent.
- The pitch is less supervision: developers delegate parallel tasks instead of babysitting each agent step by step.

## 摘要

**重點摘要：** AWS 的 Kiro bots 讓每個 agent 都有自己的長期記憶，押注的是開發者會管理一整組 agent，而不是只跟一個聊天。

- AWS 推出 Kiro bots，為 Kiro 工具組加入每個 agent 獨立的長期記憶與委派式工作流程管理。
- Bot 是有名字、長時間運作的 agent，由開發者針對特定任務定義與客製。
- Kiro 於 2025 年 7 月推出，主打規格驅動的 agent 開發環境；開源的持久化工作區 Kiro Crew 則在 2026 年 8 月登場。
- Kiro Crew 原本就能跨 session 保留記憶，bots 則把記憶延伸到每個 agent 身上。
- 主打賣點是少盯場：開發者把平行任務委派出去，不用一步步看著 agent 做事。