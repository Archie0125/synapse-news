---
title: "Google's 'Gemini Omni' Video Model Leaks Days Before I/O — and It May Unify the Entire Gemini Stack"
summary: "A UI string discovered in the Gemini app on May 2 revealed 'Powered by Omni' — Google's unreleased unified video model. Early leaked footage shows object swapping, in-chat video editing, and template-based creation. With Google I/O keynote four days away on May 19, Gemini Omni may be the biggest AI video reveal of 2026."
category: "ai-ml"
publishedAt: 2026-05-15
lang: "en"
featured: false
trending: false
sources:
  - name: "Testing Catalog"
    url: "https://www.testingcatalog.com/googles-gemini-omni-video-model-surfaces-ahead-of-i-o-debut/"
  - name: "Android Authority"
    url: "https://www.androidauthority.com/google-gemini-omni-video-model-leak-3665801/"
  - name: "Chrome Unboxed"
    url: "https://chromeunboxed.com/an-impressive-new-gemini-omni-video-model-just-leaked-ahead-of-google-i-o/"
  - name: "AIxploria"
    url: "https://www.aixploria.com/en/ai-radar/google-gemini-omni-leak-video-model-io-2026/"
tags:
  - "Google"
  - "Gemini"
  - "Gemini Omni"
  - "video AI"
  - "Google IO"
  - "AI video generation"
  - "multimodal"
relatedSlugs:
  - "2026-05-15-google-io-2026-preview-gemini-android-en"
  - "2026-05-12-android-show-io-2026-android17-xr-en"
  - "2026-05-13-google-googlebook-ai-laptop-en"
---

Four days before Google's annual developer keynote, the company accidentally previewed one of its most significant AI announcements — and it wasn't Gemini 4.

A UI string surfaced inside the Gemini app on May 2, eleven days before Google I/O opens on May 19, reading simply: "Start with an idea or try a template. Powered by Omni." The discovery, first reported by TestingCatalog — a publication with a strong track record of uncovering Google AI features before official release — set off a wave of analysis and speculation that has only intensified as the I/O keynote approaches.

What has leaked, piece by piece over the past two weeks, suggests that "Gemini Omni" is not a minor model update. It may be the most consequential thing Google announces at I/O 2026.

## What the Leak Reveals

The UI text that surfaced alongside the "Powered by Omni" string was more explicit about capabilities: "Create with Gemini Omni: meet our new video model, remix your videos, edit directly in chat, try templates, and more."

Those four capabilities — remix, chat-based editing, templates, and raw generation — represent a meaningfully different approach to AI video than what the market currently offers. Google's existing video generation capability, Veo 3.1, produces impressive output but operates as a largely standalone generation system: describe what you want, receive a clip. The Omni description implies something more interactive and iterative.

Leaked demo footage shared online before Google could remove it suggested the following specific capabilities:

**Object replacement within existing clips**: Users could select an object in a video and describe a replacement, with Omni regenerating the affected frames while maintaining visual consistency with the surrounding content. Demo examples included replacing background elements and swapping protagonist clothing between shots.

**Watermark and overlay removal**: Leaked clips showed Omni being able to identify and cleanly remove watermarks and text overlays from video footage — a capability with obvious commercial value for content cleanup and repurposing workflows.

**Scene rewriting via chat instructions**: Users could describe changes to a generated scene in conversational language — "make this sunset more dramatic," "change the dialogue to be faster-paced" — and receive an updated version without re-entering a full generation prompt.

**Template-based creation**: Pre-built scene templates that users could populate with their own content, lowering the barrier for non-technical creators to produce structured video formats like product demonstrations or explainer videos.

## What Kind of Model Is Omni?

The name has generated significant speculation about what Gemini Omni actually is under the hood. Three distinct hypotheses have emerged from the AI research community:

**Hypothesis 1: Omni is a rebrand of the Veo pathway.** The simplest interpretation is that Google is renaming its existing Veo-powered video generation capability to "Omni" for consumer-facing products while keeping the underlying model unchanged. This would be primarily a marketing decision.

