---
category: ai-ml
faqs:
- answer: Hugging Face replaced its custom router with OpenRouter's. Language model
    requests now go through OpenRouter, which picks a provider for each call based
    on live price, speed and reliability, and retries elsewhere if one fails.
  question: What changed in Hugging Face Inference Providers?
- answer: No. Hugging Face says existing code stays the same. The router supports
    OpenAI's Chat Completions and Responses APIs and Anthropic's Messages API for
    every chat model.
  question: Do developers need to change their code?
- answer: It lets developers call any served open-weight model on the Hub with one
    token and standard APIs. That removes much of the friction of choosing and managing
    inference providers.
  question: Why does this matter for open-weight model adoption?
featured: false
lang: en
publishedAt: '2026-11-16T00:00:00+00:00'
relatedSlugs: []
safeForPublic: true
sources:
- name: Hugging Face Blog
  url: https://huggingface.co/blog/openrouter
summary: Hugging Face dropping its own router for OpenRouter is a smart admission
  that model hosting and inference routing are different businesses, and open-weight
  users win.
tags:
- open-source
- ai-ml
- developer-tools
title: Hugging Face and OpenRouter join forces to make open-weight models easy to
  run
trending: false
type: news
---

Hugging Face dropping its own router for OpenRouter is a smart admission that model hosting and inference routing are different businesses, and open-weight users win.

## Key points

- Hugging Face Inference Providers now runs on OpenRouter's router instead of Hugging Face's own custom router.
- OpenRouter picks among 80+ providers per request based on live price, speed and reliability, and retries on failure.
- The router supports the OpenAI Chat Completions, OpenAI Responses and Anthropic Messages APIs, with setup guides for Claude Code, Codex, OpenCode and other agents.
- A single Hugging Face token also covers Storage Buckets, Jobs compute and Inference Endpoints.
- Implication: calling an open-weight model now takes about as much effort as calling a closed API, which removes a big adoption hurdle.

## Why it matters

Open-weight models never lost on quality. They lost on hassle. With a single Hugging Face token picking the cheapest healthy provider for each call, the 'just use the closed API' excuse is getting thin.

## Sources

- [Hugging Face Blog](https://huggingface.co/blog/openrouter)