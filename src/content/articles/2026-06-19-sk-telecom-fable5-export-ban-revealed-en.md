---
title: "Inside the Fable 5 Ban: SK Telecom, a Jailbreak, and a Refused Ultimatum"
summary: "New reporting reveals that SK Telecom's suspected China ties triggered White House scrutiny of Anthropic's Project Glasswing, while Amazon CEO Andy Jassy separately flagged a Fable 5 jailbreak to the Trump administration on June 12. Anthropic CEO Dario Amodei was offered a chance to fix the vulnerability or withdraw the model — he refused both — and the export ban followed."
category: "policy"
publishedAt: 2026-06-19
lang: "en"
featured: false
trending: true
sources:
  - name: "Korea JoongAng Daily"
    url: "https://www.koreajoongangdaily.com/business/white-house-officials-pin-anthropic-ai-export-block-on-korean-telecom-report/12726842"
  - name: "Fortune"
    url: "https://fortune.com/2026/06/14/how-a-warning-from-amazon-led-the-white-house-to-shut-down-anthropics-mythos-model/"
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-adviser-david-sacks-says-anthropic-refused-to-fix-fable-5-jailbreak-before-us-export-controls"
  - name: "MSN/Technology"
    url: "https://www.msn.com/en-us/news/technology/us-warned-anthropic-of-china-breach-but-firm-refused-to-fix-fable-5-jailbreak-says-david-sacks/ar-AA25BWh2"
tags:
  - "AI-policy"
  - "export-controls"
  - "Anthropic"
  - "SK-Telecom"
  - "Fable-5"
  - "national-security"
  - "jailbreak"
  - "White-House"
relatedSlugs:
  - "2026-06-16-claude-fable-5-mythos-5-us-government-shutdown-en"
  - "2026-06-17-anthropic-project-glasswing-150-orgs-critical-infrastructure-en"
  - "2026-06-19-anthropic-seoul-office-korea-ai-partnerships-en"
---

The week-long shutdown of Anthropic's most capable AI models didn't begin with a policy decision or a legislative hearing. It began, according to new reporting, with two separate warnings reaching the White House in close succession — one about who had access to the models, and one about what those models could be made to do.

Taken together, they produced the most significant government intervention in AI model deployment since the Trump administration began asserting control over frontier AI access: the June 12 export control directive that suspended all foreign national access to Fable 5 and Mythos 5, and which remains in effect as of June 19.

## How SK Telecom Became the Catalyst

The first thread leads to South Korea. Anthropic launched Project Glasswing in April 2026 as a cybersecurity access program, initially with roughly 50 US-based partner organizations receiving controlled access to Mythos 5, Anthropic's most capable and least restricted model. By early June, Glasswing had expanded to approximately 150 organizations globally, including participants from South Korea — Samsung Electronics, SK Hynix, and SK Telecom, among others.

SK Telecom, South Korea's largest mobile carrier and a $100 million investor in Anthropic's earlier fundraising round, was among the Korean companies admitted to Glasswing. When White House officials reviewed the expanded participant list, they identified a Korean telecommunications company "suspected of having ties to China." While SK Telecom has not been officially named and the company has declined to comment on the reports, it is the only Korean carrier in the Glasswing program and is widely identified in reporting as the entity in question.

The concern was not that SK Telecom had done anything improper with its access. The concern was that a carrier with alleged China links — even informal, historical ones — had been granted access to a model with unrestricted cybersecurity capabilities. Glasswing was designed to give trusted organizations early access to Anthropic's most powerful AI precisely because of its cyber use cases. Giving that access to an entity with suspected China exposure was, from a national security standpoint, exactly the kind of error the export control regime is designed to prevent.

Anthropic had submitted an initial list of 111 approved organizations to the administration, which was reviewed and cleared. The expanded list containing the Korean telecom was what tripped the wire.

## Amazon's Warning

The second thread arrives separately, but at nearly the same moment. Amazon CEO Andy Jassy, whose company is Anthropic's largest cloud provider and a major investor, raised concerns directly with senior Trump administration officials on June 12, 2026 — the same day the Commerce Department letter arrived.

