---
title: "Cloudflare 推出「按次付費爬取」機制，為 AI 與開放網路建立全新經濟層"
summary: "Cloudflare 7 月初推出 AI 爬蟲控制與按次付費爬取（Pay Per Crawl）功能，讓網站主除封鎖或放行 AI 爬蟲之外，終於有了第三個選項：向爬蟲收費。這項功能重塑了內容發布者與 AI 訓練管線之間的關係，可能為 AI 代理人網路催生全新的微支付基礎設施。"
category: "developer-tools"
publishedAt: 2026-07-10
lang: "zh"
featured: false
trending: true
sources:
  - name: "Cloudflare Blog"
    url: "https://blog.cloudflare.com/introducing-pay-per-crawl/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/"
  - name: "Forbes"
    url: "https://www.forbes.com/sites/sandycarter/2026/07/01/cloudflare-moves-to-make-ai-pay-for-the-content-it-consumes/"
  - name: "Cloudflare Blog"
    url: "https://blog.cloudflare.com/content-independence-day-ai-options/"
tags:
  - "Cloudflare"
  - "AI爬蟲"
  - "內容變現"
  - "開發者工具"
  - "AI政策"
  - "網頁爬取"
  - "出版業"
relatedSlugs:
  - "2026-07-09-illinois-sb315-ai-safety-audit-law-zh"
  - "2026-07-04-white-house-voluntary-ai-release-standards-zh"
  - "2026-04-04-mcp-protocol-explosion-zh"
---

開放網路的設計從未將人工智慧納入考量。當 Tim Berners-Lee 發明超連結，當 Google 建立爬取與索引帝國，當出版商透過廣告和訂閱將流量變現，這些商業模式都沒有預見到：有一天，自動化代理人每日將數十億次消耗內容，卻永遠不會成為讀者、訂閱者，或任何一個廣告曝光。

那個未來還是來了——7 月初，Cloudflare 採取行動，開始為它定價。

## 第三個選項

Cloudflare 負責全球約兩成網站的流量管理與安全防護，7 月初宣布推出兩項相互關聯的功能：AI 爬蟲控制（AI Crawl Control）和按次付費爬取（Pay Per Crawl），並向所有方案（包含免費版）的 Cloudflare 客戶開放。

在此之前，面對 AI 爬蟲，網站主只有兩種選擇：放行或封鎖。隨著發布者越來越不滿 AI 公司免費採集他們的心血來訓練商業模型，封鎖越來越普遍。而放行不僅無法獲得補償，連內容將如何被使用都毫無透明度。

Pay Per Crawl 推出了第三個選項：收費。發布者現在可以在 Cloudflare 控制台中設定，要求 AI 爬蟲以每次請求的統一費率付費。Cloudflare 扮演主要收款方（Merchant of Record）的角色，處理技術基礎設施、清算結算，以及數千家出版商與少數大型 AI 公司之間的金融關係摩擦。

AI 爬蟲控制則讓發布者能按爬蟲意圖分類管理：搜尋型（為探索建立索引）、代理人型（AI 助理用內容回答查詢）和訓練型（為模型開發採集資料），並對各類型套用不同政策。預設情況下，在 Cloudflare 上架的新網域，訓練型和代理人型爬蟲將在廣告支援頁面上被封鎖，搜尋型爬蟲則維持開放。

## 協議如何運作

技術實作巧妙地建立在現有網路標準之上。當 AI 爬蟲請求使用 Pay Per Crawl 的網站內容時，它會收到兩種回應之一：如果爬蟲提供有效的付款標頭，則回傳標準 HTTP 200；否則收到帶有 `crawler-price` 標頭的 HTTP 402 Payment Required 回應，其中嵌入了定價資訊。

402 狀態碼自 1996 年就存在於 HTTP 規範中，作為未來支付系統的預留位置。Cloudflare 現在讓它在規模化場景中真正運作了。

爬蟲可以以兩種模式運行。被動模式（Reactive）是爬蟲撞上付費牆後才發現定價，收到 402 後再帶付款確認重試。主動模式（Proactive）是設計良好的爬蟲在初始請求中就帶上 `crawler-max-price` 標頭，表示「我願意為每頁支付最多 X 分錢」，若網站設定的費率在預算之內，則立即獲得存取許可，無需重試。

為了防止偽冒並確保聲稱是合法 AI 代理人的爬蟲確實名符其實，系統採用 Web Bot Auth 和 HTTP Message Signatures。爬蟲必須在 Cloudflare 註冊、提供 Ed25519 密碼學金鑰對，並在每次請求中附上簽章標頭。偽裝成 GPT-Agent 的假爬蟲無法在沒有已註冊私鑰的情況下偽造簽章。

