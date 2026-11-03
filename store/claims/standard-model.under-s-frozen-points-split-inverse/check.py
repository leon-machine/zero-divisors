"""standard-model.under-s-frozen-points-split-inverse: exact checks.

The five-mode module Lambda(C^5) (pair modes 0, 1, 2 = W, rung modes 3, 4 = R_2), exact, with
6Y = 3 N_R - 2 N_W, 2T_3 = n_3 - n_4 and the colour Cartan n_0, n_1, n_2; and Gaussian-rational
two-spinors for the slot components' spinor parts, with the grip momentum of Theorem
standard-model.grip-mass-two-rung-module (one null momentum pi pi-bar per slot component, m^2 =
2 det of their sum). Checked:
(1) the one-mode states: (1,0) x 2 with Y = 1/2, T_3 = +-1/2, colour singlet, and (0,1) x 3 with
    Y = -1/3, T_3 = 0, colour weights of a triplet: the 5 split along the slot/pair line;
(2) the number of slot components of a state in sector (j, k), read off the module (the rung
    patterns occurring there), is 2 for the doublet and 1 for each triplet state; one component
    gives m^2 = 0 for every spinor, two give m^2 = 2 |[pi^1 pi^2]|^2, nonzero for non-proportional
    spinor parts: the doublet carries the area mass, the triplet none;
(3) over all twelve sectors of the module (every Spin(10) multiplet realised in it, whatever its
    colour), the mass is supported exactly on the slot-doublet sectors j = 1; the demanded split
    (Corollary standard-model.direction-demanded-content-doublet-heavy: doublets light, colour
    triplets heavy) is the opposite assignment on the 5.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from pyutil import get_or_set
import fock
from tp_premise import premise

# ---------------------------------------------------------------------------
# The five-mode module Lambda(W + R_2) = Lambda(C^5), exact. States are bitmasks 0..31, mode m
# occupied when bit m is set; modes 0, 1, 2 are the pair modes (W), modes 3, 4 the rung (slot)
# modes, the text's v_4, v_5. Operators are sparse matrices {(row, col): number}; creation has the
# Jordan-Wigner sign (-1)^(occupied modes below m). Sector of a state: (j, k) = (rung number,
# pair number); 6Y = 3j - 2k. The invariant pairing B(psi, phi) pairs a state only with its
# complement.
# ---------------------------------------------------------------------------
NM, DIM, FULL = 5, 32, 31
PAIRS, SLOTS = (0, 1, 2), (3, 4)
SPECIES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}


def nr(s):
    return sum(1 for m in SLOTS if s >> m & 1)


def nw(s):
    return sum(1 for m in PAIRS if s >> m & 1)


def sector(s):
    return (nr(s), nw(s))


madd, msc, comm = fock.madd, fock.msc, fock.comm


ONE = fock.eye(DIM)
VOP = [fock.cre(m, NM) for m in range(NM)]  # v_m, creation
WOP = [fock.ann(m, NM) for m in range(NM)]  # w_m, annihilation
NUM = [fock.num(m, NM) for m in range(NM)]
YOP6 = madd(msc(3, madd(NUM[3], NUM[4])), msc(-2, madd(NUM[0], NUM[1], NUM[2])))   # 6Y
T3OP2 = madd(NUM[3], msc(-1, NUM[4]))                                               # 2 T_3
EVEN = [s for s in range(DIM) if (nr(s) + nw(s)) % 2 == 0]


def ad_weight(H, x):
    """The eigenvalue of ad(H) on the operator x (None if x is not an eigenvector)."""
    c = comm(H, x)
    key, v = next(iter(x.items()))
    lam = c.get(key, 0) / v
    return lam if not madd(c, msc(-lam, x)) else None


def wedge_sign(S, T):
    sgn = 1
    for i in range(NM):
        if T >> i & 1:
            sgn *= (-1) ** bin(S >> (i + 1)).count("1")
    return sgn


def bpair(S, T):
    """B on basis states: nonzero only for T the complement of S."""
    if T != FULL ^ S:
        return 0
    k = bin(S).count("1")
    return wedge_sign(S, T) * (-1) ** (k * (k - 1) // 2)


def mass_form(c):
    """M_c(S, T) = B(S, c T) on the sixteen (even states): {(S, T): value}."""
    out = {}
    for (r, t), x in c.items():
        if t in EVEN:
            S = FULL ^ r
            if S in EVEN:
                val = bpair(S, r) * x
                if val:
                    out[(S, t)] = out.get((S, t), 0) + val
    return {key: v for key, v in out.items() if v}


def species_entries(c):
    """{(species, species) sorted: set of |entry|^2} of the mass form of c."""
    out = {}
    for (S, T), val in mass_form(c).items():
        key = tuple(sorted([SPECIES[sector(S)], SPECIES[sector(T)]]))
        mag2 = val * val if not hasattr(val, "conj") else (val * val.conj()).re
        get_or_set(out, key, set()).add(mag2)
    return out
# ---------------------------------------------------------------------------
# Two-component spinors over Q(i) (GA.QI): the momentum of a single conformal spinor is
# p_{AA'} = pi_A conj(pi_A'), a 2x2 Hermitian matrix with p^2 = 2 det p (the convention of the
# grip Fact); the slot bracket [pi^1 pi^2] = det(pi^i_A).
# ---------------------------------------------------------------------------
QI = GA.QI


def momentum(pi):
    return [[pi[a] * pi[b].conj() for b in range(2)] for a in range(2)]


def msum(ps):
    out = [[QI(0), QI(0)], [QI(0), QI(0)]]
    for p in ps:
        out = [[out[a][b] + p[a][b] for b in range(2)] for a in range(2)]
    return out


def mass2(ps):
    """m^2 = 2 det(sum p), a real number (a Fraction) for Hermitian momenta."""
    P = msum(ps)
    m = 2 * (P[0][0] * P[1][1] - P[0][1] * P[1][0])
    assert m.im == 0
    return m.re


def bracket(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]


def absq(z):
    return z * z.conj()


def mix(A, pis):
    """Slot mixing of the components: pi'_a = sum_b A_ab pi_b."""
    return [[sum((A[a][b] * pis[b][i] for b in range(len(pis))), QI(0)) for i in range(2)]
            for a in range(len(pis))]

