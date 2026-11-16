---
category: developer-tools
faqs:
- answer: Uno Platform 7.0 讓所有目標平台統一透過 SkiaSharp 4 渲染，新增實驗性 WebGPU 後端與 Apple TV 支援，並首日支援
    .NET 11。同時移除原生渲染與 Mac Catalyst。
  question: Uno Platform 7.0 最重要的改變是什麼？
- answer: Uno 團隊表示，7.0 的中位數效能約為 6.7 版的兩倍、體積小五倍，筆刷建立等部分操作最多快 38 倍。不過這些是廠商自行測試的數據，並未公開詳細的工作負載。
  question: Uno Platform 7.0 實際快了多少？
- answer: 根據團隊測試，WebGPU 後端依場景最多可提升 50% 影格率，純 WebGPU 的應用在 WebAssembly 版本中可減少約 6 MB
    未壓縮的原生程式碼。開發者也能透過新的 WebGpuCanvasElement，在 UI 中直接下達自己的 WebGPU 指令。
  question: WebGPU 後端對 .NET 開發者有什麼意義？
featured: false
lang: zh
publishedAt: '2026-11-16T09:00:00+00:00'
relatedSlugs: []
safeForPublic: true
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/Uno-Platform-6-7-targets/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: Uno Platform 7.0 全面押注 Skia 與 WebGPU，正式捨棄原生渲染。跨平台 .NET 開發的路線已經確定：寧可犧牲原生手感，也要換取各平台一致的呈現。
tags:
- developer-tools
- open-source
title: Uno Platform 7.0 新增 WebGPU 後端，支援 Apple TV 與 Reactor，並全面淘汰原生渲染
trending: false
type: news
---

Uno Platform 7.0 全面押注 Skia 與 WebGPU，正式捨棄原生渲染。跨平台 .NET 開發的路線已經確定：寧可犧牲原生手感，也要換取各平台一致的呈現。

## 重點

- 所有平台改走同一條以 SkiaSharp 4 為核心的渲染管線，另有實驗性的 WebGPU 後端；原生渲染與 Mac Catalyst 一併移除。
- 官方說 7.0 的中位數效能約是 6.7 的兩倍、體積小五倍，但這是廠商自己的測試，沒有公開詳細的工作負載。
- WebGPU 依場景最多可提升 50% 影格率，WebAssembly 版本也能少掉約 6 MB 的原生程式碼。
- 新增 Apple TV 平台、.NET 11 首日支援，Microsoft.UI.Reactor 和第三方 MAUI 控制項也能在所有平台使用。
- Uno 與微軟 .NET 團隊共同維護 SkiaSharp，在 .NET UI 生態系的位置越來越核心。

## 為什麼值得注意

Uno 7.0 最大膽的決定是砍掉原生渲染。Flutter 早就證明自己掌控每個像素比包裝原生元件更好用，.NET 陣營總算照著這個教訓做了。

## 資料來源

- [InfoQ](https://www.infoq.com/news/2026/11/Uno-Platform-6-7-targets/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)