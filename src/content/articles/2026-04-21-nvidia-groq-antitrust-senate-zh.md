---
title: "Nvidia 200 億美元 Groq 交易遭參議院與 FTC 調查——這是偽裝的收購嗎？"
summary: "Nvidia 去年 12 月以 200 億美元與 AI 推理新創 Groq 達成協議，結構為技術授權加上大量招募 Groq 核心工程師，如今遭到參議院調查與 FTC 審查。Warren、Blumenthal 和 Wyden 等議員主張，此安排是刻意規避反壟斷審查的隱性收購，旨在消滅競爭對手並鞏固 Nvidia 在 GPU 市場 90% 的主導地位。"
category: "policy"
publishedAt: 2026-04-21
lang: "zh"
featured: false
trending: true
sources:
  - name: "U.S. Senator Elizabeth Warren（新聞稿）"
    url: "https://www.warren.senate.gov/newsroom/press-releases/warren-blumenthal-question-whether-nvidias-20-billion-groq-deal-is-attempt-to-avoid-antitrust-laws"
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-03-20/nvidia-s-20-billion-groq-deal-queried-by-warren-blumenthal"
  - name: "CNBC"
    url: "https://www.cnbc.com/2025/12/24/nvidia-buying-ai-chip-startup-groq-for-about-20-billion-biggest-deal.html"
  - name: "IntuitionLabs"
    url: "https://intuitionlabs.ai/articles/nvidia-groq-ai-inference-deal"
tags:
  - "nvidia"
  - "groq"
  - "反壟斷"
  - "參議院"
  - "ftc"
  - "ai晶片"
  - "監管"
relatedSlugs:
  - "2026-04-16-asml-q1-2026-earnings-china-zh"
  - "2026-04-13-us-match-act-duv-chip-export-ban-zh"
  - "2026-04-05-match-act-chip-policy-zh"
---

2025 年聖誕夜，Nvidia 宣布與 AI 推理新創 Groq 達成一項「非獨家技術授權協議」。Groq 的語言處理器（LPU）晶片是市場上速度最快的公開推理硬體，代價是 200 億美元——Nvidia 史上最大規模的交易。Groq 創辦人兼執行長 Jonathan Ross 及大批資深工程師同步加入 Nvidia。Groq 的辦公室繼續開著；部分核心業務仍在運作。在技術定義上，這不是一次收購。

四個月後，這個「技術上的差異」已成為半導體產業史上最具影響力的反壟斷紛爭的核心。

## Nvidia 買到了什麼——以及它沒有承認買到了什麼

要理解這筆交易為何引發如此巨大的監管反彈，必須先理解 Groq 究竟建造了什麼。與 Nvidia 通用 GPU 不同——後者功能強大，但在純推理工作負載上相對昂貴且耗電——Groq 的 LPU 從架構層面專為一個任務而生：在用戶互動時快速、高效地運行已訓練好的 AI 模型。

LPU 在推理速度上的表現，對許多模型規模和架構而言，在每瓦吞吐量上比 Nvidia H100 和 H200 高出三至五倍。對於每月花費數千萬美元購買推理算力的大規模 AI 應用提供商而言，這樣的效率差距意味著實質的成本優勢。2025 年底，OpenAI 據報正在評估 Groq 晶片，以替代 Nvidia 處理特定類別的推理工作負載。

根據多方描述，OpenAI 與 Groq 之間的這些討論，在 Nvidia 授權協議宣布後數週內即告中斷。最深刻理解 LPU 架構的 Jonathan Ross 和工程師們，此時已是 Nvidia 的員工。

## 參議院調查

2026 年 3 月 20 日，參議員 Elizabeth Warren（麻薩諸塞州，民主黨）和 Richard Blumenthal（康乃狄克州，民主黨）致函 Nvidia 執行長 Jensen Huang，就交易結構與意圖提出尖銳質問，要求 Nvidia 在 4 月 3 日前回覆，措辭直率：「藉由授權其技術並招募最重要的員工，Nvidia 實際上已以名義之外的一切方式收購了 Groq。」

信件概述了議員們的擔憂：此交易刻意設計以規避《哈特—史考特—羅迪諾反壟斷改進法》（HSR）的申報要求——該法律要求超過特定金額的收購案向 FTC 和司法部提前申報以接受反壟斷審查。透過將交易結構定性為授權而非直接收購資產或股權，Nvidia 規避了這一審查觸發條件。

「Nvidia 已控制約 90% 的 GPU 市場——這些高端晶片用於開發和部署 AI，」議員們寫道。「Groq 專精於開發比 Nvidia 更節能的推理晶片。」議員們主張，此次合併在可行的 Nvidia GPU 替代方案剛開始浮現之際扼殺了競爭。

隨後，Warren、Wyden（俄勒岡州）和 Blumenthal 聯名致函聯邦監管機構，要求對他們所稱的「反向人才收購」模式展開更廣泛調查——他們認為這種模式正在 AI 產業中浮現：主導企業在不觸發收購審查門檻的前提下，透過購買技術和人才來消滅潛在競爭對手。

## FTC 的立場

美國聯邦貿易委員會（FTC）一直在監測這筆交易。接近程序的消息人士表示，FTC 科技執法團隊正在審查 Nvidia-Groq 安排是否應在機構實質授權下被重新定性為收購，儘管其名義上是授權合約。

關鍵的法律測試是功能性的：若 Nvidia 實際取得了所有權的實質等價物——對技術的獨家或近獨家控制，以及開發和延伸技術所必需的人力資本——反壟斷監管機構歷來主張形式不應決定實質。授權的非獨家性質為 Nvidia 提供了一定掩護，因為 Groq 技術上保有將 LPU 技術授權給其他方的權利。但若能執行此類授權的工程師已全部加入 Nvidia，非獨家性可能更多是形式而非實質。

若 FTC 將此交易重新定性為應申報的收購，Nvidia 可能面臨一系列補救措施，包括強制剝離授權、要求歸還 Groq 技術人員的解散令，或鉅額民事罰款。

## Nvidia 的辯護

Nvidia 堅持這是合法的授權協議，強調其非獨家性質，並對 Groq 消除了實質競爭的定性提出異議。公司發言人指出，Groq 作為法律實體仍繼續運作，其 LPU 技術仍可授權，而對人才的收攬是競爭激烈市場的標準做法。

Jensen Huang 在協議宣布後的公開場合，將 Nvidia 的推理策略定位為平台擴展——主張通過融入 LPU 設計理念改進其路線圖，是為客戶提升成果，而非限制競爭。

## 更廣泛的賭注

Nvidia-Groq 事件並非孤立案例。它處於 2026 年數股碰撞力量的交匯點：AI 產業中少數公司已達到驚人的市場集中度；AI 政策已成為政治一線議題的環境；以及被要求將 20 世紀框架應用於 21 世紀市場結構的反壟斷執法機構。

FTC 審查的結果將超越 Nvidia 本身產生影響。若監管機構確立超過一定金額的「人才加授權」交易需要 HSR 申報，將從根本上約束主導 AI 公司收購潛在競爭對手的方式——而在矽谷，「人才收購」安排長期以來都是吸收潛在競爭對手的標準工具。

對 Groq 的前競爭者和客戶而言，無論監管機構最終如何裁決，訊息已然清晰：建立足夠差異化的 AI 基礎設施產品，如今承擔著被那些最受益於其不作為獨立企業的公司吸收的風險。這種動態是否構成反壟斷違規，是 FTC 乃至法院必須回答的問題。

聽審仍在進行中。Nvidia 對參議院信函的回覆，以及 FTC 的下一步行動，預計將在未來數週內揭曉。
