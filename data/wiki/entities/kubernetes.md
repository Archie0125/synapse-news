# Kubernetes


*Mentioned in 5 articles*


## Recent Mentions


- **Podcast: Distributed LLM Inference on Kubernetes with llm-d, Wasm, & TornadoVM** (2026-11-09)
  - The interesting point in this episode is that Kubernetes' default load balancing actively wastes GPUs for LLMs, and llm-d exists to fix that.

- **Why Kubernetes 1.35 resizePolicy: RestartContainer Isn't Required for ZGC/Shenandoah** (2026-11-08)
  - The 'always restart JVMs on memory resize' advice is only a third right; a real experiment shows ZGC and Shenandoah can shrink in place if you release memory first.

- **AI agents are getting more complex. Developers shouldn’t have to babysit them.** (2026-11-06)
  - Harness engineering is the right idea, but promising agents that check their own work just moves the babysitting job from code to test suites.

- **Groundcover automates Kubernetes sizing. Engineers set the bounds.** (2026-11-05)
  - Groundcover is betting that Kubernetes right-sizing should be a continuous feedback loop rather than a quarterly cleanup, and keeping engineers in charge of the limits is what makes it credible.

- **Building a Culture for a Kubernetes-Based Platform in a Bank** (2026-11-05)
  - A bank learned that installing Kubernetes is easy and running it is a people problem, and that open source earns trust through uptime, not slide decks.