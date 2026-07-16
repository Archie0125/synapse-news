---
title: "HHS Is Using ChatGPT to Audit Medicaid Funding Across All 50 States — Without Publishing Its Error Rate"
summary: "The US Department of Health and Human Services launched AERO, an initiative that uses ChatGPT to scan five years of state healthcare audits and flag potential fraud. With the AI's accuracy metrics unpublished and no formal appeals process established, hospitals and state Medicaid agencies face enforcement decisions made by a black-box system."
category: "policy"
publishedAt: 2026-07-16
lang: "en"
featured: false
trending: false
sources:
  - name: "Healthcare Dive — HHS AI-backed health fraud crackdown"
    url: "https://www.healthcaredive.com/news/hhs-ai-fraud-state-audit-aero/820989/"
  - name: "TechTimes — HHS deploys ChatGPT on Medicaid audits"
    url: "https://www.techtimes.com/articles/319108/20260625/hhs-deploys-chatgpt-medicaid-audits-no-error-rate-no-appeals-no-deadline.htm"
  - name: "TechTimes — ChatGPT threatens Medicaid funding nationwide"
    url: "https://www.techtimes.com/articles/320302/20260713/chatgpt-now-threatens-medicaid-funding-hospitals-nationwide-error-rate-unpublished.htm"
  - name: "Paubox — HHS AI healthcare audit detection"
    url: "https://www.paubox.com/blog/hhs-to-use-ai-to-detect-healthcare-audit-backlogs"
  - name: "OnHealthcare.tech — HHS ChatGPT state audits"
    url: "https://www.onhealthcare.tech/p/hhs-goes-all-in-on-chatgpt-for-state"
tags:
  - "HHS"
  - "ChatGPT"
  - "Medicaid"
  - "AI policy"
  - "healthcare"
  - "AERO"
  - "government AI"
relatedSlugs:
  - "2026-07-15-ftc-ai-accuracy-policy-statement-en"
---

On May 21, the US Department of Health and Human Services quietly launched something remarkable: a federal enforcement program that deploys ChatGPT to scan and flag potential fraud across five years of compliance audits filed by every state Medicaid agency, nonprofit hospital system, and federal healthcare grantee in the country. The initiative — called AERO, for Audit Enforcement and Risk Oversight — can impose consequences ranging from temporary payment holds to permanent debarment from federal programs. What it has not done is disclose how accurate the AI system is.

That gap, between the scope of the authority being exercised and the transparency of the tool exercising it, is at the center of a growing controversy that has now reached Congress, healthcare advocacy groups, and a collection of state attorneys general who are watching AERO's first enforcement actions begin to land.

## What AERO Does

AERO is led by Gustav Chiarello, HHS's Assistant Secretary for Financial Resources, who announced the program to HHS staff in late May. The mandate: use ChatGPT and other large language model tools to analyze at least five years of Single Audit Act compliance records filed by organizations that receive $1 million or more in federal funding annually.

The scope is broad. Single Audit filers include state Medicaid agencies, nonprofit healthcare providers, public hospital systems, federally qualified health centers, academic medical centers that receive federal research grants, Head Start programs, and addiction treatment providers. In aggregate, this encompasses hundreds of billions of dollars in annual federal healthcare spending and thousands of organizations across all 50 states.

The AI is tasked with reading audit narratives, identifying recurring compliance findings, flagging patterns that might indicate systemic problems, and prioritizing which organizations warrant heightened human review. Enforcement consequences for organizations that fail that review include temporary payment holds — which can freeze the Medicaid reimbursements that keep rural hospitals financially viable — and, in the most serious cases, permanent debarment from federal programs.

## The Accuracy Problem

The central controversy is that HHS has not published the error rate of the AI system being used to make these determinations.

This matters in a specific, technical way. In the context of healthcare enforcement, a "false positive" — flagging an organization as potentially non-compliant when it is actually compliant — is not a neutral outcome. It triggers an investigative process that requires organizations to respond with documentation, legal counsel, and administrative resources. For a small federally qualified health center or a rural hospital already operating on thin margins, even a preliminary flag and the associated compliance burden can be financially destabilizing.

