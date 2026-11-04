"""Build the Transport Lab page from build/graph.json:  python -m tp.site"""
import datetime
import json
import os
import re
import sys
import shutil
import urllib.parse
import html as html_lib

import yaml

SIDES = [("metric", "Geometry and gravity", 0), ("algebra", "The algebra", 0),
         ("car", "The quantum side", 1), ("matter", "Matter and cosmology", 1),
         ("synthesis", "The programme", 1)]
PAPER_ORDER = ["T00", "T01", "T02", "T03", "T04", "T05", "T05-pairing", "T05-angle",
               "T05-descent-lift", "T05-state-selection", "T05-three-routes", "T06", "T07",
               "T08", "T09", "T10", "T11", "T12", "T12-lepton", "T12-rungs", "T13", "T14",
               "T14a", "T14b", "T14c", "T15", "T16", "T17", "T17-rule2", "FT"]
KEEP = ("id", "kind", "version", "title", "status", "effective", "ledger", "check",
        "region", "review", "one_liner", "formal", "technical", "lay", "locators",
        "imported_from", "flags", "typing_note", "conditional_on", "subject", "stale",
        "kill_condition", "observations", "refuted_by")
FEATURED = ["transport.transport-algorithm", "transport.noinverse", "transport.minimality",
            "singularity.type-n-only-type-n", "tower.witt-index-quantum-capacity",
            "hawking.i-state", "one-relation.two-capacities-three-consequences",
            "pred.neutrino-mass-sum-floor"]


LABELS = {"theorem": "Theorem", "proposition": "Proposition", "lemma": "Lemma",
          "corollary": "Corollary", "assembled": "Fact (assembled here)",
          "fact": "Fact (imported)", "postulate": "Postulate", "conjecture": "Conjecture",
          "refutation": "Refutation", "prediction": "Prediction", "definition": "Definition"}


def _label(b, nodes):
    from .docgen import PROVED_ENVS
    t = b.get("type")
    if t == "theorem":
        cid = (b.get("claim") or "").split("@")[0]
        num = str(((nodes.get(cid) or {}).get("locators") or {}).get("number") or "")
        t = PROVED_ENVS.get(num.split(" ")[0], "theorem")
    return LABELS.get(t, t)


def _deposited(store):
    """The deposited papers of the series (Zenodo), in series order, for the Documents page."""
    from . import docgen
    refs = docgen._refs(store)
    out = []
    for key, ent in refs.items():
        m = re.match(r"^ButlerT(\d+)([a-c]?)$", key)
        if not m or not ent.get("doi"):
            continue
        meta = docgen.paper_meta(store, f"T{m.group(1)}{m.group(2)}", refs) or {}
        out.append({"code": meta.get("short") or key[6:], "title": meta.get("title", ""),
                    "subtitle": meta.get("subtitle", ""), "doi": ent["doi"],
                    "order": int(m.group(1)) + (ord(m.group(2)) - 96) / 10 if m.group(2) else int(m.group(1))})
    return sorted(out, key=lambda x: x["order"])


def _documents(root, nodes, store=None, site="site"):
    """The stored documents: blocks, version history and audit, for the reader; with each
    paper's deposited version (title, DOI), its PDF if built, the proofs, and where each
    result comes from."""
    from . import docgen
    out = []
    if not os.path.isdir(root):
        return out
    refs = docgen._refs(store) if store is not None else {}
    for d in sorted(os.listdir(root)):
        f = os.path.join(root, d)
        if not os.path.exists(os.path.join(f, "manifest.json")):
            continue
        man = json.load(open(os.path.join(f, "manifest.json")))
        rec = yaml.safe_load(open(os.path.join(f, "recipe.yaml")))
        blocks = json.load(open(os.path.join(f, "blocks.json")))
        audit = json.load(open(os.path.join(f, "audit.json")))
        log = open(os.path.join(f, "changelog.md")).read()
        hist = []
        for m in re.finditer(r"^## v(\d+) \(([^)]*)\)\n\n- bump: (\w+)", log, re.M):
            hist.append({"v": int(m.group(1)), "date": m.group(2)[:10], "bump": m.group(3)})
        codes = {}
        for a in audit:
            codes[a["code"]] = codes.get(a["code"], 0) + 1
        code = rec.get("paper")
        meta = docgen.paper_meta(store, code, refs) if store is not None and code and "-" not in str(code) else None
        kind = "trail" if (rec.get("trail") or d == "tour") else ("paper" if code else "assembled")
        # where the document sits in the series: T-number, then its companion notes
        pm = re.match(r"^T0*(\d+)([a-c]?)(?:-(.*))?$", str(code or ""))
        if pm:
            series = f"T{int(pm.group(1))}{pm.group(2)}" + (f" companion note" if pm.group(3) else "")
            order = int(pm.group(1)) + (ord(pm.group(2)) - 96) / 10 if pm.group(2) else int(pm.group(1))
            order += 0.05 if pm.group(3) else 0
            order += 0.01 if d.endswith("results-only") else 0
        else:
            series = {"FT": "Field theory note"}.get(str(code), str(code) if code else None)
            order = 99

        def plain(t):
            return re.sub(r"\\href\{[^}]*\}\{([^}]*)\}", r"\1", t or "")

        # what has changed since the deposited version (tp.deposits)
        chg = None
        if meta and meta.get("doi"):
            from . import deposits
            try:
                chg = deposits.compare(store, store.root, str(code), blocks)
            except Exception:
                chg = None

        def extra(b):
            cid = (b.get("claim") or "").split("@")[0]
            if not cid or store is None or cid not in store.entities:
                return {}
            e = store.entities[cid]
            x = {"status": e.status}
            src = docgen.source_line(store, cid, refs)
            lp = str((e.meta.get("locators") or {}).get("paper") or "")
            if src and b.get("type") in ("theorem", "conjecture") and (
                    not code or lp.split("-")[0] != str(code).split("-")[0]):
                x["first"] = plain(src)
            elif src and b.get("type") in ("fact", "postulate"):
                x["source"] = plain(src)
            if e.kind == "note":
                x["sub"] = (e.meta.get("locators") or {}).get("subsection")
            c = (chg or {}).get("blocks", {}).get(b.get("id"))
            if c and (c["kind"] == "revised" or (c["kind"] == "added" and not c["cited"])):
                x["chg"] = {"kind": c["kind"], "what": c["what"], "dep": c.get("deposited_number"),
                            "cls": c.get("class"), "why": c.get("why") if c.get("reviewed") else "",
                            "notes": c["notes"][-3:],
                            "deposited": c["deposited"] if c["kind"] == "revised" else None}
            return x
        out.append({
            "id": d, "title": re.sub(r"\s*\((regenerated|recreated)[^)]*\)\s*$", "",
                                     (meta or {}).get("title") or rec.get("title", d)),
            "subtitle": (meta or {}).get("subtitle", "") + (" (results only)" if d.endswith("results-only") else ""),
            "level": rec.get("level"), "order": order,
            "kind": kind, "paper": series, "doi": (meta or {}).get("doi"),
            "pdf": ("pdf/" + d + ".pdf") if os.path.exists(os.path.join(site, "pdf", d + ".pdf")) else None,
            "version": man["version"], "claims": len(man["claims"]),
            "changes": None if chg is None else {
                "sentence": deposits.summary_sentence(chg), "summary": chg["summary"],
                "version": chg["version"], "removed": chg["removed"],
                "list": [{"id": bid, "kind": c["kind"], "what": c["what"], "title": c["title"],
                          "dep": c.get("deposited_number"), "cls": c.get("class"),
                          "why": c.get("why") if c.get("reviewed") else ""}
                         for bid, c in chg["blocks"].items()
                         if c["kind"] == "revised" or (c["kind"] == "added" and not c["cited"])]},
            "spine": rec.get("spine", []), "history": hist, "audit": codes,
            "blocks": [dict({k: b.get(k) for k in ("id", "type", "title", "text", "claim",
                                                    "number", "provenance", "proof")},
                            label=_label(b, nodes), **extra(b)) for b in blocks]})
    return out


