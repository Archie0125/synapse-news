---
title: "微軟取消大多數內部 Claude Code 授權，強制工程師改用 Copilot CLI"
summary: "微軟正在旗下 Experiences & Devices 部門（負責 Windows、Teams、Office 和 Surface）取消大多數 Claude Code 授權，截止日期為 2026 年 6 月 30 日。儘管工程師更喜歡 Claude Code，微軟仍強制自家團隊改用 GitHub Copilot CLI，理由是成本控制與工具鏈整合。"
category: "developer-tools"
publishedAt: 2026-05-28
lang: "zh"
featured: false
trending: true
sources:
  - name: "Windows Central"
    url: "https://www.windowscentral.com/microsoft/microsoft-cancels-claude-code-licenses-shifting-developers-to-github-copilot-cli-a-move-likely-driven-by-financial-motives"
  - name: "TechRadar"
    url: "https://www.techradar.com/pro/microsoft-may-discontinue-claude-code-internally-as-it-looks-to-push-users-towards-github-copilot"
  - name: "Yahoo Tech"
    url: "https://tech.yahoo.com/ai/copilot/articles/microsoft-ditching-claude-code-copilot-133318848.html"
tags:
  - "microsoft"
  - "claude-code"
  - "github-copilot"
  - "ai-coding"
  - "developer-tools"
relatedSlugs:
  - "2026-05-27-anthropic-2026-agentic-coding-trends-report-zh"
  - "2026-05-26-github-copilot-usage-based-billing-zh"
  - "2026-05-27-servicenow-build-agent-all-ai-coding-ides-zh"
---

微軟本月做了一個既具策略意義、又充滿諷刺意味、同時揭示企業 AI 成本現實的決定：它正在取消 Experiences & Devices 部門大多數工程師的 Claude Code 授權，要求他們改用 GitHub Copilot CLI，截止日期為 2026 年 6 月 30 日。

Experiences & Devices 部門負責微軟一些最重要的產品——Windows、Microsoft 365、Outlook、Teams 和 Surface。這些不是邊緣團隊，而是微軟工程版圖的核心。在過去六個月裡，這個部門的許多工程師悄悄地選擇了 Anthropic 的工具，而非自家老闆的產品。

## 六個月的「禁忌之愛」

2025 年 12 月，Claude Code 在 Experiences & Devices 部門內部率先推出，初期以受控方式開放給開發者、專案經理和部分設計師。普及速度驚人——幾週之內，工程師們便在內部頻道口耳相傳、自發擴散。

到了 2026 年春天，Claude Code 的使用已如此廣泛，以至於公司內部消息人士描述，AI 相關費用出現了意料之外的急劇攀升。這正是當你建出一個人們真正想用的東西時，所會遇到的問題。多年來努力說服市場「GitHub Copilot 是世界級 AI 程式工具」的微軟，尷尬地發現自己的工程師用實際行動投票，選擇了競爭對手。

官方在內部溝通中的說法是「工具鏈統一」——聽起來合理的營運目標。但多份報告指出，成本削減才是更直接的驅動因素。以企業 AI 定價計算，數千名工程師頻繁執行重量級的代理編程任務，每月可迅速產生數百萬美元的算力費用。

## 功能落差是核心問題

讓這件事真正複雜的是：據內部消息，微軟工程師明確偏好 Claude Code 而非 GitHub Copilot CLI，兩者之間的功能落差在開發者圈早已公開討論數月。

Claude Code 基於 Anthropic 的前沿 Claude 模型，提供精密的跨檔案推理、代理任務執行，以及許多開發者認為生產力顯著更高的終端機原生工作流程。GitHub Copilot CLI 雖然能力不俗，且與微軟生態系深度整合，但在長週期代理任務的處理上歷來遜於 Claude Code。

這正是內部推廣如此迅速成功的原因，也是這次取消決定引發工程師不滿的根本。讓工程師自由選擇時，他們選了 Claude Code；現在，這個選擇被替換掉了。

## 微軟 AI 戰略的核心矛盾

這件事暴露了微軟在 AI 產業中的真實處境與內在矛盾。微軟是 OpenAI 最大的外部投資者，累計承諾超過 130 億美元；近期又在洽談與 Anthropic 的 Maia AI 晶片合作；過去兩年也持續將 AI 整合到 Word、Azure、Xbox 等每一個產品介面。

然而，微軟等於公開承認：在自家工程師的評判下，目前市面上最好的 AI 程式工具是競爭對手做的，而且讓工程師使用它的成本太高了。

換個角度看，這恰恰是理性企業 AI 採購的樣貌。平台紀律至關重要。切換成本持續積累。GitHub Copilot 與微軟整個開發者技術棧——Azure DevOps、GitHub Actions、VS Code、Azure Repos——高度整合，這種整合對大多數企業工程流程確實有其價值，或許足以彌補能力上的落差。

要求使用 Copilot CLI，不只是要削減 Anthropic 的帳單，更是要確保下一代 AI 編程基礎設施在微軟內部建立時，是建立在微軟自己的基礎設施之上。

## 對 AI 編程市場的啟示

這件事的影響遠不止於微軟的內部工具選擇。

第一，這證實了 Claude Code 確實在某些任務領域優於其他 AI 編程工具。微軟工程師主動採用這一事實，是比任何排行榜都更有意義的現實基準測試。

第二，這揭示了企業 AI 大規模採用帶來的成本問題。微軟是資源極為充沛的科技公司，即便如此也發現讓數千名工程師在重度使用的 AI 工具上運行，代價高到需要強制扭轉。規模較小的組織將更早面對類似抉擇，且手上可用的資源更少。

第三，AI 編程市場正在進入一個由採購決策、而非純粹技術能力主導市場份額的階段。Google Gemini、Microsoft Copilot、Anthropic Claude Code 和 Cursor 的能力對一般工程任務都已足夠。競爭的勝負將越來越多地在企業銷售談判中決定，而非在跑分評測中決定。

最後，6 月 30 日的截止日期製造了一個清晰的分水嶺。如果 GitHub Copilot CLI 無法達到被迫換工具的工程師所要求的生產力，微軟將從自家員工那裡聽到強烈反饋。這種內部壓力，可能是推動 Copilot 路線圖加速的最有效力量。

## Anthropic 的間接損失

對 Anthropic 而言，失去微軟的內部部署主要是營收層面的打擊。Claude Code 的年化收入已突破 25 億美元且仍在快速成長，微軟的取消決定不會構成生死威脅。但微軟規模的企業內部使用所帶來的品牌價值——作為參考客戶的背書、以及工程師口耳相傳的效應——的損失，影響不容忽視。

接下來值得觀察的是：這是否會形成更廣泛的趨勢——其他大型企業是否也會得出結論，認為大規模 AI 編程工具使用的成本效益，更傾向於整合自建或強整合供應商的工具，無論工程師的個人偏好如何。

微軟已經為自己回答了這個問題，至少目前如此：當帳單來了，平台紀律勝出。
