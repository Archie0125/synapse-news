---
title: "OpenAI Codex 新功能：只需示範一次，AI 就能重複該任務"
summary: "OpenAI 在 Codex 應用程式第 26.616 版中推出了「Record & Replay」功能，讓 AI 智能體觀察使用者完成一次工作流程示範後，將其轉換為可隨時調用的可重用「技能」。這項功能向付費 ChatGPT 訂閱者（macOS 平台）開放，歐盟、英國和瑞士用戶除外，代表著無程式碼自動化領域的重要突破，有望縮短企業 RPA 工具與對話式 AI 智能體之間的差距。"
category: "developer-tools"
publishedAt: 2026-06-23
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "The Decoder"
    url: "https://the-decoder.com/openais-codex-can-now-watch-you-work-once-and-repeat-the-task-forever/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/318759/20260620/openai-codex-automation-gains-record-replay-show-it-once-skip-script.htm"
  - name: "OpenAI Developers"
    url: "https://developers.openai.com/codex/record-and-replay"
  - name: "AI Weekly"
    url: "https://aiweekly.co/alerts/openai-adds-record-replay-to-codex-for-macos-business-users"
tags:
  - "OpenAI"
  - "Codex"
  - "工作流程自動化"
  - "AI 智能體"
  - "開發者工具"
  - "電腦使用"
  - "RPA"
  - "無程式碼"
relatedSlugs:
  - "2026-06-12-openai-acquires-ona-gitpod-codex-cloud-agents-zh"
  - "2026-06-04-openai-codex-sites-role-plugins-enterprise-zh"
  - "2026-06-11-anthropic-2026-agentic-coding-trends-report-zh"
---

企業工作流程自動化最大的阻力，從來不是自動化本身——而是向工具描述自動化的過程。UiPath、Automation Anywhere 等機器人流程自動化（RPA）工具多年來就提供錄製與重播功能。它們的錄製內容捕獲的是座標和介面元素，介面一變動就會失效。

OpenAI 於 6 月 18 日在 Codex 應用程式第 26.616 版中發布的 Record & Replay 功能採取了不同方式：給智能體看你想做什麼，讓它自己找出方法。

## Record & Replay 的運作原理

這個機制在概念上很直接，但在實作層面意義深遠。用戶啟動錄製模式，像往常一樣完成他們的工作流程——開啟應用程式、輸入資料、瀏覽介面、提交表單——同時 Codex 在一旁觀察。當用戶停止錄製後，Codex 分析動作序列，識別底層意圖和模式，並將示範轉換為可重用的「技能」。

此後任何時候都可以按名稱呼叫該技能，由 Codex 智能體透過電腦使用（Computer Use）、瀏覽器自動化、插件 API 或任何可用工具的組合來執行工作流程。每次被呼叫時，工作流程都會自主運行——無需重新示範。

OpenAI 的文件說明生成的技能可以進一步調整：用戶可以要求進一步微調，例如點明命名慣例、欄位預設值或決策點等隱性偏好，並在每次執行時提供新的值，例如要上傳的不同檔案。

## 電腦使用作為基礎設施層

Record & Replay 建構在電腦使用（Computer Use）之上——這是 OpenAI 用於讓智能體像人類用戶一樣與電腦介面互動（而非透過 API）的框架。電腦使用讓 Codex 能代替用戶操控桌面應用程式。

與記錄座標的傳統 RPA 巨集不同，Record & Replay 會產生技能描述，由 Codex 的語言模型在重播時加以解讀。

Record & Replay 運作所需的電腦使用功能，意味著這項功能只在已部署電腦使用的平台上可用。從第 26.616 版開始，這包括 macOS；Windows 或 Web 存取的版本尚不支援此功能。電腦使用自 6 月 16 日起已在歐盟地區開放，但 Record & Replay 本身在歐盟、英國和瑞士尚未推出，OpenAI 也未公開說明兩者之間的差異。

## RPA 的對比——以及差異所在

UiPath、Automation Anywhere 等企業 RPA 工具多年來就提供錄製與重播功能，對比頗具啟發性。這些平台也提供「錄製」模式，讓用戶執行任務後工具生成機器人定義。根本的區別在於錄製和執行之間發生了什麼。

傳統 RPA 錄製的是字面意義上的螢幕座標、元素識別符和像素位置。更改瀏覽器視窗大小、更新應用程式的 UI，或移動一個按鈕，機器人就會崩潰。

Codex 的 Record & Replay 從示範工作流程的語義理解中生成技能，而非捕獲脆弱的座標。智能體觀察用戶試圖完成什麼——上傳帶有元數據的影片、提交費用報告、建立專案工單——並將該意圖編碼為一種能夠適應介面輕微變化而不會崩潰的形式。

## 實際應用場景

OpenAI 的文件和示範重點介紹了幾個代表性使用案例：

**內容發布。** 錄製 YouTube 影片上傳工作流程，包括中繼資料、縮圖和字幕，並將其轉換為 Codex 可重複執行的技能。

**費用管理。** 捕獲在企業入口網站中提交費用報告的過程，並將其轉換為可重複的技能，以便在新費用到來時自動處理。

**定期資料擷取。** 示範如何下載定期報告，並將其轉換為可重複使用的技能。

**工單和問題建立。** 錄製建立一個配置正確的問題單的過程，並將其轉換為可重複使用的技能。

**預訂和訂位。** 捕獲企業設施應用程式中的停車位預訂工作流程，並將其轉換為可重複執行的任務。

統一的主題是 OpenAI 所描述的「比描述更容易展示的穩定、可重複工作流程」。這是對當前智能體編排中真實局限性的務實承認：精確的自然語言描述複雜的多步驟工作流程，往往比直接做這件事更難，而且描述常常無法捕捉讓自動化正確運行所需的邊緣情況和序列依賴關係。

## 地理限制與競爭格局

歐盟、英國和瑞士不在 Record & Replay 初始版本的適用範圍內，OpenAI 尚未公開說明原因，也未提供擴大開放的時程。電腦使用涉及捕獲螢幕內容，其中可能包含個人資料、用戶憑證和專有資訊。

工作流程自動化的競爭格局非常活躍。Record & Replay 採取基於示範的方式：用戶不必在提示中描述工作流程，而是在 Codex 旁觀時親自執行任務，由 Codex 據此草擬技能。

## 對開發者工作流程的意義

示範一次工作流程就能讓它成為可重用的智能體技能，也改變了以往不值得投資撰寫腳本的一次性自動化的計算邏輯。如果自動化的成本是一次示範而非數小時的腳本撰寫和測試，值得自動化的門檻就大幅降低——這有望從根本上改變開發者和知識工作者思考整類重複性電腦輔助工作的方式。

在 Codex API 基礎上開發的團隊，有可能從人類主題專家身上捕獲特定領域的工作流程，並將其作為可重用技能在整個組織中部署——如果這一能力能夠大規模可靠運作，代表著制度性知識被編碼進軟體系統方式的一次重大加速。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 24 處。*
