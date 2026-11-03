"""The triangle anomaly in the spacetime algebra with Pauli-Villars regulators: exact checks.

Cl(1,3), signature (+,-,-,-), generators g0..g3 (GA.gen), I4 = g0 g1 g2 g3. The Dirac matrices are the
algebra's product; the unit of the Feynman rules is a coefficient outside the product (Gaussian rationals,
the right unit of the stored convention), so the chirality element of the matrix reading is
gamma5 = i I4 with i that coefficient, and the matrix trace of X is 4 <X>_0 (checked against explicit
Dirac matrices over Q(i)). Propagator S(p) = (p + M)/(Q(p) - M^2).

Triangle with the axial vertex g^mu gamma5 (momentum q = k1 + k2 in), vector vertices g^nu (k1 out) and
g^rho (k2 out):
  D1(l) = Tr[g^mu gamma5 S(l) g^nu S(l - k1) g^rho S(l - q)]
  D2(l) = Tr[g^mu gamma5 S(l) g^rho S(l - k2) g^nu S(l - q)]
  P1, P2 the same with g^mu gamma5 replaced by gamma5.
Part 1: Tr(gamma5 abcd) = 4 i <I4 abcd>_0 = -4 i lambda, a^b^c^d = lambda I4.
Part 2: vector Ward identity integrand by integrand: k1_nu (D1 + D2)(l) = B(l - k1) - B(l).
Part 3: the two-point terms: epsilon numerator mass independent, odd about its centre, and the regulated
        denominator sum is O(|l|^-6) exactly when sum c_i = 0, so legal shifts and zero integrals.
Part 4: axial identity integrand by integrand: q_mu (D1 + D2) = -2M (P1 + P2) + two-point terms.
Part 5: the regulator term: numerator of P1, P2 is M times an l-independent constant 4 i <I4 g^nu k1 g^rho k2>_0;
        with the Fact's integral -i/(32 pi^2 Delta) and sum_{i>=1} c_i = -1 the axial divergence is
        (1/(2 pi^2)) <I4 g^nu k1 g^rho k2>_0, independent of the regulator masses and of the other weights.
Part 6: field form: <I4 a1 k1 a2 k2>_0 = <I4 f1 f2>_0, f_j = a_j ^ k_j, Bose symmetric; <I4 F^2>_0 = -2 E.B.
Part 7: chiral vertices: the three projectors collapse to one; a Weyl loop carries half the axial trace.
Part 8: the anomaly tensor d(X, Y, Z) = tr(X {Y, Z}) of one generation's left-handed content vanishes on the
        whole complexified gauge algebra sl3 + sl2 + C, and tr X = 0.
Exact arithmetic only (Fractions, Gaussian rationals).
"""
from fractions import Fraction as Fr
from itertools import product, combinations_with_replacement

import GA
from GA import QI
from tp_premise import premise

S = (1, -1, -1, -1)
G = [GA.gen(i) for i in range(4)]
GU = [GA.scal(Fr(1, S[i]), G[i]) for i in range(4)]
I4 = GA.mul(GA.mul(G[0], G[1], S), GA.mul(G[2], G[3], S), S)
PS = (0, 1, 2, 3)
IU = QI(0, 1)
GAMMA5 = {PS: IU}          # i I4, i the coefficient outside the product


def mul(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, S)
    return out


def add(*xs):
    out = {}
    for x in xs:
        for b, c in x.items():
            out[b] = out.get(b, Fr(0)) + c
    return {b: c for b, c in out.items() if c != 0}


def cscal(c, x):
    return {b: c * v for b, v in x.items() if c * v != 0}


def sc(x):
    return x.get((), Fr(0))


def tr(x):
    return 4 * sc(x)


def vec(c):
    return {(i,): Fr(c[i]) for i in range(4) if c[i] != 0}


def Q(v):
    return sc(mul(v, v))


def num(c):
    return {(): Fr(c)} if c != 0 else {}


def prop(p, M):
    return cscal(Fr(1) / (Q(p) - M * M), add(p, num(M)))


def contract(k, slot_fn):
    """sum_nu k_nu X(g^nu) for X linear in its vector slot: X(k) with k = k_nu g^nu."""
    return slot_fn(k)


def im(z):
    return z.im if isinstance(z, QI) else Fr(0)


