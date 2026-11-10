"""Referee R1's own exact Clifford algebra (bitmask blades, Fractions). Independent of lib/GA.py."""
from fractions import Fraction as F
class Cl:
    def __init__(s, sq):
        s.sq = list(sq); s.n = len(sq)
    def bmul(s, a, b):
        # sign of e_a e_b, result blade a^b
        sign = 1
        t = a >> 1
        cnt = 0
        while t:
            cnt += bin(t & b).count('1'); t >>= 1
        if cnt & 1: sign = -sign
        c = a & b; i = 0
        while c:
            if c & 1: sign *= s.sq[i]
            c >>= 1; i += 1
        return sign, a ^ b
    def mul(s, x, y):
        r = {}
        for a, ca in x.items():
            for b, cb in y.items():
                sg, c = s.bmul(a, b)
                r[c] = r.get(c, 0) + sg * ca * cb
        return {k: v for k, v in r.items() if v != 0}
    def prod(s, *xs):
        r = {0: F(1)}
        for x in xs: r = s.mul(r, x)
        return r
    def dag(s, x):
        # blade inverse: e_S^{-1} = e_S / (e_S^2)
        r = {}
        for a, c in x.items():
            sg, z = s.bmul(a, a)
            r[a] = c * sg
        return r
    def gen(s, i): return {1 << i: F(1)}
def add(*xs):
    r = {}
    for x in xs:
        for k, v in x.items(): r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v != 0}
def sc(c, x): return {k: F(c) * v for k, v in x.items() if c != 0}
def sub(x, y): return add(x, sc(-1, y))
def one(c=1): return {0: F(c)} if c != 0 else {}
def s0(x): return x.get(0, F(0))