Amazon researchers had discovered that "a series of prompts" could cause Mythos-class models to "provide information about cyberattacks that was supposed to be restricted." In other words: a jailbreak. The specific prompt sequence could bypass the guardrails separating Fable 5's consumer capabilities from Mythos 5's unrestricted cyber-assistance functionality.

David Sacks, Co-Chair of the President's Council of Advisers on Science and Technology and the Trump administration's AI and crypto czar, described the source as "a highly credible, trusted partner" — a characterization consistent with Amazon's position as both a cloud partner and a significant investor in Anthropic.

## The Refused Ultimatum

Before issuing the export control directive, the administration presented Anthropic with two options: fix the jailbreak, or voluntarily withdraw Fable 5 from foreign national access. According to Sacks, CEO Dario Amodei refused both.

Anthropic's position, articulated in subsequent days, was that the jailbreak was "narrow rather than a full jailbreak" — in Amodei's framing, a targeted bypass rather than a general capability unlock. The company argued that the risk was being overstated and that the prompt sequence in question did not represent a categorical security failure.

Sacks was publicly unsympathetic. Writing on X after the directive was issued, he said the administration was "frankly bewildered that Anthropic hasn't wanted to comply with safety requests that it previously said were its highest priority." He noted the directive was "issued reluctantly" and that restoration was contingent solely on Anthropic patching the vulnerability.

The White House has since told WIRED that Anthropic must eliminate "all jailbreaks" from Fable 5 before the models can be relaunched for foreign access — a demand that security researchers have been quick to characterize as technically impossible to guarantee.

## The Impossible Standard

"Jailbreak prevention is defense-in-depth, not a solved problem," one AI safety researcher told The New Stack. No frontier AI model has ever been certified jailbreak-free, because the adversarial prompt space is effectively infinite. The requirement to eliminate all jailbreaks before relaunch sets a bar that, strictly interpreted, could keep the models offline indefinitely.

Anthropic has so far not publicly addressed this paradox directly. Chris Ciauri, the company's International Managing Director, told reporters at the Seoul office opening that he was "very confident" the models would return "in the coming days" — language suggesting the administration may be interpreting its requirement more flexibly than its public statements imply.

The practical outcome of the standoff is that negotiations between Anthropic and the Trump administration are ongoing, with neither side publicly acknowledging any specific concession.

## Who Benefits

While the established AI players navigate the fallout, at least one company has positioned itself to gain. MiniMax, a Chinese AI firm, highlighted its recently launched M3 model — a frontier-class open-weights release — as an alternative to Fable 5, specifically emphasizing that open-weight models cannot be globally recalled by government directive. The marketing message is pointed: Fable 5's dependence on Anthropic's servers and access controls is precisely the feature that made the export ban possible.

The episode has also reignited debate about the structure of AI access programs that grant frontier-model capabilities to external organizations. Project Glasswing's rapid expansion — from 50 to 150 organizations in under two months — appears to have outpaced the security vetting process that should accompany it. Whether Anthropic's internal controls or the administration's approval process failed more severely is a question both sides have so far avoided answering directly.

## What Comes Next

The export ban remains in effect for foreign nationals as of June 19, with no official restoration date set. Anthropic is continuing to operate with its older Claude 3 series models for international customers, while US users retain access to Fable 5 and Mythos 5.

The resolution path appears to require Anthropic to demonstrate meaningful remediation of the jailbreak vulnerability — however "meaningful" is ultimately defined — to the administration's satisfaction. Given that Amodei's initial refusal was public and Sacks's criticism equally public, any resolution will need to be framed in a way that allows both sides to claim they achieved their stated goals.

The broader lesson may be the most uncomfortable one: when AI models are integrated into national security programs and given access to unrestricted cyber capabilities, the political and regulatory constraints that govern their deployment become indistinguishable from the technical constraints. Anthropic built a model capable enough that its access list became a matter of state concern. That capability, it turns out, has costs.
