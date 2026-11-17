---
category: ai-ml
faqs:
- answer: JioHotstar 比較了六種協助 AI 程式碼代理理解大型程式庫的方法：一般檔案系統工具、Sourcebot、Graphify、CocoIndex
    Code、Repowise，以及自建的 RAG 流程。測試用 Claude Sonnet 在 SWE-bench 子集、CodeScaleBench 和內部問答測試上進行。
  question: JioHotstar 測試了什麼？
- answer: 要看任務類型。Sourcebot 這類結構化程式碼搜尋在需求明確的工程任務上表現好，在較難的 SWE-bench Verified 題目上勝過基準而且成本更低；需求模糊時，語意檢索比較有幫助。
  question: 哪種方法表現最好？
- answer: 多加檢索層不會自動讓程式碼代理變強，還可能增加 token 成本。投資複雜的檢索架構前，團隊應該先在自己的程式庫上和簡單的檔案系統基準做比較。
  question: 工程團隊可以學到什麼？
featured: false
lang: zh
publishedAt: '2026-11-11T14:28:00+00:00'
relatedSlugs: []
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/jiohotstar-codingagent-retrieval/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: JioHotstar 的基準測試讓程式碼 RAG 熱潮冷靜了下來：單純的檔案系統搜尋表現就相當不錯，額外加上的檢索層往往只是徒增成本。
tags:
- ai-ml
- developer-tools
title: JioHotstar 實測 AI 程式碼代理的知識庫方案
trending: false
type: news
---

JioHotstar evaluated [six approaches to helping AI coding agents navigate large codebases](https://blog.hotstar.com/what-we-learned-from-benchmarking-knowledge-bases-for-coding-agents-6bbdd9e53727), finding that structural code search performed well on clearly defined engineering tasks, while semantic retrieval helped more with ambiguous requirements. The evaluation also found that adding retrieval layers did not consistently improve task completion or reduce token consumption.

[Abhishek Bansal](https://www.linkedin.com/in/abhishek-bansal/), Senior Staff Engineer at JioHotStar, compared filesystem tools, [Sourcebot](https://github.com/sourcebot-dev/sourcebot), [Graphify](https://github.com/Graphify-Labs/graphify), [CocoIndex](https://github.com/cocoindex-io/cocoindex-code) Code, [Repowise](https://github.com/repowise-dev/repowise), and an in-house retrieval-augmented generation (RAG) pipeline. The team evaluated the approaches using subsets of [SWE-bench](https://www.swebench.com/SWE-bench/) and [CodeScaleBench](https://github.com/sourcegraph/CodeScaleBench), alongside a custom question-answering harness for JioHotstar's codebase. The experiments used Claude Sonnet as the solving model and measured task accuracy, token consumption, agent turns, and tool usability.

*JioHotstar’s benchmark setup for evaluating code retrieval approaches for AI coding agents. (Source: [JioHotstar Blog Post](https://blog.hotstar.com/what-we-learned-from-benchmarking-knowledge-bases-for-coding-agents-6bbdd9e53727))*

The filesystem baseline, which relied on locally checked out repositories and standard search and file operations, remained competitive on concrete tasks. Sourcebot, which provides indexed text search, symbol definitions, references, and file reads, performed better than the baseline on harder SWE-bench Verified tasks while also costing less. On simpler SWE-bench Lite tasks, retrieval generally added overhead without consistently improving results.

CodeScaleBench showed a different pattern. Semantic retrieval helped more when agents had to interpret ambiguous problem descriptions and map them to implementation details that were not obvious from exact text or symbol searches. The findings suggest that retrieval approaches should be selected according to task characteristics rather than treated as interchangeable solutions.

The report also highlighted the importance of tool design. Agents frequently preferred familiar developer operations such as searching text, reading files, and locating symbols over higher-level abstractions that required additional verification.

Tool call breakdown by category across coding agent knowledge base approaches. *(Source: [JioHotstar Blog Post](https://blog.hotstar.com/what-we-learned-from-benchmarking-knowledge-bases-for-coding-agents-6bbdd9e53727))*

[Siddharth Vaithinathan](https://www.linkedin.com/in/siddharth-vaithinathan-629a8150/) raised a broader architectural question in a [LinkedIn post discussing the study](https://lnkd.in/p/g2whwQcd):

Whether coding agents should understand not only the code but also the company that produced it. He argued that repository indexing alone cannot capture why architectural decisions were made, which constraints shaped them, or what earlier incidents taught the engineering team.


Vaithinathan suggested extending agent knowledge beyond code and documentation to include architecture, constraints, decisions, rationale, incidents, and outcomes. Such context could help agents evaluate existing design choices before proposing changes, particularly in systems where historical operational experience influences architectural decisions.

[Tarun Bhargava](https://www.linkedin.com/in/tarun-bhargava-3300954b/) raises a relevant question for benchmark interpretation, particularly when evaluations use limited subsets and probabilistic models.

Cost/accuracy numbers with multiple runs of the same setup.


JioHotstar's evaluation did not identify a single retrieval approach that performed best across all tasks. Instead, JioHotstar recommends retaining filesystem tools as a baseline, using structural search for concrete, code-focused problems and semantic indexing for ambiguous or cross-cutting requirements. JioHotStar engineering team also emphasizes measuring tool-use traces alongside task accuracy to determine whether retrieval reduces unnecessary exploration. The findings highlight the importance of matching retrieval capabilities to the programming task and how the agent navigates the codebase.

## Summary

**TLDR:** JioHotstar's benchmark is a reality check for the code-RAG hype: plain filesystem search held up well, and extra retrieval layers often just added cost.

- JioHotstar compared six approaches for helping coding agents navigate large codebases, using Claude Sonnet on SWE-bench, CodeScaleBench and an internal QA harness.
- A filesystem-tools baseline stayed competitive on concrete tasks; on simpler SWE-bench Lite tasks, retrieval mostly added overhead.
- Sourcebot, which offers indexed search, symbols and references, beat the baseline on harder SWE-bench Verified tasks at lower cost.
- Structural code search worked best for well-defined tasks, while semantic retrieval helped more with ambiguous requirements.
- Adding retrieval layers did not consistently improve task completion or reduce token use.

## 摘要

**重點摘要：** JioHotstar 的評測給程式碼 RAG 熱潮澆了冷水：一般的檔案系統搜尋表現不差，多加的檢索層常常只是多花錢。

- JioHotstar 用 Claude Sonnet 在 SWE-bench、CodeScaleBench 和內部問答測試上，比較六種協助程式碼代理理解大型程式庫的方法。
- 只用檔案系統工具的基準方法在具體任務上依然有競爭力；在較簡單的 SWE-bench Lite 上，檢索大多只增加負擔。
- 提供索引搜尋、符號定義與引用查詢的 Sourcebot，在較難的 SWE-bench Verified 任務上勝過基準，而且成本更低。
- 需求明確時結構化程式碼搜尋最好用，需求模糊時語意檢索比較有幫助。
- 多疊幾層檢索並沒有穩定提升完成率，也沒有穩定減少 token 用量。