---
category: ai-ml
faqs:
- answer: Hugging Face 以 OpenRouter 的路由取代自家路由。語言模型請求現在經由 OpenRouter 處理，依即時價格、速度與穩定度為每次呼叫挑選供應商，失敗時自動改用其他家。
  question: Hugging Face Inference Providers 有什麼改變？
- answer: 不需要。Hugging Face 表示既有程式碼維持不變，路由支援所有聊天模型的 OpenAI Chat Completions、Responses
    API 與 Anthropic Messages API。
  question: 開發者需要修改程式碼嗎？
- answer: 開發者只要一組 token 和標準 API，就能呼叫 Hub 上任何有供應商提供服務的開放權重模型，大幅降低挑選與管理推論供應商的負擔。
  question: 這對開放權重模型的普及有什麼意義？
featured: false
lang: zh
publishedAt: '2026-11-16T00:00:00+00:00'
relatedSlugs: []
safeForPublic: true
sources:
- name: Hugging Face Blog
  url: https://huggingface.co/blog/openrouter
summary: Hugging Face 捨棄自家路由服務、改用 OpenRouter，明智地承認了模型託管與推論路由本就是兩門不同的生意，最大受益者則是開放權重模型的使用者。
tags:
- open-source
- ai-ml
- developer-tools
title: Hugging Face 攜手 OpenRouter，讓開放權重模型輕鬆上手
trending: false
type: news
---

Hugging Face 捨棄自家路由服務、改用 OpenRouter，明智地承認了模型託管與推論路由本就是兩門不同的生意，最大受益者則是開放權重模型的使用者。

## 重點

- Hugging Face 的 Inference Providers 已從自家路由切換到 OpenRouter 的路由系統。
- OpenRouter 會依即時價格、速度與穩定度，從 80 多家供應商中為每次請求挑選最佳者，失敗時自動改用其他家。
- 支援 OpenAI Chat Completions、OpenAI Responses 與 Anthropic Messages API，並提供 Claude Code、Codex、OpenCode 等程式碼代理的設定指南。
- 同一組 Hugging Face token 也能使用 Storage Buckets、Jobs 運算與 Inference Endpoints。
- 意義：呼叫開放權重模型的門檻已接近封閉 API，開源模型採用的最大阻力之一被拆除。

## 為什麼值得注意

開放權重模型從來不是輸在品質，而是輸在麻煩。現在一組 token 就能自動挑最便宜又穩定的供應商，「直接用封閉 API 比較省事」這個藉口快站不住了。

## 資料來源

- [Hugging Face Blog](https://huggingface.co/blog/openrouter)