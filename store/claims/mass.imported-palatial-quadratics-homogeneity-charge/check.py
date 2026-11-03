"""mass.imported-palatial-quadratics-homogeneity-charge: exact checks.

Realisation: Laurent polynomials in Z^0..Z^3 with Zbar_b = -hbar d/dZ^b (hbar = 3/7, a generic rational),
q(M) = (1/2) sum M^b_a (Z^a Zbar_b + Zbar_b Z^a). Operators are compared by their action on five test
Laurent polynomials of mixed degrees (negative exponents included).
(1) [Z^a, Zbar_b] = +hbar delta^a_b on the test functions.
(2) [q(M), q(N)] = hbar q([M, N]) for all 256 ordered pairs of matrix units of gl(4) (hence on all of
    gl(4, C) by bilinearity, and on its real form su(2,2)); the sixteen q(E_ba) act independently (the
    representation of gl(4) is faithful), and [q(M), Z^c] = -hbar (M Z)^c for every matrix unit.
(3) q(id) acts on monomials of homogeneity h = -5..3 as -(h + 2) hbar; it equals the normal-ordered
    sum Z^a Zbar_a (which gives -hbar h) minus 2 hbar, the symmetric-ordering shift of hbar/2 per dimension.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

# ---------------------------------------------------------------------------
# Laurent polynomials in Z^0..Z^3 (exponents may be negative), exact; the palatial operators
# Z^a (multiplication) and Zbar_b = -hbar d/dZ^b, the realisation with [Z^a, Zbar_b] = +hbar delta.
# ---------------------------------------------------------------------------
HBAR = F(3, 7)


def lp(*terms):
    """lp((coeff, (e0, e1, e2, e3)), ...)"""
    out = {}
    for c, e in terms:
        out[e] = out.get(e, F(0)) + F(c)
    return {e: c for e, c in out.items() if c != 0}


def lp_add(*fs):
    out = {}
    for f in fs:
        for e, c in f.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c != 0}


def lp_scal(s, f):
    return {e: s * c for e, c in f.items() if s * c != 0}


def zmul(a, f):
    return {tuple(x + (1 if i == a else 0) for i, x in enumerate(e)): c for e, c in f.items()}


def deriv(b, f):
    out = {}
    for e, c in f.items():
        if e[b] != 0:
            ne = tuple(x - (1 if i == b else 0) for i, x in enumerate(e))
            out[ne] = out.get(ne, F(0)) + c * e[b]
    return {e: c for e, c in out.items() if c != 0}


def zbar(b, f):
    return lp_scal(-HBAR, deriv(b, f))


def q_op(M, f):
    """q(M) = (1/2) sum M^b_a (Z^a Zbar_b + Zbar_b Z^a), M[b][a] = M^b_a."""
    terms = []
    for b in range(4):
        for a in range(4):
            if M[b][a]:
                terms.append(lp_scal(F(1, 2) * M[b][a], lp_add(zmul(a, zbar(b, f)), zbar(b, zmul(a, f)))))
    return lp_add(*terms)


def munit(b, a):
    return [[F(1) if (r, c) == (b, a) else F(0) for c in range(4)] for r in range(4)]


ID4 = [[F(1) if r == c else F(0) for c in range(4)] for r in range(4)]


def mat_comm(M, N):
    return [[sum((M[i][k] * N[k][j] - N[i][k] * M[k][j] for k in range(4)), F(0)) for j in range(4)]
            for i in range(4)]


def degree(e):
    return sum(e)

TESTS = [lp((1, (2, -1, 0, 1)), (3, (0, 0, 1, 0))), lp((1, (-2, 0, 0, 0))), lp((2, (0, 1, -3, 1)), (-1, (1, 1, 1, 1))),
         lp((5, (1, 0, 0, 0)), (1, (0, 0, 0, -1)), (F(1, 2), (0, 2, 0, 0))), lp((1, (0, 0, 0, 0)))]
MONOMIALS = [(-3, 0, -1, -1), (0, -2, 0, -2), (-1, -1, 0, 0), (1, -2, 0, 0), (0, 0, 0, -1), (0, 0, 0, 0),
             (1, 0, 0, 0), (0, 1, 1, 0), (1, 1, 0, 1)]


def check_palatial_quadratics_represent_gl4():
    premise("correspondence.symmetrised-quadratics-palatial-algebra")
    ok = True
    for f in TESTS:
        for a in range(4):
            for b in range(4):
                c = lp_add(zmul(a, zbar(b, f)), lp_scal(-1, zbar(b, zmul(a, f))))
                ok = ok and c == lp_scal(HBAR if a == b else F(0), f)
    units = [munit(b, a) for b in range(4) for a in range(4)]
    for M in units:
        for N in units:
            K = mat_comm(M, N)
            for f in TESTS[:3]:
                lhs = lp_add(q_op(M, q_op(N, f)), lp_scal(-1, q_op(N, q_op(M, f))))
                ok = ok and lhs == lp_scal(HBAR, q_op(K, f))
    # adjoint action on the linear generators: [q(M), Z^c] = -hbar sum_a M^c_a Z^a
    for M in units:
        for c in range(4):
            for f in TESTS[:2]:
                lhs = lp_add(q_op(M, zmul(c, f)), lp_scal(-1, zmul(c, q_op(M, f))))
                rhs = lp_add(*[lp_scal(-HBAR * M[c][a], zmul(a, f)) for a in range(4)])
                ok = ok and lhs == rhs
    # faithfulness: the sixteen q(E) act independently on the test functions
    keys = sorted({e for M in units for f in TESTS for e in q_op(M, f)})
    rows = [[q_op(M, f).get(e, F(0)) for f in TESTS for e in keys] for M in units]
    ok = ok and GA.rank_of_vectors(rows) == 16
    _tp_rv = (ok); assert _tp_rv is not False, "check_palatial_quadratics_represent_gl4"; return _tp_rv


def check_identity_quadratic_is_homogeneity_shifted_by_two():
    premise("correspondence.symmetrised-quadratics-palatial-algebra")
    premise("correspondence.shared-core-ordering-dictionary")
    ok = True
    degrees = []
    for e in MONOMIALS:
        f = lp((1, e))
        h = degree(e)
        degrees.append(h)
        ok = ok and q_op(ID4, f) == lp_scal(-(h + 2) * HBAR, f)
        normal = lp_add(*[zmul(a, zbar(a, f)) for a in range(4)])
        ok = ok and normal == lp_scal(-h * HBAR, f)
        ok = ok and lp_add(q_op(ID4, f), lp_scal(-1, normal)) == lp_scal(-2 * HBAR, f)
    ok = ok and sorted(set(degrees)) == [-5, -4, -2, -1, 0, 1, 2, 3]
    _tp_rv = (ok); assert _tp_rv is not False, "check_identity_quadratic_is_homogeneity_shifted_by_two"; return _tp_rv
