"""synthesis.georgi-jarlskog-majorana-moment-map: exact checks.

The five-mode module Lambda(W + R_2) is built as 32 x 32 integer matrices (Jordan-Wigner):
modes 1,2,3 are the pair modes, 4,5 the rung modes; v_i creates, w_i annihilates,
v_i w_i + w_i v_i = 1. The pairing B is that of Lemma standard-model.invariant-pairing-five-modes,
B(psi, phi) = sum_S (-1)^{|S|(|S|-1)/2} eps(S, S^c) psi_S phi_{S^c}. Species (under (S)) by
(N_W, N_R): e^c (0,2), Q (1,1), u^c (2,0), d^c (2,2), L (3,1), nu^c (0,0).
The moment map of T is the orthogonal projection, for the trace form, of [T, T^dag] onto the
span of the 45 bivectors of the ten Majoranas a_i = v_i + w_i, b_i = v_i - w_i.
"""
import GA  # noqa: F401  (house rule; the computation is exact integer/rational matrix algebra)
from tp_premise import premise
from fractions import Fraction as F
from itertools import combinations
import fock

NM = 5
STATES = [s for k in range(NM + 1) for s in combinations(range(NM), k)]
IDX = {s: sum(1 << x for x in s) for s in STATES}       # LSB bitmask index (fock order)
STATE_OF = {i: s for s, i in IDX.items()}
D = len(STATES)
mm, madd, msc, tr, trace = fock.mm, fock.madd, fock.msc, fock.transpose, fock.trace


def zero():
    return {}


def nw(s):
    return sum(1 for x in s if x < 3)


def nr(s):
    return sum(1 for x in s if x >= 3)


def species(s):
    return {(0, 2): "ec", (1, 1): "Q", (2, 0): "uc", (2, 2): "dc", (3, 1): "L", (0, 0): "nuc"}.get((nw(s), nr(s)))


def diag(fn):
    return fock.diag(lambda i: fn(STATE_OF[i]), D)


V = [fock.cre(m, NM) for m in range(NM)]
W = [tr(v) for v in V]
ONE = fock.eye(D)
S = [madd(mm(V[i], W[i]), msc(F(-1, 2), ONE)) for i in range(NM)]     # v_i ^ w_i = n_i - 1/2
BL = diag(lambda s: 1 - F(2, 3) * nw(s))                             # B - L = 1 - (2/3) N_W
T3R = diag(lambda s: F(nr(s) - 1, 2))
CHI = diag(lambda s: -(-1) ** nr(s))
OMEGA = madd(S[0], S[1], S[2])

