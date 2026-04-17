---
title: "NVIDIA 發布 Ising：全球首批開源量子運算 AI 模型"
summary: "NVIDIA 推出全球首個專為量子運算設計的開源 AI 模型家族 Ising，針對量子位元校準與量子錯誤校正兩大核心痛點，比現有開源標準快 2.5 倍、準確率提升 3 倍。發布後帶動量子運算概念股 IonQ 單日暴漲逾 20%，標誌著 AI 基礎設施巨頭正式跨足量子硬體生態系。"
category: "hardware"
publishedAt: 2026-04-17
lang: "zh"
featured: true
trending: true
sources:
  - name: "NVIDIA Newsroom"
    url: "https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers"
  - name: "The Quantum Insider"
    url: "https://thequantuminsider.com/2026/04/14/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers/"
  - name: "NVIDIA Technical Blog"
    url: "https://developer.nvidia.com/blog/nvidia-ising-introduces-ai-powered-workflows-to-build-fault-tolerant-quantum-systems/"
tags:
  - "NVIDIA"
  - "量子運算"
  - "開源"
  - "錯誤校正"
  - "AI 模型"
  - "黃仁勳"
relatedSlugs:
  - "2026-04-15-ionq-photonic-quantum-networking-darpa-zh"
  - "2026-04-10-nvidia-cosmos-reason2-groot-physical-ai-zh"
---

NVIDIA 過去兩年悄悄組建了一支量子 AI 研究團隊。2026 年 4 月 14 日，這支團隊的成果正式公開亮相。

該公司發布了 **Ising**——全球首批專為加速量子運算研究與商業部署所設計的開源 AI 模型。模型現已免費上架 Hugging Face 及 NVIDIA NGC 目錄，針對目前阻礙量子硬體邁向生產部署的兩大核心瓶頸：**校準漂移**與**量子錯誤校正**。

模型命名取自物理學中的「易辛模型」（Ising Model），這一統計力學基礎框架長期以來是量子退火機和最佳化問題的標竿測試基準。黃仁勳親自出席發布，強力宣示量子運算已不再是 NVIDIA GPU 核心業務的旁枝末節，而是整體平台藍圖的一部分。

## 兩個模型，解決兩大瓶頸

Ising 分兩個獨立組件上市，各自針對阻礙量子硬體商業化的一類特定失效模式。

**Ising Calibration** 是一個視覺語言模型，訓練用於解讀量子處理器的原始測量輸出——即量子工程師目前須花費數天人工分析的噪音漂移訊號流。量子硬體本質上不穩定：量子位元頻率會隨溫度、電磁干擾與材料老化而漂移，從頭重新校準一台大型量子處理器可能耗費 8 小時到 3 天不等。

Ising Calibration 將此問題轉化為多模態感知任務，就像視覺模型解讀圖片一樣讀取量子態斷層掃描數據，自動識別漂移特徵並給出參數修正建議，將校準週期從數天壓縮至數小時。對試圖讓量子硬體達成高可用率的團隊而言，這個差距就是研究設備與可部署系統之間的分水嶺。

**Ising Decoding** 則攻克更難的問題：即時量子錯誤校正。量子電腦的錯誤率若不加以修正，會讓任何運算結果都失去意義。NVIDIA 以現有開源標準 pyMatching 作為基準進行評測，發現 Ising Decoding 的運算速度**快 2.5 倍**，準確率**提升 3 倍**。此次同時發布兩個版本：一個針對原始吞吐量最佳化（適用於延遲敏感的硬體管線），另一個針對解碼精度最佳化（適用於須最小化邏輯錯誤率的研究場景）。

模型設計上硬體中立，可跨超導量子位元、捕獲離子、中性原子及光子平台運作，NVIDIA 不需要押注於單一勝出的硬體路線就能受益於整個生態系的成長。

## 早期採用者陣容強勁

此次發布帶來了一份橫跨地域、陣容可信的早期採用者名單。

