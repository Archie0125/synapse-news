---
title: "Google I/O 2026: Gemini 3.5, Project Astra Goes Live, and Android XR Glasses Arrive"
summary: "Google's biggest developer event of the year delivered a sweeping AI offensive: a new Gemini flagship model, the long-awaited general availability of Project Astra, first-look hardware for Android XR smart glasses, Android 17 with Gemini Intelligence at the OS level, and Aluminium OS — a full Android-based replacement for ChromeOS."
category: "ai-ml"
publishedAt: 2026-05-19
lang: "en"
featured: true
trending: true
sources:
  - name: "Android Central Live Blog"
    url: "https://www.androidcentral.com/phones/live/google-i-o-2026-live-blog-android-17-android-xr-glasses-and-all-the-gemini-ai-news"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/google-io-2026-gemini-intelligence-android-xr-glasses"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/316755/20260517/google-i-o-2026-keynote-opens-tuesday-new-gemini-lands-behind-mythos-gpt-55.htm"
  - name: "Android Authority"
    url: "https://www.androidauthority.com/what-to-expect-from-google-io-2026-3664979/"
  - name: "NPowerUser"
    url: "https://nokiapoweruser.com/google-io-2026-gemini-spark-omni-gemini-3-5-rumors/"
tags:
  - "google"
  - "gemini"
  - "android"
  - "project-astra"
  - "android-xr"
  - "io2026"
  - "ai"
relatedSlugs:
  - "2026-05-18-google-googlebook-gemini-intelligence-android-show-en"
  - "2026-05-15-google-gemini-omni-video-model-leak-en"
  - "2026-05-15-google-io-2026-preview-gemini-android-en"
---

Google's annual developer conference arrived at Shoreline Amphitheatre in Mountain View on Tuesday with an aggressive pivot: after two years of demonstrating AI potential, Google used I/O 2026 to prove it could ship. CEO Sundar Pichai opened the keynote with a declaration that "the era of AI demonstration is over — the era of AI deployment begins today," and the two-hour event that followed backed the claim with a volley of product announcements spanning models, operating systems, and new hardware categories.

## Gemini 3.5: Closing the Gap

The headline announcement was the general availability of Gemini 3.5 Pro, Google's latest flagship model. Benchmark analysts tracking the AI race had expected a model landing between OpenAI's GPT-5.5 and Anthropic's Claude Mythos, and the released numbers align with those predictions: Gemini 3.5 Pro posts state-of-the-art scores on complex coding, multi-step reasoning, and scientific problem-solving tasks, while trailing Anthropic's Mythos on the most demanding long-horizon planning benchmarks.

More commercially significant is Gemini 3.2 Flash, a speed-optimized tier designed for mass deployment. Google confirmed it delivers 2.5× faster response times than its predecessor, with 45% faster token generation, and is priced at $0.25 per million input tokens — a price point that undercuts most competitors and is designed to make Gemini the default inference layer for developers building latency-sensitive applications. Gemini 3.2 Flash is being rolled into Google Search, Maps, YouTube, Docs, Gmail, and Chrome simultaneously, reaching billions of users on launch day.

Google also unveiled Gemini Spark, a lightweight on-device model family optimized for mobile processors. Spark handles local inference for Pixel phones and Android OEM devices without requiring a server round-trip, enabling features like real-time translation, offline summarization, and always-on ambient assistance while preserving user privacy.

## Project Astra: From Demo to Product

Two years after its splashy debut at I/O 2024, Project Astra graduated from limited preview to general availability. Astra is Google's multimodal universal assistant — capable of understanding live video, audio, and text in a continuous, stateful conversation — and it is now accessible to all Google One AI Premium subscribers and Android developers via API.

The production version adds significant new capabilities over the prototype: persistent memory that carries context across sessions, action-taking via Android's new Gemini Intelligence APIs (Astra can draft emails, set calendar events, and control compatible smart home devices based on what it sees through the camera), and a latency profile that Google claims drops average response time to under 800 milliseconds for most tasks.

