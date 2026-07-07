---
title: "Anthropic Fable 5 今日退出訂閱方案：Claude 用戶必知的計費大變革"
summary: "自 2026 年 7 月 7 日起，Anthropic 最強大的模型 Fable 5 不再包含於 Pro、Max、Team 及企業訂閱方案中。用戶若要繼續使用，需以用量點數計費，輸入每百萬 Token 10 美元、輸出每百萬 Token 50 美元。Anthropic 表示此為臨時措施，起因是解除出口禁令後需求暴增、伺服器容量吃緊。"
category: "ai-ml"
publishedAt: 2026-07-07
lang: "zh"
featured: true
trending: true
sources:
  - name: "BleepingComputer — Fable 5 Isn't Permanently Leaving Subscriptions"
    url: "https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-isnt-permanently-leaving-subscriptions-anthropic-says/"
  - name: "TechTimes — Fable 5 Subscription Ends Tomorrow: Per-Token Costs and Who Gets Hit Hardest"
    url: "https://www.techtimes.com/articles/319767/20260706/fable-5-subscription-ends-tomorrow-per-token-costs-who-gets-hit-hardest.htm"
  - name: "Digital Applied — Claude Fable 5 Pricing: The July 7 Usage-Credits Switch"
    url: "https://www.digitalapplied.com/blog/claude-fable-5-usage-credits-july-7-pricing-guide-2026"
  - name: "Codersera — Claude Fable 5 Usage Credits: What Changes After July 7, 2026"
    url: "https://codersera.com/blog/claude-fable-5-usage-credits-july-2026/amp/"
tags:
  - "anthropic"
  - "claude"
  - "fable-5"
  - "定價"
  - "AI訂閱"
relatedSlugs:
  - "2026-07-02-claude-fable5-export-ban-lifted-global-return-zh"
  - "2026-07-01-anthropic-claude-sonnet-5-agentic-launch-zh"
---

一週前，美國政府解除了對 Fable 5 的出口管制，Anthropic 最強大的模型得以回歸訂閱方案。然而，這段緩衝期在今天正式畫下句點。

自 2026 年 7 月 7 日起，Claude Fable 5 不再包含於 Pro、Max、Team，以及部分企業訂閱方案之中。若要繼續使用這款 Anthropic 的旗艦推理模型，用戶必須在帳戶中儲值「用量點數（usage credits）」，計費標準為**輸入每百萬 Token 10 美元、輸出每百萬 Token 50 美元**。

這使 Fable 5 成為 Anthropic 目前定價最高的模型——是 Opus 4.8 的整整兩倍（5 美元 / 25 美元），也是新推出的 Claude Sonnet 5 優惠價（2 美元 / 10 美元）的約五倍。對於重度用戶而言，從「訂閱包含」到「按量計費」的轉變，意味著今天起成本結構出現根本性改變。

## 為什麼會發生這樣的變化？

這次計費調整，直接源於 7 月 1 日 Fable 5 重新開放後的狀況。在美國商務部於 6 月 30 日解除出口管制後，Anthropic 給予了一週的過渡緩衝：Pro、Max、Team 及部分企業訂閱用戶，可在 7 月 7 日前以每週使用量上限 50% 免費存取 Fable 5。這段緩衝期今日屆滿。

Anthropic 官方說明，Fable 5 的需求「非常高且難以預測」。換言之，公司正透過定價機制進行容量管控——以付費門檻作為節流閥，同時加快基礎設施擴建，以應對全球龐大的使用需求。

一位 Claude Code 工程師在社群貼文中直接回應用戶疑慮：「雖然 Fable 5 在 7 月 7 日後將退出訂閱方案，但我們的目標是在產能允許後，盡快將 Fable 恢復為標準訂閱的一部分。」目前，Anthropic 尚未提供任何明確的恢復時間表。

## 哪些用戶受影響最大？

此次計費變動對不同用戶族群的衝擊程度截然不同。

**重度 Claude Code 用戶**所受衝擊最為明顯。一次跨多個檔案的重構任務，可能就會消耗數十萬個輸出 Token。以輸出每百萬 Token 50 美元計算，若開發者每天跑十個實質性的 coding 對話，光是模型費用就可能達到 50 至 100 美元——而昨天這些費用還是包含在每月 20 或 100 美元的訂閱方案內。

**輕度訂閱用戶**（主要用 Fable 5 處理偶發性複雜推理、法律分析或長文撰寫的 Pro 方案用戶）在絕對金額上或許還能接受按次計費，但從「已包含」到「額外收費」的心理門檻，仍會顯著改變使用習慣。預計大多數輕度用戶在成本不夠合理時，會選擇降級使用 Sonnet 5 或 Opus 4.8。

