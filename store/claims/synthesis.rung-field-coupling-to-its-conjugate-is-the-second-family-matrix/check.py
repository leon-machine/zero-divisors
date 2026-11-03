"""synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix: exact checks.

The general coupling of the sixteen to the complex rung field c = alpha v_4 + beta w_4 (on a frame where the
charge-preserving vev lies along rung 4) has a family matrix Y on c and a family matrix Yt on its conjugate
c* = conj(beta) v_4 + conj(alpha) w_4. Down-type entries are read from the w_4 coefficients and up-type
entries from the v_4 coefficients (the stored Yukawa pattern, checked on the 32 x 32 module), so
M_d = beta Y + conj(alpha) Yt and M_u = alpha Y + conj(beta) Yt. Family matrices are 3 x 3 Gaussian-rational
(GA.QI); N = (|alpha|^2 + |beta|^2)/2, m = (|alpha|^2 - |beta|^2)/2 and Q = alpha beta are the rung field's
Hermitian norm, hypercharge moment map and complex-bilinear form. Frames lambda are sampled rationals with
H = 1 (Hubble units), c_lambda = -lambda w_4 + (H^2/lambda) v_4.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from GA import QI
import fock
from tp_premise import premise

NM = 5
STATES = [s for k in range(NM + 1) for s in combinations(range(NM), k)]
IDX = {s: sum(1 << x for x in s) for s in STATES}
mm, madd, msc, tr = fock.mm, fock.madd, fock.msc, fock.transpose
V = [fock.cre(m, NM) for m in range(NM)]
W = [tr(v) for v in V]
W4, V4 = W[3], V[3]
SIXTEEN = [s for s in STATES if len(s) % 2 == 0]
BMAT = {}
for _s in STATES:
    _comp = tuple(x for x in range(NM) if x not in _s)
    _seq = list(_s) + list(_comp)
    _inv = sum(1 for i in range(NM) for j in range(i + 1, NM) if _seq[i] > _seq[j])
    _k = len(_s)
    BMAT[(IDX[_s], IDX[_comp])] = F((-1) ** (_k * (_k - 1) // 2) * (-1) ** _inv)


def sym_form(X):
    BX = mm(BMAT, X)
    out = {}
    for a in SIXTEEN:
        for b in SIXTEEN:
            v = (BX.get((IDX[a], IDX[b]), 0) + BX.get((IDX[b], IDX[a]), 0)) * F(1, 2)
            if v:
                out[(a, b)] = v
    return out


S10D, S10U = sym_form(W4), sym_form(V4)


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


def nrm(Y):
    return tr3(herm(Y)).re


def masses(alpha, beta, Y, Yt):
    Md = madd3(msc3(beta, Y), msc3(alpha.conj(), Yt))
    Mu = madd3(msc3(alpha, Y), msc3(beta.conj(), Yt))
    return Md, Mu


def invariants(alpha, beta):
    a2, b2 = (alpha * alpha.conj()).re, (beta * beta.conj()).re
    return (a2 + b2) / 2, (a2 - b2) / 2, alpha * beta


Y = [[q(2, 1), q(1), q(-1, 2)], [q(1), q(3), q(0, 1)], [q(-1, 2), q(0, 1), q(1, -1)]]
YT = [[q(1), q(2, -1), q(0)], [q(1, 1), q(-1, 1), q(3)], [q(0, -2), q(3), q(2)]]
CPLX = ((q(2, 1), q(-1, 3)), (q(1, -1), q(4)), (q(0, 3), q(F(1, 2), -1)))
FRAMES = (F(3), F(7), F(1, 5), F(9, 2))


def check_mass_entries_of_c_and_its_conjugate_on_the_module():
    """On the sixteen, the symmetric form of c_lambda = -lambda w_4 + (H^2/lambda) v_4 is -lambda times the
    down-type 10 form plus (H^2/lambda) times the up-type one, and that of its conjugate
    c_lambda* = -lambda v_4 + (H^2/lambda) w_4 the reverse: through c the up entry is H^2/lambda and the down
    entry lambda in size, through c* both are swapped."""
    premise("standard-model.yukawa-pattern-two-rung-module")
    premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.hyp-s-slot-statistics")
    premise("synthesis.rung-field-on-the-lift-locus")
    GA.check("down and up 10 forms live on disjoint pairs", not set(S10D) & set(S10U) and len(S10D) == len(S10U))
    for lam in FRAMES:
        c = madd(msc(-lam, W4), msc(1 / lam, V4))
        cs = madd(msc(-lam, V4), msc(1 / lam, W4))
        fc, fs = sym_form(c), sym_form(cs)
        GA.check("frame %s: c gives down -lambda, up 1/lambda" % lam,
                 all(fc[k] == -lam * v for k, v in S10D.items()) and all(fc[k] == v / lam for k, v in S10U.items()))
        GA.check("frame %s: c* gives down 1/lambda, up -lambda" % lam,
                 all(fs[k] == v / lam for k, v in S10D.items()) and all(fs[k] == -lam * v for k, v in S10U.items()))
    return True


def check_conjugate_transforms_like_the_field():
    """Under X in U(2) acting by alpha -> X alpha, beta -> conj(X) beta, the conjugate's coefficients
    (conj beta, conj alpha) transform the same way, so the coupling Yt c* is as allowed as Y c; sampled X."""
    premise("synthesis.rung-field-on-the-lift-locus")
    X = [[q(F(3, 5)), q(0, F(4, 5))], [q(0, F(4, 5)), q(F(3, 5))]]
    I2 = [[sum((X[i][k] * X[j][k].conj() for k in range(2)), q(0)) for j in range(2)] for i in range(2)]
    GA.check("X is unitary", I2 == [[q(1), q(0)], [q(0), q(1)]])
    al, be = [q(2, 1), q(-1, 3)], [q(1, -1), q(4)]

    def act(M, x):
        return [M[0][0] * x[0] + M[0][1] * x[1], M[1][0] * x[0] + M[1][1] * x[1]]
    Xb = [[X[i][j].conj() for j in range(2)] for i in range(2)]
    al2, be2 = act(X, al), act(Xb, be)
    GA.check("sample image X alpha = (-6/5 - i/5, -7/5 + 17i/5)", al2 == [q(F(-6, 5), F(-1, 5)), q(F(-7, 5), F(17, 5))])
    GA.check("v-coefficient of c* goes to X times itself", [z.conj() for z in be2] == act(X, [z.conj() for z in be]))
    GA.check("w-coefficient of c* goes to conj(X) times itself", [z.conj() for z in al2] == act(Xb, [z.conj() for z in al]))
    return True


def check_sum_rules_in_the_rung_invariants():
    """For every complex (alpha, beta) and family matrices Y, Yt:
    tr H_u - tr H_d = 2 m (|Y|^2 - |Yt|^2) and tr H_u + tr H_d = 2 N (|Y|^2 + |Yt|^2) + 4 Re(Q tr(Y Yt^dag));
    Yt = Y (the coupling to the real part c + c*) gives conj(z) M_d = z M_u with z = beta + conj(alpha)."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("standard-model.yukawa-pattern-two-rung-module")
    for alpha, beta in CPLX:
        Md, Mu = masses(alpha, beta, Y, YT)
        N, m, Qc = invariants(alpha, beta)
        Hu, Hd = herm(Mu), herm(Md)
        GA.check("difference rule", tr3(Hu) - tr3(Hd) == q(2 * m * (nrm(Y) - nrm(YT))))
        GA.check("sum rule", tr3(Hu) + tr3(Hd) == q(2 * N * (nrm(Y) + nrm(YT)) + 4 * (Qc * tr3(mmul(Y, dag3(YT)))).re))
        Md1, Mu1 = masses(alpha, beta, Y, Y)
        z = beta + alpha.conj()
        GA.check("Yt = Y: conj(z) M_d = z M_u", eq3(msc3(z.conj(), Md1), msc3(z, Mu1)))
    GA.check("norms |Y|^2 = 30, |Yt|^2 = 36", nrm(Y) == 30 and nrm(YT) == 36)
    return True


