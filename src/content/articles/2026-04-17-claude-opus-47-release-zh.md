---
title: "Claude Opus 4.7 重奪 AI 榜首：視覺能力大躍進，代理任務顯著提升"
summary: "Anthropic 於 4 月 16 日發布 Claude Opus 4.7，在幾乎所有主要基準測試上超越 GPT-5.4 與 Gemini 3.1 Pro。SWE-bench Verified 分數攀升至 87.6%，視覺準確率從 54.5% 飆升至 98.5%，全新「xhigh」算力層級讓模型能在數小時的自主工作流程中維持高強度推理，定價與前一代維持不變。"
category: "ai-ml"
publishedAt: 2026-04-17
lang: "zh"
featured: true
trending: true
sources:
  - name: "Anthropic"
    url: "https://www.anthropic.com/news/claude-opus-4-7"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/anthropic-claude-opus-4-7-coding-agentic-benchmarks-release"
  - name: "GitHub Changelog"
    url: "https://github.blog/changelog/2026-04-16-claude-opus-4-7-is-generally-available/"
tags:
  - "Claude"
  - "Anthropic"
  - "AI 模型"
  - "基準測試"
  - "代理 AI"
  - "視覺 AI"
relatedSlugs:
  - "2026-04-17-openai-cerebras-20b-chip-deal-zh"
  - "2026-04-15-anthropic-30b-revenue-google-broadcom-zh"
  - "2026-04-10-anthropic-claude-managed-agents-zh"
---

# Claude Opus 4.7 重奪 AI 榜首：視覺能力大躍進，代理任務顯著提升

Anthropic 於週三發布 Claude Opus 4.7，締造了該公司自 Opus 4 首發以來單代最大幅度的能力躍升。新模型在程式開發、代理推理與視覺任務的排行榜上全面領先——在企業開發者最關注的幾乎所有指標上超越 OpenAI 的 GPT-5.4 與 Google 的 Gemini 3.1 Pro——且定價與前代完全相同。

發布時機頗具意義。Anthropic 十天前剛披露年化營收突破 300 億美元，而前沿 AI 榜首之爭從未如此激烈：GPT-5.4 於今年三月初亮相，Gemini 3.1 Pro 緊隨二月登場，Opus 4.7 現在重新奪回 Anthropic 今年稍早失去的領先優勢。

## 基準數字一覽

成績難以輕描淡寫。在業界引用最廣的軟體工程評測 SWE-bench Verified 上，Opus 4.7 拿下 87.6% 的分數，Opus 4.6 則為 80.8%——單代提升近 7 個百分點。在 80% 至 90% 這個區間，每一個百分點的差距，代表的是模型能否應付幾乎所有真實工程票券的分野。

訓練集汙染程度更低的 SWE-bench Pro 漲幅更為陡峭：從 53.4% 躍升至 64.3%。模擬真實 IDE 多步驟程式編輯的 CursorBench 則從 58% 跳至 70%。OpenAI 現行旗艦 GPT-5.4 Thinking 在上述兩項評測的得分分別為 58% 與 62%。

在財務分析任務上——Anthropic 企業營收的重要來源——Opus 4.7 拿到 78.4%，GPT-5.4 Thinking 為 69.1%，Gemini 3.1 Pro 為 72.2%。Cursor 在發布後數小時即推送部落格文章，強調程式開發能力的提升；GitHub 已排定下週發表基準測試回應。

GPT-5.4 Thinking 目前仍在 MATH-500 等數學重度評測及競賽級定理證明上與 Opus 4.7 不相上下，甚至略勝一籌。但對多數開發者而言，這些指標的決策相關性遠低於程式開發與代理任務套件。

## 視覺能力全面重建

Opus 4.7 最戲劇性的進步在於視覺理解——直到仔細檢視測試方法之前，數字幾乎讓人難以置信。模型現在可處理長邊達 2,576 像素的圖片，是前代 Claude 版本上限的三倍以上。Anthropic 將視覺編碼堆疊描述為「全面重建」，而非漸進式改善。

基準測試結果直觀反映這一點：視覺任務準確率從 54.5% 飆升至 98.5%。上線前測試過模型的外部開發者也印證了這項改善。一位用印刷電路板（PCB）線路圖測試的工程師表示，Opus 4.7 能準確識別個別元件標籤並追蹤訊號路徑，而 Opus 4.6「基本上是在杜撰」。另一位用高密度財務報表測試的開發者指出，模型能正確解析和推理多欄資料，而這在之前的版本會系統性出錯。

