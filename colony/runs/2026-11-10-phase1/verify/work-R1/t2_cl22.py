from fractions import Fraction as F
from itertools import product
from rcl import *
# modes: e1=0,f1=1,e2=2,f2=3 ; sq +,-,+,-
A = Cl([1, -1, 1, -1]); m = A.prod
e1, f1, e2, f2 = (A.gen(i) for i in range(4))
p1 = m(f1, e1); p2 = m(f2, e2)
def chsh(a1, a2, b1, b2): return add(m(a1, add(b1, b2)), m(a2, sub(b1, b2)))
def val(rho, x): return s0(m(rho, x)) / s0(rho)
print("dagger: e1", A.dag(e1) == e1, "f1 -> -f1", A.dag(f1) == sc(-1, f1), "p1", A.dag(p1) == p1)
# anti-automorphism on random elements
import random
random.seed(1)
def rnd(): return {b: F(random.randint(-3, 3)) for b in range(16) if random.random() < .6}
ok = all(A.dag(m(x, y)) == m(A.dag(y), A.dag(x)) for x, y in [(rnd(), rnd()) for _ in range(50)])
print("anti-automorphism (50 random pairs):", ok)
x = rnd(); print("<x x+>_0 = sum squares:", s0(m(x, A.dag(x))) == sum(v * v for v in x.values()))
# (iii) the 17/8 example
Aa = add(sc(F(17, 8), e1), sc(F(15, 8), f1))
print("A^2=1:", m(Aa, Aa) == one(), "A+ != A:", A.dag(Aa) != Aa, "commutes with p2:", m(Aa, p2) == m(p2, Aa))
rho = sc(F(1, 4), m(add(one(), e1), add(one(), p2)))
Cc = chsh(Aa, Aa, p2, p2)
print("rho idempotent s.a.:", m(rho, rho) == rho, A.dag(rho) == rho, " value:", val(rho, Cc), " C^2:", m(Cc, Cc))
# is rho a state on xx+? rho = rho rho+ so yes. Value of A itself:
print("omega(A) =", val(rho, Aa), " omega(A A+) =", val(rho, m(Aa, A.dag(Aa))))
# (iv) twisted directions
E2 = m(e2, p1); K = m(e1, f2)
print("E2 s.a., sq 1:", A.dag(E2) == E2, m(E2, E2) == one(), " commutes with e1,f1:", m(E2, e1) == m(e1, E2), m(E2, f1) == m(f1, E2), " anticomm p2:", m(E2, p2) == sc(-1, m(p2, E2)))
print("K+ = K, K^2:", A.dag(K) == K, m(K, K) == one())
C0 = chsh(e1, p1, E2, p2)
print("C0 =", C0, " expected e2f1 + e1p2 + e2 - p1p2:", C0 == add(m(e2, f1), m(e1, p2), e2, sc(-1, m(p1, p2))))
print("C0^2 = 4(1+K):", m(C0, C0) == sc(4, add(one(), K)), " KC=C:", m(K, C0) == C0, " C^3=8C:", m(C0, C0, C0) == sc(8, C0))
# general directions symbolic via bilinearity: check on a degree argument -> test with independent rational points incl. generic
pts = [(F(3, 5), F(4, 5)), (F(-7, 25), F(24, 25)), (F(20, 29), F(-21, 29)), (F(1), F(0)), (F(0), F(-1)), (F(11, 61), F(60, 61))]
ok = True
for a1, a2, b1, b2 in product(pts, repeat=4):
    A1 = add(sc(a1[0], e1), sc(a1[1], p1)); A2 = add(sc(a2[0], e1), sc(a2[1], p1))
    B1 = add(sc(b1[0], E2), sc(b1[1], p2)); B2 = add(sc(b2[0], E2), sc(b2[1], p2))
    wa = a1[0] * a2[1] - a1[1] * a2[0]; wb = b1[0] * b2[1] - b1[1] * b2[0]
    Cg = chsh(A1, A2, B1, B2)
    ok &= m(Cg, Cg) == add(one(4), sc(4 * wa * wb, K))
print("C^2 = 4 + 4 wa wb K on 1296 quadruples (own points):", ok)
# sign check with non-unit coefficients (bilinear in each of 4 slots): basis test = full proof
basisA = [e1, p1]; basisB = [E2, p2]
def wedge(u, v): return u[0] * v[1] - u[1] * v[0]
okb = True
for i, j, k, l in product(range(2), repeat=4):
    # [A_i,A_j][B_k,B_l] = -4 w w K ?
    X = sub(m(basisA[i], basisA[j]), m(basisA[j], basisA[i])); Y = sub(m(basisB[k], basisB[l]), m(basisB[l], basisB[k]))
    ui = [(1, 0), (0, 1)]
    okb &= m(X, Y) == sc(-4 * wedge(ui[i], ui[j]) * wedge(ui[k], ui[l]), K)
print("XY = -4 wa wb K on the basis (bilinear => all directions):", okb)
# parity average
G = m(p1, p2)
d = add(sc(F(3, 5), E2), sc(F(4, 5), p2)); print("parity average of direction:", sc(F(1, 2), add(d, m(G, d, G))))
# P over Q(sqrt2): represent as pairs
def m2(x, y): return (add(m(x[0], y[0]), sc(2, m(x[1], y[1]))), add(m(x[0], y[1]), m(x[1], y[0])))
P = (sc(F(1, 4), add(one(), K)), sc(F(1, 8), C0))
print("P^2=P:", m2(P, P) == P, " CP = 2 sqrt2 P:", m2((C0, {}), P) == (sc(4, P[1]), sc(2, P[0])))
rk = True
for b in range(16):
    xb = ({b: F(1)}, {}); Px = m2(P, xb); t = (one(4 * s0(Px[0])), one(4 * s0(Px[1])))
    rk &= m2(Px, P) == m2(t, P)
print("PxP = 4<Px>P on blades:", rk)
print("P commutes with total parity? rational part", m(G, P[0]) == m(P[0], G), " sqrt2 part", m(G, P[1]) == m(P[1], G))
print("mode-2 projection of sqrt2 part:", {b: c for b, c in P[1].items() if b & 0b0011 == 0})
# 1 - P = -(1/16)(C-2r2)(C+4r2)
D = (C0, one(-2)); G2 = (C0, one(4))
lhs = (sub(one(), P[0]), sc(-1, P[1])); pr = m2(D, G2)
print("1-P = -(1/16)(C-2s)(C+4s):", lhs == (sc(F(-1, 16), pr[0]), sc(F(-1, 16), pr[1])))
# near state from proposal's check: y = (14/5 + C)(1+K), value 280/99 ?
y = m(add(one(F(14, 5)), C0), add(one(), K)); rr = m(y, A.dag(y)); print("near-state value:", val(rr, C0))
