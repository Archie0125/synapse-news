---
title: "Apple AFM 3：200 億參數端側模型，建構於快閃記憶體之上"
summary: "Apple 在 WWDC 2026 發表第三代 Apple Foundation Models，這是由五款 AI 模型組成、與 Google 合作打造的家族，其中的 AFM 3 Core Advanced 是一款 200 億參數的稀疏多模態端側模型，將完整權重儲存在快閃記憶體中。據 Apple 表示，這些模型將驅動全新的 Siri。"
category: "ai-ml"
publishedAt: 2026-06-29
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "Apple Machine Learning Research — 介紹 AFM 3"
    url: "https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models"
  - name: "9to5Mac — Apple 第三代 Foundation Models 詳解"
    url: "https://9to5mac.com/2026/06/11/apples-new-foundation-models-explained-on-device-ai-cloud-ai-and-everything-in-between/"
  - name: "GIGAZINE — AFM 3 Core Advanced 在 iPhone 上運行"
    url: "https://gigazine.net/gsc_news/en/20260610-apple-foundation-models"
  - name: "MacStories — 第三代 Apple Foundation Models"
    url: "https://www.macstories.net/linked/the-third-generation-of-apples-foundation-models-and-afm-core-advanced/"
  - name: "Let's Data Science — Apple 發表第三代 Foundation Models"
    url: "https://letsdatascience.com/news/apple-debuts-third-generation-foundation-models-and-afm-core-advanced-d7aeb6dc"
tags:
  - "apple"
  - "foundation-models"
  - "端側AI"
  - "siri"
  - "wwdc2026"
  - "afm3"
  - "google"
  - "多模態"
  - "稀疏模型"
  - "私有雲端運算"
relatedSlugs:
  - "2026-06-29-openai-jalapeno-broadcom-inference-chip-zh"
  - "2026-06-27-google-gemini-25-deep-think-reasoning-zh"
  - "2026-06-28-anthropic-ai-for-science-life-sciences-push-zh"
---

Apple 從來不靠模型排行榜競爭。它的 AI 策略始終繞著一個核心限制：什麼能在你口袋裡的裝置上，私密、可靠地運行？WWDC 2026 給出了迄今最有野心的答案——一個 200 億參數的 AI 模型，完全在 iPhone 的快閃記憶體上執行，不傳送任何資料到遠端伺服器。

在 WWDC26 主題演講中發表的第三代 Apple Foundation Models，既是工程壯舉，也是一份價值宣言。這個由五款模型組成的家族，從緊湊的端側模型延伸至強大的伺服器架構，由 Apple 與 Google 聯合開發，共同支撐全新改版的 Siri，並將根本性地改變 Apple 應用程式理解與回應用戶的方式。

## 五款模型，各司其職

AFM 3 分為五個版本，每款在 Apple 隱私優先的 AI 架構中佔據特定位置。

**AFM 3 Core** 是入門端側模型，30 億參數的稠密架構——與前代同類型——但在輸出品質上有顯著提升。在對比測試中，AFM 3 Core 在一般文字任務上有 45.6% 的提示獲得偏好，而 2025 年基準模型為 23.3%；在圖像理解方面，當使用者對兩者有所偏好時，選擇它而非前代的比例超過 61%。它處理每日對延遲敏感的任務，是那些哪怕等一秒鐘都讓人感到不可接受的情境。

**AFM 3 Core Advanced** 則是 Apple 工程野心的具體展現。200 億參數，大約是 AFM 3 Core 的六倍。然而它仍在端側運行，採用建立在「指令跟隨剪枝」（Instruction-Following Pruning, IFP）上的稀疏架構，這項技術由 Apple 研究人員開發。在任何時刻，模型只激活 10 到 40 億個參數——僅是理論容量的一小部分——根據當前請求的性質選擇調用哪些專家子網路。

使這一切成真的架構技巧是：「完整模型儲存在快閃記憶體（NAND）中」，而非存在主動 RAM 裡。快閃記憶體遠比 DRAM 慢，但 AFM 3 Core Advanced 的稀疏設計意味著任何時刻只需將一小部分模型載入主動記憶體。複雜推理任務時激活更多專家，簡單請求則模型輕量運行。Apple 稱此為「推論時間彈性」（inference-time elasticity）。

