---
title: "「Tokenmaxxing」退潮：企業AI支出狂潮正在急煞車"
summary: "2025年，「盡量多用AI」是企業界最時髦的策略；2026年，帳單到了。Uber四個月燒完全年AI預算，微軟撤回開發者的Claude Code授權，AT&T限制Copilot使用——企業界正從「Tokenmaxxing」急轉「Tokenminimizing」，AI成本管理成為最熱門的新賽道。"
category: "industry"
publishedAt: 2026-06-19
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/"
  - name: "Fortune"
    url: "https://fortune.com/2026/05/28/tokenmaxxing-is-dead-companies-didnt-get-the-roi-from-ai-they-wanted-to-see/"
  - name: "CBC News"
    url: "https://www.cbc.ca/news/business/ai-spending-ending-tokenmaxxing-tokenomics-9.7237680"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/tokenminimizing-companies-cap-employee-ai-spending"
tags:
  - "企業AI"
  - "AI支出"
  - "tokenmaxxing"
  - "uber"
  - "microsoft"
  - "AI投資回報"
  - "finops"
  - "github-copilot"
relatedSlugs:
  - "2026-06-19-tokenmaxxing-enterprise-ai-spending-backlash-en"
  - "2026-06-17-microsoft-mai-seven-models-openai-independence-zh"
---

2025年，企業界最炙手可熱的績效指標不是市占率、不是毛利，而是一個詞：**token消耗量**。公司爭相建立AI使用量排行榜，追蹤哪些員工消耗了最多AI token，對外宣稱自己百分之百投入AI轉型。這股風潮有了一個名字——**「Tokenmaxxing」**：把AI使用量最大化，當作AI採用率、乃至創新力的代理指標。

到了2026年中，帳單來了，而且金額觸目驚心。

## Uber：四個月燒完全年預算

這場企業AI支出危機中最震撼的案例，來自Uber。這家叫車和物流巨頭在**2026年4月——僅僅四個月**後，便耗盡了全年的AI程式設計預算，隨即對每位員工每種工具的使用費用設定每月**1,500美元**的上限，以止血為先。

爆雷背後的數字揭示了企業AI採用最核心的矛盾。Uber有約**95%的工程師**每月使用AI工具，約**70%的提交程式碼**由AI生成。從傳統指標看，Uber的AI採用率幾乎是滿分。然而，當COO Andrew Macdonald仔細審視這些token消耗到底帶來了什麼，他的結論是：「token支出與可量化產出之間的關聯，目前並不存在。」

Uber的AI帳單失控，不只是因為用量太高，恰恰也是因為採用太廣——工具沒有硬性用量上限，工程師缺乏節約的動機。一個讓AI代理反覆重構整個程式庫的工程師，和一個精準發問並應用答案的工程師，在生產力上未必有差別，在token消耗上卻可能相差千倍。

## 不止Uber：全產業的縮影

Uber的案例只是最響亮的一個，這種模式在企業界普遍存在：

**微軟**在為開發者開啟Claude Code授權數月後，悄悄將其撤回——這對一家既是OpenAI最大投資方、又主力銷售企業AI產品的公司而言，頗為耐人尋味。

**AT&T**開始限制員工使用GitHub Copilot，這款AI程式設計助手是微軟旗下最重要的企業AI產品之一。

**Meta**關閉了內部AI token使用量排行榜，因為發現成本「接近數十億美元」，而排行榜滋生的是刷數據行為而非真實生產力——據悉，某迪士尼員工在九天內與Claude AI互動了46萬次。

**Priceline**在更新Cursor合約時，發現報價上漲了**四至五倍**；公司一名工程師在單月內花掉了**4萬美元**的AI token費用。公司IT財務總監Chris Reed用了一個令人印象深刻的比喻：「就像快克可卡因的成癮模式——先讓你免費試，等你上癮了再收錢。」

一家未具名的飯店業公司，據稱因未設置任何用量限制，收到了一張**5億美元的Claude帳單**——儘管這一數字尚未獲官方證實。

## 為何企業對成本如此毫無準備？

問題的根源在於企業AI合約的初始設計，以及工具部署的速度。大多數企業AI工具以「按座位收費」或「無限量使用」模式推出，企業急於向董事會展示AI決心，用量上限、token預算、成本分攤機制統統淪為事後才想起的細節。

傳統SaaS軟體每個使用者每月收固定費用，成本結構可預測；企業AI工具按token消耗計費，成本結構是超線性的——一個工程師花一個下午讓AI代理處理大型程式庫，消耗的token量可能是一百次普通查詢的總和。乘以數千名工程師，變異數極為驚人。

FinOps Foundation執行長J.R. Storment對此描述直白：「我們開始聽到生存危機，整個對話從『Tokenmaxxing、快去用』切換成了『我們需要護欄』。」OpenAI企業業務主管Alexander Embiricos也確認：「現在的對話已經完全不同了，客戶問的是：我們到底花了多少、花在哪裡？」

## 從「Tokenmaxxing」到「Tokenminimizing」

業界迅速創造了一個鏡像詞彙：**「Tokenminimizing」**——對簡單任務使用更小、更便宜的模型，只有真正需要頂尖能力的查詢才送上昂貴的前沿模型，並在個人、團隊和部門層面設立硬性支出上限。

這個思路幾乎是複製了十年前雲端成本優化的劇本。2012至2015年間，大量企業將既有系統「搬上雲端」卻沒有針對雲原生架構重新設計，隨之而來的是巨額帳單，最終催生了FinOps這門專業學科。

現在，同樣的劇情在AI領域重演，只是時間軸更短。**Linux Foundation**已成立**Tokenomics Foundation**，致力於建立企業AI成本追蹤的標準化框架，明確參照FinOps對雲端成本管理的示範。**Pay-i**、**Paid**等新創公司應運而生，提供即時AI支出儀表板、預算強制執行和成本分攤工具——而這些，現在的雲端供應商都還沒有原生提供。

## 對AI供應商意味著什麼

支出糾正來得不是時候，對AI供應商而言尤其如此。OpenAI正在籌備萬億美元估值的IPO，部分論點建立在企業AI持續成長之上；Anthropic處境類似。兩家公司的主要收入來源，正是企業現在試圖壓縮的API token消耗。

短期影響很可能是token消耗增長的降速，即使使用者數量維持穩定甚至繼續增加。企業不會停止使用AI工具，但會更審慎地挑選哪些查詢值得送到昂貴的前沿模型，哪些可以路由到Llama、Mistral等推理成本幾乎為零的開源模型。

從長遠看，這次調整對整個生態系或許是健康的。Tokenmaxxing從來不是可持續的策略；AI帶來的真實生產力提升，需要與工作流程的深度整合，而非最大化消耗。在這場洗牌中倖存並建立成熟AI成本管理實踐的企業，也可能是真正能衡量和驗證AI價值所在的企業——而不是假設token越多等於產出越高。

以量取勝的AI採用時代正在結束，以價值取勝的AI採用時代，已別無選擇地開始了。
