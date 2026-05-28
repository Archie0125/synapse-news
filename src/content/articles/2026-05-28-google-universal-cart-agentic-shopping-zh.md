---
title: "Google 推出萬能購物車：跨 Search、Gmail、YouTube、Gemini 的代理式電商新戰場"
summary: "Google 正式推出 Universal Cart（萬能購物車），這個跨零售商的 AI 購物中心讓用戶能在任何 Google 介面加入商品，由 Gemini 主動監控價格、找尋優惠並透過新的代理付款協議完成購買。今夏首先在美國上線，合作品牌包括 Nike、沃爾瑪、Sephora、Target 和多個 Shopify 商家。"
category: "products"
publishedAt: 2026-05-28
lang: "zh"
featured: false
trending: false
sources:
  - name: "Google Blog"
    url: "https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/19/googles-new-universal-cart-wants-to-follow-your-entire-shopping-journey-across-the-internet/"
  - name: "Retail Dive"
    url: "https://www.retaildive.com/news/google-launches-cross-retailer-universal-cart/820957/"
tags:
  - "google"
  - "ai購物"
  - "電商"
  - "gemini"
  - "代理式商務"
relatedSlugs:
  - "2026-05-28-microsoft-cancels-claude-code-licenses-copilot-cli-zh"
  - "2026-05-24-google-gemini-35-flash-agentic-model-zh"
  - "2026-05-20-google-gemini-spark-personal-ai-agent-zh"
---

Google 在 5 月 19 日的 I/O 2026 發布了 Universal Cart（萬能購物車），這款產品正在今夏陸續向美國用戶推出。它是一個由 AI 驅動的跨零售商購物車，能跟著你跨越所有 Google 介面，主動替你尋找更好的價格、提示缺貨商品重新上架、並代為完成購買。這是 Google 自 2020 年取消 Google Shopping 手續費以來，在電商領域最重要的一步，同時也是直接挑戰亞馬遜作為消費者購物搜尋預設起點的地位。

Universal Cart 跨 Google Search、Gemini 應用程式、YouTube 和 Gmail 運作。當你在任何地方看到想要的商品——搜尋結果、YouTube 評測、促銷郵件——就可以加入購物車。接下來由購物車替你做你原本要手動做的事：監控歷史價格、在降價時發通知、在補貨時提醒你，並可透過 Google Pay 完成結帳，或轉跳到商家自己的結帳流程。

## 運作機制

Universal Cart 的技術架構由三個相互扣合的元件構成：購物車介面本身、作為智慧層的 Gemini，以及規範代理交易授權與執行方式的「代理付款協議」（Agent Payments Protocol，AP2）。

購物車介面跨所有 Google 產品持久存在。無論你在行動版 Search、桌面版 Gemini 還是觀看 YouTube，加入購物車的商品都會保留。商品可以透過商家整合的「加入購物車」按鈕加入、透過對話式提示（「把這個加進我的購物車」）加入，也可以在符合條件的商家中，由 Gemini 從你正在瀏覽的視覺或文字內容中自動識別並加入。

Gemini 作為主動的智慧層，不只是儲存商品，而是持續「監視」它們。價格下降時觸發通知；歷史價格資料一目了然，讓你能判斷「限時特賣」是否名副其實；多組件商品的相容性自動檢查——如果你在組裝電腦，Gemini 會提醒你新加的顯卡是否與購物車裡的主機板不相容。

AP2 是技術上最具意義的新元件。它是 Google 授權 AI 代理代表用戶進行金融交易的標準協議。用戶事先設定消費上限、指定商家範圍和特定商品條件，代理只有在所有條件都滿足時，才能執行購買。商家全程保持商家記錄身份——Google 提供交易基礎設施，本身不承擔金融或庫存風險。

## 參與品牌

