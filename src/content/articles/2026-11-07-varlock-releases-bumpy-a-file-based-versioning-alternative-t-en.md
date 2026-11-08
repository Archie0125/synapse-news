---
category: developer-tools
faqs:
- answer: Bumpy is a monorepo-friendly version management and changelog tool from
    the team behind Varlock, published as @varlock/bumpy. It presents itself as a
    successor to changesets and claims to address more than 120 of that project's
    open issues.
  question: What is Bumpy?
- answer: 'It keeps the same bump-file workflow but adds full workspace: and catalog:
    protocol support across npm, pnpm, Yarn, and Bun, custom per-package publish commands,
    and a configurable dependency propagation algorithm. Its CI runs with two commands
    and no GitHub App.'
  question: How is Bumpy different from changesets?
- answer: Teams hitting changesets limits around pnpm or Bun protocols, non-npm publish
    targets, or peer dependency bumps have the most to gain. Because the workflow
    is similar, the switching cost should be relatively low.
  question: Is it worth migrating from changesets?
featured: false
lang: en
publishedAt: '2026-11-07T06:54:00+00:00'
relatedSlugs: []
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/bumpy-changesets-alternative/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: 'Bumpy''s pitch isn''t a new idea but a fixed one: keep the changesets workflow
  and clear the 120-plus issues its maintainers never got to.'
tags:
- developer-tools
- open-source
title: 'Varlock Releases Bumpy: A File-Based Versioning Alternative to Changesets'
trending: false
type: news
---

[Bumpy](https://github.com/dmno-dev/bumpy), a modern monorepo-friendly version management and changelog tool from the team behind [Varlock](https://varlock.dev), has been gaining traction as a self-described successor to [changesets](https://github.com/changesets/changesets). First unveiled in April 2026 via a [Show HN post](https://news.ycombinator.com/item?id=47931761) from creator [Theo Ephraim](https://bsky.app/profile/theozero.bsky.social), the project now ships under the `@varlock/bumpy` package and claims to address more than 120 open issues from its predecessor.

Bumpy follows the familiar changesets workflow. Contributors drop a small markdown "bump file" into `.bumpy/` that declares which packages should be released, at what level, with a changelog description. The files are reviewable in the PR diff, consolidated into a release PR by CI, and consumed when that PR merges. An example looks like this:

```
```
```
---
'@myorg/core': minor
'@myorg/utils': patch
---
Added user lang prefs to core config.
Fixed locale fallback logic in utils.
```
Where the two tools diverge is beneath that surface. Bumpy ships with full support for `workspace:` and `catalog:` protocols across npm, pnpm, Yarn and Bun, [per-package custom publish commands](https://github.com/dmno-dev/bumpy/blob/main/docs/configuration.md) for VS Code extensions, Docker images or JSR targets, and a configurable three-phase [dependency propagation algorithm](https://github.com/dmno-dev/bumpy/blob/main/docs/version-propagation.md) that lets teams decide how peer dep bumps cascade through their graph. The CI story is leaner too, with two commands, `bumpy ci check` and `bumpy ci release`, running directly in a standard GitHub Actions workflow with no GitHub App to install or separate action repo to trust.

Version [1.14](https://github.com/dmno-dev/bumpy/releases) added [branch-based prerelease channels](https://github.com/dmno-dev/bumpy/blob/main/docs/prereleases.md) where prerelease versions are derived at publish time and never committed to git. The design targets complaints documented in the changesets [own prerelease docs](https://github.com/changesets/changesets/blob/main/docs/prereleases.md), which describe their pre mode as "very complicated" with states that are "very hard to fix". Another differentiator is AI integration. Bumpy ships an [agent skill](https://github.com/dmno-dev/bumpy/blob/main/skills/add-change/SKILL.md) that teaches LLMs how to inspect git changes, identify affected packages and generate bump files via `bumpy add`. It installs through the Vercel Labs [skills CLI](https://github.com/vercel-labs/skills), the GitHub CLI, or as a Claude Code plugin.

Getting started is a single install and an init that migrates existing changesets projects automatically:

```
```
```
bun add -d @varlock/bumpy
bunx bumpy init
```
A [Show HN thread](https://news.ycombinator.com/item?id=47931761) was candid that the project "was coded using AI, but carefully", and the team notes it is already being used to release Varlock alongside 25+ related libraries and plugins. In a separate thread on polyglot monorepos, [bumpy was mentioned](https://news.ycombinator.com/item?id=47845274) as a tool that "fixes a few things with changesets around custom publishing". Teams evaluating migration have [opened issues](https://github.com/dmno-dev/bumpy/issues/148) flagging gaps such as Yarn 4.10 catalog detection.

Competition tightened with the [changesets v3 release](https://www.infoq.com/news/2026/09/changesets-v3-release) in August 2026, which closed many of the long-standing issues bumpy originally targeted. Bumpy's own [differences doc](https://github.com/dmno-dev/bumpy/blob/main/docs/differences-from-changesets.md) now compares against v3 and credits it as "a substantial cleanup", while pointing out remaining gaps around configurable propagation, catalogs, custom publish targets and prerelease workflows. Relative to [semantic-release](https://github.com/semantic-release/semantic-release), bumpy keeps the file-based model but adds a `bumpy generate` command that can produce bump files from branch commits when teams want to bridge both styles.

Bumpy is MIT-licensed, built in TypeScript, and available via the `@varlock/bumpy` package on [npm](https://www.npmjs.com/package/@varlock/bumpy), with the full source and documentation on [GitHub](https://github.com/dmno-dev/bumpy).

## Summary

**TLDR:** Bumpy's pitch isn't a new idea but a fixed one: keep the changesets workflow and clear the 120-plus issues its maintainers never got to.

- Bumpy, from the team behind Varlock, positions itself as a successor to changesets and claims to address more than 120 of its open issues.
- It keeps the familiar flow: markdown 'bump files' in .bumpy/ declare package bumps and changelog text, then CI rolls them into a release PR.
- It fully supports workspace: and catalog: protocols across npm, pnpm, Yarn, and Bun, plus per-package custom publish commands.
- A configurable three-phase dependency propagation algorithm lets teams control how peer dependency bumps cascade.
- CI needs only two commands in GitHub Actions, with no GitHub App to install, which reduces supply-chain trust surface.

## 摘要

**重點摘要：** Bumpy 賣的不是新點子，而是修好的舊點子：保留 changesets 的流程，順手處理掉原專案擱置的 120 多個問題。

- Bumpy 由 Varlock 團隊打造，自稱是 changesets 的接班人，宣稱解決了原專案 120 多個未處理的問題。
- 流程沿用大家熟悉的做法：在 .bumpy/ 放 markdown 格式的「bump 檔」，宣告要升級的套件和變更說明，再由 CI 整合成發版 PR。
- 它完整支援 npm、pnpm、Yarn、Bun 的 workspace: 和 catalog: 協定，也能替個別套件設定自訂發布指令。
- 可設定的三階段相依傳播演算法，讓團隊自己決定 peer dependency 升級要怎麼往下連動。
- CI 只需要在 GitHub Actions 跑兩個指令，不必安裝 GitHub App，降低了需要信任的供應鏈範圍。