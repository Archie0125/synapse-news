---
title: "OpenAI Codex Can Now Watch You Work Once and Repeat Any Task Forever"
summary: "OpenAI has shipped Record & Replay in Codex app version 26.616, a feature that lets AI agents observe a user completing a workflow demonstration and convert it into a reusable, editable 'skill' executable anytime thereafter. Available to paid ChatGPT subscribers on macOS—with EU, UK, and Swiss users excluded—the feature represents a significant step toward no-code automation that closes the gap between enterprise RPA tools and conversational AI agents."
category: "developer-tools"
publishedAt: 2026-06-23
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

The single biggest friction point in enterprise workflow automation has never been the automation itself—it's been describing the automation to the tool. Robotic Process Automation (RPA) platforms spent a decade asking users to document every click, field value, and conditional branch before a bot could execute a task. The result was powerful on paper and brittle in practice, and typically required dedicated specialists to maintain.

OpenAI's Record & Replay feature, shipped June 18 in Codex app version 26.616, takes a different approach: show the agent what you want done, and it figures out the rest.

## How Record & Replay Works

The mechanism is straightforward in concept, though consequential in implementation. A user activates Record mode, completes their workflow as they normally would—opening applications, entering data, navigating interfaces, submitting forms—while Codex observes. When the user stops recording, Codex analyzes the sequence of actions, identifies the underlying intent and pattern, and converts the demonstration into a reusable "skill."

That skill can be invoked by name at any point thereafter, executed by the same Codex agent via Computer Use, browser automation, plugin APIs, or any combination of available tools. The workflow runs autonomously each time it's called—no re-demonstration required.

OpenAI's documentation describes skills as editable after creation: users can modify the generated automation logic, add conditional branches, parameterize inputs (so the same skill can process different files or fill different forms depending on context), and combine multiple skills into larger automated pipelines.

## Computer Use as the Infrastructure Layer

Record & Replay is built on Computer Use—OpenAI's framework for agents that interact with computer interfaces rather than APIs. Computer Use allows Codex to control the keyboard, mouse, and screen in the same way a human user would, enabling automation of applications that have no accessible programmatic interface.

This is what distinguishes Record & Replay from earlier workflow automation tools that required web application APIs or purpose-built integrations. Any application a user can interact with visually—a legacy internal tool, a government portal, a desktop application never designed for automation—becomes scriptable through the demonstration model. The agent doesn't need an API endpoint; it needs only to see the workflow performed.

The requirement that Computer Use be enabled for Record & Replay to function means the feature is available only on platforms where Computer Use has been deployed. As of version 26.616, that includes macOS; the feature is not yet available on Windows or web-based access. OpenAI noted that Computer Use became accessible in the European Union as of June 16—a prerequisite step—though Record & Replay itself remains unavailable in the EU, UK, and Switzerland under existing geographic restrictions tied to Codex's data processing terms.

## The RPA Parallel—and the Divergence

Enterprise RPA tools—UiPath, Automation Anywhere, Blue Prism, Microsoft Power Automate—have occupied this territory for years, and the comparison is instructive. Those platforms also offer "record" modes where a user performs a task and the tool generates a bot definition. The fundamental difference is what happens between the recording and the execution.

Traditional RPA records literal screen coordinates, element identifiers, and pixel positions. Change the browser window size, update the application's UI, or move a button, and the bot breaks. Maintenance of RPA workflows is a significant ongoing cost for enterprise IT teams; industry analysts estimate that a meaningful portion of enterprise RPA investment goes toward maintaining and debugging existing automations rather than creating new ones.

Codex's Record & Replay generates skills from semantic understanding of the demonstrated workflow, not from brittle coordinate capture. The agent observes what the user is trying to accomplish—upload a video with metadata, file an expense report, create a project ticket—and encodes that intent in a form that can adapt to minor interface changes without breaking. OpenAI hasn't published technical specifications on how this adaptive execution is implemented, but the distinction from coordinate-based RPA is significant for enterprise reliability expectations.

## Practical Applications and Demonstrated Use Cases

OpenAI's documentation and demonstrations have highlighted several representative use cases:

**Content publishing.** Recording a YouTube video upload workflow—including title, description, thumbnail selection, tag entry, and privacy settings—and converting it into a skill that handles future uploads with varying parameters.

**Expense management.** Capturing the process of filing an expense in a corporate portal and converting it into a repeatable skill that processes new expenses as they arrive.

**Recurring data extraction.** Demonstrating how to download a weekly report from an internal dashboard and save it to a designated location, then having the skill execute automatically on a schedule.

**Ticket and issue creation.** Walking through a correctly configured Jira, Linear, or GitHub issue creation process with specific field values and labels, then generating a skill that creates correctly configured issues from natural language descriptions.

**Reservations and bookings.** Capturing a parking space booking workflow in a corporate facilities app and converting it to a repeatable task.

The unifying theme is what OpenAI describes as "stable, repeatable workflows that are easier to show than describe." This is a practical acknowledgment of a real limitation in current agent orchestration: writing a precise natural language description of a complex multi-step workflow is often harder than simply doing it, and descriptions frequently fail to capture the corner cases and sequence dependencies that make automations work correctly.

## Geographic Restrictions and Competitive Context

The EU, UK, and Switzerland exclusion for Record & Replay reflects ongoing tensions between OpenAI's agentic capabilities and European data protection frameworks. Computer Use involves capturing screen content, which can include personal data, user credentials, and proprietary information. The GDPR's requirements around automated decision-making and data minimization impose constraints that OpenAI has not yet fully resolved for agentic Computer Use products in those jurisdictions.

This creates a market bifurcation where enterprise teams in Europe lack access to the same automation capabilities available to their US counterparts—a dynamic that has surfaced repeatedly as OpenAI, Anthropic, and Google deploy increasingly powerful agentic features with geographic carve-outs.

The competitive landscape for workflow automation is active. Microsoft's Power Automate has integrated Copilot capabilities for natural language workflow creation. Anthropic's Claude with Computer Use supports comparable desktop automation. Zapier and Make have added AI-powered workflow builders. What OpenAI's Record & Replay adds that most competitors lack is the demonstration-based approach: instead of describing a workflow in natural language (which requires users to think abstractly about their process) or configuring a workflow in a visual builder (which requires explicit step enumeration), Record & Replay lets users stay in the flow of actually doing the task and lets the AI handle the abstraction step.

## What This Means for Developer Workflows

For developers specifically, Record & Replay opens up automation paths for tooling that resists API-based integration: internal legacy systems, third-party SaaS platforms without public APIs, compliance and regulatory portals that only support human browser access, and proprietary enterprise applications built on desktop frameworks.

The ability to demonstrate a workflow once and have it become a reusable agent skill also changes the calculus for one-off automations that previously weren't worth the investment to script. If the cost of automation is a single demonstration rather than hours of scripting and testing, the threshold for what's worth automating drops substantially—potentially affecting how developers and knowledge workers think about the entire category of repetitive computer-mediated work.

OpenAI has indicated that Record & Replay skills will be accessible across the Codex ecosystem, including via API for enterprise integrations. Teams building on Codex APIs could potentially capture domain-specific workflows from human subject matter experts and deploy them as reusable skills across their organization—a capability that, if it works reliably at scale, represents a meaningful acceleration in how institutional knowledge gets encoded into software systems.
