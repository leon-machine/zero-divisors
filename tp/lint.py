"""tp lint: the fast rules of the full check, for one entity at a time.

  tp lint <id | path/to/check.py | path/to/entity-folder> [...] [--no-run]
          [--store store] [--json] [--timeout S]
  tp lint --changed      entities whose files differ from git HEAD
  tp lint --all          every entity in the store with a check file or a check entry

For each entity it reports, with the full check's codes where one exists:

* the static rules of the evidence layer, applied by calling the evidence layer's own
  per-check code (validate._run_new_check) with the runner replaced: E401 (missing file
  or function, unparsable check), E402 (floats, math, true division), E403 (no GA
  import), E408 (a check function asserts nothing);
* W408: a check function with no integer literal, so the mutation test cannot run;
* L402: dict.setdefault in a check file (the in-browser engine stores int keys as strings
  there); use pyutil.get_or_set;
* checked_by against the file: E401 for an entry without its function, L401 for a
  check_/test_ function that no `kind: check` entry names (the full check never runs it);
* unless --no-run: each wired function run once, sandboxed, as layer 4 runs it
  (evidence.run_check): E406 / E409 on failure, I400 with the time on a pass, L409 over
  3 s (layer 4 reruns a function once per literal), E404 for a premise touched but not
  declared by any derivation, I405 (one line) for declared premises no function touches.
  With --no-run, E404 comes from a static scan of premise("<id>") calls instead;
* layer 1 of the full check (shape, statuses, levels, LaTeX, undeclared macros, em
  dashes, banned words) for that one entity, plus L113 for "load-bearing";
* L501: each `payload` clause, evaluated in the namespace of the entity's own check.py,
  must be exactly True.

Exit status 1 if any finding is an error. Lint never runs the mutation test (W413 and
the mutation half of E408) or the second, determinism run (E407); those stay with
`tp check`, and `tp mutants <id>` runs the mutation test for one entity.
"""
from __future__ import annotations

import argparse
import ast
import contextlib
import dataclasses
import inspect
import json
import os
import re
import secrets
import subprocess
import sys
import tempfile
import time

from . import evidence, validate
from .model import (ENTITY_DIRS, ENTITY_FILE, ID_RE, Store, _read_yaml, _tombstones,
                    load_entity, parse_pin)

SLOW_SECONDS = 3.0
CHECK_PREFIXES = ("check_", "test_")
LOAD_BEARING_RE = re.compile(r"load[\s-]+bearing", re.I)

# lint-only codes (no counterpart in the full check) and their severities
LINT_CODES = {
    "L000": "error",     # target not found / not an entity
    "L113": "error",     # "load-bearing" in entity text (house style)
    "L401": "warning",   # check function not wired by any checked_by entry
    "L402": "warning",   # dict.setdefault in a check (the browser engine mishandles it)
    "L409": "warning",   # check function slower than SLOW_SECONDS
    "L501": "error",     # payload clause not exactly True
}


@dataclasses.dataclass
class LintFinding:
    code: str
    entity: str
    message: str
    fix: str = ""

    @property
    def severity(self) -> str:
        if self.code in LINT_CODES:
            return LINT_CODES[self.code]
        return {"E": "error", "W": "warning", "I": "info"}[self.code[0]]

    def as_dict(self) -> dict:
        return {"code": self.code, "severity": self.severity, "entity": self.entity,
                "message": self.message, "fix": self.fix}


# ---------------------------------------------------------------------------
# the store context: everything but the entities (loading all of them takes seconds)
# ---------------------------------------------------------------------------

def store_context(root: str) -> Store:
    root = os.path.abspath(root)
    config = _read_yaml(os.path.join(root, "config.yaml"), {})
    if os.environ.get("TP_LEGACY_DIR"):           # as model.load_store does
        config = dict(config, legacy_scripts_dir=os.path.abspath(os.environ["TP_LEGACY_DIR"]))
    tomb, repl = _tombstones(root)
    return Store(root=root, entities={}, config=config, tombstones=tomb,
                 notation=_read_yaml(os.path.join(root, "notation.yaml"), {}),
                 lock={}, duplicates=[], replaced_by=repl,
                 subjects=_read_yaml(os.path.join(root, "subjects.yaml"), []),
                 tags=_read_yaml(os.path.join(root, "tags.yaml"), []))


