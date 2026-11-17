---
category: hardware
faqs:
- answer: Tom's Hardware said the TeamGroup GA Pro mostly misses. It does well at
    QD8 and has acceptable steady-state writes, but overall performance is very low,
    efficiency is poor and it runs hot.
  question: What did Tom's Hardware conclude about the TeamGroup GA Pro 2TB?
- answer: Everyday desktop work and gaming mostly put light, low-queue-depth loads
    on an SSD. Because the GA Pro reads poorly at low queue depths, it can feel slower
    in daily use than its PCIe 5.0 spec suggests.
  question: Why does poor low-queue-depth performance matter for this SSD?
- answer: Tom's Hardware generally does not recommend the GA Pro unless it is on steep
    sale. At its listed $331.99 for 2TB, better PCIe 4.0 and PCIe 5.0 drives are available.
  question: Is the TeamGroup GA Pro worth buying?
featured: false
lang: en
publishedAt: '2026-11-07T14:00:00+00:00'
relatedSlugs: []
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/pc-components/ssds/teamgroup-ga-pro-2tb-ssd-review
summary: TeamGroup's GA Pro has the PCIe 5.0 label, but in testing it often runs slower,
  hotter and less efficiently than the cheaper PCIe 4.0 drives it should beat.
tags:
- hardware
- products
title: 'TeamGroup GA Pro 2TB SSD Review: A faltering attempt at a mid-range PCIe 5.0
  SSD'
trending: false
type: news
---

### Tom's Hardware Verdict

The TeamGroup GA Pro is a drive that mostly misses. While it has relatively good points at QD8 and acceptable steady-state write speed, overall performance is very low with this inefficient, hot-running drive.

#### Reasons to buy

- \+ Performance highlights at QD8
- \+ Respectable steady-state write speed

#### Reasons to avoid

- \- Very poor scores in some tests
- \- Poor low-QD reads
- \- Poor efficiency and high temps

