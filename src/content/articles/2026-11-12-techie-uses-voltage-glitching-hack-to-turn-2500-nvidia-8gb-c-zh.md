---
category: hardware
faqs:
- answer: 依文章說法，特定 CMP-170HX 版本實際裝有 GA100 晶片及相應 HBM2e 記憶體裸晶，只是大部分資源在出廠時遭到停用。這項修改重新取得了對被封鎖資源的存取。
  question: 一張標示 8GB 的礦卡怎麼可能變成 80GB？
- answer: 研究者刻意在受保護程式執行時干擾晶片電壓，藉此繞過熔絲控制器的防護。這使她得以修改單靠軟體破解仍無法解除的配置限制。
  question: 電壓故障注入在這次破解中做了什麼？
- answer: 對多數人而言不能。這套方法需要專業設備與知識，可能永久損壞價值 2,500 美元的硬體，而且穩定性、效能與長期可靠度仍需獨立驗證。
  question: 它能取代購買正式 A100 嗎？
featured: false
lang: zh
publishedAt: '2026-11-12T10:30:00+00:00'
relatedSlugs: []
sources:
- name: Tom's Hardware
  url: https://www.tomshardware.com/pc-components/gpus/techie-turns-usd2-500-cmp-170hx-8gb-mining-card-into-a-full-fat-a100-80gb-with-voltage-glitching-carefully-blowing-onboard-fuses-to-unlock-entire-vram-and-shader-modules
summary: 這項針對 CMP 170HX 的破解，揭露輝達透過產品分級封鎖了多少硬體價值；但其風險與操作門檻堪比實驗室級別，離真正實用的平價 A100 仍相當遙遠。
tags:
- hardware
- cybersecurity
- open-source
title: 高手利用電壓故障注入破解，將 2,500 美元的輝達 8GB 挖礦顯卡解鎖成配備 80GB VRAM、價值 2 萬美元的完整 A100
trending: false
type: news
---

