"""synthesis.hypothesis-u-readings-on-the-rung-coupling-line: exact checks (Fractions).

The one-generation module of Hypothesis (S): five fermionic modes (three colour modes 0, 1, 2 and two
rung-slot modes 3, 4), Fock basis of 32 occupation states, Jordan-Wigner creators v_i and annihilators
w_i, the sixteen = even states, and the mass form B(e_p, E e_q) pairing a state with its complement
(as in the store's equal-weight and Georgi-Jarlskog propositions).
"""
from fractions import Fraction as F
from tp_premise import premise
import GA
from pyutil import get_or_set
import fock

DIM = 32
NMODE = 5
mm, dag = fock.mm, fock.dag


def madd(A, B, cb=F(1)):
    return fock.madd(A, fock.msc(cb, B))


def msc(A, c):
    return fock.msc(c, A)


def occ(S, a):
    return (S >> a) & 1


def NW(S):
    return occ(S, 0) + occ(S, 1) + occ(S, 2)


def NR(S):
    return occ(S, 3) + occ(S, 4)


EVEN = fock.states(NMODE, 0)
NAMES = {(0, 0): 'nu^c', (0, 2): 'u^c', (1, 1): 'Q', (1, 3): 'L', (2, 0): 'e^c', (2, 2): 'd^c'}
CR = [fock.cre(a, NMODE) for a in range(NMODE)]
AN = [fock.ann(a, NMODE) for a in range(NMODE)]
V4, W4 = CR[3], AN[3]
CHI = fock.diag(lambda S: -(-1) ** NR(S), DIM)
BL = fock.diag(lambda S: 1 - F(2, 3) * NW(S), DIM)
TGJU = mm(mm(V4, BL), CHI)             # up-type twin of T_GJ, v_4 (B - L) chi
TGJ = mm(mm(W4, BL), CHI)              # T_GJ = w_4 (B - L) chi
_T = CR[0]
for _a in range(1, 5):
    _T = mm(_T, CR[_a])
PCOND = madd(mm(dag(_T), _T), mm(_T, dag(_T)))     # projector onto nu^c and its conjugate


def _eps(S):
    Sl = [a for a in range(5) if occ(S, a)]
    order = Sl + [a for a in range(5) if not occ(S, a)]
    inv = sum(1 for i in range(5) for j in range(i + 1, 5) if order[i] > order[j])
    return -1 if inv % 2 else 1


