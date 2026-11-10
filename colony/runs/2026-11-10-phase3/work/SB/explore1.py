import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F

def eadd(*xs):
    out = {}
    for x in xs:
        for key, v in x.items():
            nv = out.get(key, 0) + v
            if nv == 0:
                out.pop(key, None)
            else:
                out[key] = nv
    return out
def escal(c, x):
    return {key: c * v for key, v in x.items() if c * v != 0}
def emul(x, y):
    out = {}
    for (n1, d1, t1, m1), v1 in x.items():
        for (n2, d2, t2, m2), v2 in y.items():
            if d1 >= 0 and d2 >= 0:
                continue
            key = (n1 + n2, max(d1, d2), max(t1, t2), m1 + m2)
            nv = out.get(key, 0) + v1 * v2
            if nv == 0: out.pop(key, None)
            else: out[key] = nv
    return out
def ediff(x, coord, j=1):
    out = {}
    for (n, d, t, m), v in x.items():
        if coord == 0:
            if n != 0:
                out = eadd(out, {(n - 1, d, t, m): v * n})
            if d >= 0:
                out = eadd(out, {(n, d + 1, t, m): v})
        elif coord == j and t:
            out = eadd(out, {(n, d, 2, m + 1): -v} if t == 1 else {(n, d, 1, m + 1): v})
    return out
def mono(c, n):
    return {(F(n), -1, 0, 0): F(c)} if c != 0 else {}

def ricci(G, Gi, D):
    dG = [[[ediff(G[x][y], c) for c in range(D)] for y in range(D)] for x in range(D)]
    Gam = [[[{} for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for s in range(D):
        for x in range(D):
            for y in range(x, D):
                acc = {}
                for l in range(D):
                    if not Gi[s][l]: continue
                    t = eadd(dG[l][y][x], dG[l][x][y], escal(-1, dG[x][y][l]))
                    if t: acc = eadd(acc, emul(Gi[s][l], t))
                Gam[s][x][y] = Gam[s][y][x] = escal(F(1, 2), acc)
    Ric = {}
    for x in range(D):
        for y in range(x, D):
            acc = {}
            for s in range(D):
                acc = eadd(acc, ediff(Gam[s][x][y], s), escal(-1, ediff(Gam[s][x][s], y)))
                for l in range(D):
                    acc = eadd(acc, emul(Gam[s][s][l], Gam[l][x][y]), escal(-1, emul(Gam[s][y][l], Gam[l][x][s])))
            Ric[(x, y)] = acc
    return Ric, Gam

def reduce_ode(x, fr, pj):
    """A'' -> -fr A'/T - k^2 T^(-2 pj) A, repeatedly"""
    while True:
        hi = [key for key in x if key[1] >= 2]
        if not hi: return x
        key = max(hi, key=lambda q: q[1])
        n, d, t, m = key; v = x[key]
        x = dict(x); del x[key]
        # A^(d) = d^(d-2)/dT^(d-2) of rhs ; apply to the single term T^n * A^(2) -> T^n * D^(d-2)[rhs]
        rhs = {(F(-1), 1, 0, 0): -fr, (F(-2) * pj, 0, 0, 2): F(-1)}
        for _ in range(d - 2):
            rhs = ediff(rhs, 0)
        rhs = {(n + a, b, t, m + mm): v * c for (a, b, _, mm), c in rhs.items()}
        x = eadd(x, rhs)

def build(p, D, alpha, beta, bn, gam=None):
    G = [[{} for _ in range(D)] for _ in range(D)]
    Gi = [[{} for _ in range(D)] for _ in range(D)]
    Phi = {(F(0), 0, 1, 0): F(alpha)}
    G[0][0] = eadd(mono(-1, 0), escal(-2, Phi))
    Gi[0][0] = eadd(mono(-1, 0), escal(2, Phi))
    for i in range(1, D):
        G[i][i] = mono(1, 2 * p); Gi[i][i] = mono(1, -2 * p)
    b = {(F(bn), 1, 2, -1): F(beta)}
    G[0][1] = G[1][0] = b
    # inverse first order: g^{0x} = - g^{00} g^{xx} h_0x  = + T^{-2p} b
    Gi[0][1] = Gi[1][0] = escal(-1, emul(emul(b, mono(-1, 0)), mono(1, -2 * p)))
    return G, Gi

p = F(1, 3)
for beta in (F(1), F(-1)):
    G, Gi = build(p, 4, 1, beta, F(2, 3))
    Ric, Gam = ricci(G, Gi, 4)
    # sources: delta phi = c A cos, phi0 = c ln T, c^2 = 2/3 : (0,0): 2 c^2 Adot/T cos ; (0,1): -c^2 k A sin / T
    c2 = F(2, 3)
    src = {(0, 0): eadd(mono(c2, -2), {(F(-1), 1, 1, 0): 2 * c2}), (0, 1): {(F(-1), 0, 2, 1): -c2}}
    print("beta", beta)
    for key in sorted(Ric):
        r = eadd(Ric[key], escal(-1, src.get(key, {})))
        r = reduce_ode(r, F(1), p)
        print(key, r)
