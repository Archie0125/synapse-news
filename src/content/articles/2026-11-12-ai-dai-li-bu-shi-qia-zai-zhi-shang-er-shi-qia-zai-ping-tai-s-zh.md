---
category: ai-ml
featured: true
lang: zh
publishedAt: '2026-11-12T18:36:17.785593+00:00'
relatedSlugs: []
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/github-agentic-workflows-ga/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: The Verge
  url: https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1030787/google-gemini-4-carbon-public-rollout
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/
summary: 模型愈會做事，平台愈不想讓它進門，因為真正被搶走的是客戶與交易主導權。
tags: []
title: AI 代理不是卡在智商，而是卡在平台手上的鑰匙
trending: true
type: analysis
---

AI 代理現在最尷尬的真相，不是它不夠聰明，而是網站根本不打算讓它做事。

Google 可以叫一群代理分工，Anthropic 可以讓 Claude 邊開會邊排工作，Meta 可以讓 Muse 幫你找商品；但當代理真的走到 eBay 門口，平台只要回一句「禁止存取」，前面那些模型能力、推理分數與發表會示範，立刻全部歸零。

這才是 2026 年代理市場真正的分水嶺：模型公司以為競爭項目是「誰最會思考」，平台在意的卻是「誰有資格碰我的商品、帳號與訂單」。

Meta 的 Muse 原本能每天替使用者整理 eBay 手錶，列出價格、運費、品況與商品連結。到了 11 月，Muse 卻開始抓不到資料。[《The Verge》的實測](https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping)也出現相同結果，有時只能把使用者導向轉載 eBay 商品的外部網站。

eBay 沒有正面承認全面封鎖，只說會限制未經授權的爬取與模型訓練，並「選擇性」開放第三方代理。今年 1 月，它已修改使用條款，禁止沒有人工確認的「代買代理」與 LLM 機器人直接下單。Amazon 的態度更硬，外部購物代理連逛都困難；Target 則是有些情況放行、有些情況阻擋。

這不是幾個網站還沒把相容性做好，而是平台刻意踩煞車。

原因也不是平台突然討厭 AI。eBay 自己正在把 AI 塞進搜尋、推薦與賣家工具，Amazon、Target 同樣不缺自家 AI 功能。平台反對的不是 AI，而是「替消費者工作的外部 AI」。

兩者差很多。平台自己的助手可以優先考慮成交率、廣告版位、庫存周轉與使用者停留時間；消費者的代理則應該只在乎總價、運費、退貨條件與商品是否真的符合需求。當最便宜的商品排在贊助商品下面時，代理應該跳過廣告，平台卻希望你先看到廣告。

eBay 在 2024 年約有 1.34 億名活躍買家，全年商品交易總額達 747 億美元，營收約 103 億美元。外部代理若把這些商品全部整理成一張乾淨的比較表，只推薦其中一項，它確實替消費者省了時間，卻也把 eBay 從一座市場降格成後端資料庫。

被拿走的不只流量。平台會失去推薦排序、贊助刊登、交叉銷售、使用者行為資料，甚至失去決定「哪個商品先被看見」的權力。對電商平台而言，這些不是附加功能，而是商業模式本身。

換成台灣場景就更容易理解。假設你叫代理同時去 momo、PChome 24h 與蝦皮找一台筆電，自動計算折價券、刷卡回饋、贈品與到貨時間，最後只顯示一個答案。對消費者來說，這比開二十個分頁有效率得多；對平台來說，首頁活動、關鍵字廣告、會員導購與站內推薦，全被代理壓縮成一列數字。

沒人在談的重點是：封鎖代理正在變成新一代的通路控制。

未來平台不只會問「這個代理安不安全」，還會問它是哪家公司派來的、是否願意付費、能看哪些資料、能不能下單，以及交易完成後誰擁有客戶。所謂開放的代理網路，很可能不會像早期 Web 那麼開放，而會變成一張由合作協議、授權 API、流量費與交易抽成組成的收費地圖。

1994 年出現的 robots.txt，是網站與搜尋引擎之間的早期默契；2022 年，它被正式整理為 RFC 9309。搜尋引擎之所以能與網站共存，是因為交換條件相對清楚：Google 抓取內容，再把使用者送回原網站看廣告、訂閱或購物。

代理改寫了這筆交換。它可以讀資料、做比較、下決定、完成操作，最後讓使用者一直留在 ChatGPT、Claude、Gemini 或 Muse 裡。平台提供商品與服務，模型公司卻拿走入口、介面與使用者關係。站在平台角度，這不叫合作，這叫被抽走一層價值。

