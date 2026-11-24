"""R2: clause (iv) by a matrix route. m(x)_ij from s_i^dag x s_j = m_ij P0 (GA products), then everything with
4x4 Fraction matrices: Clifford relations, <x>_0 = tr m(x)/4 on all blades, the CHSH element, lambda on atoms."""
import sys; sys.path.insert(0, "/home/claude/zero-divisors/lib")
import GA
from fractions import Fraction as F
from itertools import combinations
SQ = (1, -1, 1, -1)
def clean(x): return {b: c for b, c in x.items() if c != 0}
def P(*xs):
    r = GA.sc(F(1))
    for x in xs: r = GA.mul(r, x, SQ)
    return clean(r)
def dag(x):
    out = {}
    for b, c in x.items():
        g = len(b); s = (-1) ** (g*(g-1)//2)
        for i in b: s *= SQ[i]
        out[b] = c * s
    return out
def L(*t):
    r = {}
    for c, x in t: r = GA.add(r, GA.scal(F(c), x))
    return clean(r)
e = [GA.gen(0), GA.gen(2)]; f = [GA.gen(1), GA.gen(3)]
v = [L((F(1,2), e[j]), (F(1,2), f[j])) for j in range(2)]; w = [L((F(1,2), e[j]), (F(-1,2), f[j])) for j in range(2)]
p0 = P(w[0], v[0], w[1], v[1]); s = [p0, P(v[0], p0), P(v[1], p0), P(v[0], v[1], p0)]
def m(x):
    M = [[F(0)]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            y = P(dag(s[i]), x, s[j]); c = y.get((), F(0)) * 4
            assert clean(y) == clean(GA.scal(c, p0)); M[i][j] = c
    return M
def mm(A, B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def add(A, B, c=1): return [[A[i][j] + c*B[i][j] for j in range(4)] for i in range(4)]
I4 = [[F(int(i == j)) for j in range(4)] for i in range(4)]
G = [m(e[0]), m(f[0]), m(e[1]), m(f[1])]
for a in range(4):
    for b in range(4):
        anti = add(mm(G[a], G[b]), mm(G[b], G[a]))
        assert anti == [[2*SQ[a]*(a == b)*I4[i][j] for j in range(4)] for i in range(4)]
blades = [()] + [c for r in range(1, 5) for c in combinations(range(4), r)]
for bl in blades:
    x = {bl: F(1)}; Mx = I4
    for i in bl: Mx = mm(Mx, G[i])
    assert m(x) == Mx
    assert sum(Mx[i][i] for i in range(4)) / 4 == (1 if bl == () else 0)
    assert m(dag(x)) == [[Mx[j][i] for j in range(4)] for i in range(4)]
print("matrix rep: Clifford relations, m multiplicative on blades, dagger=transpose, <x>_0 = tr/4: OK")
A1, A2, B1, B2 = G[0], mm(G[1], G[0]), mm(mm(G[2], G[1]), G[0]), mm(G[3], G[2])
C = add(add(mm(A1, B1), mm(A1, B2)), add(mm(A2, B1), mm(A2, B2), -1))
C2 = mm(C, C); C3 = mm(C2, C)
print("C symmetric:", C == [[C[j][i] for j in range(4)] for i in range(4)], " C^3 == 8 C:", C3 == [[8*c for c in row] for row in C], " C^2 != 8:", C2 != [[8*I4[i][j] for j in range(4)] for i in range(4)], " tr C:", sum(C[i][i] for i in range(4)))
rho = [[(I4[i][j] + C[i][j]) / 4 for j in range(4)] for i in range(4)]
def lam(r): return sum(rho[i][j]*r[i]*r[j] for i in range(4) for j in range(4)) / sum(x*x for x in r)
print("lambda(1)=", sum(rho[i][i] for i in range(4)), " lambda(Pi_(1,0,0,1)) =", lam((1,0,0,1)), " lambda(Pi_(2,1,-1,2)) =", lam((2,1,-1,2)), " lambda(C) =", sum(rho[i][j]*C[j][i] for i in range(4) for j in range(4)))