# ---------------------------------------------------------------------------
# version 2: the universe
# ---------------------------------------------------------------------------

SIDE_HUE = {"metric": 212, "algebra": 272, "car": 168, "matter": 22, "synthesis": 330}
# in the page (the map, search before its index loads, the record views) ...
V2_INLINE = ("id", "kind", "version", "status", "effective", "ledger", "check", "one_liner",
             "conditional_on", "subject", "kill_condition", "observations", "refuted_by",
             "locators")
# ... and in site/data/<subject>.json, fetched when the result is opened
V2_DEFER = ("formal", "technical", "lay", "imported_from", "flags", "typing_note", "review")
DATA_RESERVED = ("search", "documents")
SHOWN_UNDEPOSITED = ("T14c",)            # undeposited papers the Documents page still lists
# unpublished companion notes left out of the Collections menu (their results stay in the graph)
UNLISTED_COLLECTIONS = ("T05-pairing", "T05-angle", "T05-descent-lift", "T05-state-selection",
                        "T05-three-routes", "T17-rule2", "T12-lepton", "T12-rungs")


def _data_chunk_of(subject):
    """The data file that carries a result's reading text: one per subject."""
    c = re.sub(r"[^a-z0-9-]", "-", str(subject or "unplaced").lower()) or "unplaced"
    return "subject-" + c if c in DATA_RESERVED else c


def _display_title(t):
    t = re.sub(r"^\s*[Ii]mported:\s*", "", str(t or ""))
    return t[:1].upper() + t[1:]


def _paper_titles(suite):
    from .extract import PAPERS
    out = {}
    for code, tex, *_ in PAPERS:
        path = os.path.join(suite, tex)
        if not os.path.exists(path):
            continue
        src = open(path, encoding="utf-8").read()
        m = re.search(r"\\title\{(.*?)\}\s*\n\s*\\(?:author|date)", src, re.S)
        t = m.group(1) if m else code
        t = re.split(r"\\\\", t)[0]
        t = re.sub(r"\\(?:bfseries|large|Large|normalsize|small|itshape|upshape)\b", "", t)
        t = re.sub(r"[{}\\]", "", t)
        out[code] = re.sub(r"\s+", " ", t).strip().rstrip(":").strip()
    return out


def _checks_by_entity(store_obj):
    """The passing (or failing) verify-script checks attached to each claim."""
    from . import evidence
    out, cache = {}, os.path.join(store_obj.root, ".tp-cache")
    legacy_dir = os.path.join(store_obj.root, store_obj.config.get("legacy_scripts_dir") or "")
    results = {}
    for eid, e in store_obj.entities.items():
        for ev in e.meta.get("checked_by") or []:
            if ev.get("kind") != "legacy":
                continue
            script = ev.get("script")
            if script not in results:
                try:
                    results[script] = evidence.run_legacy(os.path.join(legacy_dir, script), cache)
                except Exception:
                    results[script] = []
            tags = set(ev.get("tags") or [])
            hits = [[lab[:240], bool(ok)] for lab, ok in results[script]
                    if evidence.label_keys(lab) & tags]
            if hits:
                out.setdefault(eid, []).append({"script": script, "checks": hits[:40],
                                                "count": len(hits)})
    return out


PREMISE_RE = re.compile(r"premise\(\s*[\"']([^\"']+)[\"']")


def _chunk_of(eid):
    """The published file that carries an entity's check source: one per subject prefix."""
    return re.sub(r"[^a-z0-9-]", "-", eid.split(".")[0].lower())


def _marks(src):
    """Where a check function updates its running verdict (ok = ...): [function, statement line,
    last line, indent]. The page inserts a marker after each such statement when it needs to show
    which statement first turned the verdict False in the browser engine."""
    import ast
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    lines = src.split("\n")
    out = []
    for fn in tree.body:
        if not (isinstance(fn, ast.FunctionDef) and fn.name.startswith("check_")):
            continue
        for n in ast.walk(fn):
            if not (isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign, ast.Expr)) and n.end_lineno):
                continue
            if isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant):
                continue
            first, last = lines[n.lineno - 1], lines[n.end_lineno - 1]
            if first[:n.col_offset].strip() or last[n.end_col_offset:].strip():
                continue
            name = None
            if isinstance(n, (ast.Assign, ast.AugAssign)):
                tg = n.targets if isinstance(n, ast.Assign) else [n.target]
                names = [t.id for t in tg if isinstance(t, ast.Name)]
                if names and names[0] in ("ok", "closed", "good", "holds", "res", "fine"):
                    name = names[0]
            out.append([fn.name, n.lineno, n.end_lineno, n.col_offset, name])
    return out


def _browser_src(src):
    """The source the in-browser engine runs: Brython 3.12 stores int keys as strings in
    dict.setdefault, so d.setdefault(k, v) becomes _tp_setdefault(d, k, v) (same lines, same
    columns before the call), defined by the page's runner. Returns None when nothing changes."""
    import ast
    out = src
    for _ in range(50):
        try:
            tree = ast.parse(out)
        except SyntaxError:
            return None
        lines = out.split("\n")
        calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                 and n.func.attr == "setdefault" and n.args
                 and n.func.value.lineno == n.func.end_lineno == n.func.value.end_lineno]
        if not calls:
            break
        n = max(calls, key=lambda c: (c.lineno, c.col_offset))
        ln = lines[n.func.lineno - 1]
        v0, v1 = n.func.value.col_offset, n.func.value.end_col_offset
        rest = ln[n.func.end_col_offset:]
        if not rest.lstrip().startswith("("):
            break
        k = n.func.end_col_offset + rest.index("(") + 1
        lines[n.func.lineno - 1] = ln[:v0] + "_tp_setdefault(" + ln[v0:v1] + ", " + ln[k:]
        out = "\n".join(lines)
    return None if out == src else out


