---
title: "矽片大分手：超大型雲端業者如何瓦解輝達的 AI 晶片壟斷"
summary: "Google、亞馬遜、微軟與 Meta 正部署自研 AI 加速器，意在削弱輝達在 AI 晶片領域的掌控。隨著 AI 產業重心轉向大規模推論，自研晶片正逐步攻城掠地，不過輝達仍握有約 81% 的市場。"
category: "hardware"
publishedAt: 2026-04-27
modifiedAt: 2026-11-15T00:00:00Z
lang: "zh"
featured: false
trending: true
sources:
  - name: "The Motley Fool"
    url: "https://www.fool.com/investing/2026/04/25/meet-biggest-threat-nvidia-ai-chips-its-not-amd/"
  - name: "Nerd Level Tech"
    url: "https://nerdleveltech.com/the-custom-ai-chip-race-2026-meta-google-amazon-microsoft-vs-nvidia"
  - name: "Financial Content / TokenRing"
    url: "https://markets.financialcontent.com/wral/article/tokenring-2026-1-2-the-great-decoupling-hyperscalers-accelerate-custom-silicon-to-break-nvidias-ai-stranglehold"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/inside-the-ai-accelerator-arms-race-amd-nvidia-and-hyperscalers-commit-to-annual-releases-through-the-decade"
  - name: "Intelligent Living"
    url: "https://www.intelligentliving.co/ai-accelerator-tpu-v7-trainium3-maia-200/"
tags:
  - "輝達"
  - "自研晶片"
  - "AI晶片"
  - "谷歌"
  - "亞馬遜"
  - "微軟"
  - "Meta"
  - "TPU"
  - "硬體"
relatedSlugs:
  - "2026-04-27-hyperscaler-custom-silicon-nvidia-decoupling-en"
  - "2026-04-23-google-ironwood-tpu-cloud-next-2026-zh"
  - "2026-04-15-meta-broadcom-mtia-chip-deal-zh"
---

過去四年，輝達執行長黃仁勳打造了一個科技史上前所未見的地位：幾乎獨攬整個 AI 基礎設施革命的核心硬體供應。高峰時期，輝達掌握 AI 加速器市場逾 95% 的份額，OpenAI、Anthropic、Google DeepMind、Meta AI 等各大 AI 實驗室，都將數百億美元砸進 H100 與 H200 GPU 叢集，只為訓練旗下的前沿模型。

那個時代正在走向終點。

2026 年上半年，業界正見證部分人士所稱的「矽片大分手」（Great Decoupling），全球最大科技公司紛紛部署自研晶片，以降低對輝達的依賴。Google、亞馬遜、微軟與 Meta 相繼推出自研 AI 加速器，針對當前最具經濟意義的工作負載——推論（inference）——提供遠勝 GPU 的效能與成本表現。

## 結構性轉移：訓練 vs. 推論

這場分手的根本動力，來自 AI 運算支出重心的位移。訓練一個前沿模型，需要龐大的 GPU 叢集持續運算數週乃至數月，這是輝達 H100 與 Blackwell 真正如魚得水的場域。然而，訓練是一次性成本；推論卻是永無止盡的：每一筆 ChatGPT 查詢、每一個嵌入 Google 搜尋的 Gemini 回答，都需要消耗全新的運算資源。

2025 年底，推論已佔全球 AI 運算支出的約三分之二，且隨著 AI 產品大規模普及，這一比例仍在加速攀升。更關鍵的是，推論比訓練更需要「專用化」：針對特定運算模式設計的 ASIC（特殊應用積體電路），在超大規模推論場景下，效率遠勝通用 GPU。

現實數字一目瞭然：AI 圖像生成平台 Midjourney 公開表示，將工作負載從輝達 GPU 遷移至 Google TPU 後，每月運算成本從 210 萬美元降至 70 萬美元，降幅達 65%。對每秒處理數十萬次推論請求的超大型雲端業者而言，這個比例意味著每年數十億美元的費用差距。

## 四大挑戰者與各自武器

**Google TPU v7「Ironwood」**：Google 於 11 月發表第七代 TPU Ironwood，並於 2026 年初進入一般可用階段。每顆晶片可提供 4.6 PFLOPS 的 FP8 稠密運算能力，TPU v7 規格列出 192 GiB 的 HBM 與 7,380 GiB/s 的頻寬。由 9,216 顆晶片組成的超級 Pod，可聚合至 42.5 exaFLOPS 的推論算力——達到機架層級前所未有的密度。Google 第八代 TPU 已在台積電 2nm 製程上開發中，表明 Google 的晶片路線圖已與半導體製造前沿緊密連動。

