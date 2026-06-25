---
title: "Nvidia Vera Rubin 機架飆至 780 萬美元：記憶體成本暴漲 435%，GPU 不再是主角"
summary: "摩根士丹利最新分析指出，Nvidia Vera Rubin VR200 NVL72 機架單價估計達 780 萬美元，幾乎是 Blackwell 世代 350–400 萬美元的兩倍，主要由 HBM4 和 LPDDR5X 記憶體成本暴漲 435% 所驅動，記憶體費用超過 200 萬美元，佔總成本 26%。Bernstein 更警告最終售價可能高達 910 萬美元。隨著 2026 年 Q3 開始出貨，Vera Rubin 世代標誌著一個結構性轉變：GPU 矽晶片不再是 AI 基礎設施定價的主宰。"
category: "hardware"
publishedAt: 2026-06-25
lang: "zh"
featured: true
trending: true
sources:
  - name: "Tom's Hardware：Nvidia 記憶體成本飆漲 485%，最新 AI 系統造價達 780 萬美元"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-memory-costs-soar-485-percent-latest-ai-systems-now-cost-usd7-8-million-to-build-memory-now-comprises-25-percent-of-the-total-cost-rubin-gpus-a-mere-usd50-000-apiece"
  - name: "PC Gamer：摩根士丹利估算 Nvidia Vera Rubin 機架超過 780 萬美元"
    url: "https://www.pcgamer.com/hardware/a-single-nvidia-vera-rubin-rack-is-estimated-to-cost-usd7-803-148-with-over-usd2-million-of-that-figure-spent-on-memory-alone/"
  - name: "WCCFTech：NVIDIA Vera Rubin 機架遭遇 435% 記憶體漲價，HBM4 費用達 200 萬美元"
    url: "https://wccftech.com/nvidia-vera-rubin-rack-hit-with-memory-price-surge-pushing-hbm4-lpddr5x-bill-to-2m-of-7-8m-total/"
  - name: "Bernstein：Vera Rubin 機架將達 910 萬美元"
    url: "https://wccftech.com/bernstein-warns-nvidias-vera-rubin-racks-will-hit-9-1-million-as-hbm4-prices-triple-to-53-per-gigabyte/"
tags:
  - "Nvidia"
  - "Vera Rubin"
  - "NVL72"
  - "HBM4"
  - "AI硬體"
  - "資料中心"
  - "記憶體"
  - "摩根士丹利"
relatedSlugs:
  - "2026-06-11-nvidia-rubin-platform-vera-cpu-zh"
  - "2026-06-04-big-tech-725b-ai-capex-race-zh"
  - "2026-06-14-nvidia-sk-hynix-ai-memory-partnership-zh"
---

GPU 已不再是 AI 基礎設施採購中最重要的費用項目。摩根士丹利針對 Nvidia 即將上市的 Vera Rubin 世代所發布的最新研究報告，拋出了一個正在重塑超大規模雲端業者和基礎設施投資者思維的數字：單一 **VR200 NVL72 機架估計售價 780 萬美元**（約新台幣 2.5 億元）——幾乎是上一代 Blackwell NVL72 機架 350–400 萬美元的兩倍。罪魁禍首是記憶體。從 Blackwell 到 Rubin，HBM4 和 LPDDR5X 的價格暴漲 **435%**，使單一機架的記憶體費用突破 **200 萬美元**，佔總系統成本的約 26%。

Vera Rubin 世代確認將於 2026 年 Q3 開始初步出貨、Q4 進入量產，標誌著 Nvidia 推出 NVL72 機架形式以來 AI 機架經濟學最重大的結構性轉變。AI 基礎設施定價的故事，已不再只是關於 GPU 矽晶片——而是關於記憶體。

## Vera Rubin 機架的成本解剖

要理解 VR200 NVL72 機架的定價，必須逐一分析各元件類別：

**GPU。** 每顆 Rubin GPU 在超大規模客戶的批量採購價預計約 5.5 萬美元，搭配的 Vera CPU 協處理器每顆約 5,000 美元。一個 NVL72 機架含 72 顆 GPU，原始矽晶片成本約 430 萬美元——仍是單一最大費用項目，但在總系統成本中的佔比已低於前幾代。

**記憶體。** 這是整個故事的轉折點。VR200 NVL72 內建 **20.7 TB 的 HBM4**（第四代高頻寬記憶體）和 **54 TB 的 LPDDR5X**，記憶體費用合計約 200 萬美元。HBM4 由 Nvidia 與 SK 海力士共同設計（雙方的 AI 記憶體合作夥伴關係本月稍早宣布），目前市場報價約每 GB 53 美元——幾乎是 Blackwell 系統使用的 HBM3e 的三倍。記憶體成本的飆升，既反映 HBM4 先進產能的稀缺性，也體現了一個刻意的架構選擇：Rubin 系統需要大幅更高的記憶體頻寬，才能餵飽 Vera CPU–GPU 緊密整合帶來的更高並行度。

**儲存。** VR200 NVL72 的物料清單新增了約 **100 萬美元的 3D NAND 儲存**，而 GB200 NVL72 在這個項目上的費用幾乎為零。這反映出 Nvidia 在機架設計中整合本地高速儲存的決策，以因應代理式工作負載對大型模型檢查點持久化和快速檢索的需求。