BROWSER_LIB_SKIP = ("GA.py", "tp_premise.py")   # GA ships on its own; the page builds tp_premise itself


def _browser_lib(lib):
    """The shared library modules a check may import (lib/*.py besides GA and tp_premise), in an
    order where each comes after the library modules it imports, as [[name, source the browser
    runs]] (the dict.setdefault rewrite applied where it changes anything)."""
    import ast
    mods = {}
    for f in sorted(os.listdir(lib)) if os.path.isdir(lib) else []:
        if f.endswith(".py") and f not in BROWSER_LIB_SKIP and not f.startswith("_"):
            mods[f[:-3]] = open(os.path.join(lib, f), encoding="utf-8").read()
    deps = {}
    for name, src in mods.items():
        try:
            tree = ast.parse(src)
        except SyntaxError:
            deps[name] = set()
            continue
        got = set()
        for n in ast.walk(tree):
            if isinstance(n, ast.Import):
                got.update(a.name.split(".")[0] for a in n.names)
            elif isinstance(n, ast.ImportFrom) and n.module and not n.level:
                got.add(n.module.split(".")[0])
        deps[name] = (got & set(mods)) - {name}
    order, done = [], set()

    def visit(m, stack=()):
        if m in done or m in stack:
            return
        for d in sorted(deps[m]):
            visit(d, stack + (m,))
        done.add(m)
        order.append(m)
    for m in sorted(mods):
        visit(m)
    return [[m, _browser_src(mods[m]) or mods[m]] for m in order]


def _runner_stamp(site, chunks):
    """Changes only when what the browser runs changes (check sources, GA.py, probes, the page's
    Python runner), so a resumed browser run keeps results across page edits that touch nothing else."""
    import hashlib
    from . import engine_probes
    h = hashlib.sha256()
    tpl = open(os.path.join(site, "universe.template.html"), encoding="utf-8").read()
    a = tpl.find("const CK_DRIVER = `")
    h.update(tpl[a:tpl.find("`;", a)].encode())
    h.update(json.dumps(chunks, sort_keys=True).encode())
    h.update((engine_probes.SETUP + engine_probes.TRACE_CODE + "".join(engine_probes.PROBES)).encode())
    lib = os.path.join(os.path.dirname(os.path.abspath(site)), "lib")
    h.update(open(os.path.join(lib, "GA.py"), "rb").read())
    blib = _browser_lib(lib)
    if blib:                     # an empty library leaves the stamp as it was before the library existed
        h.update(json.dumps(blib).encode())
    return h.hexdigest()[:16]


def _own_checks(st, site, build):
    """Each entity's own check.py: written to site/checks/<subject>.json for the page to fetch on
    demand, with GA.py in site/checks/runtime.json. Returns, per entity, the check's functions,
    the premise closure the browser runner needs and the last recorded run (site/check_runs.json,
    written by python -m tp.checkruns)."""
    import ast
    srcs = {}
    for eid, e in st.entities.items():
        f = os.path.join(e.path, "check.py")
        if os.path.exists(f):
            srcs[eid] = (open(f, encoding="utf-8").read(), os.path.relpath(f, os.path.dirname(st.root)))
    direct = {eid: sorted(set(PREMISE_RE.findall(src)) - {eid}) for eid, (src, _) in srcs.items()}
    runs_path = os.path.join(site, "check_runs.json")
    runs, py = {}, ""
    if os.path.exists(runs_path):
        rj = json.load(open(runs_path))
        runs, py = rj.get("runs", {}), rj.get("python", "")
    out, chunks = {}, {}
    for eid, (src, rel) in srcs.items():
        seen, todo = set(), list(direct[eid])
        while todo:
            x = todo.pop()
            if x in seen or x not in srcs:
                continue
            seen.add(x)
            todo.extend(direct.get(x, []))
        try:
            fns = [n.name for n in ast.parse(src).body
                   if isinstance(n, ast.FunctionDef) and n.name.startswith("check_")]
        except SyntaxError:
            fns = []
        chunks.setdefault(_chunk_of(eid), {})[eid] = src
        bsrc = _browser_src(src)
        if bsrc:
            chunks[_chunk_of(eid)].setdefault("__browser__", {})[eid] = bsrc
        mk = _marks(src)
        if mk:
            chunks[_chunk_of(eid)].setdefault("__marks__", {})[eid] = mk
        r = runs.get(eid) or {}
        out[eid] = {"chunk": _chunk_of(eid), "path": rel.replace(os.sep, "/"), "fns": sorted(fns),
                    "closure": sorted(seen), "lines": src.count("\n") + 1,
                    "run": {"at": r.get("ran_at"), "py": py, "load_error": r.get("load_error"),
                            "fns": [[f["name"], f["ok"], f["ms"], f["touched"], (f.get("error") or "")[-600:]]
                                    for f in r.get("functions", [])]} if r else None}
    cdir = os.path.join(site, "checks")
    os.makedirs(cdir, exist_ok=True)
    for old in os.listdir(cdir):
        if old.endswith(".json"):
            os.remove(os.path.join(cdir, old))
    for c, m in chunks.items():
        json.dump(m, open(os.path.join(cdir, c + ".json"), "w", encoding="utf-8"), ensure_ascii=False)
    lib = os.path.join(os.path.dirname(st.root), "lib")
    sys.path.insert(0, lib)
    from . import engine_probes
    json.dump({"GA": open(os.path.join(lib, "GA.py"), encoding="utf-8").read(),
               # the shared library (gtg, fock, series), in import order, as the browser runs it
               "lib": _browser_lib(lib),
               "probe_setup": engine_probes.SETUP, "probes": engine_probes.expected(),
               "trace_code": engine_probes.TRACE_CODE,
               "built": _runner_stamp(site, chunks),
               # earlier stamps whose stored browser results are still valid for this runner
               "compatible": ["2026-10-23T15:55:31Z"]},
              open(os.path.join(cdir, "runtime.json"), "w", encoding="utf-8"), ensure_ascii=False)
    return out


# ---------------------------------------------------------------------------
# per-result history, coverage, trust, programmes and quantities (roadmap 7, 8, 10, 12, 15)
# ---------------------------------------------------------------------------

