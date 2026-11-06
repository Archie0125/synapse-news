---
category: hardware
faqs:
- answer: Qualcomm moved from an all-big-core strategy to a hybrid configuration.
    The X2E96100 combines six prime cores with 12 smaller performance cores.
  question: What changed in Snapdragon X2 Elite’s CPU design?
- answer: Although Qualcomm calls them performance cores, they target lower power
    and performance points than the prime cores. They handle background work and lightweight
    applications while contributing extra throughput when workloads scale.
  question: Why does the article treat Qualcomm’s performance cores as efficiency
    cores?
- answer: The key evidence will be measured performance per watt across light tasks
    and sustained multithreaded workloads. Comparisons with Intel’s Skymont and other
    hybrid processors will show whether Qualcomm’s architectural investments overcome
    the narrower core design.
  question: What should determine whether this design is genuinely competitive?
featured: false
lang: en
publishedAt: '2026-10-24T23:13:33+00:00'
relatedSlugs: []
sources:
- name: AnandTech / Chips and Cheese
  url: https://chipsandcheese.com/p/performance-oryon-qualcomms-little
summary: Qualcomm’s smaller Oryon core looks modest on paper, but its balanced design
  suggests efficiency cores are becoming serious throughput engines, not background-task
  leftovers.
tags:
- hardware
- industry
title: '“Performance” Oryon: Qualcomm’s Little Core'
trending: false
type: news
---

Qualcomm’s Snapdragon X2 Elite uses a hybrid core setup, breaking away from the all-big-core strategy that the company previously used with in-house core designs. The Snapdragon X2 Elite Extreme X2E96100 contains 18 cores, divided into 6 “performance” cores and 12 “prime” cores. Qualcomm’s “performance” cores fill the same role as little cores or efficiency cores on other chips, so I’ll be calling them E-Cores for simplicity. Like E-Cores on other chips, Qualcomm’s E-Cores are optimized for lower power and performance points than their big-core counterparts. These smaller cores can contain background tasks and lightweight applications that don’t require maximum performance, which saves power by not waking up the big cores. Under heavy multithreaded workloads, the E-Cores can step in to boost overall throughput.

Here, I’ll be looking at Qualcomm’s E-Core architecture in the Asus Zenbook A16 UX3607OA, which Asus has kindly sampled.

# Core Overview

Qualcomm’s E-Core is a 4-wide out-of-order architecture running at 3.6 GHz, making it a modest affair next to the likes of Intel’s Skymont, or even the older Crestmont architecture used in Intel’s last-gen Meteor Lake chip. But despite being “only” a 4-wide core, Qualcomm’s E-Core can still punch pretty hard thanks to a combination of good branch prediction, substantial backend resources and large, low-latency caches.

On the instruction set side, Qualcomm’s E-Cores support SVE2 and SME to maintain consistent ISA extension support across the chip. Both features are new to the Snapdragon X2 Elite, since Qualcomm’s prior Snapdragon X Elite lacked SVE support. Besides vector extensions, Qualcomm supports a grab bag of security-focused ISA extensions like pointer authentication and memory tagging (MTE).

# Frontend: Branch Prediction

Branch prediction can heavily affect both performance and power efficiency, so even density optimized cores have to make substantial investments into fast and accurate branch prediction. For their E-Core, Qualcomm has decided on a branch predictor that does well on the basics, but doesn’t incorporate some of the bling seen on the latest branch predictors on recent AMD, Arm, and Intel cores. A 1024 entry branch target buffer (BTB) is fast enough to deliver back-to-back predictions for taken branches. Intel and AMD’s big cores as well as density optimized cores from Arm like the Neoverse N2 can do two taken branches per cycle. Unlike Qualcomm’s prior Oryon core in the Snapdragon X Elite, the 1024 entry BTB here seems to be decoupled from the L1 instruction cache. Measured capacity doesn’t vary depending on code footprint or branch spacing.

Throughput drops to one taken branch every three cycles once the test spills out of the 1024 entry BTB, with another slowdown visible after exceeding the 128 KB L1 instruction cache’s capacity. Qualcomm might be using a second level BTB tied to the instruction cache, or could even be calculating direct branch destinations as those instructions arrive at the decoder. While doing so is simpler and more area efficient than implementing a very large L2 BTB, it does mean the branch predictor can’t follow taken branches after an instruction cache miss. That could limit the core’s ability to accurately prefetch instructions over large code footprints.

