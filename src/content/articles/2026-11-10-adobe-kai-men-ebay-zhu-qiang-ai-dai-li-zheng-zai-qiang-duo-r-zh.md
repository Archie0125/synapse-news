---
category: products
featured: true
lang: zh
publishedAt: '2026-11-10T18:48:38.118522+00:00'
relatedSlugs: []
sources:
- name: Google AI Blog
  url: https://blog.google/company-news/inside-google/company-announcements/adobe-google-partnership-integration/
- name: The Verge
  url: https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping
- name: Engadget
  url: https://www.engadget.com/2312215/adobe-and-google-have-teamed-up-to-connect-drive-gmail-and-acrobat/
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/
- name: 9to5Google
  url: https://9to5google.com/2026/11/09/google-antigravity-knowledge-work/
summary: 你以後不會再打開 App，而是叫 AI 代理去打開。誰願意被代理呼叫，誰在封鎖代理，正在決定下一個十年的平台霸主。
tags: []
title: Adobe 開門、eBay 築牆：AI 代理正在搶奪軟體世界的「入口權」
trending: true
type: analysis
---

同一個禮拜，兩家公司對同一個問題給出完全相反的答案。

11 月 10 日 Adobe 在邁阿密的 MAX 大會上推出本機版 MCP（Model Context Protocol）伺服器，讓 ChatGPT、Claude、Gemini 可以直接操控 Photoshop、Illustrator、After Effects 和 Premiere。Adobe 副總裁 Deepa Subramaniam 對 TechCrunch 說，他們「沒有任何需要或意願」去限制 MCP 能開放哪些功能。

差不多同一時間，eBay 悄悄擋掉了 Meta 的 Muse 代理，讓它讀不到商品頁。

一個為 AI 代理開門，一個築牆。兩家都覺得自己在保護未來，但只有一家押對，而且多數人可能會猜錯是哪一家。

## 入口又要換手了

如果你在台灣科技圈待得夠久，應該經歷過好幾次入口轉移。從 PC 上的 Yahoo 奇摩入口網站換到 Google 搜尋，再換到手機上的 App Store 和 LINE。每次換手，掌握新入口的人就能抽成。Apple 和 Google 抽了應用程式營收的 30%，LINE 靠官方帳號和廣告把台灣的商家通路吃了一大塊。

現在正在發生的是從 App 到 AI 代理。這週的新聞可以拼出完整的樣子：

- **Adobe** 直接長進 Gmail 和 Google 雲端硬碟，檔案預覽裡多了「用 Acrobat 編輯」的按鈕。它的 CX Enterprise Coworker 代理進駐 Gemini Enterprise，創意工具也會出現在 Google 搜尋的 AI Mode 裡。
- **Google Antigravity** 原本是寫程式用的代理，現在加了「Knowledge Work」模式。原因是 Google 內部每週有好幾萬名非工程師在用它，橫跨業務、財務、法務、行銷。最值得注意的設計是：MCP 伺服器、技能、自訂代理都還在背景運作，只是介面上看不到了。
- **OpenAI** 持續把代理塞進 ChatGPT 的企業方案，讓對話框成為工作的起點，而不只是拿來問問題的地方。

把這三件事放在一起看，重點很清楚：**App 正在變成後端。**使用者對代理說一句話，代理去呼叫 Adobe、試算表或某個電商。你過去會主動點開的品牌，變成一個你根本看不到的函式呼叫。

## Adobe 為什麼甘願當水管

表面上看，Adobe 像是在投降。但細節值得看清楚：這個 MCP 是**本機版**，跑在你自己的電腦上，控制的是你已經付費訂閱的 Creative Cloud。Claude 使用者想用 Photoshop 的生成式重新打光，還是得先買一個 Photoshop 授權。

所以這不是送東西給別人，而是在**留住訂閱**。如果設計師的工作流程搬進對話框，Adobe 要確保代理第一個呼叫的是 Photoshop，而不是某個免費開源模型。這個方向其實早就看得出來：Adobe 的 App 裡已經整合了 Google、OpenAI、Runway、ElevenLabs、Black Forest Labs、可靈、字節跳動的模型，今年 6 月還買下 Topaz Labs。Adobe 已經不再主張「我的模型最強」，改成主張「每個模型都在我的工作台上用」。

和 Google 的合作則是各取所需。Adobe 拿到 Gmail 和雲端硬碟這個巨大入口，裡面躺著數不清的 PDF。Google 則讓 Gemini 多了一個重量級的創意品牌，用來對抗 Microsoft 的 Copilot 加 Office 組合，以及 OpenAI 往企業市場的擴張。這是兩家都怕被邊緣化的公司結成的同盟。

## eBay 為什麼築牆

eBay 的理由同樣清楚。今年 1 月它修改了使用者條款，禁止「代買代理」和「未經人工確認就下單的 LLM 機器人」。現在看起來連瀏覽都擋了。發言人的說法是，eBay 對第三方採取「選擇性」策略，並在「未經授權的爬取和用我們的資料做訓練」等情況下限制代理存取。

eBay 不是唯一這樣做的。Amazon 完全封鎖外部代理，2025 年 11 月還為了 Comet 瀏覽器的購物代理對 Perplexity 提告，同時砸重本推自家的 Rufus。Amazon 說 Rufus 每年可帶來超過 100 億美元的增量營收。Target 則是時開時關，代理有時進得去，有時被擋。

