---
title: "Anthropic Claude Mythos：意外洩露的「世代躍進」模型，重寫 AI 安全算式"
summary: "Anthropic 因內容管理系統設定錯誤，無意間公開了其迄今最強大模型「Claude Mythos」的存在。早期測試者描述它是超越 Opus 的全新等級，在推理與資安領域展現出史無前例的能力——同時也帶來令人憂慮的雙重用途風險。"
category: "ai-ml"
publishedAt: 2026-04-06
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

《財星》雜誌（Fortune）在 2026 年 3 月底發現並報導了這起洩漏事件。Anthropic 隨後確認，將原因歸結為「人為疏失」。但在確認的過程中，他們不得不同時確認了原本尚未準備公開的細節：這個模型是真實存在的、它叫做 Mythos、Anthropic 內部將其描述為「能力上的世代躍進（step-change）」。

「世代躍進」這個詞在 AI 產業裡有其份量。它意味著一種質的改變，而非僅僅量的增長——是那種真正改寫 AI 系統能做什麼的代際跨越。Anthropic 很少使用這樣的措辭。

## Claude Mythos 究竟是什麼？

模型命名有些複雜：「Mythos」是產品世代名稱，相當於現有陣容中的「Opus」或「Sonnet」；「Capybara」則是這一世代的等級名稱。完整稱呼形如 Claude Mythos Capybara，它位於目前 Opus 等級之上，是 Anthropic 首款明確「比 Opus 更大、更聰明」的模型。

從早期存取客戶的反饋與那份意外公開的草稿，可以拼湊出它的能力輪廓：

**大規模推理。** Mythos 在需要跨越極長上下文維持連貫邏輯鏈的複雜多步驟推理任務上，展現出顯著進步。從事科學研究的早期測試者描述，這是第一款能獨立完成文獻綜述的 AI 模型——能夠梳理相互矛盾的論文並產生新假設，嚴謹程度接近頂尖人類研究者。

**進階程式能力。** 在程式碼方面，Mythos 被描述為比 Claude Opus 4.6 有明顯跳躍。在內部測試中，Mythos 據報可以一次性完成過去需要多輪人工修正的大規模重構任務，且能在整個程式庫架構層面進行推理，而非只處理孤立函式。

**資安應用。** 這是 Anthropic 措辭最謹慎、也最具啟示性的面向。公司將 Mythos 的初期推出明確聚焦於資安領域，對象是一小群精選的企業早期存取客戶。Anthropic 將其潛力描述為「史無前例」——在防禦性應用（威脅偵測、漏洞評估、事件回應）方面，以及隱含的雙重用途風險方面，皆然。

## 安全矛盾

聚焦資安的策略，是 Anthropic 對前沿 AI 開發核心張力的正面回應：模型對複雜系統的理解與推理能力越強，攻擊它們的潛在能力也越強。

Anthropic 的做法是在資安垂直領域進行受控、有監督的部署——在更廣泛開放存取前，先透過專業操作者在實際環境中積累行為數據。這是「負責任擴展」的劇本，也是 Anthropic 長期以來差異化定位的核心敘事。

但資安研究社群的批評者指出一個顯而易見的侷限：一款能為受審核企業客戶產出「史無前例」資安洞見的模型，在架構上，與那款可能為別有居心的使用者產出史無前例攻擊能力的模型，是同一個模型。漏洞報告與攻擊程式之間的差距，有時僅是語法問題。

CNN 的報導讓這份憂慮更加具體。受訪的資安專家表示，Mythos 可能是第一款能自主開發新型零日漏洞的模型——不只是列舉已知漏洞，而是從第一原理出發，推斷特定系統防禦上可能存在的缺口。這是一種質的能力躍升，是當前這一代模型（包括 Claude Opus 4.6 和 GPT-5.4）尚未明確展現的。

## 發布策略

Mythos 不會公開上線。截至四月初，Anthropic 僅向「一小群由 Anthropic 親自挑選的早期存取客戶」開放，初期明確聚焦資安應用。公司表示，正「逐步擴大 Claude API 客戶對 Claude Mythos 的存取」。

有一個重要前提：Mythos 被描述為「一款大型、運算密集、服務成本高昂的模型」。Anthropic 正在努力提升其效率，才會考慮全面發布。這與其他前沿模型的歷史軌跡吻合——GPT-4 發布初期成本高昂、容量有限，但在 18 個月內價格下降了約 97%，並衍生出更小的蒸餾版本。

目前，Claude API 客戶對 Mythos 的預期是 2026 年 Q2 有限公測，更廣泛的開放存取可能與效率優化版本的發布掛鉤，時間點預計落在 2026 年下半年。

## 意外洩露的戰略價值

這次洩漏在操作上固然尷尬，但或許在無意間對 Anthropic 起到了正面效果。在 OpenAI 以 8,520 億美元估值融資 1,220 億美元、微軟推出自研前沿模型的競爭格局下，Anthropic 需要一個訊號，證明自己仍站在能力前沿。

Mythos 提供了這個訊號；聚焦資安的敘事框架，則提供了有別於競爭對手的安全敘事。這個訊息是：我們有最強大的模型，我們知道它的風險，而且我們比任何人都更謹慎地處理它。

「安全優先」的路線能否持續——或者競爭壓力最終是否會迫使更快、更廣泛的推出——將定義 Anthropic 的下一個篇章。目前，Claude Mythos 是最受期待的、卻沒有人被允許使用的模型。

這或許正是重點所在。
