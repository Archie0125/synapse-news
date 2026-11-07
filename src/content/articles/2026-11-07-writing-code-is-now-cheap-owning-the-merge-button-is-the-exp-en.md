---
category: ai-ml
featured: true
lang: en
publishedAt: '2026-11-07T19:15:21.114772+00:00'
relatedSlugs: []
sources:
- name: GitHub Blog
  url: https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/
- name: The New Stack
  url: https://thenewstack.io/together-compiler-gpu-optimization/
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/grab-ai-generated-code-safety/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: The New Stack
  url: https://thenewstack.io/engineers-become-process-engineers/
- name: The New Stack
  url: https://thenewstack.io/scale-ai-code-reviews/
summary: Agents now start 40% of GitHub pull requests, and the tech giants are no
  longer fighting over who writes the code but over who gets to say yes to it.
tags: []
title: Writing Code Is Now Cheap. Owning the Merge Button Is the Expensive Part
trending: true
type: analysis
---

The most revealing AI coding announcement of the year wasn't a model. It was a storage system.

At GitHub Universe, GitHub showed a rebuilt Git backend that, in internal tests, handled 5,000 concurrent agents on one repository and 7,200 pushes per second while reads stayed fast. To support it, GitHub moved 99.99999% of its repositories onto Azure and redesigned how Git handles writes. No team of human developers needs 7,200 pushes per second, and nobody rebuilds the foundations of the world's largest code host for a demo. GitHub did it because it expects machines to make most of the writes into its repositories.

That leads to the point most of the agent coverage keeps missing. **Producing code is no longer the scarce part of software. The scarce part is a human willing to put their name on a change.** Every serious platform company has noticed this, which is why GitHub, GitLab, AWS, Google and Cursor are all competing for the layer that comes after the code is written.

### The numbers show where work is piling up

The adoption curve is steep. According to GitHub's Octoverse data, more than 40% of pull requests started from an agent's first draft by September 2026. In March the figure was 17%. That share more than doubled in six months.

Delivery has not kept up. CircleCI's 2026 delivery data shows average daily workflow runs up 59% year over year. The averages hide a split: the top 5% of teams grew 97%, and the bottom quartile showed no measurable increase. Agents are not speeding up software delivery across the board. They are widening the gap between teams that changed how they ship and teams that only changed how they type.

One study looked at a company that mandated doubling pull request output. Load per reviewer doubled, and within months automated review was covering more code than human review. That is what Goldratt's *The Goal* predicts. If you speed up any step other than the bottleneck, work piles up in front of the bottleneck. Agents made the coding step faster, and the backlog moved to review, CI and deployment.

Aviator's case is the clearest example. Its weekly merged PRs grew from about 100 to more than 400. Its median AI-generated PR reached 640 lines, well past the roughly 400-line point where reviewers' bug detection drops off. No team of nine engineers can carefully read 400 PRs of that size a week. Either the reviews become rubber stamps or the process has to change.

### Reading the diff more carefully won't fix this

The usual response is to add an AI reviewer. Aviator tried that, and it went badly. On one PR, the bot opened 16 of the 18 comment threads. Most were nits about magic numbers and React keys. One thread caught a real race condition. The two comments that actually mattered were design decisions from teammates, and they got buried under the bot's output.

Aviator then tried a four-hour review SLA. First reviews got faster and approvals got emptier, because reviewers skimmed to hit the deadline.

What worked was to stop treating the diff as the thing being reviewed. Aviator's reviewers now check five things: intent, acceptance criteria, invariants the change must not break, the decisions made along the way, and evidence that it works. Machines check rules every time. Humans make decisions. A human still signs off on every PR, but reads something different. The results: the same nine engineers merged 4x more PRs, median time to merge fell from 2.1 days to 3.4 hours, and reverts dropped 40%.

Older research supports this. Microsoft's 2013 study by Bacchelli and Bird found that only 14% of code review comments were about defects. Review was never mainly about catching bugs. It was how a team kept a shared understanding of its own system. **Here's what almost nobody is talking about:** when agents write most of the code, teams lose that shared understanding first. They don't notice for months, until something breaks and nobody can explain why the code looks the way it does.

