"""standard-model.one-vev-vector-relations-breaking-pattern: exact checks.

Five-mode module Lambda(C^5) in the occupation basis (pairs 1, 2, 3; rungs 4, 5), v_a creation,
w_a contraction, the pairing B of the five-mode lemma, the sixteen = even states with species by
(occupied rungs, occupied pairs). Coefficients are Gaussian rationals (GA.QI), so c = a v_4 + b w_4
is tested at complex sample points (a, b), magnitudes compared through |.|^2.
(1) M_c(psi, phi) = B(psi, c phi) is nonzero exactly on (L, nu^c), (Q, u^c) with |entry|^2 = |a|^2
and on (L, e^c), (Q, d^c) with |entry|^2 = |b|^2.
(2) The conjugate c* (v_j* = w_j, conjugate-linear) is bbar v_4 + abar w_4, and M_{c*} has |b|^2 on
(Q, u^c), (L, nu^c): with the entries |b| of M_c on (Q, d^c), (L, e^c), all four tree masses equal |b|;
read through c itself the up-type entry is |a|, so m_u/m_d = |a|/|b| there.
(3) The v_4 term couples only the T_3 = -1/2 members of L and Q, the w_4 term only T_3 = +1/2.
(4) The stabiliser of c in su(2) + u(1)_Y = span(v_4 w_5, v_5 w_4, (N_4 - N_5)/2, Y) is one-dimensional,
spanned by T_3 - Y, for every sample (a, b): SU(2) x U(1)_Y breaks to a U(1).
The doublet-triplet sentence and the comparison with the lift-locus theorem are readings and are not
checked here.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from pyutil import get_or_set
from tp_premise import premise

QI = GA.QI
N = 5
STATES = [frozenset(c) for r in range(N + 1) for c in combinations(range(1, N + 1), r)]
FULL = frozenset(range(1, N + 1))
EVEN = [S for S in STATES if len(S) % 2 == 0]
NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}


def act(op, st):
    out = {}
    for (kind, i), c in op.items():
        for S, a in st.items():
            if kind == "v" and i not in S:
                T = S | {i}
            elif kind == "w" and i in S:
                T = S - {i}
            else:
                continue
            sign = -1 if sum(1 for j in S if j < i) % 2 else 1
            out[T] = QI(0) + out.get(T, QI(0)) + c * a * sign
    return {k: v for k, v in out.items() if v != 0}


def perm_sign(seq):
    s = 1
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s


def B(psi, phi):
    tot = QI(0)
    for S, a in psi.items():
        Sc = FULL - S
        if Sc in phi:
            k = len(S)
            tot = tot + a * phi[Sc] * ((-1) ** (k * (k - 1) // 2) * perm_sign(sorted(S) + sorted(Sc)))
    return tot


def jk(S):
    return len(S & {4, 5}), len(S & {1, 2, 3})


def norm2(z):
    z = QI(0) + z
    return z.re * z.re + z.im * z.im


def mass_form(c):
    """{species pair: set of |entry|^2} over the nonzero entries of M_c on the sixteen."""
    out = {}
    for S in EVEN:
        for T in EVEN:
            val = B({S: QI(1)}, act(c, {T: QI(1)}))
            if val != 0:
                key = tuple(sorted((NAMES[jk(S)], NAMES[jk(T)])))
                get_or_set(out, key, set()).add(norm2(val))
    return out


def star(c):
    """The conjugate-linear antiautomorphism on vectors: v_j* = w_j, w_j* = v_j."""
    swap = {"v": "w", "w": "v"}
    return {(swap[k], j): (QI(0) + z).conj() for (k, j), z in c.items()}


SAMPLES = [(QI(5), QI(F(2, 7))), (QI(3, 4), QI(1, -2)), (QI(F(-2, 3)), QI(0, 5)), (QI(1, 1), QI(F(1, 2), 3))]


def vev(a, b):
    return {("v", 4): a, ("w", 4): b}


def check_mass_form_magnitudes():
    premise("standard-model.yukawa-pattern-two-rung-module")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for a, b in SAMPLES:
        A2, B2 = norm2(a), norm2(b)
        ok = ok and mass_form(vev(a, b)) == {("L", "nu^c"): {A2}, ("Q", "u^c"): {A2},
                                             ("L", "e^c"): {B2}, ("Q", "d^c"): {B2}}
    # one sample by hand: a = 5, b = 2/7 gives |a|^2 = 25, |b|^2 = 4/49
    ok = ok and mass_form(vev(QI(5), QI(F(2, 7))))[("L", "nu^c")] == {25}
    ok = ok and mass_form(vev(QI(5), QI(F(2, 7))))[("Q", "d^c")] == {F(4, 49)}
    GA.check("one vev: M_c has |a| on (L,nu^c), (Q,u^c) and |b| on (L,e^c), (Q,d^c)", ok)
    return ok


def check_conjugate_reading_gives_four_equal_masses():
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    premise("standard-model.yukawa-pattern-two-rung-module")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for a, b in SAMPLES:
        cs = star(vev(a, b))
        ok = ok and cs == {("w", 4): a.conj(), ("v", 4): b.conj()}
        up = mass_form(cs)
        down = mass_form(vev(a, b))
        m = {norm2(b)}
        ok = ok and up[("Q", "u^c")] == m and up[("L", "nu^c")] == m
        ok = ok and down[("Q", "d^c")] == m and down[("L", "e^c")] == m
        # read through c itself: m_u^2 / m_d^2 = |a|^2 / |b|^2
        ok = ok and next(iter(down[("Q", "u^c")])) * norm2(b) == next(iter(down[("Q", "d^c")])) * norm2(a)
    GA.check("one vev: through c* the four Dirac masses are all |b|; through c, m_u/m_d = |a|/|b|", ok)
    return ok


def check_rung_terms_select_isospin_components():
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for kind, t3 in (("v", F(-1, 2)), ("w", F(1, 2))):
        seen = set()
        for S in EVEN:
            for T in EVEN:
                if B({S: QI(1)}, act({(kind, 4): QI(1)}, {T: QI(1)})) != 0:
                    for U in (S, T):
                        if NAMES[jk(U)] in ("L", "Q"):
                            seen.add(F((4 in U) - (5 in U), 2))
        ok = ok and seen == {t3}
    GA.check("one vev: the v_4 term couples T_3 = -1/2 members of L, Q; the w_4 term T_3 = +1/2", ok)
    return ok


HALF, I_ = F(1, 2), QI(0, 1)


def e45(st):
    return act({("v", 4): QI(1)}, act({("w", 5): QI(1)}, st))


def e54(st):
    return act({("v", 5): QI(1)}, act({("w", 4): QI(1)}, st))


def t3(st):
    return {S: z * (HALF * ((4 in S) - (5 in S))) for S, z in st.items() if (4 in S) != (5 in S)}


def hyp(st):
    return {S: z * F(3 * len(S & {4, 5}) - 2 * len(S & {1, 2, 3}), 6) for S, z in st.items()
            if 3 * len(S & {4, 5}) != 2 * len(S & {1, 2, 3})}


def plus(f, g, cf, cg):
    def h(st):
        out = {}
        for k, v in f(st).items():
            out[k] = out.get(k, QI(0)) + cf * v
        for k, v in g(st).items():
            out[k] = out.get(k, QI(0)) + cg * v
        return {k: v for k, v in out.items() if v != 0}
    return h


# the real Lie algebra su(2) + u(1)_Y by anti-Hermitian generators
GENS = [plus(e45, e54, I_, I_), plus(e45, e54, QI(1), QI(-1)), plus(t3, t3, I_, QI(0)), plus(hyp, hyp, I_, QI(0))]


def flat(op):
    out = []
    for S in STATES:
        st = op({S: QI(1)})
        for T in STATES:
            z = QI(0) + st.get(T, QI(0))
            out += [z.re, z.im]
    return out


def comm_vec(g, c):
    return flat(lambda st: {k: v for k, v in
                            [(T, g(act(c, st)).get(T, QI(0)) - act(c, g(st)).get(T, QI(0))) for T in STATES]
                            if v != 0})


def vec(c):
    return flat(lambda st: act(c, st))


def check_breaking_to_one_u1():
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    ok = True
    # hand values: [i(E45 + E54), v_4] = i v_5, [E45 - E54, v_4] = -v_5, [i T_3, v_4] = [i Y, v_4] = (i/2) v_4,
    # [i T_3, w_4] = [i Y, w_4] = (-i/2) w_4
    v4, w4 = {("v", 4): QI(1)}, {("w", 4): QI(1)}
    ok = ok and comm_vec(GENS[0], v4) == vec({("v", 5): QI(0, 1)})
    ok = ok and comm_vec(GENS[1], v4) == vec({("v", 5): QI(-1)})
    ok = ok and comm_vec(GENS[2], v4) == vec({("v", 4): QI(0, F(1, 2))}) == comm_vec(GENS[3], v4)
    ok = ok and comm_vec(GENS[2], w4) == vec({("w", 4): QI(0, F(-1, 2))}) == comm_vec(GENS[3], w4)
    for a, b in SAMPLES + [(QI(1), QI(0)), (QI(0), QI(2, -1))]:
        c = {k: v for k, v in vev(a, b).items() if v != 0}
        cols = [comm_vec(g, c) for g in GENS]
        # a one-dimensional stabiliser, spanned by i (T_3 - Y)
        ok = ok and 4 - GA.field_rank(cols) == 1
        ok = ok and cols[2] == cols[3] and any(x != 0 for x in cols[2])
    GA.check("one vev: a vector along one rung breaks su(2) + u(1)_Y to the u(1) of T_3 - Y", ok)
    return ok
