---
category: hardware
faqs:
- answer: 不一定。人手開始感到難以忍受的溫度，可能仍低於部分內部零件的容許範圍，因此單靠觸摸無法判定是否超標。
  question: 驅動器燙到摸不住，就代表快壞了嗎？
- answer: Tc 是驅動器在額定運作下，外殼指定熱點允許的最高溫度。它與產品的熱設計驗證及標示壽命直接相關。
  question: 驅動器銘牌上的 Tc 是什麼？
- answer: 應讓驅動器在預定負載下運作至溫度穩定，再用合適的溫度探頭量測指定 Tc 點。量測結果不應高於銘牌標示值。
  question: 安裝人員應如何確認溫度是否安全？
featured: false
lang: zh
publishedAt: '2026-11-13T05:58:23+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/your-led-driver-feels-scorching-hot-thats-normal-is-only-half-true-2kdi
summary: LED 驅動器發熱可能屬於正常現象，但光憑「燙到摸不住」無法判斷是否過熱，仍應實際量測額定 Tc 測溫點的溫度。
tags:
- hardware
- products
title: LED 驅動器燙得嚇人？「這很正常」其實只說對了一半
trending: false
type: news
---

Double 11 orders arrived, the lights went up, and then someone reached into the ceiling void and touched the small plastic box feeding the downlight. It was hot enough to pull a hand back. The seller's answer is almost always the same: "LEDs get warm, that's normal."

That answer is half right. Heat is normal. But "normal" has a ceiling, and the ceiling is printed on the driver's label. Most people just never learn where to look.

Your hand is not a thermometer. Roughly: 45 °C feels warm, like a hot bath you can keep your hand in; 55–60 °C you can touch but don't want to hold; past about 65 °C the back of your hand won't stay on it for three seconds; at 75 °C you flinch on contact.

The widely repeated field rule — "if you can hold it for three seconds, it's fine" — works out to a threshold near 70 °C.

Here is the problem: **70 °C is nothing for an electronic component.** A 105 °C / 10,000-hour electrolytic capacitor sitting in a 70 °C case is running at roughly 85–95 °C at the core, still inside its rating.

The temperature at which your hand gives up sits right in the middle of the range where the parts are perfectly comfortable. That mismatch is why this argument never resolves: the customer is asking a component question with a hand, and the seller is answering a hand question with a component standard.

Look at the driver label. Besides input and output, there is usually a line reading `Tc: 75°C` or `Tc: 80°C`.

Tc is the maximum permitted temperature at a **designated hot spot** on the housing (usually near the MOSFET or the output diode), measured at rated ambient and full load. It exists for two reasons: IEC 61347-1 sets limits on accessible surface temperature — both to prevent burns and to keep the plastic housing from softening — and Tc is the test condition behind the lifetime claim.

So "50,000 hours" never stands alone. The full statement is **50,000 hours @ Tc 75 °C**. Exceed the case temperature and that number is void. As a rule of thumb, every 10 °C of additional case temperature roughly halves electrolytic capacitor life.

The companion figure is Ta, ambient temperature — and almost everyone misreads it. **Ta is not the 22 °C in your living room. It is the air temperature inside the cavity where the driver actually sits.** In a ceiling void, behind a fixture body, or inside a sealed junction box, Ta runs 10–20 °C above room temperature as a matter of course; above 50 °C inside a ceiling on a summer afternoon is unremarkable.

A driver whose lifetime is rated at Ta 40 °C, installed in a 70 °C cavity, doesn't lose a bit of life. It loses most of it.

**Its own losses.** A 100 W driver at 88% efficiency turns about 12 W into heat. Plastic housing conducts at roughly 0.2 W/(m·K) against aluminium's 205 — three orders of magnitude — so heat cannot spread through the shell; it has to leave through convection off the surface.

**Ambient heat.** Top floors, west-facing walls, rooftop boxes. The cavity starts hot.

**Sealed cavities.** The most common and the most avoidable: insulation batting laid straight over the fixture. Unless the instructions say the luminaire is rated for insulation contact, treat it as not rated.

**Stacking.** Several drivers packed into one spot preheat each other. Individually cool, collectively over temperature.

**Non-conductive mounting.** Laid flat on plasterboard or timber: the back can't conduct, so only the front face is working.

