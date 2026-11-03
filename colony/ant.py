#!/usr/bin/env python3
"""The ant colony over the Transport Lab claim graph (v2).

Lives in <lab>/colony/. The lab is the parent folder (override with TP_LAB); the run's
state (pheromones, food, rounds, arms, ledger) lives in <lab>/colony/runs/<run>/, where
<run> is TP_COLONY_RUN or the newest run folder ('ant.py init <name>' makes one).

The graph
  every store entity except notes is a node (notes are prose settings, not results). Edges:
  - 'uses'   : the store's derivation links, walked both ways;
  - 'near'   : nearest neighbours in the universe layout;
  - 'echo'   : cross-subject look-alikes, TF-IDF over TITLE + FORMAL STATEMENT ONLY;
  - 'bridge' : any link an ant has marked between nodes the graph does not connect.

Three pheromones, one file (runs/<run>/pheromones.jsonl)
  - interesting (kind i): "worth reading together". Evaporates fast (keeps 60% per round).
  - verified    (kind v): the link carried a result that passed a check or a referee.
                 Needs --evidence (a proposal id, check path or referee report). Keeps 95%.
  - dead        (kind d): "followed this, it leads nowhere", with the reason. Keeps 85%.
  A walk steps with probability  base * (1 + tau_i + 3 tau_v)^1.5 * exp(-tau_d).

Commands
  init NAME                      start a run folder (round 0)
  walk START [--steps 10] [--explore 1] [--problem op.x] [--seed N]
                                 START is an entity id or an open-problem id
  lay A B W --kind i|v|d --ant NAME [--problem op.x,op.y] --why TEXT [--evidence REF]
  food --ant NAME --problem op.x --strength 1-5 --nodes a,b,c --text TEXT
  trails [--problem op.x] [--kind i|v|d] [--top 25]
  larder [--problem op.x]
  show ID | echo ID [--k 10] | near "free text" [--k 12]
  round [--bump]                 current round; --bump starts the next one (evaporation is by round)
  split [--seed 2026] [--include-housekeeping]
                                 assign the open problems to arms 'colony' and 'control',
                                 stratified by area and difficulty; writes arms.json
  ledger add --arm colony|control --problem op.x --tokens N --outcome O [--proposal id]
             [--verdict V]       O: settled|proved-partial|negative|findings|none;
                                 V: the referee verdict (sound|fixes|overstated|wrong|-)
  ledger summary                 outcome and referee yield per arm, per 100k tokens
"""
import argparse
import fcntl
import json
import math
import os
import pickle
import random
import re
import sys
import time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
LAB = os.environ.get("TP_LAB") or os.path.dirname(HERE)
GRAPH = os.path.join(LAB, "build", "graph.json")
LAYOUT = os.path.join(LAB, "build", "layout.json")
OPS = os.path.join(LAB, "store", "open_problems.yaml")
RUNS = os.path.join(HERE, "runs")

KEEP = {"i": 0.6, "v": 0.95, "d": 0.85}     # survival per round
ALPHA = 1.5
BASE = {"uses": 1.0, "near": 0.5, "echo": 0.8, "bridge": 1.2}
TOK = re.compile(r"[a-z][a-z0-9]{2,}")
STOP = set("the and for that with this from are its not which one two has have but all any per each into "
           "only than then them they their there where when what was were been being also under over "
           "such can will may must between both same other given gives give does done order case cases "
           "result results paper series section holds hold show shows shown let where".split())


def run_dir(create=False):
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


def path(n):
    return os.path.join(run_dir(), n)


def cur_round():
    try:
        return int(open(path("round.txt")).read().strip())
    except Exception:
        return 0


