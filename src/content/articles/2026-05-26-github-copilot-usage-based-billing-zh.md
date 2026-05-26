---
title: "GitHub Copilot終結無限制AI：6月1日起轉為按量計費"
summary: "GitHub將於2026年6月1日以「AI積分」取代Copilot的月費制，原因是AI代理工作流程的推理成本急遽攀升，使「無上限」訂閱模式在商業上難以為繼。基本程式碼補全仍維持無限制，但Copilot Chat、自主編程代理等高耗能功能將扣抵每月積分額度，迫使數百萬開發者正視AI輔助程式設計的真實成本。"
category: "developer-tools"
publishedAt: 2026-05-26
lang: "zh"
featured: false
trending: true
sources:
  - name: "GitHub Blog"
    url: "https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/"
  - name: "GitHub Docs"
    url: "https://docs.github.com/en/copilot/how-ows/manage-and-track-spending/prepare-for-your-move-to-usage-based-billing"
  - name: "Visual Studio Magazine"
    url: "https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx"
tags:
  - "GitHub"
  - "Copilot"
  - "AI計費"
  - "開發者工具"
  - "微軟"
  - "AI代理"
  - "訂閱制"
relatedSlugs:
  - "2026-05-03-microsoft-365-e7-agent-365-ga-zh"
  - "2026-04-04-cursor-devin-war-zh"
---

2026年6月1日，GitHub將終結開發者工具市場上最後幾個真正「無限制」的AI訂閱方案之一。從那天起，Copilot的按請求定額收費模式——固定月費換取幾近無上限的AI協助——將由「GitHub AI積分」取代，用多少、扣多少，成本直接與使用量掛鉤。這是一個清晰的訊號：AI代理工作流程的運算成本，正在迫使整個產業誠實地面對一個令人不舒服的現實——「無限AI」並不存在，有人終究得為帳單埋單。

## 具體改變了什麼

GitHub維持現行方案的名目價格不變：Copilot Pro每月10美元、Pro+每月39美元、Business每人每月19美元、Enterprise每人每月39美元。變化的是這些價格能買到什麼。

每個方案現在包含一定額度的月度AI積分，1積分等於0.01美元。以Pro+為例，每月獲得的39積分恰好等於月費金額。使用量的計算基準是Token消耗量：輸入Token、輸出Token和快取Token，各自依所用模型的費率計費。一場使用高階模型的長時間Copilot Chat對話，Token累積起來的費用相當可觀。

有兩項功能明確排除在積分扣抵之外：行內程式碼補全（code completion）與下一步編輯建議（Next Edit Suggestions）仍對所有付費方案維持無限使用。其餘功能——Copilot Chat、Copilot CLI、Copilot雲端代理、Copilot Spaces、Spark，以及透過平台整合的第三方編程代理——均會消耗積分。未用完的積分月底歸零，不得遞延。

對企業和商業客戶而言，積分在組織內統一共用。某個月只用了40%積分的開發者，等同在補貼同部門跑密集代理任務的同事，這樣的設計是對AI使用量因人而異這一現實的妥協。

此外，GitHub宣布推出過渡優惠：現有Business和Enterprise客戶在6月、7月、8月將自動獲得額外附贈積分，以減緩衝擊。

## GitHub為何這樣做：推理成本的困局

GitHub未公開Copilot的確切成本結構，但改變的理由並不難理解。Copilot最初推出月費制時，主要用途是行內程式碼補全——簡短、快速、使用相對輕量的模型，運算帳單可控。

此後，產品陸續擴展至多輪對話、自主雲端代理、長上下文程式碼審查等功能，每一項消耗的算力都遠超程式碼補全。AI代理工作流程的興起——讓Copilot維持整個程式庫的上下文、生成子代理、迭代修復測試失敗、執行Shell指令——使得原本可預測、有界限的工作負載，在固定月費訂閱下可以毫無限制地擴張。

「推理成本的攀升使原有的無限訂閱模式難以為繼，」遊戲開發媒體GameDeveloper.com在報導這項改變時直白點出。GitHub自己的措辭更為外交辭令式，將此次調整定調為讓開發者「在需要時使用更多AI、不需要時少用些」。

