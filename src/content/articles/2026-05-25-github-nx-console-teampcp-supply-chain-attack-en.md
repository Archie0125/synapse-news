---
title: "How a Poisoned VS Code Extension Breached GitHub and Hit OpenAI, Grafana, and Mistral"
summary: "A 18-minute window was all threat group TeamPCP needed. A malicious version of Nx Console 18.95.0 compromised a GitHub employee's device and exfiltrated approximately 3,800 internal repositories. Confirmed downstream victims include OpenAI, Grafana Labs, and Mistral AI—all traced to a TanStack npm supply chain compromise two weeks prior."
category: "developer-tools"
publishedAt: 2026-05-25
lang: "en"
featured: true
trending: false
sources:
  - name: "The Hacker News"
    url: "https://thehackernews.com/2026/05/github-internal-repositories-breached.html"
  - name: "Help Net Security"
    url: "https://www.helpnetsecurity.com/2026/05/20/github-breached-teampcp/"
  - name: "OX Security"
    url: "https://www.ox.security/blog/teampcp-strikes-again-how-a-trojan-vs-code-extension-brought-down-github/"
  - name: "StepSecurity"
    url: "https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/316978/20260521/github-ciso-names-nx-console-root-3800-repo-breach-openai-grafana-also-hit.htm"
tags:
  - "security"
  - "supply-chain"
  - "vscode"
  - "github"
  - "developer-tools"
  - "teampcp"
  - "nx-console"
  - "malware"
relatedSlugs:
  - "2026-05-17-pwn2own-berlin-2026-ai-platforms-zero-days-en"
  - "2026-05-13-red-hat-summit-agentic-ai-developer-tools-en"
  - "2026-05-16-gitlab-agentic-era-restructuring-en"
---

On the morning of May 18, 2026, a version number change in one of the most popular VS Code extensions set off a supply chain incident that will define developer security conversations for years. Nx Console version 18.95.0 was live on the Visual Studio Marketplace for just 18 minutes before Microsoft's security team pulled it. For TeamPCP, the threat group that orchestrated the operation, 18 minutes was enough.

By the time version 18.95.0 was removed, the damage was done. GitHub—itself a subsidiary of Microsoft—disclosed on May 19 that approximately 3,800 of its internal source code repositories had been exfiltrated. In the days that followed, confirmed downstream victims expanded to include OpenAI, Grafana Labs, and Mistral AI.

## The Anatomy of a Multi-Stage Attack

Understanding how TeamPCP pulled this off requires rewinding to May 11, two weeks before the extension was published. That day, the group executed a supply chain compromise of 42 TanStack npm packages, injecting a credential-stealing JavaScript payload into 84 malicious versions spread across the npm registry.

TanStack is a widely used collection of open-source JavaScript utilities—libraries like TanStack Query, TanStack Router, and TanStack Form appear in tens of thousands of production codebases. The poisoned packages were designed with one objective: harvest GitHub credentials stored or accessed through the GitHub CLI (gh). Among the tens of thousands of developers affected by that initial compromise was a legitimate contributor to the Nx Console project.

With those credentials in hand, TeamPCP moved to the second phase. Posing as a legitimate Nx Console maintainer, the attacker pushed a malicious orphan commit—one hidden inside the official nrwl/nx GitHub repository, invisible in standard branch navigation—that embedded a 498 KB obfuscated payload. That commit served as the remote payload host. On May 18, the attacker published version 18.95.0 to the Visual Studio Marketplace.

## The Payload: Silent, Redundant, and Comprehensive

The malicious extension triggered on workspace open. Within seconds of a developer opening any project, it silently fetched and executed the obfuscated payload from the hidden orphan commit. The payload was a multi-stage credential stealer and supply chain poisoning tool targeting tokens and secrets from:

- **GitHub** (personal access tokens, SSH keys)
- **npm** (publish credentials and .npmrc tokens)
- **AWS** (access keys and session tokens)
- **HashiCorp Vault** (operator tokens)
- **Kubernetes** (service account keys, kubeconfig entries)
- **1Password** (vault unlock credentials)
- **AI coding assistants** (API keys for Copilot, Cursor, and Claude)

