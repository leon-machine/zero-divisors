"""The universe layout: place every entity in a ball so that each claim sits as
close as possible to what it rests on and to what rests on it.

The mathematics, in four steps.

1. The graph.  Entities are vertices; every logical or lineage link is an
   undirected edge with a weight w (premises 1, equivalences 1.5, `about` and
   lineage links 0.6).  Direction is dropped on purpose: "close to what it
   relies on AND to what relies on it" is symmetric.

2. Graph distance.  d_ij is the weighted shortest-path length (edge length
   1/w).  It is the number of inference steps between two results, so it is
   the distance a reader would travel.

3. Two embeddings, one for the whole and one for the neighbourhoods.
   (a) Stress majorisation finds x_i in R^3 minimising the stress

       S(X) = sum_{i<j} d_ij^-2 ( ||x_i - x_j|| - d_ij )^2

   (Kamada-Kawai's energy, solved by SMACOF: Gansner, Koren and North 2004),
   started from the spectral embedding (eigenvectors 2 to 4 of the normalised
   graph Laplacian, the exact minimiser of sum w ||x_i - x_j||^2 under a spread
   constraint: Hall 1970, Belkin and Niyogi 2003).  Stress gets the global
   arrangement right (which regions face which) but keeps only about 30% of a
   claim's links among its nearest neighbours in space.
   (b) Neighbour embedding then optimises exactly what is asked for: that a
   claim's nearest neighbours in space be its nearest neighbours in the
   argument.  Graph distances become neighbour probabilities p_ij (a Gaussian
   in d_ij, perplexity 10, about ten logical neighbours each), and positions
   are chosen to minimise the Kullback-Leibler divergence KL(P || Q) to the
   heavy-tailed spatial neighbourhood q_ij of t-SNE (van der Maaten and Hinton
   2008).  It starts from (a), so the global arrangement is kept as far as the
   local fit allows.  Subjects enter weakly: graph distances between results
   of the same subject are shortened by 20%, which makes each subject a
   contiguous region without overriding the logic (it costs about 1% of the
   neighbourhood score and raises subject purity from 61% to 73%).

4. The sphere.  The embedding is centred and its radial coordinate is
   replaced by its rank, r_i = R (rank_i / n)^(1/3), keeping every direction:
   equal volume per point, nothing buried in a dense core or flung to the
   edge.  The angular arrangement, which carries the neighbourhoods, is
   untouched.  (Ordering the radius by derivation depth, foundations at the
   centre, was tried and rejected: it costs a third of the neighbourhood
   score, because a result's premises and its dependants then sit on
   different shells.)

The module also measures the result: the mean edge length relative to the
mean distance between random pairs (lower is better), the share of each
claim's nearest neighbours in space that are its neighbours in the graph, and
the stress; and it compares the subject partition with the communities that
modularity maximisation finds.

    python -m tp.layout [--build build]      writes build/layout.json
"""
from __future__ import annotations

import argparse
import json
import math
import os

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components, shortest_path
from scipy.sparse.linalg import eigsh

WEIGHT = {"uses": 1.0, "assumes": 1.0, "specialises": 1.0, "equivalent_to": 1.5,
          "about": 0.6, "motivated_by": 0.6, "refuted_by": 0.6, "derived_from": 0.6,
          "supersedes": 0.6, "inverts": 0.6, "supports": 0.6, "tests": 0.6,
          "kills": 0.6, "settled_by": 0.6, "contradicts": 0.4}
LOGICAL = ("uses", "assumes", "specialises", "founded_on")


def graph(g):
    ids = [n["id"] for n in g["nodes"]]
    ix = {k: i for i, k in enumerate(ids)}
    W = {}
    for e in g["edges"]:
        a, b = ix.get(e["src"]), ix.get(e["dst"])
        if a is None or b is None or a == b:
            continue
        w = WEIGHT.get(e["kind"], 0.5)
        key = (min(a, b), max(a, b))
        W[key] = max(W.get(key, 0), w)
    return ids, ix, W


