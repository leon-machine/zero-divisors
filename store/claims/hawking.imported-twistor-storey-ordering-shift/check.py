"""hawking.imported-twistor-storey-ordering-shift: exact checks of the finite content of this imported Fact.

(1) The spinor module (Fact correspondence.fock-model-complexified-ascended-algebra): Cl(2,4) acts on the
    eight-dimensional Fock space of three modes (Jordan-Wigner matrices over Q(i), GA.QI) through
    g0 = a1 + a1^dag, g1 = a2 + a2^dag (square +1), g2 = a1 - a1^dag, g3 = a2 - a2^dag, g4 = i (a3 + a3^dag),
    g5 = a3 - a3^dag (square -1). The Clifford relations hold; vectors flip the Fock parity; the volume element
    I6 = g0 ... g5 squares to -1, commutes with every even element and acts on the even sector as a scalar
    +-i (the complex unit); the 32 even blades restricted to the even sector span all 4 x 4 complex matrices
    (rank 16 over Q(i)): the even sector is an irreducible module of complex dimension 4, the conformal spinor
    space.
(2) The palatial storey (Lemma correspondence.symmetrised-quadratics-palatial-algebra), hbar = 1, realised on
    polynomials by Zbar_nu = -d/dZ^nu: [Z^mu, Zbar_nu] = delta^mu_nu, and for sample M (identity included)
    q(M) = 1/2 sum M_mu^nu (Z^mu Zbar_nu + Zbar_nu Z^mu) equals sum M_mu^nu Z^mu Zbar_nu - tr(M)/2 on every
    monomial of degree <= 2; for M = id the shift is -1/2 per variable, -2 in dimension 4 (and -1, -3/2 in
    dimensions 2, 3).
(3) The Clifford storey (Proposition correspondence.clifford-side-ordering-shift): in Cl(1,1) with
    v = (e0 + e1)/2, v* = (e0 - e1)/2, v v* + v* v = 1, N = v* v is idempotent and the boost generator of the plane
    is e0 e1 / 2 = N - 1/2, eigenvalues -1/2 and +1/2: a shift of -1/2 per mode, the same signed shift as (2).
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
import fock
from tp_premise import premise

QI = GA.QI
D = 8
MS = [[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
      [[2, -1, 0, 3], [1, 0, 0, 0], [0, 5, -2, 1], [0, 0, 1, 4]],
      [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]]


qmm = GA.field_mat_mul


def qadd(a, b, c=1):
    return [[a[i][j] + b[i][j] * c for j in range(len(a))] for i in range(len(a))]


def qid(n=D):
    return [[QI(1) if i == j else QI(0) for j in range(n)] for i in range(n)]


def ann(j):
    """a_j on three Jordan-Wigner modes, dense over GA.QI (LSB bitmask basis)."""
    return fock.to_dense(fock.msc(QI(1), fock.ann(j, 3)), D, QI(0))


def dag(m):
    return [[m[j][i].conj() for j in range(D)] for i in range(D)]


def gens():
    a = [ann(j) for j in range(3)]
    c = [dag(x) for x in a]
    return [qadd(a[0], c[0]), qadd(a[1], c[1]), qadd(a[0], c[0], -1), qadd(a[1], c[1], -1),
            [[x * QI(0, 1) for x in row] for row in qadd(a[2], c[2])], qadd(a[2], c[2], -1)]


def check_conformal_spinor_space_has_complex_dimension_four():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    g = gens()
    squares = [1, 1, -1, -1, -1, -1]
    ok = True
    for i in range(6):
        for j in range(6):
            anti = qadd(qmm(g[i], g[j]), qmm(g[j], g[i]))
            ok = ok and anti == [[x * (2 * squares[i] if i == j else 0) for x in row] for row in qid()]
    even = [s for s in range(D) if bin(s).count("1") % 2 == 0]
    odd = [s for s in range(D) if s not in even]
    ok = ok and all(g[k][r][c] == 0 for k in range(6) for r in even for c in even)
    I6 = qid()
    for k in range(6):
        I6 = qmm(I6, g[k])
    ok = ok and qmm(I6, I6) == [[-x for x in row] for row in qid()]
    blades = []
    for r in range(0, 7, 2):
        for S in combinations(range(6), r):
            m = qid()
            for k in S:
                m = qmm(m, g[k])
            blades.append(m)
    ok = ok and len(blades) == 32
    ok = ok and all(qmm(b, I6) == qmm(I6, b) for b in blades)
    block = [[I6[r][c] for c in even] for r in even]
    unit = block[0][0]
    ok = ok and unit in (QI(0, 1), QI(0, -1))
    ok = ok and block == [[unit if r == c else QI(0) for c in range(4)] for r in range(4)]
    ok = ok and all(I6[r][c] == 0 for r in even for c in odd)
    rows = [[b[r][c] for r in even for c in even] for b in blades]
    ok = ok and GA.field_rank(rows) == 16 and len(even) == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_conformal_spinor_space_has_complex_dimension_four"; return _tp_rv


def mono_Z(a, f):
    out = {}
    for ex, c in f.items():
        e = list(ex)
        e[a] += 1
        out[tuple(e)] = out.get(tuple(e), F(0)) + c
    return out


def mono_Zbar(a, f):
    """Zbar_a = -d/dZ^a (hbar = 1)."""
    out = {}
    for ex, c in f.items():
        if ex[a] == 0:
            continue
        e = list(ex)
        e[a] -= 1
        out[tuple(e)] = out.get(tuple(e), F(0)) - c * ex[a]
    return out


def lin(*terms):
    out = {}
    for coef, f in terms:
        for ex, c in f.items():
            out[ex] = out.get(ex, F(0)) + coef * c
    return {ex: c for ex, c in out.items() if c != 0}


def check_palatial_symmetric_ordering_shift():
    premise("correspondence.symmetrised-quadratics-palatial-algebra")
    ok = True
    n = 4
    monos = [ex for ex in product(range(3), repeat=n) if sum(ex) <= 2]
    for ex in monos:
        f = {ex: F(1)}
        for mu in range(n):
            for nu in range(n):
                cm = lin((F(1), mono_Z(mu, mono_Zbar(nu, f))), (F(-1), mono_Zbar(nu, mono_Z(mu, f))))
                ok = ok and cm == ({ex: F(1)} if mu == nu else {})
    for M in MS:
        trM = sum(M[i][i] for i in range(n))
        for ex in monos:
            f = {ex: F(1)}
            sym, normal = [], []
            for mu in range(n):
                for nu in range(n):
                    if M[mu][nu]:
                        sym.append((F(M[mu][nu], 2), mono_Z(mu, mono_Zbar(nu, f))))
                        sym.append((F(M[mu][nu], 2), mono_Zbar(nu, mono_Z(mu, f))))
                        normal.append((F(M[mu][nu]), mono_Z(mu, mono_Zbar(nu, f))))
            ok = ok and lin(*sym) == lin(*(normal + [(-F(trM, 2), f)]))
    # identity: shift -1/2 per variable
    for nvar, shift in ((2, F(-1)), (3, F(-3, 2)), (4, F(-2))):
        f = {tuple([0] * nvar): F(1)}
        tot = lin(*[(F(1, 2), mono_Z(a, mono_Zbar(a, f))) for a in range(nvar)] +
                  [(F(1, 2), mono_Zbar(a, mono_Z(a, f))) for a in range(nvar)])
        ok = ok and tot == {tuple([0] * nvar): shift}
    _tp_rv = (ok); assert _tp_rv is not False, "check_palatial_symmetric_ordering_shift"; return _tp_rv


def check_clifford_storey_shift_matches():
    premise("correspondence.clifford-side-ordering-shift")
    premise("correspondence.shared-core-ordering-dictionary")
    sq = GA.sig(1, 1)
    e0, e1 = GA.gen(0), GA.gen(1)
    v = GA.scal(F(1, 2), GA.add(e0, e1))
    vs = GA.scal(F(1, 2), GA.sub(e0, e1))
    ok = GA.add(GA.mul(v, vs, sq), GA.mul(vs, v, sq)) == {(): F(1)}
    ok = ok and GA.mul(v, v, sq) == {} and GA.mul(vs, vs, sq) == {}
    N = GA.mul(vs, v, sq)
    ok = ok and GA.eq(GA.mul(N, N, sq), N)
    boost = GA.scal(F(1, 2), GA.mul(e0, e1, sq))
    ok = ok and GA.eq(boost, GA.sub(N, GA.sc(F(1, 2))))
    # eigenvalues on the two occupation projectors N and 1 - N
    ok = ok and GA.eq(GA.mul(boost, N, sq), GA.scal(F(1, 2), N))
    ok = ok and GA.eq(GA.mul(boost, GA.sub(GA.sc(1), N), sq), GA.scal(F(-1, 2), GA.sub(GA.sc(1), N)))
    _tp_rv = (ok); assert _tp_rv is not False, "check_clifford_storey_shift_matches"; return _tp_rv
