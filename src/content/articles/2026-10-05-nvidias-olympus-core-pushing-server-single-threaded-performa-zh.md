---
category: hardware
faqs:
- answer: Olympus 採用十路寬度的亂序執行設計，並配置非常大型的內部結構，希望每個時脈完成更多有效指令。這讓它即使只有 3.3 GHz，也能追求高效能。
  question: Olympus 如何提升伺服器的單執行緒效能？
- answer: 兩者在執行單元布局與半分散式排程上有相似之處，但 Olympus 加入同步多執行緒，亂序執行資源也更加龐大。
  question: Olympus 與 Arm Cortex-X925 有何差異？
- answer: 不代表。實際競爭力還取決於記憶體、互連、能源效率、多核心擴展、軟體相容性與整體平台成本。
  question: 單顆核心很快，就代表伺服器產品一定成功嗎？
featured: false
lang: zh
publishedAt: '2026-10-05T22:49:26+00:00'
relatedSlugs: []
sources:
- name: AnandTech / Chips and Cheese
  url: https://chipsandcheese.com/p/nvidias-olympus-core-pushing-server
summary: Olympus shows NVIDIA wants server CPUs to win on responsiveness, not just
  core count, potentially challenging assumptions that Arm must trade away desktop-class
  speed.
tags:
- hardware
- industry
title: 'NVIDIA’s Olympus Core: Pushing Server Single Threaded Performance Boundaries'
trending: false
type: news
---

Server chips traditionally offered less single threaded performance than contemporary client parts. Higher core counts translate to less power per core, and the complex interconnect required to connect many cores often suffer from higher latency as well. However, that trend has been narrowing. AMD’s recent server chips have been pushing higher frequencies over the last couple generations. NVIDIA’s Olympus is another aggressive move to push server single threaded performance forward, but approaches the problem from a different angle by focusing more on performance per clock.

To deliver on that front, Olympus takes a similar approach to Arm’s Cortex X925. Growing core structures tends to run into diminishing returns, so Olympus diverges from Arm’s approach with a simultaneous multi-threading (SMT) implementation. The result is a monster core that is a force to be reckoned with in the server scene, and one that gets very close to desktop performance.

# Overview

Olympus is a 10-wide out-of-order core with almost comically large out-of-order structures depending on where you look. It runs at a modest 3.3 GHz clock speed, which isn’t high these days even by server standards, so Olympus needs very strong per-cycle performance to meet NVIDIA’s performance goals.

At a high level, Olympus’s general layout has a lot in common with Arm’s Cortex X925. Both cores use a semi-distributed scheduler with a similar execution unit layout. Both aim to deliver high performance without having to reach the clock speeds that AMD and Intel’s cores do. However, Olympus takes that goal even further by increasing out-of-order structure sizes compared to X925. NVIDIA’s core also differs in a number of areas, like having a non-scheduling queue in front of the floating point schedulers.

# Branch Prediction

A wide core with deep reordering capacity has a lot to lose from branch mispredicts, so Olympus needs a strong branch predictor. In a test with various numbers of branches that are taken/not-taken with different pattern lengths, Olympus stops just short of Arm’s X925. X925’s direction predictor can track approximately 16-24K global history patterns with a few branches in play, or over 64K patterns with 512 branches. Olympus can get to roughly 5-6K patterns with a couple branches, or 48K with 512 branches.

In SPEC CPU2026, prediction accuracy is right up there with the best of Intel and AMD’s cores. Olympus overall is slightly behind AMD’s Zen 5, and slightly ahead of Lion Cove. Each core has individual wins and losses on different workloads, highlighting the difficulty of optimizing a branch predictor to cater for a wide range of program behaviors.

SPEC CPU2026’s floating point suite is generally easier on branch predictors, but still includes a couple of workloads with slight branch prediction challenges. Olympus comes out ahead of Intel and AMD in the floating point suite, mostly because of a large win in 731.astcenc.

Branch prediction speed is also crucial to feeding a wide, high throughput design because taken branches are quite common in code. Like AMD’s Zen 5, Olympus can do two taken branches per cycle across a large branch footprint. Unlike Zen 5 and Cortex X925, Olympus’s ability to do two taken branches per cycle is tied to instruction footprint rather than branch count, which could mean it’s tied to the instruction cache. Instruction footprints beyond 48 KB break the two branches per cycle capability. For those larger instruction or branch footprints, Olympus has a 16K entry BTB with 4 cycle latency.

