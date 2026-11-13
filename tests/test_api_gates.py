from datetime import date, timedelta
import json

import httpx
import pytest

from pipeline import api_gates as G
from pipeline import api_daily as D
from pipeline.api_fetch import Fetcher, page_meta


# ------------------------------------------------------------ numbers

SRC = ("Acme said revenue reached $1.23 billion in 2026, up 30% from a year earlier. "
       "The chip is 2.5x faster and costs $120. It shipped on August 4. Margins hit 29.6 percent.")


def nums(article, pool=(SRC,)):
    return G.check_numbers(article, list(pool), "en")


def test_number_boundaries_do_not_match_inside_other_numbers():
    assert nums("Prices start at $12.")  # 12 is not in "$120" or "2026"
    assert not nums("The chip costs $120.")
    assert nums("Founded in 2012.")      # 2012 appears nowhere in the source


def test_units_convert_between_billion_and_yi():
    assert not G.check_numbers("營收達 12 億美元", [SRC], "zh")        # 1.23 billion rounds to 12 億
    assert not nums("Revenue was about $1.2 billion.")
    assert G.check_numbers("營收達 15 億美元", [SRC], "zh")


def test_percent_multiple_and_spelled_out():
    assert not nums("Revenue grew 30%.")
    assert not G.check_numbers("營收成長三成", [SRC], "zh")            # 三成 == 30%
    assert not G.check_numbers("速度快 2.5 倍", [SRC], "zh")
    assert G.check_numbers("速度快兩倍", [SRC], "zh")                  # 2x is not in the source
    assert nums("It is twelve billion strong.")
    assert nums("Margins hit 31%.")
    assert not nums("Margins hit 30%.")                               # 29.6% rounds to 30%


def test_dates_and_months():
    assert not nums("It shipped on August 4.")
    assert not G.check_numbers("8 月 4 日上市", [SRC], "zh")
    assert nums("It shipped on August 5.")
    assert G.check_numbers("9 月上市", [SRC], "zh")


def test_title_and_summary_numbers_are_checked_and_list_numbers_are_not():
    article = "Acme Hits $9 Billion\n\n1. First point\n2. Second point"
    fails = nums(article)
    assert any("9" in f for f in fails)
    assert not any("「1" in f or "「2" in f for f in fails)


def test_urls_in_links_are_not_numbers():
    assert not nums("See [the filing](https://example.com/2024/07/99/report).")


def test_vague_chinese_amounts_are_not_figures():
    assert not G.check_numbers("市場規模數十億美元", [SRC], "zh")


# ------------------------------------------------------------ quotes & names

QSRC = 'Jane Doe, chief executive of Acme, said: "We will ship the new model to every customer this year."'


def test_english_quotes_must_be_verbatim():
    assert not G.check_quotes_en('She said "We will ship the new model to every customer this year."', [QSRC], "en")
    assert G.check_quotes_en('She said "We will ship the new model to all customers soon."', [QSRC], "en")
    assert not G.check_quotes_en('a so-called "agentic" model', [QSRC], "en")  # short scare quotes ignored


def test_chinese_quotes_need_a_verbatim_original():
    good = [{"zh": "我們今年會把新模型交付給每一位客戶", "original": "We will ship the new model to every customer this year."}]
    zh = "她說：「我們今年會把新模型交付給每一位客戶」"
    assert not G.check_quotes_zh(zh, good, [QSRC])
    bad = [{"zh": "我們今年會把新模型交付給每一位客戶", "original": "We are shipping everything now."}]
    assert G.check_quotes_zh(zh, bad, [QSRC])
    assert G.check_quotes_zh(zh, [], [QSRC])


def test_names_must_come_from_sources():
    assert not G.check_names("Acme chief executive Jane Doe said the model ships soon.", [QSRC])
    assert G.check_names("Judge Donovan Frank rejected the request.", [QSRC])
    assert not G.check_names("In August the company shipped.", [QSRC])  # sentence-initial words, months


