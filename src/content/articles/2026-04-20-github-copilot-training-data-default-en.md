---
title: "GitHub Copilot Will Train on Your Code by Default — Opt Out Before April 24"
summary: "Starting April 24, 2026, Microsoft's GitHub will use Copilot interaction data from Free, Pro, and Pro+ users to train AI models by default. The change has ignited fierce backlash from developers worried about intellectual property and proprietary codebases. Business and Enterprise users are exempt, but everyone else must act before the deadline."
category: "developer-tools"
publishedAt: 2026-04-20
lang: "en"
featured: true
trending: false
sources:
  - name: "GitHub Blog — Updates to Copilot Interaction Data Usage Policy"
    url: "https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/"
  - name: "The Register — GitHub: We're Going to Train on Your Data After All"
    url: "https://www.theregister.com/2026/03/26/github_ai_training_policy_changes/"
  - name: "GitHub Changelog — Updates to Privacy Statement and Terms of Service"
    url: "https://github.blog/changelog/2026-03-25-updates-to-our-privacy-statement-and-terms-of-service-how-we-use-your-data/"
  - name: "InfoQ — GitHub Will Use Copilot Interaction Data to Train AI Models"
    url: "https://www.infoq.com/news/2026/04/github-copilot-training-data/"
tags:
  - "github"
  - "copilot"
  - "privacy"
  - "AI-training"
  - "developer-tools"
relatedSlugs:
  - "2026-04-04-cursor-devin-war-en"
  - "2026-04-04-mcp-protocol-explosion-en"
  - "2026-04-08-ai-generated-code-51-percent-en"
---

GitHub has drawn fire from the developer community after announcing it will begin harvesting interaction data from Copilot Free, Pro, and Pro+ users to train and improve its AI models — starting April 24, 2026. The move flips what had been the default: previously, GitHub did not use this data for AI training without explicit user consent. Now, the burden falls on developers to actively opt out.

The policy change was disclosed through an update to GitHub's Privacy Statement and Terms of Service on March 25, with a 30-day runway before it takes effect. For many developers, the update landed as a rude surprise buried in a routine changelog post rather than a prominent notification.

## What Data Is GitHub Collecting?

According to GitHub's official update, the interaction data being collected for training encompasses a broad sweep of developer activity. When a user accepts, modifies, or rejects a Copilot suggestion, that decision — along with the surrounding code context — becomes training material. The collection scope includes:

- Code snippets shown, accepted, or modified by the user
- Code context around the cursor, including surrounding lines, comments, and file names
- Repository structure and project navigation patterns
- Copilot Chat conversations, including prompts and AI responses
- User feedback signals such as thumbs-up and thumbs-down ratings on suggestions

The stated goal is to let GitHub "train and improve" its AI models, which power not just Copilot completions but increasingly also GitHub Actions automation, code review summaries, and security scanning tools.

Critically, Copilot Business and Copilot Enterprise customers are explicitly excluded from this policy. Those tiers operate under separate data processing agreements designed for enterprise environments, with stricter governance controls. The new policy targets the massive base of individual and small-team users on free and lower-cost plans — the very users most likely to be unaware of the change.

## How to Opt Out

The opt-out mechanism exists but requires deliberate action. Users must visit `github.com/settings/copilot/features` and disable the toggle labeled **"Allow GitHub to use my data for AI model training"** under the Privacy section.

GitHub has stated that users who previously opted out of data collection for "product improvements" — a separate but related setting that has existed for some time — will have their preference honored. Their data will not be used for training unless they explicitly opt back in. For everyone else who has not touched that setting, inaction equals consent once April 24 arrives.

## Developer Backlash

The reaction on GitHub's community forums has been swift and largely negative. The discussion thread announcing the policy change collected over 117 thumbs-down reactions within days, alongside hundreds of comments ranging from frustrated to furious. The concerns cluster around three core issues.

