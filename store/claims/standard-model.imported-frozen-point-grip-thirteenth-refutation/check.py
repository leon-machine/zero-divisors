"""standard-model.imported-frozen-point-grip-thirteenth-refutation: exact checks.

(1) Frozen point, in Cl(2,4) (e0 (+1), e1..e3 (-1), e+ (+1), e- (-1), n0 = (e+ + e-)/2, ninf = e+ - e-):
    the fibre is R^(1,3) + H_1, H_1 = span(ninf, n0) a hyperbolic plane (signature (1,1)), total (2,4).
    On a vacuum Einstein field (P = (Lambda/6) id, J = trace P = 2 Lambda/3) the section (1, 0, rho_I),
    rho_I = J/4, is parallel for the tractor gauge field, Q(I) = 2J/4 = Lambda/3, and at Lambda = 0 it is
    the null ninf.
(2) Two conformal spinors, components Z = (omega^0, omega^1, pi_0', pi_1') in Gaussian rationals (the
    complex unit is I6): p_AA' = sum pi_A conj(pi_A') has p.p = eps^AB eps^A'B' p_AA' p_BB' = 2 det p
    = 2 |<pi^1 pi^2>|^2; one spinor is null, aligned spinors give a null composite.
(3) Exact join: the grip P = M(I) from its definition <P, U> = M_{U ^ I}, M_A = i sum conj(Z).A Z (the
    chart matrices of the conformal model, as in synthesis.many-twistor-join), with the ambient Gram
    matrix inverted exactly, has Q(P) = 2 |B_Lambda|^2 + (Lambda/3) C, B_Lambda = <pi^1 pi^2>
    + (Lambda/6)[omega^1 omega^2], C = tr h^2/2 - (tr h)^2/4 for the Gram matrix h; at Lambda = 0 this is
    2 |<pi^1 pi^2>|^2, and the doubled composite has B = 0 and m^2 = (Lambda/3)(conj(Z).Z)^2.
(4) The thirteenth refutation's magnitudes (orders of ten, PDG 2024 inputs as exact rationals):
    H = hbar H_0 is 1e-33 eV and H^2/M_P is 1e-94 eV, that is 1e-44 and 1e-105 of the weak scale 1e11 eV.
The families paper's direction and residue clauses (2)-(4) are structural and are not computed.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
QI = GA.QI
I = GA.QI_I
EPS = [[0, 1], [-1, 0]]


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def dot(a, b):
    return GA.dot(a, b, S)


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def q(re, im=0):
    return QI(F(re), F(im))


def abs2(z):
    return z.re * z.re + z.im * z.im


def br(u, w):
    return u[0] * w[1] - u[1] * w[0]


def herm(Z, W):
    """conj(Z).W = conj(pi_Z).omega_W + conj(omega_Z).pi_W."""
    return sum((Z[2 + a].conj() * W[a] + Z[a].conj() * W[2 + a] for a in range(2)), q(0))


def matvec(A, Z):
    return [sum((q(A[r][c]) * Z[c] for c in range(4)), q(0)) for r in range(4)]


def moment(A, Zs):
    return I * sum((herm(Z, matvec(A, Z)) for Z in Zs), q(0))


def A_grading():
    h = F(1, 2)
    return [[-h, 0, 0, 0], [0, -h, 0, 0], [0, 0, h, 0], [0, 0, 0, h]]


def A_trans(x):
    A = [[0] * 4 for _ in range(4)]
    for a in range(2):
        for bp in range(2):
            A[a][2 + bp] = sum(x[a][ap] * EPS[ap][bp] for ap in range(2))
    return A


def A_spec(x):
    A = [[0] * 4 for _ in range(4)]
    for ap in range(2):
        for a in range(2):
            A[2 + ap][a] = -sum(x[b][ap] * EPS[b][a] for b in range(2))
    return A


XS = [(a, ap) for a in range(2) for ap in range(2)]


def unit_x(a, ap):
    x = [[0, 0], [0, 0]]
    x[a][ap] = 1
    return x


def gram_inverse():
    G = [[q(0)] * 6 for _ in range(6)]
    G[0][1] = G[1][0] = q(1)
    for r, (a, ap) in enumerate(XS):
        for s, (b, bp) in enumerate(XS):
            G[2 + r][2 + s] = q(-EPS[a][b] * EPS[ap][bp])
    cols = [GA.field_solve(G, [q(1) if r == c else q(0) for r in range(6)]) for c in range(6)]
    return [[cols[c][r] for c in range(6)] for r in range(6)]


GI = gram_inverse()


def grip_square(Zs, lam):
    """Q(P) from <P, U_j> = M_{U_j ^ I}, I = ninf + lam n0."""
    d = moment(A_grading(), Zs)
    v = [lam * d, -d]
    for (a, ap) in XS:
        x = unit_x(a, ap)
        v.append(moment(A_trans(x), Zs) + lam * moment(A_spec(x), Zs))
    return sum((GI[r][s] * v[r] * v[s] for r in range(6) for s in range(6)), q(0))


def casimir(Zs):
    h = [[herm(Zi, Zl) for Zl in Zs] for Zi in Zs]
    n = len(h)
    t1 = sum((h[i][k] * h[k][i] for i in range(n) for k in range(n)), q(0))
    t0 = sum((h[i][i] for i in range(n)), q(0))
    return t1 * F(1, 2) - t0 * t0 * F(1, 4)


PAIRS = [([q(1, 2), q(0, 1), q(F(1, 2)), q(-1, 1)], [q(0, -1), q(3), q(2, 1), q(F(1, 3), -2)]),
         ([q(2), q(-1, 1), q(0, 3), q(1)], [q(1, 1), q(0), q(-2, 1), q(F(1, 2), F(1, 2))]),
         ([q(0), q(1), q(1, -1), q(2, 2)], [q(3, 1), q(-1), q(0, 1), q(1)])]
LAMS = (F(0), F(3, 5), F(-6, 7), F(2))
H0 = F("67.4")                    # km/s/Mpc
MPC_KM = F("3.08567758149e19")    # km
HBAR_EV = F("6.582119569e-16")    # eV s
M_P_EV = F("1.220890e28")         # eV


def check_frozen_point_in_its_own_scale():
    premise("mass.imported-frozen-point-tractor-connection")
    basis = [NI, N0, E[0], E[1], E[2], E[3]]
    gram = lambda bs: GA.congruence_signature([[dot(u, v) for v in bs] for u in bs])
    ok = gram(basis[:2]) == (1, 1, 0) and gram(basis[2:]) == (1, 3, 0) and gram(basis) == (2, 4, 0)
    for lam in LAMS:
        pe = lambda A: GA.scal(lam / 6, A)
        J = sum(dot(ER[m], pe(E[m])) for m in range(4))
        ok = ok and J == 2 * lam / 3
        rho_I = J / 4
        Isec = GA.add(NI, GA.scal(rho_I, N0))
        for m in range(4):
            th = GA.add(GA.neg(comm(NI, E[m])), comm(N0, pe(E[m])))
            ok = ok and GA.is_zero(comm(th, Isec))
        ok = ok and dot(Isec, Isec) == lam / 3 == 2 * J / 4
        ok = ok and (dot(Isec, Isec) == 0) == (lam == 0)
    GA.check("frozen point (1, 0, J/4) is parallel with Q(I) = Lambda/3, null ninf at Lambda = 0", ok)
    assert ok


def check_two_spinor_mass_is_symplectic_area():
    premise("mass.mass-symplectic-area-two-twistor-formula")
    ok = True
    for Z1, Z2 in PAIRS:
        pis = [Z1[2:], Z2[2:]]
        for group, massless in (([pis[0]], True), (pis, False), ([pis[0], [I * 2 * c for c in pis[0]]], True)):
            p = [[sum((pi[A] * pi[Ap].conj() for pi in group), q(0)) for Ap in range(2)] for A in range(2)]
            pp = sum((q(EPS[A][B] * EPS[Ap][Bp]) * p[A][Ap] * p[B][Bp]
                      for A in range(2) for B in range(2) for Ap in range(2) for Bp in range(2)), q(0))
            det = p[0][0] * p[1][1] - p[0][1] * p[1][0]
            ok = ok and pp == 2 * det
            if len(group) == 2:
                ok = ok and pp == q(2 * abs2(br(group[0], group[1])))
            ok = ok and ((pp == q(0)) == massless)
    GA.check("two conformal spinors: p.p = 2 det p = 2 |<pi1 pi2>|^2, one spinor or aligned ones null", ok)
    assert ok


def check_exact_join_grip_mass():
    premise("mass.exact-join")
    ok = True
    for Z1, Z2 in PAIRS:
        for Lam in LAMS:
            lam = Lam / 6
            B = br(Z1[2:], Z2[2:]) + lam * br(Z1[:2], Z2[:2])
            rhs = q(2 * abs2(B)) + (Lam / 3) * casimir([Z1, Z2])
            ok = ok and grip_square([Z1, Z2], lam) == rhs
            if Lam == 0:
                ok = ok and grip_square([Z1, Z2], lam) == q(2 * abs2(br(Z1[2:], Z2[2:])))
            # doubled composite: B = 0 and m^2 = (Lambda/3)(conj(Z).Z)^2
            a = herm(Z1, Z1)
            ok = ok and grip_square([Z1, Z1], lam) == (Lam / 3) * a * a
    GA.check("exact join: Q(M(I)) = 2|B_Lambda|^2 + (Lambda/3) C from the moment-map definition", ok)
    assert ok


def order_of_ten(x, k):
    """x rounds to 10^k on a log scale: 10^(2k-1) <= x^2 < 10^(2k+1)."""
    lo = F(10) ** (2 * k - 1)
    hi = F(10) ** (2 * k + 1)
    return lo <= x * x < hi


def check_thirteenth_refutation_magnitudes():
    premise("families.alignment-computed-thirteenth-refutation-democracy-one")
    H = HBAR_EV * H0 / MPC_KM                     # eV
    small = H * H / M_P_EV
    weak = F(10) ** 11
    ok = order_of_ten(H, -33) and order_of_ten(small, -94)
    ok = ok and order_of_ten(H / weak, -44) and order_of_ten(small / weak, -105)
    ok = ok and not order_of_ten(H, -32) and not order_of_ten(small, -95)
    GA.check("Lambda Omega_vac lies between 1e-94 and 1e-33 eV: 1e-105 to 1e-44 of the weak scale", ok)
    assert ok
