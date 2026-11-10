---
category: developer-tools
faqs:
- answer: 先從最簡單的專案開始，看 v4 在實際程式碼上表現如何，再處理共用設計系統，最後才動高度客製的專案。這樣在處理複雜客製層之前，就已經知道哪些預設行為沒變。
  question: 多個專案要升級到 Tailwind v4，建議的順序是什麼？
- answer: 以這次經驗來說，核心 utility 大多正常，問題集中在客製外掛和設定。一個漸層邊框外掛在 v4 下失效，造成整個計畫唯一的延誤。
  question: 升級到 Tailwind v4 最常壞在哪裡？
- answer: 一起升級可以避免長時間在不同專案間維護兩套 Tailwind 寫法。而且每次升級的經驗還新鮮，可以直接用到下一個專案。
  question: 為什麼要一次升級多個 Tailwind 專案，而不是逐一處理？
featured: false
lang: zh
publishedAt: '2026-11-10T06:01:00+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/richardlemon/upgrading-three-tailwind-projects-to-v4-in-one-sprint-5gfa
summary: 這次遷移到 Tailwind v4，最寶貴的心得其實跟技術無關，而是先後順序：先拿最簡單的專案練手熟悉，自訂 plugin 則留到最後處理，因為進度最容易在那裡延誤。
tags:
- developer-tools
- open-source
title: 一個 Sprint 內把三個專案升級到 Tailwind v4
trending: false
type: news
---

## Why I upgraded three sites in the same week

I had three client projects on Tailwind 3.x that all needed new features in the same sprint. Tailwind v4 was out, the new engine looked fast enough to justify the risk, and I did not want to maintain two different utility dialects for long.

So I blocked a week and upgraded all three in one go. This is what actually mattered: the utilities that kept working, the custom pieces that did not, and the order that made it survivable.

## The order: simple static, then shared design system, then the weird one

The main decision was to pick an order that let me learn on a safer codebase and reuse that knowledge on the more fragile ones.

### 1. The simple marketing site

First was a small marketing site: no complex build pipeline, no design tokens, just Tailwind plus a few components.

The goal here was not perfection. The goal was to get a green build, scan the UI, and see what Tailwind v4 does to a real project without a lot of custom layers in the way.

### 2. The shared design system

Second was a shared design system that feeds multiple apps. It had more custom config, more abstractions, and more places where Tailwind had been bent to fit a design token setup.

Doing this second meant I already knew which defaults survived and which config knobs were now ignored, so I could focus on the design system layer instead of debugging basic utilities.

### 3. The Gate Seal site with the gradient border plugin

Last was the Gate Seal site, which had the most custom Tailwind plugins. One of them was a gradient border plugin that stopped working under v4. I only touched it after I had a cleaner mental model from the first two upgrades.

This site is also where the schedule slipped. The gradient border plugin work took longer than planned.

## What I checked before touching the config

Before changing any config, I did three quick passes on each project.

### 1. How much custom Tailwind is there, really?

I scanned for anything that smelled like Tailwind glue code:

- Custom plugins in `tailwind.config.js` or separate plugin files
- Heavy use of `@apply` in CSS files
- Design tokens wired into Tailwind `theme` sections
- Anything that depended on the old JIT behavior or file scanning

The more of these I saw, the later that project went in the order.

### 2. Where Tailwind classes live

Tailwind v4 changes how you tell it where to look for classes. So I made a list per project:

- Framework templates
- Inline HTML in CMS fields
- Markdown content rendered with class names
- Any odd places like JSON configs or data attributes

This list was useful later, when checking for missing styles. If a page suddenly looked naked, I could quickly see if its templates were still in Tailwind's world.

### 3. Which utilities are actually used

I did not generate a full usage report, but I did search for a few classes that often change behavior across versions: typography, spacing scales, and color utilities.

If a project leaned heavily on a certain pattern, I checked that pattern early after the upgrade instead of waiting for QA to stumble on it.

## What I deleted from the config

On each project, the Tailwind config had grown slowly over time. The upgrade was a good excuse to throw things out, roughly in this order.

### 1. Old purge / content settings

Anything related to the old purge/content scanning setup went away. The new engine handles this differently, and keeping the old keys around only adds confusion.

I replaced it with the minimal v4-style configuration for where the classes live, then adjusted as needed when I saw missing styles.

### 2. Redundant theme extensions

A lot of theme extensions had been added for one-off needs in the past: colors that were almost never used, spacing values that duplicated existing ones, or font sizes that had fallen out of the design system.

During the upgrade I removed anything that:

