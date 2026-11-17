---
title: "Anthropic 解密最強 AI：Claude Fable 5 正式對外公開"
summary: "Anthropic 於 6 月 9 日正式向公眾開放 Claude Fable 5，這是 Mythos 模型首個公開提供給開發者與消費者的版本。Fable 5 在高風險領域設有安全護欄，定價較 Opus 4.8 翻倍。更耐人尋味的是，這款模型的發布時間點，恰在該公司呼籲各大 AI 實驗室協調放緩前沿 AI 發展的數天之後。"
category: "ai-ml"
publishedAt: 2026-06-10
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: true
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/"
  - name: "Anthropic 新聞室"
    url: "https://www.anthropic.com/news/claude-fable-5-mythos-5"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html"
  - name: "Amazon About"
    url: "https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock"
tags:
  - "Anthropic"
  - "Claude"
  - "Fable 5"
  - "大型語言模型"
  - "AI 安全"
  - "基準測試"
relatedSlugs:
  - "2026-06-09-anthropic-ipo-s1-one-trillion-zh"
  - "2026-06-08-microsoft-ai-independence-mustafa-suleyman-mai-zh"
---

Anthropic 多年來始終堅持，最頂尖的模型能力強到難以安全地公開釋出。6 月 9 日，這道防線正式移動了。

這家舊金山 AI 安全公司宣布，將 Claude Fable 5——首個 Mythos 等級的旗艦模型——向消費者、開發者與企業全面開放。這批用戶過去只能望而興嘆，Mythos 的使用資格向來保留給一份嚴格審核的白名單。

發布時間點相當微妙。批評者立刻指出這顯而易見的矛盾。Anthropic 的隱性回應是：Fable 5 搭載了該公司有史以來最嚴密的公開模型安全架構。

## 新一代效能基準

在 SWE-bench Verified 軟體工程基準上，Fable 5 拿下 95% 的成績——遠超 Claude Opus 4.8 的 88.6%，刷新目前所有可公開使用模型的紀錄。在第三方實際場景評測中，成果更令人印象深刻。

資料分析平台 Hex 表示，Fable 5 是「第一個在我們核心分析基準上突破 90% 的模型」。AI 搜尋與工作流平台 Genspark 的全面測試中，Fable 5「擊敗所有其他模型」，在 UI 設計生成與遊戲程式撰寫上尤其突出。應用開發平台 Base44 則特別讚揚其從自然語言生成複雜多元件應用程式的卓越能力。

Anthropic 表示，Fable 5 擅長軟體工程、知識工作與視覺分析。對於企業 AI 程式設計助理來說，75% 和 95% 的任務成功率在商業上有著天壤之別。

伴隨 Fable 5 一同推出的還有 Claude Mythos 5——針對已獲得 Mythos 存取資格的組織更新的底層旗艦模型版本。

## 安全靠架構，不靠政策

Fable 5 的核心差異化設計在於全新的安全分類器。在資安、生物與化學以及蒸餾等高風險領域，分類器會偵測請求，Fable 5 的回應會被封鎖，改由 Claude Opus 4.8 處理。

這種「雙層路由」架構與業界通行做法截然不同。大多數安全措施依賴微調讓模型「學會」拒絕危險請求，但這類方法屢屢被繞過。Anthropic 選擇在路由層直接切斷，讓 Fable 5 根本不參與高風險問題的作答——每當退回發生時，用戶都會收到通知。

測試結果看來相當紮實。Anthropic 執行了外部漏洞獎勵測試，在超過 1,000 小時的測試中未出現任何通用越獄方式，不過該公司也指出，英國 AISI 在短暫的初期測試期間已朝此方向取得進展。早期部署數據顯示，約 95% 的對話完全由 Fable 5 作答，護欄觸發率低於 5%。

## 能力愈強，代價愈高

定價方面，Fable 5 設定為每百萬輸入 token 10 美元、每百萬輸出 token 50 美元，恰好是 Opus 4.8 的兩倍。對於頻繁或大量呼叫 API 的應用，這意味著需要重新計算投資報酬率。

為緩衝轉換壓力，Anthropic 將 Fable 5 免費開放給 Pro、Max、Team 和企業方案的用戶使用至 6 月 22 日，之後 Anthropic 將把 Fable 5 從這些方案中移除、改為需使用點數，但目標是在容量許可時恢復為訂閱方案的標準內容。

## 引發爭議的資料保留政策

隨著發布公告一起悄悄出現的，是一項政策異動：Anthropic 將對企業客戶在 Mythos 等級模型（包括 Fable 5 與 Mythos 5）上的所有流量要求保留 30 天。

Anthropic 的 API 過去以「零保留」承諾為賣點——即請求與回應不會被留存。對於明確選擇 Anthropic 正是因為這項保障的開發者而言，這是合約精神上的重大改變。公司方面的理由是安全必要性：日誌是即時識別新型越獄攻擊、協調防禦的關鍵。

法務與合規團隊正在重新評估這份新增的資料風險。部分開發者社群已將此列為轉向其他供應商的潛在理由。

## 矛盾核心的解讀

Fable 5 的發布時機很難與背景脈絡分開來看。Anthropic 多年來以「安全優先」的旗幟自我定位，將 AI 競賽描繪為潛在的文明威脅。在呼籲實驗室協調暫緩 AI 發展的數天後，就向公眾釋出能力如此強大的模型，至少在溝通層面是一道難題。

公司給出的答案是：唯有同時具備頂尖能力，安全架構才能真正受到市場考驗。只生產「足夠安全但性能平庸」的模型，無法引領業界標準。

這個邏輯在哲學層面連貫，在商業層面也清晰：隨著 OpenAI 準備 IPO、Google 將 Gemini 深植各平台，Anthropic 需要證明安全研究不是商業競爭力的天花板。Claude Fable 5，就是這場論證最直接的答案。

對在它上面蓋應用的開發者來說，最終的判斷將由接下來幾週的基準數字、帳單數字，以及那 5% 被護欄擋下的請求裡究竟藏著什麼，一一說明。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 12 處。*
