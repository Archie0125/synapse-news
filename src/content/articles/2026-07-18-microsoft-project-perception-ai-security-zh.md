---
title: "微軟「感知計畫」瞄準 Anthropic Mythos，以多模型架構挑戰 AI 資安市場"
summary: "微軟正準備推出「Project Perception」，一個結合微軟、OpenAI 與 Anthropic 模型的 AI 資安漏洞偵測平台，主打比 Anthropic Mythos 更低的使用成本。這是新任資安主管 Hayete Gallot 領導下，微軟對 AI 資安市場最直接的一次出手。"
category: "developer-tools"
publishedAt: 2026-07-18
lang: "zh"
featured: false
trending: false
sources:
  - name: "TechRepublic"
    url: "https://www.techrepublic.com/article/news-microsoft-project-perception-ai-security-tool/"
  - name: "NewsBytesApp"
    url: "https://www.newsbytesapp.com/news/science/microsoft-to-launch-project-perception-ai-cybersecurity-platform-this-month/tldr"
  - name: "Phemex News"
    url: "https://phemex.com/news/article/microsoft-to-launch-ai-vulnerability-detection-tool-this-month-93543"
tags:
  - "微軟"
  - "Project Perception"
  - "AI 資安"
  - "資訊安全"
  - "Anthropic Mythos"
  - "漏洞偵測"
  - "開發者工具"
relatedSlugs:
  - "2026-07-17-microsoft-mai-sales-war-openai-anthropic-en"
  - "2026-07-07-microsoft-mai-thinking-1-code-1-flash-launch-en"
  - "2026-07-05-anthropic-pentagon-autonomous-weapons-emails-unsealed-en"
---

微軟正準備推出今年最具戰略意義的 AI 產品之一。「Project Perception」——一個以 AI 為核心、用於偵測與修復軟體漏洞的平台——預計將於 7 月底前正式上線，多份引述知情人士的報導如此指出。這款工具採用多模型架構，整合了微軟、OpenAI 與 Anthropic 三家的 AI 系統，並根據每項安全任務的性質智慧路由至最合適的模型。

時機的選擇頗具針對性。Anthropic 的 Mythos——該公司作為企業資安工具推出的 AI 漏洞掃描器——正在企業市場持續擴張，但其 API 成本據報較 Opus 高出 100%、較 GPT-5.6 Sol 高出 82%。Project Perception 的核心定位正是「成本」：在企業資安團隊可承受的預算範圍內，提供與 Mythos 相當的偵測能力。

## 技術架構

Project Perception 的核心差異在於其智慧路由系統。與其將每一個安全查詢都送往同一個 AI 模型，該平台會評估每項任務的性質，再將其分配給最適合的模型。一個直接的漏洞模式比對任務，可能被路由到成本較低、速度較快的模型；而需要細膩推理的複雜多步驟漏洞鏈分析，則可能升級至更具能力的模型處理。

這種方式有兩個優勢。首先，可以顯著降低每次查詢的成本——在企業規模下，避免對每項任務都動用前沿模型所節省的費用相當可觀。其次，這讓微軟得以善用不同模型架構的各自優勢：微軟自家針對資安場景微調的模型深度整合了其現有的威脅情報基礎設施，而接入 OpenAI 和 Anthropic 的模型則為平台帶來了通用推理能力，在應對複雜、新型攻擊場景時，往往超越微軟自身資安模型的能力邊界。

這款工具是在 Hayete Gallot 的領導下打造的。Gallot 在繼 2023 年和 2024 年多起高知名度事件後接掌微軟資安主管職位，她的任命代表著一種哲學轉變——從將資安視為合規和基礎設施職能，轉變為將其視為可以透過 AI 持續強化的產品介面。

## 競爭格局

Project Perception 進入的是一個快速成為企業軟體領域最激烈競技場之一的市場。利用 AI 發現並修復安全漏洞的基本邏輯簡單明瞭——程式碼分析是 LLM 已展現出明確能力的領域，而 AI 加速漏洞發現的經濟效益，對於目前在手動滲透測試和安全審查上投入大量資源的企業而言相當具有吸引力。

Anthropic 將 Mythos 定位為其在這一領域的旗艦產品，明確瞄準企業安全作業中心（SOC）。據報導的定價溢價——讓 Mythos 的成本明顯高於同等 GPT-5.6 Sol 部署——為可信替代方案創造了進場空間。而微軟憑藉 Microsoft Defender、Azure Security Center 和 Microsoft Sentinel 在企業 IT 部門積累的現有關係，擁有 Anthropic 所缺乏的通路優勢。

多供應商模型架構從採購角度來看也是一個差異化點。越來越多的企業已強制要求採用多雲或多供應商 AI 政策——這一趨勢受到風險管理和監管要求的雙重驅動——他們發現單一模型工具比能跨供應商路由的平台更難通過企業治理審查。Project Perception 的架構天然具有供應商多元化特性，能在不要求客戶自行管理複雜性的前提下，滿足企業治理需求。

## 對 AI 資安市場的意義

Project Perception 作為 Mythos 直接競爭者的出現，標誌著 AI 輔助資安市場正進入整合階段。第一波 AI 資安工具——主要是將 AI 作為現有安全工作流程附加功能的新創公司——正在受到具備通路規模、現有企業關係以及能力在訂價上採取積極策略的平台級玩家的挑戰。

對 Anthropic 而言，這一競爭壓力出現在一個頗為微妙的時刻。7 月初披露的 IPO 保密申請顯示，該公司正準備上市，且需要在接近 1 兆美元估值的基礎上維持相應的營收成長速度。資安是企業軟體中利潤率最高、防禦性最強的類別之一，Mythos 一直是 Anthropic 說服投資人其企業營收具備可持續性的重要論據。一個可信的微軟替代方案，改變了這個估算。

對開發者和資安團隊而言，Project Perception 的出現從實際角度來看值得歡迎：更多競爭通常會拉低 AI 資安工具的價格，讓那些負擔不起 Mythos 定價的規模較小的資安團隊也能受益。智慧路由架構也是一個值得廣泛借鑑的企業 AI 技術模型——不同任務匹配不同模型、透過路由層動態優化成本與能力權衡的洞察，遠不止適用於資安領域。

## 仍存在的不確定性

需要注意的是：截至本文撰寫時，微軟尚未正式公告 Project Perception 的可用性、定價、支援的工作負載或客戶資格。現有報導的資訊來源為知情人士，而非微軟的官方披露。公司可能在 7 月底前正式宣布這款工具，也可能延至 8 月。

可以確定的是：這款產品真實存在，其設計目標是在定價上直接競爭 Mythos，這也是微軟迄今為止最明確的信號——它打算在企業 AI 資安市場上競爭，而不僅僅是讓客戶自行整合各自的模型。對正在從研究機構轉型為規模化企業軟體公司的 Anthropic 而言，Project Perception 可能是這個月最重要的競爭動態之一。
