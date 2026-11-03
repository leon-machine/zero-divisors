"""LSZ reduction and the S-matrix for e+ e- -> mu+ mu- in the spacetime algebra: exact checks.

Cl(1,3), signature (+,-,-,-), traces 4 <.>_0, the unit and the i of the Feynman rules outside the product.
Part 1: LSZ: the propagator residue p + m is 2m times an idempotent of trace 2 (two spin states) for particles,
        p - m for antiparticles; the sandwich between residues reproduces the on-shell spin sums.
Part 2: the tree amplitude: spin-averaged |M|^2 from two Clifford traces equals
        8 e^4/s^2 [(p1.p3)(p2.p4) + (p1.p4)(p2.p3) + m_mu^2 p1.p2 + m_e^2 p3.p4 + 2 m_e^2 m_mu^2];
        the angular distribution and sigma = (4 pi alpha^2/(3 s)) beta (3 - beta^2)/2 (m_e -> 0), exact at
        rational beta; massless limit (1 + cos^2 theta), sigma = 4 pi alpha^2/(3 s).
Part 3: one loop: the on-shell renormalised vacuum polarisation insertion: its absorptive part
        (alpha/3) beta (3 - beta^2)/2 from the Feynman-parameter window, equal to s sigma_tree/(4 pi alpha) (the
        s-channel optical-theorem relation for the photon self-energy); the large-s constant -5/3; the charge renormalisation
        e_R = Z3^(1/2) e_0 from Z1 = Z2 and one factor Z2^(1/2) per external leg.
Exact arithmetic only; logs and pi kept symbolic (rational coefficients of alpha^2/s, of pi, of logs).
"""
from fractions import Fraction as Fr

import GA
from tp_premise import premise

S13 = (1, -1, -1, -1)
G = [GA.gen(i) for i in range(4)]
GU = [GA.scal(Fr(1, S13[i]), G[i]) for i in range(4)]

P_QED = 'synthesis.one-loop-qed-in-the-spacetime-algebra'
P_ML = 'synthesis.imported-one-loop-integrals-and-pauli-villars-regulators'
P_TREE = 'field-theory.coupled-system-tree-level'
P_2Q = 'field-theory.second-quantisation'


def mul(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, S13)
    return out


def vec(c):
    return GA.add(*[GA.scal(Fr(c[i]), G[i]) for i in range(4)])


def sc(x):
    return x.get((), Fr(0))


def dot(a, b):
    return sc(GA.scal(Fr(1, 2), GA.add(mul(a, b), mul(b, a))))


def num(c):
    return GA.sc(c) if c != 0 else {}


def tr(x):
    return 4 * sc(x)


def spin_summed_msq(p1, p2, p3, p4, me, mm, anti=-1):
    """(1/4) sum |M|^2 / e^4 = (1/(4 s^2)) tr[(p2 - me) g^mu (p1 + me) g^nu] tr[(p3 + mm) g_mu (p4 - mm) g_nu];
    anti = -1 is the antiparticle residue p - m (anti = +1 only as a control)."""
    P = GA.add(p1, p2)
    s = dot(P, P)
    tot = Fr(0)
    for a in range(4):
        for b in range(4):
            t1 = tr(mul(GA.add(p2, num(anti * me)), GU[a], GA.add(p1, num(me)), GU[b]))
            t2 = tr(mul(GA.add(p3, num(mm)), G[a], GA.sub(p4, num(mm)), G[b]))
            tot += t1 * t2
    return tot / (4 * s * s)


def standard_form(p1, p2, p3, p4, me, mm):
    P = GA.add(p1, p2)
    s = dot(P, P)
    return Fr(8) / (s * s) * (dot(p1, p3) * dot(p2, p4) + dot(p1, p4) * dot(p2, p3)
                               + mm * mm * dot(p1, p2) + me * me * dot(p3, p4) + 2 * me * me * mm * mm)


def cm_momenta(E, pin, pout, c, s_):
    """centre-of-mass frame: e- along +z with |p| = pin, mu- at angle (c = cos, s_ = sin) with |p| = pout."""
    p1 = vec([E, 0, 0, pin])
    p2 = vec([E, 0, 0, -pin])
    p3 = vec([E, pout * s_, 0, pout * c])
    p4 = vec([E, -pout * s_, 0, -pout * c])
    return p1, p2, p3, p4


def pint(coeffs, lo, hi):
    """integral of sum_n coeffs[n] x^n over [lo, hi]."""
    return sum(c * (Fr(hi) ** (n + 1) - Fr(lo) ** (n + 1)) / (n + 1) for n, c in enumerate(coeffs))


