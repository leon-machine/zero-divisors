"""standard-model.trichotomy-what-kind-number: exact checks of the computable clauses.

Ambient space Cl(2,4) in GA.py with squares (e_0, e_1, e_2, e_3, e_+, e_-) = (+1, -1, -1, -1, +1, -1),
n_inf = e_+ + e_-, n_0 = (e_+ - e_-)/2, the frozen point I_Lambda = n_inf + (Lambda/6) n_0 in the flat chart,
H^2 = Q(I_Lambda) = Lambda/3, N^2 = M_P^2 / Q(I_Lambda) (the imported dictionary), M_P = 1.
(1) Kinematic clause: Q(I_{s^2 Lambda}) = s^2 Q(I_Lambda), so H -> sH and N^2 -> N^2/s^2 at fixed M_P, for
    Lambda in {3, 1/2, -6/5} and s in {2, 3/5}; the rescaling is I -> sI with the conformal class kept:
    the dilation rotor R = 5/4 + (3/4) e_+ e_- (R R~ = 1) fixes every spacetime vector and satisfies
    R I_Lambda R~ = (1/s) I_{s^2 Lambda} with s = 4 (computed).
(4) N^2 = 3/Lambda varies across Lambda: d(N^2)/dLambda = -3/Lambda^2 as a rational-function identity,
    and N^2 takes distinct values at distinct Lambda (read off the chart norm).
Units statement: with certified rational bounds on pi (Machin series, alternating remainders) and on
ln 2 (2 atanh(1/3) with a geometric tail bound), for every horizon capacity C = pi N^2 / ln 2 in
[4.75, 4.85] x 10^122 (that is, "about 4.8 x 10^122"): 2^407 < C < 2^408 (base-two logarithm about 407),
N^2 = C ln 2 / pi satisfies 2^405 < N^2 < 2^406 (R = log2 N^2 about 405), and N lies in
(1.0, 1.04) x 10^61 (about 1.0 x 10^61, the imported value).
Not computed: the discrete invariants' independence of the scale (they are computed elsewhere from
data that do not contain Lambda), clause (2) and the imported clause (4)'s Henneaux-Teitelboim
alternative, the conditional clause (3), and the named but unbalanced entropic and endpoint effects;
the rung sentence (p - q mod 8 kept by each rung) is Rule 1's content.
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
NINF = GA.add(GA.gen(4), GA.gen(5))
N0 = GA.scal(F(1, 2), GA.sub(GA.gen(4), GA.gen(5)))


def I_of(lam):
    return GA.add(NINF, GA.scal(lam / 6, N0))


def pi_bounds():
    """Machin bounds: 13 alternating terms of arctan(1/5), 5 of arctan(1/239)."""
    l5, u5 = series.arctan_inv_bracket(5, 13)
    l239, u239 = series.arctan_inv_bracket(239, 5)
    return 16 * l5 - 4 * u239, 16 * u5 - 4 * l239


def ln2_bounds():
    return series.ln_bounds(2)


def check_rescaling_kinematics():
    premise("standard-model.imported-frozen-point-dictionary")
    for lam in (F(3), F(1, 2), F(-6, 5)):
        q = GA.dot(I_of(lam), I_of(lam), SQ)
        assert q == lam / 3
        for s in (F(2), F(3, 5)):
            q2 = GA.dot(I_of(s * s * lam), I_of(s * s * lam), SQ)
            assert q2 == s * s * q                      # H^2 -> s^2 H^2
            if q != 0:
                assert (1 / q2) * s * s == 1 / q        # N^2 -> N^2 / s^2
    R = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), GA.mul(GA.gen(4), GA.gen(5), SQ)))
    Rt = GA.reverse(R)
    assert GA.eq(GA.mul(R, Rt, SQ), GA.sc(1))
    for i in range(4):
        assert GA.eq(GA.mul(GA.mul(R, GA.gen(i), SQ), Rt, SQ), GA.gen(i))
    lam = F(3)
    img = GA.mul(GA.mul(R, I_of(lam), SQ), Rt, SQ)
    s = F(4)
    assert GA.eq(img, GA.scal(1 / s, I_of(s * s * lam)))
    return True


def check_n_varies_across_lambda():
    premise("standard-model.imported-frozen-point-dictionary")
    L = GA.RF.var()
    Nsq = GA.RF.const(3) / L
    assert Nsq.deriv().eqrf(-(GA.RF.const(3) / (L * L)))
    vals = [1 / GA.dot(I_of(l), I_of(l), SQ) for l in (F(3), F(12), F(1, 5))]
    assert vals == [1, F(1, 4), 15]
    assert len(set(vals)) == 3
    return True


C_RANGE = (F(475, 100) * 10 ** 122, F(485, 100) * 10 ** 122)   # quoted: C "about 4.8 x 10^122", both ends


def check_units_statement_numbers():
    plo, phi = pi_bounds()
    llo, lhi = ln2_bounds()
    # known digits pi = 3.14159..., ln 2 = 0.693147...: both certified bounds truncate to them
    assert plo * 10 ** 5 // 1 == phi * 10 ** 5 // 1 == 314159 and plo < phi
    assert llo * 10 ** 6 // 1 == lhi * 10 ** 6 // 1 == 693147 and llo < lhi
    for C in C_RANGE:
        assert (C // 1).bit_length() - 1 == 407                   # floor(log2 C) = 407: 2^407 <= C < 2^408
        n2_lo, n2_hi = C * llo / phi, C * lhi / plo
        # floor(log2 N^2) = 405 at both ends of the bracket: 2^405 <= N^2 < 2^406
        assert (n2_lo // 1).bit_length() - 1 == (n2_hi // 1).bit_length() - 1 == 405
        # N in (1.0, 1.04) x 10^61: compare squares
        assert (10 ** 61) ** 2 < n2_lo and n2_hi < (F(104, 100) * 10 ** 61) ** 2
    return True
