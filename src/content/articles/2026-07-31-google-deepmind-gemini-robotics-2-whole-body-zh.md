---
title: "Google DeepMind 發布 Gemini Robotics 2：首款讓人形機器人擁有全身智慧的 AI 模型"
summary: "Google DeepMind 推出 Gemini Robotics 2 模型系列，讓人形機器人能夠協調從腳到指尖的全身動作。系統已在 Apptronik 的 Apollo 2 人形機器人上進行展示，其中 Gemini Robotics ER 2 可透過 Google AI Studio 存取，並在 Gemini Enterprise Agent Platform 上提供私人預覽。"
category: "ai-ml"
publishedAt: 2026-07-31
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Google DeepMind Blog – Gemini Robotics 2 brings whole body intelligence to robots"
    url: "https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/"
  - name: "Robotics & Automation News – Google DeepMind unveils Gemini Robotics 2"
    url: "https://roboticsandautomationnews.com/2026/07/31/google-deepmind-unveils-gemini-robotics-2-as-apptronik-humanoid-demonstrates-whole-body-ai/103802/"
  - name: "SiliconANGLE – Google DeepMind debuts Gemini Robotics 2 model series for humanoid robots"
    url: "https://siliconangle.com/2026/07/30/google-deepmind-debuts-gemini-robotics-2-model-series-humanoid-robots/"
  - name: "Bloomberg – Gemini Robotics 2 Expands Google's AI Capabilities for Humanoid Robots"
    url: "https://www.bloomberg.com/news/articles/2026-07-30/google-unveils-gemini-ai-for-robots-struggling-with-dexterity"
tags:
  - "Google DeepMind"
  - "Gemini Robotics"
  - "人形機器人"
  - "機器人"
  - "具身 AI"
  - "Apptronik"
  - "全身智慧"
relatedSlugs:
  - "2026-07-14-unitree-robotics-619m-shanghai-star-ipo-zh"
  - "2026-07-24-japan-noetra-2b-physical-ai-robotics-zh"
  - "2026-07-19-agility-robotics-spac-ipo-humanoid-nasdaq-zh"
---

Google DeepMind 發布 Gemini Robotics 2，這個模型系列讓人形機器人擁有「全身智慧」——不只能協調手臂和雙手的動作，而是涵蓋從腳到指尖的整個身體。

這是相對於原版 Gemini Robotics（2025 年初發布）的重大躍進。舊系統僅能控制機器人的上半身；新版本則能讓機器人在扭轉、俯身、蹲下、伸手等複合動作中保持協調，同時在腦中即時推理任務的下一步——這種流暢、整合的肢體推理能力，是人類視為理所當然、但 AI 控制的硬體長期以來難以企及的目標。

## 「全身智慧」究竟代表什麼？

機器人學領域長久以來把全身控制視為最棘手的挑戰之一：一具人形機器人有超過 30 個自由度——髖關節、膝關節、腳踝、脊椎、肩膀、手肘、腕部——必須同時協調指令，才能執行自然、適應性的動作。讓 AI 模型在即時回應外部變化的同時，同步推理所有這些關節，幾十年來一直是機器人領域的未解難題。

過去的主流做法，包括第一代 Gemini Robotics，是把這個問題分解：高層推理系統負責規劃任務，低層控制器則以預先設計好的動作腳本或模型預測控制來執行。這種架構的致命弱點在於：一旦現實情況偏離腳本假設，機器人就會以相當不優雅的方式失敗。

實際效果是：當物體從手中滑落、或地面傾斜時，機器人不再陷入動作程式失效的困境，而是動態調整整個身體的姿態來因應——這才是真正意義上的適應性。

## 三款模型、三種應用場景

Gemini Robotics 2 不是單一模型，而是一個包含三個成員的系列：

**Gemini Robotics 2** 是一款視覺-語言-動作（VLA）模型，能將視覺與語言輸入轉換為馬達控制，可控制從腳到指尖的完整人形機器人，以及其他雙臂機器人。

