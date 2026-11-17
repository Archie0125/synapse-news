---
category: ai-ml
faqs:
- answer: Plurai 以企業自身的數位系統為基礎，用合成資料建立模擬環境，讓 AI 代理在部署前針對困難的極端情境接受測試與改進。這套方法沿用自駕車上路前使用的技術。
  question: Plurai 在做什麼？
- answer: 還不足以在複雜工作上完全無人監督。在 LiveBench 2.0 的長時程代理任務中，Claude Fable 5.2 得到 82.9 分、ChatGPT-6
    Astra 得到 75.6 分；在 EON 的企業模擬環境中，表現最好的 Claude Opus 4.8 準確率為 76.8%。
  question: 現在的 AI 代理有多可靠？
- answer: Plurai 完成 1,300 萬美元種子輪，由 Team8 領投，U&I、Velocity 與 Mercer 跟投。共同創辦人先前任職於自駕技術公司
    Nexar。
  question: 誰投資了 Plurai？
featured: false
lang: zh
publishedAt: '2026-11-11T14:00:00+00:00'
relatedSlugs: []
sources:
- name: TechCrunch
  url: https://techcrunch.com/2026/11/11/plurai-wants-to-help-ai-agents-work-better-using-the-same-approach-that-helped-get-self-driving-cars-to-roads/
summary: Plurai 押注 AI 代理人需要的正是當年自駕車所需要的東西：一個充滿極端情境（edge case）的模擬器。這個類比確實說得通，但也恰恰凸顯出
  AI 代理人距離真正自主運作還有多遠。
tags:
- ai-ml
- startups
- developer-tools
title: Plurai 想借鏡自駕車上路的成功經驗，讓 AI 代理人表現更出色
trending: false
type: news
---

AI agents are all the rage, but they’re not quite as capable as their purveyors would have you believe.

Efforts to benchmark agents tasked with complex work show that they aren’t typically reliable enough to function without close supervision. LiveBench 2.0 [shows](https://livebench.ai/#/?cats=Long+Agentic) Claude Fable 5.2 and ChatGPT-6 Astra succeeding on 82.9 and 75.6 out of 100 tasks, respectively, and [an effort](https://arxiv.org/pdf/2609.09853) by the AI infrastructure company EON to test agents in a simulated corporate environment found the most successful model tested, Claude Opus 4.8, performed tasks at 76.8% accuracy.

Now, a startup known as Plurai wants to boost those numbers with the same techniques that put self-driving cars on the street: Simulations using synthetic data based on a company’s own digital systems, meant to prepare models to tackle difficult edge cases.

Co-founders Ilan Kadar and Elad Levi previously worked for Nexar, which develops autonomous driving technology. Kadar worked with Waymo to simulate and evaluate its end-to-end deep learning driving software.

“The moment that we saw the wave of AI agents, we saw the same pattern: That it is very easy to build a demo, but \[hard\] to get something that will be reliable and cost effective,” Kadar told TechCrunch. “Since we saw the same pattern, the same pitch was that we want to build this simulation layer.”

On Wednesday, the startup said it had raised $13 million in seed funding to make that happen. The round was led by Team8, with participation from U&I, Velocity and Mercer.

Like the end-to-end models trained to drive cars, AI agents are probabilistic systems operating in unpredictable environments. When pressed by customers, agents tasked with booking travel can ignore spending policies. Or, when tasked with querying one database, agents can reliably provide an answer, but combining information from multiple data sets tends to gum up the works. A long conversation with a customer service bot can overwhelm an agent with too much context and lead to wrong turns.

To fix that, Plurai creates a digital twin of the company’s electronic systems, including the knowledge base and tools that an agent will have access to in production. It then maps all the possible flows of the agents, and uses that graph to prepare the model with evaluations and fixes for possible edge cases. The platform works alongside existing agentic tools like Claude Code, Codex, Copilot and Cursor.

However, Kadar says the company’s real promise is using the data it gathers to post-train small, open-weight models tailored to individual customer needs. Tests performed in cooperation with Nvidia and Nebius [showed](https://www.plurai.ai/blog/vibe-post-training-turn-any-open-model-into-a-frontier-beating-model-at-44x-lower-cost) the company’s models outperforming mid-tier frontier models at lower costs.

“We can take a large language model, we can take the task, decompose it into a smaller task using the simulation, train \[an open-weight\] model, and using the simulation, verify that the quality is higher or comparable to the frontier model, and an order or two orders of magnitude cost reduction,” he said.

Reah Miyara, a Google DeepMind researcher who backed Plurai as an angel investor, said the company’s edge comes from understanding failure modes in production, and generating synthetic data to tune models. As businesses try to optimize their AI expense, Plurai’s approach could prove a real advantage, since IT leaders are seeing that “frontier-capable models are out of distribution with my specific data, and the cost of these things isn’t sustainable in the long term,” Miyara said.

Plurai hopes analogies between AI agents in physical and digital environments can prove predictive: While powerful general AI models are imbuing robots with fascinating capabilities, they aren’t yet reliable enough to be deployed widely. Meanwhile, robots powered by AI models built for specific tasks are in the field right now, working for customers and gathering valuable real-world data.

“My view is that no matter how smart OpenAI and Anthropic model will be — and they will be much smarter — they will not know your business and your policy,” Kadar said.

## Summary

**TLDR:** Plurai is betting that AI agents need what self-driving cars needed: a simulator full of edge cases. The analogy holds, which shows how far agents are from autonomy.

- Plurai raised a $13M seed round led by Team8, with participation from U&I, Velocity and Mercer.
- Co-founders Ilan Kadar and Elad Levi came from autonomous-driving company Nexar. Kadar worked with Waymo on driving simulation and evaluation.
- The startup generates synthetic simulations based on a company's own systems to stress-test agents on edge cases.
- Top models still fail a meaningful share of agentic tasks: Claude Fable 5.2 scores 82.9 on LiveBench 2.0, and Claude Opus 4.8 reached 76.8% in EON's corporate simulation.
- Typical failures include agents ignoring spending policies when pressed by customers.

## 摘要

**重點摘要：** Plurai 押注 AI 代理需要的和自駕車一樣：一個充滿極端情境的模擬器。這個類比成立，也說明代理離真正自主還有多遠。

- Plurai 完成 1,300 萬美元種子輪，由 Team8 領投，U&I、Velocity 與 Mercer 跟投。
- 共同創辦人 Ilan Kadar 與 Elad Levi 來自自駕技術公司 Nexar。Kadar 曾與 Waymo 合作進行駕駛模擬與評估。
- Plurai 以企業自身系統為基礎生成合成模擬環境，針對極端情境對 AI 代理做壓力測試。
- 頂尖模型在代理任務上仍有明顯失敗率：Claude Fable 5.2 在 LiveBench 2.0 得到 82.9 分，Claude Opus 4.8 在 EON 的企業模擬中準確率為 76.8%。
- 常見失誤包括代理在客戶施壓下無視差旅支出規範。