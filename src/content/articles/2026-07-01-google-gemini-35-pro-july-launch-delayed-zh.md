---
title: "Google Gemini 3.5 Pro 跳票 6 月，200 萬 Token 超大語境視窗等待 7 月兌現"
summary: "Google 在 I/O 大會上承諾的 Gemini 3.5 Pro 未能在 6 月如期推出，這款搭載 200 萬 Token 語境視窗——目前前沿模型中最大——的模型延期至 7 月。跳票同周，四名資深 Gemini 研究員宣布跳槽 Anthropic，競爭對手 Claude Sonnet 5 與 GPT-5.5 卻已全面上線。"
category: "ai-ml"
publishedAt: 2026-07-01
lang: "zh"
featured: false
trending: false
sources:
  - name: "Bind AI Blog"
    url: "https://blog.getbind.co/gemini-3-5-pro-slips-to-july-and-four-senior-google-researchers-just-left-for-anthropic/"
  - name: "Analytics Insight"
    url: "https://www.analyticsinsight.net/news/is-google-delaying-gemini-35-pro-launch-to-july-for-further-testing"
  - name: "FindSkill AI"
    url: "https://findskill.ai/blog/gemini-3-5-pro-release-date/"
tags:
  - "google"
  - "gemini"
  - "ai模型"
  - "大型語言模型"
  - "deepmind"
  - "語境視窗"
relatedSlugs:
  - "2026-07-01-google-gemini-35-pro-july-launch-delayed-en"
  - "2026-07-01-anthropic-claude-sonnet-5-agentic-launch-zh"
  - "2026-06-29-apple-afm3-foundation-models-wwdc-2026-zh"
---

5 月 19 日，Google 在 I/O 大會上做出了一個具體承諾：搭載 200 萬 Token 語境視窗與 Deep Think 推理模式的 Gemini 3.5 Pro，將於 6 月正式上市。6 月 30 日，截止日已過，模型仍停留在 Vertex AI 的有限企業預覽階段，Google 悄悄將目標延至 7 月。具體日期至今未公布。

這是 Google 在 2026 年的第二次重大 AI 發布跳票。Gemini Ultra 1.5 早在年初便延期了約三個月。而 3.5 Pro 的 6 月跳票，恰好與四名 Gemini 資深研究員宣布跳槽 Anthropic 的時間點完全重疊，讓一周內的負面消息密度達到峰值。

## Gemini 3.5 Pro 到底承諾了什麼

這款模型最核心的競爭差異在於語境視窗：200 萬 Token，是 Claude Opus 4.8 與 GPT-5.5 目前提供的兩倍，足以在單一提示中處理相當於五到八部長篇小說的文字量。對於仰賴長文件處理的企業場景——法律合約、程式碼庫、研究語料、財務報告——這個優勢並非理論層面：它直接改變了在無需分塊、檢索增強或摘要流水線的情況下，架構上能做到什麼。

第二個亮點功能是 Deep Think，一種讓模型在回應前花更多時間深入思考的推理模式，對標各家前沿模型的思維鏈推理能力。但 Google 已明示，Deep Think 將獨占 Ultra 訂閱方案（月費 250 美元），標準 Pro 方案用戶無法使用。大多數企業 API 客戶若要存取 Deep Think，需要 Ultra 訂閱或另行談定 Vertex AI 方案。

上市後的預期定價約為每百萬輸入 Token 15 美元、每百萬輸出 Token 60 美元——大約是 Gemini 3.5 Flash 的十倍，也明顯高於 Claude Opus 4.8（5/25 美元）與 GPT-5.5（5/30 美元）同等級方案。Google 的定價邏輯緊扣語境視窗：200 萬 Token 的能力需要付出溢價，不需要超長語境的用戶選 Flash 或競爭對手更划算。

## 6 月跳票的真正原因

