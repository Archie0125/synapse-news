---
title: "歐洲 AI 晶片新創瞄準 Nvidia 推論主導地位，各自尋求逾億美元融資"
summary: "以荷蘭新創 Euclyd 為首的歐洲 AI 晶片公司正展開百萬歐元級別融資，聲稱其推論晶片系統可達到 Nvidia Vera Rubin 架構 100 倍的能源效率。前 ASML 執行長 Peter Wennink 任顧問的 Euclyd，與 Fractile、Optalysys 等公司共同形成一股挑戰 Nvidia 推論市場的歐洲力量。"
category: "hardware"
publishedAt: 2026-04-20
lang: "zh"
featured: false
trending: true
sources:
  - name: "CNBC — Nvidia 競爭對手告知 CNBC 尋求至少 1 億美元融資"
    url: "https://www.cnbc.com/2026/04/17/nvidia-rivals-chip-market-funding-ai-asml-euclyd.html"
  - name: "NL Times — 艾因霍芬 Euclyd 目標募集 1 億歐元"
    url: "https://nltimes.nl/2026/04/17/eindhoven-based-euclyd-targets-eu100-million-funding-round-ai-chip-expansion"
  - name: "EE News Europe — Euclyd 發布 CRAFTWERK 超大規模推論架構"
    url: "https://www.eenewseurope.com/en/euclyd-unveils-craftwerk-exascale-inference-architecture-targets-agentic-ai-at-record-efficiency/"
tags:
  - "AI晶片"
  - "Nvidia"
  - "Euclyd"
  - "歐洲"
  - "AI推論"
  - "半導體"
relatedSlugs:
  - "2026-04-07-nvidia-vera-rubin-nvl72-production-zh"
  - "2026-04-19-huawei-ascend-950pr-china-ai-chip-zh"
  - "2026-04-05-cognichip-ai-chip-design-zh"
---

Nvidia 對 AI 基礎設施支出的掌控看似無懈可擊，但一群歐洲硬體新創正在押注：推論市場的經濟學將撕開這道護城河。領頭的是荷蘭艾因霍芬的 Euclyd，這家公司本週宣布正積極尋求至少 1 億歐元（約 1.18 億美元）的融資，核心論點是：其專用推論晶片系統在能源效率上可達 Nvidia 最新 Vera Rubin 世代的 100 倍。

Euclyd 並非孤軍奮戰——英國的 Fractile、光子運算新創 Optalysys，以及德國的 Arago，據報均在進行規模相近的融資，顯示歐洲硬體野心正匯聚成一股有組織的力量，目標直指 Nvidia 最具利潤的市場區段。

## Euclyd 在做什麼

Euclyd 於 2024 年由前 ASML 總監 Kas Kastrup 創立，在歐洲半導體圈擁有不容小覷的人脈背景。更引人矚目的是，公司的顧問和早期投資人是 Peter Wennink——這位將 ASML 打造為全球最具戰略價值半導體設備公司的前執行長，其人脈觸達歐洲整個晶片供應鏈生態系。對一家成立僅 18 個月的新創而言，這種資源積累殊為罕見。

公司旗艦產品是 CRAFTWERK，定位為「超大規模（Exascale）推論架構」，專攻代理型 AI 工作負載。其技術路線與 GPU 正統範式存在根本差異。

傳統 GPU（包含 Nvidia 的 Vera Rubin）的運算邏輯是：從記憶體讀取資料到運算核心處理，再將結果寫回記憶體——資料搬移消耗大量能源與時間。Euclyd 則採取「近記憶體運算（compute-near-memory）」方式：在資料存放處附近直接處理，大幅削減資料移動帶來的能耗和延遲。這個瓶頸已被業界認定為大型語言模型推論規模化的主要制約之一。

在針對 Meta Llama 4 Maverick 的模型化效能數據中，Euclyd 的 CWS 32 多晶片系統預計僅消耗 125 千瓦電力即可達到每秒 768 萬 tokens 的吞吐量，宣稱每 token 的能源效率較主流 GPU 方案高出 100 倍。需要特別注意的是，這些數字目前仍是模型預測，尚未在真實客戶環境中大規模驗證。

