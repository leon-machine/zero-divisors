"""synthesis.conjugate-reading-up-down-split-is-t3r-odd-or-cp-odd: exact checks.

Part 1 (the module): the five-mode module Lambda(W + R_2) as 32 x 32 rational matrices (fock.py, LSB order),
modes 0, 1, 2 the pairs, 3, 4 the rungs, v_i creating, w_i annihilating, with the stored pairing B on the
sixteen (even states), as in the stored check of the up-down split under the conjugate reading. For a
diagonal weighting g, the down-type and charged-lepton entries of the composite c g come from w_4 g and the
up-type and Dirac-neutrino entries from v_4 g; both the symmetric part (10 and 126 type, paired with a
symmetric family matrix) and the antisymmetric part (120 type, paired with an antisymmetric family matrix)
of B(psi, X phi) are compared with the 10 forms on the same species pairs, oriented doublet first.

Part 2 (family matrices): 3 x 3 Gaussian-rational matrices (GA.QI). A source k is a rung vector's frame
coefficient beta_k (complex), real sector weights (down d_k, up u_k) from part 1, and a family matrix Y_k
(symmetric or antisymmetric); under the conjugate reading M_d = sum beta_k d_k Y_k and
M_u = sum conj(beta_k) u_k Y_k. H = M M^dag; spectra are compared through characteristic polynomials.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from GA import QI
import fock
from tp_premise import premise

# ---------------------------------------------------------------- part 1: the module
NM = 5
STATES = [s for k in range(NM + 1) for s in combinations(range(NM), k)]
IDX = {s: sum(1 << x for x in s) for s in STATES}
STATE_OF = {i: s for s, i in IDX.items()}
D = len(STATES)
mm, madd, msc, tr = fock.mm, fock.madd, fock.msc, fock.transpose
PAIRS = (0, 1, 2)
RUNGS = (3, 4)


def nw(s):
    return sum(1 for x in s if x in PAIRS)


def nr(s):
    return sum(1 for x in s if x in RUNGS)


def diag(fn):
    return fock.diag(lambda i: fn(STATE_OF[i]), D)


V = [fock.cre(m, NM) for m in range(NM)]
W = [tr(v) for v in V]
ONE = fock.eye(D)
BETA = [madd(mm(V[i], W[i]), msc(F(-1, 2), ONE)) for i in range(NM)]
BL = diag(lambda s: 1 - F(2, 3) * nw(s))
CHI = diag(lambda s: -(-1) ** nr(s))
T3R = diag(lambda s: F(nr(s) - 1, 2))
MUP = msc(F(1, 8), madd(BETA[0], BETA[1], BETA[2]))
MUR = msc(F(1, 8), madd(BETA[3], BETA[4]))
SIXTEEN = [s for s in STATES if len(s) % 2 == 0]
W4, V4 = W[3], V[3]

BMAT = {}
for _s in STATES:
    _comp = tuple(x for x in range(NM) if x not in _s)
    _seq = list(_s) + list(_comp)
    _inv = sum(1 for i in range(NM) for j in range(i + 1, NM) if _seq[i] > _seq[j])
    _k = len(_s)
    BMAT[(IDX[_s], IDX[_comp])] = F((-1) ** (_k * (_k - 1) // 2) * (-1) ** _inv)


def forms(X):
    BX = mm(BMAT, X)
    sym, anti = {}, {}
    for a in SIXTEEN:
        for b in SIXTEEN:
            x, y = BX.get((IDX[a], IDX[b]), 0), BX.get((IDX[b], IDX[a]), 0)
            if x + y:
                sym[(a, b)] = (x + y) * F(1, 2)
            if x - y:
                anti[(a, b)] = (x - y) * F(1, 2)
    return sym, anti


S10D, _ = forms(W4)
S10U, _ = forms(V4)


def weights(X, S10, part):
    """{sector: set of ratios} of the symmetric (part 0) or antisymmetric (part 1) form of X against the 10
    form, on pairs oriented doublet first; None if X has entries off the 10's pairs."""
    f = forms(X)[part]
    out = {}
    for (p, q), v in f.items():
        if (p, q) not in S10:
            return None
        if nr(p) != 1:
            continue
        sec = "lep" if nw(p) in (0, 3) else "qrk"
        out[sec] = out.get(sec, set()) | {v / S10[(p, q)]}
    return out


