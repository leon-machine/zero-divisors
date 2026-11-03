"""The twistor form is the grading of Z = e0 nu, and the attachment's conformal energy is Z's generator: exact checks.

Representation: Cl(2,4) (squares e0:+1, e1,e2,e3:-1, nu:+1, e_-:-1) on the module of three ladder pairs,
C^8, by Jordan-Wigner matrices with Gaussian rational entries; CS and CS^- are the two chirality halves.
(1) Clifford relations, chirality commutes with every bivector.
(2) The Hermitian forms on CS invariant under the fifteen bivectors form a real line, spanned by the
    restriction of i Z; its signature is (2,2) and Z = -i on its positive plane, +i on its negative plane.
(3) h Z = -i on CS: in the twistor form the Z-quadratic is the positive Hilbert form.
(4) For every tested future translation P_a = (1/2) a n_inf (a future timelike or null), i h P_a is positive
    semidefinite with the sign of i h Z; for past a the opposite sign; for spacelike a indefinite. The de
    Sitter horizon's null rotation (1/2) n I and the null special conformal n n0 share Z's sign; boosts and
    the dilation are indefinite.
(5) Oscillator model on polynomials (Bargmann form: a+ = z, a = d/dz exact): Q(M) = sum Zhat_a^+ (h M)_ab Zhat^b
    with the h-positive twistor components annihilating. Q is a Lie homomorphism on tested pairs;
    Q(Z/2) = -i E with E = (N_a + N_b)/2 + 1; the Weyl-ordered centre is i s with s = (N_a - N_b)/2;
    on helicity s the energies are |s| + 1 + n with multiplicity (n + 1)(n + 2|s| + 1), all >= 1.
Exact arithmetic only.
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from GA import QI
from tp_premise import premise

Z0, ONE, I = QI(0), QI(1), QI(0, 1)


def _mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), QI(0)) for j in range(len(B[0]))] for i in range(len(A))]


def _kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def _dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def _sc(c, A):
    return [[c * x for x in r] for r in A]


def _add(A, B):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]


def _eq(A, B):
    return all(a == b for r, s in zip(A, B) for a, b in zip(r, s))


def _id(n):
    return [[ONE if i == j else Z0 for j in range(n)] for i in range(n)]


def _zero(n):
    return [[Z0] * n for _ in range(n)]


def _det(M):
    if len(M) == 1:
        return M[0][0]
    return sum(((QI(-1) if j % 2 else QI(1)) * M[0][j] * _det([r[:j] + r[j + 1:] for r in M[1:]])
                for j in range(len(M))), QI(0))


SX = [[Z0, ONE], [ONE, Z0]]
SY = [[Z0, QI(0, -1)], [I, Z0]]
SZ = [[ONE, Z0], [Z0, QI(-1)]]
S1 = _id(2)


def _k3(a, b, c):
    return _kron(_kron(a, b), c)


_g = [_k3(SX, S1, S1), _k3(SY, S1, S1), _k3(SZ, SX, S1), _k3(SZ, SY, S1), _k3(SZ, SZ, SX), _k3(SZ, SZ, SY)]
SQ = [1, -1, -1, -1, 1, -1]                                   # e0, e1, e2, e3, nu, e_-
G = [_g[0], _sc(I, _g[2]), _sc(I, _g[3]), _sc(I, _g[4]), _g[1], _sc(I, _g[5])]
CHIR = _k3(SZ, SZ, SZ)
ZM = _mm(G[0], G[4])                                          # Z = e0 nu
EVEN = [i for i in range(8) if CHIR[i][i] == ONE]
ODD = [i for i in range(8) if CHIR[i][i] == QI(-1)]
BIV = [(a, b) for a in range(6) for b in range(a + 1, 6)]


def _res(M, idx):
    return [[M[i][j] for j in idx] for i in idx]


def _vec(c):
    out = _zero(8)
    for ci, gi in zip(c, G[:4]):
        out = _add(out, _sc(QI(F(ci)), gi))
    return out


NINF = _add(G[4], G[5])
NO = _sc(QI(F(1, 2)), _add(G[4], _sc(QI(-1), G[5])))
H = _res(_sc(I, ZM), EVEN)                                    # the twistor form on CS


def _hM(M):
    return _mm(H, _res(M, EVEN))


def _psd_sign(Hm):
    """'+' if Hermitian PSD, '-' if NSD, 'indef' otherwise (all principal minors, exact)."""
    subs = [c for r in range(1, len(Hm) + 1) for c in combinations(range(len(Hm)), r)]
    mins = [_det([[Hm[i][j] for j in c] for i in c]) for c in subs]
    if any(m.im != 0 for m in mins):
        return "nonreal"
    if all(m.re >= 0 for m in mins):
        return "+"
    if all((m.re if len(c) % 2 == 0 else -m.re) >= 0 for m, c in zip(mins, subs)):
        return "-"
    return "indef"


def check_clifford_module_and_chirality():
    premise("correspondence.twistors-are-states-three-ladder-pairs")
    for a in range(6):
        for b in range(6):
            want = _sc(QI(2 * SQ[a]), _id(8)) if a == b else _zero(8)
            GA.check("Clifford relation", _eq(_add(_mm(G[a], G[b]), _mm(G[b], G[a])), want))
    vol = _id(8)
    for gi in G:
        vol = _mm(vol, gi)
    GA.check("the volume element e0 e1 e2 e3 nu e_- = i chir", _eq(vol, _sc(QI(0, 1), CHIR)))
    for (a, b) in BIV:
        S = _mm(G[a], G[b])
        GA.check("bivectors preserve the chirality halves", _eq(_mm(S, CHIR), _mm(CHIR, S)))
    GA.check("CS and CS^- are four-dimensional", len(EVEN) == 4 and len(ODD) == 4)
    GA.check("Z^2 = -1", _eq(_mm(ZM, ZM), _sc(QI(-1), _id(8))))
    return True


def _solve_kernel(rows, n):
    """Kernel dimension of a linear system over the Gaussian rationals (rows of length n)."""
    R = [r[:] for r in rows]
    rank, col = 0, 0
    while rank < len(R) and col < n:
        piv = next((i for i in range(rank, len(R)) if R[i][col] != Z0), None)
        if piv is None:
            col += 1
            continue
        R[rank], R[piv] = R[piv], R[rank]
        p = R[rank][col]
        R[rank] = [x / p for x in R[rank]]
        for i in range(len(R)):
            if i != rank and R[i][col] != Z0:
                f = R[i][col]
                R[i] = [x - f * y for x, y in zip(R[i], R[rank])]
        rank += 1
        col += 1
    return n - rank


def check_invariant_form_is_the_grading_of_z():
    premise("field-theory.twistor-attachment")
    premise("synthesis.positive-energy-selects-rule-2-sign")
    for idx in (EVEN, ODD):
        Hx = _res(_sc(I, ZM), idx)
        GA.check("i Z is Hermitian", _eq(_dag(Hx), Hx))
        for (a, b) in BIV:
            S = _res(_mm(G[a], G[b]), idx)
            GA.check("S^+ h + h S = 0", _eq(_add(_mm(_dag(S), Hx), _mm(Hx, S)), _zero(4)))
        # all X with S^+ X + X S = 0 for every bivector: unknowns X_ij (16 complex), equations entrywise
        rows = []
        for (a, b) in BIV:
            S = _res(_mm(G[a], G[b]), idx)
            Sd = _dag(S)
            for i in range(4):
                for j in range(4):
                    row = [Z0] * 16
                    for k in range(4):
                        row[k * 4 + j] = row[k * 4 + j] + Sd[i][k]     # (S^+ X)_ij
                        row[i * 4 + k] = row[i * 4 + k] + S[k][j]      # (X S)_ij
                    rows.append(row)
        GA.check("the invariant sesquilinear forms are one complex line", _solve_kernel(rows, 16) == 1)
        diag = [Hx[i][i] for i in range(4)]
        GA.check("i Z diagonal of signature (2,2)", sorted(d.re for d in diag) == [-1, -1, 1, 1]
                 and all(Hx[i][j] == Z0 for i in range(4) for j in range(4) if i != j))
        Zr = _res(ZM, idx)
        for i in range(4):
            GA.check("Z = -i on the h-positive plane, +i on the h-negative plane",
                     Zr[i][i] == (QI(0, -1) if diag[i] == ONE else QI(0, 1)))
    GA.check("h Z = -i on CS: the Z-quadratic is the Hilbert form", _eq(_hM(ZM), _sc(QI(0, -1), _id(4))))
    GA.check("tabulated: h on CS", [H[i][i] for i in range(4)] == [QI(-1), QI(-1), QI(1), QI(1)])
    return True


def check_future_translations_share_the_sign_of_z():
    premise("synthesis.positive-conformal-energy-gives-positive-null-translations")
    premise("synthesis.de-sitter-horizon-translation-is-conformal-null-rotation")
    zsign = _psd_sign(_sc(I, _hM(ZM)))
    GA.check("i h Z is positive definite", zsign == "+")
    future = [(1, 0, 0, 0), (1, 1, 0, 0), (1, -1, 0, 0), (1, 0, F(3, 5), F(4, 5)), (2, 1, 0, 0),
              (1, 0, 0, 1), (5, 3, 0, F(4))]
    for c in future:
        P = _sc(QI(F(1, 2)), _mm(_vec(c), NINF))
        GA.check("future a: i h P_a PSD with Z's sign", _psd_sign(_sc(I, _hM(P))) == zsign)
        nP = _sc(QI(F(1, 2)), _mm(_vec([-x for x in c]), NINF))
        GA.check("past -a: the opposite sign", _psd_sign(_sc(I, _hM(nP))) == "-")
        # null special conformal n n0 and, for null a, the de Sitter null rotation P_n + (L/12) n n0
        K = _mm(_vec(c), NO)
        GA.check("special conformal a n0 shares Z's sign", _psd_sign(_sc(I, _hM(K))) == zsign)
        for L in [F(3), F(3, 7), F(12)]:
            R = _add(P, _sc(QI(L / 12), K))
            GA.check("P_a + (L/12) a n0 shares Z's sign", _psd_sign(_sc(I, _hM(R))) == zsign)
    for c in [(0, 1, 0, 0), (0, 0, 1, 0), (1, 2, 0, 0)]:
        P = _sc(QI(F(1, 2)), _mm(_vec(c), NINF))
        GA.check("control: spacelike translation indefinite", _psd_sign(_sc(I, _hM(P))) == "indef")
    for (a, b) in [(0, 1), (4, 5), (1, 5)]:
        S = _mm(G[a], G[b])
        GA.check("control: boosts and the dilation are indefinite", _psd_sign(_sc(I, _hM(S))) == "indef")
    # tabulated: i h P_{e0} on CS
    P0 = _sc(I, _hM(_sc(QI(F(1, 2)), _mm(G[0], NINF))))
    GA.check("tabulated: i h P_e0 has trace 2", sum((P0[i][i] for i in range(4)), QI(0)) == QI(2))
    return True


# --- oscillator model: polynomials in w1, w2 (b^+), z3, z4 (a^+), sparse dicts {exponents: QI}
NEG = [i for i in range(4) if H[i][i] == QI(-1)]          # h-negative: Zhat = b^+
POS = [i for i in range(4) if H[i][i] == ONE]             # h-positive: Zhat = a


def _mult(p, v):
    out = {}
    for e, c in p.items():
        e2 = list(e)
        e2[v] += 1
        out[tuple(e2)] = out.get(tuple(e2), QI(0)) + c
    return {k: c for k, c in out.items() if c != Z0}


def _diff(p, v):
    out = {}
    for e, c in p.items():
        if e[v]:
            e2 = list(e)
            e2[v] -= 1
            out[tuple(e2)] = out.get(tuple(e2), QI(0)) + c * QI(e[v])
    return {k: c for k, c in out.items() if c != Z0}


def _zhat(p, al, neg=None):
    neg = NEG if neg is None else neg
    return _mult(p, al) if al in neg else _diff(p, al)


def _zhat_dag(p, al, neg=None):
    neg = NEG if neg is None else neg
    return _diff(p, al) if al in neg else _mult(p, al)


def _padd(p, q, c=QI(1)):
    out = dict(p)
    for e, x in q.items():
        out[e] = out.get(e, QI(0)) + c * x
    return {k: v for k, v in out.items() if v != Z0}


def _Q(Hm, p, neg=None):
    out = {}
    for al in range(4):
        for be in range(4):
            if Hm[al][be] != Z0:
                out = _padd(out, _zhat_dag(_zhat(p, be, neg), al, neg), Hm[al][be])
    return out


def _weyl_centre(p):
    """(1/2) sum h_aa (Zhat^+ Zhat + Zhat Zhat^+) times i/2: the Weyl-ordered u(1) charge times i."""
    out = {}
    for al in range(4):
        t = _padd(_zhat_dag(_zhat(p, al), al), _zhat(_zhat_dag(p, al), al))
        out = _padd(out, t, H[al][al] * QI(F(1, 2)) * QI(0, F(1, 2)))
    return out


def _monomial(e):
    return {tuple(e): QI(1)}


def check_oscillator_energy_is_generated_by_z():
    premise("field-theory.twistor-attachment")
    premise("field-theory.imported-standard-field-theory")
    premise("hawking.helicity-lift-joints-itemised")
    # Lie homomorphism on tested pairs and states
    Hs = {}
    for (a, b) in [(0, 1), (2, 4), (3, 5), (0, 4), (1, 2)]:
        Hs[(a, b)] = _mm(G[a], G[b])
    tests = [_monomial([1, 0, 2, 0]), _padd(_monomial([0, 1, 0, 1]), _monomial([2, 0, 0, 3]), QI(F(-1, 3), 2))]
    pairs = [((0, 1), (2, 4)), ((0, 4), (1, 2)), ((3, 5), (0, 1))]
    for (x, y) in pairs:
        Mx, My = _sc(QI(F(1, 2)), Hs[x]), _sc(QI(F(1, 2)), Hs[y])
        comm = _add(_mm(Mx, My), _sc(QI(-1), _mm(My, Mx)))
        for p in tests:
            lhs = _padd(_Q(_hM(Mx), _Q(_hM(My), p)), _Q(_hM(My), _Q(_hM(Mx), p)), QI(-1))
            GA.check("[Q(M), Q(N)] = Q([M, N])", lhs == _Q(_hM(comm), p))
    # energy and helicity on every monomial of total degree <= 8
    table = {}
    HZ = _hM(_sc(QI(F(1, 2)), ZM))
    for nb1 in range(5):
        for nb2 in range(5):
            for na3 in range(5):
                for na4 in range(5):
                    e = [0, 0, 0, 0]
                    e[NEG[0]], e[NEG[1]], e[POS[0]], e[POS[1]] = nb1, nb2, na3, na4
                    p = _monomial(e)
                    Na, Nb = na3 + na4, nb1 + nb2
                    En = F(Na + Nb, 2) + 1
                    GA.check("Q(Z/2) = -i E on the monomial", _Q(HZ, p) == {tuple(e): QI(0, -En)})
                    s = F(Na - Nb, 2)
                    GA.check("Weyl-ordered centre = i s", _weyl_centre(p) == ({tuple(e): QI(0, s)} if s else {}))
                    if Na <= 4 and Nb <= 4:
                        table[(s, En)] = table.get((s, En), 0) + 1
    for s2 in range(-4, 5):
        s = F(s2, 2)
        absS = abs(s)
        for n in range(0, 5):
            if n + 2 * absS > 4:
                continue
            GA.check("multiplicity (n + 1)(n + 2|s| + 1)", table.get((s, absS + 1 + n), 0) == (n + 1) * (n + 2 * absS + 1))
        GA.check("no energy below |s| + 1", all(En >= absS + 1 for (ss, En) in table if ss == s))
    GA.check("tabulated: helicity 1/2, n = 1 has multiplicity 6 at energy 5/2", table[(F(1, 2), F(5, 2))] == 6)
    GA.check("E >= 1 on every tested state", min(En for (_, En) in table) == 1)
    # control: the opposite quantisation (h-positive components creating, h-negative annihilating)
    # its commutators are [Zhat, Zhat^+] = -h^{-1}, so it quantises the form -h
    HZm = _sc(QI(-1), HZ)
    for e in ([0, 0, 0, 0], [1, 0, 0, 2], [0, 3, 1, 0]):
        out = _Q(HZm, _monomial(e), neg=POS)
        En = F(sum(e), 2) + 1
        GA.check("control: the other quantisation gives +i E, a generator bounded above", out == {tuple(e): QI(0, En)})
    return True


def _fact(n):
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out


def _fock_ip(p, q):
    """Fock (Bargmann) inner product: monomials orthogonal with norm^2 the product of factorials."""
    tot = QI(0)
    for e, c in p.items():
        if e in q:
            w = 1
            for x in e:
                w *= _fact(x)
            tot = tot + c.conj() * q[e] * QI(w)
    return tot


def check_null_translations_are_nonnegative_on_the_modules():
    premise("synthesis.positive-conformal-energy-gives-positive-null-translations")
    premise("field-theory.twistor-attachment")
    premise("synthesis.positive-null-energy-gives-r-premises")
    states = [_monomial([0, 0, 0, 0]), _monomial([1, 0, 1, 0]), _padd(_monomial([1, 0, 0, 0]), _monomial([0, 0, 1, 0]), QI(2, -1)),
              _padd(_monomial([0, 1, 0, 2]), _monomial([1, 1, 1, 0]), QI(F(-3, 2), 1)), _padd(_monomial([2, 0, 0, 0]), _monomial([0, 0, 0, 1]), QI(0, 5))]
    table = {(1, 1, 0, 0): [F(1), F(2), F(9), F(105, 8), F(83, 2)],
             (1, -1, 0, 0): [F(1), F(2), F(9), F(105, 8), F(83, 2)],
             (1, 0, F(3, 5), F(4, 5)): [F(1), F(6, 5), F(33, 5), F(569, 40), F(499, 10)],
             (1, 0, 0, -1): [F(1), F(3), F(12), F(47, 4), F(31)]}
    for c in [(1, 1, 0, 0), (1, -1, 0, 0), (1, 0, F(3, 5), F(4, 5)), (1, 0, 0, -1)]:
        P = _sc(QI(F(1, 2)), _mm(_vec(c), NINF))
        Hm = _hM(P)
        vals = []
        for p in states:
            v = _fock_ip(p, _Q(Hm, p))
            ev = QI(0, 1) * v                    # <p, i Q(P) p>, real
            GA.check("expectation is real", ev.im == 0)
            vals.append(ev.re)
        GA.check("future null translation: nonnegative on every tested state", all(x >= 0 for x in vals))
        GA.check("tabulated expectations", vals == table[c])
        GA.check("and positive on some", any(x > 0 for x in vals))
        nP = _sc(QI(-1), Hm)
        GA.check("control: the past null translation is negative on some state",
                 any((QI(0, 1) * _fock_ip(p, _Q(nP, p))).re < 0 for p in states))
    # tabulated: <1|i Q(P_{e0+e1})|1> on the lowest state (E = 1, s = 0) of the oscillator module
    P = _sc(QI(F(1, 2)), _mm(_vec((1, 1, 0, 0)), NINF))
    v = QI(0, 1) * _fock_ip(_monomial([0, 0, 0, 0]), _Q(_hM(P), _monomial([0, 0, 0, 0])))
    GA.check("tabulated: vacuum expectation of the null translation", v == QI(1))
    return True
