---
title: "The Government Is Using ChatGPT to Audit Medicaid — With No Published Error Rate"
summary: "The U.S. Department of Health and Human Services has deployed ChatGPT to scan five years of Medicaid and federal grant audits across all 50 states, under a program called AERO. Findings can trigger federal funding withholding — consequences already applied to California and Minnesota — but HHS has not disclosed the AI's error rate, methodology, or human review process, raising serious questions about due process and AI accountability in high-stakes government decisions."
category: "policy"
publishedAt: 2026-07-13
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

Somewhere in Washington, a large language model is reading five years of state Medicaid audit reports. It is looking for chronic noncompliance, repeat deficiencies, and material weaknesses. When it finds them, its findings can be used to trigger federal action that withholds funding from hospitals, state agencies, and nonprofits that collectively serve millions of Americans. The tool making those findings is ChatGPT, deployed by the U.S. Department of Health and Human Services. And as of the time of writing, HHS has not published its error rate.

This is the AERO program — Audit Enforcement and Risk Oversight — which HHS launched on May 21, 2026, under the Trump administration's broader push to use AI to identify and recover federal funds that the government believes are being misused. It is among the most consequential deployments of commercial AI by any branch of the United States government to date, and it is moving forward in the near-total absence of the transparency and accountability requirements that the administration's own AI policy mandates.

## The Scope of the Program

AERO analyzes Single Audit Act compliance records — the formal annual audits that states and federal grantees must submit for any year in which they spend $750,000 or more in federal funds. These audits cover essentially every state Medicaid program and a vast array of federal grant recipients in research, public health, addiction services, housing, and education.

The scale is staggering. Medicaid alone accounts for roughly $900 billion in annual federal and state spending. Total annual disbursements flowing through the programs subject to Single Audit Act reporting run into the trillions. AERO is, in effect, an AI system conducting real-time risk assessment across what may be the largest pool of government expenditure subject to audit in the world.

According to public documentation and reporting from multiple outlets, the AI system identifies patterns suggesting noncompliance and surfaces them for enforcement action, which can include temporary withholding of federal payments, recoupment of allegedly misspent funds, suspension of future grants, or outright termination of federal funding relationships. The system is not making final legal determinations — human officials retain formal decision-making authority — but it is functioning as the primary analytical layer that determines which entities face scrutiny and which do not.

## The Missing Transparency

The problem is what HHS has not disclosed. As of late June 2026, the agency had not published:

- The AI system's error rate on the audit classification tasks it performs
- Its methodology for identifying patterns of noncompliance
- The specific criteria or thresholds that trigger an enforcement referral
- How the system handles ambiguous or borderline cases
- What appeals process is available to entities that believe they have been incorrectly flagged
- A timeline for when enforcement actions will actually result in fund withholding

This matters enormously because the stakes of a false positive are severe. If AERO incorrectly flags a state Medicaid program or a federally-funded hospital as non-compliant, the potential outcome is federal funding withholding that disrupts healthcare services for vulnerable populations. The system is not adjudicating parking tickets; it is making risk determinations that can cascade into loss of funding for programs that communities depend on.

The funding consequences are not hypothetical. The Trump administration has already withheld more than $1 billion in Medicaid funds from California and hundreds of millions from Minnesota — actions taken on the basis of audit reviews that officials have characterized as evidence of mismanagement. Whether AERO's AI analysis was part of the trigger for those withholdings has not been publicly confirmed, but the timeline of AERO's deployment and the subsequent funding actions has prompted scrutiny from healthcare policy researchers and Democratic state officials.

## The Regulatory Framework It May Be Violating

The administration's own AI policy creates a framework that appears to apply directly to AERO. M-25-21, the Office of Management and Budget's memorandum on responsible AI adoption in the federal government, requires agencies deploying AI in applications that have significant consequences for individuals or organizations to implement minimum risk management practices. These include pre-deployment testing, documentation of the system's limitations, and an accessible human review process for affected parties.

The memo requires agencies to report their compliance with these requirements to OMB by September 2026. Whether HHS has conducted the required pre-deployment testing for AERO, or whether it can demonstrate that the system has been validated on the specific task of audit classification for compliance enforcement, is not publicly known.

The due process implications extend beyond administrative law. The Supreme Court and lower courts have established that when government action may deprive a party of property — which federal funding unambiguously is — the Fourteenth Amendment's due process clause requires meaningful notice and an opportunity to be heard. When the analytical basis for enforcement action is an opaque AI system whose methodology is not disclosed, it is genuinely unclear whether the resulting process satisfies constitutional requirements.

Several legal advocacy organizations representing healthcare providers and state governments have raised precisely these concerns in letters to HHS, and at least one state Medicaid agency has indicated it may pursue administrative or judicial challenge to AERO-related enforcement actions if funding withholding occurs based on AI analysis alone.

## The Broader Pattern

AERO is not an isolated phenomenon. The Trump administration has moved aggressively to deploy AI tools across federal government functions, including immigration enforcement screening, Social Security disability determination review, federal employee performance assessment, and now healthcare compliance enforcement. In each case, the deployment has moved faster than the transparency and accountability frameworks that AI policy documents require.

This pattern reflects a structural tension in how the current administration has approached AI in government. The efficiency and scale arguments for AI deployment are compelling: the federal government administers programs of enormous complexity across 50 states and hundreds of thousands of grant recipients, and the number of human auditors available to review compliance is a tiny fraction of what would be required for anything approaching comprehensive review. An AI system that can identify high-risk cases and prioritize them for human review is genuinely valuable.

But the same scale that makes AI valuable in government also magnifies the consequences of systematic errors. A human auditor who makes a mistake affects the cases they personally reviewed. An AI system with a 5 percent false positive rate, deployed across 50 states' Medicaid programs, generates false positive enforcement actions at scale — affecting real organizations, real funding streams, and real populations that depend on services those organizations provide.

## What Would Accountability Look Like

The path toward responsible deployment of AI in government enforcement contexts is not technically mysterious. Several components are well-understood:

Pre-deployment validation: testing the system's accuracy on representative cases before deployment, with results disclosed to oversight bodies and the public. The FDA applies this principle to AI used in medical device regulation; the analogous standard for enforcement AI in health program compliance seems clear.

Ongoing monitoring: tracking the system's performance after deployment, including error rates, appeal outcomes, and disparate impact analysis across different types of grantees and states. Published dashboards showing these metrics would allow external researchers and oversight bodies to identify problems before they compound.

Mandatory human review: for enforcement actions above a materiality threshold, requiring documented human review of the AI's analysis before a funding withholding notice is issued. The existence of human review as a formal step — rather than a theoretical possibility — is what transforms AI-assisted enforcement into AI-augmented enforcement with meaningful accountability.

Accessible appeal processes: giving affected entities a clear, timely mechanism to challenge AI-informed determinations, with specific information about what the AI flagged and why.

None of these requirements are prohibitively burdensome. What they require is that efficiency gains from AI deployment be shared between the government and the governed — not captured entirely by the government while the risks of error fall entirely on the entities being regulated.

AERO may well be catching real compliance failures. Given the scale of federal health program spending, it almost certainly is. The question is not whether AI can improve government oversight; it demonstrably can. The question is whether a system with the power to disrupt healthcare funding across an entire state should be allowed to operate without disclosure of how well it actually works.