Euclyd 目前已有可用的原型推論晶片，整套多晶片系統的生產就緒目標設定為 2028 年，並已與四家潛在客戶展開洽談。此輪募資將主要用於驅動這個產品開發衝刺至首批交付。

## 為何推論是戰場

聚焦推論而非訓練來挑戰 Nvidia，背後有清晰的市場邏輯。訓練大型模型是密集但偶發的活動，主要由少數頂尖實驗室承擔，預算充裕且對成本容忍度較高。推論——將訓練好的模型部署用於服務數十億次用戶查詢——則是持續的、與用戶規模同步成長的，是每一個在 AI 上構建應用的企業、新創與開發者都必須面對的現實。

隨著模型部署走向成熟，推論已成為多數組織 AI 算力支出的主要組成。Dealroom 估計 2026 年全球 AI 晶片新創合計融資 83 億美元，其中推論專用架構吸引的資本比例持續上升。

代理型 AI 的崛起更放大了這個動態。一次觸發可執行數十乃至數百步連續推論的 AI 代理的用戶互動，其算力需求相比簡單聊天機器人回應呈指數級增長。Euclyd 的 CRAFTWERK 正是針對這種「高吞吐、持續性推論」而非「突發式請求回應」的工作模式設計。

## Fractile、Optalysys 與歐洲晶片群落

Euclyd 是目前歐洲晶片挑戰者中最顯眼的一家，但不是唯一一家。英國的 Fractile 已確認正在尋求約 1.6 億英鎊融資，開發專為 Transformer 架構優化的推論晶片，並已獲 NATO 創新基金的早期投資——這個細節顯示歐洲國防與安全考量已融入 AI 晶片投資邏輯之中。

Optalysys 採用光子運算路線，利用光學計算執行 AI 矩陣乘法，理論速度可達電子訊號的極限。光子計算在特定推論場景有望帶來數量級的能效提升，但規模化部署面臨的工程挑戰同樣不容小覷。

德國的 Arago 則專注於軟硬體協同設計層面，在針對特定模型架構優化晶片設計的同時，也優化模型本身——而非將模型視為固定不變的輸入。

這批新創在地理上密集分布於荷比盧德英走廊，並非偶然：ASML 供應鏈與半導體設備專業知識的鄰近優勢、《歐洲晶片法案》的產業政策支持，以及來自 Arm、ASML 與高通歐洲研究中心的工程人才持續輸血，共同形成了這個新創集群的土壤。

## Nvidia 的護城河與挑戰者的路徑

這一切並不意味著 Nvidia 面臨立即的威脅。公司最新季度資料中心營收達 623 億美元，年增 75%，Q1 FY2027 指引約為 780 億美元。更重要的是，CUDA 生態系、cuDNN、NIM 推論微服務平台，以及與各大雲端巨頭的深度整合，構成了純粹的矽片效率主張無法一夕撼動的護城河。

歷史上，挑戰者晶片公司的突破路徑通常是：鎖定 GPU 通用架構確實低效的特定工作負載，打入第一批客戶，再以營收和公信力為跳板逐步擴展。Cerebras Systems 以晶圓級晶片攻佔大型模型訓練市場、Groq 以確定性低延遲推論找到立足點，都遵循了這條邏輯。歐洲這批新創押注的，是代理型推論時代將開創新的市場開口。

Euclyd 設定的 2028 年量產時間表在晶片開發週期上是合理的，但這也意味著屆時必須與當時最新一代的 Nvidia 架構競爭——而非現在的 Vera Rubin，而是可能更強大的下一代。AI 硬體的演進速度非常快。

本週歐洲晶片新創密集湧現的融資信號，至少說明了一件事：推論市場的規模與能耗成本已足夠吸引嚴肅的資本和人才投入這場挑戰。Euclyd、Fractile 或其他歐洲玩家能否將工程效率主張轉化為持續的商業牽引力，是未來 24 個月將開始給出答案的問題。