For direction prediction, Qualcomm’s E-Core can recognize fairly long patterns and handle a lot of them. The core can track roughly 16K patterns with 512 branches in play, or somewhere around 1K patterns with a single branch. Prediction accuracy across Geekbench 7’s workloads is roughly on par with Arm’s Neoverse N2, and better than Arm’s Neoverse N1.

A 40 entry return stack helps predict returns, and can sustain a call+return pair every two cycles. That’s a taken branch every cycle on average, making Qualcomm’s return stack faster than the one on AMD’s Zen 5 or Intel’s Skymont. In capacity terms, Qualcomm’s return stack lands in the middle of the pack. It’s much smaller than the 128 entry structure in Intel’s Skymont and Crestmont, but larger than the 24 entry one on Lion Cove.

Capacity has to be taken in context though. Some cores like Intel’s Lion Cove seem to fall back to an alternate predictor on a return stack underflow, letting them avoid mispredicts. Qualcomm’s E-Core and Intel’s Skymont in contrast see taken branch latency rise to over a dozen cycles, which is high enough to indicate mispredicts. It’s a story of different designs striking a balance in different ways. One approach is to design a small return stack with only a minor penalty on underflow. Another is to create a larger return stack so you only have to worry about the underflow case once in a blue moon. Qualcomm is leaning towards the latter. A 40 entry return stack should be plenty, though it stops short of Skymont’s crazy structure.

# Frontend: Instruction Fetch

Qualcomm strikes a similar balance with the instruction cache. A 128 KB instruction cache is much larger than the 64 KB or 32 KB ones found on contemporary designs, which helps the core avoid having to fetch instructions from L2. If code does spill out to L2, frontend bandwidth drops to about two instructions per cycle. It’s not bad, but it is lower than what Skymont can sustain from its shared L2.

The L2 cache acts like a last level cache for the CPU, so missing it leads to very poor instruction bandwidth.

# Dispatch

After the decoders translate instructions into micro-ops, the core has to allocate backend tracking resources for those micro-ops for bookkeeping throughout the out-of-order execution process. That process is a convenient place to carry out optimizations that expose extra parallelism to the backend, and Qualcomm does some of this. Move elimination is one example, and Qualcomm’s E-Core can do this for up to two dependent register-to-register MOVs per cycle. Eliminated MOVs execute with zero latency, as the renamer “executes” them by manipulating the register alias table to point multiple architectural registers to the same physical one.

Putting chained, dependent MOVs too close together seems to create a hazard that causes move elimination to fail. An uninterrupted chain of dependent MOVs executes at 1.38/cycle, indicating that some MOVs get eliminated, but others have to be carried out by the downstream execution units. Interleaving NOPs so that there’s no more than two MOVs in every four instructions (i.e., a decode group) brings throughput up to two dependent MOVs per cycle. Move elimination efficacy decreases depending on how many dependent MOVs go together in the same decode group.

Independent MOVs can execute at four per cycle. Even though latency isn’t a concern with independent instructions, move elimination still provides benefits because eliminated MOVs don’t need a physical register allocated, which increases reordering capacity.

