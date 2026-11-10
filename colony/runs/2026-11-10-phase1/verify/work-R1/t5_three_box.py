from fractions import Fraction as F
from itertools import product
import random
from rcl import *
random.seed(7)
A = Cl([1, -1] * 3); m = A.prod
e = [A.gen(2 * k) for k in range(3)]; f = [A.gen(2 * k + 1) for k in range(3)]; p = [m(f[k], e[k]) for k in range(3)]
XA, ZA = e[0], p[0]; XB, ZB = m(e[1], p[0]), p[1]; XD, ZD = m(e[2], p[0], p[1]), p[2]
com = lambda x, y: m(x, y) == m(y, x); anti = lambda x, y: m(x, y) == sc(-1, m(y, x))
obs = lambda x: A.dag(x) == x and m(x, x) == one()
print("three pairs observables:", all(obs(x) for x in (XA, ZA, XB, ZB, XD, ZD)), " anticommute within:", anti(XA, ZA), anti(XB, ZB), anti(XD, ZD),
      " commute across:", all(com(x, y) for x in (XA, ZA) for y in (XB, ZB, XD, ZD)) and all(com(x, y) for x in (XB, ZB) for y in (XD, ZD)))
print("single twist e3 p1 vs e2 p1 commute?", com(m(e[2], p[0]), XB), " anticommute:", anti(m(e[2], p[0]), XB))
Gm = m(p[0], p[1], p[2]); print("odd under total parity:", anti(Gm, XA), anti(Gm, XB), anti(Gm, XD))
def chsh(a1, a2, b1, b2): return add(m(a1, add(b1, b2)), m(a2, sub(b1, b2)))
val = lambda rho, x: s0(m(rho, x)) / s0(rho)
ghz = m(add(one(), m(XA, XB)), add(one(), m(XA, XD)), add(one(), Gm))
print("ghz factors commute:", com(m(XA, XB), m(XA, XD)), com(m(XA, XB), Gm), com(m(XA, XD), Gm), " ghz^2 = 8 ghz:", m(ghz, ghz) == sc(8, ghz), " s.a.:", A.dag(ghz) == ghz)
print("values (CAB, CAD) at B1=B2, D1=D2:", val(ghz, chsh(XA, ZA, XB, XB)), val(ghz, chsh(XA, ZA, XD, XD)))
# random test of the trade-off with general (non-direction) observables and random states y y+
def rdir(X, Z):
    t = F(random.randint(-9, 9), random.randint(1, 9)); c = (1 - t * t) / (1 + t * t); s = 2 * t / (1 + t * t)
    return add(sc(c, X), sc(s, Z))
def rnd(k=6): return {random.randrange(64): F(random.randint(-4, 4)) for _ in range(k)}
worst = F(0)
for _ in range(400):
    A1, A2 = rdir(XA, ZA), rdir(XA, ZA); B1, B2 = rdir(XB, ZB), rdir(XB, ZB); D1, D2 = rdir(XD, ZD), rdir(XD, ZD)
    y = rnd()
    if not y: continue
    rho = m(y, A.dag(y))
    # push the state toward large values: project with a polynomial in CAB + CAD
    CAB, CAD = chsh(A1, A2, B1, B2), chsh(A1, A2, D1, D2)
    for lam in (0, 1, 2):
        if lam:
            yy = m(add(one(3), sc(lam, CAB), CAD), y); rho = m(yy, A.dag(yy))
        if s0(rho) == 0: continue
        t = val(rho, CAB) ** 2 + val(rho, CAD) ** 2; worst = max(worst, t); assert t <= 8, t
print("trade-off held on 1200 random (state, settings); largest sum of squares:", float(worst))
# near state
IB = m(XB, ZB); y = add(one(), sc(F(-1, 2), IB)); bell = m(add(one(), m(XA, XB)), sub(one(), m(ZA, ZB)))
near = m(y, bell, A.dag(y), add(one(), p[2]))
print("near: value CAB at blade settings:", val(near, chsh(XA, ZA, XB, ZB)), " s.a.:", A.dag(near) == near)
# product with a non-even state of mode 3 is not self-adjoint:
t3 = add(one(), e[2]); bad = m(y, bell, A.dag(y), t3); print("times (1+e3)/2 (odd state of mode 3): product self-adjoint?", A.dag(bad) == bad)
print("=== box functional on Cl(2,2)")
B = Cl([1, -1, 1, -1]); mm = B.prod
e1, f1, e2, f2 = (B.gen(i) for i in range(4)); p1 = mm(f1, e1); p2 = mm(f2, e2)
a = (p1, e1); b = (p2, mm(e2, p1))
C = add(mm(a[0], b[0]), mm(a[0], b[1]), mm(a[1], b[0]), sc(-1, mm(a[1], b[1])))
M = add(one(), C); lam = lambda x: s0(mm(M, x))
print("C blades:", C, " lam(1), lam(C):", lam(one()), lam(C), " integer coefficients:", all(v in (1, -1) for v in C.values()))
print("lam(x+) = lam(x) on blades:", all(lam(B.dag({bb: F(1)})) == lam({bb: F(1)}) for bb in range(16)))
okp = True
for i, j in product(range(2), repeat=2):
    pr = {}
    for sa, sb in product((1, -1), repeat=2):
        pr[(sa, sb)] = lam(mm(sc(F(1, 2), add(one(), sc(sa, a[i]))), sc(F(1, 2), add(one(), sc(sb, b[j])))))
    okp &= all(v >= 0 for v in pr.values()) and sum(pr.values()) == 1 and pr[(1, 1)] + pr[(1, -1)] == F(1, 2) and pr[(1, 1)] + pr[(-1, 1)] == F(1, 2)
    print("  setting", i, j, sorted(pr.items()))
