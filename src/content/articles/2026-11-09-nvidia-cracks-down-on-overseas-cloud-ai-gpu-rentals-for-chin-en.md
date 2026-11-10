---
category: policy
faqs:
- answer: According to the Financial Times, Nvidia verbally told cloud partners worldwide
    that at least 51% of their services must go to non-Chinese companies. Nvidia has
    not confirmed or denied the rule.
  question: What is Nvidia's reported 51% rule?
- answer: They have bought more than 1 million Nvidia gaming and workstation cards
    this year and ordered over 6 million export-compliant RTX Pro 5500 cards. A B300
    rack reportedly sold for $2.8 million in China versus about $600,000 internationally.
  question: How are Chinese AI labs responding?
- answer: Southeast Asian data centers, whose biggest clients have been Chinese tech
    groups, may have to pull back supply. A Singapore operator told the FT it is difficult
    to find enough non-Chinese clients outside the US.
  question: Who else is affected?
featured: false
lang: en
publishedAt: '2026-11-09T17:48:17+00:00'
relatedSlugs: []
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/policy/nvidia-cracks-down-on-overseas-cloud-ai-gpu-rentals-for-china-partners-face-51-percent-non-chinese-quota-as-black-market-b300-rack-prices-surge-to-usd2-8-million
summary: Nvidia's quiet 51% rule looks like self-policing aimed at Congress, and a
  B300 rack selling for nearly five times its price in China shows how far demand
  outruns supply.
tags:
- policy
- hardware
- ai-ml
title: Nvidia cracks down on overseas cloud AI GPU rentals for China
trending: false
type: news
---

