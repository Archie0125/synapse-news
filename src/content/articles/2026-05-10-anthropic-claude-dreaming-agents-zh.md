---
title: "Anthropic 讓 AI 代理學會「作夢」——在睡眠中從自身錯誤汲取教訓"
summary: "Anthropic 推出「dreaming（作夢）」功能，讓 Claude Managed Agents 能在背景自動回顧過去的工作階段、提取規律、並悄悄升級記憶庫——無需人工重新訓練。此功能目前以開發者預覽版形式開放，支援 Claude Opus 4.7 與 Sonnet 4.6，法律 AI 公司 Harvey 啟用後，任務完成率提升約 6 倍。"
category: "developer-tools"
publishedAt: 2026-05-10
lang: "zh"
featured: true
trending: false
sources:
  - name: "Anthropic 部落格"
    url: "https://claude.com/blog/new-in-claude-managed-agents"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/anthropic-introduces-dreaming-a-system-that-lets-ai-agents-learn-from-their-own-mistakes"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/05/06/anthropic-letting-claude-agents-dream-dont-sleep-job/"
  - name: "9to5Mac"
    url: "https://9to5mac.com/2026/05/07/anthropic-updates-claude-managed-agents-with-three-new-features/"
tags:
  - "Anthropic"
  - "Claude"
  - "AI代理"
  - "代理AI"
  - "記憶"
  - "開發工具"
  - "Claude Managed Agents"
relatedSlugs:
  - "2026-04-10-anthropic-claude-managed-agents-en"
  - "2026-05-07-anthropic-44b-arr-claude-code-growth-en"
  - "2026-05-06-anthropic-enterprise-ai-jv-wall-street-en"
---

Anthropic 於 2026 年 5 月 6 日推出一項名為「dreaming（作夢）」的新功能——一套排程背景程序，讓 Claude 代理得以回顧自身的過去工作，跨工作階段找出規律，並在無需任何人工撰寫訓練資料的情況下，自動精煉記憶庫。這是 Anthropic Managed Agents 平台自推出以來最重要的更新之一，也宣示了一個更廣泛的產業方向：AI 代理的下一個疆界，不再只是原始能力的提升，而是能否在時間推移中自主進步。

## 「作夢」究竟在做什麼？

這個隱喻是刻意選用的。人類的睡眠會鞏固記憶、修剪冗餘資訊、並把一天裡潛藏的關聯浮現出來。Anthropic 的 dreaming 系統試圖為 AI 代理複製這個類比過程。

當一次 dreaming 工作階段執行時，Claude 代理會分析自己過去的工作紀錄——單次最多 100 個工作階段——以及現有的記憶庫。系統會尋找反覆出現的規律：在不同任務中重複犯下的錯誤、多個代理獨立收斂至的工作流程，以及在整個團隊中持續出現的偏好或限制條件。根據這些分析，系統會重新整理代理的記憶：合併重複項目、刪除過時條目、並將最有用的知識提升至顯著位置。

重要的是，原始工作階段資料不會被修改。Dreaming 在副本上運作，開發者可以選擇讓更新自動套用，或者在任何變更生效前先進行人工審查。這項設計對企業部署至關重要——因為代理行為的意外改變，可能會在數千個自動化工作流程中產生連鎖效應。

整個過程視資料量而定，需時數分鐘。開發者還可提供明確指示——例如要求 dreaming 工作階段優先處理與程式碼相關的規律，同時忽略不代表日常行為的一次性除錯互動。

## Dreaming 解決了什麼問題？

迄今為止，AI 代理記憶系統面臨一個根本性瓶頸：個別代理工作階段只能根據當次工作階段所學到的東西來更新記憶，卻無法看見只有在數十乃至數百個工作階段中才會浮現的規律——例如某個企業客戶的用戶始終偏好更緊湊的 JSON 結構，或是某個特定工作流程步驟在特定條件下失敗率異常偏高。

這個限制意味著，代理進步的速度，取決於人類能多快觀察到失敗、將教訓編碼、並重新部署更新後的配置。在大規模企業部署中，這個反饋循環太慢、也太耗費人力，根本跟不上代理遭遇新邊緣案例的速度。

Dreaming 自動打通這個循環。代理實質上成為了自己的品質工程師——觀察自己的輸出結果、找出薄弱環節、並在毋需等待人類介入的情況下主動改善。

「Dreaming 能浮現單一代理工作階段看不見的規律，」Anthropic 在產品公告中寫道。「包括反覆出現的錯誤、代理獨立收斂至的工作流程，以及在整個團隊中共享的偏好。」

