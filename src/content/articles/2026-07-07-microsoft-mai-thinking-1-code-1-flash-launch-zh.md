---
title: "微軟推出七款自研 MAI 模型，首款推理 AI 宣示脫離 OpenAI 依賴"
summary: "微軟在 Build 2026 發表七款全自研 AI 模型，旗艦之作 MAI-Thinking-1 是公司首款推理模型，從零訓練、不依賴 OpenAI 或 Anthropic 的模型權重；另一款 MAI-Code-1-Flash 則深度整合至 GitHub Copilot。此舉標誌著微軟向 AI 自主之路邁出最關鍵的一步。"
category: "developer-tools"
publishedAt: 2026-07-07
lang: "zh"
featured: false
trending: true
sources:
  - name: "Microsoft AI — Building a Hill-Climbing Machine: Launching Seven New MAI Models"
    url: "https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/"
  - name: "Microsoft AI — Introducing MAI-Code-1-Flash"
    url: "https://microsoft.ai/news/introducingmai-code-1-flash/"
  - name: "CNBC — Microsoft and Google Take On Anthropic and OpenAI in AI Coding Models"
    url: "https://www.cnbc.com/2026/06/01/microsoft-and-google-take-on-anthropic-and-openai-in-ai-coding-models.html"
  - name: "Euronews — Microsoft Launches Its Own AI Models to Take On OpenAI and Anthropic"
    url: "https://www.euronews.com/next/2026/06/03/microsoft-launches-its-own-ai-models-to-take-on-openai-and-anthropic"
tags:
  - "微軟"
  - "MAI"
  - "github-copilot"
  - "coding-AI"
  - "推理模型"
  - "開發工具"
relatedSlugs:
  - "2026-07-06-cursor-ios-mobile-app-spacex-coding-agents-zh"
  - "2026-07-04-google-deepmind-brain-drain-shazeer-jumper-zh"
---

過去三年，微軟的 AI 戰略幾乎與 OpenAI 密不可分。130 億美元的投資、Azure 獨家部署協議，以及 GPT 模型在所有微軟產品線的深度整合，讓兩家公司在 AI 基礎設施的語境下幾乎被劃上等號。

這個時代還沒結束，但正在改變。

在 2026 年 6 月的 Microsoft Build 大會上，微軟發表了七款完全自研的模型，冠以「MAI」品牌（Microsoft Artificial Intelligence）。這七款模型無一來自 OpenAI 模型的蒸餾或微調。發表陣容中最受矚目的兩款是：**MAI-Thinking-1**，微軟首款從零訓練的推理模型；以及 **MAI-Code-1-Flash**，一款專為 GitHub Copilot 打造的 coding 模型。這是微軟自 OpenAI 合作以來，對 AI 自主能力最強硬的一次宣示。

## MAI-Thinking-1：從零打造的推理模型

技術上最受關注的成就，是這款 350 億個 active 參數的推理模型。微軟強調，MAI-Thinking-1「從頭開始在乾淨的商業授權資料上訓練，未使用任何第三方模型蒸餾」。

這個「資料來源聲明」的背後有深刻的商業邏輯。隨著 AI 訓練資料的版權與授權問題訴訟頻發，從一開始就採用商業授權資料，能為企業和政府部署提供法律上站得住腳的基礎，也繞開了「從其他前沿模型蒸餾是否繼承了原模型訓練資料爭議」這個越來越棘手的問題。

在基準測試表現上，MAI-Thinking-1 達到當前市場的「中階」水準。微軟聲稱它在盲測人類偏好評估中優於 Anthropic 的 Claude Sonnet 4.6，並在 SWE-Bench Pro coding 任務中比肩 Claude Opus 4.6——這是相當有參考性的對標，因為 Sonnet 4.6 在 2025 至 2026 年間是企業部署最廣泛的模型之一。

模型配備 12.8 萬 Token 的上下文視窗，目前透過 Microsoft Foundry 開放私人預覽，完整上線時程尚未公布。

## MAI-Code-1-Flash：嵌入 GitHub Copilot 的新引擎

雖然 MAI-Thinking-1 是旗艦發表，但 MAI-Code-1-Flash 對開發者社群的即時影響可能更為深遠。這是一款 50 億參數的模型，訓練資料來自 GitHub Copilot 在生產環境中的實際工作流程——反映的是真實規模軟體開發的行為模式，而非學術基準或精選資料集。

在效能分級上，它與 Claude Haiku 4.5 和 Gemini 3.5 Flash 同屬高效輕量層，但微軟聲稱儘管參數量更小，它在 SWE-Bench Pro 上的表現仍優於兩者。在推理成本上，它的定價與 Haiku 相近——設計目標是成為補全建議、Tab 提示等高頻低延遲任務的預設選項。

