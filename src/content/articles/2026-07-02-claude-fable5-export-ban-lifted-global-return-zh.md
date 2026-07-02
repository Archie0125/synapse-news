---
title: "禁令解除：Claude Fable 5 重返全球市場，美國政府封鎖 21 天後開放存取"
summary: "美國政府解除對 Anthropic Claude Fable 5 及 Mythos 5 的出口管制，21 天的全球封鎖宣告結束。此次封鎖起因於一個能繞過安全防護的漏洞，解封條件包括漏洞修補及建立政府可即時監控的行為監測框架——這是 AI 模型出口管制歷史上首次遭禁後又快速恢復的完整案例。"
category: "policy"
publishedAt: 2026-07-02
lang: "zh"
featured: false
trending: true
sources:
  - name: "Anthropic"
    url: "https://www.anthropic.com/news/fable-mythos-access"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/anthropic-is-bringing-back-claude-fable-5-globally-after-us-lifts-export-control-order-where-can-enterprises-access-it"
  - name: "Euronews"
    url: "https://www.euronews.com/2026/07/01/us-lifts-export-controls-on-powerful-ai-models-anthropic-says"
tags:
  - "anthropic"
  - "claude"
  - "fable-5"
  - "export-controls"
  - "ai-policy"
  - "cybersecurity"
  - "us-government"
relatedSlugs:
  - "2026-07-02-claude-fable5-export-ban-lifted-global-return-en"
  - "2026-07-01-anthropic-claude-sonnet-5-agentic-launch-zh"
  - "2026-06-29-us-export-control-claude-fable5-foreign-ban-zh"
---

2026 年 7 月 1 日，Anthropic 最強大的 AI 模型悄然重返全球舞台。Claude Fable 5 以及更受限部署的 Mythos 5，在美國政府解除出口管制後，恢復了對非美國用戶的服務存取。這場始於 6 月 9 日的前所未有封鎖，歷時 21 天，以 Anthropic、Amazon Web Services 及川普政府三方合作修補安全漏洞、建立新監控框架的方式畫下句點。

這在商業 AI 發展史上毫無先例，而其解決過程所留下的問題，不亞於封鎖本身。

## 封鎖的起點

Fable 5 在 6 月 9 日正式上線，是 Anthropic 迄今最強大的模型，在多數基準測試上持平或超越 GPT-5.5，並引入能自主處理長期任務的 agentic 能力。同日，Mythos 5 也在 Anthropic「Project Glasswing」計畫下，向一小群受信任的資安合作夥伴限量部署。

然而幾天後，一份亞馬遜網路服務的內部研究報告在政府圈內流傳。報告描述了一種提示注入技術，在特定條件下能繞過 Fable 5 的安全過濾器，使模型輸出識別軟體漏洞的詳細指南。這個技術需要相當高的技術門檻才能執行，且尚未公開揭露，但其存在已足以依川普 6 月 2 日行政命令啟動審查。

美國商務部隨即下令，要求 Anthropic 暫停無法驗證為美國國籍的用戶對 Fable 5 和 Mythos 5 的存取。由於 Anthropic 沒有即時驗證帳號國籍的機制，公司選擇全球下架兩款模型，而非嘗試可能面臨法律挑戰的局部合規方案。

結果就是長達 21 天的空窗期——歐洲、日本、南韓、台灣、印度等所有非美國主要市場的用戶，全都失去了已整合進正式系統的模型存取。

## 修補方案與監控框架

6 月 9 日到 7 月 1 日之間發生的，不只是一個漏洞的修補，而是一套複合式應對措施的建立。Anthropic 聯合亞馬遜安全團隊與政府，針對允許繞過防護的特定漏洞，以調整微調參數、部署執行期過濾器攔截相關提示模式、以及建立異常用量即時通報政府儀表板等方式，進行多層次修補。

更廣泛地說，Anthropic 同意了一套持續監控框架：若生產部署中的安全行為與基準線出現統計顯著的偏差，自動通知商務部。這代表一種全新的 AI 合規基礎設施類型——不是上市前的能力揭露，而是部署期間的持續行為驗證。

這套框架顯然讓政府滿意。6 月 30 日，商務部通知 Anthropic 解除出口管制。Fable 5 從 7 月 1 日起，於 Claude.ai、Claude Platform、Claude Code 及 Claude Cowork 恢復國際用戶服務。

## 分階段限制存取

解封並非無條件恢復。Anthropic 實施了分階段的用量限制，讓基礎設施團隊在恢復負載前能在監控下觀察部署狀況。7 月 7 日前，Pro、Max、Team 及特定 Enterprise 用戶僅能使用封鎖前 50% 的額度。7 月 7 日後，模型轉為依用量計費的信用點數制——這也是 Anthropic 對旗艦模型早已規劃的定價方向。

雲端平台存取（包括 AWS Bedrock、Google Cloud Vertex 及其他第三方部署的 Fable 5）則分階段恢復，預計 7 月中旬前完成完整的企業 API 開放。

對於在封鎖前已將 Fable 5 整合進正式工作流程的企業客戶來說，分階段限制是在 21 天中斷之後的又一次衝擊。據悉，部分大型企業客戶的法務團隊正在評估此次斷線是否構成針對 Anthropic 的合約索賠依據——Anthropic 的服務條款中，並未包含政府強制暫停存取的 SLA 條款。

## 台灣的處境

對台灣企業和開發者而言，這 21 天的空窗期來得格外不是時候。多家科技公司在 Fable 5 上線後迅速將其導入正式環境，尤其是在程式審查、文件摘要及長期 Agent 任務方面。封鎖期間，企業被迫緊急降回 Claude Sonnet 4.6 或其他替代方案，雖然仍能運作，但造成了相當程度的作業中斷。

全球存取恢復後，台灣用戶再度受到 Anthropic 標準服務條款的保障。現行監控框架不設地理限制，所有用戶在同一套行為驗證體系下運作，政府儀表板呈現的是整體用量模式，而非個別帳號資訊。

## 這個先例意味著什麼

這起事件的深遠意義，在於它對前沿 AI 監管格局的示範效應：在政府指令下，全球最強商業 AI 模型可以在 48 小時內被關閉，又在不到一個月後被重新開放。

這開創了一種新的部署風險類型。依賴美國前沿模型建構國際 AI 部署的企業，現在必須在架構決策中為「監管中斷風險」定價——這是一種既有商業條款中不存在的風險維度。

對產業而言，最迫切的懸念是：這套快速合規框架是否將成為未來能力監管的標準模板？川普的行政命令仍然有效，而「政府可在發現安全疑慮後快速觸發全球封鎖」的先例，已然確立。問題是這個機制將以多高的頻率被啟用。

Mythos 5 目前仍維持封鎖狀態，Anthropic 尚未公布其恢復時間表，相關標準預計比 Fable 5 更為嚴格。隨著 GPT-5.6 Sol 也進入類似的政府預覽審查程序，一個模型必須通過持續安全認證才能在全球部署的時代，似乎已經正式開始。
