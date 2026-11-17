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
        [{"ts": "2026-11-13T00:00:00+00:00", "run": "a", "mode": "week", "usd": D.CAPS["week_total"] - 0.1}]))
    wk = D.Ledger(tmp_path / "w.json", "week", "r3", date(2026, 11, 13))
    with pytest.raises(D.BudgetExceeded):
        wk.reserve(0.2, "x")
    # audits have their own cap and do not eat into the recap budget (or vice versa)
    (tmp_path / "a.json").write_text(json.dumps(
        [{"ts": "2026-11-13T00:00:00+00:00", "run": "a", "mode": "week", "usd": D.CAPS["week_total"]},
         {"ts": "2026-11-13T00:00:00+00:00", "run": "b", "mode": "audit", "usd": D.CAPS["audit_total"] - 0.1}]))
    au = D.Ledger(tmp_path / "a.json", "audit", "r4", date(2026, 11, 13))
    au.reserve(0.05, "x")
    with pytest.raises(D.BudgetExceeded):
        au.reserve(0.2, "y")


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
    a.reserve(D.CAPS["week_total"] - 1.0, "write")
    with pytest.raises(D.BudgetExceeded):
        b.reserve(1.5, "write")


def test_cached_fetcher_replays_only_the_failed_runs_sources():
    f = D.CachedFetcher({"https://a.example/x": {"url": "https://a.example/x", "final_url": "https://a.example/x",
                                                  "site": "a.example", "title": "T", "date": "2026-10-05",
                                                  "text": "one two three"}})
    hit = f.fetch("https://a.example/x")
    assert hit["ok"] and hit["date"] == date(2026, 10, 5) and hit["words"] == 3
    miss = f.fetch("https://b.example/y")
    assert not miss["ok"] and miss["date"] is None


def test_backfill_false_positives_units_twice_and_title_abbreviations():
    # Each of these blocked a correct weekly recap on 2026-11-13.
    assert not G.check_numbers("修補數達到 2.6x", ["Flash Cyber produced 2.6 times more correct patches."], "zh")
    assert not G.check_numbers("耗電約 167 kW", ["Each rack draws about 167 kilowatts."], "zh")
    assert not G.check_numbers("約 6 GW 的容量", ["a site with 6 gigawatts of capacity"], "zh")
    assert G.check_numbers("耗電約 176 kW", ["Each rack draws about 167 kilowatts."], "zh")
    assert not G.check_numbers("速度將近兩倍", ["models improving nearly twice as fast"], "zh")
    assert G.check_numbers("速度快三倍", ["models improving nearly twice as fast"], "zh")
    assert not G.check_numbers("雙方會面 3 次", ["The two met 3 times this year."], "zh")
    assert not G.check_numbers("up to 4.5 times the AI performance", ["up to 4.5-times faster AI performance"], "en")


def test_review_cases_for_the_backfill_gate_changes():
    # Fable and Codex review, 2026-11-13: none of these may pass...
    assert G.check_numbers("營收成長兩倍", ["Nvidia doubled down on its AI bet this quarter."], "zh")
    assert G.check_numbers("速度快 2 倍", ["The launch has twice been delayed."], "zh")
    assert G.check_numbers("Performance improved 2x.", ["The team met twice."], "en")
    assert G.check_numbers("裁員 40 人", ["The chip is 40x faster."], "zh")
    assert G.check_numbers("The company launched 3 products.", ["Performance improved 3x."], "en")
    assert G.check_numbers("performance rose 3x", ["The office at 3 Times Square opened."], "en")
    assert G.check_names("Many buyers chose General Motors.", ["Gen Z buyers prefer Ford Motors."])
    assert G.check_numbers("速度提升兩倍", ["The speaker doubles as a smart home hub."], "zh")
    assert G.check_numbers("Revenue increased 2x.", ["The CEO doubled over laughing."], "en")
    assert G.check_numbers("It is three times faster than before.", ["The firm shipped three models."], "en")
    # ...and none of these may be blocked.
    assert not G.check_numbers("a 6-gigawatt site", ["a site with 6 gigawatts of capacity"], "en")
    assert not G.check_numbers("採用 3 奈米製程", ["built on a 3 nanometer process"], "zh")
    assert not G.check_numbers("The two met 3 times", ["The two held 3 meetings this year."], "en")
    assert not G.check_numbers("In 2025 Times reporters found it", ["In 2025, reporters found it."], "en")
    assert not G.check_numbers("It is 2.6 Times Faster", ["It is 2.6 times faster."], "en")
    assert not G.check_names("California Governor Gavin Newsom signed it.",
                             ["On Friday, California Gov. Gavin Newsom signed the bill."])
    assert G.check_names("California Senator Gavin Newsom signed it.",
                         ["On Friday, California Gov. Gavin Newsom signed the bill."])


# ------------------------------------------------------------ audit of old articles

from pipeline import api_audit as A


def test_audit_missing_fact_is_an_error_only_when_every_source_was_read():
    assert A.classify("contradicted", all_read=False) == "hard_error"
    assert A.classify("not_in_sources", all_read=True) == "unsupported"
    assert A.classify("not_in_sources", all_read=False) == "undetermined"
    assert A.classify("supported", all_read=False) == "supported"