def distances(n, W):
    rows, cols, vals = [], [], []
    for (a, b), w in W.items():
        rows += [a, b]
        cols += [b, a]
        vals += [1.0 / w, 1.0 / w]
    A = csr_matrix((vals, (rows, cols)), shape=(n, n))
    D = shortest_path(A, directed=False)
    finite = D[np.isfinite(D)]
    D[~np.isfinite(D)] = finite.max() + 1.0
    return D


def spectral(n, W, dim=3, seed=0):
    rows, cols, vals = [], [], []
    for (a, b), w in W.items():
        rows += [a, b]
        cols += [b, a]
        vals += [w, w]
    A = csr_matrix((vals, (rows, cols)), shape=(n, n)).toarray()
    A += 1e-3 / n                         # a whisper of global coupling keeps it connected
    np.fill_diagonal(A, 0)
    d = A.sum(1)
    Dm = np.diag(1 / np.sqrt(d))
    L = np.eye(n) - Dm @ A @ Dm
    vals_, vecs = np.linalg.eigh(L)
    X = Dm @ vecs[:, 1:1 + dim]
    X -= X.mean(0)
    X /= np.sqrt((X ** 2).sum(1).mean())
    return X


def smacof(D, X, iters=300, tol=1e-6):
    n = len(D)
    Wt = np.zeros_like(D)
    mask = D > 0
    Wt[mask] = D[mask] ** -2.0
    V = -Wt.copy()
    np.fill_diagonal(V, Wt.sum(1))
    Vp = np.linalg.pinv(V)
    # scale the start to the targets
    dist = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
    s = (Wt * D * dist).sum() / max((Wt * dist * dist).sum(), 1e-12)
    X = X * s
    prev = None
    for _ in range(iters):
        dist = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
        np.fill_diagonal(dist, 1.0)
        dist = np.maximum(dist, 1e-9)   # two results placed on the same spot must not divide by zero
        B = -Wt * D / dist
        np.fill_diagonal(B, 0)
        np.fill_diagonal(B, -B.sum(1))
        X = Vp @ (B @ X)
        st = stress(D, X, Wt)
        if prev is not None and abs(prev - st) < tol * prev:
            break
        prev = st
    return X - X.mean(0)


def stress(D, X, Wt=None):
    dist = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
    if Wt is None:
        Wt = np.zeros_like(D)
        Wt[D > 0] = D[D > 0] ** -2.0
    iu = np.triu_indices(len(D), 1)
    return float((Wt[iu] * (dist[iu] - D[iu]) ** 2).sum() / (Wt[iu] * D[iu] ** 2).sum())


def to_ball(X, depth_rank=None, blend=0.35, R=1.0):
    """Equal volume per point: keep directions, replace radius by its rank."""
    r = np.sqrt((X ** 2).sum(1))
    u = X / np.maximum(r, 1e-9)[:, None]
    key = np.argsort(np.argsort(r)) / max(len(r) - 1, 1)
    if depth_rank is not None:
        key = (1 - blend) * key + blend * depth_rank
    order = np.argsort(np.argsort(key))
    rad = R * ((order + 0.5) / len(r)) ** (1 / 3)
    return u * rad[:, None]


def depth_ranks(g, ids, ix):
    """Longest derivation chain beneath each entity, as a rank in [0, 1]."""
    prem = {k: [] for k in ids}
    for e in g["edges"]:
        if e["kind"] in LOGICAL and e["src"] in prem and e["dst"] in prem:
            prem[e["src"]].append(e["dst"])
    memo = {}

    def depth(k, stack=()):
        if k in memo:
            return memo[k]
        if k in stack:
            return 0
        d = 1 + max((depth(p, stack + (k,)) for p in prem[k]), default=-1)
        memo[k] = d
        return d
    dep = np.array([depth(k) for k in ids], dtype=float)
    return np.argsort(np.argsort(dep + 1e-6 * np.arange(len(dep)))) / max(len(dep) - 1, 1), dep


CORE_LINKS = ("uses", "assumes", "specialises", "equivalent_to", "founded_on")


