---
title: "中國 Z.ai 推出 ZCode：以 Claude Code 一半價格挑戰全球 AI 程式設計市場"
summary: "中國 AI 實驗室 Z.ai（智譜 AI）於 7 月 2 日發布 ZCode，一款基於 MIT 授權 GLM-5.2 模型的免費 AI 程式設計 IDE。該模型在 SWE-bench Pro 評測中超越 GPT-5.5，完全使用華為昇騰晶片訓練，月費低至 16 美元，全面挑戰西方競爭對手。"
category: "developer-tools"
publishedAt: 2026-07-08
lang: "zh"
featured: true
trending: true
sources:
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/z-ai-launches-zcode-to-challenge-cursor-claude-code-and-github-copilot-in-ai-coding"
  - name: "The Decoder"
    url: "https://the-decoder.com/zhipu-ai-launches-zcode-to-challenge-claude-code-and-openai-codex-at-a-fraction-of-the-cost/"
  - name: "南華早報"
    url: "https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic"
  - name: "Techzine Global"
    url: "https://www.techzine.eu/news/devops/142702/z-ai-takes-on-cursor-and-claude-code-with-free-zcode/"
tags:
  - "ZCode"
  - "智譜AI"
  - "GLM-5.2"
  - "程式設計工具"
  - "開源"
  - "中國AI"
  - "開發者工具"
  - "AI Agent"
relatedSlugs:
  - "2026-07-07-chinese-ai-models-openrouter-60-percent-dominance-zh"
  - "2026-04-04-cursor-devin-war-zh"
  - "2026-04-04-mcp-protocol-explosion-zh"
---

2026 年 7 月 2 日，中國 AI 實驗室智譜 AI 旗下的國際品牌 Z.ai 正式推出 ZCode——一款跨平台的智能程式設計開發環境，底層驅動模型為旗艦大模型 GLM-5.2。這款工具劍指 Cursor、Claude Code、GitHub Copilot 以及 Google 的 Antigravity 平台，挑戰意圖相當明確：在評測成績上超越 GPT-5.5，在定價上全面壓制所有西方競品。

## 在真實程式設計評測中擊敗 GPT-5.5

GLM-5.2 是一個約 7530 億參數的混合專家（MoE）架構模型，於 2026 年 6 月 13 日以 MIT 授權發布。在 SWE-bench Pro 這個最受業界重視的程式設計能力評測中——該評測使用真實 GitHub Issue 作為測試題目——GLM-5.2 得分 62.1%，高於 GPT-5.5（58.6%）與上一代 GLM-5.1（58.4%）。模型支援 100 萬 token 的超長上下文視窗，能夠在單次對話中掌握整個大型程式碼庫，不必依賴容易造成理解斷裂的分段策略。

若這份評測成績在真實生產環境中得到驗證，其意義相當重大。SWE-bench Pro 以難以「刷榜」著稱，題目源自真實開源專案的 Issue，正是開發者每天面對的那種複雜、脈絡豐富的問題。能在此評測突破 60% 門檻，代表 GLM-5.2 已達到直至 2025 年初才屬於閉源前沿模型的能力水準。

## ZCode 到底是什麼

ZCode 不是一個模型本身，而是一個將 GLM-5.2 嵌入開發者工作流程的「協作框架」（harness）。這款免費桌面應用支援 macOS、Windows 與 Linux，形態上類似 Cursor 的 Composer 或 Claude Code 的終端 Agent，核心特性包括：

- **自主編輯與終端執行**：ZCode 能自主讀取、修改、建立檔案並執行測試指令，不需逐步人工審批——這種 Agent 模式由 Claude Code 的 Agentic Mode 率先普及。
- **自帶金鑰（BYOK）**：開發者可在 ZCode 前端接入自己的 API 金鑰，連接 Anthropic 或 OpenAI 的模型。換言之，ZCode 也可以作為多後端的中立 IDE 介面。
- **開放權重、可本地部署**：GLM-5.2 的模型權重在 HuggingFace 與 ModelScope 均可取得，MIT 授權無地區限制。對於有足夠 GPU 算力的企業，整個堆疊（模型加 Agent）均可完全在本地運行，這是目前西方任何達到同等評測水準的程式設計工具都無法提供的能力。
- **7 月限時 1.5 倍配額加成**：7 月底前，透過 GLM Coding Plan 使用 GLM-5.2 將享有 0.67 倍計費係數，實際可用額度提升約 50%。

