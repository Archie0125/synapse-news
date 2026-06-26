---
title: "Sail Research 獲 Sequoia 與 Kleiner Perkins 領投 8,000 萬美元，要讓長期運行 AI 代理便宜十倍"
summary: "由前蘋果與 Nvidia 工程師創立的舊金山新創 Sail Research，完成了由 Kleiner Perkins 領投種子輪、Sequoia 領投 A 輪的合計 8,000 萬美元融資，估值達 4.5 億美元。公司的核心產品是專為長期運行 AI 代理優化的 Linux 虛擬機「Sailboxes」，可在代理等待期間暫停計算資源，並支援多代理協作，在 BrowseComp-Plus 基準測試中以同類推論成本的十分之一達到 90.72% 的新高分。"
category: "startups"
publishedAt: 2026-06-26
lang: "zh"
featured: false
trending: false
sources:
  - name: "SiliconANGLE: Sail Research raises $80M to optimize long-horizon AI agents"
    url: "https://siliconangle.com/2026/06/25/sail-research-raises-80m-optimize-long-horizon-ai-agents/"
  - name: "The Next Web: Sail raises $80M to make AI agents cheaper to run"
    url: "https://thenextweb.com/news/sail-research-80m-ai-agent-inference"
  - name: "PR Newswire: Sail Research Raises $80 Million"
    url: "https://www.prnewswire.com/news-releases/sail-research-raises-80-million-to-build-max-efficiency-infrastructure-for-ai-agents-302810497.html"
  - name: "FinSMEs: Sail Research Raises $80M in Seed and Series A"
    url: "https://www.finsmes.com/2026/06/sail-research-raises-80m-in-seed-and-series-a-funding.html"
tags:
  - "Sail Research"
  - "AI 代理"
  - "AI 基礎設施"
  - "Sequoia"
  - "Kleiner Perkins"
  - "推論優化"
  - "新創融資"
relatedSlugs:
  - "2026-06-11-cognition-devin-1b-26b-valuation-zh"
  - "2026-06-07-supabase-500m-series-f-vibe-coding-zh"
  - "2026-06-25-runlayer-30m-series-a-ai-agent-governance-zh"
---

每個 AI 代理都在燒錢思考。每一次 API 呼叫、每一個推理步驟、每一個代理等待工具回應的小時——全都在消耗 Token、消耗算力、消耗資金。隨著 AI 代理從新奇功能演進為企業基礎設施，以規模化方式運行它們的經濟成本，已成為整個行業雄心的實質約束。

Sail Research 相信，這個約束本身就是一個商業機會。這家舊金山新創本週宣布，完成了由 Kleiner Perkins 領投的種子輪與 Sequoia 領投的 A 輪融資，合計 8,000 萬美元，《財富》雜誌報導估值達 4.5 億美元。公司的賣點具體而技術性：它建立了一套基礎設施，能以現有服務十分之一的成本運行長期運行的 AI 代理——執行跨越數小時、數天乃至數週連續作業的任務。

若這個成本削減在企業條件下得以維持，它將代表著一次重大轉變：哪些任務在自動化上是經濟可行的，邊界將大幅移動。

## 長期任務的基礎設施困境

大多數 AI 基礎設施是針對短互動優化的。使用者提問，模型回應，對話結束。算力成本有邊界，記憶體需求可管理，失效模式相對簡單。企業應用不是這樣運作的。

真實世界的代理部署——自動化軟體工程、延伸型研究任務、多步驟客戶工作流程、複雜數據分析管線——需要能夠運作數小時或數天、在數千個步驟中維持上下文、與多種工具和外部服務協調，並在單一步驟失敗時優雅恢復的代理。這是一個在根本上不同於服務聊天機器人的基礎設施挑戰，而現有雲端供應商的通用 GPU 基礎設施並非為此而設計。

Sail 的創辦人——均來自蘋果和 Nvidia 工程師背景的 Neil Movva 和 Samir Menon——得出結論：長期代理的基礎設施需求，與實際存在的基礎設施之間的落差，已大到足以圍繞其建立一家公司。「代理需要規模、可靠性和可持續的成本，」執行長 Neil Movva 在融資公告中表示。

## Sailboxes 如何運作

公司的核心技術產品是它所稱的 Sailboxes：針對 AI 代理工作負載量身客製化的 Linux 虛擬機。Sailboxes 解決了幾個讓現有雲端虛擬機在長期代理任務中既昂貴又不可靠的具體問題。

