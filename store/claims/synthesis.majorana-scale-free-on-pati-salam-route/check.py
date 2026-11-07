"""synthesis.majorana-scale-free-on-pati-salam-route: exact checks.

Complex rational 3 x 3 matrices (GA.QI). Two 10 couplings Y1, Y2 (symmetric), one 126 coupling f
(symmetric), one 120 coupling h (antisymmetric), complex rational vevs, as in the imported Clebsch
structure:
M_u = sum v_u^a Y_a + w_u f + c_u h,   M_nu = sum v_u^a Y_a - 3 w_u f + c_nu h,
M_d = sum v_d^a Y_a + w_d f + c_d h,   M_e  = sum v_d^a Y_a - 3 w_d f + c_e h,
M_R = v_R f,   m_nu = -M_nu M_R^{-1} M_nu^T.
The one-parameter group acts by f -> lam f, (w_u, w_d) -> (w_u/lam, w_d/lam), everything else fixed.
pi enters only through the rational bound pi > 3.
"""
import GA
from GA import QI, qi
from tp_premise import premise
from fractions import Fraction as F

N3 = range(3)
ZERO = qi(0)


def mat(rows):
    return [[x if isinstance(x, QI) else qi(x) for x in r] for r in rows]


def madd(*Ms):
    return [[sum((M[i][j] for M in Ms), ZERO) for j in N3] for i in N3]


def msc(c, A):
    c = c if isinstance(c, QI) else qi(c)
    return [[c * A[i][j] for j in N3] for i in N3]


def tr(A):
    return [[A[j][i] for j in N3] for i in N3]


def dag(A):
    return [[A[j][i].conj() for j in N3] for i in N3]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in N3), ZERO) for j in N3] for i in N3]


def minv(A):
    cols = []
    for j in N3:
        e = [qi(1) if i == j else ZERO for i in N3]
        cols.append(GA.field_solve(A, e))
    return [[cols[j][i] for j in N3] for i in N3]


def trace(A):
    return sum((A[i][i] for i in N3), ZERO)


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def mv(A, x):
    return [sum((A[i][j] * x[j] for j in N3), ZERO) for i in N3]


def quad(A, x, y):
    return sum((x[i] * mv(A, y)[i] for i in N3), ZERO)


def clebsch(Y, f, h, v_u, v_d, w_u, w_d, c):
    ten_u = madd(*[msc(v_u[a], Y[a]) for a in range(len(Y))])
    ten_d = madd(*[msc(v_d[a], Y[a]) for a in range(len(Y))])
    Mu = madd(ten_u, msc(w_u, f), msc(c[0], h))
    Mn = madd(ten_u, msc(w_u * qi(-3), f), msc(c[1], h))
    Md = madd(ten_d, msc(w_d, f), msc(c[2], h))
    Me = madd(ten_d, msc(w_d * qi(-3), f), msc(c[3], h))
    return Mu, Mn, Md, Me


def light(Mn, MR):
    return msc(-1, mmul(mmul(Mn, minv(MR)), tr(Mn)))


def _data():
    Y1 = mat([[qi(2, 1), qi(-1), qi(3, -2)], [qi(-1), qi(5), qi(0, 1)], [qi(3, -2), qi(0, 1), qi(-4, 3)]])
    Y2 = mat([[qi(1), qi(2, 2), qi(-1)], [qi(2, 2), qi(-3, 1), qi(7)], [qi(-1), qi(7), qi(1, -1)]])
    f = mat([[qi(3), qi(1, -1), qi(2)], [qi(1, -1), qi(-2, 5), qi(-1, 1)], [qi(2), qi(-1, 1), qi(6, 1)]])
    h = mat([[0, qi(1, 2), qi(-3)], [qi(-1, -2), 0, qi(2, -1)], [qi(3), qi(-2, 1), 0]])
    v_u, v_d = [qi(3, 1), qi(-2)], [qi(1, -1), qi(5, 2)]
    w_u, w_d = qi(F(2, 7), 1), qi(-1, F(1, 3))
    c = [qi(1), qi(-2, 3), qi(0, 4), qi(5, -1)]
    v_R = qi(11, 0)
    return [Y1, Y2], f, h, v_u, v_d, w_u, w_d, c, v_R


