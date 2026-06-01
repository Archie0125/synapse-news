---
title: "微軟 Build 2026：MAI 自研模型家族正式亮相，終結對 OpenAI 的依賴"
summary: "微軟將於 6 月 2 日在舊金山舉行的 Build 2026 開發者大會上，正式發布自研 AI 模型家族 MAI，其中包括專為驅動 GitHub Copilot 打造的程式碼生成模型。這是微軟迄今最明確的訊號：該公司正在擺脫對 OpenAI 的依賴，全面掌控旗下核心產品底層的 AI 基礎能力。"
category: "developer-tools"
publishedAt: 2026-06-01
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/"
  - name: "Windows Forum"
    url: "https://windowsforum.com/threads/microsoft-build-2026-homegrown-ai-models-to-power-github-copilot.420887/"
  - name: "Notebookcheck"
    url: "https://www.notebookcheck.net/Microsoft-Build-2026-What-to-expect-from-the-June-2-keynote.1311546.0.html"
  - name: "Tom's Guide"
    url: "https://www.tomsguide.com/computing/microsoft-build-2026-preview"
tags:
  - "微軟"
  - "Build 2026"
  - "MAI"
  - "GitHub Copilot"
  - "AI 模型"
  - "開發者工具"
relatedSlugs:
  - "2026-05-27-microsoft-build-2026-sf-agents-azure-ai-foundry-zh"
  - "2026-05-26-github-copilot-usage-based-billing-zh"
  - "2026-05-28-microsoft-cancels-claude-code-licenses-copilot-cli-zh"
---

週二上午，Satya Nadella 將在舊金山 Fort Mason 中心登台，帶來一個矽谷早已預期、卻讓合作夥伴深感壓力的宣布。微軟 Build 2026 開發者大會 6 月 2 日正式開幕，核心議程是正式推出微軟自研 AI 模型家族——統一以 MAI 為前綴品牌。

此次發布涵蓋一個以強化 GitHub Copilot 為目標的程式碼生成模型，以及 MAI-Transcribe-1（語音轉文字）、MAI-Voice-1（語音合成）和 MAI-Image-2（圖片生成），後兩者首次向商業開發者全面開放。微軟最重要的開發者產品，將首次在自家模型上運行，而非依賴 OpenAI。

## MAI 家族是什麼

微軟的自研模型計畫至少從 2024 年就已在進行，但鮮少公開提及。過去一年，隨著微軟對 OpenAI 合作夥伴關係的某些面向（尤其是定價、模型更新時程，以及合約限制微軟不得將特定 OpenAI 模型能力提供給第三方雲端競爭者）日益感到不滿，這個計畫大幅加速。

程式碼生成模型——業界消息人士預期將命名為 MAI-Code-1 或類似名稱——已在內部針對 OpenAI Codex 和 Anthropic Claude Sonnet 進行基準測試。據報導，該模型在業界標準的 SWE-bench Verified 評測中表現「持平或優於」Anthropic Claude 3.7 Sonnet，推理成本卻明顯更低。更關鍵的是，此模型設計為可在微軟 Azure 基礎設施上原生運行，無需呼叫任何 OpenAI API，徹底切斷讓 GitHub Copilot 企業端利潤率備受壓縮的依賴鏈。

## 這一轉向代表的戰略意義

Build 2026 公告的弦外之音清晰可見：微軟正在向開發者、企業客戶、投資人，乃至 OpenAI 本身傳達一個訊號——它要掌控旗下最重要產品底層的基礎模型。

商業邏輯顯而易見。微軟按量支付 OpenAI 推理費用——以 GitHub Copilot 目前超過 3000 萬活躍用戶的規模計算，每年流向 OpenAI 的費用高達數十億美元。此外，OpenAI 的 IPO 計畫讓其逐漸演變為潛在競爭對手，讓微軟的單一依賴風險進一步上升。

透過以 MAI 模型替換 OpenAI 模型（在性能相當的任務上），微軟得以大幅改善 Copilot 的利潤率，同時在不依賴 OpenAI 發布節奏的情況下自主迭代功能。

更宏觀地看，微軟正在打造一個完整的 AI 全棧能力：雲端基礎設施（Azure）、開發者工具（GitHub、VS Code）、生產力軟體（Microsoft 365 Copilot）、作業系統 AI（Windows 11 Copilot Runtime），以及現在的前沿基礎模型（MAI）。這與 Google 透過 Gemini 整合 Gmail、搜尋、Android 和 Google Cloud 所打造的格局如出一轍——而且刻意設計為不依賴任何外部供應商。

## Build 大會開發者將獲得什麼

MAI 模型發布之外，Build 2026 預計還有大量以開發者為核心的 API 與工具更新。已確認的議程主題包括：GitHub Copilot 的自主多步驟工程任務流程（不只是行內自動補全，而是可以被委派執行整個功能開發任務的代理模式）；GitHub Actions、Azure DevOps 與 Azure AI Foundry 平台的深度整合；以及 Windows Local AI 的全新 API 套件。

Windows Local AI 成為本屆大會的專題研討軌道，反映微軟積極推動 AI 推理在 Windows 11 消費端和商用裝置上本地運行的方向。面向法規遵循或有斷網需求的企業應用場景，這是一個關鍵能力。

Azure AI Foundry 則被定位為企業級的多模型、多代理工作流程編排層：能夠在同一個生產管線中，混合調用 MAI 模型、OpenAI、Anthropic、Meta 及開放權重模型，並附帶合規記錄、存取控管和用量計量功能。微軟押注的方向是：企業客戶需要的是靈活性——按需求自由切換模型——而非單一模型的鎖定。

## Copilot 商業化的關鍵轉折

貫穿上述一切的是一個殘酷的經濟現實：GitHub Copilot 用量增長迅速，但由於每個生成的 Token 都需透過 OpenAI 的推理基礎設施計費，利潤率始終承壓，遠比預期難以轉化為企業利潤。

轉向 MAI 模型的過程預計是漸進式的，且對用戶透明——Copilot 不會特別標注「現由 MAI 驅動」，模型路由將在後台靜默完成，微軟會根據具體任務從其擴張中的模型組合中選擇最優方案。有特定合規要求的企業客戶，仍可透過 Azure AI Foundry 將部署固定在特定模型版本（包括 OpenAI 模型）。

但方向已不可逆。微軟近期取消大批 Claude Code 授權合約的舉措，更進一步坐實了這個訊號：公司正在將 AI 開發者工具整合到自有平台周圍，不再容忍多供應商並立的碎片化格局。

## OpenAI 關係的未來走向

Nadella 始終以不對抗的措辭描述 MAI 戰略，一再強調這與 OpenAI 合作「互補而非競爭」。OpenAI 的模型——包括 GPT-5.5 和即將推出的 GPT-6 系列——仍會透過 Azure OpenAI Service 提供，微軟也仍是 OpenAI 最大的算力客戶。

但訊號正在累積。取消 OpenAI 相關授權、發布 MAI 模型家族、大力發展自有推理能力——這是一家公司在斥資逾 130 億美元、歷經近五年深度合作後，終於得出結論：對單一外部 AI 供應商形成永久性依賴，對一個市值超過 3 兆美元的企業而言，並非可持續的長遠選項。

Build 2026 的頭條是開發者工具，潛台詞卻是誰來掌控 AI 基礎設施的未來——而微軟正在押一個非常巨大的賭注：答案是它自己。
