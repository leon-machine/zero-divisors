"""synthesis.georgi-jarlskog-square-of-majorana-element: exact checks.

The five-mode module Lambda(W + R_2) as 32 x 32 rational matrices (Jordan-Wigner), modes 1,2,3 the pairs,
4,5 the rungs, v_i creating, w_i annihilating, as in the stored moment-map check. A matrix is expanded in
the 1024 Majorana monomials a_I b_J (a_i = v_i + w_i, b_i = v_i - w_i) by the trace form; the grade of a
monomial is |I| + |J|. T = v_1 ... v_5, T^dag its adjoint (transpose).
"""
import GA  # noqa: F401  (house rule; the computation is exact rational matrix algebra)
from tp_premise import premise
from fractions import Fraction as F
from itertools import combinations
import fock

NM = 5
STATES = [s for k in range(NM + 1) for s in combinations(range(NM), k)]
IDX = {s: sum(1 << x for x in s) for s in STATES}       # LSB bitmask index (fock order)
STATE_OF = {i: s for s, i in IDX.items()}
D = len(STATES)
mm, madd, msc, tr, comm = fock.mm, fock.madd, fock.msc, fock.transpose, fock.comm


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




A = [madd(V[i], W[i]) for i in range(NM)]
Bm = [madd(V[i], msc(F(-1), W[i])) for i in range(NM)]


def gen_act(kind, i, st):
    """a_i = v_i + w_i (kind 0) or b_i = v_i - w_i (kind 1) on a basis state: (sign, new state)."""
    sign = (-1) ** sum(1 for x in st if x < i)
    if i in st:
        return (sign if kind == 0 else -sign), tuple(x for x in st if x != i)
    return sign, tuple(sorted(st + (i,)))


def monomial_cols(I, J):
    """the signed permutation a_I b_J: for each basis state its image state and sign."""
    cols = {}
    for st in STATES:
        sg, cur = 1, st
        for j in reversed(J):
            e, cur = gen_act(1, j, cur)
            sg *= e
        for i in reversed(I):
            e, cur = gen_act(0, i, cur)
            sg *= e
        cols[st] = (cur, sg)
    return cols


def monomial(I, J):
    M = zero()
    for st, (img, sg) in monomial_cols(I, J).items():
        M[(IDX[img], IDX[st])] = F(sg)
    return M


MONOS = [(I, J) for k in range(NM + 1) for I in combinations(range(NM), k)
         for l in range(NM + 1) for J in combinations(range(NM), l)]
COLS = {m: monomial_cols(*m) for m in MONOS}


def expand(X):
    """coefficients of X on the Majorana monomials by the trace form: m is a signed permutation with
    m^-1 = m^T (a_i symmetric, b_i antisymmetric), so tr(m^-1 X) = sum_s sign_s X[m(s)][s]."""
    out = {}
    for (I, J) in MONOS:
        c = sum((sg * X.get((IDX[img], IDX[st]), 0) for st, (img, sg) in COLS[(I, J)].items()), F(0)) / D
        if c:
            out[(I, J)] = c
    return out


def assemble(coeffs):
    M = zero()
    for (I, J), c in coeffs.items():
        M = madd(M, msc(c, monomial(I, J)))
    return M