def _git_history(lab, rel="store"):
    """One pass over `git log --name-only` for the store: entity folder (relative to the lab,
    e.g. store/claims/a.b) -> [[short hash, date, subject], ...], newest first. Empty when the lab
    is not a git work tree."""
    import subprocess
    try:
        cp = subprocess.run(["git", "-C", lab, "log", "--format=%x1e%h%x09%ad%x09%s", "--date=short",
                             "--name-only", "--", rel], capture_output=True, text=True, timeout=120)
    except Exception:
        return {}
    if cp.returncode != 0:
        return {}
    out = {}
    for block in cp.stdout.split("\x1e"):
        lines = [x for x in block.split("\n") if x.strip()]
        if not lines:
            continue
        head = lines[0].split("\t", 2)
        if len(head) < 3:
            continue
        seen = set()
        for f in lines[1:]:
            parts = f.strip().split("/")
            if len(parts) < 4:              # store/<kind dir>/<id>/<file>
                continue
            folder = "/".join(parts[:3])
            if folder not in seen:
                seen.add(folder)
                out.setdefault(folder, []).append(head)
    return out


VERSION_NOTE = re.compile(r"\b[Vv]ersion\s+(\d+)\s*(?:->|\u2192|to)\s*(\d+)")
KEY_DATE = re.compile(r"(\d{4})[_-](\d{2})[_-](\d{2})")


def _release(lab):
    """The release the site is built from: the latest tag reachable from HEAD, its date, and how
    many commits HEAD is past it (0 when the site is built from the tag itself, as it should be
    for the public site; see RELEASING.md). None before the first release."""
    import subprocess
    try:
        tag = subprocess.run(["git", "-C", lab, "describe", "--tags", "--abbrev=0"],
                             capture_output=True, text=True, timeout=30)
        if tag.returncode != 0 or not tag.stdout.strip():
            return None
        t = tag.stdout.strip()
        date = subprocess.run(["git", "-C", lab, "log", "-1", "--format=%ad", "--date=short", t],
                              capture_output=True, text=True, timeout=30).stdout.strip()
        ahead = subprocess.run(["git", "-C", lab, "rev-list", "--count", t + "..HEAD"],
                               capture_output=True, text=True, timeout=30).stdout.strip()
        return {"tag": t, "date": date, "ahead": int(ahead or 0)}
    except Exception:
        return None


def _entity_history(e, git_rows):
    """What changed and when: the maintainer and review passes recorded under `extraction`
    (with the version a note names). The lab's commit history is not shown: it is working
    history, kept from the first public release on."""
    rows = []
    for key, v in (e.meta.get("extraction") or {}).items():
        if not isinstance(v, dict):
            continue
        date = str(v.get("date") or "")
        if not date:
            m = KEY_DATE.search(key)
            date = "-".join(m.groups()) if m else ""
        if not date:
            continue
        note = " ".join(str(v.get("note") or v.get("summary") or v.get("finding") or "").split())
        m = VERSION_NOTE.search(note)
        rows.append({"date": date[:10], "v": int(m.group(2)) if m else None,
                     "by": str(v.get("by") or ""), "what": key.replace("_", " "),
                     "text": note[:320] + ("…" if len(note) > 320 else "")})
    rows.sort(key=lambda r: (r["date"], 0 if r.get("commit") else 1), reverse=True)
    return rows[:40]


COVERAGE_KINDS = ("exact", "complete", "sampled", "partial")


def _coverage(e):
    """store/<kind>/<id>/coverage.yaml as the page shows it, or None."""
    p = os.path.join(e.path, "coverage.yaml")
    if not os.path.exists(p):
        return None
    try:
        c = yaml.safe_load(open(p, encoding="utf-8")) or {}
    except Exception:
        return None
    fns = {}
    for name, f in (c.get("functions") or {}).items():
        if isinstance(f, dict):
            fns[str(name)] = {"kind": f.get("kind") if f.get("kind") in COVERAGE_KINDS else None,
                              "clauses": [str(x) for x in (f.get("clauses") or [])],
                              "omits": str(f.get("omits") or "")}
    j = c.get("judge") if isinstance(c.get("judge"), dict) else None
    return {"functions": fns,
            "judge": {k: str(j.get(k) or "") for k in ("by", "date", "verdict", "note")} if j else None}


def _weak_coverage(cov):
    """'sampled' or 'partial' when no function of the check is recorded as exact or complete:
    such a result is never shown with proof wording. None otherwise."""
    kinds = [f["kind"] for f in ((cov or {}).get("functions") or {}).values() if f.get("kind")]
    if not kinds or any(k in ("exact", "complete") for k in kinds):
        return None
    return "sampled" if all(k == "sampled" for k in kinds) else "partial"


TRUST_LEVELS = ("ai-proposed", "ai-refereed", "human-read", "human-checked", "published")


def _trust(e):
    t = e.meta.get("trust")
    if t in TRUST_LEVELS:
        return t
    return "ai-proposed" if e.meta.get("ai_involved") in ("yes", "unknown", None) else None


def _programmes(config):
    """store/config.yaml `programmes` as [{id, title, about}] (a list of ids, a list of
    mappings or a mapping id -> title or mapping)."""
    raw = config.get("programmes") or []
    out = []
    items = raw.items() if isinstance(raw, dict) else [(None, x) for x in raw]
    for k, v in items:
        if isinstance(v, dict):
            pid = v.get("id") or k
            out.append({"id": str(pid), "title": str(v.get("title") or pid), "about": str(v.get("about") or "")})
        elif k is not None:
            out.append({"id": str(k), "title": str(v or k), "about": ""})
        elif v:
            out.append({"id": str(v), "title": str(v), "about": ""})
    return [p for p in out if p["id"]]


def _citation(src):
    if isinstance(src, dict):
        bits = [src.get("citation") or src.get("ref") or src.get("doi") or ""]
        if src.get("locator"):
            bits.append(str(src["locator"]))
        return ", ".join(str(b) for b in bits if b)
    return str(src or "")


def _quantities(st):
    """Quantity entities (kind quantity, store/quantities/) with the results that cite them."""
    qs = {eid: e for eid, e in st.entities.items() if e.kind == "quantity"}
    if not qs:
        return []
    used = {}
    for eid, e in st.entities.items():
        for pin in e.meta.get("quantities") or []:
            used.setdefault(str(pin).split("@")[0], []).append(eid)
    out = []
    for qid, e in sorted(qs.items()):
        q = e.meta.get("quantity") or {}
        out.append({"id": qid, "title": _display_title(e.title), "status": e.status,
                    "version": e.version, "symbol": str(q.get("symbol") or ""),
                    "value": str(q.get("value") or ""), "uncertainty": str(q.get("uncertainty") or ""),
                    "units": str(q.get("units") or ""), "dimension": str(q.get("dimension") or ""),
                    "exact": bool(q.get("exact")), "source": _citation(q.get("source")),
                    "date": str(q.get("date") or ""), "note": str(q.get("note") or ""),
                    "one_liner": (e.levels.get("one-liner") or "").strip(),
                    "used_by": sorted(set(used.get(qid, [])))})
    return out