NVIDIA partitions the branch target caching structures to give each thread about half of available capacity when the core is running two threads. The two threads cannot share targets, even if they belong to the same process and therefore share an address space. Sustained taken branch throughput remains at two branches per cycle from the fastest BTB level. When servicing two threads, the 16K entry L2 BTB can deliver a taken branch target every five cycles from each thread’s point of view, or roughly every 2-3 cycles from the core’s point of view.

NVIDIA and AMD both use ahead indexing to improve branch predictor throughput, meaning that one lookup provides predictions for the next two branches rather than a single branch. NVIDIA implies they can do this for their direction predictor and not just the BTB, letting them carry out more predictions per cycle for branches with dynamic behavior.

Olympus implements advanced predictors with robust ahead pipelining mechanisms delivering up to 2.3x higher predictions per cycle vs the competition

-Vera Whitepaper


Predicting with BTB pairs allows two fetches to be predicted in one prediction cycle

-AMD’s Zen 5 Optimization Guide


I tried setting up a test with conditional branches that were not-taken 1/8 of the time in a trivially predictable manner. I was hoping that would force the core to use the conditional predictor to at least validate what comes out of the BTB via ahead indexing. But if that causes an impact, I can’t see it in either Zen 5 or Olympus. Both cores can manage two taken branches per cycle if they have to use the branch predictor. I tried making the branches taken/not-taken in more complex patterns, but stopped putting more time into after the first couple attempts caused mispredicts on both cores.

NVIDIA further noted that Olympus could sustain more predictions per cycle compared to the competition, and cited specific SPEC CPU2026 integer workloads.

Validating this is difficult because neither architecture provides hardware counters to track how many predictions they made. I also don’t think predictions per cycle is a useful metric by itself, because predictions made after a mispredict are useless and more predictions per cycle may not impact performance if the frontend is already adequately fed. Another factor is the core’s design goals around performance per cycle rather than clock speed. Olympus may be averaging more predictions per cycle, but that could be because it’s moving along more of the instruction stream in a given number of cycles compared to Zen 5. Zen 5 in contrast is designed to clock high while still being able to sustain two taken branches per cycle, and the rate at which the two designs complete branches isn’t too far apart when clock speed is taken into account.

# Instruction Fetch

Fetch addresses from the branch predictor go through address translation with a 64 entry fully associative instruction TLB. Olympus then fetches instructions from a 64 KB, 4-way set associative instruction cache that can deliver 128 bytes per cycle into a 48 instruction decode queue. A 128 byte fetch can contain up to 32 instructions, which far exceeds the core’s decode throughput and possibly serves to let the frontend catch up if it meets a straight run of instructions after a long latency branch or mispredict.

Larger instruction footprints are handled well, with the core able to fetch 32B/cycle of instructions from the L2 cache. Per-cycle L2 code throughput for a single thread is much higher on Olympus than on Zen 5 or Cortex X925. Like many other cores, code read throughput drops sharply if instructions spill into L3.

Running two threads in the core causes a sharp drop in instruction fetch bandwidth before 1 MB, indicating that Olympus is statically partitioning the L2 cache. This applies even if the sibling thread is running a trivial loop that consists of several instructions, and doesn’t make any memory accesses that could cause data-side cache capacity contention. Throughput for a high IPC thread (NOPs only) is also cut in half even if the other thread is latency bound and stuck at low IPC.

# Rename and Dispatch

Micro-ops from decoded instructions need to go through register renaming and have appropriate tracking resources allocated in the backend. This process provides opportunities to carry out other optimizations like move elimination. Olympus can do move elimination to a limited extent. A chain of dependent MOVs executes at just over 1 per cycle, indicating that some MOVs executed with zero latency. AMD’s Zen 5 can impressively do this across 5 MOVs per cycle.

If the core runs two threads, Olympus’s per-thread move elimination capability strangely gets better. Per-thread dependent MOV throughput increases to 1.7 MOVs/cycle per thread, or 3.5 across both threads. Zen 5 improves as well, with per-core throughput increasing to 7 MOVs per cycle. However, that represents a drop in per-thread throughput from 5 to 3.5 MOVs/cycle.

