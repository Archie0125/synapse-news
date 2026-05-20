---
title: "英國新創 Fractile 募資 2.2 億美元，以記憶體內運算解決 AI 推論瓶頸"
summary: "總部位於倫敦的 Fractile 完成由 Accel、Factorial Funds 和 Founders Fund 領投的 B 輪融資，募資 2.2 億美元（約新台幣 72 億元），投後估值達 10 億美元。這家公司正在開發將記憶體與運算整合於單一晶片的推論加速器，目標是消除讓前沿 AI 模型執行緩慢且成本高昂的 DRAM 瓶頸。Anthropic 據報已在洽談成為早期客戶。"
category: "hardware"
publishedAt: 2026-05-20
lang: "zh"
featured: false
trending: true
sources:
  - name: "Tech.eu"
    url: "https://tech.eu/2026/05/13/uk-ai-chip-startup-fractile-raises-220m-to-tackle-the-growing-inference-bottleneck/"
  - name: "Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/fractile-raises-220m-to-accelerate-development-of-ai-inference-chips/"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-in-early-talks-to-buy-inference-chips-from-uk-startup-fractile"
  - name: "Fractile"
    url: "https://www.fractile.ai/news/fractile-raises-220m-to-build-the-next-generation-of-inference-hardware"
tags:
  - "Fractile"
  - "AI 晶片"
  - "推論加速"
  - "硬體"
  - "英國新創"
  - "半導體"
  - "B 輪融資"
  - "Anthropic"
relatedSlugs:
  - "2026-05-18-tsmc-n2-2nm-chip-ramp-ai-hardware-zh"
  - "2026-05-05-cerebras-ipo-40b-nasdaq-zh"
  - "2026-04-03-riscv-ai-accelerators-zh"
---

AI 產業的花費問題有兩張面孔。訓練新模型需要龐大的運算叢集和數月的 GPU 時間——這個成本佔據了大多數頭條。但**推論**（inference）——執行訓練好的模型以產生實際回應的過程——正快速成為更龐大、更持久的支出。每一次 ChatGPT 查詢、每一個 Gemini API 呼叫、每一段 Claude 對話——全都運行在推論基礎架構之上，而隨著使用量規模化，這個成本正在複利累積。

總部位於倫敦的 **Fractile** 完成了 **2.2 億美元**的 B 輪融資，正是為了解決這個問題。這輪於 2026 年 5 月 13 日宣佈的融資，由 Accel、Factorial Funds 和 Founders Fund 領投，Conviction、Felicis、8VC、Gigascale、O1A、Buckley Ventures、Kindred Capital、北約創新基金（NATO Innovation Fund）和牛津科學企業（Oxford Science Enterprises）跟投，投後估值達 **10 億美元**。

## Fractile 正在解決什麼技術問題

今日的 AI 推論硬體以 Nvidia GPU 為主導，這些 GPU 功能強大，但其架構設計源自另一個時代。它們依賴獨立的外部 DRAM（動態隨機存取記憶體）來儲存執行推論所需的模型權重與中間狀態。每當晶片需要存取一個權重——在 token 生成過程中這幾乎無時無刻都在發生——就必須透過高頻寬記憶體匯流排從 DRAM 取得資料。

這種處理器與記憶體之間的反覆往返，就是推論瓶頸所在。它消耗能源、引入延遲，並限制 token 的生成速度。隨著模型越來越大——前沿模型現在動輒超過數千億個參數——記憶體頻寬需求成比例增長，用高容量 DRAM 滿足這個需求的成本也隨之暴增。

Fractile 的方法是徹底消除這種分離。公司正在建構基於**記憶體內運算（in-memory compute）**的晶片：運算直接在記憶體內部發生，使用與處理邏輯整合在同一塊矽晶片上的 SRAM（靜態隨機存取記憶體）。資料不再需要在 GPU 和外部 DRAM 之間傳輸，而是留在原地，讓運算來找它。

「我們想要從根本上加速前沿模型的推論，」執行長 Walter Goodwin 在融資公告中表示，「記憶體牆是大規模經濟運行大型模型的根本制約，我們的架構就是為了移除它而設計的。」

## 創辦人背景

Fractile 由 **Walter Goodwin** 和 **Yuhang Song** 於 2022 年創立。擔任執行長的 Goodwin，在牛津大學機器人學研究所攻讀博士期間創辦了這家公司。牛津的淵源深植於 Fractile 的投資人名單：牛津科學企業在 B 輪中投資，Acorn Computers 和 Arm 前高管 **Stan Boland**——地球上幾乎每部行動裝置內部那個架構的主要設計者之一——也個人投資入股。Arm 共同創辦人 **Hermann Hauser** 同樣出現在股東名單上。

