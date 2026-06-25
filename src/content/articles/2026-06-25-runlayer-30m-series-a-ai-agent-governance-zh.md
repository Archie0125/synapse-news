---
title: "Runlayer 獲 3,000 萬美元 A 輪融資，Khosla 力搶每一分：AI 代理治理成新顯學"
summary: "企業 AI 代理治理平台 Runlayer 完成由 Felicis 領投、Khosla Ventures 跟投的 3,000 萬美元 A 輪融資，Vinod Khosla 本人表示想「買下這輪每一分錢」。平台客戶涵蓋 Instacart、Gusto、dbt Labs 等知名企業，聚焦解決 AI 代理大規模部署後的可見性、控制與合規問題。Gartner 預估 2026 年底前 40% 的企業應用將內建 AI 代理，治理基礎設施正成為下一個 SaaS 大類。"
category: "startups"
publishedAt: 2026-06-25
lang: "zh"
featured: false
trending: true
sources:
  - name: "Fortune: Vinod Khosla 想要 Runlayer 融資輪的每一分錢（獨家報導）"
    url: "https://fortune.com/2026/06/24/exclusive-vinod-khosla-felicis-runlayer-nanit-30-million-enterprise-ai/"
  - name: "Yahoo Finance: Runlayer Raises $30M Series A to Help Enterprises Go All In On AI"
    url: "https://finance.yahoo.com/technology/ai/articles/runlayer-raises-30m-series-help-130000711.html"
  - name: "PR Newswire: Runlayer 完成 3,000 萬美元 A 輪融資"
    url: "https://www.prnewswire.com/news-releases/runlayer-raises-30m-series-a-to-help-enterprises-go-all-in-on-ai-302809271.html"
tags:
  - "Runlayer"
  - "AI代理"
  - "企業AI"
  - "AI治理"
  - "Khosla Ventures"
  - "Felicis"
  - "A輪融資"
relatedSlugs:
  - "2026-06-11-visa-openai-ai-agents-payments-zh"
  - "2026-06-23-agentjacking-sentry-mcp-ai-coding-attack-zh"
  - "2026-06-04-openai-codex-sites-role-plugins-enterprise-zh"
---

當 Vinod Khosla 得知 Runlayer 正在進行 A 輪融資時，他的反應簡短而明確：想要「這輪每一分可用的錢」。Felicis 隨即搶先完成投資，動作快到其他基金甚至來不及提交條款。結果是在 2026 年 6 月 24 日宣布的 **3,000 萬美元 A 輪**，由 Felicis 領投，Khosla Ventures 跟投，使 Runlayer 累計融資達到 **4,200 萬美元**。公司的核心主張只有一句話：企業正在各處部署 AI 代理，卻幾乎沒有任何方法知道這些代理在做什麼。

而填補這個可見性缺口，正在快速變成一筆大生意。

## 代理治理問題

Runlayer 商業模式的前提，是 2025 至 2026 年企業軟體領域發生的結構性轉變。AI 程式助理進化為自主編碼代理，客服聊天機器人升級為能執行多步驟工作流的協調器，OpenAI Codex、Anthropic Claude Code 等代理框架開始以存取生產系統的方式執行任務——隨之而來的是一種新型企業風險：**AI 代理脫軌**。

脫軌不需要科幻電影式的戲劇性場景。它可以像這樣平凡：一個獲得 CRM 寫入權限的客服代理，悄悄地以與原始指示漸漸偏離的方式編輯客戶紀錄；一個有程式庫存取權的編碼代理，因為優化目標是程式碼指標，就提交含有細微架構變更的 pull request；一個財務自動化代理，向原本未明確授權的第三方服務發起 API 呼叫。

這些代理並非惡意——問題在於，**企業目前沒有可靠的方式審計代理存取了什麼、監控它做了什麼決定、或即時撤銷它的存取權限**。當數十個代理同時在公司內運行，各自擁有不同的權限、不同的工具整合、不同的模型版本，原本適用於人類員工和傳統軟體系統的可觀測性架構就完全失效了。

