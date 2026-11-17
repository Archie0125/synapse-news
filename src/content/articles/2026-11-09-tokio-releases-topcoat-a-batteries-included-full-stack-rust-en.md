---
category: developer-tools
faqs:
- answer: Topcoat is a modular, batteries-included full-stack web framework for Rust
    built by the Tokio team, now public at version 0.9. It is entirely server-rendered
    and includes routing, an asset pipeline, Tailwind integration without Node.js,
    and a component library.
  question: What is Topcoat?
- answer: 'Topcoat''s $(...) expressions are type-checked Rust fragments that run
    on the server for the first render and are also translated to JavaScript to re-run
    in the browser. For updates that need the server, #[shard] components re-render
    on the server and swap the new HTML into the page.'
  question: How does Topcoat add interactivity without WebAssembly?
- answer: Topcoat's server-driven model places it closer to HTMX, Datastar and Phoenix
    LiveView than to client-side frameworks like React or SolidJS. It avoids shipping
    a client-side router or a separate client build step.
  question: How does Topcoat compare with other web frameworks?
featured: false
lang: en
publishedAt: '2026-11-09T06:42:00+00:00'
relatedSlugs: []
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/topcoat-rust-framework/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: Topcoat bets that Rust web developers want less JavaScript rather than more
  WASM, and that contrarian choice makes it the most interesting Rust framework in
  a while.
tags:
- developer-tools
- open-source
title: 'Tokio Releases Topcoat: A Batteries-Included Full-Stack Rust Framework'
trending: false
type: news
---

[Topcoat](https://github.com/tokio-rs/topcoat), a modular full-stack framework for Rust built by the [Tokio](https://tokio.rs/) team, has moved out of private development with a public [GitHub repository](https://github.com/tokio-rs/topcoat), a [v0.9 release](https://github.com/tokio-rs/topcoat/releases/tag/v0.9.0), and a series of blog posts outlining its direction. The project is positioned as a batteries-included web framework that stays entirely server-rendered, with reactivity added through cross-compiled Rust expressions rather than WebAssembly.

Topcoat introduces several ideas, including a `view!` macro for mixing HTML with Rust control flow, module-based routing inferred from the project's file tree, an asset pipeline with content-hashed URLs, and a Tailwind integration that works without Node.js. It also announces tighter integration with the [Toasty](https://github.com/tokio-rs/toasty) async ORM, which handles migrations and database access in the same Rust workspace.

One of the headline design choices in Topcoat is the `$(...)` expression. These are ordinary type-checked Rust fragments that Topcoat evaluates on the server for the initial render and also translates to JavaScript, so they re-run instantly in the browser without a WASM bundle or separate client build step.

When an update does need the server, developers can mark a component as a `#[shard]`. Topcoat re-renders the shard on the server whenever one of its `$(...)` arguments changes, then swaps the new HTML into the page, giving a similar feel to reactive updates without shipping a client-side router. This positions Topcoat closer to HTMX, Datastar and Phoenix LiveView than to React or SolidJS.

Topcoat also ships [Topcoat UI](https://github.com/tokio-rs/topcoat/blob/main/docs/ui.md), a component library inspired by [shadcn/ui](https://ui.shadcn.com/). Components are vendored into the project via the `topcoat ui` CLI command, so teams can edit their design and functionality rather than wrap a fixed package. The approach has drawn attention on [Hacker News](https://news.ycombinator.com/item?id=48952067), with one commenter excited by the concept:

Oh man I'd love a nice full stack framework in Rust! Django, Laravel, and Rails are very neat. I used to be a micro framework kind of guy, but having everything integrated is more and more appealing over the last few years.

This would take a long time to get feature complete with the core of those big full stack frameworks, but I'm rooting for it! Getting to use the Rust type system with a full stack web framework sounds incredible.


On the same thread, [Hobofan](https://news.ycombinator.com/item?id=48953279) worried the project "will possibly gain outsized adoption in the community based on name recognition rather than merit", whilst [frio](https://news.ycombinator.com/item?id=48953662) argued the Rust ecosystem still lacks a true Django equivalent with admin, auth and migrations baked in.

Speaking at ScyllaDB's P99 2026 conference, Tokio creator Carl Lerche [admitted](https://www.devclass.com/development/2026/10/30/topcoat-enables-rust-to-render-server-side-web-apps/5306490) Topcoat is not aimed at Figma-scale applications, but rather the "run-of-the-mill, browser-based, database-driven applications" that make up most of the web.

Within the Rust ecosystem, Topcoat sits alongside [Leptos](https://www.leptos.dev/) and [Dioxus](https://dioxuslabs.com/), both of which compile Rust to WebAssembly and therefore carry an upfront WASM bundle. It overlaps more directly with [Loco.rs](https://github.com/loco-rs/loco) and [Cot](https://cot.rs/), which chase Django-style productivity with ORMs and admin panels, though neither yet matches Topcoat's cross-compiled reactivity model.

Given the rapid 0.x cadence, there is no long-term stability guarantee. The team has committed to release notes for every version and migration guidance where needed, with the roadmap tracking authentication, background jobs, static export and tighter Toasty integration as near-term work on [GitHub issue 104](https://github.com/tokio-rs/topcoat/issues/104). New projects can follow the [Getting started guide](https://github.com/tokio-rs/topcoat/blob/main/docs/getting_started.md) or the [manual setup instructions](https://github.com/tokio-rs/topcoat/blob/main/docs/manual_setup.md). Topcoat is published on [crates.io](https://crates.io/crates/topcoat) under an MIT licence.

Topcoat is an open-source, modular full-stack web framework for Rust, developed and maintained by the [Tokio](https://tokio.rs/) project, the collective behind Rust's most popular asynchronous runtime. It aims to bring Rails or Django-style productivity to Rust developers through server-rendering, declarative reactivity and vendored components, so teams already invested in Rust for infrastructure or performance-critical work can build web applications without adopting a separate language or stack.

## Summary

**TLDR:** Topcoat bets that Rust web developers want less JavaScript rather than more WASM, and that contrarian choice makes it the most interesting Rust framework in a while.

- The Tokio team released Topcoat v0.9, a batteries-included full-stack Rust framework that stays entirely server-rendered.
- Its $(...) expressions are type-checked Rust that runs on the server and is also translated to JavaScript, so no WASM bundle is needed.
- Components marked #[shard] re-render on the server and swap HTML into the page, putting Topcoat closer to HTMX and Phoenix LiveView than to React.
- It includes file-tree routing, a content-hashed asset pipeline, Node-free Tailwind, and integration with the Toasty async ORM.
- Topcoat UI vendors shadcn-style components into projects through a CLI.

## 摘要

**重點摘要：** Topcoat 押注 Rust 網頁開發者要的是更少 JavaScript，而不是更多 WASM，這個反主流的選擇讓它成為近來最有意思的 Rust 框架。

- Tokio 團隊推出 Topcoat v0.9，這是一套「電池全包」的全端 Rust 框架，完全採用伺服器端渲染。
- $(...) 表達式是經過型別檢查的 Rust 程式碼，在伺服器執行，同時被轉譯成 JavaScript，完全不需要 WASM 套件。
- 標記為 #[shard] 的元件會在伺服器重新渲染並替換頁面 HTML，定位更接近 HTMX 與 Phoenix LiveView，而非 React。
- 內建依檔案結構推斷的路由、內容雜湊的資源管線、不需 Node.js 的 Tailwind 整合，並與 Toasty 非同步 ORM 緊密結合。
- Topcoat UI 透過 CLI 把 shadcn 風格的元件直接複製進專案。