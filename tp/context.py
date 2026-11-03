"""Context bundle: one compact Markdown file with what an agent needs to restate, check or
extend one result, so that it does not open a dozen files (roadmap item 3).

    tp context <id> [<id> ...] [--out FILE|DIR] [--store store] [--max-kb 30]
                    [--for check|restate|read]

Sections, in order: header; statement; derivation (premises, pins, proofs); quantities;
conventions (notation.yaml entries for the macros used, and the GTG digest when the result is
gravity-facing); shared library (lib/GA.py and, when present, lib/gtg.py, lib/fock.py,
lib/series.py, lib/pyutil.py, read with ast); existing evidence (check.py, coverage.yaml, the last recorded
run in site/check_runs.json, legacy tags); an example check from the same subject (--for
check); open problems and notes on the result; the rules a check must satisfy (--for check).

The bundle is trimmed to --max-kb by lowering the detail of the least important sections
first; a line under the header says what was cut. The store is loaded once per invocation
(several ids share one load); nothing is cached on disk.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
import time

import yaml

from . import derive, model
from .model import parse_pin

MODES = ("check", "restate", "read")
LIB_MODULES = ("GA", "gtg", "fock", "series", "pyutil")
SKIP_LEVEL = ("", "pending")

# --------------------------------------------------------------------------------------
# fixed digests
# --------------------------------------------------------------------------------------

GTG_DIGEST = r"""GTG conventions (digest of docs/gtg-dictionary.md C1-C11 and
store/conventions.md "Gravity"; read those for sources):
- C1 background: flat spacetime, vectors of Cl(1,3), (+,-,-,-), Q(a) = a^2; coordinates are
  labels only, with no gravitational meaning.
- C2 \hb: the position-gauge field, LDG's underbar h (LDG's overbar h is \hb^T). Derived
  metric g(a,b) = \hb^{-1}(a).\hb^{-1}(b), g_mu = \hb^{-1}(e_mu); only on U, where \hb is
  invertible (C8). Say "a field (\hb, Omega) whose derived metric is g".
- C3, C4, C10 Omega: bivector-valued; D_a M = a.\nabla M + Omega(a) x M, A x B = (AB-BA)/2;
  spinors D_a psi = a.\nabla psi + Omega(a) psi/2. Cartan-form values are the negative.
- C5, C6 store sign: R(a^b) = a.\nabla Omega(b) - b.\nabla Omega(a) + Omega(a) x Omega(b);
  calR(B) := -R(\hb(B)), opposite to LDG/DL. de Sitter calR(B) = (Lambda/3)B, Ric = Lambda g;
  Schwarzschild calR(sigma_r) = +2M/r^3 sigma_r; Ric^o = -Ric; calG(a) + Lambda a = -8 pi T(a).
  C11: R(u,v)w = -calR(u^v).w.
- PG gauge: \hb = 1 - beta P, P(a) = (a.e_t) e_r, P^2 = 0, \hb^{-1} = 1 + beta P;
  Schwarzschild beta = sqrt(2M/r), Omega(e_t) = (M/r^2) sigma_r, sigma_r = e_r e_t;
  de Sitter beta = -rH (expanding chart), H^2 = Lambda/3.
- Tractor field, Cl(2,4): Omega(a) - \nInf ^ \hb^{-1}(a) + \nO ^ \Sch(\hb^{-1}(a)).
- C9 G = c = 1; C7 keep (+,-,-,-) or the statement's declared signature."""

CHECK_RULES = """1. Header docstring: what the check tests, and which part if it tests only part.
2. `import GA` (static rule E403); shared engines from lib/ (`import gtg`, `fock`, `series`
   where present), never pasted copies.
3. Functions named `check_*`; every one contains an `assert` (E408).
4. Exact arithmetic only: Fraction, int, GA. No float literals, float(), math, cmath, numpy,
   random, sympy, and no int / int (E402). No dict.setdefault (L402): `pyutil.get_or_set`.
5. Inside each function, `premise("<id>")` for every uses/assumes premise whose content it
   relies on; none decorative (W405); never touch an undeclared premise (E404). No call for a
   restatement of the claim itself or for `-external` literature it does not rely on.
6. Mutation-sensitive: the integer literals inside a function are the independently derived
   expected values; perturbing one must fail (E408/W413). No tautologies. `tp mutants <id>`
   shows which literals survive.
7. Generic sample inputs at module level, light module-level code (others import EXPORTS).
8. Under about 3 s per function (layer 4 reruns it once per literal).
9. Test the formal statement as stated, all clauses; enumerate finite classifications. No
   computable content: no check. Misstated: report it, do not edit the statement.
10. Before reporting: `tp lint <check.py>` and `python3 colony/runcheck.py <check.py>`;
    wire it with `tp wire-check <id>`, never by hand-editing entity.md."""