# ------------------------------------------------------------ copying

def test_english_copy_twelve_words_but_quotes_allowed():
    src = "The company said the new accelerator delivers twice the throughput of its predecessor at the same power."
    copied = "Notably the new accelerator delivers twice the throughput of its predecessor at the same power."
    assert G.check_copy_en(copied, [src], "en")
    quoted = 'It said "the new accelerator delivers twice the throughput of its predecessor at the same power."'
    assert not G.check_copy_en(quoted, [src], "en")


def test_chinese_copy_against_chinese_sources():
    src = "台積電今天宣布在高雄新建兩奈米晶圓廠，預計明年第三季開始量產並供應主要客戶。" * 10
    assert G.check_copy_zh("報導指出台積電今天宣布在高雄新建兩奈米晶圓廠，預計明年量產。", [src])
    assert not G.check_copy_zh("台積電要在高雄蓋新廠，明年就要量產。", [src])


# ------------------------------------------------------------ sources, freshness, duplicates

def test_sources_must_be_in_the_search_allowlist():
    allow = {G._normalize_url("https://a.com/x"), G._normalize_url("https://b.com/y")}
    used = [{"url": "https://a.com/x", "ok": True, "words": 800},
            {"url": "https://c.com/z", "ok": True, "words": 800}]
    fails = G.check_sources(used, allow)
    assert any("c.com" in f for f in fails)
    ok = [{"url": "https://a.com/x?utm_source=t", "ok": True, "words": 800},
          {"url": "https://b.com/y", "ok": True, "words": 800}]
    assert not G.check_sources(ok, allow)


def test_daily_freshness():
    run = date(2026, 11, 13)
    assert not G.fresh_daily([date(2026, 11, 12), None], run)
    assert G.fresh_daily([date(2026, 11, 1), None], run)
    assert G.fresh_daily([None], run)


def test_week_item_dates_do_not_slip_across_weeks():
    ws, we = date(2026, 8, 10), date(2026, 8, 16)
    assert G.item_fresh(date(2026, 8, 12), [date(2026, 8, 12)], ws, we)
    assert not G.item_fresh(date(2026, 8, 17), [date(2026, 8, 17)], ws, we)   # next Monday
    assert not G.item_fresh(date(2026, 8, 12), [date(2026, 7, 1)], ws, we)     # stale source
    assert not G.item_fresh(date(2026, 8, 12), [None], ws, we)


def test_duplicates_chinese_bigrams_and_recent_tags():
    run = date(2026, 11, 13)
    recent = [
        {"title": "OpenAI 調降 GPT-5.6 Luna API 價格八成", "lang": "zh", "tags": [], "sources": [], "date": run},
        {"title": "Something else", "lang": "en", "tags": ["OpenAI", "GPT-5.6", "pricing"],
         "sources": ["https://x.com/a"], "date": run - timedelta(days=3)},
    ]
    assert G.check_duplicate("t", "OpenAI 調降 GPT-5.6 Luna API 價格", [], [], recent, run)
    assert G.check_duplicate("t", "完全不同", ["openai", "gpt-5.6", "pricing"], [], recent, run)
    assert G.check_duplicate("t", "完全不同", [], ["https://x.com/a?utm_source=z"], recent, run)
    assert not G.check_duplicate("t", "完全不同", ["nvidia"], [], recent, run)


def test_query_mentions_day():
    d = date(2026, 8, 4)
    assert G.query_mentions_day("AI news August 4 2026", d)
    assert G.query_mentions_day("AI 新聞 8月4日", d)
    assert not G.query_mentions_day("AI news August 14 2026", d)


# ------------------------------------------------------------ format

def good_draft(**over):
    body_en = ("word " * 650) + "\n\n## What to Watch\nmore."
    body_zh = ("字" * 1000) + "\n\n## 值得關注\n更多。"
    d = {"title_en": "A title", "summary_en": "One line.", "body_en": body_en, "title_zh": "標題",
         "summary_zh": "一句話。", "body_zh": body_zh, "category": "ai-ml", "tags": ["a", "b", "c"],
         "slug": "acme-new-chip", "related_slugs": [], "zh_quotes": []}
    d.update(over)
    return d


