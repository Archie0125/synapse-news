# Kubernetes


*Mentioned in 3 articles*


## Recent Mentions


- **Kubernetes - Setup External DNS** (2026-11-10)
  - Running External DNS with Flux and SOPS on a home cluster is overkill, and that is exactly why it's good practice: it is the same setup production clusters use.

- **Podcast: Distributed LLM Inference on Kubernetes with llm-d, Wasm, & TornadoVM** (2026-11-09)
  - The interesting point in this episode is that Kubernetes' default load balancing actively wastes GPUs for LLMs, and llm-d exists to fix that.

- **Why Kubernetes 1.35 resizePolicy: RestartContainer Isn't Required for ZGC/Shenandoah** (2026-11-08)
  - The 'always restart JVMs on memory resize' advice is only a third right; a real experiment shows ZGC and Shenandoah can shrink in place if you release memory first.