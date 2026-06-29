---
title: "Figma Config 2026: Code Layers, Native Animation, and AI Plugins Collapse the Design-Dev Gap"
summary: "At Config 2026, Figma unveiled code layers — executable React code directly on the collaborative canvas — alongside native animation and 3D transform support, AI-generated shader effects, and a prompt-based custom plugin system. The announcements represent the most significant evolution of Figma's product since its founding and directly challenge the traditional boundary between design and engineering workflows."
category: "developer-tools"
publishedAt: 2026-06-29
lang: "en"
featured: false
trending: true
sources:
  - name: "TechCrunch"
    url: "https://techcrunch.com/2026/06/24/figma-adds-code-layers-support-for-animations-more-ai-features-in-new-update/"
  - name: "The Next Web"
    url: "https://thenextweb.com/news/figma-config-code-layers-ai-skills-plugins-animations"
  - name: "CMSWire"
    url: "https://www.cmswire.com/digital-experience/figma-launches-code-layers-motion-at-config-2026/"
  - name: "AI Weekly"
    url: "https://aiweekly.co/alerts/figma-adds-code-layers-native-animations-and-ai-plugins"
tags:
  - "Figma"
  - "Config-2026"
  - "developer-tools"
  - "design-tools"
  - "AI-agents"
  - "code-layers"
  - "animation"
relatedSlugs:
  - "2026-06-12-opencode-displaces-cursor-ai-coding-agent-en"
  - "2026-06-04-openai-codex-sites-role-plugins-enterprise-en"
  - "2026-06-11-anthropic-2026-agentic-coding-trends-report-en"
---

For most of its existence, Figma has been the place where design work ends and engineering work begins. Designers build their components, annotate their specs, and hand the file to a developer who rebuilds it in code. Config 2026, Figma's annual user conference held in late June, was the moment the company announced it is done accepting that boundary.

The centerpiece announcement — **code layers** — lets teams clone repositories directly onto the Figma canvas and work in real code alongside design layers. It is accompanied by native animation support, AI-generated visual effects, and a prompt-based plugin creation system that lets anyone build custom AI-powered tools without writing a line of plugin code. Taken together, the announcements represent the most substantial expansion of what Figma is in the product's history.

## Code Layers: The Core Announcement

Code layers bring executable code directly to the collaborative canvas. Teams can now clone a repository into Figma and extract UI flows from the code into design layers for exploration and testing. The system supports React-based code and npm packages, including popular motion libraries and 3D frameworks.

The mechanic is meaningfully different from what Figma has offered before. Previous code-adjacent features in Figma — the Dev Mode introduced in 2023, the code inspection panel — were fundamentally about reading code. They let designers inspect what a component's specifications would translate to in CSS or React. Code layers are about executing code. You can pull production components into the canvas, modify them through Figma's AI chat interface or its built-in code composer, and use the result as the working basis for a prototype or handoff.

Chief Product Officer Yuhki Yamashita described the intent in terms that framed exploration differently from production: code layers create "an environment where you don't really care about the quality of the code" during the discovery and ideation phase. The point is to make the design canvas a space where designers, engineers, and product managers can collaborate on real UI without waiting for production-ready implementation or polished visual comps.

Code layers also work within Figma Sites, the product's no-code website builder, extending the reach of the feature to non-engineering users who want to incorporate real components into live web pages without opening a code editor.

## Native Animation and 3D Transforms

Until now, Figma's motion capabilities were awkward at best. Designers who needed to demonstrate animations had to build them in After Effects, Rive, or another specialized tool, export them, and then somehow communicate the intent to the developer who would ultimately implement them. The gap between "this is what the animation should feel like" and "this is what the animation actually does in production" was a perennial source of friction and rework.

Config 2026 closes that gap. Figma now natively supports **animations, transitions, and 3D transforms** within the design file. Designers can build and preview motion directly inside Figma, without exporting to an external tool or requiring a code translation step. The result is a motion preview that is the intended implementation specification — not an approximation of it.

The 3D transforms capability is particularly notable. Web and mobile UI design has increasingly incorporated depth, parallax, and three-dimensional transitions as device hardware has become capable enough to render them smoothly. Figma's previous inability to natively represent 3D transforms forced designers into workarounds that made it difficult to communicate the full visual intent of their designs. The Config 2026 update eliminates that constraint.

