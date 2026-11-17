---
category: ai-ml
faqs:
- answer: Phonon runs entirely on the user's device without a server or network connection,
    so the text being spoken never leaves the device. Most voice AI sends every sentence
    to a cloud server.
  question: What makes Phonon different from most voice AI?
- answer: The Phonon 31M model is released under Apache 2.0 and can be used commercially
    for free. The other Phonon models are CC BY-NC, and commercial use of them is
    priced by number of users rather than by amount of speech generated.
  question: Can Phonon be used in commercial products?
- answer: Phonon builds on the Pocket TTS lineage and uses flow matching to generate
    audio, which differs from most TTS approaches. The team says this enabled high
    quality in a small model, though early training was numerically unstable and needed
    several tricks.
  question: How does Phonon get good quality at such a small size?
featured: false
lang: en
publishedAt: '2026-11-05T00:00:00+00:00'
relatedSlugs: []
sources:
- name: Hugging Face Blog
  url: https://huggingface.co/blog/phonon-tts
summary: Phonon shows that good voice AI no longer needs the cloud, but only the 31M
  model is truly free and the licensing does the real gatekeeping.
tags:
- ai-ml
- open-source
- products
title: A Closer Look at Phonon TTS. Launching High-Quality On-Device Speech That Tops
  the Benchmarks.
trending: false
type: news
---

[Text-to-Speech •  Updated   •  54](/executorch-community/Phonon-31M-EN-ExecuTorch-WebGPU)    

Two weeks ago, we opened up Phonon, our small text-to-speech model that runs on your own device. It needs no server and no network, and what you type stays with you.

We've been very happy with the reception so far. So here's the story of the launch: why we built Phonon, what it can do, the demos that came with it, and how it did on Hugging Face's Open TTS Leaderboard.

Most voice AI lives in the cloud: every sentence makes a round trip to a server. Phonon runs on your own device instead. Your text stays there and the voice works without a network. We’ve also opened the weights. Phonon 31m is Apache 2.0, so you can use it for free, even in a commercial product. The other models are CC BY-NC, so they’re free for non-commercial projects. If you’re building something commercial with those, pricing is based on your number of users, not how much speech you generate.

Getting a good voice to run on a small device has always been hard. You could make the model small, but then it didn’t sound great. Or you could make it sound great, but then it wouldn’t fit. We addressed both.

We announced Phonon in April and spent the next six months building on it with partners and early users. Their feedback helped us to shape this release. The models got smaller, and we added more languages and support for custom voices through voice cloning and voice design.