def check_lift_family_balanced_frame_and_the_c_share():
    """On the lift family (alpha = H^2/lambda, beta = -lambda, H = 1): M_d = -lambda Y + Yt/lambda,
    M_u = Y/lambda - lambda Yt; m = (1/lambda^2 - lambda^2)/2. At the balanced frame lambda = 1, M_u = -M_d for
    every Y, Yt. Off it, with r = e^{-2 eta} = 1/lambda^2, the part of M_u carried by the coupling to c is
    (H^2/lambda) Y = -(r M_d + r^2 M_u)/(1 - r^2), and that part's down-type partner -lambda Y is 1/r times it."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    Md, Mu = masses(q(1), q(-1), Y, YT)
    GA.check("balanced frame: M_u = -M_d", eq3(Mu, msc3(q(-1), Md)))
    GA.check("balanced frame: m = 0", invariants(q(1), q(-1))[1] == 0)
    for lam in FRAMES:
        Md, Mu = masses(q(1 / lam), q(-lam), Y, YT)
        r = 1 / (lam * lam)
        share = msc3(q(1 / lam), Y)
        GA.check("frame %s: c-share of M_u" % lam,
                 eq3(share, msc3(q(-1 / (1 - r * r)), madd3(msc3(q(r), Md), msc3(q(r * r), Mu)))))
        GA.check("frame %s: down partner of the c-share is 1/r times it" % lam,
                 eq3(msc3(q(-lam), Y), msc3(q(-1 / r), share)))
        GA.check("frame %s: m = -(lambda^2 - lambda^-2)/2" % lam,
                 invariants(q(1 / lam), q(-lam))[1] == (r - lam * lam) / 2)
    Md, Mu = masses(q(F(1, 3)), q(-3), Y, YT)
    GA.check("frame 3 values: tr H_u = 982/3, tr H_d = 274",
             tr3(herm(Mu)) == q(F(982, 3)) and tr3(herm(Md)) == q(274))
    return True


# ---------------------------------------------------------------- su(2)_R covariance and the charged pair
RUNG_BASIS = [V[3], V[4], W[3], W[4]]          # coefficients (alpha_4, alpha_5, beta_4, beta_5)
BIV1 = msc(F(1, 2), madd(mm(V[3], V[4]), mm(W[3], W[4])))
BIV2 = msc(F(1, 2), madd(mm(V[3], V[4]), msc(F(-1), mm(W[3], W[4]))))


def fcomm(A, B):
    return madd(mm(A, B), msc(F(-1), mm(B, A)))


def rung_coords(X):
    co = [X.get(next(iter(Bm)), F(0)) / Bm[next(iter(Bm))] for Bm in RUNG_BASIS]
    rec = madd(*[msc(c, Bm) for c, Bm in zip(co, RUNG_BASIS) if c])
    return co if fock.meq(rec, X) else None


def act4(M, c):
    """M[i] = coordinates of [b, basis_i]; c a list of 4 Gaussian rationals -> coordinates of [b, c]."""
    return [sum((c[i] * M[i][j] for i in range(4)), q(0)) for j in range(4)]


def star4(c):
    return [c[2].conj(), c[3].conj(), c[0].conj(), c[1].conj()]


def weak4(T, c):
    """alpha -> T alpha, beta -> conj(T) beta (2 x 2 Gaussian-rational T)."""
    a = [T[0][0] * c[0] + T[0][1] * c[1], T[1][0] * c[0] + T[1][1] * c[1]]
    b = [T[0][0].conj() * c[2] + T[0][1].conj() * c[3], T[1][0].conj() * c[2] + T[1][1].conj() * c[3]]
    return a + b


def per_sector(c):
    """per-sector entries: down from the beta half of c, up from the v-part of c*, i.e. conj of the beta half."""
    return [c[2], c[3]], [c[2].conj(), c[3].conj()]


def check_coupling_is_su2r_covariant_and_per_sector_reading_is_not():
    """The bivectors b_1 = (v_4 v_5 + w_4 w_5)/2 and b_2 = (v_4 v_5 - w_4 w_5)/2 act on rung vectors by commutator
    (R_1 = [b_1, .], R_2 = i [b_2, .]), leave the pairing B anti-invariant (so x -> M_x is equivariant), commute with
    the weak su(2) action and with the conjugation c -> c*, and [R_1, R_2] is the hypercharge action:
    so Y c + Yt c* is covariant under su(2)_L + su(2)_R. The per-sector reading vanishes on the alpha half, which
    R_1 carries into the beta half where the reading is injective: it is covariant for no action on the fermions."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    M1 = [rung_coords(fcomm(BIV1, x)) for x in RUNG_BASIS]
    M2 = [rung_coords(fcomm(BIV2, x)) for x in RUNG_BASIS]
    h = F(1, 2)
    GA.check("[b_1, .] on (v4, v5, w4, w5)", M1 == [[0, 0, 0, -h], [0, 0, h, 0], [0, -h, 0, 0], [h, 0, 0, 0]])
    GA.check("[b_2, .] on (v4, v5, w4, w5)", M2 == [[0, 0, 0, h], [0, 0, -h, 0], [0, -h, 0, 0], [h, 0, 0, 0]])
    for bb in (BIV1, BIV2):
        GA.check("B anti-invariant under the bivector", fock.meq(madd(mm(tr(bb), BMAT), mm(BMAT, bb)), {}))
        GA.check("M_[b, v4] = -(b^T B v4 + B v4 b)",
                 fock.meq(mm(BMAT, fcomm(bb, V[3])), msc(F(-1), madd(mm(mm(tr(bb), BMAT), V[3]), mm(mm(BMAT, V[3]), bb)))))

    def R1(c):
        return act4(M1, c)

    def R2(c):
        return [GA.QI_I * z for z in act4(M2, c)]
    Thalf = [[[q(0), q(0, h)], [q(0, h), q(0)]], [[q(0), q(h)], [q(-h), q(0)]], [[q(0, h), q(0)], [q(0), q(0, -h)]]]
    gens = [q(2, 1), q(-1, 3), q(1, -1), q(4)]
    for R in (R1, R2):
        GA.check("conjugation commutes", star4(R(gens)) == R(star4(gens)))
        for T in Thalf:
            GA.check("commutes with a weak generator", R(weak4(T, gens)) == weak4(T, R(gens)))
    c12 = [x - y for x, y in zip(R1(R2(gens)), R2(R1(gens)))]
    hyp = [q(0, h) * gens[0], q(0, h) * gens[1], q(0, -h) * gens[2], q(0, -h) * gens[3]]
    GA.check("[R_1, R_2] = hypercharge action (i/2 on alpha, -i/2 on beta)", c12 == hyp)
    pure_alpha = [q(2, 1), q(-1, 3), q(0), q(0)]
    d0, u0 = per_sector(pure_alpha)
    d1, u1 = per_sector(R1(pure_alpha))
    GA.check("per-sector reading kills the alpha half", d0 == [q(0), q(0)] and u0 == [q(0), q(0)])
    GA.check("R_1 carries it into the beta half: per-sector entries (-1/2 + 3i/2, -1 - i/2)",
             d1 == [q(F(-1, 2), F(3, 2)), q(-1, F(-1, 2))] and u1 == [z.conj() for z in d1])
    return True


