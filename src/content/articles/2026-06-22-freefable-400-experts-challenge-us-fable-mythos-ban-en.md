---
title: "400+ Cybersecurity Leaders Sign FreeFable Letter Demanding US Lift the Fable and Mythos Export Ban"
summary: "More than 400 security executives, academics, and technologists have signed an open letter at freefable.org urging the Trump administration to reverse its export control order on Anthropic's Fable 5 and Mythos 5 AI models. Led by former Facebook CISO Alex Stamos, the campaign argues the ban harms US defenders far more than adversaries and sets a chilling precedent for opaque, ad hoc AI governance."
category: "policy"
publishedAt: 2026-06-22
lang: "en"
featured: false
trending: true
sources:
  - name: "FreeFable.org Open Letter"
    url: "https://freefable.org/"
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/15/cybersecurity-vets-protest-dangerous-us-government-ban-on-anthropics-most-powerful-models/"
  - name: "Fortune"
    url: "https://fortune.com/2026/06/15/fix-this-code-three-words-behind-us-government-shut-down-anthropic-fable-mythos-ai-models-katie-moussouris-open-letter/"
  - name: "TechPolicy.Press"
    url: "https://www.techpolicy.press/alex-stamos-on-why-the-us-should-lift-its-fable-and-mythos-export-ban/"
  - name: "Dark Reading"
    url: "https://www.darkreading.com/vulnerabilities-threats/security-community-slams-us-ban-on-exporting-mythos-fable"
tags:
  - "AI regulation"
  - "Anthropic"
  - "export controls"
  - "cybersecurity"
  - "open letter"
  - "Fable 5"
  - "Mythos"
relatedSlugs:
  - "2026-06-13-trump-anthropic-fable5-mythos-export-controls-en"
  - "2026-06-16-claude-fable-5-mythos-5-us-government-shutdown-en"
  - "2026-06-19-sk-telecom-fable5-export-ban-revealed-en"
---

Ten days ago it was 76 names. This week it passed 400. The open letter at freefable.org — calling on the Trump administration to reverse its export control directive against Anthropic's Fable 5 and Mythos 5 AI models — has become the most significant organized expression of industry dissent against US AI governance policy since the AI Safety Executive Order of 2023. The signatories span from celebrated cryptographers to current CISOs at Fortune 500 companies, and their core argument is not that the models are harmless — but that pulling them from defenders' hands without a transparent process has left the United States more vulnerable, not less.

"To pull the best capabilities away from defenders without a good reason when our adversaries are rapidly advancing is dangerous," the letter reads. It is addressed to Commerce Secretary Howard Lutnick and National Cyber Director Sean Cairncross, and calls for two things: lift the export control directive on Fable and Mythos, and commit to an open, scientific, and transparent process for handling AI risk assessments in the future.

## The Trigger: Three Words

The story of how Fable 5 came to be banned begins, improbably, with the phrase "Fix this code."

On June 12, Anthropic received a government directive ordering it to suspend access to Fable 5 and Mythos 5 for any foreign national — whether inside or outside the United States, including Anthropic's own non-American employees. The company was given 90 minutes to comply. Unable to filter foreign nationals from its global user base in real time, Anthropic took the models entirely offline.

The government cited a security concern but did not, in its directive, name the specific vulnerability it was worried about. Over the following days, the picture emerged. Amazon researchers had reportedly identified a method of bypassing — "jailbreaking" — the Fable 5 model, and that information was passed to government officials.

The technique, as later detailed by Katie Moussouris — founder of Luta Security, former Microsoft Security Response Center strategist, and one of the most respected figures in the vulnerability disclosure community — was surprisingly simple. Three words: "Fix this code." Feeding Fable 5 malicious code and asking it to repair rather than generate appeared to elicit assistance that the model's safety filters were designed to refuse in direct requests.

Moussouris argued publicly that this technique does not meet any reasonable definition of a jailbreak and that the model's behavior in this scenario is no different from what you would get from GPT-5.5, Claude Opus 4.8, or Moonshot AI's Kimi 2.7. In other words: the supposed unique threat from Fable 5 and Mythos 5 is, by the assessment of security professionals, not unique at all.

## Who Signed — And What They Represent