def entity_folders(root: str):
    for sub in ENTITY_DIRS.values():
        base = os.path.join(root, sub)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            folder = os.path.join(base, name)
            if os.path.isfile(os.path.join(folder, ENTITY_FILE)):
                yield folder


def find_folder(root: str, eid: str):
    for sub in ENTITY_DIRS.values():
        folder = os.path.join(root, sub, eid)
        if os.path.isfile(os.path.join(folder, ENTITY_FILE)):
            return folder
    # folders are named by id; fall back to the front matter
    pat = re.compile(r"^id:\s*['\"]?([^'\"\s]+)['\"]?\s*$", re.M)
    for folder in entity_folders(root):
        with open(os.path.join(folder, ENTITY_FILE), encoding="utf-8") as fh:
            head = fh.read().replace("\r\n", "\n").split("\n---", 1)[0]
        m = pat.search(head)
        if m and m.group(1) == eid:
            return folder
    return None


def changed_folders(root: str) -> list[str]:
    """Entity folders under the store holding a file that differs from git HEAD."""
    root = os.path.abspath(root)
    top = subprocess.run(["git", "-C", root, "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True)
    if top.returncode:
        raise RuntimeError("--changed needs a git work tree: " + top.stderr.strip())
    top = top.stdout.strip()
    cp = subprocess.run(["git", "-C", top, "status", "--porcelain", "--untracked-files=all"],
                        capture_output=True, text=True, check=True)
    out = []
    subs = set(ENTITY_DIRS.values())
    for line in cp.stdout.splitlines():
        path = line[3:]
        if " -> " in path:                       # renames: the new path
            path = path.split(" -> ", 1)[1]
        path = path.strip('"')
        full = os.path.abspath(os.path.join(top, path))
        rel = os.path.relpath(full, root)
        parts = rel.split(os.sep)
        if len(parts) >= 2 and parts[0] in subs and not rel.startswith(".."):
            folder = os.path.join(root, parts[0], parts[1])
            if os.path.isfile(os.path.join(folder, ENTITY_FILE)) and folder not in out:
                out.append(folder)
    return out


# ---------------------------------------------------------------------------
# per-entity rules
# ---------------------------------------------------------------------------

class _Parsed:
    """One parse per check file, shared by every rule lint applies to it."""

    def __init__(self, src: str):
        self.src = src
        try:
            self.tree = ast.parse(src)
        except SyntaxError:
            self.tree = None
        self.defs, self.used, self.segments, self.premises = [], set(), {}, {}
        if self.tree is None:
            return
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Name):
                self.used.add(node.id)
            elif isinstance(node, ast.Attribute):
                self.used.add(node.attr)
            elif (isinstance(node, ast.Call) and node.args
                  and getattr(node.func, "id", getattr(node.func, "attr", None)) == "premise"
                  and isinstance(node.args[0], ast.Constant)
                  and isinstance(node.args[0].value, str)):
                self.premises.setdefault(id(node), node.args[0].value)
        for node in self.tree.body:
            if isinstance(node, ast.FunctionDef) and node.name not in self.segments:
                self.defs.append(node.name)
                # the function's own source: the per-function rules of the evidence
                # layer read only the function, so they give the same answer on it
                self.segments[node.name] = (ast.get_source_segment(src, node), node)

    def segment(self, func):
        seg = self.segments.get(func)
        return seg[0] if seg and seg[0] else self.src

    def static_premises(self, func) -> set[str]:
        """premise("<id>") calls with a literal id inside one function."""
        seg = self.segments.get(func)
        if not seg:
            return set()
        return {self.premises[id(n)] for n in ast.walk(seg[1]) if id(n) in self.premises}


class _Fast:
    """The evidence layer's rules, memoised by source for one lint run."""

    def __init__(self):
        self.parsed, self.static = {}, {}

    def parse(self, src) -> _Parsed:
        if src not in self.parsed:
            self.parsed[src] = _Parsed(src)
        return self.parsed[src]

    def static_problems(self, src):
        if src not in self.static:
            self.static[src] = self._orig_static(src)
        return list(self.static[src])

    def has_assertion(self, src, func):
        if self.parse(src).tree is None:
            # E401 already says the file does not parse; evidence.has_assertion would
            # raise SyntaxError here (so does the full check's _run_new_check)
            return True
        return self._orig_has(self.parse(src).segment(func), func)

    def int_literal_count(self, src, func):
        return evidence.int_literal_count(self.parse(src).segment(func), func)

    @contextlib.contextmanager
    def patched(self, run_check):
        """Route the evidence layer's own code (validate._run_new_check) through the
        memoised rules and the given runner."""
        names = ("static_problems", "has_assertion", "run_check")
        saved = {n: getattr(evidence, n) for n in names}
        self._orig_static, self._orig_has = saved["static_problems"], saved["has_assertion"]
        evidence.static_problems = self.static_problems
        evidence.has_assertion = self.has_assertion
        evidence.run_check = run_check
        try:
            yield
        finally:
            for n, f in saved.items():
                setattr(evidence, n, f)


def declared_premises(e) -> set[str]:
    """As layer 4 computes them: the uses and assumes of every derivation."""
    return {parse_pin(r)[0] for d in e.derivations() if isinstance(d, dict)
            for r in (d.get("uses") or []) + (d.get("assumes") or []) if parse_pin(r)}


def _layer1(ctx: Store, e) -> list:
    """Layer 1 of the full check on a store holding only e. Its info findings are
    store summaries (counts over the whole store), so they are left out."""
    rep = validate.Report()
    validate.layer1(dataclasses.replace(ctx, entities={e.id or "<unnamed>": e}), rep)
    return [f for f in rep.findings if f.severity != "info"]


def lint_entity(ctx: Store, folder: str, run: bool = True, timeout: int = 60,
                extra_files=()) -> tuple[str, list, dict]:
    """-> (entity id, findings, stats). Findings are LintFinding, deduplicated."""
    folder = os.path.abspath(folder)
    e = load_entity(folder)
    eid = e.id or os.path.basename(folder)
    out: list[LintFinding] = []
    stats = {"functions": 0, "ran": 0, "seconds": {}}

    def add(code, msg, fix=""):
        out.append(LintFinding(code, eid, msg, fix))

    # ---- layer 1 for this entity (shape, LaTeX, house style) ----
    for f in _layer1(ctx, e):
        add(f.code, f.message, f.fix)
    if e.parse_errors:
        return eid, _dedupe(out), stats
    banned = [w.lower() for w in (ctx.config.get("house_style") or {}).get("banned_words", [])]
    if "load-bearing" not in banned:
        for where, text in validate._texts(e) + validate._note_texts(e):
            if text and LOAD_BEARING_RE.search(text):
                add("L113", f"{where}: 'load-bearing' (house style)",
                    "say what the premise is used for instead")

    # ---- checked_by against the files ----
    entries = [ev for ev in (e.meta.get("checked_by") or []) if isinstance(ev, dict)]
    checks = [ev for ev in entries if ev.get("kind") == "check"]
    wired: dict[str, set] = {}
    for ev in checks:
        ref = str(ev.get("ref", ""))
        if "::" in ref:
            fname, func = ref.split("::", 1)
            wired.setdefault(fname, set()).add(func)
    files = set(wired)
    if os.path.exists(os.path.join(folder, "check.py")):
        files.add("check.py")
    for p in extra_files:
        if os.path.dirname(os.path.abspath(p)) == folder:
            files.add(os.path.basename(p))
    sources = {}
    for fname in sorted(files):
        path = os.path.join(folder, fname)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                sources[fname] = fh.read()

    # dict.setdefault: Brython 3.12 stores int keys as strings, so the browser run would differ
    for fname, src in sources.items():
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        lines_ = sorted({n.lineno for n in ast.walk(tree) if isinstance(n, ast.Call)
                         and isinstance(n.func, ast.Attribute) and n.func.attr == "setdefault"})
        if lines_:
            add("L402", f"{fname}: dict.setdefault on line(s) {', '.join(map(str, lines_[:6]))}",
                "use get_or_set(d, k, default) from pyutil (same behaviour in both engines)")

    # legacy entries: the static half of layer 4 (the script must exist)
    legacy_dir = ctx.config.get("legacy_scripts_dir")
    for ev in entries:
        if ev.get("kind") != "legacy":
            continue
        script = ev.get("script", "")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+\.py", str(script or "")):
            add("E401", f"legacy script must be a file name in the legacy folder, "
                        f"not a path: {script!r}")
        elif not os.path.exists(validate.legacy_path(ctx, legacy_dir, script)):
            add("E401", f"legacy script not found: {script}")

    # ---- each wired check function, through the evidence layer's own code ----
    declared = (validate._declared(e) if hasattr(validate, "_declared")
                else declared_premises(e))
    results: dict = {}

    def fake_run(store_root, efolder, source, func, *a, **k):
        return {"ok": True, "error": None, "touched": sorted(declared)}

    rep = validate.Report()
    orig_run = evidence.run_check
    fast = _Fast()
    runs = []                           # per-check run records, as layer 4 keeps them
    with_info = "run_info" in inspect.signature(validate._run_new_check).parameters
    with fast.patched(fake_run if not run else
                      (lambda *a, **k: _call_real(orig_run, results, timeout, *a, **k))):
        for ev in checks:
            if with_info:
                info = {"func": str(ev.get("ref", "")).split("::")[-1],
                        "derivation": ev.get("derivation"), "ok": False,
                        "touched": [], "quantities": []}
                runs.append(info)
                validate._run_new_check(ctx, rep, e, ev, declared, False, run_info=info)
            else:
                validate._run_new_check(ctx, rep, e, ev, declared, False)
        static = fast.static_problems
    for f in rep.findings:
        if f.code in ("W405", "I405"):  # summarised below, once per entity
            continue
        add(f.code, f.message, f.fix)

    # ---- per-function static rules lint adds (W408, unwired functions, E404 static) ----
    for fname, src in sources.items():
        pf = fast.parse(src)
        if pf.tree is None:
            if fname not in wired:
                for code, msg in static(src):
                    add(code, f"{fname}: {msg}")
            continue
        cands = [f for f in pf.defs if f.startswith(CHECK_PREFIXES)
                 and (f in wired.get(fname, set()) or f not in pf.used)]
        unwired = [f for f in cands if f not in wired.get(fname, set())]
        if fname not in wired:
            # not run by the full check yet; its static rules still apply once wired
            for code, msg in static(src):
                add(code, f"{fname} (not wired): {msg}")
        if unwired:
            add("L401", f"{fname}: {len(unwired)} function(s) with no `kind: check` entry, "
                        "never run by tp check: " + ", ".join(unwired),
                "tp wire-check " + eid)
        for func in sorted(wired.get(fname, set()) | set(unwired)):
            if f"def {func}(" not in src:
                continue                 # E401 already reported
            stats["functions"] += 1
            if func in unwired and not fast.has_assertion(src, func):
                add("E408", f"{func} asserts nothing ({fname}, not wired)")
            if fast.int_literal_count(src, func) == 0:
                add("W408", f"{func} has no integer literal to perturb; mutation test "
                            "will be skipped", "assert computed values against exact "
                            "expected values written in the function")
            if not run and func in wired.get(fname, set()):
                for p in sorted(pf.static_premises(func) - declared):
                    add("E404", f"check touches {p} but no derivation declares it "
                                "(static scan of premise() calls)",
                        f"add {p}@<version> to a derivation's uses, or stop touching it")

    # ---- the run: times, pass lines, premises touched against declared ----
    if run:
        touched_all: set[str] = set()
        for (src, func), (r, secs) in sorted(results.items(), key=lambda kv: kv[0][1]):
            stats["ran"] += 1
            stats["seconds"][func] = round(secs, 3)
            touched_all |= set(r.get("touched") or [])
            if r.get("ok"):
                add("I400", f"{func}: pass in {secs:.2f} s")
            if secs > SLOW_SECONDS and not r.get("timeout"):
                add("L409", f"{func} takes {secs:.1f} s; the mutation test reruns it once "
                            "per integer literal", "keep each check function under about 3 s")
        if results and all(r.get("ok") for r, _ in results.values()):
            for f in _untouched(ctx, e, declared, touched_all, runs if with_info else None):
                add(f.code, f.message, f.fix)

    # ---- payload ----
    payload = e.meta.get("payload")
    if isinstance(payload, list) and payload:
        out += [LintFinding("L501", eid, m) for m in check_payload(ctx.root, folder,
                                                                   payload, timeout)]
    return eid, _dedupe(out), stats


def _untouched(ctx, e, declared, touched, runs):
    """Declared premises no check function touched, as one I405 line. When the full
    check compares them per entity (validate.premise_findings), its verdict is used:
    the line says which of them tp check reports as W405 and which it expects. Other
    findings of that comparison (W414, quantities) pass through."""
    idle = sorted(declared - touched)
    if not idle:
        return []
    eid = e.id
    if runs is None or not hasattr(validate, "premise_findings"):
        return [LintFinding("I405", eid, f"{len(idle)} declared premise(s) never touched "
                                         "by any check function: " + ", ".join(idle))]
    # the comparison reads the premises themselves (restatement, status) and the
    # quantity entities; load just those
    ents = {eid: e}
    for pid in idle:
        f = find_folder(ctx.root, pid)
        if f:
            ents[pid] = load_entity(f)
    qdir = os.path.join(ctx.root, ENTITY_DIRS.get("quantity", "quantities"))
    if os.path.isdir(qdir):
        for name in os.listdir(qdir):
            if os.path.isfile(os.path.join(qdir, name, ENTITY_FILE)):
                q = load_entity(os.path.join(qdir, name))
                ents.setdefault(q.id, q)
    rep = validate.Report()
    validate.premise_findings(dataclasses.replace(ctx, entities=ents), rep, e, runs)
    unexplained = [f.message.split(" ", 1)[0] for f in rep.findings if f.code == "W405"]
    expected = [f.message.split(" ", 1)[0] for f in rep.findings if f.code == "I405"]
    out = [LintFinding(f.code, eid, f.message, f.fix) for f in rep.findings
           if f.code not in ("W405", "I405")]
    parts = []
    if unexplained:
        parts.append(f"{len(unexplained)} unexplained (W405 in tp check): "
                     + ", ".join(unexplained))
    if expected:
        parts.append(f"{len(expected)} expected: " + ", ".join(expected))
    if parts:
        out.append(LintFinding("I405", eid, "declared premises no check function touches: "
                               + "; ".join(parts)))
    return out


def _call_real(orig, results, timeout, store_root, efolder, source, func, *a, **k):
    key = (source, func)
    if key not in results:               # the evidence layer runs each check twice
        t0 = time.perf_counter()
        r = orig(store_root, efolder, source, func, timeout=timeout)
        results[key] = (r, time.perf_counter() - t0)
    return results[key][0]


def _dedupe(fs):
    seen, out = set(), []
    for f in fs:
        k = (f.code, f.entity, f.message)
        if k not in seen:
            seen.add(k)
            out.append(f)
    return out


# ---------------------------------------------------------------------------
# payload: exact Python clauses evaluated in the check's own namespace
# ---------------------------------------------------------------------------

def _hook_prelude() -> str:
    """The evidence layer's sandbox (its audit hook), without its runner."""
    src = evidence.DRIVER
    if "def _main():" in src and "def _hook(" in src:
        return src.split("def _main():", 1)[0]
    return "import json, os, sys, tempfile\n_hook = None\n"


PAYLOAD_MAIN = r'''
def _main():
    nonce = sys.stdin.readline().strip()
    sys.stdin.close()
    out = sys.stdout
    sys.path[:0] = [LIB, FOLDER]
    import tp_premise
    tp_premise.configure(STORE)
    import GA
    import importlib.util
    spec = importlib.util.spec_from_file_location("check_under_test", SRC)
    mod = importlib.util.module_from_spec(spec)
    if _hook is not None:
        sys.addaudithook(_hook)
    res = {"import_error": None, "clauses": []}
    try:
        spec.loader.exec_module(mod)
    except BaseException as exc:
        res["import_error"] = type(exc).__name__ + ": " + str(exc)[:300]
    else:
        ns = vars(mod)
        for expr in EXPRS:
            try:
                v = eval(compile(expr, "<payload>", "eval"), ns)
                res["clauses"].append({"ok": v is True, "value": repr(v)[:200]})
            except BaseException as exc:
                res["clauses"].append({"ok": False,
                                       "error": type(exc).__name__ + ": " + str(exc)[:200]})
    out.write("\n@@PAYLOAD-" + nonce + "@@" + json.dumps(res) + "\n")
    out.flush()

globals().pop("_main")()
'''


def check_payload(store_root: str, folder: str, payload: list, timeout: int = 60) -> list[str]:
    """-> failure messages, one per failing clause."""
    path = os.path.join(folder, "check.py")
    if not os.path.exists(path):
        return ["payload declared but the entity has no check.py to evaluate it in"]
    exprs = [str((p or {}).get("python", "")) for p in payload]
    labels = []
    for i, p in enumerate(payload):
        p = p or {}
        lab = f"payload[{i}]"
        if p.get("clause"):
            lab += f" clause {p['clause']}"
        labels.append(f"{lab} ({p.get('kind', '?')}): {p.get('python', '')}")
    with open(path, encoding="utf-8") as fh:
        source = fh.read()
    nonce = secrets.token_hex(16)
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "check_under_test.py")
        with open(src, "w", encoding="utf-8") as fh:
            fh.write(source)
        prelude = (f"LIB={evidence.LIB!r}\nFOLDER={os.path.abspath(folder)!r}\n"
                   f"STORE={os.path.abspath(store_root)!r}\nSRC={src!r}\nEXPRS={exprs!r}\n")
        drv = os.path.join(tmp, "payload_driver.py")
        with open(drv, "w", encoding="utf-8") as fh:
            fh.write(prelude + _hook_prelude() + PAYLOAD_MAIN)
        env = {"PATH": os.environ.get("PATH", ""), "TMPDIR": tmp, "PYTHONHASHSEED": "0"}
        try:
            cp = subprocess.run([sys.executable, "-I", drv], capture_output=True, text=True,
                                timeout=timeout, env=env, cwd=tmp, input=nonce + "\n")
        except subprocess.TimeoutExpired:
            return [f"payload evaluation timed out after {timeout}s"]
    tag = "@@PAYLOAD-" + nonce + "@@"
    hits = [l for l in cp.stdout.splitlines() if l.startswith(tag)]
    if len(hits) != 1:
        return ["payload evaluation produced no result: " + (cp.stderr or cp.stdout)[-300:]]
    res = json.loads(hits[0][len(tag):])
    if res["import_error"]:
        return [f"check.py does not import for the payload: {res['import_error']}"]
    msgs = []
    for lab, r in zip(labels, res["clauses"]):
        if not r["ok"]:
            why = r.get("error") or f"evaluates to {r.get('value')}, not True"
            msgs.append(f"{lab}: {why}")
    return msgs


