#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""Build the Zenodo deposit bundle of the Physics Graph.

  python3 tools/zenodo_bundle.py [--out DIR] [--date YYYY-MM-DD]

The bundle holds the claims (statements at four levels, proofs, exact checks, coverage
records), the other stored entities, and only the code the checks need: lib/ (GA.py and the
shared helpers), legacy/ (the papers' verify scripts that claims cite), and run_checks.py.
It leaves out the site, the site generator, generated documents, run records and tests.
Writes <out>/zero-divisors-store-<date>/ and <out>/zero-divisors-store-<date>.zip.
"""
import argparse
import datetime as dt
import glob
import hashlib
import os
import re
import shutil
import subprocess
import zipfile

import yaml

LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = shutil.ignore_patterns("__pycache__", "*.pyc", ".tp-cache", ".locks")

RUN_CHECKS = r'''#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""Run the exact checks of the store. Python 3.9 or later; PyYAML only for the few checks that
read a stored quantity (pip install pyyaml).

  python3 run_checks.py                  every claim's check.py, then every legacy verify script
  python3 run_checks.py <id> [<id> ...]  the checks of the named claims only
  python3 run_checks.py --jobs 4         run in parallel (default: number of CPUs)
  python3 run_checks.py --no-legacy      skip the papers' verify scripts
  python3 run_checks.py --legacy-only    run only the papers' verify scripts

A check function fails if it raises, returns False, or records a GA.check failure. Each
claim's checks run in their own Python process. A summary is printed and written to
check_results.txt beside this script; the exit status is 0 only if everything passed.
"""
import concurrent.futures as cf
import importlib.util
import os
import subprocess
import sys
import time
import traceback

ROOT = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(ROOT, "store")
# Part L of verify_T14c.py runs supplementary checkers that are not part of this deposit (and
# that no stored result cites); the store's evidence uses its tagged parts only.
LEGACY_ARGS = {"verify_T14c.py": ["--no-supplement"]}


def run_one(path):
    """Child mode: run every check_* function of one check.py; print PASS/FAIL lines."""
    sys.path.insert(0, os.path.join(ROOT, "lib"))
    import tp_premise
    import GA
    tp_premise.configure(STORE)
    sys.path.insert(0, os.path.dirname(path))
    spec = importlib.util.spec_from_file_location("check_under_test", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fails = 0
    for name in sorted(n for n in dir(mod) if n.startswith("check_") and callable(getattr(mod, n))):
        nfail = len(GA.FAILURES)
        try:
            r = getattr(mod, name)()
            if r is False or len(GA.FAILURES) > nfail:
                fails += 1
                print(f"FAIL {name}")
            else:
                print(f"PASS {name}")
        except Exception:
            fails += 1
            print(f"FAIL {name}")
            traceback.print_exc()
    return 1 if fails else 0


def _claims(ids):
    base = os.path.join(STORE, "claims")
    names = ids or sorted(os.listdir(base))
    out = []
    for n in names:
        p = os.path.join(base, n, "check.py")
        if os.path.exists(p):
            out.append((n, p))
        elif ids:
            print(f"no check.py for {n}")
    return out


def _run(cmd, cwd, timeout=1800):
    t = time.time()
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout + r.stderr, time.time() - t
    except subprocess.TimeoutExpired:
        return 2, "timed out", time.time() - t


def main():
    args = sys.argv[1:]
    if args[:1] == ["--one"]:
        sys.exit(run_one(args[1]))
    jobs = os.cpu_count() or 2
    legacy = True
    only_legacy = False
    ids = []
    while args:
        a = args.pop(0)
        if a == "--jobs":
            jobs = int(args.pop(0))
        elif a == "--no-legacy":
            legacy = False
        elif a == "--legacy-only":
            only_legacy = True
        else:
            ids.append(a)
    tasks = [] if only_legacy else [("claim", n, [sys.executable, os.path.abspath(__file__), "--one", p], ROOT)
                                    for n, p in _claims(ids)]
    if legacy and not ids:
        ldir = os.path.join(ROOT, "legacy")
        tasks += [("legacy", f, [sys.executable, f] + LEGACY_ARGS.get(f, []), ldir)
                  for f in sorted(os.listdir(ldir)) if f.startswith("verify_") and f.endswith(".py")]
    results = []
    with cf.ThreadPoolExecutor(max_workers=jobs) as ex:
        futs = {ex.submit(_run, cmd, cwd): (kind, name) for kind, name, cmd, cwd in tasks}
        for i, fut in enumerate(cf.as_completed(futs), 1):
            kind, name = futs[fut]
            code, out, secs = fut.result()
            nfun = sum(1 for l in out.splitlines() if l.startswith(("PASS check_", "FAIL check_")))
            results.append((kind, name, code, nfun, secs, out))
            mark = "ok  " if code == 0 else "FAIL"
            print(f"[{i}/{len(tasks)}] {mark} {kind:6} {name}  ({secs:.0f}s)", flush=True)
    bad = [r for r in results if r[2] != 0]
    nfun = sum(r[3] for r in results if r[0] == "claim")
    lines = [f"claims checked: {sum(1 for r in results if r[0] == 'claim')}",
             f"check functions run: {nfun}",
             f"legacy verify scripts run: {sum(1 for r in results if r[0] == 'legacy')}",
             f"failures: {len(bad)}"]
    lines += [f"FAILED {k} {n}:\n{o[-2000:]}" for k, n, c, _, _, o in sorted(bad)]
    summary = "\n".join(lines)
    print("\n" + summary)
    with open(os.path.join(ROOT, "check_results.txt"), "w", encoding="utf-8") as fh:
        fh.write(summary + "\n")
        for k, n, c, f, s, _ in sorted(results):
            fh.write(f"{'ok' if c == 0 else 'FAIL'}\t{k}\t{n}\t{f} functions\t{s:.1f}s\n")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
'''

LICENSE_CONTENT = """Creative Commons Attribution 4.0 International (CC BY 4.0)

Copyright (c) 2026 Leon Butler.

The statements, proofs, notes, open problems and other text and data in store/ are licensed
under CC BY 4.0: you may share and adapt them for any purpose, provided you give appropriate
credit, link to the licence and indicate if changes were made.
Full text: https://creativecommons.org/licenses/by/4.0/legalcode

The code (lib/, legacy/, run_checks.py and every check.py in store/) is licensed under the MIT
License; see LICENSE-CODE.txt.
"""


def _counts(store):
    st = {}
    for f in glob.glob(os.path.join(store, "claims", "*", "entity.md")):
        m = re.search(r"^status: (\S+)", open(f, encoding="utf-8").read(), re.M)
        st[m.group(1)] = st.get(m.group(1), 0) + 1
    n = lambda sub: len(glob.glob(os.path.join(store, sub, "*", "entity.md")))
    checks = glob.glob(os.path.join(store, "claims", "*", "check.py"))
    ops = yaml.safe_load(open(os.path.join(store, "open_problems.yaml"), encoding="utf-8"))
    ops = ops if isinstance(ops, list) else ops.get("problems", ops)
    nleg = sum(1 for f in glob.glob(os.path.join(store, "claims", "*", "entity.md"))
               if "kind: legacy" in open(f, encoding="utf-8").read())
    return st, n("objects"), n("predictions"), n("quantities"), len(checks), len(ops), nleg


def _papers():
    d = yaml.safe_load(open(os.path.join(LAB, "deposits", "deposits.yaml"), encoding="utf-8"))
    return sorted((k, v.get("doi"), v.get("version")) for k, v in d.items() if v.get("doi"))


def _readme(date, commit, counts, papers, disclaimer):
    st, nobj, npred, nq, nchk, nops, nleg = counts
    total = sum(st.values())
    status = ", ".join(f"{v} {k}" for k, v in sorted(st.items(), key=lambda x: -x[1]))
    rows = "\n".join(f"| {k} | {v} | https://doi.org/{d} |" for k, d, v in papers)
    return f"""# Zero Divisors: Physics Graph ({date})

A snapshot of the claim store behind the Transport Papers series (T0 to T17, T14a to T14c and
the companion notes) and the research that has continued from it. Every result is stored as
its own entity: a statement at four levels, its proof, the results it rests on, and an exact
check that anyone can run with plain Python.

Snapshot of {date}, store commit `{commit}`: {total} results ({status}), {nobj} definitions
and objects, {npred} predictions, {nq} quantities, {nops} open problems, and {nchk} check
scripts. The deposited papers are the official versions of the series; this store records
how their results have been corrected, restated and extended since.

## Running the checks

    python3 run_checks.py                  # everything (about an hour on two cores)
    python3 run_checks.py <claim id>       # one result, e.g.
    python3 run_checks.py synthesis.hadamard-scaling-limit-premise

Python 3.9 or later. PyYAML (`pip install pyyaml`) is needed only by the few checks that read
a stored quantity. All arithmetic is exact (Fractions, Gaussian rationals, the Clifford algebra
of `lib/GA.py`); no floating point is used as evidence. The run writes `check_results.txt`.

## Layout

- `store/claims/<id>/entity.md`: one result. YAML front matter (status, version, subject,
  tags, derivations with the premises it `uses` and the postulates it `assumes`, each pinned
  to a version; checks; provenance; review notes), then four levels: `formal` (the statement),
  `technical`, `lay` and `one-liner`.
- `store/claims/<id>/proof-*.tex`: the proof of each derivation (LaTeX; `\\claimref{{id}}` cites
  another result).
- `store/claims/<id>/check.py`: the exact check. Each `check_*` function must pass;
  `premise(id)` records which stored results it builds on. `coverage.yaml` says what part of
  the statement each check covers (exact, complete, sampled or partial) and what it omits.
- `store/objects/`, `store/predictions/`, `store/quantities/`, `store/questions/`: definitions,
  registered predictions with their kill conditions, measured quantities with sources, and
  questions.
- `store/open_problems.yaml` (and `open_problems_settled.yaml`): the open problems, what is
  known and the lines of attack.
- `store/notes/`: remarks and examples attached to results. `store/conventions.md`,
  `notation.yaml`, `references.yaml`, `subjects.yaml`, `tags.yaml`, `tombstones.yaml` (retired
  ids and what replaced them).
- `lib/`: `GA.py` (exact Clifford algebra) and the shared helpers the checks import.
- `legacy/`: the papers' own verify scripts, which {nleg} results cite as evidence (by their
  tagged checks). `verify_T14c.py` is run with `--no-supplement`: its Part L calls supplementary
  checkers that are not part of this deposit and that no stored result cites.

## Statuses

`proved` (proved in the store, with a proof and a check), `imported` (a published result,
cited with provenance and what was checked against the source), `postulate` (a premise the
programme adopts; each states what it is for and how it would be refuted), `conjectured`, and
`refuted` (kept, with the refutation). Every result also records its review trail; much of the
store was produced with AI assistance and refereed by independent AI reviewers before the
author accepted it, and the front matter says so per result.

## The deposited papers

| Paper | Version | DOI |
|---|---|---|
{rows}

## Authorship

{disclaimer}

## Licence

Text and data: CC BY 4.0 (LICENSE-CONTENT.txt). Code: MIT (LICENSE-CODE.txt).
"""


def _citation(date, commit):
    return f"""cff-version: 1.2.0
message: "If you use this store, please cite it as below."
title: "Zero Divisors: Physics Graph"
type: dataset
authors:
  - family-names: Butler
    given-names: Leon
date-released: {date}
version: "{date}"
license: CC-BY-4.0
abstract: >-
  The claim store behind the Transport Papers series: every result as a separate entity with
  a statement at four levels, a proof, its premises and an exact, runnable check. Snapshot of
  {date} (store commit {commit}).
keywords:
  - geometric algebra
  - Clifford algebra
  - gauge theory gravity
  - quantum field theory
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(LAB, "build", "zenodo"))
    ap.add_argument("--date", default=dt.date.today().isoformat())
    a = ap.parse_args()
    name = f"zero-divisors-store-{a.date}"
    root = os.path.join(a.out, name)
    if os.path.exists(root):
        shutil.rmtree(root)
    os.makedirs(root)
    shutil.copytree(os.path.join(LAB, "store"), os.path.join(root, "store"), ignore=SKIP)
    shutil.copytree(os.path.join(LAB, "lib"), os.path.join(root, "lib"), ignore=SKIP)
    shutil.copytree(os.path.join(LAB, "legacy"), os.path.join(root, "legacy"), ignore=SKIP)
    with open(os.path.join(root, "run_checks.py"), "w", encoding="utf-8") as fh:
        fh.write(RUN_CHECKS)
    shutil.copy(os.path.join(LAB, "LICENSE-CODE.txt"), root)
    with open(os.path.join(root, "LICENSE-CONTENT.txt"), "w", encoding="utf-8") as fh:
        fh.write(LICENSE_CONTENT)
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=LAB,
                            capture_output=True, text=True).stdout.strip()
    cfg = yaml.safe_load(open(os.path.join(LAB, "store", "config.yaml"), encoding="utf-8"))
    disc = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", (cfg.get("house_style") or {}).get("disclaimer", ""))
    with open(os.path.join(root, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(_readme(a.date, commit, _counts(os.path.join(root, "store")), _papers(), disc))
    with open(os.path.join(root, "CITATION.cff"), "w", encoding="utf-8") as fh:
        fh.write(_citation(a.date, commit))
    files = sorted(os.path.relpath(os.path.join(d, f), root)
                   for d, _, fs in os.walk(root) for f in fs)
    with open(os.path.join(root, "MANIFEST.sha256"), "w", encoding="utf-8") as fh:
        for f in files:
            h = hashlib.sha256(open(os.path.join(root, f), "rb").read()).hexdigest()
            fh.write(f"{h}  {f}\n")
    zp = root + ".zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files + ["MANIFEST.sha256"]:
            z.write(os.path.join(root, f), os.path.join(name, f))
    print(f"{zp}  ({os.path.getsize(zp) / 1e6:.1f} MB, {len(files) + 1} files)")


if __name__ == "__main__":
    main()