**其他系統元件。** PCB、電源配送、網路（ConnectX-9 NIC）、散熱基礎設施和機箱合計約 45 萬美元，Vera CPU 架構對電源配送密度的更高要求推高了個別元件成本。

## 市場影響

780 萬美元的數字——Bernstein 分析師認為加計 OEM 加價和系統整合費用後可能達到 **910 萬美元**——對 AI 基礎設施市場有幾個立即影響：

**即使機架數量不變，超大規模業者的資本支出仍將大幅增加。** 一家以 350 萬美元採購 1,000 個 Blackwell NVL72 機架（總計 35 億美元）的超大規模業者，購置同等數量的 Vera Rubin 機架要花 78 億美元。這有助於解釋微軟、Google、亞馬遜和 Meta 為何在整個 2026 年 Q1 和 Q2 持續上修資本支出指引，同時刻意迴避說明具體機架採購數量。

**記憶體供應商成為不可或缺的基礎設施。** SK 海力士、三星和美光——HBM4 量產的唯三製造商——現在對 AI 基礎設施建設的重要性不亞於台積電。Nvidia 與 SK 海力士的記憶體合作夥伴關係與其說是行銷安排，不如說是供應鏈命脈：Nvidia 需要獲得保障的 HBM4 配額，才能對超大規模業者履行出貨承諾。

**GPU 費用佔比下降。** Blackwell 時代，GPU 佔機架成本的約 60–65%；Vera Rubin 時代這個比例降至約 55%。記憶體佔比從約 8% 升至 26%。儲存從 Blackwell 的幾乎為零，升至有意義的 13%。這種成本多元化具有結構性意義：受益於 AI 基礎設施熱潮的供應商，正從純半導體設計向記憶體封裝、先進封裝和儲存層擴展。

## Vera Rubin 為何設計上就更昂貴

Vera Rubin 架構代表 Nvidia 十餘年來與純 GPU 模型最大的一次背離。核心創新是 **Vera CPU**——一顆專為管理大型 AI 叢集的資料移動、協調和記憶體層級而設計的客製 Arm 處理器。相較於依賴 Intel 或 AMD 的主機 CPU 協調 GPU 工作負載，Vera Rubin 將 CPU 功能直接整合進機架的運算架構中。

這種緊密整合大幅提升了超大型模型推論的效率——尤其是正在成為企業 AI 主流應用場景的長上下文、多步驟代理工作負載。但代價是：Vera CPU 需要自己的記憶體層級（因此增加 LPDDR5X）、自己的電源配送（增加系統複雜度），以及客戶必須與現有 ML 基礎設施整合的新韌體和軟體堆疊。

儲存整合同樣反映了代理時代的架構需求。執行長程代理迴圈（寫程式碼、瀏覽網頁、編輯文件、管理檔案）的模型，會在各步驟間產生並消耗大量中間狀態。機架層級的本地 NVMe 儲存消除了這些工作負載對網路附加儲存的往返延遲，改善延遲性能，但增加了硬體成本。

## 對 AI 資本支出預測的意義

高盛在 2026 年 6 月發布了 2035 年前十年 AI 資本支出 76 兆美元的預測，當時引發了相當大的質疑。Vera Rubin 的定價數據為這個龐大數字提供了具體的算術支撐。

一個 1 萬機架的超大規模叢集——大致相當於第一代 Colossus 的規模——僅硬體費用就達約 780 億美元（不含散熱基礎設施、網路、電源配送和土地建物）。Meta 宣佈的 2 GW AI 叢集計畫，意味著跨多個設施超過 20 萬個高端 GPU 機架；按每機架 780 萬美元計算，僅硬體成本就接近 1.5 兆美元——不是十年後，而是在當前的資本支出週期內。

這些數字聽起來難以置信——直到你看看超大規模業者實際做出的財務承諾：微軟 2026 年 1,900 億美元的資本支出指引、Google 承諾投入 800 億美元的 AI 基礎設施，以及亞馬遜客製矽晶片業務超過 200 億美元的年化營收規模，都與每個機架售價 780 萬美元、訂單量達數千個的世界高度吻合。

## SK 海力士的訊號

Vera Rubin 故事中最值得玩味的數據點之一，是它對 SK 海力士意味著什麼。這家韓國記憶體巨頭本月稍早宣布與 Nvidia 的 AI 記憶體合作夥伴關係——超越優先供應商地位，涵蓋針對 Vera CPU 架構最佳化的 HBM4 堆疊聯合設計。對 SK 海力士股東而言，780 萬美元的機架售價不是隱憂，而是商機：每售出一個 VR200 NVL72 機架，就有 200 萬美元的記憶體內容，SK 海力士將取得其中相當大的份額。

從這個角度看，AI 基礎設施熱潮正在引發半導體價值鏈中自行動時代以來最重大的轉移——將數十億美元從邏輯晶片（Nvidia 在此獲取豐厚利潤）向記憶體（HBM4 供應商在此獲取豐厚利潤）遷移。兩者可以同時成立，這正是為何 AI 基礎設施投資週期正在為異常廣泛的硬體公司聯盟帶來財務回報。

Vera Rubin 量產出貨將在 2026 年 Q4 啟動。機架售價，將是塑造未來兩年 AI 基礎設施經濟學的關鍵數字。