def czero(x):
    return all(c == 0 for c in x.values()) if isinstance(x, dict) else x == 0


# sample data
K1 = vec([Fr(1, 2), Fr(1, 3), 0, Fr(-1, 4)])
K2 = vec([Fr(2, 3), 0, Fr(1, 5), Fr(1, 2)])
QV = add(K1, K2)
LOOPS = [vec([Fr(3, 2), Fr(1, 7), Fr(-2, 3), 1]), vec([Fr(-1, 3), 2, Fr(1, 2), Fr(5, 4)]),
         vec([Fr(7, 5), Fr(-3, 2), Fr(1, 9), Fr(-2, 5)])]
MASSES = [Fr(0), Fr(3, 2), Fr(5)]
VA, VB, VC, VD = vec([1, 2, -1, 3]), vec([Fr(1, 2), 0, 1, -2]), vec([2, -1, Fr(1, 3), 1]), vec([0, 1, 1, Fr(1, 2)])


# ---------------------------------------------------------------- Dirac matrices over Q(i)
Z, ONE = QI(0), QI(1)


def mmul(A, B):
    return [[sum((A[r][t] * B[t][c] for t in range(4)), Z) for c in range(4)] for r in range(4)]


def mtr(A):
    return sum((A[r][r] for r in range(4)), Z)


def dirac_matrices():
    """Dirac representation: g0 = diag(1,1,-1,-1), gk = [[0, s_k], [-s_k, 0]]."""
    sig = [[[Z, ONE], [ONE, Z]], [[Z, QI(0, -1)], [IU, Z]], [[ONE, Z], [Z, QI(-1)]]]
    g0 = [[ONE if r == c and r < 2 else (QI(-1) if r == c else Z) for c in range(4)] for r in range(4)]
    gs = [g0]
    for k in range(3):
        m = [[Z] * 4 for _ in range(4)]
        for r in range(2):
            for c in range(2):
                m[r][c + 2] = sig[k][r][c]
                m[r + 2][c] = -sig[k][r][c]
        gs.append(m)
    return gs


def mat_of(x, gs):
    out = [[Z] * 4 for _ in range(4)]
    for b, c in x.items():
        m = [[ONE if r == cc else Z for cc in range(4)] for r in range(4)]
        for i in b:
            m = mmul(m, gs[i])
        out = [[out[r][cc] + c * m[r][cc] for cc in range(4)] for r in range(4)]
    return out


# ---------------------------------------------------------------- the triangle integrands
def D1(l, M, mu_vec, nu_vec, rho_vec, axial=True):
    head = mul(mu_vec, GAMMA5) if axial else GAMMA5
    return tr(mul(head, prop(l, M), nu_vec, prop(add(l, cscal(-1, K1)), M), rho_vec,
                  prop(add(l, cscal(-1, QV)), M)))


def D2(l, M, mu_vec, nu_vec, rho_vec, axial=True):
    head = mul(mu_vec, GAMMA5) if axial else GAMMA5
    return tr(mul(head, prop(l, M), rho_vec, prop(add(l, cscal(-1, K2)), M), nu_vec,
                  prop(add(l, cscal(-1, QV)), M)))


def Bvec(p, M, mu_vec, rho_vec):
    """two-point term left by contracting the k1 vertex: Tr[g^mu gamma5 S(p) g^rho S(p - k2)]"""
    return tr(mul(mu_vec, GAMMA5, prop(p, M), rho_vec, prop(add(p, cscal(-1, K2)), M)))


def check_gamma5_trace_is_the_pseudoscalar_part():
    premise("synthesis.one-loop-qed-in-the-spacetime-algebra")
    gs = dirac_matrices()
    g5m = mat_of(GAMMA5, gs)
    ok = True
    # gamma5 = i g0 g1 g2 g3 is the usual chirality matrix: diagonal blocks zero, off-diagonal identity
    ok &= all(g5m[r][c] == (ONE if abs(r - c) == 2 else Z) for r in range(4) for c in range(4))
    for vs in [(VA, VB, VC, VD), (VB, VD, VA, VC), (G[0], G[1], G[2], G[3]), (G[1], G[0], G[2], G[3])]:
        X = mul(*vs)
        lhs = mtr(mmul(g5m, mat_of(X, gs)))
        ok &= lhs == tr(mul(GAMMA5, X))
        lam = sc(mul(X, cscal(Fr(-1), I4)))     # 4-vector part = lam I4 ; I4^-1 = -I4
        ok &= tr(mul(GAMMA5, X)) == QI(0, -4 * lam)
        ok &= sc(mul(I4, X)) == -lam
    # total antisymmetry
    base = sc(mul(I4, VA, VB, VC, VD))
    ok &= sc(mul(I4, VB, VA, VC, VD)) == -base and sc(mul(I4, VA, VC, VB, VD)) == -base
    ok &= sc(mul(I4, VD, VA, VB, VC)) == -base and base != 0
    ok &= sc(mul(I4, G[0], G[1], G[2], G[3])) == -1
    GA.check("check_gamma5_trace_is_the_pseudoscalar_part", ok)
    return ok


