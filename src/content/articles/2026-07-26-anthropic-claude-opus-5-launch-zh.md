---
title: "Anthropic 發布 Claude Opus 5：以一半價格逼近頂尖模型效能"
summary: "Anthropic 於 7 月 24 日推出 Claude Opus 5，在 Frontier-Bench 程式碼評測中取得 43.3% 的高分，定價維持與前代相同的每百萬輸入 token 5 美元、輸出 25 美元。新模型即日起成為 Claude Code 與 Claude Max 的預設選項，直接對標日常自主代理工作流程。"
category: "ai-ml"
publishedAt: 2026-07-26
lang: "zh"
featured: true
trending: true
sources:
  - name: "Axios"
    url: "https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5"
  - name: "ExplainX"
    url: "https://explainx.ai/blog/claude-opus-5-launch-july-2026"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-07-24/anthropic-unveils-more-cost-efficient-model-for-everyday-tasks"
tags:
  - "Anthropic"
  - "Claude"
  - "大型語言模型"
  - "AI 模型"
  - "代理 AI"
relatedSlugs:
  - "2026-07-25-meta-anthropic-10b-compute-deal-zh"
  - "2026-04-05-anthropic-claude-mythos-zh"
---

Anthropic 在 7 月 24 日正式推出 Claude Opus 5，這是該公司迄今效能最具成本效益的前沿級模型。對一直在等待 Fable 5 旗艦機型能否以更低價位複製的開發者和企業買家而言，新模型在多項關鍵評測上的表現，答案相當肯定——某些測試項目甚至超越了更昂貴的旗艦版本。

## 在某些評測上超越旗艦

最引人矚目的數字來自 Frontier-Bench，這是一套專門測試模型撰寫、除錯及推理程式碼能力的高強度評測。Claude Opus 5 在此評測取得 43.3% 的成績，遠高於 Fable 5 的 33.7%——近十個百分點的領先優勢令業界觀察者感到意外。Anthropic 將這項差距歸因於針對代理工作流程的特定微調：在無人介入的情況下，模型必須串接數十個工具呼叫與自我修正，才能完成一個完整的作業階段。

在設計上刻意抵抗死記硬背式學習的新型推理測試 ARC-AGI-3 上，Opus 5 拿下 30.2% 的分數，大約是同價位競爭模型的三倍。在 OSWorld 基準的電腦使用評測中，它更達到 70.6%，直接指向自主代理市場的商業應用：模型已能可靠地控制桌面環境，無需持續的人工引導便能處理真實的辦公室作業流程。

## 定價與市場定位

Anthropic 維持與前代相同的價格：每百萬輸入 token 5 美元、輸出 25 美元，與企業部署主力 Opus 4.8 一致。這讓 Opus 5 的推出性質更像是一次透明升級，而非掩藏在新版本外衣下的漲價。

真正的頂尖旗艦 Fable 5 依然是面對最困難問題的建議選擇——Anthropic 將其定位為「挑戰 AI 能力邊界」的工具。Opus 5 瞄準的則是這條天花板以下的廣大領域：日常知識工作、多步驟研究、文件處理，以及在這些場景中動用旗艦算力代價過高的軟體開發任務。一旦企業客戶完成自己的成本效益計算，Anthropic 預期 Opus 5 將取代 Fable 5 成為絕大多數生產環境的首選。

此外，快速模式（Fast Mode）以兩倍基本費用提供約 2.5 倍的生成速度，專為面向終端用戶的聊天機器人、即時程式碼助理等延遲敏感型管線設計。

## 為代理工作流程而生，以可信賴為設計原則

Claude Opus 5 預設啟用思考鏈（thinking）推理，反映 Anthropic 的立場：對複雜任務而言，逐步推理應是基本預設，而非可選附加功能。模型配備 100 萬 token 的上下文視窗，每次生成最多支援 128,000 個輸出 token，兩項規格都明確有利於長時程代理任務，而非短暫的對話式交流。

對企業買家而言，比原始效能數字更關鍵的可能是對齊（alignment）表現。Opus 5 的不對齊審核評分為 2.30，是 Anthropic 所有現役模型中最低的——意味著在長時程自主運作期間，它較少產生與既定指令衝突或偏離預期目標的輸出。輸出結果的低變異性也是刻意的設計目標，在實際應用中體現為跨次重複執行時更可預期的行為，對生產環境的部署至關重要。

資安方面，Opus 5 採取了審慎的取捨：模型能夠勝任軟體漏洞識別，但 Anthropic 限制了它提供詳細利用指引的能力。公司明確說明這是刻意的設計選擇，而非能力上限——向企業資安團隊傳遞的訊號是：模型可以參與防禦性工作流程，但不會成為攻擊者的助力倍增器。

## 即時平台整合

Opus 5 在發布當天即成為 Claude Code 與 Claude Max 的預設模型，無縫替換前任，沒有任何過渡緩衝期。這個決定反映了 Anthropic 對模型生產就緒狀態的高度信心，也意味著他們將 Opus 5 視為真正的品質提升，而非橫向移動。

對使用 Anthropic API 的開發者而言，Opus 5 可透過標準識別碼 `claude-opus-5` 存取。透過合作協議部署 Anthropic 模型的第三方整合平台，預計將在數日內更新預設設定。

## 更宏觀的競賽格局

此次發布恰逢 OpenAI GPT-5.6 系列與 Google Gemini 3.6 Flash 相繼推出，前沿模型的發布間隔已壓縮至兩年前難以想像的速度。在這個背景下，Opus 5 的評測數字具有特殊的競爭意義：它證明大型語言模型的成本效能曲線仍在急速下彎。

Opus 5 的 Frontier-Bench 成績最令人深思的隱含意義，在於它揭示了能力擴散的走向：Anthropic 最昂貴的模型，如今在程式碼任務上已能被中階模型超越。若這個模式在各家實驗室持續，則意味著「頂尖」與「日常」AI 之間的能力差距，正以比定價結構調整更快的速度縮小。對那些以 Fable 5 定價鎖定企業合約的買家而言，這筆帳值得重新核算。

Anthropic 的賭注在於：面對縮窄的能力差距，正確的回應不是壓制成本更低的模型，而是加速推進頂尖模型的前沿。Fable 5 在最困難的新型問題評測上仍保有領先優勢。公司的目標是讓兩個層級相互追逐、共同向上——Opus 5 鞏固 Fable 5 已開拓的領域，Fable 5 則繼續向前推進未知的邊界。
