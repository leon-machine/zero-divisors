import sys
sys.path.insert(0, '.')
from fock import *
from fractions import Fraction as F

def run(n, L, X, m):
    W = Win(n, L)
    one = [[1 if a == b else 0 for b in range(n)] for a in range(n)]
    def HN(st):
        out = scal(F(1, 2 * n), W.cur(one, 0, W.cur(one, 0, st)))
        for q in range(1, L):
            out = add(out, scal(F(1, n), W.cur(one, -q, W.cur(one, q, st))))
        return out
    res = {}
    for S in range(1 << (n * L)):
        st = {S: F(1)}
        lhs = add(HN(W.cur(X, m, st)), scal(-1, W.cur(X, m, HN(st))))
        ok = not lhs
        # depth: largest d with levels <d filled and >= L-d empty in all channels
        d = 0
        while d < L:
            good = all((S >> W.idx(x, d)) & 1 and not (S >> W.idx(x, L - 1 - d)) & 1 for x in range(n)) if d < L - 1 - d else False
            if not good: break
            d += 1
        res.setdefault(d, [0, 0])
        res[d][ok] += 1
    return res
X = [[0, 1], [0, 0]]
for L in (4, 5, 6):
    for m in (0, 1, -1, 2):
        print(L, m, run(2, L, X, m))
