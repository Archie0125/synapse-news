---
category: ai-ml
faqs:
- answer: Google DeepMind used an agentic AI framework called AlphaProof Code to formally
    verify several of the Signal protocol's key cryptographic guarantees. The proof-of-concept
    project took about four weeks.
  question: What did Google DeepMind prove about the Signal protocol?
- answer: Formal verification uses math to prove that software behaves as intended,
    but building proofs by hand has historically been extremely time-consuming. DeepMind's
    work suggests AI can greatly speed up proof construction, which could make mathematically
    checked security more practical.
  question: Why does AI-assisted formal verification matter?
- answer: The analysis covered specific protocol guarantees, not the entire Signal
    mobile app or its implementation. Researchers say it is still unclear how well
    AI-aided formal verification will scale to large codebases.
  question: What are the limits of DeepMind's Signal verification?
featured: false
lang: en
publishedAt: '2026-11-10T05:01:00+00:00'
relatedSlugs: []
sources:
- name: Wired
  url: https://www.wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol/
summary: DeepMind's AI-verified Signal proof is real progress in four weeks, but proving
  a protocol isn't the same as proving the app on your phone.
tags:
- ai-ml
- cybersecurity
- open-source
title: A New AI Tool From Google DeepMind Proved the Signal Protocol Is Secure
trending: false
type: news
---

Google DeepMind researchers used [agentic AI](https://www.wired.com/story/ai-agents-are-about-to-flood-the-workforce-no-ones-ready-for-it/) to mathematically prove, or “formally verify,” a number of the [Signal protocol’s](https://www.wired.com/story/signal-encryption-protocol-hacker-lexicon/) key cryptographic guarantees—a landmark development for the widely used cryptography and AI itself.

Conducted as a sort of proof-of-concept project in just four weeks, the work is significant in two ways. It serves as further independent validation of the cryptography that protects massive quantities of the world's communications on platforms like the [Signal app](https://www.wired.com/story/signal-tips-private-messaging-encryption/), Google Messages, and WhatsApp. And it demonstrates Google DeepMind's formal verification capabilities using a new AI framework called AlphaProof Code.

More broadly, AI-aided formal verification is having a moment, but it is [unclear how practical it will be](https://www.wired.com/story/software-verification-is-the-hot-new-answer-to-the-ai-safety-crisis/) for widespread use and how effective it can be at securing large amounts of code. Proponents of formal verification have long referred to it as a sort of holy grail in software security, because it uses math to check and validate that software is functioning as intended—in other words, that it doesn't have critical vulnerabilities.

Before the AI era, it was incredibly time-consuming for people to describe the characteristics of software they wanted to prove, turn these summaries into formulas, and then develop the proof. Agentic AI can significantly cut down the time of the latter project, enabling analyses like DeepMind's Signal evaluation. But even this analysis was limited in scope—it did not, for example, formally verify the entire Signal mobile app—and DeepMind researchers emphasize that their findings are just one milestone in a larger process.

“We are very excited by this result, but there is a long distance to go before we are able to scale this to all the software of the world, and we want to do that,” Swarat Chaudhuri, a DeepMind research scientist, tells WIRED.

The DeepMind analysis did not find any new vulnerabilities in the portions of the Signal protocol it looked at, but when the researchers used AlphaProof Code on older versions of Signal that contain known and long-fixed vulnerabilities, it correctly identified them and showed that the protocol could not be formally verified. The researchers are releasing the specification and proof they developed for the Signal protocol analysis to aid other formal verification work.

While the speed of the project was notable, the DeepMind researchers point out that they were able to get a head start to a degree because of some past formal verification work that the [Signal Foundation](https://www.wired.com/story/big-interview-meredith-whittaker-signal-2024/) has conducted.

“While prior formal verification focused on smaller portions of the code, Google DeepMind's approach enables significant expansion,” Ehren Kret, Signal's chief technology officer, says in a statement. “As AI-driven security threats grow, rigorously verifying the Signal protocol implementation gives us even greater confidence in our code's privacy guarantees.”

For critical services used in high-stakes settings, it would be a dream to be able to formally verify every code base and entire software supply chains. “If you can now verify the correctness of these implementations, then you can rest easy,” says Pushmeet Kohli, chief scientist at Google Cloud and DeepMind's vice president of research. “You can imagine banks, imagine all those other companies who rely on assurances and who worry about bugs who could now say, ‘I can prove these properties.’"

The open question across the tech sector, though, is whether AI-automated formal verification can truly scale—and whether it can do so at a workable cost. DeepMind conducted the Signal analysis free of charge as a research project, and Google declined to share the cost of the analysis. The company also declined to comment on whether it has plans to release a commercial formal verification product or service.

The researchers say that some of their crucial advancements are in developing a “human-AI collaboration process,” as Chaudhuri puts it, that allows agents to contribute and self-correct at almost every phase of the process while still seeking human input and review at key junctures. “We don’t want this sort of vibe world where AI is generating the goals and AI is generating the proofs and basically taking tests that are self-written," Chaudhuri says. “There’s a middle ground.”

## Comments

Back to top

## Summary

**TLDR:** DeepMind's AI-verified Signal proof is real progress in four weeks, but proving a protocol isn't the same as proving the app on your phone.

- Google DeepMind used a new agentic AI framework, AlphaProof Code, to formally verify several key cryptographic guarantees of the Signal protocol.
- The proof-of-concept took just four weeks, which suggests AI can sharply cut the most labor-intensive part of formal verification: building the proofs.
- The Signal protocol protects messages on Signal, WhatsApp and Google Messages, so the result also serves as independent validation for billions of users.
- The scope was limited. It did not verify the full Signal mobile app, and humans still had to specify the properties being proved.
- It's unclear whether AI-assisted formal verification can scale to large, messy codebases, and that is the real test for the method.

## 摘要

**重點摘要：** DeepMind 用 AI 在四週內驗證 Signal 協定確實是實質進展，但證明協定安全，不等於證明你手機上的 App 安全。

- Google DeepMind 用全新的代理式 AI 框架 AlphaProof Code，對 Signal 協定的多項關鍵密碼學保證完成形式化驗證。
- 這個概念驗證只花四週，顯示 AI 能大幅壓縮形式化驗證中最耗人力的環節：建構證明。
- Signal 協定保護 Signal、WhatsApp 與 Google Messages 上的通訊，所以這次成果也等於替數十億用戶再做一次獨立驗證。
- 驗證範圍有限：它沒有驗證整個 Signal 行動 App，要證明哪些性質也仍需要人來定義。
- AI 輔助的形式化驗證能不能擴展到大型、雜亂的程式碼庫還是未知數，這才是這套方法真正的考驗。