**Gemini Robotics On-Device 2** 是針對端側部署優化的輕量版本，可直接在機器人本地硬體上運行，無需連接雲端。犧牲了部分性能，換取大幅更低的延遲——對於需要即時反應的任務，哪怕 50 毫秒的雲端往返時間都可能造成明顯的反應滯後。

**Gemini Robotics ER 2** 是一款具身推理模型，可透過 Google AI Studio 存取，並在 Google 的 Gemini Enterprise Agent Platform 上提供私人預覽。它能規劃長達數分鐘的多步驟任務、與人類溝通，並讓機器人像團隊一樣協同合作。

## 測試表現：92% 成功率

DeepMind 隨發布同步公開了基準測試結果。在旋下燈泡這項需要精確協調手臂動作、握力、軀幹穩定和視覺回饋的任務中，Gemini Robotics 2 達到了 92% 的成功率，而同任務下領先的舊一代系統約為 60%。

多機器人協作是另一項新能力：DeepMind 表示，Gemini Robotics ER 2 可讓不同類型的機器人在複雜工作流程上相互溝通與協調。

## Apptronik Apollo 2：主要展示平台

DeepMind 選擇了 Apptronik 的 Apollo 2 人形機器人作為 Gemini Robotics 2 的主要展示平台。Apptronik 是一家總部位於德克薩斯州、獲 Google 投資的人形機器人公司，是極少數提前獲得新模型進行整合測試的硬體夥伴之一。

在現場展示中，搭載 Gemini Robotics 2 的 Apollo 2 展現了多項標誌性進展：從地面拾取物品同時保持身體平衡、在雜亂環境中持物行走，以及需要以軀幹作為穩定基準點的雙手操作任務。機器人的動作流暢度明顯優於上一代展示——這正是統一全身模型比分解式架構協調得更自然的直觀體現。

## 存取方式與開放時程

Gemini Robotics 2 和 On-Device 2 目前提供給部分選定的早期體驗夥伴。Gemini Robotics ER 2 可透過 Google AI Studio 的 API 端點存取，並在 Google 企業 AI 平台上提供私人預覽。

完整正式上市的時程尚未公布，但 DeepMind 表示計劃在 2026 年下半年持續擴大開放範圍，On-Device 2 的硬體整合開發套件預計在年底前提供給合格夥伴。

## 具身 AI 競賽白熱化

Gemini Robotics 2 的發布，正值「具身 AI」——讓 AI 系統透過機器人、自駕車等實體硬體在物理世界中運作——成為 2026 年科技業最競爭激烈、資本最密集的前沿戰場之一。

宇樹科技（Unitree Robotics）7 月在上海科創板上市，估值 6.19 億美元；Agility Robotics 透過 SPAC 合併登上那斯達克。Figure AI、Hyundai 旗下的波士頓動力，以及越來越多的中國人形機器人新創公司，都在爭奪誰能率先建立製造規模——高盛預測這個市場到 2035 年將突破每年 1,000 億美元。

Google 的策略押注是：模型層——而非硬體層——才是最終最具護城河價值的所在。如果 Gemini Robotics 2 能成為第三方人形機器人硬體的預設「大腦」，就像 Android 成為第三方智慧型手機預設作業系統一樣，其經濟意義將相當深遠。這正是 DeepMind 以 API 端點形式發布 Gemini Robotics ER 2 的背後邏輯：讓每一家硬體廠商都能使用這個能力，而非將其鎖定在自家機器人上。

這場賭局能否勝出，將取決於 DeepMind 能否在 NVIDIA 具身 AI 技術棧、波士頓動力 Atlas 日益強大的全身控制系統，以及中國機器人 AI 團隊日益精進的競爭中持續保持領先。

但就目前而言，Gemini Robotics 2 已為 AI 驅動的全身協調能力樹立了新的公開標竿——也為跟隨其後的所有競爭者提高了比賽的入場門檻。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 7 處。*
