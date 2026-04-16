---
title: "OpenAI 七年首度開源：gpt-oss 挑戰 Meta Llama 霸主地位"
summary: "OpenAI 發布兩款開放權重模型 gpt-oss-20b 與 gpt-oss-120b，採用 Apache 2.0 授權，終結長達七年的開源缺席。這兩款模型針對 AI 代理工作流程最佳化，直接與 Meta Llama 系列在效能與授權彈性上一較高下。"
category: "ai-ml"
publishedAt: 2026-04-05T10:15:00Z
lang: "zh"
featured: true
trending: true
sources:
  - name: "OpenAI 官方部落格"
    url: "https://openai.com/index/introducing-gpt-oss/"
  - name: "VentureBeat"
    url: "https://venturebeat.com/ai/openai-returns-to-open-source-roots-with-new-models-gpt-oss-120b-and-gpt-oss-20b"
  - name: "Hugging Face 部落格"
    url: "https://huggingface.co/blog/welcome-openai-gpt-oss"
tags:
  - "openai"
  - "開源"
  - "大型語言模型"
  - "apache-2.0"
  - "混合專家架構"
  - "llama"
relatedSlugs:
  - "2026-04-05-google-turboquant-kv-cache-zh"
  - "2026-04-05-noah-labs-fda-voice-heart-failure-zh"
---

距離 2019 年發布 GPT-2 以來，OpenAI 沉寂了整整七年，終於再度投身開源社群。2026 年 4 月 4 日，該公司發布兩款完全開放權重的模型 `gpt-oss-20b` 與 `gpt-oss-120b`，採用 Apache 2.0 授權——這是軟體業最寬鬆的開源授權之一。對於一家以「Open」冠名、卻逐漸走向封閉 API 的公司而言，這次發布代表著一次戲劇性的路線轉彎。

## 模型規格一覽

`gpt-oss-120b` 採用混合專家（MoE）架構，總參數量達 1170 億，但每次推論僅啟動約 51 億個參數，運算成本遠低於同等規模的密集模型。較小的 `gpt-oss-20b` 總參數量為 210 億，每次推論啟動約 36 億個參數。

本次初版為純文字模型，不具備多模態能力。OpenAI 將這兩款模型定位為**代理工作流程**的專屬工具，涵蓋工具呼叫（網頁搜尋、Python 程式執行）、長鏈多輪推理及指令遵循。模型原生支援 OpenAI Responses API，讓開發者幾乎不需修改程式碼，就能在開放模型與 GPT-4o/o3 等閉源端點之間自由切換。

模型同步上架 Hugging Face，並獲得 AWS、Azure、Together AI、Vercel、Cloudflare 及 Databricks 的部署整合支援。透過 Ollama 相容性，任何擁有現代筆電的開發者都能在本機直接執行 `gpt-oss-20b`，無需依賴雲端服務。

## Apache 2.0：今年 AI 界最大膽的授權選擇

授權選擇本身就是一項聲明。Meta 的 Llama 系列雖號稱「開放」，卻採用自訂授權，對月活躍用戶超過 7 億的商業應用另設條款。OpenAI 這次則走得更遠——Apache 2.0 允許不受限制的商業使用、微調、重新發布，乃至整合進專有產品。

這正是支撐 Linux 核心衍生版本與眾多企業級開源專案的授權框架。Hugging Face 執行長 Clem Delangue 稱此次發布為「生態系統的里程碑時刻」，並指出由具備頂尖安全研究能力的實驗室在此授權下承諾開放權重，從根本改變了業界對「開放」的基本預期。

## 此刻開源，背後邏輯為何？

OpenAI 此番轉向，有其清晰的競爭邏輯。2025 年開源模型爆炸性發展：Meta Llama 3.1 405B 的評測成績與 GPT-4 時代的封閉模型不相上下；Google Gemma 2 27B 成為熱門的微調基底；Mistral、Qwen、DeepSeek 等一長串開源模型，讓開發者有了脫離 OpenAI API 的真實選擇。

這些替代方案帶來更高自主性、更低成本，且無廠商鎖定疑慮。以往最忠誠的 OpenAI 開發者群體，開始將推論工作負載遷移至開放架構。

與此同時，OpenAI 長期面臨監管機構、前員工及 AI 安全社群對其偏離非營利使命的批評。開放模型的發布，既是商業競爭之舉，也是形象修復的動作——讓公司名稱中的「Open」再度名副其實。

更深層的戰略考量在於：OpenAI 的 API 層服務（微調、安全評估、Responses API、企業工具）貢獻大量營收。開放基礎模型能作為這整套服務的流量入口——當開發者發現在 `gpt-oss-120b` 上微調後，透過 OpenAI 託管基礎設施部署比自行運營更省心時，自然會回流至付費生態。

## 評測表現：具備競爭力，但未達前沿

OpenAI 公布的評估結果顯示，`gpt-oss-120b` 在 MMLU、GPQA-Diamond 及 LiveCodeBench 上超越 Llama 3.1 405B，並在多項程式碼評測上與 DeepSeek-V3 互有勝負。模型發布數小時內，Hugging Face 開放 LLM 排行榜的獨立評估大致印證了 OpenAI 公布的數字。

不過，這些模型與 OpenAI 自家前沿產品仍有落差。`gpt-oss-120b` 不及 GPT-4o，更遠遜於 o3。OpenAI 對此立場坦率：這不是頂尖系統的蒸餾版，而是為實際可用性與合理部署成本打造的開放模型。

對台灣開發者而言，`gpt-oss-20b` 尤具吸引力——每次推論僅啟動 36 億個參數，可在單張 A100 GPU 上流暢運行，早期測試者回報其工具呼叫與結構化輸出的可靠性，明顯優於同等算力的過往開源模型。

## Llama 正面對決

Meta 在數週前才發布 Llama 4 Scout，在開源生態中樹立了新的效率標竿。OpenAI 的加入，讓開發者終於有了來自不同安全研究哲學、不同微調方法論實驗室的直接比較對象。

兩大廠都有充分動機持續釋出開放模型：Meta 需要獨立於消費端 App 之外維持開發者平台影響力；OpenAI 則要奪回話語權並為 API 生態建立流量入口。真正的受益者是開發社群——手中握有的優質開源模型選擇又多了一個。

## 下一步展望

OpenAI 表示多模態版本（支援圖像與音訊）已在開發路線圖上，但未給出時程。公司也暗示將推出結構化微調計畫，讓企業提交領域專屬資料以獲得客製化變體，且微調後的模型權重仍將維持 Apache 2.0 授權。

目前看來，這次發布印證了業界日益成形的共識：AI 能力的前沿正逐漸與開放性的前沿分離，聰明的實驗室可以同時在兩個維度上競爭，而不必以一換一。OpenAI 能否維持這項承諾，還是終將在競爭壓力下再度走回封閉，是未來十二個月最值得觀察的問題。
