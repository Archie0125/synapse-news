---
title: "OpenAI Launches ChatGPT Health, Connecting 300 Million Users to Their Medical Records"
summary: "OpenAI has officially launched Health in ChatGPT for all U.S. users, enabling secure connections to Apple Health, hospital medical records, One Medical, and fitness apps including Peloton and MyFitnessPal. The feature arrives as more than 300 million people per week already ask ChatGPT health questions — and surfaces a privacy debate about whether HIPAA protections follow medical data into AI conversations."
category: "products"
publishedAt: 2026-07-27
lang: "en"
featured: false
trending: true
sources:
  - name: "OpenAI: Launching Health in ChatGPT"
    url: "https://openai.com/index/health-in-chatgpt/"
  - name: "gHacks: OpenAI Launches Health in ChatGPT"
    url: "https://www.ghacks.net/2026/07/25/openai-launches-health-in-chatgpt-for-us-users-connecting-apple-health-and-medical-records/"
  - name: "Startup Fortune: OpenAI connected 300 million weekly health queries"
    url: "https://startupfortune.com/openai-connected-300-million-weekly-health-queries-to-real-medical-records-and-the-implications-are-enormous/"
  - name: "Startup Fortune: HIPAA analysis"
    url: "https://startupfortune.com/openai-launched-chatgpt-health-and-quietly-moved-your-medical-records-outside-hipaa/"
  - name: "9to5Mac: OpenAI relaunches Apple Health feature"
    url: "https://9to5mac.com/2026/07/23/openai-relaunches-apple-health-connected-chatgpt-feature-with-expanded-access/"
tags:
  - "openai"
  - "chatgpt"
  - "health"
  - "apple-health"
  - "medical-records"
  - "privacy"
  - "hipaa"
  - "consumer-ai"
relatedSlugs:
  - "2026-07-26-anthropic-claude-opus-5-launch-en"
  - "2026-07-27-deepseek-v4-general-availability-swe-bench-pricing-en"
---

OpenAI quietly made one of the most consequential product moves in consumer health technology last week: it launched Health in ChatGPT for all logged-in U.S. adults, enabling them to connect real medical records and Apple Health data to their ChatGPT conversations. The feature is live on web and iOS across every plan tier — Free, Go, Plus, and Pro — and the implications run well beyond a new settings toggle.

The reason the stakes are high is simple arithmetic. OpenAI says more than 300 million people per week already use ChatGPT to ask health questions. Before this launch, those conversations were entirely hypothetical — ChatGPT could discuss symptoms and medications in general terms, but had no access to what a specific user was actually experiencing. Health in ChatGPT changes that from the ground up.

## What Users Can Connect

The list of supported data sources is broader than most observers expected for a first version. Users can connect:

**Medical Records:** Hospital systems throughout the United States, One Medical (Amazon's primary care network), and Function Health, a membership-based preventive diagnostics service that runs comprehensive annual lab panels.

**Fitness and Lifestyle Platforms:** Apple Health (the primary aggregator for iPhone users), MyFitnessPal for nutrition and food logging, Peloton for workout and cardiovascular data, Instacart for grocery and food purchasing history, AllTrails for outdoor activity, and Weight Watchers for dietary tracking.

Once connected, ChatGPT can access medications, lab results, recent clinical visit summaries, sleep metrics, activity data, and longitudinal changes in tracked health markers. The envisioned use cases include comparing a new lab result to prior tests, summarizing what has changed since a patient's last appointment, or correlating sleep and activity patterns with reported symptoms.

## The HIPAA Question Nobody Is Asking Loudly Enough

The most significant controversy around the launch has been muted in mainstream coverage but widely discussed in health policy and legal circles. OpenAI is not a Covered Entity under HIPAA — the U.S. health data privacy law that governs how medical information can be collected, used, and disclosed. When a patient's records leave a hospital's system and enter OpenAI's infrastructure, those records are no longer governed by the same federal protections they had in the clinical setting.

OpenAI has addressed this indirectly by committing that connected health data will not be used to train foundation models and will not be used for advertising targeting. The company has also implemented additional encryption for health conversations beyond its standard at-rest and in-transit encryption. But "additional encryption" is a security claim, not a legal privacy claim. The data's protection depends on OpenAI's contractual commitments to users, not on the federal enforcement apparatus that backs HIPAA.

For many users, that distinction won't matter in practice — the experience of asking ChatGPT to help them understand their lab results in the context of their actual history is genuinely valuable, and most people do not track whether their data is covered by federal privacy law. But for patients dealing with sensitive diagnoses — mental health conditions, reproductive health, certain infectious diseases — the absence of formal HIPAA coverage is a meaningful difference from what they might assume.

## Why Now

Three factors converged to make this launch possible in mid-2026. First, Apple's HealthKit API maturity has reached the point where third-party integrations are substantially more reliable than they were even two years ago, and Apple's own interest in expanding the health ecosystem (while maintaining its position as the preferred on-device aggregator) created alignment. Second, the proliferation of FHIR-compliant medical record APIs — the federal interoperability mandate that required most major U.S. health systems to expose machine-readable patient data by 2023 — finally gave OpenAI a standardized way to query records across diverse hospital systems without building custom integrations for each. Third, OpenAI's enterprise revenue growth has made the company genuinely invested in capturing health and life sciences as vertical markets, and a consumer-facing health feature is the company's most efficient way to demonstrate capability to enterprise buyers.

The fitness platform partnerships deserve separate attention. Instacart's inclusion is the most unexpected — it means users who connect the service give ChatGPT visibility into their grocery purchasing history, which is a surprisingly revealing signal about diet, household composition, and economic behavior. The case for inclusion is that dietary data is genuinely clinically relevant; the case against is that grocery purchase history is substantially more sensitive than step count.

## The Broader Competitive Context

ChatGPT Health arrives in a landscape where every major AI platform is making moves into healthcare. Google has been integrating health capabilities into Gemini through its partnership with major hospital systems and its acquisition of various health AI assets. Amazon has a natural incentive through One Medical and the Amazon Clinic telehealth service it launched in 2023. Apple is playing a longer game, keeping health data on-device through Apple Intelligence while partnering with third parties like OpenAI through the formal arrangement established in 2024.

OpenAI's approach — connect to the data that already exists across fragmented systems and bring it into a conversational interface that 300 million people already trust — is arguably the most pragmatic near-term strategy. The network effects are real: the more health context a user shares, the more useful ChatGPT becomes for health questions, which creates an incentive to share more health context. That flywheel is exactly what made the consumer internet companies of the 2010s so durable.

The question health advocates are starting to ask is whether the value of that flywheel should be weighed against the question of who ultimately controls the health data of hundreds of millions of people — and what accountability structures exist if OpenAI's privacy commitments ever change.

## What's Available and What's Next

The current launch covers the U.S. only, with no announced international rollout timeline. The feature requires an active ChatGPT account and age verification (18 and older). Apple Health integration is iOS-only in the current version; users on Android or desktop without an iPhone cannot access that connection today.

OpenAI has not disclosed which hospital systems are currently supported beyond the general descriptor of "U.S. hospital systems," which is expected to expand progressively as FHIR integration agreements are signed. One Medical and Function Health are fully integrated at launch.

The company has said it intends to add more fitness and lifestyle connections over time, with the current list described as an initial set rather than a complete vision. Whether that expansion includes more medically sensitive platforms — reproductive health tracking apps, mental health services, substance use recovery tools — will be a significant test of how OpenAI balances utility against the privacy exposure of its most vulnerable users.