SEARCH_TOK = re.compile(r"[a-z0-9]{2,}")
NOTE_WORDS = (re.compile(r"\\(?:claimref|cite[a-z]*|ref|eqref|label)\s*(?:\[[^\]]*\])?\s*\{[^}]*\}"),
              re.compile(r"\\[A-Za-z]+"))


def _note_words(t):
    return NOTE_WORDS[1].sub(" ", NOTE_WORDS[0].sub(" ", str(t or "")))


def _search_index(entries):
    """A prebuilt BM25 index over (type, id, text): docs [[type, id, length]], postings
    term -> [doc, count, doc, count, ...], with the document frequencies implied."""
    docs, post = [], {}
    for i, (typ, eid, text) in enumerate(entries):
        counts = {}
        for t in SEARCH_TOK.findall(str(text or "").lower()):
            counts[t] = counts.get(t, 0) + 1
        docs.append([typ, eid, sum(counts.values())])
        for t, c in counts.items():
            post.setdefault(t, []).extend([i, c])
    avg = sum(d[2] for d in docs) / max(len(docs), 1)
    return {"N": len(docs), "avg": round(avg, 3), "docs": docs, "post": post}


def _dump(obj, path):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, separators=(",", ":"), default=str)


def _trails(docs_root):
    """Each stored trail document as an ordered walk: steps with their prose."""
    out = []
    if not os.path.isdir(docs_root):
        return out
    strip = lambda t: re.sub(r"\s*\[\[(?:c:[^\]]+|t)\]\]", "", str(t or "")).strip()
    for d in sorted(os.listdir(docs_root)):
        f = os.path.join(docs_root, d)
        rp = os.path.join(f, "recipe.yaml")
        if not os.path.exists(rp):
            continue
        rec = yaml.safe_load(open(rp))
        if not (rec.get("trail") or d == "tour"):
            continue
        blocks = json.load(open(os.path.join(f, "blocks.json")))
        intro = " ".join(strip(b["text"]) for b in blocks
                         if b["type"] == "abstract" or b["id"] == "introduction")
        steps, pending, assumes, section = [], [], [], None
        for b in blocks:
            if b["type"] == "section":
                section = b["id"]
                continue
            if section == "s:cited":
                continue                     # results cited, not walked through
            if b["type"] in ("framing", "transition") and b["id"] not in ("introduction",
                                                                         "conclusion"):
                pending.append(strip(b["text"]))
            elif b.get("claim") and (section == "s:assumptions" or b["type"] == "postulate"):
                assumes.append(b["claim"].split("@")[0])
            elif b.get("claim"):
                steps.append({"id": b["claim"].split("@")[0], "type": b["type"],
                              "text": "\n\n".join(x for x in pending if x)})
                pending = []
        outro = " ".join(strip(b["text"]) for b in blocks if b["id"] == "conclusion")
        subject = d[len("trail-"):] if d.startswith("trail-") else None
        out.append({"id": d, "subject": subject, "theme": rec.get("theme") or subject,
                    "start": d == "tour",
                    "title": rec.get("title", d), "intro": intro, "outro": outro,
                    "assumes": assumes, "steps": steps})
    return out


def _mcp_tools():
    """The MCP server's tools as the server itself lists them, for the Contribute page."""
    from .mcp_server import tool_list
    return [{"name": t["name"], "description": t["description"],
             "args": list((t.get("inputSchema") or {}).get("properties") or {}),
             "required": list((t.get("inputSchema") or {}).get("required") or [])}
            for t in tool_list()]


def _contrib_example(folder=os.path.join("docs", "example-contribution")):
    """The worked example of a contribution (tested in tests/test_contrib_example.py)."""
    out = {}
    for name in ("entity.md", "proof-main.tex", "check.py"):
        p = os.path.join(folder, name)
        if os.path.exists(p):
            out[name] = open(p, encoding="utf-8").read()
    return out