def check_gj_square_of_majorana_element():
    premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.majorana-element")
    premise("families.doublet-direction-module-georgi-jarlskog-clebsch")
    premise("synthesis.georgi-jarlskog-majorana-moment-map")
    w4 = W[3]
    TGJ = mm(mm(w4, BL), CHI)
    T = mm(mm(mm(mm(V[0], V[1]), V[2]), V[3]), V[4])
    TT = mm(T, tr(T))
    # T T^dag is the projector onto the full state, the product of the five occupation numbers
    full = (0, 1, 2, 3, 4)
    assert all(TT.get((i, j), 0) == (1 if i == j == IDX[full] else 0) for i in range(D) for j in range(D))
    for (I, J) in (((0,), ()), ((), (2,)), ((1, 3), (3, 4)), ((0, 1, 2, 3, 4), (0, 1, 2, 3, 4))):
        P = ONE
        for i in I:
            P = mm(P, madd(V[i], W[i]))
        for j in J:
            P = mm(P, madd(V[j], msc(F(-1), W[j])))
        assert P == monomial(I, J)
        g = len(I) + len(J)
        assert mm(tr(P), P) == ONE
        assert tr(P) == msc(F((-1) ** (g * (g - 1) // 2) * (-1) ** len(J)), P)   # m^T = m^-1 = (-1)^|J| rev(m)
    ex = expand(TT)
    assert assemble(ex) == TT
    # only products of whole mode bivectors a_k b_k occur
    assert all(I == J for (I, J) in ex)
    MUP = msc(F(1, 8), OMEGA)                      # the stored components of the moment map
    MUR = msc(F(1, 8), madd(S[3], S[4]))
    MU = madd(MUP, MUR)
    grade = {g: {k: c for k, c in ex.items() if len(k[0]) + len(k[1]) == g} for g in range(0, 11, 2)}
    G0, G2, G4 = (assemble(grade[g]) for g in (0, 2, 4))
    assert G0 == msc(F(1, 32), ONE)
    assert G2 == msc(F(1, 2), MU)                   # bivector part of T T^dag is mu / 2
    # (i) the pair-rung part of the grade-four component is 8 mu_R mu_P
    cross = {k: c for k, c in grade[4].items() if any(i < 3 for i in k[0]) and any(i >= 3 for i in k[0])}
    X4 = assemble(cross)
    assert X4 == msc(F(8), mm(MUR, MUP)) == msc(F(8), mm(MUP, MUR))
    # (ii) it is an SU(2)_L singlet and not an SU(2)_R singlet: the (15,1,3) of the 210
    for L in (mm(V[3], W[4]), mm(V[4], W[3]), madd(S[3], msc(F(-1), S[4]))):
        assert comm(X4, L) == zero()
    assert comm(X4, mm(V[3], V[4])) != zero()
    assert comm(X4, OMEGA) == zero() and X4 != zero()
    # (iii) the rung vector times it: (3/32)(T_GJ - w4 (B - L)); symmetric part 3/32 of the GJ form
    C = mm(w4, X4)
    assert C == madd(msc(F(3, 32), TGJ), msc(F(-3, 32), mm(w4, BL)))
    sC, aC = forms(C)
    sGJ, _ = forms(TGJ)
    _, a3 = forms(mm(w4, BL))
    assert is_multiple(sC, sGJ) == F(3, 32) and is_multiple(aC, a3) == F(-3, 32)
    # (iv) the unsplit grade-four component is the polynomial 4 mu^2 - 5/64 in the moment map
    assert G4 == madd(msc(F(4), mm(MU, MU)), msc(F(-5, 64), ONE))
    s4, _ = forms(mm(w4, G4))
    s10, a10 = forms(w4)
    assert s10 and not a10                          # the 10 form is nonzero and symmetric on the sixteen
    # G4 = 5/16, -1/16, 1/16 on total mode number 0, 2, 4 of the sixteen
    assert all(G4.get((IDX[s], IDX[s]), 0) == {0: F(5, 16), 2: F(-1, 16), 4: F(1, 16)}[len(s)] for s in SIXTEEN)
    # (iv) w4 G4 has no symmetric form: the 10 relation with multiple zero
    assert s4 == {} and is_multiple(s4, s10) == 0
    # (v) scaling with a vev c along T: the square's cross part goes as c^2, the moment-map composite as c^4
    c = F(3)
    Tc = msc(c, T)
    exc = expand(mm(Tc, tr(Tc)))
    crossc = assemble({k: v for k, v in exc.items() if len(k[0]) + len(k[1]) == 4
                       and any(i < 3 for i in k[0]) and any(i >= 3 for i in k[0])})
    assert crossc == msc(c * c, X4)
    assert msc(c ** 4, mm(MUR, MUP)) == mm(msc(c * c, MUR), msc(c * c, MUP))
    return True
