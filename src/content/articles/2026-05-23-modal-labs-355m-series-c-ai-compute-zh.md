---
title: "Modal Labs 完成 3.55 億美元 C 輪融資，估值 46.5 億美元，無伺服器 GPU 算力需求爆發"
summary: "提供無伺服器 GPU 基礎設施的新創公司 Modal Labs 完成由 Redpoint Ventures 和 General Catalyst 領投的 3.55 億美元 C 輪融資，估值達 46.5 億美元，是八個月前估值的逾四倍。公司年化營收在不到一年內從 6000 萬美元激增五倍至 3 億美元，客戶涵蓋 Anthropic、Meta、Cognition 等頂尖 AI 機構，已成為 AI 時代成長最快的基礎設施公司之一。"
category: "developer-tools"
publishedAt: 2026-05-23
lang: "zh"
featured: false
trending: true
sources:
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/05/21/serverless-ai-infrastructure-startup-modal-labs-seals-355m-funding-round/"
  - name: "Tech Startups"
    url: "https://techstartups.com/2026/05/21/modal-labs-raises-355m-quadrupling-valuation-to-4-65b-as-ai-infrastructure-demand-surges/"
  - name: "Modal Blog"
    url: "https://modal.com/blog/modal-series-c"
tags:
  - "開發工具"
  - "AI基礎設施"
  - "融資"
  - "無伺服器"
  - "GPU算力"
  - "Modal Labs"
relatedSlugs:
  - "2026-05-23-exa-250m-series-c-ai-search-agents-zh"
  - "2026-05-20-fractile-220m-series-b-ai-inference-chips-zh"
  - "2026-05-17-code-with-claude-2026-managed-agents-zh"
---

在建構 AI 應用的開發者中間，有一個反覆出現的抱怨：GPU 貴、雲端伺服器管理複雜，從筆電上跑通模型到在正式環境穩定部署，中間的落差大得令人沮喪。Modal Labs 的誕生，正是為了填補這個落差。2026 年 5 月 21 日，公司宣布完成由 Redpoint Ventures 和 General Catalyst 共同領投的 3.55 億美元 C 輪融資，估值達 46.5 億美元——不到一年前估值的四倍多。

這輪融資在結構上也頗為罕見。由於投資人需求過於旺盛，本輪以兩批不同估值結束：第一批投資人以 25 億美元估值入股，隨後第二批加入時估值已被推高至 46.5 億美元。一輪融資在尚未結束之前就自行漲價——這個現象，充分說明了資本追逐 AI 基礎設施層的激烈程度。

## Modal 到底在做什麼？

Modal 的核心產品用一句話說清楚並不難，但執行的技術複雜度相當高：讓開發者能在雲端 GPU 上執行 Python 函式，完全不需要佈建或管理任何伺服器。

一個想運行圖像生成模型、微調語言模型、處理資料集或執行 AI 推理工作的開發者，只需要編寫幾乎和本地 Python 一模一樣的程式碼——在函式上加一個指定 GPU 需求的裝飾器——剩下的一切由 Modal 處理：分配硬體、排程任務、依需求擴展規模、按實際運算秒數計費，任務完成後自動釋放資源。

無伺服器計算模型在 CPU 工作負載上已推行多年——AWS Lambda 和 Google Cloud Functions 在 2010 年代中期確立了這個模式。但 GPU 無伺服器計算面臨的問題在本質上更難：GPU 實例閒置成本高、排程效率複雜、「冷啟動延遲」（啟動全新 GPU 環境的時間）的問題遠比 CPU 函式嚴重。Modal 的核心技術成就在於以對開發者完全透明的方式解決了這些問題。

公司也在開發體驗上投入大量資源：快速冷啟動、對 PyTorch 和 JAX 等主流 ML 框架的原生支援、能完整模擬雲端環境的本地測試模式，以及與 Python 套件管理器和容器工作流程的無縫整合。開發者的普遍反饋是 Modal「就是能跑起來」——在其他工具需要大量基礎設施知識才能搞定的情況下。

## 支撐估值的成長數據

Modal 的財務軌跡，是投資人願意給出 46.5 億美元估值的基本邏輯。公司的年化營收在不到一年內成長五倍，從約 6000 萬美元躍升至 3 億美元。這個成長軌跡如果持續，Modal 的年化營收到 2027 年中將超過 10 億美元。

