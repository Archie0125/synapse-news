---
title: "NVIDIA 發布 Ising 量子 AI 模型，Xanadu 股價飆漲 250%，執行長一週成億萬富翁"
summary: "加拿大光子量子運算新創 Xanadu Quantum Technologies 的股價在 NVIDIA 發布 Ising 開源量子 AI 模型後暴漲近 250%。創辦人兼 CEO Christian Weedbrook 在公司上市僅數週後身價突破 15 億美元，Xanadu 市值一度衝向 160 億美元，成為量子運算賽道唯一上市的純正標的。"
category: "hardware"
publishedAt: 2026-04-22
lang: "zh"
featured: false
trending: true
sources:
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-04-17/nvidia-helps-make-quantum-computing-ceo-a-billionaire-in-days"
  - name: "Fortune"
    url: "https://fortune.com/2026/04/22/christian-weedbrook-ceo-xanadu-quantum-technologies-net-worth-nvidia/"
  - name: "The Quantum Insider"
    url: "https://thequantuminsider.com/2026/03/27/xanadu-becomes-first-pure-play-photonic-quantum-computing-company-to-go-public/"
tags:
  - "Xanadu"
  - "量子運算"
  - "NVIDIA"
  - "光子量子"
  - "Ising模型"
  - "IPO"
  - "Christian Weedbrook"
relatedSlugs:
  - "2026-04-17-nvidia-ising-quantum-ai-models-zh"
---

Christian Weedbrook 花了大約 15 年從零打造一家量子運算公司，NVIDIA 只用了五天，就讓他成了億萬富翁。

總部位於多倫多的光子量子運算公司 Xanadu Quantum Technologies，在 NVIDIA 發布 Ising 開源 AI 模型系列後的一週內，股價從公告前水準暴漲約 250%。Ising 是一套專為解決量子運算兩大頑疾而設計的 AI 模型：誤差校正與校準（calibration）。

到 4 月中旬，Weedbrook 持有的 4,640 萬股多重投票股票，依 Bloomberg 根據市場數據與法規申報文件計算，市值約達 15 億美元。Xanadu 的市值盤中一度衝向 160 億美元——對於一家剛在三週前（3 月 27 日）才透過與 Crane Harbor Acquisition Corp. 完成 3.02 億美元 SPAC 合併、在那斯達克與多倫多證交所雙掛牌上市的公司而言，這個漲幅令人咋舌。

NVIDIA 並未投資 Xanadu，但也不需要。NVIDIA 以最高等級的公信力背書量子運算這個賽道，讓 Xanadu——全球唯一掛牌的純正光子量子運算公司——成為最直接的受益者。

## NVIDIA Ising 模型究竟解決了什麼？

要理解為何 Xanadu 受益特別明顯，需要先搞清楚 Ising 模型的作用，以及它為何與 Xanadu 的技術路線高度契合。

NVIDIA 發布的 Ising 模型系列，針對的是長期阻礙量子電腦實用化的兩大問題。其一是**校準**：量子處理器在每次使用前都必須進行繁瑣的精確調校，目前這個過程往往需要數天。Ising 的校準模型將這一設定時間從數天縮短至數小時。其二是**誤差校正**：量子位元（qubit）天生脆弱，容易因退相干而累積誤差。Ising 的誤差校正模型速度比現行業界標準快 2.5 倍、精準度高 3 倍。

這不是漸進式的改良，而是可能改變遊戲規則的躍升——讓量子電腦從實驗室裡的稀罕物，變成工程師可以排程使用的系統。更關鍵的是，Ising 模型設計上**不綁定特定硬體架構**，適用於多種量子硬體平台。

這個「硬體中立」的定位，正是 Xanadu 受益如此強烈的原因。Xanadu 以光子為量子位元載體（用光束而非超導電路或捕獲離子），技術路線長期被視為前途可期但商業前景不確定。NVIDIA 為「AI 加速量子運算」這個類別整體背書，而非押注特定硬體，等於間接宣告：光子方案是值得認真對待的競爭者。

## 從電影系學生到量子億萬富翁

Christian Weedbrook 的人生故事，恰好打破了矽谷科技創業者的刻板印象。

他曾就讀電影系，後來轉向量子物理學。他在澳洲昆士蘭大學取得量子資訊理論博士學位，之後在麻省理工學院完成博士後研究。2016 年，他在多倫多創立 Xanadu，彼時量子運算仍幾乎是純理論領域，「量子優越性」這個詞還沒走進主流話語。

在接下來十年裡，他將公司建立在一個技術信念上：**光子量子運算是正確的長期道路**——因為光子在室溫下運作，不需要讓競爭方案昂貴又難擴充的極低溫冷卻系統，且可以用現有半導體製程製造。

2026 年 1 月，Xanadu 在其 Aurora 系統上展示了 12 個邏輯 GKP 量子位元，在各家量子硬體路線邏輯量子位元數量普遍偏低的當下，這是一個具有實質意義的里程碑。公司同時維護著 PennyLane——量子機器學習領域最廣泛使用的開源函式庫之一——這讓 Xanadu 擁有規模遠超其商業體量的開發者社群。

## Aurora 系統與光子量子的可擴充性主張

Xanadu 技術論點的核心是 Aurora 系統——一套模組化的容錯光子量子電腦，其設計哲學是將量子擴充性問題類比為網路問題，而非晶片設計問題。

超導路線試圖在單一晶片上塞入越來越多的量子位元，在規模化過程中面臨嚴酷的冷卻、量子串擾與良率挑戰；Xanadu 的光子架構則透過光纖連結多個較小的光子模組來進行擴充——就像資料中心透過網路互聯伺服器而非打造越來越龐大的單一主機來擴充算力。公司認為，這種模組化方式的可擴充性在本質上更優越，因為所需的光纖互連正是全球電信基礎設施已在大規模製造和廣泛理解的技術。

這個架構押注的是長期賽道。光子系統目前的閘極保真度低於最優秀的超導處理器。但 Xanadu 及其支持者認為，可擴充性優勢會隨時間複利累積，而室溫運作則消除了量子運算大規模普及最大的成本障礙。

## 漲勢能否持續？

股價漲幅的可持續性確實值得商榷。多位分析師指出，Xanadu 股價在高峰時的隱含估值，難以用任何近期收益預測來支撐。公司尚未有實質意義的商業收入，盈利之路取決於量子運算採用曲線——而那條曲線至今仍高度不確定。

反駁的觀點是：NVIDIA 的背書從根本上改變了這道機率題。在 Ising 問世之前，量子運算的時間表模糊、硬體路線之爭懸而未決。Ising 之後，全球最大的 GPU 公司公開投入工程資源，讓量子電腦「現在就更好用」。這不等於 NVIDIA 投資了 Xanadu，但對整個產業方向是一個強烈訊號。

Xanadu 的股價能否在 100 億至 160 億美元的估值區間站穩，終究取決於它能否在 Aurora 系統上展示出明顯優於古典計算的商業工作負載。那個時刻還在前方，尚未到來。

但有一件事已經發生：Xanadu 現在是量子運算賽道的公開市場標的股票。在一個長期難以吸引主流投資人關注的領域，這個位置本身，或許就像任何單一技術里程碑一樣有價值。