對代理應用而言——模型必須讀取螢幕截圖、理解 UI 狀態並做出回應——這次視覺升級的影響可能是顛覆性的。以往需要多輪觀察-修正循環的電腦操作任務，現在許多都能一次完成。Anthropic 內部的電腦使用基準測試顯示，單次任務完成率從 51% 提升至 85%，增幅達 34%。

## 全新 xhigh 算力層級

Anthropic 同時推出名為「xhigh」的新算力層，插入現有的 high 與 max 之間。Anthropic 建議大多數程式開發和代理使用場景從 high 或 xhigh 開始，Claude Code 現在對所有訂閱方案均預設使用 xhigh。

這個新層級的設計邏輯反映了一個不那麼直觀的現象：在長時間代理對話中，當上下文密度極高、模型必須整合大量先前工具呼叫後才能行動時，有效推理深度往往會逐漸衰退，低於模型的理論上限。xhigh 設定的目的，正是讓模型在多小時的工作流程中持續維持高強度推理，而非隨對話延伸而退化。

根據 Anthropic 的基準測試，在 10 輪工具使用場景下，xhigh 設定的任務完成率比 high 設定高出 12%，算力消耗約多 30%。對生產級代理應用——客服自動化、自主程式審查、財務文件處理——這個成本效益比在多數部署場景下都是划算的。

## 安全與網路安全防護

Opus 4.7 內建網路安全防護機制，能自動偵測並阻擋涉及高風險安全用途的請求。Anthropic 未公開技術細節，大致描述為其憲法 AI（Constitutional AI）方法的演進。

時機選擇頗具針對性。OpenAI 上週推出 GPT-5.4 Cyber——一個針對攻擊性安全研究調校的特化版本——立即因其生成可用漏洞利用程式碼的能力引發爭議。Anthropic 採取了截然相反的定位：內建安全防護的通用模型，而非提供一個功能更強但限制較少的平行安全版本。

這種差異對企業採購決策者愈來愈重要。多位財星 500 大企業的採購主管告訴媒體，「雙版本」AI 產品——功能更強但受限較少的版本與一般版本並存——會使內部治理複雜化。

## 定價與供應情況

Opus 4.7 定價與前代完全相同：透過 Anthropic API 每百萬輸入 token 5 美元，每百萬輸出 token 25 美元。模型即日起可在 Claude.ai 各訂閱方案、Anthropic API、Amazon Bedrock、Google Cloud Vertex AI 及 Microsoft Azure AI Foundry 上取用。

對目前在生產環境執行 Opus 4.6 的開發者，Anthropic 的遷移文件建議優先測試代理提示詞。由於模型更強的中間推理可能改變工具呼叫的順序和內容——即便最終輸出相同——對預期輸出進行自動化迴歸測試可能出現偽失敗。建議改為針對任務完成結果而非精確輸出字串進行測試。

## 競爭時刻

這次發布讓 Anthropic 重新站上前沿模型排行榜榜首，此前 OpenAI 的 GPT-5.4 Thinking 和 Turbo 版本已大幅縮窄差距。領先幅度並不懸殊——兩家公司在多數基準上都在幾個百分點之內——但 Anthropic 同步在程式開發、視覺和代理任務取得全面進步，代表比競爭對手近期發布更為完整的能力推進。

更值得關注的是節奏本身：GPT-5.4 三月登場，Gemini 3.1 Pro 二月亮相，Opus 4.7 四月發布。曾經一年一度的前沿模型發布，現在以季度為週期，每代都帶來兩位數的基準提升。對正在評估要在哪個 AI 平台上深度押注的企業而言，這個速度讓長期平台鎖定成為一場危險的賭注——這也有助於解釋，為什麼 Anthropic、OpenAI 和 Google 都在競相加深工作流程整合和 API 黏著度，而不只是提升原始模型能力。

Opus 4.7 是 Anthropic 迄今對「能否在商業規模化的同時維持技術領先」這個問題給出的最有力回答。年化營收 300 億美元且持續成長，這家公司現在有足夠的資源繼續作答。