所以 Google 此時推出 Gemini 4 Carbon，反而凸顯了問題的荒謬。Carbon 在 Antigravity 裡加入「代理群」功能，可以把一個指令拆給多個代理協作。上市優惠價是每百萬輸入 token 2 美元、輸出 token 10 美元，約為 OpenAI GPT-6 Astra 的五分之一、Anthropic Fable 5.2 的四分之一；即使 2026 年 11 月底價格加倍，[帳面單價仍低於兩個主要對手](https://www.theverge.com/ai-artificial-intelligence/1030787/google-gemini-4-carbon-public-rollout)。

但便宜的推理買不到通行證。十個代理一起撞上 eBay 的封鎖，不會產生十倍價值，只會製造十倍請求。代理群還會讓平台更緊張：哪一個子代理讀了帳號？哪一個決定購買？遇到藏在網頁裡的惡意指令時，責任算誰的？

相較之下，GitHub Agentic Workflows 展示了比較可信的路線。這項服務在 2026 年 6 月公開預覽，10 月 28 日正式上線。代理預設只有讀取權，若想修改程式碼，必須先提出變更，再交給持有另一組寫入權杖的工作執行。企業還能加上人工審核，通過後才准寫入。

重點不是代理能不能改 code，而是「讀取、提案、核准、寫入」被拆成四個階段。防火牆與威脅偵測負責檢查內容，代理不能因為拿到一個模糊任務，就順手取得整個 repository 的完整控制權。

GitHub 也替失控的成本裝上保險絲。每個 AI Credit 是 0.01 美元，單次執行預設上限 1,000 點，也就是 10 美元；每日預設 5,000 點，相當於 50 美元；威脅偵測上限 400 點，也就是 4 美元；代理步驟最長跑 20 分鐘。團隊還能用 `gh aw forecast` 預估每月花費。

這些數字比「每週省下 29 小時」更值得注意。Accenture 一名主管確實在 GitHub 公告中提出這項成果，但[公開資料沒有交代測量方式](https://www.infoq.com/news/2026/11/github-agentic-workflows-ga/)。企業真正需要的不是漂亮的省時數字，而是能回答：代理看過什麼、提出什麼、誰准它執行、花了多少錢，以及出事後能否還原。

GitHub 的做法也不是沒有破口。開發者若直接給寫入權限，或自己加上權限過大的工作，原本的隔離就可能失效。支援 Kubernetes runner 的 Docker-in-Docker 架構，預設還需要具特權的 sidecar，形成「代理採最小權限，旁邊卻站著特權容器」的矛盾。但至少它承認：代理不是聊天機器人加上一顆執行按鈕，而是一套權限系統。

Adobe 也走向類似思路。它在 2026 年 MAX 大會推出本機 MCP，讓 ChatGPT、Claude 與 Gemini 呼叫 Photoshop、Illustrator、After Effects、Premiere 的部分功能。Adobe 不是把 Creative Cloud 大門整扇拆掉，而是逐項決定哪些操作可以對外開放。[Adobe 甚至坦白仍在摸索界線](https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/)。

這很合理。Adobe 2024 會計年度營收達 215.1 億美元，它當然希望代理替使用者操作 Photoshop，卻不想淪為藏在其他聊天介面後面的無名圖片引擎。開放 MCP 是導入代理流量，也是把代理關進 Adobe 定義的操作範圍。

Anthropic 的 Claude Meetings 則把權限問題直接帶進會議室。Claude 可以成為 Google Meet 裡看得見的與會者，邊聽邊整理時程、工作項目與白板；但若會議有外部來賓，沒有管理員授權就不能加入，外部人士中途進場時還會自動離席。[這項功能先提供 Team 與 Enterprise 方案測試](https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/)，因為企業帳號至少有管理者、身分與政策可以追蹤。

反方論點並不弱。外部代理可能誤讀二手商品品況、觸發詐騙、洩漏登入資料，或自動買進無法退貨的商品。企業代理也可能把客戶名單帶進錯誤的會議，或執行文件中暗藏的提示注入。平台原生代理掌握即時庫存、付款、物流與爭議處理，理論上比模擬滑鼠點擊的外來機器人可靠。

可是全面封鎖也不是長久解法。Muse 若找不到 eBay 商品，就會把收藏家送到其他市場。eBay 保住了介面，卻失去潛在買家。規模較小的電商與服務商反而有動機主動提供「代理可讀」的商品目錄，拿相容性當成獲客手段。

最後形成的市場不會是「代理全面自由」，也不會是「平台全部封鎖」，而是分層授權：讀取可能免費，寫入需要身分，付款需要再次確認，高風險操作需要人工核准，商業平台則按查詢、導流或成交收費。

模型能力會繼續進步，但勝負已經轉移。智慧正在快速變便宜，權限卻愈來愈昂貴。

### 值得關注

1. **2027 年會出現付費代理通道。** 至少一家大型電商或旅遊平台會推出「合作代理」方案，明訂查詢頻率、交易抽成、推薦揭露與責任歸屬。代理存取將從網路的預設能力，變成要談合約的商業產品。

2. **讀取與執行會被強制拆開。** GitHub 的模式將進入採購、退款、正式環境部署與資料匯出。代理可以大量閱讀與提出建議，但超過金額門檻或不可逆的操作，會交給另一個身分執行並留下核准紀錄。

3. **平台合作名單會比 benchmark 更能決定勝負。** 推理分數少兩分、卻能合法操作 Adobe、航空公司、零售商與企業系統的模型，實際價值會高過一個在結帳頁被擋住的天才模型。代理評比最終必須計算「成功完成的授權操作」，而不只是答題成績。

4. **每個代理都得帶著可追蹤身分。** 匿名瀏覽器自動化會逐漸被簽章身分、可撤銷權限、操作紀錄與責任條款取代。到了 2027 年底，市場最常問的問題不再是「AI 做不做得到」，而是「誰准它做、依照誰的規則，以及做錯後誰買單」。