- Was not referenced in templates
- Duplicated a core Tailwind token
- Was only used in a single place that could be refactored to a core utility

This made the config smaller and reduced the surface area for v4 differences to bite later.

### 3. Clever variants that nobody used

Some configs had custom variants that sounded clever when they were added but never made it into real components. Those went away. Tailwind v4 has its own ideas about variants, and dragging unused ones forward is not worth the mental overhead.

## The utilities that quietly survived

Most of the core Tailwind utilities behaved as expected after the upgrade. Layouts did not explode.

In practice, these stayed boring in a good way across all three sites:

- Flex and grid utilities for layout
- Spacing (margin/padding) on the default scale
- Typography basics: font sizes, weights, line heights
- Border radius, shadows, and background colors that used the standard palette

Most of the visual noise after the upgrade came from the edges: custom design tokens, custom plugins, and anything that tried to be too clever with Tailwind internals.

## The gradient border plugin that broke

The Gate Seal site had a custom gradient border plugin. Under Tailwind v3 it generated utilities that faked gradient borders with background images, padding tricks, or pseudo-elements.

Under Tailwind v4, that plugin stopped working. The new engine no longer played nicely with how the plugin registered utilities and consumed theme values. The symptoms were simple: the components that relied on those classes lost their gradient borders entirely.

I had budgeted a few hours for plugin fixes. It took longer than that to:

- Understand how the plugin interacted with the old Tailwind API
- Decide whether to patch it, rewrite it, or replace it with a simpler approach
- Update the components to match whatever new API I ended up with

The main lesson was not about gradients. It was about custom plugins in general: if a plugin reaches into Tailwind internals or relies on undocumented behavior, treat it as a small piece of framework code, not a harmless utility file.

## How I approached custom plugins under v4

Across the three projects, anything that went beyond simple `addUtilities` or `addComponents` got extra scrutiny.

The rough rule I used:

- If a plugin only registers a few static classes, try to replace it with plain CSS or a handful of custom utilities in the config.
- If it generates a lot of variants or uses theme lookups heavily, expect to touch it during the upgrade and test every component that depends on it.

On the Gate Seal site, the gradient border plugin fell into the second category. It was wired into the design system and used theme tokens for colors and radii. Under v4, that complexity became a liability.

## The practical sequence that worked

If you are staring at multiple Tailwind 3.x projects and one sprint on the calendar, the sequence that worked for me looked like this:

1. Pick the simplest site first. Upgrade it with minimal config, get a feel for v4, and accept some rough edges.
2. On that first site, delete old purge/content settings and unused theme extensions. Keep the config as small as possible.
3. Make a quick inventory of where Tailwind classes live across all projects. Update v4's input paths early.
4. Upgrade the project that acts as a design system second. Focus on keeping tokens and core utilities stable.
5. Leave the most plugin-heavy project for last. Budget extra time for each plugin that does more than add a few classes.
6. When something breaks, decide if it should be patched or simplified. The gradient border plugin was a reminder that sometimes the right fix is to reduce cleverness.

This is not a Tailwind v4 changelog. It is just what actually changed in real projects: most utilities survived quietly, old config could be trimmed aggressively, and the custom plugins were where the real work lived.

## Top comments (0)

## Summary

**TLDR:** The best lesson from this Tailwind v4 migration isn't technical. It's sequencing: learn on the easy project, and leave custom plugins for last because that's where schedules slip.

- A developer upgraded three client projects from Tailwind 3.x to v4 in one sprint rather than maintain two utility dialects.
- The order went from a simple marketing site, to a shared design system, to the site with the most custom plugins, so each step reused what the last one taught.
- Core utilities mostly carried over. Custom config and plugins were where things broke.
- A gradient border plugin stopped working under v4 and caused the only schedule slip.
- Takeaway for teams: audit custom plugins and config before estimating a v4 migration, because that's where the risk sits.

## 摘要

**重點摘要：** 這次 Tailwind v4 升級最有價值的心得不在技術，而在順序：先拿簡單專案練手，客製外掛留到最後，因為進度就是在那裡卡住的。

- 一位開發者在同一個 sprint 內，把三個客戶專案從 Tailwind 3.x 升到 v4，免得長期維護兩套 utility 寫法。
- 順序是簡單的行銷網站，接著共用設計系統，最後才是客製外掛最多的網站，每一步都沿用前一步的經驗。
- 核心 utility 大多能直接沿用，真正出問題的是客製設定和外掛。
- 有個漸層邊框外掛在 v4 下失效，成了整個計畫唯一延誤的地方。
- 給團隊的建議：估 v4 升級時程前，先盤點客製外掛和設定，風險都集中在那裡。