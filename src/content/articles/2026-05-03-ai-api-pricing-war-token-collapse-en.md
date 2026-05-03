---
title: "The AI Pricing War Is Real: How Token Costs Collapsed 99% in Three Years — and What Comes Next"
summary: "The price of AI intelligence has fallen by more than 99% since GPT-4 launched in 2023, with frontier models now available for under $3 per million tokens and budget-tier APIs hitting $0.10 or below. DeepSeek's aggressive pricing forced the hand of every major provider, and the latest round — GPT-5.5 at $2.25/M, Gemini Flash-Lite at $0.25/M, GLM-4.7 at $0.11/M — confirms the collapse is structural, not cyclical. The paradox: enterprise AI bills are still rising."
category: "ai-ml"
publishedAt: 2026-05-03
lang: "en"
featured: false
trending: true
sources:
  - name: "TokenMix Blog"
    url: "https://tokenmix.ai/blog/ai-api-pricing-war-2026"
  - name: "Epoch AI"
    url: "https://epoch.ai/data-insights/llm-inference-price-trends"
  - name: "Fortune — GPT-5.5"
    url: "https://fortune.com/2026/04/23/openai-releases-gpt-5-5/"
  - name: "AI Magicx"
    url: "https://www.aimagicx.com/blog/ai-pricing-war-llm-cost-collapse-business-strategy-2026"
tags:
  - "AI pricing"
  - "LLM"
  - "OpenAI"
  - "Google"
  - "DeepSeek"
  - "inference"
  - "API"
relatedSlugs:
  - "2026-04-25-deepseek-v4-flagship-model-release-en"
  - "2026-04-24-openai-gpt-5-5-agentic-model-en"
---

Three years ago, using GPT-4 via API cost $30 per million input tokens. Today, OpenAI's GPT-5.5—a substantially more capable model—costs $2.25 per million input tokens. Google's Gemini Flash-Lite costs $0.25. China's GLM-4.7 from Zhipu AI costs $0.11. And the price floor keeps falling.

The AI API pricing war of 2025-2026 has delivered one of the most dramatic deflationary episodes in the history of enterprise software. The question is no longer whether AI has gotten cheap—it demonstrably has—but whether cheap AI has actually changed how enterprises buy and deploy it, and whether the economics make sense for the providers racing to the bottom.

The short answer: it's complicated.

## The Numbers Behind the Collapse

The collapse is most visible when mapped across specific model generations. GPT-4 launched in March 2023 at $30 per million input tokens and $60 per million output tokens—prices that made large-scale enterprise deployment prohibitively expensive for most applications. By mid-2024, GPT-4o had cut that to $5 per million input tokens. GPT-5 in early 2026 arrived at $3. GPT-5.5, released April 23, 2026, sits at $2.25.

The trajectory on the budget side is even more striking. Google's Gemini 1.5 Flash, released in mid-2024, broke the $1 barrier. Gemini Flash-Lite, available now, is priced at $0.25 per million input tokens—a price point that was inconceivable for a frontier-quality model as recently as 18 months ago. At the extreme budget end, models like GLM-4.7 and several open-source deployments through cloud inference providers are available at $0.10 to $0.15 per million tokens.

Epoch AI's inference price tracking data shows the cost of AI inference falling at a rate of approximately 10x per year for equivalent capability levels since early 2023. That pace slightly exceeds the historical rate of Moore's Law—not because hardware alone has gotten cheaper, but because architectural innovations have compounded the hardware gains.

## Four Forces Driving the Collapse

The pricing collapse is the product of four converging forces, each significant on its own, mutually reinforcing in combination.

**Mixture-of-Experts architectures** are the most important. Models like GPT-5.5, Gemini 3.1, and DeepSeek V4 are all MoE systems: instead of running all model parameters for every token, they route computation through specialized sub-networks that handle only the relevant portion of a query. In practice, MoE models can deliver performance comparable to dense models twice their size at roughly 60-80% lower compute cost per token. Every major lab has shifted to MoE for its production models in 2025-2026.

**Next-generation inference hardware** has compounded the architectural gains. NVIDIA's H200 and Blackwell B200 accelerators, Google's Ironwood TPUs, and custom silicon from Amazon (Trainium3) and Meta (MTIA 3) all offer meaningfully higher inference throughput per dollar than the hardware generation they replaced. The Ironwood TPU, announced at Google Cloud Next in April, delivers 42.5 exaflops of compute per pod—roughly 10x the throughput of the prior TPU generation—and is already handling a significant portion of Gemini inference.

**Volume economics** are doing the rest of the arithmetic. When API call volumes grew 5-10x year-over-year in 2024 and again in 2025, providers could spread fixed data center costs across dramatically more inference requests. The marginal cost of serving the ten-millionth API call in a day is a tiny fraction of the first thousand.