def is_core(node):
    """The algebra core: the standard programme's algebra subject (docs/ALGEBRA_CORE.md), and
    the foundation postulates beneath it (store/conventions.md, "The foundation")."""
    return node.get("subject") == "standard-algebra" or node.get("is_foundation", False)


def core_distance(g, ids, about=True):
    """Fewest premise steps from each entity down to the algebra core: 0 for the core, 1 for
    a result that uses a core result, and so on; -1 when no chain of premises reaches it.
    Steps follow uses, assumes and specialises from a result to what it rests on, and
    equivalent_to either way; `about` (a result is about a definition) also counts, since
    a definition in the core is what the result is stated in."""
    down = {k: set() for k in ids}
    for e in g["edges"]:
        a, b = e["src"], e["dst"]
        if a not in down or b not in down:
            continue
        if e["kind"] in CORE_LINKS or (about and e["kind"] == "about"):
            down[a].add(b)
        if e["kind"] == "equivalent_to":
            down[b].add(a)
    up = {k: set() for k in ids}
    for a, bs in down.items():
        for b in bs:
            up[b].add(a)
    byid = {n["id"]: n for n in g["nodes"]}
    dist = {k: -1 for k in ids}
    frontier = [k for k in ids if is_core(byid[k])]
    for k in frontier:
        dist[k] = 0
    d = 0
    while frontier:
        d += 1
        nxt = []
        for b in frontier:
            for a in up[b]:
                if dist[a] < 0:
                    dist[a] = d
                    nxt.append(a)
        frontier = nxt
    return dist


def spectral_init(n, seed=0):
    """A fixed, well-spread start: points on a Fibonacci sphere."""
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], 1)


def core_depths(g, ids, cdist):
    """Longest chain of premises inside the core beneath each core result (0 for a core
    result that uses no other core result), so the core can be laid out from its axioms out."""
    core = {k for k in ids if cdist.get(k) == 0}
    prem = {k: [] for k in core}
    for e in g["edges"]:
        if e["kind"] in LOGICAL and e["src"] in core and e["dst"] in core:
            prem[e["src"]].append(e["dst"])
    memo = {}

    def depth(k, stack=()):
        if k in memo:
            return memo[k]
        if k in stack:
            return 0
        d = 1 + max((depth(p, stack + (k,)) for p in prem[k]), default=-1)
        memo[k] = d
        return d
    return {k: depth(k) for k in core}


def to_foundations(X, cdist, own_depth, core_depth, D=None, R_in=0.74, gap=0.03, outer=(0.80, 1.0)):
    """The foundations arrangement. Each point keeps its direction from the chosen layout, so
    subjects stay as sectors; only its radius changes.

    Inner ball: everything a chain of premises connects to the algebra core, in shells by
    the number of steps to the core (0 = the core itself). Radii are equal-volume by
    population: every point gets the same volume, so a shell is as thick as it is populous
    and the core is not crushed into a point, with an empty gap (a fraction `gap` of the
    points) between consecutive shells so the layers read as layers. Inside the core,
    results are ordered by their depth within the core (its axioms innermost); inside other
    shells by their radius in the chosen layout.

    Outer zone: everything that rests on the programme's postulates and imported physics but
    on no core result, ordered by its own derivation depth (roots on the inner edge), again
    equal-volume. Returns the positions and the shell radii for the page.

    The core's own directions come from a stress layout of the core alone (graph distances
    among core results): in the chosen layout the core results are neighbours and point the
    same way, which would leave them a thin spoke rather than a ball."""
    r = np.sqrt((X ** 2).sum(1))
    u = X / np.maximum(r, 1e-9)[:, None]
    cd0 = np.where(np.array(cdist) == 0)[0]
    if D is not None and len(cd0) > 3:
        Dc = D[np.ix_(cd0, cd0)]
        Y = smacof(Dc, X[cd0] - X[cd0].mean(0) + 1e-3 * spectral_init(len(cd0)))
        Y -= Y.mean(0)
        u[cd0] = Y / np.maximum(np.sqrt((Y ** 2).sum(1)), 1e-9)[:, None]
    rr = np.argsort(np.argsort(r)) / max(len(r) - 1, 1)
    cd = np.array(cdist)
    out = np.zeros(len(cd))
    inner = np.where(cd >= 0)[0]
    ds = sorted(set(cd[inner].tolist()))
    g = max(2.0, gap * len(inner))
    total = len(inner) + g * (len(ds) - 1)
    t, shells = 0.0, []
    for k, d in enumerate(ds):
        sel = inner[cd[inner] == d]
        key = [((core_depth[i] if d == 0 else 0), rr[i]) for i in sel]
        order = [sel[j] for j in sorted(range(len(sel)), key=lambda j: key[j])]
        lo = R_in * (t / total) ** (1 / 3)
        for i in order:
            out[i] = R_in * ((t + 0.5) / total) ** (1 / 3)
            t += 1
        shells.append({"d": int(d), "lo": round(float(lo), 4),
                       "hi": round(float(R_in * (t / total) ** (1 / 3)), 4), "n": int(len(sel))})
        t += g if k < len(ds) - 1 else 0
    rest = np.where(cd < 0)[0]
    if len(rest):
        order = sorted(rest, key=lambda i: (own_depth[i], rr[i]))
        a, b = outer
        for j, i in enumerate(order):
            f = (j + 0.5) / len(order)
            out[i] = (a ** 3 + (b ** 3 - a ** 3) * f) ** (1 / 3)
        shells.append({"d": -1, "lo": a, "hi": b, "n": int(len(rest))})
    return u * out[:, None], shells