def test_format_ranges_banned_words_and_related():
    assert not G.check_format(good_draft(), (600, 1200), (900, 2600), set())
    assert G.check_format(good_draft(body_en="short\n## What to Watch"), (600, 1200), (900, 2600), set())
    assert G.check_format(good_draft(summary_en="A crucial step."), (600, 1200), (900, 2600), set())
    assert G.check_format(good_draft(related_slugs=["nope"]), (600, 1200), (900, 2600), {"yes"})
    assert G.check_format(good_draft(category="crypto"), (600, 1200), (900, 2600), set())


# ------------------------------------------------------------ fetching

def make_fetcher(routes):
    def handler(request: httpx.Request):
        key = str(request.url)
        if key not in routes:
            return httpx.Response(404)
        r = routes[key]
        return r() if callable(r) else r
    client = httpx.Client(transport=httpx.MockTransport(handler))
    return Fetcher(client=client, sleep=lambda s: None)


ARTICLE_HTML = ("<html><head><title>T</title>"
                "<meta property='article:published_time' content='2026-08-04T10:00:00Z'>"
                "<meta property='article:modified_time' content='2026-11-10T10:00:00Z'>"
                "</head><body><article><p>" + ("Acme shipped a chip. " * 60) + "</p></article></body></html>")


def test_robots_checked_on_every_redirect_hop():
    f = make_fetcher({
        "https://a.com/robots.txt": httpx.Response(200, text="User-agent: *\nAllow: /\n"),
        "https://a.com/story": httpx.Response(301, headers={"location": "https://b.com/story"}),
        "https://b.com/robots.txt": httpx.Response(200, text="User-agent: *\nDisallow: /\n"),
        "https://b.com/story": httpx.Response(200, html=ARTICLE_HTML),
    })
    out = f.fetch("https://a.com/story")
    assert not out["ok"] and "robots" in out["reason"] and "b.com" in out["reason"]


def test_403_is_final_and_robots_403_blocks_everything():
    f = make_fetcher({"https://a.com/robots.txt": httpx.Response(403)})
    assert "robots" in f.fetch("https://a.com/x")["reason"]
    g = make_fetcher({"https://a.com/robots.txt": httpx.Response(404),
                      "https://a.com/x": httpx.Response(403)})
    assert g.fetch("https://a.com/x")["reason"] == "HTTP 403"


def test_size_cap():
    big = "<html><body>" + "x" * 2_100_000 + "</body></html>"
    f = make_fetcher({"https://a.com/robots.txt": httpx.Response(404),
                      "https://a.com/x": httpx.Response(200, html=big)})
    assert "larger" in f.fetch("https://a.com/x")["reason"]


def test_original_date_not_modified_date():
    d, _, _ = page_meta(ARTICLE_HTML, "https://a.com/story")
    assert d == date(2026, 8, 4)
    f = make_fetcher({"https://a.com/robots.txt": httpx.Response(404),
                      "https://a.com/story": httpx.Response(200, html=ARTICLE_HTML)})
    out = f.fetch("https://a.com/story")
    assert out["ok"] and out["date"] == date(2026, 8, 4)


def test_non_http_redirect_rejected():
    f = make_fetcher({"https://a.com/robots.txt": httpx.Response(404),
                      "https://a.com/x": httpx.Response(302, headers={"location": "ftp://a.com/x"})})
    assert f.fetch("https://a.com/x")["reason"] == "non-http redirect"


# ------------------------------------------------------------ budget & expiry

