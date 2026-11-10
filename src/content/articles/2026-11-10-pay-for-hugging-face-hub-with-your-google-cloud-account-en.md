---
category: industry
faqs:
- answer: Hugging Face organizations can now link to a Google Cloud account through
    Google Cloud Marketplace. Hugging Face usage then appears on the Google Cloud
    bill instead of being charged to a credit card.
  question: What did Hugging Face announce?
- answer: Team and Enterprise subscriptions, pay-as-you-go compute such as Jobs, Inference
    Endpoints, Inference Providers, GPU Spaces and ZeroGPU quota extensions, plus
    additional storage, all at public Hugging Face pricing.
  question: Which Hugging Face services are covered?
- answer: Companies already on Google Cloud can use their existing billing account
    and procurement process, so they do not need to onboard a new vendor or get a
    corporate card.
  question: Why does this matter for enterprises?
featured: false
lang: en
publishedAt: '2026-11-10T00:00:00+00:00'
relatedSlugs: []
sources:
- name: Hugging Face Blog
  url: https://huggingface.co/blog/hub-gcp-marketplace
summary: Hugging Face billing through Google Cloud is not exciting, but in large companies,
  getting past procurement is often what decides whether a tool gets used.
tags:
- industry
- ai-ml
- products
title: Pay for Hugging Face Hub with your Google Cloud Account
trending: false
type: news
---

You can now link your Hugging Face organization to your Google Cloud account, so that your Hugging Face usage shows up on your Google Cloud bill instead of being charged to a credit card. Get started [on the Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/huggingface-public/hugging-face-hub).

Hugging Face is where teams find, build and run open models: from hosting private models and datasets, to running GPU workloads with [Jobs](https://huggingface.co/docs/hub/jobs-overview), deploying models with [Inference Endpoints](https://huggingface.co/docs/inference-endpoints), calling thousands of models through [Inference Providers](https://huggingface.co/docs/inference-providers), or hosting demos on GPU [Spaces](https://huggingface.co/docs/hub/spaces-overview).

If your company already runs on Google Cloud, adding a new vendor and a corporate credit card just to use these services can slow things down. By linking your organization through the Google Cloud Marketplace:

- **One bill**: your Hugging Face usage appears on your existing Google Cloud invoice, next to the rest of your cloud spend.
- **No new vendor to onboard**: purchases go through your existing Google Cloud billing account and procurement process.
- **Everything is covered**: upgrading your org to a [Team or Enterprise](https://huggingface.co/enterprise) subscription, pay-as-you-go compute (Jobs, Inference Endpoints, Inference Providers, GPU Spaces, ZeroGPU quota extension), and additional storage at [public Hugging Face pricing](https://huggingface.co/pricing).

If you're an admin of your Hugging Face organization, here's how to set it up, step by step.

Go to the [Hugging Face Hub listing](https://console.cloud.google.com/marketplace/product/huggingface-public/hugging-face-hub) on the Google Cloud Marketplace, select the Google Cloud project you want to use, and click on "Subscribe".

You are now on the subscription page. Select the billing account to be charged, review and accept the terms, then click "Subscribe".

Once the order is placed, Google Cloud asks you to finish setting up your account with Hugging Face. Click on "Sign up with Hugging Face" to be redirected to Hugging Face.

You are now on Hugging Face, where you can select the organization you want to link to your Google Cloud account. Only organizations where you are an admin are listed. Select it and confirm.

You are then redirected to the billing settings of your organization. The payment method section now shows the linked Google Cloud account, with a pending status.

Every cloud marketplace subscription is reviewed by the Hugging Face team before paid usage starts being billed through it. While the subscription is pending, usage keeps being billed to the organization's existing payment method, if any.

Once your subscription is approved, you will receive an email confirming that your Google Cloud account and Hugging Face organization are linked. Organizations that already have a credit card on file switch to cloud marketplace billing at the start of their next billing period. Organizations on the free tier with no credit card on file usually switch immediately, so their paid usage is billed through the cloud marketplace right away.

To confirm it, open the billing settings of [your organization](https://huggingface.co/settings/organizations): the Google Cloud account is now shown as the organization's active payment method.

Your organization is now billed through your Google Cloud account. All members of your organization can use Hugging Face compute services, and the usage will show up on your Google Cloud bill.

A few things worth knowing:

- **Google Cloud replaces the credit card** as the organization's payment method. Usage is metered and reported to Google Cloud, so adding credits is not available while the organization is billed through the marketplace.
- **Included credits still apply**: if your organization has a Team or Enterprise subscription, the monthly included credits are applied before any pay-as-you-go usage is reported to Google Cloud.
- **Monitor your usage** at any time from the billing section of your [organization settings](https://huggingface.co/settings/organizations), and find the charges in the [Billing reports](https://console.cloud.google.com/billing) of the Google Cloud console.
- **Linking and unlinking are audited**: both actions are recorded in your organization's [audit logs](https://huggingface.co/docs/hub/audit-logs).

Thanks for reading! You can find more details in the [billing documentation](https://huggingface.co/docs/hub/billing#cloud-providers-partnerships). If you have any questions, please contact us at [billing@huggingface.co](mailto:billing@huggingface.co).

## Summary

**TLDR:** Hugging Face billing through Google Cloud is not exciting, but in large companies, getting past procurement is often what decides whether a tool gets used.

- Hugging Face organizations can now link to Google Cloud and have usage charged to their Google Cloud bill instead of a credit card.
- The arrangement covers Team and Enterprise subscriptions, pay-as-you-go compute and additional storage at public Hugging Face pricing.
- Companies can buy through existing procurement instead of onboarding a new vendor.
- Setup goes through the Hugging Face Hub listing on Google Cloud Marketplace and requires a Hugging Face org admin.

## 摘要

**重點摘要：** Hugging Face 能透過 Google Cloud 付款，聽起來很無聊，但在大公司裡，能不能順利過採購往往決定一個工具會不會被採用。

- Hugging Face 組織現在可以綁定 Google Cloud 帳戶，用量直接列在 Google Cloud 帳單上，不必再刷信用卡。
- 適用範圍包括 Team 與 Enterprise 方案、按用量計費的運算資源和額外儲存空間，價格與 Hugging Face 公開定價相同。
- 企業可以沿用既有採購流程，不必另外新增供應商。
- 設定要從 Google Cloud Marketplace 上的 Hugging Face Hub 頁面開始，並需要 Hugging Face 組織管理員權限。