Qualcomm can also eliminate adds with small immediates, though with an implementation that’s quite limited compared to what Intel has been doing. Add-immediate elimination is subject to the same two per cycle limitation as move elimination, and furthermore requires the sum of immediates in eliminated adds to be 255 or less. To give an example, `add x13, x13, 254` and `add x13, x13, 1` can be optimized, but two `add x13, x13, 128` instructions cannot. Intel’s add-immediate optimization on Golden Cove has higher throughput and works with [larger immediates](https://zenn.dev/herumi/articles/add-imm-fusion?locale=en).

Zeroing registers by MOV-ing an immediate value of zero into them doesn’t get special treatment. Qualcomm still has to allocate a physical register to hold the zeroed value.

# Backend

Qualcomm has selected reorder buffer and register file sizes closer to those of AMD’s Zen 4, rather than the likes of older 4-wide cores like Intel’s Skylake and Arm’s Neoverse N1. Other supporting structures like memory ordering queues are sized more in line with Skylake, though they’re still slightly larger.

Scalar integer execution is a primary focus on Qualcomm’s E-Core, with four ALU ports that match core width. These are fed by a distributed scheduler, which feeds each ALU port with a 19 entry scheduling queue. Three of the ALU ports can handle flag-setting instructions like SUBS/CMP, and one port can execute integer multiplies with 3 cycle latency. Two ports can resolve branches, though that throughput can only be sustained with not-taken branches because taken branches are bottlenecked by branch prediction throughput.

Floating point and vector execution isn’t emphasized as much, but Qualcomm has still created a reasonable two-port FPU for an efficiency focused core. Both FP/vector ports can execute common FP and integer vector operations, as well as cryptography ops like aese. Execution latency is about average for a modern core.

SVE is supported with a 128-bit vector length, meaning that SVE’s benefits will come from new instructions and prediction support rather than making more compute throughput available. One of the FP pipes can handle comparisons that write a predicate register, like `cmpeq`. Predicate instructions that don’t access vector registers, like SVE’s `while` instructions, can issue through an integer pipe to conserve vector/FP issue bandwidth. The core can only issue one `while*` instruction per cycle, so maybe only one of the integer pipes can write to the predicate register file. SVE also introduces non-contiguous memory accesses.

# Load/Store

Qualcomm’s E-Core has two memory access pipes, both of which can service loads or stores. Store forwarding latency is 6-7 cycles for all cases where an older store overlaps a load, regardless of the load’s alignment within the store. Impressively, Qualcomm avoids a failed store forwarding penalty in partial overlap cases. On the other hand, Qualcomm doesn’t have a very fast case for exact address matches the way Skymont does.

## Address Translation

To speed up virtual to physical address translation, Qualcomm uses very large translation lookaside buffers (TLBs) to cache frequently used translations. Qualcomm’s slides indicate that the Snapdragon X2 Elite’s big cores have a 224 entry, 7-way set associative L1 DTLB backed by a 8K entry L2 TLB.They didn’t specify TLB capacity for the E-Core, but performance counters suggest very large TLBs on it as well.

L1 DTLB misses start ticking up as test sizes exceed 768 KB, suggesting a 192 entry L1 DTLB. L2 misses start after 32 MB, which is consistent with a 8K entry L2 TLB. Getting a translation out of the L2 TLB takes more than eight cycles, based on comparing L2 latency using 4 KB and 2 MB pages.

Qualcomm’s TLBs support 4 KB and 64 KB small pages sizes, though curiously not 16 KB pages. Windows uses 4 KB pages, and Linux usually uses 4 KB pages as well. However, Ubuntu does offer a kernel version with 64 KB pages.

# Cache and Memory Access

A 64 KB L1D cache serves as the first stop for memory accesses, and delivers 3 cycle load-to-use latency. Indexed addressing increases latency to 4 cycles. It’s a good combination of speed and capacity, considering that many other modern cores have smaller 32 KB or 64 KB L1D caches and start with 4 cycle latency.

L1D misses head to a shared L2 cache. Unlike many other designs, but like Apple’s M1, Qualcomm doesn’t use a core-private mid-level cache. L2 latency is 21 cycles, or just two cycles more than Skymont’s 4 MB shared L2. While Skymont does have better actual L2 latency thanks to higher clock speeds, Qualcomm’s L2 is very fast for the capacity it offers.

SVE adds scatter/gather instructions, which lets one instruction access memory from non-contiguous memory locations. Gathers execute at a pedestrian pace of roughly one element per cycle. There’s no sign of a “combined gather” ability as described by Fujitsu for their A64FX and Monaka cores, where two elements fetched from the same 64B or 128B block can be handled with a single flow. Latency for a gather instruction is high at just under 4 ns, or 14 cycles. High gather latency is typical. For comparison, gathers on Intel’s Skymont execute with 3.7 ns of latency on a L1D hit, or 17 cycles.

L1D bandwidth is modest at 32 bytes per cycle, limited by the core’s 128-bit vector width and two memory pipelines. A linear read pattern achieves slightly more than 16 bytes per cycle from test sizes that fit in L2, with no bandwidth decrease when the array spills out to DRAM. Qualcomm’s L2 can deliver more than 32 bytes per cycle to a core even though the core can’t operate on that much bandwidth. That can be shown by only loading a subset of the data in each 64B cacheline. Any L1D miss will cause a fill for the entire 64B cacheline regardless of how much of that data the core ultimately uses, so “raw” L2 bandwidth can be inferred from the number of 64B lines touched.

The L2 bandwidth can provide just over 400 GB/s of read bandwidth to the six E-Cores it’s connected to. Per-core L2 bandwidth therefore doesn’t decrease under load, and remains at about 18 bytes per core cycle. Touching only the first 128 bits of each 64B cacheline as described above implies that Qualcomm’s L2 can offer over 500 GB/s of raw bandwidth, even though the cores can’t operate on all of it. Intel’s Skymont for comparison has smaller caches at the cluster level, with more per-core cache bandwidth to feed the higher throughput Skymont architecture.

# Final Words

A 4-wide, 3.6 GHz core isn’t flashy next to Intel’s 8-wide, 4.6 GHz Skymont, or AMD’s Zen 5c that uses the same architecture as its higher performance counterpart, albeit with a different physical implementation. But Qualcomm’s conservative E-Core architecture is a deliberate decision. The company is perfectly capable of delivering fast, high throughput cores, as shown by the 9-wide, 5 GHz P-Cores on the same chip. For their E-Cores though, Qualcomm seems to be focusing harder on reducing power consumption than increasing throughput for multithreaded applications. While not explicitly stated in Qualcomm’s slides, the “performance” core cluster seems aimed at containing lightweight applications and background tasks. “Efficiency” is probably a better term for the cluster.

For handling less performance critical tasks, a 3.6 GHz, 4-wide core looks like a good design point. Higher throughput cores are harder to feed and run into diminishing returns as any hiccup tends to leave more pipeline slots unused. Meanwhile, a narrower core is easier to build. A renamer for example has to check each instruction for dependencies on all previous instructions in that rename group. An instruction queue needs enough read and write bandwidth to handle core width. A decoder might need checks across multiple slots to determine whether multi-uop instructions can be handled in the same cycle. All of that complex logic can be seen as unused transistors whenever a pipeline slot goes unused. Intel stayed with 4-wide designs all the way from Core 2 in 2006 to Skylake in 2015, and likely with good reason. A 3-wide design probably runs into too many situations where core width becomes a limiter, while a 5-wide one starts dipping more into diminishing returns.

Thanks for the analysis!

I think the contrast between Qualcomm and Intel's approach to E-cores is very interesting. Intel seems to use them primarily as an efficient way to scale multithreaded performance, while Qualcomm seems to have added these for similar reasons as the LPE cores included in Intel's laptop SoCs since Meteor Lake. I gather the little Oryon's primary purpose is to avoid waking up the clusters of big cores, when the machine is just doing low-intensity stuff.

According to some benchmarks I've seen, these are about half as fast as the X2's big Oryon core (about 54% on integer, 48% on floating point). So, a much bigger gap than Intel's current P vs. E cores (which are about 77% as fast on integer, 73% as fast on floating point, in the 270K+).

I liked the return-stack comparison between running out less often and paying a smaller penalty when it happens.

## Summary

**TLDR:** Qualcomm’s smaller Oryon core looks modest on paper, but its balanced design suggests efficiency cores are becoming serious throughput engines, not background-task leftovers.

- Snapdragon X2 Elite abandons Qualcomm’s previous all-big-core approach for six prime cores and 12 smaller performance cores in its 18-core configuration.
- The smaller cores operate like conventional efficiency cores, handling lightweight tasks at lower power while adding throughput under heavy multithreaded loads.
- Despite a 4-wide design and 3.6 GHz clock, strong branch prediction, ample backend resources, and large low-latency caches help the core outperform its modest specifications.
- SVE2, SME, pointer authentication, and memory tagging give both core classes consistent vector and security capabilities.

## 摘要

**重點摘要：** 高通的小型 Oryon 核心規格看似保守，實際設計卻證明效能核不再只是處理背景工作，也能成為多執行緒運算的主力。

- Snapdragon X2 Elite 不再沿用全大核策略；其 18 核版本由 6 顆 Prime 核心與 12 顆較小的 Performance 核心組成。
- 這批小核心的實際定位就是效能核：平時以較低功耗承接輕量工作，重度多執行緒負載時再補上整體吞吐量。
- 雖然架構只有四路寬、時脈為 3.6 GHz，但分支預測、後端資源與低延遲大快取彌補了紙面規格的不足。
- SVE2、SME、指標驗證與記憶體標記讓大小核心維持一致的向量運算及安全功能。