---
category: hardware
faqs:
- answer: 根據 SemiAnalysis，Kessel 是 SpaceX/xAI 以 Nvidia Vera Rubin NVL72 為基礎打造的客製化機櫃，保留
    72 顆 Rubin GPU 與 36 顆 Vera CPU，但改用 84 層 PCB 中板取代 NVLink 線纜匣。
  question: SpaceX 的 Kessel 系統是什麼？
- answer: 被動式 PCB 中板省去了笨重的線纜組件，而且只有 84 層，比 Nvidia Kyber 的 156 層更容易維持量產良率。固態互連也更適合軌道部署，因為鬆脫的線纜在太空中是可靠度風險。
  question: 用 PCB 中板取代線纜有什麼意義？
- answer: SpaceX 仍會向 Nvidia 採購 GPU，但機櫃的其他零組件改為自行採購，顯示大客戶可能開始侵蝕 Nvidia 利潤較高的整機系統生意。
  question: Kessel 對 Nvidia 有什麼影響？
featured: false
lang: zh
publishedAt: '2026-11-11T15:03:08+00:00'
relatedSlugs: []
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/artificial-intelligence/spacex-develops-its-own-kessel-rack-scale-system-featuring-72-nvidia-rubin-gpus-for-data-centers-in-space-report-claims-replaces-conventional-nvlink-cable-assemblies-with-a-massive-84-layer-printed-circuit-board
summary: SpaceX 自研的 Kessel 機櫃沿用 Nvidia GPU，其餘供應鏈則全數自行掌握。Nvidia 一向以全端方案綁住客戶，這是該策略首度出現實質破口。
tags:
- hardware
- ai-ml
- industry
title: 報導：SpaceX 自研「Kessel」機櫃級系統，搭載 72 顆 Nvidia Rubin GPU，瞄準太空資料中心
trending: false
type: news
---

SpaceX/xAI is developing a custom version of Nvidia's Vera Rubin NVL72 rack-scale AI system that replaces conventional NVLink cable assemblies with a massive 84-layer printed circuit board (PCB), in part for use in orbital data centers, reports [SemiAnalysis](https://x.com/SemiAnalysis_/status/2120351564720136389). The system is codenamed Kessel and retains 36 Vera CPUs, 72 Rubin GPUs, and nine NVLink switch trays, but introduces a different solid-state interconnect architecture. While SpaceX/xAI will continue to buy Nvidia hardware directly from the company, Elon Musk's company will source other components independently, which could give it greater control over its hardware supply chain.

The Kessel system retains the fundamental configuration of Nvidia's Vera Rubin NVL72 platform, which comprises 72 GPU packages distributed across 18 compute trays and nine NVLink switch trays. However, instead of Nvidia's conventional arrangement with internal NVLink cable cartridges, SpaceX plans to position compute and switch trays back-to-back around a passive PCB midplane. The architecture resembles a smaller version of Nvidia's Kyber design with 576 AI GPUs (albeit in 144 packages), which also relies on a PCB-based interconnect rather than conventional cable assemblies, *SemiAnalysis* notes. Interestingly, the design is aimed at both terrestrial and orbital deployments, according to the analysts.

Arguably the most distinctive feature of Kessel is its 84-layer PCB midplane, which uses ultra-low-loss M10 copper-clad laminates (CCLs). By contrast, Nvidia's Kyber architecture relied on a backplane based on a considerably more complex 156-layer PCB featuring M9 CCLs. The reduction in layer count by nearly half could substantially improve manufacturability and production yields, but the more advanced copper-clad laminate will almost certainly increase material costs. In any case, an 84-layer PCB is a device that is exceptionally hard to build.

