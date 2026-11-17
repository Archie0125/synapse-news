---
category: ai-ml
featured: true
lang: zh
publishedAt: '2026-11-11T06:25:46.061594+00:00'
relatedSlugs: []
sources:
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/all-7-anthropic-founders-will-each-cash-out-about-250m-in-ipo/
- name: SaaStr
  url: https://www.saastr.com/anthropics-ipo-puts-216-billion-in-employee-hands-another-160-billion-is-reserved-for-the-next-hires/
- name: Engadget
  url: https://www.engadget.com/2312177/anthropic-takes-on-google-and-microsoft-with-claude-sheets/
- name: TechCrunch
  url: https://techcrunch.com/2026/11/10/anthropic-sets-ipo-price-range-of-70-to-78-per-share-to-reach-an-implied-valuation-of-1-404-trillion/
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1030709/anthropic-has-its-own-ai-powered-office-suite-now
summary: 掏 640 億美元買 Anthropic 股票，換到的投票權幾乎是零。同一週，它把 Claude 塞進你的試算表。
tags: []
title: Anthropic 喊價 1.4 兆美元上市：它要的不是 AGI 夢想，是你的 Excel
trending: true
type: analysis
---

先講結論：Anthropic 這次 IPO，賣的是「只分錢、不分權」的股票；同一週推出 Claude Sheets，是在跟華爾街證明「我不只賣給工程師」。這兩件事要放在一起看。

先看數字。修訂版 S-1 出來了：發行 8.25 億股 A 股，每股 70 到 78 美元，代號 ANT，預計 11 月 19 日左右在 Nasdaq 掛牌。用區間上緣、完全稀釋計算，估值 1.404 兆美元。加上 260 億美元的私募配售和承銷商的超額配售權，淨募資落在 846 億到 937 億美元之間。

拿個參照：2019 年沙烏地阿美 IPO 募了約 256 億美元，創下當時的紀錄。Anthropic 光是公開發行的部分就是它的兩倍半。台積電市值破兆美元的時候，台灣媒體已經報了好幾週，這次是一家成立才五年的 AI 公司直接以兆美元價位上市。

## 你買到的，是一張沒有投票權的門票

治理結構寫得很清楚。七位共同創辦人（Dario Amodei、Daniela Amodei、Tom Brown、Jack Clark、Jared Kaplan、Sam McCandlish、Chris Olah）每人各拿一股具超級投票權的 F 類股，合計握有約 51% 的表決權。另外，「長期利益信託」（Long-Term Benefit Trust）負責選出董事會多數席次。Amazon、Google 和這次的策略投資人拿的都是沒有投票權的 N 類股。

雙層股權不稀奇，Google 2004 年、Facebook 2012 年都這樣上市，Snap 2017 年更直接賣零投票權的股票。Anthropic 疊了兩層：創辦人掌握表決權，再由外部信託決定董事會。以台灣的經驗來說，大概是比家族控股更緊的結構，連董事會都不是股東說了算。

我的看法是：這說得通。一家強調 AI 安全的公共利益公司（PBC），如果季報不好看就被激進基金改組董事會，那安全承諾只是行銷話術。但投資人要清楚自己買的是什麼。這次最多 20% 的股份會配給散戶，等於散戶出錢支持一家在章程裡寫明「股東利益不是第一優先」的公司。

至於媒體很愛報的「創辦人各套現 2.5 億美元」，其實不太重要。每人賣 3,378,378 股，用中間價 74 美元算約 2.5 億，七人合計約 17.5 億，不到整體發行量的 3%。賣完每人仍持有約 3.2% 的 A 股，比較像資產配置，談不上落跑。

## 為什麼是現在推辦公室套件？

看營收就懂了。截至 10 月底，Anthropic 的年化營收（run-rate）達 810 億美元，比 9 月底多了約 100 億。1.404 兆除以 810 億，大約 17 倍營收。以它目前的成長速度，這個倍數不算瘋狂，前提是成長不能停。

問題在於過去的成長主要來自開發者和企業 API，尤其是 Claude Code。產品負責人 Nicholas Lin 對 *The Verge* 說得很直白：Claude Code「一年前改變了工程師的工作方式」，而非技術人員是「我們想補上的缺口」。全球專業開發者大概三千萬人，每天開 Excel、跑會議、寫會議紀錄的白領則是好幾億人。要撐起兆元估值，Anthropic 必須拿下這群人。

於是這次一口氣推出：

- **Claude Sheets**（beta，所有付費方案）：可多人協作的試算表，支援分頁和公式，Claude 的每次修改都有紀錄，可匯出 Excel，也支援 Google Workspace 外掛。
- **Claude Meetings**（beta，限 Team / Enterprise）：會議 AI 助理，先支援 Google Meet。有外部人士參加的會議，沒有管理員允許不會加入。
- **Claude Whiteboards**（beta，所有付費方案）：白板發想工具，會自動依主題分類大家的想法，並列出每個人的待辦事項。
- **Claude Data**（原名 Dashboards）：正式開放給所有付費用戶。
- **深度整合**：HubSpot、Adobe、Atlassian 的應用可以直接在 Claude 裡開啟，背後是已超過 9,000 個外掛的 MCP 生態系。

