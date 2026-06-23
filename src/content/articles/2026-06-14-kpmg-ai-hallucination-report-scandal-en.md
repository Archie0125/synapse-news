---
title: "KPMG's AI Report Was Mostly Fabricated — And Nobody Caught It Until GPTZero Did"
summary: "KPMG's October 2025 report on agentic AI, distributed widely to enterprise clients, was found to contain only 5 accurate citations out of 45. GPTZero's investigation revealed fabricated case studies, 'vibe citations,' and factual claims contradicted by KPMG's own data. The firm pulled the report, but the episode raises uncomfortable questions about how AI-generated consulting work is reviewed."
category: "industry"
publishedAt: 2026-06-14
lang: "en"
featured: false
trending: true
sources:
  - name: "GPTZero Investigation"
    url: "https://gptzero.me/news/investigations-kpmg/"
  - name: "The Register"
    url: "https://www.theregister.com/ai-and-ml/2026/06/12/kpmgs-ai-report-turns-into-a-demo-of-ai-hallucinations/5255029"
  - name: "TechRadar"
    url: "https://www.techradar.com/pro/a-major-kpmg-report-on-ai-was-found-to-be-chock-full-of-ai-hallucinations"
  - name: "Swiss Info"
    url: "https://www.swissinfo.ch/eng/swiss-ai/kpmg-report-contained-ai-hallucinations-on-benefits-of-ai/91574511"
tags:
  - "KPMG"
  - "AI hallucination"
  - "consulting"
  - "enterprise AI"
  - "GPTZero"
  - "trust"
  - "accountability"
relatedSlugs:
  - "2026-06-13-openai-state-ag-multistate-subpoena-en"
  - "2026-06-13-trump-anthropic-fable5-mythos-export-controls-en"
---

The irony was almost too neat to be real. KPMG, one of the Big Four consulting firms, published a report in October 2025 titled "Total Experience: Redefining Excellence in the Age of Agentic AI." It was pitched as authoritative guidance on how enterprises should adopt AI. The problem, as GPTZero researchers discovered and published this week, is that the report appears to have been substantially written by the same AI systems it was advising clients about — and the AI got much of it wrong.

Of the report's 45 citations, GPTZero found that only five accurately pointed to their stated sources. The remaining 40 ranged from "mangled and misleading" to "partially fabricated" to simply too vague to verify. GPTZero called the pattern "vibe citing" — AI-generated references that sound credible, use real-sounding publication names and dates, and pass casual inspection, but don't actually support the claims they're attached to.

KPMG pulled the report from several of its websites after being contacted. The firm stated it was "reviewing the circumstances surrounding its publication." That statement, notably, did not concede that the report was AI-generated.

## What GPTZero Actually Found

The GPTZero investigation was methodical. Researchers categorized each of the 45 citations into three buckets: those that correctly pointed to a real source supporting the claim (5 citations), those that paraphrased real source titles with fabricated components or mangled the source in ways that made the citation misleading (28 citations), and those that were too vague or inaccurate to determine whether a real source exists at all (12 citations).

The factual errors were not minor formatting glitches. The report claimed that Emirates airline had adopted a mobile chatbot named "Sara" capable of changing flight bookings. In reality, Sara is a physical robot assistant that Emirates introduced in 2023 and that cannot alter reservations. The claim would be easy to verify with a single web search. It wasn't verified.

More embarrassing was an internal contradiction: the report cited a statistic that 55% of CEOs were prioritizing AI investment, sourcing the figure to KPMG's own 2025 CEO Outlook survey. The actual KPMG 2025 CEO Outlook showed 71% — a significant discrepancy from a report that cited itself, incorrectly.

Case studies described purported agentic AI deployments at UBS, Swiss Federal Railways, and Transport for London. Representatives from all three organizations disputed the characterizations. None confirmed the deployments as described in the report.

## Why This Is Harder to Fix Than It Looks

Enterprise consulting reports have always had a quality problem: they are expensive to produce, under deadline pressure, and reviewed by generalists who may not verify individual citations. AI assistance has accelerated production timelines substantially — and apparently, in at least this case, accelerated the pace of errors along with it.

The core problem with AI-generated citations is that they fail in a way that looks like success. A hallucinated citation includes a plausible author name, a realistic publication date, a credible-sounding journal or outlet. It can survive a skim-read by a senior partner who is checking the argument structure, not the bibliography. Systematic verification — actually pulling each source and confirming it says what the report claims — is time-consuming and culturally undervalued in consulting deliverables.

This is not purely a KPMG problem. Earlier this year, Deloitte was reported to have refunded the Australian government after AI-generated content appeared in a taxpayer-funded report. McKinsey, Accenture, and PwC have all disclosed significant internal use of AI in report production, though none have faced comparable public scrutiny of citation accuracy.

The question of accountability is genuinely difficult. If a consulting firm uses AI to draft a report that a human partner reviews and signs off on, who is responsible for fabricated citations — the firm's editorial process, the AI vendor, or the specific engagement team? Current consulting contracts do not address this clearly, and no regulatory framework in any major jurisdiction specifies disclosure requirements for AI-generated advisory content.

## The "Vibe Citing" Problem at Scale

GPTZero's coinage of "vibe citing" has already spread rapidly in AI-critical circles because it captures something specific: the problem is not that AI makes random errors. It is that AI generates errors that have the *feel* of correctness. The citation format is right. The author affiliation sounds plausible. The publication venue is respectable. The date is consistent with the claim. Everything except the underlying fact is accurate.

This matters for enterprise AI adoption for a specific reason. Organizations consuming AI-generated content — whether consulting reports, legal briefs, or medical literature reviews — must now build verification workflows for a failure mode that was previously rare. In a world of human-authored reports, a citation to "McKinsey Global Institute, 2023" could reasonably be assumed to exist and say roughly what was claimed. In an AI-assisted world, that assumption is no longer safe.

The irony extends further: the KPMG report's stated purpose was to help enterprise clients extract value from agentic AI. Some of its clients may have used the report's fabricated case studies to justify their own AI investments. The downstream consequences of bad AI-generated information about AI are genuinely difficult to trace.

## What Comes Next

GPTZero's investigation has prompted broader scrutiny. Several journalists and academic researchers have begun applying similar citation-auditing techniques to other high-profile AI-era consulting reports, and early results suggest the KPMG report may not be an outlier.

Several things would help. Mandatory AI disclosure — requiring consulting deliverables to state which sections were AI-assisted and how they were verified — is the most obvious intervention. Some jurisdictions are moving toward this for regulated industries; general consulting remains largely unaddressed. Automated citation verification tools, ironically, could also help: AI systems capable of checking whether a cited source says what is claimed are already available, and integrating them into the publishing workflow would catch the most obvious errors before they reach clients.

For KPMG, the reputational damage is substantial. The Big Four sell trust in their analytical rigor as their primary product. A report on AI credibility that is itself not credible is exactly the kind of story that circulates in boardrooms for years. The firm's response — pulling the report and citing an internal review — is the minimum viable response. Whether it does more depends on how much regulatory or client pressure develops in coming weeks.

For the broader enterprise AI ecosystem, the incident serves as a useful stress test of a proposition that AI vendors have been making for two years: that AI-assisted knowledge work, properly supervised, can be trusted. The KPMG case suggests the supervision part of that equation is harder to implement reliably than it looks.
