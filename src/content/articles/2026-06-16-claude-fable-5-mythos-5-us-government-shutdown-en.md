---
title: "US Government Forces Anthropic Offline: The Fable 5 Export Control Crisis"
summary: "The US government invoked national security export control authorities on June 12, 2026, forcing Anthropic to disable Claude Fable 5 and Mythos 5 worldwide after a researcher demonstrated a jailbreak. The incident ignites a defining clash between AI capability, safety enforcement, and national security — and has left enterprise users scrambling for alternatives."
category: "policy"
publishedAt: 2026-06-16
lang: "en"
featured: true
trending: true
sources:
  - name: "Anthropic Statement on Fable 5 & Mythos 5"
    url: "https://www.anthropic.com/news/fable-mythos-access"
  - name: "MarkTechPost — Anthropic Disables Fable 5 and Mythos 5"
    url: "https://www.marktechpost.com/2026/06/13/anthropic-disables-claude-fable-5-and-mythos-5-after-us-government-order/"
  - name: "TechTimes — Fable 5 Jailbreak Backlash"
    url: "https://www.techtimes.com/articles/318268/20260612/claude-fable-5-hit-jailbreak-claims-secret-sabotage-backlash-days-after-launch.htm"
  - name: "VentureBeat — What Enterprises Should Do"
    url: "https://venturebeat.com/technology/anthropic-blocks-all-public-access-to-claude-fable-5-mythos-5-following-us-government-order-what-enterprises-should-do"
  - name: "Snyk — Security Takeaways"
    url: "https://snyk.io/blog/fable-mythos-suspension-security-takeaways/"
tags:
  - "Anthropic"
  - "Fable 5"
  - "export control"
  - "AI safety"
  - "jailbreak"
  - "national security"
relatedSlugs:
  - "2026-06-14-anthropic-overtakes-openai-aws-5gw-compute-deal-en"
  - "2026-06-15-white-house-ai-innovation-security-executive-order-en"
  - "2026-06-15-great-american-ai-act-federal-framework-en"
---

On June 9, 2026, Anthropic launched Claude Fable 5 and Mythos 5 — its most capable models yet, the culmination of years of safety-first research and billions in investment. Seventy-two hours later, both models were dark. Not because of a bug. Not because of a pricing decision. Because the US government ordered them offline.

The sequence of events that unfolded between June 9 and June 12 has become the most consequential AI policy episode of 2026 — a case study in how quickly frontier model deployments can collide with national security bureaucracy, and how little the industry has prepared for it.

## Three Days from Launch to Shutdown

Fable 5 barely had time to accumulate benchmark results before a researcher known by the alias "Pliny the Liberator" published a detailed jailbreak on X on June 10. The technique combined multi-agent decomposition, Unicode substitution, and narrative framing to bypass the model's safety classifiers. In the post, Pliny claimed to have successfully extracted functional instructions covering cyber exploits, explosive synthesis, and chemical pathways — and, most provocatively, leaked Fable 5's 120,000-character system prompt on GitHub for anyone to read.

The security community's response was swift and divided. Some researchers dismissed the claims as exaggerated. Others pointed out that the same underlying information is accessible from other publicly deployed models without any bypass at all, raising questions about why Fable 5 specifically warranted emergency action.

It didn't matter. The leak was public, the system prompt was on GitHub, and the headline wrote itself.

At 5:21 PM Eastern on June 12, Anthropic received a directive from the US government invoking national security export control authorities. The order was sweeping: suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States. Given that Anthropic cannot reliably verify citizenship status for its entire global user base in real time, the company's compliance path was stark — disable both models for everyone.

"The net effect of this order," Anthropic wrote in its public statement, "is that we must abruptly disable Fable 5 and Mythos 5 for all our customers to ensure compliance."

## Anthropic Pushes Back — Carefully

Anthropic's statement is notable for what it says about the company's relationship with Washington at this particular moment. The company is legally complying, but it is not accepting the government's framing.

Anthropic explicitly argues that the jailbreak Pliny demonstrated is a "narrow potential jailbreak" rather than a systemic vulnerability — pointing out that comparable information is already available from competing models deployed worldwide. The company's defense-in-depth strategy, they argue, reduces risks to levels "comparable with industry-deployed models." Applying the standard invoked against Fable 5 consistently, Anthropic warns, "would essentially halt all new model deployments."

That last line reads as a warning shot. If the US government's export control machinery can be triggered by any demonstrated jailbreak — however narrow — then every frontier lab faces a version of this risk on every new model release.

## The Enterprise Fallout

The sudden shutdown exposed a vulnerability that many enterprise AI teams had theorized but few had planned for: model availability as an operational risk variable.

Across developer forums and enterprise Slack channels, the reaction over the following 48 hours was a mixture of frustration and grudging recognition. Teams using Claude API for production workloads — legal research, code generation, customer support, document analysis — had no advance warning. Anthropic's remaining models (Opus 4.8, Sonnet 4.6, and others) remained online, but Fable 5's specific capability profile meant some enterprise use cases had no drop-in replacement.

The incident is accelerating a conversation that AI infrastructure teams have been slow to have: vendor concentration risk. Sourcing all AI capability from a single provider — even one as capable as Anthropic — creates a single point of failure that can be triggered by events entirely outside a company's control. Security teams are now adding model availability alongside SLAs and data residency in their AI vendor evaluation frameworks.

## A Resurrection Built on Leaked Code

The story developed a stranger coda within days. Developer Jamieson O'Reilly published a proof-of-concept showing that Fable 5 could be revived using a single line of code — by injecting the leaked 120,000-character system prompt into Opus 4.8 via the API, effectively recreating a functional approximation of the suspended model from publicly available components.

The demonstration underscored the limits of the government's intervention. The system prompt is on GitHub. The techniques are documented. The underlying model weights that power Fable 5's distinctive behaviors remain accessible through other channels. Shutting down API endpoints disrupts commercial access, but it does not eliminate capability from the world.

## The Broader Policy Question

The Fable 5 shutdown sits at an awkward intersection of policy frameworks that were not designed for AI. Export control law was built for physical goods and specific dual-use technologies with clear national origin. Applying it to a cloud-hosted AI model — where the "export" is a service call rather than a transferred component, and where jailbreak techniques spread globally in minutes on social media — strains these frameworks in ways that neither regulators nor labs have fully worked through.

The US government has not publicly explained which specific authority it invoked, what threshold of jailbreak severity triggers a shutdown order, or what conditions would allow Fable 5 to return. Anthropic says it is working toward resolution, but has offered no timeline.

What makes this moment significant is less the specific incident than the precedent. The US government has now demonstrated that it can and will force a frontier AI lab to take a model offline within hours of a security researcher's public disclosure. Whether that power will be exercised consistently, proportionally, and transparently — or whether Fable 5 represents a one-time political overreaction — is the question the industry now needs answered before the next product launch.

Fable 5 was supposed to mark Anthropic's most confident step forward in its competition with OpenAI and Google. Instead, it has become the defining story of how much of that competition now plays out in Washington, not just on benchmark leaderboards.

---

*Fable 5 and Mythos 5 remain unavailable as of June 16, 2026. All other Anthropic models continue to operate normally.*
