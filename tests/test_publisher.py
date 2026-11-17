import logging

import frontmatter

from pipeline.build.publisher import publish_article


SOURCE_SENTENCE = "Distinctive source prose must never appear in a republished news body."


def make_post(**metadata):
    defaults = {
        "title": "Test article",
        "published": "2026-11-14T00:00:00+00:00",
        "summary": "Our short comment.",
        "key_points_en": ["One original key point."],
        "hot_take_en": "This is why the development matters.",
        "sources": [{"name": "Example", "url": "https://example.com/story"}],
    }
    defaults.update(metadata)
    return frontmatter.Post(f"# Test article\n\n{SOURCE_SENTENCE}\n" * 20, **defaults)


def test_news_uses_original_sections_and_never_source_content(tmp_path):
    path = publish_article(make_post(), str(tmp_path), "en", "news")
    output = frontmatter.load(path)
    assert SOURCE_SENTENCE not in output.content
    assert "Our short comment." in output.content
    assert "One original key point." in output.content
    assert "This is why the development matters." in output.content
    assert "https://example.com/story" in output.content
    assert output["safeForPublic"] is True


def test_zh_news_requires_and_uses_chinese_comment(tmp_path, caplog):
    post = make_post(
        summary="English fallback must not be used",
        summary_zh="這是繁體中文短評。",
        key_points_zh=["這是繁體中文重點。"],
        hot_take_zh="這就是值得注意的原因。",
    )
    path = publish_article(post, str(tmp_path), "zh", "news")
    output = frontmatter.load(path)
    assert "這是繁體中文短評。" in output.content
    assert "這是繁體中文重點。" in output.content
    assert "English fallback" not in output.content
    assert SOURCE_SENTENCE not in output.content

    with caplog.at_level(logging.WARNING):
        skipped = publish_article(make_post(summary_zh=""), str(tmp_path), "zh", "news")
    assert skipped is None
    assert "Skipping zh news" in caplog.text

    english_only = publish_article(
        make_post(summary_zh="English text mislabeled as Chinese"),
        str(tmp_path),
        "zh",
        "news",
    )
    assert english_only is None


def test_analysis_keeps_original_body_and_strips_duplicate_h1(tmp_path):
    post = make_post()
    path = publish_article(post, str(tmp_path), "en", "analysis")
    output = frontmatter.load(path)
    assert not output.content.startswith("# Test article")
    assert SOURCE_SENTENCE in output.content
    assert output["safeForPublic"] is True
