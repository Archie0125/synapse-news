---
title: "Anthropic 洽談採用微軟 Maia 200 自研晶片，Claude 推論成本有望降低 50%"
summary: "Anthropic 正與微軟磋商，計畫租用搭載 Maia 200 自研 AI 加速器的 Azure 伺服器執行 Claude 推論工作負載，每 Token 成本有望較同等 NVIDIA H200 實例降低 30～50%。若交易達成，Anthropic 將成為微軟自研晶片計畫的首位主要外部客戶，進一步深化雙方現有的 300 億美元雲端合作關係。"
category: "hardware"
publishedAt: 2026-05-25
lang: "zh"
featured: false
trending: false
sources:
  - name: "CNBC"
    url: "https://www.cnbc.com/2026/05/21/anthropic-microsoft-maia-200-ai-chip.html"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317072/20260524/anthropic-microsoft-negotiate-maia-200-chip-deal-claude-could-become-custom-silicons-first.htm"
  - name: "Windows News AI"
    url: "https://windowsnews.ai/article/microsoft-maia-200-deal-with-anthropic-what-it-means-for-azure-ai-costs.419293"
tags:
  - "anthropic"
  - "microsoft"
  - "maia-200"
  - "ai晶片"
  - "推論"
  - "azure"
  - "claude"
  - "自研矽晶片"
relatedSlugs:
  - "2026-05-25-anthropic-microsoft-maia-200-chip-deal-en"
  - "2026-05-18-tsmc-n2-2nm-chip-ramp-ai-hardware-zh"
  - "2026-05-23-anthropic-milan-emea-expansion-9x-revenue-zh"
---

據 CNBC 本週引述知情人士透露，Anthropic 正與微軟就租用搭載 Maia 200 晶片的 Azure 伺服器進行初步談判。若交易達成，這將是首家主要外部 AI 實驗室承諾在微軟自研矽晶片上執行生產推論工作負載的案例——這一里程碑可能重塑前沿 AI 公司看待算力供應鏈的方式。

此次談判的重心是推論工作負載，即持續不斷、成本高昂地從已訓練模型生成回應的過程。Anthropic 目前幾乎完全依賴 NVIDIA GPU 執行 Claude 推論，算力來源涵蓋多家雲端服務商，主要集中在其 300 億美元的 Azure 承諾框架內。Maia 200 協議一旦落地，將在微軟自研硬體上為 Anthropic 劃出專屬叢集。

## Maia 200 的競爭底氣

微軟於 2026 年 1 月發布 Maia 200，這是其第二代 AI 加速器，採用台積電 N3（3 奈米）製程打造。晶片搭載 216 GB HBM3e 記憶體，FP4 效能超過 10 PFLOPS——這些規格讓它在推論任務上足以與 NVIDIA H200 和 AMD MI325X 同台競技。

Maia 200 的核心論點在於性價比。微軟向潛在客戶表示，Maia 200 叢集的每美元 Token 產出量較 Azure 現有 GPU 機隊最新機型提升逾 30%。對每日處理數十億次 Claude 查詢的 Anthropic 而言，這意味著可觀的節省空間：內部估算顯示，每 Token 推論成本相比同等 NVIDIA H200 或 B200 實例可能降低 30～50%。

Maia 200 的架構專為推論效率而設計，其記憶體頻寬特性針對 Transformer 架構模型的大型 Key-Value 快取進行了優化——而 Claude 正是 Transformer 架構的代表性模型。微軟同時在自研網路架構和機架級散熱管理上投入重金，以最大化 Maia 200 叢集的利用率，這對全天候 24 小時運行的大規模推論工作負載尤為關鍵。

## 雙方各有盤算

對 Anthropic 而言，動機顯而易見：算力成本是其商業模型中的主導變量。公司在 SpaceX Colossus 超算基礎設施上為訓練工作付出每月估計 12.5 億美元的代價，Azure 承諾在推論端的支出規模同樣不容小覷。以 Anthropic 的業務規模，推論每 Token 成本降低 30～50% 意味著每年節省數億美元，這些資金可以重新配置到前沿模型研究。

