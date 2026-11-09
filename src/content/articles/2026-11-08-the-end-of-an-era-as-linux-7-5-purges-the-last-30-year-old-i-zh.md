---
category: hardware
faqs:
- answer: Linux 7.5 預計移除核心中最後一段 Intel MMX 最佳化程式碼，位於軟體 RAID 的 XOR 運算。這項變更刪除 800 多行程式碼，只用
    12 行取代。
  question: Linux 7.5 要移除什麼？
- answer: 可以。Pentium MMX 和 Pentium II 系統在新核心上仍能使用軟體 RAID，只是少了 MMX 最佳化的加速路徑。
  question: 舊的 Pentium 電腦還能用軟體 RAID 嗎？
- answer: 就算幾乎沒人用，舊程式碼路徑仍需要持續維護和測試。移除後核心更精簡，開發者也能把心力放在現在大家實際使用的硬體上。
  question: 移除舊的最佳化程式碼有什麼意義？
featured: false
lang: zh
publishedAt: '2026-11-08T14:40:00+00:00'
relatedSlugs: []
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/software/linux/the-end-of-an-era-as-linux-7-5-purges-the-last-30-year-old-intel-mmx-optimizations-from-pentium-age-open-source-os-retires-ancient-1997-pentium-instructions-to-streamline-code
summary: Linux 用 12 行程式碼取代 800 行 MMX 程式碼，看似只是懷舊話題，但真正值得關注的是核心終於開始積極清理舊程式碼。
tags:
- open-source
- hardware
- developer-tools
title: 一個時代的終結：Linux 7.5 清除 Pentium 時期留下、已有 30 年歷史的最後一批 Intel MMX 最佳化程式碼
trending: false
type: news
---

[Linux](https://www.tomshardware.com/news/live/my-week-with-linux) developers are preparing to make Intel’s ancient MultiMedia eXtensions an irrelevance. Intel introduced MMX in the [Pentium](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-language-model-runs-on-a-windows-98-system-with-pentium-ii-and-128mb-of-ram-open-source-ai-flagbearers-demonstrate-llama-2-llm-in-extreme-conditions) era, but a patch expected to merge into mainline Linux 7.5 will remove the last remaining optimized software from the open-source OS. Expected to be released in 2027, the new kernel will wipe MMX-optimized code from its software RAID XOR code, explains [Phoronix](https://www.phoronix.com/news/Linux-Dropping-Last-MMX-Opt).

Admittedly, there wasn’t much left in Linux in terms of MMX optimizations. But few folks will be running the most modern kernels on [Pentium MMX](https://www.tomshardware.com/reviews/pentium-mmx-live-expectations,19.html) and [Pentium II](https://www.tomshardware.com/reviews/empire-strikes-back,23.html) chips in 2026. And most other MMX-optimized code disappeared from the OS half a decade ago, when some MMX-optimized memory management code was removed. Note that, if you are a determined late-90s Pentium devotee, you can still use software RAID, but it will lack the MMX fast path.

This is a classic case of Linux code housekeeping. With this change, the kernel will lose over 800 lines of code and replace them with just 12.

## Remembering MMX

Intel first introduced MMX Pentium chips in January 1997. Though I vaguely remember these processors being marketed as being enhanced by ‘MultiMedia eXtensions,’ Wikipedia insists that “MMX is officially a meaningless initialism\[6\] trademarked by Intel.”

In a subsequent trademark battle with longtime foe AMD, a document produced in court indicated that MMX stood for ‘Matrix Math Extensions.’ AMD relied on this to sidestep the trademark, as an initialism cannot be trademarked, according to the encyclopedic source.

Eventually, all rival x86 processors managed to integrate MMX instructions – so as not to be pushed into the shade during the multimedia boom. A surprisingly large number of non-Intel chips ended up offering MMX, too. Along with Pentium MMX chips, AMD, Centaur, [Cyrix](https://www.tomshardware.com/reviews/overclocking-guide,15-12.html), Rise, and [Transmeta](https://www.tomshardware.com/news/last-x86-via-chip-centuar-cns-cpu-tested) eventually offered MMX CPUs.

After MMX's marketing success, AMD pioneered [3DNow! instructions](https://www.tomshardware.com/news/3dnow-simd-extensions-phenom-sse,11128.html), and about a year later, Intel fired back with [SSE](https://www.tomshardware.com/reviews/cpus-amd-intel,101-17.html) and SSE2.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

*Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.*

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

- 
The Wikipedia phrasing seems misleading.
In today's 2026 software sure MMX probably does not do much. However at the time and for many years, I think MMX was benchmarked on and benchmarked disabled and had been show to produce worthwhile gains.
[Reply](https://forums.tomshardware.com/threads/the-end-of-an-era-as-linux-7-5-purges-the-last-30-year-old-intel-mmx-optimizations-from-pentium-age.3902088/)

## Summary

**TLDR:** Linux replacing 800 lines of MMX code with 12 is a nostalgia piece, but the real story is the kernel finally getting tough about legacy code.

- A patch expected in Linux 7.5 removes the last MMX-optimized code, which lives in the software RAID XOR routines.
- The kernel loses more than 800 lines of code, replaced by just 12.
- Intel introduced MMX Pentium chips in January 1997; most other MMX code in Linux was removed about five years ago.
- Software RAID will still work on Pentium MMX-era hardware, just without the MMX fast path.
- Implication: every line of legacy code costs maintenance time, and dropping paths almost nobody uses frees attention for modern hardware.

## 摘要

**重點摘要：** Linux 用 12 行取代 800 行 MMX 程式碼，看似懷舊新聞，真正的重點是核心終於狠下心清理歷史包袱。

- 預計併入 Linux 7.5 的修補，會移除最後一段 MMX 最佳化程式碼，位於軟體 RAID 的 XOR 運算。
- 核心因此少掉 800 多行程式碼，只用 12 行取代。
- Intel 在 1997 年 1 月推出 MMX Pentium；Linux 其他 MMX 程式碼大約五年前就已移除。
- Pentium MMX 時代的硬體仍能使用軟體 RAID，只是少了 MMX 加速路徑。
- 背後意義：每一行舊程式碼都要花維護成本，砍掉幾乎沒人用的路徑，才能把心力放在現代硬體。