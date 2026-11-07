"""synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins: exact checks.

Generators: g_1, g_2 (squares -1, -1; J = g_1 g_2), then one plane (e, f) (squares +1, -1) per mode
(k, alpha), k in the window I = {-2, -1, 0, 1} (generator momentum), alpha in the channels {+, -}.
Ladder: a* = v = (e + f)/2, a = w = (e - f)/2, n = v w; the adjoint * is the antiautomorphism fixing
generators of square +1 and negating those of square -1 (so v* = w, J* = -J). Channel matrices M have
entries in span{1, J} (J commutes with every mode); M* is the conjugate transpose (J -> -J).
rho_q(M) = sum_{k, k+q in I} sum_{alpha, beta} M_{alpha beta} a*_{k, alpha} a_{k+q, beta}.

(i)   window identity [rho_q(M), rho_q(M')*] = sum_{k, k+q in I} a*_k (M M'*) a_k
      - sum_{k, k-q in I} a*_k (M'* M) a_k, q = 1, 2, six matrices;
(ii)  on the edge-clean projector E (lowest q momenta filled, highest q empty, every channel)
      [rho_q(M), rho_q(M)*] E = (q tr(M* M) + rho_0([M, M*])) E; scalar on E for normal M, not for E_{+-};
(iii) helicity: weights W = diag(1/2, -1/2) (and a four-channel case); helicity +-1 matrices are
      nilpotent and not normal; the linear pair M_1 = E_{+-} + E_{-+}, M_2 = J(E_{+-} - E_{-+}) rotates
      as a vector and [M_1, M_2*] != 0; the mode rotation at the rational half angle (12/13, 5/13)
      multiplies rho(E_{+-}) by e^{theta J} and fixes rho(E_{++});
(iv)  on the chiral sea Omega (k < 0 filled), B = rho_q(E_{+-})* has |B^p Omega|^2 = (p!)^2 C(q, p),
      B^{q+1} Omega = 0 (q = 1, 2), [rho_q(E_{+-}), B] B^p Omega = (q - 2p) B^p Omega; the Cartan mode
      at q = 1 has |D^2 Omega|^2 = 2; a rank-one nilpotent rational M gives B^2 Omega = 0 at q = 1;
(v)   the sea annihilates every rho_q(M) and omega([rho_q(M), rho_q(M)*]) = q tr(M M*) >= 0; for the
      reversed sea the value is -q tr(M M*) and rho_q(M)* annihilates.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

WINDOW = [-2, -1, 0, 1]
CHANNELS = ['+', '-']
WEIGHT = {'+': F(1, 2), '-': F(-1, 2)}
MODES = [(k, c) for k in WINDOW for c in CHANNELS]
SQ = tuple([-1, -1] + [1, -1] * len(MODES))
POS = {md: 2 + 2 * i for i, md in enumerate(MODES)}
ONE = GA.sc(1)
J = GA.mul(GA.gen(0), GA.gen(1), SQ)
HALF_ANGLE = (F(12, 13), F(5, 13))


def factorial(n):
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out


def comb(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def m(*xs):
    out = ONE
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def comm(a, b):
    return GA.sub(m(a, b), m(b, a))


def star(x):
    out = {}
    for b, c in x.items():
        k = len(b)
        s = (-1) ** (k * (k - 1) // 2) * (-1) ** sum(1 for i in b if SQ[i] == -1)
        if c * s != 0:
            out[b] = c * s
    return out


def cr(md):
    i = POS[md]
    return GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(i + 1)))


def an(md):
    i = POS[md]
    return GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(i + 1)))


def num(md):
    return m(cr(md), an(md))


def cnum(re, im=0):
    """The number re + im J."""
    return GA.add(GA.sc(F(re)), GA.scal(F(im), J))


def mat(entries):
    """Channel matrix from {(alpha, beta): (re, im)}."""
    return {k: cnum(*v) for k, v in entries.items() if v != (0, 0)}


def mstar(M):
    return {(b, a): star(c) for (a, b), c in M.items()}


def mmul(A, B):
    out = {}
    for (a, b), x in A.items():
        for (c, d), y in B.items():
            if b == c:
                out[(a, d)] = GA.add(out.get((a, d), {}), m(x, y))
    return {k: v for k, v in out.items() if not GA.is_zero(v)}


def msub(A, B):
    out = dict(A)
    for k, v in B.items():
        out[k] = GA.sub(out.get(k, {}), v)
    return {k: v for k, v in out.items() if not GA.is_zero(v)}


def mtrace(A):
    return GA.add(*[A.get((c, c), {}) for c in CHANNELS])


def rho(q, M):
    out = {}
    for k in WINDOW:
        if k + q in WINDOW:
            for (a, b), c in M.items():
                out = GA.add(out, m(c, cr((k, a)), an((k + q, b))))
    return out


def site_sum(ks, M):
    """sum_{k in ks} a*_k M a_k."""
    out = {}
    for k in ks:
        for (a, b), c in M.items():
            out = GA.add(out, m(c, cr((k, a)), an((k, b))))
    return out


def projector(filled, modes=None):
    """Product of n (filled) or 1 - n (empty) over the given modes (all modes by default)."""
    out = ONE
    for md in (MODES if modes is None else modes):
        out = m(out, num(md) if md in filled else GA.sub(ONE, num(md)))
    return out


def scalar_of_product(x, y):
    """<x y>_0, using only the blade pairs whose product is a scalar (equal blades)."""
    out = F(0)
    for b, c in x.items():
        if b in y:
            s, bb = GA.blade_mul(b, b, SQ)
            assert bb == ()
            out += c * y[b] * s
    return out


def omega(P, X, size=None):
    """Expectation in the state of the projector P over `size` modes: 2^size <P X>_0."""
    return scalar_of_product(P, X) * 2 ** (len(MODES) if size is None else size)


def norm2(X, size=None):
    """Squared norm of the vector X = Y P (P the projector over `size` modes): 2^size <X* X>_0."""
    return scalar_of_product(star(X), X) * 2 ** (len(MODES) if size is None else size)


E = lambda a, b: {(a, b): (1, 0)}
SAMPLES = [
    mat(E('+', '+')),                                         # Cartan, helicity 0
    mat(E('+', '-')),                                         # helicity +1
    mat({('-', '+'): (0, 1)}),                                # J E_{-+}, helicity -1
    mat({('+', '+'): (F(12, 25), 0), ('+', '-'): (F(-9, 25), 0),
         ('-', '+'): (F(16, 25), 0), ('-', '-'): (F(-12, 25), 0)}),   # t u^T, t = (3/5, 4/5), u = (4/5, -3/5)
    mat({('+', '-'): (1, 0), ('-', '+'): (1, 0)}),            # M_1, linear
    mat({('+', '-'): (0, 1), ('-', '+'): (0, -1)}),           # M_2 = J(E_{+-} - E_{-+})
]
SEA = [md for md in MODES if md[0] < 0]
REVERSED = [md for md in MODES if md[0] >= 0]


def check_window_commutator_identity():
    """(i) [rho_q(M), rho_q(M')*] = sum_{k,k+q in I} a*_k M M'* a_k - sum_{k,k-q in I} a*_k M'* M a_k."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("std-algebra.orthogonal-anticommute")
    premise("hawking.current-commutator-exactly-edge-split")
    for md in MODES:   # CAR and J commuting with the modes
        assert GA.eq(GA.add(m(an(md), cr(md)), m(cr(md), an(md))), ONE)
        assert GA.eq(star(cr(md)), an(md)) and GA.commutes(J, cr(md), SQ)
    assert GA.eq(m(J, J), GA.sc(-1)) and GA.eq(star(J), GA.neg(J))
    # pairs (i, j) with tr(M_j* M_i) = re + im J: on the sea the commutator has the value q tr(M_j* M_i)
    expected = {(0, 0): (1, 0), (1, 1): (1, 0), (2, 2): (1, 0), (3, 3): (1, 0), (4, 4): (2, 0), (5, 5): (2, 0),
                (4, 5): (0, 0), (1, 3): (F(-9, 25), 0), (0, 2): (0, 0), (5, 1): (0, 1)}
    Om = projector(SEA)
    for q in (1, 2):
        lo = [k for k in WINDOW if k + q in WINDOW]
        hi = [k for k in WINDOW if k - q in WINDOW]
        for (i, j), (re, im) in expected.items():
            M, Mp = SAMPLES[i], SAMPLES[j]
            lhs = comm(rho(q, M), star(rho(q, Mp)))
            rhs = GA.sub(site_sum(lo, mmul(M, mstar(Mp))), site_sum(hi, mmul(mstar(Mp), M)))
            assert GA.eq(lhs, rhs), (q, i, j)
            got = (omega(Om, lhs), omega(Om, m(GA.neg(J), lhs)))
            assert got == (q * re, q * im), (q, i, j, got)
    return True


def check_edge_clean_value_and_normality():
    """(ii) on the edge-clean projector the commutator is q tr(M*M) + rho_0([M, M*]); scalar iff M normal."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("hawking.current-commutator-exactly-edge-split")
    q = 1
    Eproj = ONE
    for c in CHANNELS:
        Eproj = m(Eproj, num((WINDOW[1], c)), GA.sub(ONE, num((WINDOW[-1], c))))
    bulk = WINDOW[1:-1]
    for i, M in enumerate(SAMPLES):
        Ms = mstar(M)
        C = comm(rho(q, M), star(rho(q, M)))
        central = GA.scal(F(q), mtrace(mmul(Ms, M)))
        defect = msub(mmul(M, Ms), mmul(Ms, M))
        assert GA.eq(m(C, Eproj), m(GA.add(central, site_sum(WINDOW, defect)), Eproj)), i
        normal = not defect
        assert normal == (i in (0, 4, 5)), i
        if normal:
            assert GA.eq(m(C, Eproj), m(central, Eproj)), i
    # the helicity-one mode: two edge-clean bulk states give different values (q + 1 and q - 1)
    C = comm(rho(q, SAMPLES[1]), star(rho(q, SAMPLES[1])))
    edge = [(WINDOW[0], c) for c in CHANNELS]
    vals = [omega(projector(edge + [(bulk[0], c)]), C) for c in CHANNELS]
    assert vals == [q + 1, q - 1], vals
    return True


def check_helicity_one_is_nilpotent_and_not_normal():
    """(iii) [W, M] = h M with h = +-1 forces M nilpotent and (M != 0) not normal; the linear doublet."""
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    premise("std-algebra.orthogonal-anticommute")
    W = mat({('+', '+'): (WEIGHT['+'], 0), ('-', '-'): (WEIGHT['-'], 0)})

    def wcomm(M):
        return msub(mmul(W, M), mmul(M, W))

    def scalem(c, M):
        return {k: m(c, v) for k, v in M.items()}
    hp, hm = SAMPLES[1], SAMPLES[2]
    assert not msub(wcomm(hp), hp) and not msub(wcomm(hm), scalem(GA.sc(-1), hm))
    for M in (hp, hm):
        assert not mmul(M, M)                                       # nilpotent
        assert msub(mmul(M, mstar(M)), mmul(mstar(M), M))           # not normal
    M1, M2 = SAMPLES[4], SAMPLES[5]
    assert not msub(scalem(J, wcomm(M1)), M2)                       # J[W, M1] = M2
    assert not msub(scalem(J, wcomm(M2)), scalem(GA.sc(-1), M1))    # J[W, M2] = -M1
    assert msub(mmul(M1, mstar(M2)), mmul(mstar(M2), M1))           # [M1, M2*] != 0
    Mplus = msub(M1, scalem(J, M2))                                 # M1 - J M2 = 2 E_{+-}
    assert not msub(Mplus, scalem(GA.sc(2), hp))
    # four channels, weights (1/2, 1/2, -1/2, -1/2): integer matrices projected to helicity +1
    w4 = [F(1, 2), F(1, 2), F(-1, 2), F(-1, 2)]
    for seed in range(1, 6):
        A = [[F((7 * seed + 3 * i + 5 * j) % 11 - 5) for j in range(4)] for i in range(4)]
        H = [[A[i][j] if w4[i] - w4[j] == 1 else F(0) for j in range(4)] for i in range(4)]
        HH = GA.mat_mul(H, H)
        HT = [[H[j][i] for j in range(4)] for i in range(4)]
        assert all(x == 0 for row in HH for x in row)
        assert any(H[i][j] != 0 for i in range(4) for j in range(4))
        assert not GA.mat_eq(GA.mat_mul(H, HT), GA.mat_mul(HT, H))
    # the rotation at the rational half angle: a_alpha -> e^{-theta w_alpha J} a_alpha
    c, s = HALF_ANGLE

    def phase(w):   # e^{-theta w J} for w = +-1/2
        return cnum(c, -s if w > 0 else s)
    rot_cr = {md: m(star(phase(WEIGHT[md[1]])), cr(md)) for md in MODES}
    rot_an = {md: m(phase(WEIGHT[md[1]]), an(md)) for md in MODES}
    for md in MODES:
        assert GA.eq(GA.add(m(rot_an[md], rot_cr[md]), m(rot_cr[md], rot_an[md])), ONE)

    def rot_rho(q, M):
        out = {}
        for k in WINDOW:
            if k + q in WINDOW:
                for (a, b), x in M.items():
                    out = GA.add(out, m(x, rot_cr[(k, a)], rot_an[(k + q, b)]))
        return out
    cos_t, sin_t = c * c - s * s, 2 * c * s
    assert (cos_t, sin_t) == (F(119, 169), F(120, 169))
    q = 1
    assert GA.eq(rot_rho(q, hp), m(cnum(cos_t, sin_t), rho(q, hp)))
    assert GA.eq(rot_rho(q, SAMPLES[0]), rho(q, SAMPLES[0]))
    assert GA.eq(rot_rho(q, M1), GA.add(GA.scal(cos_t, rho(q, M1)), GA.scal(sin_t, rho(q, M2))))
    return True


def check_helicity_one_mode_is_a_quasi_spin():
    """(iv) on the chiral sea the helicity-one mode at momentum q holds at most q quanta."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("field-theory.how-close-tower-comes-ccr")
    # the modes a helicity-one mode at momentum q touches; the others are spectators (factor 1)
    for q in (1, 2):
        S = sorted({(k, '+') for k in WINDOW if k + q in WINDOW} | {(k + q, '-') for k in WINDOW if k + q in WINDOW})
        Om = projector(SEA, S)
        A = rho(q, SAMPLES[1])
        B = star(A)
        C = comm(A, B)
        X = Om
        for p in range(0, q + 2):
            if p > 0:
                X = m(B, X)
            want = factorial(p) ** 2 * comb(q, p)
            assert norm2(X, len(S)) == want, (q, p, norm2(X, len(S)), want)
            assert GA.eq(m(C, X), GA.scal(F(q - 2 * p), X)), (q, p)
        assert GA.is_zero(X) and q + 1 == p
    Sc = [(k, '+') for k in WINDOW]
    Omc = projector(SEA, Sc)
    D = star(rho(1, SAMPLES[0]))
    assert norm2(m(D, Omc), len(Sc)) == 1 and norm2(m(D, D, Omc), len(Sc)) == 2
    Om = projector(SEA)
    Br = star(rho(1, SAMPLES[3]))
    assert norm2(m(Br, Om)) == 1 and GA.is_zero(m(Br, Br, Om))
    return True


def check_sea_annihilates_and_forms_are_nonnegative():
    """(v) rho_q(M) Omega = 0 and omega([rho, rho*]) = q tr(M M*) >= 0; reversed sea gives the opposite."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("hawking.current-commutator-exactly-edge-split")
    Om, Rv = projector(SEA), projector(REVERSED)
    for q in (1, 2):
        for M in SAMPLES:
            A = rho(q, M)
            t = mtrace(mmul(M, mstar(M))).get((), F(0))
            assert t > 0
            assert GA.is_zero(m(A, Om)) and GA.is_zero(m(star(A), Rv))
            assert omega(Om, comm(A, star(A))) == q * t
            assert omega(Om, m(A, star(A))) == q * t
            assert omega(Rv, comm(A, star(A))) == -q * t
    return True
