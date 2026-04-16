---
title: "Google 與 Intel 擴大多年期 AI 晶片合作：Xeon 6 加客製 IPU 搶攻資料中心"
summary: "Google 與 Intel 於 4 月 9 日宣布擴大多年期合作協議，Google Cloud 承諾採用多代 Intel Xeon 6 處理器執行 AI 工作負載，同時深化雙方自 2022 年起共同開發的客製基礎架構處理單元（IPU）。這項協議讓 Intel 在長期由 Nvidia 主導的資料中心市場取得重要立足點，也預示著 CPU 在 AI 基礎架構中的地位正悄然回歸。"
category: "hardware"
publishedAt: 2026-04-11T09:05:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/09/google-expands-partnership-with-intel-for-ai-chips-.html"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/04/09/intel-inks-multiyear-data-center-chip-partnership-google/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-04-09/intel-wins-google-commitment-to-use-xeon-chips-in-data-centers"
  - name: "The Register"
    url: "https://www.theregister.com/2026/04/09/google_intel_ipu/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/09/google-and-intel-deepen-ai-infrastructure-partnership/"
tags:
  - "Intel"
  - "Google"
  - "Xeon"
  - "IPU"
  - "AI 晶片"
  - "資料中心"
  - "硬體"
  - "雲端基礎架構"
relatedSlugs:
  - "2026-04-07-nvidia-vera-rubin-nvl72-production-zh"
  - "2026-04-04-amd-mi300x-enterprise-zh"
  - "2026-04-10-tsmc-q1-2026-record-revenue-zh"
---

過去將近三年，Intel 一直試圖說服 AI 產業：GPU 不是唯一的答案。4 月 9 日，這家晶片巨頭終於拿到了迄今最有份量的背書——與 Google Cloud 公開宣布擴大多年期合作，讓 Alphabet 旗下的雲端部門承諾採用多代 Intel Xeon 處理器執行 AI 推論與通用運算，同時深化雙方自 2022 年便在悄悄共同開發的客製基礎架構處理單元（IPU）。

消息一出，Intel 股價當天應聲上漲。在歷經一段痛苦的組織重整、裁員與領導層更迭之後，這份合作公告難得地向市場傳遞了一個清晰訊號：全球最精於挑選硬體的雲端業者之一，選擇長期押注 Intel 的矽晶片路線圖。

## 兩根支柱：Xeon 與客製 IPU

這次合作涵蓋兩個方向不同、各自針對 AI 資料中心架構不同層次的面向。

**第一根支柱：Intel Xeon 6 處理器。** Google Cloud 將持續在基礎設施中部署 Xeon 系列，並引進最新的 Xeon 6 晶片，用於 AI 推論工作負載、訓練輔助運算以及通用雲端服務。這一點之所以重要，在於現代 AI 系統——尤其是大規模推論服務、檢索增強生成（RAG）以及代理式工作負載——都需要 CPU 端的處理能力，其擴展方式在經濟性和架構上都與 GPU 計算截然不同。隨著 AI 工作負載逐漸從訓練密集型轉向推論密集型，CPU 在資料中心扮演的角色也悄然回升。

**第二根支柱：客製 IPU 的共同研發。** Intel 與 Google 自 2022 年起便聯合開發 IPU 硬體，但最新協議擴大了合作範疇，也延長了路線圖承諾。IPU（基礎架構處理單元）是一種針對基礎架構管理任務設計的特殊應用晶片（ASIC），專門處理網路流量加解密、儲存裝置協調、虛擬機器管理程序控制等工作——這些任務過去全由主要 CPU 承擔，嚴重占用其能處理用戶工作負載的計算容量。將這些開銷卸載至專用 IPU，讓執行 Google AI 服務的伺服器得以釋出可觀的計算容量，用於真正的智慧運算層。

根據《The Register》的報導，Google 在 IPU 計畫中的參與程度，已延伸至對未來晶片設計規格的實質影響力——這已超越一般客戶關係，更像是 Google 以共同架構師的身份參與 Intel 基礎架構矽晶片的設計。

## 對 Intel 的戰略意義

