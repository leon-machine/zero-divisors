"""Polynomial first-order fields on flat spacetime, exact (gtg.Jet of infinite order as a polynomial ring)."""
import sys, os
LAB = "/home/claude/zero-divisors"
sys.path.insert(0, os.path.join(LAB, "lib"))
from fractions import Fraction as F
import GA, gtg

D = 4
ETA = [1, -1, -1, -1]
J = gtg.Jet
X = [J.var(i, 0, D, None) for i in range(D)]      # t, x, y, z as exact polynomials
ZJ = J.const(0, D)
ONE = J.const(1, D)


def jc(v):
    return v if isinstance(v, J) else J.const(v, D)


def zeros():
    return [[ZJ for _ in range(D)] for _ in range(D)]


def pm_add(A, B, c=1):
    return [[A[m][k] + B[m][k] * c for k in range(D)] for m in range(D)]


def pm_scal(c, A):
    return [[A[m][k] * c for k in range(D)] for m in range(D)]


def ptrace(H):
    out = ZJ
    for a in range(D):
        out = out + H[a][a] * ETA[a]
    return out


def ppair(A, B):
    out = ZJ
    for a in range(D):
        for k in range(D):
            out = out + A[a][k] * B[a][k] * (ETA[a] * ETA[k])
    return out


def papply(H, v):
    """h(v) for a vector field v (upper components)."""
    return [sum((H[m][k] * v[m] * ETA[m] for m in range(D)), ZJ) for k in range(D)]


def grad(f):
    return [f.d(mu) * ETA[mu] for mu in range(D)]


def pdiv(H):
    """d = h(grad), derivative on h: d^k = sum_mu d_mu H[mu][k]."""
    return [sum((H[mu][k].d(mu) for mu in range(D)), ZJ) for k in range(D)]


def vdiv(v):
    return sum((v[mu].d(mu) for mu in range(D)), ZJ)


def vadd(u, v, c=1):
    return [u[k] + v[k] * c for k in range(D)]


def vscal(c, u):
    return [u[k] * c for k in range(D)]


def vdot(u, v):
    return sum((u[k] * v[k] * ETA[k] for k in range(D)), ZJ)


def pomega(H1, H2):
    """the symplectic current of R1 clause (i), a vector field."""
    t1, t2 = ptrace(H1), ptrace(H2)
    d1, d2 = pdiv(H1), pdiv(H2)
    g1_, g2_ = grad(t1), grad(t2)
    out = []
    first = []
    for mu in range(D):
        a = ZJ
        for m in range(D):
            for k in range(D):
                a = a + (H1[m][k].d(mu) * H2[m][k] - H1[m][k] * H2[m][k].d(mu)) * (ETA[m] * ETA[k])
        first.append(a * (F(1, 2) * ETA[mu]))
    w = first
    w = vadd(w, vadd(papply(H2, g1_), papply(H1, g2_), -1), F(1, 2))
    w = vadd(w, vadd(vscal(t2, d1), vscal(t1, d2), -1), F(1, 2))
    w = vadd(w, vadd(papply(H1, d2), papply(H2, d1), -1))
    w = vadd(w, vadd(vscal(t2, g1_), vscal(t1, g2_), -1), F(-1, 2))
    return w


def box(f):
    return sum((f.d(mu).d(mu) * ETA[mu] for mu in range(D)), ZJ)


def peinstein(H):
    """E[h](a) = 1/2 (box h(a) + (a.grad) grad tau - (a.grad) d - grad(a.d)) - 1/2 a (box tau - div d), as a matrix."""
    t, d = ptrace(H), pdiv(H)
    s = box(t) - vdiv(d)
    out = zeros()
    for m in range(D):
        for k in range(D):
            x = box(H[m][k]) + t.d(m).d(k) * (ETA[m] * ETA[k]) - d[k].d(m) * ETA[m] - d[m].d(k) * ETA[k]
            if m == k:
                x = x - s * ETA[m]
            out[m][k] = x * F(1, 2)
    return out


def displacement(xi):
    """D_xi(a) = a.grad xi + grad(xi.a): matrix M[m][k] = eta_m d_m xi^k + eta_k d_k xi^m."""
    return [[xi[k].d(m) * ETA[m] + xi[m].d(k) * ETA[k] for k in range(D)] for m in range(D)]


def lie(xi, H):
    """Lie derivative of the symmetric field along xi: (L h)^{mk} = xi.grad h^{mk} - h^{ak} d_a xi^m - h^{ma} d_a xi^k."""
    out = zeros()
    for m in range(D):
        for k in range(D):
            x = sum((xi[a] * H[m][k].d(a) for a in range(D)), ZJ)
            x = x - sum((H[a][k] * xi[m].d(a) + H[m][a] * xi[k].d(a) for a in range(D)), ZJ)
            out[m][k] = x
    return out


def bwedge(u, v):
    return {(i, j): u[i] * v[j] - u[j] * v[i] for i in range(D) for j in range(i + 1, D)}


def badd(A, B, c=1):
    return {b: A[b] + B[b] * c for b in A}


def superpotential(H, xi):
    """K_xi[h] = xi ^ (d - grad tau) - grad ^ h(xi) [on h] + grad ^ h(xi) [on xi] - 1/2 tau grad ^ xi."""
    t, d = ptrace(H), pdiv(H)
    K = bwedge(xi, vadd(d, grad(t), -1))
    for mu in range(D):
        emu = [ONE * ETA[mu] if k == mu else ZJ for k in range(D)]
        dH = [[H[m][k].d(mu) for k in range(D)] for m in range(D)]
        K = badd(K, bwedge(emu, papply(dH, xi)), -1)
        K = badd(K, bwedge(emu, papply(H, [xi[k].d(mu) for k in range(D)])))
        K = badd(K, bwedge(emu, [xi[k].d(mu) for k in range(D)]), t * F(-1, 2))
    return K


def bdiv(K):
    """grad . K: (grad.K)^j = sum_i d_i K^{ij}."""
    def comp(i, j):
        if i < j:
            return K[(i, j)]
        if i > j:
            return K[(j, i)] * (-1)
        return ZJ
    return [sum((comp(i, j).d(i) for i in range(D)), ZJ) for j in range(D)]


def peval(f, pt):
    out = F(0)
    for e, c in f.c.items():
        term = c
        for i in range(D):
            term = term * F(pt[i]) ** e[i]
        out += term
    return out


def subst_N(f):
    """restrict to the null plane n.x = 0: t = z = lam; returns {(a, b, c): coeff} in (lam, x, y)."""
    out = {}
    for e, c in f.c.items():
        key = (e[0] + e[3], e[1], e[2])
        out[key] = out.get(key, F(0)) + c
    return {k: v for k, v in out.items() if v}


def integrate3(P, lo, hi):
    """exact integral of a polynomial {(a,b,c): coeff} over a box."""
    tot = F(0)
    for e, c in P.items():
        term = c
        for i in range(3):
            n = e[i] + 1
            term = term * (F(hi[i]) ** n - F(lo[i]) ** n) * F(1, n)
        tot += term
    return tot


def integrate2(P, fix, lo, hi):
    """integral over the two remaining variables with variable index fix[0] set to fix[1]."""
    i0, val = fix
    rest = [i for i in range(3) if i != i0]
    tot = F(0)
    for e, c in P.items():
        term = c * F(val) ** e[i0]
        for j, i in enumerate(rest):
            n = e[i] + 1
            term = term * (F(hi[j]) ** n - F(lo[j]) ** n) * F(1, n)
        tot += term
    return tot