另一個考量是供應鏈多元化。Anthropic 目前的推論堆疊高度依賴 NVIDIA GPU 供應，受制於同樣的供應約束和定價話語權——正是這種話語權讓 NVIDIA 的資料中心業務毛利率長期維持在 70% 以上。與微軟自研矽晶片建立合作關係，賦予了 Anthropic 另一條算力供應路徑，而微軟可以將這一路徑的定價完全納入更廣泛的合作框架，而非依照 GPU 市場即時行情計費。

對微軟而言，此次交易的戰略意義同樣不可低估。公司在 Maia 矽晶片計畫上已投入兩年以上時間和數十億美元，但截至 2026 年中，Maia 200 仍僅用於微軟第一方 AI 工作負載，包括 Copilot 推論、Azure OpenAI 服務和內部模型訓練。若 Anthropic 成為首位外部參考客戶，將驗證該晶片的商業可行性，並為微軟在自研晶片持續投入提供商業層面的正當性——在與 NVIDIA 的晶片市場競爭中，這依然是一場上坡之戰。

此次交易還將深化微軟與 Anthropic 於 2025 年 11 月確立的財務依存關係：當時微軟宣布向 Anthropic 投資 50 億美元，Anthropic 同步承諾在 Azure 上花費 300 億美元。Maia 200 協議意味著 Anthropic 不只是在 Azure 上消費，而是特定地消費微軟的自研硬體——這是一種更深層的捆綁，有助於微軟在與 Google Cloud 和 AWS 的戰略競爭中鞏固自身定位。

## 行業意涵：自研矽晶片競賽的轉折點

Anthropic 與微軟潛在交易的浮現，恰逢 AI 晶片產業的關鍵時刻。NVIDIA 對 AI 加速器的主導地位無以復加，以至於這家 GPU 製造商的市值在 2026 年初一度觸及 4 兆美元。然而超大規模雲端廠商長期以來持續押注自研矽晶片，恰恰是為了降低對 NVIDIA 的依賴，並攫取目前流入聖塔克拉拉的那部分利潤。

Google 的第七代 TPU 已為 Gemini 推論工作負載提供相當大比例的算力；Amazon 的 Trainium 2 和 Inferentia 3 晶片正被越來越多地用於 AWS 託管模型工作負載。微軟的 Maia 計畫作為最後入局者，一直是其中最不透明的存在——直到現在。

若 Anthropic 承諾在 Maia 200 上部署生產推論，則意味著微軟自研矽晶片已跨越一個關鍵門檻：從內部成本控制工具，進化為具備商業競爭力的產品。這對其他 AI 實驗室、企業客戶和雲端使用者評估自身晶片策略，具有重要的參考意義。

「超大規模廠商的自研矽晶片計畫，骨子裡始終是關於成本控制與供應鏈自主，」一位持續追蹤此次洽談的半導體分析師指出，「一旦外部前沿實驗室在 Maia 上跑起生產推論，微軟就有了一張遠比現在更大的商業版圖的概念驗證。」

## 仍存在的不確定性

談判目前仍處於早期階段，若干因素可能使交易複雜化或延遲。Anthropic 需要投入工程資源，將 Claude 推論堆疊移植並優化至 Maia 200 架構——即便有微軟的技術支援，這項工作也並非易事，可能耗時數月。此外，效能對等性仍是待解問題：儘管 Maia 200 的吞吐量指標具備競爭力，但針對 Anthropic 特定模型架構的實際效能需要進行大量基準測試，才能做出任何生產環境的承諾。

定價結構也是另一個開放變量。微軟可能以低於同等 NVIDIA 實例的折扣提供 Maia 200 叢集，以激勵 Anthropic 成為首位外部客戶，但這類條款通常附帶用量最低要求、容量保障，以及可能限制 Anthropic 同時在其他地方運行相同模型的排他性條款。

截至報導發布，微軟與 Anthropic 均未公開確認談判的存在，兩家公司對媒體詢問均拒絕置評。

若交易最終落地，其意義將遠超一筆採購決策。它將代表前沿 AI 產業對算力獨立性認知的根本轉變——以及對微軟多年押注的一次有力背書：自研矽晶片，而非 GPU 租賃，才是大規模 AI 基礎設施的未來。
