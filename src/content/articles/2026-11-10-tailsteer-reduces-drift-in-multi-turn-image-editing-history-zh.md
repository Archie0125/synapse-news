---
category: ai-ml
faqs:
- answer: 兩者處理的都是「漂移」，也就是誤差在多次生成中不斷累積。TailSteer 降低連續 15 到 20 次影像編輯的漂移，History Forcing
    則讓 15 秒這類長時段影片生成更穩定。
  question: TailSteer 和 History Forcing 解決什麼問題？
- answer: TailSteer 只學習修正去噪後期，早期軌跡維持原樣，所以基礎模型原有的生成和編輯能力大多保得住。過去的做法常用多輪資料重新訓練，可能蓋掉預訓練學到的知識。
  question: 為什麼 TailSteer 只修正尾段很重要？
- answer: History Forcing 把 15 秒影片的 VBench 品質分數提升到 85.07，MemoBench 上鏡頭回到原場景時的物件一致性達到
    62.18。Evolution Quality 從 2.35 升到 2.70，代表畫面外的場景變化更合理。
  question: History Forcing 對影片生成提升了多少？
featured: false
lang: zh
publishedAt: '2026-11-10T06:00:00+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/olaughter/tailsteer-reduces-drift-in-multi-turn-image-editing-history-forcing-stabilizes-long-horizon-video-5eo6
summary: TailSteer 與 History Forcing 瞄準的是生成式 AI 真正的弱點：問題不在第一張圖，而在第十五次編輯、影片的第十五秒。
tags:
- ai-ml
title: TailSteer 抑制多輪圖像編輯的漂移問題，History Forcing 讓長時段影片生成更穩定
trending: false
type: news
---

Multi‑turn image editing and long‑horizon video rollouts still suffer from drift that compounds after just a handful of steps, making iterative creative tools brittle. TailSteer preserves the early denoising dynamics while History Forcing injects historic context, effectively halting that drift.

Earlier solutions either retrain on multi‑turn data—rewriting the pretrained priors—or rely on inference hacks that do not scale to large diffusion backbones. Those workarounds trade off fidelity for stability and often require hand‑crafted rollout pipelines.

TailSteer cuts cumulative drift across 15‑20 successive edits. It learns tail‑focused corrections from on‑policy rollouts, leaving the early denoising trajectory untouched; experiments across the FLUX, SenseNova, and Qwen families show a substantial reduction while largely preserving base‑model performance [\[1\]](https://arxiv.org/abs/2611.06741).

TailSteer maintains the generative and editing abilities of the original model. Its tail‑focused design “improves long‑horizon editing robustness while largely preserving the generative and editing capabilities acquired through earlier training,” even surpassing GPT‑Image‑2.5 Sunburst on all three preservation metrics, proving that long‑horizon stability can be unlocked without erasing prior knowledge [\[1\]](https://arxiv.org/abs/2611.06741).

History Forcing lifts the VBench quality of 15‑second video generation to 85.07. By feeding the residual between teacher predictions with and without informative history into the student’s distillation target, the method aligns the student to a corrected prediction that respects long‑range constraints.

Object consistency rises to 62.18 on MemoBench when the camera returns, while Evolution Quality improves from 2.35 to 2.70, demonstrating more plausible scene evolution during out‑of‑sight intervals; training overhead grows by only \~2 % in time and memory per step [\[2\]](https://arxiv.org/abs/2611.02782).

TailSteer has only been validated up to 20 edit turns, leaving behavior on longer sequences uncertain, and History Forcing depends on a teacher that retains visibility of the scene—a condition that may not hold for arbitrary content changes; together this suggests further research is needed to scale tail‑steering beyond dozens of edits and to generalize historical forcing without specialized teachers.

Future iterative video editors should replace naïve autoregressive rollouts with a History Forcing‑distilled student and fine‑tune diffusion backbones using TailSteer before exposing them to user‑driven edit sequences, ensuring stable 60‑second generation and consistent visual quality.

## Top comments (0)

## Summary

**TLDR:** TailSteer and History Forcing go after generative AI's real weakness, which isn't the first image but the fifteenth edit and the fifteenth second.

- TailSteer reports a substantial reduction in cumulative drift across 15 to 20 successive image edits. It learns corrections only for the tail of the denoising process from on-policy rollouts.
- Because the early denoising trajectory is left alone, base-model abilities are largely preserved. The paper says it beats GPT-Image-2.5 Sunburst on all three preservation metrics, tested on FLUX, SenseNova and Qwen models.
- History Forcing distills a student model toward teacher predictions corrected with informative history, reaching a VBench score of 85.07 on 15-second video.
- On MemoBench, object consistency reaches 62.18 when the camera returns to a scene, and Evolution Quality rises from 2.35 to 2.70.
- The shared idea is to add stability without retraining away pretrained priors, which matters for iterative creative tools.

## 摘要

**重點摘要：** TailSteer 和 History Forcing 處理的是生成式 AI 真正的弱點：問題不在第一張圖，而在第 15 次編輯、第 15 秒影片。

- TailSteer 透過 on-policy rollout，只學習修正去噪過程的尾段，在連續 15 到 20 次影像編輯中大幅降低累積漂移。
- 早期去噪軌跡維持不動，所以基礎模型的能力大多保留。論文指出在 FLUX、SenseNova、Qwen 系列上測試，三項保留指標都勝過 GPT-Image-2.5 Sunburst。
- History Forcing 讓學生模型去對齊「加入歷史資訊後修正的」教師預測，15 秒影片的 VBench 分數達到 85.07。
- 在 MemoBench 上，鏡頭回到原場景時的物件一致性達 62.18，Evolution Quality 從 2.35 提升到 2.70。
- 兩者的共同思路是：不必重新訓練、也不犧牲預訓練知識，就能換到穩定性，這對反覆修改的創作工具很關鍵。