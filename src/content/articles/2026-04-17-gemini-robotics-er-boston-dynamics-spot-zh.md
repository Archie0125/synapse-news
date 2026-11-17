---
title: "Google DeepMind 發布 Gemini Robotics-ER 1.6，讓 Boston Dynamics Spot 擁有真正的空間推理能力"
summary: "Google DeepMind 推出 Gemini Robotics-ER 1.6，這款以推理為核心的模型強化機器人的空間推理與多視角理解能力，並新增複雜儀表的讀取功能。Boston Dynamics 正將其整合進 Spot 的 Orbit AIVI-Learning 巡檢軟體。"
category: "ai-ml"
publishedAt: 2026-04-17
modifiedAt: 2026-11-15T00:00:00Z
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

Google DeepMind 發布了 **Gemini Robotics-ER 1.6**，這道鴻溝縮小了。

DeepMind 將這款模型定位為 Gemini Robotics 系列的「推理優先」升級版，為實體系統帶來截然不同的智慧：能夠看著一個環境並真正理解它——不只是偵測物體，而是推理空間關係、評估任務完成狀況，並決定何時調用更專門的工具。同日，Boston Dynamics 宣布將 Gemini 與 Gemini Robotics-ER 1.6 整合進 Orbit AIVI-Learning，這是用於 Spot 工業巡檢工作流程的軟體平台的一部分。

模型即日起可讓開發者透過 Gemini API 與 Google AI Studio 使用。

## 「具身推理」究竟意味著什麼

DeepMind 將 Gemini Robotics-ER 描述為以「具身推理」為核心的推理優先模型，這項能力讓機器人得以連結數位智慧與實體行動。

標準視覺語言模型擅長描述所見；具身推理模型則設計為理解如何因應所見——聽起來細微，但在實體環境中至關重要。搭載純描述型模型的機器人可以告訴你牆上有一個壓力錶；具身推理模型則能讀取儀表，解讀指針、刻度線與數字。

Gemini Robotics-ER 1.6 特別改進了機器人的幾項能力：

**空間推理**：DeepMind 表示該模型強化了空間推理與多視角理解，包括指向與計數，有助機器人更精確地理解所處環境。

**任務完成判斷**：模型不依賴預設的成功標準，而是透過解讀視覺證據來評估任務是否完成——對自主品質巡檢工作流程至關重要，因為成功與否往往難以從單一畫面判斷。

**工具調用升級**：當模型遇到超出直接處理能力的情況，能識別並調用專門的視覺語言行動（VLA）模型來處理特定子任務，使 Gemini Robotics-ER 1.6 成為更廣泛機器人模型生態系的協調層。

## Boston Dynamics 押注 AI 驅動的巡檢

與 Boston Dynamics 的合作是 Gemini Robotics-ER 1.6 發布的重要部分，由 Gemini 驅動的 AIVI-Learning 系統已對現有客戶上線。

Boston Dynamics 將模型整合進其 Orbit 軟體平台，包括 **AI 視覺巡檢（AIVI）**（讓 Spot 能根據視覺資料回答有關設施的問題）和 **AIVI-Learning**（提供以工業資料集訓練出的洞察）。

搭載 Gemini Robotics-ER 1.6 後，Spot 獲得了代表質的飛躍的新能力。系統現在可以自主偵測地板和表面上的危險碎片或液體洩漏——在製造業、石油天然氣和公用事業環境中攸關安全。它能讀取複雜的壓力錶和液位鏡，解讀過去需要人工目視評估的類比儀表。它還能在遇到直接知識範圍之外的情況時——前所未見的製造異常、陌生的設備配置——調用專門的 VLA 模型。

工業巡檢一直是自主移動機器人最具說服力的早期應用場景，但限制因素始終是智慧而非移動能力。欠缺的是對所見事物做出細緻判斷的能力。Gemini Robotics-ER 1.6 直接填補了這個缺口。

## 實體 AI 賽局升溫

此次發布落在一個日益競爭激烈的實體 AI 版圖上。

DeepMind 不謀求擁有機器人，而是謀求擁有智慧層。

這與 Google 的整體戰略一脈相承。透過 API 開放 Gemini Robotics-ER，意味著任何建構機器人應用的開發者都能調用 DeepMind 的最新研究成果，無需從零開始構建具身推理能力。

Boston Dynamics 的合作尤其值得關注，因為 Boston Dynamics 在機器人市場佔據獨特地位：它生產的硬體是人們真正信任用於安全關鍵任務的。

## 開發者存取與後續展望

Gemini Robotics-ER 1.6 即日起可透過 Gemini API 與 Google AI Studio 提供給開發者使用。

對機器人開發者和整合商而言，Gemini Robotics-ER 1.6 拉高了現成 AI 的可達成下限。如果模型能推理應對新奇情境，機器人就不再需要為每種場景預先程式設計。這個轉變——從腳本自動化到自適應智慧——正是整個產業多年來一直朝向建構的方向。

它不再只是理論。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 25 處。*
