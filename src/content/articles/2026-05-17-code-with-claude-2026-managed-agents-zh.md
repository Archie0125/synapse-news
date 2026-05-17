---
title: "Code with Claude 2026：Anthropic發布能自我改進的智慧代理——夢境記憶、成果自評與平行編排"
summary: "在5月6日舊金山舉行的第二屆年度開發者大會上，Anthropic為Claude Managed Agents發布了三項重大新功能：Dreaming（讓代理在會話間自我改進的記憶整合）、Outcomes（使用獨立評估代理的自評循環），以及Multiagent Orchestration（將任務分配給平行運作的專業子代理的協調器）。法律AI公司Harvey表示，使用新功能後任務完成率提升了六倍。"
category: "developer-tools"
publishedAt: 2026-05-17
lang: "zh"
featured: false
trending: false
sources:
  - name: "Claude官方部落格 — Claude Managed Agents新功能"
    url: "https://claude.com/blog/new-in-claude-managed-agents"
  - name: "SD Times — Claude Managed Agents：夢境、成果與多代理編排"
    url: "https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/"
  - name: "Simon Willison — Code w/ Claude 2026即時直播紀錄"
    url: "https://simonwillison.net/2026/May/6/code-w-claude-2026/"
  - name: "MindStudio — Code with Claude 2026：5項新代理功能"
    url: "https://www.mindstudio.ai/blog/code-with-claude-2026-new-agent-features"
tags:
  - "Anthropic"
  - "Claude"
  - "AI代理"
  - "開發者工具"
  - "多代理"
  - "Code with Claude"
  - "主動式AI"
relatedSlugs:
  - "2026-05-15-anthropic-agent-sdk-billing-split-zh"
  - "2026-05-13-red-hat-summit-agentic-ai-developer-tools-zh"
---

Code with Claude 2026沒有發布新旗艦模型。這是刻意的選擇。當Anthropic於5月6日在舊金山莫斯孔尼中心舉辦第二屆年度開發者大會——這是三城巡迴的第一站，接下來是5月19日的倫敦和6月10日的東京——公司做出了一個經過深思熟慮的決定：把舞台時間留給基礎設施，而非跑分。Anthropic今年大會所押注的，是「能力展示的時代已過，代理可靠性的時代已到」。

當天發布的三項功能——Dreaming、Outcomes和Multiagent Orchestration——是迄今為止對Anthropic認為2026年下半年競爭前沿所在最清晰的表達。

## Dreaming：越用越聰明的記憶

三項功能中概念上最具創新性的是「Dreaming」，目前處於研究預覽階段。核心洞察簡單，但影響深遠：AI代理在目前的部署方式下，不會在會話間改進。每次對話都從零開始，第100次會話中習得的模式，若不通過提示工程或檢索增強明確取用，在第101次會話中便不復存在。Dreaming是Anthropic對這個限制的解答。

其機制以非破壞性為設計原則。一次「夢境」是一個排程進程，它讀取現有記憶庫和一批過往會話記錄，生成一個新的、經過重組的記憶庫。重複條目被合併，過時條目被替換，新發現的模式被索引。原始記憶庫在此過程中從不被修改——輸出是一個獨立的產物，開發者可以審閱、接受或捨棄，然後再決定是否應用。這在保持開發者控制權的同時，實現了一種長期以來在代理研究社群中備受追求的自主自我改進。

Anthropic的內部基準測試顯示，運行Dreaming週期後，PowerPoint生成品質提升了10.1%——這個數字看似不大，卻可能低估了該功能對長期運行工作流程的價值。在這類工作流程中，數百次會話後記憶漂移是真實存在的運營問題。

## Outcomes：能給自己打分的代理

「Outcomes」現已進入公開測試階段，針對的是另一種失敗模式：代理完成了任務，卻完成得不正確，而且缺乏自我意識來辨識輸出與意圖之間的落差。

這項功能使用獨立的評估代理實現了一個自評循環。主代理完成任務後，評估代理根據開發者撰寫的評分標準對輸出進行評分，並返回結構化批評：哪裡做對了、哪裡有問題、應該修正什麼。主代理據此修改輸出。這個循環可以多次執行，直到評估者的評分達到設定閾值，或到達配置的迭代上限以防止運算失控。

按Anthropic的內部測量，Outcomes在結構化輸出生成任務上帶來了10.1%的品質提升。更有意義的是，早期測試客戶反映，Outcomes顯著降低了「靜默失敗」的比率——即代理看似已完成任務，但輸出在下游品質檢查中失敗的情況。AI法律研究公司Harvey引用了任務完成率提升六倍的數據，作為該功能影響力最具說服力的外部佐證。

## Multiagent Orchestration：平行智能

第三項功能解決了阻礙複雜代理工作流企業級部署的序列處理瓶頸。「Multiagent Orchestration」同樣處於公開測試階段，提供了一個原生協調代理，能夠將複雜任務分解為子任務，並將其分配給平行運作的專業子代理。

協調器負責任務分解、向子代理分發上下文、彙整結果，以及當子代理輸出需要協調時的衝突解決。從開發者視角看，關鍵優勢在於平行編排能夠大幅縮短複雜任務的實際完成時間——一個原本需要40分鐘序列執行的研究與綜合工作流，在平行子代理下可能在8至12分鐘內完成，具體取決於任務結構。

該功能附帶常見工作流程模式的預建協調器模板，而隨多代理編排功能一同發布的Claude Finance，包含10個針對財務建模、財報分析、監管文件解析和投資組合報告的預建代理。

## 基礎設施：看似無聊卻至關重要的故事

在產品功能的背後，Anthropic宣布了對生產環境部署中頻繁碰觸速率限制的開發者而言意義重大的運營調整：訂閱方案的速率限制翻倍、Pro和Max使用者的尖峰時段上限取消、特定等級的API速率限制提升最高達17倍——這個數字反映了Anthropic一直在悄悄擴充的運算容量。

最重要的基礎設施披露，是與SpaceX合作使用位於孟菲斯的Colossus資料中心專用容量——這座由馬斯克旗下xAI建造的設施，是美國境內AI訓練與推理算力最高度集中的地點之一。這筆協議讓Anthropic獲得了此前只有最大型超大規模雲端業者才能取得的算力規模。

## 平台下注

綜觀Code with Claude 2026的系列發布，戰略意圖已清晰可辨：Anthropic正在將Claude Managed Agents定位為一個專為生產級代理工作流設計的平台，而非一個附加了代理功能的模型API。上週宣布的計費分拆——將Agent SDK使用從6月15日起移至獨立的點數池——是同一框架的組成部分：代理基礎設施理應有其獨立的經濟模型，區別於互動式對話的使用。

大會擴展至倫敦和東京同樣值得玩味。倫敦代表企業法律、金融和專業服務——Harvey六倍提升的故事在這些領域最有共鳴。東京代表日本企業市場，這個市場將AI整合進核心業務工作流程的速度快過任何可比較的經濟體，且有其獨特的監管要求與語言需求，Anthropic一直在投入資源服務這個市場。

這家花了三年時間告訴業界「安全與能力並不衝突」的公司，現在正在提出第二個論點：建立在可靠、自我改進基礎設施之上的代理，其表現將超越建立在原始跑分性能之上的代理。對於那些在2025年飽受不可靠代理運營成本之苦的開發者，Code with Claude 2026的功能陣容，是迄今為止任何主要AI實驗室對這些痛點最直接的正面回應。
