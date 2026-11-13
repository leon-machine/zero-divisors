"""tp: command line for the Physics Graph.

  python -m tp check  [--store store] [--layers 1-6] [--author NAME] [--no-mutants]
  python -m tp build  [--store store] [--out build] [--no-mutants]
  python -m tp lock   [--store store]        record the accepted state (after merge)
  python -m tp doc    RECIPE.yaml [--store store]       generate and store a document
  python -m tp regen  DOC_ID [--store store]            regenerate from the stored version
  python -m tp credit [--store store] [--dry-run]       fill in who did what, and which model
  python -m tp release-notes vX.Y.Z [--store store]     draft releases/vX.Y.Z.md
  python -m tp ga-report [--store store]                entities written outside geometric algebra, undeclared
  python -m tp check-one ID [--store store]             run one result's machine checks
  python -m tp reviews check|hash|fingerprint|add [--store store]   reviews sealed by ORCID
"""
import argparse
import os
import sys

from .model import load_store, write_lock
from .validate import validate


def _layers(s):
    out = []
    for part in s.split(","):
        if "-" in part:
            a, b = part.split("-")
            out += range(int(a), int(b) + 1)
        elif part.strip():
            out.append(int(part))
    return tuple(sorted(set(out)))


# subcommands that live in their own modules: each module defines main(argv) -> int
EXTENSIONS = {
    "bump": "edit", "note": "edit", "wire-check": "edit", "restate": "edit",
    "reviews": "reviews",
    "lint": "lint", "context": "context", "checkruns": "checkruns", "quantity": "quantity",
    "mutants": "mutants", "credit": "credit", "release-notes": "releases", "ga-report": "galang",
    "check-one": "checkone",
}


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "sign":
        print("tp sign is retired: a human review is recorded through the review page with "
              "ORCID sign-in, and checked with `tp reviews check` (docs/REVIEWS.md)")
        return 1
    if argv and argv[0] in EXTENSIONS:
        import importlib
        mod = importlib.import_module(f"tp.{EXTENSIONS[argv[0]]}")
        return mod.main(argv)
    ap = argparse.ArgumentParser(prog="tp")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("check", "build", "lock", "doc", "regen", "audit", "accept", "repin"):
        p = sub.add_parser(name)
        p.add_argument("--store", default="store")
        if name in ("check", "build"):
            p.add_argument("--layers", default="1-6")
            p.add_argument("--author", default=os.environ.get("TP_AUTHOR"))
            p.add_argument("--no-mutants", action="store_true")
            p.add_argument("--keep-going", action="store_true")
            p.add_argument("--jobs", type=int, default=None,
                           help="layer-4 worker processes (default TP_JOBS or the CPU count)")
            p.add_argument("--full", action="store_true",
                           help="rerun layer 4 on every entity, ignoring the layer-4 cache "
                                "(store/.tp-layer4.json)")
            p.add_argument("--cache-dir", default=None,
                           help="where layer 4 caches series script results "
                                "(default store/.tp-cache)")
        if name == "build":
            p.add_argument("--out", default="build")
        if name == "doc":
            p.add_argument("recipe")
        if name in ("regen", "audit"):
            p.add_argument("doc_id")
        if name == "accept":
            p.add_argument("proposal_id")
            p.add_argument("--update", action="store_true",
                           help="replace a stored entity with a proposal of a higher version, "
                                "keeping stored files the proposal does not carry")
        if name == "repin":
            p.add_argument("--ids", default="",
                           help="comma-separated dependants to re-confirm (default: all)")
    a = ap.parse_args(argv)
    if getattr(a, "cache_dir", None):
        os.environ["TP_CACHE_DIR"] = a.cache_dir
    if getattr(a, "full", False):
        os.environ["TP_FULL"] = "1"
    if getattr(a, "jobs", None):
        os.environ["TP_JOBS"] = str(a.jobs)
    if a.cmd == "check":
        rep = validate(load_store(a.store), layers=_layers(a.layers),
                       keep_going=a.keep_going, author=a.author,
                       run_mutants=not a.no_mutants)
        for f in rep.findings:
            if not f.code.startswith("I4"):
                print(f.render())
        n = len(rep.errors())
        from .validate import summarise
        st = getattr(rep, "l4_stats", None)
        if st:
            print(f"layer 4: ran {st['ran']} entities in {st.get('jobs', 1)} process(es), "
                  f"replayed {st['replayed']} unchanged from the cache (--full to rerun all)")
        print("\n" + summarise(rep))
        print(f"\nlayers run: {rep.layers_run}; {n} error(s), "
              f"{sum(f.severity == 'warning' for f in rep.findings)} warning(s)")
        return 1 if n else 0
    if a.cmd == "build":
        from .build import compile_store
        _, rep, graph = compile_store(a.store, a.out, run_mutants=not a.no_mutants,
                                      author=a.author, layers=_layers(a.layers))
        print(f"built {len(graph['nodes'])} entities, {len(graph['edges'])} edges; "
              f"{len(rep.errors())} error(s); see {os.path.join(a.out, 'report.md')}")
        return 1 if rep.errors() else 0
    if a.cmd == "lock":
        write_lock(load_store(a.store))
        from . import reviews
        reviews.write_lock(a.store)
        print("lock written")
        return 0
    if a.cmd == "doc":
        from .docgen import generate
        doc = generate(a.store, a.recipe)
        print(f"stored {doc['doc_id']} v{doc['version']} in {doc['folder']}")
        return 0
    if a.cmd == "repin":
        from .repin import repin
        n = repin(a.store, [x for x in a.ids.split(",") if x])
        print(f"re-confirmed {n} edge(s) against the current versions of their targets")
        return 0
    if a.cmd == "accept":
        return _accept(a)
    if a.cmd == "audit":
        from .docgen import reaudit
        from collections import Counter
        f = reaudit(a.store, a.doc_id)
        for x in f:
            if x["code"] != "D110":
                print(x["code"], x["block"], x["message"])
        print(dict(Counter(x["code"] for x in f)))
        return 1 if any(x["code"] != "D110" for x in f) else 0
    if a.cmd == "regen":
        from .docgen import regenerate
        doc = regenerate(a.store, a.doc_id)
        print(f"regenerated {doc['doc_id']} -> v{doc['version']}: {doc['bump']} "
              f"({len(doc['changelog'])} change(s))")
        return 0