def main(build="build", site="site", store="store", template="universe.template.html",
         out="transport_lab.html"):
    from .model import ID_RE, load_store
    g = json.load(open(os.path.join(build, "graph.json")))
    lay_path = os.path.join(build, "layout.json")
    if not os.path.exists(lay_path):
        from . import layout
        layout.main(build)
    lay = json.load(open(lay_path))
    st = load_store(store)
    known = {"proved", "imported", "conjectured", "refuted", "postulate", "defined",
             "live", "confirmed", "killed", "open", "settled"}
    g["nodes"] = [n for n in g["nodes"] if isinstance(n.get("id"), str)
                  and ID_RE.fullmatch(n["id"]) and n.get("status") in known
                  and n["id"] in lay["positions"]]
    keep = {n["id"] for n in g["nodes"]}
    g["edges"] = [e for e in g["edges"] if e["src"] in keep and e["dst"] in keep]
    checks = _checks_by_entity(st)
    own = _own_checks(st, site, build)
    from . import labels as labelreg
    reg = labelreg.load(store)
    ids_all = set(st.entities)

    def res(eid, text):
        e = st.entities.get(eid)
        if e is None or not text:
            return text
        loc = e.meta.get("locators") or {}
        return labelreg.resolve(text, loc.get("paper"), reg, entities=ids_all, plain=True)

    notes, notes_of, note_text = {}, {}, {}
    for eid, e in sorted(st.entities.items()):
        if e.kind != "note":
            continue
        on = [t for t in e.meta.get("comments_on") or [] if t in keep]
        if not on:
            continue
        notes[eid] = {"id": eid, "title": e.title, "status": e.status,
                      "comments_on": on,
                      "line": int((e.meta.get("locators") or {}).get("line") or 0)}
        note_text[eid] = res(eid, (e.levels.get("formal") or "").strip())
        for t in on:
            notes_of.setdefault(t, []).append(eid)
    # what the map, the search box and the record views need stays in the page; everything a
    # reader opens (statement levels, proofs, notes, runs, history, coverage) goes to
    # site/data/<subject>.json, fetched when a result is selected (roadmap item 14)
    lab = os.path.dirname(os.path.abspath(st.root))
    git_rows = {}   # commit history is not shown (see _entity_history)
    programmes = _programmes(st.config)
    default_prog = st.config.get("default_programme") or (programmes[0]["id"] if len(programmes) == 1 else None)
    nodes, data_chunks, search_entries = [], {}, []
    for n in g["nodes"]:
        nid = n["id"]
        e = st.entities.get(nid)
        d = {k: n.get(k) for k in V2_INLINE}
        d["title"] = _display_title(n.get("title"))
        d["pos"] = lay["positions"][nid]
        d["depth"] = lay["depth"].get(nid, 0)
        if lay.get("positions_core"):
            d["posf"] = lay["positions_core"].get(nid, d["pos"])
            d["cd"] = lay.get("core_distance", {}).get(nid, -1)
        if d.get("one_liner"):
            d["one_liner"] = res(nid, d["one_liner"])
        full = {k: n.get(k) for k in V2_DEFER}
        for lv in ("formal", "technical", "lay"):
            if full.get(lv):
                full[lv] = res(nid, full[lv])
        if e is not None:
            full["proofs"] = {k: res(nid, v.strip()) for k, v in e.proofs.items() if v.strip()}
            full["derivations"] = [{"name": x.get("name"), "uses": x.get("uses") or [],
                                    "assumes": x.get("assumes") or []}
                                   for x in e.derivations() if isinstance(x, dict)]
            if e.meta.get("tags"):
                d["tags"] = list(e.meta["tags"])
            rel = os.path.relpath(os.path.abspath(e.path), lab).replace(os.sep, "/")
            full["history"] = _entity_history(e, git_rows.get(rel, []))
            cov = _coverage(e)
            if cov:
                full["coverage"] = cov
                weak = _weak_coverage(cov)
                if weak:
                    d["cov"] = weak
            d["trust"] = _trust(e)
            if e.meta.get("credit"):
                full["credit"] = [dict(c) for c in e.meta["credit"] if isinstance(c, dict)]
            if e.meta.get("amendments"):
                full["amendments"] = [dict(x) for x in e.meta["amendments"] if isinstance(x, dict)]
            if e.meta.get("signoffs"):
                full["signoffs"] = [dict(s) for s in e.meta["signoffs"] if isinstance(s, dict)]
            if e.meta.get("quantities"):
                full["quantities"] = [str(q).split("@")[0] for q in e.meta["quantities"]]
            if programmes:
                d["programme"] = e.meta.get("programme") or default_prog
        full["verified"] = checks.get(nid, [])
        if nid in own:
            full["own"] = own[nid]
            r = own[nid].get("run") or {}
            # the in-browser run of every check orders by this (CPython ms of the fast functions)
            d["ck"] = sum(f[2] for f in (r.get("fns") or []) if f[2] <= 400)
        if nid in notes_of:
            d["notes"] = sorted(notes_of[nid], key=lambda x: notes[x]["line"])
        # the record and open-problem views and the trail steps show these levels without
        # opening the result, so they stay in the page for those results
        if (n.get("kind") == "prediction" or n.get("status") in ("refuted", "conjectured")
                or (n.get("kind") == "question" and n.get("status") == "open")):
            d.update({k: full.get(k) for k in ("formal", "lay", "technical") if full.get(k)})
        chunk = data_chunks.setdefault(_data_chunk_of(d.get("subject")), {})
        chunk[nid] = full
        for x in d.get("notes") or []:
            chunk.setdefault("__notes__", {})[x] = note_text[x]
        search_entries.append(("n", nid, " ".join(str(x or "") for x in (
            d["title"], d["title"], d.get("one_liner"), full.get("lay"), full.get("technical")))))
        nodes.append(d)
    trail_ids = {s["id"] for t in _trails(os.path.join(lab, "documents")) for s in t["steps"]}
    for d in nodes:
        if d["id"] in trail_ids and not d.get("lay"):
            lay_text = data_chunks[_data_chunk_of(d.get("subject"))][d["id"]].get("lay")
            if lay_text:
                d["lay"] = lay_text
    for nid, nt in notes.items():
        search_entries.append(("t", nid, " ".join((nt["title"], nt["title"], _note_words(note_text[nid])))))
    quantities = _quantities(st)
    for q in quantities:
        search_entries.append(("q", q["id"], " ".join((q["title"], q["title"], q["symbol"], q["one_liner"],
                                                       q["note"], q["source"]))))
    ddir = os.path.join(site, "data")
    os.makedirs(ddir, exist_ok=True)
    for old in os.listdir(ddir):
        if old.endswith(".json"):
            os.remove(os.path.join(ddir, old))
    for c, m in data_chunks.items():
        _dump(m, os.path.join(ddir, c + ".json"))
    _dump(_search_index(search_entries), os.path.join(ddir, "search.json"))
    subjects_y = yaml.safe_load(open(os.path.join(store, "subjects.yaml")))
    by_side = {}
    for x in subjects_y:
        by_side.setdefault(x.get("side", "synthesis"), []).append(x["id"])
    subjects = []
    for x in subjects_y:
        side = x.get("side", "synthesis")
        members = by_side[side]
        k, m = members.index(x["id"]), len(members)
        hue = SIDE_HUE.get(side, 0) + (k - (m - 1) / 2) * (44 / max(m, 1))
        subjects.append({"key": x["id"], "title": x["title"], "side": side,
                         "about": x.get("about", ""), "hue": round(hue, 1),
                         "shade": k % 2})
    docs_root = os.path.join(os.path.dirname(os.path.abspath(store)), "documents")
    # one generated document per deposited paper: variants (results-only), companion notes and
    # assembled documents that were never deposited stay in the store, off the page; T14c, a
    # working note not yet deposited, is shown by Leon's decision of 2026-10-27
    documents = [d for d in _documents(docs_root, {n["id"]: n for n in g["nodes"]}, st, site)
                 if d["kind"] != "trail" and not d["id"].endswith("results-only")
                 and not d["id"].startswith("trail-")
                 and (d.get("doi") or d.get("paper") in SHOWN_UNDEPOSITED)]
    shown = {d["id"] for d in documents}
    pdir = os.path.join(site, "pdf")
    if os.path.isdir(pdir):              # a PDF of a document off the page is not published
        for f in os.listdir(pdir):
            if f.endswith(".pdf") and f[:-4] not in shown:
                os.remove(os.path.join(pdir, f))
    for d in documents:
        if not d.get("subtitle") and ": " in d["title"]:
            d["title"], d["subtitle"] = d["title"].split(": ", 1)
        ab = next((b.get("text") for b in d["blocks"] if b.get("type") == "abstract"), "") or ""
        ab = re.sub(r"\s*\[\[(?:c:[^\]]+|t)\]\]", "", ab).strip()
        words = ab.split()
        d["abstract"] = " ".join(words[:90]) + (" …" if len(words) > 90 else "")
    titles = _paper_titles(os.path.normpath(os.path.join(
        st.root, st.config.get("legacy_scripts_dir") or "..")))
    papers = {}
    for n in nodes:
        code = (n.get("locators") or {}).get("paper")
        if code:
            papers.setdefault(code, []).append(n["id"])
    order = {c: i for i, c in enumerate(PAPER_ORDER)}
    collections = [{"id": "paper:" + c, "kind": "Transport Papers",
                    "title": (c.replace("T0", "T") + ": " + titles[c]) if c in titles else c,
                    "members": ids}
                   for c, ids in sorted(papers.items(), key=lambda kv: order.get(kv[0], 99))
                   if c not in UNLISTED_COLLECTIONS]
    collections += [{"id": "doc:" + d["id"], "kind": "Generated documents",
                     "title": d["title"],
                     "members": [b["claim"].split("@")[0] for b in d["blocks"] if b.get("claim")]}
                    for d in documents]
    tag_members = {}
    for n in nodes:
        for t in n.get("tags") or []:
            tag_members.setdefault(t, []).append(n["id"])
    tags = [{"id": t["id"], "title": t.get("title", t["id"]), "group": t.get("group", ""),
             "about": t.get("about", ""), "count": len(tag_members.get(t["id"], []))}
            for t in st.tags if tag_members.get(t["id"])]
    collections += [{"id": "tag:" + t["id"], "kind": "Tags", "title": t["title"],
                     "about": t["about"], "members": tag_members[t["id"]]} for t in tags]
    nb_path = os.path.join(store, "notebook.yaml")
    s = g["summary"]
    data = {"nodes": nodes,
            "notes": notes,
            "edges": [{k: e[k] for k in ("src", "kind", "dst")} for e in g["edges"]],
            "subjects": subjects,
            "sides": [{"key": k, "title": t} for k, t, _ in SIDES],
            "collections": collections,
            "tags": tags,
            "trails": _trails(docs_root),
            "shells": lay.get("shells") or [],
            "documents": [{k: d[k] for k in d if k != "blocks"} for d in documents],
            "deposited": _deposited(st),
            "guides": (yaml.safe_load(open(os.path.join(site, "guides.yaml"), encoding="utf-8")) or []
                       if os.path.exists(os.path.join(site, "guides.yaml")) else []),
            "notebook": yaml.safe_load(open(nb_path)) if os.path.exists(nb_path) else [],
            "open_problems": [{**op, "entities": [x for x in (op.get("entities") or []) if x in keep]}
                              for op in (st.open_problems or [])],
            "references": {k: v.get("citation") for k, v in (yaml.safe_load(open(
                os.path.join(store, "references.yaml"))) or {}).items()}
            if os.path.exists(os.path.join(store, "references.yaml")) else {},
            "notation": yaml.safe_load(open(os.path.join(store, "notation.yaml"))),
            "layout": lay["report"],
            "summary": {"results": len(nodes), "links": len(g["edges"]),
                        "verified": s["checks"].get("pass-legacy", 0) + s["checks"].get("pass", 0),
                        "own_checks": sum(1 for n in nodes if n.get("ck") is not None),
                        "proofs": sum(1 for m in data_chunks.values() for k, v in m.items()
                                      if not k.startswith("__") and v.get("proofs")),
                        "sampled_only": sum(1 for n in nodes if n.get("cov") and n.get("check") in ("pass", "pass-legacy")),
                        "notes": len(notes),
                        "status": s["status"]},
            "trust_levels": list(TRUST_LEVELS),
            "programmes": programmes,
            "quantities": quantities,
            "data_files": sorted(data_chunks),
            "featured": [f for f in FEATURED if f in keep],
            "mcp_tools": _mcp_tools(),
            "contrib_example": _contrib_example(),
            "release": _release(lab),
            "site_url": _site_url(st.config),
            "preview_url": str(st.config.get("preview_url") or "")}
    _dump({d["id"]: d["blocks"] for d in documents}, os.path.join(ddir, "documents.json"))
    tpl = open(os.path.join(site, template), encoding="utf-8").read()
    html = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False, default=str,
                                                      separators=(",", ":")).replace("<", "\\u003c"))
    html = html.replace("/*SITE_URL*/", _site_url(st.config))
    path = os.path.join(site, out)
    open(path, "w", encoding="utf-8").write(html)
    _share_pages(site, nodes, _site_url(st.config))
    _singularity(site, nodes, store, _site_url(st.config))
    _publish_list(site)
    return path


