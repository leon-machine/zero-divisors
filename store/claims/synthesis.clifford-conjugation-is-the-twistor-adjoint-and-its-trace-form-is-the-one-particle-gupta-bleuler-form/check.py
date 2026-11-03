"""synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form: exact checks.

Model 1 (the attachment): the eight-dimensional Fock module CS of Cl(2,4), three modes in the Jordan-Wigner
basis, ground generators e1 (square +1, time), e2, e3, e4 (square -1), ascent plane e+ (+1), e- (-1); the
positive Hermitian structure h is the identity Gram matrix (every generator unitary); J = i e1 e+,
Sigma = h(., J .), as in synthesis.positive-structure-is-twistor-form-at-imaginary-time.
The Sigma-adjoint of an operator A is A# = Sigma^-1 A^dagger Sigma = J A^dagger J.
Model 2 (the polarisations): the polynomials in z0..z3 with <z^n, z^m> = n! delta (Proposition
field-theory.fock-space-maxwell-modes), Cl(1,3) for the Lorentz generators.
Model 3 (the ghost floor): two tower modes b, d (Jordan-Wigner, 4 states, the CAR of Fact
field-theory.imported-tower-limit), S = 1 - (b* - d*)(b - d), the ghost twist of clause (K2) of the Krein premise.
Exact Gaussian rationals (GA.QI) and Fractions throughout.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA as g
import fock
from tp_premise import premise

Z = g.QI(0)
IU = g.QI(0, 1)
N = 8


def zeros(n, m=None):
    return [[g.QI(0) for _ in range(m if m is not None else n)] for _ in range(n)]


def eye(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = g.QI(1)
    return M


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def ms(c, A):
    c = c if isinstance(c, g.QI) else g.QI(c)
    return [[c * x for x in r] for r in A]


def mm(*Ms):
    out = Ms[0]
    for M in Ms[1:]:
        out = g.field_mat_mul(out, M)
    return out


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def tr(A):
    return sum((A[i][i] for i in range(len(A))), Z)


def fock_ops(m):
    n = 2 ** m
    cr = [[[g.QI(x) for x in r] for r in fock.to_dense(fock.cre(j, m), n)] for j in range(m)]
    return cr, [dag(c) for c in cr]


CR, AN = fock_ops(3)
HERM = []
for _j in range(3):
    HERM.append(madd(CR[_j], AN[_j]))
    HERM.append(ms(IU, madd(CR[_j], ms(-1, AN[_j]))))
GEN = {"e1": HERM[0], "e2": ms(IU, HERM[1]), "e3": ms(IU, HERM[2]), "e4": ms(IU, HERM[3]),
       "ep": HERM[4], "em": ms(IU, HERM[5])}
SQ = {"e1": 1, "e2": -1, "e3": -1, "e4": -1, "ep": 1, "em": -1}
NAMES = ["e1", "e2", "e3", "e4", "ep", "em"]
SPACETIME = ["e1", "e2", "e3", "e4"]
J = ms(IU, mm(GEN["e1"], GEN["ep"]))
SAMPLES = [(1, 2, -1, 3, 0, 1), (2, -1, 0, 1, 3, -2), (0, 1, 1, -1, 2, 5)]   # sample real vectors
LAMBDAS = (F(-3), F(2, 7))                                                   # rescalings of Sigma
SAMPLES2 = SAMPLES[:2]
SIGNATURES = ((1, 3), (2, 4))
DEG = 3                                                                      # polynomial degree sampled


def minv(M):
    n = len(M)
    cols = [g.field_solve(M, [g.QI(1) if i == k else g.QI(0) for i in range(n)]) for k in range(n)]
    return [[cols[k][i] for k in range(n)] for i in range(n)]


def sharp(A, Sig=None):
    """Adjoint for the Hermitian form Sig (default Sigma = J): Sig^-1 A^dagger Sig."""
    if Sig is None:
        return mm(J, dag(A), J)
    inv = minv(Sig)
    return mm(inv, dag(A), Sig)


def blade(names):
    out = eye(N)
    for a in names:
        out = mm(out, GEN[a])
    return out


def clifford_conjugate_sign(names):
    """Clifford conjugation (reversion composed with the grade involution) on a blade of grade k: (-1)^{k(k+1)/2}."""
    k = len(names)
    return (-1) ** (k * (k + 1) // 2)


def vec(coeffs):
    """Real combination of the six generators."""
    out = zeros(N)
    for a, c in zip(NAMES, coeffs):
        if c != 0:
            out = madd(out, ms(g.QI(c), GEN[a]))
    return out


def form(A, B, adj):
    """Normalised trace form (1/8) tr(adj(A) B)."""
    return tr(mm(adj(A), B)) * g.QI(F(1, 8))


# ------------------------------------------------------------------ (i) the twistor adjoint is Clifford conjugation
def check_twistor_adjoint_is_clifford_conjugation():
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    ok = meq(mm(J, J), eye(N)) and meq(dag(J), J)
    for a in NAMES:
        ok = ok and meq(mm(GEN[a], GEN[a]), ms(SQ[a], eye(N)))
        ok = ok and meq(sharp(GEN[a]), ms(-1, GEN[a]))          # every real vector is Sigma-anti-self-adjoint
    count = 0
    for k in range(len(NAMES) + 1):
        for names in combinations(NAMES, k):
            B = blade(names)
            ok = ok and meq(sharp(B), ms(clifford_conjugate_sign(names), B))
            count += 1
    ok = ok and count == 64
    # rescaling Sigma by a nonzero real factor leaves the adjoint unchanged
    for lam in LAMBDAS:
        Sig = ms(g.QI(lam), J)
        for a in ("e1", "e2", "ep"):
            ok = ok and meq(sharp(GEN[a], Sig), sharp(GEN[a]))
    g.check("twistor adjoint is Clifford conjugation on all 64 blades, independent of the factor of Sigma", ok)
    return ok


# ------------------------------------------------------------------ (ii) its trace form on vectors is the Gupta-Bleuler form
def check_trace_form_on_vectors_is_gupta_bleuler():
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    ok = True
    hadj = dag
    for i, a in enumerate(NAMES):
        for j, b in enumerate(NAMES):
            want = -SQ[a] if i == j else 0
            ok = ok and form(GEN[a], GEN[b], sharp) == g.QI(want)          # Krein: -a.b
            ok = ok and form(GEN[a], GEN[b], hadj) == g.QI(1 if i == j else 0)  # positive: Euclidean
    # on general real vectors: (1/8) tr(u# w) = -u.w with u.w the metric of signature (2,4)
    for u in SAMPLES:
        for w in SAMPLES:
            dotuw = sum(SQ[n] * x * y for n, x, y in zip(NAMES, u, w))
            ok = ok and form(vec(u), vec(w), sharp) == g.QI(-dotuw)
    # restricted to spacetime vectors: signature (1, 3) with the time direction negative (the GB form -u.w)
    gram = [[form(GEN[a], GEN[b], sharp).re for b in SPACETIME] for a in SPACETIME]
    ok = ok and gram == [[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    # the two forms differ by Ad(J): Krein(u, w) = positive(u, J w J); Ad(J) reflects e1 and e+ only
    for a in NAMES:
        img = mm(J, GEN[a], J)
        sgn = -1 if a in ("e1", "ep") else 1
        ok = ok and meq(img, ms(sgn, GEN[a]))
        for b in NAMES:
            ok = ok and form(GEN[a], GEN[b], sharp) == form(GEN[a], mm(J, GEN[b], J), hadj)
    g.check("trace form of the twistor adjoint on vectors is -u.w; the positive structure gives the Euclidean form", ok)
    return ok


# ------------------------------------------------------------------ (iii) invariance: conformal group for Krein, no boost for positive
def rotor_conj(R, A):
    Rinv = minv(R)
    return mm(R, A, Rinv)


BOOST = madd(ms(F(5, 4), eye(N)), ms(F(3, 4), mm(GEN["e1"], GEN["e2"])))           # e1 e2 squares +1
NINF = madd(GEN["ep"], ms(-1, GEN["em"]))
TRANSL = madd(eye(N), ms(F(1, 2), mm(GEN["e3"], NINF)))                              # (e3 ninf)^2 = 0
ROT = madd(ms(F(3, 5), eye(N)), ms(F(4, 5), mm(GEN["e2"], GEN["e3"])))               # e2 e3 squares -1
DIL = madd(ms(F(5, 4), eye(N)), ms(F(3, 4), mm(GEN["ep"], GEN["em"])))               # e+ e- squares +1


def check_krein_trace_form_is_conformally_invariant_and_positive_one_is_not():
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    boost = BOOST
    ok = True
    for R in (BOOST, TRANSL, ROT, DIL):
        for u in SAMPLES2:
            for w in SAMPLES2:
                U, W = vec(u), vec(w)
                ok = ok and form(rotor_conj(R, U), rotor_conj(R, W), sharp) == form(U, W, sharp)
    # the boost maps vectors to vectors and moves the positive form
    E1 = GEN["e1"]
    pos_before = form(E1, E1, dag)
    pos_after = form(rotor_conj(boost, E1), rotor_conj(boost, E1), dag)
    krein_after = form(rotor_conj(boost, E1), rotor_conj(boost, E1), sharp)
    ok = ok and pos_before == g.QI(1) and pos_after == g.QI(F(257, 32)) and krein_after == g.QI(-1)
    img = rotor_conj(boost, E1)
    ok = ok and meq(img, madd(ms(F(17, 8), E1), ms(F(-15, 8), GEN["e2"])))
    g.check("Krein trace form invariant under boost, rotation, translation and dilation rotors; positive form not", ok)
    return ok


# ------------------------------------------------------------------ (iv) uniqueness on polarisations (Schur, computed)
def _lorentz_vector_rep():
    s = g.sig(1, 3)
    gens = [g.gen(i) for i in range(4)]
    reps = []
    for i, j in combinations(range(4), 2):
        Bv = g.mul(gens[i], gens[j], s)
        M = []
        for col in range(4):
            img = g.sub(g.mul(Bv, gens[col], s), g.mul(gens[col], Bv, s))
            M.append([img.get((r,), F(0)) for r in range(4)])
        reps.append([[M[c][r] for c in range(4)] for r in range(4)])     # column = image of basis vector
    return reps


def _nullspace(rows, n):
    M = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = 1 / F(M[r][c])
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fcol in free:
        v = [F(0)] * n
        v[fcol] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fcol]
        basis.append(v)
    return basis


def check_invariant_forms_on_polarisations_are_multiples_of_the_metric():
    reps = _lorentz_vector_rep()
    # unknown real 4x4 matrix M (16 entries); invariance X^T M + M X = 0 for the six generators
    rows = []
    for X in reps:
        for a in range(4):
            for b in range(4):
                row = [F(0)] * 16
                for c in range(4):
                    row[c * 4 + b] += X[c][a]          # (X^T M)_{ab} = sum_c X_{ca} M_{cb}
                    row[a * 4 + c] += X[c][b]          # (M X)_{ab} = sum_c M_{ac} X_{cb}
                rows.append(row)
    ns = _nullspace(rows, 16)
    ok = len(ns) == 1
    v = ns[0]
    ok = ok and all(v[a * 4 + b] == 0 for a in range(4) for b in range(4) if a != b)
    ok = ok and v[0] != 0 and all(v[5 * k] == -v[0] for k in (1, 2, 3))
    # a Hermitian invariant form H = S + iA has S, A real invariant (the equation is real-linear):
    # the solution space is real one-dimensional and symmetric, so A = 0 and H is a real multiple of the metric,
    # indefinite: no Lorentz-invariant positive form on the polarisations
    ok = ok and len(rows) == 96
    g.check("Lorentz-invariant bilinear forms on polarisation vectors: one-dimensional, the metric", ok)
    return ok


# ------------------------------------------------------------------ (v) second quantisation: the Fock form over -u.w is the stored eta form
def _monos(deg):
    out = []
    for d in range(deg + 1):
        for a in product(range(d + 1), repeat=4):
            if sum(a) == d:
                out.append(a)
    return out


def _fact(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def check_fock_form_over_the_trace_form_is_the_stored_krein_form():
    premise("field-theory.fock-space-maxwell-modes")
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    kdiag = [form(GEN[a], GEN[a], sharp).re for a in SPACETIME]       # one-particle Krein norms of z_mu
    monos = _monos(DEG)
    ok = kdiag == [-1, 1, 1, 1]
    metric = (1, -1, -1, -1)

    def fock(a, b, signs):
        if a != b:
            return F(0)
        v = F(1)
        for n, s in zip(a, signs):
            v *= _fact(n) * (s ** n)
        return v

    for a in monos:
        for b in monos:
            krein = fock(a, b, kdiag)
            eta = (-1) ** a[0]
            ok = ok and krein == eta * fock(a, b, (1, 1, 1, 1))            # = <z^a, eta z^b>, eta = (-1)^{n0}
    # adjoint of a_mu = d/dz_mu for the Krein Fock form is -g_{mu mu} z_mu, so [a(u), a(w)^dag] = -u.w
    for mu in range(4):
        for a in monos:
            for b in monos:
                if sum(b) == 0 or b[mu] == 0:
                    lhs = F(0)
                else:
                    bm = tuple(x - (1 if i == mu else 0) for i, x in enumerate(b))
                    lhs = b[mu] * fock(a, bm, kdiag)                      # <z^a, a_mu z^b>
                am = tuple(x + (1 if i == mu else 0) for i, x in enumerate(a))
                rhs = -metric[mu] * fock(am, b, kdiag)                    # <(-g z_mu) z^a, z^b>
                ok = ok and lhs == rhs
    g.check("Fock form over the trace form is <x, (-1)^{n0} y>, with a_mu^dag = -g_mumu z_mu", ok)
    return ok


# ------------------------------------------------------------------ (vi) ghost twist: the same mode parity, Clifford conjugation of a (2,2) frame
def check_ghost_twist_is_a_mode_parity_as_j_is():
    premise("field-theory.imported-tower-limit")
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    cr, an = fock_ops(2)
    b, d = an[0], an[1]
    bs, ds = cr[0], cr[1]
    I4m = eye(4)
    S = madd(I4m, ms(-1, mm(madd(bs, ms(-1, ds)), madd(b, ms(-1, d)))))
    ok = meq(mm(S, S), I4m) and meq(dag(S), S) and meq(mm(S, b, S), d)
    # S = 1 - 2 n_-, n_- the number of the mode m- = (b - d)/sqrt2: n_- = (b* - d*)(b - d)/2
    nminus = ms(F(1, 2), mm(madd(bs, ms(-1, ds)), madd(b, ms(-1, d))))
    ok = ok and meq(mm(nminus, nminus), nminus) and meq(S, madd(I4m, ms(-2, nminus)))
    # twistor side: J = 2 n_c - 1, n_c the number of the mode c = (e1 + i e+)/2 of the time and ascent generators
    c = ms(F(1, 2), madd(GEN["e1"], ms(IU, GEN["ep"])))
    nc = mm(dag(c), c)
    ok = ok and meq(mm(c, c), zeros(N)) and meq(mm(nc, nc), nc) and meq(J, madd(ms(2, nc), ms(-1, eye(N))))
    g.check("ghost twist S is the parity of one mode, as J is up to sign", ok)
    return ok


# ------------------------------------------------------------------ (vii) the vector identity needs no module and no twistor form
def check_scalar_part_of_clifford_conjugate_is_minus_the_metric_in_any_signature():
    ok = True
    for (p, q) in SIGNATURES:
        s = g.sig(p, q)
        n = p + q
        for i in range(n):
            for j in range(n):
                ei, ej = g.gen(i), g.gen(j)
                conj_ei = g.neg(ei)                                   # Clifford conjugation of a vector
                val = g.mul(conj_ei, ej, s).get((), F(0))
                want = -s[i] if i == j else 0
                ok = ok and val == want
    ok = ok and len(SIGNATURES) == 2
    g.check("<conj(a) b>_0 = -a.b in Cl(1,3) and Cl(2,4) with no module and no twistor form", ok)
    return ok
