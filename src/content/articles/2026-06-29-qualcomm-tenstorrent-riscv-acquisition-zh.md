---
title: "Qualcomm 傳百億美元洽購 Tenstorrent：RISC-V 押注，劍指英偉達資料中心霸權"
summary: "Qualcomm 據報正在與 RISC-V AI 晶片新創 Tenstorrent 進行進階收購談判，出價 80 至 100 億美元，是該公司去年估值的三倍。Tenstorrent 由傳奇晶片架構師 Jim Keller 領軍，其 Blackhole AI 晶片採用開源 RISC-V 架構。若交易完成，Qualcomm 將取得資料中心 AI 的可信戰略、深厚的 RISC-V 技術根基，以及當世最受尊崇的晶片設計師。"
category: "hardware"
publishedAt: 2026-06-29
lang: "zh"
featured: false
trending: false
sources:
  - name: "The Register — Qualcomm 傳洽購 Tenstorrent"
    url: "https://www.theregister.com/systems/2026/06/16/qualcomm-said-to-be-circling-ai-chip-biz-tenstorrent-in-10b-risc-v-power-play/5256084"
  - name: "AI Weekly — Qualcomm 瞄準 Tenstorrent 百億收購"
    url: "https://aiweekly.co/alerts/qualcomm-targets-tenstorrent-in-reported-10b-risc-v-deal"
  - name: "AI Unfiltered — Qualcomm 洽購 Tenstorrent 80-100 億美元"
    url: "https://www.arturmarkus.com/qualcomm-in-talks-to-acquire-tenstorrent-for-8-10-billion-jim-kellers-risc-v-ai-chip-startup-valuation-triples-in-one-year/"
  - name: "TechTimes — Qualcomm 押注 RISC-V 破英偉達壟斷"
    url: "https://www.techtimes.com/articles/319017/20260624/qualcomm-bets-14-billion-cracking-nvidias-ai-monopoly-risc-v-open-compiler.htm"
tags:
  - "qualcomm"
  - "tenstorrent"
  - "risc-v"
  - "jim-keller"
  - "ai晶片"
  - "收購"
  - "硬體"
  - "英偉達"
  - "資料中心"
  - "blackhole"
relatedSlugs:
  - "2026-06-29-openai-jalapeno-broadcom-inference-chip-zh"
  - "2026-06-29-ai-chip-stock-selloff-june-2026-zh"
  - "2026-06-29-onsemi-synaptics-7b-edge-ai-acquisition-zh"
---

根據本月多份報告，Qualcomm 正與加拿大 AI 晶片新創 Tenstorrent 進行進階收購談判，出價介於 80 至 100 億美元，約為該公司一年前估值的三倍。消息最早由《The Information》披露，《路透社》隨後獨立確認。目前兩家公司均未公開置評，交易尚未完成。

但戰略邏輯顯而易見。若交易達成，這將是 Qualcomm 多年來最重大的押注，清楚宣示這家行動晶片巨頭不再旁觀資料中心 AI 熱潮。

## Tenstorrent 是誰？

Tenstorrent 成立於 2016 年，總部位於多倫多，十年來一直在追求一種與英偉達三十年磨練的 GPU 範式根本不同的 AI 硬體路線。這家公司不是改造圖形處理器來承擔 AI 工作負載，而是從零開始基於 RISC-V 指令集架構打造晶片——一種開放標準，允許晶片設計師自訂處理器核心，無需向 Arm 或 Intel 支付授權費用。

旗艦產品 Blackhole 晶片於 2026 年 4 月正式量產上市，其計算架構圍繞 Tensix 核心構建，對神經網路運算如何在矽晶片上分配有獨特主張。每顆 Blackhole 晶片包含 768 個 RISC-V 核心，搭配專用 AI 引擎與高頻寬互連，針對大規模 AI 部署所需的分散式推論工作負載而設計。

Galaxy Blackhole 平台將 32 顆 Blackhole 晶片封裝進一個 6U 伺服器機箱——這是高密度、高吞吐量的配置，瞄準希望以低於英偉達 H 系列與 B 系列 GPU 每晶片成本運行大型模型的資料中心客戶。

## 為什麼 Jim Keller 才是真正的核心資產