def build():
    cache = os.path.join(HERE, ".graph_cache_v2.pkl")
    if os.path.exists(cache) and os.path.getmtime(cache) > os.path.getmtime(GRAPH):
        return pickle.load(open(cache, "rb"))
    g = json.load(open(GRAPH))
    nodes = {n["id"]: n for n in g["nodes"] if n.get("kind") != "note"}
    adj = defaultdict(dict)
    for e in g["edges"]:
        a, b = e["src"], e["dst"]
        if a in nodes and b in nodes and a != b:
            adj[a][b] = "uses"
            adj[b][a] = "uses"
    pos = json.load(open(LAYOUT)).get("positions", {}) if os.path.exists(LAYOUT) else {}
    ids = [i for i in nodes if i in pos]
    for i in ids:
        for _, j in sorted((math.dist(pos[i], pos[j]), j) for j in ids if j != i)[:5]:
            adj[i].setdefault(j, "near")
            adj[j].setdefault(i, "near")
    # echo: title + formal statement only
    docs = {}
    for i, n in nodes.items():
        f = n.get("formal") or ""
        if f.strip() in ("", "pending"):
            f = n.get("technical") or ""
        docs[i] = Counter(t for t in TOK.findall(((n.get("title") or "") + " " + f).lower()) if t not in STOP)
    df = Counter(t for c in docs.values() for t in c)
    N = len(docs)
    vec = {}
    for i, c in docs.items():
        v = {t: (1 + math.log(k)) * math.log(N / df[t]) for t, k in c.items() if 1 < df[t] < N * 0.2}
        nrm = math.sqrt(sum(x * x for x in v.values())) or 1
        vec[i] = {t: x / nrm for t, x in v.items()}
    inv = defaultdict(list)
    for i, v in vec.items():
        for t, x in v.items():
            inv[t].append((i, x))
    echoes = {}
    for i, v in vec.items():
        acc = Counter()
        for t, x in v.items():
            if len(inv[t]) > 150:
                continue
            for j, y in inv[t]:
                if j != i:
                    acc[j] += x * y
        si = nodes[i].get("subject")
        if i.endswith("-external"):      # provenance stubs (textbook pointers) echo each other's boilerplate
            echoes[i] = []
            continue
        cand = [(s, j) for j, s in acc.most_common(60) if nodes[j].get("subject") != si and j not in adj[i]
                and not j.endswith("-external")]
        echoes[i] = cand[:8]
        for s, j in cand[:3]:
            if s > 0.15:
                adj[i].setdefault(j, "echo")
                adj[j].setdefault(i, "echo")
    data = {"nodes": nodes, "adj": dict(adj), "inv": dict(inv), "echoes": echoes}
    pickle.dump(data, open(cache, "wb"))
    return data


def load_ops():
    """The store's open problems plus any run-level targets (runs/<run>/targets_extra.yaml)."""
    import yaml
    ops = {o["id"]: o for o in (yaml.safe_load(open(OPS)) or [])} if os.path.exists(OPS) else {}
    try:
        extra = os.path.join(run_dir(), "targets_extra.yaml")
        if os.path.exists(extra):
            ops.update({o["id"]: o for o in (yaml.safe_load(open(extra)) or [])})
    except SystemExit:
        pass
    return ops


def pheromone(problem=None):
    """tau[kind][(a,b)] with evaporation; rows without 'kind' count as interesting."""
    tau = {"i": defaultdict(float), "v": defaultdict(float), "d": defaultdict(float)}
    rnow = cur_round()
    rows = []
    p = path("pheromones.jsonl")
    if os.path.exists(p):
        for line in open(p):
            try:
                r = json.loads(line)
            except Exception:
                continue
            rows.append(r)
            if problem and problem not in (r.get("problems") or []):
                continue
            k = r.get("kind", "i")
            key = tuple(sorted((r["a"], r["b"])))
            tau[k][key] += abs(float(r["w"])) * KEEP[k] ** max(0, rnow - int(r.get("round", 0)))
    return tau, rows


def append(p, obj):
    with open(p, "a") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")
        fcntl.flock(f, fcntl.LOCK_UN)


def short(n, w=150):
    s = (n.get("one_liner") or n.get("title") or "").replace("\n", " ")
    return s if len(s) <= w else s[:w] + "..."


def cmd_init(a, G):
    d = os.path.join(RUNS, a.name)
    os.makedirs(os.path.join(d, "findings"), exist_ok=True)
    os.makedirs(os.path.join(d, "work"), exist_ok=True)
    os.makedirs(os.path.join(d, "verify"), exist_ok=True)
    if not os.path.exists(os.path.join(d, "round.txt")):
        open(os.path.join(d, "round.txt"), "w").write("0")
    print(f"run {a.name} at {d}; export TP_COLONY_RUN={a.name} to pin it")


