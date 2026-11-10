---
category: hardware
faqs:
- answer: A Reddit user found heat-damaged braided sleeving on the 12V-2x6 cables
    of two RTX PRO 6000 Blackwell GPUs. The sleeving was stiff, cracked, and peeling,
    even though both cards were limited to 500W.
  question: What happened to the RTX PRO 6000 cables?
- answer: At 500W each pin should carry only about 6.94A, but uneven current distribution
    can push much more through a few pins. Damage on only two pins per cable suggests
    those pins regularly took high-current spikes.
  question: Why would cables overheat below the 600W limit?
- answer: The user said dropping to 300W would cut performance by up to 50%, which
    would not work with their work deadlines. A lower power limit lowers the risk
    but does not fix uneven load across the pins.
  question: Why not just lower the power limit further?
featured: false
lang: en
publishedAt: '2026-11-09T14:00:00+00:00'
relatedSlugs: []
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-pro-6000-users-cables-almost-melted-even-when-limited-to-500w-12v-2x6-cables-appear-to-still-cause-problems-show-clear-signs-of-melting
summary: When a 500W cap still cooks 12V-2x6 cables on a workstation card, the connector
  design has a problem that a power limit will not fix.
tags:
- hardware
- products
title: Nvidia RTX PRO 6000 user’s cables almost melted, even when limited to 500W
trending: false
type: news
---

Reddit user u/Doomslayer606 posted about frayed braided sleeving on both 12V-2x6 cables for their two RTX PRO 6000 Blackwell Workstation GPUs the other day, asking whether it’s normal cable degradation or a sign of overheating. The GPUs were running at 500W, below the maximum 600W power draw, but commenters are confident it’s overheated cables, as the poster reports stiff, cracked, and easily peeling sleeves on only some of the wires.

u/Doomslayer606 posted on r/PcBuild with the title “Did I just save my RTX PRO 6000 GPUs from melting?” with photos of the 12V-2x6 cable’s braided sleeving frayed. The poster asked in the description whether this was normal degradation, a manufacturing issue, or overheating. The poster reported that the damaged braided sleeving felt stiff and peeled off easily, which is a strong indication of heat damage, and the comments were sure that it was.

Luckily, the poster’s GPUs were safe, but the [<u>12-2x6 connectors are notorious for melting</u>](https://www.tomshardware.com/desktops/gaming-pcs/usd5-245-prebuilt-rtx-5090-pcs-connectors-melt-after-sitting-boxed-for-a-year-digital-storm-and-pny-deny-warranty-claims-over-expired-coverage-and-third-party-cables) due to high power draw. One comment asked if they kept the stock power limit, to which the poster responded that they lowered both GPUs to 500W — another user responded asking why the poster wouldn’t use 300W, but the poster said it would reduce performance by up to 50% and they need to keep up with their deadlines.

Theoretically, the cable should be able to handle 500W, as each positive pin would only handle 6.94 A, which isn’t enough current to significantly heat up 16 AWG wire, but one of the main causes of cable overheating is uneven current distribution across the pins. Since only two of the pins melted on both cables, it’s likely those received high-current spikes often, leading to heat buildup.

Users have suggested aftermarket cables like the Corsair ThermalProtect 12V-2x6 cable that detects overheating cables, and the Thermal Grizzly WireView Pro II or Aqua Computing AMPINEL, which have active current balancing to prevent any wire from taking too much current alone. In a recent story, someone even created a power distributor, [<u>distributing the 12 pins into two 8-pin cables</u>](https://www.tomshardware.com/pc-components/gpus/modder-fixes-melting-rtx-5090-power-connectors-with-custom-distributor-dual-8-pin-mod-peaks-at-just-40c-during-a-48-hour-550w-stress-test) with a custom-designed PCB, which lowered the cable temperatures significantly — while another modder had a [<u>cursed solution</u>](https://www.tomshardware.com/pc-components/gpus/modders-solder-power-cables-directly-to-rtx-5090-pcb-to-eliminate-notorious-melting-16-pin-connector-bare-board-galax-hof-card-pulls-600w-under-chiller-cooling), soldering thick cables directly to the RTX 5090’s power pins.

In an ideal world, consumers shouldn’t need another product or mod their GPUs to stop them destroying themselves. GPUs have only gotten more powerful, but instead of using more or thicker wires, we’re getting fewer wires of the same thickness. Understandably, having multiple 8-pin connectors gets messy, but surely there has to be a better solution. Maybe GPUs have outgrown the Mini-Fit Jr. connectors and need to have their own special connector with thicker pins and thicker wires.

*Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

*Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.*

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.

- 
Every time i try to plug and unplug this connector i exercise in cursing and swearing in address of those who adopted 12V-6x2, this standard is a failure of PC industry. I have even seen the GPU card where clearly angy user bent and unrooted the connector 45 degrees corrupting motherboard.
And have anyone ever heard the final click when you insert the cable with all your force?
Changing tripple 8pin connectors carrying 450 W on older cards with just one driving 600W is a design crime. Before 9 larger contacts (3×3 ) were sharing 12V power load now only 6 tiny ones handling even larger load. When somebody start a lawsuit?
[Reply](https://forums.tomshardware.com/threads/nvidia-rtx-pro-6000-user%E2%80%99s-cables-almost-melted-even-when-limited-to-500w.3902119/)

## Summary

**TLDR:** When a 500W cap still cooks 12V-2x6 cables on a workstation card, the connector design has a problem that a power limit will not fix.

- A Reddit user found stiff, cracked, easily peeling sleeving on both 12V-2x6 cables feeding two RTX PRO 6000 Blackwell cards.
- Both GPUs were capped at 500W, below their 600W maximum; dropping to 300W would cost up to 50% of performance.
- On paper, 500W works out to only 6.94A per pin, which is not enough to heat 16 AWG wire much.
- Damage on only two pins of each cable points to uneven current distribution, a known cause of 12V-2x6 failures.
- These are professional cards running under deadlines, so a cable failure costs downtime as well as hardware.

## 摘要

**重點摘要：** 限制在 500W 的工作站顯卡，12V-2x6 線材照樣被燒，問題出在接頭設計，降功耗救不了。

- 一位 Reddit 使用者發現，供電給兩張 RTX PRO 6000 Blackwell 的 12V-2x6 線材，編織套管都變硬、龜裂，而且一撕就掉。
- 兩張 GPU 都限制在 500W，低於 600W 上限；如果降到 300W，效能最多會掉 50%。
- 照計算，500W 下每根正極針腳只承受 6.94A，照理不足以讓 16 AWG 線材明顯發熱。
- 每條線只有兩根針腳受損，顯示電流分配不均，這也是 12V-2x6 出問題的已知原因。
- 這是在趕交期的專業顯卡，線材一燒，損失的不只是硬體，還有停機時間。