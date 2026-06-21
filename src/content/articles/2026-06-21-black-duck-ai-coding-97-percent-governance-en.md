---
title: "97% of Enterprise Developers Use AI Coding Tools—But Only 30% Have Governance in Place"
summary: "A new Black Duck study of 831 enterprise software engineers finds AI coding tools have achieved near-total adoption, with developers reclaiming an average of 8 hours per week. But fewer than one-third of teams have governance frameworks covering AI-generated code, and 64% express significant concern about AI-introduced security vulnerabilities."
category: "developer-tools"
publishedAt: 2026-06-21
lang: "en"
featured: false
trending: false
sources:
  - name: "Black Duck Press Release"
    url: "https://news.blackduck.com/2026-06-09-AI-Coding-Hits-97-Enterprise-Adoption-New-Black-Duck-Study-Shows-Governance-Is-the-ROI-Multiplier"
  - name: "SD Times"
    url: "https://sdtimes.com/ai/ai-coding-adoption-rate-hits-97-black-duck-study-reveals/"
  - name: "Infosecurity Magazine"
    url: "https://www.infosecurity-magazine.com/news/ai-coding-adoption-governance-lags/"
tags:
  - "ai-coding"
  - "developer-tools"
  - "security"
  - "governance"
  - "enterprise"
relatedSlugs:
  - "2026-06-12-opencode-displaces-cursor-ai-coding-agent-en"
  - "2026-06-11-anthropic-2026-agentic-coding-trends-report-en"
---

# 97% of Enterprise Developers Use AI Coding Tools—But Only 30% Have Governance in Place

AI coding assistants have achieved something that enterprise software almost never does: near-universal adoption in roughly three years. According to a new study from Black Duck, the application security firm formerly known as Synopsys's Software Integrity Group, 97% of enterprise software engineers and DevOps professionals at organizations with 500 or more employees now use AI coding tools in their daily work.

That number, drawn from a survey of 831 developers conducted in March 2026, represents not a gradual climb but a practical endpoint. The remaining 3% may reflect workflow-specific exceptions, compliance-constrained environments, or individual preference—not meaningful resistance. AI coding assistance, across the enterprise landscape, is simply how software is written now.

The harder story is what comes next: 68% of those same developers say it is "extremely important" to have a clear, automated system for tracking AI-generated code—and fewer than one in three teams (30%) actually has full governance in place to do it.

## The Productivity Data

The productivity gains are real, large, and consistent across the survey. 92% of development teams report improved productivity and release velocity as a result of AI coding tools; 58% describe the improvement as "major." The quantitative anchor is striking: developers reclaim an average of eight hours per week—roughly an entire working day—through AI assistance on tasks like code completion, test generation, documentation drafting, and refactoring.

More than half of surveyed organizations (53%) have seen their total code volume grow by over 25% since AI adoption. That figure captures something important beyond raw productivity: AI coding tools are not merely accelerating the same work—they are enabling development teams to tackle scope they would previously have deferred or declined.

The business case for AI coding adoption, at this point, does not require making. Productivity improvements of this magnitude, delivered consistently across 92% of adopting teams, represent one of the clearest enterprise software ROI stories in years. The debate has moved on.

## The Governance Gap

The problem the data surfaces is not whether to adopt AI coding tools—that decision has been made, at scale, across the industry. The problem is what happens when adoption runs well ahead of the controls needed to manage its risks.

68% of developers say having an automated system to track AI-generated code is "extremely important." Only 30% of teams have full governance frameworks to do it. That is a gap of roughly 38 percentage points between stated importance and operational reality—and it is the gap where security and liability exposure accumulates.

The consequences are documented in the data. Open-source vulnerability exposure has doubled as AI accelerates code creation, according to a separate Black Duck finding. AI coding tools frequently surface code from training corpora that includes dependencies with known vulnerabilities, outdated APIs, and licensing terms that create compliance exposure. Without governance frameworks that can identify AI-generated code at the point of commit—and assess it against security policies, license requirements, and architectural standards—those exposures enter the codebase silently.

