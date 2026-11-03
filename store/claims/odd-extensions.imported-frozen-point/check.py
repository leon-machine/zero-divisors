"""odd-extensions.imported-frozen-point: exact checks in Cl(2,4).

Conventions: e0 (+1), e1..e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-; tractors
sigma ninf + mu + rho n0; the Einstein field has P = (Lambda/6) id, a sample hb (through hb^{-1}) and a
sample Omega; Theta(A) = -ninf ^ A + n0 ^ P(A), A = hb^{-1}(a).
  (1) For Lambda > 0 and Lambda < 0: I = ninf + (Lambda/6) n0 is parallel, Q(I) = Lambda/3, I^perp has
      signature (1,4) or (2,3), and the stabiliser is 10-dimensional with trace form (4,6) (so(1,4)) or
      (6,4) (so(2,3)).
  (2) The Stelle-West vector V = n0 - (3/Lambda) I lies in I^perp with Q(V) = -3/Lambda (Q(I) Q(V) = -1);
      {I, V}^perp has signature (1,3) on both branches and the bivectors fixing I and V form a
      6-dimensional algebra with trace form (3,3): the Lorentz algebra of {I, V}^perp.
  (3) For constant V, D^T_a V = Omega_T(a) x V = hb^{-1}(a): the covariant derivative is the soldering
      form. Omega(a) fixes I and V (the Lorentz part), and the translation part is
      Theta(A) = A ^ V/Q(V) = -A ^ V/l^2 (l^2 = 3/Lambda), so the reduced connection is
      Omega(a) - hb^{-1}(a) ^ V/l^2, with Theta(A) x Theta(B) = (Lambda/3) A ^ B.
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


def linmap(M):
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), E[n])
                              for n in range(4)])


def perp(vs):
    M = [[dot(E[i], v) for i in range(6)] for v in vs]
    return [GA.add(*[GA.scal(k[i], E[i]) for i in range(6) if k[i]]) for k in GA.field_kernel(M)]


def signature(basis):
    return GA.congruence_signature([[dot(u, v) for v in basis] for u in basis])


def stabiliser(vs):
    bl = [{b: F(1)} for b in BIV]
    M = []
    for v in vs:
        cols = [GA.basis_vector_of(comm(B, v), VB) for B in bl]
        M += [[cols[j][r] for j in range(15)] for r in range(6)]
    ker = [GA.add(*[GA.scal(k[j], bl[j]) for j in range(15) if k[j]]) for k in GA.field_kernel(M)]
    form = GA.congruence_signature([[mul(B, C).get((), F(0)) for C in ker] for B in ker])
    return ker, form


HINV = [[2, 1, 0, 0], [0, 1, 0, -1], [1, 0, 3, 0], [0, 0, 1, 1]]
OMEGA = [mul(E[0], E[1]), GA.add(mul(E[1], E[2]), mul(E[0], E[3])), mul(E[2], E[3]), mul(E[0], E[2])]
POS, NEG = (F(3, 4), F(2)), (F(-3, 2), F(-6, 7))
DIRS = ([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [3, 1, -2, 5])


def theta(A, lam):
    return GA.add(GA.neg(comm(NI, A)), comm(N0, GA.scal(lam / 6, A)))


def omega_of(av):
    return GA.add(*[GA.scal(dot(av, ER[m]), OMEGA[m]) for m in range(4)])


def check_frozen_point_norm_complement_stabiliser_both_signs():
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    for lams, sig5, form in ((POS, (1, 4, 0), (4, 6, 0)), (NEG, (2, 3, 0), (6, 4, 0))):
        for lam in lams:
            I = GA.add(NI, GA.scal(lam / 6, N0))
            ok = ok and all(GA.is_zero(comm(GA.add(omega_of(vec(a)), theta(linmap(HINV)(vec(a)), lam)), I))
                            for a in DIRS)
            ok = ok and dot(I, I) == lam / 3
            ok = ok and signature(perp([I])) == sig5
            ker, f = stabiliser([I])
            ok = ok and len(ker) == 10 and f == form
    GA.check("frozen point: Q(I) = Lambda/3, I^perp (1,4) or (2,3), stabiliser so(1,4) or so(2,3)", ok)
    assert ok


def check_stelle_west_vector_and_lorentz_stabiliser():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok = True
    for lam in POS + NEG:
        I = GA.add(NI, GA.scal(lam / 6, N0))
        V = GA.sub(N0, GA.scal(3 / lam, I))
        ok = ok and dot(V, I) == 0 and dot(V, V) == -3 / lam and dot(I, I) * dot(V, V) == -1
        ok = ok and signature(perp([I, V])) == (1, 3, 0)
        ker, f = stabiliser([I, V])
        ok = ok and len(ker) == 6 and f == (3, 3, 0)
    # by hand at Lambda = 3/4: V = n0 - 4 (ninf + n0/8) = n0/2 - 4 ninf, Q(V) = 2 (1/2)(-4) = -4
    I = GA.add(NI, GA.scal(F(1, 8), N0))
    ok = ok and GA.eq(GA.sub(N0, GA.scal(4, I)), GA.sub(GA.scal(F(1, 2), N0), GA.scal(4, NI)))
    ok = ok and dot(GA.sub(N0, GA.scal(4, I)), GA.sub(N0, GA.scal(4, I))) == -4
    GA.check("Stelle-West vector in I^perp with Q(V) = -3/Lambda; its stabiliser is the Lorentz algebra of (1,3)", ok)
    assert ok


def check_soldering_form_and_reduced_connection():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    hinv = linmap(HINV)
    ok = True
    for lam in POS + NEG:
        I = GA.add(NI, GA.scal(lam / 6, N0))
        V = GA.sub(N0, GA.scal(3 / lam, I))
        ell2 = 3 / lam
        for a in DIRS:
            av = vec(a)
            A = hinv(av)
            om = omega_of(av)
            full = GA.add(om, theta(A, lam))
            ok = ok and GA.eq(comm(full, V), A)                      # soldering form
            ok = ok and GA.is_zero(comm(om, I)) and GA.is_zero(comm(om, V))
            ok = ok and GA.eq(theta(A, lam), GA.scal(1 / dot(V, V), comm(A, V)))
            ok = ok and GA.eq(theta(A, lam), GA.scal(-1 / ell2, comm(A, V)))
            for b in DIRS:
                B = hinv(vec(b))
                ok = ok and GA.eq(comm(theta(A, lam), theta(B, lam)), GA.scal(lam / 3, comm(A, B)))
    GA.check("D^T_a V = hb^{-1}(a); reduced connection Omega(a) - hb^{-1}(a) ^ V/l^2", ok)
    assert ok