GRAV_MACRO = re.compile(r"\\(?:hb|Omega|Ric|Sch|calR)\b|\\mathcal\{[RGW]\}")
GRAV_WORD = re.compile(r"\b(?:gravit\w*|connection|curvature|field strength|horizons?|metric|"
                       r"Schwarzschild|de Sitter|Ricci|Riemann|geodesics?|Einstein|Kerr|"
                       r"tractor|Painlev|gauge field|surface gravity|black hole)\b", re.I)
MACRO_RE = re.compile(r"\\([A-Za-z]+)")
FOCK_WORD = re.compile(r"Fock|\\ket|\\bra|\bCAR\b|ladder|creation|annihilat|vacuum|"
                       r"fermion|occupation|\bmodes?\b|Witt pair|number operator", re.I)
SERIES_WORD = re.compile(r"power series|series|expansion|Taylor|asymptotic|order \$?N|"
                         r"truncat|two loops?|one loop|running", re.I)
CLAIMREF = re.compile(r"\\claimref\{([^}]+)\}")


# --------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------

class _FastYaml:
    """yaml with the C safe loader, for the duration of one store load (about ten times
    faster than the pure-Python loader on the full store)."""

    def __getattr__(self, name):
        return getattr(yaml, name)

    @staticmethod
    def safe_load(text):
        return yaml.load(text, Loader=yaml.CSafeLoader)


def load_store_fast(root: str):
    if not hasattr(yaml, "CSafeLoader"):
        return model.load_store(root)
    real = model.yaml
    model.yaml = _FastYaml()
    try:
        return model.load_store(root)
    finally:
        model.yaml = real


def _cut(text: str, cap, where: str = "") -> str:
    text = (text or "").strip()
    if cap is None or len(text) <= cap:
        return text
    tail = f" [... {len(text) - cap} more chars" + (f"; full text in {where}]" if where else "]")
    return text[:cap].rstrip() + tail


def _first_para(text: str) -> str:
    return re.split(r"\n\s*\n", (text or "").strip(), maxsplit=1)[0].strip()


def _first_line(doc) -> str:
    doc = (doc or "").strip()
    return doc.splitlines()[0].strip() if doc else ""


def _bytes(s: str) -> int:
    return len(s.encode("utf-8"))


def _fence(text: str, lang: str = "") -> str:
    fence = "````" if "```" in text else "```"
    return f"{fence}{lang}\n{text.rstrip()}\n{fence}"


def lib_api(path: str, with_docs: bool = True) -> list[str]:
    """Public top-level functions and classes of a library module, by ast (never imported)."""
    try:
        with open(path, encoding="utf-8") as fh:
            tree = ast.parse(fh.read())
    except (OSError, SyntaxError) as exc:
        return [f"- (could not read: {exc})"]
    out = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("_"):
            sig = f"{node.name}({ast.unparse(node.args)})"
        elif isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
            init = next((n for n in node.body if isinstance(n, ast.FunctionDef)
                         and n.name == "__init__"), None)
            args = ast.unparse(init.args).replace("self, ", "").replace("self", "") if init else ""
            sig = f"class {node.name}({args})"
        else:
            continue
        doc = _first_line(ast.get_docstring(node)) if with_docs else ""
        out.append(f"- `{sig}`" + (f": {doc}" if doc else ""))
    return out


