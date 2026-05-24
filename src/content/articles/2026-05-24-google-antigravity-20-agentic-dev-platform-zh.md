---
title: "Google Antigravity 2.0：以代理人為核心的開發平台，想要取代你的 IDE"
summary: "Google 在 I/O 2026 發布了 Antigravity 2.0，一套獨立的代理人優先開發平台，包含桌面應用程式、CLI、SDK 和託管執行環境。不同於傳統 AI 程式碼輔助工具，Antigravity 將代理人視為軟體開發的主要介面，實現多代理人編排、非同步任務管理，以及跨編輯器、終端機和瀏覽器的自主驗證。"
category: "developer-tools"
publishedAt: 2026-05-24
lang: "zh"
featured: false
trending: false
sources:
  - name: "Google Developers Blog"
    url: "https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/google-antigravity-2-desktop-cli-sdk-io-2026"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/05/19/google-accelerates-agent-native-software-development-expanded-antigravity-platform/"
tags:
  - "google"
  - "developer-tools"
  - "agentic-ai"
  - "ide"
  - "coding-agents"
relatedSlugs:
  - "2026-05-24-google-gemini-35-flash-agentic-model-zh"
  - "2026-05-17-code-with-claude-2026-managed-agents-zh"
---

過去三年，開發者工具的故事是一場穩健的漸進式增添：這裡加一個 Copilot、那裡加一個自動補全、在開發者早已熟悉的編輯器旁邊再嵌入一個聊天面板。工具愈來愈好，但底層模型始終沒變——人類坐在駕駛座上，AI 負責給建議。

Google 在 I/O 2026 發布的 Antigravity 2.0，是一個更為激進的命題。它不試圖在現有的編輯器上疊加代理人能力，而是從「代理人應當成為開發的主要介面」這個前提出發，從零開始建構一個圍繞這一假設的平台。

成果是一款獨立的桌面應用程式——支援 macOS、Windows 和 Linux——搭配命令列介面、開發者 SDK，以及 Gemini API 中的託管執行環境，整個系統圍繞一個核心理念組織：開發者應該在**任務和目標**的層次上操作，而不是在個別檔案編輯和指令執行的層次上。

## 核心架構：任務優先於檔案

傳統 IDE 以檔案為中心。你打開專案、導航到檔案、編輯行、運行測試、提交更改。AI 程式碼助手在這個模型上疊加了補全和重構功能，但仍在檔案範式之內運作。Antigravity 2.0 顛倒了這個邏輯：工作的主要單位是**任務**，由代理人自行判斷需要打開、修改和驗證哪些檔案來完成它。

2.0 版的關鍵架構原語是**子代理人**（subagents）、**鉤子**（hooks）和**非同步任務管理**。子代理人允許主代理人生成並行工作者來處理獨立子任務——一個調查失敗的測試、另一個查閱 API 文件、第三個生成草稿實作——其結果被合成為一致的輸出。鉤子讓開發者定義觸發條件：當代理人遇到特定情況時，應自動發生什麼。非同步任務管理意味著開發者可以提交任務後離開，等待收到完成通知，而不必監督每一個步驟。

這三個原語共同實現了一種與現有 AI 程式碼工具在質地上截然不同的工作流程。開發者可以描述一個功能——「用 OAuth 2.0 支援實作使用者認證、寫單元測試，並更新 API 文件」——Antigravity 的代理人將規劃工作、分配給子代理人、跨編輯器/終端機/瀏覽器執行、驗證結果，然後提交完成的工作供審查。開發者的角色從執行者轉變為審查者。

## 知識庫：會學習的代理人

Antigravity 2.0 中一個引發開發者關注的細節是**知識庫**原語。不同於將每個工作階段視為白板的無狀態程式碼助手，Antigravity 代理人可以持久保存上下文、程式碼片段、文件筆記和架構決策到跨工作階段持久存在的知識庫中。

這對長期運行的專案意義重大。開發者一旦解釋了專案使用自訂事件匯流排模式、偏好函數式而非物件導向風格，或有特定的錯誤處理慣例——這些資訊就成為代理人持久上下文的一部分。未來的任務將自動繼承這些約束，無需開發者在每次對話中重新建立。

知識庫也可以透過 Antigravity SDK 程式化填充，讓團隊在代理人開始工作之前預先載入特定於專案的文件、內部 API 參考資料和風格指南。對企業用例而言，這將平台從通用程式碼助手轉變為更接近具備機構知識的「已入職的團隊成員」。

## 模型彈性與跨提供商支援

