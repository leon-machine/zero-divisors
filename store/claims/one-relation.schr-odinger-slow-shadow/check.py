"""one-relation.schr-odinger-slow-shadow: exact checks of the computable steps.

Cl(1,3) in GA.py (signature (+,-,-,-)), gamma^mu = eta^{mu mu} gamma_mu; I sigma_3 = gamma_2 gamma_1.
(1) The operator: for six rational rotors R^-1 gamma^mu R = M^mu_nu gamma^nu with M a Lorentz matrix
    (M eta M^T = eta), so nabla = gamma^mu d_mu is covariant (its uniqueness is the premise lemma).
(2) The Klein-Gordon square: (I sigma_3)^-1 = -I sigma_3, gamma_0 (I sigma_3) gamma_0 = I sigma_3,
    {gamma^mu, gamma^nu} = 2 eta^{mu nu}; the law nabla psi = m psi C has C = -gamma_0 I sigma_3 =
    gamma_0 gamma_1 gamma_2 with C^2 = -1. On plane waves psi = psi_0 exp(-I sigma_3 p.x) the
    Dirac-Hestenes equation reduces to p psi_0 = m psi_0 gamma_0 (psi_0 even); its solution space,
    computed as a kernel on the 8 even components, has dimension 4 on the mass shell p^2 = m^2 and 0 off
    it, at sample momenta: every solution is a Klein-Gordon field of mass m.
(3) The imaginary unit: (gamma_0 gamma_1)^2 = +1 (the boost plane is not a complex structure),
    (I sigma_3)^2 = -1, it commutes with gamma_0 and anticommutes with gamma_1, gamma_2; C (I sigma_3) =
    gamma_0. For rotors R of the (gamma_0, gamma_1, gamma_2) space (two boosts and a boost times a
    rotation; a pure g1g2 rotation fixes I sigma_3), R commutes with C, J' = R (I sigma_3) R~ is even with J'^2 = -1 and commutes with C, and C J' = R gamma_0 R~ is a
    different unit timelike vector orthogonal to gamma_3; conversely J = -C t for such a t recovers J'.
    A rest-space rotation (5/13 + 12/13 g1g3) carries I sigma_3 to another bivector squaring to -1 and
    commuting with gamma_0.
(4) The Pauli identity a b = a.b + I_3 (a x b) in Cl(3,0) with I_3^2 = -1, on all nine basis pairs (so
    for all vectors, by bilinearity) and on rational samples.
The level statements (sourced, half sourced, unsourced) and the imported descent are not computable.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
G = [GA.gen(i) for i in range(4)]
GUP = [GA.scal(F(SQ[i]), G[i]) for i in range(4)]
EVEN = [b for b in GA.all_blades(4) if len(b) % 2 == 0]
ISIG3 = GA.mul(G[2], G[1], SQ)
ROTORS = [(0, 1, F(5, 4), F(3, 4)), (0, 2, F(13, 12), F(5, 12)), (0, 3, F(17, 15), F(8, 15)),
          (1, 2, F(3, 5), F(4, 5)), (1, 3, F(5, 13), F(12, 13)), (2, 3, F(8, 17), F(15, 17))]
MASS = F(5)
ON_SHELL = [(5, 0, 0, 0), (13, 12, 0, 0), (7, 2, 4, 2), (-13, 0, 0, 12), (13, F(36, 5), F(48, 5), 0)]
OFF_SHELL = [(6, 0, 0, 0), (13, 11, 0, 0), (1, 2, 3, 4)]
PAULI_A = [[1, 2, 3], [0, -1, F(5, 2)], [7, 0, 0]]
PAULI_B = [[2, -1, 1], [F(1, 3), 4, -2], [0, 0, 1]]


def rotor(i, j, a, b):
    return GA.add(GA.sc(a), GA.scal(b, GA.mul(G[i], G[j], SQ)))


def m3(x, y, z):
    return GA.mul(GA.mul(x, y, SQ), z, SQ)


def check_vector_derivative_is_covariant():
    premise("one-relation.vector-derivative-covariant-first-order-operator")
    ok = True
    for i, j, a, b in ROTORS:
        R = rotor(i, j, a, b)
        Ri = GA.reverse(R)
        ok = ok and GA.eq(GA.mul(R, Ri, SQ), GA.sc(1))
        M = []
        for mu in range(4):
            y = m3(Ri, GUP[mu], R)
            ok = ok and all(len(bl) == 1 for bl in y)
            M.append([GA.dot(y, G[nu], SQ) for nu in range(4)])
        # M eta^{-1} M^T = eta^{-1} (eta = diag(1,-1,-1,-1) is its own inverse)
        ok = ok and all(sum(M[r][k] * SQ[k] * M[c][k] for k in range(4)) == (SQ[r] if r == c else 0)
                        for r in range(4) for c in range(4))
    R = rotor(*ROTORS[0])
    ok = ok and m3(GA.reverse(R), GUP[0], R) == {(0,): F(17, 8), (1,): F(15, 8)}
    _tp_rv = (ok); assert _tp_rv is not False, "check_vector_derivative_is_covariant"; return _tp_rv


def check_klein_gordon_square():
    premise("one-relation.form-law-forced-square")
    ok = GA.eq(GA.mul(ISIG3, GA.neg(ISIG3), SQ), GA.sc(1))
    ok = ok and GA.eq(m3(G[0], ISIG3, G[0]), ISIG3)
    ok = ok and all(GA.eq(GA.add(GA.mul(GUP[m], GUP[n], SQ), GA.mul(GUP[n], GUP[m], SQ)),
                          GA.sc(2 * SQ[m] if m == n else 0)) for m in range(4) for n in range(4))
    C = GA.neg(GA.mul(G[0], ISIG3, SQ))
    ok = ok and GA.eq(C, {(0, 1, 2): F(1)}) and GA.eq(GA.mul(C, C, SQ), GA.sc(-1))
    dims = []
    for p in ON_SHELL + OFF_SHELL:
        pv = GA.add(*[GA.scal(F(p[mu]) * SQ[mu], G[mu]) for mu in range(4)])   # p = p_mu gamma^mu
        cols = []
        for b in EVEN:
            x = {b: F(1)}
            r = GA.sub(GA.mul(pv, x, SQ), GA.scal(MASS, GA.mul(x, G[0], SQ)))
            cols.append([r.get(c, F(0)) for c in GA.all_blades(4)])
        ker = GA.field_kernel([list(rw) for rw in zip(*cols)])
        p2 = F(p[0]) ** 2 - sum(F(x) ** 2 for x in p[1:])
        ok = ok and (len(ker) > 0) == (p2 == MASS ** 2)
        for k in ker:
            psi = {b: c for b, c in zip(EVEN, k) if c}
            ok = ok and GA.eq(GA.mul(GA.mul(pv, pv, SQ), psi, SQ), GA.scal(MASS ** 2, psi))
        dims.append(len(ker))
    ok = ok and dims == [4, 4, 4, 4, 4, 0, 0, 0]
    _tp_rv = (ok); assert _tp_rv is not False, "check_klein_gordon_square"; return _tp_rv


def check_imaginary_unit_and_rest_frame_are_one_datum():
    premise("one-relation.one-datum-not-two-imaginary-unit")
    B01 = GA.mul(G[0], G[1], SQ)
    ok = GA.eq(GA.mul(B01, B01, SQ), GA.sc(1)) and GA.eq(GA.mul(ISIG3, ISIG3, SQ), GA.sc(-1))
    ok = ok and GA.commutes(ISIG3, G[0], SQ) and GA.anticommutes(ISIG3, G[1], SQ) and GA.anticommutes(ISIG3, G[2], SQ)
    C = GA.neg(GA.mul(G[0], ISIG3, SQ))
    ok = ok and GA.eq(GA.mul(C, ISIG3, SQ), G[0])
    # a rotation in the gamma_1 gamma_2 plane fixes I sigma_3 itself
    R12 = rotor(1, 2, F(3, 5), F(4, 5))
    ok = ok and GA.commutes(R12, C, SQ) and GA.eq(m3(R12, ISIG3, GA.reverse(R12)), ISIG3)
    for R in (rotor(0, 1, F(5, 4), F(3, 4)), rotor(0, 2, F(13, 12), F(5, 12)),
              GA.mul(rotor(0, 1, F(5, 4), F(3, 4)), R12, SQ)):
        Rr = GA.reverse(R)
        ok = ok and GA.commutes(R, C, SQ)
        Jp = m3(R, ISIG3, Rr)
        ok = ok and all(len(b) % 2 == 0 for b in Jp) and GA.eq(GA.mul(Jp, Jp, SQ), GA.sc(-1))
        ok = ok and GA.commutes(Jp, C, SQ)
        t = GA.mul(C, Jp, SQ)
        ok = ok and GA.eq(t, m3(R, G[0], Rr)) and all(len(b) == 1 for b in t)
        ok = ok and GA.dot(t, t, SQ) == 1 and GA.dot(t, G[3], SQ) == 0 and GA.dot(t, G[0], SQ) > 0
        ok = ok and not GA.eq(t, G[0])
        ok = ok and GA.eq(GA.neg(GA.mul(C, t, SQ)), Jp)
    R13 = rotor(1, 3, F(5, 13), F(12, 13))
    Jr = m3(GA.reverse(R13), ISIG3, R13)
    ok = ok and GA.eq(GA.mul(Jr, Jr, SQ), GA.sc(-1)) and GA.commutes(Jr, G[0], SQ) and not GA.eq(Jr, ISIG3)
    _tp_rv = (ok); assert _tp_rv is not False, "check_imaginary_unit_and_rest_frame_are_one_datum"; return _tp_rv


def check_pauli_identity():
    S3 = GA.sig(3, 0)
    I3 = GA.mul(GA.mul(GA.gen(0), GA.gen(1), S3), GA.gen(2), S3)
    ok = GA.eq(GA.mul(I3, I3, S3), GA.sc(-1))

    def vec(a):
        return GA.add(*[GA.scal(F(a[i]), GA.gen(i)) for i in range(3)])

    def cross(a, b):
        a, b = [F(x) for x in a], [F(x) for x in b]
        return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
    basis = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    pairs = list(product(basis, basis)) + list(product(PAULI_A, PAULI_B))
    for a, b in pairs:
        lhs = GA.mul(vec(a), vec(b), S3)
        rhs = GA.add(GA.sc(sum(F(x) * F(y) for x, y in zip(a, b))), GA.mul(I3, vec(cross(a, b)), S3))
        ok = ok and GA.eq(lhs, rhs)
    ok = ok and len(pairs) == 18
    ok = ok and GA.mul(GA.gen(0), GA.gen(1), S3) == GA.mul(I3, GA.gen(2), S3) == {(0, 1): F(1)}
    _tp_rv = (ok); assert _tp_rv is not False, "check_pauli_identity"; return _tp_rv