def check_vector_ward_identity_integrand_by_integrand():
    premise("synthesis.one-loop-qed-in-the-spacetime-algebra")
    ok = True
    for M, l in ((MASSES[0], LOOPS[0]), (MASSES[1], LOOPS[1]), (MASSES[2], LOOPS[2])):
        if True:
            for mu in range(4):
                for rho in range(4):
                    lhs = D1(l, M, GU[mu], K1, GU[rho]) + D2(l, M, GU[mu], K1, GU[rho])
                    rhs = Bvec(add(l, cscal(-1, K1)), M, GU[mu], GU[rho]) - Bvec(l, M, GU[mu], GU[rho])
                    ok &= lhs == rhs
    # the other vector vertex: k2 contraction
    for M in MASSES[1:2]:
        l = LOOPS[0]
        for mu in range(4):
            for nu in range(4):
                lhs = D1(l, M, GU[mu], GU[nu], K2) + D2(l, M, GU[mu], GU[nu], K2)
                b1 = tr(mul(GU[mu], GAMMA5, prop(l, M), GU[nu], prop(add(l, cscal(-1, K1)), M)))
                lq = add(l, cscal(-1, K2))
                b2 = tr(mul(GU[mu], GAMMA5, prop(lq, M), GU[nu], prop(add(lq, cscal(-1, K1)), M)))
                ok &= lhs == b2 - b1
    GA.check("check_vector_ward_identity_integrand_by_integrand", ok)
    return ok


def check_two_point_terms_integrate_to_zero_under_the_regulator():
    premise("synthesis.imported-one-loop-integrals-and-pauli-villars-regulators")
    ok = True
    # (a) the epsilon numerator of Tr[g^mu gamma5 (a+M) g^rho (b+M)] is mass independent and depends on a^b only
    a, b = VA, VB
    for mu in range(4):
        for rho in range(4):
            vals = [tr(mul(GU[mu], GAMMA5, add(a, num(M)), GU[rho], add(b, num(M)))) for M in MASSES]
            ok &= im(vals[0]) == im(vals[1]) == im(vals[2]) != 0 or (mu == rho and im(vals[0]) == 0)
            # depends on a, b only through a ^ b: replace b by b + 2a
            b2 = add(b, cscal(2, a))
            ok &= im(tr(mul(GU[mu], GAMMA5, a, GU[rho], b2))) == im(vals[0])
            # (b) about the centre c = k/2 with a = c + u, b = c + u - k: odd in u
            k = K2
            u = VC
            c = cscal(Fr(1, 2), k)
            plus = im(tr(mul(GU[mu], GAMMA5, add(c, u), GU[rho], add(c, u, cscal(-1, k)))))
            minus = im(tr(mul(GU[mu], GAMMA5, add(c, cscal(-1, u)), GU[rho], add(c, cscal(-1, u), cscal(-1, k)))))
            ok &= plus == -minus
    # (c) sum_i c_i / ((t^2 Q(u) - M_i^2) (Q(t u - k) - M_i^2)) has numerator degree <= 2 (O(t^-6)) iff sum c_i = 0
    u, k = VC, K2
    Qu, Qk, uk = Q(u), Q(k), sc(mul(u, k))

    def dens(M2):
        d1 = [-M2, Fr(0), Qu]                             # t^2 Q(u) - M^2
        d2 = [Qk - M2, -2 * uk, Qu]                       # Q(t u - k) - M^2
        return GA.pmul(d1, d2)

    def numerator(weights):
        ds = [dens(M2) for _, M2 in weights]
        tot = [Fr(0)]
        for i, (ci, _) in enumerate(weights):
            term = [Fr(ci)]
            for j, d in enumerate(ds):
                if j != i:
                    term = GA.pmul(term, d)
            tot = GA.padd(tot, term)
        return GA.ptrim(tot)

    good = numerator([(1, Fr(0)), (-1, Fr(9))])
    ok &= len(good) - 1 <= 2                          # two fields: product degree 8, need <= 2
    three = numerator([(1, Fr(0)), (Fr(-3, 2), Fr(4)), (Fr(1, 2), Fr(16))])
    ok &= len(three) - 1 <= 6                          # three fields: product degree 12, need <= 6
    bad = numerator([(1, Fr(0)), (Fr(-1, 2), Fr(9))])
    ok &= len(bad) - 1 == 4
    GA.check("check_two_point_terms_integrate_to_zero_under_the_regulator", ok)
    return ok


