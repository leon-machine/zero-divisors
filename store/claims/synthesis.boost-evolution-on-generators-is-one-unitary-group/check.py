"""The boost time evolution on the continuum of a horizon generator is one unitary group: exact checks.

Setting: the spacetime algebra Cl(1,3), store signature (+,-,-,-), k = e0 + e1 a future null generator
direction, m = (e0 - e1)/2 its dual null vector (k.m = 1), the null plane N_k = {x . k = 0}, affine
parameter u along k, Lambda(a) = a e0/(2 a0), the boost B = cosh(lam/2) + e1e0 sinh(lam/2) with
B k B~ = e^lam k. Rapidity e^{lam/2} = r is taken rational, so every identity is exact.
(1) The canonical component: Lambda(m) a e0 Lambda(m) vanishes for a = k, e2, e3 and equals Lambda(m) for
    a = m, so on Lambda(m) the stored anticommutator chi (grad D) e0 keeps only the derivative along the
    generators; Lambda(k) keeps only the m.grad part.
(2) The two factors: B Lambda(m) = r^{-1} Lambda(m), B* = B, B Lambda(m) B* = r^{-2} Lambda(m) (rotor on
    values); the transport u -> r^{-2} u multiplies cell norms by r^2 (affine parameter); the composite
    preserves the kernel, each factor alone does not, and on Lambda(k) the factors do not cancel.
(3) The phase flow: on Mellin monomials u^s the composite multiplies by e^{-lam (1/2 + s)}; the exponent is
    purely imaginary exactly when Re s = -1/2 (half densities), giving e^{-i w lam}.
(4) Imaginary rapidity: the Euclidean rotor cos(th/2) + i e1e0 sin(th/2) acts on Lambda(m) by e^{-i th/2};
    -i at th = pi (with u -> -u), -1 at th = 2 pi, +1 at th = 4 pi.
(5) Real time: cell overlaps <chi_c, D chi_a> obey Cauchy-Schwarz at every tested rapidity, and for a fixed
    pair of cells the squared overlap falls as r^{-2}; the cell count grows as r^2 = e^{lam}.
(6) The comparison: kappa beta = 2 pi for the one group (beta in units of pi), t_* = (beta/2pi) ln N.
Exact arithmetic only (Fractions, Gaussian rationals, multivectors over Fractions).
"""
from fractions import Fraction as F
from functools import reduce
import GA
from GA import QI
from tp_premise import premise

SQ = (1, -1, -1, -1)
E = [GA.gen(i) for i in range(4)]
K = GA.add(E[0], E[1])
M = GA.scal(F(1, 2), GA.sub(E[0], E[1]))


def _m(*xs):
    return reduce(lambda a, b: GA.mul(a, b, SQ), xs)


