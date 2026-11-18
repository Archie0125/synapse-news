---
title: 微軟 MAI Code 2 打價格戰：宣稱用 5% 的價格拿到 Claude Opus 5.5 九成六的實力
summary: 微軟在 Ignite 推出 7 款 MAI 模型，主打 MAI Code 2，宣稱在 4 項程式基準測試中以 5% 的價格達到 Claude Opus 5.5 的 96% 表現。這些數字都是微軟自己公布的，附帶的條件也不少。
category: ai-ml
publishedAt: '2026-11-18T14:02:26Z'
lang: zh
type: news
safeForPublic: true
featured: false
trending: false
sources:
- name: Microsoft AI
  url: https://microsoft.ai/news/microsoft-ignite-2026/
- name: Microsoft AI
  url: https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/
- name: Interesting Engineering
  url: https://interestingengineering.com/ai-robotics/microsoft-seven-mai-models-launch
- name: Dataconomy Media
  url: https://dataconomy.com/2026/11/18/microsoft-unveils-cheaper-ai-models-to-challenge-openai/
tags:
- Microsoft
- MAI Code 2
- GitHub Copilot
- Anthropic
- OpenAI
- Azure
- AI pricing
relatedSlugs:
- 2026-11-16-hugging-face-and-openrouter-join-forces-to-make-open-weight-zh
- 2026-11-15-cohere-finding-shows-self-hosted-open-weight-models-still-ne-zh
---

微軟宣稱，MAI Code 2 只要 Claude Opus 5.5 的 5% 價格，就能達到對方 96% 的表現。跟 OpenAI 比差距小一些，但仍然可觀：用 GPT-6.1 Sol 四成的價格，拿到 98% 的表現。

微軟 11 月 17 日一口氣發表 7 款 MAI 模型，MAI Code 2 是其中的主角。其他幾款涵蓋資安、圖片編輯、即時語音、醫療逐字稿和模型路由。共同的主軸就是便宜。微軟的說法是，token 花費持續暴增，客戶需要價格低到能讓 agent 24 小時不停跑的模型。

## 程式模型的數字

MAI Code 2 的成績是 4 項基準測試的平均：DeepSWE 1.1、Terminal Bench 2.1、SWE-Atlas 和 FrontierCode v1.1。微軟說這幾項對應的是 GitHub Copilot 裡常見的企業日常寫程式工作。在前端作品的盲測中，評審有 64% 的時候選 MAI Code 2 的結果，而不是 GPT-6 Sol 的。

輕量版 MAI Code 2 Flash 負責解釋程式碼、局部修改、例行修 bug 這類大量重複的工作。微軟宣稱它的表現與 GPT-6 Luna、Claude Haiku 5.5 相當，價格分別只要對方的 65% 和 20%。

通路已經鋪好。MAI Code 2 已經開放給 GitHub Copilot 的 Pro、Pro+、Max、Business 和 Enterprise 方案，Code 2 Flash 連 Free 和 Student 用戶也能用。Code 2 Flash 也在 Microsoft Foundry 開放有限預覽。

## 附帶條件

微軟自己也把限制講得很清楚：這 2 款程式模型還沒有針對較難的任務調校，例如基礎科學研究，或是時間跨度非常長的 agent 工作。微軟也註明，效能和成本的比較會因工作負載、模型設定、推理強度和定價假設而不同。

所有比較數字都是微軟自己的說法，其中一項已經跟外部報導對不上。微軟稱 MAI Image 2.7 是全球最強的圖片編輯模型，在 Artificial Analysis 排名第一，而且只要 GPT Image 2.6 Sunburst (max) 五分之一的價格就能勝出。但 Dataconomy 報導，Artificial Analysis 在 AA-Image-Editing v2.1 排行榜上把它排在第二，1,193 Elo，落後 GPT Image 2.5 Sunburst 的 1,199 Elo；在 Arena Edit 排行榜則是第三。兩者可能是不同時間點的排名，因為 Dataconomy 提到這款模型在 10 月 27 日先以預覽版推出。不過這也說明，排名類的宣稱最好再查證一次。

## 資安、圖片、語音與路由

- **MAI Cyber 2 Flash**：用於持續性的資安防禦，包括替線上正式環境修補漏洞。微軟宣稱它在 CyberGymE2E 基準上達到 GPT-6 Astra 的水準，每項任務成本不到 2%。輸出 token 的價格比 MAI Cyber 1.1 Flash 低 86%。目前只開放給一小群客戶。
- **MAI Image 2.7 Flash**：針對大量圖片生成，每 1,000 張約 10 美元。
- **MAI Realtime 1**：微軟第一款語音對語音模型，每分鐘音訊 0.01 美元起。在微軟自己的評測中勝過 GPT-Realtime 2.1。
- **Dragon Copilot Transcribe**：建立在 MAI-Transcribe-2 上。微軟說它每月處理 1,000 萬次看診對話，多語環境的錯誤率減半，美國有三分之一的醫師在用。
- **Decision 1.1**：模型路由，只有任務真的需要時才交給較大、較貴的模型。微軟說它有 4,000 家客戶，速度是 GPT-Sol 6.1 的 50 倍，成本低 79 倍。

微軟把這批模型定位成針對特定工作負載的專才，而不是靠單一模型包辦所有事。

## 「你的權重」，但在 Azure 上

微軟同時推出 MAI Licensed Weights。企業可以用自家資料客製 MAI 模型，再放在自己的 Azure 環境裡執行。Microsoft AI 負責人 Mustafa Suleyman 表示，授權的前提是模型必須部署在 Azure 內。微軟舉的例子是 AT&T：它用 MAI 客製了一款 5G 網路分析模型，微軟說表現勝過 GPT-6.1 Sol，成本低 50 倍。

微軟表示，客戶可以決定誰能存取模型，資料和客製成果也都歸客戶所有。微軟在宣傳中直接質疑開放權重是否值得信任。

微軟自家產品也已經在用這批模型。從 Code 2 Flash 再優化出來的 MAI Work Flash，現在支援 M365 和 Fabric IQ 的多項產品。微軟也提到自研加速器 Maia 200：它已經在正式環境跑微軟最大的模型，據微軟說每瓦產出的 token 最多是主流 GPU 架構的 1.7 倍。

Suleyman 表示，他的團隊正在打造「真正的超級智慧」，但沒有給出通用前沿模型的推出日期。談到專才模型策略，他說：「這不只是一款模型，也不是曇花一現。」

## 值得關注

- Code 2 Flash 是否如期登上 Open Router、Vercel、Hermes、Open Code 和 Kilo，讓開發者能直接跟對手比價。
- MAI Cyber 2 Flash 會不會開放給那一小群客戶以外的用戶。
- MAI Image 2.7 在 Artificial Analysis 編輯排行榜上最後落在哪裡，和微軟「第一名」的說法是否一致。
- Suleyman 的通用前沿模型何時公布推出日期。

---

*本文由 AI 依本頁列出的來源撰寫；文中的數字、人名與引言在發佈前已由程式逐一對照來源。*
