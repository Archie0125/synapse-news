---
category: hardware
faqs:
- answer: Yandex Cloud said 2.84% of affected customer data could not be restored
    because critical equipment was physically damaged. The article does not identify
    the individual customers or datasets involved.
  question: What data was permanently lost?
- answer: Cloud reliability is judged per customer and workload, not by an aggregate
    percentage. A small overall loss can still mean complete and irreversible loss
    for particular organizations.
  question: Why does losing less than 3% matter?
- answer: Keeping facility locations confidential may make deliberate targeting harder,
    but it does not guarantee resilience. Customers still need tested backups that
    are geographically and operationally independent from Yandex.
  question: Will secret availability zones prevent another loss?
featured: false
lang: en
publishedAt: '2026-11-12T21:00:00+00:00'
relatedSlugs: []
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/data-centers/russias-google-says-nearly-3-percent-of-its-data-was-lost-after-crippling-ukraine-drone-strikes-opens-secret-availability-zones-yandex-cloud-blames-lack-of-user-backups-for-lost-data-now-forcibly-applies-backup-rules-by-default
summary: Yandex restored most customer data, but the irrecoverable 2.84% exposes how
  quickly cloud-resilience promises collapse when physical infrastructure becomes
  a military target.
tags:
- cybersecurity
- industry
title: Russia’s Google says nearly 3% of its data was lost after crippling Ukraine
  drone strikes, opens secret availability zon
trending: false
type: news
---

Yandex, sometimes called Russia’s [Google](https://www.tomshardware.com/tag/google), has updated its [customers in the wake of extensive damage to its data centers in drone strikes](https://www.tomshardware.com/tech-industry/data-centers/second-russian-data-center-targeted-by-ukrainian-drones-in-just-two-days-as-yandex-reels-from-another-service-outage-russian-state-media-admits-that-multiple-modules-completely-taken-out). In a [blog post](https://yandex.cloud/ru/blog/recovery?utm_referrer=about%3Ablank) this week, the firm’s cloud business boasted that it had “restored access to more than 97% of customer data” \[machine translation\]. That might sound like a great success, but in the small print, as highlighted by [*The Register*](https://www.theregister.com/off-prem/2026/11/12/russian-cloud-yandex-says-drone-attacks-on-its-datacenters-caused-data-loss/5309234), there’s the admission “the remaining 2.84% cannot be restored due to critical damage to equipment.”

Data centers operated by Yandex have been [under attack from Ukrainian drones](https://www.tomshardware.com/tech-industry/data-centers/second-russian-data-center-targeted-by-ukrainian-drones-in-just-two-days-as-yandex-reels-from-another-service-outage-russian-state-media-admits-that-multiple-modules-completely-taken-out) for several weeks now. We covered reports about withering online troll activity and online payment system disruption last month. We know of at least three Yandex locations that have been damaged by Ukrainian [drone assaults](https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drone-attacks-hammer-russias-finance-ministry-data-center-damaged-facility-reportedly-holds-tax-databases-facility-also-holds-other-important-state-registry-data) to date.

The recent Yandex blog post also appears to blame the small proportion of users who suffered unrecoverable data loss for not making backups. When talking about the 2.84% of data that cannot be restored, it says that was partly due to “the lack of customer backups on the platform.” In contrast, those who made use of the Yandex Cloud backup tools “did not lose any data,” says the firm.

Yandex has now changed the backup policy, so that “currently, all virtual machines created in Yandex Cloud work with the backup function enabled by default.” Even if Putin decides to end his [war on Ukraine](https://www.tomshardware.com/tech-industry/cyber-security/hackers-claim-to-have-stolen-23tb-of-data-from-russian-statistics-body-including-ukraine-war-casualty-figures-russian-federal-state-statistics-service-admits-its-servers-were-hit-by-coordinated-cyberattacks), it might be beneficial to stick with a backup-by-default policy. Users are advised to have their own data backup systems in addition to the cloud. Following the [3-2-1 backup strategy](https://www.tomshardware.com/software/windows/optical-drive-demand-surges-amid-windows-10-retirement-japanese-users-switching-to-windows-11-are-buying-up-blu-ray-drives), for example.

Yandex is also opening a new *ru-central1-f* availability zone at a new location. This is designed to improve the cloud’s fault tolerance and disaster resilience. Servers at *ru-central1-f* will be more limited in the range of services they can offer, for now. Yandex didn’t share any geographic details of the newly opened datacenter site.

*Download the Tom's Hardware app for up-to-the-minute updates on iOS and Android. Also follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

## Summary

**TLDR:** Yandex restored most customer data, but the irrecoverable 2.84% exposes how quickly cloud-resilience promises collapse when physical infrastructure becomes a military target.

- Yandex Cloud says it restored access to more than 97% of customer data after Ukrainian drone strikes damaged its data centers.
- The remaining 2.84% cannot be recovered because the underlying equipment suffered critical physical damage.
- At least three Yandex locations have reportedly been damaged, turning geographic redundancy into a national-security problem.
- Secret availability zones may reduce targeting risk, but undisclosed locations cannot compensate for customers lacking independent backups.

## 摘要

**重點摘要：** Yandex 雖救回多數資料，但永久遺失的 2.84% 已揭穿雲端韌性的盲點：機房成為軍事目標後，再漂亮的承諾都可能失效。

- 烏克蘭無人機攻擊多座資料中心後，Yandex Cloud 表示已恢復超過 97% 的客戶資料。
- 仍有 2.84% 因設備遭到致命破壞而無法復原；對受影響客戶而言，這不是小比例，而是永久損失。
- 據報至少三處 Yandex 設施受損，顯示雲端備援一旦集中在同一戰區，跨區設計也可能同時失守。
- 隱藏可用區位置或能降低被鎖定的風險，但真正的保險仍是客戶自行維持獨立、可驗證的異地備份。