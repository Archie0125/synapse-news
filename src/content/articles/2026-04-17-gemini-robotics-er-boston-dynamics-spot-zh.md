---
title: "Google DeepMind 發布 Gemini Robotics-ER 1.6，讓 Boston Dynamics Spot 擁有真正的空間推理能力"
summary: "Google DeepMind 於 4 月 15 日推出 Gemini Robotics-ER 1.6，這款以推理為核心的模型大幅提升機器人理解空間關係、讀取複雜儀表及自主偵測危險的能力。Boston Dynamics 已立即將其整合進 Spot 的工業巡檢平台，是迄今最具體的實體 AI 量產部署案例之一。"
category: "ai-ml"
publishedAt: 2026-04-17
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google DeepMind Blog"
    url: "https://deepmind.google/blog/gemini-robotics-er-1-6/"
  - name: "SiliconAngle"
    url: "https://siliconangle.com/2026/04/15/deepmind-launches-gemini-robotics-er-1-6-meet-precise-physical-ai-demands/"
  - name: "The Robot Report"
    url: "https://www.therobotreport.com/boston-dynamics-and-google-deepmind-are-using-gemini-to-make-spot-smarter/"
  - name: "IEEE Spectrum"
    url: "https://spectrum.ieee.org/boston-dynamics-spot-google-deepmind"
tags:
  - "Google DeepMind"
  - "機器人"
  - "Boston Dynamics"
  - "實體 AI"
  - "Gemini"
  - "Spot"
relatedSlugs:
  - "2026-04-10-nvidia-cosmos-reason2-groot-physical-ai-zh"
  - "2026-04-17-nvidia-ising-quantum-ai-models-zh"
---

多年來，機器人硬體與機器人智慧之間的落差，一直是工業自動化的核心難題。硬體——相機、致動器、感測器——已進化到極為出色的程度；智慧層卻遲遲追不上，迫使機器人在嚴格預設的環境中運作，對現實世界的混亂情境幾乎毫無容錯空間。

2026 年 4 月 15 日，Google DeepMind 發布了 **Gemini Robotics-ER 1.6**，這道鴻溝縮小了。

DeepMind 將這款模型定位為 Gemini Robotics 系列的「推理優先」升級版，為實體系統帶來截然不同的智慧：能夠看著一個環境並真正理解它——不只是偵測物體，而是推理空間關係、評估任務完成狀況，並決定何時調用更專門的工具。同日，Boston Dynamics 宣布直接將 Gemini Robotics-ER 1.6 整合進驅動 Spot 機器人工業巡檢工作流程的 Orbit 軟體平台，是迄今為止大型機器人公司最具體的實體 AI 量產部署案例之一。

模型現已可讓開發者透過 Gemini API 與 Google AI Studio 立即存取，無需候補等待。

## 「具身推理」究竟意味著什麼

Gemini Robotics-ER 中的「ER」代表 Embodied Reasoning（具身推理）——這個刻意明確的命名，將此模型與傳統視覺語言模型區分開來。

標準視覺語言模型擅長描述所見；具身推理模型則設計為理解如何因應所見——聽起來細微，但在實體環境中至關重要。搭載純描述型模型的機器人可以告訴你牆上有一個壓力錶；具身推理模型則能讀取數值、判斷讀數是否在正常操作範圍內，並決定是否需要立即採取行動。

Gemini Robotics-ER 1.6 特別強化了工業機器人長期面臨的三個瓶頸能力：

**空間推理**：模型能解讀多攝影機視角並建構精確的三維環境心智模型，讓機器人無需預先建圖就能確定物體位置、理解深度與遮擋關係、在複雜場景中導航。

**任務完成判斷**：模型不依賴預設的成功標準，而是透過解讀視覺證據來評估任務是否完成——對自主品質巡檢工作流程至關重要，因為成功與否往往難以從單一畫面判斷。

**工具調用升級**：當模型遇到超出直接處理能力的情況，能識別並調用專門的視覺語言行動（VLA）模型來處理特定子任務，使 Gemini Robotics-ER 1.6 成為更廣泛機器人模型生態系的協調層。

