---
title: "ChipAgents 完成 6,000 萬美元 A2 輪融資，與 Nvidia 合作開發晶片設計專用 AI 模型"
summary: "自動化晶片設計驗證流程的新創公司ChipAgents宣布完成6,000萬美元Series A2融資，B Capital領投，Series A系列累計融資額達1.34億美元。同步宣布與Nvidia深化合作，共同開發專為半導體設計任務訓練的AI模型。公司報告今年上半年年化營收成長6倍，已在逾120家半導體企業部署。"
category: "hardware"
publishedAt: 2026-07-30
lang: "zh"
featured: false
trending: false
sources:
  - name: "Yahoo Finance – Nvidia Partner ChipAgents Raises $60 Million"
    url: "https://finance.yahoo.com/technology/ai/articles/nvidia-partner-chipagents-raises-60-114953354.html"
  - name: "The Next Web – ChipAgents Raises $60M for Agentic Chip Design"
    url: "https://thenextweb.com/news/nvidia-partner-chipagents-raises-60m-for-agentic-chip-design"
  - name: "Quartz – ChipAgents Expanded Its Partnership With Nvidia"
    url: "https://qz.com/chipagents-series-a2-funding-nvidia-partnership-072926"
tags:
  - "ChipAgents"
  - "Nvidia"
  - "半導體"
  - "晶片設計"
  - "AI代理"
  - "EDA"
  - "B Capital"
  - "融資"
relatedSlugs:
  - "2026-07-05-oxmiq-raja-koduri-35m-series-a-gpu-architecture-zh"
  - "2026-07-04-qualcomm-tenstorrent-acquisition-talks-zh"
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-zh"
---

設計一顆現代半導體，是工程界最勞力密集的挑戰之一。一顆先進晶片可能包含數十億個電晶體，排列精度達奈米等級，需要數百名工程師花費兩到四年完成，並在任何一片晶圓送去生產之前，通過數百萬組測試案例的驗證。光是「驗證」（verification）這個階段——確認晶片的行為符合設計規格——就可能吃掉整個專案70%以上的時間和預算。

ChipAgents認為，AI代理可以從根本上改變這條算式。

7月29日，這家總部位於聖塔克拉拉的新創公司宣布完成Series A2融資6,000萬美元，由B Capital領投，現有投資人Bessemer Venture Partners、美光（Micron）、聯發科（MediaTek）和愛立信（Ericsson）跟投，A系列累計融資金額達1.34億美元。同步宣布的，是與Nvidia深化技術合作，共同開發一個專為半導體設計任務訓練的AI模型。

## ChipAgents 做的是什麼？

電子設計自動化（EDA）是支撐晶片設計的軟體品類，Cadence和Synopsys等公司數十年來主導這個市場，提供工程師佈局電晶體、模擬電路行為、驗證設計正確性所需的工具。

ChipAgents的差異化在於一個不同的架構賭注：不是在現有EDA工具上附加AI功能，而是打造能自主操作這些工具的AI代理。代理可以讀取晶片設計規格書、自動生成測試案例、執行模擬、分析錯誤、反覆迭代——幾乎不需要工程師手動干預。

執行長William Wang用一句話描述核心價值：「我們做的核心工作，就是確保沒有bug。但今天這件事的完成方式，是讓人類寫數千個測試案例、跑模擬、看日誌。這完全可以改變。」

驗證階段之所以值得重點攻破，正是因為代價不對稱：在設計階段發現bug，改的是程式碼；在晶圓生產後才發現，整批晶圓報廢，損失可能高達數千萬美元。

## 融資節奏：不到一年燒進 1.34 億

ChipAgents 2024年從San Jose的Alpha Design AI分拆成立，融資速度相當罕見：2025年10月完成2,100萬美元Series A，2026年2月追加5,000萬美元，如今再獲6,000萬，A系列在不到一年內累計達1.34億美元。

公司目前有約64名員工，已在逾120家半導體企業部署。今年上半年年化營收成長6倍，雖然未揭露絕對金額，這樣的增速已足以讓ChipAgents躋身企業軟體領域成長最快的公司之列。

B Capital領投、美光與聯發科跟投的組合特別值得注意——客戶就是投資人，這是驗證產品真實需求最有力的信號。

## 與 Nvidia 的合作：為半導體設計打造專屬模型

本次公告中最具戰略意義的，不是融資金額，而是與Nvidia的深化合作。

兩家公司將共同開發一個專為半導體設計任務訓練的AI模型：理解硬體描述語言（HDL）程式碼、解析設計規格、預測驗證覆蓋率缺口、提出測試策略。

這類領域專屬模型，與一般程式碼模型被應用於硬體設計的效果截然不同。撰寫RTL（暫存器傳輸層）程式碼要求對時序約束、功耗預算和製程規則有深入理解，而這些知識在以軟體程式碼為主訓練的模型中幾乎不存在。真正在硬體設計文件——規格書、RTL程式碼、測試框架、模擬日誌、矽晶圓失效分析——上訓練的模型，才能提供質的躍升。

Wang拒絕透露Nvidia是否同時作為股東參與了本輪融資。但Nvidia的戰略動機顯而易見：加速晶片設計軟體工具，直接縮短下一代硬體的上市時程，降低Nvidia自身晶片從設計到客戶能採用的整個週期長度。

## 競爭格局：老牌廠商也在動

EDA市場規模龐大、壁壘深厚，且正在整合中。Cadence和Synopsys過去兩年均已在主力設計環境中整合AI功能，也都推出了代理式產品，直接與ChipAgents競爭。老牌廠商有一樣ChipAgents沒有的東西：幾十年在晶片設計團隊中建立起來的信任關係，以及與現有工作流程深度整合的生態。

ChipAgents的優勢，在於架構純粹性——代理從一開始就是為自主操作而設計，而不是在人類操作界面上貼AI補丁——以及一個迫切需要降低晶片開發成本與時間的市場環境。

AI基礎建設浪潮對新晶片架構的需求從未如此旺盛：更高效的注意力機制處理器、客製化推論晶片、為Transformer工作負載優化的記憶體控制器、能以足夠速度為GPU叢集供料的互連。每晚六個月上市，就是失去六個月的競爭優勢。

## 最大的挑戰：信任

晶片製造是不可逆的。台積電或三星一旦開始生產晶圓，設計中的任何缺陷都會永久固化在矽晶片裡，沒有任何軟體補丁能修復一個位置錯誤的電晶體。今天負責簽署驗證結果的工程師，是在充分意識到這個後果的重壓下做出判斷的。

要讓驗證團隊把有意義的工作委託給自主代理，需要的不只是展示代理有多快，而是要證明它的正確性是可靠的、可稽核的、可被理解的。一個通過99%測試案例但漏掉特定角落情況的時序違規的AI代理，比沒有更糟——它給了一個在後果最嚴峻的流程中最不應該出現的東西：虛假的信心。

Nvidia的合作或許能在這裡提供幫助。一個在Nvidia內部設計文件上訓練、並以Nvidia自身的矽晶圓量產結果驗證的模型，擁有任何通用模型都無法比擬的可信度。如果ChipAgents能指出某顆Nvidia晶片在代理輔助驗證後順利量產，那將是整個業界都會認真考量的參考案例。

自動化晶片設計的競賽才剛開始。ChipAgents切入的是整個工作流中衝擊最大的環節，融資了足以競爭的資本，並鎖定了能為模型開發提供背書的最具說服力的夥伴。接下來兩年，將會揭示業界是否準備好讓AI代理，在晶圓入爐之前，替他們把關最後一道防線。
