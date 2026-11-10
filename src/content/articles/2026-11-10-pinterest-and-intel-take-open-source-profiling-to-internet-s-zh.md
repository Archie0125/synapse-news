---
category: developer-tools
faqs:
- answer: 兩家公司擴充了 Intel 的開源持續效能分析工具 gProfiler，加入動態分析、硬體遙測、wall-time 分析與效能計數器火焰圖，並強化它在
    Pinterest 網際網路規模機群上的穩定性。
  question: Pinterest 與 Intel 做了什麼？
- answer: Pinterest 在數十萬台實例上運行 Java、Python、C++、Go 和 Node.js 服務。各自為政的工具產出零散資料，很難跨語言、跨機器比對。
  question: Pinterest 為什麼需要統一的效能分析工具？
- answer: 回饋上游後，這些改進由更廣的社群共同維護，而不是只靠單一內部團隊。其他擁有多語言機群的公司也能直接使用，不必重新造輪子。
  question: 貢獻回開源有什麼意義？
featured: false
lang: zh
publishedAt: '2026-11-10T12:00:00+00:00'
relatedSlugs: []
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/pinterest-intel-profiling/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: Pinterest 選擇將自家剖析器的開發成果回饋至開源上游，而非閉門自建。這是一步高明的棋：押注共享基礎設施，勝過打造私有護城河。
tags:
- open-source
- developer-tools
- hardware
title: Pinterest 攜手 Intel，將開源效能剖析推向網際網路規模
trending: false
type: news
---

