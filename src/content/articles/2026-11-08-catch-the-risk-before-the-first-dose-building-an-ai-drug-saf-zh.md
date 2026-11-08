---
category: ai-ml
faqs:
- answer: TrialSleuth AI 是一個 AI 代理，會在新藥首次人體試驗前審查藥物，並比對過往的藥物結果紀錄。它會輸出整體風險等級、各器官系統的風險與依據、試驗方案的修改建議和建議檢測。
  question: TrialSleuth AI 是做什麼的？
- answer: 作者認為，很多早期試驗的傷害其實可以預見。同類藥物的肝毒性、藥物交互作用等知識早就存在，只是散落在舊報告、論文和人的記憶裡。
  question: 作者為什麼認為需要這種工具？
- answer: 這套工具會明確列出自身記憶無法回答的部分，而且它是開發者專案，不是經過驗證的法規系統。它有多大用處，取決於所記得的歷史數據品質和涵蓋範圍。
  question: 這種做法有什麼限制？
featured: false
lang: zh
publishedAt: '2026-11-08T05:53:55+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/sohapatel26/catch-the-risk-before-the-first-dose-building-an-ai-drug-safety-reviewer-that-remembers-npo
summary: 過往臨床試驗的經驗教訓分散各處，TrialSleuth AI 正是瞄準這個真實存在的缺口；但 AI 藥物安全審查員是否值得信賴，終究取決於它能實際拿出多少證據。
tags:
- ai-ml
- developer-tools
title: 在第一劑投藥前揪出風險：打造具備記憶力的 AI 藥物安全審查員
trending: false
type: news
---

💡 **In one line:** I built **TrialSleuth AI**, an agent that reviews a new drug *before* its first human trial and remembers every past drug result, so it gets smarter with each one.


Every new medicine eventually reaches a day when it is given to a human for the first time. By then it has passed lab tests and animal studies. Yet people in early trials still sometimes get hurt.

When you read about those cases afterwards, many of them look **predictable**:

| What went wrong | Was it known before? | 
|---|---|
| A similar molecule damaged the liver | ✅ Yes, in an earlier drug of the same class | 
| A chemical feature affected heart rhythm | ✅ Yes, a well-known warning sign | 
| A common medicine pushed drug levels 2.5× higher | ✅ Yes, seen in a past trial | 
| Six volunteers were dosed on the same morning | ✅ Yes, a lesson learned the hard way | 

The knowledge existed. It was just **scattered** across old reports, papers and people's memories.

So I asked myself: *what if a tool could remember every past drug result and check each new drug against all of it before anyone takes the first dose?*

A pharma team describes their drug the way they would in a planning meeting:

- 🧬 **What it is:** composition and chemical features
- 💊 **How much:** the dose and how it goes up
- 👥 **Who gets it:** which patients are allowed in
- 🗓️ **How:** the trial design
- 🔗 **With what:** which other medicines are allowed
- 🔬 **What we know:** lab results so far

TrialSleuth then gives back a clear review:

1. **An overall risk level** (High, Medium or Low)
2. **Risks by body system** (liver, heart, kidneys…), each with the evidence it used
3. **Suggested changes:** lower the starting dose, exclude a patient group, ban an interacting medicine, dose one person first
4. **Tests to run** before anyone is dosed
5. **Limits of the review:** what memory can't tell us

## 👉 Click to see a sample TrialSleuth report

**Risk level:** High - changes needed before human dosing

System 
Risk 
Why (IDs) 
Liver 
2–3× higher exposure in Child-Pugh B patients; interaction with strong CYP3A4 inhibitors 
HB-02, HB-03, PC-101, PC-102 
Heart 
Possible hERG block and QT prolongation (aniline + basic amine core) 
PC-702, HB-05 
Whole group 
Six people dosed on the same morning 
PC-801 
**Suggested changes**
Exclude Child-Pugh B patients until liver data exists (HB-02)
Ban strong CYP3A4 inhibitors with a 14-day washout (PC-102)
Dose one sentinel participant first and wait before the rest (PC-801)
Run a hERG assay and add ECG monitoring (PC-702)

*This is an example of the report format. It flags known risks; it never declares a drug safe.*


⚠️ **The rule I never broke:** TrialSleuth never says a drug is "safe" or "will work". No software can promise that. Its job is to make sure *known* risks are designed out before human dosing, so experts start from a better plan.


A normal AI chatbot only knows what you paste into the chat, and forgets it when the chat ends. Ask it to review a drug and you get:

*"Monitor liver function. Watch for drug interactions."*


That sounds sensible, but it's generic. It isn't linked to any real past case, and it never learns.

A real safety expert works differently. They remember **what went wrong before, and what fixed it**. That's exactly what **agent memory** gives an AI. If the idea is new to you, Vectorize has a great explainer: [What is agent memory?](https://vectorize.io/what-is-agent-memory)