# Backend Execution Engine

Olympus’s backend has massive register files and queues just about everywhere. It’s a bit like Cortex X925, but with many things taken up a notch. The only structure with a somewhat lower entry count is the FP/vector register file, which has fewer entries than Zen 5’s. However, Olympus compensates by often letting a 128-bit vector register hold a pair of scalar FP values written by separate instructions. It’s a useful optimization because a lot of code cannot be vectorized.

Testing with NOPs puts a very high ceiling on the number of instructions that Olympus can have in flight. The core can overlap two long latency loads with more than 1000 NOPs spaced between them, but the practical number of in-flight instructions is likely to be significantly lower because Olympus can only have a bit over 606 registers allocated. The \~606 allocated register limit applies on the architectural register side, because using the scalar FP optimization mentioned above still results in the number of allocated architectural registers capping out at 606.

Olympus’s schedulers are laid out similarly to those on Arm’s Cortex X925. Eight integer ALUs are arranged into pairs, with each pair fed by a scheduling queue with approximately 25 entries. One of the ALU pairs is special and can handle less common operations. Olympus and Cortex X925 both use a six-pipe FPU, again with a scheduling queue for each pair of pipes. However, NVIDIA uses a non-scheduling queue in front of smaller scheduling queues, while Arm uses three very large scheduling queues.

All of the backend structures I checked are statically partitioned, meaning that each thread gets half (or less) of a structure’s capacity when the sibling thread is not idle. That applies even to scheduling queues, which are often watermarked or competitively shared on other architectures. Static partitioning even extends to the execution units, with execution throughput cut in half regardless of whether the sibling thread is running instructions that hit the same ports. AMD’s SMT implementation for comparison flexibly shares most structures, though it sets limits (watermarking) to ensure one thread cannot unfairly monopolize a resource.

## Load/Store

Olympus executes memory accesses down a set of four pipelines, all of which can handle loads, and two of which can handle stores. The core’s L1 data cache has a nominal latency of four cycles, but a simple memory latency test can measure 2-3 cycles of L1D latency possibly because of value prediction.

Memory disambiguation behavior on Olympus has more in common with older cores from Arm or Intel’s Atom line. Olympus can do fast forwarding from a 64-bit store to a dependent 32-bit load as long as the load is aligned to either half of the store. Forwarding latency is 3-4 cycles for exact address matches, or 5-6 cycles when forwarding the upper half. All other overlap cases lead to a 12-13 cycle penalty, likely because the core blocks the load and waits for the store to commit.

Olympus encounters a strange hiccup when doing store forwarding across the 32B boundary in the middle of a 64B cacheline. It strangely doesn’t hiccup in the same way when accesses cross a 64B cacheline boundary, even though every 64B aligned boundary is of course also 32B aligned. Also, independent loads and stores that touch the same 32-bit block at the end of the first 32B half of a cacheline sometimes aren’t allowed to proceed in parallel.

Wider vector accesses show the same strange behavior at the middle 32B boundary, and show an additional hiccup at the first 16B aligned boundary into the cacheline. Latency for vector store forwarding is higher, which is typical for many cores.

For address translation, Olympus has a large 112 entry fully associative data TLB, backed by the unified 3K entry L2 TLB. Zen 5 for comparison has a 96 entry fully associative data TLB backed by a 4K entry L2 data TLB. AMD doesn’t use a unified L2 TLB, and stores instruction-side translations in a separate 2048 entry L2 instruction TLB. NVIDIA ran a kernel with 64 KB pages on the system we had access to, which extends TLB reach compared to using typical 4 KB pages. 64 KB pages basically meant that address translation latency was a non-factor for a lot of testing, but made direct comparisons difficult.

## Cache and Memory Access

Large out-of-order structures, prefetchers, branch prediction, and value prediction help a core tolerate memory access latency. Caches attack the problem from the other side by cutting memory latency for frequently accessed addresses. Vera’s caching strategy is greatly improved compared to NVIDIA’s prior Grace CPU. Olympus’s data memory hierarchy starts with a large 96 KB 6-way set associative data cache, which offers more capacity than the 32, 48, or 64 KB data caches often found on AMD, Arm, and Intel’s server cores.