def cmd_walk(a, G):
    nodes, adj = G["nodes"], G["adj"]
    rng = random.Random(a.seed if a.seed is not None else time.time_ns())
    start, ops = a.start, load_ops()
    if start in ops:
        ents = [e for e in ops[start].get("entities") or [] if e in nodes]
        if not ents:
            sys.exit(f"{start} has no non-note entities in the graph")
        a.problem = a.problem or start
        start = rng.choice(ents)
    if start not in nodes:
        sys.exit(f"no node {start} (notes are not nodes; use labcli.py get_claim to read them)")
    tau, _ = pheromone(a.problem)
    for k in tau:
        for (x, y) in tau[k]:
            if x in nodes and y in nodes:
                adj.setdefault(x, {}).setdefault(y, "bridge")
                adj.setdefault(y, {}).setdefault(x, "bridge")
    path_, seen, cur = [start], {start}, start
    for _ in range(a.steps):
        cand = [(b, k) for b, k in adj.get(cur, {}).items() if b not in seen]
        if not cand:
            break
        ws = []
        for b, k in cand:
            key = tuple(sorted((cur, b)))
            w = BASE[k] * (1 + tau["i"].get(key, 0) + 3 * tau["v"].get(key, 0)) ** ALPHA
            w *= math.exp(-tau["d"].get(key, 0))
            if nodes[b].get("subject") != nodes[cur].get("subject"):
                w *= 1.3
            ws.append(w ** (1.0 / max(a.explore, 0.05)))
        r = rng.random() * sum(ws)
        for (b, k), w in zip(cand, ws):
            r -= w
            if r <= 0:
                break
        path_.append((k, b))
        seen.add(b)
        cur = b
    n0 = nodes[path_[0]]
    print(f"START {path_[0]}  [{n0.get('subject')} | {n0.get('status')}]\n    {short(n0)}")
    prev = path_[0]
    for k, b in path_[1:]:
        key = tuple(sorted((prev, b)))
        tags = "".join(f" {x}={tau[x][key]:.1f}" for x in "ivd" if tau[x].get(key))
        n = nodes[b]
        print(f" --{k}{tags}--> {b}  [{n.get('subject')} | {n.get('status')}]\n    {short(n)}")
        prev = b


def cmd_lay(a, G):
    for x in (a.a, a.b):
        if x not in G["nodes"]:
            sys.exit(f"no node {x} (anchor problem-level marks on one of the problem's entities)")
    if a.kind == "v" and not a.evidence:
        sys.exit("verified pheromone needs --evidence (proposal id, check path or referee report)")
    if a.kind == "d" and not a.why:
        sys.exit("dead-end pheromone needs --why (what was tried and why it fails)")
    append(path("pheromones.jsonl"), {
        "t": time.time(), "round": cur_round(), "ant": a.ant, "kind": a.kind, "a": a.a, "b": a.b,
        "w": max(0.0, min(5.0, a.w)), "problems": [p for p in (a.problem or "").split(",") if p],
        "why": a.why, "evidence": a.evidence})
    label = {"i": "interesting", "v": "verified", "d": "dead end"}[a.kind]
    print(f"laid {label} {a.w} on {a.a} -- {a.b} ({G['adj'].get(a.a, {}).get(a.b, 'new bridge')})")


def cmd_food(a, G):
    nodes = [x for x in (a.nodes or "").split(",") if x]
    append(path("food.jsonl"), {"t": time.time(), "round": cur_round(), "ant": a.ant, "problem": a.problem,
                                "strength": a.strength, "nodes": nodes, "text": a.text})
    for x, y in zip(nodes, nodes[1:]):
        if x in G["nodes"] and y in G["nodes"]:
            append(path("pheromones.jsonl"), {
                "t": time.time(), "round": cur_round(), "ant": a.ant, "kind": "i", "a": x, "b": y,
                "w": a.strength * 0.5, "problems": [a.problem] if a.problem else [],
                "why": "food trail: " + a.text[:80], "evidence": ""})
    print("food recorded")