據熟悉開發進度的消息人士透露，Google 利用這段額外時間優化了模型在複雜任務上的表現，整合早期企業測試者的回饋，並修正有限預覽期間發現的 Token 效率問題。延期決定顯然是在早期 Vertex AI 客戶反映超長語境處理存在不一致性之後做出的——而這恰恰是該模型最核心的差異化能力。

諷刺意味十足：Gemini 3.5 Pro 的最大賣點是可靠地處理海量語境視窗，延期理由卻正是這個功能尚未在所有企業場景下達到生產穩定性。預測市場 Polymarket 追蹤 6 月發布概率，月底收盤時顯示「6 月無法發布」的概率高達 97%——市場早在官方承認前就已把這次延期計入預期。

## 研究員出走潮

Gemini 四名資深研究員在 6 月 21 至 27 日跳槽 Anthropic 的消息，為這次發布延期增添了厚重的敘事份量。這幾次離職緊接在年初一系列高調出走之後：Noam Shazeer 6 月中旬加入 OpenAI，John Jumper 與另外兩位同事隨即轉投 Anthropic。

累積起來——五個月內六名 DeepMind 資深研究員離職，密集的人才流失恰好疊加在跳票的產品節點——外界開始質疑 Google AI 模型研發組織的深層健康狀況。谷歌共同創辦人謝爾蓋·布林（Sergey Brin）6 月底的內部備忘錄在 AI 圈廣泛流傳，他呼籲團隊「迫切填補我們在 Agentic 執行力上的差距」——這被解讀為 Google 高層從內部認知到競爭壓力的明確信號。

當然，這並不意味著 Google 大局已定。Google 擁有全球最大的 AI 產品用戶基礎（Google 搜尋）、最深厚的基礎設施底盤，且持續大規模投入算力。但 2026 年上半年的跳票記錄與人才外流，已讓「持續引領前沿」的品牌敘事面臨挑戰。

## 競爭格局的移位

自 Google I/O 發布以來的六周，競爭形勢已發生實質性變化。Anthropic 推出了 Claude Sonnet 5，以更低價格提供接近旗艦的 Agent 能力，重寫了開發者部署的性價比算式。OpenAI 的 GPT-5.6 雖在 6 月底完成預覽，但訪問權限仍限定於政府用途。Gemini 3.5 Flash——這個家族中已上市的輕量成員——已成為成本敏感型工作負載的首選。

Gemini 3.5 Pro 必須盡快落地才能保住競爭地位。200 萬 Token 語境視窗是真實的差異化優勢，但延期越久，企業客戶就越可能基於替代架構完成部署決策。語境壓縮技術、檢索增強生成（RAG）和分塊流水線能夠以更低的每 Token 成本近似實現超長語境的部分效益——用戶一旦建立了這些替代方案，切換動力就會大幅減弱。

Google 選擇了「7 月」這個模糊目標——刻意保留彈性，不再設定可能再次食言的硬性截止日。這在執行上是務實之舉，但商業代價不小：預覽期的每一周，都是競爭對手在搶佔部署決策的一周。

## 值得追蹤的關鍵指標

最直接的催化劑是 Gemini 3.5 Pro 正式上市的具體時間。若在 7 月第一周發布、同步交出亮眼基準測試成績和 API 穩定性，Google 仍有機會重新奪回節奏。若進一步推遲至 7 月底，甚至再度因品質問題延期，人才流失與競爭壓力的雙重敘事恐將進一步強化。

除了時間節點，還需觀察 Google 是否在 API 定價上將超長語境視窗與 Deep Think 拆分——以更低的價格提供 200 萬 Token 語境，讓標準語境的替代方案難以競爭。現有預期定價結構對大多數場景都偏向競爭對手，Google 需要在中階市場提供更有說服力的性價比，才能贏得多數企業客戶的部署選擇。

Gemini 3.5 Pro 手握一個等待釋放的真實技術優勢。問題只剩一個：它能在這個優勢還有效時，及時出現在市場面前嗎？
