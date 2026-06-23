---
title: "Google收下6000個社群貢獻後關閉Gemini CLI——開發者怒了"
summary: "Google將於6月18日終止免費用戶對開源Gemini CLI的存取，以閉源的Antigravity CLI取而代之。社群開發者在這個Apache 2.0儲存庫貢獻了超過6000個合併PR後，卻被迫遷移至無法自行審計原始碼的工具，批評者稱此為AI開源史上最赤裸的「誘餌換包」操作。"
category: "developer-tools"
publishedAt: 2026-06-10
lang: "zh"
featured: false
trending: false
sources:
  - name: "The Register"
    url: "https://www.theregister.com/ai-ml/2026/05/20/bye-bye-gemini-cli-google-nudges-devs-toward-antigravity/5243605"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317407/20260529/linux-foundation-tool-spotlighted-furious-developers-accuse-sickening-google-gemini-cli-bait-and-switch.htm"
  - name: "AI Builder Club"
    url: "https://www.aibuilderclub.com/blog/google-kills-gemini-cli-june-18-2026"
tags:
  - "Google"
  - "Gemini CLI"
  - "Antigravity CLI"
  - "開源"
  - "開發者工具"
  - "社群"
  - "Linux Foundation"
  - "企業版"
relatedSlugs:
  - "2026-06-04-google-io-2026-search-ai-agents-overhaul-zh"
  - "2026-06-01-github-copilot-ai-credits-billing-change-zh"
  - "2026-06-02-microsoft-build-2026-mai-coding-models-zh"
---

開源軟體的歷史從不缺乏公司對社群許下承諾、又悄悄反悔的案例。但即便如此，Google對Gemini CLI的處置方式，仍以異乎尋常的力度激怒了開發者社群。

2026年5月19日，Google宣布：Gemini CLI——一個採用Apache 2.0授權的命令列AI代理，Google鼓勵開發社群在近一年內共同建設與擴展——將於6月18日終止對免費用戶的服務。替代品是Antigravity CLI，一款由Google內部開發、無公開原始碼的Go語言二進位程式。那些累積貢獻超過6000個合併PR的社群開發者，留下的是一個授權技術上依然有效、卻缺乏運行後端的空殼儲存庫。

GitHub公告貼文最突出的回應，是31個踩的表情。開發者@anthuanvasquez直接道破社群心聲：「一如既往，Google就是Google。」

## Gemini CLI 是什麼

Gemini CLI約在一年前以Google對命令列AI代理趨勢的回應姿態問世。它採用Apache 2.0授權，在GitHub上公開，被定位為在終端機建立多步驟工作流程的一流開發者工具。它能瀏覽網頁、執行程式碼、管理檔案，並與Gemini API互動——更重要的是，任何人都可以擴展、分叉和修改它。

社群反應熱烈。儲存庫積累了數千顆星，更值得關注的是：貢獻者開始以穩定的步調提交PR——改善代理框架、新增工具整合、修補邊緣案例，並將專案能力拓展至Google內部團隊未及優先處理的方向。到Google宣布關閉時，已有超過6000個PR被合併，代表著相當可觀的無償工程貢獻。

## 「誘餌換包」的機制

開發者@lingyaochu在GitHub議題串中精準點出了這個模式：「開源Gemini CLI，讓開發者貢獻，然後把程式碼遷移到閉源專案。」

機制上頗為微妙。Gemini CLI儲存庫的Apache 2.0授權並沒有被撤銷，Google表示儲存庫將繼續公開存取。被撤銷的，是讓工具得以運作的基礎設施存取權：身份驗證後端、API配額系統，以及Gemini CLI執行指令時所呼叫的服務端點。

如記者Christine Hall所寫，Google「實際上只移除了開源的部分」——程式碼依然可見，但工具對免費用戶已無法使用。持有Google AI Standard或Enterprise授權的企業用戶，仍可透過付費API金鑰繼續存取Gemini CLI，這意味著開源儲存庫作為付費客戶的遺留相容性包裝繼續存在，而非一個活躍的社群專案。