Enterprising techies looking to build their own local AI cluster have far more interesting options than buying DGX Sparks or Apple Mac Studios. Used data center GPUs are everywhere, and a server rack's garbage is an enthusiast's treasure. This option has become even more popular with [CMPunlocker](https://github.com/amoghmunikote/cmpunlocker), a soft-mod for Nvidia CMP-170HX cards that unlocks abilities well beyond stock. Now, a techie [has taken it a step further](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/), blasting through the remaining limitations with voltage glitching and creating a card faster than the actual $20,000 Nvidia A100 GPU with 80GB of VRAM... but from an $2,500 8GB CMP-170HX mining card.

The volt-mod was done by Kate ([GitHub link here](https://github.com/kate-land/ga100vfi)), who got her starting point [from a paper](https://www.researchgate.net/publication/408132536_A_Canary_in_the_Crypto_Mine_Defeating_Stack_Protection_in_a_GPU_Secure_Coprocessor) that described how one could exploit GA100 cards' microcode. She turned her attention to the normally protected onboard fuse controller. Although it's rarely discussed, a "fuse box" has been integral in most any CPU and GPU for a while — though it's normally used once at the factory to break physical connections in chips to parts that have tested poorly, thus disabling them so they can be sold as a lower-end model.

If you're wondering how people are getting 80-40GB of VRAM out of 8-10GB, the explanation is simple: the GA100 silicon actually includes all the corresponding HBM2e VRAM dies within; but they get disabled at the factory like the shader modules. The smaller version is more desirable, as it's based on the variant of GA100 with 80GB of HBM2e within, while the 10GB cards spawn from the 40GB GA100.

The Nvidia cards in question have quite an elaborate eFuse controller (16,384 in a 512 x 32 array) — which can be read to obtain the card's current configuration. Most every part of the card has related fuses: VRAM sections, individual shader modules, PCIe 4.0 and NVLink, and even video codec hardware. However, as Kate succinctly put it: Nvidia's design is insecure, as popping fuses can grant access to *more* features, not fewer.

Under normal conditions, these fuses can't be popped, or "written to," by the user — but a geek armed with a soldering iron isn't a normal user. Kate had GPT-6 Astra design a simple circuit board based on an $8 STM32G4 microcontroller to tap into the power signals on the card's PCB.

The voltage regulators (VRMs) on the card "speak" PWMVID, an Nvidia standard, and Kate's board intercepted the PWM signals sent into the VRM controller, forcing it to produce voltage glitches on the line feeding the GPU, where the fuse controller lies.

Remember when we said the fuse controller was read-only? With the voltage glitches, many fuse-status reads in a tight loop, and she managed to set the controller to a state in which its [security](https://www.tomshardware.com/tag/security) bit flags allowed writes through. From that point, it was "easy" to reconfigure her card. She was careful to force-disable any shader modules previously marked as defective, because these are physical fuses — there's no "undo" button.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

She applied the mod to her cards and, after testing with multiple workloads, found that nine had the full 80 GB of VRAM working, and one card "only" had 64 GB usable. Most interestingly, unlocking all the shader modules (SM) nets her FP16 FMA performance 20% *beyond* a regular A100 card. She thinks this is due to the chips often having 120 or more usable SMs — over the 108 on the spec sheet. The GA100 die starts with 128 SMs to account for defects, which is normal in chip manufacturing.

The CMPUnlocker soft mod is required for enabling the "new" features on the [drivers](https://www.tomshardware.com/tag/drivers), but it doesn't unlock the card's full potential: the VRAM upper limit is 40-64GB (depending on the variant), many shader modules remain locked, and PCIe bandwidth only goes to 2.0. Additionally, there's no ECC, NVLink, or multi-instance GPU support, all of which are critical in a server setup and are also used for product segmentation.

Kate's volt-mod does away with all of these limits, and her best test card is happily working at PCIe 4.0 speed with the full feature set. She didn't test the video encoder bits, but it's unlikely anybody using these cards cares much for that.

As for the cost, a CMP-170HX 8GB is currently hovering around $3,000, and the 10GB variant costs around $2,500. A full-fat Nvidia A100 80GB in a PCIe configuration can reach $20,000 or more. The SXM server-module versions are cheaper, but they require infrastructure around them. Note that these prices will likely vary significantly, especially as people become increasingly aware of the mods.

Kate says she's publishing her research now because another person independently found the same issue. She has informed Nvidia of the vulnerability, though there's not much the company can do for existing cards already on the market.

*Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.*

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

## Summary

**TLDR:** The CMP-170HX hack exposes how much value Nvidia disables through segmentation, but its laboratory-grade risks keep it far from a practical bargain A100.

- Researcher Kate combined a CMPunlocker software modification with voltage glitching against the GA100 fuse controller.
- The project reportedly re-enabled disabled compute resources and expanded accessible HBM2e memory from an 8GB configuration to 80GB.
- The $2,500 source card is compared with an 80GB A100 commonly priced around $20,000, although the excerpt provides no complete independent benchmark validation.
- Voltage fault injection can damage hardware or create unstable results, making this an advanced security experiment rather than a routine upgrade.

## 摘要

**重點摘要：** CMP-170HX 破解揭露了產品分級封鎖多少硬體價值，但高風險實驗門檻，讓它離「便宜 A100」仍非常遙遠。

- 研究者 Kate 在 CMPunlocker 軟體修改基礎上，進一步用電壓故障注入攻擊 GA100 的熔絲控制器。
- 該計畫據稱重新啟用了被關閉的運算單元，並把原本 8GB 配置可用的 HBM2e 擴展至 80GB。
- 文章把約 2,500 美元的礦卡與約 20,000 美元的 80GB A100 相比，但摘錄未提供完整的獨立效能與穩定性驗證。
- 電壓干擾可能損壞硬體或導致不穩定，因此這更像進階資安研究，而不是一般玩家可放心採用的升級方式。