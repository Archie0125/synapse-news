---
title: "Etched Raises $300M at $10.3B Valuation, Doubles Worth in Seven Months on GPU-Free Inference Bets"
summary: "Etched, the AI inference chip startup building ASICs optimized exclusively for transformer models, has closed a $300 million Series C led by Sequoia Capital at a $10.3 billion valuation — doubling from its $5 billion round in December 2025. With $1 billion in chip orders and SK Hynix joining as a strategic investor, the company is mounting the most credible challenge yet to Nvidia's inference dominance."
category: "hardware"
publishedAt: 2026-07-25
lang: "en"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/07/23/ai-chip-startup-etched-defies-skeptics-hits-10-3b-valuation-from-big-name-investors/"
  - name: "GlobeNewswire"
    url: "https://www.globenewswire.com/news-release/2026/07/23/3332366/0/en/Etched-raises-300M-at-a-10-3B-Valuation-to-Scale-Production-of-Frontier-Scale-Inference-Hardware.html"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/etched-300m-series-c-10-3b-valuation-sequoia-sk-hynix"
  - name: "MLQ News"
    url: "https://mlq.ai/news/etched-raises-300m-series-c-at-10-3b-valuation-to-scale-gpu-free-inference-chips/"
tags:
  - "Etched"
  - "AI chips"
  - "inference"
  - "semiconductors"
  - "Sequoia"
  - "SK Hynix"
  - "startup funding"
relatedSlugs:
  - "2026-07-25-intel-q2-2026-earnings-comeback-en"
  - "2026-07-08-nvidia-sk-hynix-hbm4-vera-rubin-partnership-en"
  - "2026-07-01-etched-5b-valuation-1b-sales-inference-chip-en"
---

Seven months ago, Etched raised $500 million at a $5 billion valuation and most of the semiconductor industry wrote it off as an overfunded curiosity. On July 23, 2026, the AI inference chip startup raised $300 million more at a $10.3 billion valuation — doubling its worth in less than a year — and now carries $1 billion in committed chip orders. Sequoia Capital led the round, with Andreessen Horowitz, Jane Street, Diffusion, and memory giant SK Hynix all joining as new investors.

The round is, by several measures, an inflection point: TechCrunch noted it is the highest valuation ever achieved by a Sequoia-led Series C. More importantly, it validates a thesis that has attracted skepticism since Etched's founding in 2022 — that building a chip optimized entirely for transformer model inference, rather than general-purpose GPU computation, is a viable and profitable business strategy.

## What Etched Actually Builds

The vast majority of the AI chip conversation focuses on training — the massive compute clusters used to build frontier models. Nvidia's H100 and H200 GPUs, the computing substrate underpinning OpenAI, Anthropic, Google DeepMind, and Meta's model development, dominate this segment so completely that they are effectively the global currency of AI capability.

But training a model is only half the equation. Once a model is trained, it must be deployed — serving inference requests to millions of users, embedding into enterprise software, powering autonomous agents. Inference is where AI products are actually experienced by end users, and increasingly where the bulk of AI compute spending is headed.

Etched's bet is that Nvidia's GPUs, designed to be flexible enough for both training and inference across a vast range of applications, are fundamentally overengineered for the inference use case. A GPU that can run matrix multiplications, ray tracing, scientific simulation, and any conceivable neural network architecture carries a price premium and a power budget that pure inference workloads don't need.

Etched's flagship chip, called Sohu, is built to do exactly one thing: run transformer models at inference time. By eliminating the architectural flexibility required for training and non-transformer workloads, Etched claims Sohu can achieve dramatically higher tokens-per-second throughput and substantially lower cost per inference than comparable Nvidia hardware. The company has published benchmarks suggesting Sohu outperforms Nvidia H100 clusters on standard language model serving tasks by a factor of 10 to 20 times on throughput-per-dollar metrics.

## Why the Valuation Doubled

The $1 billion in confirmed chip orders is the clearest explanation for the valuation jump. Seven months ago, Etched was a credible technical concept with a promising manufacturing roadmap. Today it is a company with a backlog.

The identity of those customers matters as much as the number. Inference at scale is dominated by a small number of buyers: the major cloud providers (AWS, Google Cloud, Microsoft Azure) and the model companies themselves (OpenAI, Anthropic, xAI, Meta). Any company writing checks to Etched for a billion dollars in chips is almost certainly drawing from that list, though Etched has not named specific customers publicly.

