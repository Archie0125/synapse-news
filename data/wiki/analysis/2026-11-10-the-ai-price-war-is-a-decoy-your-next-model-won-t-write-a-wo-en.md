---
category: ai-ml
lang: en
published: '2026-11-10T18:45:38.604939+00:00'
sources:
- name: The Verge
  url: https://www.theverge.com/ai-artificial-intelligence/1030787/google-gemini-4-carbon-public-rollout
- name: Engadget
  url: https://www.engadget.com/2311855/gemini-4-carbon-now-available-worldwide/
- name: 9to5Google
  url: https://9to5google.com/2026/11/10/gemini-app-4-carbon/
- name: Hacker News
  url: https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/
- name: Hugging Face Blog
  url: https://huggingface.co/blog/decision
summary: Google halved frontier prices and Amazon cut its costs by 98%, but the bigger
  move is that much of production AI no longer needs a frontier model at all.
title: The AI Price War Is a Decoy. Your Next Model Won't Write a Word
trending_theme: Frontier Model Price War Intensifies
type: analysis
---

The most interesting line in Google's Gemini 4 Carbon launch isn't the price. It's Google telling customers to mostly use something else.

Carbon reached general availability on November 10, two weeks after a limited preview for "cybersecurity defenders." Google's own blog post says the older Gemini 4 Argon, which launched only last month, "remains the ideal choice for the majority of software engineering and knowledge work." The flagship is for "tasks that test the limits of a model's intelligence." So a frontier lab has launched its best model and, on the same day, said most of you don't need it.

That is the price war in one sentence. Watching the per-token sticker prices misses it. The real competition is over how few frontier tokens a company can get away with buying.

## The sticker prices

Here are the numbers. Carbon launches at $2 per million input tokens and $10 per million output tokens until November 30. After that it goes to $4 and $20. According to BenchLM's token price index, the introductory rate is about one-fifth the cost of OpenAI's GPT-6 Astra and one-quarter the cost of Anthropic's Fable 5.2, which shipped the day before Carbon. Even at double the price, Carbon undercuts both.

Meta is pitching Muse Ember the same way: cost per task, not leaderboard rank. When the three richest AI spenders all start selling on efficiency, a market has stopped being sold on capability. GPT-4 launched in 2023 at $30/$60 per million tokens, and nobody blinked because nothing else could do the job. That premium is gone. The best models in 2026 trade within a few benchmark points of each other, so price is the only lever left that customers can actually feel.

Even so, a cheap per-token price can mislead. The Verge points out that models use different numbers of tokens for the same task. A model that costs a quarter as much per token but thinks four times as long costs you the same. That's why Google's more pointed claim isn't the $2 price. It's the new Multimodal Knowledge Agents (MKA) benchmark Google built with Artificial Analysis, where Google says Carbon ranks first across 200 agentic tasks while using **3x fewer tokens than the next-best model**. Google is choosing what to be measured on: cost per finished job, not cost per token. Expect every lab to copy that framing within a quarter.

## What nobody is talking about: the frontier model is becoming middle management

Look at how Google built Antigravity's new `/swarm` feature. Carbon gets the roles that "demand the deepest reasoning": architectural design, coordination, auditing. Faster, lighter models do the parallel work in isolated workspaces, and adversarial verifiers check every change.

Put plainly, the frontier model is the manager and the cheap models are the workers. The token volume, which is where the money goes, flows to the workers.

Then Amazon showed how far down that goes.

In a post on the Strands Agents blog, two Amazon engineers, Carr and Mehul, describe replacing Claude Sonnet 4.6 on one of the world's largest internal ticketing systems. The system sorts every ticket (customer escalations, capacity requests, alarms, security findings) into 20 categories. Sonnet had been running a long system prompt on every ticket and writing out JSON with its reasoning. It was the "goldilocks" choice, smart enough and cheap enough.

They replaced it with **Strands Decider**, a "decision model" built on Gemma 4 E4B. It can't generate text. You give it a state (the ticket) and a set of options (the 20 labels), and it returns a probability for each option plus a confidence score. In their tests it beat production Sonnet on accuracy **at 98% lower cost**, which comes to millions of dollars a year.