L1 misses can be caught by a 2 MB 8-way set associative L2, which delivers 10-cycle load-to-use latency. The low cycle count latency means that Olympus’s L2 can deliver data nearly as fast as the Cortex X925’s 12-cycle L2, despite the X925’s higher 4 GHz clock speed. Having 2 MB of L2 capacity is a welcome improvement compared to Grace’s Neoverse V2 cores, which had to make do with 1 MB L2 caches. Vera’s L3 latency is comparable to Grace’s and isn’t great in absolute terms at over 120 cycles. However, that’s typical of designs that implement a L3 cache over a massive monolithic interconnect. Vera at least increases L3 capacity from 114 to 164 MB.

NVIDIA covers for high L3 latency with aggressive prefetching. A linear read pattern from a single thread achieves 88.53 GB/s from L3, and applying Little’s Law indicates that Olympus was able to sustain 50-51 outstanding requests to L3 (88.53 GB/s /(64B lines \* 3.3 GHz) = 0.42 cachelines per cycle, multiplied by 121.5 cycle latency = 50.9 requests in flight). Doing the same calculation for Grace/GH200 gives 35-36 requests in flight. As with many other cores, Olympus likely has a deeper queue for L2 misses than L1 misses. Testing with Lemire’s memory level parallelism microbenchmark shows that Olympus can have 18-19 demand L1D misses in flight. Lemire’s test uses a randomized pointer chasing pattern that won’t work with L2 prefetchers, and therefore won’t take advantage of a larger L2 miss queue.

Olympus’s SMT implementation partitions the L1D and L2 caches for data access too, meaning that each thread gets half the capacity of all core-private caches if the sibling thread is active. As with the instruction side, this partitioning applies even if the sibling thread makes no data-side accesses.

# Performance: SPEC CPU2026

SPEC CPU2026 scores show Olympus delivering very strong single threaded performance for a server core. It isn’t far off Intel and AMD’s latest cores in desktop settings, represented here with the Core Ultra 9 285K and Ryzen 7 9800X3D. Against Arm server competitors like Neoverse V2 and Neoverse N2, Olympus has no trouble pulling off a significant lead. A significant problem here is that the kernel on the test system we had access to uses 64 KB pages, while all other results are obtained with 4 KB pages. Estimating page size impact will be difficult, but I expect Olympus will still compare well against its Neoverse counterparts even with a smaller page size.

Examining individual scores show NVIDIA doing well across many integer workloads including the ones highlighted in their whitepaper (723.llvm\_r, 727.cppcheck\_r, 721.gcc\_r, 714.cpython\_r). Olympus’s large loss to Zen 5 in 706.stockfish\_r has more to do with instruction set differences than core architecture, because Olympus had to execute roughly twice as many instructions as Zen 5 did in that workload. ISA differences also affect 772.marian\_r on the floating point side. Instruction count can go the other way too, with aarch64 requiring fewer instructions for 750.sealcrypto\_r, but Zen 5 is able to maintain a strong performance in that workload thanks to its overall higher throughput design when taking clock speed into account.

Olympus’s goal is to achieve high single threaded performance by emphasizing performance per clock, and performance counters unsurprisingly indicate very high IPC. NVIDIA’s IPC is often higher than Zen 5’s, even in workloads where Zen 5 manages to deliver higher performance.

