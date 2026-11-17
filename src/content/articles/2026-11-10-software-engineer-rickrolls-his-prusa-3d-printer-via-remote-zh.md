---
category: hardware
faqs:
- answer: Dixken 在一週內發現 14 項問題，涵蓋約 23 個個別缺陷，其中包括一條能透過網路在印表機主控制器上執行程式碼的漏洞鏈。他用 Rickroll
    印表機的方式示範這個漏洞。
  question: Yannick Dixken 在 Prusa MK4S 上發現了什麼？
- answer: 只要更新韌體就沒有。這些漏洞是和 Prusa 協調後才公開，並已在 Buddy 韌體 7.0.0 之後的版本修補。
  question: Prusa 印表機現在還有風險嗎？
- answer: Dixken 表示他用了 Opus 4.8 和模糊測試工具，而資安研究只是他的業餘興趣。這顯示 AI 工具讓嚴肅的漏洞研究變得更快、更容易，防守方和攻擊方都一樣。
  question: 這次研究用到 AI 為什麼值得注意？
featured: false
lang: zh
publishedAt: '2026-11-10T12:18:07+00:00'
relatedSlugs: []
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/tech-industry/cyber-security/software-engineer-rickrolls-his-prusa-3d-printer-via-remote-code-execution-exploit-one-week-of-testing-with-claude-opus-uncovers-23-prusa-buddy-firmware-defects
summary: 一名業餘玩家借助 AI 模型與模糊測試工具，僅花一週就在 Prusa 印表機上找到一條可遠端執行程式碼的漏洞鏈。這顯示 AI 輔助的漏洞挖掘成本已低到業餘玩家也能負擔。
tags:
- cybersecurity
- ai-ml
- hardware
title: 軟體工程師利用遠端程式碼執行漏洞，讓自家 Prusa 3D 印表機播放「Rickroll」
trending: false
type: news
---

Software engineer Yannick Dixken spent a week attacking his [Prusa MK4S 3D printer](https://www.tomshardware.com/3d-printing/prusa-mk4s-review) in the name of science. At the end of the relatively short but intense period, he produced a video demonstrating the ability to Rickroll the printer via remote code execution (RCE). Dixken shared the video and findings – charting “roughly 23 individual defects” with Prusa and published his amusing but detailed [Never gonna print you up!](https://dixken.de/blog/never-gonna-print-you-up) blog in coordination with the 3D printer maker. Yes, all the vulnerabilities are now patched in the Buddy firmware versions >7.0.0.

Dixken is an experienced Freelance Cloud Architect, DevOps and Platform Engineer. [Security](https://www.tomshardware.com/tag/security) research is more of a hobby, he notes in the blog post, but it is clearly a passion strong enough to spend a whole week probing the MK4S for vulnerabilities. The result is far more than the funny old [Rickroll](https://www.tomshardware.com/maker-stem/rickroll-asic-heralded-as-a-world-first-this-chip-is-never-gonna-let-you-down). The week of debugging, fuzzing and reverse engineering “armed with Opus 4.8 and a fuzzer” resulted in “14 findings, roughly 23 individual defects, and a chain that ends with the printer's main controller running code I sent it over the network,” noted Dixken. “Yup, fully fledged RCE.”

The headlining RCE scored 8.1 and is officially described as High Severity. This serious bug was in the cloud (or self-hosted) management platform called Prusa Connect. You can see proof-of-concept code Rickrolling the user in Dixken’s embedded video. He sent this video to [Prusa](https://www.tomshardware.com/3d-printing/prusa-core-one-plus-indx-review).

The methods used to uncover these vulnerabilities are outlined in the source blog, if you’d like to know more. Meanwhile, there were many other vulnerabilities uncovered and cataloged. These include a USB filename attack, heap overflows triggered by malformed encrypted print files, and network denial-of-service flaws. Many of the bugs were probably symptoms of the original developers’ use of assert statements to enforce assumptions.

Happily for [Prusa 3D printer](https://www.tomshardware.com/3d-printing/3d-printing-legend-josef-prusa-takes-emergency-command-of-printed-solid-after-ceo-exit-prusa-holds-the-fort-as-successor-hunt-begins) users, Dixken has responsibly disclosed this multitude of vulnerabilities. The engineer says that within 24 hours of the Rickroll video being shared on social media, the 3D printing firm’s team coordinated professionally, efficiently, and kindly. Companies [don’t always react so positively](https://dixken.de/blog/i-found-a-vulnerability-they-found-a-lawyer) to those helping them find vulnerabilities in their wares.

*Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

## Summary

**TLDR:** A hobbyist using an AI model and a fuzzer found a remote code execution chain in a Prusa printer in a week. AI-assisted bug hunting is now cheap enough for hobbyists.

- Software engineer Yannick Dixken spent a week probing his Prusa MK4S 3D printer using Opus 4.8 and a fuzzer.
- He reported 14 findings covering roughly 23 individual defects, including a remote code execution chain.
- The main bug, in the Prusa Connect management platform, was rated 8.1 (High Severity).
- Dixken disclosed the issues in coordination with Prusa, and they are patched in Buddy firmware versions above 7.0.0.
- IoT devices that connect to cloud services face more pressure as AI tools make vulnerability research faster.

## 摘要

**重點摘要：** 一名業餘研究者用 AI 模型加模糊測試，一週內就在 Prusa 印表機找到遠端程式碼執行漏洞鏈。AI 輔助找漏洞已經便宜到業餘玩家也能做。

- 軟體工程師 Yannick Dixken 花了一週，用 Opus 4.8 和模糊測試工具檢查自己的 Prusa MK4S 3D 印表機。
- 他回報了 14 項發現，涵蓋約 23 個個別缺陷，其中包括一條遠端程式碼執行漏洞鏈。
- 主要漏洞位在 Prusa Connect 管理平台，評分 8.1，屬於高嚴重性。
- 他和 Prusa 協調後才公開，相關漏洞已在 Buddy 韌體 7.0.0 之後的版本修補。
- AI 工具讓找漏洞變快，會連網的物聯網裝置面臨的資安壓力也更大。