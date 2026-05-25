---
title: "以色列 AI 新創 Decart 完成 3 億美元 B 輪融資，估值 40 億美元，押注實體 AI 世界模型"
summary: "以色列 AI 新創 Decart 完成由 Radical Ventures 領投、Nvidia 跟投的 3 億美元 B 輪融資，估值達 40 億美元。資金將加速三條產品線：每秒處理逾 1,600 個 Token（行業均值 8 倍）的 DOS 推論堆疊、實時影像修改世界模型 Lucy，以及為機器人訓練提供仿真環境的 Oasis 實體 AI 世界模型。Andrej Karpathy 等知名 AI 學者以天使投資人身份跟投，彰顯業界對世界模型基礎設施賽道的高度認可。"
category: "ai-ml"
publishedAt: 2026-05-25
lang: "zh"
featured: false
trending: false
sources:
  - name: "Decart AI"
    url: "https://decart.ai/publications/decart-raises-300m-tech-leaders-back-the-company-as-both-customers-and-investors"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/05/18/decart-raises-300m-ai-optimization-software-world-models/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/decart-300-million-radical-ventures-world-models"
tags:
  - "decart"
  - "世界模型"
  - "實體ai"
  - "機器人"
  - "nvidia"
  - "推論"
  - "以色列科技"
relatedSlugs:
  - "2026-05-25-decart-ai-300m-world-models-physical-ai-en"
  - "2026-05-19-mind-robotics-400m-rivian-physical-ai-manufacturing-zh"
  - "2026-05-09-genesis-ai-gene-265-dexterous-robot-zh"
---

當 Andrej Karpathy 以個人名義投資一家 AI 新創時，市場都會側耳傾聽。這位 OpenAI 共同創辦人、前 Tesla AI 主管，正是 Decart 3 億美元 B 輪融資的天使投資人之一。這筆融資給這家以色列 AI 新創帶來 40 億美元估值，同時將其推至目前 AI 最具戰略意義的前沿之一：為實體系統構建世界模型。

Radical Ventures 領投本輪，Nvidia 與 Adobe Ventures、Toyota Ventures、Atreides Management、Valor Equity Partners 及 eBay Ventures 共同跟投。Sequoia Capital、Benchmark 和 Zeev Ventures 等老股東也參與其中。本輪融資完成後，Decart 累計募資逾 4.5 億美元。

## Decart 究竟在建造什麼

Decart 將產品組織為三條各自獨立、彼此關聯的產品線，每一條都針對 AI 向實體世界擴張時的不同瓶頸而設計。

**DOS（Decart 作業系統）**：公司的推論與訓練基礎設施堆疊。DOS 2.0 透過優化的核心級計算管理和自定義記憶體存取模式，使 AI 代理每秒能處理逾 1,600 個 Token——是行業均值的 8 倍。該系統與硬體無關，已在數十萬張 GPU 上部署，客戶涵蓋 Google、Microsoft 與 xAI。對每年在算力上花費數十億美元的 AI 實驗室而言，一套能在不更換底層模型的前提下榨取 8 倍以上吞吐量的系統，意味著直接的成本縮減。

**Lucy**：Decart 為沉浸式體驗打造的世界模型。Lucy 接收視訊串流作為輸入，並對畫面中的物體進行實時修改——可應用於虛擬試衣（購物者對著鏡頭舉起衣物，即可在螢幕上看到穿著效果）、互動式室內設計可視化，以及即時產品客製化。模型每秒能處理高達 100 幀高畫質影像，達到消費端實時應用的速度要求。Decart 已與零售、時尚及電商企業簽署合作協議，將 Lucy 部署至生產環境。

**Oasis**：被 Decart 描述為「世界首個專為實體 AI 設計的世界模型」，Oasis 能實時模擬物理環境。該模型可生成逼真的環境渲染圖、模擬物體交互的物理特性，並作為機器人系統的訓練基底，讓這些系統在模擬環境中發展運動技能和空間推理能力。下一版本 Oasis 3 即將推出，預計將大幅提升空間推理精度和仿真保真度。

## 世界模型為何此刻關鍵