At larger scale, the population of AERO filers is diverse enough that even a modest error rate — say, 5% false positives across 5,000 organizations — translates to 250 organizations facing enforcement scrutiny they do not merit. The AI system's ability to distinguish between genuine compliance failures and audit language patterns that superficially resemble them is untested in public.

HHS has also not disclosed: what specific model or version of ChatGPT is being used; what prompting methodology or fine-tuning approach is applied; what human review is performed on AI-flagged determinations before enforcement actions are initiated; or what the appeals pathway is for organizations that believe they have been incorrectly flagged.

As of July 13, TechTimes reported that "the federal government is now using ChatGPT to make enforcement decisions that can freeze Medicaid funding to hospitals, nonprofits, and state agencies across all 50 states — and it has not published the tool's error rate, disclosed its methodology, or specified when funds will actually be cut."

## The Legal and Regulatory Context

AERO operates under existing HHS authority over Single Audit Act compliance, which means it does not require new legislation. HHS framed it as an efficiency initiative: the agency faces a substantial backlog of unreviewed audits, and using AI to triage and prioritize review is a defensible response to resource constraints.

But the use of AI in federal enforcement contexts touches an increasingly active area of administrative law. The Administrative Procedure Act requires agencies to follow notice-and-comment rulemaking when making substantive changes to how they enforce regulations; whether AERO constitutes such a change is now being debated by administrative law scholars. The FTC's recent policy statement on AI accuracy in commercial contexts — which requires AI systems used in consumer-facing decisions to meet disclosed accuracy standards — does not directly apply to federal agencies, but it has set a normative benchmark that critics are invoking.

The Biden-era Executive Order 13960 on trustworthy AI in government required federal agencies to conduct algorithmic impact assessments before deploying AI in high-stakes decision-making contexts. The Trump administration rescinded portions of that order; whether the remaining requirements apply to AERO is a question that has not been publicly resolved.

## Congressional and State Responses

Senator Ron Wyden of Oregon sent a letter to HHS Secretary in late June demanding the disclosure of AERO's accuracy metrics, the AI model specifications, and the appeals process before any enforcement action resulting from AI-flagged determinations is finalized. A bipartisan group of eight senators signed on to a follow-up letter requesting a 90-day implementation pause pending methodology disclosure.

Several state attorneys general — including those from California, New York, and Illinois — have opened inquiries into how AERO's operation interacts with state Medicaid program administration, particularly around questions of whether federal AI-flagged determinations supersede state-level compliance determinations.

The American Hospital Association has publicly called for a moratorium on AERO enforcement actions until HHS publishes validation data. The National Council of Nonprofits and several federally qualified health center advocacy groups have joined that call.

## The Broader Stakes

AERO is not the only federal AI enforcement initiative underway. The Department of Labor has piloted AI-assisted ERISA audit triage. The Small Business Administration has deployed AI to flag PPP loan applications for review. The IRS has used AI in tax return anomaly detection for several years.

What distinguishes AERO is the scale of its enforcement authority and the directness of the economic consequences it can trigger. Medicaid payment holds are not fines that an organization can dispute over years of litigation; they can interrupt cash flows that pay clinical staff within weeks. The asymmetry between the speed and scale of AI-flagged enforcement and the speed of the human review and appeals process that should accompany it is the core governance problem AERO has created.

Healthcare policy experts note a deeper irony: AI is being deployed to enforce compliance with auditing standards that were themselves designed to be verified by human auditors who could exercise contextual judgment. An AI reading a compliance narrative does not know, for example, that a particular internal control finding was already resolved through a corrective action plan that postdates the audit period under review. Whether the system can handle that kind of document-level context, and how reliably it does so, is precisely the question the missing accuracy data would answer.

For now, the organizations receiving AERO letters are navigating that uncertainty on their own — with potential consequences that run into the millions of dollars per entity, and a federal system that has not yet explained how it will know if it has made a mistake.
