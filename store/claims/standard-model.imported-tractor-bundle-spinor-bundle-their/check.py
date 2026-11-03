"""standard-model.imported-tractor-bundle-spinor-bundle-their: exact checks in Cl(2,4).

Conventions: e0 (+1), e1..e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-; tractors
sigma ninf + mu + rho n0; conformal spinors CS = Cl^+(2,4) P with complex unit I6 (built in, and
exported by, the check of correspondence.imported-tractor-connection-local-twistor-transport).
  (1) Tractor fibre: ninf, e0..e3, n0 are a basis (rank 6) with Gram signature (2,4); each of the 15
      bivectors acts skew-adjointly ((B x u).v + u.(B x v) = 0 on all basis pairs), the commutator of two
      bivectors is a bivector, so the structure algebra is so(2,4) of dimension 15; the tractor gauge
      field Omega_T(a) is such a bivector.
  (2) Spinor bundle: CS has real dimension 8, rank 4 over I6; rho(B) = B/2 maps CS to CS, commutes with
      I6, is injective on the 15 bivectors (operator rank 15), is a Lie map, [rho(B), rho(C)] = rho(B x C),
      and is the spin lift of the tractor action, rho(B)(v psi) - v rho(B) psi = (B x v) psi; the odd
      elements (vectors) carry CS out of itself and the even ones keep it.
  (3) Dependence on the conformal class only: a change of scale is a gauge transformation of the same
      shape. With U = 1 - n0 Y/2 (Y the gradient of the log of the conformal factor, an affine field),
      U Omega_T(a) U~ - 2 (a.grad U) U~ = Omega(a) + A ^ Y - ninf ^ A + (Y.A) ninf ^ n0
      + n0 ^ (P(A) + D_A Y - (Y.A) Y + Q(Y) A/2), D_A Y = a.grad Y + Omega(a) x Y, the ninf ^ n0 term being
      the dilation of the weight-one slot; for hb = 1, Omega = 0 the new Schouten map is symmetric when Y
      is a gradient and not otherwise.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
BIV = [(i, j) for i in range(6) for j in range(i + 1, 6)]
BLADES = GA.all_blades(6)


def mul(*xs):
    r = GA.sc(1)
    for x in xs:
        r = GA.mul(r, x, S)
    return r


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def dot(a, b):
    return GA.dot(a, b, S)


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def linmap(M):
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), E[n])
                              for n in range(4)])

def symmap(M):
    """A -> sum_n (sum_m M[m][n] A.e^m) e^n: for symmetric M a metric-symmetric map (P(e_m).e_n = M[m][n])."""
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), ER[n])
                              for n in range(4)])


HINV = [[2, 1, 0, 0], [0, 1, 0, -1], [1, 0, 3, 0], [0, 0, 1, 1]]
PSYM = [[2, 1, 0, -3], [1, -1, 4, 0], [0, 4, 5, 2], [-3, 0, 2, 7]]
OMEGA = [mul(E[0], E[1]), GA.add(mul(E[1], E[2]), mul(E[0], E[3])), mul(E[2], E[3]), mul(E[0], E[2])]
DIRS = ([1, 0, 0, 0], [0, 1, 2, 0], [3, 1, -2, 5])
Y0 = [1, 2, 0, -1]                                  # Y at the point
HESS = [[1, 2, 0, 0], [2, -1, 1, 0], [0, 1, 3, 1], [0, 0, 1, 2]]   # a.grad Y = HESS a (symmetric)
CURL = [[0, 1, 0, 0], [-1, 0, 0, 2], [0, 0, 0, 0], [0, -2, 0, 0]]  # antisymmetric part: not a gradient


def omega_of(av):
    return GA.add(*[GA.scal(dot(av, ER[m]), OMEGA[m]) for m in range(4)])


def check_tractor_fibre_metric_and_structure_algebra():
    premise("interior.imported-tractor-connection")
    basis = [NI, E[0], E[1], E[2], E[3], N0]
    ok = GA.rank_of_vectors([GA.basis_vector_of(v, BLADES) for v in basis]) == 6
    ok = ok and GA.congruence_signature([[dot(u, v) for v in basis] for u in basis]) == (2, 4, 0)
    bivs = [{b: F(1)} for b in BIV]
    ok = ok and len(bivs) == 15
    for B in bivs:
        for u in basis:
            for v in basis:
                ok = ok and dot(comm(B, u), v) + dot(u, comm(B, v)) == 0
        for C in bivs:
            ok = ok and all(len(b) == 2 for b in comm(B, C))
    hinv, P = linmap(HINV), symmap(PSYM)
    for a in DIRS:
        A = hinv(vec(a))
        om = GA.add(omega_of(vec(a)), GA.neg(comm(NI, A)), comm(N0, P(A)))
        ok = ok and om and all(len(b) == 2 for b in om)
    GA.check("tractor fibre: rank 6, signature (2,4), structure algebra the 15 bivectors so(2,4)", ok)
    assert ok


# sample inputs of check_spinor_bundle_and_induced_spin_connection
BIVS = [{b: F(1)} for b in BIV]              # the 15 basis bivectors e_i e_j, i < j
LIE_B, LIE_C = BIVS[::2], BIVS[1::3]         # sample pairs (B, C) for the Lie-map identity
SPIN_B = BIVS[::4]                           # sample bivectors for the spin-lift identity
SPIN_V = (E[1], N0, NI)                      # sample vectors (spacelike and the two null ones)
PSI_SAMPLE, PSI_ODD = slice(0, 3), slice(0, 2)   # the spinors of CS used in the sampled identities
ODD_EL, EVEN_EL = E[0], mul(E[0], E[4])      # a sample odd (vector) and even element


def check_spinor_bundle_and_induced_spin_connection():
    premise("correspondence.local-twistor-transport-ascended-spinor-connection")
    X = premise("correspondence.imported-tractor-connection-local-twistor-transport")
    CS, I6, rank, in_span, rho = X["CS"], X["I6"], X["rank"], X["in_span"], X["rho"]
    ok = len(CS) == 8 and rank(CS + [mul(I6, p) for p in CS]) == 8
    bivs = BIVS
    ops = []
    for B in bivs:
        row = []
        for p in CS:
            img = rho(B, p)
            ok = ok and in_span(img, CS) and GA.eq(mul(I6, img), rho(B, mul(I6, p)))
            row += GA.basis_vector_of(img, BLADES)
        ops.append(row)
    ok = ok and GA.rank_of_vectors(ops) == 15
    for B in LIE_B:
        for C in LIE_C:
            for p in CS[PSI_SAMPLE]:
                lhs = GA.sub(rho(B, rho(C, p)), rho(C, rho(B, p)))
                ok = ok and GA.eq(lhs, rho(comm(B, C), p))
    for B in SPIN_B:
        for v in SPIN_V:
            for p in CS[PSI_SAMPLE]:
                ok = ok and GA.eq(GA.sub(rho(B, mul(v, p)), mul(v, rho(B, p))), mul(comm(B, v), p))
    ok = ok and all(not in_span(mul(ODD_EL, p), CS) for p in CS[PSI_ODD])
    ok = ok and all(in_span(mul(EVEN_EL, p), CS) for p in CS)
    GA.check("spinor bundle: CS of rank 4 over I6, rho(B) = B/2 a faithful Lie map lifting the tractor action", ok)
    assert ok


def gauge_transform(a, hy, omega_on):
    """Both sides of the change-of-scale identity at the point: Y(x0) = Y0, (e_m.grad Y).e_n = hy[m][n]
    (symmetric exactly when Y is a gradient)."""
    av = vec(a)
    A = linmap(HINV)(av) if omega_on else av
    P = symmap(PSYM)
    om = omega_of(av) if omega_on else {}
    Y = vec(Y0)
    dY = GA.add(*[GA.scal(sum(F(hy[m][n]) * dot(av, ER[m]) for m in range(4)), ER[n])
                  for n in range(4)])                                 # a.grad Y: (e_m.grad Y).e_n = hy[m][n]
    omT = GA.add(om, GA.neg(comm(NI, A)), comm(N0, P(A)))
    U = GA.sub(GA.sc(1), GA.scal(F(1, 2), mul(N0, Y)))
    dU = GA.scal(F(-1, 2), mul(N0, dY))
    lhs = GA.sub(mul(U, omT, GA.reverse(U)), GA.scal(2, mul(dU, GA.reverse(U))))
    DY = GA.add(dY, comm(om, Y))
    Phat = GA.add(P(A), DY, GA.scal(-dot(Y, A), Y), GA.scal(dot(Y, Y) / 2, A))
    rhs = GA.add(om, comm(A, Y), GA.neg(comm(NI, A)), GA.scal(dot(Y, A), comm(NI, N0)), comm(N0, Phat))
    return lhs, rhs, Phat


def check_change_of_scale_is_tractor_gauge_transformation():
    premise("interior.imported-tractor-connection")
    ok = True
    for a in DIRS + ([0, 0, 1, 0],):
        for hy in (HESS, [[HESS[i][j] + CURL[i][j] for j in range(4)] for i in range(4)]):
            lhs, rhs, _ = gauge_transform(a, hy, True)
            ok = ok and GA.eq(lhs, rhs)
    # symmetry of the new Schouten map (hb = 1, Omega = 0): gradient Y yes, curl part no
    for hy, sym in ((HESS, True), ([[HESS[i][j] + CURL[i][j] for j in range(4)] for i in range(4)], False)):
        ph = [gauge_transform([1 if k == m else 0 for k in range(4)], hy, False)[2] for m in range(4)]
        symmetric = all(dot(ph[m], E[n]) == dot(E[m], ph[n]) for m in range(4) for n in range(4))
        ok = ok and symmetric == sym
    # by hand: a = e0, hb = 1, Omega = 0, Y = e0 + 2 e1 - e3: Y.A = 1, so the dilation term is
    # ninf ^ n0 = e+ e- (coefficient 1), and the Lorentz part A ^ Y = 2 e0e1 - e0e3
    lhs, _, _ = gauge_transform([1, 0, 0, 0], HESS, False)
    ok = ok and lhs.get((4, 5)) == 1 and lhs.get((0, 1)) == 2 and lhs.get((0, 3)) == -1
    GA.check("change of scale is a tractor gauge transformation of the same shape (conformal invariance)", ok)
    assert ok