其他值得注意的個人投資者還包括：自動駕駛新創 Wayve（2024 年獲 Nvidia 和軟銀逾十億美元投資）的共同創辦人 **Amar Shah**，以及前英特爾執行長 **Pat Gelsinger**——他花了四年試圖重振英特爾製造業務後，於 2024 年底離職。

Gelsinger 和 Boland 的加入不只是象徵性的。這些工程師親手建造了好幾個世代的運算架構，對設計、製造並將能夠競爭既有龍頭的晶片推向市場所需的一切，有著骨子裡的了解。他們的投資，是對 Fractile 技術可行性的一種背書。

## 為什麼選擇 SRAM 而非 DRAM？

SRAM 在主動運算方面比 DRAM 更快、更節能——但它每位元的面積更大、成本更高。傳統觀點認為，在晶片上放置足夠多的 SRAM 來存放大型前沿模型的權重，在實際上是不可行的。Fractile 的賭注是：晶片密度的進步、積極的模型壓縮技術，以及在權重管理上的架構創新，能夠讓基於 SRAM 的推論不僅可行，而且在 AI 實驗室現在所需的推論規模上，在經濟效益上更具優越性。

Tom's Hardware 的一篇報導指出，**Anthropic** 已與 Fractile 展開初步洽談，希望在晶片量產後購買用於推論工作負載，Fractile 的目標是在 **2027 年**推出硬體產品。如果屬實，這將具有重大意義：Anthropic 的 Claude 3.5 系列模型是目前量產中運算需求最高的推論工作負載之一，Anthropic 的背書將表明 Fractile 的架構能夠在前沿規模下運作，而不只是在實驗室條件下。

## 競爭格局

Fractile 進入的市場，比兩年前更開放，也更擁擠。Nvidia 的推論主導地位依然龐大——其 H100 和 H200 晶片驅動著全球大部分的量產 AI 推論。但針對推論優化的晶片類別已吸引了大量新進入者：

- **Cerebras**：於 2026 年 5 月在那斯達克上市，採用晶圓級晶片架構實現極高的記憶體頻寬。
- **Groq**：專注推論的晶片公司，透過確定性 SIMD 架構追求極端的 token 生成速度。
- **Rebellions**（南韓）：於 2026 年 3 月完成 4 億美元融資，開發針對資料中心部署的 AI 推論晶片。
- **d-Matrix** 和 **Etched**：各自圍繞特定的 Transformer 推論優化假設建造矽晶片。

讓 Fractile 與眾不同的，正是其記憶體內運算架構本身。其他主要推論晶片新創中，沒有任何一家在追求相同的根本架構，這意味著 Fractile 下的是更難的賭注，但潛在回報也更大。如果基於 SRAM 的記憶體內運算能在前沿 AI 所需的規模下被證明經濟可行，Fractile 可能達到傳統架構——無論是 Nvidia 的，還是其他新創的——在結構上無法比擬的效能與能源效率優勢。

## 英國矽谷的策略意義

Fractile 的融資，是歐洲半導體新創更廣泛時刻的一部分。圍繞先進晶片供應的地緣政治緊張——美國對中國出口管制高端晶片、台積電先進產能集中在台灣，以及歐洲對依賴美國控制 AI 基礎架構日益增加的焦慮——已創造了投資人對主權和地理分散晶片研發的胃口。

Fractile 在倫敦、布里斯托、舊金山和台北設有辦公室，反映了其英國根基以及實際接觸台灣先進製程的必要性。北約創新基金的參與尤為值得注意：這是少數由軍事聯盟支持的創投基金之一，其對 AI 推論晶片公司的投資，反映出 AI 基礎架構現在被明確視為國家安全議題的認知。

公司正在四個地點大力招聘，尤其著重晶片設計工程師——儘管 AI 投資浪潮持續，這個人才庫在全球仍然稀缺。

## 邁向 2027 年的路

Fractile 的晶片尚未量產。公司公佈的時程目標是在 **2027 年**推出硬體，這意味著 B 輪融資的 2.2 億美元，是繼續研發、原型矽晶片流片成本，以及與晶圓代工夥伴合作將新穎晶片架構帶入可製造現實的漫長昂貴過程的彈藥。

到 2027 年，推論晶片市場的面貌將與今日大不相同。Nvidia 將推出新架構；當前多家推論新創將會各有成敗；隨著 AI 模型更深度整合進企業與消費者軟體，需求將持續成長。

不會改變的，是那個根本的物理定律：在獨立的記憶體與處理器晶片之間移動資料，代價是能源與時間。如果 Fractile 的記憶體內運算架構如設計所示運作，它將解決所有其他推論晶片——包括 Nvidia 的——都在對抗的那個制約。這種技術差異化，一旦被驗證，往往不只吸引投資，更吸引客戶。
