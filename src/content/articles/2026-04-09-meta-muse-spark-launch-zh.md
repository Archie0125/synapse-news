---
title: "Meta 發布首款自研 AI 模型 Muse Spark，告別開源路線正面迎戰 OpenAI 與 Google"
summary: "Meta 旗下超智慧實驗室（Meta Superintelligence Labs）正式推出第一款自研 AI 模型 Muse Spark，由前 Scale AI 執行長 Alexandr Wang 主導開發。這款閉源模型代表 Meta 放棄延續多年的 Llama 開源策略，在醫療推理與視覺多模態任務上表現突出，直接挑戰 OpenAI 與 Google 的前沿模型地位。"
category: "ai-ml"
publishedAt: 2026-04-09
lang: "zh"
featured: true
trending: true
sources:
  - name: "Meta AI Blog"
    url: "https://ai.meta.com/blog/introducing-muse-spark-msl/"
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html"
  - name: "Fortune"
    url: "https://fortune.com/2026/04/08/meta-unveils-muse-spark-mark-zuckerberg-ai-push/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/goodbye-llama-meta-launches-new-proprietary-ai-model-muse-spark-first-since"
  - name: "Artificial Analysis"
    url: "https://artificialanalysis.ai/articles/muse-spark-everything-you-need-to-know"
tags:
  - "Meta"
  - "Muse Spark"
  - "Alexandr Wang"
  - "AI 模型"
  - "超智慧實驗室"
  - "大型語言模型"
  - "多模態"
relatedSlugs:
  - "2026-04-08-meta-hybrid-open-source-models-zh"
  - "2026-04-04-open-source-llm-race-zh"
  - "2026-04-05-openai-gpt-oss-open-weight-zh"
---

在 Mark Zuckerberg 以約 140 億美元的天價條件延攬 Alexandr Wang 入主 Meta 的九個月後，這家公司終於給出了市場最想看到的答案：Muse Spark。這款由 Meta 超智慧實驗室（Meta Superintelligence Labs，MSL）打造的首款自研大型語言模型，於週三正式發布，在業界引發審慎但真實的關注。

Muse Spark 在開發期間代號為「Avocado」，代表著 Meta AI 戰略的一次根本性轉向。多年來，Meta 在 AI 領域的競爭識別度幾乎與 Llama 開源系列密不可分。如今，Muse Spark 幾乎徹底拋棄了這個姿態——這是一款閉源模型，Meta 只淡淡表示「希望未來版本能夠開源」。對於一家以開放共享為研究文化核心的公司而言，這個轉變的象徵意義不容忽視。

## Muse Spark 的能力邊界

Muse Spark 支援語音、文字與圖像輸入，但目前僅輸出文字，Meta 表示後續版本將補足這個缺口。模型有兩種運作模式：標準模式與「Contemplating（深思）」模式——後者能並行啟動多個子代理，分頭處理複雜任務的不同面向。Meta 描述深思模式足以「媲美 Gemini Deep Think 和 GPT Pro 等前沿模型的極限推理模式」。

在 Artificial Analysis Intelligence Index（綜合能力排行榜）上，Muse Spark 拿到 52 分，躋身全球前五，超越 Claude Sonnet 4.6、GLM-5.1、MiniMax M2.7 與 Grok 4.20，但仍落後於 Gemini 3.1 Pro Preview 和 GPT-5.4。這不是業界最頂尖的模型，但確實具備真正的競爭力。

Muse Spark 真正出類拔萃之處在於醫療推理。在高難度醫療問答基準 HealthBench Hard 上，它以 42.8% 的成績擊敗包括 GPT-5.4 和 Claude Opus 4.6 在內的所有競爭對手。Wang 加入 Meta 時就明確宣示：目標不只是通用前沿模型，而是在醫療與科學領域具備深度專業能力的模型。

視覺多模態表現同樣亮眼。Muse Spark 在 MMMU-Pro 基準上拿到 80.5%，全球排名第二，僅次於 Gemini 3.1 Pro Preview（82.4%）。在深思模式下，它在 CharXiv Reasoning（科學圖表理解）上以 86.4 分超越 Gemini 的 80.2 分與 GPT-5.4 的 82.8 分。

推理能力上，Muse Spark 深思模式在「人類最後考試」（Humanity's Last Exam）這個以極度困難著稱的專業知識測試中，拿到 50.2% 的成績，高於 GPT-5.4 Pro 和 Gemini Deep Think。

## 效率才是真正的殺手鐧

除了跑分，Meta 更大力強調運算效率。公司聲稱 Muse Spark 能以超過十倍少的算力，達到前一代 Llama 4 Maverick 中型模型的同等能力水準。這個效率主張在一個推論成本愈來愈成為戰略差異化因素的市場中舉足輕重——尤其是跨越 WhatsApp、Instagram、Facebook 等數十億用戶平台的 Meta，對 GPU 帳單極度敏感。

Wang 和 MSL 這九個月不只是在訓練模型，而是從頭重建 Meta 的整套 AI 基礎設施：全新的訓練管線、改良的資料處理方法、重新設計的評估框架。公司表示，正是這次徹底的地基重建，才讓運算效率大幅提升成為可能。

## 仍然存在的差距：程式碼能力

Meta 對 Muse Spark 的短板出奇坦誠：寫程式是公認的弱項。Meta 高管向媒體坦承，雖然模型「在多模態理解和醫療資訊處理等特定任務上具有競爭力，但在程式碼方面與現有模型仍有差距」。這對開發者社群的採用影響不小——這個族群最可能實際呼叫新模型 API、建立起 Meta 所需的第三方生態系統。

Meta 表示持續「投資於當前效能存在差距的領域，特別是長程代理系統和程式碼工作流」。考量到 Muse Spark 只歷時九個月開發，今年晚些時候推出聚焦程式碼能力的後續版本相當可期。

## 上線與開放方式

Muse Spark 目前已在 meta.ai 和 Meta AI 助理網站上線，初期僅限美國使用者存取。整合至 WhatsApp、Instagram、Facebook、Messenger 及 Meta AI 智慧眼鏡的工作預計在未來數週內完成。企業合作夥伴可透過私人預覽方式申請 API 存取。

模型不開源，Meta 也未承諾任何公開釋出模型權重的時間表。這讓公司陷入一個陌生的處境：違背了它花費多年透過 Llama 精心培育的開發者文化。這個取捨最終能否換來商業回報，業界將密切觀察。

## 更大的賭注

Muse Spark 的發布，關乎公信力，不下於技術能力本身。Meta 在 Wang 這筆交易上投入了 140 億美元（包含估值、股權與承諾），然後眼睜睜看著 OpenAI 推出 GPT-5.4、Anthropic 確認 Claude Mythos 存在、Google 發布 Gemini 3.1 Pro。Meta 需要證明，這筆投資正在產出真實的成果。

Muse Spark 給出的答案是：一款在特定領域——醫療、視覺與複雜推理——真正與最頂尖系統一較高下，且運算效率出色的模型。但 Meta 自己也承認，它不是全面的前沿領導者。

儘管如此，Muse Spark 確立了 Meta 作為真正全棧 AI 實驗室的地位，而非僅僅是開源模型的發行者，也為 MSL 下一階段的產品藍圖奠定基礎。Llama 時代的 Meta AI 尚未落幕——公司表示開源仍是長期策略的一部分。但 Muse Spark 標誌著一個清晰的轉折：Meta 現在以閉源產品與企業界和開發者社群正面競爭，而勝負將在未來幾個季度逐漸揭曉。