**Proprietary code exposure.** Many developers access GitHub with personal Pro accounts while working on corporate codebases. Code that encodes business logic, authentication flows, security architecture, or proprietary algorithms may be subject to non-disclosure agreements or internal data governance policies. The idea that snippets of that code — and Copilot's responses to it — could become part of Microsoft's AI training pipeline strikes many as a potential violation of employer trust, even when the data is nominally anonymized.

**Intellectual property uncertainty.** Courts in the US and EU are still adjudicating whether AI models trained on copyrighted code constitute infringement. Developers worry about becoming unknowing participants in legally contested training pipelines. Several prominent open-source maintainers have publicly called for GitHub to adopt an opt-in model by default, arguing that the current approach inverts reasonable expectations of informed consent.

**Reproducibility and auditability.** If today's prompt-response interaction subtly influences tomorrow's model behavior, the effect is difficult to audit or attribute. Teams that depend on Copilot's suggestion consistency for regulated workflows — think fintech compliance code or medical device software — face a new layer of unpredictability.

## GitHub's Justification

GitHub's public rationale centers on model quality. In its blog post, the company argued that Copilot has become more accurate and contextually aware precisely because of feedback loops aggregating behavior across its user base. Without access to real-world interaction data, the argument goes, model improvement either stagnates or requires far more expensive synthetic data generation.

The business context matters too. Microsoft, which owns GitHub, faces mounting competitive pressure to keep Copilot relevant. As of early 2026, GitHub Copilot leads in enterprise adoption with over 4.7 million paid subscribers — but Cursor, the fast-growing VS Code fork, has been closing the gap fast, now valued at $50 billion after a surge in developer enthusiasm. Google's Gemini CLI and Anthropic's Claude Code are also aggressively expanding. The race to accumulate high-quality real-world coding data has become, in effect, the race to stay competitive.

## The Broader Pattern

GitHub's move fits a familiar playbook. LinkedIn, X, and Slack (before it reversed course following backlash) have all attempted similar data collection defaults over the past two years, with the same arc: change the default, provide an opt-out, absorb the initial outrage, and largely proceed as planned.

What makes GitHub's case distinctive is the specificity and sensitivity of the data involved. Source code is not social media posts or search queries. It often encodes years of engineering decisions, system architecture, and competitive advantage that organizations invest enormous resources protecting. A developer casually accepting a Copilot suggestion while working on a fintech API has different expectations than someone deliberately contributing data to a public dataset.

Industry observers also note the strategic dimension: frontier models like GPT-5.5 Spud and Claude Opus 4.7 are pushing the frontier on general reasoning, but the differentiator for specialized coding tools is increasingly training data anchored in real developer workflows. GitHub — with its roughly 150 million registered developers — is in a structurally unique position to accumulate that data at a scale no competitor can easily replicate. The April 24 policy change is, at its core, an attempt to turn that structural advantage into a durable moat.

## What Developers Should Do Now

The immediate action is clear: if you use Copilot Free, Pro, or Pro+, visit your settings and verify your opt-out status before April 24.

If you work in a corporate environment, confirm with your legal or IT team whether your organization's Copilot usage falls under a Business or Enterprise plan. If it does, you are already exempt. If your team is using individual or Pro accounts for work, the new policy applies, and the right escalation is to evaluate whether to switch to a Business plan or impose an explicit opt-out policy for all staff accounts.

For developers who work primarily on personal or open-source projects, the calculus may be different — contributing interaction data to improve an AI tool you rely on is not inherently unreasonable. But until GitHub provides substantially more transparency about how specific interactions are weighted, used, and eventually removed from training pipelines, the cautious path is to opt out and reassess as more information becomes available.

GitHub has not signaled any intention to change from opt-out to opt-in, and given that the policy aligns with clear commercial interests, a reversal seems unlikely without significant regulatory pressure — or a meaningful flight of enterprise accounts to rivals.

**Deadline: April 24, 2026. Check your settings now.**
