"""correspondence.symmetrised-quadratics-palatial-algebra: exact checks.

The palatial algebra is realised on polynomials in z_0..z_3 over Q(i): Z^a = multiplication by z_a and
Zbar_b = -hbar d/dz_b, which gives [Z^a, Zbar_b] = +hbar delta_ab (checked), at sample values of hbar.
Operators are compared on all monomials of degree <= 2 (enough: every operator compared has differential
order <= 2) and, for (3), of degree <= 3. q(M) = (1/2) sum M^b_a (Z^a Zbar_b + Zbar_b Z^a), M[b][a] = M^b_a.
(1) [q(M), Z^g] = -hbar (M Z)^g and [q(M), Zbar_g] = +hbar (M^T Zbar)_g for all 16 matrix units and two
    Gaussian samples.
(2) [q(M), q(N)] = hbar q([M, N]) for sample pairs and 64 unit pairs E_ab, E_cd (a < 2 <= c) at one hbar; q is injective:
    the 16 operators q(E_ab) are linearly independent (their values on monomials of degree <= 1).
(3) q(M) = sum M^b_a Z^a Zbar_b - (hbar/2) tr M; for M = id, q(id) = sum Z^a Zbar_a - 2 hbar.
"""
from fractions import Fraction as F
from itertools import product

import GA

QI = GA.QI
Z0, ONE = QI(0), QI(1)
HBARS = [QI(1), QI(F(2, 3))]
MM = [[QI(1), QI(0, 2), QI(0), QI(-1)], [QI(2), QI(1, 1), QI(0, -1), QI(0)],
      [QI(0), QI(3), QI(1), QI(1, 2)], [QI(1, -1), QI(0), QI(2), QI(0, 1)]]
NN = [[QI(0), QI(1), QI(1, 1), QI(0)], [QI(0, 1), QI(2), QI(0), QI(3)],
      [QI(1), QI(0, -2), QI(1, -1), QI(0)], [QI(0), QI(1), QI(0), QI(2, 1)]]


def monos(maxdeg):
    return [e for e in product(range(maxdeg + 1), repeat=4) if sum(e) <= maxdeg]


def padd(f, g, c=ONE):
    out = dict(f)
    for k, v in g.items():
        out[k] = out.get(k, Z0) + c * v
    return {k: v for k, v in out.items() if v}


def pscal(c, f):
    return {k: c * v for k, v in f.items() if c * v}


def opZ(a, f):
    out = {}
    for e, c in f.items():
        e2 = list(e)
        e2[a] += 1
        out[tuple(e2)] = out.get(tuple(e2), Z0) + c
    return out


def opZbar(b, f, hbar):
    out = {}
    for e, c in f.items():
        if e[b]:
            e2 = list(e)
            e2[b] -= 1
            out[tuple(e2)] = out.get(tuple(e2), Z0) - hbar * QI(e[b]) * c
    return {k: v for k, v in out.items() if v}


def opq(M, f, hbar):
    out = {}
    for a in range(4):
        for b in range(4):
            if M[b][a]:
                t = padd(opZ(a, opZbar(b, f, hbar)), opZbar(b, opZ(a, f), hbar))
                out = padd(out, t, M[b][a] * QI(F(1, 2)))
    return out


def mat_comm(A, B):
    return [[sum((A[i][k] * B[k][j] - B[i][k] * A[k][j] for k in range(4)), Z0) for j in range(4)]
            for i in range(4)]


UNITS = [[[ONE if (i, j) == (a, b) else Z0 for j in range(4)] for i in range(4)] for a in range(4) for b in range(4)]
# sample inputs of check_lie_homomorphism_and_injective
SAMPLE_PAIRS = ((MM, NN), (NN, MM), (MM, UNITS[6]))   # Gaussian pairs and one Gaussian/unit pair
UNITS_LOW, UNITS_HIGH = UNITS[:8], UNITS[8:]          # E_ab with a < 2 and E_cd with c >= 2: 64 unit pairs
HBAR_UNITS = HBARS[0]                                 # the one hbar used for the unit pairs and injectivity
DEG_SAMPLE = 2   # monomial degree bound for the sample pairs (every operator compared has order <= 2)
DEG_UNIT = 1     # degree bound for the unit pairs and injectivity (q(M) and [q(M), q(N)] have order <= 1)


