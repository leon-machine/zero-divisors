from fractions import Fraction as F
from itertools import product
from rcl import *
A = Cl([1, -1, 1, -1]); m = A.prod
e1, f1, e2, f2 = (A.gen(i) for i in range(4))
p1 = m(f1, e1); p2 = m(f2, e2); E2 = m(e2, p1); K = m(e1, f2); G = m(p1, p2)
def chsh(a1, a2, b1, b2): return add(m(a1, add(b1, b2)), m(a2, sub(b1, b2)))
v = lambda e, f: sc(F(1, 2), add(e, f)); w = lambda e, f: sc(F(1, 2), sub(e, f))
v1, w1, v2, w2 = v(e1, f1), w(e1, f1), v(e2, f2), w(e2, f2)
def pair(r, cs):  # stored pair state: 1/4 (1+p1p2)(1+r p1) + cs (w1w2 + v2v1)
    return add(sc(F(1, 4), m(add(one(), G), add(one(), sc(r, p1)))), sc(cs, add(m(w1, w2), m(v2, v1))))
print("=== parity (iv): equal-weight pair state")
rho = pair(0, F(1, 2))
print("rho^2=rho, s.a., even:", m(rho, rho) == rho, A.dag(rho) == rho, m(G, rho) == m(rho, G), " <rho>_0 =", s0(rho))
phi = lambda x: 4 * s0(m(rho, x))
print("corr p1p2, e1E2, p1E2, e1p2:", phi(m(p1, p2)), phi(m(e1, E2)), phi(m(p1, E2)), phi(m(e1, p2)))
for c, s in [(F(3, 5), F(4, 5)), (F(20, 29), F(21, 29)), (F(119, 169), F(120, 169))]:
    Bp = add(sc(c, p2), sc(s, E2)); Bm = sub(sc(c, p2), sc(s, E2))
    print("  directions (c,s)=", c, s, " CHSH(p1,e1;B+,B-) =", phi(chsh(p1, e1, Bp, Bm)), " 2(c+s) =", 2 * (c + s))
print("=== stored pair state with AMPLITUDES (3/5,4/5): r=-7/25, cs=12/25")
rho2 = pair(F(-7, 25), F(12, 25)); phi2 = lambda x: 4 * s0(m(rho2, x))
print("pure:", m(rho2, rho2) == rho2, " corr p1p2, e1E2, p1E2, e1p2:", phi2(m(p1, p2)), phi2(m(e1, E2)), phi2(m(p1, E2)), phi2(m(e1, p2)))
# full correlation matrix T_ij = phi(a_i b_j), a in {e1,p1}, b in {E2,p2}; max CHSH = 2 sqrt(t1^2+t2^2) (sing. values)
print("  -> max over plane directions: 2 sqrt(1 + (2cs)^2) = 2 sqrt(1+576/625) =", 2 * (1 + 576 / 625) ** .5, " vs 2(c+s)=14/5 =", 2.8)
x, z = F(20, 29), F(21, 29)
Bp = add(sc(z, p2), sc(x, E2)); Bm = sub(sc(z, p2), sc(x, E2))
S = phi2(chsh(p1, e1, Bp, Bm)); print("  S at (x,z)=(20/29,21/29):", S, " 8-S^2 =", 8 - S * S, " 4r^2 =", 4 * F(49, 625))
print("=== which states give 14/5 at the BLADE settings (e1,p1;E2,p2)?")
C0 = chsh(e1, p1, E2, p2)
I = m(E2, p2); Cp = m(C0, I)
print("I^2:", m(I, I), " I+=-I:", A.dag(I) == sc(-1, I), " IC=-CI:", m(I, C0) == sc(-1, m(C0, I)), " Cperp s.a.:", A.dag(Cp) == Cp, " Cperp = A2(B1+B2)-A1(B1-B2):", Cp == sub(m(p1, add(E2, p2)), m(e1, sub(E2, p2))))
PK = sc(F(1, 2), add(one(), K))
def rhoXY(X, Y): return add(sc(F(1, 2), PK), sc(F(1, 16), add(sc(X, C0), sc(Y, Cp))))
def pure(r): return m(r, r) == r and A.dag(r) == r and all(m(r, {b: F(1)}, r) == sc(4 * s0(m(r, {b: F(1)})), r) for b in range(16))
for X, Y in [(F(2), F(-2)), (F(14, 5), F(2, 5)), (F(14, 5), F(-2, 5)), (F(82, 29), F(2, 29)), (F(478, 169), F(-2, 169))]:
    r = rhoXY(X, Y); print("  rho_{%s,%s}: pure=%s value C=%s Cperp=%s even=%s" % (X, Y, pure(r), 4 * s0(m(r, C0)), 4 * s0(m(r, Cp)), m(G, r) == m(r, G)))