print("probabilities non-negative, normalised, marginals 1/2:", okp)
Kk = sc(-1, mm(a[0], a[1], b[0], b[1]))
print("lam((C-t)^2), t=0..8:", [lam(mm(sub(C, one(t)), sub(C, one(t)))) if t else lam(mm(C, C)) for t in range(9)], " lam((1-K)^2):", lam(mm(sub(one(), Kk), sub(one(), Kk))))
# signature of the form (x,y) -> lam(x y+) on the 16-dim algebra: count negative directions exactly (LDL^T over Q)
G = [[lam(mm({i: F(1)}, B.dag({j: F(1)}))) for j in range(16)] for i in range(16)]
print("Gram symmetric:", all(G[i][j] == G[j][i] for i in range(16) for j in range(16)))
# eigenvalues: G = <(1+C) e_i e_j^+>. Use numeric eigen via simple Jacobi? do exact inertia by Sylvester with pivoting on a perturbation-free congruence
import copy
def inertia(Mx):
    Mx = [row[:] for row in Mx]; n = len(Mx); pos = neg = zero = 0; idx = list(range(n))
    while idx:
        # find nonzero diagonal
        d = next((i for i in idx if Mx[i][i] != 0), None)
        if d is None:
            # find off-diagonal nonzero
            pr = next(((i, j) for i in idx for j in idx if i < j and Mx[i][j] != 0), None)
            if pr is None: zero += len(idx); break
            i, j = pr
            # add row/col j to i
            for k in range(n): Mx[i][k] += Mx[j][k]
            for k in range(n): Mx[k][i] += Mx[k][j]
            continue
        piv = Mx[d][d]
        if piv > 0: pos += 1
        else: neg += 1
        idx.remove(d)
        for i in idx:
            fct = Mx[i][d] / piv
            if fct:
                for k in range(n): Mx[i][k] -= fct * Mx[d][k]
                for k in range(n): Mx[k][i] -= fct * Mx[k][d]
    return pos, neg, zero
print("inertia (pos, neg, zero) of x -> lam(x x+):", inertia(G))
# an element inside ONE setting pair's algebra can't be negative; a simple negative element other than (C-t):
x = sub(add(mm(a[0], b[0]), mm(a[1], b[1])), one(0)); 
for name, x in [("A1B1 - A2B2 - 2", sub(sub(mm(a[0], b[0]), mm(a[1], b[1])), one(2))), ("A1B1 + A1B2 - 2", sub(add(mm(a[0], b[0]), mm(a[0], b[1])), one(2))), ("A1B1+A2B1-2", sub(add(mm(a[0], b[0]), mm(a[1], b[0])), one(2)))]:
    print("  lam(x x+) for x =", name, ":", lam(mm(x, B.dag(x))))
print("=== three-mode anticommutator example")
Pp = sc(F(1, 2), add(one(), p[2])); Pm = sc(F(1, 2), sub(one(), p[2]))
a1 = p[0]; a2 = add(m(e[0], Pp), m(p[0], Pm)); b1 = p[1]; b2 = m(e[1], p[0])
print("observables:", all(obs(x) for x in (a1, a2, b1, b2)), " commute:", all(com(x, y) for x in (a1, a2) for y in (b1, b2)), " {A1,A2'} = 1 - p3:", add(m(a1, a2), m(a2, a1)) == sub(one(), p[2]))
Cc = chsh(a1, a2, b1, b2); K3 = sc(-1, m(p[0], e[0], b1, b2)); print("C^2 = 4 + 4 K P+:", m(Cc, Cc) == add(one(4), sc(4, m(K3, Pp))))
for r in (F(1, 3), F(7, 20), F(239, 676)):
    rho = m(add(one(), K3), add(one(), p[2]), add(one(), sc(r, Cc))); ac = sub(one(), p[2])
    # positivity sample
    okk = all(s0(m(rho, xx, A.dag(xx))) >= 0 for xx in [rnd() for _ in range(200)])
    print("  r=%s: phi(1)=%s phi(C)=%s phi(C^2)=%s phi(ac^2)=%s positive on 200 random xx+: %s" % (r, s0(rho), s0(m(rho, Cc)), s0(m(rho, Cc, Cc)), s0(m(rho, ac, ac)), okk))
