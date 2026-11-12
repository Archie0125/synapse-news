---
category: developer-tools
faqs:
- answer: LinkedIn replaced its Argo CD-based deployment layer with a custom GitOps
    engine serving more than 4,000 services across over 250 Kubernetes clusters. The
    platform manages more than 100,000 deployments per week.
  question: What did LinkedIn replace, and at what scale?
- answer: LinkedIn encountered ambiguous deployment status, stale repository-cache
    results, resource-watch contention, and field-ownership limitations in server-side
    apply. These issues became material on clusters containing tens of thousands of
    pods.
  question: Why was Argo CD creating problems for LinkedIn?
- answer: No. LinkedIn’s decision reflects an unusually large operating scale and
    specialized deployment architecture; most organizations should first determine
    whether their actual reliability problems justify owning a custom control plane.
  question: Does this mean other companies should replace Argo CD?
featured: false
lang: en
publishedAt: '2026-11-12T09:00:00+00:00'
relatedSlugs: []
sources:
- name: InfoQ
  url: https://www.infoq.com/news/2026/11/kubernetes-argocd-linkedin/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
summary: LinkedIn’s Argo CD replacement is less an open-source rejection than proof
  that hyperscale eventually makes deployment semantics worth owning.
tags:
- developer-tools
- open-source
- industry
title: LinkedIn Replaces Argo CD with a Custom GitOps Engine for Kubernetes Deployments
trending: false
type: news
---

In a recent [post](https://www.linkedin.com/blog/engineering/infrastructure/how-we-scale-deployments-with-a-custom-gitops-engine), LinkedIn revealed it has replaced [Argo CD](https://argo-cd.readthedocs.io/en/stable/) with its own [GitOps](https://about.gitlab.com/topics/gitops/) engine. This new system deploys applications across over 250 Kubernetes clusters. It supports more than 4,000 services and manages over 100,000 deployments each week. According to a post, deployment infrastructure failures fell from 925 to 63 despite a 3.7x increase in deployment volume. The median time to detect and conclude a failed deployment dropped from 16.1 to 2.45 minutes.

LinkedIn started with one Argo CD instance per cluster, a topology it chose because Argo CD already managed its cluster add-ons that way. Clusters run up to 5,000 nodes each. A central deployment orchestrator spawned an ephemeral pod per deployment, with Argo CD hidden behind it. The team lists seven problems that emerged at scale. Argo CD doesn't have an `observedGeneration`, so you can't link sync and health status to a specific deployment. LinkedIn created a Lua health check that uses a tracking annotation to address this. A Synced and Healthy application could also resolve to an unintended revision when stale repo-server cache entries were used.

Two of the issues were architectural. Argo CD maintains one watch per group-version-resource across Applications. LinkedIn’s clusters have low resource-type diversity. This means etcd churn from one app can slow syncs for all apps. In one test, sync took under 3 minutes on a cluster with 60,000 pods and over 10 minutes with more than 80,000. The second was server-side-apply PATCH. Kubernetes truncates managedFields once an object has had more than 10 distinct field managers, and the API server then forgets who owns a field. In LinkedIn's AI workloads, which run multiple containers per Pod, a container removed from a manifest could therefore survive on the live Pod. The team had pruning disabled because destructive operations in production require approval. The remaining problems were CRD schema changes that required controller restarts across the fleet. Some OutOfSync states did not reflect real drift. Error messages were buried in boilerplate.

LinkedIn evaluated [Flux](https://fluxcd.io) but found it shared the same controller paradigm, so it built the engine as a library. Each deployment runs in its pod, with no shared controller state. Updates use PUT for full replacements, not PATCH. They retry on `resourceVersion` conflicts with exponential backoff. A 3-way diff across the live object, the previously deployed manifest, and the newly rendered manifest detects drift, and genuine drift fails the deployment. The same pod then watches the object's status until it converges or times out, and the API server unwraps errors for the user. Objects missing from the rendered manifest become deletion candidates, subject to delete protection, and convergence logic for LinkedIn's CRDs is built in.


The comparison uses the same calendar month a year apart. The migration ran from July 2025 to April 2026, which makes May 2026 the first clean post-migration month. The infra failure count covers only failures caused by the deployment system and excludes drift errors, since the two systems define drift differently. LinkedIn states that the improvement isn't solely due to the new engine. The orchestrator's error classification and reliability also got better during this time. The median duration for successful deployments is similar for both systems. However, the mean and tail have improved. The team attributes this to a namespace-scoped informer cache.

The engine is internal, and no open-source release is mentioned. Argo CD remains in use at LinkedIn for cluster add-ons and system services. The team had also found that maintaining 200+ Argo CD instances made each upgrade a multi-week project.

Teams running Argo CD at scale can check two things without a rewrite. Count the field managers on long-lived objects, since managedFields truncation can leave orphaned containers that produce no error. Then check whether sync latency tracks total pod count on shared clusters, which points to watch contention. LinkedIn concludes that the build-or-extend decision relies on the operational model. They say that per-deployment isolation, not controller tuning, allows the system to scale with compute.

LinkedIn is not the only large operator to build deployment logic around Kubernetes rather than adopt a general-purpose GitOps controller. Uber’s [Up platform](https://www.uber.com/us/en/blog/evolving-ubers-compute-platform/) assigns each deployment to a dedicated controller. This is the Uber Deployment Controller. It translates the intent into Kubernetes primitives and sends status updates. This helps the workflow move forward. Uber keeps a long-running controller, while LinkedIn runs one ephemeral pod per deployment with no shared controller state.

Airbnb went further back and built its own tooling years earlier. In a talk at [QCon London 2019 on InfoQ](https://www.infoq.com/presentations/airbnb-kubernetes-services/), infrastructure engineer Melanie Cebula introduced kube-gen. This internal framework creates Kubernetes configuration from one versioned project file. It also includes a deploy tool that applies or replaces objects and restarts pods, so changes take effect right away. Airbnb's deploy tool also returns an atomic success or failure, and a container that restarts for 30 seconds at the start of a rollout counts as a failed deploy. Airbnb was then at roughly 125,000 production deploys a year.

## Summary

**TLDR:** LinkedIn’s Argo CD replacement is less an open-source rejection than proof that hyperscale eventually makes deployment semantics worth owning.

- LinkedIn’s custom GitOps engine manages more than 4,000 services, 250 Kubernetes clusters, and 100,000 weekly deployments.
- Infrastructure-related deployment failures fell from 925 to 63 even as deployment volume increased 3.7 times.
- Median time to detect and conclude a failed deployment dropped from 16.1 minutes to 2.45 minutes.
- At LinkedIn’s scale, Argo CD’s status semantics, stale caches, shared resource watches, and server-side apply behavior created correctness or performance risks.
- The lesson is not that Argo CD is inadequate generally, but that infrastructure economics change when clusters reach tens of thousands of pods.

## 摘要

**重點摘要：** LinkedIn 換掉 Argo CD 並非否定開源，而是證明規模大到極致後，部署語意本身就值得自行掌控。

- LinkedIn 的自製 GitOps 引擎服務逾 4,000 個服務、250 多個 Kubernetes 叢集，每週處理超過 10 萬次部署。
- 部署量成長至 3.7 倍之際，基礎設施造成的部署失敗仍從 925 次降至 63 次。
- 判定部署失敗所需的中位時間由 16.1 分鐘縮短到 2.45 分鐘。
- 當規模放大後，Argo CD 的狀態對應、快取過期、資源監看機制與 server-side apply 都可能影響正確性或效能。
- 這不是 Argo CD 不堪使用，而是超大型平台對部署可驗證性與故障隔離有截然不同的要求。