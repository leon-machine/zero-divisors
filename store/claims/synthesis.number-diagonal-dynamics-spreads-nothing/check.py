"""synthesis.number-diagonal-dynamics-spreads-nothing: exact checks.

Four CAR modes in Cl(4,4): v_k = (e_k + e_{4+k})/2, v_k^* = (e_k - e_{4+k})/2, sigma_k = e_k e_{4+k}.
check_diagonal_support_never_grows: for number-diagonal H (chain couplings sigma_j sigma_{j+1},
a field on mode 0, and a three-body term sigma_0 sigma_1 sigma_2) the nested commutators
ad_H^n(v_0), n = 1..5, equal v_0 (-2 H_1)^n with H = H_0 + sigma_0 H_1, and never involve mode 3
(nor mode 2 when the three-body term is absent); adding a hop between modes 1, 2 and 2, 3 makes
ad^2 reach mode 2 and ad^3 reach mode 3.
check_real_time_dressing_exact: with all-to-all couplings and cos = 3/5, sin = 4/5, the exact unitary
U = prod_k (cos + i sin sigma_0 sigma_k) gives U v_0 U^{-1} = v_0 prod_k (cos 2 - i sin 2 sigma_k) with
(cos 2, sin 2) = (-7/25, 24/25), whose size distribution is binomial with mean 3 (24/25)^2; and the
evolved v_0 anticommutes with v_3, v_3^* on the chain (no out-of-time-order growth outside N(0)).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = GA.sig(4, 4)
NM = 4


def v(k):
    return GA.scal(F(1, 2), GA.add(GA.gen(k), GA.gen(NM + k)))


def vs(k):
    return GA.scal(F(1, 2), GA.sub(GA.gen(k), GA.gen(NM + k)))


def m(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def sig(k):
    return GA.sub(m(vs(k), v(k)), m(v(k), vs(k)))


def ad(H, X):
    return GA.sub(m(H, X), m(X, H))


def support(X):
    s = set()
    for b in X:
        for g in b:
            s.add(g % NM)
    return s


def check_diagonal_support_never_grows():
    premise("singularity.modular-structure-completed-pair")
    premise("singularity.number-diagonal-dynamics-models-scrambling-derived")
    for k in range(NM):
        assert GA.eq(sig(k), GA.mul(GA.gen(k), GA.gen(NM + k), SQ))
        assert GA.eq(m(v(k), sig(k)), v(k))                         # v sigma = v
        assert GA.eq(m(sig(k), v(k)), GA.neg(v(k)))                 # sigma v = -v
    s0, s1, s2, s3 = sig(0), sig(1), sig(2), sig(3)
    for three in (0, 5):
        H1 = GA.add(GA.sc(F(1, 3)), GA.scal(2, s1), GA.scal(three, m(s1, s2)))
        H = GA.add(m(s0, H1), GA.scal(F(-1, 2), m(s1, s2)), GA.scal(7, m(s2, s3)), GA.scal(F(5, 4), s3))
        X, P = v(0), GA.sc(1)
        for n in range(1, 6):
            X = ad(H, X)
            P = m(P, GA.scal(-2, H1))
            assert GA.eq(X, m(v(0), P))                             # ad^n v0 = v0 (-2 H_1)^n
            assert 3 not in support(X)
            assert (2 in support(X)) == (three != 0)
            assert support(X) <= {0, 1, 2}
            if three == 0:
                # (-2 H_1)^n = ((a+b)^n + (a-b)^n)/2 + sigma_1 ((a+b)^n - (a-b)^n)/2, a + b = -14/3, a - b = 10/3
                p_, q_ = F(-14, 3) ** n, F(10, 3) ** n
                assert GA.eq(X, GA.add(GA.scal((p_ + q_) / 2, v(0)), GA.scal((p_ - q_) / 2, m(v(0), s1))))
    # a hop (outside the diagonal algebra) propagates along the chain
    hop = GA.add(m(vs(1), v(2)), m(vs(2), v(1)), m(vs(2), v(3)), m(vs(3), v(2)))
    Hh = GA.add(GA.scal(2, m(s0, s1)), hop)
    X = v(0)
    reach = []
    for n in range(1, 4):
        X = ad(Hh, X)
        reach.append(max(support(X)))
    assert reach == [1, 2, 3]
    return True


def qmul(x, y):
    # Clifford product with Gaussian-rational coefficients
    out = {}
    for b1, c1 in x.items():
        for b2, c2 in y.items():
            s, b = GA.blade_mul(b1, b2, SQ)
            c = c1 * c2 * s
            if c != 0:
                out[b] = out.get(b, GA.QI(0)) + c
    return {b: c for b, c in out.items() if c != 0}


def qadd(*xs):
    out = {}
    for x in xs:
        for b, c in x.items():
            out[b] = out.get(b, GA.QI(0)) + c
    return {b: c for b, c in out.items() if c != 0}


def q(x, c=1):
    return {b: GA.QI(cc) * c for b, cc in x.items()}


def check_real_time_dressing_exact():
    premise("singularity.number-diagonal-dynamics-models-scrambling-derived")
    premise("synthesis.phase-flow-is-time-rotor-flow-kms-continuation")
    premise("scrambling.spreading-law-chaos-bound-saturated")
    c, s = F(3, 5), F(4, 5)
    assert c * c + s * s == 1
    I = GA.QI(0, 1)
    one = q(GA.sc(1))
    U, Ui = one, one
    for k in (1, 2, 3):
        Z = q(m(sig(0), sig(k)))
        U = qmul(U, qadd(q(GA.sc(c)), {b: z * I * s for b, z in Z.items()}))
        Ui = qmul(Ui, qadd(q(GA.sc(c)), {b: z * I * (-s) for b, z in Z.items()}))
    assert qmul(U, Ui) == one                                       # unitary, exactly
    ev = qmul(U, qmul(q(v(0)), Ui))
    c2, s2 = c * c - s * s, 2 * s * c
    assert (c2, s2) == (F(-7, 25), F(24, 25))
    D = one
    for k in (1, 2, 3):
        D = qmul(D, qadd(q(GA.sc(c2)), {b: z * I * (-s2) for b, z in q(sig(k)).items()}))
    assert qadd(ev, q(qmul(q(v(0)), D), -1)) == {}                  # v0(t) = v0 prod_k (c2 - i s2 sigma_k)
    # size distribution: weight of |S| = j in the product is C(3, j) s2^{2j} c2^{2(3-j)}; mean 3 s2^2
    w = [1 * c2 ** 6, 3 * s2 ** 2 * c2 ** 4, 3 * s2 ** 4 * c2 ** 2, s2 ** 6]
    assert sum(w) == 1
    assert sum(j * w[j] for j in range(4)) == 3 * s2 ** 2 == F(1728, 625)
    # chain dressing: v0 evolved under J sigma_0 sigma_1 only anticommutes with v3, v3^*
    Uc = qadd(q(GA.sc(c)), {b: z * I * s for b, z in q(m(sig(0), sig(1))).items()})
    Uci = qadd(q(GA.sc(c)), {b: z * I * (-s) for b, z in q(m(sig(0), sig(1))).items()})
    evc = qmul(Uc, qmul(q(v(0)), Uci))
    for w3 in (v(3), vs(3)):
        assert qadd(qmul(evc, q(w3)), qmul(q(w3), evc)) == {}
    assert qadd(qmul(evc, q(v(1))), qmul(q(v(1)), evc)) != {}       # mode 1 is reached
    return True
