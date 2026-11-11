"""Run every own check (store/*/<id>/check.py) once and record the result of each function.

    python -m tp.checkruns [--store store] [--out site/check_runs.json] [--jobs 2] [--ids a,b]

Each check file runs in its own process. A function passes when it returns without raising,
does not return False and records no GA.check failure (the evidence layer's rule). The record
keeps, per function: pass or fail, wall time, the premises it touched and the error text. The
Physics Graph page shows these records beside the check's source as the last recorded run.
"""
import argparse
import datetime
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

RUNNER = r'''
import importlib.util, io, json, os, sys, time, traceback, contextlib
lab, path = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(lab, "lib"))
import tp_premise, GA
tp_premise.configure(os.path.join(lab, "store"))
sys.path.insert(0, os.path.dirname(path))
out = {"functions": [], "load_error": None}
buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf):
        spec = importlib.util.spec_from_file_location("check_under_test", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
except Exception:
    out["load_error"] = traceback.format_exc()[-1500:]
    print(json.dumps(out)); sys.exit(0)
for name in sorted(n for n in dir(mod) if n.startswith("check_") and callable(getattr(mod, n))):
    tp_premise.TOUCHED.clear(); nfail = len(GA.FAILURES); err = None; buf = io.StringIO()
    t0 = time.perf_counter()
    try:
        with contextlib.redirect_stdout(buf):
            r = getattr(mod, name)()
        if r is False:
            err = "returned False"
        elif len(GA.FAILURES) > nfail:
            err = "GA.check failure: " + "; ".join(GA.FAILURES[nfail:])
    except Exception:
        err = traceback.format_exc()[-1500:]
    out["functions"].append({"name": name, "ok": err is None,
                             "ms": int((time.perf_counter() - t0) * 1000),
                             "touched": sorted(tp_premise.TOUCHED), "error": err,
                             "stdout": buf.getvalue()[-800:]})
print(json.dumps(out))
'''


def _check_files(store):
    for sub in ("claims", "objects", "predictions", "questions"):
        base = os.path.join(store, sub)
        if not os.path.isdir(base):
            continue
        for d in sorted(os.listdir(base)):
            f = os.path.join(base, d, "check.py")
            if os.path.exists(f):
                yield d, f


def run_one(lab, path, timeout=600):
    try:
        cp = subprocess.run([sys.executable, "-c", RUNNER, lab, os.path.abspath(path)],
                            capture_output=True, text=True, timeout=timeout, cwd=lab)
        return json.loads(cp.stdout.strip().splitlines()[-1])
    except subprocess.TimeoutExpired:
        return {"functions": [], "load_error": f"timeout after {timeout}s"}
    except Exception as exc:  # noqa: BLE001
        return {"functions": [], "load_error": f"runner error: {exc}"}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", default="store")
    ap.add_argument("--out", default=os.path.join("site", "check_runs.json"))
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--ids", default="")
    if argv and argv[0] == "checkruns":
        argv = argv[1:]
    a = ap.parse_args(argv)
    lab = os.path.dirname(os.path.abspath(a.store))
    want = set(x for x in a.ids.split(",") if x)
    files = [(i, f) for i, f in _check_files(a.store) if not want or i in want]
    old = {}
    if want and os.path.exists(a.out):
        old = json.load(open(a.out)).get("runs", {})
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        res = list(ex.map(lambda x: (x[0], run_one(lab, x[1])), files))
    runs = dict(old)
    runs.update({i: r for i, r in res})
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    for i, _ in res:
        runs[i]["ran_at"] = now
    json.dump({"python": sys.version.split()[0], "runs": runs}, open(a.out, "w"), indent=0)
    nf = sum(len(r["functions"]) for r in runs.values())
    bad = [(i, f["name"]) for i, r in runs.items() for f in r["functions"] if not f["ok"]]
    bad += [(i, "load") for i, r in runs.items() if r.get("load_error")]
    print(f"{len(runs)} check files, {nf} functions, {len(bad)} failing")
    for b in bad[:40]:
        print("FAIL", *b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
