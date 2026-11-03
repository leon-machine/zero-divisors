"""standard-model.bidoublet-complex: exact checks.

The five-mode module as 32 x 32 matrices over Q(i) (GA.QI), pair modes 0, 1, 2 and slot (rung) modes 3, 4,
the text's v_4, w_4 being v_3, w_3 here. As in the proof, the imaginary unit is I (central), gamma_6 = v_4 + w_4
and gamma_7 = I (v_4 - w_4).
(1) The lemma: for real sample (x, y), including the proof's (3, 5), x gamma_6 + y gamma_7 = a v_4 + b w_4 with
    a = x + I y read off the matrix, b = conj(a), |a|^2 = |b|^2 = x^2 + y^2. Conversely a v_4 + b w_4 lies in
    the real span of gamma_6, gamma_7 exactly when b = conj(a) (solved: x = (a + b)/2, y = (a - b)/(2I) real).
(2) The mass form M_c(psi, phi) = B(psi, c phi) on the sixteen (B the invariant pairing of the five modes,
    built from its formula) has its nonzero entries on (L, nu^c), (Q, u^c) with magnitude |a| and on
    (L, e^c), (Q, d^c) with magnitude |b| (the Corollary's entries).
(3) One rung vector, under the c* reading of the one-vev Corollary (up-type masses are the entries of M_{c*}
    on (Q, u^c), (L, nu^c), with c* = conj(b) v_4 + conj(a) w_4; down-type the entries of M_c on (Q, d^c),
    (L, e^c)): for real and complex samples the up-type and down-type magnitudes are equal (both |b|), so
    m_u = m_d at tree level whether the vector is real or complex; control: read through c itself the
    complex samples would separate them.
(4) Two independent couplings, down-type through c_1 and up-type through c_2*: the magnitudes are |b_1| and
    |b_2|, unequal at the samples (ratios of squares 25 and 1/2), so a second doublet coupling separates
    m_u from m_d.
"""
from fractions import Fraction as F

import GA
from pyutil import get_or_set
import fock
from tp_premise import premise

# ---------------------------------------------------------------------------
# The five-mode module Lambda(W + R_2) = Lambda(C^5), exact.
# States are bitmasks s in 0..31; mode m is occupied when bit m is set.
# Modes 0, 1, 2 are the three pair modes (W), modes 3, 4 the two slot (rung)
# modes, the text's modes 4 and 5. Operators are sparse matrices
# {(row, col): Fraction}; Jordan-Wigner sign (-1)^(occupied modes below m).
# ---------------------------------------------------------------------------
NM = 5
DIM = 32
PAIRS = (0, 1, 2)
SLOTS = (3, 4)


def nw(s):
    return sum(1 for m in PAIRS if s >> m & 1)


def nr(s):
    return sum(1 for m in SLOTS if s >> m & 1)


def ntot(s):
    return nw(s) + nr(s)


mm, madd, msc, msub = fock.mm, fock.madd, fock.msc, fock.msub
meq, restrict = fock.meq, fock.restrict


def gam(p):
    """Majorana p = 0..9 of mode p // 2 in the real form: gamma_{2m} = v_m + w_m (square +1),
    g_{2m+1} = w_m - v_m (square -1). The text's gamma_{2m+1} = I g_{2m+1}, I^2 = -1 central."""
    return fock.majorana(p, NM)


ONE = fock.eye(DIM)
V = [fock.cre(m, NM) for m in range(NM)]  # v_m, creation
W = [fock.ann(m, NM) for m in range(NM)]  # w_m, annihilation
NUM = [fock.num(m, NM) for m in range(NM)]  # n_m