**亞馬遜 Trainium3**：亞馬遜旗下 Annapurna Labs 推出的 Trainium3，是其首款 3nm 製程自研 AI 晶片，目前已進入量產。它提供 2.52 petaFLOPS 的 MXFP8 運算能力，搭載最高 128 GB HBM3E 記憶體。最能體現其實力的佐證是：Anthropic 與 OpenAI 均宣布將訓練與推論工作負載部署在 Trainium3 實例上，為這款晶片提供了過往世代所缺乏的第三方公信力。

**微軟 Maia 200**：Maia 200 是以推論為優先的加速器，搭載 216 GB HBM3E，頻寬 7 TB/s。微軟宣稱 Maia 200 的 FP4 效能是亞馬遜 Trainium3 的三倍，FP8 效能也超越 Google TPU v7。該晶片已部署於 Azure 資料中心，與前一代系統相比，每元效能提升 30%。微軟亦已開始向特定 Azure 客戶提供 Maia 200 的推論實例。

**Meta MTIA 300 至 500 路線圖**：Meta 公布了各超大型業者中最積極的自研晶片路線圖，詳細揭示四個世代——MTIA 300、400、450 與 500——從 2026 至 2027 年陸續部署。從 MTIA 300 到 MTIA 500，HBM 頻寬提升 4.5 倍，原始算力在不到兩年內暴增 25 倍。考量到 Meta 2026 年高達 1,150 至 1,350 億美元的 AI 資本支出計畫，自研晶片佔比只會日益增加。

## 輝達的反擊：Vera Rubin 平台

輝達的應對之道是把運算密度推向新的極限。Vera Rubin 平台搭載的 Rubin 架構預計於 2026 年底推出，將導入 HBM4 記憶體與採用 Arm 架構的「Vera」CPU。在機架層級，Vera Rubin NVL144 透過 NVLink 6 串聯 144 顆 Rubin GPU，直指任何自研 ASIC 都無法比擬的超大規模訓練場景。黃仁勳估計，輝達將在 2026 至 2027 年間售出逾 1 兆美元的 Blackwell 與 Vera Rubin 晶片。

在訓練工作負載上，輝達的護城河依然深厚。歷經 17 年、無數開發者心血累積的 CUDA 生態系，賦予輝達 GPU 自研 ASIC 難以複製的通用彈性。任何新的模型架構、任何新奇的研究方向，都能以最低摩擦在輝達硬體上完成原型開發與訓練。

然而，推論的經濟邏輯是殘酷的。就能源效率而言，自研 ASIC 最高可比通用 GPU 高出 3 倍。對現代 AI 機架耗電量動輒達 130 千瓦的資料中心而言，能源效率已從偏好化為生存命題。

## 市場算術

數字描繪出輝達中期市場地位的嚴峻走向。根據市場分析師數據，AI 自研 ASIC 市場年增速達 44.6%，遠超 GPU 的 16.1%。分析師預估，自研晶片到 2028 年可能佔 AI 晶片市場總量的 45%。IDC 估計輝達仍掌控 81% 的 AI 晶片市場。

業界人士以直白語言描述這一動態：超大型業者的基礎設施團隊在內部稱之為「輝達稅」（Nvidia tax）——為並不需要的 GPU 通用彈性所支付的溢價。對固定模型架構、每天處理數千億次推論的雲端業者而言，那份彈性就是純粹的額外開銷。

## 對台灣科技產業的意義

值得關注的是，無論哪個陣營最終勝出，台積電都是這場競爭中最穩定的受益者——輝達的 Vera Rubin、Google 的 Ironwood、亞馬遜的 Trainium3 與微軟的 Maia 200，全都仰賴台積電的先進製程生產。AI 晶片軍備競賽愈激烈，台積電的訂單只會愈多。

這場大分手，並非輝達走向衰亡的故事，而是 AI 供應鏈的結構性重組：數千億美元的硬體支出，將從單一供應商分散至更廣泛的自研矽片生態系。對於在 AI 基礎設施上佈局的企業與投資者而言，誰掌控了運算的「矽」，就掌控了智慧經濟的命脈。

*更正（2026 年 11 月 15 日）：已依本頁列出的來源更正或刪除 9 處。*
