---
title: "OpenAI Codex Can Now Watch You Work Once and Repeat the Task"
summary: "OpenAI has shipped Record & Replay in Codex app version 26.616, a feature that lets AI agents observe a user completing a workflow demonstration and convert it into a reusable, editable 'skill' executable anytime thereafter. Available to paid ChatGPT subscribers on macOS—with EU, UK, and Swiss users excluded—the feature represents a significant step toward no-code automation that closes the gap between enterprise RPA tools and conversational AI agents."
category: "developer-tools"
publishedAt: 2026-06-23
modifiedAt: 2026-11-15T00:00:00Z
lang: "en"
featured: false
trending: true
sources:
  - name: "The Decoder"
    url: "https://the-decoder.com/openais-codex-can-now-watch-you-work-once-and-repeat-the-task-forever/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/318759/20260620/openai-codex-automation-gains-record-replay-show-it-once-skip-script.htm"
  - name: "OpenAI Developers"
    url: "https://developers.openai.com/codex/record-and-replay"
  - name: "AI Weekly"
    url: "https://aiweekly.co/alerts/openai-adds-record-replay-to-codex-for-macos-business-users"
tags:
  - "OpenAI"
  - "Codex"
  - "workflow automation"
  - "AI agents"
  - "developer tools"
  - "Computer Use"
  - "RPA"
  - "no-code"
relatedSlugs:
  - "2026-06-12-openai-acquires-ona-gitpod-codex-cloud-agents-en"
  - "2026-06-04-openai-codex-sites-role-plugins-enterprise-en"
  - "2026-06-11-anthropic-2026-agentic-coding-trends-report-en"
---

The single biggest friction point in enterprise workflow automation has never been the automation itself—it's been describing the automation to the tool. Robotic Process Automation (RPA) tools such as UiPath and Automation Anywhere have offered record-and-replay functionality for years. Their recordings capture coordinates and UI elements, and they break when the interface changes.

OpenAI's Record & Replay feature, shipped June 18 in Codex app version 26.616, takes a different approach: show the agent what you want done, and it figures out the rest.

## How Record & Replay Works

The mechanism is straightforward in concept, though consequential in implementation. A user activates Record mode, completes their workflow as they normally would—opening applications, entering data, navigating interfaces, submitting forms—while Codex observes. When the user stops recording, Codex analyzes the sequence of actions, identifies the underlying intent and pattern, and converts the demonstration into a reusable "skill."

That skill can be invoked by name at any point thereafter, executed by the same Codex agent via Computer Use, browser automation, plugin APIs, or any combination of available tools. The workflow runs autonomously each time it's called—no re-demonstration required.

OpenAI's documentation describes the generated skill as refinable: users can ask for further refinements, such as calling out hidden preferences like naming conventions, field defaults, or decision points, and give new values, such as a different file to upload, on each run.

## Computer Use as the Infrastructure Layer

Record & Replay is built on Computer Use—OpenAI's framework for agents that interact with computer interfaces rather than APIs. Computer Use lets Codex control desktop applications on the user's behalf.

Unlike traditional RPA macros, which record coordinates, Record & Replay generates a skill description that Codex's language model interprets on replay.

The requirement that Computer Use be enabled for Record & Replay to function means the feature is available only on platforms where Computer Use has been deployed. As of version 26.616, that includes macOS; the feature is not yet available on Windows or web-based access. Computer Use has been available in the European Union since June 16, though Record & Replay itself is not yet available in the EU, UK, or Switzerland, and OpenAI has not publicly explained the distinction.

## The RPA Parallel—and the Divergence

Enterprise RPA tools such as UiPath and Automation Anywhere have offered record-and-replay functionality for years, and the comparison is instructive. Those platforms also offer "record" modes where a user performs a task and the tool generates a bot definition. The fundamental difference is what happens between the recording and the execution.

Traditional RPA records literal screen coordinates, element identifiers, and pixel positions. Change the browser window size, update the application's UI, or move a button, and the bot breaks.

Codex's Record & Replay generates skills from semantic understanding of the demonstrated workflow, not from brittle coordinate capture. The agent observes what the user is trying to accomplish—upload a video with metadata, file an expense report, create a project ticket—and encodes that intent in a form that can adapt to minor interface changes without breaking.

## Practical Applications and Demonstrated Use Cases

OpenAI's documentation and demonstrations have highlighted several representative use cases:

**Content publishing.** Recording a YouTube video upload workflow, including metadata, a thumbnail, and subtitles, and converting it into a skill that Codex can repeat.

**Expense management.** Capturing the process of filing an expense in a corporate portal and converting it into a repeatable skill that processes new expenses as they arrive.

**Recurring data extraction.** Demonstrating how to download a recurring report and converting it into a reusable skill.

**Ticket and issue creation.** Recording the creation of a correctly configured issue and converting it into a reusable skill.

**Reservations and bookings.** Capturing a parking space booking workflow in a corporate facilities app and converting it to a repeatable task.

The unifying theme is what OpenAI describes as "stable, repeatable workflows that are easier to show than describe." This is a practical acknowledgment of a real limitation in current agent orchestration: writing a precise natural language description of a complex multi-step workflow is often harder than simply doing it, and descriptions frequently fail to capture the corner cases and sequence dependencies that make automations work correctly.

## Geographic Restrictions and Competitive Context

The EU, UK, and Switzerland exclusion for Record & Replay applies to the initial release, and OpenAI has not publicly explained the reason or given a timeline for expansion. Computer Use involves capturing screen content, which can include personal data, user credentials, and proprietary information.

The competitive landscape for workflow automation is active. Record & Replay takes a demonstration-based approach: instead of describing a workflow in a prompt, users perform the task while Codex watches and drafts a skill from it.

## What This Means for Developer Workflows

For developers specifically, Record & Replay opens up automation paths for tooling that resists API-based integration: internal legacy systems, third-party SaaS platforms without public APIs, compliance and regulatory portals that only support human browser access, and proprietary enterprise applications built on desktop frameworks.

The ability to demonstrate a workflow once and have it become a reusable agent skill also changes the calculus for one-off automations that previously weren't worth the investment to script. If the cost of automation is a single demonstration rather than hours of scripting and testing, the threshold for what's worth automating drops substantially—potentially affecting how developers and knowledge workers think about the entire category of repetitive computer-mediated work.

Teams building on Codex APIs could potentially capture domain-specific workflows from human subject matter experts and deploy them as reusable skills across their organization—a capability that, if it works reliably at scale, represents a meaningful acceleration in how institutional knowledge gets encoded into software systems.

*Correction (November 15, 2026): 23 sentences were corrected or removed to match the sources listed on this page.*
