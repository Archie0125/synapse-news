---
category: ai-ml
faqs:
- answer: On most major AI providers, output tokens are priced higher than input tokens,
    often three to five times higher. Users also control output length least, because
    the model decides how much to say.
  question: Why do output tokens matter more than input tokens for AI costs?
- answer: In the author's example, sorting 50 customer messages into a simple table
    takes about 500 output tokens, while a paragraph-per-message explanation takes
    about 2,500. That is five times the output cost for the same result.
  question: How much can a verbose answer cost compared with a concise one?
- answer: Ask explicitly for compact formats such as tables, lists or one-line answers,
    and say when no explanation is needed. The savings on each answer are small, but
    they add up across daily chats and tools.
  question: How can users reduce output token spending?
featured: false
lang: en
publishedAt: '2026-11-11T05:54:43+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/mohsinakram91/stop-paying-for-ai-to-think-out-loud-1dgn
summary: Your AI bill is bloated by verbose answers, not your prompts, and output
  tokens are where the real money quietly leaks.
tags:
- ai-ml
- developer-tools
title: Stop Paying for AI to Think Out Loud
trending: false
type: news
---

Most of us watch the wrong side of our AI bill. We obsess over what we type in — the prompt, the pasted document, the giant file we attached — and barely glance at what comes back. But on most major AI providers, output tokens cost more than input tokens. Often three to five times more. Every long-winded answer, every over-explained fix, every "here's a detailed breakdown" you didn't ask for is billed at the most expensive rate on the menu.

I started noticing this when I looked at my own usage. The prompts were reasonable. The answers were the problem: a simple question returning a five-paragraph essay, a one-line bug fix arriving with a 400-word explanation of what the bug was, a request for a list returning a list — plus an introduction, a conclusion, and a friendly offer to explain further. None of it was wrong. All of it was billed.

Think of it as two different prices for two different things:

- **Input tokens** are what you send. They are usually the cheaper side.
- **Output tokens** are what the model writes back. They are usually the expensive side — and they are the side you control least, because the model decides how much to say.

A prompt of 1,000 tokens might cost you a few cents. But if the model answers with 2,000 tokens of thorough explanation, the answer can cost several times the question. Now multiply that by every chat, every day, across every tool in your stack. The waste is quiet because no single answer looks expensive. The bill is where it adds up.

Here is a small, concrete example. Say you ask an AI assistant to sort 50 customer messages into categories. The smart way to get that answer is a short table: message, category, done. Instead, the model writes a paragraph per message explaining its reasoning, then a summary, then a note about edge cases. The table would have been roughly 500 tokens. The essay version is closer to 2,500. Same result, five times the output cost — and you still have to read it.

**1. Asking open questions when you want a closed answer.** "What do you think about this code?" invites an essay. "List the three bugs in this function, one line each" invites a short list. The shape of your question decides the length of the answer.

**2. Never setting a format.** If you don't say how you want the answer, the model defaults to its most generous format: headings, introductions, bullet points, and a closing summary. A format instruction is the cheapest cost control you own.

**3. Accepting explanations you didn't ask for.** When a model fixes your code, it often explains the fix at length. If you already understand the area, that explanation is pure cost. Ask for the fix first, and the explanation only if you need it.

**4. Letting agents narrate their own work.** Coding agents and multi-step automations often log every thought, every tool call, every "let me check that" in the output stream. If that narration is saved, summarized, or passed along to the next step, you are paying to store and re-read a diary of the work instead of the work itself.

- **Ask for the shape, not just the content.** "Answer in a table." "Five bullets, max." "One sentence per item." Models follow format instructions well, and a format is worth more than a word limit because it removes the filler, not just the length.
- **Split "do it" from "explain it."** First message: do the task, output only. Second message, only when you need it: explain the tricky part. Most of the time you will never send the second message — and that is the saving.
- **Use structured output for repeatable jobs.** If the same task runs daily — classifying messages, extracting fields, summarizing tickets — ask for JSON or a fixed table. Structured output is shorter, cheaper, and easier to feed into the next step without re-reading prose.
- **Cap reasoning where the tool allows it.** Some providers and coding tools let you limit how much the model reasons before answering. For routine jobs, a short reasoning budget is plenty. Save the deep thinking for genuinely hard problems.
- **Audit one week of output, not input.** Most usage dashboards show tokens in and tokens out. Look at the ratio. If your output tokens are consistently much larger than your input tokens, your prompts are fine — your answers are too long.

None of this means using AI less, or getting worse answers. It means getting the same answers in fewer words, at the expensive end of the bill. The best AI users I know are not the ones with the cleverest prompts. They are the ones who are specific about what should come back.

I write about the real cost of building with AI — and the tools I build to keep it under control — on my YouTube channel ([https://www.youtube.com/@onyxaipk](https://www.youtube.com/@onyxaipk)) and my Gumroad store ([https://onyxailabs.gumroad.com](https://onyxailabs.gumroad.com)), where my AI Spend Tracker helps you see exactly where your AI money goes.

What is the longest, least useful answer an AI tool has ever given you — and how much of it did you actually read?

## Top comments (0)

## Summary

**TLDR:** Your AI bill is bloated by verbose answers, not your prompts, and output tokens are where the real money quietly leaks.

- On most major AI providers, output tokens cost more than input tokens, often three to five times more.
- Users focus on prompt size, but the model controls answer length, and unrequested explanations are billed at the highest rate.
- In the author's example, sorting 50 messages as a table takes about 500 tokens, while an essay-style answer takes about 2,500, five times the output cost for the same result.
- No single verbose answer looks expensive, but the waste adds up across chats, days and tools.
- Asking explicitly for concise formats such as tables or lists is the most direct way to cut costs.

## 摘要

**重點摘要：** AI 帳單會膨脹，問題不在你的提示詞，而在模型的長篇大論；輸出 token 才是悄悄漏錢的地方。

- 多數主流 AI 服務的輸出 token 比輸入 token 貴，常常貴三到五倍。
- 使用者只盯著提示詞長度，但回答長度是模型決定的，沒人要求的解釋全都按最高費率計價。
- 作者舉例：把 50 則訊息分類，用表格約 500 個 token，寫成長文約 2,500 個，同樣結果、輸出成本五倍。
- 單一則冗長回答看起來不貴，但累積到每天、每個對話、每個工具，帳單就爆了。
- 最直接的省錢方法，是明確要求精簡格式，例如表格或清單。