"""standard-model.moment-map-grip-mass-are-insensitive: exact checks.

The five-mode module Lambda(W + R_2) = Lambda(C^5) (pair modes 0, 1, 2, rung modes 3, 4), exact,
with the Fock form (a product form: orthonormal occupation basis, Gaussian-rational states). The
ground vectors V_C are the six pair operators v_a, w_a with g(v_a, w_b) = delta_ab / 2; for an
ambient vector I of V the generator A(U ^ I) = (U I - I U)/2 is a bivector of V_C, the moment is
M_{U ^ I}(Psi) = <Psi, A(U ^ I) Psi>, the grip P(Psi) is the vector of V_C with g(P, U) = M_{U ^ I}
for the six basis vectors U, and m^2 = g(P, P). The rung mixing A in U(2) acts on the module as
Lambda(1 + A): rung creators substituted by A, pair creators untouched. Checked, for two frozen
points I and three states:
(i) M and P are sums over the rung-number components Psi_0 + Psi_1 + Psi_2 (no cross-sector
    terms), and P and m^2 are invariant under two unitary rung mixings (Gaussian-rational), which
    preserve the Fock form;
(ii) on the doublet sector the moment is <psi_1, A_W psi_1> + <psi_2, A_W psi_2> with A_W the 8 x 8
    block on Lambda W, and on each singlet sector the single component's moment; so P is the sum
    of the components' grips;
(iii) the grip and m^2 depend on the components only as a multiset: swapping the two slot states
    of the doublet, or moving a single component between the two singlet sectors (j = 0, 2, both
    of size one), leaves them unchanged.
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


mm, madd, msc, comm = fock.mm, fock.madd, fock.msc, fock.comm


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

QI = GA.QI
U_BASIS = [VOP[0], VOP[1], VOP[2], WOP[0], WOP[1], WOP[2]]
FROZEN = [madd(VOP[0], WOP[0]), madd(VOP[1], msc(-2, WOP[1]), msc(3, VOP[2]), WOP[2])]
MIXINGS = [[[QI(F(3, 5)), QI(0, F(4, 5))], [QI(0, F(4, 5)), QI(F(3, 5))]],
           [[QI(F(1, 2), F(1, 2)), QI(F(1, 2), F(-1, 2))], [QI(F(1, 2), F(-1, 2)), QI(F(1, 2), F(1, 2))]]]


def sample_state(seed, d=DIM):
    return [QI(F((seed * (s + 3)) % 7 - 3, 2), F((seed * (s + 5)) % 5 - 2, 3)) for s in range(d)]


STATES = [sample_state(1), sample_state(2), sample_state(5)]
COMPONENTS = [sample_state(3, 8), sample_state(4, 8), sample_state(6, 8)]


def apply(X, psi):
    out = [QI(0)] * len(psi)
    for (r, c), x in X.items():
        out[r] = out[r] + psi[c] * x
    return out


def form(phi, psi):
    return sum((a.conj() * b for a, b in zip(phi, psi)), QI(0))


def gen(U, I):
    return msc(F(1, 2), madd(mm(U, I), msc(-1, mm(I, U))))


def moments(psi, I):
    return [form(psi, apply(gen(U, I), psi)) for U in U_BASIS]


def grip(psi, I):
    """Coordinates of P on (v_0, v_1, v_2, w_0, w_1, w_2): g(P, v_a) = c_{w_a}/2 etc."""
    M = moments(psi, I)
    return [2 * M[3 + a] for a in range(3)] + [2 * M[a] for a in range(3)]


def g_PP(P):
    return sum((P[a] * P[3 + a] for a in range(3)), QI(0))


def vadd(*vs):
    return [sum((v[i] for v in vs), QI(0)) for i in range(len(vs[0]))]


def project_j(psi, j):
    return [psi[s] if nr(s) == j else QI(0) for s in range(DIM)]


def embed(psi_w, rung_bits):
    """e_R (x) psi_W: the state with pair part psi_W and rung pattern rung_bits (0..3)."""
    return [psi_w[s & 7] if (s >> 3) == rung_bits else QI(0) for s in range(DIM)]


def mixing_operator(A):
    """Lambda(1 + A) on the module: |s> = (pair creators)(rung creators)|0>, rung creators
    replaced by sum_b A_{b a} c_b^dagger."""
    cols = {}
    for s in range(DIM):
        vec = [QI(1)] + [QI(0)] * (DIM - 1)
        for m in (4, 3):
            if s >> m & 1:
                new = [QI(0)] * DIM
                for b, mb in enumerate(SLOTS):
                    t = apply(VOP[mb], vec)
                    new = [x + A[b][m - 3] * y for x, y in zip(new, t)]
                vec = new
        for m in (2, 1, 0):
            if s >> m & 1:
                vec = apply(VOP[m], vec)
        cols[s] = vec
    return {(r, s): cols[s][r] for s in range(DIM) for r in range(DIM) if cols[s][r]}


def check_sector_additivity_and_rung_mixing_invariance():
    premise("standard-model.module-factorises-even-ground-elements-act")
    ok = True
    Gs = [mixing_operator(A) for A in MIXINGS]
    for G in Gs:
        # unitary for the Fock form on basis states
        for s in range(DIM):
            col = apply(G, [QI(1) if t == s else QI(0) for t in range(DIM)])
            ok = ok and form(col, col) == QI(1)
    for I in FROZEN:
        for psi in STATES:
            parts = [project_j(psi, j) for j in range(3)]
            M = moments(psi, I)
            ok = ok and M == vadd(*[moments(x, I) for x in parts])
            P = grip(psi, I)
            ok = ok and P == vadd(*[grip(x, I) for x in parts])
            ok = ok and any(m != QI(0) for m in M)
            for G in Gs:
                Gpsi = apply(G, psi)
                ok = ok and grip(Gpsi, I) == P and g_PP(grip(Gpsi, I)) == g_PP(P)
                ok = ok and Gpsi != psi
    GA.check("(i) moment and grip add over rung sectors and are invariant under the rung mixing U(2)", ok)
    return ok


def block_w(X):
    return {(r, c): x for (r, c), x in X.items() if r < 8 and c < 8}


def check_sum_over_slot_components():
    premise("standard-model.module-factorises-even-ground-elements-act")
    ok = True
    for I in FROZEN:
        for p1, p2 in combinations(COMPONENTS, 2):
            dbl = vadd(embed(p1, 1), embed(p2, 2))
            want = [form(p1, apply(block_w(gen(U, I)), p1)) + form(p2, apply(block_w(gen(U, I)), p2))
                    for U in U_BASIS]
            ok = ok and moments(dbl, I) == want
        for p1 in COMPONENTS:
            want = [form(p1, apply(block_w(gen(U, I)), p1)) for U in U_BASIS]
            ok = ok and moments(embed(p1, 0), I) == want and moments(embed(p1, 3), I) == want
    GA.check("(ii) the doublet's moment is the sum of its two components' moments, a singlet's its one", ok)
    return ok


def check_grip_depends_on_the_multiset():
    premise("standard-model.module-factorises-even-ground-elements-act")
    ok = True
    for I in FROZEN:
        for p1, p2 in combinations(COMPONENTS, 2):
            a = grip(vadd(embed(p1, 1), embed(p2, 2)), I)
            b = grip(vadd(embed(p2, 1), embed(p1, 2)), I)
            ok = ok and a == b and g_PP(a) == g_PP(b)
            ok = ok and a == vadd(grip(embed(p1, 0), I), grip(embed(p2, 3), I))
        for p1 in COMPONENTS:
            ok = ok and grip(embed(p1, 0), I) == grip(embed(p1, 3), I)
    GA.check("(iii) the grip and mass depend only on the multiset of slot components", ok)
    return ok
