import sys, itertools
sys.path.insert(0, '.')
from fock import *
from fractions import Fraction as F

def test(n, L):
    W = Win(n, L)
    one = [[1 if a == b else 0 for b in range(n)] for a in range(n)]
    bad = 0
    for S in range(1 << (n * L)):
        st = {S: F(1)}
        K = W.num(st, lambda k: k)
        N = W.num(st, lambda k: 1)
        # T_gl
        Tgl = {}
        for q in range(1, L):
            for x in range(n):
                for y in range(n):
                    Tgl = add(Tgl, W.cur(W.E(y, x), -q, W.cur(W.E(x, y), q, st)))
        TN = {}
        for q in range(1, L):
            TN = add(TN, W.cur(one, -q, W.cur(one, q, st)))
        G0 = {}
        for x in range(n):
            for y in range(n):
                G0 = add(G0, W.cur(W.E(x, y), 0, W.cur(W.E(y, x), 0, st)))
        N02 = W.cur(one, 0, W.cur(one, 0, st))
        lhs = scal(n + 1, K)
        rhs = add(Tgl, TN, scal(F(1, 2), add(G0, N02)), scal(F(-(n + 1), 2), N))
        if add(lhs, scal(-1, rhs)):
            bad += 1
    return bad

for n, L in ((1, 4), (2, 3), (3, 2), (2, 4), (3, 3)):
    print(n, L, test(n, L))
