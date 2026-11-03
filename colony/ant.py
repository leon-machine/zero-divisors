#!/usr/bin/env python3
"""Run folders and the outcome ledger for open-problem runs.

The file keeps its old name because the research-run skill calls it; the ant-colony exploration it
once held (random walks, pheromone, scout rounds, the colony-versus-control split) was dropped on
2026-10-22 (POLICIES.md section 0) and removed.

Runs live in <lab>/colony/runs/<run>/; the lab is this folder's parent (override with TP_LAB).
<run> is TP_COLONY_RUN, or the newest run folder.

Commands
  init NAME            make runs/NAME/ with findings/, work/ and verify/
  ledger add --problem op.x --tokens N --outcome O [--proposal ID] [--verdict V]
                       O: settled | proved-partial | negative | findings | none
                       V: the referee verdict, sound | fixes | overstated | wrong | -
  ledger summary       problems, tokens, outcome score (per 100k tokens), proposals filed and how
                       they fared with the referees
"""
import argparse
import fcntl
import json
import os
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "runs")
OUTCOME_SCORE = {"settled": 3, "proved-partial": 2, "negative": 2, "findings": 1, "none": 0}


def run_dir():
    name = os.environ.get("TP_COLONY_RUN")
    if not name:
        runs = sorted((d for d in os.listdir(RUNS) if os.path.isdir(os.path.join(RUNS, d))),
                      key=lambda d: os.path.getmtime(os.path.join(RUNS, d))) if os.path.isdir(RUNS) else []
        if not runs:
            sys.exit("no run yet: ant.py init <name>")
        name = runs[-1]
    d = os.path.join(RUNS, name)
    if not os.path.isdir(d):
        sys.exit(f"no run {name}")
    return d


def cmd_init(a):
    d = os.path.join(RUNS, a.name)
    for sub in ("findings", "work", "verify"):
        os.makedirs(os.path.join(d, sub), exist_ok=True)
    print(f"run {a.name} at {d}; export TP_COLONY_RUN={a.name} to pin it")


def verdict_word(v):
    v = (v or "").lower()
    return ("fixes" if "fixes" in v else "sound" if v.startswith("sound") else
            "overstated" if "overstated" in v else "wrong" if "wrong" in v else v)


def cmd_ledger(a):
    p = os.path.join(run_dir(), "ledger.jsonl")
    if a.action == "add":
        if not a.problem or a.outcome not in OUTCOME_SCORE:
            sys.exit("ledger add needs --problem and --outcome " + "|".join(OUTCOME_SCORE))
        with open(p, "a", encoding="utf-8") as fh:
            fcntl.flock(fh, fcntl.LOCK_EX)
            fh.write(json.dumps({"t": time.time(), "problem": a.problem, "tokens": a.tokens,
                                 "outcome": a.outcome, "proposal": a.proposal, "verdict": a.verdict}) + "\n")
        print("logged")
        return
    rows = [json.loads(line) for line in open(p, encoding="utf-8")] if os.path.exists(p) else []
    if not rows:
        print("no entries")
        return
    tok = sum(r.get("tokens") or 0 for r in rows)
    score = sum(OUTCOME_SCORE.get(r.get("outcome"), 0) for r in rows)
    verdicts = Counter(verdict_word(r.get("verdict")) for r in rows if r.get("proposal"))
    print(f"{len({r['problem'] for r in rows})} problems, {tok:,} tokens, outcome score {score} "
          f"({100000 * score / max(tok, 1):.2f} per 100k), proposals {sum(1 for r in rows if r.get('proposal'))}, "
          f"survived referee {verdicts['sound'] + verdicts['fixes']}, "
          f"overstated or wrong {verdicts['overstated'] + verdicts['wrong']}")
    print("   outcomes:", dict(Counter(r.get("outcome") for r in rows)))


def main():
    p = argparse.ArgumentParser(prog="ant.py", description=__doc__.split("\n\n")[0])
    s = p.add_subparsers(dest="cmd", required=True)
    x = s.add_parser("init"); x.add_argument("name")
    lg = s.add_parser("ledger"); lg.add_argument("action", choices=["add", "summary"])
    lg.add_argument("--problem"); lg.add_argument("--tokens", type=int, default=0)
    lg.add_argument("--outcome"); lg.add_argument("--proposal", default="")
    lg.add_argument("--verdict", default="")
    lg.add_argument("--arm", help=argparse.SUPPRESS)      # accepted from older instructions; ignored
    a = p.parse_args()
    {"init": cmd_init, "ledger": cmd_ledger}[a.cmd](a)


if __name__ == "__main__":
    main()