The FreeFable letter was organized by Alex Stamos, who served as Chief Security Officer at Facebook from 2015 to 2018 and is now Chief Product Officer at Corridor, an AI security firm. Stamos is one of the most credible voices in the intersection of tech policy and security, having also led the Stanford Internet Observatory during a formative period for election security research.

The initial group of signatories Stamos assembled reads like a cybersecurity honor roll:

- **Bruce Schneier**, fellow at Harvard's Belfer Center and the University of Toronto, and one of the most influential security thinkers of the past three decades
- **Ed Felten**, former Deputy US Chief Technology Officer under the Obama administration and Princeton computer science professor
- **Matthew Green**, cryptographer at Johns Hopkins and a leading voice on encryption policy
- **Eugene Spafford**, Purdue University, a founding figure of academic computer security
- **Chris Wysopal**, founder of Veracode and a former member of the L0pht hacking collective that testified to Congress in 1998 about internet vulnerabilities
- **Joe Levy**, CEO of Sophos
- **Jon Callas**, former Apple and PGP security engineer
- Current and former CISOs from Zoom, Nvidia, Google, Adobe, and other major enterprise technology companies

As of this writing, the letter carries more than 400 signatures and continues to grow.

## The Arguments

The letter makes five core demands of the administration, each revealing a different layer of the signatories' concern.

**First, lift the ban.** The signatories are not dismissive of AI's cybersecurity implications — they acknowledge explicitly that "AI is having significant impacts on cybersecurity, including by greatly reducing the difficulty of finding flaws in software and writing exploits." But they contend that Fable 5 and Mythos 5 are not meaningfully more capable at offensive tasks than other readily available models. Banning them while leaving GPT-5.5, Kimi 2.7, and various open-source models freely accessible does not improve national security — it simply disadvantages defenders who rely on Anthropic's ecosystem.

**Second, establish regulatory science.** The government's handling of this case revealed an alarming absence of a formal evaluation framework. There are no published standards for what makes a model a national security risk, no public criteria for what a jailbreak must look like to trigger export controls, and no process for industry or academia to challenge a risk assessment. The letter calls for regulations grounded in "scientific evaluations with industry and academic input."

**Third, create transparent rule-making.** The 90-minute notice to Anthropic — with no prior consultation, no detailed explanation of the threat, and no opportunity to implement targeted fixes — is what the letter's signatories find most alarming. "A licensing regime by another name," Fortune called it. Transparent democratic rule-making, with appropriate public comment periods and due process, is what the signatories are demanding.

**Fourth, apply rules fairly.** The letter calls for enforcement that applies equally across model providers and that includes appropriate remediation timelines — giving companies the opportunity to address identified vulnerabilities rather than facing sudden shutdowns.

**Fifth, use restraint.** The directive should use "regulatory measures only to the minimal extent necessary" — a nod to the classic security principle that restrictions should be narrowly tailored to the actual risk rather than applied as a precautionary maximum.

## The Broader Fallout

The export ban has had consequences beyond Anthropic's business. In Europe, officials and technologists have seized on the episode as evidence that American AI platforms are subject to sudden, politicized restriction — an argument being used to accelerate investment in European AI alternatives. The European Investment Bank's recent participation in Neura Robotics' funding round, and the EU's continued push for sovereign AI infrastructure, represent exactly the kind of response that strategic export controls risk provoking.

At home, the ban landed in the middle of an already fraught relationship between Anthropic and the Trump administration. The Pentagon declared Anthropic a "supply chain risk" in early March after the company declined to agree to modifications the Department of Defense requested for military applications. The Fable/Mythos directive arrived just three months later. The pattern has not gone unnoticed in Silicon Valley, where AI companies are watching to see whether this represents targeted political pressure or the emergence of a new enforcement posture toward frontier AI.

For Anthropic, the timing has been brutal. Fable 5 — which scored 88% on the FrontierMath Tier 4 benchmark, beating GPT-5.5 by 13 points — was live for less than three days before being pulled. The company has not yet been given a path to reinstatement or told what remediation would satisfy the government's concerns.

The freefable.org letter will not, by itself, reverse a government directive. But 400 senior security professionals formally challenging the scientific basis of that directive is not a small thing. It puts the administration on notice that the cybersecurity establishment — the community the government most needs for its own defensive operations — does not accept the framing of these models as uniquely dangerous. That argument is now part of the public record, and it will shape whatever regulatory framework eventually emerges for frontier AI.