### The deploy button stays human

Together AI's new Together Compiler sets the pattern the rest of the industry is likely to follow. Coding agents tune GPU kernels overnight, a job that used to take engineers days or weeks. Together AI says the optimization loop is fully autonomous. Final evaluation and deployment are automated too, but a human has to start them after reviewing the changes. The agents do the iterating. A person signs off on what goes to production.

Grab reached the same structure from the mobile side. Its explanation: AI makes code faster to write, and a layered defense is what makes that speed safe. The layers are:

- Lint rules (Android Lint, SwiftLint, plus custom rules) before merge
- Automated tests and QA
- Grab Early Access, which ships pre-release builds to internal users and watches for crashes
- Staged rollouts and feature flags to limit how many users see a change

The incentives are blunt. A mobile crash that ships stays on users' phones, because not everyone updates. It also lowers crash-free session rates, which hurts the app's ranking on Google Play.

None of this is new engineering. Toyota built quality checks into every station on the line. Sakichi Toyoda's loom stopped itself when a thread broke, so one operator could run many machines. Ford cut assembly time for a Model T from 12.5 hours to 93 minutes by 1914 by redesigning the line, not by making workers eight times faster. The New Stack's framing fits: engineers are becoming process engineers, and what they build is the factory the code runs through.

### Why the platforms are racing for this layer

This explains the land grab:

- **GitHub** is building infrastructure for fleets of agents. Agent HQ is meant to be the place where third-party agents get dispatched, and the merge button sits there too.
- **GitLab** is betting that whoever owns CI/CD and security scanning owns governance, and it has a decade-long head start in that pipeline.
- **AWS** is building spec-driven development into its agent tooling. That puts intent and acceptance criteria up front, before any code exists.
- **Google** is pushing asynchronous agents that come back with completed tasks, which shifts the whole problem onto verification.
- **Cursor** started in the editor and has been moving toward review. Bugbot was the first step, and buying Graphite, a stacked-PR and code review tool, made the direction clear.

The second-order effect: **the money moves from seats to gates.** If a company runs 50 agents per engineer, per-seat pricing stops making sense. The scarce, billable thing becomes each verified merge, each policy check, each safe rollout. Whoever owns the gate where changes get approved controls both the audit log and the bill.

### The bear case

The honest counterargument is that "governance layer" might just be the new name for the ticket queue: more dashboards, more approvals, more process. Aviator's approach worked for a disciplined team of nine. It is unclear whether intent documents survive a 2,000-person organization where nobody writes acceptance criteria today.

A second bear case: verification may get good enough that the review bottleneck disappears before the platforms finish building around it. That would leave them with expensive orchestration layers nobody needs.

I don't buy the second one. Formal verification has been "almost ready" for 40 years. Meanwhile, liability keeps landing on the human who clicked approve. If Together AI won't let agents deploy GPU kernels on their own, your bank won't let them deploy its payment code on its own either.

### What to Watch

1. **Platforms will cap PR size by default.** By the end of 2027, expect at least one major platform to warn about or block agent PRs over a set line count unless they include a structured intent or spec file. The 400-line research finding becomes a product rule.
2. **Revert rate becomes the headline metric.** Engineering leaders will report reverts and change failure rate, not "PRs per engineer." Vendors selling AI code generation will be forced to publish revert numbers, and many will look bad.
3. **Feature flag and rollout tools get acquired.** Release control is the last line of defense, and every platform that wants to own the agent loop needs rollback. Expect an acquisition in that space within 18 months.
4. **The CircleCI gap widens.** Next year's data will show the top-quartile versus bottom-quartile gap growing, not shrinking. The difference won't be model choice. It will be whether a team rebuilt its review process.
5. **"Agent fleet" pricing replaces per-seat pricing** at at least two of the five companies above by mid-2027.

Cheap code was the easy part. The companies that win the next round will be the ones that make approving a change cheap without making it careless.