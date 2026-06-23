---
title: "Anthropic 解密最強 AI：Claude Fable 5 正式對外公開"
summary: "Anthropic 於 6 月 9 日正式向公眾開放 Claude Fable 5，這是該公司首次將 Mythos 等級的旗艦模型釋出給一般開發者與消費者。Fable 5 在 SWE-bench Verified 拿下 95% 的高分，並在高風險領域內建硬性安全護欄，定價為前代 Opus 4.8 的兩倍。更耐人尋味的是，這款模型的發布時間點恰在公司研究人員剛對外示警「AI 正變得過於危險」的數天之後。"
category: "ai-ml"
publishedAt: 2026-06-10
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

發布時間點相當微妙。就在數天之前，Anthropic 研究人員才聯署一封公開信，警告前沿 AI 系統「正在變得過於危險」，呼籲業界採取空前的監管措施。批評者立刻指出這顯而易見的矛盾。Anthropic 的隱性回應是：Fable 5 搭載了該公司有史以來最嚴密的公開模型安全架構。

## 新一代效能基準

在 SWE-bench Verified 軟體工程基準上，Fable 5 拿下 95% 的成績——遠超 Claude Opus 4.8 的 88.6%，刷新目前所有可公開使用模型的紀錄。在第三方實際場景評測中，成果更令人印象深刻。

資料分析平台 Hex 表示，Fable 5 是「第一個在我們核心分析基準上突破 90% 的模型」。AI 搜尋與工作流平台 Genspark 的全面測試中，Fable 5「擊敗所有其他模型」，在 UI 設計生成與遊戲程式撰寫上尤其突出。應用開發平台 Base44 則特別讚揚其從自然語言生成複雜多元件應用程式的卓越能力。

Fable 5 的優勢集中在 Anthropic 一貫主打的三個領域：軟體工程、知識工作與視覺分析。對於企業 AI 程式設計助理來說，75% 和 95% 的任務成功率在商業上有著天壤之別。

伴隨 Fable 5 一同推出的還有 Claude Mythos 5——針對已獲得 Mythos 存取資格的組織更新的底層旗艦模型版本。

## 安全靠架構，不靠政策

Fable 5 的核心差異化設計在於硬性護欄系統。在四個高風險領域——資安攻擊、生物武器、化學武器、核子或放射性物質合成——Fable 5 的回應被設計層封鎖，系統自動退回 Opus 4.8 以標準安全訓練作答。

這種「雙層路由」架構與業界通行做法截然不同。大多數安全措施依賴微調讓模型「學會」拒絕危險請求，但這類方法屢屢被繞過。Anthropic 選擇在路由層直接切斷，讓 Fable 5 根本不參與高風險問題的作答——對用戶而言無縫透明。

測試結果看來相當紮實。Anthropic 執行了超過 1,000 小時的外部漏洞獎勵測試，未發現任何通用的越獄方式。早期部署數據顯示，約 95% 的對話完全由 Fable 5 作答，護欄觸發率低於 5%。

## 能力愈強，代價愈高

定價方面，Fable 5 設定為每百萬輸入 token 10 美元、每百萬輸出 token 50 美元，恰好是 Opus 4.8 的兩倍。對於頻繁或大量呼叫 API 的應用，這意味著需要重新計算投資報酬率。

為緩衝轉換壓力，Anthropic 將 Fable 5 免費開放給 Pro、Max、Team 和企業方案的用戶使用至 6 月 22 日，之後改為使用點數計費，何時回歸標準方案尚未確定。Fable 5 同步上架 Amazon Bedrock，觸及大量習慣透過 AWS 管理 AI 工作負載的企業客戶。

## 引發爭議的資料保留政策

隨著發布公告一起悄悄出現的，是一項讓不少企業用戶感到不安的政策異動：所有 Fable 5 與 Mythos 5 的 API 流量，現在強制保留 30 天。

Anthropic 的 API 過去以「零保留」承諾為賣點——即請求與回應不會被留存。對於明確選擇 Anthropic 正是因為這項保障的開發者而言，這是合約精神上的重大改變。公司方面的理由是安全必要性：日誌是即時識別新型越獄攻擊、協調防禦的關鍵。

法務與合規團隊正在重新評估這份新增的資料風險。部分開發者社群已將此列為轉向其他供應商的潛在理由。

## 矛盾核心的解讀

Fable 5 的發布時機很難與背景脈絡分開來看。Anthropic 多年來以「安全優先」的旗幟自我定位，將 AI 競賽描繪為潛在的文明威脅。在剛聯署 AI 危險警告的數天後就釋出全球最強大的公開 AI 模型，至少在溝通層面是一道難題。

公司給出的答案是：唯有同時具備頂尖能力，安全架構才能真正受到市場考驗。只生產「足夠安全但性能平庸」的模型，無法引領業界標準。

這個邏輯在哲學層面連貫，在商業層面也清晰：隨著 OpenAI 準備 IPO、Google 將 Gemini 深植各平台，Anthropic 需要證明安全研究不是商業競爭力的天花板。Claude Fable 5，就是這場論證最直接的答案。

對在它上面蓋應用的開發者來說，最終的判斷將由接下來幾週的基準數字、帳單數字，以及那 5% 被護欄擋下的請求裡究竟藏著什麼，一一說明。
