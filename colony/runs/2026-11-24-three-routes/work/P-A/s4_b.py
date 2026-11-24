import sys
sys.path.insert(0, '/home/claude/leon-machine/zero-divisors/lib')
from fractions import Fraction as F
from itertools import product
import GA
SQ = (1, -1, 1, -1)
ONE = GA.sc(1)
e1, f1, e2, f2 = [GA.gen(i) for i in range(4)]
def M(*xs):
    out = ONE
    for x in xs: out = GA.mul(out, x, SQ)
    return out
def dag(x):
    out = {}
    for b, c in x.items():
        g = len(b); s = F(-1) ** (g * (g - 1) // 2)
        for k in b: s *= SQ[k]
        out[b] = s * c
    return out
A = [e1, M(f1, e1)]; B = [M(e2, f1, e1), M(f2, e2)]
T = {(i, j): M(A[i], B[j]) for i in range(2) for j in range(2)}
C = GA.add(T[0, 0], T[0, 1], T[1, 0], GA.neg(T[1, 1]))
D1 = GA.sub(T[0, 0], T[1, 1]); D2 = GA.add(T[0, 1], T[1, 0])
print('D1^3=4D1', GA.eq(M(D1, D1, D1), GA.scal(4, D1)), 'D2^3=4D2', GA.eq(M(D2, D2, D2), GA.scal(4, D2)), 'commute', GA.commutes(D1, D2, SQ), 'D1^2', M(D1, D1), 'D2^2', M(D2,D2))
v = [GA.scal(F(1, 2), GA.add(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(2)]
w = [GA.scal(F(1, 2), GA.sub(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(2)]
P0 = M(w[0], v[0], w[1], v[1])
s = [P0, M(v[0], P0), M(v[1], P0), M(v[0], v[1], P0)]
def atom(r):
    y = GA.add(*[GA.scal(F(r[i]), s[i]) for i in range(4) if r[i]])
    return GA.scal(F(1, sum(c * c for c in r)), M(y, dag(y)))
def lam(x): return M(GA.add(ONE, C), x).get((), F(0))
print('box atom', lam(atom((1, 0, 0, 1))))
loc = {}
for i, j in product(range(2), repeat=2):
    for a, b in product((1, -1), repeat=2):
        E = M(GA.scal(F(1, 2), GA.add(ONE, GA.scal(a, A[i]))), GA.scal(F(1, 2), GA.add(ONE, GA.scal(b, B[j]))))
        assert GA.eq(M(E, E), E) and GA.eq(dag(E), E)
        loc[i, j, a, b] = lam(E)
print('box local table', sorted(set(loc.values())), [str(loc[0,0,a,b]) for a,b in product((1,-1),repeat=2)], [str(loc[1,1,a,b]) for a,b in product((1,-1),repeat=2)])
best = None
vals = {}
for r in product(range(-3, 4), repeat=4):
    if not any(r): continue
    P = atom(r)
    S = 4 * M(P, C).get((), F(0))
    vals[r] = S
    assert S * S < 8
    if best is None or S > best[0]: best = (S, r)
print('max S over atoms with entries up to 3:', best)
for r in [(1, 0, 0, 0), (1, 1, 0, 0), (2, 1, 0, 0), (1, 2, 2, 1), (1, 0, 0, 1), (2, 1, 1, 2), (1,2,-2,-1), (3,1,1,2)]:
    P = atom(r)
    k = [4 * M(P, T[i, j]).get((), F(0)) for i in range(2) for j in range(2)]
    print(r, [str(x) for x in k], 'S =', k[0] + k[1] + k[2] - k[3], ' L(K)=', 4 * M(P, M(e1, f2)).get((), F(0)))
K = M(e1, f2)
print('K self-adjoint', GA.eq(dag(K), K), 'K^2=1', GA.eq(M(K, K), ONE), 'C^2 = 4+4K', GA.eq(M(C, C), GA.add(GA.scal(4, ONE), GA.scal(4, K))))