The ROI connection is not abstract. Black Duck's data shows that teams with full governance in place are 55% more likely to report a major improvement in efficiency compared to teams without governance. The counterintuitive finding is that governance is not a drag on productivity—it is a force multiplier for the productivity AI delivers.

## The Security Dimension

64% of surveyed developers express moderate or extreme concern about AI coding assistants introducing security defects or vulnerabilities. That is a high proportion for a technology that 97% of those same respondents are using daily—and it reflects a genuine operational tension: teams are using tools they know to be imperfect, in ways they know to be insufficiently monitored, because the productivity benefit is too significant to forego.

The security concern is warranted. AI coding tools learn from training data that includes public repositories containing both secure and insecure code patterns. Without fine-tuning on security-specific corpora and explicit safety guardrails, these tools will suggest insecure patterns alongside secure ones, and developers under productivity pressure may not catch the difference. Black Duck's research found that open-source vulnerabilities have doubled in correlation with AI adoption timelines—though causation is difficult to establish given the simultaneous increase in total code volume.

The security vendors have noticed. The AI application security market—tools designed to scan AI-generated code for vulnerabilities, track AI-generated code provenance, and enforce policy at the commit level—is expanding rapidly. Black Duck itself has released capabilities specifically targeting AI-generated code. GitHub's Advanced Security platform has added AI-specific scanning. The market is responding to a problem that the adoption data makes difficult to ignore.

## What Governance Actually Looks Like

The 30% of teams that have full governance frameworks in place are doing several things that their less-governed counterparts are not. They are tracking which code was AI-generated, at the commit level, so they can apply differential scanning policies. They are using composition analysis tools to identify vulnerable dependencies that AI-generated code may inadvertently introduce. They are establishing policy on which AI models developers can use, under what conditions, and for what categories of work—recognizing that not all code is equivalent in its security requirements.

Critically, the most effective governance frameworks are automated rather than manual. Asking developers to self-report AI-generated code in commit messages, or to apply separate review processes when they use AI assistance, degrades over time as adoption normalizes. The teams reporting the strongest security and productivity outcomes are those that have integrated governance into the development pipeline itself—where AI-generated code is tagged, scanned, and policy-checked automatically, without requiring any individual judgment call.

That is an achievable state for most enterprise engineering organizations, but it requires intentional investment. The teams that have not yet made that investment—the 70% without full governance—are accumulating what the security industry calls "AI technical debt": an audit exposure, a vulnerability surface, and a license compliance question that grows larger with every sprint.

## Industry Context

The Black Duck study lands in a developer tools market that has reorganized dramatically around AI since 2023. GitHub Copilot remains the highest-adoption tool, but the landscape has fragmented into dozens of competing assistants at multiple price points. Cursor had been the fastest-growing premium tier product before SpaceX's $60 billion acquisition last week changed its trajectory. OpenCode, Claude Code, and Amazon Q compete for the enterprise segment. Each AI coding tool has slightly different training data, slightly different code suggestion patterns, and slightly different security profiles—a variable that governance frameworks need to account for.

The study's broader finding—that 97% enterprise adoption has arrived without commensurate governance infrastructure—is not unique to AI coding tools. It mirrors patterns from earlier enterprise software transitions, including cloud adoption, open-source dependency adoption, and mobile development. What makes AI adoption different is the speed: those prior transitions took a decade to reach comparable saturation. AI coding tools reached 97% enterprise adoption in roughly three years, which means governance infrastructure had less time to catch up.

For CTOs, VPs of Engineering, and AppSec teams, the Black Duck data is an accountability document as much as a market research report. The productivity benefits are real and captured. The governance gap is real and documented. The 55% efficiency premium for governed teams is real and measurable. What happens next is a choice.
