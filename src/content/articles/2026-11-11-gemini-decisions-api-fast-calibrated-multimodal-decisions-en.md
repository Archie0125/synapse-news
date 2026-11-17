---
category: ai-ml
faqs:
- answer: The Gemini Decisions API is a Google endpoint for fast, closed-set decisions
    such as tool selection, policy checks and model routing. It runs on the Gemini
    Decision 1 model, which scores candidate options and returns probabilities instead
    of generating text.
  question: What is the Gemini Decisions API?
- answer: Gemini Decision 1 returns results in about 150-250 ms end-to-end and costs
    $0.10 per 1M input tokens, with no output tokens billed. Google says it is nearly
    5x cheaper than Gemini 3.5 Flash-Lite across its benchmark suite.
  question: How fast and how cheap is Gemini Decision 1?
- answer: Calibration means a model's confidence scores match how often it is actually
    correct, so a 90% score should be right about 90% of the time. Well-calibrated
    scores let developers set reliable thresholds for when an agent acts automatically
    and when it hands off to a human.
  question: Why does calibration matter for AI agents?
featured: false
lang: en
publishedAt: '2026-11-11T18:00:00+00:00'
relatedSlugs: []
sources:
- name: Google AI Blog
  url: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
summary: Gemini Decisions API recognizes that most agent steps are multiple-choice
  questions, and charging zero for output tokens makes it a serious threat to LLM-based
  routing.
tags:
- ai-ml
- developer-tools
- products
title: 'Gemini Decisions API: Fast, calibrated multimodal decisions'
trending: false
type: news
---

# Gemini Decisions API: Fast, calibrated multimodal decisions

