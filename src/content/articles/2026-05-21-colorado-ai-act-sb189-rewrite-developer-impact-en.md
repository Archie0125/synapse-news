---
title: "Colorado Rewrites Its Landmark AI Law: What SB 189 Means for Developers and Deployers"
summary: "Colorado's legislature passed SB 189, a sweeping rewrite of the state's original AI Act that eliminates mandatory risk management programs, annual impact assessments, and algorithmic discrimination duties in favor of a narrower transparency framework. The original law was stayed by a federal court after the DOJ joined xAI in challenging its constitutionality — setting a precedent with national implications for state-level AI regulation."
category: "policy"
publishedAt: 2026-05-21
lang: "en"
featured: false
trending: false
sources:
  - name: "Consumer Finance Monitor"
    url: "https://www.consumerfinancemonitor.com/2026/05/12/colorado-rewrites-its-landmark-ai-law-unpacking-sb-26-189-and-what-it-means-for-businesses/"
  - name: "Littler"
    url: "https://www.littler.com/news-analysis/asap/colorado-amends-its-artificial-intelligence-law-substantially-reducing"
  - name: "Brownstein"
    url: "https://www.bhfs.com/insight/colorados-landmark-ai-law-coming-online-what-developers-and-deployers-should-know/"
  - name: "Ropes & Gray"
    url: "https://www.ropesgray.com/en/insights/alerts/2026/05/colorado-scales-back-ai-law-with-targeted-implications-for-health-care"
  - name: "Fisher Phillips"
    url: "https://www.fisherphillips.com/en/insights/insights/colorado-moves-to-replace-ai-laws-bias-audit-requirements-with-transparency-framework"
tags:
  - "Colorado AI Act"
  - "SB 189"
  - "AI regulation"
  - "policy"
  - "algorithmic discrimination"
  - "AI compliance"
  - "developer obligations"
  - "US AI law"
relatedSlugs:
  - "2026-05-17-eu-ai-act-high-risk-delay-2027-en"
  - "2026-04-04-eu-ai-act-enforcement-en"
  - "2026-05-19-caisi-five-ai-labs-predeployment-government-testing-en"
---

When Colorado passed SB 205 in 2024, it became the first U.S. state to enact comprehensive AI regulation addressing algorithmic discrimination in high-stakes decisions — and immediately became the focal point of an intense national debate about where the responsibility for AI harms should sit. By May 2026, that experiment had produced an unexpected outcome: a federal judge stayed the original law, the Department of Justice intervened on the side of challengers, and the legislature voted to replace the law with something significantly narrower. The journey from enactment to rewrite offers the clearest data point yet on how state-level AI legislation struggles against coordinated opposition from the federal government and major technology interests.

## The Original Law and Its Troubled Path to Enforcement

The original Colorado AI Act (SB 205) was notable for its scope. It required developers and deployers of "high-risk AI systems" — defined as AI making or substantially influencing consequential decisions in areas like employment, housing, healthcare, education, and financial services — to implement risk management programs, conduct annual impact assessments, maintain consumer notice systems, and exercise "reasonable care" to avoid algorithmic discrimination.

The law's effective date was twice delayed. A special legislative session in August 2025 failed to pass amendments, pushing the date to June 30, 2026. But enforcement never reached that date. On April 27, 2026, a federal magistrate judge stayed the original law pending resolution of a constitutional challenge filed by technology interests including Elon Musk's xAI. The U.S. Department of Justice subsequently joined the challenge, arguing the law imposed unconstitutional burdens on interstate commerce — a significant escalation in the federal posture toward state AI regulation.

The DOJ's intervention was the pivotal moment. State legislatures can withstand industry opposition; they are considerably less equipped to maintain a law that the federal executive branch has officially opposed on constitutional grounds. Colorado's legislature moved quickly after the stay, passing SB 189 on May 9, with the expectation that Governor Jared Polis would sign it.

## What SB 189 Actually Changes

