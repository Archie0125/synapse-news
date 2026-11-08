---
category: ai-ml
faqs:
- answer: Hugging Face 和 Liva AI 新增了埃及英語（1.34 小時）和奈及利亞英語（1.55 小時）兩組不公開的對話測試集。排行榜也開始分開列出美國與非美國口音，以及
    Kachru 模型中內圈與外圈、擴展圈口音的成績。
  question: Open ASR 排行榜這次改了什麼？
- answer: 開發者看不到測試資料，就沒辦法拿它訓練或調參，刷榜會難很多。這樣排行榜的分數比較能反映模型在真實環境的準確度。
  question: 不公開的測試集對語音辨識評測有什麼意義？
- answer: Hugging Face 表示，隨著口音越來越多，會把外圈與擴展圈再拆得更細。最值得看的是：頂尖模型在內圈英語和其他英語之間，是否一直有明顯的準確度落差。
  question: 接下來值得關注什麼？
featured: false
lang: zh
publishedAt: '2026-11-06T00:00:00+00:00'
relatedSlugs: []
sources:
- name: Hugging Face Blog
  url: https://huggingface.co/blog/open-asr-leaderboard-liva
summary: Open ASR 排行榜納入埃及與奈及利亞英語，是對抗「刷榜」現象的必要一步，但測試音檔總長不到三小時，樣本量仍嫌單薄，難以據此下定論。
tags:
- ai-ml
- open-source
title: Open ASR 排行榜新增埃及與奈及利亞英語
trending: false
type: news
---

A few months ago, we added private data to the [Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard): 11 splits from Appen and DataOceanAI covering scripted and conversational speech from five accents ([blog](https://huggingface.co/blog/open-asr-leaderboard-private-data)). The community response was great, with many **highlighting the importance of held-out sets for trustworthy evaluations**. Since then, we added one more private split for Indian-accented English with Voice Arena ([blog](https://huggingface.co/blog/open-asr-leaderboard-global-south)).

We’re excited to announce a new collaboration with [Liva AI](https://huggingface.co/liva-ai) to add even more private data with two new accents: **Egyptian** 🇪🇬 and **Nigerian** 🇳🇬.

| Dataset | Accent | Duration \[h\] | Style | Transcription | 
|---|---|---|---|---|
| Liva AI Conversational EG | Egyptian | 1.34 | Conversational, spontaneous | Punctuated, cased, with disfluencies. | 
| Liva AI Conversational NG | Nigerian | 1.55 | Conversational, spontaneous | Punctuated, cased, with disfluencies. | 

This is part of our continued effort to improve representation in ASR evals (more accents and more languages) and to improve trust (new private data to minimize benchmaxxing, and new data providers). We’re excited to see the community continuing to push ASR performance for the world 🤗

With these new accents, we can now present a richer breakdown of accents, based on [Kachru’s Three Circles](https://en.wikipedia.org/wiki/World_Englishes#Kachru%27s_Three_Circles_of_English) (kudos to Hume AI for this idea in their [leaderboard](https://huggingface.co/spaces/HumeAI/asr-leaderboard)). The Open ASR Leaderboard will now report:

1. US vs. non-US (*UK, Australia, Canada, India, Nigeria, Egypt*)
2. Inner Circle (*US, UK, Australia, Canada*) vs. Outer & Expanding Circles (*India, Nigeria, Egypt*)

As more accents join, we’ll split the Outer and Expanding Circles.

Liva AI collects multimodal interaction data through consumer products used by real people. Because Liva owns both the collection environment and distribution, it can design products around specific model gaps across domains, industries, languages, modalities, and interaction types. This gives it access to natural, high-context behavior that emerges through real product use, rather than artificially elicited or task-based interactions.

## Summary

**TLDR:** Adding Egyptian and Nigerian English to the Open ASR Leaderboard is a needed step against benchmaxxing, but under three hours of audio is a thin sample to judge by.

- Hugging Face partnered with Liva AI to add private, held-out conversational test sets in Egyptian English (1.34 hours) and Nigerian English (1.55 hours).
- The leaderboard now reports US vs. non-US results and, based on Kachru's Three Circles, Inner Circle vs. Outer and Expanding Circle accents.
- Private data is meant to reduce benchmaxxing, where models are tuned to public test sets instead of real-world speech.
- The new sets are spontaneous speech transcribed with disfluencies, which is much harder than scripted read-aloud audio and closer to how real voice products get used.

## 摘要

**重點摘要：** Open ASR 排行榜加入埃及與奈及利亞英語口音，方向正確，能抑制刷榜，但兩組加起來不到三小時，樣本還是太薄。

- Hugging Face 與 Liva AI 合作，新增埃及英語（1.34 小時）與奈及利亞英語（1.55 小時）兩組不公開的對話測試集。
- 排行榜現在會分開列出美國與非美國口音的成績，也會依 Kachru 三個同心圓模型比較內圈與外圈、擴展圈口音。
- 用不公開資料評測，是為了防止模型只針對公開測試集「刷榜」。
- 新資料是自然對話，逐字稿保留了口吃、贅詞，比朗讀稿難得多，也更接近語音產品實際的使用情境。