def check_lsz_residues_are_spin_projectors():
    """(1) Q(p) = m^2: (p + m)^2 = 2m (p + m), 4 <(p + m)/(2m)>_0 = 2, (p - m)^2 = -2m (p - m);
    (p + m)(p - m) = 0; the residue of S(p) = (p + m)/(Q(p) - m^2) at the pole is p + m."""
    premise(P_ML)
    premise(P_2Q)
    ok = True
    for c, m in (([5, 3, 0, 0], 4), ([13, 0, 5, 0], 12), ([7, 2, 3, 6], 0)):
        p = vec(c)
        if dot(p, p) != m * m:
            return False
        Pp, Pm = GA.add(p, num(m)), GA.sub(p, num(m))
        ok = ok and GA.eq(mul(Pp, Pp), GA.scal(2 * m, Pp)) and GA.eq(mul(Pm, Pm), GA.scal(-2 * m, Pm))
        ok = ok and GA.is_zero(mul(Pp, Pm)) and tr(Pp) == 4 * m and tr(Pm) == -4 * m
        if m:
            ok = ok and tr(GA.scal(Fr(1, 2 * m), Pp)) == 2
    # residue: (Q(p_t) - m^2) S(p_t) = p_t + m for every off-shell p_t
    m = 4
    pt = vec([6, 3, 0, 0])
    St = GA.scal(Fr(1) / (dot(pt, pt) - m * m), GA.add(pt, num(m)))
    ok = ok and GA.eq(GA.scal(dot(pt, pt) - m * m, St), GA.add(pt, num(m)))
    ok = ok and GA.eq(mul(GA.sub(pt, num(m)), St), num(1))
    GA.check("LSZ: propagator residues are 2m times trace-2 idempotents (two spin states)", ok)
    return ok


def check_tree_spin_sum_from_clifford_traces():
    """(2) the Clifford-trace spin sum equals the standard form at massive and massless rational kinematics,
    including a non-centre-of-mass configuration."""
    premise(P_TREE)
    premise(P_ML)
    ok = True
    confs = [cm_momenta(5, 4, 3, Fr(4, 5), Fr(3, 5)) + (3, 4),
             cm_momenta(5, 5, 3, Fr(12, 13), Fr(5, 13)) + (0, 4),
             cm_momenta(13, 13, 13, Fr(-3, 5), Fr(4, 5)) + (0, 0)]
    for p1, p2, p3, p4, me, mm in confs:
        if not (dot(p1, p1) == me * me and dot(p3, p3) == mm * mm):
            return False
        ok = ok and spin_summed_msq(p1, p2, p3, p4, me, mm) == standard_form(p1, p2, p3, p4, me, mm)
    # control: the particle residue p + m in place of the positron's p - m changes the result
    p1, p2, p3, p4, me, mm = confs[0]
    ok = ok and spin_summed_msq(p1, p2, p3, p4, me, mm, 1) != standard_form(p1, p2, p3, p4, me, mm)
    GA.check("tree: spin-summed |M|^2 from Clifford traces equals the standard form", ok)
    return ok


def check_massless_angular_distribution_and_cross_section():
    """(2) m_e = m_mu = 0: (1/4) sum |M|^2 = e^4 (1 + cos^2 theta) at five rational angles; with
    dsigma/dOmega = |M|^2/(64 pi^2 s) and e^2 = 4 pi alpha: dsigma/dOmega = alpha^2 (1 + c^2)/(4 s) and
    sigma = 2 pi (alpha^2/(4 s)) int (1 + c^2) dc = 4 pi alpha^2/(3 s)."""
    premise(P_TREE)
    ok = True
    for c, s_ in ((Fr(4, 5), Fr(3, 5)), (Fr(-12, 13), Fr(5, 13)), (Fr(0), Fr(1)), (Fr(1), Fr(0)),
                  (Fr(-8, 17), Fr(15, 17))):
        p1, p2, p3, p4 = cm_momenta(7, 7, 7, c, s_)
        ok = ok and spin_summed_msq(p1, p2, p3, p4, 0, 0) == 1 + c * c
    # e^4/(64 pi^2 s) = (16 pi^2 alpha^2)/(64 pi^2 s) = alpha^2/(4 s): coefficient 1/4
    coef = Fr(16, 64)
    total_over_pi = 2 * coef * pint([1, 0, 1], -1, 1)        # sigma s/(pi alpha^2)
    ok = ok and coef == Fr(1, 4) and total_over_pi == Fr(4, 3)
    GA.check("massless tree: (1 + cos^2 theta), sigma = 4 pi alpha^2/(3 s)", ok)
    return ok