def test_reserve_refuses_before_calling_and_failures_are_recorded(tmp_path):
    led = D.Ledger(tmp_path / "ledger.json", "daily", "r1", date(2026, 11, 13))
    led.record("research", "claude-sonnet-5-5", None, ok=False, note="400")
    assert json.loads((tmp_path / "ledger.json").read_text())[0]["ok"] is False
    entries = json.loads((tmp_path / "ledger.json").read_text())
    entries.append({"ts": "2026-11-13T00:00:00+00:00", "run": "r1", "mode": "daily", "usd": 1.9})
    (tmp_path / "ledger.json").write_text(json.dumps(entries))
    with pytest.raises(D.BudgetExceeded):
        led.reserve(0.2, "write")
    led.reserve(0.05, "write")


def test_month_and_week_caps(tmp_path):
    (tmp_path / "l.json").write_text(json.dumps(
        [{"ts": "2026-11-02T00:00:00+00:00", "run": "old", "mode": "daily", "usd": 34.9}]))
    led = D.Ledger(tmp_path / "l.json", "daily", "r2", date(2026, 11, 13))
    with pytest.raises(D.BudgetExceeded):
        led.reserve(0.2, "x")
    (tmp_path / "w.json").write_text(json.dumps(
        [{"ts": "2026-11-13T00:00:00+00:00", "run": "a", "mode": "week", "usd": 39.9}]))
    wk = D.Ledger(tmp_path / "w.json", "week", "r3", date(2026, 11, 13))
    with pytest.raises(D.BudgetExceeded):
        wk.reserve(0.2, "x")


def test_unknown_fallback_model_is_priced_high():
    assert D.price_of("claude-something-new") == D.MAX_PRICE


def test_daily_refuses_without_renewal(tmp_path, monkeypatch):
    monkeypatch.setattr(D, "CONFIG", tmp_path / "config.json")
    assert D.main(["--mode", "daily"]) == 3
    (tmp_path / "config.json").write_text(json.dumps({"daily_until": "2026-01-01"}))
    assert D.main(["--mode", "daily"]) == 3


# ------------------------------------------------------------ false positives seen in the 2026-11-13 trial

def test_spelled_out_source_numbers_support_digits():
    assert not G.check_numbers("Only 3 locks work today.", ["Only three locks support it at launch."], "en")
    assert not G.check_numbers("目前只有 3 家廠商支援", ["目前只有三家廠商支援"], "zh")
    assert G.check_numbers("Only 4 locks work today.", ["Only three locks support it at launch."], "en")


def test_names_do_not_run_across_sentences_or_include_sentence_openers():
    src = ["Android Police reported the feature. Aliro locks from Nest Hub owners.", "Android Authority"]
    assert not G.check_names("It was spotted by Android Police. Your phone becomes a key.", src)
    assert not G.check_names("More Aliro locks are coming. Several Nest Hub models act as hubs.", src)
    assert not G.check_names("As Android Authority noted, the keys sync.", src)
    assert G.check_names("Engineer Maria Gomez built it.", src)


def test_chinese_brackets_for_terms_are_not_quotes():
    assert not G.check_quotes_zh("打開「Home 頁籤 > Google Wallet 卡片」就能設定", [], ["x"])
    assert G.check_quotes_zh("他說：「我們今年會把新模型交付給每一位客戶」", [], ["x"])


def test_product_name_lists_are_not_copying():
    src = "Supported hubs include the Nest Hub 2nd Gen Nest Hub Max Nest Wifi Pro and Google TV Streamer today."
    art = "You will need the Nest Hub 2nd Gen Nest Hub Max Nest Wifi Pro and Google TV Streamer as a hub."
    assert not G.check_copy_en(art, [src], "en")


def test_apply_edits_replaces_exactly_once_and_reports_misses():
    d = {"body_en": "Alpha is fine. Beta is wrong. Gamma.", "body_zh": "甲。乙錯了。"}
    out, probs = G.apply_edits(d, [
        {"field": "body_en", "old": "Beta is wrong. ", "new": ""},
        {"field": "body_zh", "old": "乙錯了。", "new": "乙對了。"},
        {"field": "body_en", "old": "Delta", "new": "x"},
        {"field": "nope", "old": "a", "new": "b"},
    ])
    assert out["body_en"] == "Alpha is fine. Gamma."
    assert out["body_zh"] == "甲。乙對了。"
    assert len(probs) == 2 and d["body_en"].startswith("Alpha is fine. Beta")


