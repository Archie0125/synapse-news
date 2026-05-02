---
title: "Under Oath, Musk Admits xAI 'Partly' Distilled OpenAI's Models to Build Grok"
summary: "In a striking moment from the Musk v. Altman trial, Elon Musk testified under oath that xAI used distillation techniques on OpenAI's models to help train Grok — an admission that may violate OpenAI's terms of service and opens a broader reckoning about how widely the practice is used across the AI industry."
category: "ai-ml"
publishedAt: 2026-05-02
lang: "en"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/"
  - name: "MIT Technology Review"
    url: "https://www.technologyreview.com/2026/05/01/1136800/musk-v-altman-week-1-musk-says-he-was-duped-warns-ai-could-kill-us-all-and-admits-that-xai-distills-openais-models/"
  - name: "Benzinga"
    url: "https://www.benzinga.com/markets/prediction-markets/26/04/52189236/elon-musk-admits-xai-partly-distilled-openai-models-what-do-prediction-markets-say-about-the-lawsuit"
  - name: "DQ India"
    url: "https://www.dqindia.com/news/elon-musk-says-xai-partly-used-openai-models-in-ai-training-11785204"
tags:
  - "Elon Musk"
  - "xAI"
  - "OpenAI"
  - "Grok"
  - "distillation"
  - "trial"
  - "AI training"
  - "intellectual property"
relatedSlugs:
  - "2026-05-01-musk-altman-openai-trial-week-1-recap-en"
  - "2026-04-29-musk-altman-openai-trial-opens-en"
---

Elon Musk went to federal court in Oakland to accuse OpenAI of betraying the public trust. What he ended up doing — in one of the most stunning moments of the trial so far — is accidentally illustrating how the entire AI industry may be doing something very similar to what he's suing OpenAI for: quietly leveraging others' work while publicly claiming the moral high ground.

On Thursday, April 30, during cross-examination, Musk was asked whether xAI had used distillation techniques on OpenAI's models to help train Grok. His response: "Generally, AI companies distill other AI companies." Pressed for a direct yes or no, he landed on a single syllable that ricocheted across the industry: "Partly."

## What Distillation Actually Means

To understand why Musk's admission matters, it helps to understand what model distillation is — and why it's become a flashpoint in AI competition.

In machine learning, distillation is a technique where a smaller, more efficient model is trained to mimic the behavior of a larger, more capable one. In the most common form, a company queries a rival's model via its API or public interface, collects the responses at scale, and uses those responses as training data for their own model. The result is a "student" model that has absorbed patterns, reasoning styles, and capabilities from the "teacher" model — often without the teacher's knowledge or consent.

The appeal is obvious: training a truly frontier model costs hundreds of millions or billions of dollars in compute. Distillation offers a shortcut. By systematically querying a competitor's billion-dollar model and harvesting its outputs, a company can bake the equivalent of years of expensive training into its own system at a fraction of the cost.

The legal status, however, is murky. Distillation is not explicitly illegal under U.S. law. But it may violate the terms of service that AI companies impose on their APIs — and OpenAI's terms of service explicitly prohibit using its models' outputs to train competing systems. Whether that constitutes copyright infringement, trade secret misappropriation, or is simply an unenforced contractual clause is a question lawyers are actively debating.

## The Irony That Wrote Itself

The courtroom irony was almost too clean. Musk has spent weeks in that Oakland federal courthouse arguing that OpenAI betrayed a foundational agreement — that the company he co-founded promised to develop AI for the benefit of humanity, not to enrich its employees and investors. He's demanding $134 billion in damages, the removal of Sam Altman and Greg Brockman from OpenAI, and the unwinding of its conversion to a for-profit structure.

And yet, there he was, testifying that xAI — his AI company, built while he was publicly attacking OpenAI — had itself used OpenAI's models as training data. The technique he partially admitted to is precisely the kind of thing that OpenAI's lawyers have characterized as unfair appropriation of their intellectual property and competitive advantage.

Musk's defense was to normalize the practice: "Generally, AI companies distill other AI companies." That may be true. But it's also the same logic that the companies he's suing have sometimes used to justify their own allegedly borderline behaviors — that everyone does it, that it's an industry norm, that the ethics were never as clear as the aggrieved party later claims.

OpenAI's legal team, unsurprisingly, was quick to highlight the admission. It fits neatly into their counter-narrative of the trial: that Musk is not a principled whistleblower but a competitor who built his own AI empire by exploiting the same infrastructure and knowledge he now claims belongs to the public.

## An Industry-Wide Reckoning

Musk's "partly" lands in the middle of a much larger conversation the AI industry has been quietly avoiding: the extent to which today's top models are built, at least in part, by learning from each other.

The practice of distillation — often referred to in more benign terms as "synthetic data generation" or "knowledge transfer" — is, by most expert accounts, widespread. When DeepSeek released its R1 model in early 2025 and dramatically undercut competitors on both price and capability, one of the first questions the research community asked was how it achieved those results at such low cost. One prominent theory, backed by behavioral and structural analysis of the model, was that DeepSeek had distilled from frontier models including GPT-4o and Claude. OpenAI at the time noted it was investigating "evidence" of distillation.

More broadly, the entire ecosystem of smaller, open-weight models that have proliferated over the past two years — many of them excellent — rests to some degree on the existence of frontier models. The knowledge doesn't transfer magically; it's extracted, sometimes by legitimate means (researchers training on publicly shared outputs), sometimes by methods that sit in legal gray zones.

What makes Musk's admission different is that it happened under oath, in federal court, in a case that could set legal precedents about AI development practices. As one IP attorney quoted in analysis of the case put it: "When you distill a model using another company's proprietary system, you're arguably encoding that company's intellectual property into your own product — not just copying text or images, but capturing the learned patterns, reasoning structures, and knowledge representations that the original company spent billions of dollars to build."

## Industry Counter-Moves

The admission has prompted discussion of defensive strategies already underway. OpenAI, Anthropic, and Google have reportedly been coordinating through the Frontier Model Forum to identify and combat distillation attempts — typically characterized by systematic, large-scale querying patterns that look different from typical organic API usage. Frontier labs have been developing rate-limiting and behavioral detection systems designed to identify when an API user is running queries that look more like training-data harvesting than product development.

It's an arms race with no clean resolution. Distillation detection is an imperfect science; legitimate customers sometimes query models at high volumes for production applications. The legal framework for pursuing distillation claims is nascent and untested. And the practice, by Musk's own account, is widespread enough that any aggressive legal campaign against it would implicate much of the industry.

## What Comes Next

For the Musk v. Altman trial itself, the distillation admission is a gift to OpenAI's legal team — not necessarily because it creates new legal liability for Musk, but because it undermines the moral architecture of his case. Musk has positioned himself as a principled actor protecting the public from OpenAI's corporate capture. His testimony that xAI quietly used OpenAI's models while he was publicly attacking the company as a betrayal of public trust is difficult to square with that framing.

The trial continues through late May, with Sam Altman, Greg Brockman, and Satya Nadella of Microsoft all scheduled to testify. Whatever the jury ultimately decides about Musk's $134 billion damages claim, the cross-examination moment when a man suing OpenAI admitted his company used OpenAI's models to help build its competitor product has already made its mark on the record.

The broader question — who owns the latent knowledge baked into a large language model, and whether extracting it through systematic querying constitutes misappropriation — may ultimately be decided not in this courtroom, but in future litigation that the Musk v. Altman proceedings have unwittingly helped set in motion.