Nvidia-based compute is getting scarce and expensive for Chinese AI labs on both of their main routes, buying export-compliant cards and renting abroad, and the [*Financial Times* reports](https://www.ft.com/content/1902df70-1380-4588-bad5-171352b575f2) that Nvidia’s own crackdowns are part of the reason. Nvidia has told cloud partners worldwide that [at least 51% of their services](https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits) must go to non-Chinese firms, while Chinese companies have bought more than 1 million Nvidia gaming and workstation cards this year to cover the shortfall. Meanwhile, a B300 rack that sells for about $600,000 internationally reportedly fetched $2.8 million in China last month.

Chinese customers have ordered more than 6 million of Nvidia’s export-compliant RTX Pro 5500 cards. That is at least twice the 3 million that the company could reportedly manufacture in 2027. One source told *CNBC* that it was proposed that Moonshot pay 30% to 50% more upfront, in comparison to a non-Chinese entity.

Many Chinese groups have relied on overseas leases for advanced AI work, which can include model training, and these tech groups have been the biggest clients for data centers in Southeast Asia. Data centers unable to find non-Chinese clients could be forced to pull back supply, and it’s “difficult to find enough non-Chinese clients outside the US,” one Singapore-based group told the *FT*. While Nvidia hasn’t confirmed or denied its new rule, implementing it would ease criticism from U.S. lawmakers just as Chinese demand is growing.

What Nvidia told partners has come through verbal instructions, via sales and regional teams, and applies globally rather than just in Asia. Existing deals and leases are not changed, but new ones must comply. Nvidia’s whitelist more than halved its authorized Asian buyer count, which encouraged more Chinese groups to lease over other options, including smuggling. On top of this, [Fleet Intelligence tracking](https://www.tomshardware.com/tech-industry/big-tech/nvidia-tightens-tracking-of-ai-gpus-in-southeast-asia-as-chinese-chip-smuggling-draws-scrutiny-report-claims-cloud-providers-must-join-monitoring-program-to-qualify-for-official-partner-status) is now required for Southeast Asian providers that want to become Nvidia Cloud Partners. All of these combined — whitelist, cap, and tracking — may act to alleviate U.S. concerns.

Among companies that have moved to renting, Moonshot has held discussions to [rent capacity from neoclouds that host in Europe](https://www.tomshardware.com/tech-industry/policy/chinese-ai-lab-moonshot-reportedly-looked-at-european-data-centers-to-access-nvidia-chips-report-claims-kimi-maker-primarily-interested-in-inferencing-capacity-but-also-asked-about-training-clusters) with Nvidia GPUs. Specifically, it’s looking for Nvidia Blackwell systems, which export controls bar from China; one source said the talks covered clusters of 8,000 or more Blackwell GPUs in Europe. These clusters would handle inference, serving models to end users, and the European talks for them happened after the White House said Moonshot [accessed Blackwell chips through a facility in Thailand](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-moonshot-ai-reportedly-used-nvidia-blackwell-chips-for-training-kimi-k3-company-circumvented-both-u-s-export-and-chinese-import-controls-to-acquire-compute). The firm has been fervent about its intentions to secure more compute.

Moonshot isn't the only Chinese company looking to secure Nvidia chips for AI training. Tencent has a deal with Oracle to [lease 100,000 GPUs](https://www.tomshardware.com/tech-industry/data-centers/tencent-scores-100-000-offshore-ai-chip-deal-with-oracle-for-usd7-billion-despite-climbing-prices-per-hour-costs-estimated-to-be-43-percent-under-standard-h100-rental-rates) in Southeast Asian data centers. ByteDance and Alibaba are also pursuing similar long-term leases, and most of these overseas data centers run chips like the forbidden B300. MiniMax, like Moonshot, also leases significant compute both at home and abroad.

The big reason is that domestic AI chip supply is simply not up to the task, although not for a lack of trying. Huawei is expected to hit 1.6 million chips this year, with about 1 million from Alibaba and Baidu, and 300,000 from Cambricon. Total supply this year will be up to 3.5 million, including about 1 million made overseas, against a demand that far exceeds 5 million. That number could more than double next year.

Part of the problem is that the [export-compliant cards Chinese firms have been buying](https://www.tomshardware.com/pc-components/gpus/chinese-ai-companies-buy-1-million-nvidia-gpus-in-a-single-year-report-claims-export-control-compliant-chips-flood-the-market-to-bridge-gap-in-compute-demand), mostly the RTX Pro 6000D, RTX Pro 5000, and RTX 5090, are mostly useful for simpler work such as prefill. Even so, the discontinued 6000D’s pricing in China has reportedly doubled. Huawei’s Ascend 910C outperforms them in most areas, but these lower-end options are still coveted, partly because of a preference for CUDA over Huawei’s CANN. Nvidia’s programming platform is supported by most AI frameworks and libraries, and much in-house code is optimized for it.

Then there’s the [RTX Pro 5500](https://www.tomshardware.com/pc-components/gpus/gaming-takes-a-backseat-as-nvidia-overhauls-the-rtx-5090-for-maximum-ai-margins-rtx-pro-5500-delivers-2-6x-vram-at-matching-specs), with 84GB of GDDR7 with ECC and 1,398 GB/s of memory bandwidth. The card runs on a full PCIe Gen 5 x16 interface, draws up to 600 W, and can be split into up to two MIG instances. That still leaves it well short of a B300, which has about 3.4 times the memory and 5.7 times the bandwidth, plus NVLink, which the 5500 lacks.

| What Chinese labs can buy vs. what they rent |  |  |  |  | 
|---|---|---|---|---|
| GPU | Memory | Bandwidth | Interconnect | Status for Chinese buyers | 
| RTX Pro 5500 | 84GB GDDR7 | 1.4 TB/s | PCIe Gen 5 x16 | Export-compliant; samples in December, deliveries from Q1 2027 | 
| H200 | 141GB HBM3E | 4.8 TB/s | NVLink | Licensed by the U.S. case by case; Beijing withholding approval for large-scale imports | 
| B300 | 288GB HBM3E | 8 TB/s | NVLink (1.8 TB/s) | Banned for sale to China; rented abroad | 

Indicated orders from China are not precise, but the total of over six million includes more than three million from ByteDance, Alibaba, and Tencent. The big three ordered at about $11,400 each, for a total sticker price over $35 billion. This is difficult to fill when there may be fewer than three million produced next year, and partners might only actually get 5% to 10% of the original ask. Starting in 2027, much of Nvidia’s TSMC capacity may shift to Rubin, taking more production, while the RTX Pro 5500’s early samples are due in December.

On the legal side, it’s currently easier to rent than to own as current U.S. law does not give regulators broad authority over overseas cloud access. The Remote Access [Security](https://www.tomshardware.com/tag/security) Act (RASA), which would extend U.S. export controls to that area, has sailed through the House but has not yet passed the Senate. Those directly affected — neoclouds and related financiers — price in a possible ban regardless, which drives the upfront premium.

China’s side is not completely clean, either, with about 600,000 H200s reportedly stuck in storage in Hong Kong awaiting shipment to the mainland. Beijing is withholding approvals for large-volume imports such as this. Only relatively small quantities have come in during recent months, for some big internet companies, with others coming through intermediaries and indirect routes in small quantities. The price: over $900,000 for an eight-card H200 server in China at the end of last month, about 3x the cost a year ago. This is despite the fact that H200 sales are already under U.S. license.

The first test that will show how many cards will actually land occurs in Q1 2027, when the RTX Pro 5500 is expected in commercial deliveries. For rentals, whether or not the Remote Access Security Act is a factor depends on a Senate vote, which is not yet scheduled. Nvidia’s Q3 results come in soon, on Nov. 17, which could bring some illumination.

With CEO Jensen Huang under scrutiny lately over reports that he was [targeted by an alleged Chinese spy](https://www.tomshardware.com/pc-components/gpus/nvidia-ceo-jensen-huang-admits-to-having-an-affair-with-suspected-chinese-spy-jensen-apologizes-in-letter-to-staff-company-board-forms-independent-committee-to-investigate), which Nvidia’s board is now investigating, he’s going to feel the heat even more just a day later, when lawmakers have asked him to attend a closed-door briefing. He’s been pushing for laxer controls and more access, so the assumed 51% rule will also be put to the test.

## Summary

**TLDR:** Nvidia's quiet 51% rule looks like self-policing aimed at Congress, and a B300 rack selling for nearly five times its price in China shows how far demand outruns supply.

- The FT reports Nvidia verbally told cloud partners worldwide that at least 51% of their services must go to non-Chinese firms.
- Chinese companies bought more than 1 million gaming and workstation cards this year to make up for the shortfall.
- A B300 rack that sells for about $600,000 internationally reportedly fetched $2.8 million in China last month.
- Chinese orders for the export-compliant RTX Pro 5500 exceed 6 million, at least double the roughly 3 million Nvidia could reportedly make in 2027.
- Southeast Asian data centers that depend on Chinese tenants may have to cut supply because non-Chinese clients are hard to find.

## 摘要

**重點摘要：** Nvidia 低調推出的 51% 規定，看起來是做給國會看的自律；B300 機櫃在中國賣到將近五倍價格，顯示需求遠遠超過供給。

- 根據《金融時報》報導，Nvidia 以口頭方式要求全球雲端夥伴，至少 51% 的服務必須提供給非中國企業。
- 中國企業今年買了超過 100 萬張遊戲卡與工作站卡來補缺口。
- 國際售價約 60 萬美元的 B300 機櫃，上個月在中國據報賣到 280 萬美元。
- 中國對合規版 RTX Pro 5500 的訂單超過 600 萬張，至少是 Nvidia 2027 年預估產能（約 300 萬張）的兩倍。
- 依賴中國租戶的東南亞資料中心可能被迫縮減供給，因為很難找到足夠的非中國客戶。