The deployment is plain on purpose. One SageMaker `ml.g5.xlarge` instance with a single A10G GPU and 24 GB of memory. The model uses about 19 GiB. Each request takes about 640 ms. That's roughly 5,600 tickets per hour per instance without any batching, on a GPU generation that came out in 2021. The pipeline is SQS to Lambda to SageMaker, with an AppConfig switch that ran Sonnet and the Decider side by side before the cutover. No new infrastructure, no research team, and the same setup is available to any AWS customer.

Hugging Face has already added a `pipeline("decision")` task to Transformers. TypeSafe AI introduced its own version as "Jev," which it calls a "System One model," after Kahneman's fast, intuitive mode of thinking. When Hugging Face gives something its own pipeline type, it has stopped being a research curiosity.

There's an irony here. Amazon has put billions into Anthropic, and the workload it moved off was Sonnet, the mid-tier model that is the high-volume, high-margin core of any lab's API business. Frontier labs don't make their money on rare hard problems. They make it on millions of routine calls: classify this, route that, pull out these fields. That is exactly the work decision models do for almost nothing.

## The second-order effects

**1. The mid-tier gets squeezed from both sides.** Carbon's introductory price brings frontier capability close to what mid-tier models cost. Decision models take the bottom of the workload. The "good enough and cheap" tier where Sonnet-class models sit gets pressed from above and below. If I ran product at a frontier lab, that's the tier I'd be worried about, not the flagship.

**2. Routing becomes the product.** A swarm only works if something decides which job goes to which model. Whoever owns that layer (Antigravity for Google, Bedrock and SageMaker for Amazon) controls the money. Model providers become suppliers, and the router becomes the general contractor.

**3. Accuracy improves for a structural reason.** A decision model can't hallucinate a 21st label because it can only choose among the options you give it. You also get a usable confidence score, so you can set a threshold and send low-confidence cases to a human or to a bigger model. That's an engineering guarantee, not a better prompt, and auditors and compliance teams will like it more than they ever liked "the LLM usually returns valid JSON."

## The bear case

There's a fair argument on the other side. Decision models only work when you already know the set of possible answers. Debugging a cross-subsystem failure, designing a migration, writing the report: none of those come with a fixed menu of options. And as agents take on longer tasks, open-ended work grows faster than closed-set work.

Then there's the Jevons problem. A cheaper model leads to more calls, not fewer. A `/swarm` that turns one prompt into a team of agents with adversarial verifiers multiplies token use. Google can halve the price and still raise each customer's bill if it gets them to run ten agents where they used to run one. In that reading, the price war is a land grab dressed up as a discount, and the introductory rate that ends November 30 looks like a teaser rate.

I think both points are true and they don't conflict. Total frontier spending can keep growing while the share of production calls that need a frontier model shrinks. The labs will report revenue growth. What they won't report is how much of that growth now comes from a smaller and more contested slice of the work.

Google's 10,000-scientist program, with six months of free Carbon access, deserves some skepticism too. It's generous, and it also collects high-value research reasoning traces that no price war can buy.

## What to Watch

- **December 1, when Carbon's price doubles.** I expect Google to blunt the jump, either by extending the introductory rate or by adding usage-tier or Antigravity bundle discounts by Q1 2027. Doubling a price in the middle of a price war is how you hand customers to Meta.
- **Frontier labs will ship their own decision endpoints.** Within six months, expect at least one of OpenAI, Anthropic, or Google to offer a "score these options" API that bills per decision rather than per token. Otherwise teams like Amazon's ticketing group keep leaving.
- **Cost per task becomes the headline benchmark.** MKA's "3x fewer tokens" claim is the template. By mid-2027, launch posts that list only accuracy will look dated, and Artificial Analysis-style cost-per-completed-task charts will lead.
- **Sonnet-class prices fall first.** The next big price cut won't be on a flagship. It will be on the workhorse tier, because that's the tier decision models are taking customers from right now.
- **More "we replaced X" posts.** Amazon's post is a playbook with a CDK stack attached. Expect a stream of enterprise write-ups that each say roughly "we swapped a $X-million LLM bill for one GPU."

The model that wins the next two years won't be the smartest one. It will be the one that runs only on the 10% of calls that actually need it, and charges fairly for that.