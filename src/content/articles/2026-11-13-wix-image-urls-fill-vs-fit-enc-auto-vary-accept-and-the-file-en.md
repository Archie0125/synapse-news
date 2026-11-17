---
category: developer-tools
faqs:
- answer: The path before /v1/ identifies the stored media file. The segments after
    /v1/ specify transformations and end with a presentation filename.
  question: Which part of a Wix image URL identifies the original asset?
- answer: 'Wix can negotiate the response format using the request''s Accept header.
    A cache or diagnostic tool that ignores Vary: Accept may therefore treat different
    representations as if they were identical.'
  question: Why can the same-looking URL return different image formats?
- answer: Developers should compare the transformation path, request Accept header,
    response Content-Type, pixel dimensions and byte size. The page's data-image-info
    metadata also reveals the original dimensions and crop settings.
  question: What should developers inspect when debugging Wix image quality?
featured: false
lang: en
publishedAt: '2026-11-13T05:58:44+00:00'
relatedSlugs: []
sources:
- name: Dev.to
  url: https://dev.to/casper_tran_59c6a8b1e1f3d/wix-image-urls-fill-vs-fit-encauto-vary-accept-and-the-file-behind-v1-1ppn
summary: Wix image URLs are a useful transformation API disguised as filenames, but
  content negotiation makes casual URL inspection dangerously misleading.
tags:
- developer-tools
- products
title: 'Wix image URLs: fill vs fit, enc_auto, Vary: Accept and the file behind /v1/'
trending: false
type: news
---

Every image on a Wix site comes from `static.wixstatic.com`, and the URL carries its own resize instructions:


```
https://static.wixstatic.com/media/f86c86_2daf6097903349128271971dcdfeaf46~mv2.jpg/v1/fill/w_800,h_604,fp_0.49_0.50,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/Awaken-team-FINAL.jpg
```
The part before `/v1/` is the stored file. Everything after it is a list of operations, and the last segment is a file name. I wanted to know which of those options do anything, so today (13 November 2026) I took images from two sites listed on Wix's own showcase, [awakenstudio.nyc](https://www.awakenstudio.nyc/) and [photodesign.co.uk](https://www.photodesign.co.uk/), plus [wix.com](https://www.wix.com/) itself, and changed one option at a time with `curl`. Pixel sizes come from Pillow, or from `ffprobe` for AVIF.

On awakenstudio.nyc the server-rendered HTML mostly holds placeholders. The `<img>` for one project thumbnail points here:


```
.../89f747_47ed037775c443a1926377c45c53510f~mv2.jpg/v1/fill/w_147,h_98,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/Angel_April_2024-16.jpg
```
That returns a blurred 147×98 AVIF of 2,689 bytes. Once the scripts run, Wix swaps in a URL sized to the container. In a Chromium window 800 px wide, the team photo became the `w_800,h_604` URL at the top of this post.

Each image wrapper also carries a `data-image-info` attribute with JSON in it, and `imageData.width` and `imageData.height` there are the stored file's dimensions. For the team photo it says 6480×3261, and for a cropped portrait 2400×3600 plus the crop box. Both matched the files I downloaded later, so the page tells you how big the original is before you fetch anything.

All rows below use the team photo with no `Accept` header, so every response is a JPEG and the sizes compare directly.

| Options after `/v1/` | Pixels | Bytes | 
|---|---|---|
| `fill/w_800,h_604` | 800×604 | 69,269 | 
| `fill/w_800,h_604,q_85` | 800×604 | 55,428 | 
| `fill/w_800,h_604,q_30` | 800×604 | 22,315 | 
| `fill/w_800,h_604,q_100` | 800×604 | 231,832 | 
| `fill/w_800,h_604,q_85,usm_0.66_1.00_0.01` | 800×604 | 58,669 | 
| `fill/w_800,h_800,q_85` | 800×800 | 78,027 | 
| `fill/w_800,h_800,al_l,q_85` | 800×800 | 11,578 | 
| `fit/w_800,h_800,q_85` | 800×402 | 30,679 | 
| `crop/x_0,y_0,w_800,h_800` | 800×800 | 9,641 | 
| `fill/w_800,h_604,q_85,blur_2` | 800×604 | 36,431 | 
| `fill/w_800,h_604,q_85,blur_30` | 800×604 | 17,472 | 

`fill` scales and crops to the exact box. `al_c` (centre) gave the same bytes as leaving alignment out, and `al_l` moved the crop to the left edge. `fit` keeps the whole picture inside the box. `crop` cuts a pixel region out of the original, which is how the portrait's `crop/x_92,y_276,w_2165,h_2641` works. `usm_` is an unsharp mask and adds a few kilobytes. `blur_2` is the value the placeholders use.

| Options | Pixels | Bytes | 
|---|---|---|
| `fill/w_10000,h_5032,q_85` | 10000×5032 | 1,582,357 | 
| `fill/w_10000,h_5032,lg_1,q_85` | 10000×5032 | 1,582,357 | 
| `fit/w_10000,h_10000,q_85` | 6480×3261 | 786,714 | 

`fill` upscales without complaint, and the result is larger in bytes than the 1,018,693-byte original. `fit` stops at the stored size. Some of Wix's own URLs include `lg_1`, but in both of my tests the output with and without it had the same MD5.