SPINORS = [[QI(1, 0), QI(0, 1)], [QI(2, -1), QI(1, 1)], [QI(0, 3), QI(-1, 2)],
           [QI(F(1, 2), 0), QI(F(3, 2), -1)], [QI(-1, 1), QI(4, 0)]]


def colour_weight(s):
    n = [s >> m & 1 for m in PAIRS]
    t = sum(n)
    return tuple(3 * x - t for x in n)


def components(sec):
    """The slot components of a state in a sector: the distinct rung patterns there."""
    return sorted({s >> 3 for s in range(DIM) if sector(s) == sec})


def mass_values(ncomp):
    """m^2 over all ordered choices of ncomp sample spinors (repeats allowed)."""
    out = set()
    for idx in combinations(range(len(SPINORS)), ncomp):
        out.add(mass2([momentum(SPINORS[i]) for i in idx]))
    return out


def check_one_mode_states_are_the_split_five():
    premise("standard-model.under-s-composites-state-space-spinor")
    premise("standard-model.hyp-s-slot-statistics")
    one = [s for s in range(DIM) if bin(s).count("1") == 1]
    data = sorted((sector(s), YOP6.get((s, s), 0), T3OP2.get((s, s), 0), colour_weight(s)) for s in one)
    want = sorted([((0, 1), -2, 0, (2, -1, -1)), ((0, 1), -2, 0, (-1, 2, -1)), ((0, 1), -2, 0, (-1, -1, 2)),
                   ((1, 0), 3, 1, (0, 0, 0)), ((1, 0), 3, -1, (0, 0, 0))])
    ok = data == want
    GA.check("the one-mode states: a slot doublet of Y = 1/2 and a pair triplet of Y = -1/3", ok)
    return ok


def check_doublet_massive_triplet_massless():
    premise("standard-model.grip-mass-two-rung-module")
    ok = len(components((1, 0))) == 2 and len(components((0, 1))) == 1
    # one component: null momentum, massless for every spinor
    ok = ok and mass_values(1) == {F(0)}
    # two components: the area formula, nonzero unless proportional
    for a, b in combinations(SPINORS, 2):
        m2 = mass2([momentum(a), momentum(b)])
        ok = ok and m2 == 2 * absq(bracket(a, b)) and m2 != 0
    pr = [QI(3, 1) * x for x in SPINORS[1]]
    ok = ok and mass2([momentum(SPINORS[1]), momentum(pr)]) == 0
    GA.check("the doublet has two slot components and the area mass; each triplet state one, massless", ok)
    return ok


def check_mass_supported_on_slot_doublets_everywhere():
    premise("standard-model.grip-mass-two-rung-module")
    premise("standard-model.direction-demanded-content-doublet-heavy")
    sectors = sorted({sector(s) for s in range(DIM)})
    massive = sorted(sec for sec in sectors if mass_values(len(components(sec))) != {F(0)})
    ok = len(sectors) == 12 and massive == [(1, k) for k in range(4)]
    # the 5: the frozen point's heavy member is the doublet, the demanded heavy member the triplet
    five = sorted({sector(s) for s in range(DIM) if bin(s).count("1") == 1})
    fp_heavy = [sec for sec in five if sec in massive]
    demanded_heavy = [sec for sec in five if colour_weight(next(s for s in range(DIM) if sector(s) == sec)) != (0, 0, 0)]
    ok = ok and fp_heavy == [(1, 0)] and demanded_heavy == [(0, 1)]
    GA.check("the frozen-point mass lives exactly on j = 1 in every multiplet: inverse to the demanded split", ok)
    return ok
