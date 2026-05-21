---
title: "Google I/O 2026：Gemini Spark 永不停機的 AI 代理、Omni 世界模型，以及最大膽的訂閱佈局"
summary: "Google I/O 2026 大會推出了 Gemini 3.5 Flash（速度快 4 倍、成本更低）、全天候背景代理 Gemini Spark、多模態世界模型 Gemini Omni，以及月費 100 美元的 AI Ultra 方案。這場發表會傳遞了一個清晰訊號：Google 要同時贏得最便宜和最強大這兩場仗。"
category: "ai-ml"
publishedAt: 2026-05-21
lang: "zh"
featured: true
trending: false
sources:
  - name: "Google Blog – 100 Things We Announced at I/O 2026"
    url: "https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/"
  - name: "CNBC – Google debuts new AI models at I/O 2026"
    url: "https://www.cnbc.com/2026/05/19/google-ai-ultra-gemini-spark-omni.html"
  - name: "Latent Space – Google I/O 2026 Recap"
    url: "https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash"
tags:
  - "Google"
  - "Gemini"
  - "AI 代理"
  - "Google I/O"
  - "Gemini Spark"
  - "Gemini Omni"
  - "開發者工具"
relatedSlugs:
  - "2026-05-21-google-io-2026-gemini-spark-recap-en"
  - "2026-05-15-google-io-2026-preview-gemini-android-zh"
  - "2026-05-15-google-gemini-omni-video-model-leak-zh"
---

每年的 Google I/O 都在為整個科技產業定調，今年的基調比以往更加清晰：AI 競賽的主戰場，不再只是模型能力的排名，而是誰能把 AI 代理送到最多人手中、以最低的成本、全天候不間斷地運行。

5 月 19 日，Sundar Pichai 站上加州山景城 Shoreline Amphitheatre 的舞台，帶來了近年來內容最密集的一場 I/O 主題演講。四條主線貫穿全場：旗艦級效能卻以 Flash 定價的新模型、趁你睡覺時持續工作的個人 AI 代理、影片世界模型，以及為高端用戶重新設計的訂閱架構。

## Gemini 3.5 Flash：旗艦效能、Flash 定價

本場最核心的模型發表是 Gemini 3.5 Flash。Google 主張這款「輕量」模型在程式碼編寫與代理任務基準測試上，實際超越了上一代旗艦 Gemini 3.1 Pro，同時運行速度快約 4 倍。

定價方面：每百萬輸入 token 1.50 美元、每百萬輸出 token 9.00 美元，快取輸入為每百萬 0.15 美元。這約是 Gemini 3 Flash 定價的 3 倍，但 Google 認為，由於模型本身需要更少 token 完成複雜任務，整體使用成本依然具有競爭力。

Gemini 3.5 Flash 自 5 月 19 日起成為全球 Gemini 應用程式與 Google 搜尋 AI 模式的預設模型，同日開放開發者透過 Gemini API 使用。Pichai 直接說出了策略核心：「我們要打造出足夠便宜、足夠快速的模型，在服務數十億用戶的產品中大規模部署，同時維持前沿水準。」

## Gemini Spark：從不下線的 AI 代理

最受矚目的發表是 Gemini Spark——Google 針對 OpenAI Operator 和 Anthropic 自主代理研究的正面回應。傳統 AI 助理只在你保持對話視窗開啟時工作；Spark 不同，它在 Google Cloud 的專屬虛擬機器上全天候 24 小時運行，無論你的筆電是開著、闔上，還是根本沒開機。

Spark 由 Gemini 3.5 模型與更新版 Antigravity 代理框架驅動，設計用於長程任務：自主起草並寄出電子郵件、監控資訊流並整理重點、跨時區管理行程、完成多步驟研究工作。上線初期，它與整個 Google Workspace 套件原生整合；接下來幾週，將透過 Model Context Protocol（MCP）支援第三方應用程式。

推出時程相對保守：本週起開放信任測試用戶；下週起，美國的 Google AI Ultra 訂閱者可使用 Beta 版本。全球上線日期尚未公布。

這背後有個重大賭注：Google 認為，消費者 AI 的下一個戰場不是對話品質，而是持續性。一個在你睡覺或開會時還在持續工作的代理，與一個再優秀的聊天機器人，根本是兩種不同的產品形態。

## Gemini Omni：把影片當作第一公民的輸入與輸出

Google 同時發表了 Gemini Omni，將其定位為「世界模型」，而不只是影片生成器。這個區別至關重要：Omni 不只能從文字提示生成影片，它能同時原生處理影片、音訊和文字輸入，在長達數個步驟的多模態對話中進行編輯——理解影片的能力與生成影片的能力旗鼓相當。

面向消費者的 Gemini Omni Flash 今日起開放付費 Gemini 用戶使用，本週起免費用戶可在 YouTube Shorts 與 YouTube Create 中使用。開發者 API 接取將在數週內開放。

值得一提的是：I/O 正式發表之前，Omni 規格已在五月中旬流出，而實際產品幾乎如傳言所述。這說明 Google 內部的資訊安全仍是挑戰，但也側面印證這款產品夠真實、夠完整，即使提前曝光也無損發表效果。

## AI Ultra 月費 100 美元：瞄準頂級用戶

訂閱架構也全面翻新。Google 推出月費 100 美元的 AI Ultra，以更清晰的兩層結構取代舊有的 AI One 和 AI Premium 方案。AI Ultra 包含比 20 美元 AI Pro 方案高出 5 倍的使用限額、20TB 的 Google One 雲端儲存空間、YouTube Premium 會員，以及 Gemini Spark 的 Beta 使用權。

這讓 Google 與 OpenAI 月費 200 美元的 ChatGPT Pro 直接交鋒——Google 的定價是後者的一半。這也隱含著一個訊號：Google 有能力以規模優勢補貼高端 AI 服務，而這正是同時擁有全球最大雲端和搜尋業務的結構性紅利。

## Managed Agents API：給開發者的基礎設施層

對開發者而言，技術含量最高的可能是 Gemini API 中的 Managed Agents API。一次 API 呼叫即可佈建一個遠端 Linux 環境，讓代理在其中推理、規劃、呼叫工具、在沙盒中執行程式碼、管理檔案，以及瀏覽網頁取得即時資料。

開發者可以用 markdown 檔案——`AGENTS.md`（指令）和 `SKILL.md`（技能）——來擴充和客製化代理，並將其註冊為具名代理。這套設計刻意借鏡過去一年開源代理生態系統中浮現的慣例。

此外，Google 宣布舉辦 Build with Gemini XPRIZE 黑客松，獎金池高達 200 萬美元，是有史以來獎金最高的黑客松活動。

## 競爭格局的算盤

Google、OpenAI、Anthropic 的高層都愈來愈直接地說：前沿競賽已是勢均力敵。Google I/O 2026 的這批發表，是一次清晰的戰略宣示：在最便宜的生產模型和最深度的產品整合兩個維度上同時領先，才是持久的競爭優勢——無論哪家在某個基準測試上拿下第一。

真正的考驗現在才開始。Gemini Spark 會不會在無人監督的情況下確實完成任務？Gemini Omni 的影片品質能否媲美 Sora、Runway 和 Kling？Gemini 3.5 Flash 會不會成為開發者構建下一代 AI 應用時的預設選擇？

Google 已備齊所有棋子。整盤棋局的勝負，取決於執行力——而這，正是 Google 在消費者 AI 領域長期以來的最大罩門。
