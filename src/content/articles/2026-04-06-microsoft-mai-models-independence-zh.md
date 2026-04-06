---
title: "微軟單飛：三款自研 MAI 模型宣告終結對 OpenAI 的依賴"
summary: "微軟發布三款完全自主研發的基礎 AI 模型——MAI-Transcribe-1、MAI-Voice-1 與 MAI-Image-2，是迄今為止微軟最明確的訊號，顯示其意圖直接與 OpenAI 競爭。這一舉措背後，是雙方重新談判的合作協議——微軟獲得自建前沿模型的自由，同時保留至 2032 年取用 OpenAI 成果的授權。"
category: "ai-ml"
publishedAt: 2026-04-06
lang: "zh"
featured: true
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/"
  - name: "GeekWire"
    url: "https://www.geekwire.com/2026/microsoft-releases-new-ai-models-to-further-expand-beyond-openai/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/microsoft-mai-models-openai-independence"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google"
tags:
  - "微軟"
  - "OpenAI"
  - "AI模型"
  - "MAI"
  - "基礎模型"
  - "企業AI"
relatedSlugs:
  - "2026-04-04-google-gemini-everywhere-zh"
  - "2026-04-04-open-source-llm-race-zh"
  - "2026-04-06-microsoft-mai-models-independence-en"
---

## 一紙協議的終結

多年來，微軟的 AI 策略有一條隱形紅線：與 OpenAI 的合作協議。原始合約中的一項條款，實際上禁止微軟獨立開發通用 AI 模型。2019 年，當 OpenAI 還是學術非營利機構時，這樣的安排或許合理；但隨著微軟砸入數百億美元，AI 成為本世代最關鍵的科技競賽，這條束縛越來越難以承受。

2025 年 9 月，局面徹底改變。雙方重新簽署的合作備忘錄給了微軟三件事：保留取用 OpenAI 所有成果至 2032 年的授權、2,500 億美元的新 Azure 雲端業務承諾，以及最關鍵的一點——自由開發競爭性前沿模型的權利。

協議簽訂後，微軟內部 AI 研究團隊（正式更名為 Microsoft AI，簡稱 MAI）立刻從研究轉向量產。2026 年 4 月 3 日，三款模型正式上架 Azure Foundry 平台。

## 微軟究竟造了什麼？

**MAI-Transcribe-1** 是一款多語言語音轉文字系統，支援 25 種語言。關鍵指標是速度：微軟宣稱比現有 Azure Fast 語音轉文字服務快 2.5 倍。對於需要大規模即時通話分析、會議記錄或無障礙工具的企業客戶，這不是邊際改善，而是足以影響採購決策的突破。

**MAI-Voice-1** 是音訊生成模型，可在約一秒的運算時間內產生 60 秒自然語音，用戶還能建立自訂音色。這讓企業可以在不向第三方授權的情況下，打造專屬語音助理，應用場景涵蓋客服自動化到語言障礙輔助工具。

**MAI-Image-2** 或許是最具話題性的一款。這款模型三月已在 Arena.ai 的文字生圖排行榜上以第三名亮相，僅次於 Google 的 Gemini 3.1 Flash 和 OpenAI 的 GPT Image 1.5。以微軟自研模型挑戰 OpenAI 的圖像生成器，在舊協議下根本是禁區。

## 三款模型背後的戰略意義

發布本身固然重要，但它所傳遞的戰略訊號更加深遠。

多年來，微軟在 AI 前沿競賽中一直是個強大卻本質上依賴外部的玩家：用 GPT-4 強化 Bing、以 OpenAI API 打造 Copilot、靠 OpenAI 獨家授權支撐 Azure 的 AI 差異化優勢。當 OpenAI 是無可爭議的前沿領袖時，這個策略行得通。

但隨著 Google、Anthropic、Meta 和開源社群接連追上，以及 OpenAI 的長期路線越來越清晰地朝消費者產品和企業服務發展——這些正好與微軟的核心業務競爭——局面已然改變。

MAI 三款模型尚未達到前沿通用大語言模型的水準，但語音、配音和圖像是低風險的試煉場域：微軟藉此建立自主研發所需的基礎設施、工具鏈與人才梯隊，為日後角逐頂尖能力做準備。

成本邏輯同樣不可忽視。微軟每年支付給 OpenAI 的 API 費用據稱高達數十億美元。只要能將部分工作負載移至自研模型，即使是較窄域的專用模型，也能降低依賴、改善毛利。隨著 MAI 能力提升，將企業客戶從 OpenAI 支撐的 Copilot 服務導向原生 Azure 模型的空間，也將越來越大。

## 平台層的競爭重構

這次發布也重塑了微軟在模型供應商生態中的角色。Azure 的模型目錄原本已涵蓋 OpenAI、Meta（Llama）、Mistral 等廠商的模型；加入自研 MAI 模型後，微軟成為同時扮演市集管理者與供應商的雙重角色。

此次伴隨發布的 Copilot 平台更新同樣值得關注：微軟推出了允許多個 AI 模型（包括 OpenAI GPT 和 Anthropic Claude）在單一工作流程中協作的功能，一個模型生成回應，另一個審查準確性。這讓 Azure 不再是 OpenAI 的運送工具，而是定位為中立的多模型編排層——長遠來看，這是更難被取代的護城河。

## 走向完全獨立的道路

業界正在觀察兩個指標：一是 MAI 語音和轉錄模型能否在企業客戶間獲得採用，驗證微軟自研模型的品質競爭力；二是微軟研究團隊是否開始發表前沿 LLM 架構論文，那將是認真挑戰 OpenAI 與 Google 的明確訊號。

目前，微軟仍在謹慎地走鋼索——既要彰顯獨立性，又不引發與 OpenAI 公開決裂所帶來的商業衝擊。這段合作仍然互利：OpenAI 需要 Azure 的算力，微軟需要 OpenAI 的模型品質來銷售企業 Copilot 授權。

但在一週內接連推出三款自研模型，傳遞的訊息再清楚不過：如果這段合作關係破裂，微軟不會無路可走。這是六個月前完全不同的談判籌碼——也將在未來數年形塑雙方的每一次對話。

微軟與 OpenAI 史上最重要的 AI 合作關係仍在持續。只是，它已不再是一種依賴。