DATA = _data()
LAMS = [qi(F(7, 3)), qi(2, 1), qi(F(-1, 5), F(3, 4))]


def scaled(lam):
    Y, f, h, v_u, v_d, w_u, w_d, c, v_R = DATA
    return Y, msc(lam, f), h, v_u, v_d, w_u / lam, w_d / lam, c, v_R


def check_dirac_matrices_invariant_majorana_scales():
    premise("standard-model.imported-clebsch-structure-seesaw")
    Y, f, h, v_u, v_d, w_u, w_d, c, v_R = DATA
    base = clebsch(Y, f, h, v_u, v_d, w_u, w_d, c)
    MR = msc(v_R, f)
    for lam in LAMS:
        Y_, f_, h_, vu_, vd_, wu_, wd_, c_, vR_ = scaled(lam)
        new = clebsch(Y_, f_, h_, vu_, vd_, wu_, wd_, c_)
        GA.check("four Dirac matrices invariant", all(new[k] == base[k] for k in range(4)))
        GA.check("M_R -> lam M_R", msc(vR_, f_) == msc(lam, MR))
    # control: scaling f alone (w fixed) moves every Dirac matrix
    Y, f, h, v_u, v_d, w_u, w_d, c, v_R = DATA
    bad = clebsch(Y, msc(LAMS[0], f), h, v_u, v_d, w_u, w_d, c)
    GA.check("control: f alone is not a symmetry", bad[0] != base[0] and bad[3] != base[3])
    return True


def check_light_masses_scale_mixing_invariant():
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("neutrino.rank-one-seesaw-ordering-sum-double")
    Y, f, h, v_u, v_d, w_u, w_d, c, v_R = DATA
    _, Mn, _, _ = clebsch(Y, f, h, v_u, v_d, w_u, w_d, c)
    m0 = light(Mn, msc(v_R, f))
    H0 = mmul(m0, dag(m0))
    I1, I2, I3 = trace(H0), trace(mmul(H0, H0)), det3(H0)
    GA.check("nondegenerate light matrix", I3 != ZERO)
    for lam in LAMS:
        Y_, f_, h_, vu_, vd_, wu_, wd_, c_, vR_ = scaled(lam)
        _, Mn_, _, _ = clebsch(Y_, f_, h_, vu_, vd_, wu_, wd_, c_)
        m = light(Mn_, msc(vR_, f_))
        GA.check("m_nu -> m_nu / lam", msc(lam, m) == m0)
        H = mmul(m, dag(m))
        a2 = lam * lam.conj()
        GA.check("H -> H/|lam|^2: eigenvectors (mixing) unchanged", msc(a2, H) == H0)
        J1, J2, J3 = trace(H), trace(mmul(H, H)), det3(H)
        GA.check("scale-free invariants I2/I1^2, I3/I1^3 unchanged (mass ratios)",
                 J2 * I1 * I1 == I2 * J1 * J1 and J3 * I1 * I1 * I1 == I3 * J1 * J1 * J1)
        GA.check("overall scale moves: I1 -> I1/|lam|^2", J1 * a2 == I1 and J1 != I1)
    # explicit scale 2: I1 falls by 4 and the determinant by 64
    Y_, f_, h_, vu_, vd_, wu_, wd_, c_, vR_ = scaled(qi(2))
    _, Mn_, _, _ = clebsch(Y_, f_, h_, vu_, vd_, wu_, wd_, c_)
    H2 = mmul(light(Mn_, msc(vR_, f_)), dag(light(Mn_, msc(vR_, f_))))
    GA.check("scale 2: I1 -> I1/4, I3 -> I3/64", trace(H2) * 4 == I1 and det3(H2) * 64 == I3)
    return True