class Span:
    """Incremental exact span of sparse vectors (dicts with hashable keys), reduced row echelon."""

    def __init__(self):
        self.piv, self.where = {}, {}

    def reduce(self, v):
        v = {k: x for k, x in v.items() if x}
        for k in [k for k in v if k in self.piv]:
            c = v.pop(k)
            for kk, xx in self.piv[k].items():
                if kk != k:
                    y = v.get(kk, 0) - c * xx
                    if y:
                        v[kk] = y
                    else:
                        v.pop(kk, None)
        return v

    def add(self, v):
        v = self.reduce(v)
        if not v:
            return False
        k0 = next(iter(v))
        c0 = v[k0]
        v = {k: x / c0 for k, x in v.items()}
        for p in list(self.where.get(k0, ())):
            row = self.piv[p]
            c = row.pop(k0)
            for kk, xx in v.items():
                if kk != k0:
                    y = row.get(kk, 0) - c * xx
                    if y:
                        row[kk] = y
                        get_or_set(self.where, kk, set()).add(p)
                    else:
                        row.pop(kk, None)
                        self.where.get(kk, set()).discard(p)
        self.where.pop(k0, None)
        self.piv[k0] = v
        for kk in v:
            if kk != k0:
                get_or_set(self.where, kk, set()).add(k0)
        return True

    def __len__(self):
        return len(self.piv)


def rank(vecs):
    """Exact rank of sparse vectors (dicts with hashable keys)."""
    sp = Span()
    for v in vecs:
        sp.add(v)
    return len(sp)


def in_span(vecs, v):
    sp = Span()
    for u in vecs:
        sp.add(u)
    return not sp.reduce(v)


def bilinears():
    """The 45 products g_p g_q, p < q, of the real-form Majoranas (the bivectors of the ten,
    up to the central factors of I)."""
    G = [gam(p) for p in range(2 * NM)]
    return {(p, q): mm(G[p], G[q]) for p in range(2 * NM) for q in range(p + 1, 2 * NM)}


def commutant_dim(gens, states):
    """Dimension of {X on span(states) : [X, g] = 0 for all g}, by exact sparse elimination."""
    S = list(states)
    Sset = set(S)
    rows = []
    for g in gens:
        g = restrict(g, S)
        grow, gcol = {}, {}
        for (r, c), x in g.items():
            get_or_set(grow, r, []).append((c, x))
            get_or_set(gcol, c, []).append((r, x))
        for r in S:
            for c in S:
                eq = {}
                # (X g)_{rc} = sum_k X_{rk} g_{kc};  (g X)_{rc} = sum_k g_{rk} X_{kc}
                for k, x in gcol.get(c, ()):
                    eq[(r, k)] = eq.get((r, k), 0) + x
                for k, x in grow.get(r, ()):
                    eq[(k, c)] = eq.get((k, c), 0) - x
                eq = {k: x for k, x in eq.items() if x}
                if eq:
                    rows.append(eq)
    return len(S) * len(S) - rank(rows)

QI = GA.QI
I = GA.QI_I
SAMPLES = [(F(3), F(5)), (F(-2), F(7, 3)), (F(1, 2), F(-4)), (F(6), F(0))]
MASS_FORM_AB = ((QI(3, 5), QI(3, -5)), (QI(3), QI(1)))   # sample (a, b): the proof's real (3, 5) and a complex pair
SPECIES = {(0, 0): "nuc", (2, 0): "uc", (1, 1): "Q", (3, 1): "L", (0, 2): "ec", (2, 2): "dc"}


def species(s):
    return SPECIES.get((nw(s), nr(s)))


