---
title: "OpenAI, Google, and Anthropic Form Unprecedented Alliance to Stop Chinese AI Cloning"
summary: "Three rival AI giants are sharing classified threat intelligence through the Frontier Model Forum to detect and block 'adversarial distillation' attacks, where Chinese competitors use millions of fake accounts to extract training data from US frontier models. The collaboration marks a historic moment of competitive solidarity driven by national security concerns."
category: "ai-ml"
publishedAt: 2026-04-08T09:05:00Z
lang: "en"
featured: true
trending: true
sources:
  - name: "Bloomberg"
    url: "https://www.bloomberg.com/news/articles/2026-04-06/openai-anthropic-google-unite-to-combat-model-copying-in-china"
  - name: "Japan Times"
    url: "https://www.japantimes.co.jp/business/2026/04/07/tech/openai-anthropic-google-china-copy/"
  - name: "StartupNews"
    url: "https://startupnews.fyi/2026/04/07/openai-anthropic-google-come-together-to-combat-model-copying-in-china/"
tags:
  - "openai"
  - "google"
  - "anthropic"
  - "china"
  - "ai-security"
  - "frontier-model-forum"
  - "adversarial-distillation"
relatedSlugs:
  - "2026-04-03-us-china-chip-war-en"
  - "2026-04-04-openai-gpt5-leak-en"
---

In one of the most remarkable competitive collaborations Silicon Valley has ever seen, OpenAI, Google, and Anthropic — three companies that compete ferociously for top AI talent, enterprise contracts, and benchmark supremacy — are now sharing proprietary threat intelligence about a sophisticated Chinese campaign to steal the intellectual essence of their frontier models.

The effort is being coordinated through the Frontier Model Forum, the industry body that also includes Microsoft. According to sources familiar with the arrangement, the three companies are pooling data about what researchers call "adversarial distillation" attacks: a technique where adversaries create massive numbers of fake user accounts, systematically feed carefully crafted prompts into frontier models, collect the outputs at industrial scale, and use those outputs as training data to build competing models at a fraction of the cost of original training.

## The Scale of the Problem

The catalyst for this unprecedented cooperation was Anthropic's disclosure in February 2026 that three Chinese AI companies had used more than **24,000 fake accounts** to generate over **16 million exchanges** with Claude. The operation was methodical and sophisticated — the accounts mimicked legitimate developer behavior, spread queries across categories to avoid detection, and aggregated outputs in structured formats optimized for fine-tuning.

OpenAI has separately told members of the US Congress that DeepSeek, the Chinese AI lab that shocked Silicon Valley with its R1 model in early 2025, had been attempting to "free-ride" on American AI capabilities through similar methods. Google identified analogous patterns targeting Gemini endpoints. When the three companies compared notes, the scope of the coordinated campaign became impossible to ignore.

"This isn't one actor doing one thing — it's a systematic, industrial-scale effort to use our own outputs against us," said one person familiar with the Frontier Model Forum discussions, speaking on condition of anonymity. "The only rational response is to share information that we would never share under normal competitive circumstances."

## Why Rivals Are Cooperating

The decision to collaborate is being framed internally at all three companies as a matter of national security rather than competitive strategy. The argument goes like this: if Chinese labs can train models nearly as capable as GPT-5, Gemini 3.1 Pro, or Claude Mythos by distilling their outputs, the massive capital and computational advantage that US AI labs currently hold evaporates — without a single GPU being exported or a single engineer being hired.

The economic logic of distillation is brutal. Training a frontier model from scratch requires hundreds of millions to billions of dollars in compute. But if you can use a frontier model to generate hundreds of millions of high-quality synthetic training examples, you can fine-tune a smaller base model to approximate frontier performance at a fraction of the cost. The technique has been openly discussed in academic literature for years — what's new is the scale and the brazenness.

The Frontier Model Forum collaboration involves sharing detection signatures: patterns of API usage, prompt structures, and account behavior that indicate distillation attacks rather than legitimate use. Each company's security team contributes to a shared database that all three can query. Crucially, the companies are not sharing model weights, architectures, or commercial intelligence — only threat data.

## Technical Countermeasures

Beyond intelligence-sharing, the alliance is prompting each lab to independently accelerate its defensive capabilities. Anthropic has reportedly deployed new behavioral clustering models that can detect when a set of accounts is querying in coordinated patterns, even when individual queries appear innocuous. OpenAI has implemented what insiders describe as "output watermarking" — subtle statistical signatures embedded in model outputs that survive the distillation process and can be detected in derivative models.

Google is taking a different approach: rather than watermarking outputs, Gemini's API now uses adaptive rate-limiting and prompt-complexity analysis to identify when a querying pattern resembles synthetic data generation. The system doesn't block the traffic — that would be detectable — but subtly degrades the quality of outputs in ways that make them less useful for fine-tuning.

None of these measures are foolproof. Sophisticated adversaries can route queries through multiple jurisdictions, use residential proxies, vary their prompt styles, and post-process outputs to remove watermarks. But the combination of intelligence-sharing and technical countermeasures significantly raises the cost and complexity of running adversarial distillation campaigns at scale.

## The Broader Geopolitical Context

The alliance reflects a broader hardening of positions in the US AI industry toward Chinese competition. For much of 2023 and 2024, major US AI labs maintained that open scientific exchange with Chinese researchers was net-positive for global AI development. That consensus has shifted dramatically.

The shift accelerated after DeepSeek's January 2025 release demonstrated that Chinese labs could produce models competitive with US frontier systems on a fraction of the compute budget. Whether DeepSeek was genuinely more efficient or benefited from distillation of US model outputs remains contested — but the question itself is now driving policy.

The Frontier Model Forum's move puts pressure on smaller AI labs and open-source model providers, which lack the resources to run sophisticated adversarial detection programs. If distillation attacks succeed against Llama, Mistral, or Falcon models, the benefits could indirectly flow to efforts targeting closed frontier models.

## What It Means for the Industry

For enterprise customers, the alliance is mostly invisible — their API access and pricing are unaffected. But the collaboration signals that the "AI race" framing of US-China tech competition is shifting from a story about who can build the most capable model to a story about who can protect their model's value once built.

For policymakers, the alliance creates pressure to establish formal legal frameworks governing model distillation. Currently, it is unclear whether systematic output extraction for commercial fine-tuning violates terms of service in ways that are legally enforceable across jurisdictions. Several members of the Frontier Model Forum have begun lobbying both the Commerce Department and the Office of the US Trade Representative to create explicit trade protections for AI model outputs — treating them more like trade secrets than like publicly accessible information.

The irony is sharp: three companies that have spent years arguing they are in fierce, zero-sum competition for AI supremacy are now cooperating on what amounts to an industrial self-defense pact. In doing so, they are also implicitly acknowledging that the outputs of their frontier models — not just the models themselves — have become geopolitically significant assets worth defending collectively.

Whether the alliance holds as competitive pressures intensify remains to be seen. But for now, at least, the threat from adversarial distillation has accomplished something that years of government urging could not: getting OpenAI, Google, and Anthropic to share.
