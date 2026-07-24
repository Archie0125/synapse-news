---
title: "White House Accuses Moonshot AI of Stealing Anthropic's Fable Model; Treasury Threatens Sanctions"
summary: "The White House OSTP director publicly accused Chinese AI startup Moonshot AI of conducting large-scale distillation attacks on Anthropic's Fable model to build its Kimi K3 system, and alleged the company accessed banned Nvidia GB300 chips via Thailand. Treasury Secretary Scott Bessent followed up by putting sanctions and Entity List designations on the table, escalating the U.S.-China AI rivalry into open economic warfare."
category: "policy"
publishedAt: 2026-07-24
lang: "en"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/22/treasury-threatens-sanctions-after-white-house-claims-moonshot-distilled-anthropics-fable/"
  - name: "CyberScoop"
    url: "https://cyberscoop.com/white-house-accuses-moonshot-ai-anthropic-model-distillation/"
  - name: "The Hill"
    url: "https://thehill.com/policy/technology/5984510-white-house-moonshot-ai-anthropic-nvidia/"
  - name: "Quartz"
    url: "https://qz.com/white-house-moonshot-ai-nvidia-chips-anthropic-kimi-k3-072226"
tags:
  - "China AI"
  - "Moonshot AI"
  - "Kimi K3"
  - "Anthropic"
  - "Fable"
  - "model distillation"
  - "export controls"
  - "sanctions"
  - "IP theft"
  - "Nvidia GB300"
relatedSlugs:
  - "2026-07-17-moonshot-kimi-k3-open-weight-model-en"
  - "2026-07-11-china-ai-model-export-restrictions-alibaba-bytedance-en"
  - "2026-07-02-taiwan-super-micro-nvidia-chip-smuggling-probe-en"
---

The U.S. government's simmering conflict with China over artificial intelligence escalated dramatically this week when the White House's top science official publicly accused Chinese AI startup Moonshot AI of stealing capabilities from Anthropic's most advanced model — and the U.S. Treasury responded by threatening sanctions.

The accusations, leveled by Michael Kratsios, director of the White House Office of Science and Technology Policy (OSTP), center on Moonshot's Kimi K3 — an open-weight model released on July 21 that immediately drew comparisons to the most capable U.S. frontier systems. Kratsios alleged that K3's impressive performance was not earned through legitimate research but extracted covertly from American AI through a method known as model distillation.

## The Distillation Allegations

Model distillation is a recognized AI technique in which a smaller "student" model is trained to replicate the outputs of a larger "teacher" model. It becomes legally and ethically contested when done without permission using commercial AI APIs — essentially using fraudulent access to systematically mine proprietary knowledge from a competitor's system.

Kratsios wrote that the administration has "information that Moonshot AI distilled Anthropic's Fable for the development of its K3 model." He further alleged that Moonshot "built a sophisticated internal platform capable of conducting distillation across U.S. models while rapidly switching between different access methods to avoid detection."

Anthropic had previously flagged the suspicious activity to authorities: the company alleged that Moonshot generated more than **3.4 million Claude exchanges through fraudulent accounts** to extract capabilities including reasoning, coding, tool use, and computer vision. Critically, Anthropic said the metadata connected the activity to senior Moonshot employees and that internal company documents explicitly described the operation as a "distillation attack."

## The Hardware Angle: Banned Blackwell Chips

The allegations extend beyond software. Kratsios also accused Moonshot of violating U.S. export controls on advanced semiconductors — the most sensitive layer of the AI geopolitical conflict.

Specifically, he alleged that Moonshot "acquired Nvidia's GB300-equipped servers and has accessed GB300s in Thailand" — a reference to Nvidia's Blackwell architecture GPU, which is classified as export-controlled hardware that cannot be legally sold to Chinese entities under current U.S. Department of Commerce regulations. The Thailand reference is significant: it suggests the company may have been routing hardware purchases through third-party jurisdictions to circumvent the restrictions, a pattern regulators have identified in previous chip-smuggling investigations.

## Treasury's Response: Sanctions and Entity List

Treasury Secretary Scott Bessent moved quickly to amplify the threat. In a statement, he warned that "sanctions and Entity List designations will be on the table" for firms conducting what he characterized as "covert, industrial-scale distillation attacks that cross the line into IP theft."

An Entity List designation — administered by the Commerce Department's Bureau of Industry and Security — would effectively ban U.S. companies from exporting any technology or components to Moonshot without a hard-to-obtain license. Sanctions from the Treasury's OFAC division would go further, potentially freezing assets and barring any U.S. person or entity from transacting with the company.

The dual threat, coming within hours of each other from two senior cabinet-level officials, signals coordinated escalation rather than a loose comment. It positions the Kimi K3 affair as a possible inflection point in how the United States polices AI model boundaries with Chinese companies.

## The Timeline Problem

Not everyone is convinced the accusations are airtight. The chronology creates a puzzle that several AI researchers have publicly flagged.

Anthropic's Fable model only became publicly accessible on **July 1**, after being briefly taken offline due to U.S. export control compliance reviews. Moonshot released Kimi K3 as an open-weight model on **July 21** — a window of just **20 days** between Fable's public availability and K3's launch.

Distillation attacks at the scale described — 3.4 million API calls generating structured training data, followed by a full training run producing a frontier-caliber open-weight model — typically require weeks of compute time and infrastructure preparation, not to mention data curation and post-training alignment. Multiple AI researchers have publicly questioned whether a complete distillation pipeline starting from Fable's July 1 release could realistically produce K3's capabilities within that window.

An alternative reading: Moonshot may have begun distillation efforts against earlier Claude models (Anthropic's earlier flagship systems predating Fable) long before the July 1 release, with Fable specifically contributing refinements to later training stages. The White House statement leaves this ambiguity unresolved.

## Broader Context: An Escalating Playbook

Former White House AI adviser Dean Ball, who was not directly involved in the current accusations, advocated separately for restricting Chinese open-weight models from U.S. distribution channels on national security grounds — suggesting the administration is weighing policy options well beyond sanctions against individual companies.

The Kimi K3 affair is the latest chapter in a broader pattern. U.S. authorities have previously investigated Chinese entities suspected of accessing restricted Nvidia hardware through Singapore, Malaysia, and the Middle East. The Moonshot allegations, if proven, would represent the clearest case yet of both hardware circumvention and software IP extraction working in tandem.

Moonshot AI, headquartered in Beijing with engineering operations in Hong Kong, had not issued a public response to the allegations at time of publication. Neither had the U.S. Treasury Department responded to press inquiries about the specific legal mechanism for any forthcoming action.

## What Happens Next

The government has not announced a formal investigation or specified a timeline for any designations. Both Commerce and Treasury designations can take weeks to finalize and typically involve a due-process period in which the targeted company can respond.

The practical effect may be felt even before any formal action. Kimi K3's status as an open-weight model means it is already publicly available and cannot be "recalled." But a Moonshot Entity List designation could cut off the company's access to U.S. cloud platforms, developer tools, and model-serving infrastructure — effectively neutering its ability to operate globally.

For the broader AI industry, the case sets an uncomfortable precedent. If distillation attacks on API access are to be treated as IP theft triggering sanctions — rather than a garden-variety terms-of-service violation — it reshapes the legal landscape for AI competition globally. And it raises an uncomfortable question for U.S. AI companies: how many of their commercial API offerings have already been systematically distilled by competitors they cannot yet name?