談到 Tenstorrent，第一個被提及的名字永遠是 Jim Keller。他在半導體設計領域的成就記錄，是在世從業者中無可比擬的：他設計了 AMD K8 處理器，讓那家公司在 21 世紀初起死回生；設計了 Apple A4 和 A5 晶片，奠定初代 iPhone 的矽晶片基礎；主導了 AMD Zen 微架構的開發；打造了特斯拉的全自動駕駛晶片；還擔任過英特爾矽晶片工程部門主管。

在 Tenstorrent，Keller 將這些經驗從第一原理出發應用於 AI 硬體問題。他的設計哲學強調激進效率——以最小的功耗和面積榨取最大計算量——而非單純擴展現有架構。RISC-V 的押注反映了一種信念：AI 硬體的未來需要開放、可定制的核心，能針對特定工作負載量身打造，而非改造自通用設計。

對 Qualcomm 而言，收購 Tenstorrent 不只是買下一家公司，而是雇用當代最受推崇的晶片架構師，來領導公司硬體戰略的全新戰線。

## Qualcomm 缺少什麼？

Qualcomm 在 AI 時代的處境，是行動市場主導地位未能順滑轉化為資料中心機會的典型案例。Snapdragon SoC 系列主導了高端 Android 市場，為全球大多數智慧手機提供動力。但資料中心 AI——過去三年技術領域創造最多財富的賽道——基本上是英偉達的天下，AMD、Google TPU 和 Amazon Trainium 僅佔據部分市場份額。

Qualcomm 曾有機地嘗試進入資料中心 AI 領域，但成果有限。其伺服器級 Arm 晶片找到了客戶，但無論規模還是定價都未能在推論或訓練上挑戰英偉達。與此同時，Qualcomm 與 Arm Holdings 的授權糾紛，更為其 RISC-V 野心增添了戰略緊迫性——深度掌握 RISC-V 能力，意味著減少對正在訴訟中的供應商的存亡依賴。

2025 年 12 月，Qualcomm 收購了規模較小的 RISC-V 伺服器晶片新創 Ventana Micro Systems，分析師將此解讀為進軍資料中心的第一步。Tenstorrent 的收購談判規模估計是前者的 20 至 25 倍，代表著截然不同量級的承諾。

## RISC-V 的時代節點

Tenstorrent 的 RISC-V 架構，處於 2025 至 2026 年加速演進的更廣泛產業轉型的核心。隨著 Arm 授權費用上漲，以及西方晶片設計面臨的地緣政治壓力加劇，這個開放標準吸引了 Google、三星、Western Digital 及越來越多新創公司的認真投入。

吸引力是結構性的：RISC-V 允許任何公司針對特定工作負載設計定制處理器，無需支付版稅、無需談判技術存取協議、也不面臨私有指令集帶來的供應商鎖定風險。對於 AI 推論——工作負載特性已充分理解、優化空間巨大的賽道——基於 RISC-V 的設計有潛力以遠優於通用替代方案的每美元效能競爭。

若 Qualcomm 完成收購，RISC-V 在 AI 領域最具技術信譽的實作，將進入一家擁有製造關係、客戶資源與資本規模的公司手中。這個組合若執行得當，正是挑戰英偉達資料中心地位所需的能量。

## 前路充滿變數

目前不確定性真實存在。報告顯示談判持續進行中，但無法保證達成協議。80 至 100 億美元的估值範圍，相較 Tenstorrent 在 2025 年中 32 億美元的融資估值，約 12 個月內增長了三倍，反映了 AI 晶片的市場熱情與 Tenstorrent 在量產競爭性硬體方面的真實進展。

Qualcomm 現有的半導體市場地位意味著可能面臨監管審查，但鑒於 RISC-V 晶片目前市場份額仍小，反壟斷顧慮或許可控。更關鍵的問題可能是 Jim Keller 自身的去留意願——他是否願意留下來領導一家大型企業內部的晶片事業部，還是這次出售將成為最終推動他離開的契機。

可以確定的是大方向：當 OpenAI 在打造 Jalapeño 推論晶片、Apple 在 iPhone 快閃記憶體上運行 200 億參數模型、onsemi 以 70 億美元收購 Synaptics 強化邊緣 AI，AI 硬體市場正在從英偉達的近壟斷格局，走向多元化的專用矽晶片生態系。Qualcomm 若成功收購 Tenstorrent，正是在這個新世界豪下巨注，押注自己成為核心玩家。

---

*談判仍在進行中，尚未宣布任何交易。路透社與《The Information》率先於 2026 年 6 月披露相關討論。*
