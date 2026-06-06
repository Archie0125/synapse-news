---
title: "OpenAI's GPT-5.5 and Codex Land on Amazon Bedrock, Unlocking Enterprise AI at Scale"
summary: "OpenAI's most advanced models — GPT-5.5, GPT-5.4, and Codex — are now generally available on Amazon Bedrock, bringing frontier AI into enterprise AWS environments with native IAM, PrivateLink, and compliance controls. The move removes the last major barrier blocking regulated industries from adopting OpenAI in production."
category: "products"
publishedAt: 2026-06-06
lang: "en"
featured: false
trending: true
sources:
  - name: "OpenAI – Frontier Models on AWS"
    url: "https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/"
  - name: "AWS Blog – OpenAI on Amazon Bedrock"
    url: "https://aws.amazon.com/blogs/aws/get-started-with-openai-gpt-5-5-gpt-5-4-models-and-codex-on-amazon-bedrock/"
  - name: "About Amazon – Bedrock OpenAI Models"
    url: "https://www.aboutamazon.com/news/aws/bedrock-openai-models"
tags:
  - "OpenAI"
  - "GPT-5.5"
  - "Amazon Bedrock"
  - "AWS"
  - "enterprise AI"
  - "cloud"
  - "Codex"
relatedSlugs:
  - "2026-06-04-openai-codex-sites-role-plugins-enterprise-en"
  - "2026-06-05-openai-gpt-realtime-2-voice-api-ga-en"
---

For two years, the question haunting enterprise AI adoption wasn't capability — it was compliance. Procurement teams, legal departments, and CISOs could point at GPT-5.5's benchmark numbers and still veto deployment because the model lived outside their governance perimeter. On June 2, 2026, that barrier effectively fell.

OpenAI and Amazon Web Services announced that **GPT-5.5, GPT-5.4, and Codex** are now generally available on **Amazon Bedrock**, extending OpenAI's frontier AI directly into the cloud environment where the majority of large enterprises already run their infrastructure.

## What's Available and How It Works

The GA launch covers three distinct products delivered through Amazon Bedrock's unified model marketplace:

**GPT-5.5** is OpenAI's most capable production model, designed for advanced reasoning, multi-step agentic tasks, long-context document workflows, and autonomous software operation. It excels at writing and debugging code, data analysis, and complex research synthesis — tasks that require sustained multi-turn reasoning rather than single-shot responses.

**GPT-5.4** sits one rung below, offering a price-performance trade-off suited for high-volume inference workloads where GPT-5.5's full reasoning depth isn't always required.

**Codex** is OpenAI's dedicated coding agent, now available through Bedrock with integration into the Codex CLI and major IDE extensions. On Bedrock, all Codex inference routes through Amazon's infrastructure, inheriting the same security controls as the language models.

Pricing matches OpenAI's first-party rates with no additional platform fee — and critically, usage counts toward existing **AWS commitment drawdowns**. For enterprises that have negotiated multi-year AWS Enterprise Discount Programmes, this means accessing frontier AI against budget already committed rather than opening a new procurement line.

## The Compliance Problem, Solved

The practical significance of this launch is less about the models themselves — sophisticated enterprises had workarounds — and more about removing the governance friction that blocked production deployment in regulated industries.

OpenAI models on Bedrock now inherit the full AWS enterprise control set:

- **IAM-based access management**: the same role and policy framework teams already use to govern S3 buckets and EC2 instances now controls who can call GPT-5.5
- **AWS PrivateLink**: model calls route through private VPC endpoints, never traversing the public internet
- **Amazon KMS encryption**: data at rest and in transit uses customer-managed keys
- **AWS CloudTrail audit logging**: every model invocation is logged, timestamped, and queryable — satisfying auditors in healthcare (HIPAA), finance (SOC 2, FedRAMP), and government (ITAR, CMMC) contexts
- **Amazon Bedrock Guardrails**: content filtering, topic blocking, and PII redaction apply to OpenAI model outputs using the same configuration interface as any other Bedrock model

For a healthcare provider building a clinical documentation assistant, or a bank deploying an internal research agent, the ability to point their existing compliance team at a familiar AWS architecture diagram is a qualitative change from "we're evaluating" to "we're deploying."

## Codex for Enterprise Software Development

The inclusion of Codex in the Bedrock GA announcement addresses a distinct use case: software engineering at enterprise scale.

Codex on Bedrock is not the lightweight code-completion tool familiar from early ChatGPT integrations. It is OpenAI's fully agentic coding system — capable of reading a codebase, understanding a ticket, writing the implementation, running tests, and iterating based on failure output, all autonomously. Within a Bedrock environment, development teams can invoke Codex agents through the Bedrock Responses API with the same authentication tokens used for everything else in their AWS estate.

AWS also revealed a forthcoming integration: **Managed Agents on Bedrock** (currently in limited preview) will allow enterprises to orchestrate Codex agents alongside other Bedrock models in multi-step workflows. A CI/CD pipeline could, for example, call a Bedrock-hosted Codex agent automatically when a pull request fails tests, have it diagnose and propose a fix, and route the suggestion to a human reviewer — all within the AWS security boundary.

## Strategic Calculus: OpenAI, AWS, and Microsoft

The partnership carries obvious strategic tension. Microsoft owns a major stake in OpenAI and Azure is the primary cloud for OpenAI's consumer and enterprise products. Making GPT-5.5 available on a direct competitor's cloud — and counting usage against AWS commitments — is a significant departure.

The logic, however, is straightforward: the enterprise AI market is too large to leave to any single cloud distribution channel. The millions of AWS-first organizations that have built their data infrastructure on S3, their security posture on IAM, and their networking on VPC have a high switching cost to any other cloud. If OpenAI wants to serve those organizations in production — not just in proofs of concept — it needs to meet them where they are.

For AWS, the win is equally clear. Amazon's own Titan models and the broader Bedrock model marketplace benefit from Bedrock becoming the default enterprise inference layer, regardless of which model a customer ultimately selects. Every GPT-5.5 call through Bedrock is a call that deepens AWS infrastructure lock-in.

## What Comes Next: Daybreak on Bedrock

OpenAI previewed a future addition to the Bedrock lineup: **Daybreak**, described as OpenAI's vision for "changing how software is built and defended." Daybreak bundles cyber-focused models and **Codex Security**, a variant tuned for vulnerability detection, penetration testing assistance, and secure code review.

Daybreak's placement on AWS infrastructure is symbolically significant. Security-conscious enterprises — the very organizations most likely to be blocked by compliance concerns from using AI tools — are also the organizations with the most mature AWS governance environments. Routing a security-focused AI tool through the same infrastructure as existing security tooling lowers the integration burden considerably.

A GA date for Daybreak on Bedrock has not been announced, but its inclusion in the GA announcement positions it as the next milestone in the OpenAI-AWS partnership roadmap.

## The Broader Enterprise AI Shift

The GPT-5.5 Bedrock launch is a leading indicator of a broader pattern in enterprise AI: **model providers are decoupling from single cloud distributors**. Anthropic's Claude is available on both AWS Bedrock and Google Vertex AI. Meta's Llama models are available across all major clouds. OpenAI resisting that multicloud pattern was, by the end of 2025, increasingly untenable as enterprise customers demanded deployment flexibility.

For the enterprise IT teams navigating this landscape, the immediate practical takeaway is that the procurement and legal friction that previously required months of negotiation to run a GPT model on AWS infrastructure has been compressed to a checkbox in the Bedrock model access configuration panel.

For the roughly 300,000 organizations that are AWS-primary customers, OpenAI just became significantly easier to deploy. That is the real headline behind today's launch.
