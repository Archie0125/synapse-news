---
category: hardware
faqs:
- answer: MetaRoCE 是 Meta 推出的開放式 RDMA 傳輸層，在 OCP Summit 2026 以 OCP NIC 3.0 網卡展示。它能在一般乙太網路上把封包分散到多條路徑，支援逐路徑壅塞控制，並能容忍封包遺失與亂序。
  question: MetaRoCE 是什麼？
- answer: Meta 先在 AMD Pensando 可程式化網卡上實作這個協定，不需要專用硬體。這讓 Meta 能向多家廠商採購網卡，不必被單一網路供應商綁住。
  question: MetaRoCE 能跑在可程式化網卡上，為什麼重要？
- answer: Meta 想打造一套能擴展到百萬 GPU 規模 AI 訓練的網路傳輸協定，能在不同拓撲與硬體上運作，而且只依賴 ECN、ECMP 等標準乙太網路功能。
  question: MetaRoCE 要解決什麼問題？
featured: false
lang: zh
publishedAt: '2026-11-12T04:51:39+00:00'
relatedSlugs: []
sources:
- name: ServeTheHome
  url: https://www.servethehome.com/this-is-the-meta-metaroce-network-adapter/
summary: MetaRoCE 的重點不在單一張網卡，而是 Meta 想讓 RDMA 傳輸不再綁定特定廠商。這步棋低調，卻會對所有販售封閉式 AI 網路方案的業者形成壓力。
tags:
- hardware
- ai-ml
- open-source
title: 一窺 Meta 自研 MetaRoCE 網路卡
trending: false
type: news
---

At OCP Summit 2026, we saw Meta’s new MetaRoCE network adapter. This is Meta’s answer to providing an open RDMA transport layer that has features like packet spraying, congestion control, and more. This was a presentation we saw at OCP Summit, but Meta had a NIC on display.

## Meta MetaRoCE Network Adapter at OCP 2026

Here is the display from the Meta booth at OCP Summit 2026, where you can see an [OCP NIC 3.0](https://www.servethehome.com/ocp-nic-3-0-form-factors-quick-guide-intel-broadcom-nvidia-meta-inspur-dell-emc-hpe-lenovo-gigabyte-supermicro/) card.

During its OCP 2026 presentation, Meta shared some of the big features of MetaRoCE:

- *Per-path reliability and congestion control*
- *Receiver rate hints (RCN) for fast incast convergence*
- *Tolerates packet loss and reordering*
- *Single QP carries multiple streams over multiple network paths*
- *Runs on commodity Ethernet: ECN + ECMP, no switch **(Source**: Meta)*

Before OCP Summit, Meta demonstrated this with the AMD Pensando NIC series. The programmability allowed it to implement the protocol without having dedicated hardware. That allows Meta to potentially source from multiple vendors.

Meta is trying to build a network protocol that can scale to million-GPU training, but also that can run on different network topologies and hardware.

As a quick aside, the NIC shown was an OCP NIC 3.0 with SFF pull tab design, which is our favorite form factor that we wish all server vendors used.

## Final Words

Given Meta’s heritage of starting OCP Summit, they usually have super-cool hardware in the booth. Last year, we got the [AMD Helios MI450 Rack at OCP Summit with a Different Version from Meta](https://www.servethehome.com/amd-helios-mi450-rack-at-ocp-summit-with-a-different-version-from-meta/) as an example. This year, the company brought some larger nodes, but also small items like this adapter. It is always neat to see what Meta is working on.

If you want to see what AWS is doing, for example, you can check out our [Inside the Secretive AWS Networking Lab](https://www.servethehome.com/inside-the-secretive-aws-networking-lab/).

## Summary

**TLDR:** MetaRoCE is less about one NIC and more about Meta making RDMA transport vendor-neutral, which quietly pressures anyone selling proprietary AI networking.

- Meta showed a MetaRoCE adapter at OCP Summit 2026, built as an OCP NIC 3.0 card with an SFF pull tab.
- MetaRoCE adds per-path reliability and congestion control, receiver rate hints for incast, and tolerance for packet loss and reordering.
- A single QP can carry multiple streams over multiple network paths on commodity Ethernet using ECN and ECMP.
- Meta first demonstrated it on programmable AMD Pensando NICs, so it needs no dedicated silicon and can be sourced from several vendors.
- The goal is a transport that scales to million-GPU training across different topologies and hardware.

## 摘要

**重點摘要：** MetaRoCE 的重點不在一張網卡，而在 Meta 想讓 RDMA 傳輸擺脫特定供應商，這對販售專有 AI 網路方案的廠商是無聲的壓力。

- Meta 在 OCP Summit 2026 展出 MetaRoCE 網路卡，採用 OCP NIC 3.0 規格與 SFF 拉環設計。
- MetaRoCE 支援逐路徑的可靠性與壅塞控制、針對 incast 的接收端速率提示，並能容忍封包遺失與亂序。
- 單一 QP 可透過多條網路路徑承載多個資料流，在一般乙太網路上靠 ECN 與 ECMP 就能運作。
- Meta 先在可程式化的 AMD Pensando 網卡上展示，不需專用晶片，因此能向多家供應商採購。
- 目標是打造能擴展到百萬 GPU 訓練、並適用不同拓撲與硬體的傳輸協定。