def metrics(X, W, D, subjects):
    n = len(X)
    dist = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
    iu = np.triu_indices(n, 1)
    mean_pair = dist[iu].mean()
    el = np.array([dist[a, b] for (a, b) in W])
    nbr = [set() for _ in range(n)]
    for (a, b) in W:
        nbr[a].add(b)
        nbr[b].add(a)
    two = [set(s) for s in nbr]
    for i in range(n):
        for j in nbr[i]:
            two[i] |= nbr[j]
        two[i].discard(i)
    p1, p2, same = [], [], []
    order = np.argsort(dist, 1)
    for i in range(n):
        k = len(nbr[i])
        if k == 0:
            continue
        near = [j for j in order[i, 1:k + 1]]
        p1.append(sum(j in nbr[i] for j in near) / k)
        near10 = order[i, 1:11]
        p2.append(sum(j in two[i] for j in near10) / 10)
        same.append(sum(subjects[j] == subjects[i] for j in near10) / 10)
    return {"edge_length_ratio": round(float(el.mean() / mean_pair), 4),
            "neighbours_recovered": round(float(np.mean(p1)), 4),
            "two_step_in_nearest_10": round(float(np.mean(p2)), 4),
            "same_subject_in_nearest_10": round(float(np.mean(same)), 4)}


def communities(ids, W, subjects):
    import networkx as nx
    G = nx.Graph()
    G.add_nodes_from(range(len(ids)))
    for (a, b), w in W.items():
        G.add_edge(a, b, weight=w)
    parts = {}
    for i, s in enumerate(subjects):
        parts.setdefault(s, set()).add(i)
    q_subj = nx.algorithms.community.modularity(G, list(parts.values()), weight="weight")
    comms = nx.algorithms.community.louvain_communities(G, weight="weight", seed=1)
    q_louv = nx.algorithms.community.modularity(G, comms, weight="weight")
    # how well subjects explain the found communities (normalised mutual information)
    lab_c = np.zeros(len(ids), int)
    for k, c in enumerate(comms):
        for i in c:
            lab_c[i] = k
    from collections import Counter
    def H(lab):
        c = Counter(lab)
        p = np.array(list(c.values())) / len(lab)
        return float(-(p * np.log(p)).sum())
    joint = Counter(zip(subjects, lab_c))
    pj = np.array(list(joint.values())) / len(ids)
    hj = float(-(pj * np.log(pj)).sum())
    mi = H(subjects) + H(list(lab_c)) - hj
    nmi = 2 * mi / (H(subjects) + H(list(lab_c)))
    return {"modularity_subjects": round(q_subj, 4), "modularity_louvain": round(q_louv, 4),
            "louvain_communities": len(comms), "nmi_subjects_vs_louvain": round(nmi, 4)}