def cmd_trails(a, G):
    tau, rows = pheromone(a.problem)
    nodes = G["nodes"]
    why = defaultdict(list)
    for r in rows:
        if a.problem and a.problem not in (r.get("problems") or []):
            continue
        why[(r.get("kind", "i"), tuple(sorted((r["a"], r["b"]))))].append(f"{r['ant']}: {r.get('why', '')[:110]}")
    kinds = a.kind or "vid"
    print(f"round {cur_round()}" + (f", problem {a.problem}" if a.problem else ""))
    for k in kinds:
        label = {"i": "INTERESTING", "v": "VERIFIED", "d": "DEAD ENDS"}[k]
        items = sorted(tau[k].items(), key=lambda kv: -kv[1])[:a.top]
        print(f"\n== {label} ({len(tau[k])} links)")
        for (x, y), t in items:
            print(f"{t:5.1f}  {x} [{nodes.get(x, {}).get('subject')}] -- {y} [{nodes.get(y, {}).get('subject')}]")
            for w in why[(k, (x, y))][-2:]:
                print(f"         {w}")


def cmd_larder(a, G):
    p = path("food.jsonl")
    rows = [json.loads(l) for l in open(p) if l.strip()] if os.path.exists(p) else []
    if a.problem:
        rows = [r for r in rows if r.get("problem") == a.problem]
    for r in sorted(rows, key=lambda r: -r["strength"]):
        print(f"[{r['strength']}] {r['problem']} ({r['ant']}, round {r['round']}): {r['text']}\n      nodes: {', '.join(r['nodes'])}")


def cmd_show(a, G):
    n = G["nodes"].get(a.id)
    if not n:
        sys.exit(f"no node {a.id}")
    adj = G["adj"].get(a.id, {})
    print(f"{a.id}  [{n.get('subject')} | {n.get('kind')} | {n.get('status')} | effective {n.get('effective')} | check {n.get('check')}]")
    print("title:", n.get("title"))
    print("one-liner:", n.get("one_liner"))
    f = n.get("formal") or ""
    print("formal:", f[:1500] + ("..." if len(f) > 1500 else ""))
    for key in ("conditional_on", "kill_condition"):
        if n.get(key):
            print(f"{key}:", n[key])
    for k in ("uses", "near", "echo"):
        xs = [b for b, kk in adj.items() if kk == k]
        if xs:
            print(f"{k}: " + ", ".join(xs[:25]))
    print("cross-subject echoes:", ", ".join(f"{j}({s:.2f})" for s, j in G["echoes"].get(a.id, [])[:6]))


def cmd_echo(a, G):
    for s, j in G["echoes"].get(a.id, [])[:a.k]:
        n = G["nodes"][j]
        print(f"{s:.2f}  {j} [{n.get('subject')} | {n.get('status')}]\n      {short(n)}")


def cmd_near(a, G):
    q = Counter(t for t in TOK.findall(a.text.lower()) if t not in STOP)
    acc = Counter()
    for t in q:
        for j, y in G["inv"].get(t, []):
            acc[j] += y
    for j, s in acc.most_common(a.k):
        n = G["nodes"][j]
        print(f"{s:.2f}  {j} [{n.get('subject')} | {n.get('status')}]\n      {short(n)}")


def cmd_round(a, G):
    if a.bump:
        nxt = cur_round() + 1          # read before opening for write (which truncates)
        open(path("round.txt"), "w").write(str(nxt))
    print(cur_round())


def cmd_split(a, G):
    ops = load_ops()
    rng = random.Random(a.seed)
    strata = defaultdict(list)
    for o in ops.values():
        if o.get("status") == "settled":
            continue
        if o.get("kind") == "housekeeping" and not a.include_housekeeping:
            continue
        strata[(o.get("area"), o.get("difficulty"))].append(o["id"])
    arms = {"colony": [], "control": []}
    flip = rng.random() < 0.5
    for key in sorted(strata, key=str):
        ids = sorted(strata[key])
        rng.shuffle(ids)
        for k, pid in enumerate(ids):
            arm = "colony" if (k % 2 == 0) != flip else "control"
            arms[arm].append(pid)
            flip = not flip if k == len(ids) - 1 else flip
    out = {"seed": a.seed, "made": time.strftime("%Y-%m-%d"), **arms}
    json.dump(out, open(path("arms.json"), "w"), indent=1)
    print(f"colony {len(arms['colony'])}, control {len(arms['control'])} -> {path('arms.json')}")
    for k in ("colony", "control"):
        print(f"{k}: " + ", ".join(arms[k]))