def check_ew_and_dirac_reading_of_u_invariant():
    premise("synthesis.majorana-scale-is-126-doublet-vev")
    premise("synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition")
    Y, f, h, v_u, v_d, w_u, w_d, c, v_R = DATA
    x = [qi(1)] * 3
    xx = sum((a * a for a in x), ZERO)
    m_t = qi(91)
    # impose (EW) along x: x^T M_nu x = 0 via v_u^1, then normalise the up sector so x^T M_u x = m_t x.x
    base_n = madd(msc(v_u[1], Y[1]), msc(w_u * qi(-3), f), msc(c[1], h))
    v1 = -quad(base_n, x, x) / quad(Y[0], x, x)
    vu = [v1, v_u[1]]
    Mu, Mn, Md, Me = clebsch(Y, f, h, vu, v_d, w_u, w_d, c)
    s = m_t * xx / quad(Mu, x, x)
    Y2 = [msc(s, Y[0]), msc(s, Y[1])]
    f2, h2, wu2 = f, msc(s, h), w_u * s
    vd2 = [v / s for v in v_d]
    wd2 = w_d / s
    Mu, Mn, Md, Me = clebsch(Y2, f2, h2, vu, vd2, wu2, wd2, c)
    GA.check("(EW) holds on the instance", quad(Mn, x, x) == ZERO and quad(Mu, x, x) == m_t * xx)
    MR = msc(v_R, f2)
    GA.check("heavy-direction entry m_t v_R x.x / 4 w_u", quad(MR, x, x) == v_R * m_t * xx / (wu2 * qi(4)))
    HD = mmul(Mn, dag(Mn))
    for lam in LAMS:
        Mu_, Mn_, Md_, Me_ = clebsch(Y2, msc(lam, f2), h2, vu, vd2, wu2 / lam, wd2 / lam, c)
        GA.check("(EW) invariant", quad(Mn_, x, x) == ZERO and quad(Mu_, x, x) == m_t * xx)
        GA.check("Dirac Gram matrix invariant (singular values, so (U) in its Dirac reading)",
                 mmul(Mn_, dag(Mn_)) == HD)
        GA.check("heavy entry scales by lam", quad(msc(v_R, msc(lam, f2)), x, x) == lam * quad(MR, x, x))
    return True


def check_fit_observables_one_scale():
    premise("standard-model.fits-record-level")
    premise("standard-model.imported-clebsch-structure-seesaw")
    # the eighteen fitted observables: nine charged masses, four CKM numbers (functions of M_u, M_d, M_e),
    # three lepton angles (eigenvectors of H and of M_e M_e^dag), m3/m2 (a ratio), m3 (a scale).
    # Under the group the first seventeen are invariant and m3 -> m3/|lam|: exactly one degree of freedom.
    Y, f, h, v_u, v_d, w_u, w_d, c, v_R = DATA
    Mu, Mn, Md, Me = clebsch(Y, f, h, v_u, v_d, w_u, w_d, c)
    m0 = light(Mn, msc(v_R, f))
    H0 = mmul(m0, dag(m0))
    invariant = 0
    scaling = 0
    for lam in LAMS[:1]:
        Y_, f_, h_, vu_, vd_, wu_, wd_, c_, vR_ = scaled(lam)
        Mu_, Mn_, Md_, Me_ = clebsch(Y_, f_, h_, vu_, vd_, wu_, wd_, c_)
        m = light(Mn_, msc(vR_, f_))
        H = mmul(m, dag(m))
        # charged masses and CKM: Gram matrices of M_u, M_d, M_e invariant (counts 9 + 4)
        if all(mmul(A, dag(A)) == mmul(B, dag(B)) for A, B in ((Mu_, Mu), (Md_, Md), (Me_, Me))):
            invariant += 13
        # lepton angles: H is a positive multiple of H0, so its eigenvectors coincide (counts 3)
        a2 = lam * lam.conj()
        if msc(a2, H) == H0:
            invariant += 3
        # m3/m2: ratio of eigenvalues of a multiple of H0 (counts 1); m3 itself scales (counts 1)
        if trace(mmul(H, H)) * trace(H0) * trace(H0) == trace(mmul(H0, H0)) * trace(H) * trace(H):
            invariant += 1
        if trace(H) != trace(H0):
            scaling += 1
    GA.check("17 fitted observables invariant, 1 (the scale m3) moves", invariant == 17 and scaling == 1)
    return True


