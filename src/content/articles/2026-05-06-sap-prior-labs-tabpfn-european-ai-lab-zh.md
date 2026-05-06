---
title: "SAP 收購 Prior Labs，打造歐洲首屈一指的結構化資料前沿 AI 研究院"
summary: "SAP 宣布與德國 AI 新創公司 Prior Labs 簽署收購協議，承諾投入逾 10 億歐元，將其打造為專注於表格與結構化商業資料的全球頂尖前沿 AI 研究院。Prior Labs 由機器學習研究員 Frank Hutter 等人創立，開創了表格基礎模型（TFM）這一 AI 架構新類別，旗下 TabPFN 系列已發表於《自然》期刊，可直接從結構化資料預測業務結果，無需傳統機器學習工程流程。"
category: "startups"
publishedAt: 2026-05-06
lang: "zh"
featured: false
trending: true
sources:
  - name: "SAP Newsroom"
    url: "https://news.sap.com/2026/05/sap-to-acquire-prior-labs-establish-frontier-ai-lab-europe/"
  - name: "CIO Dive"
    url: "https://www.ciodive.com/news/sap-buys-dremio-prior-labs/819263/"
  - name: "TechTarget"
    url: "https://www.techtarget.com/searchdatamanagement/news/366642794/SAP-acquisitions-of-Dremio-Prior-Labs-target-AI-development"
tags:
  - "SAP"
  - "Prior Labs"
  - "TabPFN"
  - "企業 AI"
  - "歐洲 AI"
  - "結構化資料"
  - "收購"
relatedSlugs:
  - "2026-04-25-cohere-aleph-alpha-merger-sovereign-ai-zh"
  - "2026-04-22-salesforce-headless-360-tdx-2026-zh"
---

SAP 歷來的收購邏輯主要圍繞市場版圖擴張——買下 Concur 是為了差旅費用管理，買下 Qualtrics 是為了客戶體驗，買下 Ariba 是為了採購。此次同步宣布收購 Prior Labs 和開源資料平台 Dremio，傳遞的卻是截然不同的企圖心：SAP 想要建立自己的前沿 AI 研究能力，而且要在歐洲做到這件事。

交易金額未予披露，但 SAP 附帶了一項在軟體業收購中頗為罕見的承諾：未來四年投入逾 10 億歐元，將 Prior Labs 擴建為「結構化商業資料領域的全球頂尖前沿 AI 研究院」。

## Prior Labs 究竟在做什麼

Prior Labs 是那種學術聲望遠超市場知名度的公司。由 Frank Hutter、Noah Hollmann 和 Sauraj Gambhir 共同創立，這家新創公司開創了一個稱為「表格基礎模型（Tabular Foundation Models，TFM）」的 AI 架構新類別——這類模型的設計目標不是文字或圖像，而是驅動幾乎所有企業系統運作的那種行列格式結構化資料。

公司旗艦產品 TabPFN 採用了截然不同於主流企業資料科學方法的路徑。過去十年主導這一領域的梯度提升演算法（XGBoost、LightGBM）需要繁瑣的特徵工程、超參數調整和大量資料前處理；TabPFN 則使用基於數千萬筆合成表格資料集預訓練的 Transformer 架構，即使面對傳統方法容易失效的超小型資料集，也能近乎即時地輸出精確預測。

這樣的成果足以登上《自然》期刊。最新版本 TabPFN-2.6 目前在 TabArena 表格基礎模型榜單上排名第一，開源版本累計下載量已突破 300 萬次。這種在學術 AI 研究中罕見的開發者採用規模，說明 TabPFN 在實際生產環境中具備真實的使用價值，而非單純追求榜單排名。

## 為什麼企業需要表格 AI

這筆收購的時機，在理解當前企業 AI 浪潮的缺口後便顯得合理。2025 至 2026 年間的主流焦點高度集中於大型語言模型和多模態系統，這類技術在非結構化資料（文字、圖像、程式碼）上表現卓越；但實際驅動大多數企業決策的資料，仍是那些根深蒂固的結構化資料：財務交易、供應鏈紀錄、客戶資料庫、ERP 表格。