def check_axial_identity_integrand_by_integrand():
    premise("synthesis.one-loop-qed-in-the-spacetime-algebra")
    ok = True
    for M, l in ((MASSES[0], LOOPS[0]), (MASSES[1], LOOPS[1])):
        if True:
            lk1 = add(l, cscal(-1, K1))
            lk2 = add(l, cscal(-1, K2))
            lq = add(l, cscal(-1, QV))
            for nu in range(4):
                for rho in range(4):
                    lhs = D1(l, M, QV, GU[nu], GU[rho]) + D2(l, M, QV, GU[nu], GU[rho])
                    pp = D1(l, M, None, GU[nu], GU[rho], axial=False) + D2(l, M, None, GU[nu], GU[rho], axial=False)
                    two = (- tr(mul(GAMMA5, prop(l, M), GU[nu], prop(lk1, M), GU[rho]))
                           - tr(mul(GAMMA5, GU[nu], prop(lk1, M), GU[rho], prop(lq, M)))
                           - tr(mul(GAMMA5, prop(l, M), GU[rho], prop(lk2, M), GU[nu]))
                           - tr(mul(GAMMA5, GU[rho], prop(lk2, M), GU[nu], prop(lq, M))))
                    ok &= lhs == QI(-2 * M) * pp + two
    GA.check("check_axial_identity_integrand_by_integrand", ok)
    return ok


def check_regulator_term_gives_one_over_two_pi_squared():
    premise("synthesis.imported-one-loop-integrals-and-pauli-villars-regulators")
    ok = True
    # numerator of P1, P2 over the common denominator: M times an l-independent constant
    for nu in range(4):
        for rho in range(4):
            target = QI(0, 4) * sc(mul(I4, GU[nu], K1, GU[rho], K2))
            for M, l in ((MASSES[1], LOOPS[0]), (MASSES[2], LOOPS[2])):
                if True:
                    lk1, lk2, lq = add(l, cscal(-1, K1)), add(l, cscal(-1, K2)), add(l, cscal(-1, QV))
                    n1 = tr(mul(GAMMA5, add(l, num(M)), GU[nu], add(lk1, num(M)), GU[rho], add(lq, num(M))))
                    n2 = tr(mul(GAMMA5, add(l, num(M)), GU[rho], add(lk2, num(M)), GU[nu], add(lq, num(M))))
                    ok &= n1 == QI(M) * target and n2 == QI(M) * target
    # the Fact's integral: int d^4l/(2 pi)^4 (l^2 - Delta)^-3 = -i/(32 pi^2 Delta): its rational part from the
    # Wick rotation (factor i, sign (-1)^3), angular volume 2 pi^2, radial integral 1/(4 Delta), (2 pi)^-4
    Dl = Fr(7, 3)
    Fprim = lambda uu: -Fr(1) / (uu + Dl) + Dl / (2 * (uu + Dl) ** 2)       # antiderivative of u/(u+Dl)^3
    dFprim = lambda uu: Fr(1) / (uu + Dl) ** 2 - Dl / (uu + Dl) ** 3          # its derivative, term by term
    for uu in (Fr(0), Fr(1, 2), Fr(5), Fr(17, 3)):
        ok &= dFprim(uu) == uu / (uu + Dl) ** 3
    radial = Fr(1, 2) * (Fr(0) - Fprim(Fr(0)))          # u = r^2; F(infinity) = 0
    ok &= radial == Fr(1, 4) / Dl
    ok &= Fr(-1) * 2 * radial / 16 == Fr(-1, 32) / Dl   # i (-1)^3 2 pi^2 / (16 pi^4): coefficient of i/pi^2
    # assemble: q.T = sum_{i>=1} c_i (-2 M_i) * (M_i C) * (-i/(32 pi^2 M_i^2)) with C = 2 * 4 i <I4 g^nu k1 g^rho k2>_0
    # (the Feynman measure 2 int_simplex = 1; M_i^2/Delta_i -> 1). Coefficient of <...>_0 / pi^2:
    for weights in ([(-1, 9)], [(Fr(-3, 2), 4), (Fr(1, 2), 16)], [(Fr(-5, 2), 1), (Fr(3, 2), 7)]):
        sw = sum(Fr(c) for c, _ in weights)
        ok &= sw == -1                                   # sum_i c_i = 0 with c_0 = 1
        coef = Fr(0)
        for c, M2 in weights:
            M2 = Fr(M2)
            # c (-2 M) (M) (2 * 4 i) (-i/(32 M^2)) = c * (-2) * 8 * (i * -i) / 32 = c * (-1/2)
            val = QI(c) * QI(-2) * M2 * QI(0, 8) * QI(0, -1) / (32 * M2)
            ok &= val.im == 0
            coef += val.re
        ok &= coef == Fr(1, 2)                           # q.T = (1/(2 pi^2)) <I4 g^nu k1 g^rho k2>_0
    GA.check("check_regulator_term_gives_one_over_two_pi_squared", ok)
    return ok