I built the memory layer on [**Hindsight**](https://github.com/vectorize-io/hindsight), an open-source agent memory system by Vectorize. I used Hindsight Cloud with its Python client, and the [Hindsight docs](https://hindsight.vectorize.io/) got me from zero to a working memory quickly.

The agent uses four simple operations:

| Operation | What TrialSleuth does with it | 
|---|---|
| 🏦 **Create bank** | One memory bank, `drug-safety-memory`, told to keep IDs, doses and percentages exact | 
| 💾 **Retain** | Saves body knowledge, past drug outcomes (with the fix that worked), and a summary of every review | 
| 🔎 **Recall** | For each new drug, pulls back the relevant body facts, similar past drugs and earlier reviews | 
| 🪞 **Reflect** | A "What have you learned?" button that sums up lessons across all memory | 

## What is Hindsight?

Hindsight™ is an agent memory system built to create smarter agents that learn over time. Most agent memory systems focus on recalling conversation history. Hindsight is focused on making agents that learn, not just remember.

## hindsight-learning-demo.mp4

It eliminates the shortcomings of alternative techniques such as RAG and knowledge graph and delivers state-of-the-art performance on long term memory tasks.

🆕 **[Introducing Hindsight Models](https://hindsight.vectorize.io/blog/2026/11/03/hindsight-models)**: decision, rerank and embedding models built for agent memory. Open weights on [Hugging Face](https://huggingface.co/hindsight-ai), or hosted on Hindsight Inference. [Read the post →](https://hindsight.vectorize.io/blog/2026/11/03/hindsight-models)


**Contents**

Every memory has an ID, like `HB-02` for a body fact or `PC-102` for a past drug. The language model (Groq, running `openai/gpt-oss-120b`) must **cite the ID** for every claim. That makes each point traceable, and the app shows exactly what was recalled in a side panel, so reviewers can check the evidence themselves.

Our demo drug is a made-up cancer medicine called **HLV-772**. Its plan hides a few quiet problems: patients with weak livers are allowed in, six people are dosed on the same day, and no other medicines are banned.

- 😶 **Memory OFF:** a generic answer with no evidence.
- 🧠 **Memory ON:** it flagged a **liver risk**, citing `HB-02` (weak livers can mean 2–3× more drug in the blood) and `PC-102` (a similar drug where certain common medicines raised levels 2.5×). It suggested banning those medicines before the first dose, which is exactly the fix that worked last time.

Then I **taught it one new result**: a sister drug that affected heart rhythm in animal tests (`PC-702`). I ran the same review again and a brand-new **❤️ Heart** row appeared, citing `PC-702` and asking for ECG monitoring and heart tests before dosing.

🌱 **One new result, saved once, and every future review gets better.** That learning loop is the whole point.


**1. Better memory beats more memory.**

At first I sent *everything* recalled to the model. The prompt grew with every saved review until the model refused it. Recalling a tighter set of the most relevant records fixed the errors and made the reports sharper.

**2. Show the evidence.**

The side panel of recalled memories became the most convincing part of the app. People trust a review more when they can see what it's based on.

**3. Honest framing is a feature.**

"Here are the known risks and how to reduce them" is more useful, and far more responsible, than a confident yes or no.

Right now the memory holds a small, curated set of example records. A real version would be filled from a company's own trial history, published safety data and regulator reports, with access controls and expert sign-off on every review. I'd also love reviewers to mark which suggestions they accepted, so the agent learns which advice actually helps.

- 🚀 **Live demo:** [trialsleuthai.streamlit.app](https://trialsleuthai.streamlit.app/)
- 💻 **Source code:** [github.com/Sohapatel-26/trialsleuth-production](https://github.com/Sohapatel-26/trialsleuth-production)
- 🧠 **Hindsight on GitHub:** [github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
- 📚 **Hindsight docs:** [hindsight.vectorize.io](https://hindsight.vectorize.io/)
- 📖 **What is agent memory?** [vectorize.io/what-is-agent-memory](https://vectorize.io/what-is-agent-memory)

*If you're building AI agents that should get better with experience instead of starting from zero every time, give agent memory a try. I'd love to hear what you build!* 🙌

## Top comments (0)

## Summary

**TLDR:** TrialSleuth AI targets a real gap, since lessons from past trials are scattered, but an AI drug-safety reviewer is only as trustworthy as the evidence it can actually show.

- TrialSleuth AI is an agent that reviews a new drug before first-in-human trials and checks it against a memory of past drug results.
- The author argues that many early-trial injuries were predictable, such as known liver toxicity in a drug class or the risk of dosing six volunteers at once.
- Teams describe the drug's composition, dose, patients, trial design, allowed co-medications and lab data.
- The tool returns an overall risk level, risks by organ system with supporting evidence, suggested changes, tests to run and the limits of its review.
- It is a developer project, not a validated regulatory tool, so its clinical reliability hasn't been proven.

## 摘要

**重點摘要：** TrialSleuth AI 瞄準的是真實痛點：過去試驗的教訓散落各處。但 AI 藥物安全審查能不能信，要看它能拿出多少實際證據。

- TrialSleuth AI 是一個 AI 代理，會在新藥首次人體試驗前進行審查，並比對過往的藥物結果紀錄。
- 作者認為，許多早期試驗的傷害其實可以預見，例如同類藥物已知的肝毒性，或同一天早上替六名受試者給藥的教訓。
- 研發團隊只要描述藥物成分、劑量、受試族群、試驗設計、可併用藥物和實驗室數據即可。
- 系統會輸出整體風險等級、各器官系統的風險與依據、修改建議、該做的檢測，以及這份審查的局限。
- 這是開發者的個人專案，不是經過驗證的法規工具，臨床上可不可靠還沒有證明。