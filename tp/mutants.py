"""tp mutants: the mutation half of layer 4 for one entity, with the surviving literals shown.

  tp mutants <id | folder> [...] [--func NAME] [--every] [--store store] [--json]

For each wired check function it perturbs integer literals exactly as `tp check` does (the
k-th integer literal inside the function becomes n + 1; the same eight evenly spaced
literals when there are more than eight) and reruns the function, sandboxed. It prints each
surviving literal with its line, so the author can tell a sample input (a survivor that is
harmless: the identity holds at the next sample too) from an asserted value or a count
that the check does not pin down.

--every perturbs every literal, not the eight the full check samples; the verdict is always
the full check's, over the sampled literals. Each killed mutant records whether an assert
caught it or an exception (a mutant killed only by an exception may hide a weak assert).
The unmutated function runs first; if it fails the verdict is E406 and no mutants run.
Verdicts follow the full check: E408 when every perturbation survives, W413 when more than
half survive. Exit status 1 when any function gets E406, E408 or W413.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import sys

from . import evidence
from .lint import find_folder, store_context
from .model import load_entity


class _Locator(ast.NodeVisitor):
    """Positions of the integer literals inside one function, in the mutator's order."""

    def __init__(self, func):
        self.func, self.inside, self.found = func, False, []

    def visit_FunctionDef(self, node):
        if node.name != self.func:
            return
        self.inside = True
        self.generic_visit(node)
        self.inside = False

    def visit_Constant(self, node):
        if self.inside and isinstance(node.value, int) and not isinstance(node.value, bool):
            self.found.append((node.lineno, node.col_offset, node.value))


def literals(source: str, func: str) -> list[tuple[int, int, int]]:
    loc = _Locator(func)
    loc.visit(ast.parse(source))
    return loc.found


def sampled(n: int) -> list[int]:
    """The literal indices the full check perturbs (validate._run_new_check)."""
    return sorted({round(i * (n - 1) / 7) for i in range(8)}) if n > 8 else list(range(n))


def wired_functions(e) -> list[tuple[str, str]]:
    out = []
    for ev in e.meta.get("checked_by") or []:
        if isinstance(ev, dict) and ev.get("kind") == "check" and "::" in str(ev.get("ref", "")):
            fname, func = str(ev["ref"]).split("::", 1)
            out.append((fname, func))
    return out


def run_entity(root: str, folder: str, only=None, every=False, timeout=60) -> dict:
    e = load_entity(folder)
    res = {"id": e.id, "functions": []}
    for fname, func in wired_functions(e):
        if only and func not in only:
            continue
        path = os.path.join(folder, fname)
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        lines = src.splitlines()
        base = evidence.run_check(root, folder, src, func, timeout=timeout)
        if not base["ok"]:
            res["functions"].append({"file": fname, "func": func, "literals": 0, "tried": 0,
                                     "survived": 0, "verdict": "E406", "rows": [],
                                     "error": str(base.get("error"))[:300]})
            continue
        lits = literals(src, func)
        in_sample = set(sampled(len(lits)))
        ks = list(range(len(lits))) if every else sorted(in_sample)
        rows = []
        for k in ks:
            mut = evidence.mutate(src, func, k)
            if mut is None:
                continue
            r = evidence.run_check(root, folder, mut, func, timeout=timeout)
            ln, col, val = lits[k]
            err = str(r.get("error") or "")
            killed_by = (None if r["ok"] else "assert" if err.startswith("assertion failed")
                         or "AssertionError" in err or "returned False" in err
                         else "exception: " + err[:80])
            rows.append({"k": k, "line": ln, "col": col, "value": val, "survived": bool(r["ok"]),
                         "sampled": k in in_sample, "killed_by": killed_by,
                         "text": lines[ln - 1].strip() if 0 < ln <= len(lines) else ""})
        # the verdict is the full check's: over the sampled literals only
        srows = [r for r in rows if r["sampled"]]
        surv = sum(r["survived"] for r in srows)
        verdict = ("W408" if not lits else "E408" if srows and surv == len(srows)
                   else "W413" if surv * 2 > len(srows) else "ok")
        res["functions"].append({"file": fname, "func": func, "literals": len(lits),
                                 "tried": len(srows), "survived": surv, "verdict": verdict,
                                 "every_tried": len(rows),
                                 "every_survived": sum(r["survived"] for r in rows),
                                 "killed_by_exception": sum(1 for r in rows if r["killed_by"]
                                                            and r["killed_by"] != "assert"),
                                 "rows": rows})
    return res


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="tp mutants", description=__doc__.split("\n\n")[0])
    ap.add_argument("targets", nargs="+", help="entity ids or folders")
    ap.add_argument("--store", default="store")
    ap.add_argument("--func", action="append", help="only this check function (repeatable)")
    ap.add_argument("--every", action="store_true", help="perturb every literal")
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv[1:])
    ctx = store_context(a.store)
    bad = 0
    out = []
    for t in a.targets:
        folder = t if os.path.isdir(t) else find_folder(ctx.root, t)
        if not folder:
            print(f"tp mutants: no entity {t}", file=sys.stderr)
            bad += 1
            continue
        res = run_entity(ctx.root, folder, a.func, a.every, a.timeout)
        out.append(res)
        for f in res["functions"]:
            bad += f["verdict"] in ("E406", "E408", "W413")
    if a.json:
        json.dump(out, sys.stdout, indent=1)
        print()
    else:
        for res in out:
            print(res["id"])
            for f in res["functions"]:
                if f["verdict"] == "E406":
                    print(f"  {f['func']}: E406 the unmutated function fails: {f['error']}")
                    continue
                extra = ""
                if f["every_tried"] != f["tried"]:
                    extra = f"; every literal: {f['every_survived']} of {f['every_tried']}"
                if f["killed_by_exception"]:
                    extra += f"; {f['killed_by_exception']} killed by an exception, not an assert"
                print(f"  {f['func']}: {f['survived']} of {f['tried']} sampled perturbations survive"
                      f" ({f['literals']} literals{extra}) {f['verdict']}")
                for r in f["rows"]:
                    if r["survived"]:
                        mark = "*" if r["sampled"] else " "
                        print(f"   {mark}survives  line {r['line']} col {r['col']}: {r['value']} -> "
                              f"{r['value'] + 1}   {r['text'][:100]}")
                if any(r["survived"] for r in f["rows"]) and f["every_tried"] != f["tried"]:
                    print("    (* = a literal the full check perturbs)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(["mutants"] + sys.argv[1:]))
