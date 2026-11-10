import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
ONE = GA.sc(F(1))
def dsign(b, sq):
    g = len(b); s = (-1) ** (g * (g - 1) // 2)
    for i in b: s *= sq[i]
    return s
def dagger(x, sq): return {b: c * dsign(b, sq) for b, c in x.items()}
def prod(sq, *xs):
    r = ONE
    for x in xs: r = GA.mul(r, x, sq)
    return r
def s0(x): return x.get((), F(0))
def clean(x): return {b: c for b, c in x.items() if c != 0}
def modes(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]; f = [GA.gen(2 * k + 1) for k in range(m)]
    p = [GA.mul(f[k], e[k], sq) for k in range(m)]
    return sq, e, f, p
def chsh(sq, a1, a2, b1, b2):
    return GA.add(prod(sq, a1, b1), prod(sq, a1, b2), prod(sq, a2, b1), GA.neg(prod(sq, a2, b2)))
def is_obs(x, sq): return clean(dagger(x, sq)) == clean(x) and clean(prod(sq, x, x)) == ONE
def par(x): return {b: (c if len(b) % 2 == 0 else -c) for b, c in x.items()}
def even(x): return clean({b: c for b, c in x.items() if len(b) % 2 == 0})
def odd(x): return clean({b: c for b, c in x.items() if len(b) % 2 == 1})
def lin(*terms):
    r = {}
    for c, x in terms: r = GA.add(r, GA.scal(F(c), x))
    return clean(r)
