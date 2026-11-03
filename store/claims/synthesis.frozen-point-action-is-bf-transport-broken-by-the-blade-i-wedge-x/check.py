"""The frozen-point MacDowell-Mansouri functional in BF form: exact checks in Cl(2,4).

Cl(2,4): generators e0 (+1), e1, e2, e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-; the frozen
point I = ninf + (Lambda/6) n0 with Q(I) = Lambda/3, the canonical tractor X = n0, the Stelle-West vector
V = X - (3/Lambda) I (as in the stored frozen-point checks). The fibre volume form is
eps(a, b, P, Q) = <a b P Q I6^{-1}>_0, I6 = e0 e1 e2 e3 e+ e-. A bivector-valued 2-form B is stored by its
values B_P on the six coordinate planes P = (m, n), m < n; the 4-form B ^ C is sum_{P,Q} omega(P,Q) B_P C_Q d^4x
with omega(P,Q) the sign of the permutation P + Q (zero when P, Q share an index).
(1) The breaking term. eps(I, V, B, B') = -<B iota B'>_0 on all 225 pairs of basis bivectors, symmetric,
    invariant under the stabiliser of (I, V) (dimension 6; that of I has dimension 10) and odd under the
    reflection in e1 (orthogonal to I and V); iota = (I ^ V) I6 = e0 e1 e2 e3, iota^2 = -1, and
    I ^ V = I ^ X = ninf ^ n0 with (I ^ V)^2 = 1, at Lambda = 3/4, -3/2, 12.
(2) Elimination. L(B) = sum omega [<B_P F_Q> - (1/4)<B_P M(B_Q)>], M = a iota + b on the Lorentz block of
    {I, V}-perp. For Lorentz-block F the point B_P = 2 M^{-1} F_P, M^{-1} = (b - a iota)/(a^2 + b^2), is
    stationary in all 90 directions, the breaking form has rank 36 on the Lorentz block (so it is the unique
    Lorentz-block stationary point), and L there equals (a eps(I,V,F,F) + b <F ^ F>)/(a^2 + b^2). If F has a
    component off the Lorentz block (a translational, torsion, component) the gradient in the matching B
    direction is independent of B and nonzero: no stationary point. Rescaling B by k multiplies the value by k^2.
(3) Normalisation. On a de Sitter field (H = 1/2) and a generic Bianchi I field (synchronous diagonal data),
    sum omega eps(I, V, R_P, (e^e)_Q) = -(1/2) R det(hb^{-1}) and sum omega eps(I, V, (e^e)_P, (e^e)_Q) = 6 det(hb^{-1}),
    R the store-sign scalar curvature (R = 4 Lambda on de Sitter); hence the Einstein-Hilbert part of
    (1/Q(I)) eps(I, V, F, F) is -(R - 2 Lambda) det(hb^{-1}), coefficient of magnitude one; the coupling ratio
    alpha N^2 / pi = 16 a^2/(a^2 + b^2) (16 at b = 0). The parity-even Lorentz pairing of e^e with itself is zero
    and with R is zero on these torsion-free fields.
(4) BF sector and torsion. On de Sitter the Lorentz block -calR + (Lambda/3) e^e vanishes, so B = 0; on a
    Lambda != 0 field with Weyl part (calR = (Lambda/3) id + Kasner Weyl operator) the block is -W and
    B = (2/alpha) iota W is nonzero. The vacuum connection equation of the functional, T -> sum eps^{qmnp}
    eps(I, V, b, T_mn ^ e_p) over Lorentz b and q, has rank 24 on the 24 torsion components.
(5) Translational term. <B_V B'_V>_0 on V ^ {I, V}-perp is Stab(I, V)-invariant with rank 4; with
    -(c/4) <B_V ^ B_V>_0 added, B_V = 2 F_V / c is stationary and the value is the Lorentz-block value plus
    (1/c) sum omega <F_V F_V>_0 (nonzero on the sample), at c = 3, -1/2: the torsion constraint becomes a
    torsion-squared term that vanishes as c grows.
Orientation: the stored check's chart; the opposite orientation of (ninf, n0) reverses every sign of eps(I, V, ., .).
Exact arithmetic only (Fractions); the sample fields and field strengths are fixed tables.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
PLANES = [(m, n) for m in range(4) for n in range(m + 1, 4)]
BIVIDX = [(i, j) for i in range(6) for j in range(i + 1, 6)]


def mul(x, y):
    return GA.mul(x, y, S)


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(mul(X, Y), mul(Y, X)))


def wedge(a, b):
    return comm(a, b)


def dot(a, b):
    return GA.dot(a, b, S)


def sp(x):
    return x.get((), F(0))


BIV = [wedge(E[i], E[j]) for i, j in BIVIDX]
LOR = [wedge(E[i], E[j]) for i in range(4) for j in range(i + 1, 4)]
I6 = mul(mul(mul(E[0], E[1]), mul(E[2], E[3])), mul(E[4], E[5]))
IOTA = mul(mul(E[0], E[1]), mul(E[2], E[3]))


def frozen(lam):
    I = GA.add(NI, GA.scal(lam / 6, N0))
    return I, GA.sub(N0, GA.scal(3 / lam, I))


def coords(B):
    return [B.get(b, F(0)) for b in BIVIDX]


def lin(cs, basis):
    return GA.add(*[GA.scal(c, b) for c, b in zip(cs, basis) if c])


def eps(a, b, P, Q):
    return sp(mul(mul(mul(mul(a, b), P), Q), GA.scal(1 / sp(mul(I6, I6)), I6)))


def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def omega(P, Q):
    idx = tuple(P) + tuple(Q)
    return perm_sign(idx) if len(set(idx)) == 4 else 0


def pair(f):
    """sum_{P,Q} omega(P,Q) f(P, Q)."""
    return sum(omega(P, Q) * f(P, Q) for P in PLANES for Q in PLANES if omega(P, Q))


def stab(vectors):
    rows = []
    for v in vectors:
        rows += [[comm(B, v).get((k,), F(0)) for B in BIV] for k in range(6)]
    return [lin(k, BIV) for k in GA.field_kernel(rows)]


# ---------------------------------------------------------------------------
# synchronous diagonal gravitational field on flat spacetime (as in the stored frozen-point checks)
# ---------------------------------------------------------------------------
class Synchronous(object):
    def __init__(self, data):
        self.d = {0: (F(1), F(0), F(0))}
        self.d.update({i + 1: tuple(F(v) for v in data[i]) for i in range(3)})

    def a(self, m):
        return self.d[m][0]

    def hb_inv(self, m):
        return GA.scal(self.d[m][0], E[m])

    def Omega(self, m):
        return {} if m == 0 else GA.scal(-self.d[m][1], wedge(E[0], E[m]))

    def d_Omega(self, m):
        return {} if m == 0 else GA.scal(-self.d[m][2], wedge(E[0], E[m]))

    def R_bg(self, m, n):
        t1 = self.d_Omega(n) if m == 0 else {}
        t2 = self.d_Omega(m) if n == 0 else {}
        return GA.add(t1, GA.neg(t2), comm(self.Omega(m), self.Omega(n)))

    def calR(self, B):
        out = {}
        for m, n in PLANES:
            c = sp(mul(B, wedge(ER[n], ER[m])))
            if c:
                out = GA.add(out, GA.scal(-c / (self.a(m) * self.a(n)), self.R_bg(m, n)))
        return out

    def ricci(self, b):
        return GA.add(*[{k: v for k, v in comm(ER[m], self.calR(wedge(E[m], b))).items() if len(k) == 1}
                        for m in range(4)])

    def scalar(self):
        return sum(sp(mul(ER[m], self.ricci(E[m]))) for m in range(4))

    def det(self):
        return self.a(1) * self.a(2) * self.a(3)

    def R2(self):
        """R_P = -calR(e_m ^ e_n) on the coordinate plane P = (m, n), e_m = hb^{-1}(e_m)."""
        return {P: GA.neg(self.calR(wedge(self.hb_inv(P[0]), self.hb_inv(P[1])))) for P in PLANES}

    def ee(self):
        return {P: wedge(self.hb_inv(P[0]), self.hb_inv(P[1])) for P in PLANES}


DE_SITTER = [(F(2), F(1), F(1, 2))] * 3                       # H = 1/2: (a, 2H, 2H^2), Lambda = 3/4
BIANCHI = [(F(2), F(3), F(-1)), (F(1, 3), F(2), F(5)), (F(3), F(-1, 2), F(7))]
LAMBDAS = (F(3, 4), F(-3, 2), F(12))
# fixed Lorentz-block field strength on the six planes (integer table)
FTAB = [[1, -2, 0, 3, 1, -1], [2, 0, -1, 1, -3, 2], [0, 1, 2, -2, 1, 3],
        [-1, 3, 1, 0, 2, -2], [3, -1, 2, 1, 0, 1], [1, 2, -3, -1, 2, 0]]
AB_SAMPLES = ((F(2, 5), F(0)), (F(1, 3), F(1, 7)), (F(0), F(2)), (F(-3), F(1, 2)))


def lagrangian(B, Fd, a, b, k=1):
    Mop = lambda X: GA.add(GA.scal(a, mul(IOTA, X)), GA.scal(b, X))
    return pair(lambda P, Q: k * sp(mul(B[P], Fd[Q])) - F(1, 4) * sp(mul(B[P], Mop(B[Q]))))


def check_breaking_term_lives_on_the_blade():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("dark-energy.stelle-west-vector-frozen-point")
    ok = True
    for lam in LAMBDAS[:2]:
        I, V = frozen(lam)
        sIV = stab([I, V])
        ok = ok and len(stab([I])) == 10 and len(sIV) == 6
        ok = ok and dot(E[1], I) == 0 and dot(E[1], V) == 0
        # eps(I, V, ., .) = -<. iota .>_0 on all pairs, invariant under Stab(I, V), odd under the e1 reflection
        refl = lambda B: GA.scal(1 / sp(mul(E[1], E[1])), mul(mul(E[1], B), E[1]))
        odd = 0
        for i in range(15):
            for j in range(15):
                e_ij = eps(I, V, BIV[i], BIV[j])
                ok = ok and e_ij == -sp(mul(mul(BIV[i], IOTA), BIV[j])) and e_ij == eps(I, V, BIV[j], BIV[i])
                ok = ok and eps(I, V, refl(BIV[i]), refl(BIV[j])) == -e_ij
                odd += e_ij != 0
        for g in sIV:
            for i in range(15):
                for j in range(15):
                    ok = ok and (eps(I, V, comm(g, BIV[i]), BIV[j]) + eps(I, V, BIV[i], comm(g, BIV[j]))) == 0
        ok = ok and odd == 6
    for lam in LAMBDAS:
        I, V = frozen(lam)
        IV = wedge(I, V)
        ok = ok and GA.eq(IV, wedge(I, N0)) and GA.eq(IV, wedge(NI, N0))
        ok = ok and GA.eq(mul(IV, IV), GA.sc(1)) and GA.eq(mul(IV, I6), IOTA)
        ok = ok and dot(I, I) * dot(V, V) == -1
    ok = ok and GA.eq(mul(IOTA, IOTA), GA.sc(-1))
    GA.check("breaking term eps(I,V,B,B') = -<B iota B'>_0, Stab(I,V)-invariant, odd; I^V = I^X = ninf^n0, square 1", ok)
    assert ok


def check_eliminating_b_gives_the_frozen_point_integrand():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok = True
    I, V = frozen(LAMBDAS[0])
    Fv = {P: lin([F(c) for c in FTAB[k]], LOR) for k, P in enumerate(PLANES)}
    Ecal = pair(lambda P, Q: eps(I, V, Fv[P], Fv[Q]))
    Kil = pair(lambda P, Q: sp(mul(Fv[P], Fv[Q])))
    ok = ok and Ecal != 0 and Kil != 0
    for a, b in AB_SAMPLES:
        den = a * a + b * b
        Minv = GA.add(GA.sc(b / den), GA.scal(-a / den, IOTA))
        Bs = {P: GA.scal(2, mul(Minv, Fv[P])) for P in PLANES}
        for P0 in PLANES:
            for d in BIV:
                g = sum(omega(P0, Q) * (sp(mul(d, Fv[Q]))
                                        - F(1, 2) * (a * sp(mul(mul(d, IOTA), Bs[Q])) + b * sp(mul(d, Bs[Q]))))
                        for Q in PLANES if omega(P0, Q))
                ok = ok and g == 0
        val = lagrangian(Bs, Fv, a, b)
        ok = ok and val == (a * Ecal + b * Kil) / den
        # BF coefficient k: the stationary value scales by k^2 (B -> k B), so alpha alone is not invariant
        Bk = {P: GA.scal(3, Bs[P]) for P in PLANES}
        ok = ok and lagrangian(Bk, Fv, a, b, k=3) == 9 * val
    # uniqueness on the Lorentz block: the breaking form (a = 1, b = 0) has rank 36
    basisB = [(P, l) for P in PLANES for l in LOR]
    rows = [[omega(P, Q) * sp(mul(mul(l, IOTA), m)) for (Q, m) in basisB] for (P, l) in basisB]
    ok = ok and GA.field_rank(rows) == 36
    # a translational (torsion-block) component of F: its B-gradient is independent of B and nonzero
    Ft = dict(Fv)
    Ft[(2, 3)] = GA.add(Fv[(2, 3)], wedge(E[1], V))
    d = wedge(E[1], V)
    for Btry in ({P: {} for P in PLANES}, {P: GA.scal(2, Fv[P]) for P in PLANES}):
        g = sum(omega((0, 1), Q) * (sp(mul(d, Ft[Q])) - F(1, 2) * sp(mul(mul(d, IOTA), Btry[Q])))
                for Q in PLANES if omega((0, 1), Q))
        ok = ok and g == omega((0, 1), (2, 3)) * dot(V, V) * dot(E[1], E[1]) * (-1) and g != 0
    GA.check("eliminating B: B_L = 2 M^-1 F_L unique, value (a eps(I,V,F,F) + b <F^F>)/(a^2+b^2), torsion block a multiplier",
             ok)
    assert ok


def check_coupling_is_sixteen_pi_over_n_squared():
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    premise("standard-model.imported-frozen-point-dictionary")
    premise("synthesis.de-sitter-entropy-pi-n-squared")
    ok = True
    seen = set()
    for lam in LAMBDAS:
        I, V = frozen(lam)
        for data in (DE_SITTER, BIANCHI):
            f = Synchronous(data)
            R, ee = f.R2(), f.ee()
            seen.add(pair(lambda P, Q: eps(I, V, R[P], ee[Q])) / (f.scalar() * f.det()))
            ok = ok and pair(lambda P, Q: eps(I, V, ee[P], ee[Q])) == 6 * f.det()
            ok = ok and pair(lambda P, Q: sp(mul(ee[P], ee[Q]))) == 0
            ok = ok and pair(lambda P, Q: sp(mul(R[P], ee[Q]))) == 0
            Fd = {P: GA.add(R[P], GA.scal(lam / 3, ee[P])) for P in PLANES}
            lhs = pair(lambda P, Q: eps(I, V, Fd[P], Fd[Q])) / dot(I, I)
            rhs = -(f.scalar() - 2 * lam) * f.det() + (3 / lam) * pair(lambda P, Q: eps(I, V, R[P], R[Q]))
            ok = ok and lhs == rhs
    f = Synchronous(DE_SITTER)
    ok = ok and f.scalar() == 4 * LAMBDAS[0]
    # coupling: the coefficient of eps(I,V,F,F) is a/(a^2+b^2) after elimination and k/Q(I) in the stored
    # functional, |k| = 1/(16 pi G) because the Einstein-Hilbert coefficient of (1/Q(I)) eps is |2 c_eh| = 1;
    # with N^2 = 1/(G Q(I)): alpha N^2 / pi = 16 |2 c_eh| a^2/(a^2+b^2)
    ok = ok and seen == {F(-1, 2)}
    c_eh = seen.pop()
    for a, b in AB_SAMPLES[:2] + AB_SAMPLES[3:]:
        ratio = 16 * abs(2 * c_eh) * a * a / (a * a + b * b)
        ok = ok and (ratio == 16 if b == 0 else ratio < 16)
    GA.check("coupling: EH part of (1/Q(I)) eps(I,V,F,F) is -(R - 2 Lambda) sqrt g, so alpha N^2 = 16 pi a^2/(a^2+b^2)",
             ok)
    assert ok


def check_bf_sector_is_pure_transport_and_torsion():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok = True
    alpha = F(2, 5)
    lam = LAMBDAS[0]
    I, V = frozen(lam)
    f = Synchronous(DE_SITTER)
    R, ee = f.R2(), f.ee()
    FL = {P: GA.add(R[P], GA.scal(lam / 3, ee[P])) for P in PLANES}
    B = {P: GA.scal(-2 / alpha, mul(IOTA, FL[P])) for P in PLANES}
    ok = ok and all(GA.is_zero(FL[P]) and GA.is_zero(B[P]) for P in PLANES)
    # Kasner Weyl operator added to (Lambda/3) id: the Lorentz block is -W, B = (2/alpha) iota W, nonzero
    k = Synchronous([(F(4), F(1, 3), F(-1, 72)), (F(4), F(1, 3), F(-1, 72)), (F(1, 2), F(-1, 48), F(1, 288))])
    ok = ok and all(GA.is_zero(k.ricci(e)) for e in ER)
    nonzero = 0
    for m, n in PLANES:
        Bmn = wedge(E[m], E[n])
        W = k.calR(Bmn)
        FLmn = GA.add(GA.neg(GA.add(GA.scal(lam / 3, Bmn), W)), GA.scal(lam / 3, Bmn))
        ok = ok and GA.eq(FLmn, GA.neg(W))
        Bm = GA.scal(-2 / alpha, mul(IOTA, FLmn))
        ok = ok and GA.eq(Bm, GA.scal(2 / alpha, mul(IOTA, W)))
        ok = ok and GA.is_zero(comm(Bm, I)) and GA.is_zero(comm(Bm, V))
        nonzero += not GA.is_zero(Bm)
    ok = ok and nonzero == 6
    # vacuum connection equation: torsion T (vector-valued 2-form) -> sum eps^{qmnp} eps(I, V, b, T_mn ^ e_p)
    cols = []
    for (m, n) in PLANES:
        for a in range(4):
            col = []
            for b in LOR:
                for q in range(4):
                    col.append(sum(perm_sign((q, m, n, p)) * eps(I, V, b, wedge(E[a], E[p]))
                                   for p in range(4) if len({q, m, n, p}) == 4))
            cols.append(col)
    rows = [list(r) for r in zip(*cols)]
    ok = ok and len(cols) == 24 and GA.field_rank(rows) == 24
    GA.check("BF sector: B = 0 exactly on de Sitter (pure transport), B = (2/alpha) iota W otherwise; torsion rank 24",
             ok)
    assert ok


TRANS_TAB = [[1, 0, -2, 1], [0, 3, 1, -1], [2, -1, 0, 1], [-1, 1, 2, 0], [0, -2, 1, 3], [1, 1, -1, 2]]


def check_translational_term_restores_unconstrained_torsion():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("synthesis.imported-einstein-cartan-matter-coupling")
    ok = True
    I, V = frozen(LAMBDAS[0])
    TRV = [wedge(E[k], V) for k in range(4)]
    # the translational form <B_V B'_V>_0 is invariant under Stab(I, V) and nondegenerate
    G = [[sp(mul(x, y)) for y in TRV] for x in TRV]
    ok = ok and GA.field_rank(G) == 4
    for g in stab([I, V]):
        for x in TRV:
            for y in TRV:
                ok = ok and sp(mul(comm(g, x), y)) + sp(mul(x, comm(g, y))) == 0
    Fl = {P: lin([F(c) for c in FTAB[k]], LOR) for k, P in enumerate(PLANES)}
    Fv = {P: lin([F(c) for c in TRANS_TAB[k]], TRV) for k, P in enumerate(PLANES)}
    Fd = {P: GA.add(Fl[P], Fv[P]) for P in PLANES}
    Ecal = pair(lambda P, Q: eps(I, V, Fl[P], Fl[Q]))
    Kil = pair(lambda P, Q: sp(mul(Fl[P], Fl[Q])))
    TT = pair(lambda P, Q: sp(mul(Fv[P], Fv[Q])))
    ok = ok and TT != 0
    for a, b in AB_SAMPLES[:2]:
        den = a * a + b * b
        Minv = GA.add(GA.sc(b / den), GA.scal(-a / den, IOTA))
        for c in (F(3), F(-1, 2)):
            BL = {P: GA.scal(2, mul(Minv, Fl[P])) for P in PLANES}
            BV = {P: GA.scal(2 / c, Fv[P]) for P in PLANES}
            Bs = {P: GA.add(BL[P], BV[P]) for P in PLANES}
            val = pair(lambda P, Q: sp(mul(Bs[P], Fd[Q]))
                       - F(1, 4) * (a * sp(mul(mul(BL[P], IOTA), BL[Q])) + b * sp(mul(BL[P], BL[Q]))
                                    + c * sp(mul(BV[P], BV[Q]))))
            ok = ok and val == (a * Ecal + b * Kil) / den + TT / c
            for P0 in PLANES:
                for d in TRV:
                    g = sum(omega(P0, Q) * (sp(mul(d, Fd[Q])) - (c / 2) * sp(mul(d, GA.scal(2 / c, Fv[Q]))))
                            for Q in PLANES if omega(P0, Q))
                    ok = ok and g == 0
    GA.check("translational term c<B_V^B_V>: B_V = 2F_V/c, value S_ab + (1/c)<F_V^F_V>, torsion squared, -> 0 as c grows",
             ok)
    assert ok