Runlayer 的平台以三個相互扣合的層次應對這個問題：**賦能**（給員工一套結構化的方式把任務委派給代理）、**控制**（定義並執行這些代理能存取哪些工具和數據）、**審計**（以防竄改、符合合規要求的格式記錄每一個代理動作）。公司將這套架構稱為「委派黃金通道」——一個讓 AI 採用感覺安全而非混亂的結構化工作流。

## 客戶名單說話

Runlayer 的早期採用者不是實驗性 AI 實驗室，而是有真實合規義務的大規模生產企業：**Instacart**、**Gusto**、**Decagon**、**Opendoor**、**dbt Labs**、**AngelList**、**Lemonade** 都是已公開的客戶。它們的共同點是運營領域容不下 AI 代理犯錯：財務紀錄、福利管理、保險理賠、開發者工具。

以 Gusto 為例，它為超過 30 萬家小型企業處理薪資和員工福利。若一個 AI 代理在 Gusto 基礎設施內做出未經授權的薪資紀錄變更，後果從監管罰款到實際傷害員工利益都可能發生。Runlayer 的存取控制和審計追蹤能力，在此情境下不是「有了更好」的功能，而是負責任部署 AI 代理的最低門檻。

## Khosla 為何搶快

Vinod Khosla 多年來一直預測企業軟體將圍繞 AI 代理發生根本性重組。他「要每一分可用的錢」這句話，與他長期以來的投資命題完全吻合：建立代理時代基礎設施層的公司——相當於雲端時代的 AWS——將創造遠超其上層應用程式的回報。

對 Runlayer 的具體押注，是押注**治理本身就是一個層**，而非事後補丁。回顧過往，企業軟體的安全與合規一向是被動地移植到現有平台上——SIEM 工具、DLP 解決方案、身份管理系統——而非從設計之初就內建。Runlayer 的創辦人相信，代理時代提供了一個罕見的機會：在代理部署爆炸式增長、形成難以治理的技術債之前，就把治理機制搭建進去。

Gartner 預估 2026 年底前 40% 的企業應用將內建 AI 代理（2025 年不到 5%），讓這個押注有了非常緊迫的時間窗口。三年後再來補做治理，已經太晚；企業需要的是現在就能上線的解決方案。

## 新興的治理類別

Runlayer 並非這個領域的唯一玩家。競爭對手包括增設代理監控模組的老牌安全廠商、將產品延伸到 AI 代理遙測的 Datadog 和 Dynatrace，以及 Galileo、Arize AI、TruEra 等已轉向代理評估與監控的新創。

Runlayer 的差異化定位在於強調**面向員工的委派介面**，而非純粹的後端記錄。大多數可觀測性工具是為安全工程師和平台團隊設計的；Runlayer 的介面是為想把任務交給代理的一線員工設計的——讓他們可以結構化地管理代理的權限範圍、存取清單和升級流程，不需要理解底層基礎設施。

這種以使用者體驗為優先的策略，是對企業 AI 採用實際瓶頸的判斷：大多數大型企業的障礙不是缺乏後端監控工具，而是業務部門員工不知道如何為代理設定適當的護欄。Runlayer 的「黃金通道」就是把這個複雜問題包裝成引導式工作流。

## 4,200 萬美元的下一步

有了累計 4,200 萬美元的資本，Runlayer 近期優先事項包括加速企業銷售、深化與主要代理框架（OpenAI Codex、Anthropic Claude、Microsoft Copilot Studio、Salesforce Agentforce）的整合，以及建立合規認證體系——SOC 2 Type II 是近期目標，政府客戶則瞄準 FedRAMP。

公司也在投資所謂的「代理身份」框架：為 AI 代理頒發可加密驗證的身份憑證，讓下游系統能可靠地區分人類發起的動作與代理發起的動作。當代理開始跨越組織邊界運作——向供應商採購、與監管機構溝通、協調合作夥伴系統——這項能力將變得越來越關鍵。

這輪融資驗證了一個更宏觀的命題：企業 AI 浪潮不只在應用層製造機會，還正在創造一整個新的基礎設施需求類別。就像雲端時代催生了數百億美元規模的雲端安全、可觀測性和治理工具市場，代理時代很可能形成規模相當的新一層。Runlayer 背後有 Khosla 的熱情和 Felicis 的資本，是這個市場最早的幾張重要賭注之一。