## 沒人在講的事：廣告版位

多數報導把這件事說成爬蟲或資料訓練的爭議。那只是表面。真正的重點是**廣告生意**。

eBay 的搜尋結果頁本身就是廣告版位。賣家付費讓商品排前面的 Promoted Listings，一年營收超過 10 億美元。Amazon 的廣告業務更大，一年超過 500 億美元。這兩門生意都建立在同一個前提上：有人類在看平台排好的頁面。

AI 代理不會看贊助版位。它直接讀商品資料，比價、比商品狀況，然後回傳最好的選項。那位讀者讓 Muse 每天整理手錶清單時，每一個被跳過的廣告商品都是 eBay 少賺的錢。每一個從鏡像網站抓到的商品，都是 eBay 的庫存被別人免費拿去用。

換成台灣的例子會更好懂。想像你叫 AI 代理去蝦皮、momo、PChome 幫你找最便宜的 AirPods。它不會點任何「推薦商品」，不會看到任何站內廣告，也不會被首頁的限時活動吸引。對這些靠流量和站內廣告賺錢的電商來說，這樣的使用者等於只拿資料、不帶來廣告收入。

所以真正的二階效應是：**AI 代理會打掉電商「靠探索賺錢」的商業模式。**平台不會坐視不管，選項只有兩個：直接封鎖，像 eBay 和 Amazon；或者向代理收過路費，也就是 eBay 那句「正和潛在夥伴洽談中」背後的意思。

這劇本我們看過。2023 年 Twitter 和 Reddit 先後讓 API 改成付費，Reddit 之後和 Google 簽了據報一年約 6,000 萬美元的資料授權合約。電商代理會是下一個走上這條路的。

## 替 eBay 說句話

公平起見，eBay 的立場也有道理。AI 代理目前是很不可靠的買家。它會看錯商品說明、忽略賣家評價，也分不出那支「全新未拆」的錶是不是假貨。代理買錯東西時，買家會怪 eBay，客訴和糾紛成本也是 eBay 在吸收。雙邊市集的核心是信任，在買賣雙方之間插進一個沒人負責的中間人，確實可能破壞這份信任。

但這個論點有個破綻：它假設使用者會一直主動回到 eBay。使用者不會忠於平台，他們選的是方便。The Verge 測試時發現，被擋住的 Muse 轉而引導使用者去「鏡像 eBay 商品的外部網站」。封鎖代理沒有把人留在 eBay，只是把人推去更爛的盜版 eBay，而 eBay 在那裡一毛錢都賺不到，也什麼都控制不了。

## 真正的分界線

Adobe 敢開放，是因為它賣的是**能力**，代理每呼叫一次，最後都會回到一個付費授權。eBay 猶豫，是因為它賣的是**注意力**，而代理正好會吃掉注意力。用這條線判斷誰會開放、誰會封鎖，比看任何一家公司的 AI 策略簡報都準：

- **賣能力的公司**，例如 Adobe、Figma、Notion、Salesforce、Stripe，會搶著推 MCP。能被代理呼叫，就是新的通路。
- **賣注意力的公司**，例如 Amazon、eBay、Meta 的動態消息，以及 Google 自己的搜尋廣告，會封鎖外部代理、自己做代理，再把存取權賣給別人。

Google 剛好兩邊都是：它一邊在 AI Mode 裡迎接 Adobe，一邊靠人類點擊廣告賺錢，而代理正好會跳過那些廣告。這個矛盾 Google 遲早要處理。

台灣的 SaaS 和電商業者也該想一下自己站在哪一邊。如果你做的是會計、排班、POS 這類工具，現在就該準備 MCP 介面，否則客戶的 AI 代理會直接選別家。如果你做的是靠流量和廣告賺錢的平台，那麼「要不要擋代理」很快就會成為董事會要討論的議題。

## 值得關注

1. **2027 年中以前，eBay 會簽下授權代理合作。**最可能的對象是 OpenAI 或 Google，走 OpenAI 的 Agentic Commerce Protocol 或 Google 的 AP2 這類結構化結帳協議，而不是讓代理直接瀏覽網頁。Meta 的 Muse 除非付錢，否則會一直被擋。
2. **「代理存取費」會成為正式收費項目。**12 個月內，至少會有一家大型電商公開按查詢次數或交易筆數向第三方代理收費。這就是 2023 年 API 付費化在電商領域重演。
3. **Adobe 會在財報裡揭露「代理來源使用量」。**2027 年的法說會上，預期會出現「X% 的 Firefly 生成來自 Adobe App 之外」這類數字，用來向懷疑的投資人證明 MCP 能留住訂閱。
4. **Microsoft 會在兩季內加碼 Office 的 MCP 布局。**Adobe 和 Google 的同盟直接衝著 Microsoft 的生產力工具而來，Microsoft 不可能不回應。
5. **Amazon 告 Perplexity 的案子會成為指標判例。**法院怎麼界定代理的存取權，對這個市場的影響會比今年任何新產品發表都大。

這場入口戰爭的核心問題是：你的產品是一個「目的地」，還是一個「工具」。賣工具的會擁抱代理，賣目的地的會對抗代理。而越來越多使用者，已經不打算親自去任何目的地了。