「世界模型」指一種能維護對物理或虛擬環境內部表徵的 AI 系統——使其能夠預測環境在給定動作下的變化，而無需實時觀察每個步驟。在機器人領域，這一能力決定了系統是必須為每次決策持續查詢感測器和攝影機，還是能夠提前規劃並推理行動後果。

Decart 的賭注在於：自動駕駛汽車、人形機器人、倉儲自動化和外科系統等實體 AI 的快速發展，正在為能讓這些系統安全、高效地訓練和運行的實時仿真基礎設施，創造出龐大需求。在過去 12 個月中，實體 AI 市場共吸引了超過 50 億美元的風險投資，Figure、1X、Apptronik 和 Physical Intelligence 等公司相繼獲得重大融資。

實體 AI 的計算瓶頸不在模型架構本身，而在於能否以足夠快的速度生成充分逼真且物理精確的訓練環境。一台人形機器人在能安全疊衣服或組裝電子零件之前，需要完成數百萬次模擬試驗；若這些模擬緩慢、昂貴或物理精度不足，訓練便成為整個系統的致命瓶頸。

Decart 的 DOS 堆疊直接解決速度與成本的約束。Oasis 則解決逼真度與物理精度的約束。兩者結合，讓 Decart 不僅是實體 AI 浪潮的受益者，更是其他實體 AI 公司所依賴的基礎設施提供者。

## 投資人陣容的戰略意涵

Decart 投資人陣容的構成異常耐人尋味。Nvidia 的參與格外值得關注：這家 GPU 製造商鮮少投資可被描述為「圍繞自家硬體進行優化」的軟體公司。Nvidia 選擇押注 DOS——一套能大幅提升 GPU 利用率的系統——意味著公司將其視為讓自家 GPU 更具部署吸引力的互補基礎設施，而非業務威脅。

Toyota Ventures 的現身同樣意義深遠。豐田是實體 AI 基礎設施領域最活躍的汽車投資方之一，其對 Oasis 的投注表明，傳統汽車製造商正開始將自身定位為仿真基礎設施的錨定客戶，而非僅僅是自動駕駛系統的終端用戶。

Adobe 的加入則指向 Lucy 在企業影像和可視化應用上的商業潛力——這與 Adobe Creative Cloud 客戶群體存在天然的業務鄰接性，虛擬產品視覺化和實時渲染在其中具有顯著的商業價值。

Karpathy 的天使投資帶有特殊的可信度背書：他在 OpenAI 和 Tesla 花費多年時間，正是在構建 Decart 現在正在商業化的那類系統。他對世界模型是通往可擴展實體 AI 之真實技術路徑的判斷，比大多數機構投資人的倉位更具信號意義。

## 以色列 AI 生態的崛起時刻

Decart 是 2025-2026 年完成重大融資的一批以色列 AI 新創之一，這一現象既反映了以色列 AI 研究社群的深厚技術積累，也折射出一線矽谷創投基金日益願意押注灣區以外公司的結構性變化。領投本輪的 Radical Ventures，這家以多倫多為基地的創投機構，已成為傳統美國中心創投生態系以外最活躍的前沿 AI 投資者之一。

公司在特拉維夫設有研究部門，同時在美國擴展商業運營。

## 融資資金的用途

Decart 計畫將這 3 億美元資金重點投入三個方向：擴大 DOS 推論基礎設施規模以支持企業客戶更大規模的 GPU 部署、發布 Oasis 3 並擴展實體 AI 仿真產品線，以及壯大商業團隊，將 Oasis 能力所吸引的大量潛在需求轉化為企業合約。

據悉，公司目前正與多家汽車製造商及人形機器人公司就成為其實體 AI 訓練仿真底座進行洽談——一旦完成，這些協議將代表可觀的多年期收入承諾。

以 40 億美元估值，Decart 被定價為技術已實現規模化部署的公司——這也是事實，DOS 已在數十萬張 GPU 上運行。市場隱含回答的問題在於：Oasis 能否對實體 AI 開發產生類似 CUDA 對 GPU 計算所產生的那種影響——成為沒有它、一切都更昂貴更緩慢的基礎設施層。

由 Nvidia 領銜、Karpathy 加持的投資人陣容，表明聰明的資本正在下注「是的」。