def ud(g, part):
    return weights(mm(W4, g), S10D, part), weights(mm(V4, g), S10U, part)


def single(w):
    """{sector: {x}} -> (lep, qrk) as Fractions."""
    return (min(w["lep"]), min(w["qrk"])) if w and all(len(v) == 1 for v in w.values()) else None


# ---------------------------------------------------------------- part 2: family matrices
def q(a, b=0):
    return QI(F(a), F(b))


def zero3():
    return [[q(0) for _ in range(3)] for _ in range(3)]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), q(0)) for j in range(3)] for i in range(3)]


def madd3(*Ms):
    R = zero3()
    for M in Ms:
        R = [[R[i][j] + M[i][j] for j in range(3)] for i in range(3)]
    return R


def msc3(c, M):
    return [[c * M[i][j] for j in range(3)] for i in range(3)]


def conj3(M):
    return [[M[i][j].conj() for j in range(3)] for i in range(3)]


def dag3(M):
    return [[M[j][i].conj() for j in range(3)] for i in range(3)]


def tr3(M):
    return M[0][0] + M[1][1] + M[2][2]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def charpoly(Hm):
    m2 = sum((Hm[i][i] * Hm[j][j] - Hm[i][j] * Hm[j][i] for i in range(3) for j in range(i + 1, 3)), q(0))
    return (tr3(Hm), m2, det3(Hm))


def herm(M):
    return mmul(M, dag3(M))


def eq3(A, B):
    return all(A[i][j] == B[i][j] for i in range(3) for j in range(3))


def sym3(d0, d1, d2, o01, o02, o12):
    return [[d0, o01, o02], [o01, d1, o12], [o02, o12, d2]]


def ant3(o01, o02, o12):
    return [[q(0), o01, o02], [-o01, q(0), o12], [-o02, -o12, q(0)]]


def axial(A):
    """A_ij = eps_ijk a_k."""
    return [A[1][2], A[2][0], A[0][1]]


def masses(srcs):
    """srcs: (beta, down weight, up weight, Y) -> (M_d, M_u) under the conjugate reading."""
    Md = madd3(*[msc3(b * d, Y) for b, d, u, Y in srcs])
    Mu = madd3(*[msc3(b.conj() * u, Y) for b, d, u, Y in srcs])
    return Md, Mu


def trace_law(srcs):
    tot = F(0)
    for bk, dk, uk, Yk in srcs:
        for bl, dl, ul, Yl in srcs:
            ek, ok, el, ol = (dk + uk) / 2, (dk - uk) / 2, (dl + ul) / 2, (dl - ul) / 2
            t, p = tr3(mmul(Yk, dag3(Yl))), bk * bl.conj()
            tot += -2 * (ek * ol + ok * el) * t.re * p.re + 2 * (ek * el + ok * ol) * t.im * p.im
    return tot


# fixed instances (complex symmetric, complex antisymmetric, real, and frame coefficients)
Y1 = sym3(q(2, 1), q(3), q(1, -1), q(1), q(-1, 2), q(0, 1))
Y2 = sym3(q(1), q(-1, 1), q(2), q(2, -1), q(0), q(3))
A1 = ant3(q(1, 1), q(2), q(-1, 3))
A2 = ant3(q(0, 2), q(1, -1), q(1))
R1 = sym3(q(1), q(-1), q(3), q(2), q(0), q(1))
R2 = sym3(q(2), q(1), q(1), q(0), q(1), q(-1))
RA = ant3(q(1), q(-2), q(1))
OMEGA = q(2, -1)
B1, B2, B3 = q(3, 1), q(1, -2), q(-2, 1)