def check_field_form_is_the_pseudoscalar_part_of_f_squared():
    premise("synthesis.one-loop-qed-in-the-spacetime-algebra")
    ok = True
    a1, a2 = VA, VC
    f1 = {b: c for b, c in mul(a1, K1).items() if len(b) == 2}
    f2 = {b: c for b, c in mul(a2, K2).items() if len(b) == 2}
    ok &= sc(mul(I4, a1, K1, a2, K2)) == sc(mul(I4, f1, f2))
    ok &= sc(mul(I4, f1, f2)) == sc(mul(I4, f2, f1))    # Bose symmetry of the two photons
    ok &= sc(mul(I4, f1, f2)) == Fr(-7, 6)
    # F = E + I4 B, E = E^k g_k g_0, B = B^k g_k g_0: <I4 F^2>_0 = -2 E.B
    sig = [mul(G[k], G[0]) for k in (1, 2, 3)]
    for Ev, Bv in (((1, 2, 3), (Fr(1, 2), -1, 2)), ((Fr(2, 3), 0, 5), (3, Fr(1, 7), -1))):
        E = add(*[cscal(Fr(Ev[k]), sig[k]) for k in range(3)])
        B = add(*[cscal(Fr(Bv[k]), sig[k]) for k in range(3)])
        F = add(E, mul(I4, B))
        EB = sum(Fr(Ev[k]) * Fr(Bv[k]) for k in range(3))
        ok &= sc(mul(I4, F, F)) == -2 * EB
        ok &= EB == {(1, 2, 3): Fr(9, 2), (Fr(2, 3), 0, 5): Fr(-3)}[Ev]
    GA.check("check_field_form_is_the_pseudoscalar_part_of_f_squared", ok)
    return ok


def check_chiral_projectors_collapse_to_one():
    premise("synthesis.one-loop-qed-in-the-spacetime-algebra")
    ok = True
    PL = cscal(Fr(1, 2), add(num(1), cscal(Fr(-1), GAMMA5)))
    PR = cscal(Fr(1, 2), add(num(1), GAMMA5))
    a, b, c = LOOPS[0], add(LOOPS[0], cscal(-1, K1)), add(LOOPS[0], cscal(-1, QV))
    for mu, nu, rho in [(0, 1, 2), (1, 2, 3), (0, 0, 3), (3, 1, 0)]:
        lhs = tr(mul(GU[mu], PL, a, GU[nu], PL, b, GU[rho], PL, c))
        rhs = tr(mul(GU[mu], a, GU[nu], b, GU[rho], c, PR))
        ok &= lhs == rhs
        # half the vector trace plus half the axial one
        vt = tr(mul(GU[mu], a, GU[nu], b, GU[rho], c))
        at = tr(mul(GU[mu], a, GU[nu], b, GU[rho], c, GAMMA5))
        ok &= rhs == QI(Fr(1, 2)) * vt + QI(Fr(1, 2)) * at
        pinned = {(0, 1, 2): QI(Fr(374, 945), Fr(-21331, 17640)), (0, 0, 3): QI(Fr(13359, 1960), Fr(226, 945))}
        if (mu, nu, rho) in pinned:
            ok &= rhs == pinned[(mu, nu, rho)]
    GA.check("check_chiral_projectors_collapse_to_one", ok)
    return ok