Why you can trust Tom's Hardware
Our expert reviewers spend hours testing and comparing products and services so you can choose the best for you. [Find out more about how we test](https://www.tomshardware.com/news/how-we-test).

Every once in a while we get a drive that comes across our desk that stands out, for good or for bad. The TeamGroup GA Pro falls into the latter category, enough so that we re-checked our results and contacted the company. We’ve managed to mostly sort out what’s going on and, while this is not the worst drive around, it has enough problems that we would generally not recommend it except if it's on steep sale.

TeamGroup’s array of storage offerings knows no bounds: if there’s a niche to cover, it makes an attempt. The GA Pro feels like such a try, although we’re not completely sure where it fits into the mix. The company is still working to iron out the bugs, if it can, but the technology is old enough that we wouldn’t hold our breath. On paper, it’s a PCIe 5.0 drive with DRAM that should beat any PCIe 4.0 SSD, but we found it struggles to live up to its own class of drive. Bright points are few and far between, but at least we can say it’s not *the* worst drive we’ve seen. The edges are just rougher than usual.

## TeamGroup GA Pro Specifications

| **Product** | 1TB | 2TB | 4TB | 8TB | 
|---|---|---|---|---|
| **Pricing** | N/A | $331.99 | N/A | N/A | 
| **Form Factor** | M.2 2280 (graphene heatsink) | M.2 2280 (graphene heatsink) | M.2 2280 (graphene heatsink) | M.2 2280 (AirFlow I heatsink) | 
| **Interface / Protocol** | PCIe 5.0 x4 / NVMe 2.0 | PCIe 5.0 x4 / NVMe 2.0 | PCIe 5.0 x4 / NVMe 2.0 | PCIe 5.0 x4 / NVMe 2.0 | 
| **Controller** | InnoGrit IG5666 | InnoGrit IG5666 | InnoGrit IG5666 | InnoGrit IG5666 | 
| **DRAM** | Yes | 2GB DDR4 | Yes | Yes | 
| **Memory** | YMTC 232-layer TLC | YMTC 232-layer TLC | YMTC 232-layer TLC | YMTC 232-layer TLC | 
| **Sequential Read** | 10,000 MB/s | 10,000 MB/s | 10,000 MB/s | 10,000 MB/s | 
| **Sequential Write** | 8,500 MB/s | 8,500 MB/s | 8,500 MB/s | 8,500 MB/s | 
| **Random Read** | N/A | N/A | N/A | N/A | 
| **Random Write** | N/A | N/A | N/A | N/A | 
| **Security** | N/A | N/A | N/A | N/A | 
| **Endurance (TBW)** | 600TB | 1,200TB | 2,400TB | 4,800TB | 
| **Part Number** | TM8FFJ001T0C129 | TM8FFJ002T0C129 | TM8FFJ004T0C129 | TM8FGL008TTC133 | 
| **Height** | 3.9 mm (w/ graphene) | 3.9 mm (w/ graphene) | 3.9 mm (w/ graphene) | 62.3 mm (w/ AirFlow I) | 
| **Warranty** | 5-Year | 5-Year | 5-Year | 5-Year | 

The TeamGroup GA Pro is available in 1TB, 2TB, 4TB, and 8TB capacities, although we only have the 2TB showing up at $331.99 at retail right now. The 8TB will probably be hard to find at this point. The drive is rated for up to 10,000 / 8,500 MB/s for sequential reads and writes, with no IOPS rating, although a drive like this can achieve 1 million or more. It has the standard five-year warranty with up to 600 TB of writes per TB of capacity.

## TeamGroup GA Pro Software and Accessories

TeamGroup has a [<u>number of downloads</u>](https://support.teamgroupinc.com/en/support/download.php?index_m1_id=3&index_m2_id=136) available for this range of drives, which is better than nothing. They do maintain firmware for their drives, and we made sure our test sample had the newest revision, 050g05E7. Also available is the SSD S.M.A.R.T. TOOL, which is their SSD toolbox with basic functions, such as health monitoring. For backup and cloning on Windows, we continue to recommend [<u>MultiDrive,</u>](https://multidrive.io/) which continues to be updated based on user feedback.

## TeamGroup GA Pro: A Closer Look

The good news is, the GA Pro has a graphene heat-spreading label. The bad news is, it’s insufficient to cool this drive. In most cases, you will want a heatsink on this. You can use a heatsink with the label in place, but you will have better luck if it’s removed. We are fond of graphene labels as they can be surprisingly effective, but it’s just not enough here.

Then we have the label which, with the 3.3V / 2.5A rating, puts the drive at a very optimistic 8.25W. We measured over 12.5W peak in our testing below. We can’t go by reported power states, as these top off at 3.50 W. Since we can’t rely on that, we can’t say for sure what even the expected enter/exit latencies are, relevant given TeamGroup’s claims about the drive, which we’ll get to later. The drive is otherwise double-sided with a controller, two DRAM packages, and four NAND flash packages.

The SSD controller is InnoGrit’s IG5666, the company’s answer to the Phison E26 high-end PCIe 5.0 champion. We have better controllers in that segment now, like the E28 and SMI’s SM2508, but even at the time of release, the IG5666 was not very popular. Both the E26 and IG5666 run very hot due to using an older process node, and newer flash wasn’t available yet to more easily reach the bus speeds needed. The GA Pro is not running full-out but, to be honest, that doesn’t help much. Phison put a lot of work into getting the E26 up to full speed in steps, and even the base 10 GB/s ones run toasty.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The drive does have the right amount of DDR4, 2GB, for this amount of flash. No problems there. The flash also looks to be YMTC’s 232-layer TLC, which is also perfectly fine. The controller is the weak spot here and, as we’ll find out, its firmware really keeps the GA Pro from reaching its full potential, even with its bandwidth cap.

**MORE: Best SSDs**

**MORE: Best External SSDs**

**MORE: Best SSD for the Steam Deck**

## Summary

**TLDR:** TeamGroup's GA Pro has the PCIe 5.0 label, but in testing it often runs slower, hotter and less efficiently than the cheaper PCIe 4.0 drives it should beat.

- Tom's Hardware found the GA Pro's results poor enough that it re-ran its tests and contacted TeamGroup before publishing.
- The 2TB model costs $331.99 and pairs a PCIe 5.0 interface with DRAM, yet it struggles to match even its own class.
- Its few strengths are performance at QD8 and respectable steady-state write speeds.
- Weaknesses include poor low-queue-depth reads, which matter most for everyday use, plus low efficiency and high temperatures.
- TeamGroup is still trying to fix bugs, but the reviewer expects little improvement because the underlying technology is already dated.

## 摘要

**重點摘要：** TeamGroup GA Pro 掛著 PCIe 5.0 的名號，實測卻常常輸給更便宜的 PCIe 4.0 SSD，而且更熱、更耗電。

- Tom's Hardware 覺得 GA Pro 的成績差到不太正常，發稿前還重測了一遍，並聯絡 TeamGroup 確認。
- 2TB 版售價 331.99 美元，有 PCIe 5.0 介面也有 DRAM，表現卻連同級產品都追不上。
- 少數亮點是 QD8 的成績，還有表現不錯的穩態寫入速度。
- 低佇列深度讀取很差，偏偏日常使用最常碰到的就是這種負載；效率也低，溫度又高。
- TeamGroup 還在修 bug，但評測者認為底層技術已經過時，不必期待會有大幅改善。