MAI-Code-1-Flash 正陸續向 Visual Studio Code 中的 GitHub Copilot Individual 用戶開放，出現在模型選擇器中，並納入「自動」選項——意味著未明確選擇模型的用戶，可能已在不知不覺中使用它。整合 GitHub Actions、Copilot Workspace 和 Azure DevOps 的計畫已在路線圖中。

## 完整 MAI 模型家族

Build 2026 發表的七款模型除上述兩款外，還包含：

- **MAI-Image-2.5**：文字生成圖像及圖像編輯，整合至 Microsoft Designer 和 Bing Image Creator
- **MAI-Image-2.5-Flash**：高吞吐量圖像生成的輕量版本
- **MAI-Transcribe-1.5**：語音轉文字模型，鎖定 Teams 和 Azure AI Speech
- **MAI-Voice-2**：高品質語音合成，用於 Teams 自動回覆及 Azure 認知服務
- **MAI-Voice-2-Flash**：高效語音生成輕量版

這個涵蓋多模態的模型家族清楚說明，微軟打造的不只是單點能力，而是一套縱向整合的 AI 基礎設施——讓自研模型成為橫跨 Teams、Office、Azure 和 GitHub 的預設選項，而非 OpenAI 模型。

## 企業級技術：Microsoft Frontier Tuning

此次發表中戰略意義最深的技術，是 **Microsoft Frontier Tuning**——一套讓企業客戶在安全隔離環境中，以自有專屬工作流程資料對 MAI 模型進行微調的能力。

微軟展示了一個用 Excel 生產環境支援工作流程微調的 MAI-Thinking-1 版本，在 Excel 特定任務上達到 GPT-5.4 水準，但每次推理所需算力「最多節省 10 倍」。對於每年處理數千萬次 Excel 相關支援互動的大型企業而言，在品質不妥協的前提下降低 10 倍算力成本，代表極具說服力的單位經濟效益改善。

Frontier Tuning 使微軟能夠提供一個 Anthropic 和 OpenAI 目前都無法大規模提供的價值主張：在商業授權乾淨的基礎模型上，實現完全私有、客戶租戶內的模型客製化，並保證資料不離境。這個組合對金融服務、醫療、政府等受監管行業尤為吸引——這些領域的資料主權和來源文件要求不容退讓。

## 競爭態勢

AI coding 市場已成為企業軟體中競爭最激烈的類別，原因在於它既高價值又具黏性——開發者一旦圍繞特定 AI coding 助手建立工作流程整合，若沒有充分理由就不會輕易轉換。

目前 Anthropic 在純模型能力上以 Claude Code 和 Fable 5 領跑；OpenAI 的 Codex 透過既有 GitHub Copilot 整合廣泛部署；Google 在悄悄提升 Gemini 的 coding 表現——Gemini 3.1 Pro 在六月的評測中躍升 6 分；DeepMind 研究人員也在持續推進程式碼生成的前沿。

微軟將 MAI-Code-1-Flash 置入 Copilot 預設體驗，走的是與純效能競爭截然不同的路線——**通路制勝**。GitHub 擁有超過 1 億名註冊開發者，並整合進多數財富 500 強企業的 CI/CD 工作流程。即使是效能上排第三或第四的模型，若能無縫嵌入開發者每天使用的工具，光靠降低摩擦就足以奪取可觀的市場份額。

長遠來看，整個 MAI 生態的目標更為明確：若微軟能讓自研模型成為 Teams、Office、Azure 和 GitHub 上成本合理、來源乾淨、企業主權的預設選項，就能逐步降低對 OpenAI 定價與可用性的結構性依賴——而這個依賴在 OpenAI 準備 IPO、開拓更廣泛客戶關係的當下，已日益顯得脆弱。

## 對開發者的實際意義

對個人開發者和工程團隊而言，MAI 的發布改變了工具選型的幾個具體考量：

- **GitHub Copilot 用戶**應針對自己的使用場景評估 MAI-Code-1-Flash 是否帶來明顯改善。針對特定任務的模型效能宣稱，未必能在所有程式語言和任務類型上均等體現。
- **Azure 客戶**應密切追蹤 MAI-Thinking-1 在 Microsoft Foundry 的上線進度，特別是在訓練資料來源文件是採購或合規要求的應用場景。
- **企業 AI 團隊**在評估微調選項時，應認真審視 Microsoft Frontier Tuning。若 10 倍效率宣稱在其特定領域成立，對高頻特定任務部署而言，這是相當有說服力的單位經濟故事。

MAI 的發布並非宣告微軟拋棄 OpenAI——兩家公司在基礎設施層面仍深度綑綁，Azure 依然是 OpenAI 自身工作負載的獨家雲端。但這是一個明確訊號：微軟正在建立選擇權，按自己的時間表、以自己的技術逐步降低依賴。在 AI 競賽中，這種戰略靈活性的價值，遠超任何單一的基準分數。