OUTCOME_SCORE = {"settled": 3, "proved-partial": 2, "negative": 2, "findings": 1, "none": 0}


def cmd_ledger(a, G):
    p = path("ledger.jsonl")
    if a.action == "add":
        if a.arm not in ("colony", "control") or a.outcome not in OUTCOME_SCORE:
            sys.exit("--arm colony|control and --outcome settled|proved-partial|negative|findings|none")
        append(p, {"t": time.time(), "arm": a.arm, "problem": a.problem, "tokens": a.tokens,
                   "outcome": a.outcome, "proposal": a.proposal, "verdict": a.verdict})
        print("logged")
        return
    rows = [json.loads(l) for l in open(p)] if os.path.exists(p) else []
    for arm in ("colony", "control"):
        rs = [r for r in rows if r["arm"] == arm]
        if not rs:
            print(f"{arm}: no entries")
            continue
        tok = sum(r["tokens"] or 0 for r in rs)
        score = sum(OUTCOME_SCORE[r["outcome"]] for r in rs)
        def vnorm(v):
            v = (v or "").lower()
            return ("fixes" if "fixes" in v else "sound" if v.startswith("sound") else
                    "overstated" if "overstated" in v else "wrong" if "wrong" in v else v)
        survived = sum(1 for r in rs if vnorm(r.get("verdict")) in ("sound", "fixes"))
        filed = sum(1 for r in rs if r.get("proposal"))
        bad = sum(1 for r in rs if vnorm(r.get("verdict")) in ("overstated", "wrong"))
        print(f"{arm}: {len({r['problem'] for r in rs})} problems, {tok:,} tokens, outcome score {score} "
              f"({100000 * score / max(tok, 1):.2f} per 100k), proposals {filed}, "
              f"survived referee {survived}, overstated/wrong {bad}")
        print("   outcomes:", dict(Counter(r["outcome"] for r in rs)))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="cmd", required=True)
    x = s.add_parser("init"); x.add_argument("name")
    w = s.add_parser("walk"); w.add_argument("start"); w.add_argument("--steps", type=int, default=10)
    w.add_argument("--seed", type=int); w.add_argument("--explore", type=float, default=1.0); w.add_argument("--problem")
    l = s.add_parser("lay"); l.add_argument("a"); l.add_argument("b"); l.add_argument("w", type=float)
    l.add_argument("--kind", choices=["i", "v", "d"], required=True); l.add_argument("--ant", required=True)
    l.add_argument("--problem", default=""); l.add_argument("--why", default=""); l.add_argument("--evidence", default="")
    f = s.add_parser("food"); f.add_argument("--ant", required=True); f.add_argument("--problem", default="")
    f.add_argument("--strength", type=float, default=3); f.add_argument("--nodes", default=""); f.add_argument("--text", required=True)
    t = s.add_parser("trails"); t.add_argument("--problem"); t.add_argument("--kind"); t.add_argument("--top", type=int, default=25)
    ld = s.add_parser("larder"); ld.add_argument("--problem")
    sh = s.add_parser("show"); sh.add_argument("id")
    e = s.add_parser("echo"); e.add_argument("id"); e.add_argument("--k", type=int, default=10)
    n = s.add_parser("near"); n.add_argument("text"); n.add_argument("--k", type=int, default=12)
    r = s.add_parser("round"); r.add_argument("--bump", action="store_true")
    sp = s.add_parser("split"); sp.add_argument("--seed", type=int, default=2026); sp.add_argument("--include-housekeeping", action="store_true")
    lg = s.add_parser("ledger"); lg.add_argument("action", choices=["add", "summary"])
    lg.add_argument("--arm"); lg.add_argument("--problem"); lg.add_argument("--tokens", type=int, default=0)
    lg.add_argument("--outcome"); lg.add_argument("--proposal", default=""); lg.add_argument("--verdict", default="-")
    a = p.parse_args()
    G = build() if a.cmd not in ("init", "round", "ledger") else None
    globals()["cmd_" + a.cmd](a, G)


if __name__ == "__main__":
    main()
