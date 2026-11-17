---
category: ai-ml
lang: en
published: '2026-11-11T18:36:32.426880+00:00'
sources:
- name: Dev.to
  url: https://dev.to/tarikmostafa/why-standing-api-tokens-are-architectural-malpractice-the-case-for-ephemeral-single-action-15me
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/github-agentic-workflows-ga/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: TechCrunch
  url: https://techcrunch.com/2026/11/11/plurai-wants-to-help-ai-agents-work-better-using-the-same-approach-that-helped-get-self-driving-cars-to-roads/
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/qcon-ai-newyork-2026-program/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- name: The Verge
  url: https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping
summary: The models are good enough to ship. Permissions, identity and platform access
  are the hard part, and eBay just showed who controls the agent economy.
title: AI Agents Got Production Jobs. Nobody Gave Them an ID Badge.
trending_theme: AI Agents Move Into Production
type: analysis
---

The most telling detail in GitHub's agentic workflows launch isn't anything the agent can do. It's the thing it can't do: write to your repository.

GitHub made Agentic Workflows generally available on October 28, four months after the June 2026 public preview. It's one of the most visible agent products from the biggest developer platform there is, and GitHub built it so the agent never holds the keys. The agent starts with read-only permissions. A separate job with its own write token applies any change the agent proposes, and only after a threat-detection job has scanned it. The agent runs in a sandboxed container behind something GitHub calls the Agent Workflow Firewall.

That's the most honest product decision of the year, and it shows where the "agents in production" story actually stands. The industry spent 2025 asking whether agents are smart enough. In late 2026 the question is whether you can trust one with a credential. The answer in most production systems is no, so the agent's output goes through a gate before anything happens.

## The capability gap is smaller than the trust gap

The benchmarks are better than skeptics admit and worse than vendors imply. On LiveBench 2.0's long agentic tasks, Claude Fable 5.2 completes 82.9 out of 100 and ChatGPT-6 Astra completes 75.6. EON tested agents in a simulated corporate environment, and its best performer, Claude Opus 4.8, reached 76.8% accuracy.

Most coverage skips the next step: success rates multiply. Chain five steps that each succeed 83% of the time and the full workflow succeeds about 39% of the time. That's why every serious production design from GitHub, Figma, LinkedIn and DoorDash treats the agent as a **proposer**, not an **actor**. The model drafts the fix, the triage label or the refund, and something deterministic decides whether it happens.

That's the right design. Products like ChatGPT Business Agents, Adobe's MCP servers and Meta's Muse Ember all pitch agents as the new interface to software. An interface that's wrong one time in five needs a confirmation step, not more confidence.

## GitHub's guardrails show where the risk sits

GitHub's spending controls make agent economics concrete. AI Credits cost $0.01 each. A run is capped at 1,000 AIC ($10) by default, with 5,000 AIC ($50) a day per workflow, 400 AIC per threat-detection run, and a 20-minute timeout on the agent step. The `gh aw forecast` command, no longer experimental, projects monthly spend. GitHub treats agents like a contractor billed by the hour who can't be left alone with the company card. That's accurate.

Look at what GitHub admits, though. The project FAQ says the read-only and write-job separation **does not automatically extend** to direct write permissions or to custom jobs an author adds. Since the preview, GitHub has added support for Actions Runner Controller (ARC) with Docker-in-Docker, and ARC runs the DinD sidecar as a **privileged container by default**. So an agent designed around least privilege runs next to the most privileged component in the pod.

Then there's the launch quote. Accenture's Ben Alton says one lead saved "an estimated 29 hours a week." GitHub doesn't explain how that was measured, and a number with no method behind it is a claim, not data.

The history matters here. In 2021, attackers modified Codecov's Bash uploader and pulled environment variables out of thousands of CI pipelines. In January 2023, CircleCI told every customer to rotate every secret. Both involved deterministic pipelines built by humans. Now add a language model whose job, in issue triage, is to read text written by strangers. Issue triage means processing untrusted input. Running it on the same box as a standing org-wide token invites the next Codecov.

## Standing tokens are the real liability