其餘三款模型在 Apple 私有雲端運算（Private Cloud Compute）基礎設施上運行。**AFM 3 Cloud** 針對速度、效率與效能進行最佳化；**ADM 3 Cloud（Image）**負責圖像生成與編輯；**AFM 3 Cloud Pro**——家族中最強大的伺服器端模型——驅動最吃重的使用情境，例如代理式工具使用與複雜推理。

## Google 與 NVIDIA 的協作

AFM 3 由 Apple 與 Google 聯合開發，這一合作比基礎設施協議還要深入。特別是 AFM 3 Cloud Pro，Apple 與 Google 及 NVIDIA 合作，將其私有雲端運算架構延伸至 Google Cloud 中的 NVIDIA GPU，同時維持相同的隱私保證。

這次合作代表了一家向來堅持掌控自有硬體的公司的務實調整。即使是 Apple 世界級的 Apple Silicon，也無法比肩運行數百顆 Blackwell GPU 的 Google Cloud 叢集。面對 AI 效用最前沿——長週期代理工作流——Apple 選擇擴展架構，而非限制模型的能力邊界。

## 這對 Siri 意味著什麼

Apple 將 AFM 3 定位為「全新 Siri」的核心引擎——這個承諾自 2022 年起以各種形式出現，但現在終於建立在遠更強大的基礎之上。

關鍵變化在於推理深度與多模態理解。AFM 3 Core Advanced 能處理複雜的多輪請求，模型需保持跨模態（文字、圖像、語音）的上下文記憶並進行推理，產出真正具有回應感的輸出，而非照本宣科。AFM 3 Core Advanced 的表現力語音在 5 分制平均意見分（MOS）上獲得 4.15 分，Apple 現行文字轉語音系統的基準為 3.87 分，提升 0.28 分。

在並排的聽寫評測中，AFM 3 Core Advanced 在整體品質上以 44.7% 對 17.6% 的比例勝過 Apple 先前的聽寫系統。

## 以工程實現隱私，而非靠政策承諾

AFM 3 發表中最鮮明的特色，是 Apple 始終把隱私當作工程約束，而非廣告賣點來處理。整個架構——只激活必要參數的稀疏模型、基於快閃記憶體的儲存、具備可驗證隱私屬性的私有雲端運算——確保隱私保證從系統結構中自然產生，而非依賴政策承諾。

Apple 明確表示，除非用戶明確選擇協助改進，否則訓練基礎模型時不會使用用戶的私人個人資料或用戶互動記錄。訓練資料來自公開可取得的資訊、向第三方授權或購買的資料、開源資料、專門研究的資料，以及合成資料。雲端元件運行在 Apple 擁有密碼學證明的基礎設施上，確保用戶資料無法被記錄或儲存，且獨立安全研究人員可透過審查安全飛地中運行的軟體來驗證這些屬性。

這一架構與大多數其他前沿 AI 系統形成對比——在那些系統中，隱私通常是服務條款承諾，而非技術保障。

## 端側智慧的競賽

Apple AFM 3 的發表，恰逢整個產業正廣泛應對雲端依賴型 AI 的成本與延遲問題。每個需要遠端伺服器的請求都增加延遲、消耗 API 費用，並引發隱私疑慮。將更多 AI 運算推向邊緣裝置的經濟壓力巨大——而 AFM 3 Core Advanced 證明了端側 AI 的能力前沿正在以比多數觀察者預期更快的速度移動。

在手機上運行 200 億參數——即使是稀疏的——過去被認為是 2027 或 2028 年才可信的挑戰。Apple 基於快閃記憶體的 IFP 架構在 2026 年就做到了。這不僅關係到 iPhone 用戶，更刷新了整個產業對邊緣推論能做到什麼的認知基準。

憑借 Apple Silicon 的記憶體頻寬優勢，以及為這個模型家族從頭打造的軟體堆疊，AFM 3 Core Advanced 為「主權、私密、端側 AI」樹立了新標竿。現在的問題是，業界其他玩家需要多長時間追上——以及屆時 Apple 是否已再次移動了目標。

---

*AFM 3 適用於搭載 Apple Silicon 的 iPhone、iPad 與 Mac 裝置，各項功能將透過 iOS 20、iPadOS 20 與 macOS Tahoe 在 2026 年下半年陸續推出。*

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 12 處。*