The presence of SK Hynix as a strategic investor is also significant. SK Hynix is one of the world's two dominant producers of High Bandwidth Memory (HBM) — the specialized memory architecture that modern AI chips require to feed data to their compute cores fast enough to stay saturated. Nvidia's leadership in AI chips is inseparable from its privileged relationships with HBM suppliers. Etched having SK Hynix as both an investor and presumably a preferred memory partner gives it an immediate supply chain advantage that money alone cannot buy.

For Sequoia, leading a Series C at a $10.3 billion valuation for a company that has never shipped chips at commercial scale represents an unusual level of conviction. Sequoia's semiconductor portfolio includes some of the most consequential chip companies of the last two decades, and the firm rarely makes moves of this size without substantial diligence on both the technical thesis and the market dynamics.

"We're entering a world where inference compute is the scarce resource," said a Sequoia partner in the company's announcement. "Etched is building the right chip for that world."

## The Case for Specificity

The broader semiconductor industry has traditionally valued flexibility. General-purpose chips sell into a wide range of applications and reduce customer concentration risk. Specialized chips offer performance advantages but create dependency on a specific technology trajectory.

For Etched, the bet is that the transformer architecture has become so dominant that specializing around it is not risky — it is simply accurate forecasting. Since 2017, when the original "Attention is All You Need" paper introduced transformers, the architecture has come to underpin virtually every frontier AI system, from language models to image generators to video models to robotic control systems.

If transformers are the architecture of AI and will remain so for the next five to ten years — which most researchers currently believe — then a chip optimized exclusively for transformers is not a narrow specialization. It is a chip designed for the central computing workload of the AI era.

Critics of this thesis argue that architectural diversity is returning: mixture-of-experts models, state space models like Mamba, and hybrid architectures are gaining traction alongside standard transformers. If the industry moves away from pure transformers at scale, Etched's single-purpose chip becomes much less valuable. The company counters that its architecture can accommodate these variants, but the debate remains live.

## Competing With Nvidia in the Real World

Building a chip that outperforms Nvidia in benchmarks is achievable. Building a business that wins orders against Nvidia is significantly harder.

Nvidia's advantage in inference extends well beyond chip performance. The company's CUDA software ecosystem, developed over two decades, allows developers to write inference code once and run it across any Nvidia hardware. The switching cost of moving to a non-Nvidia chip is not just the chip price — it is re-engineering the software stack, retraining operations teams, and accepting a new risk profile for systems that may already be running in production.

Etched's response to this challenge is to target the hyperscalers and model companies directly, rather than the broader market of enterprises running inference on managed cloud services. These customers have large software engineering teams capable of adapting code to new hardware, strong incentives to reduce inference costs (which at scale represent billions of dollars annually), and the buying power to make large custom chip commitments economical.

The $1 billion in orders suggests this strategy is working — at least with early adopters. The test of the next 12 to 18 months will be whether those orders translate into successful deployments that create enough satisfied customers to expand the installed base, or whether supply chain challenges, software integration friction, or competitive responses from Nvidia slow the momentum.

## The Broader Inference Chip Race

Etched is not alone in challenging Nvidia's inference dominance. Groq, which builds Language Processing Units (LPUs) for low-latency inference, has raised billions on a similar thesis. Cerebras, whose wafer-scale chips offer extraordinary memory bandwidth, targets the same large model inference market. Tenstorrent, led by former AMD chief architect Jim Keller, is building more general-purpose AI chips that compete across training and inference. Qualcomm's AI inference portfolio is expanding from edge to cloud.

The fact that Sequoia, a16z, and SK Hynix are all willing to back Etched specifically, at this price, in the current market, suggests sophisticated investors believe there is room for more than one winner in the inference chip transition. The annual cost of running frontier AI models at global scale is now in the hundreds of billions of dollars — a market large enough to support multiple successful chip companies even if Nvidia retains majority share.

For three Harvard dropouts who founded a chip company in 2022, landing $10.3 billion in market recognition and $1 billion in orders in under four years is either a proof-of-concept for the thesis that application-specific AI chips are the next wave of semiconductor value creation — or the most expensive bet in Silicon Valley's current cycle. Given the order backlog, the former looks increasingly likely.
