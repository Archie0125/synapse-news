---
title: "Anthropic Claude Mythos：意外洩露的「世代躍進」模型，重寫 AI 安全算式"
summary: "Anthropic 因內容管理系統設定錯誤，無意間證實了「Claude Mythos」的存在，並稱其為迄今能力最強的模型。外流的部落格草稿描述了一個超越 Opus 的全新等級，並警告其帶來史無前例的資安風險。"
category: "ai-ml"
publishedAt: 2026-04-06T09:05:00Z
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Fortune"
    url: "https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/"
  - name: "CNN Business"
    url: "https://www.cnn.com/2026/04/03/tech/anthropic-mythos-ai-cybersecurity"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/03/27/anthropic-launch-new-claude-mythos-model-advanced-reasoning-features/"
  - name: "Euronews"
    url: "https://www.euronews.com/next/2026/03/30/what-is-anthropics-mythos-the-leaked-ai-model-that-poses-unprecedented-cybersecurity-risks"
tags:
  - "Anthropic"
  - "Claude"
  - "Mythos"
  - "AI安全"
  - "資安"
  - "前沿模型"
  - "大語言模型"
relatedSlugs:
  - "2026-04-04-openai-gpt5-leak-zh"
  - "2026-04-04-open-source-llm-race-zh"
  - "2026-04-06-microsoft-mai-models-independence-zh"
  - "2026-04-06-anthropic-claude-mythos-en"
---

## 不該發生的洩露

Anthropic 花了四年時間打造「安全優先」的 AI 實驗室形象——由前 OpenAI 研究人員創立，他們認為前東家走得太快太猛。因此，當這家公司最強大模型的存在，不是透過新聞稿，而是透過一個設定錯誤、讓未發布草稿變成公開可搜尋文件的內容管理系統被世界知曉，這份諷刺實在難以迴避。

《財星》雜誌（Fortune）查閱了外洩資料，並於 2026 年 3 月底報導；資安研究人員也曾另行發現這些資料。Anthropic 隨後確認，將原因歸結為「人為疏失」。但在確認的過程中，他們證實了原本尚未準備公開的細節：這個模型是真實存在的、它叫做 Claude Mythos，且 Anthropic 發言人形容它是「一次世代躍進（step change）」，也是「我們迄今打造過最強大的模型」。

「世代躍進」這個詞在 AI 產業裡有其份量。它意味著一種質的改變，而非僅僅量的增長——是那種真正改寫 AI 系統能做什麼的代際跨越。Anthropic 很少使用這樣的措辭。

## Claude Mythos 究竟是什麼？

模型命名有些複雜：「Mythos」是這款新模型的名稱，草稿部落格稱之為 Claude Mythos；「Capybara」則是草稿部落格為新等級模型取的名稱，而 Capybara 與 Mythos 看來指的是同一個底層模型。根據草稿，這個新等級位於目前 Opus 等級之上：「比我們的 Opus 模型更大、更聰明——而 Opus 直到現在都是我們最強大的模型。」

從早期存取客戶的反饋與那份意外公開的草稿，可以拼湊出它的能力輪廓：

**大規模推理。** Mythos 在需要跨越極長上下文維持連貫邏輯鏈的複雜多步驟推理任務上，展現出顯著進步。從事科學研究的早期測試者描述，這是第一款能獨立完成文獻綜述的 AI 模型——能夠梳理相互矛盾的論文並產生新假設，嚴謹程度接近頂尖人類研究者。

**進階程式能力。** 在程式碼方面，Mythos 被描述為比 Claude Opus 4.6 有明顯跳躍。在內部測試中，Mythos 據報可以一次性完成過去需要多輪人工修正的大規模重構任務，且能在整個程式庫架構層面進行推理，而非只處理孤立函式。

**資安應用。** 這是 Anthropic 措辭最謹慎、也最具啟示性的面向。公司正與一小群早期存取客戶合作測試這款模型，草稿部落格並稱，將向各機構提供早期存取，讓資安防禦者搶得先機。草稿部落格指出該模型帶來「史無前例的資安風險」，Anthropic 並表示希望了解近期風險，並分享研究結果，協助資安防禦者做好準備。

## 安全矛盾

聚焦資安的策略，是 Anthropic 對前沿 AI 開發核心張力的正面回應：模型對複雜系統的理解與推理能力越強，攻擊它們的潛在能力也越強。

Anthropic 的做法是在資安垂直領域進行受控、有監督的部署——在更廣泛開放存取前，先透過專業操作者在實際環境中積累行為數據。這是「負責任擴展」的劇本，也是 Anthropic 長期以來差異化定位的核心敘事。

但資安研究社群的批評者指出一個顯而易見的侷限：一款能為受審核企業客戶產出「史無前例」資安洞見的模型，在架構上，與那款可能為別有居心的使用者產出史無前例攻擊能力的模型，是同一個模型。漏洞報告與攻擊程式之間的差距，有時僅是語法問題。

CNN 的報導讓這份憂慮更加具體。受訪的資安專家表示，Mythos 可能是第一款能自主開發新型零日漏洞的模型——不只是列舉已知漏洞，而是從第一原理出發，推斷特定系統防禦上可能存在的缺口。這是一種質的能力躍升，是當前這一代模型（包括 Claude Opus 4.6 和 GPT-5.4）尚未明確展現的。

## 發布策略

Mythos 不會公開上線。截至四月初，Anthropic 僅向「一小群由 Anthropic 親自挑選的早期存取客戶」開放。公司表示，正「逐步擴大 Claude API 客戶對 Claude Mythos 的存取」。

有一個重要前提：草稿部落格指出，Mythos 運行成本高昂，尚未準備好全面發布。Anthropic 正在努力提升其效率，才會考慮全面發布。這與其他前沿模型的歷史軌跡吻合——GPT-4 發布初期成本高昂、容量有限，但在 18 個月內價格下降了約 97%，並衍生出更小的蒸餾版本。

目前，Claude API 客戶對 Mythos 的預期是 2026 年 Q2 有限公測，更廣泛的開放存取可能與效率優化版本的發布掛鉤，時間點預計落在 2026 年下半年。

## 意外洩露的戰略價值

這次洩漏在操作上固然尷尬，但或許在無意間對 Anthropic 起到了正面效果。在 OpenAI 以 8,520 億美元估值融資 1,220 億美元、微軟推出自研前沿模型的競爭格局下，Anthropic 需要一個訊號，證明自己仍站在能力前沿。

Mythos 提供了這個訊號；聚焦資安的敘事框架，則提供了有別於競爭對手的安全敘事。這個訊息是：我們有最強大的模型，我們知道它的風險，而且我們比任何人都更謹慎地處理它。

「安全優先」的路線能否持續——或者競爭壓力最終是否會迫使更快、更廣泛的推出——將定義 Anthropic 的下一個篇章。目前，Claude Mythos 是最受期待的、卻沒有人被允許使用的模型。

這或許正是重點所在。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 10 處。*