def test_audit_sample_is_half_after_the_cliff_and_reproducible():
    arts = [{"slug": f"a{i}", "date": date(2026, 4, 3) + timedelta(days=i % 121)} for i in range(900)]
    s1 = A.draw_sample(arts, 40, 7)
    s2 = A.draw_sample(arts, 40, 7)
    assert s1 == s2 and len(s1) == 40 and len({r["slug"] for r in s1}) == 40
    assert sum(r["stratum"] == "after-7/17" for r in s1) == 20


def test_audit_units_cover_title_summary_headings_and_sentences():
    a = {"title": "T", "summary": "S.", "body": "Intro one. Intro two.\n\n## Head\n\nBody sentence."}
    units = A.audit_units(a)
    assert [u["where"] for u in units] == ["title", "summary", "intro", "intro", "heading", "Head"]
    assert [u["id"] for u in units] == list(range(1, 7))


def test_wilson_interval_bounds():
    lo, hi = A.wilson(0, 59)
    assert lo == 0.0 and 0.05 < hi < 0.07
    lo, hi = A.wilson(30, 100)
    assert 0.21 < lo < 0.23 and 0.39 < hi < 0.41


def test_audit_source_dated_after_the_article_is_not_evidence():
    page = {"ok": True, "words": 500, "date": date(2026, 6, 20), "reason": ""}
    assert not A.readable_now(dict(page), date(2026, 6, 15))
    assert A.readable_now(dict(page), date(2026, 6, 20))
    assert not A.readable_now({**page, "words": 50}, date(2026, 7, 1))
    assert A.readable_now({**page, "date": None}, date(2026, 6, 15))


# ------------------------------------------------------------ adding a day to a recap

RECAP_EN = ("Opening.\n\n## Tuesday, August 4\n\nA [S1].\n\n## Thursday, August 6\n\nB [S2].\n\n"
            "## Also this week\n\nC [S3].\n\n## What to Watch\n\n- D")


def test_insert_day_section_goes_in_date_order():
    out = G.insert_day_section(RECAP_EN, "## Wednesday, August 5\n\nNew [S4].", date(2026, 8, 5))
    assert out.index("August 4") < out.index("August 5") < out.index("August 6")
    late = G.insert_day_section(RECAP_EN, "## Saturday, August 8\n\nNew [S4].", date(2026, 8, 8))
    assert late.index("August 6") < late.index("August 8") < late.index("Also this week")
    zh = "開場。\n\n## 8 月 4 日（週二）\n\n甲 [S1]。\n\n## 值得關注\n\n- 乙"
    out_zh = G.insert_day_section(zh, G.day_heading(date(2026, 8, 5), "zh") + "\n\n新 [S2]。", date(2026, 8, 5))
    assert out_zh.index("8 月 4 日") < out_zh.index("8 月 5 日（週三）") < out_zh.index("值得關注")
    with pytest.raises(ValueError):
        G.insert_day_section(RECAP_EN, "## Tuesday, August 4\n\nx", date(2026, 8, 4))


def test_shift_markers_appends_after_existing_sources():
    assert G.shift_markers("A [S1]. B [S1][S2]. C [S1, S2].", 7) == "A [S8]. B [S8][S9]. C [S8, S9]."
    assert G.day_heading(date(2026, 8, 5), "en") == "## Wednesday, August 5"
    assert G.heading_day("## Wednesday, August 5", 2026) == date(2026, 8, 5)


def test_insert_also_paragraph_appends_or_creates_the_section():
    out = G.insert_also_paragraph(RECAP_EN, "Reported on August 5: E [S4].", "en")
    assert out.index("C [S3]") < out.index("Reported on August 5") < out.index("What to Watch")
    no_also = "Opening.\n\n## Tuesday, August 4\n\nA [S1].\n\n## What to Watch\n\n- D"
    out2 = G.insert_also_paragraph(no_also, "Reported on August 5: E [S2].", "en")
    assert out2.index("A [S1]") < out2.index("## Also this week") < out2.index("Reported on") < out2.index("What to Watch")


def test_audit_weighting_and_unchecked_articles():
    def art(stratum, verdicts):
        return {"status": "checked", "stratum": stratum, "all_read": True,
                "units": [{"verdict": v} for v in verdicts]}
    results = [art("2026-05", ["hard_error"]), art("2026-05", ["supported"]),
               art("after-7/17", ["supported"]), art("after-7/17", ["supported"])]
    est, lo, hi = A.weighted(results, A.HARD, {"before": 900, "after": 100})
    assert abs(est - 0.45) < 1e-9          # 0.9 * 1/2 + 0.1 * 0/2, not the unweighted 1/4
    assert not A.is_checked({"status": "checked", "units": [{"verdict": "unchecked"}]})
    s = A.summarize([art("2026-05", ["unsupported"])])
    assert s["articles_with_hard_error"] == 0 and s["articles_with_any_error"] == 1


def test_audit_weighting_does_not_invent_certainty():
    def art(stratum, v):
        return {"status": "checked", "stratum": stratum, "all_read": True, "units": [{"verdict": v}]}
    est, lo, hi = A.weighted([art("2026-05", "supported"), art("after-7/17", "supported")], A.HARD,
                             {"before": 500, "after": 500})
    assert est == 0 and hi > 0.2                       # one clean article per stratum is not "<5%"
    only_after = [art("after-7/17", "hard_error")] * 5 + [art("after-7/17", "supported")] * 5
    est, lo, hi = A.weighted(only_after, A.HARD, {"before": 990, "after": 10})
    assert (lo, hi) == (0.0, 1.0) and A.decision(lo, hi, 10).startswith("no estimate")