print("  non-circle point (1,1) idempotent?", m(rhoXY(1, 1), rhoXY(1, 1)) == rhoXY(1, 1))
rho0 = sc(F(1, 4), m(add(one(), m(e1, E2)), sub(one(), m(p1, p2))))
print("rho0 = rho_{2,-2}:", rho0 == rhoXY(2, -2), " even:", m(G, rho0) == m(rho0, G))
for u in [F(0), F(-1, 2), F(-2, 5), F(-5, 12), F(1, 3), F(7, 4)]:
    y = add(one(), sc(u, I)); ru = sc(1 / (1 + u * u), m(y, rho0, A.dag(y)))
    c = (1 - u * u) / (1 + u * u); s = 2 * u / (1 + u * u)
    b1 = add(sc(c, E2), sc(s, p2)); b2 = sub(sc(c, p2), sc(s, E2))
    print("  u=%s: rho_u == rho_{2(c-s),-2(c+s)}: %s ; value %s ; closed form %s ; turned-direction value on rho0: %s" % (u, ru == rhoXY(2 * (c - s), -2 * (c + s)), 4 * s0(m(ru, C0)), 2 * (1 - 2 * u - u * u) / (1 + u * u), 4 * s0(m(rho0, chsh(e1, p1, b1, b2)))))
rinf = m(I, rho0, A.dag(I)); print("rho_inf = rho_{-2,2}:", rinf == rhoXY(-2, 2), " = stored pair state r=0, cs=-1/2:", rinf == pair(0, F(-1, 2)), "; parity-proposal state (cs=+1/2) in sector K=+1?", m(K, pair(0, F(1, 2))) == pair(0, F(1, 2)), " K rho = -rho?", m(K, pair(0, F(1, 2))) == sc(-1, pair(0, F(1, 2))))
print("Gamma rho_{X,Y} Gamma = rho_{-Y,-X}:", m(G, rhoXY(F(14, 5), F(2, 5)), G) == rhoXY(F(-2, 5), F(-14, 5)))
# corner dimension: P_K b P_K
import itertools
vecs = [m(PK, {b: F(1)}, PK) for b in range(16)]
def rank(vs):
    rows = [[v_.get(b, F(0)) for b in range(16)] for v_ in vs]; r = 0
    for c in range(16):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                fct = rows[i][c] / rows[r][c]; rows[i] = [a - fct * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r
print("corner dim:", rank(vecs), " basis rank:", rank([PK, C0, m(I, PK), Cp]))
print("=== Pell / denominator law")
from math import gcd
bad = 0; eq = []
for Q in range(1, 601):
    for P in range(0, 3 * Q):
        if gcd(P, Q) != 1 or P * P >= 8 * Q * Q: continue
        d = 8 * Q * Q - P * P
        if d < 4: bad += 1
        if d == 4: eq.append((P, Q))
print("violations:", bad, " equality cases Q<=600:", eq, " all Pell:", all(P % 2 == 0 and (P // 2) ** 2 - 2 * Q * Q == -1 for P, Q in eq))
# records: best value at each denominator bound
best = F(0); rec = []
for Q in range(1, 200):
    for P in range(0, 3 * Q):
        if P * P < 8 * Q * Q and F(P, Q) > best and F(P, Q).denominator == Q:
            best = F(P, Q); rec.append(best)
print("running records of P/Q < 2sqrt2 by increasing denominator:", [str(r) for r in rec])
