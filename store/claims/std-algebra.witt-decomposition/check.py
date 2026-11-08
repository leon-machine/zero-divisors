from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


# nondegenerate planes (Gram matrices) with a nonzero null vector u in coordinates
PLANES = [
    ([[1, 0], [0, -1]], [1, 1]),
    ([[0, 1], [1, 0]], [1, 0]),
    ([[3, 1], [1, -1]], [1, -1]),
    ([[1, 2], [2, 0]], [4, -1]),
]


def B_(G, x, y):
    return sum(F(G[i][j]) * x[i] * y[j] for i in range(len(G)) for j in range(len(G)))


def check_hyperbolic_partner_in_a_plane():
    premise("std-algebra.polarisation")
    premise("std-algebra.vector-squares")
    ok = True
    ws = []
    for G, u in PLANES:
        u = [F(a) for a in u]
        ok = ok and B_(G, u, u) == 0
        x = next(e for e in ([F(1), F(0)], [F(0), F(1)]) if B_(G, u, e) != 0)
        x = [a / (2 * B_(G, u, x)) for a in x]
        t = -B_(G, x, x)
        w = [a + t * b for a, b in zip(x, u)]
        ok = ok and B_(G, w, w) == 0 and B_(G, u, w) == F(1, 2)
        e = [a + b for a, b in zip(u, w)]
        f = [a - b for a, b in zip(u, w)]
        ok = ok and B_(G, e, e) == 1 and B_(G, f, f) == -1 and B_(G, e, f) == 0
        ws.append(w)
    ok = ok and ws == [[F(1, 4), F(-1, 4)], [F(0), F(1, 2)], [F(1, 16), F(3, 16)], [F(0), F(1, 16)]]
    GA.check("a null vector in a nondegenerate plane has a hyperbolic partner; e = u + w, f = u - w", ok)
    return ok


def check_witt_decomposition_and_maximal_null_subspace():
    premise("synthesis.completion-recovers-the-real-clifford-algebras")
    ok = True
    tested = 0
    for p, q, r in S.signatures(5):
        sq = GA.sig(p, q, r)
        n = len(sq)
        m = min(p, q)
        us = [S.vec([F(1, 2) if k in (i, p + i) else 0 for k in range(n)]) for i in range(m)]
        ws = [S.vec([F(1, 2) if k == i else (F(-1, 2) if k == p + i else 0) for k in range(n)]) for i in range(m)]
        for i in range(m):
            ok = ok and GA.dot(us[i], us[i], sq) == 0 and GA.dot(ws[i], ws[i], sq) == 0
            ok = ok and GA.eq(GA.add(GA.mul(us[i], ws[i], sq), GA.mul(ws[i], us[i], sq)), GA.sc(1))
            for j in range(m):
                if j != i:
                    ok = ok and GA.dot(us[i], ws[j], sq) == 0 and GA.dot(us[i], us[j], sq) == 0
        # N = span(u_i) + radical; its orthogonal complement has form of signature (p-m, q-m, m+r)
        rad = [S.vec([1 if k == j else 0 for k in range(n)]) for j in range(p + q, n)]
        Nvecs = [S.coords(x, n)[1:n + 1] for x in us + rad]
        rows = [[a * sq[k] for k, a in enumerate(v)] for v in Nvecs]
        perp = S.nullspace(rows) if rows else [[F(1) if k == j else F(0) for k in range(n)] for j in range(n)]
        G = [[sum(a[k] * b[k] * sq[k] for k in range(n)) for b in perp] for a in perp]
        ok = ok and GA.congruence_signature(G) == (p - m, q - m, m + r)
        ok = ok and len(perp) == n - m
        tested += 1
    ok = ok and tested == 3 + 6 + 10 + 15 + 21
    GA.check("Witt decomposition of every R^{p,q,r}, n <= 5; N^perp/N definite, so N is maximal totally null", ok)
    return ok