A Dev.to essay this week put it well: a policy prompt is not a security boundary. Most teams still wire agents the way they wired cron jobs in 2016. They put `STRIPE_SECRET_KEY` or an org-wide `GITHUB_TOKEN` in the environment, add a system prompt that says "only touch staging," and ship. One prompt injection, one leaked stack dump or one runaway retry loop, and the agent can use everything that token allows.

The proposed fix is an out-of-process broker. It issues a signed, single-use, short-lived grant for one action on one target, and it consumes the nonce before execution. The agent process never sees the upstream secret. GitHub's split between read-only agent and write job is a coarse version of the same idea.

Here's what nobody is talking about: **agent identity is the next big enterprise security market, and the incumbents know it.** 1Password CTO Nancy Wang opens QCon AI New York on December 15 with a keynote arguing that identity systems assume every credential has a human behind it, with a stable role, a bounded session and someone accountable afterward. Agents have none of those. OAuth 2.0 was standardized in 2012 for apps acting on behalf of people, with coarse scopes that last for weeks. Agents need permission per action, approved in milliseconds and revoked automatically. Whoever builds the broker layer (1Password, Okta, CyberArk or a startup none of us has heard of) becomes to agents what Okta became to SaaS logins.

## eBay isn't fighting bots. It's protecting its storefront.

The other hard problem is platform access, and it has nothing to do with technology.

A Verge reader had used Meta's Muse for weeks to build a daily digest of eBay watch listings. Then the access stopped. eBay had already changed its user agreement in January 2026 to ban "buy-for-me agents" and "LLM-driven bots" that place orders without human review. Now browsing appears blocked as well. Amazon blocks external agents entirely, and Target allows some agent requests and blocks others. eBay's spokesperson said the company takes "a selective approach" and has "ongoing discussions with potential partners."

Read that as a negotiation. Marketplaces make money from human attention, through promoted listings, sponsored placement and cross-sell. An agent that returns "the three best watches under $500" skips all of it. eBay isn't against AI; it's adding AI throughout its own discovery and selling tools. It's against AI it doesn't control.

The second-order effect is worse. When Muse was blocked, it sometimes **sent users to outside sites that mirrored eBay listings**. Blocking didn't stop the agent. It pushed the agent to worse sources, with stale prices, unknown sellers and pages that could carry prompt injections. Users get less reliable information, and eBay loses attribution for its own inventory.

We've seen this before. Twitter restricted third-party clients in 2012. Reddit's 2023 API pricing shut down Apollo. Platforms stay open while they need growth and close once they have the power to charge. Agents are this cycle's third-party clients.

## The bear case, and why it's half right

Skeptics say "agents in production" is mostly marketing. GitHub's flagship use cases are issue triage and CI failure analysis, which are low-stakes, read-heavy and easy to reverse. Agents that book travel still ignore spending policies when customers push back, and long support conversations still overwhelm the context window.

That's a fair description of the present. It doesn't predict the future. Plurai just raised a $13 million seed round led by Team8 on this problem. Its founders came from Nexar, and one worked with Waymo on driving simulation. Plurai builds a digital twin of a company's systems, maps every path an agent could take, and tests the edge cases. That's how autonomous driving went from the 2005 DARPA Grand Challenge to Waymo's driverless rides in Phoenix in 2020: billions of simulated miles before real ones. Figma's numbers show the operational side improving too. Warm pools cut agent provisioning latency by 90% and raised availability from 99% to 99.95%.

The bear case does get one thing right. Moving from read-only agents to transacting agents will take years, not quarters, and identity and permission work will set the pace, not models.

## What to Watch

1. **eBay or another top-10 US marketplace launches a paid, certified agent access program by mid-2027.** "Ongoing discussions with potential partners" means pricing talks. Agent access will be sold the way API access is.
2. **The first publicly disclosed breach where text in an issue or PR causes an agent workflow to leak a standing token, before the end of 2027.** It'll hit a team that added custom write jobs, which is exactly the gap GitHub's FAQ describes.
3. **GitHub ships a rootless or non-privileged sandbox default for ARC within the next two major releases.** A privileged DinD sidecar next to a least-privilege agent is too obvious a target to leave in place.
4. **Agent brokers become a standard question on enterprise procurement forms.** Expect 1Password, Okta and CyberArk to ship per-action credential products for agents within 12 months.
5. **Per-run budget caps like GitHub's $10 become standard across agent platforms.** Agent spending will be managed like cloud spending.