客戶群橫跨整個 AI 生態系統。Anthropic 使用 Modal 處理部分模型評估和研究工作流程；Meta 已將 Modal 整合進部分 AI 實驗基礎設施；自主程式碼代理公司 Cognition 在 Modal 上運行大量工作負載；DoorDash 用它驅動 AI 驅動的營運優化。客戶名單的廣度——從前沿 AI 實驗室到消費者 App 到企業軟體——反映了 GPU 算力需求在業界的水平屬性。

C 輪的投資方陣容包括共同領投的 Redpoint Ventures 和 General Catalyst，以及同時參與的 Accel 和 Menlo Ventures。多家頂尖機構分兩批在不同估值入場，而非單一主要投資方的模式，反映的是投資人之間的競爭動態，而非一般意義上買賣雙方的談判。

## 基礎設施投資的底層邏輯

Modal 的融資是 2026 年 AI 基礎設施投資大潮的縮影。同一週，Exa 為 AI 搜尋基礎設施募得 2.5 億美元，此前 Fractile 為 AI 推理晶片募得 2.2 億美元，Blackstone-Google TPU 合資企業則瞄準數十億美元的 AI 算力容量。從矽晶片到搜尋到無伺服器計算，投資人正在押注：AI 採用的瓶頸不是模型智慧，而是將那份智慧可靠地規模化部署所需的基礎設施。

Modal 在這個技術棧中所處位置的論點相當直接：隨著 AI 應用激增，建構 AI 的開發者群體從 AI 原生新創擴展到主流企業，能夠抽象化 GPU 基礎設施的工具將變成剛需。2026 年建構 AI 應用的公司，已不只是 Cursor 和 Cognition，還有物流公司、律師事務所、金融機構和醫療系統——這些組織的開發者對成為 GPU 叢集管理員毫無興趣。

在這個框架下，Modal 的可服務市場隨著 AI 採用的擴大而擴大。每一個建立在生成式 AI 模型上的新應用，都是潛在的 Modal 客戶。

## 競爭格局

Modal 所在的賽道競爭者包括雲端服務商——AWS SageMaker、Google Cloud Vertex AI、Azure Machine Learning——以及 Replicate、Baseten、RunPod 等專門競爭者。雲端服務商在規模和整合生態上具有明顯優勢，但普遍被認為更複雜、小規模使用成本更高、上手門檻更陡。

專門競爭者與 Modal 的定位更接近，但執行模式不同。Replicate 主要聚焦於模型推理部署，Baseten 專注於低延遲的生產推理，Modal 的定位更廣：不只處理推理，還涵蓋訓練、微調、批次任務、排程任務，以及任何能受益於 GPU 加速的任意 Python 計算——一個更通用的算力基底。

Modal 最重要的戰略優勢，或許是在 AI 開發者社群中積累的網絡效應。當開發者習慣用 Modal 的 API 思考無伺服器 GPU 計算，切換成本是真實存在的——不是因為鎖定，而是因為思維模式已經內化。

## 3.55 億美元能做什麼？

Modal 尚未公布資金用途的具體分配。根據公司既定優先事項與 GPU 算力市場動態，最可能的用途包括：擴大與主要硬體供應商的 GPU 容量協議以減少需求高峰時的供應瓶頸；深化工程投資以提升效能、可靠性和開發體驗；以及建立企業級功能——合規控制、安全機制、專屬算力預留——這些都是服務大型組織所必需的。

企業市場是 Modal 尚待開拓的重要機會。目前公司大部分營收來自 AI 原生公司和開發者團隊。擁有更完整採購流程、更嚴格安全要求、更長銷售週期的企業客戶，代表的是不同類型的客戶——但也意味著更大的合約金額和更穩定的可預測營收。

## AI 基礎設施投資的溫度計

Modal 的 3.55 億美元融資，緊接在 Exa 的 2.5 億美元融資之後，折射出基礎設施投資人的一個共同信念：AI 轉型仍處於早期階段，AI 經濟的「鏟子和斧頭」層至少會和應用層一樣可靠地積累價值。

建構 AI 應用的開發者需要算力。算力很貴。讓算力變得負擔得起、易於取用且可靠的工具，會被所有建構 AI 的人使用。Modal 已在快速成長的開發者社群中建立了這樣的地位，如今正募集資金，從最早發現它的社群擴張到將大規模部署 AI 的企業用戶。

46.5 億美元的估值，意味著投資人相信它能做到這一點。過去一年五倍的營收成長，表明他們的判斷可能是正確的。