替代品Antigravity CLI沒有公開原始碼，其GitHub儲存庫只含文件和設定檔，沒有實作。工具以`agy`而非`gemini`指令執行，這個變更使所有基於Gemini CLI指令建構的Shell腳本和CI管線，在沒有相容性墊片的情況下直接失效。

## Antigravity 究竟提供什麼

對Google的立場持平而論：Antigravity CLI確實是一個不同的工具，而非Gemini CLI的改名重包裝。它專為多代理工作流程打造，圍繞Google的Antigravity平台設計——後者是Google「代理優先開發」技術棧的統一品牌。二進位檔不依賴任何執行期環境，這是相對於Gemini CLI Python環境需求的真實優勢。

然而，Antigravity CLI在推出時尚未達到與Gemini CLI的完整功能對等。Google在遷移指南中承認，代理技能（agent skills）、掛鉤（hooks）和子代理（subagent）支援目前僅部分涵蓋。對於在Gemini CLI開源可擴展性上建立了複雜工作流程的那部分開發者，遷移意味著真實的能力損失，而非單純的二進位替換。

6月18日的遷移截止日期，也讓受影響的開發者只有不到一個月的時間，在一個功能還在補全的工具上重建管線。

## Linux Foundation 的角度

這場爭議提升了Linux Foundation一個相對低調倡議的能見度：模型開放性工具（Model Openness Tool），可透過isitopen.ai存取。這個工具針對17個維度對AI相關軟體專案進行評分——從訓練資料透明度到推論基礎設施，再到建構工具的開放性——專門設計用於揭露「開源」宣稱與實際運作開放性之間的落差。

Gemini CLI在程式碼授權項目得分良好，但在基礎設施依賴度上得分偏低，而後者正是這次關閉之所以可能發生的根本原因。Linux Foundation的框架，將Gemini CLI的遭遇定性為一個典型案例：為什麼將某個東西標記為開源，並不保證社群能獲得開源用戶歷來所期待的那種存取。

這個工具在開發者評估其他AI CLI工具時獲得了更多關注，包括Anthropic、OpenAI和較小AI公司發行的工具。在一個每家廠商都透過標榜開源資歷爭奪開發者心占率的領域，Gemini CLI事件讓開發者對這些宣稱的持久性產生了明顯更高的懷疑。

## 更廣泛的規律

Google在當前週期中AI開發者工具的歷史，充斥著加速與碎片化。公司以異常的速度推出、改名或棄置重要的面向開發者產品：Google AI Studio、Gemini API、Gemini Code Assist、Gemini CLI、Firebase Genkit，如今再加上Antigravity，構成了一串部分重疊的計畫，要求開發者就可能在18個月內面目全非的工具做出採用決策。

這種碎片化有累積性的代價。開發者在這些產品之上建立工作流程、CI整合和內部工具；當底層工具改變或消失，這些投資就會貶值。Gemini CLI事件之所以引人注目，不在於開發者工具在Google的動盪有多罕見——那其實很常見——而在於這次牽涉到徵集了整整一年的無償開源貢獻後，才限制存取。

## 開發者現在該怎麼做

對受6月18日截止日期影響的開發者，實際選項如下：

遷移至Antigravity CLI，接受現有功能缺口，押注Google在這些缺口阻礙工作流程之前補全。`agy`二進位現已可用，支援基本的多代理使用場景。

轉移至競爭工具。Anthropic的Claude Code、GitHub Copilot CLI以及數個開源替代方案，都在Gemini CLI公告後獲得了用戶增長。Claude Code在終端機原生代理功能上具備可比擬的能力，且採用有償但透明的定價模型。

利用Apache 2.0授權自行fork並維護Gemini CLI。程式碼依然可取得，技術能力足夠的團隊可以維護自有分叉和自訂後端設定，但這需要大多數團隊無力為一個開發工具投入的工程資源。

對更廣泛的AI開發者社群而言，Gemini CLI事件是一個提醒：對依賴基礎設施的工具，開源標籤需要仔細審視。真正的問題不在於程式碼是否可見——而在於後端是否可存取，以及在誰的條件下存取。

Google尚未就社群的強烈反彈發表超出原始遷移公告的公開回應，6月18日的日期維持不變。
