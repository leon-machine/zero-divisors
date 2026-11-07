"""The Dirac field's bulk states restricted to a null plane of the flat gravitational field: exact checks.

Spacetime algebra Cl(1,3), e0^2 = +1, e1^2 = e2^2 = e3^2 = -1; the null plane N through a point with
generators along k = e0 + e3 and second null vector m = e0 - e3 (k . m = 2); the canonical part on N is
the image of Lambda(m) = (1 + e0 e3)/2 = m k / 4, which acts on spinors from the left (the stored
result on the canonical part of a spinor on a null plane). Points of N: x = lambda k + y with y in the span of e1, e2, so for a momentum p,
p . x = lambda (p . k) - p_perp . y (Euclidean dot on the transverse plane).
The bulk two-point kernels of a free Dirac field of mass m0 (matrix reading, labelled: omega(psi psi^dag) =
int d^3p/((2 pi)^3 2 p0) (p + m0) e0 e^{-ip.x}, the other ordering with (p - m0) e0 and e^{+ip.x}) restricted
to N and compressed by Lambda(m) need:
  (1) Lambda(m) is an idempotent, self-adjoint for the Dirac adjoint (e0 reverse(Lambda) e0 = Lambda), its
      left image on the even subalgebra has real dimension 4 (two complex channels), and
      Lambda e0 Lambda = 0, Lambda e_mu e0 Lambda = (e_mu . k) Lambda for mu = 0..3; so by linearity
      Lambda (p +- m0) e0 Lambda = (p . k) Lambda for every p and every mass: the mass drops out.
  (2) On the positive-energy mass shell, parametrised by p+ = p . k > 0 and p_perp (s = Q_E(p_perp) + m0^2):
      p0 = (p+ + s/p+)/2, p3 = (s/p+ - p+)/2 give p0^2 - p3^2 - Q_E(p_perp) = m0^2, p0 > 0, p . k = p+;
      dp3/dp+ = -p0/p+, so d^3p/(2 p0) = dp+ d^2p_perp/(2 p+), and the good-part density
      (1/(2 p0)) (p0/p+) (p . k) = 1/2 for every p+, p_perp and m0 >= 0; every positive-energy shell momentum
      with s > 0 has p . k > 0 and every negative-energy one p . k < 0 (p0 > |p3| from p0^2 - p3^2 = s > 0).
  (3) Hence in (p+, p_perp) the restricted kernels have densities (1/2) theta(p+) and (1/2) theta(-p+) for
      every p_perp and m0, computed here from the shell (the projector coefficient, the Jacobian and 1/(2 p0)
      at each null frequency, with zero where the positive-energy shell has no momentum): with
      psi_N = sqrt(2) Lambda(m) psi the anticommutator density is 1 (delta(lambda) delta^2(y) Lambda) and the
      occupation symbol in p+ is theta, the stored null vacuum's symbol; the
      Fourier transform int_0^inf e^{-i lambda p} dp = -i/(lambda - i0) is standard and not evaluated.
  (4) p0 >= p+/2 and p0 >= s/(2 p+) on the shell (samples), so a bulk remainder symbol decaying in p0 decays
      in p+ at both ends of the positive half-line.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1)
E = [GA.gen(i) for i in range(4)]
K_NULL = GA.add(E[0], E[3])
M_NULL = GA.sub(E[0], E[3])
LAM = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(E[0], E[3], S)))
EVEN = [b for b in GA.all_blades(4) if len(b) % 2 == 0]
SHELL = [(F(1), F(0), F(0), F(0)), (F(3, 2), F(1), F(-2), F(0)), (F(1, 5), F(3), F(1, 2), F(2)),
         (F(7), F(-1, 3), F(0), F(5, 4)), (F(1, 100), F(2), F(2), F(1)), (F(40), F(0), F(1), F(3))]


def _premises():
    premise("synthesis.canonical-part-of-a-spinor-on-a-null-plane")
    premise("synthesis.positive-null-energy-gives-r-premises")
    premise("field-theory.second-quantisation")


def mul(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, S)
    return out


def shell(pp, p1, p2, m0):
    s = p1 * p1 + p2 * p2 + m0 * m0
    return (pp + s / pp) / 2, (s / pp - pp) / 2, s


def check_good_part_projector_drops_the_mass():
    _premises()
    GA.check("Lambda(m) = m k / 4", GA.eq(LAM, GA.scal(F(1, 4), mul(M_NULL, K_NULL))))
    GA.check("Lambda(m) is idempotent", GA.eq(mul(LAM, LAM), LAM))
    GA.check("Dirac-self-adjoint: e0 reverse(Lambda) e0 = Lambda", GA.eq(mul(E[0], GA.reverse(LAM), E[0]), LAM))
    rows = []
    cols = [mul(LAM, {b: F(1)}) for b in EVEN]
    rows = [[c.get(d, F(0)) for c in cols] for d in EVEN]
    GA.check("left image of Lambda(m) on the even subalgebra has real dimension 4", GA.mat_rank(rows) == 4)
    GA.check("mass term drops: Lambda e0 Lambda = 0", GA.is_zero(mul(LAM, E[0], LAM)))
    for mu in range(4):
        GA.check("Lambda e_%d e0 Lambda = (e_%d . k) Lambda" % (mu, mu),
                 GA.eq(mul(LAM, E[mu], E[0], LAM), GA.scal(GA.dot(E[mu], K_NULL, S), LAM)))
    for pp, p1, p2, m0 in SHELL:
        p0, p3, _ = shell(pp, p1, p2, m0)
        pv = GA.add(GA.scal(p0, E[0]), GA.scal(p1, E[1]), GA.scal(p2, E[2]), GA.scal(p3, E[3]))
        for sgn in (1, -1):
            lhs = mul(LAM, GA.add(pv, GA.sc(sgn * m0)), E[0], LAM)
            GA.check("Lambda (p %s m0) e0 Lambda = (p . k) Lambda" % ("+" if sgn > 0 else "-"),
                     GA.eq(lhs, GA.scal(GA.dot(pv, K_NULL, S), LAM)))
    GA.check("tabulated: Lambda(m) = 1/2 + e0 e3 / 2", LAM == {(): F(1, 2), (0, 3): F(1, 2)})
    GA.check("tabulated: Lambda e3 e0 Lambda = -Lambda",
             mul(LAM, E[3], E[0], LAM) == {(): F(-1, 2), (0, 3): F(-1, 2)})
    GA.check("tabulated: e0 Lambda = k / 2", GA.eq(mul(E[0], LAM), GA.scal(F(1, 2), K_NULL)))
    seen = []
    for mu in range(4):
        if not GA.is_zero(GA.sub(mul(LAM, E[mu], E[0], LAM), GA.scal(GA.dot(E[mu], K_NULL, S), LAM))):
            break
        seen.append(mu)
    GA.check("the identity holds on all four basis vectors", seen == [0, 1, 2, 3])
    pp, p1, p2, m0 = SHELL[2]
    p0, p3, _ = shell(pp, p1, p2, m0)
    pv = GA.add(GA.scal(p0, E[0]), GA.scal(p1, E[1]), GA.scal(p2, E[2]), GA.scal(p3, E[3]))
    plus = mul(GA.add(pv, GA.sc(m0)), E[0])
    minus = mul(GA.add(pv, GA.sc(-m0)), E[0])
    GA.check("uncompressed, the two mass signs differ by 2 m0 e0 (the compression removes it)",
             GA.eq(GA.sub(plus, minus), GA.scal(2 * m0, E[0])) and m0 == 2)
    GA.check("k annihilates nothing in the image: k Lambda(m) is not zero, m Lambda(m) is",
             not GA.is_zero(mul(K_NULL, LAM)) and GA.is_zero(mul(M_NULL, LAM)))


def check_shell_density_of_the_good_part_is_one_half():
    _premises()
    for pp, p1, p2, m0 in SHELL:
        p0, p3, s = shell(pp, p1, p2, m0)
        pv = GA.add(GA.scal(p0, E[0]), GA.scal(p1, E[1]), GA.scal(p2, E[2]), GA.scal(p3, E[3]))
        GA.check("on shell: p0^2 - p3^2 - Q_E(p_perp) = m0^2", p0 * p0 - p3 * p3 - p1 * p1 - p2 * p2 == m0 * m0)
        GA.check("Q(p) = m0^2 in the algebra", GA.dot(pv, pv, S) == m0 * m0)
        GA.check("p . k = p+", GA.dot(pv, K_NULL, S) == pp)
        GA.check("positive energy", p0 > 0)
        GA.check("dp3/dp+ = -p0/p+", -(s / (pp * pp) + 1) / 2 == -p0 / pp)
        density = (1 / (2 * p0)) * (p0 / pp) * GA.dot(pv, K_NULL, S)
        GA.check("good-part density 1/2, independent of mass and transverse momentum", density == F(1, 2))
        if s > 0:
            GA.check("p0 > |p3| when s > 0", p0 > abs(p3))
            neg = GA.scal(-1, pv)
            GA.check("the negative-energy shell has p . k < 0", GA.dot(neg, K_NULL, S) < 0)


def _compressed_coefficient(X):
    """c with Lambda X Lambda = c Lambda (fails the check if not of that form)."""
    Y = mul(LAM, X, LAM)
    c = Y.get((), F(0)) * 2
    GA.check("compression is a multiple of Lambda", GA.eq(Y, GA.scal(c, LAM)))
    return c


def _branch_density(q, p1, p2, m0, mass_sign):
    """Compressed density at null momentum p . k = q from the positive-energy shell, 0 if that shell
    has no momentum there: (Lambda (p + mass_sign m0) e0 Lambda coefficient) |dp3/dp+| / (2 p0)."""
    p0, p3, s = shell(q, p1, p2, m0)
    if p0 <= 0:
        return F(0)
    pv = GA.add(GA.scal(p0, E[0]), GA.scal(p1, E[1]), GA.scal(p2, E[2]), GA.scal(p3, E[3]))
    coeff = _compressed_coefficient(mul(GA.add(pv, GA.sc(mass_sign * m0)), E[0]))
    jac = (s / (q * q) + 1) / 2
    return coeff * jac / (2 * p0)


def check_restricted_vacuum_is_the_null_vacuum_symbol():
    """Symbol of the restricted vacuum, computed from the shell: at frequency q (phase e^{i q (u - v)})
    omega(psi* psi) collects the positive-energy momentum with p . k = q (kernel (p - m0) e0), and
    omega(psi psi*) the one with p . k = -q (kernel (p + m0) e0, phase e^{-i p . x}); psi_N carries a
    factor 2. The occupation symbol 2 w must be theta(q) and 2 (w + w_tilde) = 1 (the CAR)."""
    _premises()
    seen_pos = seen_neg = 0
    for q in (F(-3), F(-1, 7), F(1, 9), F(2), F(11, 3)):
        for p1, p2, m0 in ((F(0), F(1), F(0)), (F(3), F(-1, 2), F(2)), (F(1, 3), F(0), F(5, 4))):
            w = _branch_density(q, p1, p2, m0, -1)
            w_tilde = _branch_density(-q, p1, p2, m0, 1)
            GA.check("restricted anticommutator density is 1 for psi_N", 2 * (w + w_tilde) == 1)
            if q > 0:
                seen_pos += 1
                GA.check("positive null frequency: occupation 1 (from the positive shell)", 2 * w == 1)
            else:
                seen_neg += 1
                GA.check("negative null frequency: occupation 0 (the shell has no momentum there)",
                         w == 0 and 2 * w_tilde == 1)
    GA.check("both signs of the null frequency sampled", seen_pos == 9 and seen_neg == 6)


def check_shell_energy_bounds_give_decay_at_both_ends():
    _premises()
    premise("synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state")
    premise("synthesis.imported-microlocal-hadamard-condition")
    for pp, p1, p2, m0 in SHELL:
        p0, p3, s = shell(pp, p1, p2, m0)
        GA.check("p0 >= p+/2", p0 >= pp / 2)
        GA.check("p0 >= s/(2 p+)", p0 >= s / (2 * pp))
        GA.check("p0 = p+/2 + s/(2 p+) exactly", p0 == pp / 2 + s / (2 * pp))
