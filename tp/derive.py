"""Derived state: everything the build computes and no file may hand-write.

Edges are read from front matter.  Logical edges (uses, assumes, specialises)
spread staleness and form light cones; lineage edges never do.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from .model import Store, parse_pin

RANK = {"unsupported": 0, "conjectured": 1, "conditional": 2, "proved": 3}
RANK_NAME = {v: k for k, v in RANK.items()}
# entities whose standing is given rather than derived keep their own name as their
# effective status (a postulate is assumed, not proved); they rank as fully supported
GIVEN = ("imported", "postulate", "defined")
RANK.update({g: 3 for g in GIVEN})
RANK["killed"] = 0
RANK["refuted"] = 0

LOGICAL = ("uses", "assumes", "specialises")
TOP_PINNED = ("specialises", "equivalent_to", "contradicts", "supports",
              "tests", "kills")
LINEAGE = ("derived_from", "supersedes", "inverts", "motivated_by")


@dataclass(frozen=True)
class Edge:
    src: str
    kind: str
    dst: str
    pin: int | None       # pinned version, None for unpinned edges
    derivation: str | None = None


def edges(store: Store) -> list[Edge]:
    out = []
    for eid, e in store.entities.items():
        for d in e.derivations():
            if not isinstance(d, dict):
                continue
            for k in ("uses", "assumes"):
                for ref in d.get(k) or []:
                    p = parse_pin(ref)
                    if p:
                        out.append(Edge(eid, k, p[0], p[1], d.get("name")))
        for k in TOP_PINNED:
            for ref in e.meta.get(k) or []:
                p = parse_pin(ref)
                if p:
                    out.append(Edge(eid, k, p[0], p[1]))
        for ref in e.meta.get("about") or []:
            out.append(Edge(eid, "about", ref, None))
        for k in LINEAGE:
            for ref in (e.meta.get("lineage") or {}).get(k) or []:
                out.append(Edge(eid, k, ref, None))
        for k in ("settled_by", "refuted_by", "comments_on"):
            for ref in e.meta.get(k) or []:
                out.append(Edge(eid, k, ref, None))
    return out


def logical_graph(store: Store, es: list[Edge] | None = None):
    """src -> set(dst) over logical edges whose target exists."""
    g = defaultdict(set)
    for ed in es if es is not None else edges(store):
        if ed.kind in LOGICAL and ed.dst in store.entities:
            g[ed.src].add(ed.dst)
    return g


def find_cycles(graph) -> list[list[str]]:
    """Strongly connected components of size > 1, plus self-loops (Tarjan)."""
    index, low, on, stack, out = {}, {}, set(), [], []
    counter = [0]
    nodes = set(graph) | {d for ds in graph.values() for d in ds}

    def visit(root):
        work = [(root, iter(sorted(graph.get(root, ()))))]
        index[root] = low[root] = counter[0]; counter[0] += 1
        stack.append(root); on.add(root)
        while work:
            v, it = work[-1]
            advanced = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = counter[0]; counter[0] += 1
                    stack.append(w); on.add(w)
                    work.append((w, iter(sorted(graph.get(w, ())))))
                    advanced = True
                    break
                elif w in on:
                    low[v] = min(low[v], index[w])
            if advanced:
                continue
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stack.pop(); on.discard(w); comp.append(w)
                    if w == v:
                        break
                if len(comp) > 1 or v in graph.get(v, ()):
                    out.append(sorted(comp))

    for n in sorted(nodes):
        if n not in index:
            visit(n)
    return out


def effective_status(store: Store) -> dict[str, str]:
    """Least fixpoint of: a claim is as strong as its best derivation, and a
    derivation is as strong as its weakest premise.  Starting every derived
    claim at 0 means a cycle can never support itself."""
    fixed, derived = {}, {}
    for eid, e in store.entities.items():
        s = e.status
        if e.kind == "object":
            fixed[eid] = 3
        elif e.kind == "note":
            fixed[eid] = 0
        elif s in ("imported", "postulate"):
            fixed[eid] = 3
        elif s in ("refuted", "killed"):    # a killed prediction supports nothing
            fixed[eid] = 0
        elif e.kind == "question":
            fixed[eid] = 0
        else:
            derived[eid] = 0
    val = {**fixed, **derived}

    def dval(d):
        prem = list(d.get("uses") or []) + list(d.get("assumes") or [])
        if not prem:
            r = 3          # a derivation from nothing (e.g. direct computation)
        else:
            r = 3
            for ref in prem:
                p = parse_pin(ref)
                r = min(r, val.get(p[0], 0) if p else 0)
        return min(r, 2) if d.get("conditional") else r

    changed = True
    while changed:
        changed = False
        for eid in derived:
            e = store.entities[eid]
            ds = [d for d in e.derivations() if isinstance(d, dict)]
            best = max((dval(d) for d in ds), default=0)
            cap = 1 if e.status == "conjectured" else 3
            new = max(min(best, cap), 1 if e.status == "conjectured" else 0)
            if new > val[eid]:
                val[eid] = new
                changed = True
    out = {}
    for eid, v in val.items():
        e = store.entities[eid]
        if e.kind == "object":
            out[eid] = "defined"
        elif e.kind == "note":
            out[eid] = e.status
        elif e.status in ("imported", "postulate"):
            out[eid] = e.status
        elif e.status in ("killed", "refuted"):
            out[eid] = e.status
        else:
            out[eid] = RANK_NAME[v]
    return out


def topo_order(graph, nodes) -> list[str]:
    """Premises before dependants.  Edges inside a cycle are ignored (the cycle
    itself is reported as E301), so a cycle's members and everything resting
    on them still receive an order."""
    in_cycle = {}
    for i, comp in enumerate(find_cycles(graph)):
        for n in comp:
            in_cycle[n] = i
    indeg = {n: 0 for n in nodes}
    rev = defaultdict(set)
    for s, ds in graph.items():
        for d in ds:
            if s in in_cycle and in_cycle.get(d) == in_cycle[s]:
                continue
            if s in indeg and d in indeg:
                indeg[s] += 1
                rev[d].add(s)
    ready = sorted(n for n, k in indeg.items() if k == 0)
    out = []
    while ready:
        n = ready.pop(0)
        out.append(n)
        for s in sorted(rev[n]):
            indeg[s] -= 1
            if indeg[s] == 0:
                ready.append(s)
    return out


def ledger(store: Store, graph=None) -> dict[str, str]:
    roots = set(store.config.get("transport_roots") or [])
    graph = graph if graph is not None else logical_graph(store)
    order = topo_order(graph, store.entities.keys())
    T = {}
    for eid in order:
        e = store.entities[eid]
        if eid in roots:
            T[eid] = "essential"
            continue
        ds = [d for d in e.derivations() if isinstance(d, dict)]
        if not ds:
            T[eid] = "absent"
            continue
        dep, touch = [], []
        for d in ds:
            prem = [parse_pin(r) for r in (d.get("uses") or []) + (d.get("assumes") or [])]
            prem = [p[0] for p in prem if p]
            dep.append(any(p in roots or T.get(p) == "essential" for p in prem))
            touch.append(any(p in roots or T.get(p) in ("essential", "convenient")
                             for p in prem))
        T[eid] = ("essential" if all(dep) else
                  "absent" if not any(touch) else "convenient")
    return T


def cones(graph, nodes):
    """Past cone (ancestors via logical edges) and future cone (dependants)."""
    rev = defaultdict(set)
    for s, ds in graph.items():
        for d in ds:
            rev[d].add(s)

    def closure(start, g):
        seen, todo = set(), [start]
        while todo:
            for n in g.get(todo.pop(), ()):
                if n not in seen:
                    seen.add(n); todo.append(n)
        seen.discard(start)
        return seen
    return ({n: closure(n, graph) for n in nodes},
            {n: closure(n, rev) for n in nodes})


def staleness(store: Store, check_failed: set[str], graph=None) -> dict:
    """An edge is stale when its pin is behind the target's current version.
    A claim is stale only when every derivation is broken: it holds a stale
    edge, a failed check, or a stale premise."""
    graph = graph if graph is not None else logical_graph(store)
    stale_edges = []
    for ed in edges(store):
        t = store.entities.get(ed.dst)
        if ed.pin is not None and t is not None and ed.pin < t.version:
            stale_edges.append(ed)
    stale_pairs = {(ed.src, ed.dst, ed.derivation) for ed in stale_edges}
    stale = set()
    order = topo_order(graph, store.entities.keys())
    while True:
        before = len(stale)
        _stale_pass(store, order, stale_pairs, stale, check_failed)
        _stale_specialisations(store, stale_pairs, stale, check_failed)
        if len(stale) == before:
            break
    return {"stale": stale, "stale_edges": stale_edges}


def _stale_pass(store, order, stale_pairs, stale, check_failed):
    for eid in order:
        if eid in stale:
            continue
        e = store.entities[eid]
        ds = [d for d in e.derivations() if isinstance(d, dict)]
        if not ds:
            continue
        broken = []
        for d in ds:
            prem = [parse_pin(r) for r in (d.get("uses") or []) + (d.get("assumes") or [])]
            b = False
            for p in prem:
                if not p:
                    continue
                if ((eid, p[0], d.get("name")) in stale_pairs or p[0] in stale
                        or p[0] in check_failed):
                    b = True
            broken.append(b)
        if all(broken):
            stale.add(eid)


def _stale_specialisations(store, stale_pairs, stale, check_failed):
    """A stale or broken specialisation / equivalence also makes a claim stale."""
    changed = True
    while changed:
        changed = False
        for ed in edges(store):
            if ed.kind in ("specialises", "equivalent_to") and ed.src not in stale:
                if (ed.src, ed.dst, None) in stale_pairs or ed.dst in stale \
                        or ed.dst in check_failed:
                    stale.add(ed.src)
                    changed = True


def conditions(store: Store, past: dict) -> dict[str, list[str]]:
    """The postulates each claim ultimately rests on: its past cone's
    postulates.  A result is shown as proved *given* these."""
    post = {k for k, e in store.entities.items() if e.status == "postulate"}
    return {k: sorted(past.get(k, set()) & post) for k in store.entities}