def module_weights():
    """(lep, qrk) down and up weights of the named weightings, symmetric and antisymmetric parts."""
    X4 = msc(F(8), mm(MUR, MUP))
    P4 = madd(msc(F(4), mm(MUP, MUP)), msc(F(-3, 64), ONE))
    named = {"10": ONE, "BL": BL, "BL2": mm(BL, BL), "chi": CHI, "muP": MUP, "P4": P4,
             "T3R": T3R, "muR": MUR, "X4": X4, "T3R.BL2": mm(T3R, mm(BL, BL))}
    out = {}
    for name, g in named.items():
        for part in (0, 1):
            d, u = ud(g, part)
            if d is None or u is None:
                out[(name, part)] = "off-pattern"
            elif d == {} and u == {}:
                out[(name, part)] = None
            else:
                out[(name, part)] = (single(d), single(u))
    return out


def check_symmetric_and_antisymmetric_entries_are_e_plus_o_and_e_minus_o():
    """On the sixteen, for diagonal weightings h(T3R, B - L), both the symmetric (10 and 126 type) and the
    antisymmetric (120 type) entries of the composite are e + o (down-type) and e - o (up-type), e and o
    from the parts of h even and odd in T3R; checked against hand-tabulated weights, with the antisymmetric
    weight the half-difference of h between singlet and doublet."""
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.yukawa-pattern-two-rung-module")
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.generation-ten-under-pati-salam")
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    premise("synthesis.georgi-jarlskog-majorana-moment-map")
    premise("synthesis.up-down-split-under-conjugate-reading-needs-su2r-odd-weighting")
    GA.check("the sixteen is the even half", all(len(s) % 2 == 0 for s in SIXTEEN) and len(SIXTEEN) == 16)
    GA.check("T3R = 4 mu_R", T3R == msc(F(4), MUR))
    w = module_weights()
    # T3R-even weightings: up = down, hand values (lep, qrk)
    even = {("10", 0): (F(1), F(1)), ("BL2", 0): (F(1), F(1, 9)), ("P4", 0): (F(3, 32), F(-1, 32)),
            ("BL", 1): (F(1), F(-1, 3)), ("chi", 1): (F(-1), F(-1)), ("muP", 1): (F(-3, 16), F(1, 16))}
    for key, val in even.items():
        GA.check("T3R-even %s part %s: down = up = %s" % (key[0], key[1], val), w[key] == (val, val))
    # T3R-odd weightings: up = -down, in both parts
    odd = {"T3R": (F(1, 4), F(1, 4)), "muR": (F(1, 16), F(1, 16)), "X4": (F(-3, 32), F(1, 32)),
           "T3R.BL2": (F(1, 4), F(1, 36))}
    for name, val in odd.items():
        for part in (0, 1):
            GA.check("T3R-odd %s part %s: down %s, up = -down" % (name, part, val),
                     w[(name, part)] == (val, (-val[0], -val[1])))
    # the complementary parts vanish: 10, P4, BL2 have no antisymmetric entry; BL, chi, muP no symmetric one
    GA.check("no antisymmetric part of the 10, P4, (B-L)^2",
             w[("10", 1)] is None and w[("P4", 1)] is None and w[("BL2", 1)] is None)
    GA.check("no symmetric part of B-L, chi, mu_P",
             w[("BL", 0)] is None and w[("chi", 0)] is None and w[("muP", 0)] is None)
    return True


