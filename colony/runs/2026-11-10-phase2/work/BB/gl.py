from bbl import *
from itertools import product
from math import gcd
R = 3
vecs = []
for v in product(range(-R, R+1), repeat=4):
    if v == (0,0,0,0): continue
    g = 0
    for x in v: g = gcd(g, abs(x))
    if g != 1: continue
    fn = next(x for x in v if x != 0)
    if fn < 0: continue
    vecs.append(v)
dot = lambda a, b: sum(x*y for x, y in zip(a, b))
n = len(vecs); print('rays', n)
adj = [[j for j in range(n) if j > i and dot(vecs[i], vecs[j]) == 0] for i in range(n)]
tets = []
for i in range(n):
    for j in adj[i]:
        sj = set(adj[j])
        for k in adj[i]:
            if k > j and k in sj:
                sk = set(adj[k])
                for l in adj[i]:
                    if l > k and l in sj and l in sk: tets.append((i, j, k, l))
print('tetrads', len(tets))
for m in (2, 3, 4):
    def cls(v):
        c = tuple(x % m for x in v); c2 = tuple((-x) % m for x in v)
        return min(c, c2)
    classes = sorted(set(cls(v) for v in vecs)); ci = {c: i for i, c in enumerate(classes)}
    rows = set()
    for t in tets:
        r = [0] * (len(classes) + 1)
        for i in t: r[ci[cls(vecs[i])]] += 1
        r[-1] = 1
        rows.add(tuple(r))
    M = [[F(x) for x in r[:-1]] for r in rows]
    rk = GA.mat_rank(M); rk2 = GA.mat_rank([[F(x) for x in r] for r in rows])
    print('mod', m, 'classes', len(classes), 'distinct constraints', len(rows), 'rank', rk, 'aug rank', rk2, 'solution dim', len(classes) - rk)
