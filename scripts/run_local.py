"""Local scheduled runner: probe subscription CLIs, run pipeline via router.

Usage: .venv/bin/python scripts/run_local.py [--probe-only] [--phase X]
Exit codes: 0 ok / empty, 2 no provider available, 3 LLM calls all failed, 1 crash.
"""
import argparse, asyncio, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "scripts"))
import os; os.chdir(ROOT)
import sub_router as R


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe-only", action="store_true")
    ap.add_argument("--phase", default="all")
    a = ap.parse_args()
    res = R.probe()
    print("PROBE", json.dumps(res, ensure_ascii=False, indent=1))
    live = [k for k, v in res.items() if v == "ok"]
    if a.probe_only:
        return 0 if live else 2
    if not live:
        R._log({"purpose": "run", "status": "aborted_no_provider", "probe": res})
        print("NO PROVIDER AVAILABLE - aborting before fetch", file=sys.stderr)
        return 2
    os.environ["ROUTER_ORDER"] = ",".join(live)  # only use providers that passed probe
    R.install()
    from pipeline import main as P
    if a.phase == "all":
        asyncio.run(P.run_full_pipeline("config.yaml"))
    else:
        sys.argv = ["pipeline", "--phase", a.phase]; P.main()
    R._log({"purpose": "run", "status": "done", "stats": R.STATS})
    print("STATS", json.dumps(R.STATS))
    if R.STATS["calls"] and not R.STATS["ok"]:
        return 3
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        R._log({"purpose": "run", "status": "crash", "error": str(e)[:500]})
        raise
