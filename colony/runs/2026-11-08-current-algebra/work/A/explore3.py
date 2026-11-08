import sys, itertools
sys.path.insert(0, '.')
from fock import *
from fractions import Fraction as F

def run(n, L, X, m, d):
    W = Win(n, L)
    one = [[1 if a == b else 0 for b in range(n)] for a in range(n)]
    def HN(st):
        out = scal(F(1, 2 * n), W.cur(one, 0, W.cur(one, 0, st)))
        for q in range(1, L):
            out = add(out, scal(F(1, n), W.cur(one, -q, W.cur(one, q, st))))
        return out
    inner = [W.idx(x, k) for x in range(n) for k in range(d, L - d)]
    base = sum(1 << W.idx(x, k) for x in range(n) for k in range(d))
    bad = tot = 0
    for bits in itertools.product((0, 1), repeat=len(inner)):
        S = base + sum(b << i for b, i in zip(bits, inner))
        st = {S: F(1)}
        lhs = add(HN(W.cur(X, m, st)), scal(-1, W.cur(X, m, HN(st))))
        tot += 1
        bad += bool(lhs)
    return bad, tot
X = [[0, 1], [0, 0]]
for L in (6, 7):
    for m in (1, 2, 3, -2, -3):
        for d in (1, 2, 3):
            if 2 * d < L:
                print(L, m, d, run(2, L, X, m, d))
