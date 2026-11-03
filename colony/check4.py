#!/usr/bin/env python3
"""Run the maintainer's evidence layer (layer 4: static rules, the check itself, premise
tracking and the mutation test) on ONE proposal, as `python -m tp accept` would, without
touching the store.

  python3 colony/check4.py proposals/<id>      (or an absolute folder path)

Exit status 0 when the proposal has no layer-4 error. Prints every finding for it.
Static rules it enforces: exact arithmetic only (no float literals, float(), math,
random, integer true division), the check imports GA, every premise the check touches
is declared in the derivations, and perturbing the check's integer literals makes it fail.
"""
import json
import os
import shutil
import sys
import tempfile

LAB = os.environ.get("TP_LAB") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, LAB)
# the proposal is checked in a temporary copy of the store, where the store's relative
# legacy_scripts_dir (../legacy) would not resolve: point it at the repository's folder
os.environ.setdefault("TP_LEGACY_DIR", os.path.join(LAB, "legacy"))
from tp.model import load_store            # noqa: E402
from tp import validate as V               # noqa: E402


def main():
    folder = os.path.abspath(sys.argv[1])
    pid = os.path.basename(folder.rstrip("/"))
    info = json.load(open(os.path.join(folder, "proposal.json"))) if os.path.exists(
        os.path.join(folder, "proposal.json")) else {}
    sub = {"claim": "claims", "object": "objects", "prediction": "predictions",
           "question": "questions"}.get(info.get("kind") or "claim", "claims")
    with tempfile.TemporaryDirectory() as tmp:
        root = os.path.join(tmp, "store")
        shutil.copytree(os.path.join(LAB, "store"), root,
                        ignore=shutil.ignore_patterns("__pycache__"))
        dst = os.path.join(root, sub, pid)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(folder, dst, ignore=shutil.ignore_patterns("proposal.json", "__pycache__"))
        store = load_store(root)
        if pid not in store.entities:
            sys.exit(f"{pid} did not load; run validate_draft first")
        rep = V.Report() if hasattr(V, "Report") else None
        full = store.entities
        store.entities = {pid: full[pid]}
        try:
            V.layer4(store, rep, run_mutants=True)
        finally:
            store.entities = full
    mine = [f for f in rep.findings if f.entity.split("@")[0] == pid]
    for f in mine:
        print(f.render() if hasattr(f, "render") else f)
    errs = [f for f in mine if f.severity == "error"]
    print(f"\n{pid}: {len(errs)} error(s), {len(mine) - len(errs)} other finding(s); "
          f"check result: {rep.check_results.get(pid)}")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