**DeepSeek's deliberate pressure** is the wildcard that turned gradual decline into rapid collapse. When DeepSeek released its V3 model in December 2024—priced at a fraction of comparable OpenAI and Google offerings despite strong benchmark performance—it set off a repricing cascade. Within 90 days, every major Western provider had cut prices for their midrange models. DeepSeek V4, released in April 2026, renewed the pressure cycle.

## The Paradox: Falling Prices, Rising Bills

The single most counterintuitive fact about the AI pricing war is that enterprise AI spending is rising, not falling, despite collapsing unit costs.

The explanation is agentic AI. A standard chatbot interaction consumes perhaps 1,000 to 5,000 tokens. An agentic workflow—where an AI model plans a multi-step task, calls external tools, reads retrieved documents, maintains a long-running context, and writes back to a database—can consume 50,000 to 500,000 tokens for a single task completion. The 10x price drop in per-token costs has been more than offset by a 50-200x increase in tokens consumed per business outcome.

Finance teams at mid-sized technology companies report that their monthly API bills increased between 3x and 8x over the past twelve months despite the pricing environment, because their engineering teams deployed agentic workflows during the same period. The token cost of running a continuous background agent that monitors enterprise software systems, summarizes alerts, and drafts incident tickets is roughly equivalent—at today's API prices—to having a full-time junior analyst read every alert manually.

This is not a problem unique to any particular company. It is the structural dynamic of the agentic transition: cheaper tokens enable more ambitious applications, which consume more tokens, which generates more revenue for AI providers even as the per-token price falls.

## Provider Economics: Who Can Sustain the Race?

The pricing war raises an uncomfortable question for AI investors: can any provider actually make money at these price points?

For Google and Microsoft, the answer is relatively straightforward. Both companies operate at cloud-scale infrastructure with decades of hardware procurement leverage and custom silicon programs. Google's Ironwood TPU gives it a structural cost advantage over any provider running commodity NVIDIA hardware. Microsoft's Azure partnership with OpenAI gives it access to OpenAI's models while benefiting from Azure's infrastructure margins. Neither company's AI API business is a standalone profit center—it is a strategic investment in cloud platform dominance, and the economics are evaluated accordingly.

For OpenAI, the arithmetic is more complex. The company has disclosed annualized revenue approaching $25 billion, but its compute costs remain the largest line item on its expense ledger. CEO Sam Altman has repeatedly stated that inference costs are falling faster than the company expected, which is why GPT-5.5's pricing is structurally lower than comparable GPT-4 pricing despite being a substantially larger model. OpenAI's bet is that volume growth—measured in tokens, users, and enterprise contracts—will drive margin improvement even as per-token revenue falls.

For smaller inference providers—Groq, Cerebras, Together AI, and the many cloud platforms reselling model capacity—the economics are harder still. These companies depend on infrastructure margins in a market where the model providers themselves are cutting prices aggressively.

## Where the Floor Is

Analysts generally agree that the current pricing trajectory has a floor, though there is disagreement about where it is.

The physical constraints are relatively clear: power, cooling, and silicon are not free, and the marginal cost of inference on any hardware combination has a non-zero floor. At current hardware costs, most analysts place the physical cost floor for frontier model inference at $0.10 to $0.50 per million tokens depending on model size, utilization rate, and hardware generation.

The strategic floor is different. As long as hyperscalers view AI APIs as a loss-leader for cloud platform dominance—a reasonable assumption for at least the next 24 months—prices may remain below cost for certain model tiers. Google's Gemini Flash-Lite at $0.25 per million tokens is plausibly at or below Google's direct infrastructure cost for that service; it exists to onboard developers who will eventually use Gemini Ultra and pay for Google Cloud credits.

The most likely near-term equilibrium, per Goldman Sachs' analysis from March: flagship models at $1-3 per million input tokens by end of 2026; mid-range models at $0.15-0.50; budget tiers at $0.05-0.15. Open-source models deployed on consumer hardware will push the true bottom toward zero for developers willing to run their own infrastructure.

## What It Means for Builders

For developers and product teams, the pricing collapse has already changed the design space for what's worth building. Applications that were economically irrational at $30 per million tokens—real-time document analysis, always-on customer service agents, continuous code review bots—are routine at $0.25. The design question has shifted from "can we afford to run this?" to "what's the user experience we want to create?"

That shift is visible in the product landscape. The App Store and Google Play both saw AI-native application submissions more than double in Q1 2026 compared to Q1 2025, according to app store analytics providers. The marginal cost of intelligence is approaching the marginal cost of storage: still non-zero, but low enough that it no longer determines what gets built.

The more significant change may be in enterprise architecture. When token costs were high, engineering teams optimized aggressively—caching responses, routing simple queries to cheaper models, minimizing context length. As costs fall, those optimizations become less economically necessary, and the temptation is to let agentic workflows sprawl without metering. The enterprises that will perform best in the AI infrastructure environment of 2026 and 2027 are those that develop internal token governance practices—not because individual tokens are expensive, but because agentic workflows can accumulate token consumption faster than any IT budget can track.

The AI pricing war has made intelligence cheap. Making cheap intelligence productive remains the harder problem.
