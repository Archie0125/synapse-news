---
category: developer-tools
faqs:
- answer: Technical debt can be rational when releasing imperfect software produces
    valuable customer, operational, or business feedback. The choice remains sound
    only if the learning is later incorporated into the system.
  question: When can taking on technical debt be a rational choice?
- answer: The cost of debt depends on whether a team retains context, communicates
    new knowledge, and agrees to revise earlier decisions. Clean-looking code can
    still carry serious debt when nobody understands its assumptions or ownership.
  question: Why is technical debt described as social rather than purely technical?
- answer: AI can increase code output faster than teams can review, understand, and
    maintain it. That gap can multiply undocumented assumptions and make future changes
    more expensive even when the generated code initially works.
  question: How does AI-assisted coding change the risk?
featured: false
lang: en
publishedAt: '2026-11-12T11:05:00+00:00'
relatedSlugs: []
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/tech-debt-learning-doing/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: Technical debt is healthy when it buys learning, but AI makes repayment harder
  by producing code faster than teams can absorb context.
tags:
- developer-tools
- ai-ml
- industry
title: Technical Debt is Social; it is the Price of Learning by Doing
trending: false
type: news
---

Technical debt is not necessarily a sign of poor engineering. It can be the price of learning through software in use. As AI accelerates code production beyond our capacity to understand code and context, technical debt increasingly becomes a sociotechnical challenge, Xin Yao noted in her talk "What If Your Biggest Technical Debt Is Social", at [GOTO Copenhagen](https://gotocph.com/).

Yao quoted Ward Cunningham, who defined debt as "not-quite-right code". Debt sounds like a negative thing, but it can be a deliberate business strategy, she explained:

If we release the code now, well knowing it’s not perfect for the future yet, we’ll get some business feedback, we’ll get some user feedback, we’ll probably get paid for something, and that’s good as a business strategy.


Debt isn’t about poorly written code; it arises when we design software with incomplete knowledge. Hence, debt is the price of learning by doing, Yao argued. Releasing software allows us to test our assumptions against reality. Once we’ve got a learning experience, we have to put that experience back into our code and pay off the debt, she added. The debt becomes problematic when our software doesn’t catch up with our new learning.

Debt can be a good communication strategy toward management. It provides an economic argument for the cost of postponing architectural improvements. However, framing technical debt solely as something to eliminate misses its strategic value. The question is not whether to incur debt, but whether the learning it enables justifies the cost, and whether we actually repay it.

Yao referred to Kent Beck’s article ["Earn and Learn](https://newsletter.kentbeck.com/p/earn-and-learn)," which explores features vs. futures. Features deliver value today, while the future is actually the optionality to adapt those features, Yao explained:

Every bit of code already coded is complexity and a constraint. Every feature removes some future. If you go on producing features, maybe using your LLMs, then at a certain point, all you can do is use your capacity to pay the interest, to fix the code, and you can no longer release features.


The challenge is to balance delivering features with preserving future options, Yao said. Sometimes, delaying a design commitment preserves options until we know more, and this includes postponing some upfront architecture decisions to the last responsible moment as well. As Beck argues, waiting is not laziness; waiting is holding an asset.

Technical debt can therefore be understood as learning made visible in software. We design based on what we know, observe software’s impact, modularity, and its architecture’s implications, and we update our understanding, Yao explained:

The software no longer fits what we now understand, and yesterday’s good understanding becomes today’s debt.


AI introduces a new challenge: software can now be produced faster than teams can develop a shared understanding of its behavior, design decisions and consequences, Yao argued.

Agentic coding makes debt repayment more complex; beyond addressing poorly written AI-generated code, teams must close the gap between what the software actually does and what they understand it to do, while ensuring the code keeps pace with their evolving domain and architectural understanding. Paying off debt is no longer just a technical task, but a sociotechnical one, Yao concluded.

InfoQ interviewed [Xin Yao](https://www.linkedin.com/in/xinxin/) after her talk.

**InfoQ: What does learning from technical debt look like, and what benefit does it bring?**

**Xin Yao**: We design and release software based on our best current understanding, then test our assumptions against business and user reality. Paying off debt means incorporating that learning back into the software and closing the gap between what we knew when we released the first iteration and what we know now.

Each iteration creates new debt and new learning. Small batches and tight feedback loops help teams retain the memory of their initial design decisions and continuously repay the old debt with new learning.


**InfoQ: What does technical debt look like now that developers are using artificial intelligence?**

**Yao**: With agentic coding, software production can outpace human understanding. Code increasingly becomes a fossil record of agents’ decisions, while humans remain accountable for its consequences. Local productivity gains can create collective costs: more code, weaker ownership and growing gaps in shared understanding.

A study on [How Developers Discuss the Burden of AI-Assisted Software Development](https://arxiv.org/abs/2603.27249) describes this as "a tragedy of the commons". The danger is not merely more poorly written agentic code, but accelerated learning debt across the sociotechnical system.

## Summary

**TLDR:** Technical debt is healthy when it buys learning, but AI makes repayment harder by producing code faster than teams can absorb context.

- Xin Yao argues that technical debt often results from designing software with incomplete knowledge, not from careless engineering.
- Shipping imperfect software can be rational when real customer and business feedback is more valuable than speculative future-proofing.
- Debt becomes harmful when new learning is not incorporated back into the code, architecture, and team’s shared understanding.
- The debt metaphor gives engineers an economic language for explaining why postponed architectural work accumulates costs.
- AI raises the stakes because code can now be generated faster than organizations can review it or preserve the context behind it.

## 摘要

**重點摘要：** 技術債若能換來真實學習並不可怕；真正危險的是人工智慧產碼太快，團隊還沒搞懂就已失去償還能力。

- Xin Yao 認為，技術債常源自資訊不足下的設計選擇，不必然代表工程品質差。
- 先交付不完美的軟體，有時能更快取得客戶回饋、收入與市場證據，比憑空預測未來更合理。
- 真正的問題出現在團隊已學到新知，卻沒有把它寫回程式碼、架構與共同認知。
- 「債務」這個說法能把延後改善的代價轉成管理層較容易討論的經濟問題。
- 人工智慧加速產碼後，組織理解系統與傳承脈絡的速度若跟不上，技術債就會迅速變成社會性債務。