---
category: products
faqs:
- answer: NexoPeek is a virtual reality molecular visualization app for Meta Quest.
    The developer built it after struggling to understand a fossilized heme structure
    on a flat screen.
  question: What is NexoPeek?
- answer: Meta Quest needs 72–90 frames per second, and rendering full molecular structures
    on the headset became unstable above a few thousand atoms. The solution was to
    parse and prepare data on a backend and stream simplified geometry to the headset.
  question: What technical challenge did the developer face?
- answer: Rotating 3D molecules on a 2D screen loses depth, which makes spatial structures
    hard to understand. VR lets researchers see molecules in real three-dimensional
    space instead of simulating 3D on a flat surface.
  question: Why does VR matter for molecular visualization?
featured: false
lang: en
publishedAt: '2026-11-08T05:50:17+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/ashish_624379625242c5d263/ce-que-115-millions-dannees-dheme-fossilise-mont-appris-sur-la-visualisation-moleculaire-en-vr-57o1
summary: NexoPeek's best insight isn't VR itself. It's the realization that the problem
  was the camera, not the data, which is a lesson flat-screen science tools keep ignoring.
tags:
- products
- developer-tools
- hardware
title: Ce que 115 millions d'années d'hème fossilisé m'ont appris sur la visualisation
  moléculaire en VR (et pourquoi j'ai cons
trending: false
type: news
---

# 
  
  Ce que 115 millions d'années d'hème fossilisé m'ont appris sur la visualisation moléculaire en VR (et pourquoi j'ai construit NexoPeek pour Meta Quest)

L'été dernier, je tenais un bloc de grès dans une main et mon téléphone dans l'autre, sur une falaise du Dorset. Un ami paléontologue venait d'y repérer ce qu'il pensait être un nodule ferrugineux — la gangue minérale qui piège parfois la matière organique pendant des millions d'années. En le fendant, une teinte rouge sombre est apparue : de l'hème, le groupement fer d'une protéine, préservé là depuis environ 115 millions d'années.

J'ai passé trois heures à essayer de comprendre ce que je regardais. Pas à chercher sur Google — à comprendre, spatialement, comment un noyau porphyrinique et un atome de fer peuvent survivre à un enfouissement géologique. Sur un écran plat, je tournais une molécule avec ma souris, je perdais la profondeur, je recommençais. La troisième fois que j'ai cliqué sur « reset view », j'ai compris que mon problème n'était pas la donnée. C'était la caméra.

Deux mois plus tard, j'ai commencé à prototyper NexoPeek, une application de visualisation moléculaire en réalité virtuelle pour Meta Quest. L'idée était simple : arrêter de simuler la 3D sur une surface 2D.

Sur le plan technique, la question centrale était : où placer la charge ? Le rendu VR impose 72–90 images par seconde par œil sur Quest, ce qui laisse très peu de marge. J'ai testé deux approches. La première consistait à faire le rendu complet des structures dans le casque — coûteux, instable dès qu'une molécule dépasse quelques milliers d'atomes. La seconde, celle que j'ai retenue, délègue le parsing et la préparation des données à un backend, puis streame une géométrie allégée vers le casque. Le Quest ne fait que le rendu de ce qu'il doit afficher.

Le vrai changement, pourtant, n'était pas dans le pipeline. C'était dans la main. Saisir une molécule, la faire tourner, la traverser — le geste remplace l'abstraction. L'hème n'est plus un diagramme plat avec des flèches ; c'est un objet qu'on contourne, dont on voit le fer au centre comme un point d'ancrage.

Je ne prétends pas que la VR remplace la cristallographie ou la modélisation quantique. Mais pour transmettre une intuition structurelle — à un étudiant, à un collègue, à soi-même à 23 heures — la dimension manquante compte. Ce fossile m'a appris qu'une molécule n'est pas une image. C'est un lieu. Et certains lieux méritent d'être visités autrement qu'à plat.

## Top comments (0)

## Summary

**TLDR:** NexoPeek's best insight isn't VR itself. It's the realization that the problem was the camera, not the data, which is a lesson flat-screen science tools keep ignoring.

- The developer found what was believed to be 115-million-year-old fossilized heme in Dorset and struggled to understand its 3D structure on a flat screen.
- That frustration led to NexoPeek, a molecular visualization app for Meta Quest.
- Quest rendering requires 72–90 frames per second, and rendering full structures on the headset became unstable above a few thousand atoms.
- The chosen design moves parsing and data preparation to a backend and streams simplified geometry to the headset.
- The project shows that spatial computing may be most useful in niche scientific work rather than consumer entertainment.

## 摘要

**重點摘要：** NexoPeek 最好的洞見不是 VR 本身，而是發現「問題出在鏡頭，不是資料」。這正是平面螢幕科學工具一直忽略的教訓。

- 開發者在英國多塞特發現疑似保存了 1.15 億年的血基質化石，卻在平面螢幕上怎麼也看不懂它的 3D 結構。
- 這份挫折促成了 NexoPeek，一款 Meta Quest 上的分子視覺化應用程式。
- Quest 需要每秒 72–90 幀的渲染，在頭戴裝置上完整渲染分子，超過幾千個原子就會不穩定。
- 最後的架構把解析和資料準備交給後端，再把精簡過的幾何資料串流到頭戴裝置。
- 這個專案顯示，空間運算真正的用武之地，可能是小眾科學領域，而不是消費娛樂。