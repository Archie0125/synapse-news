---
title: "GitHub Copilot 終結月費時代：6 月 1 日起改採 AI Credits 計量計費"
summary: "GitHub 旗下 AI 程式碼助理自 2026 年 6 月 1 日起正式切換至用量計費制，以「GitHub AI Credits」取代原有的進階請求單位（PRU）。各方案月費不變，但 AI 代理工作流程與程式碼審查等功能將消耗每月額度——一旦用盡，企業管理員須決定是否允許超額計費，或直接停用相關功能。"
category: "developer-tools"
publishedAt: 2026-06-01
lang: "zh"
featured: false
trending: true
sources:
  - name: "GitHub Blog"
    url: "https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/"
  - name: "GitHub Docs"
    url: "https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises"
  - name: "Visual Studio Magazine"
    url: "https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx"
tags:
  - "GitHub Copilot"
  - "AI Credits"
  - "開發者工具"
  - "Microsoft"
  - "計費"
  - "AI 代理"
relatedSlugs:
  - "2026-06-01-github-copilot-ai-credits-billing-change-en"
  - "2026-06-01-microsoft-build-2026-mai-coding-models-zh"
---

對於數百萬將 GitHub Copilot 視為日常工作夥伴的開發者而言，今天是一個看似平靜、實則影響深遠的轉捩點。2026 年 6 月 1 日起，GitHub 正式告別這款 AI 助理的月費固定制，轉向以全新虛擬貨幣「GitHub AI Credits」為核心的計量計費模式。

這項異動自四月公告以來已醞釀多時，但隨著遷移正式上線，對企業客戶與個人訂閱者的實際影響，此刻才開始真正清晰。

## PRU 走入歷史，Credits 登場

舊有系統給予付費用戶每月固定的「進階請求單位（Premium Request Units，PRU）」額度，作為使用進階 AI 功能的上限——包括搭配 GPT-4o 的 Copilot Chat、多檔案編輯與程式碼審查。一旦 PRU 耗盡，用戶會被自動降級到較弱的模型回應，直到下個月重置。

GitHub AI Credits 的運作方式則大相徑庭。1 個 AI Credit 等於 0.01 美元，依據實際的 token 用量計費，涵蓋輸入、輸出與快取的上下文，並按各底層模型公開的 API 費率計算。用量複雜度與模型選擇直接影響消耗速度——以 Claude Sonnet 執行跨多個檔案的複雜重構，所需 Credits 遠多於一次簡單的行內補全。

最關鍵的是，基礎功能仍然免費：程式碼自動補全（Code Completions）與「下一步編輯建議」（Next Edit Suggestions）——也就是大多數開發者每分鐘都在使用的核心功能——在所有方案中依然完全包含，不消耗任何 Credits。只有在呼叫前沿模型的 Copilot Chat、多檔案 AI 代理工作流程、Pull Request 程式碼審查等功能時，計費時鐘才會開始運轉。

## 方案定價：數字不變，價值有別

GitHub 特別強調月費方案價格不會調整，三種商業方案如下：

- **Copilot Pro+** — $39/月，含每月 $39 的 AI Credits
- **Copilot Business** — $19/使用者/月，含每月 $19 的 AI Credits  
- **Copilot Enterprise** — $39/使用者/月，含每月 $39 的 AI Credits

每個方案的包含額度數值上等於訂閱金額，意即每付出 1 美元，就對應 1 美元的 Credit。超出包含額度的用量，可依公開 API 費率額外購買，企業組織可自行選擇是否開放或設定上限。

然而，這套算法並不如表面看起來那麼直觀。在舊有 PRU 制度下，重度代理功能使用者耗盡進階額度後，功能會優雅降級，但絕不會產生超額費用。而在 AI Credits 制度下，若企業大規模運行自動化程式碼審查流水線或代理重構機器人，在管理員未設定支出上限的情況下，確實可能產生實際的超額費用。

## 開發者怎麼看？

開發者社群的反應好壞參半，整體偏向審慎懷疑。Visual Studio Magazine 在四月公告後進行了社群調查，最具代表性的一句話——「你將得到更少，但付一樣的錢」——精準點出了主流情緒。核心擔憂在於：雖然表面月費相同，但對重度用戶而言，實際獲得的價值縮水了；原本可以盡情運行複雜代理工作流程的 $39/月訂戶，如今面臨一個可能在月中耗盡的計量預算。

GitHub 的回應是：一般開發者主要使用補全功能與偶爾的對話功能，不會感受到任何差異，「這項變動對絕大多數用戶來說完全無感，最常用的程式碼補全功能根本不碰 Credits，」GitHub 發言人表示。

對企業客戶而言，情況更為複雜。管理員現在擁有細粒度的預算控制：可在企業、成本中心、團隊與個人用戶層級各自設定支出上限。當包含額度用完，組織可選擇按計量費率繼續允許額外用量，或強制設定硬上限，在下一個計費週期前停用進階功能。這種治理能力對 IT 採購團隊而言是全新且實用的工具——在代理應用場景激增後，Copilot 的總擁有成本一直難以預測。

## 更大的脈絡：AI 正在成為基礎設施

從 PRU 轉向 AI Credits，不只是計費方式的調整，更反映了 GitHub 對 Copilot 定位的根本性轉變。2021 年 Copilot 推出時，它是一款程式碼自動補全工具；到了 2026 年，它已越來越像一個能夠規劃並執行多步驟開發任務的代理平台：撰寫測試、建立 Pull Request、審查變更、跨倉庫協調操作。

計量計費正是這類運算的天然基礎設施模型。AWS Lambda 與 Azure Functions 等雲端服務一直採用「按調用次數計費」而非月費制，正因為其成本結構是非線性的。GitHub 正將同樣的邏輯套用到 AI 工作負載上。

競爭時機也很微妙。Cursor 在四月以 500 億美元估值完成 20 億美元融資，其按請求計費的透明定價深受開發者認可。Devin、JetBrains AI 及新一波代理程式設計工具也都在試驗用量計費模式。GitHub 此次跟上市場走向，雖有風險流失習慣把 Copilot 視為固定成本「工具」的用戶，但方向正確。

## 開發者現在應該怎麼做

對個人 Copilot Pro+ 訂閱者而言，最實際的建議是善用 GitHub 新增的 Credits 即時用量儀表板（位於 Copilot 設定面板），留意哪些功能消耗最多額度。消耗最多 Credits 的通常是使用前沿模型的長時間代理工作階段，而非一般的對話問答。

對企業而言，這次轉換是一個好機會，用來審計 Copilot 的實際使用狀況。許多組織廣泛部署了 Copilot，卻對哪些團隊產生了最多模型流量缺乏清晰認識。全新的成本中心報告讓這件事第一次變得可見。

最終結論：GitHub Copilot 仍是市場上性價比最高的 AI 生產力工具之一。對主要使用補全功能與偶爾問答的開發者，今天的變化不過是換了個標籤；對在 Copilot 代理能力上構建自動化的重度用戶，計量計費的時代已然到來——帳單即將變得更清晰，也更直白。