def charged_ratios(lam, Yc, Ytc):
    """normalised (per N) squared Yukawa weight of the charged direction alpha' = (0, 1), beta' = (0, r), relative
    to that of the vev c_lambda, for the covariant coupling (one family, scalars Yc, Ytc), down and up."""
    r = 1 / (lam * lam)
    al, be = [q(1 / lam), q(0)], [q(-lam), q(0)]
    ap, bp = [q(0), q(1)], [q(0), q(r)]

    def entries(a, b, k):
        return b[k] * Yc + a[k].conj() * Ytc, a[k] * Yc + b[k].conj() * Ytc

    def nn(a, b):
        return sum(((z * z.conj()).re for z in a + b), F(0)) / 2
    dv, uv = entries(al, be, 0)
    dc, uc = entries(ap, bp, 1)
    w = lambda z: (z * z.conj()).re
    return (w(dc) / nn(ap, bp)) / (w(dv) / nn(al, be)), (w(uc) / nn(ap, bp)) / (w(uv) / nn(al, be))


def check_charged_pair_couples_at_yukawa_strength_under_the_covariant_coupling():
    """At c_lambda (H = 1) the direction alpha' = (0, a), beta' = (0, r conj a), r = 1/lambda^2, is tangent to the
    locus Q = -1, orthogonal (Re of the Hermitian product) to the gauge-orbit tangents and to the neutral line:
    it is the charged plane. Under Y c + Yt c* its normalised down and up weights relative to the vev's are
    |Yt + r Y|^2/|Y - r Yt|^2 and |Y + r Yt|^2/|Yt - r Y|^2 (361/49 and 121/289 at lambda = 3, Y = 1, Yt = 2),
    of order one; the per-sector reading gives r^2 for both."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("standard-model.yukawa-pattern-two-rung-module")
    lam = F(3)
    r = 1 / (lam * lam)
    al, be = [q(1 / lam), q(0)], [q(-lam), q(0)]
    h = F(1, 2)
    Ts = [[[q(0), q(0, h)], [q(0, h), q(0)]], [[q(0), q(h)], [q(-h), q(0)]], [[q(0, h), q(0)], [q(0), q(0, -h)]],
          [[q(0, h), q(0)], [q(0), q(0, h)]]]

    def mv(T, x):
        return [T[0][0] * x[0] + T[0][1] * x[1], T[1][0] * x[0] + T[1][1] * x[1]]

    def herm_re(a1, b1, a2, b2):
        return sum(((x.conj() * y).re for x, y in zip(a1 + b1, a2 + b2)), F(0)) / 2
    tangents = [(mv(T, al), mv([[z.conj() for z in row] for row in T], be)) for T in Ts]
    neutral = ([q(-1 / (lam * lam)), q(0)], [q(-1), q(0)])
    for a in (q(1), q(0, 1), q(2, -3)):
        ap, bp = [q(0), a], [q(0), q(r) * a.conj()]
        GA.check("tangent to Q = -1", ap[0] * be[0] + ap[1] * be[1] + al[0] * bp[0] + al[1] * bp[1] == q(0))
        GA.check("orthogonal to the gauge orbit and the neutral line",
                 all(herm_re(ta, tb, ap, bp) == 0 for ta, tb in tangents) and herm_re(neutral[0], neutral[1], ap, bp) == 0)
    GA.check("covariant coupling, lambda = 3, Y = 1, Yt = 2: (361/49, 121/289)",
             charged_ratios(lam, q(1), q(2)) == (F(361, 49), F(121, 289)))
    for lam2 in FRAMES:
        rr = 1 / (lam2 * lam2)
        for Yc, Ytc in ((q(1), q(2)), (q(2, 1), q(-1, 3))):
            dn, up = charged_ratios(lam2, Yc, Ytc)
            w = lambda z: (z * z.conj()).re
            GA.check("frame %s: down |Yt + rY|^2/|Y - rYt|^2, up |Y + rYt|^2/|Yt - rY|^2" % lam2,
                     dn == w(Ytc + q(rr) * Yc) / w(Yc - q(rr) * Ytc) and up == w(Yc + q(rr) * Ytc) / w(Ytc - q(rr) * Yc))
        dn, up = charged_ratios(lam2, q(1), q(0))
        GA.check("frame %s: Yt = 0 (per-sector-like down coupling) gives r^2 down" % lam2, dn == rr * rr)
    return True