def pairing():
    B = {}
    for s in range(DIM):
        S = [m for m in range(NM) if s >> m & 1]
        seq = S + [m for m in range(NM) if not s >> m & 1]
        inv = sum(1 for i in range(NM) for j in range(i + 1, NM) if seq[i] > seq[j])
        k = len(S)
        B[(s, (DIM - 1) ^ s)] = F((-1) ** (k * (k - 1) // 2 + inv))
    return B


def rung_vector(x, y):
    g6 = madd(V[3], W[3])
    g7 = msc(I, msub(V[3], W[3]))
    return madd(msc(QI(x), g6), msc(QI(y), g7))


def norm2(z):
    z = QI(z)
    return (z * z.conj()).re


def check_real_rung_vector_has_conjugate_coefficients():
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for x, y in SAMPLES:
        c = rung_vector(x, y)
        a, b = c[(8, 0)], c[(0, 8)]
        ok = ok and meq(c, madd(msc(a, V[3]), msc(b, W[3])))
        ok = ok and b == a.conj() and norm2(a) == norm2(b) == x * x + y * y
    ok = ok and rung_vector(F(3), F(5))[(8, 0)] == QI(3, 5)
    # converse: a v + b w is real (x, y real) iff b = conj(a)
    for a, b, real in ((QI(2, 1), QI(2, -1), True), (QI(1), QI(0), False), (QI(0, 3), QI(0, 3), False)):
        x, y = (a + b) / 2, (a - b) / (2 * I)
        ok = ok and ((x.im == 0 and y.im == 0) == real) and ((b == a.conj()) == real)
    GA.check("a real vector of the rung plane is a v4 + conj(a) w4", ok)
    return ok


def check_mass_form_magnitudes():
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.hyp-s-slot-statistics")
    B = pairing()
    sixteen = [s for s in range(DIM) if ntot(s) % 2 == 0]
    ok = True
    for a, b in MASS_FORM_AB:
        c = rung(a, b)                       # a v_4 + b w_4
        M = mm(B, c)
        mags = {}
        for (r, col), z in M.items():
            if r in sixteen and col in sixteen:
                pair = tuple(sorted((species(r), species(col))))
                if pair not in mags:
                    mags[pair] = set()
                mags[pair].add(norm2(z))
        want = {("L", "nuc"): {norm2(a)}, ("Q", "uc"): {norm2(a)},
                ("L", "ec"): {norm2(b)}, ("Q", "dc"): {norm2(b)}}
        ok = ok and mags == want
    GA.check("the mass form has |a| on (L, nu^c), (Q, u^c) and |b| on (L, e^c), (Q, d^c)", ok)
    return ok


def rung(a, b):
    return madd(msc(QI(a), V[3]), msc(QI(b), W[3]))


def entry_mags(c):
    """|entry|^2 of M_c on the sixteen, by species pair."""
    B = pairing()
    sixteen = {s for s in range(DIM) if ntot(s) % 2 == 0}
    mags = {}
    for (r, col), z in mm(B, c).items():
        if r in sixteen and col in sixteen:
            get_or_set(mags, tuple(sorted((species(r), species(col)))), set()).add(norm2(z))
    return mags


# one rung vector (a, b): real ones (b = conj(a)) and complex ones (a, b independent, |a| != |b|)
ONE_REAL = [(QI(3, 5), QI(3, -5)), (QI(F(-2), F(7, 3)), QI(F(-2), F(-7, 3)))]
ONE_COMPLEX = [(QI(3), QI(1)), (QI(2, -1), QI(0, 4)), (QI(1, 2), QI(F(-1, 2), 1))]
# two couplings: ((a_1, b_1) for the down-type vector c_1, (a_2, b_2) for the up-type vector c_2)
TWO = [((QI(2, 1), QI(1)), (QI(0, 1), QI(3, 4))), ((QI(1, -1), QI(0, 2)), (QI(5), QI(1, 1)))]


def check_one_rung_vector_gives_equal_up_and_down_masses():
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for real, samples in ((True, ONE_REAL), (False, ONE_COMPLEX)):
        for a, b in samples:
            ok = ok and (b == a.conj()) == real
            c = rung(a, b)
            cstar = rung(b.conj(), a.conj())
            up, down = entry_mags(cstar), entry_mags(c)
            m = {norm2(b)}
            ok = ok and up[("Q", "uc")] == m and up[("L", "nuc")] == m
            ok = ok and down[("Q", "dc")] == m and down[("L", "ec")] == m
            # control: read through c itself, the up-type entry is |a|, which separates the complex samples
            ok = ok and (down[("Q", "uc")] == down[("Q", "dc")]) == real
    GA.check("one rung vector, real or complex: through c*, m_u = m_d = |b| at tree level", ok)
    return ok


def check_two_couplings_separate_up_and_down():
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    ratios = []
    for (a1, b1), (a2, b2) in TWO:
        down = entry_mags(rung(a1, b1))[("Q", "dc")]
        up = entry_mags(rung(b2.conj(), a2.conj()))[("Q", "uc")]
        ok = ok and down == {norm2(b1)} and up == {norm2(b2)} and up != down
        ratios.append(next(iter(up)) / next(iter(down)))
    ok = ok and ratios == [F(25), F(1, 2)]
    GA.check("two independent doublet couplings: m_u = |b_2| and m_d = |b_1|, unequal", ok)
    return ok