**企業用戶**面臨最複雜的操作問題。標準企業方案（Standard Enterprise）從未享有緩衝期——自 Fable 5 上線以來就一直採用用量點數計費。進階企業方案（Premium Enterprise）則共享了 7 月 7 日的截止日。若企業帳戶尚未開通用量點數，Fable 5 將直接無法使用，且不會自動降級到 Opus 4.8，這意味著所有明確呼叫 Fable 5 的工作流程或 AI Agent，在管理員完成設定前都將靜默失敗。

## Fable 5 的市場地位

Fable 5 在今年五月底，伴隨 Anthropic 歷史性的 650 億美元 H 輪融資（估值達 9,650 億美元，短暫超越 OpenAI）正式推出，並立即在所有主要 AI 基準測試中奪冠。SWE-Bench Verified、GPQA Diamond 等評測結果均顯示，Fable 5 在推理能力上大幅領先 GPT-5.5；在長程自主 coding 任務上，優勢更為懸殊。

然而，強大的能力帶來了 Anthropic 基礎設施團隊始料未及的需求衝擊。從 6 月 12 日到 6 月 30 日，全球存取中斷了三週。7 月 1 日重新開放後，用戶湧入的規模超出預期，容量管控措施因此而生。

從更宏觀的角度看，這也揭示了前沿 AI 的一個結構性現實：不同於邊際成本趨近於零的一般軟體，在 Fable 5 這種規模（據推測參數量達數千億）的推理服務，需要龐大的 GPU 叢集投資。Anthropic 正在積極擴建：上週宣布的 19 億美元 TeraWulf 核能供電肯塔基資料中心協議，是公司應對容量缺口的多項基礎設施投資之一。

## 競爭態勢的微妙時刻

這次調整的時機頗為敏感。Anthropic 正準備 IPO——6 月 1 日已向美國證交會秘密提交 S-1 草稿——並積極向機構投資者描繪健康的單位經濟效益與持續擴大的企業客戶基礎。在此關鍵節點，旗艦模型的使用門檻提高，無疑給競爭對手提供了攻擊角度。

OpenAI 的 GPT-5.5 仍包含在標準 API 方案和 ChatGPT 訂閱中；Google 的 Gemini 3.2 Pro 深度整合於 Workspace 訂閱，無需額外點數。兩者都可以向企業採購團隊強調「存取連續性」與「成本可預測性」——而這正是 Anthropic 目前在 Fable 5 上無法完全提供的。

Anthropic 的反駁也言之有理：目前沒有其他前沿模型能在長程 coding、進階科學推理及複雜多文件分析上與 Fable 5 匹敵。對於模型品質直接關乎生產力與產出品質的專業場景，溢價定價是有其依據的。但風險在於過渡期——當訂閱保障被打破，替代方案有機會趁隙建立用戶習慣。

## 用戶現在該怎麼做？

面對新的計費制度，訂閱用戶可依據自身需求採取以下行動：

- **立即開通用量點數**：若打算繼續定期使用 Fable 5，可在帳戶設定中新增點數，即時生效。
- **策略性分配任務**：將不同複雜度的工作分流至 Fable 5 與其他低成本模型。Claude Sonnet 5 以 2 美元 / 10 美元的優惠定價上市，在多數任務上的表現接近 Opus 4.8，是大多數不需要 Fable 5 頂尖推理能力任務的理想替代選項。
- **企業管理員**應立即稽核哪些團隊的 Agent 工作流程明確呼叫了 Fable 5，設定用量上限以避免超支，並確認自動化流程具備降級邏輯。
- **設定用量警報**：在消耗型計費模式下，費用隨使用量線性增加，不再受方案上限保護。Anthropic 主控台提供的用量警報功能是必要的防護機制。

一個值得注意的重要細節：以點數計費的 Fable 5 並非降級版本——無論透過訂閱還是點數存取，都是完全相同的模型，享有相同的 SLA、延遲特性與 API 保障。

## 未來展望

最關鍵的問題是：「臨時」究竟意味著多長？從 Anthropic 積極擴建基礎設施的步調來看，TeraWulf 肯塔基協議、AWS 早期基礎設施承諾，以及與三星洽談晶片合作等多項動作，顯示容量缺口正在獲得認真對待。

若問題在數週內解決，今天的計費變動將只是個小插曲。若問題延續至整個夏季，恰逢 OpenAI GPT-5.6 Sol、Terra、Luna 預計全面上市的時間窗口，Anthropic 的模型可及性問題就會在最需要展現 IPO 穩定性、贏得企業續約的關鍵時刻，成為不可忽視的競爭弱點。

目前，Fable 5 仍是開發者和企業可取得的最強大 AI 模型。只是，它不再是訂閱費用內的免費福利。在固定月費內享用前沿 AI 無限存取的時代，至少暫時落幕了。