Today, we’re introducing the Gemini Decisions API, a new endpoint for fast, closed-set decisions powered by our new Gemini Decision 1 model (gemini-decision-1), available through the [Gemini API](https://aistudio.google.com/docs/decisions-api) in [Google AI Studio](https://aistudio.google.com/apps/bundled/gemini-decisions-api-playground?fullscreenApplet=true).

The Decisions API gives you purpose-built primitives for bounded choices like tool selection, policy checks, model routing, and context grading. You can pass one multimodal input across text, images, audio, video, and PDFs (up to 256K tokens) along with up to 1,000 independent questions. Rather than generating answer text token by token, Gemini Decision 1 scores your candidate options in a single forward pass, returning probabilities and confidence scores in 150-250 ms end-to-end latency at $0.10 per 1M input tokens with zero output tokens billed.

## Strong performance and calibration

On benchmarks spanning agent routing, reasoning, ranking, and multimodal understanding, Gemini Decision 1 leads across the suite, with the lowest calibration error.

Gemini Decision 1 scores options without token-by-token decoding, keeping median latency 50-100 ms of model compute (150-250 ms end-to-end), across multimodal inputs and contexts up to 16K tokens, remaining nearly flat from 1 to 100 questions per request. With zero output tokens billed, Gemini Decision 1 with the Decisions API is nearly 5x cheaper across the shared benchmark suite than Gemini 3.5 Flash-Lite with the Interactions API.

## Native multimodal evaluation across three decision types in one pass

Built on Gemini’s native multimodal architecture, Gemini Decision 1 can process text, images, audio, video, and PDFs directly in a single forward pass. You can combine modalities in one shared input, such as pairing a call recording with account metadata or a scanned PDF claim with damage photos, and tune resolution on image and video inputs to control visual detail and token cost.

You can evaluate multiple questions against that shared input in a single request, mixing yes/no checks, multiple choice, and rubric scores. Every answer includes a confidence score (from 0 to 1) so your code can route ambiguous cases to a fallback or human reviewer:

- **noul (Yes/No):** Estimates the probability that a yes/no condition holds, with optional true and false description criteria.
- **choice (Multiple Choice):** Selects from 2 to 255 choices, returning the winner and normalized probabilities for every candidate.
- **score (Ordered Rubric):** Grades inputs across an ordered rubric (starting at 0), returning a continuous weighted score and per-level probabilities.

The `input` field uses the same `Content` block format as the [Interactions API](https://aistudio.google.com/docs/interactions-overview). Here is how to check a photo of a breakroom counter, together with a text note, against all three question types in one request:

```
from google import genai
client = genai.Client(http_options={"api_version": "v1beta"})
result = client.decisions.create(
    model="gemini-decision-1",
    input=[{
            "type": "image",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/spill.jpg",
            "mime_type": "image/jpeg",
        },
        {
            "type": "text",
            "text": "Breakroom counter check before the 9 AM client meeting.",
        },
    ],
    questions={
        "has_spill": {
            "type": "noul",
            "instructions": "Is there an uncleaned liquid spill on the counter?",
        },
        "next_action": {
            "type": "choice",
            "instructions": "Which cleanup action fits the scene?",
            "criteria": {
                "wipe_with_cloth": "Small counter spill with a cloth or towel already nearby.",
                "dispatch_janitorial": "Large floor hazard, broken glass, or active leak.",
                "ready_for_meeting": "Counter is clean and ready.",
            },
        },
        "severity": {
            "type": "score",
            "instructions": "Rate the severity of the counter mess.",
            "criteria": [
                "Clean and ready.",
                "Minor localized spill.",
                "Major spill or safety hazard.",
            ],
        },
    },
)
```
## How teams are building with the Decisions API

Teams across Google are already using the Decisions API as a low-latency control plane, shipping features simply by defining options rather than training custom classifiers or waiting on generative calls:

- **Dynamic model routing in Gemini Notebook:** Gemini Notebook uses the Decisions API as a real-time router to instantly direct incoming queries to the optimal model tier and thinking level for each request. The Decisions API classifies intent in milliseconds to serve everyday queries with up to 40% lower latency while reserving deep reasoning models for complex tasks.
- **Rapid design iteration in Stitch:** The new [rapid canvas experiment in Stitch](https://stitch.withgoogle.com/rapid) uses the Decisions API to generate playable wireframes of a product flow in seconds and to apply edits made by voice or tap almost instantly. When the flow feels right, one click hands the screens off to the full Stitch experience for deeper design polish.
- **Emoji selection in CC:** CC from Google Labs uses the Decisions API to pick the right emoji reaction from a palette of more than 200 options in a fraction of a second, so reactions appear instantly without adding latency.
- **Safety layer for MCP tools in Search**: Google Search uses the Decision API to detect adversarial behavior and content against adversarial evals with high efficacy within the latency envelope.

Stitch Rapid uses the Decisions API to design an entire product flow in seconds (1x speed).

## Start building today

Gemini Decision 1 is priced at $0.10 per 1M input tokens and $0 for output tokens, with an API no-cost tier you can use in [Google AI Studio](https://aistudio.google.com/apps/bundled/gemini-decisions-api-playground?fullscreenApplet=true) for prototyping. Your shared `input` is billed once per request no matter how many questions you evaluate (each question adds only its own instruction and criteria tokens). There are no output-token charges, variable thinking-token bills, or separate audio transcription and OCR costs.

You can start building today by grabbing an API key in [Google AI Studio](https://aistudio.google.com/api-keys), trying our [Doorstep Parcels](https://aistudio.google.com/apps/bundled/doorstep-parcels-qa?fullscreenApplet=true), [Speed Sketch](https://aistudio.google.com/apps/bundled/speed-sketch?fullscreenApplet=true), and [Find the Zoo Keeper](https://aistudio.google.com/apps/bundled/find-the-zoo-keeper?fullscreenApplet=true) demo apps, and following the Python, JavaScript, and REST guides in the [Decisions API documentation](https://aistudio.google.com/docs/decisions-api).

Ecosystem integrations are rolling out across [OpenRouter](https://openrouter.ai/google/gemini-decision-1), [LangChain](https://docs.langchain.com/oss/python/integrations/providers/google), [Vercel](https://ai-sdk.dev/providers/ai-sdk-providers/google), [LiteLLM](https://docs.litellm.ai/docs/providers/gemini), [Pydantic AI](https://pydantic.dev/docs/ai/models/google/), [Pipecat](https://docs.pipecat.ai/api-reference/server/classifiers/google), [LiveKit](https://docs.livekit.io/agents/integrations/google/), and [OpenCode](https://opencode.ai/) alongside the `google-genai` SDKs, with support [coming soon](https://forms.gle/NFt1W6pL1gCY9FGM8) to Gemini in Google Cloud.

## Summary

**TLDR:** Gemini Decisions API recognizes that most agent steps are multiple-choice questions, and charging zero for output tokens makes it a serious threat to LLM-based routing.

- Google launched the Gemini Decisions API, powered by the new Gemini Decision 1 model (gemini-decision-1), for closed-set choices such as tool selection, policy checks, model routing and context grading.
- Instead of generating text, the model scores the candidate options in a single forward pass and returns probabilities and confidence scores, with 150-250 ms end-to-end latency.
- It accepts one multimodal input of up to 256K tokens across text, images, audio, video and PDFs, plus up to 1,000 questions per request.
- Pricing is $0.10 per 1M input tokens with no output tokens billed. Google says that is nearly 5x cheaper than Gemini 3.5 Flash-Lite on its benchmark suite.
- Google claims the model has the lowest calibration error on its benchmarks, meaning its confidence scores better match how often it is right, which matters for automated decisions.

## 摘要

**重點摘要：** Gemini Decisions API 抓到一個重點：AI 代理大多數步驟其實是選擇題。輸出 token 完全不收費，對用 LLM 做路由的現行做法是一大威脅。

- Google 推出 Gemini Decisions API，由新的 Gemini Decision 1 模型（gemini-decision-1）驅動，專門處理工具選擇、政策檢查、模型路由和情境評分等封閉式選擇。
- 模型不生成文字，而是用一次前向運算替候選選項評分，回傳機率和信心分數，端對端延遲 150 到 250 毫秒。
- 單次請求可輸入最多 256K token 的多模態內容，涵蓋文字、圖片、音訊、影片和 PDF，並可同時問最多 1,000 個問題。
- 價格為每百萬輸入 token 0.10 美元，輸出 token 完全不計費。Google 表示在其基準測試中比 Gemini 3.5 Flash-Lite 便宜近 5 倍。
- Google 宣稱該模型在基準測試中的校準誤差最低，也就是信心分數更貼近實際準確率，這對自動化決策很重要。