[Pinterest](https://en.wikipedia.org/wiki/Pinterest) has partnered with Intel to [extend gProfiler](https://medium.com/%40Pinterest_Engineering/open-source-profiler-on-an-internet-scale-fleet-pinterest-and-intel-partnership-on-gprofiler-8fcb387d899c), an open-source continuous profiler that provides production performance visibility across an internet-scale fleet of infrastructure.

Pinterest claims it operates hundreds of thousands of instances supporting 640 million monthly active users, with services written in [Java](https://www.java.com/en/), [Python](https://www.python.org/), [C++](https://en.wikipedia.org/wiki/C%2B%2B), [Go](https://go.dev/), and [Node.js](http://node.js). At that scale, even a small efficiency improvement can have significant infrastructure and cost implications. The challenge was that engineers were using separate tools such as perf, async-profiler, and py-spy, producing fragmented profiles that were difficult to correlate across languages and machines.

Rather than building another proprietary profiling platform, Pinterest worked with Intel to extend gProfiler and contribute those capabilities back to the open-source project. The collaboration adds dynamic profiling, hardware-level telemetry, wall-time profiling, and performance-counter flame graphs, while also hardening the system for large production fleets.

[gProfiler](https://github.com/intel/gprofiler) acts as an orchestration layer over several existing profilers. It combines system-wide perf data with runtime-specific tools such as async-profiler for Java and eBPF-based profiling for Python, producing a unified flame graph across the processes running on a host.

This is important for modern services where application execution crosses multiple layers. A Java application may spend time inside the JVM, native libraries, or the Linux kernel, while a Python service can involve interpreter, native, and kernel activity. Instead of requiring engineers to select and manually correlate separate profilers, gProfiler combines those views.

The agent discovers processes, starts the appropriate profilers, merges their stack traces, and uploads the resulting profile without requiring application code changes.

The new capability allows engineers to select services, hosts, or clusters and trigger profiling remotely through the UI or API. Agents normally remain dormant, consuming less than 1% CPU and 100 MB of memory, and receive profiling instructions through periodic heartbeats. You can change profiling frequency, duration, and the profilers used without redeploying the agent.

This effectively turns profiling into an operational capability rather than something that requires engineers to gain shell access to individual machines.

Integration with [Intel PerfSpect](https://github.com/intel/PerfSpect) allows gProfiler to collect hardware-level information such as cache behaviour, memory bandwidth, and CPU stalls. Pinterest also added [PMC flame graphs](https://en.wikipedia.org/wiki/Flame_graph), which correlate functions with hardware performance events such as cache misses and branch mispredictions.

Another addition is wall-time profiling. CPU profiling shows where processor time is being spent, but a service can still be slow while consuming relatively little CPU because threads are waiting on I/O, locks, or remote procedure calls. Wall-time profiling makes those waiting periods visible.

The gProfiler architecture separates collection from analysis. Agents run on individual hosts, while gProfiler Performance Studio aggregates and visualises the resulting profiles.

Profiles are stored in S3, passed through SQS for asynchronous indexing, and stored in ClickHouse for analytical queries. A React frontend provides flame-graph exploration, while aggregated data allows engineers to compare profiles across hosts, services, and time periods.

Pinterest and Intel also hardened the platform for production, addressing issues involving agent resource consumption, disk usage, and multi-terabyte ingestion before deploying it across the fleet.

gProfiler sits in an increasingly crowded continuous-profiling landscape. [Parca](https://www.parca.dev/) and [Grafana Pyroscope](https://grafana.com/oss/pyroscope/) use [eBPF](https://ebpf.io/) and related sampling technologies to provide fleet-wide profiling, while commercial platforms such as [Datadog](https://www.datadoghq.com/) offer continuous profiling alongside broader observability capabilities.

The distinction with gProfiler is its emphasis on system-wide, multi-runtime profiling and open-source extensibility. Rather than replacing tools such as perf or async-profiler, it orchestrates them. It also adds hardware-level profiling through Intel's tooling.

[Intel's VTune](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html) provides much deeper processor and application performance analysis, but it was designed primarily as a performance-engineering tool rather than a cloud-native fleet profiler. Pinterest specifically notes that this difference influenced the decision to build on gProfiler rather than adapt VTune for its environment.

At small scale, profiling is usually something an engineer enables when a performance problem appears. At Pinterest's scale, the cost of waiting for engineers to reproduce problems or manually profile machines becomes too high. Continuous profiling provides a baseline, while dynamic profiling allows teams to investigate specific anomalies when they occur.

By combining runtime profiles, system behaviour, and hardware performance data under an open-source platform, Pinterest is effectively making profiling another layer of production observability.

## Summary

**TLDR:** Pinterest chose to upstream its profiler work to open source instead of building in-house, a smart bet that shared infrastructure beats a private moat.

- Pinterest and Intel extended gProfiler, an open-source continuous profiler, to run across Pinterest's fleet of hundreds of thousands of instances serving 640 million monthly active users.
- Engineers had been piecing together fragmented output from perf, async-profiler and py-spy across Java, Python, C++, Go and Node.js services.
- gProfiler orchestrates existing profilers into one unified flame graph per host, covering JVM, interpreter, native and kernel time.
- New contributions include dynamic profiling, hardware-level telemetry, wall-time profiling and performance-counter flame graphs, all hardened for large production fleets.
- At this scale, small efficiency gains turn into large infrastructure savings, and that is the real business case.

## 摘要

**重點摘要：** Pinterest 沒有自建效能分析平台，而是把成果貢獻回開源。這一步押得很聰明：共享的基礎設施勝過自家護城河。

- Pinterest 與 Intel 合作擴充開源持續效能分析工具 gProfiler，讓它能在 Pinterest 數十萬台實例上運行，這些實例服務 6.4 億月活躍使用者。
- 過去工程師得在 Java、Python、C++、Go、Node.js 服務之間，拼湊 perf、async-profiler、py-spy 各自產出的零散資料。
- gProfiler 負責統籌現有的分析工具，在每台主機上產出統一的火焰圖，涵蓋 JVM、直譯器、原生程式碼與核心層。
- 這次新增了動態分析、硬體層遙測、wall-time 分析和效能計數器火焰圖，並針對大型正式環境做了強化。
- 在這種規模下，一點點效率提升就能省下可觀的基礎設施成本，這才是真正的商業理由。