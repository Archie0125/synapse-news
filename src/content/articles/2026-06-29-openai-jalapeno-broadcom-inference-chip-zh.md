---
title: "OpenAI 與 Broadcom 發表 Jalapeño：專為 LLM 推論打造的自製 AI 晶片，劍指英偉達"
summary: "OpenAI 與 Broadcom 於 6 月 24 日揭曉 Jalapeño，這是 OpenAI 首款專為大型語言模型推論工作負載設計的自製 AI 加速晶片。從設計到流片僅歷時九個月，創下高效能 ASIC 開發史上最快紀錄，標誌著 OpenAI 正式啟動掌控完整運算堆疊的長期戰略。"
category: "hardware"
publishedAt: 2026-06-29
lang: "zh"
featured: false
trending: true
sources:
  - name: "OpenAI — Jalapeño 推論晶片公告"
    url: "https://openai.com/index/openai-broadcom-jalapeno-inference-chip/"
  - name: "TechCrunch — OpenAI 首款自製晶片由 Broadcom 打造"
    url: "https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/"
  - name: "CNBC — OpenAI 與 Broadcom 揭曉 Jalapeño"
    url: "https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html"
  - name: "VentureBeat — OpenAI 首款自製 AI 推論晶片 Jalapeño"
    url: "https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models/"
  - name: "Tom's Hardware — Jalapeño ASIC 技術細節"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle"
tags:
  - "openai"
  - "broadcom"
  - "ai晶片"
  - "硬體"
  - "推論"
  - "自製矽晶片"
  - "英偉達"
  - "jalapeno"
relatedSlugs:
  - "2026-06-29-ai-chip-stock-selloff-june-2026-zh"
  - "2026-06-29-onsemi-synaptics-7b-edge-ai-acquisition-zh"
  - "2026-06-27-openai-gpt56-sol-terra-luna-preview-zh"
---

6 月 24 日，OpenAI 與 Broadcom 聯合發表了代號「Jalapeño」的 AI 智慧處理器——OpenAI 有史以來第一顆自製晶片。這不只是一款新硬體的誕生，更是一份宣言：全球最廣泛使用的 AI 公司，正式宣告要掌握自身的運算命脈，而不再完全仰賴輝達（Nvidia）。

## 九個月：打破 ASIC 開發史上最快紀錄

Jalapeño 最令業界震驚的數字，不是效能指標，而是開發週期。這顆晶片從最初設計到製造流片（tape-out），僅歷時九個月。相較之下，Google、Amazon 等超大型雲端業者的自製晶片計畫，傳統上通常需要 18 到 24 個月才能完成首版矽晶片。

這驚人的速度並非偶然。OpenAI 的工程師在設計過程中直接使用自家 AI 模型加速晶片設計與最佳化，形成「AI 幫 AI 造基礎設施」的遞迴迴圈。Broadcom 負責矽晶片實作，Celestica 則處理電路板、機架與系統整合。

目前，工程樣品已在實驗室中以量產目標頻率與功耗運行機器學習工作負載，包括 OpenAI 內部的程式碼模型 GPT-5.3-Codex-Spark。預計 2026 年底前大規模量產部署。

## Jalapeño 的定位：專攻推論，不取代訓練

這顆晶片的架構專為「推論」設計——也就是在模型訓練完成後，回應使用者輸入、執行模型的運算過程。這正是 OpenAI 每天最燒錢的地方：每一次 ChatGPT 對話、每一個 API 呼叫、每一行 Codex 補全，都是推論運算。

Jalapeño 的設計著重解決 LLM 推論規模化時的核心瓶頸：記憶體與運算核心之間的資料搬移效率、記憶體頻寬與運算能力的平衡、晶片間網路效率，以及影響使用者延遲的服務模式。初步測試顯示，其每瓦效能顯著優於現有最先進替代方案，不過 OpenAI 目前尚未公布具體基準數據。

值得注意的是，Jalapeño 並不打算取代 Nvidia 的前沿模型訓練角色。訓練大型模型這種消耗月計算量的超重量級工作，短期內仍將繼續仰賴 Nvidia GPU。Jalapeño 的目標是推論——OpenAI 每日成本最高的環節。

## 自製晶片的成本邏輯

要理解這件事的重要性，需要了解 OpenAI 的成本結構。ChatGPT 擁有數億用戶，每天產生龐大的推論工作負載。儘管 OpenAI 的年化營收已接近主要雲端業者的規模，但長期以來有相當大比例的營收都回流給了 Nvidia。

自製推論晶片提供了大幅改善經濟效益的路徑。Google 的 TPU（張量處理器）讓其在 Gemini 規模化成本上具備結構性優勢已逾十年；Amazon 的 Trainium 與 Inferentia 也發揮類似作用。加入這個行列，意味著 OpenAI 未來可以在與雲端業者的談判中取得更有利的條件，降低對現貨 GPU 市場的依賴，並改善每一次 API 呼叫的單位經濟效益。

OpenAI 總裁 Greg Brockman 表示，公司正在尋找「特定未被充分服務的工作負載」，並致力於「加速可能的邊界」——謹慎的措辭，同時承認了這顆晶片能做與不能做的事。

## 多代晶片平台的長期佈局

OpenAI 與 Broadcom 將 Jalapeño 定位為「多代運算平台」的第一步，而非一次性產品。雙方合作夥伴關係於 2025 年 10 月正式宣布，構想多個世代的自製 AI 加速器，規模從初始部署，逐步擴展到與 Microsoft 及其他基礎設施夥伴共建的千兆瓦（gigawatt）級資料中心。

千兆瓦的野心不容小覷。一千兆瓦的資料中心用電量，大約相當於一座中型美國城市的總用電量。OpenAI 正在規劃一個用國家電網規模衡量的 AI 運算版圖。

## 更大的晶片競賽

Jalapeño 出現在 AI 硬體版圖正在劇烈重塑的時刻。Qualcomm 據報正與 RISC-V 晶片新創 Tenstorrent 商談約 80 到 100 億美元的收購案；三星與 SK 海力士正在爭搶供應所有這些晶片所需的新一代 HBM 記憶體；Nvidia 的 AI 運算壟斷地位雖然仍在，但正被多個方向同步蠶食。

對整個產業而言，每一家主要 AI 實驗室推出的自製晶片都在傳遞一個訊號：AI 公司只要採購 Nvidia 最新 GPU 就算策略的時代，已經結束了。未來十年主導 AI 產業的，將是那些不只打造模型、更掌控模型底層完整堆疊的公司——包括晶片、互連、伺服器，以及資料中心。

OpenAI 剛剛在這條路上邁出了最認真的一步。

---

*Jalapeño 預計於 2026 年底前開始在 OpenAI 資料中心部署，Broadcom、Celestica 與 Microsoft 為主要合作夥伴。*