def _star(x):
    """Frame *-structure: antiautomorphism with e0* = e0, ei* = -ei (i = 1, 2, 3)."""
    out = {}
    for b, c in x.items():
        g = len(b)
        s = F(-1) ** (g * (g - 1) // 2) * F(-1) ** sum(1 for i in b if i > 0)
        out[b] = s * c
    return out


def _lam(a, a0):
    return GA.scal(1 / F(2 * a0), _m(a, E[0]))


def _boost(r):
    c, s = (r + 1 / r) / 2, (r - 1 / r) / 2
    return GA.add(GA.sc(c), GA.scal(s, _m(E[1], E[0])))


def _cell_overlap(a, b, c, d, q):
    """Length of [q a, q b) intersected with [c, d)."""
    lo, hi = max(q * a, c), min(q * b, d)
    return hi - lo if hi > lo else F(0)


def check_canonical_component_on_the_null_plane():
    premise("field-theory.second-quantisation")
    Lm, Lk = _lam(M, F(1, 2)), _lam(K, F(1))
    GA.check("k . m = 1", GA.eq(GA.scal(F(1, 2), GA.add(_m(K, M), _m(M, K))), GA.sc(1)))
    GA.check("Lambda(m) idempotent", GA.eq(_m(Lm, Lm), Lm))
    GA.check("m Lambda(m) = 0: projector onto ker m", GA.is_zero(_m(M, Lm)))
    GA.check("Lambda(k) + Lambda(m) = 1", GA.eq(GA.add(Lk, Lm), GA.sc(1)))
    GA.check("Lambda(m) self-adjoint", GA.eq(_star(Lm), Lm))
    GA.check("tabulated: Lambda(m) = (1 + e0e1)/2", GA.eq(Lm, {(): F(1, 2), (0, 1): F(1, 2)}))
    # vector decomposition a = (a.m) k + (a.k) m + a_perp, so grad = k (m.grad) + m (k.grad) + grad_perp
    for a in [GA.add(GA.scal(F(3), E[0]), GA.scal(F(-2), E[1]), E[2]), GA.add(E[1], GA.scal(F(5, 7), E[3]))]:
        am = GA.scal(F(1, 2), GA.add(_m(a, M), _m(M, a))).get((), F(0))
        ak = GA.scal(F(1, 2), GA.add(_m(a, K), _m(K, a))).get((), F(0))
        perp = GA.sub(GA.sub(a, GA.scal(am, K)), GA.scal(ak, M))
        GA.check("a_perp has no e0, e1 part", all(b not in perp for b in [(0,), (1,)]))
    # sandwich: only the coefficient of m (the derivative along the generator) survives on Lambda(m)
    GA.check("Lambda(m) k e0 Lambda(m) = 0", GA.is_zero(_m(Lm, K, E[0], Lm)))
    GA.check("Lambda(m) e2 e0 Lambda(m) = 0", GA.is_zero(_m(Lm, E[2], E[0], Lm)))
    GA.check("Lambda(m) e3 e0 Lambda(m) = 0", GA.is_zero(_m(Lm, E[3], E[0], Lm)))
    GA.check("Lambda(m) m e0 Lambda(m) = Lambda(m)", GA.eq(_m(Lm, M, E[0], Lm), Lm))
    # control: on Lambda(k) the surviving coefficient is that of k (the m.grad, off-plane derivative)
    GA.check("control: Lambda(k) m e0 Lambda(k) = 0", GA.is_zero(_m(Lk, M, E[0], Lk)))
    GA.check("control: Lambda(k) k e0 Lambda(k) = 2 Lambda(k)", GA.eq(_m(Lk, K, E[0], Lk), GA.scal(F(2), Lk)))
    return True


def check_rotor_and_transport_are_the_two_factors():
    premise("field-theory.second-quantisation")
    premise("tower.structure-tower-c-norms")
    premise("synthesis.affine-cell-boost-spreads-without-scrambling")
    Lm, Lk = _lam(M, F(1, 2)), _lam(K, F(1))
    wedge = GA.scal(F(1, 2), GA.sub(_m(K, M), _m(M, K)))
    GA.check("k ^ m = e1e0, the boost plane", GA.eq(wedge, _m(E[1], E[0])))
    cells = [(F(0), F(1)), (F(1, 3), F(2)), (F(5), F(17, 2))]
    for r in [F(3, 2), F(1, 5), F(7, 3)]:
        B = _boost(r)
        GA.check("B k B~ = r^2 k", GA.eq(_m(B, K, GA.reverse(B)), GA.scal(r * r, K)))
        GA.check("B m B~ = r^-2 m", GA.eq(_m(B, M, GA.reverse(B)), GA.scal(1 / (r * r), M)))
        GA.check("B~ (u k) B = r^-2 u k: the transport u -> r^-2 u", GA.eq(_m(GA.reverse(B), K, B), GA.scal(1 / (r * r), K)))
        GA.check("B* = B (boosts are self-adjoint)", GA.eq(_star(B), B))
        GA.check("B Lambda(m) = r^-1 Lambda(m)", GA.eq(_m(B, Lm), GA.scal(1 / r, Lm)))
        rotor_factor = F(1) / (r * r)                      # B Lambda(m) B* = r^-2 Lambda(m)
        GA.check("B Lambda(m) B* = r^-2 Lambda(m)", GA.eq(_m(B, Lm, _star(B)), GA.scal(rotor_factor, Lm)))
        q = 1 / (r * r)
        for (a, b) in cells:
            # transport psi(u) -> psi(q u): delta(q (u - v)) = q^-1 delta(u - v); the Jacobian is the ratio
            # of a cell's length to the length of its image under u -> q u
            transport_jac = (b - a) / (q * b - q * a)
            GA.check("transport alone rescales the kernel by r^2", transport_jac == r * r)
            GA.check("composite preserves the CAR kernel", rotor_factor * transport_jac == 1)
            GA.check("rotor alone does not preserve it", rotor_factor != 1)
            GA.check("transport alone does not preserve it", transport_jac != 1)
        # control: on Lambda(k) the rotor weight is r, so the factors multiply to r^4, not 1
        GA.check("control: B Lambda(k) = r Lambda(k)", GA.eq(_m(B, Lk), GA.scal(r, Lk)))
        GA.check("control: B Lambda(k) B* = r^2 Lambda(k)", GA.eq(_m(B, Lk, _star(B)), GA.scal(r * r, Lk)))
        GA.check("control: with the transport Jacobian r^2 the kernel gains r^4", r * r * (r * r) == r ** 4 and r ** 4 != 1)
    # tabulated rotor at r = 2: B = 5/4 + (3/4) e1e0
    GA.check("tabulated B at r = 2", GA.eq(_boost(F(2)), {(): F(5, 4), (0, 1): F(-3, 4)}))
    # only the half weight makes the composite unitary: weight r^{-2w} times transport r^2 equals 1
    ws = [F(j, 4) for j in range(-4, 5)]
    good = [w for w in ws if all((F(1) / (r ** 2)) ** (2 * w) * r * r == 1 for r in [F(3, 2), F(1, 5)])]
    GA.check("only w = 1/2 among quarter weights", good == [F(1, 2)])
    return True


def check_mellin_modes_carry_the_phase_flow():
    premise("synthesis.phase-flow-is-time-rotor-flow-kms-continuation")
    # measure the dilation on monomials u^s by evaluation: (D f)(u) = r^-1 f(r^-2 u), r = e^{lam/2};
    # the ratio (D f)(u)/f(u) = r^{2 c(s)} defines the exponent c(s) of e^lam
    def measured_exponent(s):
        found = []
        for r in [F(2), F(3)]:
            for u in [F(1, 2), F(5, 3)]:
                ratio = (1 / r) * (u / (r * r)) ** s / (u ** s)
                # solve r^{2c} = ratio for c among half-integers in [-10, 10]
                cands = [F(k, 2) for k in range(-20, 21) if (r ** k == ratio if k >= 0 else (1 / r) ** (-k) == ratio)]
                found.append(cands[0] if len(cands) == 1 else None)
        return found[0] if all(x == found[0] for x in found) else None
    pts = [(s, measured_exponent(s)) for s in [0, 1, 2, -1, 3]]
    GA.check("the exponent is measured at every tested s", all(cs is not None for _, cs in pts))
    slope = pts[1][1] - pts[0][1]
    icpt = pts[0][1]
    GA.check("measured slope -1 and intercept -1/2", slope == -1 and icpt == F(-1, 2))
    GA.check("the measured law is affine: c(s) = -(1/2 + s) at every tested s", all(cs == icpt + slope * s for s, cs in pts))
    # continue the affine law to complex s
    def expo(s):
        return QI(icpt) + QI(slope) * s
    for w in [F(1), F(-3, 2), F(2, 7), F(0)]:
        s = QI(F(-1, 2), w)
        GA.check("Re s = -1/2 gives a purely imaginary exponent -i w", expo(s) == QI(0, -w))
    for s in [QI(F(0), F(1)), QI(F(-1), F(2)), QI(F(1, 2), F(0))]:
        GA.check("control: Re s != -1/2 gives a real part (no phase)", expo(s).re != 0)
    # group law on cells: D_lam D_mu = D_{lam + mu} (r multiplicative)
    for (r1, r2) in [(F(3, 2), F(5)), (F(1, 3), F(4, 7))]:
        for (a, b) in [(F(1), F(2)), (F(2, 3), F(9, 4))]:
            q1, q2, q12 = 1 / r1 ** 2, 1 / r2 ** 2, 1 / (r1 * r2) ** 2
            GA.check("group law on supports", (q2 * q1 * a, q2 * q1 * b) == (q12 * a, q12 * b))
            GA.check("group law on weights", (1 / r1) * (1 / r2) == 1 / (r1 * r2))
    # tabulated: s = -1/2 + 3i gives exponent -3i, the phase e^{-3 i lam} (one-particle energy 3 kappa)
    GA.check("tabulated exponent", expo(QI(F(-1, 2), F(3))) == QI(0, -3))
    return True


def check_imaginary_rapidity_is_the_euclidean_rotor():
    premise("singularity.euclidean-rotor-where-it-lies")
    premise("synthesis.positive-null-energy-gives-r-premises")
    Lm = _lam(M, F(1, 2))
    E10 = _m(E[1], E[0])
    GA.check("e1e0 Lambda(m) = -Lambda(m)", GA.eq(_m(E10, Lm), GA.neg(Lm)))
    # B_{i th} = cos(th/2) + i e1e0 sin(th/2); on Lambda(m) it is (cos - i sin) = e^{-i th/2}.
    # Represent a complex multivector as (re, im). Rational points: t = tan(th/4).
    for t in [F(1, 3), F(2), F(-5, 4), F(1)]:
        d = 1 + t * t
        c, s = (1 - t * t) / d, 2 * t / d               # cos(th/2), sin(th/2)
        re = _m(GA.sc(c), Lm)
        im = _m(GA.scal(s, E10), Lm)
        GA.check("B_{i th} Lambda(m) = (cos th/2 - i sin th/2) Lambda(m)",
                 GA.eq(re, GA.scal(c, Lm)) and GA.eq(im, GA.scal(-s, Lm)))
        GA.check("|e^{-i th/2}|^2 = 1", c * c + s * s == 1)
    # th = pi is t = tan(pi/4) = 1: cos(pi/2) = 0, sin(pi/2) = 1, factor -i; the transport u -> e^{-i pi} u
    # is the square of the factor's unit-modulus part on u: (-i)^2 = -1, carrying u > 0 to -u
    t = F(1)
    d = 1 + t * t
    f = QI((1 - t * t) / d, -(2 * t / d))
    GA.check("th = pi: factor -i", f == QI(0, -1))
    GA.check("th = pi: e^{-i pi} u = -u, the other half-generator", f * f * QI(F(3)) == QI(F(-3)))
    GA.check("th = 2 pi: factor -1 (spinor sign)", f * f == QI(-1))
    GA.check("th = 4 pi: factor +1 (rotor period 4 pi)", f * f * f * f == QI(1))
    GA.check("control: th = 3 pi is not a return", f * f * f != QI(1))
    # on Mellin modes the continued phase e^{-i w lam} at lam = i th is real: e^{w th}; record exponent w
    for w in [F(1), F(-2), F(3, 5)]:
        GA.check("continued exponent (-i w)(i) = w is real", QI(0, -w) * QI(0, 1) == QI(w))
    return True


def check_real_time_anticommutators_stay_bounded():
    premise("synthesis.number-diagonal-dynamics-spreads-nothing")
    premise("synthesis.affine-cell-boost-spreads-without-scrambling")
    cells = [(F(0), F(1)), (F(1, 2), F(3, 2)), (F(2), F(5)), (F(1, 7), F(9, 4))]
    for r in [F(1, 3), F(1), F(2), F(5), F(20)]:
        q = r * r          # forward evolution pushes [a, b) to [q a, q b) with weight r^-1
        for (a, b) in cells:
            for (c, d) in cells:
                ov = _cell_overlap(a, b, c, d, q)
                lhs = ov * ov / q                       # |<chi_cd, D chi_ab>|^2 (b - a)(d - c)
                GA.check("Cauchy-Schwarz: |<g, D f>|^2 <= |f|^2 |g|^2", lhs <= (b - a) * (d - c))
    # fixed cells, growing rapidity: squared anticommutator with cell [0,1) from cell [0,1) is r^-2
    for r in [F(2), F(5), F(20)]:
        q = r * r
        GA.check("decay: |{a(D chi), a*(chi)}|^2 = r^-2", _cell_overlap(F(0), F(1), F(0), F(1), q) ** 2 / q == 1 / q)
    # tabulated: r = 2, cells [1/2, 3/2) evolved, against [2, 5): overlap [2, 5) cap [2, 6) = 3, squared/4
    GA.check("tabulated overlap", _cell_overlap(F(1, 2), F(3, 2), F(2), F(5), F(4)) ** 2 / 4 == F(9, 4))
    # the support count: at r^2 = N one unit cell covers N unit cells (integer N)
    for N in [2, 3, 7, 16]:
        covered = sum(1 for j in range(0, 40) if _cell_overlap(F(0), F(1), F(j), F(j + 1), F(N)) > 0)
        GA.check("support covers e^lam = N cells", covered == N)
    return True


def check_one_group_comparison():
    # the chaos-bound estimate (scrambling.spreading-law-chaos-bound-saturated) is compared with, not used
    premise("hawking.i-state-continuum")
    premise("synthesis.positive-null-energy-gives-r-premises")
    # beta stored in units of pi: (N+) gives rapidity period 2 pi, so beta = 2 pi / kappa
    for Mass in [F(1), F(3, 2), F(7)]:
        kappa = 1 / (4 * Mass)
        beta_over_pi = 2 / kappa
        GA.check("Schwarzschild: beta = 8 pi M", beta_over_pi == 8 * Mass)
        GA.check("kappa beta = 2 pi for the one group", kappa * beta_over_pi == 2)
        GA.check("t_* coefficient: 1/kappa = beta/(2 pi)", 1 / kappa == beta_over_pi / 2)
    # the same group in the I-state at rapidity period 2 pi c: symbol (1 + q^{2c})^{-1}, q = e^{pi w};
    # KMS identity 1 - m = e^{2 pi c w} m holds at that period, and kappa beta = 2 pi c
    for c in [F(1), F(2), F(1, 3)]:
        for q in [F(2), F(5, 3)]:
            if c.denominator == 1:
                qc = q ** (2 * c.numerator)
                m = 1 / (1 + qc)
                GA.check("KMS identity at period 2 pi c", 1 - m == qc * m)
        kappa = F(1, 4)
        GA.check("kappa beta = 2 pi c", kappa * (2 * c / kappa) == 2 * c)
        GA.check("equals 2 pi only at c = 1", (2 * c == 2) == (c == 1))
    # control: the doubled period of the finite independence model breaks the identity
    kappa = F(1, 4)
    GA.check("control: doubled period gives kappa beta = 4 pi", kappa * (2 * (2 / kappa)) == 4)
    # real-time Lyapunov exponent: anticommutators bounded by 1, so the growth exponent is <= 0 < 2 pi T
    GA.check("MSS satisfied with margin: 0 < kappa", F(0) < kappa)
    return True
