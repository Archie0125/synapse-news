---
title: "Groq 在 Nvidia 以 200 億美元授權 LPU 技術後，再融資 6.5 億美元轉型 AI 算力雲服務"
summary: "AI 推理晶片新創 Groq 正向現有投資人籌集最多 6.5 億美元，以支持公司轉型為 AI 算力雲（Neocloud）服務商。此前，Nvidia 以創紀錄的 200 億美元完成對 Groq 語言處理單元（LPU）推理技術的授權，並同步延攬 Groq 創辦人 Jonathan Ross 等核心管理層加入，由財務長 Simon Edwards 接任 CEO，正式啟動 Groq 2.0 時代。"
category: "startups"
publishedAt: 2026-05-30
lang: "zh"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/29/after-nvidias-20b-not-acqui-hire-ai-chip-startup-groq-reportedly-raising-650m/"
  - name: "Axios"
    url: "https://www.axios.com/2026/05/28/groq-650-million-nvidia"
  - name: "TechRepublic"
    url: "https://www.techrepublic.com/article/news-nvidia-licenses-groq-ai-inference-technology-in-20b-deal/"
  - name: "Seeking Alpha"
    url: "https://seekingalpha.com/news/4598000-groq-pursues-650m-fundraise-following-nvidias-20b-licensing-deal-report"
tags:
  - "Groq"
  - "Nvidia"
  - "AI 推理"
  - "LPU"
  - "算力雲"
  - "融資"
  - "半導體"
relatedSlugs:
  - "2026-05-27-nvidia-vera-rubin-q3-launch-5x-blackwell-zh"
  - "2026-05-22-nvidia-q1-fy2027-earnings-china-huawei-concession-zh"
---

AI 晶片戰爭剛剛產生了一個耐人尋味的結局。Groq——這家花費七年時間以自主研發的語言處理單元（LPU）挑戰 Nvidia GPU 霸主地位的新創公司——已悄然成為 Nvidia 最重要的推理技術供應商，同時正籌集 6.5 億美元，準備以雲端服務商的身分重新出發。

這兩個發展在 5 月 28 至 29 日由 Axios 和 TechCrunch 相繼確認，解答了半導體業界自 2025 年 12 月以來的疑問：Nvidia 與 Groq 之間的安排並非傳統收購，卻比一般採購協議影響深遠得多。Groq 正在押注：這筆安排所帶來的收益，加上新一輪融資，足以支撐它在全球最激烈競爭的基礎設施市場之一開創真正的第二章。

## Nvidia 的 200 億美元賭注

2025 年 12 月 24 日，Nvidia 與 Groq 宣布了一項約 200 億美元的技術授權協議——Nvidia 迄今最大規模的交易。協議給予 Jensen Huang 的公司非排他性使用 Groq LPU 架構的授權，同時伴隨著大規模人才移轉：Groq 創辦人兼執行長 Jonathan Ross、總裁 Sunny Madra，以及大多數資深工程管理層已加入 Nvidia。

這份協議在結構上是授權交易而非收購——Groq 繼續作為獨立法人存在，財務長 Simon Edwards 接任執行長。GroqCloud（公司的推理即服務平台）被明確排除在交易範圍之外，持續獨立運營。

**Nvidia 為何需要 LPU？**

LPU 的架構差異化之處，對 Nvidia 的下一階段布局至關重要。相較於設計用於兼顧訓練與推理的通用平行處理 GPU，Groq 的晶片採用確定性、以編譯器為核心的設計，以極低延遲、高度可預測的吞吐量執行 AI 推理任務。在基準測試中，Groq 系統在特定大型語言模型推理任務上展現出比 GPU 方案快 2 至 3 倍的速度優勢，尤其是需要 50 毫秒以下回應時間的場景。

隨著 AI 部署進入成熟期，這種效能特性愈發重要。訓練模型只需一次；向用戶提供服務則每天發生數十億次。語音介面、金融交易系統、自駕車決策、互動式 AI 助理——這些即時應用要求的延遲以個位數毫秒計。Nvidia 的 Blackwell 和 Vera Rubin 架構在訓練和吞吐量上無可匹敵，但 Groq LPU 的確定性、低抖動特性，填補了以 GPU 為中心的設計未能高效覆蓋的空白。

## Groq 2.0：6.5 億美元的第二章

