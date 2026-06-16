---
title: "美國政府強制 Anthropic 下線：Claude Fable 5 出口管制風波始末"
summary: "2026年6月12日，美國政府援引國家安全出口管制條例，強制 Anthropic 在全球範圍內關閉 Claude Fable 5 與 Mythos 5。事件導火線是一名研究員公開的越獄技術，此舉震撼整個 AI 產業，企業用戶措手不及，也為 AI 模型部署的國安風險敲響了警鐘。"
category: "policy"
publishedAt: 2026-06-16
lang: "zh"
featured: false
trending: true
sources:
  - name: "Anthropic 官方聲明"
    url: "https://www.anthropic.com/news/fable-mythos-access"
  - name: "MarkTechPost — Anthropic 關閉 Fable 5 與 Mythos 5"
    url: "https://www.marktechpost.com/2026/06/13/anthropic-disables-claude-fable-5-and-mythos-5-after-us-government-order/"
  - name: "TechTimes — Fable 5 越獄風波"
    url: "https://www.techtimes.com/articles/318268/20260612/claude-fable-5-hit-jailbreak-claims-secret-sabotage-backlash-days-after-launch.htm"
  - name: "VentureBeat — 企業應對指南"
    url: "https://venturebeat.com/technology/anthropic-blocks-all-public-access-to-claude-fable-5-mythos-5-following-us-government-order-what-enterprises-should-do"
  - name: "Snyk — 資安啟示"
    url: "https://snyk.io/blog/fable-mythos-suspension-security-takeaways/"
tags:
  - "Anthropic"
  - "Fable 5"
  - "出口管制"
  - "AI 安全"
  - "越獄"
  - "國家安全"
relatedSlugs:
  - "2026-06-14-anthropic-overtakes-openai-aws-5gw-compute-deal-zh"
  - "2026-06-15-white-house-ai-innovation-security-executive-order-zh"
  - "2026-06-15-great-american-ai-act-federal-framework-zh"
---

2026年6月9日，Anthropic 正式推出 Claude Fable 5 與 Mythos 5，這是該公司迄今為止最強大的模型，也是多年「安全優先」研究路線與數十億美元投入的成果結晶。然而，僅僅七十二小時後，兩款模型全面下線。不是因為技術漏洞，不是因為商業決策，而是因為美國政府的一紙命令。

從6月9日到6月12日這短短三天，已成為2026年 AI 政策領域最具衝擊力的事件，為整個產業揭示了一個殘酷現實：前沿模型的商業部署，隨時可能與國家安全官僚體系正面相撞。

## 從發布到下線的七十二小時

Fable 5 甚至還來不及在各大基準測試中累積成績，6月10日，一名自稱「Pliny the Liberator」的研究員便在 X 上公開了詳細的越獄方法。技術手段結合了多代理分解、Unicode 替換與敘事框架操縱，成功繞過模型的安全分類器。

在貼文中，Pliny 聲稱已提取出涵蓋網路漏洞利用、爆炸物合成與化學品製造路徑的功能性指令，並在 GitHub 上公開了 Fable 5 長達十二萬字元的系統提示詞，讓任何人都能取閱。

資安社群的反應兩極。部分研究人員認為此說法誇大其詞；另一些人則指出，同樣的底層資訊在其他已公開部署的模型中無需任何繞過即可取得，質疑為何唯獨 Fable 5 要受到緊急處置。

然而事態已無法挽回。系統提示詞在 GitHub 上廣為流傳，相關報導鋪天蓋地。

6月12日東部時間下午5時21分，Anthropic 收到美國政府援引國家安全出口管制條例發出的指令：暫停任何外國公民對 Fable 5 與 Mythos 5 的一切訪問，無論其身處美國境內或境外。由於 Anthropic 無法即時核實所有全球用戶的公民身份，合規之路只剩一個選項——對所有用戶一律關閉兩款模型。

Anthropic 在官方聲明中寫道：「此命令的實際效果是，我們必須緊急對所有客戶停用 Fable 5 與 Mythos 5，以確保合規。」

