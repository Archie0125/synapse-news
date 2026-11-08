---
category: hardware
faqs:
- answer: 'Blizzard ran WoW: Forever''s launch on 3,924 virtual machines with 70,480
    CPU cores and 251,136 GB (about 251 TB) of memory. That averages about 18 cores
    and 64GB per virtual machine.'
  question: 'How much hardware did WoW: Forever use at launch?'
- answer: 'In 2009, Blizzard used 13,250 server blades with 75,000 CPU cores and 112.5
    TB of memory across 10 data centers. WoW: Forever uses 6% fewer cores but about
    2.2 times more memory.'
  question: How does that compare with WoW's infrastructure in 2009?
- answer: Modern processors are far faster than chips from 2009, so CPU cores are
    no longer the main constraint. Memory capacity and bandwidth have become the bottleneck,
    so Blizzard runs fewer cores with much more RAM.
  question: Why does the new setup rely so heavily on memory?
featured: false
lang: en
publishedAt: '2026-11-08T11:30:00+00:00'
relatedSlugs: []
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/video-games/pc-gaming/wow-forever-launch-used-70-480-cpu-cores-and-251-terabytes-of-ram-3-924-virtual-machines-powered-one-of-world-of-warcrafts-smoothest-launches-ever
summary: Blizzard's smooth launch shows that in 2026 you avoid server meltdowns by
  throwing memory at the problem, which costs more every month as DRAM prices climb.
tags:
- hardware
- industry
- products
title: 'WoW: Forever launch used 70,480 CPU cores and 251 terabytes of RAM'
trending: false
type: news
---

Blizzard pulled out all the stops to ensure *World of Warcraft: Forever* survived a chaotic launch night. What was the company's secret weapon? Splurging an absurd amount of money on infrastructure made up of 3,924 virtual machines with 70,480 CPU cores and a whopping 251,136 GB, or 251 TB, of memory.

Praised by media and players as one of the smoothest launches in Blizzard's history, *World of Warcraft: Forever* requires significant computing firepower. 3,924 virtual machines work out to 18 cores and 64GB of memory per instance. Or, the company could be using a mixture of 16-core and 32-core nodes with slightly less memory.

To put the infrastructure's scale in consumer terms, we are looking at about 8,810 mainstream processors, or 7,848 high-end gaming systems with 32GB of memory each. In any event, the hardware is greatly improved compared to what *World of Warcraft* used to run on back in 2009.

In 2009, Blizzard said it used 10 data centers worldwide to host *World of Warcraft.* At the time, the infrastructure included 13,250 server blades, totaling 75,000 CPU cores and 112.5 TB of memory. By comparison, *World of Warcraft: Forever* leverages 6% fewer CPU cores but rocks 2.2X more memory. Modern processors are leagues faster than chips from 17 years ago. By today's standards, the bottleneck is memory capacity and bandwidth, which is why the infrastructure can run on fewer cores but has more than double the memory to compensate.

Blizzard does not specify the exact hardware that *World of Warcraft: Forever* runs on. However, if we were to translate the core specifications to, for example, AMD's EPYC 128-core [Bergamo](https://www.tomshardware.com/news/amd-details-epyc-bergamo-cpus-with-128-zen-4c-cores) or 96-core [Genoa](https://www.tomshardware.com/reviews/amd-4th-gen-epyc-genoa-9654-9554-and-9374f-review-96-cores-zen-4-and-5nm-disrupt-the-data-center) chips, it could be anywhere between 275 and 365 2U server nodes, depending on which processor it uses. Therefore, *World of Warcraft: Forever* could be running on just eight to ten 42U server racks, a noteworthy improvement over 17 years ago.

Blizzard should have no trouble building the infrastructure for *World of Warcraft: Forever*. A ballpark estimate for about ten 42U server racks with EPYC chips is at least $15 million, even with today's memory pricing. But then again, since [Microsoft](https://www.tomshardware.com/tag/microsoft) owns Blizzard now, the company could just be tapping its parent's existing Azure platform. Technically, it is not free compute, but Blizzard would benefit from cost pricing and priority allocation of Azure's capacity.

*World of Warcraft: Forever* shows that a high-profile launch does not have to be a nightmare when companies are willing to invest in computing infrastructure. In this case, many would agree Blizzard is putting those 251TB to good use, although [Sam Altman may say otherwise](https://www.tomshardware.com/tech-industry/data-centers/openai-ceo-says-its-quite-terrible-for-your-pc-to-have-ram-sam-altman-says-data-centers-offer-better-utilization).

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

*Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.*

Zhiye Liu is a news editor, memory reviewer, and SSD tester at Tom’s Hardware. Although he loves everything that’s hardware, he has a soft spot for CPUs, GPUs, and RAM.

- 
Clearly we need a moratorium on gaming and protestors should swarm gaming studios to put a stop to this waste and driving up our energy prices. Gaming needs to end as it clearly causes inflated prices for some consumers. (if you find this post offensive Google sarcasm).
[Reply](https://forums.tomshardware.com/threads/wow-forever-launch-used-70-480-cpu-cores-and-251-terabytes-of-ram.3902078/)

## Summary

**TLDR:** Blizzard's smooth launch shows that in 2026 you avoid server meltdowns by throwing memory at the problem, which costs more every month as DRAM prices climb.

- WoW: Forever launched on 3,924 virtual machines with 70,480 CPU cores and about 251 TB of memory.
- In 2009, WoW ran on 75,000 cores and 112.5 TB, so the new setup uses 6% fewer cores and 2.2x more memory.
- Modern CPUs are much faster, so memory capacity and bandwidth are now the main bottleneck.
- Media and players called it one of the smoothest launches in Blizzard's history.
- Implication: game infrastructure is competing with AI for the same increasingly scarce DRAM.

## 摘要

**重點摘要：** Blizzard 這次上線順利，說明 2026 年要避免伺服器爆掉，靠的是砸記憶體，而記憶體正越來越貴。

- 《WoW: Forever》上線動用 3,924 台虛擬機、70,480 個 CPU 核心與約 251 TB 記憶體。
- 2009 年 WoW 使用 75,000 核心與 112.5 TB，新架構核心少 6%，記憶體卻多 2.2 倍。
- 現代 CPU 快很多，瓶頸已經轉到記憶體容量與頻寬。
- 媒體與玩家都稱這是 Blizzard 史上最順利的上線之一。
- 背後意義：遊戲基礎設施正在跟 AI 搶同一批越來越稀缺的 DRAM。