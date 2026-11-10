"""Run one result's machine checks and say whether they pass.

  python -m tp check-one ID [--store store]

For each `checked_by` item of the result:

  - kind check (`check.py::function`): runs the function exactly as layer 4 of `tp check` does
    (a separate interpreter, GA.py on the path, premises reached through premise());
  - kind legacy (a series verify script with tags): runs the script once (cached as layer 4
    caches it) and reports the checks whose labels carry the result's tags;
  - kind proof: a written proof, nothing to run; other kinds are listed as not run here.

It prints one line per check and exits 0 when every check that ran passed, 1 otherwise. It runs
no mutation test and compares no premises: `python -m tp check --store store --layers 4` does
the whole layer.
"""
import argparse
import os
import sys

from . import evidence
from .model import load_store


def command(eid, store="store"):
    """The command that checks one result, as shown to readers and agents."""
    return f"python -m tp check-one {eid} --store {store}"


def run(store_dir, eid, out=print):
    st = load_store(store_dir)
    e = st.entities.get(eid)
    if e is None:
        out(f"no result {eid!r} in {store_dir}")
        return 2
    from .validate import legacy_path
    legacy_dir = st.config.get("legacy_scripts_dir")
    cache = os.environ.get("TP_CACHE_DIR") or os.path.join(st.root, ".tp-cache")
    ran = failed = 0
    items = [ev for ev in (e.meta.get("checked_by") or []) if isinstance(ev, dict)]
    out(f"{eid} (version {e.version}): {e.title}")
    if not items:
        out("  no checks recorded")
    for ev in items:
        kind = ev.get("kind")
        if kind == "check":
            ref = str(ev.get("ref") or "")
            fname, _, func = ref.partition("::")
            path = os.path.join(e.path, fname)
            if not func or not os.path.exists(path):
                out(f"  FAIL  {ref}: check file or function not found")
                ran += 1
                failed += 1
                continue
            with open(path, encoding="utf-8") as fh:
                src = fh.read()
            r = evidence.run_check(st.root, e.path, src, func)
            ran += 1
            if r.get("ok"):
                out(f"  pass  {ref}")
            else:
                failed += 1
                out(f"  FAIL  {ref}: {str(r.get('error') or '').strip()[-400:]}")
        elif kind == "legacy":
            script = str(ev.get("script") or "")
            tags = set(ev.get("tags") or [])
            path = legacy_path(st, legacy_dir, script)
            if not os.path.exists(path):
                ran += 1
                failed += 1
                out(f"  FAIL  {script}: script not found")
                continue
            out(f"  ...   running {script} (the paper's verify script; the first run can take minutes)")
            try:
                results = evidence.run_legacy(path, cache)
            except Exception as exc:
                ran += 1
                failed += 1
                out(f"  FAIL  {script}: {exc}")
                continue
            hits = [(lab, ok) for lab, ok in results if evidence.label_keys(lab) & tags]
            if not hits:
                ran += 1
                failed += 1
                out(f"  FAIL  {script}: no check carries tags {sorted(tags)}")
            for lab, ok in hits:
                ran += 1
                if not ok:
                    failed += 1
                out(f"  {'pass' if ok else 'FAIL'}  {script}: {lab}")
        elif kind == "proof":
            out(f"  proof {ev.get('derivation') or ''}: a written proof (read it with get_proof)")
        else:
            out(f"  ----  {kind}: not run by check-one")
    if ran:
        out(f"{ran - failed} of {ran} checks passed" if failed else f"all {ran} checks passed")
    return 1 if failed else 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="tp check-one")
    ap.add_argument("cmd")
    ap.add_argument("id")
    ap.add_argument("--store", default="store")
    a = ap.parse_args(argv)
    return run(a.store, a.id)


if __name__ == "__main__":
    sys.exit(main(["check-one"] + sys.argv[1:]))
