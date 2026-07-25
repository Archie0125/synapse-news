---
title: "Apple 將私有雲端運算擴展至 Google Cloud 與 Nvidia Blackwell——隱私承諾還成立嗎？"
summary: "Apple 宣布將私有雲端運算（PCC）基礎設施延伸至 Google Cloud，並採用具備保密運算功能的 Nvidia Blackwell GPU。此舉讓 Apple Intelligence 得以處理更高強度的 AI 工作負載，但也引發外界對於 Apple 隱私承諾能否在橫跨三大科技巨頭的架構中繼續成立的深刻質疑。"
category: "ai-ml"
publishedAt: 2026-07-25
lang: "zh"
featured: false
trending: false
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/08/apple-google-nvidia-ai-chips.html"
  - name: "Nvidia 官方部落格"
    url: "https://blogs.nvidia.com/blog/nvidia-confidential-computing-apple-private-cloud-compute/"
  - name: "Business Standard"
    url: "https://www.business-standard.com/technology/tech-news/apple-intelligence-siri-ai-google-nvidia-privacy-promise-private-cloud-compute-126061200846_1.html"
  - name: "Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/apples-private-cloud-compute-to-run-on-google-cloud/"
tags:
  - "Apple Intelligence"
  - "私有雲端運算"
  - "Google Cloud"
  - "Nvidia Blackwell"
  - "AI 隱私"
  - "保密運算"
relatedSlugs:
  - "2026-07-24-alphabet-q2-2026-earnings-cloud-gemini4-zh"
---

Apple 的品牌建立在隱私之上。在 AI 領域，這個品牌背後有具體的技術架構支撐：**私有雲端運算（Private Cloud Compute，PCC）**——Apple 的專有系統，透過無狀態運算、密碼學驗證與在 Apple 自建資料中心的實體隔離，讓需要上雲的 AI 任務仍能保護用戶隱私。

這套架構，剛剛變得複雜多了。

在 WWDC 2026 上，Apple 宣布將私有雲端運算擴展至 **Google Cloud**，並採用具備保密運算功能的 **Nvidia Blackwell GPU**。此舉讓 Apple Intelligence 得以處理更高強度的工作負載，包括複雜推理、長文脈絡分析及代理式（agentic）工具使用——這些任務已超出 Apple 自有伺服器基礎設施的處理上限。

這項公告在隱私研究人員、資安工程師與 Apple 用戶社群中引發激烈討論。爭議核心只有一個問題：Apple 的隱私承諾，在橫跨三家公司的基礎設施堆疊中，還能成立嗎？

## 擴展後的架構如何運作

Apple 原本的 PCC 設計完全運行於 Apple Silicon 伺服器和 Apple 自建資料中心，信任模型圍繞 Apple 自家硬體與軟體而建構。新架構加入了第三方層，但試圖維持原有的安全保證。

Google Cloud 端的實作採用**三層硬體信任堆疊**：

1. **Nvidia Blackwell GPU** 搭載保密運算（Confidential Computing）——GPU 記憶體加密，確保連 Nvidia 或 Google 的主機系統都無法讀取運算中的資料
2. **Intel CPU** 搭載信任域擴展（TDX）——為伺服器 CPU 環境提供硬體級隔離
3. **Google Titan 安全晶片**——用於驗證，提供密碼學證明確保硬體上執行的軟體符合 Apple 規格

Apple 表示，Google Cloud 端的部署維持了其為自有基礎設施所訂定的五項 PCC 要求：
- **無狀態運算**：用戶資料在運算後立即丟棄，從不儲存
- **可執行保證**：隱私屬性由硬體強制執行，非僅靠政策宣示
- **無特權執行時存取**：包括 Google 在內的營運者，無法存取用戶資料或推論結果
- **不可針對性**：系統無法被指定針對特定用戶進行監控
- **可驗證透明度**：Apple 公開在 PCC 伺服器上運行的軟體映像，供獨立審查

「Google Cloud 端的實作維持了我們為自有硬體所確立的相同 PCC 要求，」Apple 發言人表示，「隱私模型由硬體強制執行，而非依賴 Google 的政策或合約承諾。」

## 重構一切的一月聯盟

PCC 擴展至 Google Cloud 並非孤立事件。2026 年 1 月，Apple 與 Google 宣布**多年期 AI 合作**，下一代 Apple Foundation Model——即驅動 Apple Intelligence 的 AI 系統——將以 Google 的 Gemini 模型技術與雲端基礎設施為基礎共同研發。

那項公告本身意義重大，但完整的技術圖像直到 WWDC 才浮現：Apple 正實質上將其最高強度 AI 任務的推論基礎設施外包給 Google，同時以 Nvidia Blackwell 硬體作為兩家公司之間的隱私邊界。

