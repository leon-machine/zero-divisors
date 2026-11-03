"""interior.sign-fixed-internally: exact checks in Cl(2,4).

Conventions: e0 (+1), e1..e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-; tractors
sigma ninf + mu + rho n0. The store's curvature sign: de Sitter has R(B) = (Lambda/3) B; its Ricci map
and Schouten map are computed by contraction (R(a) = Lambda a, P = (Lambda/6) id). The Schouten term of
the tractor gauge field is taken with either sign s: Theta_s(A) = -ninf ^ A + s n0 ^ P(A).
  (1) s = +1 (the displayed sign): the parallel scale tractor ninf + rho n0 has rho = Lambda/6, so for
      Lambda > 0, Q(I) = Lambda/3 > 0; I^perp has signature (1,4), the stabiliser bivectors span a
      10-dimensional algebra with trace form of signature (4,6) (so(1,4)), and the flat-model section
      Y = X/(X.I) - I/Q(I) (X the null lifts n0 + x - Q(x) ninf/2) has Q(Y) = -3/Lambda < 0 with
      Lorentzian tangent space {I, Y}^perp of signature (1,3): de Sitter space.
  (2) s = -1: rho = -Lambda/6, Q(I) = -Lambda/3 < 0, I^perp of signature (2,3), trace form (6,4)
      (so(2,3)), Q(Y) = 3/Lambda > 0: anti-de Sitter space, contradicting the naming Ric = Lambda g.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
VB = [(i,) for i in range(6)]
BIV = [(i, j) for i in range(6) for j in range(i + 1, 6)]


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


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def perp(vs):
    """Basis of the orthogonal complement of the vectors vs in R^(2,4)."""
    M = [[dot(E[i], v) for i in range(6)] for v in vs]
    return [GA.add(*[GA.scal(k[i], E[i]) for i in range(6) if k[i]]) for k in GA.field_kernel(M)]


def signature(basis):
    return GA.congruence_signature([[dot(u, v) for v in basis] for u in basis])


def stabiliser(I):
    """Basis of the bivectors B with B x I = 0, and the signature of the trace form <B B'>_0 on it."""
    bl = [{b: F(1)} for b in BIV]
    cols = [GA.basis_vector_of(comm(B, I), VB) for B in bl]
    M = [[cols[j][r] for j in range(15)] for r in range(6)]
    ker = [GA.add(*[GA.scal(k[j], bl[j]) for j in range(15) if k[j]]) for k in GA.field_kernel(M)]
    form = GA.congruence_signature([[mul(B, C).get((), F(0)) for C in ker] for B in ker])
    return ker, form


def de_sitter_R(lam):
    return lambda B: GA.scal(lam / 3, B)


def ricci(R, b):
    return GA.add(*[grade(comm(ER[m], R(comm(E[m], b))), 1) for m in range(4)])


def schouten(R):
    sc = sum(dot(ER[m], ricci(R, E[m])) for m in range(4))
    return lambda A: GA.scal(F(1, 2), GA.sub(ricci(R, A), GA.scal(sc / 6, A)))


def lift(x):
    X = vec(x)
    return GA.add(N0, X, GA.scal(-dot(X, X) / 2, NI))


LAMS = (F(3, 4), F(2), F(9, 5))
POINTS = ([0, 0, 0, 0], [1, 2, 0, -1], [F(1, 2), 0, 3, 1], [0, -1, 1, 1])


def parallel_rho(lam, s):
    """The rho for which ninf + rho n0 is parallel under Theta_s, read off the e0 component, and a test."""
    R = de_sitter_R(lam)
    P = schouten(R)
    ok = all(GA.eq(ricci(R, E[m]), GA.scal(lam, E[m])) for m in range(4))
    # Theta_s(e0) x ninf = 0 and Theta_s(e0) x n0 = e0 - ... : rho from the e0 component
    th = lambda A: GA.add(GA.neg(comm(NI, A)), GA.scal(s, comm(N0, P(A))))
    c_inf = dot(comm(th(E[0]), NI), E[0])
    c_0 = dot(comm(th(E[0]), N0), E[0])
    rho = -c_inf / c_0
    I = GA.add(NI, GA.scal(rho, N0))
    ok = ok and all(GA.is_zero(comm(th(E[m]), I)) for m in range(4))
    return rho, I, ok


def section_data(I):
    qi = dot(I, I)
    out = []
    for x in POINTS:
        X = lift(x)
        Y = GA.sub(GA.scal(1 / dot(X, I), X), GA.scal(1 / qi, I))
        out.append((dot(X, X), dot(Y, I), dot(Y, Y), signature(perp([I, Y]))))
    return out


def check_displayed_sign_attaches_de_sitter():
    premise("interior.scale-tractor-leaves-cone")
    premise("interior.non-null-stabilisers-section-they-act")
    ok = True
    for lam in LAMS:
        rho, I, good = parallel_rho(lam, 1)
        ok = ok and good and rho == lam / 6 and dot(I, I) == lam / 3 and dot(I, I) > 0
        ok = ok and signature(perp([I])) == (1, 4, 0)
        ker, form = stabiliser(I)
        ok = ok and len(ker) == 10 and form == (4, 6, 0)
        for qX, yI, qY, tsig in section_data(I):
            ok = ok and qX == 0 and yI == 0 and qY == -3 / lam and tsig == (1, 3, 0)
    # by hand at Lambda = 3/4: rho = 1/8, Q(I) = 1/4, de Sitter radius l^2 = 4
    rho, I, _ = parallel_rho(F(3, 4), 1)
    ok = ok and rho == F(1, 8) and dot(I, I) == F(1, 4) and section_data(I)[1][2] == -4
    GA.check("displayed Schouten sign: Lambda > 0 gives Q(I) = Lambda/3 > 0 and the de Sitter section", ok)
    assert ok


def check_opposite_sign_attaches_anti_de_sitter():
    premise("interior.scale-tractor-leaves-cone")
    premise("interior.non-null-stabilisers-section-they-act")
    ok = True
    for lam in LAMS:
        rho, I, good = parallel_rho(lam, -1)
        ok = ok and good and rho == -lam / 6 and dot(I, I) == -lam / 3 and dot(I, I) < 0
        ok = ok and signature(perp([I])) == (2, 3, 0)
        ker, form = stabiliser(I)
        ok = ok and len(ker) == 10 and form == (6, 4, 0)
        for qX, yI, qY, tsig in section_data(I):
            ok = ok and qX == 0 and yI == 0 and qY == 3 / lam and tsig == (1, 3, 0)
    GA.check("opposite Schouten sign: Lambda > 0 would give Q(I) < 0 and the anti-de Sitter section", ok)
    assert ok
