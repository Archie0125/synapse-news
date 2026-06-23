---
title: "Microsoft Claims 1,000x Qubit Reliability Breakthrough With Majorana 2 — Scientists Remain Skeptical"
summary: "Microsoft unveiled Majorana 2 at Build 2026, claiming a 1,000-fold improvement in qubit stability over its predecessor and a mean qubit lifetime of 20 seconds. The announcement accelerates the company's quantum computing roadmap to 2029, but physicists argue the demonstration is incomplete and that the existence of Majorana particles in the devices remains unproven."
category: "hardware"
publishedAt: 2026-06-08
lang: "en"
featured: true
trending: true
sources:
  - name: "Microsoft"
    url: "https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/"
  - name: "SiliconANGLE"
    url: "https://siliconangle.com/2026/06/02/microsofts-new-majorana-2-quantum-chip-claims-dramatic-breakthrough-qubit-stability/"
  - name: "Science News"
    url: "https://www.sciencenews.org/article/microsoft-quantum-chip-upgrade-majorana"
  - name: "Scientific American"
    url: "https://www.scientificamerican.com/article/microsofts-upgraded-majorana-quantum-computing-chip-fizzles-with-physicists/"
  - name: "TechTimes"
    url: "https://www.techtimes.com/articles/317648/20260602/majorana-2-quantum-chip-revealed-microsoft-build-2026-features-specs-explained.htm"
tags:
  - "quantum-computing"
  - "microsoft"
  - "majorana"
  - "topological-qubits"
  - "microsoft-build-2026"
  - "hardware"
  - "azure-quantum"
relatedSlugs:
  - "2026-06-08-apple-wwdc-2026-keynote-siri-gemini-ios27-en"
  - "2026-06-08-microsoft-ai-independence-mustafa-suleyman-mai-en"
---

Quantum computing has a credibility problem. A field that has promised transformational hardware for two decades has produced a string of impressive announcements that rarely survive close scrutiny from independent physicists. When Microsoft took the stage at Build 2026 in San Francisco on June 2 to unveil Majorana 2—its second-generation topological quantum chip—it brought both the most compelling qubit performance numbers the company has ever published and a familiar cloud of scientific skepticism.

The headline claim is dramatic: Majorana 2 achieves qubit stability 1,000 times greater than its predecessor, with a mean qubit lifetime of 20 seconds and instances recorded at nearly one minute. That compares favorably with Majorana 1's five-to-ten-second range and represents a meaningful advance in the physics of quantum coherence. Microsoft also says the chip brings its timeline to a commercially viable, scalable quantum computer forward to 2029—cutting its previous projection by roughly half.

## What Topological Qubits Are Supposed to Do

To understand why Microsoft's Majorana approach is both theoretically compelling and empirically contested, it helps to understand what makes qubits hard to keep alive in the first place.

Conventional qubits—whether superconducting rings, trapped ions, or photons—store quantum information in physical states that are exquisitely sensitive to environmental interference. A single photon from a nearby electronic device, a stray vibration, or a minor temperature fluctuation can collapse a quantum state instantly. The entire field of quantum error correction exists to work around this fragility, and it imposes enormous overhead: depending on the error rate, thousands of physical qubits may be needed to maintain a single reliable logical qubit.

Microsoft's approach, based on theoretical work by physicist Alexei Kitaev, proposes a different architecture. Topological qubits store information not in a single physical location but distributed across exotic quasiparticles called Majorana fermions. The key insight is that quantum information encoded in parity—the evenness or oddness of electrons in a wire—is inherently less sensitive to local disturbances. You would need to disturb the entire wire simultaneously to corrupt the encoded state, rather than disturbing a single particle.

This "hardware-protected" approach, if it works, would reduce the overhead for error correction dramatically and potentially allow a smaller number of physical qubits to achieve the error rates needed for practical computation.

## The Materials Upgrade Behind the Numbers

Majorana 2's performance improvement relative to its predecessor stems primarily from a change in the superconducting material used in the device. The first generation used aluminum superconductors; Majorana 2 switches to lead. Lead's properties appear to provide better shielding against the external disturbances that cause qubit decoherence, and Microsoft's engineers worked with an agentic AI system called Microsoft Discovery to optimize the materials stack systematically.

The role of AI in the chip's development is itself notable. Microsoft Discovery's agents automated complex measurements that previously took weeks, analyzed nearly two decades of fabrication data across multiple formats, and identified calibration issues in raw process data that human researchers had missed. "The agents can really accelerate things as much or as little as you want," said Chetan Nayak, Microsoft's head of quantum hardware. "It can be as little as pulling information together and summarizing it, or it can go further down the road of synthesizing it more or generating an interesting hypothesis."

Qubit dimensions remain extremely small—on the order of one hundredth of a millimeter—and operational speeds have been reduced to microseconds. Both characteristics matter for eventual integration into larger quantum processors.

## Where the Science Gets Complicated

Microsoft's claims met a familiar response from the physics community: cautious skepticism rooted in a field with a troubled history.

Physicist Henry Legg of the University of St Andrews was direct in his assessment. "Nothing in this preprint resolves the fundamental issues" with topological quantum computing, he said, pointing to a critical methodological gap in Microsoft's published data. Demonstrating a functional qubit requires two types of measurements—X and Z—but the new research presents only Z measurements. "Nothing in the presented data proves the existence of a topological qubit or Majoranas in these devices," Legg wrote.

The core scientific question is whether Microsoft has actually created Majorana fermions—the exotic particles the entire approach depends on. Many physicists in the field remain unconvinced that the company has produced the real thing rather than mimicking Majorana-like signatures with conventional physics. The field has seen multiple high-profile retractions, including a 2021 Nature paper by Microsoft that was withdrawn after reviewers concluded its data did not support its claims. That history makes independent verification of any new Majorana claim particularly important.

Microsoft has not yet submitted the Majorana 2 results to peer review.

## The Stakes for Microsoft's Quantum Strategy

For Microsoft, Majorana 2 represents an unusually long bet. The company has been working on topological quantum computing since at least 2012, an investment measured in the hundreds of millions of dollars and the careers of some of the world's best condensed matter physicists. Unlike IBM and Google, which have pursued superconducting qubit approaches that have produced increasingly capable (if error-prone) quantum processors, Microsoft placed its bet on an approach that requires first proving the existence of a new type of quasiparticle.

If Majorana 2's performance numbers are validated by independent researchers and the 2029 timeline for a commercially viable machine holds, Microsoft would have a structural advantage in quantum hardware: fewer physical qubits required, inherently lower error rates, and a platform that scales more gracefully than competing architectures. The addressable use cases—drug discovery, materials design, financial optimization, cryptographic applications—represent trillions of dollars in potential economic value.

If the fundamental physics doesn't hold up under scrutiny, Microsoft faces the prospect of having invested more than a decade in an approach that competes on the wrong terrain.

Constellation Research analyst Holger Mueller called Majorana 2 "a massive step forward," while acknowledging that independent verification remains the appropriate next step. The announcement is, at minimum, the most credible quantum hardware claim Microsoft has made. Whether it is the breakthrough the company insists it is will depend not on what Microsoft says at Build 2026, but on what happens when physicists outside Redmond examine the devices themselves.

Azure Quantum, Microsoft's cloud quantum platform, is expected to incorporate Majorana 2-based hardware in future commercial offerings, with roadmap details to be shared before the 2029 target date.
