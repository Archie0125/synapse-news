---
title: "SAP Acquires Prior Labs to Expand AI Capabilities for Structured Data"
summary: "SAP has signed a definitive agreement to acquire German AI startup Prior Labs, pledging over €1 billion in investment to establish it as a globally leading frontier AI lab focused on tabular and structured business data. Prior Labs, founded by machine learning researcher Frank Hutter and colleagues, pioneered Tabular Foundation Models — including the TabPFN series published in Nature — which predict business outcomes directly from structured data without traditional ML engineering."
category: "startups"
publishedAt: 2026-05-06
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "SAP Newsroom"
    url: "https://news.sap.com/2026/05/sap-to-acquire-prior-labs-establish-frontier-ai-lab-europe/"
  - name: "CIO Dive"
    url: "https://www.ciodive.com/news/sap-buys-dremio-prior-labs/819263/"
  - name: "TechTarget"
    url: "https://www.techtarget.com/searchdatamanagement/news/366642794/SAP-acquisitions-of-Dremio-Prior-Labs-target-AI-development"
  - name: "HPC Wire"
    url: "https://www.hpcwire.com/aiwire/2026/05/04/sap-to-acquire-prior-labs-to-establish-a-globally-leading-frontier-ai-lab-in-europe/"
tags:
  - "SAP"
  - "Prior Labs"
  - "TabPFN"
  - "enterprise AI"
  - "European AI"
  - "structured data"
  - "acquisition"
relatedSlugs:
  - "2026-04-25-cohere-aleph-alpha-merger-sovereign-ai-en"
  - "2026-04-22-salesforce-headless-360-tdx-2026-en"
---

SAP's acquisition playbook has historically been about market extension — buying Concur for travel expenses, Qualtrics for experience management, Ariba for procurement. The purchase of Prior Labs, announced Monday alongside a simultaneous deal for open-source data platform Dremio, signals a fundamentally different ambition: SAP is investing in AI data capabilities through the Prior Labs deal.

The deal, terms of which were not disclosed, comes with a sizable commitment: SAP has committed $1.17 billion over the next four years to help scale Prior Labs.

## What Prior Labs Does

Prior Labs is the kind of company that generates outsized academic reputation and undersized mainstream recognition. Founded by Frank Hutter, Noah Hollmann, and Sauraj Gambhir, the startup pioneered an AI architecture category called Tabular Foundation Models (TFMs) — models purpose-built not for text or images but for the rows-and-columns structured data that powers virtually every enterprise system on Earth.

The company's flagship product, TabPFN, took a different approach to tabular machine learning than the gradient boosting methods (XGBoost, LightGBM) that have dominated enterprise data science for a decade. Where those methods require careful feature engineering, hyperparameter tuning, and significant data preparation, TabPFN uses a transformer-based architecture pre-trained on tens of millions of synthetic tabular datasets to make accurate predictions almost instantly — even on very small datasets where traditional methods struggle.

The results were significant enough to publish in *Nature*. TabPFN-2.6, the current flagship version, now leads the TabArena benchmark for tabular foundation models and has accumulated more than 3 million downloads as an open-source tool. That developer adoption — rare for academic AI research to achieve — reflects genuine utility in production settings, not just benchmark chasing.

## The Business Case for Tabular AI

The timing of this acquisition makes sense when you understand what's missing in the current enterprise AI wave. Most of the attention in 2025 and 2026 has focused on large language models and multimodal systems — technology that excels at unstructured data like text, images, and code. But the data that actually drives most enterprise decisions remains stubbornly structured: financial transactions, supply chain records, customer databases, ERP tables.

Traditional approaches to tabular ML require data scientists to build custom pipelines for every use case. TFMs change that economics dramatically. A model like TabPFN can predict payment default risk, supplier failure probability, customer churn likelihood, and upsell opportunities using the same underlying architecture, with minimal setup per application.

For SAP — whose customer base runs global enterprises on structured data SAP systems generate — this is not a theoretical benefit. The company already sits on or processes structured business data at a scale few organizations can match. Prior Labs' technology could theoretically let SAP build prediction and intelligence features directly into its ERP, supply chain, and finance applications with much lower development overhead than current approaches require.

## Dremio: The Other Half of SAP's Double Play

The simultaneous acquisition of Dremio adds an important data access layer to SAP's AI ambitions. Dremio provides a data lakehouse platform optimized for open source Apache Iceberg tables, technology that lets users access data across platforms without physically moving or copying it.

Together, the two acquisitions address a common enterprise AI failure mode: models trained or fine-tuned on data that doesn't reflect the full breadth of an organization's information. Dremio helps SAP customers make more data accessible for AI use; Prior Labs' technology helps SAP build models that work effectively on that data.

"Data access without intelligence is incomplete. Intelligence without data access is incomplete."

## A European AI Lab Strategy

The strategic significance of Prior Labs extends beyond SAP's product roadmap. By committing to keep Prior Labs operating as an independent entity under its founding team — and anchoring significant AI research investment in Germany — SAP is making an implicit argument about European AI sovereignty.

Europe's AI ecosystem has struggled to compete with US and Chinese frontier labs for funding, compute, and talent. Cohere's merger with Aleph Alpha earlier this year was partly motivated by a similar desire to create a scaled European alternative to OpenAI and Anthropic. SAP's bet is different: rather than building a general-purpose LLM competitor, it's investing in specialized AI research that addresses a specific domain where European enterprise infrastructure companies have genuine competitive advantage.

Frank Hutter brings particular credibility to this positioning. A professor at the University of Freiburg and a pioneer in automated machine learning (AutoML), Hutter has published foundational work in neural architecture search, meta-learning, and hyperparameter optimization. His academic profile — combined with Prior Labs' Nature publication and TabPFN's open-source traction — suggests SAP is acquiring a genuine research capability rather than merely buying a product.

## What Comes Next

The acquisition is expected to close in Q2 or Q3 of 2026, subject to regulatory approvals. Prior Labs will continue operating as an independent entity, preserving the team's research culture and open-source commitments. SAP has indicated the €1B+ investment will fund expansion of research staff, computing resources, and dataset scale.

For the enterprise software industry, the deal may signal a broader pattern. If structured tabular data represents a meaningful frontier in AI capability — and the evidence from TabPFN's benchmark performance and adoption suggests it does — then the companies best positioned to benefit are those that already sit at the center of enterprise structured data flows: SAP, Oracle, Salesforce, Microsoft's Dynamics division.

The race to turn rows and columns into actionable intelligence has barely started.

*Correction (November 15, 2026): 6 sentences were corrected or removed to match the sources listed on this page.*