I kept the size options fixed and varied `enc_` and the `Accept` header:

| `enc_` value | Chrome's image Accept | `image/webp,*/*` | no Accept | 
|---|---|---|---|
| `enc_avif,quality_auto` | AVIF 32,313 | WebP 32,724 | JPEG 50,044 | 
| `enc_avif` | AVIF 35,657 | WebP 32,724 | JPEG 50,044 | 
| `enc_auto` | AVIF 32,313 | WebP 32,724 | JPEG 50,044 | 
| `enc_webp`, `enc_jpg`, `enc_png`, or none | JPEG 58,577 | JPEG 58,577 | JPEG 58,577 | 

So `enc_avif` and `enc_auto` behave the same way: the server picks AVIF, WebP or JPEG from what the client accepts, and the response carries `vary: Accept`. The other three values had no effect at all, and without an `enc_` option the response was the same JPEG for every header, with no `Vary`. `quality_auto` only changed the AVIF size.

The last path segment is ignored. I replaced `Awaken-team-FINAL.jpg` with `a.jpg` and got a file with the same MD5.

Delete `/v1/` and everything after it:


```
curl -s -H 'Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
  -D - -o team.jpg \
  'https://static.wixstatic.com/media/f86c86_2daf6097903349128271971dcdfeaf46~mv2.jpg'
```
That returned a 6480×3261 JPEG of 1,018,693 bytes, against 32,313 bytes for the 800×604 AVIF the page loads. A second photo (`89f747_47ed…~mv2.jpg`) came back as the same 2880×1920 JPEG of 3,735,681 bytes with and without the browser `Accept` header, and the bare response has no `Vary`. The cropped portrait came back whole, at 2400×3600.

The headers differ from the resized copies:

|  | Resized copy | Bare file | 
|---|---|---|
| `cache-control` | `public, max-age=2592000, immutable` (30 days) | `public, max-age=15552000, immutable` (180 days) | 
| `x-seen-by` | `image-manipulator-…` | `gcp.us-central-1.media-router-…` | 
| `etag`, `last-modified` | none | present | 

The `etag` is the MD5 of the body, so you can check a download against it. Both responses send `access-control-allow-origin: *`, so `fetch()` from any page can read them.

Two variants also worked: an ID with no `~mv2` (`04b15d1b030049d1b3746f8ef5a72955.png`, a 200×200 PNG on photodesign.co.uk) and a URL with the tilde encoded as `%7E`. A trailing slash or the wrong extension (`~mv2.png` for a JPEG) gave `403` with the body `Forbidden`.

The stored file is what was uploaded, and sometimes that is small. On wix.com one illustration is requested as `fill/w_235,h_262,al_c,lg_1,…`, which returns a 235×262 AVIF. The bare PNG is 168×187. The page shows an upscaled copy, so stripping `/v1/` gives you fewer pixels than you see, though they are the real ones. Another wix.com photo was stored at exactly 880×600, the size the page asks for. There the bare JPEG is 354,103 bytes against the page's 34,135-byte AVIF, so the same pixels cost ten times the data.

If size matters, compare against `data-image-info` or the downloaded file before assuming the bare URL is bigger.

1. On `static.wixstatic.com/media/<id>.<ext>/v1/...`, cut the path at the first `/v1/` and drop any query string.
2. If you read URLs out of raw HTML, expect `blur_` placeholders. Cutting them at `/v1/` still gives the stored file, but their `w_`/`h_` say nothing about the displayed size.
3. For a resized copy, prefer `fit` so you never get an upscale. Add `enc_auto` for AVIF or WebP, or omit `enc_` for a JPEG; `enc_jpg` and the other values do nothing.

I build PixLasso, a browser extension for saving images from pages, and its Wix rule is step 1. The manual version for site owners is in my [Wix download guide](https://pixlasso.com/guides/download-images-from-wix-site?src=devto).

## Top comments (0)

## Summary

**TLDR:** Wix image URLs are a useful transformation API disguised as filenames, but content negotiation makes casual URL inspection dangerously misleading.

- The media identifier before /v1/ points to the stored asset, while the path after /v1/ describes resizing, cropping, quality and encoding operations.
- Wix initially serves tiny blurred placeholders, then its client-side code swaps in an image sized for the rendered container.
- The data-image-info attribute exposes original dimensions and crop metadata, allowing developers to inspect source geometry before downloading the full asset.
- Tests without an Accept header returned JPEG even when modern-format options appeared in the URL, showing that request headers and Vary: Accept matter to debugging and caching.

## 摘要

**重點摘要：** Wix 圖片網址其實是披著檔名外衣的轉換 API；若忽略內容協商，只看網址很容易判錯實際回傳內容。

- 網址中 /v1/ 前方才是實際儲存的媒體識別碼，後方則是一串縮放、裁切、畫質與編碼指令。
- Wix 伺服器端頁面多半先放入小型模糊預覽，瀏覽器執行腳本後才換成符合容器尺寸的圖片。
- data-image-info 會揭露原圖尺寸與裁切資料，因此不必先下載完整檔案，也能掌握素材幾何資訊。
- 未送出 Accept 標頭時，測試即使帶有現代格式參數仍收到 JPEG；除錯與快取若忽略 Vary: Accept，便可能誤判格式。