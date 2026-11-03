"""standard-model.imported-twistor-charge-helicity: exact checks.

Realisation: Laurent polynomials in Z^0..Z^3, Zbar_b = -hbar d/dZ^b (hbar = 3/7), q(M) the symmetrised
quadratic, helicity operator s = (1/2) q(id).
(1) The operator identity q(id) = -hbar (Upsilon + 2), Upsilon = Z^a d_a the Euler operator, on six test
    Laurent polynomials of mixed degree.
(2) A homogeneous function of degree h is an eigenfunction of s with eigenvalue s hbar where h = -2s - 2:
    checked on monomials of degree -6..3, which give s = 2, 3/2, 1, 1/2, 0, -1/2, -1, -3/2, -2, -5/2; a sum of
    two different homogeneities is not an eigenfunction.
(3) The offset -2 is the ordering shift: the normal-ordered charge sum Z^a Zbar_a is -hbar Upsilon, with
    no offset, and the symmetric ordering subtracts hbar/2 for each of the four dimensions.
The identification with the Penrose transform's cohomological classification is literature with no finite
core; hawking.imported-penrose-transform is that restatement and is not called.
"""
from fractions import Fraction as F

import GA  # noqa: F401
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
         lp((5, (1, 0, 0, 0)), (1, (0, 0, 0, -1)), (F(1, 2), (0, 2, 0, 0))), lp((1, (0, 0, 0, 0))),
         lp((1, (-4, 0, 0, 0)), (7, (-1, -1, -1, -1)))]
MONOMIALS = [(-6, 0, 0, 0), (-3, 0, -1, -1), (-2, -1, 0, -1), (0, -2, 0, -2), (0, -1, -1, -1), (-1, -1, 0, 0),
             (1, -2, 0, 0), (0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 1, 0), (1, 1, 0, 1)]


def euler(f):
    return lp_add(*[zmul(a, deriv(a, f)) for a in range(4)])


def check_identity_charge_is_shifted_euler_operator():
    premise("hawking.homogeneity-ordering-shift")
    ok = True
    for f in TESTS:
        ok = ok and q_op(ID4, f) == lp_add(lp_scal(-HBAR, euler(f)), lp_scal(-2 * HBAR, f))
    _tp_rv = (ok); assert _tp_rv is not False, "check_identity_charge_is_shifted_euler_operator"; return _tp_rv


def check_homogeneity_is_minus_two_s_minus_two():
    premise("hawking.homogeneity-ordering-shift")
    ok = True
    helicities = []
    for e in MONOMIALS:
        f = lp((1, e))
        h = degree(e)
        sf = lp_scal(F(1, 2), q_op(ID4, f))
        # eigenvalue s hbar
        s = sf.get(e, F(0)) / (HBAR * f[e])
        ok = ok and sf == lp_scal(s * HBAR, f) and h == -2 * s - 2
        helicities.append(s)
    ok = ok and sorted(set(helicities)) == [F(k, 2) for k in range(-5, 5)]
    mixed = lp((1, (1, 0, 0, 0)), (1, (-3, 0, 0, 0)))
    smix = lp_scal(F(1, 2), q_op(ID4, mixed))
    ok = ok and all(smix != lp_scal(c, mixed) for c in (smix[(1, 0, 0, 0)], smix[(-3, 0, 0, 0)]))
    _tp_rv = (ok); assert _tp_rv is not False, "check_homogeneity_is_minus_two_s_minus_two"; return _tp_rv


def check_offset_is_the_ordering_shift():
    premise("correspondence.shared-core-ordering-dictionary")
    ok = True
    for f in TESTS:
        normal = lp_add(*[zmul(a, zbar(a, f)) for a in range(4)])
        ok = ok and normal == lp_scal(-HBAR, euler(f))
        shift = lp_add(q_op(ID4, f), lp_scal(-1, normal))
        ok = ok and shift == lp_scal(4 * (-HBAR / 2), f)
        # per dimension: the symmetrised Z^a Zbar_a minus its normal order is -hbar/2
        for a in range(4):
            sym = lp_scal(F(1, 2), lp_add(zmul(a, zbar(a, f)), zbar(a, zmul(a, f))))
            ok = ok and lp_add(sym, lp_scal(-1, zmul(a, zbar(a, f)))) == lp_scal(-HBAR / 2, f)
    _tp_rv = (ok); assert _tp_rv is not False, "check_offset_is_the_ordering_shift"; return _tp_rv