中性原子量子硬體新創 **Atom Computing** 正在其自動化漂移校正管線中使用 Ising Calibration；以液氦-3 表面電子為基礎的量子系統公司 **EeroQ** 正在評估 Ising Decoding 的導入可行性。

**費米國家加速器實驗室（Fermilab）**與**哈佛大學量子研究團隊**均已開始試跑早期研究工作負載——兼具國家實驗室的公信力與頂尖學術背書。台灣**中央研究院**也在採用名單之列，考量到台灣在 NVIDIA 硬體供應鏈中的核心地位以及台灣政府近年對量子運算的積極投入，這項合作格外引人注目。

量子編譯器新創 **Conductor Quantum** 則宣布直接將 Ising Decoding 整合至其控制堆疊作為預設錯誤校正層，強烈暗示這批模型已達商業級品質，而非僅供學術實驗。

## IonQ 暴漲 20%，量子概念股全面走揚

此次發布在量子運算股市引發立即且顯著的反應。NYSE 上市的量子硬體公司 **IonQ** 在消息公布後單日股價飆漲逾 **20%**；Rigetti Computing 與 D-Wave 等量子相關個股也紛紛上漲 8 至 12%。

投資人的解讀不僅止於 NVIDIA 的具體產品，更著眼於其所傳遞的訊號：傳統 AI 基礎設施的建置浪潮，正在為量子硬體創造跨越商業化門檻的條件。NVIDIA 願意投資開放的量子 AI 工具，意味著該公司認為商業量子系統即將在以「年」計而非「十年」計的時間軸內落地。

一位量子基礎設施投資人在消息公布後表示：「校準與錯誤校正問題是量子路線圖的墓地，已經埋葬了無數計畫整整十年。如果 NVIDIA 的模型在生產環境中站得住腳，那就移除了不部署的兩個最大技術藉口。」

## 黃仁勳的平台賭局

黃仁勳親自出面發表 Ising 的決定，其戰略意涵遠超量子領域本身。在今年稍早的 GTC 2026 大會上，他將實體 AI 與量子運算列為大型語言模型典範之後的兩大前沿。Ising 是 NVIDIA 量子 AI 研究部門（於 2024 年底悄然成立，成員延攬自 IBM Quantum、Google Quantum AI 及各大學術量子實驗室）的首批具體交付成果。

此次發布也是一個日益清晰的戰略模式的組成部分：NVIDIA 不再甘於只是 GPU 供應商。從物理 AI 模擬的 **Cosmos**、機器人的 **Isaac GR00T**，到量子領域的 **Ising**，加上透過 NGC 持續擴充的模型目錄，NVIDIA 正在構建一個軟體與模型層，讓任何未來的硬體競爭者都難以在不影響客戶關鍵基礎設施存取的情況下取代 NVIDIA GPU。

Ising 開源並非讓步，而是護城河策略：成為量子研究工作流程核心基礎的模型，能在生態系層面創造黏著度，無論底層運算是否為 NVIDIA 硬體。而 NVIDIA 受益於這些模型所驅動的系統規模擴張——那些經典控制系統，在可預見的未來，都將跑在 NVIDIA 晶片上。

## 後續展望

NVIDIA 已表示 Ising 只是更廣泛量子 AI 模型系列的首批發布。預計 2026 年下半年將推出的後續模型，包括量子電路編譯最佳化（協助古典編譯器將邏輯量子電路映射至特定硬體拓撲），以及量子優勢基準測試——一個長期懸而未決的挑戰，即如何可靠地證明量子系統在商業上有意義的任務中勝過最優秀的古典演算法。

這份路線圖顯示，NVIDIA 意圖以當年透過 CUDA 掌控 GPU 加速機器學習軟體層的方式，掌控量子運算的軟體層。那次花了十五年。這次或許更快。

模型已上線。通往實用量子運算的競賽，剛加入了一個新對手——而那正是整個產業賴以運作的硬體供應商。
