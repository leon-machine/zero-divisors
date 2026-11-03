"""Gauge Theory Gravity's pair (hb, Omega) and the frozen point as the I-preserving Cl(2,4) connections;
the Omega-equation of the frozen-point functional is the torsion equation. Exact checks.

Cl(2,4) with generators e0 (+1), e1, e2, e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-
(n0 . ninf = 1); W = span(e0, ..., e3), the physical vectors. For rho rational, I = ninf + rho n0
(Q(I) = 2 rho = Lambda/3 with Lambda = 6 rho) and u = ninf - rho n0 (Q(u) = -2 rho, u . I = 0).
The physical frame E(a) = hb^{-1}(a) is a W-valued one-form, Omega a Lambda^2 W-valued one-form.
  Phi(E, Omega)(a) = Omega(a) - u ^ E(a) = Omega(a) - ninf ^ E(a) + rho n0 ^ E(a).
(2) Bijection (clause (ii)): {B : B x I = 0} has dimension 10 = 6 + 4 and is Lambda^2 W + u ^ W, uniquely; at rho = 0
    the u ^ W block is abelian (iso(1,3), GTG's Poincare algebra), else [u^a, u^b] = 2 rho a ^ b.
    Rotation-gauge equivariance under rational rotors of W (which fix n0 and ninf); the vectors annihilated
    by all of Lambda^2 W + u ^ W form the line of I.
(2') Field strength of Phi(E, Omega) from first jets at a point: F = R(Omega) + 2 rho E ^ E - u ^ T,
    T the torsion D ^ E; F x I = 0.
(1) The Omega-equation (clause (i)) of eps(I, V, F, F) sees only the torsion block: eps(I, w, B, C) = 0 for w in W and
    B, C in Lambda^2 W; the linear map torsion -> Omega-equation is invertible (rank 24) at a generic
    frame, so on torsion-free fields the Omega-equation holds identically.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as Fr
from itertools import combinations, permutations

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E6 = [GA.gen(i) for i in range(6)]
N0 = GA.scal(Fr(1, 2), GA.add(E6[4], E6[5]))
NI = GA.sub(E6[4], E6[5])
W = E6[:4]
BIV = [GA.mul(E6[i], E6[j], S) for i, j in combinations(range(6), 2)]
L2W = [GA.mul(W[a], W[b], S) for a, b in combinations(range(4), 2)]
RHOS = (Fr(0), Fr(1, 2), Fr(-1, 2), Fr(3, 14))


def mul(x, y):
    return GA.mul(x, y, S)


I6 = mul(mul(mul(E6[0], E6[1]), mul(E6[2], E6[3])), mul(E6[4], E6[5]))


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def wedge(x, y, r, s):
    return grade(mul(x, y), r + s)


def comm(x, y):
    return GA.scal(Fr(1, 2), GA.sub(mul(x, y), mul(y, x)))


def sc(x):
    return x.get((), Fr(0))


def vec(c):
    return GA.add(*[GA.scal(Fr(c[i]), W[i]) for i in range(4) if c[i]])


def bivw(c):
    return GA.add(*[GA.scal(Fr(c[i]), L2W[i]) for i in range(6) if c[i]])


def eps(a, b, F, G):
    """coefficient of i6 in a ^ b ^ F ^ G (a, b vectors; F, G bivectors)."""
    top = wedge(wedge(wedge(a, b, 1, 1), F, 2, 2), G, 4, 2)
    return sc(mul(top, GA.reverse(I6))) / sc(mul(I6, GA.reverse(I6)))


def flatten(xs):
    blades = sorted({b for x in xs for b in x})
    return [[x.get(b, Fr(0)) for b in blades] for x in xs]


def rank(xs):
    xs = [x for x in xs]
    return GA.rank_of_vectors(flatten(xs)) if xs else 0


def nullspace(rows, n):
    piv = {}
    for r in rows:
        r = list(r)
        for c, pr in piv.items():
            if r[c] != 0:
                f = r[c]
                r = [a - f * b for a, b in zip(r, pr)]
        c0 = next((c for c in range(n) if r[c] != 0), None)
        if c0 is None:
            continue
        p = r[c0]
        r = [a / p for a in r]
        for c, pr in list(piv.items()):
            if pr[c0] != 0:
                f = pr[c0]
                piv[c] = [a - f * b for a, b in zip(pr, r)]
        piv[c0] = r
    out = []
    for fc in [c for c in range(n) if c not in piv]:
        x = [Fr(0)] * n
        x[fc] = Fr(1)
        for c, pr in piv.items():
            x[c] = -pr[fc]
        out.append(x)
    return out


def lin_rows(images):
    """rows of the linear system 'sum_k x_k images[k] = 0' (one row per blade)."""
    blades = sorted({b for im in images for b in im})
    return [[im.get(b, Fr(0)) for im in images] for b in blades]


def tractors(rho):
    I = GA.add(NI, GA.scal(rho, N0))
    u = GA.sub(NI, GA.scal(rho, N0))
    return I, u


def phi(u, Evec, Om):
    return GA.sub(Om, wedge(u, Evec, 1, 1))


def _premises_definition():
    # the chart (n0, ninf), the GTG pair and its gauge laws as set up for the tractor gauge field
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")


def check_gtg_pair_is_bijective_with_connections_preserving_i():
    _premises_definition()
    ok = True
    for rho in RHOS:
        I, u = tractors(rho)
        ok = ok and sc(mul(I, I)) == 2 * rho and sc(mul(u, u)) == -2 * rho and GA.dot(u, I, S) == 0
        stab = nullspace(lin_rows([comm(b, I) for b in BIV]), 15)
        ok = ok and len(stab) == 10
        trans = [wedge(u, w, 1, 1) for w in W]
        parts = L2W + trans
        ok = ok and all(GA.is_zero(comm(p, I)) for p in parts)
        ok = ok and rank(parts) == 10
        for a, b in combinations(range(4), 2):
            br = comm(trans[a], trans[b])
            ok = ok and GA.eq(br, GA.scal(2 * rho, wedge(W[a], W[b], 1, 1)))
        if rho == 0:
            ok = ok and all(GA.is_zero(comm(trans[a], trans[b])) for a in range(4) for b in range(4))
        # the vectors annihilated by every value (Lambda^2 W and u ^ W) form exactly the line of I
        rows = []
        for p in parts:
            rows.extend(lin_rows([comm(p, v) for v in E6]))
        ker = nullspace(rows, 6)
        ok = ok and len(ker) == 1
        J = GA.add(*[GA.scal(c, E6[i]) for i, c in enumerate(ker[0]) if c])
        ok = ok and rank([J, I]) == 1
    rho = Fr(3, 14)
    I, u = tractors(rho)
    rotors = [GA.add(GA.sc(Fr(5, 4)), GA.scal(Fr(3, 4), mul(W[0], W[1]))),
              GA.add(GA.sc(Fr(3, 5)), GA.scal(Fr(4, 5), mul(W[1], W[2]))),
              GA.add(GA.sc(Fr(13, 12)), GA.scal(Fr(5, 12), mul(W[0], W[3])))]
    Evec = vec([2, -1, 3, 5])
    Om = bivw([1, -2, 0, 3, 7, -1])
    for U in rotors:
        Ur = GA.reverse(U)
        ok = ok and GA.eq(mul(U, Ur), GA.sc(1))
        ok = ok and GA.eq(mul(mul(U, N0), Ur), N0) and GA.eq(mul(mul(U, NI), Ur), NI)
        lhs = mul(mul(U, phi(u, Evec, Om)), Ur)
        rhs = phi(u, mul(mul(U, Evec), Ur), mul(mul(U, Om), Ur))
        ok = ok and GA.eq(lhs, rhs)
    GA.check("GTG pairs (E, Omega) <-> Lambda^2(I^perp)-valued one-forms, 10 = 6 + 4, equivariant; rho = 0 is iso(1,3)", ok)
    assert ok
    return ok


def _jets():
    """first jets at a point of a GTG pair: E[mu], dE[nu][mu], Om[mu], dOm[nu][mu]."""
    E = [vec([2, 1, 0, -1]), vec([0, 3, 1, 1]), vec([1, 0, -2, 1]), vec([-1, 1, 1, 4])]
    dE = [[vec([(3 * n + m) % 5 - 2, (n * m) % 3 - 1, (n + 2 * m) % 4 - 1, (n - m) % 3])
           for m in range(4)] for n in range(4)]
    Om = [bivw([1, 0, -1, 2, 0, 1]), bivw([0, 2, 1, -1, 1, 0]),
          bivw([3, -1, 0, 0, 2, 1]), bivw([-1, 1, 1, 1, 0, -2])]
    dOm = [[bivw([(n + m) % 3 - 1, (2 * n + m) % 5 - 2, (n * m) % 4 - 1, (n - 2 * m) % 3, (m + 1) % 2,
                  (3 * n + m) % 4 - 2]) for m in range(4)] for n in range(4)]
    return E, dE, Om, dOm


def check_field_strength_splits_into_shifted_curvature_and_torsion():
    _premises_definition()
    E, dE, Om, dOm = _jets()
    ok = True
    for rho in RHOS:
        I, u = tractors(rho)
        A = [phi(u, E[m], Om[m]) for m in range(4)]
        dA = [[phi(u, dE[n][m], dOm[n][m]) for m in range(4)] for n in range(4)]
        for m, n in combinations(range(4), 2):
            F = GA.add(GA.sub(dA[m][n], dA[n][m]), comm(A[m], A[n]))
            R = GA.add(GA.sub(dOm[m][n], dOm[n][m]), comm(Om[m], Om[n]))
            T = GA.add(GA.sub(dE[m][n], dE[n][m]), comm(Om[m], E[n]), GA.neg(comm(Om[n], E[m])))
            pred = GA.add(R, GA.scal(2 * rho, wedge(E[m], E[n], 1, 1)), GA.neg(wedge(u, T, 1, 1)))
            ok = ok and GA.eq(F, pred) and GA.is_zero(comm(F, I))
            ok = ok and not GA.is_zero(T)
    GA.check("F = R(Omega) + 2 rho E^E - u^T, valued in Lambda^2(I^perp), for rho in {0, 1/2, -1/2, 3/14}", ok)
    assert ok
    return ok


def _levi(idx):
    p = list(idx)
    if len(set(p)) < 4:
        return 0
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s = -s
    return s


def check_omega_equation_is_the_torsion_equation():
    _premises_definition()
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("synthesis.curvature-only-tractor-actions-are-macdowell-mansouri")
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    premise("synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared")
    ok = True
    for rho in (Fr(1, 2), Fr(-1, 2), Fr(3, 14)):
        I, u = tractors(rho)
        # algebraic lemma: eps(I, w, B, C) = 0 for w in W, B, C in Lambda^2 W
        ok = ok and all(eps(I, w, B, C) == 0 for w in W for B in L2W for C in L2W)
        ok = ok and any(eps(I, w, B, wedge(u, t, 1, 1)) != 0 for w in W for B in L2W for t in W)
        # D_A V for V proportional to u: (u ^ e) x u = -Q(u) e
        ok = ok and all(GA.eq(comm(wedge(u, w, 1, 1), u), GA.scal(2 * rho, w)) for w in W)
        for frame in ([vec([1, 0, 0, 0]), vec([0, 1, 0, 0]), vec([0, 0, 1, 0]), vec([0, 0, 0, 1])],
                      _jets()[0]):
            # Omega-equation: for direction mu and b in L2W,
            # Z[mu, b] = sum_{nu, rho, sigma} levi(nu, mu, rho, sigma) eps(I, E_nu, b, F_{rho sigma}) / 2,
            # F_{rho sigma} = -u ^ T_{rho sigma}; unknown T: 6 planes x 4 components = 24
            planes = list(combinations(range(4), 2))
            cols = []
            for p_i, (r1, s1) in enumerate(planes):
                for c in range(4):
                    Fp = GA.neg(wedge(u, W[c], 1, 1))
                    col = []
                    for mu in range(4):
                        for b in L2W:
                            z = Fr(0)
                            for nu in range(4):
                                lv = _levi((nu, mu, r1, s1))
                                if lv:
                                    z += lv * eps(I, frame[nu], b, Fp)
                            col.append(z)
                    cols.append(col)
            mat = [[cols[j][i] for j in range(24)] for i in range(24)]
            ok = ok and GA.rank_of_vectors(mat) == 24
            # the Lorentz block (any values in Lambda^2 W) never enters
            for B in L2W:
                z = sum(_levi((nu, mu, 0, 1)) * eps(I, frame[nu], b, B)
                        for nu in range(4) for mu in range(4) for b in L2W)
                ok = ok and z == 0
    GA.check("Omega-equation of eps(I, V, F, F) depends on F only through its torsion block, invertibly (rank 24)", ok)
    assert ok
    return ok