## 超越爬取：按使用付費

初次推出明確定位為第一步。Cloudflare 已宣布 Pay Per Crawl 將演進為「按使用付費」（Pay Per Use）——一種更精細的模型，不僅在 AI 公司抓取內容時收費，而是在內容真正創造價值時收費。

這個區別對發布者而言意義重大。在 Pay Per Crawl 模式下，每當 AI 爬取一頁就能帶來收益——但該頁內容可能被快取、與數千個其他來源合併，或以貢獻完全不透明的方式被使用。在 Pay Per Use 模式下，發布者理論上可以在他們的文章出現在 AI 生成的回答中、代理人為特定任務購買資訊，或推薦系統將其內容推送給終端用戶時獲得收益。

Cloudflare 描述了企業客戶可設定的三個內容使用層級：即時（Immediate，不儲存、不再使用——AI 看過即忘）、引用（Reference，允許索引、摘錄和回連結）和完整（Full，允許摘要和再現）。這為網路規模的內容授權奠定了基礎。

## 它所解決的結構性問題

這次發布的背景是網路經濟中醞釀已久的危機。從地方報紙到維基百科到個人部落格，各類發布者眼睜睜看著 AI 公司吸走他們多年的心血，用來打造商業產品，再與他們爭奪用戶注意力。曾經從搜尋引擎獲得大量推薦流量的新聞網站，因為 AI 助理直接回答問題、消除了點擊需求，流量持續下滑。

法律局面動盪不安。《紐約時報》起訴了 OpenAI 和微軟，數十家小型發布者也提出了索賠。部分 AI 公司達成了協議——OpenAI 與美聯社、Google 與路透社——但這些協議只涵蓋了內容宇宙的極小部分。大多數發布者處於法律灰色地帶：不清楚 AI 訓練是否構成合理使用，無法大規模執行任何主張，即便法律明確也沒有技術機制要求付費。

Cloudflare 的網路位置改變了這個算式。由於眾多網站都在 Cloudflare 後面，一個想要廣泛存取網路的爬蟲根本無法忽視它的政策。如果 Cloudflare 在網路層強制執行認證和付費，AI 爬蟲就必須參與——否則面臨大規模拒絕存取。

## 對 AI 公司的影響

主要 AI 開發商正密切關注此事。OpenAI、Google、Anthropic 等投入了大量資源建構爬取基礎設施，以採集訓練資料並提供即時代理人查詢服務。爬取成本歷來接近於零——只有頻寬和伺服器時間，別無其他。如果大量網站轉向 Pay Per Crawl 定價，訓練資料採集和即時內容擷取的經濟學將發生根本性變化。

對於打造代理人系統的新創公司——即代替用戶瀏覽網路、完成任務的 AI——這是更直接的挑戰。每次查詢讀取數十個飯店和航班頁面的 AI 旅遊代理人、摘要主題前擷取 50 篇新聞文章的研究助理、任務中途查閱技術文件的程式碼代理人：所有這些都會產生每次存取可能附帶費用的爬取請求。這些成本如何吸收——由 AI 公司承擔、轉嫁給用戶、或透過整批授權協商解決——目前仍是未知數。

Cloudflare 與 Pay Per Crawl 同期宣布的貨幣化閘道（Monetization Gateway）將這個邏輯延伸得更遠：Cloudflare 後面的任何資源都有可能透過 x402 微支付協議進行計量，不只是網頁內容，還包括 API、資料饋送和計算服務。

## 網路的新預設值

Cloudflare 打造的不只是一個產品功能——它是一個對 AI 與開放網路關係的新預設值提案。舊模型是：內容公開、爬取免費、變現透過廣告和人類讀者的訂閱實現。Cloudflare 設想的新模型是：內容可用但計量，爬蟲按存取次數或價值付費，Cloudflare 坐在中間充當結算層。

這是否真正成為網路規範，取決於有多少發布者設定定價、AI 公司如何回應，以及競爭的基礎設施供應商是否建立相容系統。Cloudflare 掌控著大量網站的基礎設施，但並非全部。

可以確定的是：AI 與發布者之間的經濟關係，再也無法被默認為免費。Cloudflare 剛剛讓收費——首次以網路規模——成為可能。

---

*Cloudflare 的 Pay Per Crawl 目前處於私測階段，隨著系統成熟，全面開放可望逐步推進。*
