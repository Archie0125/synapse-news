---
title: "MiniMax M3：中國開源 AI 以 100 萬 Token 上下文挑戰頂級閉源模型"
summary: "中國 AI 公司 MiniMax 發布 M3 開源模型，具備 100 萬 Token 上下文窗口與原生多模態輸入。根據 MiniMax 自家數據，M3 在 SWE-Bench Pro 上小幅領先 GPT-5.5，並在 BrowseComp 網路搜尋基準上勝過 Claude Opus 4.7。"
category: "ai-ml"
publishedAt: 2026-06-20
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "The Decoder"
    url: "https://the-decoder.com/minimax-m3-open-weight-model-with-a-million-token-context-challenges-proprietary-leaders/"
  - name: "Codersera"
    url: "https://codersera.com/blog/minimax-m3-developer-guide/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317532/20260601/minimax-m3-open-weight-coding-model-frontier-claims-unverified-benchmarks.htm"
  - name: "DataNorth"
    url: "https://datanorth.ai/news/minimax-launches-m3"
tags:
  - "MiniMax"
  - "M3"
  - "開源模型"
  - "大型語言模型"
  - "多模態"
  - "中國AI"
  - "前沿AI"
  - "上下文窗口"
relatedSlugs:
  - "2026-04-04-open-source-llm-race-zh"
  - "2026-06-17-deepseek-74b-first-funding-tencent-catl-50b-zh"
---

總部位於上海的 AI 公司 MiniMax 於 2026 年 6 月 1 日發布 M3。

M3 是第一個同時具備頂級編程性能、真實的 100 萬 Token 上下文窗口，以及原生多模態輸入的開源（開放權重）模型。

## M3 的三大核心能力

M3 的價值主張建立在三項能力上，每項能力單獨看其他模型已有提供，但在單一開源模型中的組合正是此次發布的意義所在。

**100 萬 Token 的上下文窗口。** M3 的上下文窗口是其前代 M2.7 的五倍。

**原生多模態能力。** M3 接受文字、圖片和影片作為輸入（輸出為文字）。MiniMax 將此定位為可與 Anthropic 電腦操作 API（computer-use API）媲美的電腦使用能力；模型能操作桌面電腦。

**前沿級別的編程能力。** 在 SWE-Bench Pro 基準上，M3 得分 59.0%，高於 GPT-5.5 的 58.6%，低於 Claude Opus 4.7 的 64.3%。在網路研究評估基準 BrowseComp 上，M3 得分 83.5，Opus 4.7 為 79.3。

需要注意的是：MiniMax 的部分基準測試是在自家基礎設施上以自家的代理框架執行，獨立第三方驗證尚未完成。M3 與 Opus 4.7 在 SWE-Bench Pro 上 5.3 個百分點的差距是真實存在的，不容忽視。M3 具備前沿競爭力，但並未全面超越。

## 架構創新：MiniMax 稀疏注意力

M3 能夠支援 100 萬 Token 上下文的關鍵，是一個名為「MiniMax 稀疏注意力」（MiniMax Sparse Attention，MSA）的新架構元件。以標準全注意力 Transformer 處理 100 萬 Token 的成本很高：注意力機制會將每個 Token 與其他所有 Token 比較，因此運算成本隨輸入長度呈二次方成長。

MSA 透過區塊化的鍵值快取（KV cache）解決這個問題。它不對序列中的每個 Token 計算全注意力，而是將儲存的上下文分割成區塊，預先過濾哪些區塊與當前查詢相關，並批次處理需要同一區塊的查詢，消除同一工作階段中的冗餘記憶體讀取。根據 MiniMax 自己的測量，與 M2 相比，MSA 在 100 萬 Token 上下文下實現了 15.6 倍更快的解碼速度和 9.7 倍更快的預填充，每個 Token 在 100 萬 Token 上下文下的計算量降低至上一代的約 1/20。

這對實際部署至關重要。一個理論上能處理 100 萬 Token 但每次推論需要 100 美元成本的模型，在實踐中並不可部署。MiniMax 表示，MSA 讓百萬 Token 上下文在成本上可負擔，運算成本不致失控。

## 自主能力示範

MiniMax 公布了三項內部延伸自主運作示範，展示了 M3 的代理潛力：

**12 小時論文復現。** M3 接到任務，獨立復現一篇 ICLR 2025 微調論文。無需人工干預，模型工作近 12 小時，產生 18 次提交和 23 個圖表，並確認了論文的關鍵發現。這項跨越多小時、多次提交的任務，遠超單次生成所能完成的範圍。

**24 小時 GPU 核心優化。** 在針對 NVIDIA Hopper 架構優化 CUDA 核心的任務中，M3 透過 147 次嘗試將硬體使用率從 7.6% 提升至 71.3%，效率提升近 10 倍。MiniMax 表示，大多數競爭模型在數十次嘗試後就放棄了，而 M3 在全天的迭代過程中保持了連貫的上下文，充分展示了長上下文架構在延伸自主任務中的實際優勢。

**PostTrainBench 自主訓練。** M3 自主完成了四個基礎模型的訓練，包括資料合成和迭代優化，全程無需人工干預。若此能力能夠泛化，對 AI 自我改進管道將有深遠影響。

這些示範來自 MiniMax 內部，而非獨立研究人員，應保持適度批判性。但它們足夠具體，可以被驗證，其公開也顯示 MiniMax 有一定信心接受外界核查。

## 開放權重的戰略意義

M3 透過 MiniMax API 提供分級定價（每月 20 至 120 美元），標準每 Token 費率適用於 512,000 Token 以內，更長的上下文另計費用。模型權重和技術報告預計在公告後十天內發布至 Hugging Face。

開放權重的發布具有超越技術規格的戰略意義。開放權重模型可以自行部署、微調，並運行在組織自己的防火牆後方。

這也深刻影響著 AI 市場的地緣政治格局。DeepSeek 的早期版本暗示了中國開源模型接近前沿的可能性；M3 則提出了一個更有力的論據，表明這個差距已進一步縮小。

出口管制的動態影響是雙向的：性能接近前沿的中國開放權重模型，任何人只要有足夠的算力就能使用，不受這些規則約束。對國際開發者和企業而言，M3 及其後繼者代表著一條可信的替代供應鏈。

## 競爭格局與後續展望

MiniMax 在此空間中並非孤軍奮戰。中國開源 AI 領域已在數週內集中在相同的能力目標上——長上下文、強編程能力、多模態輸入——顯示出對技術路線圖的高度一致認知。

對正在評估 M3 的開發者而言，實際問題集中在推論成本、微調穩定性，以及 MiniMax 內部基準測試方法與獨立復現之間的差距。這些問題將在未來數週內，隨著研究和開發社群實際使用開放的模型權重而得到解答。

更大格局的問題是：2026 年 6 月是否標誌著前沿級別的 AI 真正成為可用的開放基礎設施的轉折點——不只在理論上，而是在生產成本下、以足夠長的上下文窗口處理真實世界問題複雜度的實踐中。M3 的發布，為肯定這個問題提出了可信的論據。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 20 處。*