def check_adjoint_action_on_generators():
    for hbar in HBARS:
        for M in UNITS + [MM, NN]:
            for g in range(4):
                for e in monos(2):
                    f = {e: ONE}
                    lhs = padd(opq(M, opZ(g, f), hbar), opZ(g, opq(M, f, hbar)), QI(-1))
                    rhs = {}
                    for a in range(4):
                        if M[g][a]:
                            rhs = padd(rhs, opZ(a, f), -hbar * M[g][a])
                    assert lhs == rhs
                    lhs2 = padd(opq(M, opZbar(g, f, hbar), hbar), opZbar(g, opq(M, f, hbar), hbar), QI(-1))
                    rhs2 = {}
                    for b in range(4):
                        if M[b][g]:
                            rhs2 = padd(rhs2, opZbar(b, f, hbar), hbar * M[b][g])
                    assert lhs2 == rhs2
    # the realisation has the palatial sign
    for e in monos(2):
        f = {e: ONE}
        for a in range(4):
            for b in range(4):
                c = padd(opZ(a, opZbar(b, f, HBARS[1])), opZbar(b, opZ(a, f), HBARS[1]), QI(-1))
                assert c == (pscal(HBARS[1], f) if a == b else {})
    return True


def check_lie_homomorphism_and_injective():
    for hbar in HBARS:
        for (M, N) in SAMPLE_PAIRS:
            for e in monos(DEG_SAMPLE):
                f = {e: ONE}
                lhs = padd(opq(M, opq(N, f, hbar), hbar), opq(N, opq(M, f, hbar), hbar), QI(-1))
                assert lhs == pscal(hbar, opq(mat_comm(M, N), f, hbar))
    hbar = HBAR_UNITS
    for M in UNITS_LOW:
        for N in UNITS_HIGH:
            for e in monos(DEG_UNIT):
                f = {e: ONE}
                lhs = padd(opq(M, opq(N, f, hbar), hbar), opq(N, opq(M, f, hbar), hbar), QI(-1))
                assert lhs == pscal(hbar, opq(mat_comm(M, N), f, hbar))
    keys = monos(DEG_UNIT)       # q(M) preserves degree, so the images stay in degree <= DEG_UNIT
    rows = []
    for M in UNITS:
        vals = []
        for e in keys:
            img = opq(M, {e: ONE}, hbar)
            assert set(img) <= set(keys)      # no coordinate of the image is dropped
            vals += [img.get(k, Z0) for k in keys]
        rows.append(vals)
    assert GA.field_rank(rows) == 16
    return True


def check_symmetric_minus_normal_is_half_trace():
    for hbar in HBARS:
        for M in UNITS + [MM, NN, [[ONE if i == j else Z0 for j in range(4)] for i in range(4)]]:
            tr = sum((M[i][i] for i in range(4)), Z0)
            for e in monos(3):
                f = {e: ONE}
                normal = {}
                for a in range(4):
                    for b in range(4):
                        if M[b][a]:
                            normal = padd(normal, opZ(a, opZbar(b, f, hbar)), M[b][a])
                assert opq(M, f, hbar) == padd(normal, f, -hbar * tr * QI(F(1, 2)))
        ID = [[ONE if i == j else Z0 for j in range(4)] for i in range(4)]
        for e in monos(3):
            f = {e: ONE}
            normal = {}
            for a in range(4):
                normal = padd(normal, opZ(a, opZbar(a, f, hbar)))
            assert padd(opq(ID, f, hbar), normal, QI(-1)) == pscal(-2 * hbar, f)
    return True


EXPORTS = {"opZ": opZ, "opZbar": opZbar, "opq": opq, "padd": padd, "pscal": pscal, "monos": monos}
