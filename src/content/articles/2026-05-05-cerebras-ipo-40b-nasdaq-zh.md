---
title: "Cerebras 申請 400 億美元 Nasdaq IPO，背後是 OpenAI 百億運算大單"
summary: "AI 晶片新創 Cerebras Systems 重新遞交 IPO 申請書，目標在 Nasdaq 以 400 億美元估值籌資 40 億美元。公司背後有 OpenAI 簽下的逾 100 億美元推理運算合約，2025 年營收達 5.1 億美元，訂單積壓高達 246 億美元，這將是美國史上規模最大的 AI 晶片上市案之一。"
category: "hardware"
publishedAt: 2026-05-05
lang: "zh"
featured: true
trending: true
sources:
  - name: "The Next Web"
    url: "https://thenextweb.com/news/cerebras-ipo-4-billion-40-billion-valuation"
  - name: "Seeking Alpha"
    url: "https://seekingalpha.com/article/4898002-wall-street-lunch-ai-chipmaker-seeks-3-5b-in-ipo-eyes-26-5b-valuation"
  - name: "Winbuzzer"
    url: "https://winbuzzer.com/2026/05/04/cerebras-refiles-ipo-40-billion-valuation-xcxwbn/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/04/openais-cozy-partner-cerebras-is-on-track-for-a-blockbuster-ipo/"
tags:
  - "Cerebras"
  - "IPO"
  - "AI 晶片"
  - "OpenAI"
  - "Nasdaq"
  - "半導體"
  - "晶圓級運算"
relatedSlugs:
  - "2026-04-17-openai-cerebras-20b-chip-deal-zh"
  - "2026-05-05-whitehouse-ai-model-prerelease-review-zh"
  - "2026-04-24-sk-hynix-q1-2026-record-earnings-hbm-zh"
---

對台灣半導體業來說，Cerebras 的 IPO 不只是另一家美國 AI 新創的資本故事，更像是一個熟悉卻又充滿變數的劇本：一家以 TSMC 最先進製程為基礎的公司，靠著顛覆傳統架構的賭注，試圖在輝達壟斷的 AI 晶片市場殺出一條血路。

周一（5 月 5 日），Cerebras Systems 重新向美國證管會遞交 S-1 申請書，目標在 Nasdaq 以每股 115 至 125 美元的定價區間籌資 40 億美元，對應估值高達 400 億美元。若上市成功，這將是美國歷史上規模最大的 AI 晶片 IPO 之一，代號 CBRS。

## OpenAI 是這場 IPO 的命脈

整個故事的核心，是 Cerebras 與 OpenAI 之間的特殊共生關係。2026 年 1 月，雙方宣布一項為期至 2028 年的協議：Cerebras 將為 OpenAI 提供多達 750 百萬瓦（MW）的 AI 推理運算容量，合約總值逾 100 億美元，部分分析師估計若含全部條款，實際價值接近 200 億美元。

這份關係的結構非同尋常。OpenAI 在 2025 年 12 月先行貸款給 Cerebras 10 億美元，並以可認購逾 3300 萬股的認股權證作為擔保——意味著 Cerebras 最大的客戶，同時也是它最重要的財務支柱，日後還可能成為主要股東。支持者說這叫「利益綑綁」，公司治理學者則稱之為高度集中的單點風險。

財務面的數字同樣驚人。Cerebras 在 2025 年底揭露的訂單積壓（revenue backlog）高達 246 億美元，管理層預計 2026 至 2027 年間將認列其中約 15%。2025 年全年營收為 5.1 億美元，已幾乎是 2024 年上半年年化數字 2.72 億美元的兩倍，這樣的能見度在半導體產業中實屬罕見。

## 「晶圓級晶片」的架構豪賭

Cerebras 由 Andrew Feldman 與 Gary Lauterbach 於 2016 年創立，核心技術是被稱為「晶圓級引擎」（Wafer Scale Engine）的單片巨型晶片。不同於輝達將多個 GPU Die 透過高速匯流排串接的架構，Cerebras 直接在整片矽晶圓上製造單一晶片，面積約 46,225 平方毫米，整合 4 兆個電晶體，徹底消除晶片間通訊的延遲瓶頸。

這個設計的代價是製造難度極高。要在晶圓規模下維持商業級良率，必須仰賴 TSMC 最先進的製程與特殊的冗餘設計工程。對熟悉台積電技術難題的台灣業界人士而言，這背後的技術門檻相當清楚。每顆晶片的成本也遠高於一般 GPU，產能擴展空間受限。

然而，Cerebras 的切入點並非訓練市場，而是「推理」（inference）——也就是把訓練好的大型模型跑起來、即時回應使用者請求的這個環節。對推理工作負載來說，記憶體頻寬與每個 token 的低延遲往往比原始吞吐量更關鍵，而這恰恰是晶圓級架構的優勢所在。OpenAI 的合約以推理容量計費，等於直接為 Cerebras 的架構論點蓋章背書。

## 輝達的陰影始終存在

市值在四月初創下 5.26 兆美元歷史新高的輝達，並未袖手旁觀。其新一代 Rubin 平台於四月底正式量產，輝達宣稱推理每 token 成本較前代 Blackwell 平台下降十倍——而這正是 Cerebras 宣傳的決戰戰場。

Cerebras 的對策是：不試圖在全面戰場與輝達硬碰硬，而是在特定高價值推理場景中勝出，尤其是對超低延遲有極高要求、單晶片記憶體頻寬優勢最明顯的應用。OpenAI 願意簽下數百百萬瓦的容量合約，至少說明這個市場區間真實存在。

但 S-1 所揭露的客戶集中風險仍是最大的未解疑問：若 OpenAI 因模型架構調整、轉換供應商或自身財務問題而縮減採購，Cerebras 的積壓訂單將在一夜之間面臨重新評估。主承銷商高盛、摩根士丹利與花旗集團在機構路演中必然已詳細推演過這些情境。

## 市場時機與台灣的角色

Cerebras 目標在 2026 年 5 月中旬正式掛牌，路演本週已陸續展開。時機精心選擇：本季財報期剛落幕，亞馬遜、微軟、Alphabet 全數再次確認鉅額 AI 資料中心資本支出計畫，AI 基礎設施類股氣氛熱絡。

對台灣投資人與業界觀察者而言，Cerebras 的意義不只在於一場美國 IPO。它的晶片製造仰賴台積電最先進製程，其上市成功與否，某種程度上也是對「台積電能否支撐下一代非輝達 AI 晶片架構」的一次市場驗證。

若 Cerebras 以 400 億美元成功掛牌並穩住二級市場股價，它將成為輝達之外美國第二家具規模的公開上市 AI 晶片公司，為正在積極尋求半導體供應多元化的地緣政治格局，增添一個重要的棋子。答案，就在五月中旬。