傳統的表格機器學習方案要求資料科學家為每個應用場景建立客製化流程。TFM 從根本上改變了這種經濟性。TabPFN 這樣的模型可以用同一套底層架構預測應付帳款逾期風險、供應商違約可能性、客戶流失機率和追加銷售機會，各應用場景所需的定製工作量極低。

對 SAP 而言——其客戶群在 SAP 系統上管理著全球規模的企業結構化資料——這絕非理論上的好處。SAP 本身就處理著任何組織都難以匹敵的結構化商業資料規模。Prior Labs 的技術，理論上可以讓 SAP 以遠低於現有方式的開發成本，將預測和智慧功能直接內嵌到 ERP、供應鏈和財務應用中。

## Dremio：SAP 雙管齊下的另一半

同步宣布的 Dremio 收購，為 SAP 的 AI 策略補上了關鍵的資料存取層。Dremio 是一款開源資料湖屋查詢引擎，讓分析師和 AI 應用能夠跨資料湖、資料倉儲及各類異構資料源執行 SQL 查詢，無需實際搬移或複製資料。

這兩筆收購合力解決了企業 AI 部署的一個常見失敗模式：模型訓練所用資料未能充分反映組織的完整資訊全貌。Dremio 幫助 SAP 客戶讓更多資料可供 AI 使用，Prior Labs 的技術則幫助 SAP 建立能在這些資料上有效運作的模型。

SAP 執行長 Christian Klein 在週一的媒體發布會上，將這兩筆收購定位為公司 AI 轉型敘事的基石。「隨著企業資料工作負載演變為 AI 的使能因素，我們需要完整的技術堆疊，」Klein 表示，「有資料存取卻沒有智慧是不完整的。有智慧卻沒有資料存取同樣不完整。」

## 歐洲 AI 研究院策略

Prior Labs 的戰略意義超越 SAP 的產品藍圖。透過承諾讓 Prior Labs 在創始團隊的領導下作為獨立實體繼續運作，並將大規模 AI 研究投資錨定在德國，SAP 正在為「歐洲 AI 主權」發展做出隱性表態。

歐洲 AI 生態在資金、算力和人才方面長期難以與美國、中國的前沿實驗室競爭。今年稍早 Cohere 與 Aleph Alpha 的合併，部分動機也是希望建立一個規模夠大、足以抗衡 OpenAI 和 Anthropic 的歐洲替代方案。SAP 的路線不同：不是建立通用大型語言模型的競爭者，而是投資解決特定領域問題的 AI 研究——而歐洲企業基礎設施公司在這個領域具備真實的競爭優勢。

Frank Hutter 為這種定位帶來了特別的可信度。他是弗萊堡大學教授，也是自動化機器學習（AutoML）領域的先驅，在神經架構搜尋、元學習和超參數優化方面發表過奠基性成果。他的學術背景，加上 Prior Labs 的《自然》論文和 TabPFN 的開源社群吸引力，說明 SAP 收購的是真正的研究能力，而非單純的產品資產。

## 後續展望

這筆收購預計在 2026 年第二至三季度完成，尚待監管審批。Prior Labs 將以獨立實體持續運作，保留研究文化和開源承諾。SAP 表示，10 億歐元以上的投資將用於擴充研究人員、算力資源和資料集規模。

對企業軟體業而言，這筆交易可能預示著一個更廣泛的趨勢。如果結構化表格資料確實代表 AI 能力的一條重要前沿——TabPFN 的基準表現和採用規模已提供了初步佐證——那麼受益最大的公司，正是那些本就站在企業結構化資料流核心的玩家：SAP、Oracle、Salesforce，以及微軟的 Dynamics 部門。

讓一排一欄的數字變成可行動的商業智慧，這場競賽才剛剛開始。
