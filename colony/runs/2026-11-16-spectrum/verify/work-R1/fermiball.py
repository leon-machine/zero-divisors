"""R1: exact bipolar integrals for the filled Weyl ball (k_F = 1), polynomials in (r, s, k) over Fractions.
T_{++} = (|p|+|q|)^2 (1+c)/8, T_{-+} = (|p|-|q|)^2 (1-c)/8 (derived by hand), d^3p = 2 pi r s dr ds / k."""
from fractions import Fraction as F
# polynomial: dict {(i,j,l): coeff} for r^i s^j k^l
def pmul(a, b):
    o = {}
    for (i, j, l), x in a.items():
        for (I, J, L), y in b.items():
            key = (i+I, j+J, l+L); o[key] = o.get(key, 0) + x*y
    return {k: v for k, v in o.items() if v}
def padd(*ps):
    o = {}
    for p in ps:
        for k, v in p.items(): o[k] = o.get(k, 0) + v
    return {k: v for k, v in o.items() if v}
def sc(p, c): return {k: v*c for k, v in p.items()}
def ppow(p, n):
    o = {(0,0,0): F(1)}
    for _ in range(n): o = pmul(o, p)
    return o
R = {(1,0,0): F(1)}; S = {(0,1,0): F(1)}; K = {(0,0,1): F(1)}; ONE = {(0,0,0): F(1)}
def subst(p, var, q):
    """substitute variable index var (0 r, 1 s) by polynomial q"""
    o = {}
    for key, v in p.items():
        rest = list(key); e = rest[var]; rest[var] = 0
        term = pmul({tuple(rest): v}, ppow(q, e))
        o = padd(o, term)
    return o
def integ(p, var, lo, hi):
    """integral over variable var from polynomial lo to hi"""
    anti = {}
    for key, v in p.items():
        kk = list(key); kk[var] += 1
        anti[tuple(kk)] = anti.get(tuple(kk), 0) + v / kk[var]
    return padd(subst(anti, var, hi), sc(subst(anti, var, lo), -1))
# integrands times 16 k/(2 pi):  A: (r+s)^2((r+s)^2 - k^2);  B: (r-s)^2(k^2 - (r-s)^2)
A = pmul(ppow(padd(R, S), 2), padd(ppow(padd(R, S), 2), sc(ppow(K, 2), -1)))
B = pmul(ppow(padd(R, sc(S, -1)), 2), padd(ppow(K, 2), sc(ppow(padd(R, sc(S, -1)), 2), -1)))
# A: r in [1-k, 1], s in [1, r+k]
IA = integ(integ(A, 1, ONE, padd(R, K)), 0, padd(ONE, sc(K, -1)), ONE)
# B: s in [0,1] (|q|<=1), r in [|s-k|, s+k]; split s in [0,k]: r from k-s; s in [k,1]: r from s-k
B1 = integ(integ(B, 0, padd(K, sc(S, -1)), padd(S, K)), 1, {}, K)
B2 = integ(integ(B, 0, padd(S, sc(K, -1)), padd(S, K)), 1, K, ONE)
IB = padd(B1, B2)
def kpoly(p):
    o = {}
    for (i, j, l), v in p.items():
        assert i == 0 and j == 0
        o[l] = o.get(l, 0) + v
    return {k: v for k, v in sorted(o.items()) if v}
# S_E = (2 pi / (16 k)) * I / (2 pi)^3 = I / (64 pi^2 k): report coefficient of 1/(pi^2)
ia, ib = kpoly(IA), kpoly(IB)
print('particle-hole * pi^2:', {l-1: v/64 for l, v in ia.items()})
print('pair-blocked  * pi^2:', {l-1: v/64 for l, v in ib.items()})
print('claimed ph: k/8 - k^5/1280 ; pair: k^4/240 - k^5/480 ; excess k/8 (1 - k^3/30 + k^4/96)')
