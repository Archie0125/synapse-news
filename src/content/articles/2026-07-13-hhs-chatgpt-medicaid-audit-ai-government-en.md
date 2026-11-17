---
title: "The Government Is Using ChatGPT to Audit Medicaid — With No Published Error Rate"
summary: "The U.S. Department of Health and Human Services has deployed ChatGPT to scan at least five years of federal grant audits across all 50 states, under a program called AERO. Findings can trigger federal funding withholding, but HHS has not disclosed the AI's error rate or methodology, raising serious questions about due process and AI accountability in high-stakes government decisions."
category: "policy"
publishedAt: 2026-07-13
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: false
sources:
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/319108/20260625/hhs-deploys-chatgpt-medicaid-audits-no-error-rate-no-appeals-no-deadline.htm"
  - name: "Healthcare Dive"
    url: "https://www.healthcaredive.com/news/hhs-ai-fraud-state-audit-aero/820989/"
  - name: "Boston Globe"
    url: "https://www.bostonglobe.com/2026/05/21/nation/trump-ai-healthcare-fraud/"
  - name: "Paubox"
    url: "https://www.paubox.com/blog/hhs-to-use-ai-to-detect-healthcare-audit-backlogs"
tags:
  - "HHS"
  - "ChatGPT"
  - "Medicaid"
  - "government AI"
  - "AERO"
  - "AI policy"
  - "healthcare"
  - "due process"
relatedSlugs:
  - "2026-07-10-ftc-ai-accuracy-policy-state-law-preemption-en"
  - "2026-07-12-anthropic-claude-corps-150m-fellowship-en"
---

Somewhere in Washington, a large language model is reading five years of state Medicaid audit reports. It is looking for chronic noncompliance, repeat deficiencies, and material weaknesses. When it finds them, its findings can be used to trigger federal action that withholds funding from hospitals, state agencies, and nonprofits. The tool making those findings is ChatGPT, deployed by the U.S. Department of Health and Human Services. And as of the time of writing, HHS has not published its error rate.

This is the AERO program — Audit Enforcement and Risk Oversight — which HHS launched on May 21, 2026, under the Trump administration's broader push to use AI to identify and recover federal funds that the government believes are being misused.

## The Scope of the Program

AERO analyzes Single Audit Act compliance records — the formal annual audits that states and federal grantees must submit for any year in which they spend $1 million or more in federal funds. These audits cover HHS-funded programs, including state Medicaid programs and federal grantees in research, addiction services, Head Start childcare, and more.

The scale is staggering.

According to public documentation and reporting from multiple outlets, the AI system identifies patterns suggesting noncompliance and surfaces them for human reviewers, with possible consequences that include temporary withholding of federal payments, disallowance of costs, suspension or termination of awards, or debarment proceedings. The system is not making final legal determinations — human officials retain formal decision-making authority — but it is functioning as the primary analytical layer that determines which entities face scrutiny and which do not.

## The Missing Transparency

The problem is what HHS has not disclosed. As of late June 2026, the agency had not published:

- The AI system's error rate on the audit classification tasks it performs
- Its methodology for identifying patterns of noncompliance
- What appeals process is available to entities that believe they have been incorrectly flagged
- A timeline for when enforcement actions will actually result in fund withholding

This matters enormously because the stakes of a false positive are severe. If AERO incorrectly flags a state Medicaid program or a federally-funded hospital as non-compliant, the potential outcome is federal funding withholding that disrupts healthcare services for vulnerable populations. The system is not adjudicating parking tickets; it is making risk determinations that can cascade into loss of funding for programs that communities depend on.

The funding consequences are not hypothetical. The Trump administration has already withheld more than $1 billion in Medicaid funds from California and hundreds of millions from Minnesota in separate enforcement actions.

## The Regulatory Framework It May Be Violating

The administration's own AI policy creates a framework that appears to apply directly to AERO. M-25-21, the Office of Management and Budget's memorandum on responsible AI adoption in the federal government, requires agencies deploying AI in applications that have significant consequences for individuals or organizations to implement minimum risk management practices. These include pre-deployment testing and an accessible human review process for affected parties.

The memo requires agencies to report their compliance with these requirements to OMB by September 2026. Whether HHS has conducted the required pre-deployment testing for AERO, or whether it can demonstrate that the system has been validated on the specific task of audit classification for compliance enforcement, is not publicly known.

The due process implications extend beyond administrative law. When the analytical basis for enforcement action is an opaque AI system whose methodology is not disclosed, it is genuinely unclear whether the resulting process satisfies constitutional requirements.

## The Broader Pattern

AERO is not an isolated phenomenon.

This pattern reflects a structural tension in how the current administration has approached AI in government. An AI system that can identify high-risk cases and prioritize them for human review is genuinely valuable.

But the same scale that makes AI valuable in government also magnifies the consequences of systematic errors. A human auditor who makes a mistake affects the cases they personally reviewed. An AI system with a 5 percent false positive rate, deployed across 50 states' Medicaid programs, generates false positive enforcement actions at scale — affecting real organizations, real funding streams, and real populations that depend on services those organizations provide.

## What Would Accountability Look Like

The path toward responsible deployment of AI in government enforcement contexts is not technically mysterious. Several components are well-understood:

Pre-deployment validation: testing the system's accuracy on representative cases before deployment, with results disclosed to oversight bodies and the public.

Ongoing monitoring: tracking the system's performance after deployment, including error rates, appeal outcomes, and disparate impact analysis across different types of grantees and states. Published dashboards showing these metrics would allow external researchers and oversight bodies to identify problems before they compound.

Mandatory human review: for enforcement actions above a materiality threshold, requiring documented human review of the AI's analysis before a funding withholding notice is issued. The existence of human review as a formal step — rather than a theoretical possibility — is what transforms AI-assisted enforcement into AI-augmented enforcement with meaningful accountability.

Accessible appeal processes: giving affected entities a clear, timely mechanism to challenge AI-informed determinations, with specific information about what the AI flagged and why.

None of these requirements are prohibitively burdensome. What they require is that efficiency gains from AI deployment be shared between the government and the governed — not captured entirely by the government while the risks of error fall entirely on the entities being regulated.

AERO may well be catching real compliance failures. Given the scale of federal health program spending, it almost certainly is. The question is not whether AI can improve government oversight; it demonstrably can. The question is whether a system with the power to disrupt healthcare funding across an entire state should be allowed to operate without disclosure of how well it actually works.

*Correction (November 15, 2026): 20 sentences were corrected or removed to match the sources listed on this page.*
