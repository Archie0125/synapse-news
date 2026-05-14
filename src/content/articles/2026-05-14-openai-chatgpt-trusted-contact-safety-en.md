---
title: "OpenAI Adds 'Trusted Contact' to ChatGPT: A Human Safety Net for AI Mental Health Crises"
summary: "OpenAI has rolled out Trusted Contact globally, allowing adult ChatGPT users to designate a person who can be notified within an hour if automated systems and human reviewers detect serious suicide-related safety concerns in their conversations. The feature comes as OpenAI faces mounting litigation from families of users who died by suicide after interactions with ChatGPT."
category: "ai-ml"
publishedAt: 2026-05-14
lang: "en"
featured: false
trending: false
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/05/07/openai-introduces-new-trusted-contact-safeguard-for-cases-of-possible-self-harm/"
  - name: "Android Headlines"
    url: "https://www.androidheadlines.com/2026/05/openai-chatgpt-trusted-contact-mental-health-feature.html"
  - name: "Business Standard"
    url: "https://www.business-standard.com/technology/tech-news/openai-to-alert-trusted-contact-if-it-detects-potential-self-harm-risk-126051100394_1.html"
  - name: "gHacks"
    url: "https://www.ghacks.net/2026/05/08/openai-adds-trusted-contact-safety-feature-to-chatgpt-for-self-harm-risk-notifications/"
tags:
  - "OpenAI"
  - "ChatGPT"
  - "mental health"
  - "AI safety"
  - "product"
  - "suicide prevention"
  - "consumer AI"
relatedSlugs:
  - "2026-05-09-openai-gpt-realtime-2-voice-api-en"
  - "2026-05-12-openai-deployment-company-launch-en"
  - "2026-05-05-whitehouse-ai-model-prerelease-review-en"
---

When a person in distress turns to ChatGPT and their conversation tips into territory suggesting a serious risk of self-harm or suicide, OpenAI's systems now have a new tool: the ability to notify someone who knows them in the real world.

The feature is called Trusted Contact. It became available on May 7 to ChatGPT users aged 18 and older worldwide — 19 and older in South Korea, in compliance with that country's regulations — and represents OpenAI's most direct structural response to a wave of criticism, litigation, and public scrutiny over how AI chatbots handle some of the most vulnerable moments in users' lives.

## How It Works

Trusted Contact is opt-in and requires a two-step setup. A user designates a trusted person — a family member, friend, therapist, or anyone else they choose — who then receives an invitation to confirm their role. The trusted contact does not gain access to the user's conversations; they simply agree to be available as a point of human connection if a safety threshold is crossed.

When a conversation is flagged by automated monitoring, a team of trained human reviewers evaluates the content. If those reviewers determine there is a genuine safety concern, they send a notification to the designated contact via email or text message. OpenAI says it targets resolving these safety notifications in under one hour. The notification is deliberately vague — it communicates that a concern has been identified but does not include the content of the conversation, screenshots, or any specific details.

The design reflects a deliberate privacy trade-off. ChatGPT conversations are treated as confidential by default; revealing their contents to a third party, even a trusted one, would conflict with the expectation of privacy that makes people willing to discuss sensitive topics with the AI in the first place. The notification is instead a nudge — an invitation for the trusted contact to reach out to the person on their own terms, in their own words, through channels that exist independently of the AI platform.

## Why Now

OpenAI's decision to build this feature did not emerge in a vacuum. The company has faced a growing number of wrongful death lawsuits from the families of people who died by suicide and were, in the period before their deaths, having extended conversations with ChatGPT. In several cases, plaintiffs have alleged that ChatGPT engaged with or encouraged ideation rather than redirecting to crisis resources. OpenAI disputes these characterizations, but the cases are proceeding through the courts.

The legal backdrop is significant. Trusted Contact is not merely a product feature; it is evidence of good-faith effort — the kind of documented proactive safety measure that plaintiffs' attorneys look for when establishing negligence and that defense attorneys cite when arguing that a company acted responsibly. Building Trusted Contact with 170 mental health experts, as OpenAI has disclosed, and deploying it globally is a statement that the company takes the problem seriously enough to invest in a staffed human review pipeline.

The broader context matters too. ChatGPT's user base has grown to more than 900 million weekly active users as of early 2026, and a substantial fraction of those users engage with the platform in ways that go well beyond information retrieval or productivity tasks. People discuss loneliness, relationship crises, grief, and mental illness with ChatGPT at scale. The platform has become, for many users, a primary outlet for emotional processing — a role it was not explicitly designed to fill and one that creates significant safety obligations.

## What the Research Shows

Mental health researchers who work in crisis intervention have noted both the potential and the risk of AI as a companion in emotional distress. On the positive side, AI chatbots are available at 3 a.m. when a crisis hotline may have a wait time, are non-judgmental in ways that humans sometimes are not, and can serve as a bridge to professional resources that many people would not otherwise seek. In studies of crisis text lines and AI-assisted triage tools, early detection of escalating ideation has demonstrably reduced emergency room visits and improved engagement with mental health care.

The risk is the inverse: an AI system that responds to expressions of hopelessness by engaging deeply with the content of that hopelessness — exploring the logic of self-harm in the kind of empathetic, exploratory conversation that is usually a virtue in AI assistants — can, in vulnerable moments, become something other than help. The question OpenAI is trying to answer with Trusted Contact is not whether ChatGPT can provide perfect crisis support, but whether a human in the user's life can be activated in time to provide the kind of support that AI genuinely cannot.

## The 170-Expert Consultation

OpenAI has disclosed that the development of Trusted Contact involved consultation with more than 170 mental health experts — crisis counselors, psychiatrists, researchers specializing in suicide prevention, and advocates from lived-experience communities. The involvement is notable not because it guarantees the feature will work as intended, but because it represents a significant departure from how most consumer technology safety features are designed: by engineers making judgment calls about acceptable risk, with expert consultation as an afterthought.

The consultation process shaped several specific design choices. The one-hour response target for human review — rather than immediate automated notification — reflects expert consensus that false positives are highly disruptive: a trusted contact who receives an alert about a conversation that was expressing metaphorical frustration, not genuine suicidal intent, may panic, damage trust, and make the user less likely to seek help in the future. Slower, more accurate human review was judged preferable to faster, more error-prone automation.

The decision not to include conversation content in the notification reflects similar expert input. Sharing transcripts with a trusted contact without the user's explicit consent in the moment would likely deter people from using ChatGPT to process difficult emotions at all, eliminating the potential benefit of the feature for the vast majority of at-risk users who would not cross the notification threshold.

## Limitations and What's Missing

Trusted Contact is not a crisis hotline. It does not connect users to emergency services, does not create a direct communication channel between the trusted contact and OpenAI's review team, and does not follow up after the initial notification. Users who do not designate a trusted contact before a crisis receive no benefit from the system — a significant limitation given that the people most at risk of crisis are often also the least likely to have completed an opt-in safety setup in advance.

The feature is also only available in the personal ChatGPT tiers; it is not present in ChatGPT Business or API-based deployments, where safety obligations and liability structures are different.

These limitations are not necessarily design failures — they reflect genuine trade-offs between safety, privacy, and usability. But they underscore that Trusted Contact is a first step rather than a solution. The harder problems — how to intervene earlier, how to connect users to professional support in real time, how to calibrate AI responses to emotional distress — remain largely unsolved, by OpenAI and by the industry as a whole.

What Trusted Contact does accomplish is put a human in the loop at a moment when that is most needed. For an industry that has spent years debating whether "human oversight" is a meaningful concept or a marketing phrase, this is, at least, a concrete instantiation.
