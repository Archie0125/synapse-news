---
title: "Arcade 募得 6000 萬美元 A 輪，要解開卡住企業 AI Agent 部署的權限死結"
summary: "撰寫 MCP 授權規範、並在財富 500 大企業管理 AI Agent 行動的 Arcade，完成 6000 萬美元 A 輪融資，由 SYN Ventures 領投。這輪融資反映出企業界對 AI Agent 治理的迫切需求——在生產環境中，沒有人能清楚說出哪個 agent 代表哪個使用者執行了哪個動作。"
category: "startups"
publishedAt: 2026-06-27
lang: "zh"
featured: false
trending: true
sources:
  - name: "BusinessWire"
    url: "https://www.businesswire.com/news/home/20260615229631/en/Arcade-Raises-$60M-to-Become-the-Secure-Action-Layer-Behind-Every-Production-AI-Agent"
  - name: "Pulse2"
    url: "https://pulse2.com/arcade-raises-60-million-series-a-to-secure-ai-agents-in-production/"
  - name: "PYMNTS"
    url: "https://www.pymnts.com/news/investment-tracker/2026/arcade-raises-60-million-to-control-ai-agents/"
tags:
  - "Arcade"
  - "AI Agent"
  - "MCP"
  - "企業安全"
  - "A輪融資"
  - "Agent治理"
relatedSlugs:
  - "2026-06-27-arcade-60m-ai-agent-security-mcp-en"
  - "2026-06-27-anthropic-claude-tag-slack-enterprise-zh"
---

## 資安團隊答不出的問題

當一個跑在公司基礎設施上的 AI Agent 執行了某個動作——寄出一封 email、查詢一個資料庫、送出採購單、修改了一份設定檔——你能回答以下問題嗎？

那是哪個 agent？代表哪個使用者？它真的被授權在那個系統上做那件事嗎？

2026 年，對大多數正在部署 AI Agent 的企業而言，誠實的答案是：不行。這個缺口，就是 Arcade 存在的原因，也是這家公司剛拿到 6000 萬美元 A 輪融資的原因。

本輪由 SYN Ventures 領投，Morgan Stanley 和 Wipro 跟投。加上 2025 年的 1200 萬美元種子輪，Arcade 的累計融資額達到 7200 萬美元。這背後的邏輯很明確：AI Agent 的治理問題，已從可選功能變成企業部署的必要前提。

## Arcade 在做什麼

Arcade 把自己定位為 AI Agent 的「安全行動層」，這個描述非常精準。它嵌在 AI 模型和企業系統之間，提供三個在實務上長期缺席的能力：

**授權驗證**：在 agent 執行動作之前，Arcade 驗證特定 agent 代表特定使用者，對特定資源執行特定動作的權限。不是籠統的能力核查，而是每次動作、每個使用者、每個資源的細粒度授權決策。

**受控執行**：Arcade 在受控環境中代為執行動作，而不是讓 agent 直接以廣泛權限憑證調用企業 API。

**完整稽核軌跡**：每個動作都被結構化記錄：哪個模型調用了它、哪個使用者觸發了工作流程、存取了什麼資料、改變了什麼。

Arcade CEO Alex Salazar 把核心問題說得很直白：「Agent 在生產環境失敗，不是因為模型本身出了問題——是因為權限模型出了問題。沒有人能對任意一個 agent 動作，證明它代表那個使用者、對那個資源是否真的有授權。」

## MCP 連結

Arcade 不只是安全包裝層，它還是 MCP（模型上下文協定）授權規範的原始撰寫者，這份規範現已被 Anthropic 採用。MCP 已成為 AI Agent 連接工具與外部系統的事實標準；Arcade 在其上搭建的授權層，則定義了這些連接如何被治理。

這個定位具有戰略意義。透過撰寫規範，Arcade 讓自己與所有部署相容 MCP 的 agent 企業產生了結構性關聯——而隨著 Anthropic Claude 和其他平台標準化於 MCP，這幾乎等同於所有主要的企業 AI 部署。

目前公司維護超過 8,000 個針對企業工作流程打造的 MCP 工具，過去六個月工具呼叫量成長了 25 倍。生產環境使用者包括一家美國頂級銀行、Prosus 和 LangChain——每一個都是高吞吐量、高風險的 agent 應用場景，在這些場景中，一次權限漏洞不只是尷尬，而是合規事件。

## 為什麼這個問題會越來越嚴重

AI Agent 的治理挑戰，是技術採用速度遠超制度框架的直接後果。

2024 年到 2025 年初，AI Agent 大多停留在沙盒示範和概念驗證階段。到 2026 年，它們已在路由客戶理賠、執行交易、管理基礎設施、起草並發送通訊，持有的存取權限甚至超過任何單一人類員工。

傳統以人為核心設計的身份與存取管理（IAM）系統，根本沒想到要處理 agent。人類員工有角色、有固定的權限集、有組織層級的問責機制。AI Agent 可以被多個使用者調用，同時跑在數千個並行工作流程中，使用的憑證無法清晰對應到任何個人。傳統 IAM 給了你一把大鎚，但你需要的是手術刀。

SYN Ventures 合夥人 Jay Leek 把投資邏輯說得很清楚：「採用速度總是跑在讓它安全的基礎設施之前。Agent 現在正卡在這道牆上。」

## 企業的盤算

對企業而言，安全顧慮不是抽象的。金融服務、醫療和關鍵基礎設施的監管機構已明確表示：AI 系統的治理必須可稽核、可記錄、可回溯。「是 AI 做的」在銀行審查員或 SEC 調查員面前，不構成任何辯護。

現實情況是：許多企業已完成 AI Agent 的能力驗證和內部審批，最後卻卡在安全合規關卡，因為沒人能回答最基本的治理問題。Arcade 的主張是：移除這個阻礙，而且不需要企業從頭建立自己的授權基礎設施。

本輪的策略投資人——Morgan Stanley（直接押注在 AI 治理工具的金融機構）和 Wipro（深度參與全球企業 AI 部署的顧問公司）——都說明這個需求並非假設，而是已有迫切的商業現實在後面推動。

## 6000 萬美元要拿來做什麼

新資金將用於加速產品開發、擴展 MCP 工具生態，以及擴充工程和商業化團隊。公司也在擴大與主流企業身份平台的整合——把 Arcade 的授權層接入現有企業 SSO 和 IAM 基礎設施，這是無縫企業部署的先決條件。

六個月 25 倍的工具呼叫量成長，加上頂級金融機構的生產環境部署，已驗證市場存在且產品可用。A 輪要回答的問題是：公司能否從少數旗艦設計夥伴，擴展到讓 Arcade 真正成為 AI Agent 經濟基礎設施的千家企業部署規模？

AI Agent 的採用沒有放緩的跡象。讓大規模部署安全可行的治理基礎設施，代表著一個龐大且尚未被充分滿足的市場。而 Arcade 目前是最接近完整解方的公司。
