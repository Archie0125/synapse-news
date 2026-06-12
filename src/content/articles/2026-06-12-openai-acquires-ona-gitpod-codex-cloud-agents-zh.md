---
title: "OpenAI 收購前身為 Gitpod 的 Ona，強化 Codex 雲端長程代理執行能力"
summary: "OpenAI 宣布收購雲端開發平台 Ona（前身為 Gitpod），讓旗下 Codex 程式代理能在安全的雲端沙盒中執行跨天任務。這是 OpenAI 2026 年的第六起收購案，也是對 Anthropic Claude Code 強勢攻佔企業開發市場的直接回應。"
category: "developer-tools"
publishedAt: 2026-06-12
lang: "zh"
featured: false
trending: true
sources:
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/06/11/openai-acquires-ai-agent-orchestration-startup-ona/"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-06-11/openai-to-acquire-cloud-platform-ona-to-support-ai-agents"
  - name: "OpenTools"
    url: "https://opentools.ai/news/openai-acquires-ona-cloud-startup-codex-2026"
tags:
  - "openai"
  - "codex"
  - "gitpod"
  - "開發工具"
  - "ai代理"
  - "企業併購"
  - "雲端運算"
relatedSlugs:
  - "2026-06-04-openai-codex-sites-role-plugins-enterprise-zh"
  - "2026-06-12-opencode-displaces-cursor-ai-coding-agent-zh"
  - "2026-06-11-cognition-devin-1b-26b-valuation-zh"
---

OpenAI 於 6 月 11 日宣布，已同意收購雲端開發平台 Ona——即 Gitpod 改名後的新身份。這筆金額未公開的交易，是 OpenAI 2026 年的第六起收購案，也是公司搶進 AI 輔助軟體開發基礎設施層的最新動作。交易仍待監管機關審查，完成日期尚未公布。

Ona 團隊將加入 OpenAI 的 Codex 部門，負責推動兩家公司技術的整合。外界普遍將此次收購解讀為 OpenAI 對 Anthropic Claude Code 在企業開發市場強勢擴張的直接回應。

## 從瀏覽器 IDE 到 AI 代理執行平台

Gitpod 由德國工程師 Johannes Landgraf 與 Christian Weichel 於 2020 年創立，核心價值主張簡單直接：讓開發者用一條連結，在瀏覽器裡秒速開啟完整設定好的雲端開發環境，省去本機建環境的繁瑣。這個看似低調的功能，讓 Gitpod 逐步累積超過 200 萬開發者用戶。

2025 年 9 月，公司更名為 Ona，策略重心大幅轉向——從服務人類開發者，轉為打造讓 AI 代理在雲端長時間自主執行任務的基礎設施：跑測試、重構程式碼、掃描漏洞，全程不需人類介入。轉型時機恰到好處：2026 年初，OpenAI 的 Codex 已累積超過 500 萬週活躍用戶，在全球約 4,700 萬名開發者中快速滲透。

然而，隨著代理能力提升，任務的複雜度與執行時長也水漲船高：一次框架遷移要跑一整週、一輪漏洞掃描得花三天、舊系統重構更是曠日持久。這些任務根本塞不進一個綁定到某台筆電、一關蓋就斷線的工作階段。這正是 OpenAI 花錢買 Ona 要解決的問題。

## 持久沙盒：代理永不下班

Ona 的核心技術提供安全的雲端沙盒環境，即使發起任務的開發者已關機離開，沙盒內的代理仍持續運作——編譯、測試、寫程式、呼叫外部 API——整夜或整個週末不停歇。開發者只需要在適當的節點非同步確認進度、提供方向修正，而非全程守著螢幕監督。

OpenAI 表示，Ona 將「提升 Codex 執行需要數小時乃至數天的長程任務能力」，並讓使用者在代理工作的關鍵節點更輕鬆地確認成果或調整方向。

安全架構同樣值得關注。Ona 沙盒採用密碼學雜湊驗證應用程式，而非僅依賴檔名——這意味著重新命名的惡意程式無法繞過防護。敏感憑證與執行環境分開保存，對外連線至高風險伺服器的行為則在基礎設施層直接封鎖。這些功能並非附加配件，而是核心賣點：企業安全團隊評估 AI 開發工具時，最常點名的兩大風險，正是憑證外洩與供應鏈污染。

本次收購延續了 OpenAI 今年以來的收購邏輯。今年 3 月，OpenAI 收購 Promptfoo，為 Codex 的 Frontier 安全平台增添自動化紅隊測試與漏洞掃描能力。Ona 的加入則把同樣的強化邏輯延伸到執行環境本身，讓企業客戶不只擁有一個聰明的程式代理，更有一套可在生產環境中實際部署的安全可觀測基礎設施。

## 對決 Claude Code 的基礎設施之戰

這筆收購的競爭意味不難看出。Anthropic 的 Claude Code 已成為企業軟體開發市場最具威脅的挑戰者，特別受到金融服務業與醫療機構青睞。根據 2026 年 5 月發布的市調數據，Claude Code 企業版授權量較前一年同期成長 340%。

OpenAI 的回應策略，是把 Codex 打造成獨立的全生命週期產品，而非 ChatGPT 的功能附件。Ona 讓 Codex 擁有一個由 OpenAI 端對端掌控的專屬執行基礎設施，無需依賴開發者自行搭建環境。這也使 Codex 差異化於雲端原生對手：Google Gemini Code Assist 深度綁定 Google Cloud Run，GitHub Copilot Workspace 依賴 Azure DevOps 管道；而 Ona 的架構與雲端服務商無關，可在任何主流平台上運行，符合企業採購團隊日益重視的靈活性需求。

## 現有用戶何去何從

Ona 工程師將整合進 OpenAI 的 Codex 部門。OpenAI 尚未宣布既有 Ona 訂閱用戶的遷移計畫，也未說明 Ona 是否會繼續作為獨立產品運營。2025 年從 Gitpod 更名為 Ona 時已流失部分用戶轉向 Codeflare 和 Daytona，此次收購讓 Ona 現有客戶對長期產品規劃更加關注。

## 基礎設施地盤爭奪進入深水區

OpenAI 2026 年的一系列收購——涵蓋安全強化（Promptfoo）、執行基礎設施（Ona）以及更早的語音與硬體交易——折射出一個深刻判斷：模型能力本身已不再是頂尖 AI 公司的核心區隔點。Anthropic、Google、微軟與 OpenAI，都在全力搶進讓模型在真實生產環境發揮效用的周邊層：記憶體管理、沙盒隔離、可觀測性，以及銜接代理與企業系統的協作層。

AI 程式助理市場正進入整合階段。第一代工具在 IDE 裡提供程式建議；第二代工具（Cursor、Devin、Claude Code）執行更長的自主任務；正在成形的第三代，以 OpenAI 打造中的 Codex+Ona 為代表，是將持久的雲端代理放在軟體開發生命週期的核心，在自然的節點向人類確認，而非每一行程式都等待批准。

Codex 週活躍用戶持續增長，Ona 提供的持久雲端執行能力讓 OpenAI 在企業軟體開發市場（全球規模估計逾 6,500 億美元）的競爭格局中取得了更穩固的基礎設施護城河。