One more that gets forgotten: **dust and grease.** Above a commercial kitchen, in a woodworking shop, on a street-facing shopfront, a layer of dust on the heat-dissipating surface behaves like another blanket and cuts thermal performance by 30–50%.

The practical conclusion: what determines how long a driver lasts is usually not its wattage rating, but where it was put.

Without an IR thermometer, use symptoms. Any one of these three means it is not "normal warmth":

1. **It goes out after a few hours and comes back on once it cools.** Classic thermal protection cycling — output cut, then restored.
2. **Slight brightness wobble, or visible flicker.** Derating, or the step before protection trips. A phone camera at 1/100 s will show banding if it's happening.
3. **Yellowed housing, or a hot-plastic smell.** Thermal ageing of the enclosure has started. Stop using it.

If none of the three is present and it's merely hot to the touch, leave it and observe. Components are designed to run in a range that feels unpleasant to skin.

If the ceiling is already closed, these are still worth doing:

- Move the driver onto a joist or a metal surface; don't lay it flat on plasterboard.
- Leave air around it. Don't cover it with insulation; if it doesn't fit with clearance, it doesn't fit.
- Don't stack drivers. Leave spacing.
- For remote (separate) drivers, put them where a service hatch can reach them — the driver, not the LED board, is what gets replaced in year three.
- Keep 20% power headroom. Drivers running at full load run hottest.
- Keep the driver-to-board lead under 0.5 m with at least 0.5 mm² conductor. Past 1 m, voltage drop and losses become visible — a frequent cause of "the light works but isn't bright enough."

1. What is the **Tc** of this driver?
2. What **Ta** is the lifetime figure rated at, and at what case temperature?
3. What is the **efficiency**? (Same 100 W: 88% and 93% differ by 5 W of heat.)
4. Is the driver **integrated or remote**, and can it be replaced on its own?

Any legitimate manufacturer can answer all four. If they can't, it's usually not an oversight.

**I measured 70+ °C on the bench with the light lying on a table. Is it defective?**

Bench testing and installed operation are different thermal paths. On a table there is no aluminium body and no cavity — the conditions are far worse than in a ceiling, so that reading is an upper bound, not a verdict. In July a user bench-tested a recessed spotlight, measured the driver in the seventies, and melted the wax in a decorative candle tin it was resting on. That is a real observation, but an extreme one: once the fixture is installed in plasterboard against an aluminium body, the thermal path is entirely different.

**It's hot, but it has run for a year without failing. Should I do anything?**

If none of the three symptoms are present, no. The margin is designed to sit in the range that feels uncomfortable. The signal to act is a symptom, not a temperature.

The reason heat is so easy to misjudge is that it is slow. Nothing fails on the spot. It fails three years later as flicker, five years later as darkness. By then the verdict is "bad quality" — and nobody remembers that the driver spent its first summer under a layer of insulation.

## Top comments (0)

## Summary

**TLDR:** A hot LED driver may be operating normally, but “too hot to touch” is no substitute for measuring its rated Tc point.

- Human touch becomes intolerable around temperatures that electronic components may still handle, so the three-second touch rule is not a reliable component-health test.
- A driver label's Tc value is the maximum permitted temperature at a designated housing hotspot under rated conditions.
- The article notes that a 70°C case can leave an internal electrolytic capacitor around 85–95°C, illustrating why surface feel and component temperature are different questions.
- Lifetime claims such as 50,000 hours depend on a specified Tc condition; exceeding that condition undermines the claim even if the driver continues operating.

## 摘要

**重點摘要：** LED 驅動器燙手不一定異常，但「摸不住」從來不能取代對 Tc 指定測點的實際量測。

- 人手無法久觸的溫度，對電子零件而言可能仍在工作範圍內，因此「三秒摸得住」不是可靠的健康判斷。
- 銘牌上的 Tc 代表外殼指定熱點在額定條件下允許的最高溫度，不能拿任意位置的手感代替。
- 文章舉例指出，外殼 70°C 時，內部電解電容核心可能落在 85 至 95°C；表面溫度與零件溫度是兩回事。
- 「五萬小時」之類的壽命數字通常綁定特定 Tc 條件；超出該溫度後，即使燈還亮著，原本的壽命承諾也不再成立。