**Hypothesis 2: Omni is a new standalone video model.** The capability descriptions — particularly the interactive chat-based editing and object replacement — go beyond what Veo 3.1 has demonstrated publicly. This hypothesis holds that Omni is a purpose-built video generation and editing model that runs alongside, rather than replacing, the Veo family.

**Hypothesis 3: Omni is a unified multimodal model.** The most expansive interpretation is that Gemini Omni is a new architecture that handles text, image, and video generation within a single model family, replacing the patchwork of separate systems (Gemini for text, Imagen for images, Veo for video) with a unified generation pipeline. This would represent a significant architectural consolidation and would explain why the model is called "Omni" — it handles everything.

The evidence from the leaked UI and demo footage is most consistent with Hypothesis 3. The in-chat editing interface, in particular, suggests a model that understands video content in the same contextual way that Gemini understands text — able to follow instructions that reference specific elements of existing content rather than generating from scratch.

## Usage Limits and Compute Cost

One detail from early leaked access has attracted attention: Gemini Omni appears to be heavily resource-intensive, and Google has imposed significant usage limits even for subscribers to its highest consumer tier.

A user on the Google AI Pro plan — which currently costs $20 per month — reported that generating two detailed video clips consumed 86 percent of their daily usage limit. This suggests that the daily compute allocation for Omni generation is approximately 2 to 3 full video generations per day at the highest quality settings, or a larger number of shorter clips at reduced resolution.

For context, Runway and Sora allocate video generation budgets in minutes of generated footage per month, with monthly limits ranging from 125 to 2,000 seconds depending on subscription tier. Google's apparent approach of daily limits rather than monthly cumulative budgets is unusual and may reflect the compute cost of real-time interactive editing compared to batch generation.

## Competitive Context

The AI video generation market has accelerated dramatically in 2026. ByteDance's Seedance 2 — widely considered the current leader in raw generation fidelity — has set a high quality bar that competing models are racing to meet. OpenAI's Sora has expanded access but remains constrained in editing capabilities. Runway's Gen-4 series continues to improve, particularly for cinematic-style generation.

Early assessments of the Gemini Omni footage suggest that on pure generation quality — the realism and motion coherence of newly created clips — it lags behind Seedance 2 at equivalent resolutions. But the comparison may be somewhat unfair: Omni's apparent differentiation is not generation quality alone but the interactive editing layer, which positions it as a tool for content modification and remixing rather than primarily a from-scratch generation system.

If the Hypothesis 3 (unified multimodal) interpretation is correct, the competitive comparison also shifts. A model that can discuss, analyze, edit, and generate video within the same conversational context as text — integrated into the Gemini assistant interface that billions of people already use — has a distribution advantage that specialized video generators cannot easily replicate, regardless of output quality at the margin.

## What to Watch at Google I/O

Google I/O 2026 opens on May 19 with a keynote beginning at 10:00 a.m. PT. Based on the leaked information and the cadence of Google's pre-I/O disclosure pattern, the following is expected:

Google will formally reveal Gemini Omni by name and demonstrate its interactive editing capabilities with curated examples that showcase the gap between Omni and existing video generation systems. The specific framing — whether it's positioned as a new Gemini model, an upgrade to Veo, or a standalone product — will clarify the Hypothesis 1/2/3 question.

Availability timeline is also critical. Leaked UI typically precedes rollout by two to eight weeks for Google AI features. If Gemini Omni follows that pattern, Pro plan subscribers could have access to the model within days of I/O.

Pricing remains entirely unclear. The heavy compute footprint of interactive video editing suggests Omni may eventually be gated behind a higher-priced tier or offered as a separate add-on — though Google may choose to include it in existing Pro plans as a competitive differentiator against the launch period for Apple's iOS 27 AI features at WWDC in June.

For now, the existence of Gemini Omni is no longer speculative. The question is how large the gap between the leak and the reality turns out to be.