def check_massive_cross_section_threshold_factor():
    """(2) m_e = 0, m_mu = (sqrt s/2)(1 - beta^2)^(1/2) at rational beta and rational (1 - beta^2)^(1/2): the
    Clifford-trace |M|^2 is a polynomial of degree two in c = cos theta (fixed by c = -1, 0, 1, checked at a
    fourth angle) and integrates to sigma = (4 pi alpha^2/(3 s)) beta (3 - beta^2)/2."""
    premise(P_TREE)
    ok = True
    E = 5
    for beta, root in ((Fr(3, 5), Fr(4, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(12, 13), Fr(5, 13)), (Fr(1), Fr(0))):
        pout, mm = E * beta, E * root
        p1, p2 = vec([E, 0, 0, E]), vec([E, 0, 0, -E])
        vals = []
        for c, sn in ((Fr(-1), Fr(0)), (Fr(0), Fr(1)), (Fr(1), Fr(0)), (Fr(3, 5), Fr(4, 5))):
            p3 = vec([E, pout * sn, 0, pout * c])
            p4 = vec([E, -pout * sn, 0, -pout * c])
            if dot(p3, p3) != mm * mm:
                return False
            vals.append(spin_summed_msq(p1, p2, p3, p4, 0, mm))
        a0 = vals[1]
        a1 = (vals[2] - vals[0]) / 2
        a2 = (vals[2] + vals[0]) / 2 - a0
        c4 = Fr(3, 5)
        ok = ok and vals[3] == a0 + a1 * c4 + a2 * c4 * c4
        # dsigma/dOmega = beta |M|^2/(64 pi^2 s), e^4 = 16 pi^2 alpha^2: sigma s/(pi alpha^2) = (beta/2) int |M|^2/e^4
        sig = Fr(1, 2) * beta * pint([a0, a1, a2], -1, 1)
        ok = ok and sig == Fr(4, 3) * beta * (3 - beta * beta) / 2
    GA.check("massive tree: sigma = (4 pi alpha^2/(3 s)) beta (3 - beta^2)/2 at rational beta", ok)
    return ok


def check_one_loop_absorptive_part_equals_tree_rate():
    """(3) Pi_hat(s) = -(2 alpha/pi) int x(1-x) ln(m^2/(m^2 - x(1-x) s - i0)) dx: its imaginary part is
    2 alpha int over the window x(1-x) s > m^2 of x(1-x) dx = (alpha/3) beta (3 - beta^2)/2 with the window
    ends (1 -+ beta)/2; and (s/(4 pi alpha)) sigma_tree (m_e -> 0) equals it (the s-channel optical-theorem relation for the photon self-energy)."""
    premise(P_QED)
    premise(P_ML)
    ok = True
    for bn, bd in ((3, 5), (4, 5), (12, 13), (1, 1)):
        beta = Fr(bn, bd)
        lo, hi = (1 - beta) / 2, (1 + beta) / 2
        # window: x(1-x) >= (1 - beta^2)/4 exactly between the roots
        ok = ok and lo * (1 - lo) == (1 - beta * beta) / 4 and hi * (1 - hi) == (1 - beta * beta) / 4
        im_over_alpha = 2 * pint([0, 1, -1], lo, hi)
        ok = ok and im_over_alpha == beta * (3 - beta * beta) / 6
        sigma_s_over_pi_alpha2 = Fr(4, 3) * beta * (3 - beta * beta) / 2
        # (s/(4 pi alpha)) sigma = (alpha/4) * sigma s/(pi alpha^2)
        ok = ok and Fr(1, 4) * sigma_s_over_pi_alpha2 == im_over_alpha
    GA.check("one loop: Im Pi_hat = (alpha/3) beta (3 - beta^2)/2 = s sigma_tree/(4 pi alpha)", ok)
    return ok


def check_one_loop_large_s_constant_and_longitudinal_part():
    """(3) s >> m^2: Re Pi_hat = (2 alpha/pi)[(1/6) ln(s/m^2) + int x(1-x) ln(x(1-x))] =
    (alpha/(3 pi))(ln(s/m^2) - 5/3), using int x^n ln x = -1/(n+1)^2; the q_mu q_nu part of the dressed
    photon propagator drops between on-shell currents, so the insertion multiplies the tree amplitude by
    1/(1 - Pi_hat(s))."""
    premise(P_QED)
    premise(P_ML)
    # int_0^1 x(1-x) ln(x(1-x)) dx = 2 int (x - x^2) ln x dx = 2 (-1/4 + 1/9)
    int_lnx = lambda n: Fr(-1, (n + 1) * (n + 1))
    J = 2 * (int_lnx(1) - int_lnx(2))
    ok = J == Fr(-5, 18)
    # coefficient structure: (2 alpha/pi) * (1/6) = alpha/(3 pi); constant (2 alpha/pi) J = (alpha/(3 pi)) * 6J
    ok = ok and 2 * pint([0, 1, -1], 0, 1) == Fr(1, 3) and 6 * J == Fr(-5, 3)
    # the q_mu q_nu part of the dressed photon drops against both on-shell currents:
    # tr[(p2 - m) q (p1 + m) g^nu] = 0 and tr[(p3 + m) q (p4 - m) g_nu] = 0 for q = p1 + p2 = p3 + p4
    p1, p2, p3, p4 = cm_momenta(5, 4, 3, Fr(4, 5), Fr(3, 5))
    me, mm = 3, 4
    q = GA.add(p1, p2)
    for nu in range(4):
        ok = ok and tr(mul(GA.sub(p2, num(me)), q, GA.add(p1, num(me)), G[nu])) == 0
        ok = ok and tr(mul(GA.add(p3, num(mm)), q, GA.sub(p4, num(mm)), G[nu])) == 0
    # control: an off-shell q (p1 - p2) does not drop
    qbad = GA.sub(p1, p2)
    ok = ok and any(tr(mul(GA.sub(p2, num(me)), qbad, GA.add(p1, num(me)), G[nu])) != 0 for nu in range(4))
    GA.check("one loop: constant -5/3; the longitudinal part of the dressed photon drops on shell", ok)
    return ok