最關鍵的是閒置成本。AI 代理在運行期間有相當大比例的時間是在等待——等待工具呼叫回應、等待外部 API 返回、等待人類審批、等待長計算步驟完成。在標準雲端部署中，等待回應的代理仍佔用 GPU 記憶體並支付未使用的算力費用。Sail 的基礎設施能在等待期間暫停代理，釋放計算資源，並在回應到達時無縫恢復。對於等待時間佔比可觀的工作負載——這包括大多數真實世界的企業代理部署——這種暫停-恢復能力本身就能代表顯著的成本削減。

Sailboxes 也可以連結成協作的代理「集群」：多個代理協作執行一個共同任務的網路，由 Sail 的全局控制器基礎設施統籌調度。這在架構上對複雜的企業工作流程至關重要——對於那些規模過大、過於多維，無法由單一代理依序執行的任務——從並行工作流、專業分工到相互錯誤檢查，都能受益。

在推論側，Sail 基於成熟的開源工具鏈，包括 vLLM 及其 PagedAttention 算法——後者通過更智能地管理 Transformer 推論中使用的鍵值快取（Key-Value Cache），比樸素實現更高效地利用 GPU 記憶體。公司在此基礎上疊加了自身的優化，針對長期代理工作負載的記憶體存取模式專門調整。

## BrowseComp-Plus 基準測試

Sail 隨融資公告一同發布了基準測試結果——這個舉動反映了對其技術性能的信心，也反映了在日益擁擠的 AI 基礎設施市場中，可驗證的效率指標的重要性正在增長。

在 BrowseComp-Plus——一個評估 AI 系統在需要多步驟信息收集和綜合的複雜在線研究任務上的基準——Sail 報告了 90.72% 的分數，被描述為該基準的新高，同時在相同任務上的推論成本僅為競爭對手服務的十分之一。

性能與成本效率的組合，是核心主張。一個更便宜但性能更差的基礎設施很容易被否定；一個更昂貴但性能更好的則代表不同類型的產品。Sail 在標準化基準上同時實現兩者的斷言，使這次融資公告的意義超越其美元價值本身。

## 投資人陣容

本輪融資的投資人構成，反映了頂級機構對代理 AI 基礎設施論題的信心規模。Sequoia 和 Kleiner Perkins 是矽谷最具選擇性的一線創投機構，它們在連續融資階段的共同參與，表明對論題和創辦團隊都有高度的一致判斷。

天使投資人名單增添了另一個維度的可信度。John Hennessy，Alphabet 董事會主席、電腦架構傳奇人物，其對 RISC 處理器的研究塑造了現代 CPU；Lip-Bu Tan，英特爾執行長，帶來了半導體專業知識和製造大部分全球 AI 晶片先進封裝的公司的戰略投資關係；Tri Dao，Together AI 首席科學家，也是 FlashAttention 算法的共同作者——這個算法顯著提升了 Transformer 推論效率——或許是最具技術針對性的背書：讓 AI 推論更快的核心研究者之一，正在用個人資金押注 Sail 的方法。

其他機構投資人包括 Redpoint Ventures、Theory Ventures、Vine Ventures、CRV、A* Capital 和 Abstract Ventures。

## 市場背景：代理 AI 的基礎設施競賽

Sail 進入的是一個正在快速吸引競爭的市場。隨著企業從實驗 AI 聊天機器人轉向在生產工作流程中部署 AI 代理，支撐這些部署的基礎設施層，已成為重要的投資主題。多家新創正在追求相關方向——優化推論成本、建設代理專用算力，或為長期運行的 AI 工作負載提供託管環境。

使 Sail 定位獨特的，是它專注於長期使用案例的成本維度。許多 AI 基礎設施公司強調性能——更低的延遲、更高的吞吐量、更好的可靠性。Sail 的主要主張是：針對一類市場日益認為具有戰略意義、但以當前價格點在經濟上處於邊際的工作負載的成本效率。

公司的時機同樣值得注意。融資公告緊隨著在 AI 代理工具方面的重大投資浪潮之後——從 OpenAI 的 Codex 平台到 Anthropic 的 Claude Code，再到 GitHub Copilot 的代理能力——這些已將代理 AI 確立為主流企業類別，而非研究上的好奇心。隨著類別成熟，底層基礎設施的經濟學對採用速度變得更加關鍵。

Sail 能否在市場擴大、更大型雲端供應商優化自身代理基礎設施時維持其所聲稱的成本優勢，仍是一個開放問題。雲端運算的歷史表明，超大規模供應商最終會縮小與專業供應商之間的性能差距——但也表明，專業供應商可以在界定清晰的使用案例中維持有意義的優勢相當長的時間。

眼下，Sail 正押注於：專業化、成本優化的代理基礎設施能夠維持溢價的窗口，足夠長到建立一個持久的業務。有了 8,000 萬美元、Sequoia、Kleiner Perkins，以及業界一些最受尊敬的技術人物的背書，它有足夠的跑道去找出答案。