def check_one_rung_vector_gives_proportional_mass_matrices():
    """Every T3R-even composite of ONE rung vector (10, P4, and the antisymmetric B-L, chi, mu_P entries),
    each with its own complex family matrix: conj(beta) M_d = beta M_u in both sectors, so equal spectra and
    V = 1; adding one T3R-odd composite (mu_R) breaks the proportionality."""
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("standard-model.imported-spinor-bilinears")
    premise("synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing")
    w = module_weights()
    for sec in (0, 1):
        srcs = []
        for (name, part), Y in ((("10", 0), Y1), (("P4", 0), Y2), (("muP", 1), A1), (("chi", 1), A2), (("BL", 1), RA)):
            (dl, dq), (ul, uq) = w[(name, part)]
            srcs.append((B1, (dl, dq)[sec], (ul, uq)[sec], Y))
        Md, Mu = masses(srcs)
        GA.check("sector %s: conj(beta) M_d = beta M_u" % sec, eq3(msc3(B1, Mu), msc3(B1.conj(), Md)))
        GA.check("sector %s: H_u = H_d" % sec, eq3(herm(Mu), herm(Md)))
        (dl, dq), (ul, uq) = w[("muR", 0)]
        Md2, Mu2 = masses(srcs + [(B1, (dl, dq)[sec], (ul, uq)[sec], R2)])
        GA.check("sector %s: a T3R-odd composite splits" % sec, charpoly(herm(Mu2)) != charpoly(herm(Md2)))
    Md, Mu = masses([(B1, F(1), F(1), Y1), (B1, F(-1, 32), F(-1, 32), Y2)])
    GA.check("instance value tr H_d (10 + P4, quarks)", tr3(herm(Md)) == q(F(152175, 512)))
    return True


def check_relatively_real_family_matrices_give_conjugate_squares():
    """Several rung vectors with independent complex frame coefficients, T3R-even composites, family matrices
    omega R_k with R_k real: H_u = conj(H_d), equal characteristic polynomials (equal masses family by family),
    while [H_u, H_d] has nonzero determinant (the mixing is not trivial and the Jarlskog invariant is not zero)."""
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("standard-model.imported-spinor-bilinears")
    premise("synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing")
    srcs = [(B1, F(1), F(1), msc3(OMEGA, R1)), (B2, F(-1, 32), F(-1, 32), msc3(OMEGA, R2)),
            (B3, F(-1), F(-1), msc3(OMEGA, RA))]
    Md, Mu = masses(srcs)
    Hd, Hu = herm(Md), herm(Mu)
    GA.check("M_u = (omega / conj omega) conj(M_d)", eq3(msc3(OMEGA.conj(), Mu), msc3(OMEGA, conj3(Md))))
    GA.check("H_u = conj(H_d)", eq3(Hu, conj3(Hd)))
    GA.check("equal characteristic polynomials", charpoly(Hu) == charpoly(Hd))
    GA.check("tr H_d = 691005/512", tr3(Hd) == q(F(691005, 512)))
    C = madd3(mmul(Hu, Hd), msc3(q(-1), mmul(Hd, Hu)))
    GA.check("det [H_u, H_d] is nonzero (nontrivial mixing, J != 0)", det3(C) != q(0) and det3(C).re == 0)
    return True


def check_trace_law_two_channels():
    """tr H_u - tr H_d = -2 sum (e_k o_l + o_k e_l) Re t_kl Re p_kl + 2 sum (e_k e_l + o_k o_l) Im t_kl Im p_kl,
    t_kl = tr(Y_k Y_l^dag), p_kl = beta_k conj(beta_l): on a mixed instance (two 10s, mu_R, X4, 120-type
    entries) and on one rung vector with real matrices (the T3R-odd channel alone)."""
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("standard-model.imported-spinor-bilinears")
    srcs = [(B1, F(1), F(1), Y1), (B2, F(1, 16), F(-1, 16), Y2), (B3, F(-3, 32), F(3, 32), Y1),
            (B2, F(1, 16), F(1, 16), A1), (B1, F(1, 4), F(-1, 4), A2)]
    Md, Mu = masses(srcs)
    dif = tr3(herm(Mu)) - tr3(herm(Md))
    GA.check("trace law on the mixed instance", dif.im == 0 and dif.re == trace_law(srcs))
    GA.check("value -1843/32", dif == q(F(-1843, 32)))
    one = [(B1, F(1), F(1), R1), (B1, F(1, 16), F(-1, 16), R2)]
    Md, Mu = masses(one)
    dif = tr3(herm(Mu)) - tr3(herm(Md))
    GA.check("T3R-odd channel alone: -4 |beta|^2 e o Re t = -5", dif == q(-5) and trace_law(one) == -5)
    cp = [(B1, F(1), F(1), Y1), (B2, F(1), F(1), Y2)]
    Md, Mu = masses(cp)
    t12, p12 = tr3(mmul(Y1, dag3(Y2))), B1 * B2.conj()
    GA.check("CP channel alone: 4 Im t_12 Im p_12", tr3(herm(Mu)) - tr3(herm(Md)) == q(4 * t12.im * p12.im))
    GA.check("t between a symmetric and an antisymmetric matrix vanishes", tr3(mmul(Y1, dag3(A1))) == q(0))
    return True


