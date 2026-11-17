---
category: ai-ml
faqs:
- answer: Gemini Omni 1.2 Flash 支援原生生成 15 秒影片（先前為 10 秒），新增多輪對話式編輯，對角色、商品與風格參考素材的遵循度也更高。目前已透過
    Gemini API 與 Gemini for business 全面開放。
  question: Gemini Omni 1.2 Flash 有哪些新功能？
- answer: 720p 影片每秒 0.07 美元，比 Gemini Omni 1.1 便宜 30%。生成一段 15 秒的 720p 影片約 1.05 美元，使用者也可以先用
    360p 或 720p 打草稿，再把最好的版本升級到 1080p 或 4K。
  question: Gemini Omni 1.2 Flash 的價格是多少？
- answer: 它的功能主要針對商業影片製作，例如虛擬試穿、商品環繞展示與品牌社群廣告。參考素材遵循度提升後，臉孔、服裝、包裝字體與品牌色在不同鏡頭角度下都能保持一致，對電商與行銷團隊最有用。
  question: Gemini Omni 1.2 Flash 適合哪些使用者？
featured: false
lang: zh
publishedAt: '2026-11-05T17:00:00+00:00'
relatedSlugs: []
sources:
- name: Google AI Blog
  url: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/
summary: Gemini Omni 1.2 Flash 鎖定的是廣告代理商，而不是電影創作者。價格砍三成，單支影片最長可達 15 秒，用 AI 生成產品廣告的成本已經比請人拍一組照片還低。
tags:
- ai-ml
- products
title: Gemini Omni 1.2 Flash 登場：更快、更便宜，影片長度再拉長
trending: false
type: news
---

# Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips

Today, we’re rolling out [Gemini Omni](https://deepmind.google/models/gemini-omni/) 1.2 Flash, and making it generally available across the [Gemini API](https://aistudio.google.com/docs/omni) and [Gemini for business](https://cloud.google.com/blog/products/ai-machine-learning/gemini-omni-1-2-flash-generally-available). Gemini Omni 1.2 Flash introduces native 15-second video creation, multi-turn conversational editing capabilities, and enhanced reference following. We have dropped the price 30% from Gemini Omni 1.1 making it available at $0.07 per second for 720p video.

Here’s an overview of what’s new:

## Fast and cost-effective at scale

Beyond the lower price, the workflow keeps costs down: you can draft fast at 360p or 720p, fix a detail with a follow-up edit instead of re-generating the entire clip, and then upscale your best creations to 1080p or 4K.

## Longer clips up to 15 seconds

You can now generate and edit videos natively up to 15 seconds long, up from 10 seconds with Omni 1.1. You can also specify duration in one-second increments from 3 to 15 seconds, giving you room to tell complete stories, create product explainers, or produce full social ad spots in a single generation.

## Better reference adherence

You can guide generation combining character, product, or style images, short motion clips (up to three seconds), and audio cues — and Omni 1.2 Flash holds onto those details from start to finish. Faces, garments, packaging typography, and brand colors stay consistent across camera angles, making it easy to turn existing product photography or character sheets into virtual try-on clips, catalog spins, and branded video ads.

Combining one model photo with front-and-back product shots of three outfits, Gemini Omni 1.2 Flash generates a 15-second virtual try-on sequence across 360-degree turns and match cuts while keeping the model’s identity and each garment’s cut, drape, and back details consistent.

## More consistent results

You can maintain stronger character, object, and scene consistency from the first to the last frame, with less visual drift or morphing across motion and camera transitions. Whether you’re interpolating between a first and last keyframe, or extending a clip to build a longer sequence, products, characters, props, and environments stay consistent from shot to shot.

Given the same static studio lighting exhibition poster and five-layer animation prompt, Gemini Omni 1.1 Flash does not match the reference image as closely as 1.2 does. Gemini Omni 1.2 Flash builds the poster sequentially layer by layer on the dusty-pink cyclorama rising the hexagonal plinth, assembling the ribbed glass, warm filament, faceted crystal, and coiled-cord letterforms for HALO, GLOW, and LUMEN, and locking every material, shadow, and typographic detail consistently through the final frame.

## Easier editing in conversation

You can refine the same clip turn by turn — such as swapping a product or background, changing the lighting or weather, or switching the aspect ratio — instead of starting over from scratch. Multi-turn conversational editing works across full 15-second clips, making it easy to produce ad variants for different audiences and placements without re-briefing or re-generating.

Starting from one generated clip, multi-turn conversational prompts swap the background turn by turn — from a striped pavilion tent to an oak forest, a stable with a white horse, a market fair, and a stone castle — while keeping both characters’ performances, armor reflections, and camera framing intact.

## More natural speech

You can generate scenes with more fluid, natural-sounding dialogue, clearer lip-sync, and distinct multi-speaker conditioning. This will show up whether you’re directing multi-character dialogue in [Flow](https://labs.google/fx/tools/flow), creating video explainers in [Gemini for business](https://cloud.google.com/gemini-enterprise), or creating polished, pro videos with avatars, music and narration in [Google Vids](https://docs.google.com/videos/create?usp=blog).

Conditioned on one conservatory scene image alongside four character, mouth, and one-second voice references, Gemini Omni 1.2 Flash routes each sampled voice to the right character with expressive lip-sync and natural comedic timing across a 15-second animated scene.

## More controllable, cinematic look

You can direct complex, continuous camera movements like sweeping FPV flythroughs to dramatic zoom-outs and orbits with significantly fewer unwanted jump cuts, steadier scale, and a more polished, cinematic look.

Guided by two architectural reference photos, Gemini Omni 1.2 Flash directs one continuous FPV drone flight across the piazza, through the bronze doors, and up through the Pantheon’s coffered dome to the oculus with zero jump cuts.

## Longer clips with smoother motion and tighter consistency

Gemini Omni 1.2 Flash generates clips up to 15 seconds long that hold references together better than before. You can scroll through to see characters, text, and camera moves stay consistent across longer shots, multiple turns and transitions with no cuts.

## Real-world results, from creatives to global brands

Businesses, startups, and creatives are already using Gemini Omni 1.2 Flash in their workflows. And for the first time, Gemini Omni is now generally available, backed by Google Cloud’s enterprise-grade infrastructure and security. [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput) is available, and outputs carry an imperceptible [SynthID](https://deepmind.google/models/synthid/) watermark.

## Get started with Gemini Omni 1.2 Flash

While development is ongoing to further improve things like fast sports action, rapid script changes and complex physics, Gemini Omni 1.2 Flash is ideal for businesses, developers, and creators producing videos at scale. You can get started with Gemini Omni 1.2 Flash today as it rolls out across Google’s products and developer platforms:

- **For developers using the Gemini API:** Prototype in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-omni-1.2-flash&utm_source=deepmind.google&utm_medium=referral&utm_campaign=gdm&utm_content=), explore interactive starter apps, and check out the [developer documentation](https://aistudio.google.com/docs/omni) and [pricing](https://aistudio.google.com/docs/pricing#gemini-omni-1.2-flash).
- **For businesses:** Try it in the [Google Cloud console](https://console.cloud.google.com/vertex-ai/studio/media), and build enterprise solutions with the [API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-2-flash).
- **For everyone using Google apps:** Direct scenes and multi-turn edits in [Flow](https://labs.google/fx/tools/flow), generate 15-second clips at no additional cost in [Google Vids](https://docs.google.com/videos/create?usp=blog) with a Google account or Google Workspace subscription, create 15-second videos in the [Gemini app](https://gemini.google.com/) (rolling out to Google AI Ultra subscribers), and scale video campaigns in [Google Ads](https://ads.google.com/aw/assetstudio).

## Summary

**TLDR:** Gemini Omni 1.2 Flash goes after ad agencies, not filmmakers. A 30% price cut plus 15-second clips makes AI-generated product ads cheaper than a photo shoot.

- Gemini Omni 1.2 Flash is generally available through the Gemini API and Gemini for business at $0.07 per second for 720p, 30% cheaper than Omni 1.1.
- Native video length rises from 10 to 15 seconds, set in one-second increments from 3 to 15 seconds.
- Multi-turn conversational editing lets users fix one detail without regenerating the whole clip.
- Better reference adherence keeps faces, garments, packaging text, and brand colors consistent across camera angles.
- The features target e-commerce use cases such as virtual try-ons, catalog spins, and social ads.

## 摘要

**重點摘要：** Gemini Omni 1.2 Flash 鎖定的是廣告代理商，不是電影人。降價 30% 加上 15 秒影片，讓 AI 生成的商品廣告比拍一場照片還便宜。

- Gemini Omni 1.2 Flash 已透過 Gemini API 與 Gemini for business 全面開放，720p 影片每秒 0.07 美元，比 Omni 1.1 便宜 30%。
- 原生影片長度從 10 秒增加到 15 秒，可在 3 到 15 秒之間以一秒為單位設定。
- 支援多輪對話式編輯，修改單一細節時不必重新生成整段影片。
- 參考素材的遵循度提升，臉孔、服裝、包裝字體與品牌色在不同鏡頭角度下都能保持一致。
- 這些功能瞄準電商用途，例如虛擬試穿、商品環繞展示與社群廣告。