在定價方面，ZCode 的標準方案月費為 16.20 美元，頂級 Max 方案為 144 美元，低於 Cursor Pro（20 美元起），更大幅低於 Claude Code 或 GitHub Copilot Enterprise 的企業授權費用。

## 令人意外的硬體故事

GLM-5.2 技術文件中最具戰略意義的細節，可能是這句話：該模型**完全使用華為昇騰晶片訓練**，整個訓練過程中未使用任何美國硬體。這使 Z.ai 成為首批能夠在不依賴 Nvidia 出口管制 GPU 的情況下，訓練出超越 GPT-5.5 主流評測表現的前沿 AI 實驗室之一。

這一結果的意涵遠超出中國本身。對於任何在晶片出口管制框架下尋求替代方案的國家或企業而言，Z.ai 的成果提供了一個有力的概念驗證：純國產硬體堆疊同樣能夠支撐前沿 AI 能力。

## 西方市場的回應

Z.ai 將 ZCode 定位為直接挑戰 Cursor、Claude Code、GitHub Copilot 與 Google Antigravity。每個競爭對手都有其弱點：

- **Cursor** 以精緻的使用者體驗和深度 IDE 整合贏得開發者信任，但其模型層依賴 Anthropic 與 OpenAI 的第三方前沿模型。如果 ZCode 能以八折的價格提供相當的輸出品質，對成本敏感的工程團隊而言會形成相當吸引力。
- **Claude Code** 是 Anthropic 自有產品，估計年化營收在 2026 年 2 月已達 25 億美元，但定價面向企業預算，而驅動其核心優勢的 Claude Fable 5 自 7 月 8 日起也已轉為付費附加功能。
- **GitHub Copilot** 的用戶規模最大，但企業授權費用一直是中小型團隊的摩擦點。

BYOK 功能也帶來有趣的混用場景：開發者可在需要最高模型品質時，使用 Z.ai 的 Agent 前端搭配 Claude 或 GPT-4 後端；在需要壓低 Token 成本或希望程式碼不落入美國管控基礎設施時，切換至 GLM-5.2。

## 地緣政治背景

ZCode 的上市恰逢外界對中國 AI 的高度關注期。CNBC 上週確認，自 2026 年 2 月以來，美國企業 30% 至 46% 的 AI Token 使用量流向中國模型，這一數字令部分美國立法者感到警覺。此外，美國政府及多家企業軟體廠商已開始將中國模型 API 的使用列為潛在的資料主權風險，商務部也在研議進一步的模型出口管制措施。

Z.ai 顯然已預判這波壓力。選擇 MIT 授權、不附加地區限制，是一個刻意的訊號：ZCode 在法律上可在任何地區使用，開放的模型權重也允許任何組織自行審查模型內容。但對於高度監管行業而言，這是否足夠，仍有待觀察。

## 值得持續關注的三個關鍵

ZCode 能否真正威脅西方 AI 程式設計工具的主導地位，取決於三個因素：

**一、真實生產環境的表現**。SWE-bench Pro 成績固然有意義，但開發者最終效忠的是在實際工作流中感覺流暢、可靠的工具。ZCode 需要第三方針對多元程式碼庫的獨立驗證。

**二、資料落地的顧慮**。BYOK 部分緩解了資料主權問題，但 ZCode 的預設配置會將請求路由至 Z.ai 在中國的伺服器。企業的大規模採用，特別是在亞洲以外地區，將取決於 Z.ai 能否提供符合 GDPR 或 FedRAMP 要求的託管方案。

**三、生態系整合深度**。Cursor 的護城河有部分來自其 VS Code 外掛生態。ZCode 目前以獨立桌面應用形式推出，IDE 外掛支援將大幅擴展其潛在用戶群。

這家清華大學學術團隊創立的 AI 實驗室，過去五年一直嘗試進入全球市場。如今，憑藉一個前沿量級的開放權重模型、一款免費的開發者工具，以及全面壓制西方競品的定價，Z.ai 或許終於找到了打入全球市場的切入點。