def check_ten_plus_120_keeps_the_trace_and_splits_the_determinant():
    """One symmetric source (a 10) and one antisymmetric source (a 120-type entry), any complex data:
    tr H_u = tr H_d; det(x S + y A) = x^3 det S + x y^2 a^T S a; and
    det H_u - det H_d = -4 |beta|^2 Im(det S conj(a^T S a)) Im((conj(beta) gamma)^2), which vanishes when the
    relative phase of the two frame coefficients is a multiple of pi/2."""
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("standard-model.imported-spinor-bilinears")
    G = q(1, 3)
    S, A = Y1, msc3(q(F(1, 16)), A1)
    Md, Mu = masses([(B1, F(1), F(1), Y1), (G, F(1, 16), F(1, 16), A1)])
    Hd, Hu = herm(Md), herm(Mu)
    GA.check("tr H_u = tr H_d", tr3(Hu) == tr3(Hd))
    a = axial(A)
    qa = sum((a[i] * S[i][j] * a[j] for i in range(3) for j in range(3)), q(0))
    DS = det3(S)
    GA.check("det(x S + y A) = x^3 D + x y^2 q", det3(madd3(msc3(B1, S), msc3(G, A))) == B1 * B1 * B1 * DS + B1 * G * G * qa)
    bg = B1.conj() * G
    law = -4 * (B1 * B1.conj()).re * (DS * qa.conj()).im * (bg * bg).im
    GA.check("determinant law", det3(Hu) - det3(Hd) == q(law) and law == -13770)
    Md, Mu = masses([(B1, F(1), F(1), Y1), (B1 * q(0, 2), F(1, 16), F(1, 16), A1)])
    GA.check("relative phase pi/2: equal determinants", det3(herm(Mu)) == det3(herm(Md)))
    return True


def check_second_ten_splits_only_through_the_cp_channel():
    """Two 10s with independent complex family matrices and frame coefficients of different phase: different
    characteristic polynomials and det [H_u, H_d] != 0; with aligned frame coefficients M_u is proportional to
    M_d, and with real family matrices the spectra are equal."""
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing")
    Md, Mu = masses([(B1, F(1), F(1), Y1), (B2, F(1), F(1), Y2)])
    Hd, Hu = herm(Md), herm(Mu)
    GA.check("split: char. polynomials (541, 48650, 450157) and (429, 52626, 1463813)",
             charpoly(Hu) == (q(541), q(48650), q(450157)) and charpoly(Hd) == (q(429), q(52626), q(1463813)))
    C = madd3(mmul(Hu, Hd), msc3(q(-1), mmul(Hd, Hu)))
    GA.check("det [H_u, H_d] = 809153063376 i", det3(C) == q(0, 809153063376))
    Md, Mu = masses([(B1, F(1), F(1), Y1), (B1 * q(F(3, 2)), F(1), F(1), Y2)])
    GA.check("aligned frame coefficients: beta M_u = conj(beta) M_d", eq3(msc3(B1, Mu), msc3(B1.conj(), Md)))
    Md, Mu = masses([(B1, F(1), F(1), R1), (B2, F(1), F(1), R2)])
    GA.check("real family matrices: equal spectra", charpoly(herm(Mu)) == charpoly(herm(Md)))
    return True
