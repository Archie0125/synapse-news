---
title: "微軟將 Aion 1.0 直接內建於 Windows：無需雲端的端側 AI 代理"
summary: "微軟在 Build 2026 發表 Aion 1.0——兩款直接內建於 Windows 11 的小型語言模型。Aion 1.0 Plan 是一個 140 億參數、32K 上下文的推理與工具呼叫模型，隨相容裝置開箱即用，可實現完全本地化的代理工作流程。Aion 1.0 Instruct 是更快的通用 SLM，今日在 Edge Insider 進入預覽，開放權重將於 7 月登陸 Hugging Face。"
category: "developer-tools"
publishedAt: 2026-06-03
lang: "zh"
featured: false
trending: false
sources:
  - name: "Windows Forum — Aion 1.0 APIs"
    url: "https://windowsforum.com/threads/microsoft-aion-1-0-on-device-ai-for-windows-11-instruct-plan-and-new-apis.421596/"
  - name: "WinCentral"
    url: "https://thewincentral.com/microsoft-aion-1-ai-models-expanded-windows-ai-apis-build-2026/"
  - name: "Windows Developer Blog — Build 2026"
    url: "https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/"
  - name: "byteiota"
    url: "https://byteiota.com/windows-aion-1-0-microsoft-ships-on-device-ai-into-windows-itself/"
  - name: "AI Weekly"
    url: "https://aiweekly.co/alerts/microsoft-unveils-aion-10-on-device-ai-at-build-2026"
tags:
  - "微軟"
  - "Aion 1.0"
  - "Windows 11"
  - "端側AI"
  - "SLM"
  - "Build 2026"
  - "開發工具"
  - "智能代理"
relatedSlugs:
  - "2026-06-02-microsoft-build-2026-project-polaris-windows-agents-zh"
  - "2026-06-02-microsoft-mai-thinking-1-reasoning-model-build-zh"
  - "2026-06-03-nvidia-rtx-spark-superchip-computex-zh"
---

在過去五十年的歷史中，Windows 一直是執行他人軟體的平台。在 Build 2026，微軟做出了迄今最直接的改變：它正將自家 AI 模型作為作業系統本身的一等公民元件出貨，和字型渲染器、檔案系統驅動程式一樣與 Windows 捆綁——在使用者安裝任何應用程式之前就已就位、可用、運行中。

這個產品叫做 Aion 1.0，是一個從頭為端側推理設計的小型語言模型家族，於 6 月 2 日在微軟於舊金山舉辦的年度開發者大會 Build 2026 發表。發表內容涵蓋兩個具有不同能力和部署目標的模型，以及 Windows AI API 的大幅擴展——第三方開發者可透過這個介面呼叫上述模型。

## Aion 1.0 Plan：本地代理的大腦

兩個模型中技術意義更深遠的是 Aion 1.0 Plan。這是一個 140 億參數、32,000 token 上下文長度的推理與工具呼叫模型，設計目標是讓微軟所稱的「完全代理工作流程」能夠在裝置本地執行——無需雲端連線。

實際意義：應用程式可以向 Aion 1.0 Plan 下達高層級指令（「找出過去一個月所有關於 X 專案的電子郵件，並將行動事項整理成文件」），模型將把目標分解為步驟，在每個步驟呼叫對應的 Windows 工具和 API，管理中間檔案狀態，並協調子代理流程以完成任務。這是雲端 AI 代理的架構——LLM 作為協調者、工具作為能力——完全在本地算力上運行。

Aion 1.0 Plan 隨 Windows 內建於「相容裝置」上，微軟將其定義為具備足夠 NPU 或 GPU 算力、能以互動速度執行 140 億參數推理的機器。硬體門檻尚未公布，但 Nvidia 在 Computex 2026 發表的 RTX Spark 平台——具備 1 petaFLOP FP4 算力和 128GB 統一記憶體——代表 Aion 1.0 Plan 能夠善用的高階配備。在搭載 NPU 級晶片的中階 AI PC 上，效能表現將相對受限。

32K 上下文窗口讓 Aion 1.0 Plan 有別於早期的 Windows 端側模型。過去的 Windows AI 努力通常上限在 2,000 至 4,000 token 的上下文——足以改寫句子、分類意圖，卻不足以對多文件任務進行連貫推理。32K 開啟了真正的文件理解大門：一份法律合約、一個完整程式碼檔案、一長串電子郵件往返。

## Aion 1.0 Instruct：日常使用的引擎

第二個模型是 Aion 1.0 Instruct，定位為更快、更高效的通用 SLM，用於日常文字智能任務。微軟形容它「比現有 Windows OS SLM 更小、更快、更高效」——這裡指的是自 Windows 11 24H2 起驅動 Windows AI 功能的 Phi 系列模型。