VERDICT_STATE = {"consistent": "hold", "confirms": "hold", "survived": "hold", "tension": "press",
                 "contested": "press", "refutes": "press", "killed": "press"}


def _site_url(config):
    """store/config.yaml site_url, the public address of the page, ending in a slash; '' if unset."""
    u = str((config or {}).get("site_url") or "").strip()
    return u if not u or u.endswith("/") else u + "/"


TEX_SYM = {"neq": "≠", "ne": "≠", "leq": "≤", "le": "≤", "geq": "≥", "ge": "≥", "to": "→", "times": "×",
           "infty": "∞", "pi": "π", "cdot": "·", "pm": "±", "sim": "~", "approx": "≈", "in": "∈", "ell": "ℓ",
           "hbar": "ħ"}


def _plain_tex(t):
    """A one-liner as plain text for a link preview: TeX symbols to characters, commands to names."""
    t = re.sub(r"\\(?:mathbb|mathrm|mathcal|operatorname|text|mathbf)\{([^}]*)\}", r"\1", t)
    t = re.sub(r"\\frac\{([^}]*)\}\{([^}]*)\}", r"\1/\2", t)
    t = re.sub(r"\\([A-Za-z]+)", lambda m: TEX_SYM.get(m.group(1), m.group(1)), t)
    return re.sub(r"\s+", " ", t.replace("$", "").replace("{", "").replace("}", "")).strip()


def _share_pages(site, nodes, site_url):
    """site/r/<id>.html, one per result, only when the site has a public address: a small page whose
    link preview names the result (title, one-liner, the site's image) and which opens the result
    on the main page. Links shared from a result point here, since a preview cannot see a hash."""
    folder = os.path.join(site, "r")
    if not site_url:
        if os.path.isdir(folder):
            shutil.rmtree(folder)
        return 0
    os.makedirs(folder, exist_ok=True)
    keep = set()
    for n in nodes:
        nid = n["id"]
        if n.get("kind") == "note":
            continue
        title = _display_title(n.get("title")) or nid
        desc = _plain_tex(n.get("one_liner") or "")[:280]
        target = site_url + "#" + urllib.parse.quote(nid)
        e = html_lib.escape
        page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<title>{e(title)} | Zero Divisors</title>'
                f'<meta name="description" content="{e(desc)}">'
                f'<link rel="canonical" href="{e(target)}">'
                f'<meta property="og:type" content="article"><meta property="og:site_name" content="Zero Divisors">'
                f'<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">'
                f'<meta property="og:url" content="{e(site_url + "r/" + urllib.parse.quote(nid) + ".html")}">'
                f'<meta property="og:image" content="{e(site_url)}img/share.jpg">'
                f'<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
                f'<meta name="twitter:card" content="summary_large_image">'
                f'<meta http-equiv="refresh" content="0; url={e(target)}">'
                f'<script>location.replace({json.dumps(target)});</script></head>'
                f'<body><p><a href="{e(target)}">{e(title)}</a></p></body></html>')
        name = nid + ".html"
        keep.add(name)
        with open(os.path.join(folder, name), "w", encoding="utf-8") as fh:
            fh.write(page)
    for f in os.listdir(folder):
        if f not in keep:
            os.remove(os.path.join(folder, f))
    return len(keep)