## AI-Generated Shaders and Custom Skills

The AI design agent that Figma introduced in 2024 has been substantially extended. Two new capabilities stand out.

**Shader generation**: Figma's AI can now generate GLSL shader effects and fills — the mathematical programs that run on the GPU to produce visual effects like light scattering, texture distortion, fluid simulations, and complex gradients. Shader programming is highly technical and has historically been inaccessible to designers without a graphics programming background. AI-generated shaders change that, letting designers describe the visual effect they want in natural language and receive a working shader implementation that can be applied directly to elements in their design file.

**Custom AI skills**: Users can now create reusable AI-powered capabilities for the Figma design agent through text prompts. Describe a repeated task — "generate a layout from a list of content items," "trace a vector path from a raster image," "resize all instances of this component to a specific breakpoint" — and the system creates a repeatable skill the agent can execute on demand. These skills are shareable across teams, which means a design system team can build and publish a library of AI-assisted automation that everyone in the organization can use without having to re-specify the behavior each time.

The custom skills system also integrates with external tools. Users can connect Notion, Granola, Excel, GitHub, and other services to give the Figma AI agent richer context when executing tasks. A design agent that can read from a product spec in Notion and a content spreadsheet in Excel while simultaneously executing a layout task represents a meaningful step toward the kind of agentic design workflow that automates the mechanical parts of the job and leaves creative judgment to the human.

## Weavy Integration on the Roadmap

One announcement for later in 2026: Figma plans to integrate Weavy, the node-based AI media workflow tool it acquired in October 2025, directly into the Figma canvas. The integration will let users generate Weavy workflows from within Figma, tightening the connection between visual design and backend AI-powered media processing.

The Weavy acquisition had raised questions at the time about how Figma intended to integrate a workflow automation tool into a design product. Config 2026 provides the first concrete answer: Weavy workflows will be accessible from the design canvas as generatable, executable processes — another layer in Figma's push to make the canvas the coordination surface for an increasingly automated design-to-production pipeline.

## The Broader Strategic Context

The timing of these announcements is not coincidental. Figma faces competitive pressure from multiple directions.

**AI-native design tools** — including products like Vercel's v0, Cursor-based UI generation, and a growing number of AI-first design prototyping tools — are attracting developer-designers who want to work closer to code from the beginning, rather than in a separate design layer. Code layers are Figma's direct answer to this: if the canvas can host real code, there is no reason to leave Figma to get closer to the implementation.

**The design-developer handoff problem** has intensified as AI coding assistants have accelerated the speed at which developers can ship UI. When a developer using Copilot or Cursor can implement a design specification in an hour rather than a day, the friction cost of the handoff gap increases proportionally. Every hour spent translating design intent into code specification is a larger fraction of the total time. Code layers attack this directly by making the design file itself the source of implementation truth.

**Platform consolidation** is the secular trend across the developer tools market. Teams running Figma for design, GitHub for code, Notion for specs, and Linear for project management have incentive to reduce the number of context switches in their workflow. Figma's Config 2026 announcements — external tool integrations, code layers that bring code into the design environment, Weavy workflow generation — all move in the direction of making Figma the hub that reduces those context switches, rather than one of the nodes in a sprawling tool chain.

CPO Yuhki Yamashita framed this explicitly in the code layers announcement, noting that the feature produces "different behaviour not just with designers, but also with engineers and PMs." Figma is positioning itself as a collaboration surface, not just a design tool — and the Config 2026 announcements make that positioning more concrete than it has ever been.

## What It Means for Developers

The practical implication for product teams is significant. Design reviews no longer require a separate prototype environment or a developer to build a rough implementation for stakeholder review. Engineering managers can show non-technical stakeholders how a feature actually behaves using real code in a Figma canvas. Designers can test edge cases in component behavior — what happens when the list has 200 items, what does the empty state look like — without asking a developer to stand up a test environment.

Whether this shift accelerates product development or simply moves friction from the handoff phase to the design phase is something teams will learn empirically over the next several months. But the direction is clear: Figma is done being just a design tool, and Config 2026 is the most concrete statement yet of what it intends to become.