這輪最多 6.5 億美元的新融資，目標投資人是 Groq 的現有股東。兩位主要投資機構 Disruptive 和 Infinitium 已承諾在其他投資人放棄比例認購權時包下全額，顯示即便在核心管理層移轉至 Nvidia 之後，他們對新戰略方向仍有強烈信心。

這筆資金旨在支持業界所稱的「Groq 2.0」：從晶片製造和直接硬體銷售，轉型為 AI 算力雲（Neocloud）服務商。算力雲模式以受管理服務形式提供專屬、高效能的推理基礎設施——向企業客戶提供公有雲共享資源模式往往無法穩定達到的吞吐量保證、延遲服務水準協議（SLA），以及專業工具鏈。

算力雲的商業邏輯正在被市場驗證。CoreWeave 190 億美元的 IPO，以及 Lambda 成長至年化 5 億美元收入的軌跡，證實了對推理專屬雲端服務的切實市場需求。論點直截了當：AWS、Azure、Google Cloud 提供大規模的廣泛 AI 基礎設施，但共享資源模式無法為推理密集型生產工作負載提供持續一致的效能保障。算力雲業者以專屬叢集、可預測定價和效能 SLA 填補這個缺口。

GroqCloud 現有的開發者社群，是 Groq 在這個市場的核心差異優勢。平台目前提供以 LPU 硬體驅動的主流開源模型推理 API，包含 Llama 4、Mixtral-8x22B 和 Gemma 3，開發者滿意度評分持續優異，在業界基準測試中頻繁被評為最快的可用推理選項。6.5 億美元融資將用於擴充基礎設施、建立企業銷售能力，以及開發服務生產級工作負載所需的軟體工具鏈。

## 留守團隊的挑戰

Jonathan Ross、Sunny Madra 及多數資深工程管理層轉投 Nvidia，是 Groq 2.0 面臨的最嚴峻運營挑戰。Ross 不僅是執行長，更是 LPU 設計哲學的核心架構師；他的離開既代表技術領導力的流失，也可能預示著留守公司在未來 LPU 硬體演進上的天花板。

接任執行長的 Simon Edwards 背景在財務運營與雲端業務建模。他的任務顯然是在技術基礎（現大部分歸屬 Nvidia）之上建立算力雲業務，聚焦商業執行、企業銷售，以及 GroqCloud 平台開發，而非下一代晶片設計。

支持這輪 6.5 億美元融資的投資人，顯然判斷 GroqCloud 的商業機會足夠大，值得在原始創辦團隊缺席的情況下繼續押注。這個判斷是否能在多年的建設期間獲得驗證，很大程度上取決於 GroqCloud 能否將開發者社群轉化為企業合約。

## 推理經濟的更大格局

Groq 的故事是當前 AI 基礎設施轉型的縮影。AI 熱潮的第一階段（2020 至 2024 年）以訓練為主軸：誰能建最大的叢集、訓練最大的模型、推動能力前沿。Nvidia 在這個階段贏得決定性勝利。

第二階段——推理時代——現在才是核心戰場。Anthropic、OpenAI、Google DeepMind 和 Meta 每天運行數十億次推理查詢。服務這些查詢的基礎設施成本，是 AI 產品規模化後的主要運營費用。誰能以低成本、高可靠性和低延遲在規模上解決推理問題，就能贏得一個耐久、經常性收入的基礎設施業務。

Groq 2.0 在算力雲市場的直接競爭者陣容強大：已上市的 Cerebras、5 月融資 2.2 億美元的 Fractile、3 月以 23 億美元估值融資 4 億美元的 Rebellions，以及已建立相當規模的 CoreWeave 和 Lambda。這是一個資金充裕、競爭激烈的市場。

Groq 以 200 億美元將 LPU 智慧財產權授權給最大競爭對手，再用所得資本重組為服務商的路徑，代表 AI 基礎設施生態的一種新興模式：專業架構創新被主導平台吸收，原創公司以服務提供者身分延續，依託已出售的技術能力繼續運作。

這個安排是否能支撐一個可防禦的算力雲業務，還是最終演變為被更大雲端業者收購的過渡安排，未來十二到十八個月將逐漸明朗。推理經濟才剛起步，Groq 的第二章將是這場競爭中最值得追蹤的故事之一。
