---
title: "AMD 豪賭 50 億美元押注 Anthropic，部署 2GW MI450 GPU 挑戰 Nvidia 霸主地位"
summary: "AMD 與 Anthropic 於 2026 年 7 月 22 日宣布重大戰略合作：Anthropic 將透過 AMD Helios 機架級解決方案部署高達 2 吉瓦的 AMD Instinct MI450 系列 GPU，AMD 則承諾在達成部署里程碑後向 Anthropic 投資最高 50 億美元。這是 AMD 史上首次對 AI 公司的股權投資，使 AMD 繼 OpenAI 之後再添一家旗艦 AI 實驗室客戶，並直接衝撞 Nvidia 在 AI 訓練與推論基礎設施上的寡占地位。"
category: "hardware"
publishedAt: 2026-08-02
lang: "zh"
featured: false
trending: true
sources:
  - name: "CNBC – AMD to invest up to $5 billion in Anthropic as part of computing power deal"
    url: "https://www.cnbc.com/2026/07/22/amd-anthropic-ai-chip-investment.html"
  - name: "AMD 新聞稿 – AMD and Anthropic Announce Strategic Partnership to Deploy Up to 2 Gigawatts of AMD Instinct MI450 Series GPUs"
    url: "https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus"
  - name: "The Next Web – AMD is investing $5 billion in Anthropic and deploying 2 gigawatts of Helios GPUs to run Claude"
    url: "https://thenextweb.com/news/amd-anthropic-5-billion-investment-2gw-helios-mi450"
tags:
  - "AMD"
  - "Anthropic"
  - "MI450"
  - "AI晶片"
  - "Nvidia"
  - "ROCm"
  - "AI基礎設施"
  - "資料中心"
  - "Helios"
relatedSlugs:
  - "2026-07-26-anthropic-claude-opus-5-launch-en"
  - "2026-07-10-ai-chip-stocks-bear-market-correction-en"
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-en"
---

多年來，一句話可以概括 AMD 的 AI 策略困境：硬體夠強，軟體太差。AMD Instinct GPU 系列在帳面規格上表現亮眼，開發者卻依然選擇 Nvidia 的 CUDA 生態系——只因為它能用、可靠、在規模化部署時不會出現 AMD ROCm 開源 GPU 軟體堆疊長年帶來的種種摩擦。2026 年 7 月 22 日，AMD 選擇同時解決這兩個問題。

AMD 宣布與 Anthropic 達成全面戰略合作：Anthropic 將透過 AMD Helios 機架級解決方案，部署高達 2 吉瓦的 AMD Instinct MI450 系列 GPU；AMD 則承諾在達到特定部署里程碑後，向 Anthropic 投資最高 50 億美元。這筆交易在 Nvidia 市場地位看似無懈可擊的時刻，重塑了 AI 基礎設施的競爭格局。

## 硬體：Helios 與 MI450 系列

此次合作的技術核心是 Helios 機架級解決方案——AMD 對標 Nvidia NVL 系列全整合伺服器平台的答案。一個 Helios 機架將 AMD Instinct MI455X GPU（MI450 系列的主力晶片）、AMD EPYC「Venice」CPU、用於高頻寬網路的 AMD Pensando DPU，以及 AMD ROCm 軟體堆疊整合進一個統一系統，專為超大規模部署設計。

MI455X 基於 AMD CDNA 4 架構，鎖定大規模訓練與推論市場。AMD 尚未公布 MI455X 的完整規格，但聲稱以完整 Helios 機架計算，該晶片在總系統成本上低於 Nvidia Blackwell H200，同時提供相近的密集計算性能。獨立第三方基準測試通常落後重大發布數月，最終將為這項主張做出裁判。

為 Anthropic 部署首個吉瓦 Helios 算力的時程定在 2027 年上半年。第二個吉瓦尚無明確時間表，但 AMD 表示兩個批次均與投資承諾里程碑掛鉤。

## 50 億美元的賭注：理解這筆投資

「50 億美元投資」這個數字需要背景說明。AMD 並非一次性支票：這項承諾採里程碑解鎖機制，意味著 AMD 在 Anthropic 實際部署承諾算力時才取得股份。這讓雙方利益在一段漫長時程內保持一致，並給予 AMD 確保 Helios 部署順暢的切實動機——而非貨出門後便算了事。

這是 AMD 史上首次對 AI 公司進行股權投資，是其作為純晶片廠商身分認同的結構性轉變。這一舉動呼應了業界日益顯著的趨勢：晶片公司意識到下游 AI 應用的成功直接驅動硬體需求，使前沿模型實驗室的股權持有既是高效的渠道佈局，也是戰略對沖。

