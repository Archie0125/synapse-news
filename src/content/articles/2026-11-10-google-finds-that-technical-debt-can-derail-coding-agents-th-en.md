---
category: ai-ml
faqs:
- answer: Agent distraction is Google's term for AI coding agents being derailed by
    stale context such as old TODO comments, obsolete bug references and outdated
    specs. It leads them into work the user never requested.
  question: What is agent distraction?
- answer: In Google's traces, about 13% of agent sessions encountered inline TODO/FIXME
    references, and agents acted on the referenced bug in 6% of those cases. Of these
    detours, 41% targeted already-closed bugs and 57% targeted open but out-of-scope
    bugs.
  question: How often does it happen?
- answer: Teams should treat stale TODOs, closed bug references and outdated docs
    as agent-facing risks. Google's approach of cross-referencing TODOs against bug
    status and the user's prompt shows that this kind of noise can be detected automatically
    at scale.
  question: What should engineering teams do about it?
featured: false
lang: en
publishedAt: '2026-11-10T18:00:00+00:00'
relatedSlugs: []
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/google-agent-distraction/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: Google's data shows stale TODO comments have become instructions for AI agents,
  which means technical debt now actively misleads the code's newest readers.
tags:
- ai-ml
- developer-tools
title: Google Finds that Technical Debt Can Derail Coding Agents Through "Agent Distraction"
trending: false
type: news
---

In a recent article, Google senior staff software engineer Sam Saccone and senior staff data scientist Madhuri Garikapati highlighted the cost of *agent distraction*, where [AI coding agents get derailed by stale technical debt](https://developers.googleblog.com/agent-distraction/), such as old `TODO` comments, obsolete bug references, and outdated specs, leading them to embark on unrequested "side-quests".

Obsolete specs, long resolved bugs, and lagging documentation no longer rest in long forgotten corners of the codebase, but rather are unintentionally ingested as context indirecting and misdirecting the next wave of coders - the agents.


According to the authors, at best, agent distraction increases token consumption and execution time; at worst, it can lead agents to "incorrect logic and decisions". To investigate this impact, they focused on `TODO(bug/...)` comments, which, as they note, "tend to be left behind long after the underlying bug is resolved or abandoned".

By cross-referencing every TODO an agent encounters against the TODO's bug status and the user's prompt, we can automatically separate valid work from wasted detours at scale.


Using distributed traces from thousands of engineers and hundreds of millions of agent steps, Google found that approximately 13% of sessions exposed agents to inline `TODO/FIXME` references, leading agents to take action targeting the reference bug in 6% of those cases. In most cases, the prompt did not even mention the referenced bug. Furthermore, in 41% of these unprompted detours, the agent worked on tickets that were already closed; in 57% of them they worked on bugs that were still open, but fell outside the scope of the developer's request, which the investigators classified as "scope creep".

Using a multi-way fixed-effects regression with developer-clustered standard errors, the investigators found that these detours add substantial overhead per session, with 70% more steps, 77% more tokens, and 105% more wait time.

To address this issue, Google developed scanner agents to identify and clean up obsolete TODOs across the codebase. In some cases, the agents had to inspect years of git history to be able to confirm that both the `TODO` and the intent behind it were obsolete. However, only once confirmed this, they submitted a PR to remove the outdated reference from the codebase.

As a result of this multi-layer approach, our todo cleaner has been able to remove thousands of actually obsolete references over the last 6 months exceeding 95% acceptance from human reviewers.


The investigators conclude that tools such as presubmit analyzers, codebase scanners, and automated agents can help mitigate "agent distraction" and thus improve the effectiveness of AI coding agents.

Commenting on the finding, X user Tulasiram noted that "[this is a useful reminder that comments are context too](https://x.com/p_tulasiram/status/2119382913007702046?a=QmVCaTZT7d2z6NXDdts&s=20)". [Ryan White emphasized](https://x.com/AdDadRyanW/status/2119329946065637758?a=T4Rwm595sybw4v5_NKI&s=20):

This is just junior dev behavior at machine speed. Leave a misleading comment and someone chases it for a day. Except now it happens 40 times an hour and you're paying for the tokens.


On LinkedId, user Awais Raza [expressed optimism about the potential to mitigate agent distraction](https://lnkd.in/p/eE7rMGbx):

The 95%+ human acceptance of the todo cleaner is telling: it shows cleanup can be automated without losing human judgment.


Finally, [Muhammad Zohaib extended this perspective](https://lnkd.in/p/e2s2TU8m), pointing out that "the same probably applies to websites: outdated pages and conflicting info make it harder for AI systems to pick the right answer."

## Summary

**TLDR:** Google's data shows stale TODO comments have become instructions for AI agents, which means technical debt now actively misleads the code's newest readers.

- Google engineers call the problem agent distraction: coding agents read stale TODOs, obsolete bug references and outdated specs, then go on side-quests nobody asked for.
- Across hundreds of millions of agent steps, about 13% of sessions exposed agents to inline TODO/FIXME references, and agents acted on the referenced bug in 6% of those cases.
- In 41% of these unprompted detours, agents worked on bugs that were already closed. Another 57% targeted open bugs outside the request, which the researchers classified as scope creep.
- At minimum, the detours waste tokens and time. At worst, they lead agents into incorrect logic and decisions.
- For teams adopting agents, code hygiene is now an operating cost, not just a matter of taste.

## 摘要

**重點摘要：** Google 的數據顯示，過時的 TODO 註解已經變成 AI 代理會照做的指令。技術債不再只是放著不管，而是會主動誤導程式碼最新的讀者。

- Google 工程師將這個現象命名為「代理分心」：程式碼代理讀到過時的 TODO、早已失效的 bug 編號和舊規格，就自行跑去做沒人要求的支線任務。
- 在數億個代理步驟中，約 13% 的工作階段接觸到行內 TODO/FIXME，其中 6% 的情況下代理真的去處理了那個 bug。
- 這些未經要求的偏離中，41% 處理的是早已關閉的 bug；57% 則是仍未關閉、卻超出使用者需求範圍的 bug，研究者將其歸類為範疇蔓延。
- 最好的情況是浪費 token 和執行時間，最糟的情況是讓代理寫出錯誤的邏輯和決策。
- 對導入 AI 代理的團隊來說，程式碼整潔度已經是實實在在的營運成本，而不只是工程美學。