這份公告的時機，對 Intel 作為一家企業的意義，不亞於合作本身的策略價值。在 2025 年初接任執行長的 Lip-Bu Tan 領導下，Intel 正在執行一套更清晰的策略：聚焦核心 CPU 與客製矽晶片優勢、縮減製造業務的過度擴張、重建超大規模客戶的信任。Google 這份合約，是迄今最明確的公開訊號，證明這套策略正在獲得業界最挑剔的採購方的認可。

Intel Xeon 6 架構在每瓦效能上較前代有顯著提升，讓它在過去被認為不適合 CPU 的工作負載中也具備競爭力。更重要的是，Xeon 6 在推論管線中的高密度部署表現——在延遲和每次查詢成本比訓練峰值吞吐量更為關鍵的場景下——使得 CPU 推論在特定工作負載上再度具有經濟吸引力。

Intel 也需要在純 GPU 加速器市場以外取得突破，而那個市場至今仍是 Nvidia 以驚人利潤率主導。與其正面強攻 Nvidia H100 和 Blackwell 系列短期內難以撼動的 AI 訓練霸主地位，不如在互補的 CPU 與網路基礎架構層建立競爭優勢——這個策略或許更具防禦性。Google 的承諾驗證了 Intel 的戰略方向是正確的。

## CPU 在 AI 時代的悄然回歸

更宏觀的視角是：整個 AI 產業一直對這個趨勢反應遲緩——隨著 AI 部署從實驗走向量產，工作負載組合的轉變方式，其實有利於異質運算，而非單純的 GPU 叢集。早期 AI 基礎設施由訓練運算主導，那是 GPU 無與倫比的強項。但推論服務才是如今經濟上佔主導地位的 AI 運作模式，它具有截然不同的特性：大量的小型、對延遲敏感的請求，以及用於資料檢索、上下文組裝和路由決策的 CPU 端處理。

包括 AWS、Microsoft Azure，以及現在明確公開表態的 Google Cloud 在內，多家大型雲端業者都已將 CPU 定位為 AI 基礎架構的一等公民，而非等待被淘汰的傳統元件。Intel Xeon 6 被定位為在 CPU 端高效處理 AI 工作負載、同時由客製 IPU 承擔基礎架構開銷的組合，正好契合了這種架構趨勢。

Bernstein 的分析師指出，Google 的合作夥伴關係「有效降低了 Intel 資料中心業務收入至少到 2028 年的不確定性」，提供了公司過去幾個季度所欠缺的能見度。這份合作並不保證 Intel 更廣泛的整體復甦——公司在晶圓代工服務和客製矽晶片領域仍面臨來自台積電和 AMD 的嚴峻競爭——但它有力地說明：Intel 的 CPU 事業，若能保持精準聚焦，在 AI 資料中心生態系中仍具有持久的立足之地。

## Google 的算盤

對 Google 而言，這次合作是一項刻意為之的分散風險策略。雖然 Google Cloud 已大量部署 Nvidia 硬體，並將持續提供 TPU 和 GPU 選項，但維持與 Intel 的深度合作關係，提供了架構上的靈活性和採購談判上的議價籌碼。客製 IPU 尤其代表了在超大規模下能夠持續複利的基礎設施成本節約：網路、儲存和安全管理開銷的每一個效率提升，都直接轉化為更多可用於計費 AI 運算的伺服器容量。

這次合作也推進了 Google 對大規模部署矽晶片施加設計影響力的更大版圖。Google 已自行設計張量處理單元（TPU）、客製 Axion ARM 架構 CPU，並參與客製網路 ASIC 的設計。與 Intel 共同開發 IPU，將這種設計影響力延伸至基礎架構矽晶片層，讓 Google 在日益由軟硬體緊密協同定義的資料中心架構中，多了一個客製硬體籌碼。

對於關注這項公告的業界人士，訊息已然清晰：GPU 或許是 AI 淘金熱的明星，但讓 GPU 在規模化環境中真正發揮效用的周邊基礎設施——CPU、IPU 和網路晶片——才是下一波硬體差異化競爭的主戰場。Intel 在這個層次找到了自己的位置，並剛剛讓最重要的客戶之一簽下了長期承諾。
