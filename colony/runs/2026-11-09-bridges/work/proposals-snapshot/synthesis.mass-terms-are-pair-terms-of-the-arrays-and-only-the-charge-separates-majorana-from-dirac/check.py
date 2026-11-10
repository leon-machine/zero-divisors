"""synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac: exact checks.

Four tower modes in Cl(4,4): e_j (square +1), f_j (square -1), w_j = (e_j + f_j)/2, v_j = (e_j - f_j)/2, both
null, {v_j, w_k} = delta_jk, n_j = v_j w_j. Modes 0, 1: the two modes (a, c) of a first array; modes 2, 3: the two
modes of a second array. Pair terms: the cross pairing D = w_0 w_3 + w_2 w_1 and the self pairing S = w_2 w_3 of
the second array. Charges: N (total), L = n_0 + n_1 - n_2 - n_3 (opposite on the two arrays), Na = n_0 + n_2,
Nc = n_1 + n_3 (the fixed charges of the stored gap theorem), Qd = Na - Nc.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = GA.sig(4, 4)
ONE = GA.sc(1)
NMODES = 4
HALF = F(1, 2)
MASS_SAMPLES = ((F(1), F(1)), (F(2), F(3)), (F(1, 3), F(5)), (F(7, 2), F(0)), (F(0), F(4)))
KIN_SAMPLES = (F(0), F(1), F(2, 3))


def e(j):
    return GA.gen(j)


def f(j):
    return GA.gen(NMODES + j)


def w(j):
    return GA.scal(HALF, GA.add(e(j), f(j)))


def v(j):
    return GA.scal(HALF, GA.sub(e(j), f(j)))


def mul(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, SQ)
    return out


def comm(x, y):
    return GA.sub(mul(x, y), mul(y, x))


def n(j):
    return mul(v(j), w(j))


def adjoint(x):
    """Reverse, with f_j -> -f_j: the anti-automorphism exchanging v_j and w_j."""
    out = {}
    for bl, c in GA.reverse(x).items():
        out[bl] = c * (-1) ** sum(1 for i in bl if i >= NMODES)
    return out


def flip(x, modes):
    """The automorphism f_j -> -f_j for j in modes: it exchanges v_j and w_j on those modes."""
    out = {}
    for bl, c in x.items():
        out[bl] = c * (-1) ** sum(1 for i in bl if i >= NMODES and i - NMODES in modes)
    return out


def total(coeffs):
    return GA.add(*[GA.scal(F(c), n(j)) for j, c in enumerate(coeffs)])


def total_frac(coeffs):
    return GA.add(*[GA.scal(c, n(j)) for j, c in enumerate(coeffs)])


CHARGE_SAMPLES = ((F(1), F(2), F(-2), F(-1)), (F(3), F(-3), F(3), F(-3)), (F(1, 2), F(5), F(-5), F(-1, 2)),
                  (F(1), F(1), F(1), F(1)), (F(1), F(2), F(-2), F(1)), (F(1), F(0), F(1), F(-1)), (F(2), F(7), F(-7), F(-2)))

D = GA.add(mul(w(0), w(3)), mul(w(2), w(1)))
S = mul(w(2), w(3))
N = total((1, 1, 1, 1))
L = total((1, 1, -1, -1))
NA = total((1, 0, 1, 0))
NC = total((0, 1, 0, 1))
QD = GA.sub(NA, NC)


def hamiltonian(K, m, M):
    return GA.add(GA.scal(K, N), GA.scal(m, GA.add(D, adjoint(D))), GA.scal(M, GA.add(S, adjoint(S))))


def parity():
    out = ONE
    for j in range(NMODES):
        out = mul(out, GA.sub(ONE, GA.scal(F(2), n(j))))
    return out


def check_one_mode_has_no_pair_term_and_all_mass_terms_are_pair_terms():
    premise("field-theory.imported-tower-limit")
    premise("field-theory.composite-scalars-mean-field-level")
    for j in range(NMODES):
        GA.check("Q(w_j) = 0", GA.is_zero(mul(w(j), w(j))))
        GA.check("Q(v_j) = 0", GA.is_zero(mul(v(j), v(j))))
        GA.check("adjoint exchanges v_j and w_j", GA.eq(adjoint(w(j)), v(j)))
        for k in range(NMODES):
            anti = GA.add(mul(v(j), w(k)), mul(w(k), v(j)))
            GA.check("{v_j, w_k} = delta_jk", GA.eq(anti, GA.sc(1 if j == k else 0)))
            GA.check("{w_j, w_k} = 0", GA.is_zero(GA.add(mul(w(j), w(k)), mul(w(k), w(j)))))
    # a general combination of the w_j is null, so x x = 0: a pair term needs two modes
    x = GA.add(GA.scal(F(2), w(0)), GA.scal(F(-3), w(1)), GA.scal(F(5, 7), w(2)), w(3))
    GA.check("the span of the w_j is null", GA.is_zero(mul(x, x)))
    pairs = [mul(w(j), w(k)) for j, k in combinations(range(NMODES), 2)]
    GA.check("six pair terms on four modes, none on one", len(pairs) == 6 and all(not GA.is_zero(p) for p in pairs))
    # the stored block: ad_H^2 = K^2 + mu^2 on the mode operators of one array
    K, mu = F(2), F(3)
    H1 = GA.add(GA.scal(K, GA.add(n(0), n(1))), GA.scal(mu, GA.add(mul(w(0), w(1)), mul(v(1), v(0)))))
    for op in (w(0), w(1), v(0), v(1)):
        GA.check("stored block: ad^2 = K^2 + mu^2", GA.eq(comm(H1, comm(H1, op)), GA.scal(K * K + mu * mu, op)))


def check_charges_of_the_cross_and_self_pair_terms():
    premise("standard-model.majorana-element")
    premise("synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy")
    premise("synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content")
    GA.check("[N, D] = -2 D", GA.eq(comm(N, D), GA.scal(F(-2), D)))
    GA.check("[N, S] = -2 S", GA.eq(comm(N, S), GA.scal(F(-2), S)))
    GA.check("[L, D] = 0", GA.is_zero(comm(L, D)))
    GA.check("[L, S] = 2 S for the second array's charge -1", GA.eq(comm(L, S), GA.scal(F(2), S)))
    stored = mul(w(0), w(1))
    GA.check("the stored one-array pair term has L charge -2", GA.eq(comm(L, stored), GA.scal(F(-2), stored)))
    GA.check("and Na - Nc charge 0", GA.is_zero(comm(QD, stored)))
    # diagonal charges conserved by D are (alpha, beta, -beta, -alpha); S has charge alpha + beta under them
    for q in CHARGE_SAMPLES:
        C = total_frac(q)
        conserved = (q[0] + q[3] == 0 and q[1] + q[2] == 0)
        GA.check("a diagonal charge commutes with D exactly on the two-parameter family", GA.is_zero(comm(C, D)) == conserved)
        GA.check("S has charge -(q2 + q3)", GA.eq(comm(C, S), GA.scal(-(q[2] + q[3]), S)))
        if conserved:
            GA.check("which is alpha + beta on the family", -(q[2] + q[3]) == q[0] + q[1])
    for X in (D, S):
        GA.check("[Na, X] = -X", GA.eq(comm(NA, X), GA.scal(F(-1), X)))
        GA.check("[Nc, X] = -X", GA.eq(comm(NC, X), GA.scal(F(-1), X)))
        GA.check("[Na - Nc, X] = 0", GA.is_zero(comm(QD, X)))
        GA.check("the grading commutes with X", GA.is_zero(comm(parity(), X)))
    G = parity()
    GA.check("the grading squares to 1", GA.eq(mul(G, G), ONE))
    GA.check("the grading anticommutes with each mode", all(GA.is_zero(GA.add(mul(G, w(j)), mul(w(j), G))) for j in range(NMODES)))
    for K in KIN_SAMPLES:
        for m, M in MASS_SAMPLES:
            H = hamiltonian(K, m, M)
            GA.check("H is self-adjoint", GA.eq(adjoint(H), H))
            GA.check("H commutes with Na - Nc", GA.is_zero(comm(QD, H)))
            GA.check("H commutes with the grading", GA.is_zero(comm(G, H)))
            GA.check("H commutes with L exactly when M = 0", GA.is_zero(comm(L, H)) == (M == 0))
            GA.check("H commutes with N exactly when m = M = 0", GA.is_zero(comm(N, H)) == (m == 0 and M == 0))
            GA.check("H commutes with Na exactly when m = M = 0", GA.is_zero(comm(NA, H)) == (m == 0 and M == 0))


SAMPLE_X = GA.add(w(0), GA.scal(F(2), v(3)), mul(e(1), f(2)))
SAMPLE_Y = GA.add(v(1), GA.scal(F(3), mul(w(2), w(3))))


def check_flip_of_the_second_modes_turns_the_block_into_hopping():
    premise("field-theory.composite-scalars-mean-field-level")
    premise("standard-model.majorana-element")
    second = (1, 3)
    for j in range(NMODES):
        GA.check("the flip exchanges v and w on the second modes only",
                 GA.eq(flip(w(j), second), v(j) if j in second else w(j)))
    x, y = SAMPLE_X, SAMPLE_Y
    GA.check("the flip is multiplicative", GA.eq(flip(mul(x, y), second), mul(flip(x, second), flip(y, second))))
    GA.check("the flip carries Na - Nc to N - 2", GA.eq(flip(QD, second), GA.sub(N, GA.sc(2))))
    GA.check("the flip carries the self pair term to a hop", GA.eq(flip(S, second), mul(w(2), v(3))))
    GA.check("the flip carries L to a charge the hop changes", GA.eq(comm(flip(L, second), flip(S, second)), GA.scal(F(2), flip(S, second))))
    for K in KIN_SAMPLES:
        for m, M in MASS_SAMPLES:
            Hf = flip(hamiltonian(K, m, M), second)
            GA.check("the flipped block conserves the total number", GA.is_zero(comm(N, Hf)))
            GA.check("the flipped block is self-adjoint", GA.eq(adjoint(Hf), Hf))


def check_block_spectrum_is_the_quadratic_with_sum_M_and_product_minus_m_squared():
    premise("field-theory.composite-scalars-mean-field-level")
    modes = [w(j) for j in range(NMODES)] + [v(j) for j in range(NMODES)]
    for m, M in MASS_SAMPLES:
        H = hamiltonian(F(0), m, M)
        for op in modes:
            a2 = comm(H, comm(H, op))
            a4 = comm(H, comm(H, a2))
            lhs = GA.add(a4, GA.scal(-(M * M + 2 * m * m), a2), GA.scal(m ** 4, op))
            GA.check("ad^4 - (M^2 + 2 m^2) ad^2 + m^4 = 0 on the mode operators", GA.is_zero(lhs))
        if m != 0 and M != 0:
            a2 = comm(H, comm(H, w(0)))
            GA.check("ad^2 is not a multiple of the identity when m M != 0",
                     not GA.eq(a2, GA.scal(m * m, w(0))) and not GA.eq(a2, GA.scal(m * m + M * M, w(0))))
    # K != 0: ad^2 - K^2 satisfies the same quadratic
    for K in KIN_SAMPLES:
        for m, M in MASS_SAMPLES:
            H = hamiltonian(K, m, M)
            for op in modes:
                y1 = GA.sub(comm(H, comm(H, op)), GA.scal(K * K, op))
                y2 = GA.sub(comm(H, comm(H, y1)), GA.scal(K * K, y1))
                lhs = GA.add(y2, GA.scal(-(M * M + 2 * m * m), y1), GA.scal(m ** 4, op))
                GA.check("(ad^2 - K^2)^2 - (M^2 + 2 m^2)(ad^2 - K^2) + m^4 = 0", GA.is_zero(lhs))
    # rank: the self term alone gives a mass to the second array only, the cross term alone to all four modes
    HS, HD = hamiltonian(F(0), F(0), F(5)), hamiltonian(F(0), F(3), F(0))
    GA.check("S alone: no mass on the first array", all(GA.is_zero(comm(HS, op)) for op in (w(0), w(1), v(0), v(1))))
    GA.check("S alone: mass M on the second array", all(GA.eq(comm(HS, comm(HS, op)), GA.scal(F(25), op)) for op in (w(2), w(3), v(2), v(3))))
    GA.check("D alone: mass m on all four", all(GA.eq(comm(HD, comm(HD, op)), GA.scal(F(9), op)) for op in modes))
    # y^2 - (M^2 + 2 m^2) y + m^4 has roots x^2 for x^2 - M x - m^2 = 0: check at a rational point of the conic
    m, M = F(2), F(3)                         # roots 4 and -1
    for xr in (F(4), F(-1)):
        GA.check("root of x^2 - M x - m^2", xr * xr - M * xr - m * m == 0)
        y = xr * xr
        GA.check("its square solves the quartic's quadratic", y * y - (M * M + 2 * m * m) * y + m ** 4 == 0)
    GA.check("sum M and product -m^2", F(4) + F(-1) == M and F(4) * F(-1) == -m * m)
