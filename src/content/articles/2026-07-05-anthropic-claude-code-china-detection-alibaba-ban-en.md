---
title: "Anthropic's Hidden Spy Code, Alibaba's Ban, and the Claude-China Crisis"
summary: "Anthropic secretly embedded steganographic detection code in Claude Code to flag Chinese users, triggering an Alibaba ban and a broader crackdown on Chinese firms accessing Claude through VPNs and offshore subsidiaries. The covert code was removed after public backlash, but the access war is far from over."
category: "ai-ml"
publishedAt: 2026-07-05
lang: "en"
featured: true
trending: true
sources:
  - name: "The Register"
    url: "https://www.theregister.com/ai-and-ml/2026/07/01/anthropic-is-removing-its-covert-code-for-catching-chinese-competitors/5265366"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/alibaba-bans-claude-code-anthropic-tracking-chinese-users"
  - name: "BanklessTimes"
    url: "https://www.banklesstimes.com/articles/2026/07/03/anthropic-moves-to-block-chinese-firms-using-claude-via-offshore-workarounds/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/319415/20260701/claude-code-hid-proxy-fingerprints-system-prompts-anthropic-promises-fix.htm"
tags:
  - "Anthropic"
  - "Claude"
  - "China"
  - "developer-tools"
  - "AI policy"
  - "Alibaba"
relatedSlugs:
  - "2026-07-05-anthropic-samsung-custom-ai-chip-talks-en"
  - "2026-06-29-us-export-control-claude-fable5-foreign-ban-en"
---

When developers began noticing something strange about the timestamps in Claude Code's output last week, they could not have anticipated what they were about to uncover: a covert, steganography-based surveillance system quietly baked into one of the most popular AI developer tools in the world — designed specifically to detect and flag Chinese users.

The story, which has since triggered an Alibaba-wide ban on Claude Code and a broader Anthropic campaign to shut down all Chinese access channels, offers a window into the messy, secretive front lines of the US-China AI technology war.

## The Hidden Code

Researchers and developers noticed in late June that the date separator in Claude Code's output would inexplicably switch from the standard dash format (`2026-06-30`) to a slash format (`2026/06/30`) on certain machines. Further investigation revealed that the character encoding of an apostrophe in the word "Today's" would also flip between four visually identical Unicode characters depending on the user's system timezone.

The logic was simple: if your system timezone was set to `Asia/Shanghai` or `Asia/Urumqi`, you got a different output. The date separator swap and the Unicode apostrophe encoding together formed a lightweight steganographic fingerprint — hidden in plain sight in the text responses themselves.

Portions of the detection code were XOR-obfuscated with the key `91`, a lightweight technique used specifically to prevent the logic from surfacing in plain-text string searches. The code also cross-referenced hostnames against a curated list of known Chinese AI labs, account resellers, and gateway proxy domains — what the industry calls "transfer stations."

"The implementation should not have been concealed," one security researcher who analyzed the code wrote. "Even if the goal — detecting proxy abuse — is defensible, hiding the detection logic crosses an important line of trust."

## Anthropic's Response

An Anthropic engineer confirmed the existence of the detection system and announced on July 1 that it would be removed. By July 2, the covert code was stripped from Claude Code's codebase.

Anthropic said the experiment, launched in March 2026, was designed to prevent account abuse by unauthorized resellers and to protect against model distillation — the practice of using one company's AI outputs to train a competing model. The company stopped short of apologizing directly, calling it an "internal experiment" that had not been properly reviewed for public trust implications.

But the damage was already done.

## Alibaba Bans Claude Code

On July 4, Alibaba Group issued an internal directive banning the use of Claude Code across all engineering teams starting July 10. The company cited both the privacy implications of the covert tracking and broader concerns about the reliability of third-party AI developer tools following the disclosure.

Alibaba is pushing its internal replacement, **Qoder**, as the preferred alternative. Qoder is built on Alibaba's own Qwen model family — which itself has grown into a leading open-weight model series — and integrates directly into the company's internal development infrastructure.

The Alibaba ban is more than symbolic. Alibaba Cloud is one of the largest enterprise platforms in Asia, and its internal stance on AI tooling carries weight among the broader ecosystem of Chinese enterprises and startups that follow its standards.

## The Broader Crackdown

The hidden code controversy is only one piece of a larger Anthropic effort to shut down unauthorized Chinese access to Claude. As detailed in a Financial Times investigation, Chinese companies had developed an extensive infrastructure of workarounds:

- **Corporate subsidiary channels**: Firms such as Ant Group provided employees with Claude accounts linked to Singapore-based subsidiaries, maintaining a layer of geographic separation between the China-based developers and Anthropic's terms of service.
- **Personal VPN subscriptions**: ByteDance programmers used personal Claude subscriptions accessible via VPN, with the company reimbursing the cost — keeping the accounts nominally personal while the usage was clearly corporate.
- **Cloud routing**: Some organizations routed access through Microsoft Azure accounts registered by foreign-incorporated subsidiaries, allowing mainland developers to query Claude through a technically compliant intermediary layer.
- **Transfer stations**: Dozens of intermediary relay services, listed openly on Chinese-language websites and GitHub pages, accept WeChat and Alipay payments and route queries through reputable foreign accounts on behalf of Chinese users.

Anthropic is now deploying behavioral monitoring to detect these channels — analyzing system timezones, usage timing patterns, and account behavior signatures to identify accounts functioning as transfer nodes. Since April 2026, flagged accounts have been required to complete identity verification with government-issued IDs and live selfie verification before regaining access.

## The Governance Dilemma

The incident crystallizes a tension that AI companies operating in the post-export-control environment have been struggling to navigate.

Anthropic's technology is subject to US export controls — Fable 5, the company's flagship model, was taken offline globally for 19 days in June after a Commerce Department order, before being restored July 1. But the access restrictions are difficult to enforce technically: Claude is a software service, not physical hardware, and the global internet provides abundant routing options for motivated users.

The covert detection approach Anthropic chose — embedding hidden tracking logic in the tool itself — crossed a line that the developer community considers foundational: that tools should not surveil their users in ways those users cannot see or consent to.

The Alibaba ban may signal a broader rethinking among large Chinese tech companies of their dependency on US-origin developer tooling, regardless of whether that tooling is formally accessible. For Anthropic, which has increasingly positioned Claude Code as a professional developer product, the incident is a trust liability that will take time to repair — even if the code itself has been removed.

The access war between US AI companies and Chinese users is likely to continue escalating, with both sides developing more sophisticated detection and circumvention techniques. What Anthropic's experiment showed is that in this conflict, the tools themselves have become part of the battlefield.