The rewrite is substantial. The original law's most demanding provisions — mandatory risk management programs modeled on NIST's AI RMF, annual algorithmic impact assessments, and the duty to use "reasonable care" to avoid algorithmic discrimination — are removed entirely.

In their place, SB 189 establishes a narrower notice-and-transparency framework. Organizations deploying high-risk AI in Colorado must disclose to consumers that a covered AI system is being used, explain the general purpose of the system, and provide information about how consumers can request human review or seek recourse. The focus shifts from preventing harm through procedural controls to informing consumers so they can protect themselves.

The liability framework is also restructured. Under SB 189, developers are only liable if a deployer uses the covered AI technology as "intended, documented, marketed, advertised, configured, or contracted" by the developer — a standard that protects developers from downstream misuse by deployers who go beyond the intended use case. This is a meaningful change for software vendors who sell general-purpose AI tools without knowledge of specific deployment contexts.

Enforcement is channeled exclusively through the Colorado Attorney General, with violations constituting unfair and deceptive trade practices carrying civil penalties of up to $20,000 per violation. Private rights of action — which consumer advocates had championed in the original law — are eliminated.

The law takes effect January 1, 2027, contingent on Governor Polis's signature, and enforcement is further deferred until the Attorney General completes required rulemaking, meaning practical enforcement is unlikely before mid-2027 at the earliest.

## Healthcare: The One Area That Got Stricter

One notable exception to the general trend of reduction: SB 189 imposes more specific obligations on AI systems used in clinical decision-making in healthcare settings. Deployers in the healthcare sector face enhanced disclosure requirements and must ensure that healthcare providers are informed when AI systems are influencing clinical recommendations. Given that Colorado's electorate includes large rural populations with limited access to specialist care — and therefore higher exposure to AI-assisted diagnostic systems — this targeted tightening makes political sense even if it cuts against the overall deregulatory direction.

## The National Significance of Colorado's U-Turn

The Colorado story matters beyond state borders for two reasons.

First, the DOJ's intervention sets a precedent. Several other states — including California, Texas, and Illinois — have advanced or are considering AI legislation with compliance requirements similar to Colorado's original law. If the DOJ's position is that comprehensive state AI mandates burden interstate commerce unconstitutionally, those efforts face the same constitutional jeopardy. The federal government has effectively signaled that it prefers to own the AI regulatory space rather than allow a patchwork of state regimes to develop — and has shown it is willing to use constitutional litigation as a tool to enforce that preference.

Second, the replacement law's transparency-over-accountability framework may become the model other states adopt as they recalibrate their ambitions in light of Colorado's experience. Notice-and-transparency requirements are easier to defend constitutionally, impose lower compliance costs on industry, and are politically sustainable in a way that "reasonable care to avoid algorithmic discrimination" arguably is not when facing coordinated opposition.

## Implications for Developers and Deployers

For the technology industry, SB 189 is largely good news in the short term. The compliance burden relative to SB 205 is dramatically lower. Organizations that had been building risk management programs, impact assessment processes, and consumer disclosure infrastructure in anticipation of the original law's enforcement date may find that much of that work exceeds what SB 189 actually requires.

That said, the trend toward transparency requirements is likely durable. The question is not whether disclosure obligations will apply to high-risk AI systems but how granular and how auditable those disclosures must be. Organizations that build robust documentation practices now — capturing training data provenance, model evaluation results, and deployment context — will be better positioned as both federal baseline requirements and international frameworks like the EU AI Act continue to develop.

The EU AI Act's recent omnibus simplification, agreed in May and extending key compliance deadlines to late 2027 and 2028, creates a compressed but real window for organizations operating in both U.S. and European markets to synchronize their compliance frameworks. Colorado's SB 189 and the EU's omnibus deal together suggest a global regulatory trajectory that is real but slower-moving than many had anticipated two years ago — giving the industry more runway to adapt, but not license to postpone.
