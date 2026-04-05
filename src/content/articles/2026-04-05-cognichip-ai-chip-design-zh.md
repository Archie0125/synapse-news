---
title: "Cognichip 獲 6,000 萬美元融資，以 AI 設計下一代晶片，Intel 執行長親自入董事會"
summary: "舊金山新創 Cognichip 利用物理資訊 AI 模型大幅壓縮晶片設計成本與週期，完成由 Seligman Ventures 領投的 6,000 萬美元 A 輪融資。公司宣稱可實現 75% 成本降低與 50% 週期縮短。Intel 執行長 Lip-Bu Tan 加入董事會，為這家旨在顛覆 EDA 工作流程的新創公司送出了業界最重量級的背書。"
category: "startups"
publishedAt: 2026-04-05
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/01/cognichip-wants-ai-to-design-the-chips-that-power-ai-and-just-raised-60m-to-try/"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/04/01/cognichip-raises-60m-reinvent-chip-design-physics-inspired-ai-models/"
  - name: "Unite.AI"
    url: "https://www.unite.ai/cognichip-raises-60m-series-a-to-rebuild-chip-design-around-ai/"
tags:
  - "晶片設計"
  - "EDA"
  - "AI硬體"
  - "新創"
  - "半導體"
  - "cognichip"
relatedSlugs:
  - "2026-04-05-intel-fab34-buyback-zh"
  - "2026-04-03-riscv-ai-accelerators-zh"
---

晶片設計長期以來一直是工程領域最後幾個人類專業知識的堡壘之一。AI 已改變了軟體開發、藥物發現、材料科學和蛋白質折疊，但設計一顆現代半導體的過程——由數百位專業工程師耗費數月，使用動輒耗資數十億美元的 EDA（電子設計自動化）軟體進行精細作業——基本上仍然抵抗著自動化的浪潮。

Cognichip 打賭，這種局面將在此刻終結。

這家成立於 2024 年的舊金山新創公司，於 4 月 1 日宣布完成由 Seligman Ventures 領投的 6,000 萬美元 A 輪融資，累計融資額達 9,300 萬美元。這輪融資最引人注目之處不在於金額，而在於董事會席位：Intel 執行長 Lip-Bu Tan 親自加入 Cognichip 董事會——來自全球最大晶片製造商掌舵者的親身背書，意義重大。

## 技術核心：晶片設計的物理資訊 AI

Cognichip 的平台——公司稱之為「人工晶片智能」（Artificial Chip Intelligence，ACI）——建立在一類稱為物理資訊神經網路（Physics-Informed Neural Networks，PINNs）的 AI 模型之上。與從文字或程式碼學習的通用大型語言模型不同，PINNs 將半導體行為的基本物理方程式直接整合進模型架構之中。

這一點至關重要，因為晶片設計從根本上是一個物理問題。電晶體切換特性、散熱、信號傳播、次奈米尺度下的電子穿隧——這些都受到不隨訓練資料改變的物理方程式支配。透過將物理原理內建於模型，Cognichip 的 AI 能在無需從頭模擬每種可能配置的情況下，可靠預測電路的實際行為。

依據 Cognichip 的宣稱（尚未經過獨立基準測試驗證）：相較於傳統 EDA 工作流程，其平台可帶來超過 75% 的晶片開發成本降低和超過 50% 的設計至製造交付週期縮短。作為參照，光罩製作（tape-out）——晶片設計定案並送交晶圓廠的那一刻——對複雜的 SoC 通常需要 18 至 36 個月。縮短 50% 意味著壓縮至 9 至 18 個月，這將從根本上改變半導體產業的競爭動態。

## EDA 市場的現有格局

現有的 EDA 軟體市場由三大廠商主導：Synopsys、Cadence Design Systems，以及西門子旗下的 Siemens EDA（前身為 Mentor Graphics）。這些公司提供所有主要半導體設計團隊使用的工具，其軟體套件對大型晶片廠商每年的授權費用高達數千萬至數億美元。

Synopsys 和 Cadence 都在將 AI 整合進其平台——Cadence 的 Cerebrus 和 Synopsys 的 DSO.ai 均採用強化學習優化電路佈置與布線。但這些是對現有 EDA 工作流程的漸進式改進，而非替代。

Cognichip 定位的是另一種層次的顛覆：不是在現有工作流程內提供更好的工具，而是從頭基於 AI 構建一套替代性工作流程。這與 AI 顛覆其他既有軟體平台的模式如出一轍——問題始終在於新典範是否足夠成熟以取代現有廠商，還是現有廠商只會簡單地將新方法整合進自身產品。

## Lip-Bu Tan 加入的深層意義

Intel 執行長 Lip-Bu Tan 出任 Cognichip 董事的意義，恰恰在於 Tan 是誰。加入 Intel 之前，他在 Cadence Design Systems——全球第二大 EDA 軟體公司——擔任執行長超過十年，對晶片設計工作流程的理解，在業界幾乎無人能出其右。

Tan 選擇在一家明確宣稱要顛覆他職業生涯所建立的 EDA 核心工作流程的公司擔任董事，傳遞的信號是：他相信這場顛覆是真實且即將到來的。對 Intel 而言，戰略利益同樣清晰：若 Cognichip 的平台成功，將大幅擴大能夠負擔設計客製晶片的公司範疇——而這些客製晶片設計者，都需要一座晶圓廠來生產。

Intel 執行長坐進一家讓晶片設計民主化的新創公司的董事會，本質上是為 Intel 代工服務下一注需求創造的賭注，同時也是一種對沖：若 AI 驅動的晶片設計必然到來，Intel 寧可近身參與，而不是在場外觀望。

## 30 家以上設計夥伴

Cognichip 表示目前正與 30 家以上的半導體設計公司合作，其中包括若干未具名的「業界最大廠商」，進行生產工作流程的測試。目前，該公司尚未發布任何主要透過其平台設計的晶片，財務收入也未對外揭露。

生產測試階段至關重要。半導體設計工具必須以光罩製作結果進行驗證——唯一重要的是從晶圓廠拿回的實際晶片是否符合模擬器的預測。任何 Cognichip 物理資訊預測與實際矽晶行為之間的落差，都可能是致命傷。

未具名的「業界最大廠商」參與測試，暗示至少有幾家一線晶片商正在進行並行驗證——同時使用 Cognichip 的 ACI 平台和傳統 EDA 工作流程，並比對結果。若這些驗證結果正面，正式合作與客戶公告可能在未來十二個月內陸續跟進。

## 更大的產業賭注

Cognichip 站在兩股強大趨勢的交叉點上：AI 在工程堆疊各個層面自動化知識工作，以及半導體產業在 AI 硬體需求的演進速度超越傳統設計週期的背景下，迫切需要壓縮客製晶片開發的成本與時程。

硬體-軟體協同設計的命題——下一代 AI 模型需要針對其算力模式量身設計的客製晶片，而非從通用 GPU 架構改裝——在業界的認識已日益深入。但客製晶片設計的成本與週期，歷史上一直將這種協同設計機會限制在規模最大的公司。

若 Cognichip 能在生產環境中兌現其 75% 成本降低的承諾，將讓客製矽片進入更廣大的 AI 公司的可及範圍——使目前只有少數超大規模雲端廠商才能負擔的系統級硬體-軟體協同優化成為可能。那將是 AI 產業真正具有變革性的發展。而 9,300 萬美元的押注加上 Intel 執行長親坐董事會，是業界對這種可能性所給出的最早期、也最明確的肯定。