def _singularity(site, nodes, store, site_url=""):
    """site/singularity.html, the Lab's introduction (a first-person fall into a black hole),
    from site/singularity.template.html: its predictions board is read from the record, and
    the deposited result numbers its subtitles cite (T5 Thm 2.5) are mapped to the results."""
    tpl_path = os.path.join(site, "singularity.template.html")
    if not os.path.exists(tpl_path):
        return None
    preds = []
    for n in nodes:
        if n.get("kind") != "prediction":
            continue
        o = (n.get("observations") or [{}])[0] or {}
        paper = str((n.get("locators") or {}).get("paper") or "")
        m = re.match(r"^T0*(\d+)([a-c]?)", paper)
        note = " ".join(str(o.get("result") or "no data yet").split())
        if len(note) > 70:
            note = note[:70].rsplit(" ", 1)[0].rstrip(",;:") + "..."
        preds.append({"st": VERDICT_STATE.get(o.get("verdict"), "wait"), "title": n.get("title", ""),
                      "paper": f"T{int(m.group(1))}{m.group(2)}" if m else paper.split(" ")[0], "note": note,
                      "id": n.get("id")})
    order = {"press": 0, "hold": 1, "wait": 2}
    preds.sort(key=lambda p: (order[p["st"]], p["paper"]))
    refs = {}
    lp = os.path.join(store, "labels.yaml")
    if os.path.exists(lp):
        for k, v in (yaml.safe_load(open(lp, encoding="utf-8")) or {}).items():
            if not isinstance(v, dict) or not v.get("entity") or ":" not in k:
                continue
            m = re.match(r"^T0*(\d+)([a-c]?)$", k.split(":", 1)[0])
            if m and v.get("number"):
                refs.setdefault(f"T{int(m.group(1))}{m.group(2)}", {}).setdefault(str(v["number"]), v["entity"])
    data = {"preds": preds, "refs": refs}
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    out = None
    # the two story pages: the Transport Principle (the landing page) and The Singularity
    for name in ("singularity", "principle"):
        tp_ = os.path.join(site, name + ".template.html")
        if not os.path.exists(tp_):
            continue
        tpl = open(tp_, encoding="utf-8").read()
        html = re.sub(r"/\*LAB_DATA\*/.*?/\*END_LAB_DATA\*/", lambda _m: blob, tpl, count=1, flags=re.S)
        html = html.replace("/*SITE_URL*/", site_url)
        out = os.path.join(site, name + ".html")
        open(out, "w", encoding="utf-8").write(html)
    return out


def _publish_list(site):
    """site/publish_files.json: every supporting file the artifact publishes beside the page,
    as published path -> source path (relative to the lab), for the publish call's `files`."""
    lab = os.path.dirname(os.path.abspath(site))
    files = {}
    for sub in ("checks", "data", "pdf"):
        d = os.path.join(site, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".json") or (sub == "pdf" and f.endswith(".pdf")):
                files[sub + "/" + f] = os.path.relpath(os.path.join(os.path.abspath(d), f), lab).replace(os.sep, "/")
    for page in ("singularity.html", "principle.html"):
        if os.path.exists(os.path.join(site, page)):
            files[page] = os.path.relpath(os.path.join(os.path.abspath(site), page), lab).replace(os.sep, "/")
    with open(os.path.join(site, "publish_files.json"), "w", encoding="utf-8") as fh:
        json.dump(files, fh, indent=1)
    return files


def main_v1(build="build", site="site", store="store", template="lab.template.html",
            out="transport_lab_v1.html"):
    g = json.load(open(os.path.join(build, "graph.json")))
    s = g["summary"]
    # the page shows only well-formed entities: a malformed id or status (which the
    # validator reports) never reaches the HTML
    from .model import ID_RE
    known = {"proved", "imported", "conjectured", "refuted", "postulate", "defined",
             "live", "confirmed", "killed", "open", "settled"}
    dropped = [n.get("id") for n in g["nodes"]
               if not (isinstance(n.get("id"), str) and ID_RE.fullmatch(n["id"])
                       and n.get("status") in known)]
    if dropped:
        print(f"site: left out {len(dropped)} malformed entities: {dropped[:5]}")
    g["nodes"] = [n for n in g["nodes"] if n.get("id") not in set(dropped)]
    keep_ids = {n["id"] for n in g["nodes"]}
    g["edges"] = [e for e in g["edges"] if e["src"] in keep_ids and e["dst"] in keep_ids]
    nodes = [{k: n.get(k) for k in KEEP} for n in g["nodes"]]
    typed = sum(1 for n in nodes if n["review"] == "typed")
    short = (f"{len(nodes)} results · {len(g['edges'])} links · "
             f"{s['checks'].get('pass-legacy', 0)} verified by script · {typed} typed")
    line = (", ".join(f"{k} {v}" for k, v in sorted(s["status"].items())) +
            "; evidence: " + ", ".join(f"{k} {v}" for k, v in sorted(s["checks"].items())))
    subjects = yaml.safe_load(open(os.path.join(store, "subjects.yaml")))
    tag_members = {}
    for n in nodes:
        for t in n.get("tags") or []:
            tag_members.setdefault(t, []).append(n["id"])
    tags = [{"id": t["id"], "title": t.get("title", t["id"]), "group": t.get("group", ""),
             "about": t.get("about", ""), "count": len(tag_members.get(t["id"], []))}
            for t in st.tags if tag_members.get(t["id"])]
    collections += [{"id": "tag:" + t["id"], "kind": "Tags", "title": t["title"],
                     "about": t["about"], "members": tag_members[t["id"]]} for t in tags]
    nb_path = os.path.join(store, "notebook.yaml")
    notebook = yaml.safe_load(open(nb_path)) if os.path.exists(nb_path) else []
    ids = {n["id"] for n in nodes}
    documents = _documents(os.path.join(os.path.dirname(os.path.abspath(store)), "documents"),
                           {n["id"]: n for n in g["nodes"]})
    data = {"nodes": nodes,
            "notes": notes,
            "edges": [{k: e[k] for k in ("src", "kind", "dst")} for e in g["edges"]],
            "subjects": [{"key": x["id"], "title": x["title"], "side": x.get("side", "")}
                         for x in subjects],
            "sides": [{"key": k, "title": t, "row": r} for k, t, r in SIDES],
            "papers": [{"code": c} for c in PAPER_ORDER],
            "notation": yaml.safe_load(open(os.path.join(store, "notation.yaml"))),
            "notebook": notebook,
            "documents": documents,
            "summary": {"short": short, "line": line},
            "featured": [f for f in FEATURED if f in ids]}
    tpl = open(os.path.join(site, template), encoding="utf-8").read()
    html = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False, default=str)
                       .replace("<", "\\u003c"))
    path = os.path.join(site, out)
    open(path, "w", encoding="utf-8").write(html)
    return path


if __name__ == "__main__":
    print(main(*sys.argv[1:3]))