Aion 1.0 Instruct 負責摘要、改寫建議、意圖分類和無障礙功能——那層使用者不一定意識到其存在、卻在應用程式中無所不在的環境文字智能。這個模型將驅動檔案總管的右鍵摘要、即時字幕清理和 Windows 搜尋的意圖比對。

開發者今日即可透過 Edge Insider 頻道試用 Aion 1.0 Instruct 預覽版。微軟承諾於 2026 年 7 月在 Hugging Face 發布開放權重，讓開發者能在廣泛 Windows 推出前，針對特定應用領域進行驗證和微調。

## 擴展的 Windows AI API 層

除了 Aion 系列模型，微軟同時宣布對 Windows AI API 的重大擴展——這是第三方應用程式無需自行打包推理套件、直接呼叫端側智能的程式介面。

三項新能力現已可用或已宣布：

**NPU 和 CPU 上的語音轉文字** — 完全本地執行的即時語音辨識，無需將音訊傳送至任何雲端端點。這解決了雲端語音辨識的隱私和延遲限制，對音訊資料不得離開裝置的醫療、法律和企業應用場景意義尤其重大。

**獨立顯卡上的文字智能** — 將端側 SLM 能力擴展至搭載獨立顯卡（包括遊戲筆電和工作站）的機器，讓先前需要 NPU 硬體的文字智能功能更廣泛可用。

**CPU 上的影片超解析度** — 在無相容 GPU 或 NPU 硬體的機器上，以 CPU 執行 AI 放大技術，用較低的吞吐量換取更廣的相容性。

API 的設計將硬體細節抽象化，遠離應用程式開發者：應用程式呼叫語音轉文字 API，作業系統負責將工作負載路由到可用的加速器，並在硬體能力下降時依序退回。

## 為何這個架構至關重要

從微軟試圖預防的情境，Aion 1.0 的競爭邏輯最為清晰。目前 AI 驅動 Windows 應用程式的主流工作流程是：每次推理都呼叫雲端 API（通常是 OpenAI、Anthropic 或 Azure AI）。這個模式容易建構，但從微軟的視角看存在三個問題。

第一，每次 Windows 應用程式使用 AI，都讓微軟持續依賴第三方 AI 提供商——這是微軟投資 MAI 系列自有模型試圖化解的結構性弱點。第二，雲端推理的延遲和成本特性，讓作業系統看起來「有時聰明」而非「真正智能」的那種隨時可用的環境 AI 響應成為不可能。第三，在企業環境中越來越重要的是：用戶資料會離開裝置。

透過將 Aion 1.0 作為 Windows 元件出貨——以標準 API 提供給所有應用程式、在用戶自有硬體上本地運行——微軟打造了一個應用程式開發者無需雲端依賴即可建構的 AI 能力底座。類比是 DirectX：微軟標準化繪圖 API，讓顯卡廠商在硬體上競爭，開發者針對標準撰寫程式，Windows 成為讓這個生態系成為可能的平台。

若 Aion 1.0 成為 AI 版 DirectX——一個所有 Windows 應用程式都能呼叫的本地推理共享基礎設施——它將把 AI 應用層的競爭態勢向微軟方向大幅傾斜。

## 對開發者的賭注

微軟要求第三方開發者把本地 AI 當作可靠的基礎設施而非可選的強化功能。這需要信任：相信 API 將在足夠比例的 Windows 安裝基礎上存在、效能表現一致，並跨越 OS 世代持續維護。

承諾在 Hugging Face 上以開放權重發布 Aion 1.0 Instruct 是一個有意義的信號：讓開發者能夠驗證模型行為、針對特定領域建立微調版本，並避免推理層面的廠商鎖定。開放權重發布也讓 Aion 1.0 Instruct 有機會在 Windows 以外的場景本地部署，與 Phi-4 Mini、Mistral 7B 和 Llama 家族在端側 SLM 生態系中競爭。

對於 Aion 1.0 Plan，隨 Windows 內建的發布模式意味著問題不在開發者能否取用，而在他們是否願意圍繞它設計應用程式。這是微軟在 1995 年以 DirectX 下的同一個生態賭注：投資平台，開發者終將跟進。

Aion 1.0 究竟能催生一個真正以代理為本的 Windows 應用程式世代，還是成為大多數用戶從未親眼看見的精工之作，取決於微軟直接掌控範圍之外的因素：硬體採用率、開發工具成熟度，以及 32K 上下文模型是否真的足夠強大，能夠勝任讓本地代理令人信服而非僅僅「本地化」的複雜推理任務。

軟體已在 Windows 裡。硬體將在今年秋天進入筆電。剩下的，由開發者決定。