時機的選擇並非偶然。GitHub Copilot的競爭對手——Cursor、Windsurf、Devin等——從一開始就採用按使用量計費的模式。GitHub的月費制讓重度用戶可以以固定費用消耗龐大的運算資源，形成競爭上的結構性劣勢。新計費模式讓GitHub回到與競爭對手相同的經濟基準線。

## 開發者反應：數學算不過去

開發者社群的反應相當懷疑。Visual Studio Magazine的標題抓住了主流情緒：「開發者砲轟Copilot按量計費新政：花一樣的錢，得到更少。」在GitHub社群討論串中，數千則留言提出了幾項具體疑慮。

第一是可預測性。每月19美元的座位費過去就是19美元，清清楚楚。新模式下，一個頻繁使用代理功能的開發者可能幾天就用盡月度積分，之後面臨降速或——如果啟用超額付費設定——意料外的帳單。對個人開發者是財務規劃的麻煩，對管理幾十人團隊的工程主管則是需要新工具和流程的治理問題。

第二是模型存取的差異。Copilot模型選擇器中的高階模型——包括來自Anthropic等廠商的前沿模型——收費更高。固定積分額度在高階模型下能換到的使用量，遠少於預設的低成本模型。已依賴特定模型能力的開發者，可能在名目月費不變的情況下，實質上能使用的AI功能縮水了。

第三是代理工作的成本極高。Copilot自主審閱一個PR、跑測試、找出失敗、提出修正、再跑一輪測試，這樣一個完整循環可能消耗數萬Token。以高階模型的費率計算，19美元的月度積分可能在單一複雜任務中就告罄。對於工作流程已轉向自主代理的開發者——正是GitHub和微軟大力推廣的使用方式——新計費模式立刻形成減少AI用量的誘因，否則就得追加預算。

## 更大的趨勢：無限制AI時代的終結

GitHub的轉型反映了整個行業的共同困境，而這個困境自AI代理工作流程成為主流以來就一直在積累。當AI協助意味著程式碼自動補全時，「無限訂閱」模式合理；當AI協助意味著雇用一個全年無休、每月每名用戶消耗數千美元算力的軟體工程師時，這個模式就不再成立。

OpenAI的ChatGPT已為高算力功能設立獨立等級；Anthropic的Claude按Token計費；Google的Gemini為最強大模型設有使用上限。把AI當作固定費率公用事業的時代正在終結，因為在真正能解決複雜工程問題的層次上，AI根本不是固定費率的公用事業。

對企業買家而言，這催生了一個全新的採購對話類別：AI使用治理。大規模部署Copilot的IT部門，將需要追蹤開發者用量、設定每人花費上限，並決定哪些功能值得使用高階模型、哪些用預設便宜模型就夠了。這是兩年前根本不存在的對話。

## 開發者現在該怎麼做

GitHub已在Copilot的組織與個人設定中新增了用量儀表板。對任何Copilot用戶——尤其是跑代理工作流程的人——第一步是在6月1日前建立用量基準。了解自己典型的週工作量消耗多少積分，才能實際評估附贈額度夠不夠用、是否需要追加預算。

GitHub的文件建議在過渡前確認「超額支出上限」的設定——預設情況下，超出附贈積分後系統會降速而非自動追加收費，重度用戶若需要不中斷的代理存取，應主動設定明確的消費上限。

Business和Enterprise客戶的6月至8月優惠期提供了收集實際用量數據的視窗，趁現在弄清楚自己的消費模式，才能在真正計費後做出有依據的決策。

對於在Copilot與Cursor、Windsurf等工具之間評估的個人開發者而言，新計費模式已大幅縮小比較的維度。現在的關鍵問題不再是「哪個工具的月費最優惠」，而是「同樣的Token預算，哪個工具能提供最多的AI能力」。這是一個更誠實、也更有意義的問題——而現在，回答這個問題終於比以前容易多了。
