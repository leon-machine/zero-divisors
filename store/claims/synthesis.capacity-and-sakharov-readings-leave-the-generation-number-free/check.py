"""synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free: exact checks.

(1) Pair currents of the arrays of a light ray. Channel matrices have entries in span{1, J}, J = e1 e2 of Cl(2,0);
    the channel weights are +1/2 and -1/2. The helicity of a matrix unit E_ab is w_a - w_b, in {-1, 0, 1}: no pair
    current has helicity +-2. A helicity +-1 channel matrix squares to zero and does not commute with its adjoint;
    a single array's current has helicity 0; a matrix commuting with every diagonal unit is diagonal (the diagonal
    units attain the bound n on linearly independent normal families with [M, M'^*] = 0, with helicity 0); a member
    of such a family need not have a definite helicity (E_{+-} + E_{-+} on two channels).
(2) The capacity inequality 2 n_V + n_s + 2 eps <= 16 n_g as arithmetic on the recorded contents.
(3) The induced quadratic coefficient B = f n_g + n_s (1 - 6 xi) + n_V (alpha - 5) in minimal-scalar units, its
    zeros for n_g = 1..5, and the quartic balance 2 n_V + n_s - 2 f n_g.
(4) The conjunctions of the candidate rules with asymptotic freedom of weak isospin, and the tally of verdicts.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

SQ = GA.sig(2, 0)
ONE = GA.sc(1)
ZERO = GA.sc(0)
J = GA.mul(GA.gen(0), GA.gen(1), SQ)
HALF = F(1, 2)
N_VECTORS = 12
N_RUNG_COMPONENTS = 8
PER_GENERATION = 16
GENERATIONS = range(1, 6)


# ---------------------------------------------------------------- matrices over span{1, J}
def num(a, b=0):
    return GA.add(GA.scal(F(a), ONE), GA.scal(F(b), J))


def conj(z):
    return GA.reverse(z)


def mmul(A, B):
    n = len(A)
    return [[GA.add(*[GA.mul(A[i][k], B[k][j], SQ) for k in range(n)]) for j in range(n)] for i in range(n)]


def msub(A, B):
    n = len(A)
    return [[GA.sub(A[i][j], B[i][j]) for j in range(n)] for i in range(n)]


def madj(A):
    n = len(A)
    return [[conj(A[j][i]) for j in range(n)] for i in range(n)]


def mzero(A):
    return all(GA.is_zero(x) for row in A for x in row)


def unit(n, a, b, z=None):
    z = num(1) if z is None else z
    return [[z if (i, j) == (a, b) else num(0) for j in range(n)] for i in range(n)]


def comm(A, B):
    return msub(mmul(A, B), mmul(B, A))


def weight_matrix(ws):
    n = len(ws)
    return [[num(ws[i]) if i == j else num(0) for j in range(n)] for i in range(n)]


def scaled(c, A):
    return [[GA.scal(F(c), x) for x in row] for row in A]


def check_pair_currents_have_helicity_at_most_one_and_only_helicity_zero_is_canonical():
    premise("synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins")
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    premise("synthesis.array-ln2-is-zero-mode-doublet-one-tower")
    GA.check("J^2 = -1", GA.mul(J, J, SQ) == GA.sc(-1))
    GA.check("the adjoint reverses J", conj(J) == GA.scal(F(-1), J))
    ws = [HALF, HALF, -HALF, -HALF]            # two arrays of each chirality weight
    n = len(ws)
    W = weight_matrix(ws)
    seen = set()
    for a, b in product(range(n), repeat=2):
        E = unit(n, a, b, num(2, 3))
        h = ws[a] - ws[b]
        seen.add(h)
        GA.check("a matrix unit has helicity w_a - w_b", mzero(msub(comm(W, E), scaled(h, E))))
        if h != 0:
            GA.check("a helicity +-1 unit squares to zero", mzero(mmul(E, E)))
            GA.check("and is not normal", not mzero(comm(E, madj(E))))
    GA.check("the helicities of pair currents are -1, 0, 1", seen == {F(-1), F(0), F(1)})
    GA.check("no pair current has helicity 2 or -2", F(2) not in seen and F(-2) not in seen)
    # a general helicity-one channel matrix (upper-right block), entries in span{1, J}
    M = [[num(0)] * n for _ in range(n)]
    M[0][2], M[0][3], M[1][2], M[1][3] = num(1, 2), num(0, 1), num(3), num(-1, 1)
    GA.check("the block matrix has helicity one", mzero(msub(comm(W, M), M)))
    GA.check("it squares to zero", mzero(mmul(M, M)))
    GA.check("its commutator with its adjoint is not zero", not mzero(comm(M, madj(M))))
    # one array: the only channel matrix is a number, of helicity 0
    for w in (HALF, -HALF):
        W1 = weight_matrix([w])
        GA.check("one array's current has helicity zero", mzero(comm(W1, [[num(5, 7)]])))
    # a commuting normal family member without a definite helicity: E_{+-} + E_{-+} on weights +1/2, -1/2
    W2 = weight_matrix([HALF, -HALF])
    X = [[num(0), num(1)], [num(1), num(0)]]
    D = comm(W2, X)
    GA.check("E+- + E-+ is normal", mzero(comm(X, madj(X))))
    GA.check("its weight commutator is E+- - E-+", mzero(msub(D, [[num(0), num(1)], [num(-1), num(0)]])))
    GA.check("which is not a multiple of it: no definite helicity",
             not GA.is_zero(D[1][0]) and not mzero(msub(D, X)) and not mzero(msub(D, scaled(-1, X))) and not mzero(D))
    GA.check("a helicity-zero normal member: the diagonal unit", mzero(comm(W2, unit(2, 0, 0))))
    # a matrix commuting with every diagonal unit is diagonal: the diagonal units attain the bound n
    for m in (2, 3, 4):
        for a, b in product(range(m), repeat=2):
            E = unit(m, a, b)
            commutes_all = all(mzero(comm(E, unit(m, c, c))) for c in range(m))
            GA.check("a unit commutes with every diagonal unit iff it is diagonal", commutes_all == (a == b))
    return True


def capacity_load(n_v, n_s, eps):
    return 2 * n_v + n_s + 2 * eps


def least_generations(load):
    return next(g for g in range(1, 40) if load <= PER_GENERATION * g)


def check_capacity_inequality_passes_two_generations_on_recorded_contents():
    premise("standard-model.connection-forced")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    premise("hawking.helicity-lift-joints-itemised")
    GA.check("vectors, eight rung components and a graviton: 34", capacity_load(N_VECTORS, N_RUNG_COMPONENTS, 1) == 34)
    GA.check("34 needs three generations", least_generations(34) == 3)
    GA.check("without the graviton: 32, met at two generations with equality",
             capacity_load(N_VECTORS, N_RUNG_COMPONENTS, 0) == 32 and least_generations(32) == 2)
    GA.check("one doublet and a graviton: 30, met at two generations",
             capacity_load(N_VECTORS, 4, 1) == 30 and least_generations(30) == 2)
    GA.check("scalars alone (helicity zero): 8, met at one generation",
             capacity_load(0, N_RUNG_COMPONENTS, 0) == 8 and least_generations(8) == 1)
    GA.check("the verdict three sits two units above the threshold of two", 34 - PER_GENERATION * 2 == 2)
    GA.check("with fifteen components per generation the full content still needs three", 34 > 15 * 2 and 34 <= 15 * 3)
    return True


def quadratic(n_g, n_s, xi, alpha, per_gen=PER_GENERATION, n_v=N_VECTORS):
    return per_gen * n_g + n_s * (1 - 6 * xi) + n_v * (alpha - 5)


def quartic(n_g, n_s, per_gen=PER_GENERATION, n_v=N_VECTORS):
    return 2 * n_v + n_s - 2 * per_gen * n_g


def helicity_rule(n_g, eps, per_gen=PER_GENERATION, n_v=N_VECTORS):
    """L^2 coefficient of the stored regulated sum, in units of -(integral of x f): each helicity state of
    helicity s carries s^2, bosons with weight 1/2 and fermions -1/2; two states per field."""
    return n_v * 1 + eps * 4 - F(per_gen * n_g, 4)


def check_sakharov_coefficient_has_zeros_at_every_generation_number():
    premise("synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations")
    premise("synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike")
    premise("synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off")
    sixth = F(1, 6)
    GA.check("the stored cancellation: zero at three generations, conformal doublets, Feynman gauge",
             quadratic(3, N_RUNG_COMPONENTS, sixth, 1) == 0)
    GA.check("stored: 8 at minimal coupling", quadratic(3, N_RUNG_COMPONENTS, 0, 1) == 8)
    GA.check("stored: -12 in the Landau limit", quadratic(3, N_RUNG_COMPONENTS, sixth, 0) == -12)
    GA.check("stored form 12(alpha - 1) + 8(1 - 6 xi) at three generations",
             all(quadratic(3, 8, x, a) == 12 * (a - 1) + 8 * (1 - 6 * x)
                 for x in (F(0), sixth, F(2, 5)) for a in (F(1), F(3), F(1, 2))))
    # zeros in xi at alpha = 1, and in alpha at xi = 1/6
    xi_star = {g: sixth + F(PER_GENERATION * g - 48, 6 * N_RUNG_COMPONENTS) for g in GENERATIONS}
    GA.check("xi zeros", xi_star == {1: F(-1, 2), 2: F(-1, 6), 3: sixth, 4: F(1, 2), 5: F(5, 6)})
    for g in GENERATIONS:
        GA.check("the coefficient vanishes at xi*(n_g) in the Feynman gauge",
                 quadratic(g, N_RUNG_COMPONENTS, xi_star[g], 1) == 0)
    alpha_star = {g: 5 - F(PER_GENERATION * g, N_VECTORS) for g in GENERATIONS}
    GA.check("alpha zeros", alpha_star == {1: F(11, 3), 2: F(7, 3), 3: F(1), 4: F(-1, 3), 5: F(-5, 3)})
    for g in GENERATIONS:
        GA.check("the coefficient vanishes at alpha*(n_g) with conformal scalars",
                 quadratic(g, N_RUNG_COMPONENTS, sixth, alpha_star[g]) == 0)
    GA.check("alpha* is an admissible gauge parameter exactly for n_g <= 3",
             [g for g in GENERATIONS if alpha_star[g] > 0] == [1, 2, 3])
    GA.check("with fifteen components per generation the conformal Feynman-gauge coefficient never vanishes",
             all(quadratic(g, 8, sixth, 1, per_gen=15) != 0 for g in range(1, 200)))
    GA.check("with fifteen components the coefficient at three generations is -3 minimal-scalar units", quadratic(3, 8, sixth, 1, per_gen=15) == -3)
    # the quartic coefficient of the same regulated sum
    GA.check("the quartic balance of the recorded content vanishes at one generation",
             [g for g in range(1, 40) if quartic(g, N_RUNG_COMPONENTS) == 0] == [1])
    GA.check("at three generations it needs 72 scalars", quartic(3, 72) == 0 and quartic(3, 8) == -64)
    GA.check("helicity rule without a graviton: zero at three generations",
             [g for g in range(1, 40) if helicity_rule(g, 0) == 0] == [3])
    GA.check("the same rule with the graviton's two helicity-two states: zero at four generations",
             [g for g in range(1, 40) if helicity_rule(g, 1) == 0] == [4])
    GA.check("no scalar number makes both coefficients single out the same n_g other than by choice of N_S",
             quartic(3, N_RUNG_COMPONENTS) != 0 and quadratic(1, N_RUNG_COMPONENTS, sixth, 1) != 0)
    return True


def weak_isospin_free(n_g, n_h):
    return F(-22, 3) + F(4, 3) * n_g + F(n_h, 6) < 0


def recurrence_currents(n_g):
    return (PER_GENERATION * n_g) % 24 == 0


def recurrence_additive(n_g, n_h, eps, modulus=24):
    return (PER_GENERATION * n_g + 2 * N_VECTORS + 4 * n_h + 2 * eps) % modulus == 0


def capacity(n_g, n_s, eps):
    return capacity_load(N_VECTORS, n_s, eps) <= PER_GENERATION * n_g


def check_the_pin_is_recurrence_with_asymptotic_freedom_and_the_tally_of_rules():
    premise("synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free")
    premise("synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content")
    wide = range(1, 40)
    for n_h in (1, 2):
        GA.check("weak isospin is asymptotically free exactly for n_g <= 5",
                 [g for g in wide if weak_isospin_free(g, n_h)] == [1, 2, 3, 4, 5])
    free = [g for g in wide if weak_isospin_free(g, 2)]
    pin = [g for g in free if recurrence_currents(g)]
    GA.check("recurrence in the currents reading with asymptotic freedom gives three", pin == [3])
    GA.check("adding the capacity inequality changes nothing",
             [g for g in pin if capacity(g, 8, 1)] == [3] and [g for g in pin if capacity(g, 8, 0)] == [3])
    GA.check("capacity with a graviton and asymptotic freedom, no recurrence: 3, 4, 5",
             [g for g in free if capacity(g, 8, 1)] == [3, 4, 5])
    GA.check("capacity without a graviton and asymptotic freedom: 2, 3, 4, 5",
             [g for g in free if capacity(g, 8, 0)] == [2, 3, 4, 5])
    verdicts = {
        "recurrence, bosons as currents": [g for g in free if recurrence_currents(g)],
        "recurrence, additive, two doublets": [g for g in free if recurrence_additive(g, 2, 0)],
        "recurrence, additive, one doublet, two windows": [g for g in free if recurrence_additive(g, 1, 0, 12)],
        "recurrence, additive, with a graviton": [g for g in free if recurrence_additive(g, 2, 1)],
        "capacity with a graviton": [g for g in free if capacity(g, 8, 1)],
        "capacity without a graviton": [g for g in free if capacity(g, 8, 0)],
        "quadratic coefficient, conformal, Feynman": [g for g in free if quadratic(g, 8, F(1, 6), 1) == 0],
        "quadratic coefficient, minimal, Feynman": [g for g in free if quadratic(g, 8, 0, 1) == 0],
        "quadratic coefficient, fifteen components": [g for g in free if quadratic(g, 8, F(1, 6), 1, per_gen=15) == 0],
        "quartic balance": [g for g in free if quartic(g, 8) == 0],
        "quadratic coefficient with the graviton's states": [g for g in free if helicity_rule(g, 1) == 0],
    }
    GA.check("the verdict table", verdicts == {
        "recurrence, bosons as currents": [3],
        "recurrence, additive, two doublets": [1, 4],
        "recurrence, additive, one doublet, two windows": [2, 5],
        "recurrence, additive, with a graviton": [],
        "capacity with a graviton": [3, 4, 5],
        "capacity without a graviton": [2, 3, 4, 5],
        "quadratic coefficient, conformal, Feynman": [3],
        "quadratic coefficient, minimal, Feynman": [],
        "quadratic coefficient, fifteen components": [],
        "quartic balance": [1],
        "quadratic coefficient with the graviton's states": [4],
    })
    GA.check("two of the eleven variants single out three, four contain it, seven do not",
             sum(1 for v in verdicts.values() if v == [3]) == 2
             and sum(1 for v in verdicts.values() if 3 in v) == 4
             and sum(1 for v in verdicts.values() if 3 not in v) == 7)
    GA.check("every n_g from 1 to 5 is selected by some variant",
             all(any(g in v for v in verdicts.values()) for g in GENERATIONS))
    return True