Exfiltration happened over three independent channels: HTTPS to an attacker-controlled endpoint, the GitHub API for secrets disguised as repository activity, and DNS tunneling as a fallback. This three-channel redundancy made detection and blocking significantly harder for perimeter-based security controls.

Nx Console had over 2.2 million installs before the incident. Despite the extension being available for only 18 minutes on the Visual Studio Marketplace (and 36 minutes on OpenVSX, where the malicious version was caught later), the Nx Console development team estimates the malicious build may have reached over 6,000 developers, many of whom had auto-update enabled.

## GitHub's Internal Breach

GitHub disclosed the incident publicly on May 19, confirming that an employee's device was compromised by the poisoned extension, and that the resulting access was used to exfiltrate approximately 3,800 internal repositories. GitHub's CISO confirmed that Nx Console was the root cause. The company characterized the 3,800 figure as "directionally consistent" with its ongoing investigation.

The repositories included internal tooling, configuration management code, and infrastructure automation scripts. GitHub emphasized that the breach did not affect the public GitHub platform or customer repositories directly—but the downstream implications were significant. Any secrets or API keys embedded in those internal repositories could provide access to systems far beyond GitHub itself.

Confirmed downstream victims illustrate the cascading nature of modern supply chain attacks. Developers at OpenAI, Grafana Labs, and Mistral AI who ran VS Code with auto-update enabled received the malicious build during the 18-minute window. The secrets on those machines—credentials to AI training infrastructure, observability platforms, cloud providers—were potentially exposed to the same exfiltration pipeline.

## TeamPCP's Fingerprints

The threat group publicly claimed responsibility through posts on a dark web forum, framing the attack as a demonstration of "the inherent fragility of the modern developer supply chain." Security researchers at OX Security, which published one of the earliest technical analyses, identified multiple previous TeamPCP campaigns targeting developer tooling, noting the group's preference for patience: they often wait weeks between initial credential theft and exploitation. The gap between the TanStack compromise on May 11 and the Nx Console publish on May 18 fits that pattern precisely.

StepSecurity, which issued an independent advisory for the Nx Console compromise, noted that this attack represents an evolution in developer-targeting tactics. Previous supply chain attacks have typically focused on injecting malicious code into libraries used in production deployments. This attack instead targeted the development environment itself—VS Code extensions running with developer-level privileges on machines that hold credentials for every system those developers can reach.

## The Fix and the Fallout

Nx Console published version 18.95.1 on May 18, immediately after the malicious version was removed. The team issued security guidance urging all developers to rotate credentials, audit their machines for signs of compromise, and review any recent deployments or CI/CD pipeline outputs for anomalous activity.

Microsoft announced plans to implement real-time behavioral analysis for VS Code Marketplace extension updates—a capability that would have caught the malicious payload before distribution. The Marketplace had previously relied primarily on static analysis and publisher reputation signals, a posture that proved inadequate against a compromised legitimate maintainer account.

For organizations, the incident raises hard questions about developer endpoint security. The credentials harvested by TeamPCP—AWS tokens, Kubernetes service account keys, CI/CD secrets—are precisely the credentials that enable attackers to pivot from a compromised developer laptop to production infrastructure. Endpoint detection and response coverage for developer machines, which many organizations historically treated as lower-priority than production servers, has emerged as an urgent remediation target.

## A Systemic Risk the Industry Has Long Ignored

The Nx Console incident follows a pattern that security researchers have been warning about for years: the attack surface created by the modern developer toolchain is enormous and consistently underestimated. Developers run VS Code with dozens of extensions, npm global packages, GitHub Actions workflows, and CLI tools—each representing a trust boundary that, if compromised, provides access not to one system but to every system that developer can reach.

The fact that a 2.2-million-install extension could be compromised and weaponized, have a malicious version published, and breach GitHub's internal codebase in a window of 18 minutes serves as a stark demonstration of how quickly supply chain attacks can move once the initial foothold is established.

GitHub has not commented on whether any of the stolen repository contents have been observed in the wild. For enterprises still assessing their exposure, that silence offers little comfort.
