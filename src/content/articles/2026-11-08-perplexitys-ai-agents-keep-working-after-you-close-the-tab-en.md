---
category: ai-ml
faqs:
- answer: Teammates is a Perplexity feature that coordinates multiple AI agents. The
    agents remember where earlier sessions left off and keep working without another
    prompt, even after the user closes the tab.
  question: What are Perplexity Teammates?
- answer: When several agents run at the same time, they share project state and may
    have different permissions. Without careful coordination, they can conflict, duplicate
    work or act on stale information.
  question: Why is keeping agents in sync hard?
- answer: Users should watch how reliably the agents coordinate, how permissions are
    enforced, and how much visibility users get into what the agents do while they
    are away.
  question: What should users watch as Teammates rolls out?
featured: false
lang: en
publishedAt: '2026-11-08T15:30:00+00:00'
relatedSlugs: []
sources:
- name: The New Stack
  url: https://thenewstack.io/perplexity-teammates-agent-orchestration/
summary: Perplexity's Teammates agents keep working after you close the tab. The hard
  part isn't autonomy but keeping multiple agents in sync on state and permissions.
tags:
- ai-ml
- products
title: Perplexity’s AI agents keep working after you close the tab
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

Perplexity’s AI agents keep working after you close the tab

Perplexity’s Teammates coordinate multiple AI agents that remember past sessions and keep working unprompted. The real challenge is keeping them in sync.

Perplexity’s new Teammates can coordinate multiple agents, remember where previous sessions left off, and keep working without another prompt. The challenge is keeping everything in sync, especially when agents are working at the same time, sharing project state, and operating with different permissions.

Announced Wednesday, Teammates builds on infrastructure Perplexity has spent much of the year developing. The launch puts that earlier work to use in workflows where agents can delegate tasks and continue operating across sessions.

The challenge of keeping agents stateful

When Nate Kupp, Perplexity’s vice president of infrastructure, took The New Stackinside the company’s agent sandboxes, he described the difficulty of maintaining reliable systems at that scale.

“Stateful systems are incredibly hard to build,” Kupp said, pointing to the durability and uptime requirements of operating millions of sandboxes.

“Stateful systems are incredibly hard to build”

Teammates relies on Perplexity Computer’s existing infrastructure, which separates persistent project state from individual execution environments. That allows agents to continue working on the same project without depending on a single uninterrupted session.

Shared state lives in Git

In a technical breakdown of its shared workspaces, the company described how it uses Git-backed repositories to keep project state intact across sessions. Each Computer project has its own repository, while agents work in separate sandboxes and submit their changes back to the shared project.

That gets more complicated when agents are working on the same code at once since if one agent commits its changes first, another may have to reapply its work against the latest version.

Perplexity says fewer than 2% of submissions are rejected because they’re based on outdated repository state. Median submission latency is under 1.7 seconds, while p99 stays below eight seconds.

Median submission latency is under 1.7 seconds, while p99 stays below eight seconds.

Memory is handled separately through Perplexity’s Brain system, which keeps what agents have learned in dedicated repositories. That lets background agents update shared knowledge without interfering with changes to the project’s files.

Pausing and forking agents

Perplexity built SPACE around Firecracker microVMs and Btrfs snapshots, making it possible to pause, resume, or fork agent sessions without losing their saved state.

With Teammates, developers can connect tools like Slack and GitHub and set up triggers that tell agents when to act. Perplexity hasn’t said much about what happens when that work gets stuck, particularly when one agent is waiting on another or acting on information that’s already out of date.

The open permission questions

Each teammate runs in its own isolated environment and browser session, with access managed through Computer’s existing permissions and credentials handled securely through encryption. Users can also monitor progress and take control when needed.

It’s unclear how it prevents agents from accessing resources beyond their permissions when tasks are handed off. For enterprises, that uncertainty could influence how much autonomy they’re willing to give agents without requiring human approval.

Teammates is initially available on the web for Perplexity Max subscribers, with iOS support planned.

Teammates is initially available on the web for Perplexity Max subscribers, with iOS support planned.

## Summary

**TLDR:** Perplexity's Teammates agents keep working after you close the tab. The hard part isn't autonomy but keeping multiple agents in sync on state and permissions.

- Perplexity announced Teammates, which coordinates multiple AI agents that remember earlier sessions and keep working without new prompts.
- The agents keep running after the user closes the browser tab, moving Perplexity from answering questions toward doing ongoing work.
- The main engineering challenge is keeping agents in sync when they run at the same time, share project state and have different permissions.
- The launch puts Perplexity in the race for persistent, multi-agent products, where reliability and governance matter more than how capable a single model is.

## 摘要

**重點摘要：** Perplexity 的 Teammates 代理在你關掉分頁後仍會繼續工作。難的不是讓它們自主，而是讓多個代理在專案狀態和權限上保持同步。

- Perplexity 推出 Teammates，可以協調多個 AI 代理，記住先前工作階段的進度，不需新指令就能繼續工作。
- 使用者關掉瀏覽器分頁後代理仍會運作，讓 Perplexity 從回答問題走向持續執行任務。
- 最大的工程挑戰是同步：多個代理同時運作、共用專案狀態，而且權限各不相同。
- 這次發表讓 Perplexity 加入常駐型多代理產品的競爭，在這個領域，可靠性和治理比單一模型多強更重要。