同一時間推出的 Fable 5.2 降價，另外有一個限制存取的 Mythos 模型。這個組合的策略很清楚：主力模型變便宜，才能大量用在每一格試算表、每一份逐字稿；最強的模型限量供應，維持稀缺性、守住安全形象，也撐住高端定價。跟 NVIDIA 把消費級顯卡和資料中心 GPU 分開定價是同一套做法。

## 沒人在談的事：股東名單本身就是利益衝突

看看 260 億美元私募是誰買的：AMD、Broadcom、Google、Micron、Microsoft、NVIDIA、台積電。Google 和 NVIDIA 各出 100 億。

第一點，這七家裡有五家是 Anthropic 的算力供應鏈。這些錢很大一部分會以晶片、記憶體、晶圓代工訂單的形式流回這些公司。說它有部分是「預付貨款」並不過分。這不違法，但「策略投資人背書」這種說法要打點折扣。對台灣讀者來說，台積電入股很值得注意：先投資、再拿 AI 晶片訂單，等於台積電在最大客戶群裡直接押了股權。這是過去晶圓代工「不跟客戶競爭、不碰客戶股權」那套中立原則的一次微妙轉向。

第二點更有意思。Google 和微軟現在都是 Anthropic 的股東，而 Anthropic 剛推出直接對打 Google Workspace 和 Microsoft 365 的產品。Claude Meetings 第一站是 Google Meet，而 Meet 本來就內建 Gemini 筆記；Claude Sheets 匯出成 Excel，而 Excel 裡已經有 Copilot。Anthropic 在投資人的平台上搶投資人的生意。只要雙方還互相需要，這種關係就能維持：Google 要 Anthropic 這個 TPU 大客戶，微軟要 OpenAI 以外的模型選項。哪天任一方覺得沒那麼需要了，只要改一條 API 政策，Anthropic 的通路就會被卡住。

還有一個數字很少人注意。根據 SaaStr 對 S-1 的分析，以 78 美元計算，員工手上的選擇權和 RSU 淨值約 **2,160 億美元**，約 5,300 名員工平均每人 4,100 萬美元。另外還有 **1,600 億美元**的股份保留給未來新進員工。員工數從 2024 年底的約 940 人暴增到現在的 5,300 人。這 1,600 億的預留股權是一筆搶人預算，未來三年整個 AI 和 B2B SaaS 產業的薪酬都會被它拉高。台灣的 AI 新創想挖一位資深工程師，對手開出的是可以馬上在 Nasdaq 變現的股票。

## 空方論點：這些風險是真的

第一，年化營收不等於獲利。S-1 揭露約 323 億美元尚未認列的 RSU 費用，而且上市那一季會跳升。第一份季報的 GAAP 虧損大概會很難看，到時候標題會很刺眼。

第二，估值走勢沒有標題那麼樂觀。幾個月前傳出的目標是 2 兆美元，現在是 1.4 兆；5 月私募輪是 9,650 億。TechCrunch 也提到，這次是在「市場更不穩、AI 投資降溫」的情況下硬上。從 2 兆砍到 1.4 兆，代表市場已經壓過價了。

第三，辦公室軟體很難打。微軟 Office 稱霸三十年，Google Docs、Notion、Airtable 都沒能撼動，Salesforce 花 7.5 億美元買的 Quip 也沒做起來。AI 再強，也很難改變會計部門用了十幾年的 Excel 快捷鍵和 IT 採購流程。

但我還是偏多。關鍵在於 Claude 不需要取代 Excel，只需要成為工作開始的地方，Excel 退居匯出格式。MCP 外掛生態的用意就是讓底層的應用程式變得可以替換。

## 值得關注

1. **定價會超過 78 美元。** 光董事 Reed Hastings 就想透過捐贈基金買 3 億美元。我預估最終定價在 82 美元以上，加上散戶配額，首日漲幅超過 20%。
2. **微軟和 Google 會在 90 天內在價格上反擊。** 2027 年第一季前，Copilot 和 Gemini 的會議、試算表功能會出現更積極的綑綁或降價。Fable 5.2 降價只是第一步。
3. **Claude Meetings 會在 2027 年中前支援 Zoom 和 Teams。** 只支援 Google Meet 是 beta 階段的限制，不是長期策略。微軟會不會開放 Teams，正好可以檢驗這段投資關係到底有多穩。
4. **Mythos 會變成企業加購方案，而不是公開模型。** 限制存取最後會變成一個價格層級，很可能跟 Enterprise 方案和合規條款綁在一起。
5. **真正的考驗是禁售期結束。** 上市大約半年後，也就是 2027 年 5 月前後，那 2,160 億的員工股權有很大一部分可以賣。如果年化營收成長在那之前放緩，就算基本面沒問題，ANT 也可能重挫。
6. **OpenAI 會加速上市。** 一旦有純 AI 實驗室在公開市場交易，所有對手都會被拿來跟它比估值，想晚上市都難。