# ---------------------------------------------------------------------------
# command line
# ---------------------------------------------------------------------------

def resolve_targets(ctx: Store, targets) -> tuple[list, list]:
    """-> ([(folder, extra_files)], [error findings])."""
    out, errs, seen = [], [], {}
    for t in targets:
        extra = []
        if os.path.exists(t):
            p = os.path.abspath(t)
            if os.path.isfile(p):
                extra = [p]
                p = os.path.dirname(p)
            if not os.path.isfile(os.path.join(p, ENTITY_FILE)):
                errs.append(LintFinding("L000", t, f"no {ENTITY_FILE} in {p}"))
                continue
            folder = p
        elif ID_RE.fullmatch(t):
            folder = find_folder(ctx.root, t)
            if folder is None:
                errs.append(LintFinding("L000", t, f"no entity {t} in {ctx.root}"))
                continue
        else:
            errs.append(LintFinding("L000", t, "neither an entity id nor an existing path"))
            continue
        if folder in seen:
            seen[folder].extend(extra)
        else:
            seen[folder] = list(extra)
            out.append((folder, seen[folder]))
    return out, errs


def _has_check(folder: str) -> bool:
    if os.path.exists(os.path.join(folder, "check.py")):
        return True
    with open(os.path.join(folder, ENTITY_FILE), encoding="utf-8") as fh:
        return "kind: check" in fh.read()


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="tp lint", description=__doc__.split("\n\n")[0])
    ap.add_argument("targets", nargs="*",
                    help="entity ids, check.py paths or entity folders")
    ap.add_argument("--store", default="store")
    ap.add_argument("--no-run", action="store_true",
                    help="static rules only; do not run the check functions")
    ap.add_argument("--changed", action="store_true",
                    help="add every entity with a file that differs from git HEAD")
    ap.add_argument("--all", action="store_true",
                    help="every entity with a check file or a kind: check entry")
    ap.add_argument("--json", action="store_true", help="machine-readable findings")
    ap.add_argument("--timeout", type=int, default=60,
                    help="seconds per check function (default 60, as layer 4)")
    ap.add_argument("--quiet", action="store_true",
                    help="omit info lines (I400 pass times, I405)")
    a = ap.parse_args(argv[1:])
    t0 = time.perf_counter()
    if not os.path.isdir(a.store):
        print(f"tp lint: no store at {a.store}", file=sys.stderr)
        return 2
    ctx = store_context(a.store)
    targets = list(a.targets)
    if a.changed:
        try:
            targets += changed_folders(ctx.root)
        except (RuntimeError, subprocess.CalledProcessError) as exc:
            print(f"tp lint: {exc}", file=sys.stderr)
            return 2
    if a.all:
        targets += [f for f in entity_folders(ctx.root) if _has_check(f)]
    if not targets:
        if a.changed:
            if a.json:
                json.dump({"findings": [], "entities": [],
                           "summary": {"entities": 0, "functions": 0, "errors": 0,
                                       "warnings": 0, "info": 0, "seconds": 0.0,
                                       "run": not a.no_run}}, sys.stdout, indent=1)
                print()
            else:
                print("tp lint: no changed entities")
            return 0
        ap.print_usage(sys.stderr)
        return 2
    folders, findings = resolve_targets(ctx, targets)
    groups = []                         # [(eid, folder, findings, stats)]
    for folder, extra in folders:
        try:
            eid, fs, st = lint_entity(ctx, folder, run=not a.no_run, timeout=a.timeout,
                                      extra_files=extra)
        except Exception as exc:        # a lint crash on one entity must not hide the rest
            eid = os.path.basename(folder)
            fs, st = [LintFinding("L000", eid, f"lint failed: {type(exc).__name__}: {exc}")], {}
        groups.append((eid, folder, fs, st))
        findings += fs
    if a.quiet:
        findings = [f for f in findings if f.severity != "info"]
    elapsed = time.perf_counter() - t0
    n = {s: sum(f.severity == s for f in findings) for s in ("error", "warning", "info")}
    nfun = sum(g[3].get("functions", 0) for g in groups)
    summary = {"entities": len(groups), "functions": nfun, "errors": n["error"],
               "warnings": n["warning"], "info": n["info"], "seconds": round(elapsed, 2),
               "run": not a.no_run}
    if a.json:
        json.dump({"findings": [f.as_dict() for f in findings], "summary": summary,
                   "entities": [{"id": g[0], "folder": g[1], "stats": g[3]} for g in groups]},
                  sys.stdout, indent=1)
        print()
    else:
        for f in findings:
            if f.code == "L000":
                print(f"{f.code}  {f.entity}: {f.message}")
        verbose = len(groups) <= 20
        for eid, folder, fs, st in groups:
            fs = [f for f in fs if not (a.quiet and f.severity == "info")]
            if not fs and not verbose:
                continue
            print(f"{eid}  ({os.path.relpath(folder)})" + ("" if fs else ": ok"))
            for f in sorted(fs, key=lambda f: ("EWI".index(f.severity[0].upper()), f.code)):
                print(f"  {f.code}  {f.message}")
                if f.fix and f.severity != "info":
                    print(f"        fix: {f.fix}")
        print(f"tp lint: {len(groups)} entities, {nfun} check functions"
              f"{'' if a.no_run else ' run'}; {n['error']} error(s), "
              f"{n['warning']} warning(s), {n['info']} info; {elapsed:.1f} s")
    return 1 if n["error"] else 0


if __name__ == "__main__":
    sys.exit(main(["lint"] + sys.argv[1:]))