Wider pipelines are difficult to feed, and checking top-down performance events reveals that nearly all workloads leave over 50% of dispatch slots unused on average. SPEC CPU2026’s integer workloads lose a lot of throughput because the frontend couldn’t supply micro-ops fast enough (frontend bound), showing that even a fast two-ahead branch predictor and large instruction cache can’t always keep up. The same is true of [Zen 5 as well](https://chipsandcheese.com/p/evaluating-spec-cpu2026).

SPEC’s floating point workloads tend to be more backend bound, meaning that micro-ops couldn’t dispatch because a backend resource was full. In other words, the core reached a limiting factor for how many instructions it could keep in flight.

## “Spatial Multithreading”

SMT is a way to claw back unused core width and more efficiently utilize backend resources when a second thread is available. NVIDIA’s “spatial multithreading” takes a rather unconventional approach to SMT, and definitely shows promise when looking at SPEC CPU2026’s integer workloads. There, Olympus’s SMT gains are on par with Zen 5’s. Zen 5 is ahead in actual performance, but I’m focusing on gains here because again a client CPU is expected to maximize per-core performance.

Olympus’s gains are less convincing on the floating point side, though SPEC CPU2026’s floating point suite still enjoys a significant overall uplift.

Individual workloads show varied gains, with Zen 5 or Olympus getting more out of SMT on different subtests compared to the other. However, the general pattern is the same for both cores. Low IPC, frontend bound workloads like 723.llvm tend to see massive gains from SMT. Higher IPC, throughput bound workloads like 750.sealcrypto and 714.cpython don’t gain as much.

SPEC CPU2026’s floating point suite tends to be more backend bound, and Olympus’s SMT implementation surprisingly suffers throughput losses on 709.cactus and 782.lbm. SMT implementations ideally don’t lose overall throughput when using both threads, so Olympus’s spatial multithreading doesn’t seem ideal in those two workloads. Zen 5 also gains less from SMT in SPEC’s floating point workloads, but manages to avoid situations where using both SMT threads would be worse than running two tasks in serial.

## SPEC CPU2017

SPEC CPU2017 remains an interesting suite because it features difficult workloads without analogues in SPEC CPU2026. I also have more SPEC CPU2017 data on hand, including from systems I no longer have access to. That data shows Olympus beating several more server cores, including a Zen 5 server implementation. It also shows Olympus drawing even with AMD’s top end Zen 4 desktop chip, which is an impressive feat for a server core.

SMT gains in SPEC CPU2017 are even higher than in SPEC CPU2026, thanks to workloads that wreak havoc on branch predictors and suffer from backend memory latency. 505.mcf comes to mind.

Olympus again takes a few concerning SMT losses in the floating point suite. AMD’s Zen 4 isn’t immune, but its losses are comparatively light. A 3% or 1% performance decrease is far from ideal, but is likely less noticeable than 11.98% or 9.78% losses.

Explaining Olympus’s SMT behavior is difficult, because analyzing SMT test cases is harder than looking at single threaded ones. 709.cactus’s situation can be explained by L2 data MPKI increasing from 3.58 to 6.52 when the core is running two copies of the workload in its SMT threads. Then, the partitioned resources in the backend may be insufficient to deal with high L3 latency.

However, I can’t apply the same explanation for SPEC CPU2017’s 503.bwaves and 549.fotonik3d. 503.bwaves thrashes the L2 in both cases, with 32.12 MPKI for a single thread and 33.03 MPKI when running two threads. Top-down events indicate performance losses for non-memory bound reasons. 549.fotonik3d also suffers a lot of L2 misses (52.45 MPKI for a single thread, 57.13 for two threads), but again the relative difference isn’t too big. In general, Olympus’s spatial multithreading seems to deliver strong gains on par with a conventional SMT implementation for frontend bound workloads, but doesn’t handle as well with backend bound ones.

# Thoughts on Spatial Multithreading

NVIDIA’s spatial multithreading is less like a conventional SMT implementation, and more like dynamically splitting Olympus into two smaller cores when it’s running two threads. Just about every imaginable core resource down to the L2 cache is statically partitioned, so each thread can only access half of what’s available. This approach certainly eases performance analysis, because viewing the two SMT threads as two 5-wide cores is simpler than thinking about how two threads might dynamically use various core resources in, say, AMD’s Zen 5. I imagine it’s easier on the core design front too. NVIDIA doesn’t have to tune complicated mechanisms that ensure thread fairness because splitting everything in half already gives a fairness guarantee.

I think the jury is still out on whether spatial multithreading is a good idea or a simplification meant to ease NVIDIA’s first generation SMT implementation. Spatial multithreading shows promise by delivering gains on par with conventional SMT implementations in SPEC CPU’s integer workloads. In the best cases, Olympus demonstrates that how efficiently you can let two threads share resources might not matter if your core resources are sufficiently massive in the first place. However, gains can be inconsistent and even negative in backend-bound scenarios in SPEC’s floating point tests. It’s hard to tell whether those rough spots come from teething issues in a first generation SMT implementation, or from fundamental inefficiencies that arise from locking each thread into half of a core. I imagine a certain portion of SMT gains come from dynamically letting each thread dip into resources left under-utilized by its sibling, and limiting each thread’s ability to do that could negatively impact SMT gains.

As with any architectural feature, it’s probably best to wait and see if NVIDIA continues the same strategy. Successful architectural techniques tend to stay around for multiple generations and gain adoption across the industry. Whether that’ll happen with spatial multithreading is anyone’s guess.

# Final Words

Arm’s early server chips emphasized core count over per-core performance, but the Arm server scene has diversified as newer Arm cores took aim at higher performance targets. Now, NVIDIA’s Vera delivers top-notch single threaded performance and turns the situation around. NVIDIA is now the one with a lower core count (though 88 cores is still a lot in an absolute sense), and AMD’s server chips have more cores with less single threaded performance. There is some wiggle room in the SPEC results because of different page sizes, but I suspect that would only narrow the gap between Olympus and the fastest AMD server cores rather than changing their relative rankings.

Against its Arm Neoverse competition, Olympus dominates on per-core throughput terms thanks to both its high single threaded performance and its ability to increase throughput by running a second thread. Debating the merits of a conventional SMT approach versus Olympus’s spatial multithreading one doesn’t matter when Arm cores can’t simultaneously run a second thread at all. Olympus gains throughput from running a second thread in the vast majority of cases, and any throughput it gains widens the per-core performance gap between it and its Neoverse contemporaries. NVIDIA’s prior Grace chip is included in that mix. Vera is a huge step up from Grace, with both faster cores and more cores.

Olympus overall is a very exciting server core. Its performance shows the merits of a low frequency design that aims to maximize work done per clock cycle, and definitely pushes boundaries for single-threaded performance in a server. Other server core designers should take note, because performance in low-threaded workloads continues to be important even as server core counts continue to increase. I look forward to seeing NVIDIA further evolve this impressive core.

Chester, thank you for the comprehensive review & analysis!

However, could you please clarify what the SMT benchmarks measured? Since I think the rest of your testing is Rate N=1, did you simply perform a SPEC Rate test with N=2 and use something like taskset to force the threads onto the same physical core?

Chester, the tiny loop triggering the cache split caught my eye. I'd be curious to see a service paired with a small, continuously active background task, rather than two copies of the same benchmark. Does the fixed split make the slowest requests more predictable, or mostly leave one thread short of resources its neighbour isn't using?

## Summary

**TLDR:** Olympus shows NVIDIA wants server CPUs to win on responsiveness, not just core count, potentially challenging assumptions that Arm must trade away desktop-class speed.

- Olympus is a 10-wide out-of-order core designed to push server single-threaded performance close to desktop levels.
- Its 3.3 GHz clock is modest, so NVIDIA relies on high instructions-per-cycle performance and very large out-of-order structures.
- The design resembles Arm's Cortex-X925 in its broad layout and semi-distributed scheduling, but adds simultaneous multithreading and larger structures.
- Strong branch prediction is crucial because a misprediction wastes more work in such a wide core with deep reordering capacity.
- The architecture strengthens NVIDIA's server CPU ambitions, although platform power, scaling, software, and total cost will determine commercial impact.

## 摘要

**重點摘要：** Olympus 顯示 NVIDIA 不只想拚伺服器核心數，也要搶單執行緒反應速度，挑戰 Arm 必須犧牲桌機級效能的舊印象。

- Olympus 是十路寬度的亂序執行核心，目標是把伺服器單執行緒效能推近桌上型處理器。
- 它的 3.3 GHz 時脈並不突出，因此 NVIDIA 把重點放在每時脈效能與超大型亂序執行結構。
- 整體布局與半分散式排程和 Arm Cortex-X925 相似，但 Olympus 加入同步多執行緒，內部結構也更大。
- 核心越寬、可重新排序的指令越多，分支預測錯誤浪費的工作就越大，因此預測能力是關鍵。
- 這套設計強化 NVIDIA 的伺服器 CPU 野心，但功耗、擴展性、軟體支援與總持有成本才會決定商業結果。