def tsne(D, init, perplexity=10, seed=0):
    from sklearn.manifold import TSNE
    init = (init / np.std(init) * 1e-2).astype(np.float32)
    return TSNE(3, metric="precomputed", init=init, perplexity=perplexity,
                random_state=seed, max_iter=1500).fit_transform(D).astype(float)


def global_order(X, D, sample=60000, seed=0):
    """Spearman correlation between spatial and graph distance over pairs."""
    from scipy.stats import spearmanr
    n = len(X)
    iu = np.triu_indices(n, 1)
    rng = np.random.default_rng(seed)
    sel = rng.choice(len(iu[0]), min(sample, len(iu[0])), replace=False)
    dist = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
    return round(float(spearmanr(dist[iu][sel], D[iu][sel]).statistic), 4)


def compute(g, cohesion=0.2, perplexity=10, compare=True):
    # notes (remarks, examples) are commentary, not points of the universe
    g = dict(g, nodes=[n for n in g["nodes"] if n.get("kind") != "note"])
    ids, ix, W = graph(g)
    n = len(ids)
    subjects = [nd.get("subject") or "none" for nd in g["nodes"]]
    D = distances(n, W)
    X0 = spectral(n, W)
    Ds = D.copy()
    same = np.array(subjects)[:, None] == np.array(subjects)[None, :]
    Ds[same] *= (1 - cohesion)
    np.fill_diagonal(Ds, 0)
    report = {}

    def rec(name, X):
        report[name] = metrics(X, W, D, subjects)
        report[name]["global_order"] = global_order(X, D)
    Xs = smacof(Ds, X0.copy())
    X = tsne(Ds, Xs, perplexity)
    Xb = to_ball(X)
    if compare:
        rec("random", to_ball(np.random.default_rng(0).normal(size=(n, 3))))
        rec("spectral", to_ball(X0))
        rec("stress", to_ball(Xs))
    rec("chosen", Xb)
    report["chosen"]["method"] = (f"t-SNE (perplexity {perplexity}) on graph distance, "
                                  f"started from stress majorisation, subject cohesion "
                                  f"{cohesion}, equal-volume ball")
    report["communities"] = communities(ids, W, subjects)
    dr, dep = depth_ranks(g, ids, ix)
    pos = {k: [round(float(v), 4) for v in Xb[i]] for k, i in ix.items()}
    # the foundations arrangement: the algebra core at the centre (see to_foundations)
    cdist = core_distance(g, ids)
    cdep = core_depths(g, ids, cdist)
    Xf, shells = to_foundations(Xb, [cdist[k] for k in ids], dep,
                                {ix[k]: v for k, v in cdep.items()}, D=D)
    rec("foundations", Xf)
    report["foundations"]["method"] = ("directions of the chosen layout; radius by premise steps to "
                                       "the algebra core, equal volume per point with gaps between "
                                       "shells; results resting on postulates and imports but no core "
                                       "result in an outer zone")
    report["foundations"]["shells"] = shells
    vals = list(cdist.values())
    strict = core_distance(g, ids, about=False)
    report["core"] = {"core": sum(1 for v in vals if v == 0),
                      "reach_core": sum(1 for v in vals if v >= 0),
                      "reach_core_by_premises_only": sum(1 for v in strict.values() if v >= 0),
                      "unconnected": sum(1 for v in vals if v < 0),
                      "entities": len(vals), "max_distance": max(vals) if vals else 0}
    pos_core = {k: [round(float(v), 4) for v in Xf[i]] for k, i in ix.items()}
    return pos, report, {k: int(dep[i]) for k, i in ix.items()}, pos_core, cdist


def main(build="build"):
    g = json.load(open(os.path.join(build, "graph.json")))
    pos, report, depth, pos_core, cdist = compute(g)
    json.dump({"positions": pos, "depth": depth, "positions_core": pos_core,
               "core_distance": cdist, "shells": report["foundations"]["shells"],
               "report": report},
              open(os.path.join(build, "layout.json"), "w"))
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", default="build")
    main(ap.parse_args().build)