def _accept(a):
    """tp accept <id> [--update]: move proposals/<id>/ into the store after validation.

    Without --update an existing entity is never overwritten. With --update the proposal's
    version must exceed the stored one; its files are copied over the stored folder, stored
    files it does not carry (orig-proof-main.tex, coverage.yaml, a check.py it leaves out)
    are kept, and the old folder is restored if validation finds new errors."""
    import json
    import shutil
    import tempfile
    from .model import ENTITY_DIRS, ENTITY_FILE, ID_RE, parse_entity_text
    if not ID_RE.fullmatch(a.proposal_id):
        print(f"{a.proposal_id!r} is not an entity id")
        return 1
    lab = os.path.dirname(os.path.abspath(a.store))
    src = os.path.join(lab, "proposals", a.proposal_id)
    if not os.path.isfile(os.path.join(src, "proposal.json")):
        print(f"no proposal {a.proposal_id} in {os.path.dirname(src)}")
        return 1
    with open(os.path.join(src, "proposal.json"), encoding="utf-8") as fh:
        info = json.load(fh)
    kind = info.get("kind") or "claim"
    if kind not in ENTITY_DIRS:
        print(f"proposal kind {kind!r} is not an entity kind")
        return 1
    dst = os.path.join(a.store, ENTITY_DIRS[kind], a.proposal_id)
    update = os.path.exists(dst)
    if update and not a.update:
        print(f"{dst} exists; refusing to overwrite (use --update for a new version)")
        return 1
    old_v = new_v = None
    if update:
        def _version(folder):
            with open(os.path.join(folder, ENTITY_FILE), encoding="utf-8") as fh:
                meta, _, errs = parse_entity_text(fh.read())
            if errs:
                raise ValueError("; ".join(errs))
            if meta.get("id") != a.proposal_id:
                raise ValueError(f"entity.md carries id {meta.get('id')!r}")
            return int(meta.get("version") or 0)
        try:
            old_v = _version(dst)
            new_v = _version(src)
        except (OSError, ValueError) as exc:
            print(f"cannot read the versions to compare: {exc}")
            return 1
        if new_v <= old_v:
            print(f"proposal {a.proposal_id} is version {new_v}, not above the stored "
                  f"version {old_v}; refusing")
            return 1
    base = validate(load_store(a.store), layers=(1, 2, 3), keep_going=True,
                    run_mutants=False)
    before = {(f.code, f.entity, f.message) for f in base.errors()}
    backup = None
    kept = []
    if update:
        backup = os.path.join(tempfile.mkdtemp(prefix="tp-accept-"), "old")
        shutil.copytree(dst, backup)
        theirs = set()
        for root, _, files in os.walk(src):
            for f in files:
                rel = os.path.relpath(os.path.join(root, f), src)
                if rel == "proposal.json":
                    continue
                theirs.add(rel)
                os.makedirs(os.path.dirname(os.path.join(dst, rel)), exist_ok=True)
                shutil.copy2(os.path.join(root, f), os.path.join(dst, rel))
        for root, _, files in os.walk(backup):
            for f in files:
                rel = os.path.relpath(os.path.join(root, f), backup)
                if rel not in theirs:
                    kept.append(rel)
    else:
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("proposal.json"))

    def _restore():
        shutil.rmtree(dst)
        if backup:
            shutil.copytree(backup, dst)

    # the maintainer's acceptance runs everything MCP did not: the proposal's
    # own checks (layer 4, with the mutation test) and the people rules
    try:
        rep = validate(load_store(a.store), layers=(1, 2, 3, 4), keep_going=True)
    except BaseException:
        _restore()
        raise
    mine = lambda f: f.entity.split("@")[0] == a.proposal_id
    errs = [f for f in rep.errors()
            if mine(f) or (f.code, f.entity, f.message) not in before
            and not f.code.startswith("E4")]
    if errs:
        _restore()
        for f in errs:
            print(f.render())
        if update:
            print(f"update of {a.proposal_id} refused; the stored version {old_v} is restored")
        return 1
    if backup:
        shutil.rmtree(os.path.dirname(backup), ignore_errors=True)
    shutil.rmtree(src)
    if update:
        print(f"updated {a.proposal_id} version {old_v} -> {new_v} in {dst}; kept "
              f"{', '.join(sorted(kept)) or 'no stored-only files'}; run tp lock after review")
    else:
        print(f"accepted {a.proposal_id} into {dst}; run tp lock after review")
    return 0


if __name__ == "__main__":
    sys.exit(main())
