---
title: "Anthropic 推出 Claude Sonnet 5：以一半價格實現旗艦級 AI 自動化能力"
summary: "Anthropic 發布 Claude Sonnet 5，這款中階模型在自動化任務基準測試上幾乎達到旗艦 Opus 4.8 的水準，定價卻便宜了三分之二。Sonnet 5 即日起成為免費與 Pro 方案的預設模型，被定位為 AI Agent 時代的主力骨幹。"
category: "ai-ml"
publishedAt: 2026-07-01
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/"
  - name: "Anthropic 官方公告"
    url: "https://www.anthropic.com/news/claude-sonnet-5"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/anthropic-launches-claude-sonnet-5-at-a-steep-discount-to-its-top-model-as-the-company-races-toward-a-blockbuster-ipo"
tags:
  - "anthropic"
  - "claude"
  - "ai模型"
  - "agentic-ai"
  - "大型語言模型"
  - "開發工具"
relatedSlugs:
  - "2026-07-01-anthropic-claude-sonnet-5-agentic-launch-en"
  - "2026-06-30-anthropic-california-government-claude-deal-zh"
  - "2026-06-29-us-export-control-claude-fable5-foreign-ban-zh"
---

Anthropic 於 6 月 30 日正式推出 Claude Sonnet 5，這是旗下中階模型系列的最新版本。官方強調，新模型帶來接近旗艦 Opus 4.8 的表現，但成本僅有後者的三分之一左右。這次發布標誌著 AI Agent 經濟結構的一個關鍵轉折：過去必須動用最貴旗艦模型才能完成的複雜自動化任務，如今中階定價即可搞定。

## 幾乎追平旗艦的基準成績

最直觀的數字對比：在自動化程式碼修復基準 SWE-bench Verified 上，Sonnet 5 拿下 63.2% 的分數；Opus 4.8 是 69.2%；上一代 Sonnet 4.6 只有 58.1%。短短四個月，Anthropic 就把中階與旗艦之間的差距縮小了約八成。

在知識性工作基準測試上，差距更是幾乎抹平：Sonnet 5 在複雜推理任務上甚至略微超越 Opus 4.8。對於大多數企業自動化工作流程——起草、摘要、研究與多步驟決策——Sonnet 5 已是效益最高的選擇。

相較前代模型最受矚目的改進，在於它完成多步驟複雜任務的能力大幅提升。早期版本的 Sonnet 面對複雜指令時，常常中途放棄，需要人工重新介入。Sonnet 5 則透過專門的訓練序列來解決這個問題，「即使沒有明確要求，也會主動檢查自己的輸出結果」。對於不允許人工干預的全自動流水線，這項行為改善等於消除了一整類故障模式。

## 重塑 AI Agent 成本結構的定價策略

Sonnet 5 推出時的定價為每百萬輸入 Token 2 美元、每百萬輸出 Token 10 美元，此優惠價格維持至 8 月 31 日。之後調整為每百萬輸入 3 美元、輸出 15 美元，仍低於 Opus 4.8 和 OpenAI 的 GPT-5.5。Gemini 3.5 Flash 定價更便宜，但 Anthropic 認為 Sonnet 5 的可靠性溢價物有所值。

對於搭建 AI Agent 系統的開發者而言，一次使用者互動可能跨越數十次工具呼叫、消耗數千萬個 Token，Opus 與 Sonnet 的定價差異絕非小事，而是決定產品能否有正向毛利的關鍵。自動化平台 Zapier 的工程師表示：「日常自動化任務根本不用考慮，直接用 Sonnet 5 就對了。」

Sonnet 5 即日起全面開放：取代前一代成為免費與 Pro 用戶的預設模型，Max、Team 與 Enterprise 方案也同步支援。同時陸續在 AWS Bedrock 上線，並將整合進 GitHub Copilot 及其他第三方平台。

## 把安全性當作產品功能

Anthropic 在發布說明中特別強調了 Sonnet 5 的安全改進，並將其定位為生產環境可靠性指標，而非合規成本。相較 Sonnet 4.6，新模型在拒絕惡意請求的準確率上有所提升，對提示注入攻擊（prompt injection）的抵抗力也更強——這在 Agent 部署場景中尤為重要，因為外部網頁、電子郵件或使用者上傳的文件都可能夾帶對抗性輸入。

幻覺（hallucination）與討好用戶（sycophancy）的發生率也雙雙下降。後者對企業應用尤為關鍵：模型若習慣性地迎合用戶而非糾正錯誤，就會在自動化流程中悄悄埋下隱患。代碼開發工具 Lovable 的共同創辦人就此評論道：「一個懂得何時說不的模型，跟一個懂得如何建構的模型同樣重要。」

在防範最高風險任務執行方面，Sonnet 5 的防護力尚未達到 Opus 4.8 的水準。但對絕大多數生產環境部署而言，其安全表現已是顯著進步。

## 時機背後的戰略意涵

這次發布對 Anthropic 而言意義重大。公司正朝 IPO 加速衝刺，最近完成 650 億美元 H 輪融資後估值升至 9650 億美元，超越 OpenAI 成為獨立 AI 實驗室中估值最高的一家。營收持續加速，企業 API 客戶的使用深度持續提升。

以 Sonnet 5 作為數百萬免費用戶的預設模型，同時達成兩個目標：讓消費者零成本體驗頂尖 AI Agent 能力，建立使用習慣與資料積累；同時為開發社群提供一個在商業上可行的定價切入點，無需談判企業合約即可打造生產級 Agent。

這也對競爭對手持續施壓：OpenAI 的 GPT-5.5 定價明顯更貴；Google 的 Gemini 3.5 Pro 已推遲至 7 月，截至本文發布時仍未上線。在成為自主軟體預設推理層的競爭中，Anthropic 將效能、價格與普及度整合進了同一個產品時刻。

## 展望未來

Anthropic 已明確表示將持續投入 Sonnet 系列，使其成為整個產品線的高用量主力。Opus 仍將是最高要求任務的首選——特別是安全性優先於成本的場景——但每一代發布都在縮小兩者之間的差距。

對整個開發者生態而言，Sonnet 5 的到來，恰逢 LangGraph、AutoGen 等 Agent 框架以及各類企業自建腳手架走向成熟的時刻。能在真實 Agent 任務上達到旗艦級推理能力、卻保持中階定價，或許將加速各行業——從法律到醫療再到金融服務——從實驗性試點邁向大規模生產部署的進程。

AI Agent 時代目前並不需要更好的旗艦模型。它需要的，是一個可靠且經濟實惠的中階選擇。Anthropic 剛剛交出了這份答案。