BMAT = zero()
for s in STATES:
    comp = tuple(x for x in range(NM) if x not in s)
    seq = list(s) + list(comp)
    inv = sum(1 for i in range(NM) for j in range(i + 1, NM) if seq[i] > seq[j])
    k = len(s)
    BMAT[(IDX[s], IDX[comp])] = F((-1) ** (k * (k - 1) // 2) * (-1) ** inv)

SIXTEEN = [s for s in STATES if len(s) % 2 == 0]


def forms(X):
    """symmetric and antisymmetric parts of B(psi, X phi) on the sixteen, as dicts keyed by
    ordered state pairs (nonzero entries only)."""
    BX = mm(BMAT, X)
    sym, anti = {}, {}
    for a in SIXTEEN:
        for b in SIXTEEN:
            x, y = BX.get((IDX[a], IDX[b]), 0), BX.get((IDX[b], IDX[a]), 0)
            if x + y:
                sym[(a, b)] = (x + y) / 2
            if x - y:
                anti[(a, b)] = (x - y) / 2
    return sym, anti


def is_multiple(f, g):
    """f = c g for one scalar c (as dicts); returns c or None."""
    keys = set(f) | set(g)
    c = None
    for k in keys:
        a, b = f.get(k, F(0)), g.get(k, F(0))
        if b == 0:
            if a != 0:
                return None
            continue
        if c is None:
            c = a / b
        elif a != c * b:
            return None
    return c if c is not None else F(0)


def bivector_projection(M):
    a = [madd(V[i], W[i]) for i in range(NM)]
    b = [madd(V[i], msc(F(-1), W[i])) for i in range(NM)]
    gens = a + b
    sq = [F(1)] * NM + [F(-1)] * NM
    owner = list(range(NM)) + list(range(NM))
    full, pair, rung = zero(), zero(), zero()
    for x in range(2 * NM):
        for y in range(x + 1, 2 * NM):
            E = mm(gens[x], gens[y])
            Einv = msc(-sq[x] * sq[y], E)
            assert mm(E, Einv) == ONE
            c = trace(mm(Einv, M)) / D
            if not c:
                continue
            full = madd(full, msc(c, E))
            if owner[x] < 3 and owner[y] < 3:
                pair = madd(pair, msc(c, E))
            elif owner[x] >= 3 and owner[y] >= 3:
                rung = madd(rung, msc(c, E))
            else:
                raise AssertionError("mixed pair-rung component in the moment map")
    return full, pair, rung


def check_moment_map_georgi_jarlskog():
    premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.majorana-element")
    premise("families.doublet-direction-module-georgi-jarlskog-clebsch")
    premise("standard-model.grade-three-georgi-jarlskog-direction")
    premise("standard-model.under-s-composites-state-space-spinor")
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    # the pairing: so(10)-invariant (sample bivectors) and pairs a state with its complement only
    for X in (mm(V[0], W[1]), mm(V[0], V[3]), mm(W[2], W[4]), S[3]):
        assert madd(mm(tr(X), BMAT), mm(BMAT, X)) == zero()
    w4 = W[3]
    TGJ = mm(mm(w4, BL), CHI)
    # controls against the store's statements on this module
    s10, a10 = forms(w4)
    assert not a10 and s10
    ec_L = [(a, b) for (a, b) in s10 if species(a) == "L" and species(b) == "ec"]
    Q_dc = [(a, b) for (a, b) in s10 if species(a) == "Q" and species(b) == "dc"]
    assert ec_L and Q_dc and all(abs(s10[k]) == 1 for k in ec_L + Q_dc)
    sGJ, aGJ = forms(TGJ)
    assert not aGJ
    assert all(abs(sGJ[k]) == 1 for k in ec_L) and all(abs(sGJ[k]) == F(1, 3) for k in Q_dc)
    assert set(sGJ) == set(ec_L + Q_dc + [(b, a) for (a, b) in ec_L + Q_dc])
    s3, a3 = forms(mm(w4, BL))
    assert not s3 and a3                                  # grade three: antisymmetric
    assert TGJ == msc(F(4, 3), mm(mm(w4, S[4]), OMEGA))   # T_GJ = (4/3) w4 (v5^w5)(sum v^w)
    # (i) the moment map of T and its Pati-Salam components
    T = mm(mm(mm(mm(V[0], V[1]), V[2]), V[3]), V[4])
    MU, MUP, MUR = bivector_projection(madd(mm(T, tr(T)), msc(F(-1), mm(tr(T), T))))
    assert MU == msc(F(1, 8), madd(*S))
    assert MUP == msc(F(1, 8), OMEGA) == msc(F(-3, 16), BL)
    assert MUR == msc(F(1, 8), madd(S[3], S[4])) == msc(F(1, 4), T3R)
    X13 = madd(msc(F(2), T3R), msc(F(-3, 2), BL))         # thirteenth generator 2 T3R - (3/2)(B - L)
    assert MU == msc(F(1, 8), X13)
    assert madd(mm(MU, T), msc(F(-1), mm(T, MU))) == msc(F(5, 8), T)   # T is an eigenvector of ad mu
    # (ii) any polynomial in the unsplit moment map gives only the 10 relation
    P = ONE
    for k in range(6):
        sk, _ = forms(mm(w4, P))
        if sk:
            assert is_multiple(sk, s10) is not None
        P = mm(P, MU)
    # (iii) the rung vector times the pair component: the grade-three direction
    assert mm(w4, MUP) == msc(F(-3, 16), mm(w4, BL))
    # (iv) the rung vector times both components: GJ 126 plus the grade-three direction
    C = mm(mm(w4, MUR), MUP)
    assert C == msc(F(3, 256), mm(mm(w4, BL), madd(CHI, msc(F(-1), ONE))))
    assert C == madd(msc(F(3, 256), TGJ), msc(F(-3, 256), mm(w4, BL)))
    # the same identity among generators: w4 T3R (B - L) = -(1/4)(T_GJ - w4 (B - L))
    assert mm(mm(w4, T3R), BL) == msc(F(-1, 4), madd(TGJ, msc(F(-1), mm(w4, BL))))
    sC, aC = forms(C)
    assert is_multiple(sC, sGJ) == F(3, 256)
    assert is_multiple(aC, a3) == F(-3, 256)
    assert all(abs(sC[k]) == abs(aC[k]) for k in sC)       # equal moduli entry by entry
    # one-sided: C annihilates every state with N_R odd (the doublet sector)
    for s in STATES:
        if nr(s) % 2 == 1:
            assert all(C.get((i, IDX[s]), 0) == 0 for i in range(D))
    return True
