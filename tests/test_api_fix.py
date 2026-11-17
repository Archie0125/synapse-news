import frontmatter
import pytest

from pipeline import api_fix as F

EN = (
    '---\n'
    'title: "OpenAI Releases First Open-Weight Models"\n'
    'summary: "OpenAI released two models on April 4, 2026."\n'
    'category: "ai-ml"\n'
    'publishedAt: 2026-04-05T10:15:00Z\n'
    'lang: "en"\n'
    'tags:\n  - "openai"\n'
    '---\n\n'
    'Seven years after GPT-2, OpenAI is back. On April 4, 2026, it published two models. They are big.\n\n'
    '## The Models\n\n'
    'It is the first open model in years.\n\n'
    '- One item. Another item.\n'
)

ZH = (
    '---\n'
    'title: "OpenAI 七年首度開源"\n'
    'summary: "OpenAI 於 2026 年 4 月 4 日發布兩款模型。"\n'
    'publishedAt: 2026-04-05T10:15:00Z\n'
    'lang: "zh"\n'
    '---\n\n'
    'OpenAI 於 2026 年 4 月 4 日發布兩款模型。這是多年來首款開放模型。\n'
)


def test_only_named_sentences_change_and_the_rest_is_byte_identical():
    fm, body = F.apply_en(EN, [
        {"kind": "summary", "old": "OpenAI released two models on April 4, 2026.", "new": "OpenAI released two models in August 2025."},
        {"kind": "body", "old": "On April 4, 2026, it published two models.", "new": "In August 2025, it published two models."},
        {"kind": "body", "old": "It is the first open model in years.", "new": ""},
        {"kind": "heading", "old": "The Models", "new": "The models"},
    ])
    out = F.finish(fm, body, F.note_en(4))
    assert "Seven years after GPT-2, OpenAI is back. In August 2025, it published two models. They are big.\n" in out
    assert "first open model" not in out
    assert "## The models\n\n- One item. Another item.\n" in out  # the emptied paragraph is gone, no triple newline
    assert "\n\n\n" not in out
    post = frontmatter.loads(out)
    assert post["summary"] == "OpenAI released two models in August 2025."
    assert post["title"] == "OpenAI Releases First Open-Weight Models"
    assert str(post["modifiedAt"]).startswith("2026-11-15")
    assert out.endswith("4 sentences were corrected or removed to match the sources listed on this page.*\n")
    # everything before the summary line and the tags are untouched
    assert out.startswith('---\ntitle: "OpenAI Releases First Open-Weight Models"\n')
    assert 'publishedAt: 2026-04-05T10:15:00Z\nmodifiedAt: 2026-11-15T00:00:00Z\nlang: "en"\ntags:\n  - "openai"\n---\n' in out


def test_deleting_inside_a_sentence_run_keeps_single_spaces():
    fm, body = F.apply_en(EN, [{"kind": "body", "old": "On April 4, 2026, it published two models.", "new": ""}])
    assert "Seven years after GPT-2, OpenAI is back. They are big.\n" in body


def test_list_item_emptied_is_removed():
    fm, body = F.apply_en(EN, [{"kind": "body", "old": "One item.", "new": ""},
                              {"kind": "body", "old": "Another item.", "new": ""}])
    assert "\n- " not in body and "\n-\n" not in body
    assert body.rstrip().endswith("It is the first open model in years.")


@pytest.mark.parametrize("change", [
    {"kind": "body", "old": "not in the article.", "new": "x"},
    {"kind": "title", "old": "OpenAI Releases First Open-Weight Models", "new": ""},
    {"kind": "summary", "old": "a different summary", "new": "x"},
    {"kind": "heading", "old": "The Models", "new": ""},
])
def test_unplaceable_changes_are_refused(change):
    with pytest.raises(F.Skip):
        F.apply_en(EN, [change])


def test_a_sentence_that_occurs_twice_is_refused():
    with pytest.raises(F.Skip):
        F.replace_once("A b. A b.", "A b.", "C.")


def test_title_with_quotes_round_trips_through_yaml():
    fm, _ = F.split_doc(EN)
    fm2 = F.fm_set(fm, "title", 'OpenAI\'s "gpt-oss" models')
    assert F.fm_get(fm2, "title") == 'OpenAI\'s "gpt-oss" models'
    assert frontmatter.loads(fm2 + "body\n")["title"] == 'OpenAI\'s "gpt-oss" models'


def test_zh_edits_need_a_unique_fragment_and_keep_frontmatter_valid():
    fm, body, problems = F.apply_zh(ZH, [
        {"change": 1, "old": "OpenAI 於 2026 年 4 月 4 日發布兩款模型。這是", "new": "OpenAI 於 2025 年 8 月發布兩款模型。這是"},
        {"change": 2, "old": "於 2026 年 4 月 4 日發布兩款模型。", "new": "於 2025 年 8 月發布兩款模型。"},  # also in body -> refused
        {"change": 3, "old": "不存在的片段", "new": "x"},
    ])
    assert "2025 年 8 月發布兩款模型。這是多年來首款開放模型" in body
    assert len(problems) == 2
    post = frontmatter.loads(fm + body)
    assert post["summary"] == "OpenAI 於 2026 年 4 月 4 日發布兩款模型。"


def test_zh_summary_edit_in_frontmatter():
    fm, body, problems = F.apply_zh(ZH, [{"change": 1, "old": "七年首度開源", "new": "推出 \"gpt-oss\" 開放模型"}])
    assert not problems
    assert frontmatter.loads(fm + body)["title"] == 'OpenAI 推出 "gpt-oss" 開放模型'


def test_overlapping_change_is_skipped_not_fatal():
    plan = [{"kind": "body", "old": "On April 4, 2026, it published two models.", "new": "In August 2025, it published two models."},
            {"kind": "body", "old": "it published two models.", "new": "it released two models."}]
    fm, body = F.apply_en(EN, plan, strict=False)
    assert "In August 2025, it published two models." in body
    assert "unplaced" in plan[1] and "unplaced" not in plan[0]
    with pytest.raises(F.Skip):
        F.apply_en(EN, [dict(p) for p in plan[:1]] + [{"kind": "body", "old": "nope", "new": "x"}])


def test_crlf_article_round_trips_with_its_own_line_ends():
    crlf = EN.replace("\n", "\r\n")
    lf = crlf.replace("\r\n", "\n")
    fm, body = F.apply_en(lf, [{"kind": "body", "old": "They are big.", "new": "They are large."}])
    out = F.finish(fm, body, F.note_en(1)).replace("\n", "\r\n")
    assert "\r\n" in out and "\n" not in out.replace("\r\n", "")
    assert out.startswith("---\r\ntitle:")


def test_zh_correction_note_is_found_and_replaced():
    fm, body, _ = F.apply_zh(ZH, [])
    once = F.finish(fm, body, F.note_zh(2))
    m = F.ZH_NOTE_RE.search(once)
    assert m and m.group(1) == "2"
    base = once[:m.start()] + "\n"
    fm2, body2 = F.split_doc(base)
    twice = F.finish(fm2, body2, F.note_zh(5))
    assert twice.count("*更正（") == 1 and "更正或刪除 5 處" in twice