首波美國上線品牌覆蓋了消費者支出的重要版圖：Nike、Sephora、Target、Ulta Beauty、沃爾瑪、Wayfair，以及 Fenty Beauty 和 Steve Madden 等 Shopify 商家。Shopify 的整合尤為重要——Shopify 約佔美國電商總量的 15%，Universal Cart 整合意味著數十萬家商家無需自行開發，即可自動獲得代理式結帳功能。

Google 特意強調「商家保持商家記錄身份」的模式，這有助於緩解外界長期擔憂的問題：Google 是否正在把自己打造成與它轉介流量的零售商直接競爭的市場平台。AP2 的設計透過讓支付流程透明化、保留品牌對結帳環節的控制權，來解決這個矛盾。

## 這與 Google 過去電商嘗試有何不同

Google 不是第一次嘗試進軍電商。2012 年推出 Google 購物廣告，2019 年推出 Google Shopping Actions，2020 年推出免費商品列表。每一版都擴大了 Google 在商務領域的涉足範圍，但都沒有從根本上改變用戶行為，因為沒有一個改變了用戶真正開始購物旅程的起點。

Universal Cart 是一個不同類別的產品，因為它的目標不是截獲「主動搜尋購物」的意圖，而是捕捉「被動式購物」——邊看邊瀏覽、邊讀邊滑的模式，這種模式貢獻了大量的商品發現，但一直缺乏良好的持久儲存機制。

如果有人在 YouTube 看跑鞋評測時順手加入 Universal Cart，三天後收到降價通知，兩下點擊完成購買——他們從未在亞馬遜開始一個新的購物流程。這個從發現到購買的完整旅程，始終在 Google 的生態系中完成。這正是 Google 想要工程化實現的行為改變。

## 亞馬遜的問題

亞馬遜在商品搜尋中的市場地位，是 Universal Cart 一切設計的隱形背景。美國調查數據持續顯示，約 60% 的線上購物者選擇從亞馬遜而非 Google 開始商品搜尋——這是自 2010 年代初 Google 還是主要商品發現引擎以來的重大轉變。亞馬遜透過物流基礎設施、Prime 會員制和賣家關係，建立了極難撼動的預設習慣。

Universal Cart 不是正面攻擊這個預設行為，而是試圖讓它變得無關緊要——在購買意圖還未有機會前往亞馬遜之前，就將其捕獲在 Google 的生態系內。如果商品已經在看 YouTube 影片或讀 Gmail 郵件的過程中加入了 Google 購物車，要不要去亞馬遜搜尋的問題根本就不會出現。

關鍵在於 AP2 和代理媒介的購買流程是否足夠順暢。Google Pay 的結帳成功率，以及商家整合的品質，將決定 Universal Cart 究竟能成為亞馬遜一鍵購物的真實行為替代方案，還是又一個被加入購物車後在結帳前放棄的功能。

## 品牌商家需要知道的事

對零售品牌和數位行銷團隊而言，Universal Cart 既是機會也是責任。機會在於：商品的發現和購買可以在 YouTube 內容、Gmail 促銷郵件和 Gemini 對話中直接完成，不需要用戶切換到獨立的購物流程。責任在於：品牌需要整合「通用商業協議」（Universal Commerce Protocol，UCP）——Google 面向商家的 API——確保商品在購物車搜尋結果中正確呈現，提供準確的歷史價格資料，並啟用順暢的 AP2 結帳。

深度整合 UCP 的品牌，將在 Universal Cart 的商品展示上獲得結構性優勢——類似亞馬遜 Prime 資格對黃金購物車的影響。未整合的品牌雖然仍可被發現，但會失去原生結帳體驗，用戶將被轉到品牌自己的結帳頁面，而非在 Google 生態系內完成。

Google 設定今夏為零售品牌的關鍵整合視窗。現在就針對 Universal Cart 進行優化的商家，正在為「返校季」和「假日購物季」做準備——那才是代理式商務是否成為主流消費者行為的真實考驗。