# ---------------------------------------------------------------- the content of one generation
def generation():
    """left-handed Weyl content of one generation: (colour, weak, Y)."""
    return [("1", 1, Fr(0)), ("3b", 1, Fr(-2, 3)), ("3", 2, Fr(1, 6)), ("1", 2, Fr(-1, 2)),
            ("1", 1, Fr(1)), ("3b", 1, Fr(1, 3))]


def gauge_basis():
    """basis of sl3 + sl2 + C as triples (A 3x3, B 2x2, y)."""
    z3 = [[Fr(0)] * 3 for _ in range(3)]
    z2 = [[Fr(0)] * 2 for _ in range(2)]
    out = []
    for i in range(3):
        for j in range(3):
            if i != j:
                A = [r[:] for r in z3]
                A[i][j] = Fr(1)
                out.append((A, z2, Fr(0)))
    out.append(([[Fr(1), 0, 0], [0, Fr(-1), 0], [0, 0, Fr(0)]], z2, Fr(0)))
    out.append(([[Fr(0), 0, 0], [0, Fr(1), 0], [0, 0, Fr(-1)]], z2, Fr(0)))
    out.append((z3, [[Fr(0), Fr(1)], [Fr(0), Fr(0)]], Fr(0)))
    out.append((z3, [[Fr(0), Fr(0)], [Fr(1), Fr(0)]], Fr(0)))
    out.append((z3, [[Fr(1), Fr(0)], [Fr(0), Fr(-1)]], Fr(0)))
    out.append((z3, z2, Fr(1)))
    return out


def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def eye(n):
    return [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]


def rep_matrix(X, content):
    A, B, y = X
    blocks = []
    for col, w, Y in content:
        if col == "1":
            Ac = [[Fr(0)]]
        elif col == "3":
            Ac = A
        else:
            Ac = [[-A[j][i] for j in range(3)] for i in range(3)]
        Bc = [[Fr(0)]] if w == 1 else B
        nc, nw = len(Ac), len(Bc)
        ka, kb = kron(Ac, eye(nw)), kron(eye(nc), Bc)
        m = [[ka[i][j] + kb[i][j] + (y * Y if i == j else Fr(0)) for j in range(nc * nw)] for i in range(nc * nw)]
        blocks.append(m)
    n = sum(len(b) for b in blocks)
    out = [[Fr(0)] * n for _ in range(n)]
    o = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                out[o + i][o + j] = b[i][j]
        o += len(b)
    return out


def check_anomaly_tensor_of_one_generation_vanishes_on_the_whole_gauge_algebra():
    premise("synthesis.anomaly-freedom-forces-slot-content")
    content = generation()
    mats = [rep_matrix(X, content) for X in gauge_basis()]
    ok = len(mats[0]) == 16
    n = len(mats)
    prod2 = {(b, c): GA.mat_mul(mats[b], mats[c]) for b in range(n) for c in range(n)}
    for a, b, c in combinations_with_replacement(range(n), 3):
        A, bc, cb = mats[a], prod2[(b, c)], prod2[(c, b)]
        d = sum(A[i][j] * (bc[j][i] + cb[j][i]) for i in range(16) for j in range(16) if A[i][j] != 0)
        ok &= d == 0
    ok &= all(sum(m[i][i] for i in range(16)) == 0 for m in mats)        # gravitational: tr X = 0
    # the nonzero pieces of single fields: the cancellation is between fields, not term by term
    yonly = rep_matrix(gauge_basis()[-1], [content[2]])
    ok &= sum(GA.mat_mul(yonly, GA.mat_mul(yonly, yonly))[i][i] for i in range(6)) == Fr(6, 216)
    GA.check("check_anomaly_tensor_of_one_generation_vanishes_on_the_whole_gauge_algebra", ok)
    return ok


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("check_") and callable(fn):
            GA.check(name, fn())