對比 Nvidia 耐人尋味：Nvidia 與 OpenAI、微軟和 Meta 的關係主要是商業採購。AMD 如今與 Anthropic 的利益綁定，遠超一紙採購訂單的層次。

## 軟體合作：用 Claude 修復 ROCm

硬體面是新聞頭條，但工程合作在未來數年內可能是更具決定性的環節。AMD 與 Anthropic 啟動多年合作，以 Claude 加速 ROCm（AMD Radeon 開放計算軟體堆疊，支撐 AMD GPU 程式設計）的開發。

ROCm 長期是 AMD 對抗 CUDA 的競爭弱點。CUDA 已有二十年歷史，積累了龐大的生態系統：函式庫、框架、第三方工具，以及最關鍵的——數千位從 CUDA 優化起步學習的機器學習工程師的集體知識。ROCm 沒有這些遺產，靠傳統軟體工程縮短差距需要十年。

Claude 輔助的 ROCm 開發工作，目標是用 AI 壓縮這段時程——以人類工程團隊無法匹敵的速度生成優化程式碼、識別性能瓶頸、撰寫並除錯核心函式庫。與此同時，AMD 將在自身工程與產品開發流程中全面採用 Claude，為 Anthropic 提供一個高價值的企業部署場景，同時也是 Claude 的實戰壓力測試。

ROCm 在兩到三年內能否縮短多少相對 CUDA 的差距，仍充滿不確定性。但將其解讀為「AMD 已解決軟體問題」是誤讀。AMD 真正做到的，是為自己開闢了一條可信的縮差路徑——針對那個歷史上讓開發者卻步的核心痛點——這已足夠使其他前沿實驗室的未來 Instinct 部署變成一個可以認真討論的話題，而非紙上談兵。

## 分散 Anthropic 的算力供應鏈

對 Anthropic 而言，此次合作解決了一個多年來令投資者憂慮的結構性弱點：過度依賴 Google Cloud TPU。Google 同時是 Anthropic 最大投資人（在最近 Meta 交易之前便已進行多輪巨額承諾）、雲端服務商，以及透過 Google DeepMind 與 Gemini 模型家族對 Anthropic 形成日益直接競爭壓力的對手。

將 2 吉瓦算力分散至 AMD 基礎設施，讓 Anthropic 在與 Google Cloud 談判時有更多籌碼，提供了在 Google 對 TPU 存取設限情況下的替代部署路徑，並向企業客戶表明：Claude 的基礎設施並非完全捆綁於單一雲端廠商的商業利益之上。

此次合作未涉及任何主要超大規模雲端廠商，這同樣值得注意。Anthropic 正在與半導體公司建立直接關係，而非將算力採購完全通過雲端中間商路由——這一模式賦予 Anthropic 對長期基礎設施成本更強的掌控力。

## 對 Nvidia-AMD AI 晶片戰意味著什麼

從短期來看，這筆交易並不威脅 Nvidia 在 AI 訓練與推論 GPU 市場的主導地位。Nvidia 每季出貨數十萬片 Blackwell H200 和 B200；AMD 的裝機基礎相對較小。但此次合作改變了市場的二階動態，其影響將隨時間複利積累。

首先，Anthropic 的工作負載是現存最苛刻的之一。若 AMD 能成功在 Helios 硬體上大規模運行 Claude——在關鍵性能與可靠性指標上匹敵甚至接近 Nvidia——它將成為每一個不想被 Nvidia 定價鎖定的企業 AI 部署的參考架構。2 吉瓦的 Anthropic 部署，實際上是全球最大、最受矚目的 AMD 概念驗證。

其次，AMD 的股權持有為 Anthropic 創造了讓 Claude 在 ROCm 上良好運行的動機——意味著 Anthropic 工程師將提交錯誤報告、提出優化方案，並為 ROCm 生態系貢獻改進，使所有其他 AMD GPU 用戶受益。這種商業利益綁定所產生的軟體投入，是 Nvidia 客戶無法形成的等效激勵。

第三，此次合作恰逢 Nvidia 自身供應動態轉變之際。在 SK Hynix 加速 HBM4 產能、Nvidia Vera Rubin 平台要到 2027 年才出貨的背景下，存在一個窗口期——雖然窄小卻真實存在——企業 AI 買家正比以往任何周期都更認真地評估自己的選擇。AMD 帶著 2 吉瓦 Anthropic 背書，在這個窗口期進場，時機恰到好處。

問題的核心在於執行力。AMD 此前多次做出可信的承諾，卻一再延遲或低於規格交付。這筆合作是公司有史以來規模最大、能見度最高的 AI 基礎設施承諾。若 Helios 在 2027 年上半年首個吉瓦上線時如廣告所述般表現，2028 年的 AI 晶片版圖將與今日顯著不同。