## Boston Dynamics 押注 AI 驅動的巡檢

與 Boston Dynamics 的合作是 Gemini Robotics-ER 1.6 發布的核心，且是即時、以生產為導向的，而非實驗性的。

Boston Dynamics 將模型整合進 Orbit 軟體平台的兩個核心組件：**AI 視覺巡檢（AIVI）**（處理 Spot 巡邏路線中的即時異常偵測）和 **AIVI-Learning**（讓系統從運營數據中持續提升偵測能力）。

搭載 Gemini Robotics-ER 1.6 後，Spot 獲得了代表質的飛躍的新能力。系統現在可以自主偵測地板和表面上的危險碎片或液體洩漏——在製造業、石油天然氣和公用事業環境中攸關安全。它能讀取複雜的壓力錶和液位鏡，解讀過去需要人工目視評估的類比儀表。它還能在遇到直接知識範圍之外的情況時——前所未見的製造異常、陌生的設備配置——調用專門的 VLA 模型。

工業巡檢一直是自主移動機器人最具說服力的早期應用場景，但限制因素始終是智慧而非移動能力。Spot 已能在複雜環境中導航、應對樓梯、在對人類巡檢員構成風險的危險條件下作業。欠缺的是對所見事物做出細緻判斷的能力。Gemini Robotics-ER 1.6 直接填補了這個缺口。

## 實體 AI 賽局升溫

此次發布落在一個日益競爭激烈的實體 AI 版圖上。NVIDIA 透過 Cosmos 世界模型模擬平台與 Isaac GR00T 機器人學習框架大力投入；微軟透過 Azure 基礎設施展現機器人抱負；Amazon 在倉儲自動化領域大動作佈局；Figure、Physical Intelligence、1X、Neura Robotics 等人型機器人新創則正在打造結合客製硬體與專有 AI 的垂直整合系統。

Google DeepMind 的 Gemini Robotics-ER 走的是截然不同的路線：一個跨製造商、跨應用場景、在現有硬體——四足機器人、機械臂、移動底盤——上運行的水平模型。DeepMind 不謀求擁有機器人，而是謀求擁有智慧層。

這與 Google 的整體戰略一脈相承。Gemini 已覆蓋手機、筆電、雲端服務，現在又延伸至機器人。透過 API 開放 Gemini Robotics-ER，意味著任何建構機器人應用的開發者都能調用 DeepMind 的最新研究成果，無需從零開始構建具身推理能力。同時也意味著 Google 在規模上收集部署數據——改進後續模型世代的關鍵原料。

Boston Dynamics 的合作尤其值得關注，因為 Boston Dynamics 在機器人市場佔據獨特地位：它生產的硬體是人們真正信任用於安全關鍵任務的。其 Spot 機器人部署於核電廠、海上石油平台、建築工地和災難應對環境。讓 Gemini Robotics-ER 1.6 在這些部署場景中運行，給了 DeepMind 來自任何模擬都無法複製的條件的真實世界反饋。

## 開發者存取與後續展望

與許多在廣泛開放前先走限制存取計畫的前沿模型發布不同，Gemini Robotics-ER 1.6 對開發者立即開放。DeepMind 選擇開放發布，既反映了競爭壓力——NVIDIA 的 Cosmos 和 GR00T 正獲得牽引力，實體 AI 人才池的爭奪也日趨激烈——也展現了對「在此階段生態系廣度比管控存取更重要」的真誠信念。

DeepMind 表示後續版本將沿著更通用的具身智慧方向持續演進：能從單次示範學習、跨機器人形態泛化、在無需明確程式設計的情況下規劃多步驟操作序列的模型。預計 2026 年下半年，處理底層運動控制的 Gemini Robotics-Actions 系列也將迎來更新。

對機器人開發者和整合商而言，Gemini Robotics-ER 1.6 拉高了現成 AI 的可達成下限。如果模型能推理應對新奇情境，機器人就不再需要為每種場景預先程式設計。這個轉變——從腳本自動化到自適應智慧——正是整個產業多年來一直朝向建構的方向。

它不再只是理論。