def check_functions(src: str) -> list[tuple[str, str, bool]]:
    """(name, first docstring line, has assert) for each top-level check_/test_ function."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    out = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name.startswith(("check_", "test_")):
            has = any(isinstance(n, ast.Assert) for n in ast.walk(node))
            out.append((node.name, _first_line(ast.get_docstring(node)), has))
    return out


# --------------------------------------------------------------------------------------
# the bundle builder
# --------------------------------------------------------------------------------------

class Context:
    """Loads the store once; `bundle(id)` renders one context file."""

    def __init__(self, store_root: str = "store"):
        self.root = os.path.abspath(store_root)
        self.lab = os.path.dirname(self.root)
        self.store = load_store_fast(self.root)
        ents = self.store.entities
        self.eff = derive.effective_status(self.store)
        self.runs = {}
        rp = os.path.join(self.lab, "site", "check_runs.json")
        if os.path.exists(rp):
            try:
                with open(rp, encoding="utf-8") as fh:
                    self.runs = json.load(fh).get("runs") or {}
            except (OSError, ValueError):
                self.runs = {}
        self.notes_on = {}
        for n in ents.values():
            if n.kind == "note":
                for t in n.meta.get("comments_on") or []:
                    self.notes_on.setdefault(t, []).append(n.id)
        self.problems_on = {}
        for op in self.store.open_problems or []:
            if isinstance(op, dict):
                for t in op.get("entities") or []:
                    self.problems_on.setdefault(t, []).append(op)
        self.users = {}
        for a, bs in derive.logical_graph(self.store).items():
            for b in bs:
                self.users.setdefault(b, []).append(a)
        self.subject_titles = {s.get("id"): s.get("title") for s in self.store.subjects or []
                               if isinstance(s, dict)}
        self._lib = {}
        self._examples = None

    # ---- small lookups -------------------------------------------------------------
    def rel(self, path: str) -> str:
        return os.path.relpath(path, self.lab)

    def one_liner(self, e) -> str:
        one = (e.levels.get("one-liner") or "").strip()
        if one in SKIP_LEVEL:
            one = re.sub(r"\s+", " ", (e.levels.get("formal") or "")).strip()
            one = one[:200] + ("..." if len(one) > 200 else "")
        return one

    def lib(self, name: str, with_docs: bool):
        key = (name, with_docs)
        if key not in self._lib:
            p = os.path.join(self.lab, "lib", f"{name}.py")
            self._lib[key] = lib_api(p, with_docs) if os.path.exists(p) else None
        return self._lib[key]

    def run_passes(self, eid: str) -> bool:
        r = self.runs.get(eid)
        return bool(r and not r.get("load_error") and r.get("functions")
                    and all(f.get("ok") for f in r["functions"]))

    def example_for(self, e):
        """Shortest passing own check.py from the same subject that imports GA, calls
        premise() and asserts in every function. -> (entity id, path, source, note)."""
        if self._examples is None:
            self._examples = []
            for x in self.store.entities.values():
                p = os.path.join(x.path, "check.py")
                if os.path.exists(p):
                    self._examples.append((os.path.getsize(p), x.id, p, x.meta.get("subject")))
            self._examples.sort()
        subj = e.meta.get("subject")
        for same in (True, False):
            for _size, xid, p, s in self._examples:
                if xid == e.id or (same and s != subj):
                    continue
                if self.runs and not self.run_passes(xid):
                    continue
                with open(p, encoding="utf-8") as fh:
                    src = fh.read()
                fns = check_functions(src)
                if (re.search(r"^\s*import GA\b|^\s*from GA import", src, re.M)
                        and "premise(" in src and fns and all(h for _, _, h in fns)):
                    note = "same subject" if same else f"no passing example in subject {subj}; from {s}"
                    if not self.runs:
                        note += "; no recorded run (site/check_runs.json missing)"
                    return xid, p, src, note
        return None

    # ---- sections --------------------------------------------------------------------
    def s_header(self, e, mode):
        m = e.meta
        L = [f"# Context: `{e.id}`", "", f"**{e.title}**", ""]
        eff = e.status if e.kind == "prediction" else self.eff.get(e.id)
        st = f"{e.status}" + (f" (effective: {eff})" if eff and eff != e.status else "")
        L.append(f"- kind: {e.kind}; status: {st}; version: {e.version}")
        subj = m.get("subject")
        if subj:
            t = self.subject_titles.get(subj)
            L.append(f"- subject: {subj}" + (f" ({t})" if t else "")
                     + (f"; tags: {', '.join(m['tags'])}" if m.get("tags") else ""))
        for k in ("programme", "trust"):
            if m.get(k):
                L.append(f"- {k}: {m[k]}")
        if m.get("signoffs"):
            L.append("- signoffs: " + "; ".join(
                f"{s.get('level')} by {s.get('by')} {s.get('date')} (v{s.get('version')})"
                for s in m["signoffs"] if isinstance(s, dict)))
        loc = m.get("locators") or {}
        if loc:
            L.append("- locators: " + "; ".join(f"{k}: {v}" for k, v in loc.items()))
        L.append(f"- folder: {self.rel(e.path)}; used directly by {len(self.users.get(e.id, []))}")
        L.append(f"- one-liner: {self.one_liner(e)}")
        L.append(f"- bundle for: {mode}")
        return "\n".join(L)

    def s_statement(self, e, level):
        L = ["## Statement", "", "### formal", "", (e.levels.get("formal") or "(none)").strip()]
        tech = (e.levels.get("technical") or "").strip()
        if tech not in SKIP_LEVEL:
            L += ["", "### technical", "",
                  _cut(tech, 1500 if level >= 1 else None, self.rel(e.path) + "/entity.md")]
        lay = _first_para(e.levels.get("lay") or "")
        if lay not in SKIP_LEVEL and level < 2:
            L += ["", "### lay (first paragraph)", "", lay]
        if e.meta.get("payload"):
            L += ["", "### payload (exact Python, evaluated in check.py's namespace)", ""]
            for p in e.meta["payload"]:
                if isinstance(p, dict):
                    L.append(f"- {p.get('kind')}" + (f" {p['clause']}" if p.get("clause") else "")
                             + f": `{p.get('python')}`" + (f" ({p['note']})" if p.get("note") else ""))
        return "\n".join(L)

    def _premise_line(self, ref):
        p = parse_pin(ref)
        if not p:
            return f"- `{ref}`: malformed pin", None
        pid, pin = p
        x = self.store.entities.get(pid)
        if x is None:
            repl = self.store.replaced_by.get(pid)
            return (f"- `{ref}`: MISSING" + (f" (retired; replaced by `{repl}`)" if repl else "")), None
        stale = f"; STALE PIN: pinned v{pin}, current v{x.version}" if pin < x.version else ""
        ahead = f"; PIN AHEAD: pinned v{pin}, current v{x.version}" if pin > x.version else ""
        return (f"- `{ref}` [{x.kind}, {x.status}, v{x.version}{stale}{ahead}]: "
                f"{self.one_liner(x)}"), x

    def s_derivation(self, e, mode, level):
        prem_cap = {"check": None, "restate": 1200, "read": 0}[mode]
        prem_cap = {0: prem_cap, 1: 600 if prem_cap is None else min(prem_cap, 600)}.get(level, 0)
        proof_cap = {0: None, 1: 4000, 2: 1500}.get(level, 0)
        L = ["## Derivation", ""]
        m = e.meta
        if m.get("imported_from"):
            L.append("Imported from:")
            for s in m["imported_from"]:
                if isinstance(s, dict):
                    L.append("- " + "; ".join(f"{k}: {v}" for k, v in s.items()))
            L.append("")
        if m.get("kill_condition"):
            L.append("Kill condition: " + "; ".join(f"{k}: {v}" for k, v in m["kill_condition"].items()))
            L.append("")
        for ob in m.get("observations") or []:
            if isinstance(ob, dict):
                L.append(f"- observation {ob.get('date')}, {ob.get('dataset')}: "
                         f"{ob.get('verdict', '')} {_cut(str(ob.get('result', '')), 300)}")
        if m.get("observations"):
            L.append("")
        if m.get("comments_on"):
            L.append("Comments on:")
            for t in m["comments_on"]:
                x = self.store.entities.get(t)
                L.append(f"- `{t}`" + (f" [{x.kind}, {x.status}, v{x.version}]: {self.one_liner(x)}"
                                       if x else ": MISSING"))
            L.append("")
        shown = set()
        ds = [d for d in e.derivations() if isinstance(d, dict)]
        if not ds and e.kind in ("claim", "prediction"):
            L += [f"No derivation: the result is {e.status}.", ""]
        for d in ds:
            name = d.get("name", "")
            L.append(f"### derivation `{name}`" + (" (conditional)" if d.get("conditional") else ""))
            if d.get("note"):
                L.append(f"Note: {d['note']}")
            for k in ("uses", "assumes"):
                refs = d.get(k) or []
                if not refs:
                    continue
                L += ["", f"{k}:"]
                for ref in refs:
                    line, x = self._premise_line(ref)
                    L.append(line)
                    if x is None or prem_cap == 0:
                        continue
                    if x.id in shown:
                        L.append("  formal: (shown above)")
                        continue
                    shown.add(x.id)
                    f = (x.levels.get("formal") or "").strip()
                    if f:
                        f = _cut(f, prem_cap, self.rel(x.path) + "/entity.md")
                        L.append("  formal: " + f.replace("\n", "\n  "))
            text = e.proofs.get(name)
            if d.get("proof"):
                where = f"{self.rel(e.path)}/{d['proof']}"
                if text and proof_cap != 0:
                    L += ["", f"proof ({where}):", "", _fence(_cut(text, proof_cap, where), "latex")]
                else:
                    L += ["", f"proof: {where}" + ("" if text else " (empty)")]
            L.append("")
        for k in derive.TOP_PINNED:
            for ref in m.get(k) or []:
                L.append(f"{k}: " + self._premise_line(ref)[0][2:])
        for k in ("refuted_by", "settled_by"):
            for ref in m.get(k) or []:
                x = self.store.entities.get(ref)
                L.append(f"{k}: `{ref}`" + (f" [{x.kind}, {x.status}, v{x.version}]: "
                                             f"{self.one_liner(x)}" if x else ": MISSING"))
        prem = {parse_pin(r)[0] for d in ds for k in ("uses", "assumes")
                for r in d.get(k) or [] if parse_pin(r)}
        about = [a for a in m.get("about") or [] if a not in prem]
        cited = sorted(set(CLAIMREF.findall("\n".join([e.levels.get("formal") or "",
                                                        e.levels.get("technical") or ""]
                                                       + list(e.proofs.values()))))
                       - prem - set(about) - set(m.get("comments_on") or []) - {e.id})
        for title, ids in (("about (definitions)", about),
                           ("cited with \\claimref but not a premise", cited)):
            if ids:
                L += ["", f"{title}:"]
                for t in ids:
                    x = self.store.entities.get(t)
                    L.append(f"- `{t}`" + (f" [{x.kind}, {x.status}, v{x.version}]: "
                                           f"{self.one_liner(x)}" if x else ": MISSING"))
        lin = m.get("lineage") or {}
        for k, v in lin.items():
            if v:
                L.append(f"lineage {k}: " + ", ".join(f"`{x}`" for x in v))
        return "\n".join(L).rstrip()

    def s_quantities(self, e):
        rows = []
        if e.kind == "quantity" and isinstance(e.meta.get("quantity"), dict):
            rows.append((e.id, e.version, e.meta["quantity"]))
        for ref in e.meta.get("quantities") or []:
            p = parse_pin(ref)
            x = self.store.entities.get(p[0]) if p else None
            if x is None:
                rows.append((ref, None, None))
            else:
                rows.append((ref, x.version, x.meta.get("quantity") or {}))
        if not rows:
            return ""
        L = ["## Quantities", "", "| quantity | symbol | value | uncertainty | units | source |",
             "|---|---|---|---|---|---|"]
        for ref, _v, q in rows:
            if q is None:
                L.append(f"| `{ref}` | MISSING | | | | |")
                continue
            src = q.get("source") or {}
            src = "; ".join(str(src.get(k)) for k in ("citation", "locator") if src.get(k)) \
                if isinstance(src, dict) else str(src)
            L.append(f"| `{ref}` | {q.get('symbol', '')} | {q.get('value', '')} | "
                     f"{q.get('uncertainty', '')} | {q.get('units', '')} | {src} |")
        return "\n".join(L)

    def texts_for_macros(self, e, mode):
        parts = [e.levels.get(k) or "" for k in model.LEVELS] + list(e.proofs.values())
        if mode == "check":
            for d in e.derivations():
                if isinstance(d, dict):
                    for ref in (d.get("uses") or []) + (d.get("assumes") or []):
                        p = parse_pin(ref)
                        x = self.store.entities.get(p[0]) if p else None
                        if x is not None:
                            parts.append(x.levels.get("formal") or "")
        return "\n".join(parts)

    def gravity_facing(self, e) -> bool:
        own = "\n".join([e.levels.get("formal") or "", e.levels.get("technical") or ""]
                        + list(e.proofs.values()))
        return bool(GRAV_MACRO.search(own) or GRAV_WORD.search(own))

    def s_conventions(self, e, mode, level):
        notation = self.store.notation or {}
        used = sorted({m for m in MACRO_RE.findall(self.texts_for_macros(e, mode)) if m in notation})
        L = ["## Conventions", ""]
        if used:
            L.append("Macros (store/notation.yaml) used in the statement, proofs"
                     + (" and premise statements" if mode == "check" else "") + ":")
            if level == 0:
                L += [f"- `\\{m}` = `{notation[m]}`" for m in used]
            elif level == 1:
                L.append(", ".join(f"`\\{m}`" for m in used))
            else:
                L.append(f"{len(used)} macros; see store/notation.yaml")
        else:
            L.append("No store macros are used.")
        if e.meta.get("notation"):
            L.append("Entity notation: " + "; ".join(str(x) for x in e.meta["notation"]))
        L.append("")
        L.append("House notation: Q(v) for the square of a vector; Cl(p,q) has p generators of "
                 "square +1; spacetime Cl(1,3) (+,-,-,-); completion Cl(2,4). Imaginary units: "
                 "i = I_4 in field theory, right multiplication by I_6 = I_4 E on conformal "
                 "spinors (store/conventions.md).")
        if self.gravity_facing(e):
            L += ["", GTG_DIGEST]
        return "\n".join(L)

    def relevant_libs(self, e) -> set:
        """GA always; gtg for gravity-facing results; fock and series when the text
        speaks of modes or of expansions. The others are listed by name only."""
        text = "\n".join([e.title, e.levels.get("one-liner") or "", e.levels.get("formal") or "",
                          e.levels.get("technical") or ""] + list(e.proofs.values()))
        rel = {"GA"}
        if self.gravity_facing(e):
            rel.add("gtg")
        if FOCK_WORD.search(text):
            rel.add("fock")
        if SERIES_WORD.search(text):
            rel.add("series")
        return rel

    def s_library(self, e, level):
        L = ["## Shared library (lib/, on the path for checks)", ""]
        present = [n for n in LIB_MODULES if os.path.exists(os.path.join(self.lab, "lib", f"{n}.py"))]
        if level >= 3:
            return "\n".join(L + ["Modules: " + ", ".join(f"lib/{n}.py" for n in present)
                                  + ". Read their docstrings for the API."])
        rel = self.relevant_libs(e)
        brief = []
        for name in present:
            full = level < 2 and name in rel
            api = self.lib(name, with_docs=level == 0)
            if full:
                L += [f"### lib/{name}.py (`import {name}`)", ""] + api + [""]
            else:
                names = [m.group(1) for m in (re.match(r"- `(?:class )?([A-Za-z0-9_]+)", a)
                                              for a in api) if m]
                brief.append(f"- lib/{name}.py: " + (", ".join(names) or api[0][2:]))
        if brief:
            if level < 2:
                L.append("Other modules (names only; not obviously needed here):")
            L += brief
        return "\n".join(L).rstrip()

    def s_evidence(self, e, level):
        L = ["## Existing evidence", ""]
        cp = os.path.join(e.path, "check.py")
        src = None
        if os.path.exists(cp):
            with open(cp, encoding="utf-8") as fh:
                src = fh.read()
            L.append(f"Own check: {self.rel(cp)} ({_bytes(src)} bytes)")
            try:
                mdoc = _first_para(ast.get_docstring(ast.parse(src)) or "")
            except SyntaxError:
                mdoc = "(does not parse)"
            if mdoc and level == 0:
                L.append("Docstring: " + _cut(mdoc.replace("\n", " "), 600))
            for name, doc, has in check_functions(src):
                L.append(f"- `{name}`" + ("" if has else " (NO ASSERT)")
                         + (f": {doc}" if doc and level < 2 else ""))
        cov = os.path.join(e.path, "coverage.yaml")
        if os.path.exists(cov):
            with open(cov, encoding="utf-8") as fh:
                ctext = fh.read()
            if level == 0:
                L += ["", f"Coverage ({self.rel(cov)}):", _fence(_cut(ctext, 2500), "yaml")]
            else:
                L.append(f"Coverage: {self.rel(cov)}")
        run = self.runs.get(e.id)
        if run:
            L += ["", f"Last recorded run (site/check_runs.json, {run.get('ran_at', '?')}):"]
            if run.get("load_error"):
                L.append("- LOAD ERROR: " + _first_line(run["load_error"].strip().splitlines()[-1]))
            for f in run.get("functions") or []:
                line = f"- `{f.get('name')}`: {'pass' if f.get('ok') else 'FAIL'}, {f.get('ms')} ms"
                if f.get("touched") and level < 2:
                    line += "; touched " + ", ".join(f.get("touched"))
                if f.get("error"):
                    line += "; error: " + _cut(f["error"].strip().splitlines()[-1], 200)
                L.append(line)
        elif src is not None:
            L.append("No recorded run for this check in site/check_runs.json.")
        for ev in e.meta.get("checked_by") or []:
            if not isinstance(ev, dict):
                continue
            k = ev.get("kind")
            if k == "legacy":
                L.append(f"- legacy: {ev.get('script')} tags {', '.join(ev.get('tags') or [])}")
            elif k == "proof":
                L.append(f"- proof: derivation `{ev.get('derivation')}` (not machine-checked)")
            elif k == "lean":
                L.append(f"- lean: {ev.get('ref')}")
        if len(L) == 2:
            L.append("None declared.")
        return "\n".join(L)

    def s_example(self, e, level):
        ex = self.example_for(e)
        L = ["## Example check (house conventions)", ""]
        if ex is None:
            return "\n".join(L + ["No passing example found."])
        xid, p, src, note = ex
        L.append(f"`{self.rel(p)}` (for `{xid}`; {note}; {_bytes(src)} bytes)")
        if level == 0:
            L += ["", _fence(src, "python")]
        return "\n".join(L)

    def s_open(self, e, level):
        ops = self.problems_on.get(e.id, [])
        notes = self.notes_on.get(e.id, [])
        if not ops and not notes:
            return ""
        L = ["## Open problems and notes", ""]
        if level >= 1:
            return "\n".join(L + [f"{len(ops)} open problems and {len(notes)} notes name this result "
                                  "(store/open_problems.yaml; store/notes/)."])
        for op in ops:
            L.append(f"- open problem `{op.get('id')}` [{op.get('status')}, {op.get('difficulty')}]: "
                     f"{op.get('title')}")
        for nid in sorted(notes):
            n = self.store.entities[nid]
            L.append(f"- note `{nid}` ({n.status}): {n.title}")
        return "\n".join(L)

    # ---- assembly ---------------------------------------------------------------------
    ORDER = ("header", "statement", "derivation", "quantities", "conventions", "library",
             "evidence", "example", "open", "rules")
    # (section, level) steps, least important first
    CUTS = {
        "check": [("open", 1), ("evidence", 1), ("library", 1), ("statement", 1),
                  ("conventions", 1), ("derivation", 1), ("library", 2), ("example", 1),
                  ("derivation", 2), ("evidence", 2), ("conventions", 2), ("library", 3),
                  ("derivation", 3), ("statement", 2)],
        "restate": [("open", 1), ("evidence", 1), ("library", 3), ("statement", 1),
                    ("conventions", 1), ("derivation", 1), ("evidence", 2), ("derivation", 2),
                    ("conventions", 2), ("derivation", 3), ("statement", 2)],
        "read": [("evidence", 1), ("open", 1), ("statement", 1), ("derivation", 1),
                 ("conventions", 1), ("evidence", 2), ("derivation", 2), ("conventions", 2),
                 ("derivation", 3), ("statement", 2)],
    }
    START = {"check": {}, "restate": {"library": 2}, "read": {"library": 3}}
    WHAT = {("open", 1): "open problems and notes (counts only)",
            ("evidence", 1): "evidence (docstrings, coverage text)",
            ("evidence", 2): "evidence (names and pass/fail only)",
            ("library", 1): "library docstrings",
            ("library", 2): "library signatures (names only)",
            ("library", 3): "library (module list only)",
            ("statement", 1): "technical statement beyond 1500 chars",
            ("statement", 2): "lay statement",
            ("conventions", 1): "macro definitions (names only)",
            ("conventions", 2): "macro list",
            ("derivation", 1): "premise formals beyond 600 chars, proofs beyond 4000",
            ("derivation", 2): "premise formal statements, proofs beyond 1500 chars",
            ("derivation", 3): "proof text (paths only)",
            ("example", 1): "example check text (path only)"}

    def render(self, e, mode, levels, only=None):
        out = {}
        for s in (only or self.ORDER):
            lv = levels.get(s, 0)
            if s == "header":
                out[s] = self.s_header(e, mode)
            elif s == "statement":
                out[s] = self.s_statement(e, lv)
            elif s == "derivation":
                out[s] = self.s_derivation(e, mode, lv)
            elif s == "quantities":
                out[s] = self.s_quantities(e)
            elif s == "conventions":
                out[s] = self.s_conventions(e, mode, lv)
            elif s == "library":
                out[s] = self.s_library(e, lv)
            elif s == "evidence":
                out[s] = self.s_evidence(e, lv)
            elif s == "example":
                out[s] = self.s_example(e, lv) if mode == "check" and e.kind != "note" else ""
            elif s == "open":
                out[s] = self.s_open(e, lv)
            elif s == "rules":
                out[s] = ("## Rules a check must satisfy\n\n" + CHECK_RULES
                          if mode == "check" and e.kind != "note" else "")
        return out

    @staticmethod
    def join(parts, cut_line):
        blocks = [parts["header"]] + ([cut_line] if cut_line else []) + \
                 [parts[s] for s in Context.ORDER[1:] if parts.get(s)]
        return "\n\n".join(blocks) + "\n"

    def bundle(self, eid: str, mode: str = "check", max_kb: float = 30):
        """-> (markdown, info) where info has bytes, cuts, per-section bytes, gravity, ms."""
        t0 = time.perf_counter()
        if mode not in MODES:
            raise ValueError(f"--for must be one of {', '.join(MODES)}")
        e = self.store.entities.get(eid)
        if e is None:
            repl = self.store.replaced_by.get(eid)
            raise KeyError(f"no entity {eid!r}" + (f"; it was retired and replaced by {repl!r}"
                                                   if repl else ""))
        budget = int(max_kb * 1024)
        levels = dict(self.START[mode])
        if e.kind == "note":            # nothing to check in a note: list the modules only
            levels["library"] = 3
        parts = self.render(e, mode, levels)
        cuts = []
        steps = [st for st in self.CUTS[mode] if levels.get(st[0], 0) < st[1]]
        reserve = 400       # room for the line saying what was cut
        text = self.join(parts, "")
        target = budget - reserve if _bytes(text) > budget else budget
        for sec, lv in steps:
            if _bytes(text) <= target:
                break
            if not parts.get(sec):
                continue
            levels[sec] = lv
            new = self.render_one(e, mode, sec, lv)
            if _bytes(new) < _bytes(parts[sec]):
                parts[sec] = new
                cuts.append(self.WHAT[(sec, lv)])
            text = self.join(parts, "")
        cut_line = ""
        if cuts:
            cut_line = (f"> Trimmed to fit {max_kb:g} KB; cut, least important first: "
                        + "; ".join(cuts) + ". Read the files named below for the full text.")
            text = self.join(parts, cut_line)
            if _bytes(text) > budget:
                text = self.join(parts, cut_line + f" Still {(_bytes(text) + 1023) // 1024} KB: "
                                 "the statement itself is long.")
        info = {"id": eid, "mode": mode, "bytes": _bytes(text), "cuts": cuts,
                "sections": {s: _bytes(parts[s]) for s in self.ORDER if parts.get(s)},
                "gravity": self.gravity_facing(e),
                "ms": round((time.perf_counter() - t0) * 1000, 1)}
        return text, info

    def render_one(self, e, mode, sec, lv):
        return self.render(e, mode, {sec: lv}, only=(sec,))[sec]

    # ---- what an agent would otherwise open ----------------------------------------
    def baseline_files(self, eid: str):
        """The files an agent opens without the bundle: the entity's folder (entity.md,
        proofs, check.py, coverage.yaml), each direct premise's entity.md, the example check,
        store/notation.yaml and the GTG dictionary."""
        e = self.store.entities[eid]
        files = [os.path.join(e.path, f) for f in sorted(os.listdir(e.path))
                 if os.path.isfile(os.path.join(e.path, f))]
        for d in e.derivations():
            if isinstance(d, dict):
                for ref in (d.get("uses") or []) + (d.get("assumes") or []):
                    p = parse_pin(ref)
                    x = self.store.entities.get(p[0]) if p else None
                    if x is not None:
                        files.append(os.path.join(x.path, model.ENTITY_FILE))
        ex = self.example_for(e)
        if ex:
            files.append(ex[1])
        files.append(os.path.join(self.root, "notation.yaml"))
        files.append(os.path.join(self.lab, "docs", "gtg-dictionary.md"))
        files = list(dict.fromkeys(f for f in files if os.path.exists(f)))
        return files, sum(os.path.getsize(f) for f in files)


# --------------------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------------------

def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "context":
        argv = argv[1:]
    ap = argparse.ArgumentParser(prog="tp context", description=__doc__.split("\n\n")[0])
    ap.add_argument("ids", nargs="+", help="entity id(s); several share one store load")
    ap.add_argument("--out", help="output file (one id) or directory (several ids); "
                                  "default stdout")
    ap.add_argument("--store", default="store")
    ap.add_argument("--max-kb", type=float, default=30)
    ap.add_argument("--for", dest="mode", choices=MODES, default="check")
    a = ap.parse_args(argv)
    ctx = Context(a.store)
    many = len(a.ids) > 1
    if many and a.out:
        os.makedirs(a.out, exist_ok=True)
    rc = 0
    for eid in a.ids:
        try:
            text, info = ctx.bundle(eid, a.mode, a.max_kb)
        except KeyError as exc:
            print(f"tp context: {exc.args[0]}", file=sys.stderr)
            rc = 2
            continue
        if a.out:
            path = os.path.join(a.out, f"{eid}.md") if many else a.out
            d = os.path.dirname(os.path.abspath(path))
            os.makedirs(d, exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
            print(f"wrote {path} ({info['bytes'] / 1024:.1f} KB, {info['ms']} ms"
                  + (f"; cut: {len(info['cuts'])} steps" if info["cuts"] else "") + ")",
                  file=sys.stderr)
        else:
            sys.stdout.write(text)
            if many:
                sys.stdout.write("\n---\n\n")
    return rc


if __name__ == "__main__":
    sys.exit(main())
