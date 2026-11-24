"""Scratch: P3. The CHSH element at the stored settings of Cl(2,2)."""
import sys
sys.path.insert(0, '/home/claude/leon-machine/zero-divisors/lib')
from fractions import Fraction as F
from itertools import combinations
import GA
SQ = (1, -1, 1, -1)
e1, f1, e2, f2 = GA.gen(0), GA.gen(1), GA.gen(2), GA.gen(3)
ONE = GA.sc(1)
def M(*xs):
    out = ONE
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out
def dag(x):
    out = {}
    for b, c in x.items():
        g = len(b); s = F(-1) ** (g * (g - 1) // 2)
        for k in b: s *= SQ[k]
        out[b] = s * c
    return out
A1, A2 = e1, M(f1, e1)
B1, B2 = M(e2, f1, e1), M(f2, e2)
for X in (A1, A2, B1, B2):
    assert GA.eq(dag(X), X) and GA.eq(M(X, X), ONE)
assert all(GA.commutes(a, b, SQ) for a in (A1, A2) for b in (B1, B2))
assert GA.anticommutes(A1, A2, SQ) and GA.anticommutes(B1, B2, SQ)
T = {(1, 1): M(A1, B1), (1, 2): M(A1, B2), (2, 1): M(A2, B1), (2, 2): M(A2, B2)}
C = GA.add(T[1, 1], T[1, 2], T[2, 1], GA.neg(T[2, 2]))
E = {k: GA.scal(F(1, 2), GA.add(ONE, t)) for k, t in T.items()}
for k in E:
    assert GA.eq(M(E[k], E[k]), E[k]) and GA.eq(dag(E[k]), E[k]), k
print('E_ij are projectors; scalar parts (rank/4):', [str(E[k].get((), 0)) for k in E])
dec = GA.sub(GA.scal(2, GA.add(E[1, 1], E[1, 2], E[2, 1], GA.neg(E[2, 2]))), GA.scal(2, ONE))
print('C = 2(E11+E12+E21-E22) - 2 :', GA.eq(C, dec))
print('commuting pairs among the E_ij:', [(a, b) for a, b in combinations(sorted(E), 2) if GA.commutes(E[a], E[b], SQ)])
print('anticommuting pairs among the terms:', [(a, b) for a, b in combinations(sorted(T), 2) if GA.anticommutes(T[a], T[b], SQ)])
C2 = M(C, C); C3 = M(C2, C)
print('C^3 = 8 C:', GA.eq(C3, GA.scal(8, C)), ' C^2 = 8 ?', GA.eq(C2, GA.scal(8, ONE)), ' C^2 =', C2)
K0 = GA.sub(ONE, GA.scal(F(1, 8), C2))
print('kernel projector 1 - C^2/8: idempotent', GA.eq(M(K0, K0), K0), 'self-adjoint', GA.eq(dag(K0), K0), 'scalar part', K0.get((), 0), ' C K0 = 0', GA.is_zero(M(C, K0)))
# the box functional
def lam(x):
    return M(GA.add(ONE, C), x).get((), F(0))
print('lambda(C) =', lam(C), ' lambda(E_ij) =', {k: str(lam(E[k])) for k in E}, ' lambda(1-E_ij) =', {k: str(lam(GA.sub(ONE, E[k]))) for k in E})
# commutant of C among rational self-adjoint elements: which rational projectors commute with C?
blades = GA.all_blades(4)
# linear system: x C - C x = 0
rows = []
for b in blades:
    x = {b: F(1)}
    z = GA.sub(M(x, C), M(C, x))
    rows.append(GA.basis_vector_of(z, blades))
print('dimension of the commutant of C:', 16 - GA.mat_rank(rows))