## 早期成果令人印象深刻

目前最具體的成效來自 Harvey——Anthropic 最重要的企業合作夥伴之一，專注於法律 AI 領域。Harvey 在其由 Claude 驅動的法律研究與文件起草工作流程中啟用 dreaming 功能後，回報任務完成率提升了約 **6 倍**。

這個幅度值得細思。6 倍的任務完成率提升，並不意味著代理的速度加快了六倍，而是代表代理能在不依賴大量人工監督的情況下，以此前無法達到的比例，將複雜的多步驟任務完成至令人滿意的標準。對於法律工作而言，這意味著代理正在學習套用客戶律所的特定慣例、判例偏好和文件標準，而無需針對每種新案件類型重新設定程式。

Anthropic 謹慎地將此定位為研究預覽版而非正式功能，Harvey 的成果也僅代表單一高流量部署的結果。在其他情境下，效果會因代理工作階段量、任務多樣性，以及初始記憶配置的品質而有所不同。

## 三個功能，一個方向

Dreaming 是 Claude Managed Agents 一次更廣泛更新的一部分，同時還包含另外兩項重要新功能。

第一是**成果記錄（outcomes）**——讓開發者能依照結構化分類法記錄代理任務的結果，為代理（以及 Anthropic 的平台）提供哪些工作流程產出了可接受結果、哪些未能達標的反饋信號。成果資料會進入 dreaming 流程，使記憶整合能加重對成功工作階段的權重。

第二是擴充版**多代理協作（multi-agent orchestration）**功能，允許主要 Claude 代理在執行複雜任務時動態生成並協調子代理。協作層現在更加穩健，更好地支援代理層次間的狀態與情境傳遞，並能在子代理失敗時，無需重啟整個工作流程。

三項功能合在一起，構成一套連貫的架構：能夠分派任務（協作）、接收反饋（成果記錄）、並內化教訓（dreaming）的代理系統。Anthropic 的產品路線圖看來正在朝一個方向構建：讓 Claude Managed Agents 不只是任務執行層，而是一套在組織內部署時間越長、就越有價值的自我改善系統。

## 企業的疑慮：這是把雙面刃

並非所有人都感到振奮。一篇廣泛流傳的 VentureBeat 分析指出，Anthropic 正在定位自己，以掌控企業 AI 的關鍵三要素：記憶（代理記住什麼）、評估（成果資料）、以及協作（代理如何協調）。而這三個層面，同時也是潛在的供應商綁定點。

若一家企業圍繞 Claude Managed Agents 建立工作流程、累積了數個月經 dreaming 精煉的記憶庫、並將成果記錄整合進業務指標，一旦想遷移至其他 AI 供應商，將面臨極高的摩擦成本。記憶庫是專有的，成果分類法建立在 Anthropic 的基礎設施上，協作依存關係則編碼在代理配置中。

這不必然是 Anthropic 的刻意盤算——建立深度整合進客戶工作流程的高品質基礎設施，本就是企業軟體的商業邏輯。但這也意味著，採用 Claude Managed Agents 的決策，比一項功能公告所呈現的樣子，要更加深遠。

## 開放方式與使用條件

Dreaming 目前以有限開發者存取計畫的形式提供，尚未對所有 Managed Agents 客戶開放。Anthropic 透過其開發者入口接受申請，優先考量已有高流量代理部署的團隊——因為這些環境最能發揮 dreaming 的規律辨識優勢。

成果記錄與多代理協作功能則以公開測試版形式開放，兩者均需 Claude Opus 4.7 或 Claude Sonnet 4.6。計算需求較高的 dreaming 功能，目前僅支援 Opus 4.7。

對於正在 Claude Managed Agents 上構建產品的開發者，真正的問題不是 dreaming 是否會最終進入全面開放——Anthropic 的定價策略與發展軌跡都暗示這幾乎是確定的。問題在於：自動在背景進行記憶整合的自我改善代理架構，是否符合其特定企業情境下的治理與合規要求。對於多數法律、金融與醫療健康部署而言，答案將需要仔細審查 dreaming 所產生的資料處理機制與稽核軌跡。

Anthropic 這次發布清楚傳遞了一個論點：企業 AI 代理的未來，不只是執行任務，而是學習把任務做得更好——且需要人類在改善循環間介入的頻率越來越低。這條軌跡最終帶來的是組織層面的更大槓桿，還是更深的供應商依賴，有一部分取決於企業此刻所做的決策。
