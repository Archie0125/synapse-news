---
title: "Qualcomm 傳 40 億美元收購 Modular，正面挑戰 Nvidia 軟體護城河"
summary: "Bloomberg 報導，Qualcomm 正就以約 40 億美元收購 AI 基礎設施軟體新創 Modular 進行深度談判。此舉直指 Nvidia 最持久的競爭優勢——CUDA 生態系綁定——將 Modular 的硬體無關 Mojo 語言與 MAX 推論引擎納入 Qualcomm 持續壯大的晶片矩陣。"
category: "hardware"
publishedAt: 2026-06-24
lang: "zh"
featured: false
trending: true
sources:
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-06-22/qualcomm-is-said-to-near-deal-for-ai-chip-startup-modular"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/318921/20260624/qualcomm-reportedly-nears-4-billion-modular-deal-attack-nvidia-software-moat.htm"
  - name: "GuruFocus"
    url: "https://www.gurufocus.com/news/8925977/qualcomm-in-talks-to-acquire-modular-for-4-billion"
tags:
  - "Qualcomm"
  - "Modular"
  - "Mojo語言"
  - "CUDA"
  - "Nvidia"
  - "AI晶片"
  - "併購"
relatedSlugs:
  - "2026-06-17-qualcomm-tenstorrent-acquisition-risc-v-ai-chip-zh"
  - "2026-04-21-nvidia-groq-antitrust-senate-zh"
---

Qualcomm 正就以約 40 億美元收購 Modular 進行深度談判。Modular 是由 Chris Lattner 與 Tim Davis 聯合創辦的 AI 基礎設施軟體新創，這筆交易若告達成，將是這家晶片廠商迄今對 Nvidia 軟體生態系霸權最具針對性的一次挑戰。

Bloomberg 於 6 月 22 日率先披露這項談判。消息人士表示，相關公告預計在未來數日內發布，時間點刻意接近 Qualcomm 於 6 月 24 日舉行的投資者日。

## Modular 的核心價值

Modular 由兩位在 Google 相識的工程師於 2022 年創辦：Chris Lattner 是 Swift 程式語言的發明人，也是支撐現代晶片工具鏈的 LLVM 編譯器基礎設施之父；Tim Davis 則是資深系統工程師。公司旗下兩款核心產品——Mojo 程式語言與 MAX 推論引擎——均圍繞同一核心論題打造：AI 產業應能「一次撰寫、多處執行」，不需要在不同硬體間切換時承受效能損耗或程式碼重寫的代價。

Mojo 是 Python 的超集，能編譯為高效機器碼，並設計為可在 Nvidia H 系列 GPU、AMD Instinct 加速器、Intel Gaudi 晶片及 Qualcomm 自家 AI 處理器等異質硬體上，以接近 C++ 的速度運行。MAX 則是坐落於 PyTorch 或 JAX 匯出模型之上的推論優化引擎，能從底層矽晶體中榨取接近最優的效能，不論底層是哪家廠商的晶片。

Qualcomm 試圖打破的 Nvidia 護城河，是真實且深度嵌入的。CUDA 作為 Nvidia 的專有運算平台，已是 AI 研發的預設開發環境逾十年。以 CUDA 撰寫的程式碼無法在競爭晶片上原生執行。將一個生產 AI 工作負載從 Nvidia H100 遷移至 AMD MI450 或 Qualcomm 雲端 AI 晶片，需要程式碼重寫——有時是局部的，有時是大規模的——這帶來了時間、成本與功能退化的風險。這種摩擦讓客戶繼續留在 Nvidia 硬體上，即使替代方案在技術上已具競爭力甚至更便宜。

Mojo 與 MAX 試圖以一個抽象掉底層硬體差異的軟體層，消解這種摩擦。若成功，這套工具將把 AI 推論晶片的採購決策，從「我的程式碼已跑在哪裡」轉移到純粹比拼效能、功耗與價格。

## Qualcomm 的併購狂潮

若 Modular 交易獲確認，這將是 Qualcomm 本月的第二筆重大 AI 收購，此前還有單獨報導的以 80–100 億美元追購 RISC-V AI 晶片新創 Tenstorrent 的計畫，後者獲現代汽車與三星支持。

加上此前 24 億美元收購高速互連技術廠商 Alphawave，以及對 RISC-V 設計公司 Ventana 的收購，Qualcomm 已拼湊出垂直整合的 AI 運算堆疊完整版圖：處理核心（Ventana）、互連織網（Alphawave）、加速器晶片（Tenstorrent），以及如今的軟體可移植性（Modular）。

40 億美元的估值相較 Modular 九個月前上一輪融資的約 16 億美元，出現了約 2.5 倍的大幅跳升，漲幅完全由 AI 軟體基礎設施日益高漲的戰略重要性所驅動。

## 投資者日的時機計算

這筆傳聞交易與 Qualcomm 6 月 24 日投資者日的高度接近，似乎經過精心部署。執行長 Cristiano Amon 全年向分析師發出信號：Qualcomm 的資料中心 AI 雄圖，需要的不只是具競爭力的矽晶片，還需要一個能為企業客戶提供可行遷移路徑、讓他們有機會脫離 Nvidia 生態系的軟體故事。

若在投資者日前後宣布收購，Amon 即可向市場呈現一幅完整的願景：自研處理核心、高頻寬互連、加速器硬體，以及一個讓模型從 Nvidia 硬體跑上 Qualcomm 晶片而無需完整重寫的軟體平台。正是這個完整的故事，是 Qualcomm 向超大規模雲端業者推銷時一直缺少的拼圖。

Bloomberg 報導當天，Nvidia 股價下跌約 1.8%——這對一家鮮少因晶片挑戰者的競爭新聞而波動的公司來說，是一個微小但值得關注的信號。Bernstein 的分析師在客戶報告中指出：「若 Modular 收購告成，這將是自 ROCm 以來對 CUDA 最具公信力的軟體層挑戰，而 ROCm 已經努力了十年。」

## 開源承諾的隱憂

此次交易存在一個懸而未決的不確定因素：Modular 的開源承諾。Mojo 與 MAX 均以寬鬆授權條款作為開源項目開發，Lattner 公開承諾保持開源，圍繞這個預期已形成規模可觀的開發者社群。

Qualcomm 如何平衡商業利益——讓 Modular 工具在 Qualcomm 晶片上特別優化——與「在所有硬體上都能良好運作」的開源承諾之間的張力，將受到開發者社群和 Modular 企業客戶的密切檢視。一旦外界認為這套工具已被改造為 Qualcomm 專屬，而非真正維持硬體中立性，那就從根本上動搖了支撐這筆收購價格的核心價值主張。

截至發稿時，Qualcomm 與 Modular 均未就傳聞中的交易發表評論。