# ------------------------------------------------------------ source markers

def test_citations_required_for_facts_and_markers_must_exist():
    body = ("Nvidia said Huang resigned [S1]. Kress has been CFO since 2013. [S2]\n\n"
            "I think this matters a lot.\n\n## What to Watch\n- Results due Tuesday from Nvidia.")
    fails = G.check_citations(body, 2, "en")
    assert len(fails) == 1 and "Results due Tuesday" in fails[0]
    assert G.check_citations("Nvidia fell 12% [S3].", 2, "en")
    zh = "輝達表示黃仁勳辭職 [S1]。Kress 自 2013 年起擔任財務長。我認為這很重要。"
    fails = G.check_citations(zh, 2, "zh")
    assert len(fails) == 1 and "2013" in fails[0]


def test_tags_are_stripped_and_do_not_count_as_numbers():
    assert G.strip_tags("Shares fell 12% [S1][S2]. Kress steps in [S2].") == "Shares fell 12%. Kress steps in."
    assert G.strip_tags("輝達股價下跌 [S1]。") == "輝達股價下跌。"
    assert not G.check_numbers("Shares fell 12% [S2].", ["Shares fell 12% on Thursday."], "en")


def test_decimals_and_abbreviations_do_not_split_sentences():
    sents = G.tagged_sentences("The U.S. share was 1.5% [S1]. Next sentence here [S2].")
    assert [t for _, t in sents] == [{1}, {2}]


def test_title_case_units_and_combined_markers():
    assert not G.check_numbers("Oracle Raises $20 Billion", ["Oracle sought $20 billion from investors."], "en")
    body = "Valuation fell to $1.25 trillion [S1, S2]. Max costs $200 per month [S1,S3]."
    assert [t for _, t in G.tagged_sentences(body)] == [{1, 2}, {1, 3}]
    assert G.strip_tags(body) == "Valuation fell to $1.25 trillion. Max costs $200 per month."
    assert G.check_citations(body, 2, "en")  # S3 does not exist


def test_copy_check_lists_each_passage():
    src = ("the company said it would expand the program to every region next year according to people "
           "familiar with the plan. separately it said quarterly revenue rose on strong demand from cloud customers")
    art = ("Reportedly the company said it would expand the program to every region next year according to people. "
           "Also, separately it said quarterly revenue rose on strong demand from cloud customers today.")
    fails = G.check_copy_en(art, [src], "en")
    assert len(fails) == 2 and "rephrase" in fails[0]


def test_text_mentions_day():
    d = date(2026, 11, 4)
    assert G.text_mentions_day("On November 4, OpenAI introduced Images 2.6", d)
    assert G.text_mentions_day("announced Nov. 4 in a post", d)
    assert G.text_mentions_day("OpenAI 於 11 月 4 日推出", d)
    assert not G.text_mentions_day("On November 14 it shipped", d)
    assert not G.text_mentions_day("On November 5, METR published", d)


def test_source_states_day_by_weekday_or_today():
    tue = date(2026, 11, 3)
    assert G.source_states_day("OpenAI said on Tuesday that it would", date(2026, 11, 5), tue)
    assert not G.source_states_day("OpenAI said on Tuesday that it would", date(2026, 11, 12), tue)
    assert G.source_states_day("Today, Gemini is generally available", tue, tue)
    assert not G.source_states_day("Today, Gemini is generally available", date(2026, 11, 4), tue)


# ------------------------------------------------------------ Fable code review, 2026-11-13