Phonon is based on the [Pocket TTS](https://huggingface.co/kyutai/pocket-tts) lineage and as such uses flow matching to generate the audio which is very different from the modeling techniques used in other TTS systems. This is what allowed us to bring this level of quality to such a small model but it created new challenges while training the models. The training was initially numerically unstable and required several tricks to produce quality results on all five languages.

Phonon comes in two sizes, at about 65 MB and 75 MB. Together they speak English, French, German, Spanish and Portuguese. There are more than 100 built-in voices, and you can create your own in [Gradium Studio](https://studio.gradium.ai/). Phonon also handles the important things that most other TTS systems often stumble on, like phone numbers, dates and codes.

It runs on phones, laptops, single-board computers and in a browser tab, so you can [hear it right now](https://huggingface.co/spaces/gradium/phonon). Phonon 31m speaks English and is Apache 2.0, so you can build on it freely, including for commercial products. Phonon 40m covers all five languages under a non-commercial license.

[The launch](https://gradium.ai/blog/release-phonon-open-weight) came with demos from friends and from our own team. On an Apple Watch with Wi-Fi off, Phonon talks you through a coffee brew step by step. On an iPhone with no signal, it counts your reps and keeps you going. A robot called Lamp, from Autonomous, wears a sorting hat and talks in character. In a browser, an offline dino runner becomes a radio show hosted by Rex. There's also a sci-fi game voiced on the player's own machine, and Proust read aloud page by page.

The Hugging Face team built the Transformers integration, so developers could use Phonon in Transformers from day one.

Developers have started building on it too. An [ExecuTorch conversion](https://huggingface.co/executorch-community/Phonon-31M-EN-ExecuTorch-WebGPU) runs Phonon on a visitor's GPU in the browser, [Micdrop](https://micdrop.dev/docs/ai-integration/provided-integrations/phonon.md) brings it to Node.js apps, and Spaces like [smallest-s2s](https://huggingface.co/spaces/Steveeeeeeen/smallest-s2s) build on it.

Phonon was downloaded more than 200,000 times in its first two weeks, and it’s still trending on Hugging Face.

The [Open TTS Leaderboard](https://huggingface.co/spaces/hf-audio/open_tts_leaderboard) is a very new project from Hugging Face, and we love it. With more than 9,000 TTS models on the [Hugging Face Hub](https://huggingface.co/models?pipeline_tag=text-to-speech), the leaderboard gives developers one place to compare open models and hear them side by side. Across 23 languages, models are evaluated on **intelligibility** (*word error rate of the outputs*), **speed** (*inverse real-time factor and time-to-first audio*), and **naturalness** (*UTMOS for English and KOMOS for Korean*). Fixed-voice and voice cloning are evaluated, with an additional speaker similarity metric for the latter. The leaderboard also has a Listen tab, where you can conveniently compare TTS outputs yourself and vote for the ones you like the most.

On intelligibility, Phonon ranks first in [German](https://huggingface.co/spaces/hf-audio/open_tts_leaderboard?languages=de) and [Spanish](https://huggingface.co/spaces/hf-audio/open_tts_leaderboard?languages=es), and in the top three in every language we evaluated, next to models up to 100 times its size.

Speed is where we see Phonon truly shine, as the models top the [CPU streaming benchmark](https://huggingface.co/spaces/hf-audio/open_tts_leaderboard?streaming-cpu) on time-to-first audio.

We built a new inference framework, [ptts](https://github.com/gradium-ai/xn-ptts), specifically for Phonon. The goal of ptts is to get the best performance on a wide variety of devices and as such supports more than 10 backends: CPU (Intel, Arm, WebAssembly), GPU (CUDA, Vulkan, Metal, WebGPU), and NPU (Apple Core ML, Snapdragon®).

Phonon is also available in 🤗 Transformers, from v5.21, as its reference PyTorch implementation. Where `ptts` runs a single stream on device, Transformers targets GPU throughput: batched generation, full-graph `torch.compile`, e.g., for synthesizing speech datasets at scale. Being native PyTorch, it is a base to build upon, whether to integrate Phonon into your own stack or to study the model itself.

It belongs to the Pocket TTS lineage, so we first added Pocket TTS to Transformers. Phonon sits on top as a [modular](https://huggingface.co/docs/transformers/modular_transformers) model: about [200 lines](https://github.com/huggingface/transformers/blob/main/src/transformers/models/gradium_phonon_tts/modular_gradium_phonon_tts.py) describing only what differs.

Phonon generates audio latents autoregressively: each step outputs a latent that is fed back as the next input, and the training loss is computed on them. Latents are the model's inputs, outputs and targets, as text tokens are for a language model, so the codec mapping audio to latents plays the role of a tokenizer. Transformers ships it as such: an [audio tokenizer](https://huggingface.co/docs/transformers/model_doc/pocket_tts_audio_tokenizer), held by the processor next to the text tokenizer:

```
from transformers import AutoProcessor, GradiumPhononTTSForConditionalGeneration
model_id = "gradium/phonon-31m-en"
processor = AutoProcessor.from_pretrained(model_id, device_map="auto")
model = GradiumPhononTTSForConditionalGeneration.from_pretrained(model_id, device_map="auto")
print(f"{model.num_parameters():,}")  # 30,788,354
print(f"{processor.audio_tokenizer.num_parameters():,}")  # 10,305,313
```
A voice is not a recording but a tensor of speaker latents. Phonon never encodes audio directly with its audio tokenizer, which ships decoder-only, and voices come precomputed: [gradium/phonon-voices](https://huggingface.co/gradium/phonon-voices).

```
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
path = hf_hub_download("gradium/phonon-voices", "voices/LMDIYE0Oa377Qh6Z.safetensors")
voice = load_file(path)["speaker_wavs"][0].T  # (num_frames, 512)
```
The prompt layout (voice positions, text, then a token opening the audio) ships with the checkpoint as a chat template, as for other multimodal models in Transformers. You write a standard conversation, with an empty `audio` item where the voice goes, and your code stays the same across checkpoints. The processor then expands the voice placeholder to one position per frame, normalizes and tokenizes the text, and batches the inputs:

```
conversation = [
    {"role": "user", "content": [{"type": "audio"}, {"type": "text", "text": "Hello from Phonon."}]}
]
inputs = processor.apply_chat_template(
    conversation,
    tokenize=True,
    return_dict=True,
    add_generation_prompt=True,
    processor_kwargs={"audio_prompt_latents": [voice]},
).to(model.device)
# prompt: <|audio_prompt|> × num_frames, "Hello from Phonon.", <|audio_bos|>
```
`generate` returns latents, which the processor decodes to audio:

```
outputs = model.generate(**inputs)  # audio_latents: (batch_size, num_frames, 32)
audio = processor.decode(outputs.audio_latents, outputs.audio_latents_mask)
processor.save_audio(audio, "phonon.wav")
```
See the [docs](https://huggingface.co/docs/transformers/model_doc/gradium_phonon_tts) 🤗 for more!

Phonon can speak with any voice. Clone one from a short recording with the speaker’s consent, or describe a new one in plain text in [Gradium Studio](https://studio.gradium.ai/). Then download the voice file, load it in Phonon, and it runs fully on the device.

We also train custom Phonon models with design partners. If your memory budget is tight, we can make the model smaller. If you need Korean, Arabic or Japanese, we can train for that too. And if your product has its own vocabulary, we can fine-tune on it. [Get in touch](https://gradium.ai/contact?subject=Sales) and tell us what you need.

Thank you to the Hugging Face team, and to everyone who tried Phonon in its first two weeks.

Phonon is our first open release. [Try it out](https://huggingface.co/spaces/gradium/phonon) and tell us what you build.

## Summary

**TLDR:** Phonon shows that good voice AI no longer needs the cloud, but only the 31M model is truly free and the licensing does the real gatekeeping.

- Phonon is a small text-to-speech model family that runs fully on-device, with no server and no network, so typed text never leaves the device.
- The 31M model is Apache 2.0 and free for commercial use. The other models are CC BY-NC, and commercial pricing is based on number of users rather than amount of speech generated.
- It builds on the Pocket TTS lineage and uses flow matching, which the team says enabled high quality at small size but made training numerically unstable at first.
- Over six months since the April announcement, the models got smaller and added more languages, voice cloning, and voice design.
- The launch claims top results on Hugging Face's Open TTS Leaderboard, which puts pressure on cloud TTS APIs that charge per character.

## 摘要

**重點摘要：** Phonon 證明好聽的語音 AI 不必再依賴雲端，但真正免費的只有 31M 模型，實際設下門檻的是授權條款。

- Phonon 是一系列小型文字轉語音模型，完全在裝置端執行，不需伺服器也不需網路，輸入的文字不會離開裝置。
- 31M 模型採 Apache 2.0 授權，可免費商用。其他模型為 CC BY-NC，商用則依使用者人數計價，而不是依生成的語音量。
- 模型承襲 Pocket TTS 系譜並採用 flow matching，團隊表示這讓小模型也能有高音質，但訓練初期數值不穩定。
- 從 4 月發表至今的六個月裡，模型變得更小，並加入更多語言、聲音複製與聲音設計功能。
- 團隊宣稱在 Hugging Face Open TTS 排行榜名列前茅，這對按字元收費的雲端 TTS API 形成壓力。