Apple 與 Google 在 AI 領域的聯手，在競爭背景下顯得格外引人注目。Apple 長期以「隱私替代方案」自居，對抗 Google 以資料為核心的商業模式。Gemini 合作——以及現在 PCC on Google Cloud 的部署——並未消除這一定位，但確實讓 Apple 多年精心建立的清晰敘事變得更為複雜。

## 資安研究者怎麼說

安全研究人員與隱私倡議者對架構是否足夠安全看法分歧。

認為架構可信的一方指出，Nvidia 的保密運算是真實的技術控制，而非單純的合約承諾。在保密運算模型下，載入 GPU 記憶體的資料以金鑰加密，金鑰的存取範圍限縮在運算本身之內，Google 系統管理員與 Nvidia 工程師均無法觸及。Titan 驗證晶片提供獨立確認，確保軟體環境符合 Apple 的公開規格。

「這與單純跑在 Google Cloud 上有本質上的差異，」一位審閱過 Apple PCC 技術文件的資安工程師說，「保密運算堆疊讓 Google 從技術上無法觀察推論結果，而不僅是合約禁止。」

批評者則認為信任鏈已拉得過長。Apple 最初的 PCC 架構只涉及一家公司的硬體與軟體，信任鏈相對短暫。新堆疊卻需要同時信任 Apple 軟體、Nvidia 保密運算實作、Intel TDX、Google Titan 驗證，以及 Google 的網路路由——五個獨立信任關係，每一個都是潛在攻擊面。

「隱私保證只有最薄弱的環節那麼強，」一位要求匿名的知名學術安全實驗室研究員說，「搭載 Apple Silicon 的 PCC 只需要信任一家廠商；現在變成四家。」

Apple 也承認，Google Cloud 端的實作目前處於「夏季預覽期」，正在「逐步完善整套保護機制」，但未說明哪些保護尚未就位。

## Apple 為什麼需要 Google 的基礎設施

促成這次擴展的實際驅動力是算力容量。Apple Intelligence 的採用速度遠超出 Apple 自建伺服器基礎設施的承載上限，尤其是 Apple Intelligence 2.0 引入的高算力密集任務：延伸推理、跨裝置代理工作流程，以及複雜的多模態分析。

Apple Silicon 伺服器的製造與部署成本高昂；而儘管 Nvidia Blackwell GPU 本身亦有供貨壓力，其可用規模仍遠超 Apple 自有晶片在同等時間框架內的產能上限。

與 Google 長達三年的合作，反映了 Apple 的長期策略：將 Apple Intelligence 最高強度工作負載的推論基礎設施與 Gemini 模型能力交由 Google 處理，同時維持敏感且時延敏感任務的端側處理模式。

## 競爭格局的諷刺之處

這個安排創造了一個引人深思的競爭態勢。Apple、Google、Nvidia 多年來在行動作業系統、雲端服務、AI 硬體與 AI 模型多個維度上激烈競爭。而 PCC on Google Cloud 的部署，卻要求三家公司在共同的技術與法律框架上取得一致。

Nvidia 的位置尤其耐人尋味。Nvidia Blackwell GPU 同時為 Google 自家 Gemini 推論工作負載、Apple 的私有雲端運算，以及 Microsoft Azure 的 AI 基礎設施提供動力——成為橫跨競爭 AI 生態系的硬體層中立方。

對 Google 而言，Apple 合約是雲端收入的重要來源，也是 Google Cloud 企業安全能力的有力背書。對其他有嚴格資料保護要求的企業客戶而言，「連 Apple 都信任這套基礎設施處理最敏感的 AI 工作負載」，將成為 Google Cloud 最有說服力的銷售論點之一。

## 用戶需要知道什麼

對 Apple Intelligence 用戶而言，實際影響取決於哪些任務會觸發 Google Cloud 後端。Apple 表示，簡單的端側任務——文字摘要、照片編輯、本地搜尋——繼續完全在裝置上執行；只有超出端側容量的任務才會呼叫 Google Cloud 基礎設施。

Apple 表示用戶可透過 Apple Intelligence 設定中的「隱私透明度」指示器，確認目前使用的是哪一層處理，此功能延續自原始 PCC 設計。公司也已將在 Google Cloud PCC 伺服器上運行的軟體映像發布至公開的透明度日誌，供獨立安全研究人員驗證。

這樣的透明度水準，是否足以維繫用戶信任——在 Apple 的 AI 工作負載史上首次落於另一家公司實體基礎設施上的架構中——是接下來幾個月隱私辯論必然持續審視的問題。