def check_stored_inequalities_leave_an_interval():
    premise("standard-model.what-angle-asks-neutrino-sector")
    premise("standard-model.chain")
    premise("synthesis.majorana-scale-is-126-doublet-vev")
    # (M_R)_33 = f_33 v_R with f_33 = m_t/(4 w_u). Perturbativity f_33 <= 4 pi, and |w_u| <= v = 174 GeV.
    v_R = F(42, 1) * 10 ** 9           # 4.2e10 GeV
    v = F(174)
    pi_lo = F(3)
    lo_of = lambda m_t: m_t * v_R / (4 * v)           # |w_u| = v
    for m_t in (F(80), F(91), F(100)):
        lower = lo_of(m_t)
        upper_min = 4 * pi_lo * v_R                    # 4 pi v_R > 12 v_R
        GA.check("interval nonempty at m_t(M_I) = %s" % m_t, lower < upper_min)
        GA.check("width exceeds a factor 83 for m_t(M_I) <= 100", upper_min / lower > 83)
    GA.check("lower end 5.49e9 GeV at m_t = 91", F(549, 100) * 10 ** 9 < lo_of(F(91)) < F(550, 100) * 10 ** 9)
    # the seeding window (M_3 > 1.36e12 GeV, quoted, not used) lies above 4 pi v_R < (22/7) 4 v_R = 5.28e11
    GA.check("seeding window disjoint from the interval", F(22, 7) * 4 * v_R < F(136, 100) * 10 ** 12)
    return True


def check_electroweak_normalisation_restored():
    premise("standard-model.imported-clebsch-structure-seesaw")
    # S = sum |v^a|^2 + |w_u|^2 + |w_d|^2 (120 terms fixed) changes under g_lam; rescaling the first 10,
    # (Y_1, v^1) -> (mu Y_1, v^1/mu), fixes every Dirac matrix, and a real mu > 0 restores S.
    Y, f, h, v_u, v_d, w_u, w_d, c, v_R = DATA
    n2 = lambda z: (z * z.conj()).re
    base = clebsch(Y, f, h, v_u, v_d, w_u, w_d, c)
    S = sum(n2(z) for z in v_u + v_d) + n2(w_u) + n2(w_d)
    for lam in LAMS:
        a2 = n2(lam)
        need = S - sum(n2(z) for z in (v_u[1], v_d[1])) - (n2(w_u) + n2(w_d)) / a2
        inv_mu2 = need / (n2(v_u[0]) + n2(v_d[0]))
        GA.check("a real mu restores the normalisation (1/mu^2 > 0)", inv_mu2 > 0)
        GA.check("normalisation moved by g_lam alone", (n2(w_u) + n2(w_d)) / a2 != n2(w_u) + n2(w_d))
        for mu in (qi(F(3, 2)), qi(F(5, 7))):
            Yc = [msc(mu, Y[0]), Y[1]]
            vuc = [v_u[0] / mu, v_u[1]]
            vdc = [v_d[0] / mu, v_d[1]]
            new = clebsch(Yc, msc(lam, f), h, vuc, vdc, w_u / lam, w_d / lam, c)
            GA.check("composite fixes every Dirac matrix", all(new[k] == base[k] for k in range(4)))
    return True
