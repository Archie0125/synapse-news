---
title: "Google 徹底放棄 Gemini 3.5 Pro 原有架構，以全新設計瞄準 7 月 17 日發布"
summary: "Google DeepMind 在距原訂部署僅剩數天之際，決定完全放棄現有的 Gemini 3.5 Pro 架構，並從頭啟動全新的預訓練流程，目標在 7 月 17 日發布。被廢棄的架構在多步驟數學推理和 SVG 場景生成上觸及性能上限，促使 DeepMind 採取了一次史無前例的工程轉向。"
category: "ai-ml"
publishedAt: 2026-07-11
lang: "zh"
featured: false
trending: false
sources:
  - name: "BigGo Finance"
    url: "https://finance.biggo.com/news/6f0c6bb2-795f-4c57-9d09-6db691d7638a"
  - name: "HackerNoon"
    url: "https://hackernoon.com/google-delays-gemini-35-pro-to-july-17-the-strategic-play-behind-the-scrapped-base-model"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/319877/20260708/gemini-35-pro-targets-july-17-deepseeks-july-24-deadline-hits-developers-now.htm"
  - name: "Bind AI Blog"
    url: "https://blog.getbind.co/gemini-3-5-pro-slips-to-july-and-four-senior-google-researchers-just-left-for-anthropic/"
tags:
  - "Google"
  - "Gemini"
  - "DeepMind"
  - "AI模型"
  - "大型語言模型"
  - "模型訓練"
relatedSlugs:
  - "2026-07-01-google-gemini-35-pro-july-launch-delayed-zh"
  - "2026-07-04-google-deepmind-brain-drain-shazeer-jumper-zh"
---

Google Gemini 3.5 Pro 的故事，已演變得比最初報道的更為戲劇性。本月初以「標準品質檢查」為由的一紙延期公告，如今揭露了一個規模遠超預期的決定：Google DeepMind 在距原訂部署僅剩數天之際，徹底放棄了現有的 Gemini 3.5 Pro 架構，從零啟動全新的預訓練流程。新的目標發布日期是 7 月 17 日。

## 原有架構究竟出了什麼問題

根據多位知情人士的說法，DeepMind 工程師得出結論：基於 2.5 Pro 基礎架構訓練的 Gemini 3.5 模型已觸及無法透過微調或後訓練介入加以解決的性能上限。兩個能力領域被認定為關鍵失效點：

**多步驟數學推理**：模型在複雜的鏈式數學推導上表現持續不佳——這類需要多階段延伸論證的問題，是前沿模型在學術、工程和科學情境中的核心應用場景。內部基準測試據報顯示，模型在長程推理鏈上出現性能退化，以後訓練無法修補的方式在中間步驟中迷失方向。

**SVG 場景生成**：模型在生成準確、結構良好的可縮放向量圖形方面表現欠佳。隨著企業日益將 AI 用於 UI 設計、數據可視化和技術圖表生成，這一能力的重要性持續上升。DeepMind 的評估認為，模型在 SVG 任務上的表現，相較於 OpenAI 的 GPT-5.6 和 Anthropic 的 Fable 5 缺乏競爭力，即便在同等或更高成本下亦然。

DeepMind 選擇了主動放棄——寧可重來，也不願發布一個帶有已知缺陷的模型，更不願冒著出現「基準測試與實際表現脫節」的公眾信任危機——類似的問題已讓多個競爭對手付出代價。

## 這次轉向的規模

徹底放棄一個接近部署就緒的基礎模型並啟動全新預訓練，並非尋常的工程決策。前沿級模型的預訓練耗費數千萬乃至數億美元的算力，根據叢集規模不同需要數週乃至數月的實際時間，且模型架構決策一旦確定便難以在訓練進行中途逆轉。

有知情人士描述，這個決定發生在「距原訂部署僅剩數天」之際，暗示 DeepMind 的內部評估流程直到後期測試才發現關鍵缺陷——可能是因為模型的真實性能上限只有在通過全面保留評估集測試後才完全顯現，也可能是因為競爭情報——關於 GPT-5.6 實際能力的資訊——在最後關頭重置了 DeepMind 的性能門檻。

Sundar Pichai 在 Google I/O 主題演講中曾將 Gemini 3.5 Pro 定義為「下個月」就會推出的產品，讓這個項目背負了一個公開承諾，如今的架構廢棄決定讓乾淨收場的代價大幅提高。

## 重建後架構的規格

重建版 Gemini 3.5 Pro 不僅針對廢棄版本的短板，還加入了 DeepMind 定位為競爭差異化優勢的新功能：

- **200 萬 Token 上下文視窗**：遠大於 Gemini 2.5 Pro 提供的 100 萬 Token 上下文，專為容納完整的企業程式碼庫、長文本文件分析和延伸研究工作流程而設計
- **Deep Think 推理層**：針對複雜問題求解的深度思考能力——對 Gemini 2.5 Pro 中引入的 Deep Think 模式進行精進，在高難度問題上選擇性地應用延伸推理時間，而非均一分配，從而降低日常查詢的成本
- **自主工作流程能力**：使 Gemini 3.5 Pro 與 OpenAI 和 Anthropic 自 2026 年初以來持續推出的代理式執行功能接軌

## 人才流失的背景

架構決策並非孤立事件。DeepMind 過去幾週接連流失了多位資深研究人員，包括兩位在 Gemini 多模態架構上發揮關鍵作用的人物，以及一位曾參與推理擴展流程的高級研究員。這些離職事件在本週早些時候已有報道，並引發外界對 DeepMind 內部人才儲備能否維持前沿研發節奏的質疑。

架構廢棄與人才流失並置，即便兩者在因果關係上尚無定論，也為 Google 製造了形象上的困境。從外部視角看，一家將旗艦模型延期、又徹底廢棄架構、同時流失核心研究人員的公司，很容易被解讀為內部陷入動盪——無論完全重啟是否恰恰是策略上最正確的選擇。

## 7 月 17 日意味著什麼

7 月 17 日這個目標日期，距離 DeepSeek V4 API 遷移截止日（7 月 24 日）僅差七天——在這個短暫的視窗期內，正在評估中國模型替代方案的開發者，同時也會評估重建版 Gemini 3.5 Pro 是否改變了他們的選擇。這個時機的重疊，在 DeepMind 的發布規劃中幾乎不會是偶然的。

如果重建版 Gemini 3.5 Pro 兌現其規格承諾——尤其是 200 萬 Token 上下文視窗和改進後的數學推理能力——它將有意義地縮短 Google 與當前領先者在企業買家最關心的任務上的差距。問題在於：一個在過去兩週經歷了史無前例架構重啟的模型，是否已準備好迎接主流實驗室旗艦發布所帶來的一切審視。

7 月 17 日將告訴我們：重啟決定，究竟是「以快制勝的遠見」，還是「人造出來的自信心」。
