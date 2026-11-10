import sys, os, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations, product
import GA

E9 = GA.sig(9, 0)
IDX = range(3, 9)
EVEN = [b for k in (0, 2, 4, 6) for b in combinations(IDX, k)]
POS = {b: i for i, b in enumerate(EVEN)}
TAB = [[None] * 32 for _ in range(32)]
for i, a in enumerate(EVEN):
    for j, b in enumerate(EVEN):
        s, c = GA.blade_mul(a, b, E9)
        TAB[i][j] = (int(s), POS[c])


def m(x, y):
    out = [F(0)] * 32
    for i, a in enumerate(x):
        if a:
            row = TAB[i]
            for j, b in enumerate(y):
                if b:
                    s, k = row[j]
                    out[k] += s * a * b
    return tuple(out)


def to_arr(mv):
    a = [F(0)] * 32
    for b, c in mv.items():
        a[POS[b]] += c
    return tuple(a)


def rev(x):
    return tuple(c if len(EVEN[i]) % 4 == 0 else -c for i, c in enumerate(x))


def bv(i, j):
    return to_arr(GA.mul(GA.gen(i), GA.gen(j), E9))


ONE = to_arr(GA.sc(1))
I6 = to_arr({(3, 4, 5, 6, 7, 8): F(1)})
e34, e56, e78 = bv(3, 4), bv(5, 6), bv(7, 8)


def add(*xs):
    return tuple(sum(c) for c in zip(*xs))


def sca(c, x):
    return tuple(c * v for v in x)


half = F(1, 2)
E = ONE
for ek in (e34, e56, e78):
    E = m(E, sca(half, add(ONE, m(I6, ek))))
print('E scalar', E[0], 'E^2==E', m(E, E) == E, 'rev E == E', rev(E) == E)

# su(3): bivectors commuting with J, traceless
J = add(e34, e56, e78)
so6 = [bv(i, j) for i, j in combinations(IDX, 2)]
# annihilation of E by the u(3) generators
u3 = []
for i, j in combinations(IDX, 2):
    pass

# rotors
d1 = sca(half, m(add(ONE, sca(-1, e34)), add(ONE, e56)))
d2 = sca(half, m(add(ONE, sca(-1, e56)), add(ONE, e78)))
v = lambda k: to_arr(GA.gen(k)) if False else None
# vectors live in the odd part; use GA for sandwich
def to_mv(x):
    return {EVEN[i]: c for i, c in enumerate(x) if c}


def act(R, k):
    """R e_k R~ as vector coefficients over e3..e8"""
    y = GA.mul(GA.mul(to_mv(R), GA.gen(k), E9), to_mv(rev(R)), E9)
    assert all(len(b) == 1 for b in y)
    return [y.get((t,), F(0)) for t in IDX]


def S(a, b, c, d):
    # (e_a - e_b)(e_c - e_d)/2
    x = GA.sub(GA.gen(a), GA.gen(b)); y = GA.sub(GA.gen(c), GA.gen(d))
    return to_arr(GA.scal(half, GA.mul(x, y, E9)))


S12 = S(3, 5, 4, 6)
S23 = S(5, 7, 6, 8)
c = m(S23, S12)
t = m(S12, e78)
for name, R in (('d1', d1), ('d2', d2), ('c', c), ('t', t)):
    RE = m(R, E)
    sgn = 1 if RE == E else (-1 if RE == sca(-1, E) else 0)
    print(name, 'RR~', m(R, rev(R)) == ONE, 'RE=sE', sgn, [act(R, k) for k in IDX])