The move to a PCB midplane could simplify system assembly by eliminating numerous high-speed cable connections, but it would not necessarily reduce manufacturing costs. An 84-layer PCB that relies on ultra-low-loss M10 laminate is an exceptionally expensive component that requires sophisticated manufacturing processes and precise quality control. To put an 84-layer PCB number into context, modern high-end server motherboards use 15 – 20 layers, whereas server development boards use more than 20 layers to virtually eliminate any electrical issues with the board itself. Furthermore, manufacturing yields of an 84-layer PCB could become a major obstacle, as defects in internal layers may render an entire board unusable. Consequently, the economic viability of Kessel will depend on whether savings from cable elimination and independent component procurement can offset the cost of its complex midplane.

Perhaps more importantly, Kessel represents a departure from Nvidia's conventional system-level procurement model. Instead of purchasing Nvidia's assembled L6 compute boards or even [L10 trays that Nvidia plans to sell with its Vera Rubin generation](https://www.tomshardware.com/tech-industry/artificial-intelligence/jp-morgan-says-nvidia-is-gearing-up-to-sell-entire-ai-servers-instead-of-just-ai-gpus-and-componentry-jensens-master-plan-of-vertical-integration-will-boost-profits-purportedly-starting-with-vera-rubin), SpaceX reportedly plans to acquire AI accelerators, CPUs, switches, and networking components directly from Nvidia and procure other components from third-party suppliers (one can wonder how easy it will be for SpaceX/xAI to procure memory amid today's shortages). This would enable SpaceX to select its own PCB manufacturers, component vendors, and manufacturing partners, optimize its hardware for its infrastructure (which will be important for orbital deployments), and perhaps reduce intermediary costs. Meanwhile, the company would assume greater responsibility for system design, validation, manufacturing quality, and supply-chain management, which is something that most hyperscalers have been doing in recent years.

For Nvidia, the implications are less straightforward. Although direct sales of CPU and AI GPU packages could reduce the company's revenue from complete compute-board assemblies, the arrangement could also encourage other large customers to develop their own Nvidia-based systems and eventually deploy more Nvidia-based machines, something that may be important in a world where custom silicon developed by hyperscalers is rapidly gaining traction. However, to make this happen, Kessel must be a smashing success that will offer clear advantages over systems designed by Nvidia.

*Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

## Summary

**TLDR:** SpaceX's custom Kessel rack keeps Nvidia's GPUs but takes over the rest of the supply chain, which is the first real crack in Nvidia's full-stack lock-in.

- SemiAnalysis reports that SpaceX/xAI's Kessel system keeps Vera Rubin NVL72's 36 Vera CPUs, 72 Rubin GPUs, and nine NVLink switch trays.
- Kessel swaps Nvidia's NVLink cable cartridges for a passive 84-layer PCB midplane, with compute and switch trays mounted back-to-back.
- The 84-layer design uses M10 laminates, compared with the 156-layer M9 backplane in Nvidia's Kyber. That should improve yields but raise material costs.
- The design targets both terrestrial and orbital data centers, where a solid-state interconnect may hold up better than cables.
- SpaceX will keep buying GPUs from Nvidia but will source other components independently, gaining more control over its supply chain.

## 摘要

**重點摘要：** SpaceX 自製的 Kessel 機櫃保留 Nvidia GPU，但其餘供應鏈自己掌控，這是 Nvidia 全堆疊綁定第一次出現實質裂縫。

- 根據 SemiAnalysis，SpaceX/xAI 的 Kessel 系統沿用 Vera Rubin NVL72 的 36 顆 Vera CPU、72 顆 Rubin GPU 和 9 個 NVLink 交換器托盤。
- Kessel 以 84 層被動式 PCB 中板取代 Nvidia 的 NVLink 線纜匣，運算托盤與交換器托盤背對背安裝。
- 84 層設計採用 M10 銅箔基板，Nvidia Kyber 則是 156 層的 M9 背板。層數減半有助於良率，但材料成本會上升。
- 這套設計同時鎖定地面與軌道資料中心，在太空環境中，固態互連可能比線纜更耐用。
- SpaceX 仍向 Nvidia 直接採購 GPU，其他零組件則自行採購，對供應鏈的掌控度更高。