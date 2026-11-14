---
category: developer-tools
faqs:
- answer: 它在 Isaac Sim 中使用 UR17G 手臂、Robotiq 夾爪與 SimReady 物件資產建立飲料罐抓取放置場景。流程包含檢查資產行為，並以代理生成的控制指令執行任務。
  question: 這份教學實際完成了什麼？
- answer: SimReady 資產已配置質量、碰撞、關節與驅動等物理和控制屬性。開發者能直接重用較完整的模擬設定，不必為每個下載模型重新從頭配置。
  question: SimReady 對機器人開發者有何實際價值？
- answer: 教學證明資產與控制流程能在模擬環境運作，但沒有證明相同行為可穩定轉移至實體硬體。真實世界驗證、跨模擬器一致性及更多任務覆蓋仍是後續關鍵。
  question: 這場示範還沒有證明哪些事情？
featured: false
lang: zh
publishedAt: '2026-11-13T18:00:39+00:00'
relatedSlugs: []
safeForPublic: true
sources:
- name: Hugging Face Blog
  url: https://huggingface.co/blog/nvidia/simready-assets-robot-pick-and-place
summary: SimReady 真正的突破，不在於又多展示了一個機器人範例，而是提供可重複使用的模擬資產，讓機器人實驗更快速、更穩定可靠。
tags:
- developer-tools
- open-source
- ai-ml
title: 運用 SimReady 資產打造機器人取放模擬
trending: false
type: news
---

SimReady 真正的突破，不在於又多展示了一個機器人範例，而是提供可重複使用的模擬資產，讓機器人實驗更快速、更穩定可靠。

## 重點

- 教學在 Isaac Sim 中組合 UR17G 機械手臂、Robotiq 夾爪與飲料罐，並以代理生成的控制指令完成抓取與放置任務。
- SimReady 資產不只是外觀模型，還預先加入碰撞、質量、關節及關節驅動等模擬所需屬性。
- Hugging Face 上的 SimReady Central 提供開放的機器人與物件資產庫，並附上設定檔驗證依據，方便重用及檢查。
- SimReady Foundation 以設定檔、功能和可驗證需求建立相容性規格，讓資產製作者與模擬使用者有更明確的共同標準。
- 標準化資產有望減少反覆整理模擬場景的工程成本，但這篇教學只證明模擬流程，尚未展示成果能否轉移到實體機器人。

## 為什麼值得注意

機器人人工智慧最缺的未必是更炫的代理，而是那些看似無聊、卻經過驗證的資產，讓團隊不必每次都重做質量、碰撞與關節設定。

## 資料來源

- [Hugging Face Blog](https://huggingface.co/blog/nvidia/simready-assets-robot-pick-and-place)