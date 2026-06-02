---
title: "微軟 Build 2026：Project Polaris 擺脫 OpenAI 依賴，Windows 正式成為 AI 代理平台"
summary: "微軟在 6 月 2 日的 Build 2026 主題演講中，宣布以自研 AI 編程模型 Project Polaris 取代 OpenAI GPT-4 Turbo，作為 GitHub Copilot 的預設引擎，最快 2026 年 8 月上線。演講同時宣布 Windows 代理框架開源、Azure Agent Mesh 上線，以及 Copilot Workspace 正式發布，標誌著微軟全面擁抱代理式運算的策略轉折。"
category: "developer-tools"
publishedAt: 2026-06-02
lang: "zh"
featured: false
trending: true
sources:
  - name: "ChatForest — Build 2026 Recap"
    url: "https://chatforest.com/builders-log/microsoft-build-2026-recap-windows-agent-platform-project-polaris-copilot-workspace/"
  - name: "Windows News — 自研 AI 模型將驅動 GitHub Copilot"
    url: "https://windowsnews.ai/article/microsoft-build-2026-homegrown-ai-models-to-power-github-copilot.420887"
tags:
  - "微軟"
  - "Build 2026"
  - "Project Polaris"
  - "GitHub Copilot"
  - "AI 代理"
  - "Windows"
  - "Azure"
  - "開發者工具"
relatedSlugs:
  - "2026-06-01-microsoft-build-2026-mai-coding-models-zh"
  - "2026-06-01-github-copilot-ai-credits-billing-change-zh"
---

微軟執行長 Satya Nadella 在 6 月 2 日 Build 2026 主題演講的開場說了一句話，放在兩年前聽起來像是誇大其詞，如今卻像是對現狀最平實的描述：「Windows 不再只是人類使用者的平台。代理（Agent）現在是這個系統的一等公民——無論是在執行環境、工具鏈，還是分發模式上。」

在舊金山 Fort Mason Center 登場的這場會議，以一系列宣告兌現了這個定調——這是 Windows 與開發者工具自雲端轉型以來最重大的一次平台躍遷。

## Project Polaris：微軟的自研 AI 編程模型

最受矚目的宣告是 **Project Polaris**——微軟自主研發的 AI 編程模型，設計目標即是取代 OpenAI GPT-4 Turbo，成為 GitHub Copilot 的預設引擎。替換預計於 **2026 年 8 月**生效，所有 Copilot 訂閱者將自動遷移，希望保留 GPT-4 的工程團隊則有三個月的選擇退出緩衝期。

這是一步具有重大戰略意涵的棋。GitHub Copilot 如今活躍用戶數以千萬計，自創立以來一直由 OpenAI 模型驅動。微軟決定以內部研發的模型替換核心引擎，標誌著謀求 AI 基礎設施獨立的方向已從傳聞成為現實。

Polaris 採用**混合專家（MoE）架構**，內含針對不同程式語言與框架調校的專業子模組。微軟的基準測試顯示，Polaris 在 HumanEval 和 MBPP 編程基準上均勝過 GPT-4 Turbo，在 Rust、Haskell 等訓練資料相對匱乏的「低資源語言」上進步尤為顯著——那正是通用語言模型向來表現較弱的區域。

**Pro 版訂閱者**可使用多檔案上下文，支援最高 **10 萬行程式碼**的跨檔推理，讓模型能針對整個服務或子系統進行分析，而非只能聚焦單一檔案。自主生成測試（Autonomous Test Generation）也在 Pro 版中上線——模型會主動偵測覆蓋不足的區域並自動補寫測試，無需開發者提示。Polaris 運行於微軟 Azure 的 Maia AI 加速器上，微軟表示這降低了推論延遲並削減了相較於呼叫 OpenAI API 的運算成本。

伴隨 Polaris 一同推出的還有 **Code Content Guarantee**（程式碼內容保障）——為客戶因 Copilot 程式碼建議引發的智慧財產權索賠提供賠償擔保，直接化解了部分企業客戶長期對部署 Copilot 的顧慮。

## Windows 成為代理平台：全棧宣告

Polaris 之外，Build 2026 還交付了微軟多年來布局的完整代理基礎設施：

**Windows Agent Framework** 正式開源。它提供了作業系統層面讓代理與應用程式互動、管理檔案系統、呼叫 API、執行多步驟任務的核心原語。開源意味著第三方開發者可以在這套原語之上打造原生整合 Windows 的代理，而非依靠瀏覽器自動化或螢幕截圖等繞道方式。

**Azure Agent Mesh** 是新推出的多代理協調雲端服務，讓運行在不同 Azure 服務——甚至不同提供商——的代理能以標準化方式溝通、委派任務和共享狀態。它被定位為企業部署中的連接層，處理合約分析、程式碼審計、保單理賠處理等需要跨多個專業代理協作的複雜任務。

**Copilot Workspace** 從擴大測試正式轉為全面可用（GA）。這個功能讓開發者用自然語言描述 Bug 或功能需求，由 Copilot 生成計畫、跨儲存庫修改檔案並開啟 Pull Request。微軟透露，在測試期間 Copilot Workspace 處理了超過 4,000 萬次檔案編輯，全程無需開發者撰寫初始程式碼。

**Office 365 Copilot Agent Mode** 現已成為 Word、Excel 和 PowerPoint 的**預設模式**，不再等待用戶提示，而是主動根據文件內容與近期活動浮現建議、草稿與分析。用戶仍可關閉 Agent Mode，回到傳統的助手行為。

**電腦使用代理（CUAs）**、代理對代理通訊，以及即時語音介面，三項功能在 Copilot Studio 中同步從預覽轉為正式發布（GA）。

## 獨立化的戰略棋局

綜觀 Build 2026 的全貌，微軟展現的是：花了三年時間將 OpenAI 技術深度整合進產品的同時，也在系統性地為最關鍵的環節建構替代能力。Project Polaris 是最顯眼的例子，但支撐 Polaris 推論的 Maia AI 加速器、開源的 Windows Agent Framework，以及 Azure Agent Mesh，都代表了降低對單一外部供應商依賴的自主能力。

對台灣開發者而言，Build 2026 的核心意涵在於：Windows 平台的代理化已進入實作階段。Windows Agent Framework 的開源，讓在地開發者能以作業系統層級的原語打造更深度整合的代理應用，而非只能在 Web 瀏覽器或 Electron 容器中湊合。GitHub Copilot 轉換至 Polaris 的過渡期（8 月上線，3 個月選擇退出），也是評估 Polaris 對台灣企業常用技術棧（特別是 TypeScript、Python、Java、Go）表現的最佳時間窗口。

2026 年 8 月的 Polaris 正式上線，將是真正的測試。如果模型表現符合基準測試預期，Code Content Guarantee 也確實降低了企業對 IP 風險的顧慮，Copilot 的企業採用有望在微軟需要的時間點加速，為公司龐大的 AI 基礎設施投資交出成績單。