## Anthropic 的謹慎反擊

Anthropic 的官方聲明值得細讀，它揭示了公司與華府關係在這個關鍵時刻的微妙張力——法律上服從，立場上不認同。

Anthropic 明確將 Pliny 的演示定性為「局部越獄漏洞」而非系統性缺陷，並指出競爭對手的已部署模型中同樣可取得相當的資訊。公司的「縱深防禦」策略，他們認為，已將風險降低至「與業界已部署模型相當」的水準。若一致地援引對 Fable 5 動用的標準，Anthropic 警告，「實際上將導致所有新模型的部署停頓」。

這最後一句話，形同一記警示。若任何公開的越獄演示——無論多麼侷限——都能觸發美國政府的出口管制機制，那麼每家前沿 AI 實驗室在每次新模型上線前都將面臨同樣的風險。

## 企業的連鎖衝擊

突如其來的下線事件暴露了企業 AI 團隊長期忽視的風險：模型可用性作為營運風險變數。

在開發者論壇和企業內部群組裡，48小時內充斥著沮喪與反省之聲。正在生產環境中使用 Claude API 的團隊——法律研究、程式生成、客服系統、文件分析——毫無預警。雖然 Anthropic 的其他模型（Opus 4.8、Sonnet 4.6 等）維持正常運作，但 Fable 5 特有的能力組合，使部分企業應用場景難以找到直接替代方案。

這次事件正在加速一個 AI 基礎架構團隊長期迴避的對話：供應商集中風險。將所有 AI 能力押注於單一供應商，即便是 Anthropic 這樣強大的廠商，都將製造一個可能因完全超出企業控制的因素而觸發的單點故障。資安團隊現在開始在 AI 供應商評估框架中，將「模型可用性」與服務水準協議、資料駐留要求並列考量。

## 用洩露的程式碼「復活」模型

事件在數日內出現了更奇詭的後記。開發者 Jamieson O'Reilly 發表了概念驗證，示範只需一行程式碼即可「復活」Fable 5——將洩露的十二萬字元系統提示詞注入 Opus 4.8 的 API 呼叫，便能從公開元件中重建 Fable 5 功能特性的近似版本。

這一示範揭示了政府干預的侷限性。系統提示詞在 GitHub 上公開可得，相關技術已有文件記錄，支撐 Fable 5 獨特行為的底層模型能力依然可透過其他途徑取用。關閉 API 端點阻斷了商業存取，卻無法將能力從世界上抹除。

## 更深層的政策困境

Fable 5 的下線事件，恰恰落在一批並非為 AI 設計的政策框架的尷尬交叉點。出口管制法為有形商品和具有明確來源地的特定兩用技術而設計。將其套用於雲端 AI 服務——「出口」發生在每一次 API 呼叫，而越獄技術在幾分鐘內透過社群媒體擴散至全球——已使這套框架面臨監管機構與業界均未充分應對的挑戰。

美國政府至今未公開說明援引了哪項具體授權、觸發關閉命令的越獄嚴重性門檻在哪裡，以及 Fable 5 重新上線的條件是什麼。Anthropic 表示正在積極尋求解決方案，但未提供時間表。

此事件的意義，不僅在於這次具體事故本身，更在於它確立的先例：美國政府已展示其能力與意願，在安全研究員公開披露的數小時內，強制前沿 AI 實驗室將模型下線。這種權力未來是否會被一致、相稱、透明地行使，還是 Fable 5 只是一場一次性的政治過度反應——這是整個產業在下一次產品發布前急需得到答案的問題。

Fable 5 原本應標誌著 Anthropic 在對抗 OpenAI 與 Google 競爭中最自信的一步。最終，它成了一個關於「AI 競爭有多大程度在華府而非基準測試排行榜上決出勝負」的最佳詮釋。

---

*截至2026年6月16日，Fable 5 與 Mythos 5 仍處於下線狀態。Anthropic 其他所有模型維持正常運作。*
