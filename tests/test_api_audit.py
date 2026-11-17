import json

import pytest

from pipeline import api_audit as A


def test_shards_cover_every_row_once():
    rows = [{"slug": str(i)} for i in range(10)]
    parts = [A.shard(rows, f"{i}/3") for i in (1, 2, 3)]
    assert sorted(r["slug"] for p in parts for r in p) == sorted(r["slug"] for r in rows)
    assert A.shard(rows, "") == rows


@pytest.mark.parametrize("spec", ["0/3", "4/3", "x/3"])
def test_bad_shard_is_refused(spec):
    with pytest.raises(ValueError):
        A.shard([{"slug": "a"}], spec)


def test_reports_read_only_their_own_rows(tmp_path, monkeypatch):
    results = tmp_path / "articles"
    results.mkdir()
    for slug in ("a", "b", "c"):
        (results / f"{slug}.json").write_text(json.dumps({"slug": slug}), "utf-8")
    monkeypatch.setattr(A, "RESULTS", results)
    rows_file = tmp_path / "sample.json"
    rows_file.write_text(json.dumps({"rows": [{"slug": "c"}, {"slug": "a"}, {"slug": "not-yet"}]}), "utf-8")
    assert [r["slug"] for r in A.load_results(rows_file)] == ["a", "c"]