def test_headings_are_review_units_and_hash_lines_are_text():
    d = {"title_en": "T", "summary_en": "S", "title_zh": "T", "summary_zh": "S",
         "body_en": "## Nvidia fires its CFO\nShares fell [S1].\n#1 seller Acme shipped 5 units.",
         "body_zh": "## 標題\n內容 [S1]。"}
    units = G.sentences_for_review(d)
    assert any(u["where"] == "heading" and "Nvidia fires" in u["text"] for u in units)
    assert any("#1 seller" in u["text"] for u in units)
    assert G.check_citations(d["body_en"], 1, "en")  # "#1 seller ..." is a sentence and needs a marker


def test_numbers_with_technical_units():
    src = ["The plant draws 1GW and the chip uses a 3nm process with 16 GB of memory."]
    assert G.check_numbers("It draws 10GW.", src, "en")
    assert G.check_numbers("A 2nm chip.", src, "en")
    assert not G.check_numbers("A 3nm chip with 16GB.", src, "en")


def test_multi_character_chinese_numerals_are_checked():
    assert G.check_numbers("公司裁員五千人", ["The company cut 3,000 jobs."], "zh")
    assert not G.check_numbers("公司裁員五千人", ["The company cut 5,000 jobs."], "zh")
    assert not G.check_numbers("千萬不要忽略", ["x"], "zh")


def test_chinese_quote_with_comma_or_trailing_verb():
    assert G.check_quotes_zh("黃仁勳說，「我們今年會把新模型交付給客戶」", [], ["x"])
    assert G.check_quotes_zh("「我們今年會把新模型交付給客戶」，黃仁勳表示", [], ["x"])


def test_links_and_long_week_titles_rejected():
    d = good_draft(body_en=("word " * 650) + "[site](https://x.com)\n## What to Watch")
    assert any("link" in f for f in G.check_format(d, (600, 1200), (900, 2600), set()))
    long = good_draft(title_en="x" * 95)
    assert G.check_format(long, (600, 1200), (900, 2600), set(), (88, 100))


def test_ledger_rereads_file_before_writing(tmp_path):
    path = tmp_path / "l.json"
    a = D.Ledger(path, "week", "a", date(2026, 11, 13))
    b = D.Ledger(path, "week", "b", date(2026, 11, 13))
    a.record("x", "claude-haiku-5-5", None, ok=True, usd_override=0.5)
    b.record("y", "claude-haiku-5-5", None, ok=True, usd_override=0.25)
    assert len(json.loads(path.read_text())) == 2


# ------------------------------------------------------------ Codex code review, 2026-11-13

def test_redirect_aliases_count_as_one_source():
    allow = {G._normalize_url("https://a.com/x"), G._normalize_url("https://b.com/y")}
    used = [{"url": "https://a.com/x", "final_url": "https://c.com/story", "ok": True, "words": 900},
            {"url": "https://b.com/y", "final_url": "https://c.com/story", "ok": True, "words": 900}]
    fails = G.check_sources(used, allow, min_total_words=900)
    assert any("1 readable source" in f for f in fails)


def test_reservation_is_on_disk_before_the_call_and_replaced_after(tmp_path):
    path = tmp_path / "l.json"
    led = D.Ledger(path, "week", "r", date(2026, 11, 13))
    led.reserve(1.5, "write")
    on_disk = json.loads(path.read_text())
    assert len(on_disk) == 1 and on_disk[0]["pending"] and on_disk[0]["usd"] == 1.5  # a crash here still counts
    led.record("write", "claude-opus-5-5", None, ok=True, usd_override=0.4)
    on_disk = json.loads(path.read_text())
    assert len(on_disk) == 1 and on_disk[0]["usd"] == 0.4 and "pending" not in on_disk[0]
    assert not (tmp_path / "l.lock").exists()


def test_second_process_sees_first_process_reservation(tmp_path):
    path = tmp_path / "l.json"
    a = D.Ledger(path, "week", "a", date(2026, 11, 13))
    b = D.Ledger(path, "week", "b", date(2026, 11, 13))
    a.reserve(39.0, "write")
    with pytest.raises(D.BudgetExceeded):
        b.reserve(1.5, "write")