Antigravity 2.0 最令人意外的方面之一，是它明確支援競爭提供商的模型。平台以 Gemini 3.5 Flash 和 Gemini 3 Pro 為主力模型提供慷慨的速率限制，但同時也在同一介面中支援 Anthropic 的 Claude Sonnet 4.5 和 OpenAI 的 GPT-OSS。開發者可以按任務配置使用哪個模型，或讓平台根據任務類型自動選擇。

這是一個刻意為之的策略。Google 的賭注是：**平台**——工具鏈、工作流程、部署基礎設施——才是黏性層，而不是模型本身。透過支援競爭性模型，Antigravity 降低了在其他場景中已使用 Claude 或 GPT 的開發者的遷移成本，同時讓 Google 的模型保持在大多數用戶不會更改的預設位置。

這個動作與 Amazon Bedrock 在 AWS 端的模型選擇處理方式如出一轍：雲端和工具基礎設施是護城河，模型可攜性是特性而非威脅。

## CLI 與 SDK：無頭化與可嵌入

對不喜歡 GUI 的開發者，Antigravity 提供了一個一流的 CLI，可從終端機完整存取平台的代理人編排能力。CLI 設計為與現有 CI/CD 管道整合——任務可以由合併請求、失敗的測試套件或排程的 cron 任務觸發，結果自動提交到分支並建立拉取請求。

Antigravity SDK 讓開發者以程式化方式控制代理人行為，允許自訂工具、數據連接器和執行環境被註冊並提供給平台內的代理人。SDK 整合了 Google AI Studio（用於模型配置）、Firebase（用於狀態持久化和即時更新），以及 Cloud Run（用於代理人管理服務的無伺服器部署）。

Android 擴展是一項值得注意的新功能。穩定版 Android CLI 讓 Antigravity 代理人可以直接與 Android Studio 互動，執行下載 Android SDK、配置模擬器和在連接設備上運行應用程式等任務。對行動開發者而言，這意味著同樣的任務導向工作流程現在可以延伸至原生 Android 開發。

## 企業部署與安全性

Antigravity 2.0 透過 Gemini Enterprise Agent Platform 提供企業支援，具備在受監管環境中生產部署所需的合規和安全功能，包括代理人行動的審計日誌、知識庫內容的角色存取控制，以及可配置的代理人工具調用策略。

對 Google 的企業客戶而言，Gemini Enterprise Agent Platform 整合將 Antigravity 連接到更廣泛的 Google Workspace 生態系統。代理人可以讀寫 Google Drive 和 Docs、將 Google Sheets 作為數據來源進行互動，並觸發 Google Cloud 工作流程——這些能力顯著擴展了代理人能夠完成的工作範圍，無需開發者在開發環境和協作層之間手動橋接。

## 可用性與定價

Antigravity 2.0 從 I/O 發布日起以公開預覽版提供，個人使用免費，具有慷慨的模型使用限制。企業定價透過 Google Cloud 和 Gemini Enterprise Agent Platform 提供。

公開預覽的框架很重要：Google 明確邀請開發者對新原語提供反饋，尤其是子代理人編排行為和知識庫功能。鑑於 Antigravity 直接競爭 Anthropic 的 Claude Code、Cursor 和 GitHub Copilot Workspace——這些工具都已擁有相當大的開發者採用規模——Google 根據早期用戶反饋快速迭代的能力，將是決定平台能否取得主流採用的關鍵因素。

## 競爭格局

這次發布恰逢代理人 IDE 類別正被激烈競爭的時刻。Claude Code 以 CLI 優先的代理人程式設計工具在專業開發者中取得了強勁的採用。Cursor 的 AI 優先編輯器吸引了大量希望 AI 更深入編輯迴圈的用戶群。GitHub Copilot Workspace 和 Devin 則以不同方式處理任務層面的代理人軟體開發。

Antigravity 2.0 是 Google 迄今為止在這個領域以第一方、完全整合平台最直接的競爭嘗試。其優勢是整合深度——尤其是在 Android 開發和 Google Cloud 部署方面——以及規模化利用 Google 模型基礎設施的能力。其挑戰與 Google 在開發者工具上普遍面臨的問題相同：信任。開發者在工具選擇上是保守的，說服他們採用一個新的主要開發環境，需要的是可靠性的證明，而不僅僅是主題演講上令人印象深刻的展示。

平台對 Anthropic 和 OpenAI 模型的支援，從這個角度來看是一個聰明的讓步：它降低了採用門檻，讓開發者可以在新的環境中繼續使用熟悉的模型，同時押注平台體驗足夠引人注目，讓他們在初始遷移之後持續保持投入。