Google demoed Astra reading a whiteboard sketch, reasoning about a chemistry equation, then navigating to a relevant research paper and summarizing it — all without breaking conversational flow. Whether that performance holds outside a keynote stage will be the question every developer with early API access is now running down.

## Android XR Glasses: Hardware Finally Lands

The most visually striking segment of the keynote was the debut of Android XR smart glasses. Google confirmed two variants: a lightweight audio-focused model with built-in microphones, speakers, and a Qualcomm Snapdragon AR1 chip for hands-free Gemini interaction; and a more advanced version with in-lens optical displays capable of overlaying navigation directions, live translation subtitles, and contextual information in the wearer's field of view.

The reference hardware, codenamed Jinju, carries a 12-megapixel Sony camera module, Bluetooth 5.3, and weighs approximately 50 grams — light enough for all-day wear. Google confirmed hardware partners including Samsung, with OEM devices expected in late 2026. Project Astra vision technology powers the glasses' contextual awareness, with Gemini 2.5 Pro handling on-cloud reasoning when the local AR1 chip reaches its limits.

The glasses put Google in direct competition with Meta's Ray-Ban smart glasses and the anticipated Apple AR product roadmap. Unlike Meta's current offering, Google's display-equipped variant can surface visual information without requiring the user to check a phone — a meaningful usability distinction in navigation and translation scenarios.

## Android 17 and Gemini Intelligence

Android 17 developer preview shipped alongside the keynote, with stable release targeted for Q3 2026. The central theme is Gemini Intelligence — a set of OS-level APIs that give apps direct access to on-device Gemini models. Developers can invoke Gemini for in-app summarization, content generation, semantic search, and real-time assistance without building their own model integrations.

Material 3 Expressive brings a redesigned visual language with more dynamic, adaptive UI animations. Android Auto received the largest update in years, adding widgets, native video app support, and Dolby Atmos audio processing for supported vehicles. Wear OS 7, bundled with Android 17, adds health-monitoring improvements and a Gemini-powered watch face that surfaces personalized daily briefings.

## Aluminium OS: Google's ChromeOS Replacement

The most strategically significant non-model announcement was Aluminium OS, Google's Android-based replacement for ChromeOS, targeting consumer laptops. Google VP Sameer Samat had confirmed a 2026 launch earlier in the year, and I/O delivered the first full public preview.

Aluminium OS runs a full Android app ecosystem, supports Linux containers for developer workflows, and integrates Gemini at the system layer — search, clipboard, and camera all route through Gemini for contextual suggestions. Google confirmed hardware partner support from Acer, ASUS, Dell, HP, and Lenovo, with the first Aluminium OS laptops (running as "Googlebooks") expected in fall 2026.

The move acknowledges what the market has communicated for years: ChromeOS's limited app ecosystem has capped its addressable market to education and enterprise. By pivoting to Android as the base, Google gains a mature app store and a developer ecosystem several orders of magnitude larger than ChromeOS ever had.

## Context: Why This Keynote Matters

The AI industry benchmark context makes Google's position clear. OpenAI leads at the frontier with GPT-5.5 and its successors; Anthropic holds the highest ceiling with Claude Mythos on complex reasoning. Google's advantage is distribution — no other AI company can roll a model update to billions of active users on day one across Search, Gmail, Maps, and YouTube simultaneously.

Gemini 3.5 and 3.2 Flash represent Google's attempt to convert that distribution advantage into lasting model momentum. The $0.25/M Flash pricing is a direct challenge to Anthropic's Haiku and OpenAI's GPT-4o-mini for developer adoption. And Project Astra's production launch finally gives Google a multimodal flagship product rather than a research demonstration.

The two-day conference continues through May 20 with deep-dive developer sessions on Gemini APIs, Astra integration, Android 17's Gemini Intelligence framework, and Android XR development tools. The product pipeline Google revealed on Tuesday suggests the company intends to win the AI deployment race on volume, price, and ecosystem reach — even if it trails the frontier on raw model capability.