def form(E):
    Fm = {}
    for (r, c), v in E.items():
        if c in EVEN:
            p = (DIM - 1) ^ r
            if p in EVEN:
                k = bin(p).count("1")
                Fm[(p, c)] = v * ((-1) ** (k * (k - 1) // 2) * _eps(p))
    return {k: v for k, v in Fm.items() if v != 0}


def species(Fm):
    out = {}
    for (p, q), v in Fm.items():
        key = tuple(sorted((NAMES[(NR(p), NW(p))], NAMES[(NR(q), NW(q))])))
        get_or_set(out, key, set()).add(v)
    return out


def commutes_with_condensate(E):
    C = madd(mm(E, PCOND), mm(PCOND, E), F(-1))
    return all(k[1] not in EVEN for k in C)


GRID = [F(1), F(-2), F(3, 5), F(0), F(7, 4)]


def check_species_entries():
    """a v_4 + a' T^u_GJ has entries -(a - a') on (L, nu^c) and +-(a + a'/3) on (Q, u^c);
    b w_4 + b' T_GJ has entries (b - b') on (L, e^c) and +-(b + b'/3) on (Q, d^c); the up-type
    combination commutes with the condensate projector exactly when a' = a."""
    premise("standard-model.equal-weight-module")
    premise("families.doublet-direction-module-georgi-jarlskog-clebsch")
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.bidoublet-complex")
    for a in GRID:
        for a2 in GRID:
            if a == 0 and a2 == 0:
                continue
            up = species(form(madd(msc(V4, a), msc(TGJU, a2))))
            yn, yu = a - a2, a + a2 / 3
            if yn != 0:
                assert up[('L', 'nu^c')] == {-yn}
            else:
                assert ('L', 'nu^c') not in up
            if yu != 0:
                assert up[('Q', 'u^c')] == {yu, -yu}
            else:
                assert ('Q', 'u^c') not in up
            assert set(up) <= {('L', 'nu^c'), ('Q', 'u^c')}
            assert commutes_with_condensate(madd(msc(V4, a), msc(TGJU, a2))) == (a == a2)
            dn = species(form(madd(msc(W4, a), msc(TGJ, a2))))
            ye, yd = a - a2, a + a2 / 3
            if ye != 0:
                assert dn[('L', 'e^c')] == {ye}
            if yd != 0:
                assert dn[('Q', 'd^c')] == {yd, -yd}
            assert set(dn) <= {('L', 'e^c'), ('Q', 'd^c')}


def check_ratio_line_and_bottom_point():
    """With one family matrix F, M_nu = y_nu F and M_u = y_u F have singular values in the ratio
    kappa = |a - a'|/|a + a'/3| for every F.  kappa = 1 at a' = 0 (pure 10) and at a' = 3a only (real
    line), kappa = 0 exactly at a' = a; the bottom reading kappa = m_b/m_t at M_I needs a'/a in
    (0.9804, 0.9805) on the real same-sign branch."""
    premise("standard-model.equal-weight-module")
    premise("families.doublet-direction-module-georgi-jarlskog-clebsch")
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    # every F: the democratic rank-one F = J and a generic F; M_nu M_nu^T = kappa^2 M_u M_u^T
    J = [[F(1)] * 3 for _ in range(3)]
    G = [[F(2), F(-1), F(0)], [F(1, 3), F(4), F(1)], [F(0), F(5, 2), F(-3)]]
    for Fm in (J, G):
        for a, a2 in ((F(1), F(0)), (F(1), F(1, 2)), (F(2), F(-3))):
            yn, yu = -(a - a2), a + a2 / 3
            Mn = [[yn * x for x in r] for r in Fm]
            Mu = [[yu * x for x in r] for r in Fm]
            kap2 = (yn * yn) / (yu * yu)
            T = lambda A: [list(r) for r in zip(*A)]
            lhs = GA.mat_mul(Mn, T(Mn))
            rhs = [[kap2 * x for x in r] for r in GA.mat_mul(Mu, T(Mu))]
            assert lhs == rhs
    # the democratic F = J: the rank-one eigenvalue of M_s M_s^T is 9 y_s^2 (J J^T = 3 J)
    assert GA.mat_mul(J, J) == [[3 * x for x in r] for r in J]
    # kappa = 1 on the real line exactly at a' = 0 and a' = 3a: (a - a')^2 - (a + a'/3)^2 = a'(8a'/9 - 8a/3)
    for a in (F(1), F(-5, 2)):
        for a2 in (F(0), 3 * a, F(1, 7), a, -a):
            diff = (a - a2) ** 2 - (a + a2 / 3) ** 2
            assert diff == a2 * (F(8, 9) * a2 - F(8, 3) * a)
            assert (diff == 0) == (a2 == 0 or a2 == 3 * a)
    # bottom point: kappa = m_b/m_t with the T12 fit targets at M_I (m_b = 1.3651, m_t = 92.45 GeV)
    mb, mt = F(13651, 10000), F(9245, 100)
    kap = mb / mt
    assert F(1476, 100000) < kap < F(1477, 100000)
    ratio = (1 - kap) / (1 + kap / 3)               # a'/a on the same-sign real branch
    assert F(9804, 10000) < ratio < F(9805, 10000)
    # and it is a solution: (1 - r)/(1 + r/3) = kappa
    assert (1 - ratio) / (1 + ratio / 3) == kap
    # the top reading needs kappa = 1 and the (EW) point gives 0; the bottom point is neither
    assert ratio != 0 and ratio != 1 and ratio != 3


EXPORTS = {}
