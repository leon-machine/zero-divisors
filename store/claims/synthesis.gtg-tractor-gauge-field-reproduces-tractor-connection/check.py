"""synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection: exact checks in Cl(2,4).

Generators: e0 (square +1), e1, e2, e3 (square -1), e+ (square +1), e- (square -1);
n0 = (e+ + e-)/2, ninf = e+ - e-, so Q(n0) = Q(ninf) = 0 and n0 . ninf = 1. A tractor in the
splitting of a scale is V = sigma ninf + mu + rho n0 (mu a physical vector), so Q(V) = 2 sigma rho + Q(mu).
The algebraic part of the gauge field is Theta(A) = -ninf ^ A + n0 ^ P(A), acting by the commutator
product, A = hb^{-1}(a) the physical direction and P the Schouten map.
  (1) Theta(A) x V has slots (-mu.A, A rho - P(A) sigma, P(A).mu): the stored tractor connection's
      algebraic terms; and V . (Theta(A) x V) = 0 (the tractor metric is preserved).
  (2) I = ninf + rho n0: Theta(A) x I = rho A - P(A), so I is parallel iff P = rho id; Q(I) = 2 rho,
      = Lambda/3 at rho = Lambda/6; a non-Einstein P moves I.
  (3) Flat spacetime (hb = 1, Omega = 0, P = 0): V(x) = sigma(x) ninf - (Lambda/6) x + (Lambda/6) n0,
      sigma = 1 - Lambda Q(x)/12, satisfies a.grad V + Theta(a) x V = 0 (a.grad by the central
      difference, exact on quadratics), Q(V) = Lambda/3, and V(0) = ninf + (Lambda/6) n0.
  (4) The algebraic part of the field strength, -R(A^B) + Theta(A) x Theta(B) with R the store-sign
      curvature operator and P its Schouten map, has spacetime block -W(A^B), no ninf ^ n0 block;
      on de Sitter (R(B) = (Lambda/3) B) it vanishes.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def wedge(a, b):
    return comm(a, b)


def dot(a, b):
    return GA.dot(a, b, S)


def smap(M):
    """Symmetric map A -> sum_n (sum_m M[m][n] A.e_m) e^n on spacetime vectors."""
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), ER[n])
                              for n in range(4)])


def theta(A, P):
    return GA.add(GA.neg(wedge(NI, A)), wedge(N0, P(A)))


def tractor(sig, mu, rho):
    return GA.add(GA.scal(sig, NI), mu, GA.scal(rho, N0))


def slots(V):
    """(sigma, mu, rho) of V = sigma ninf + mu + rho n0."""
    return dot(V, N0), grade({b: c for b, c in V.items() if max(b) < 4}, 1), dot(V, NI)


def _premises():
    for pid in ("interior.imported-tractor-connection", "interior.scale-tractor-leaves-cone",
                "mass.de-sitter-scale-frozen-point", "synthesis.imported-gtg-dictionary",
                "dark-energy.stelle-west-vector-frozen-point"):
        premise(pid)


P1 = [[2, 1, 0, -3], [1, -1, 4, 0], [0, 4, 5, 2], [-3, 0, 2, 7]]
P2 = [[F(1, 3), 0, 1, 0], [0, F(-5, 2), 0, 1], [1, 0, 2, 0], [0, 1, 0, F(1, 4)]]
CASES = [(P1, [3, 1, -2, 5], (F(2), [1, 0, 3, -1], F(-7))),
         (P2, [1, 2, 2, 0], (F(-1, 3), [0, 4, 1, 1], F(5, 2))),
         (P1, [0, 0, 1, 1], (F(5), [2, -1, 0, 3], F(1, 7)))]


def check_gauge_field_reproduces_stored_connection():
    _premises()
    ok = True
    for M, a, (sig, m, rho) in CASES:
        P, A, mu = smap(M), vec(a), vec(m)
        V = tractor(sig, mu, rho)
        dV = comm(theta(A, P), V)
        s1, m1, r1 = slots(dV)
        ok = ok and s1 == -dot(mu, A)
        ok = ok and GA.eq(m1, GA.sub(GA.scal(rho, A), GA.scal(sig, P(A))))
        ok = ok and r1 == dot(P(A), mu)
        ok = ok and GA.eq(dV, tractor(s1, m1, r1))          # nothing outside the three slots
        ok = ok and dot(V, dV) == 0                           # Q(V) preserved
        ok = ok and dot(V, V) == 2 * sig * rho + dot(mu, mu)
    # first case by hand: A = (3,1,-2,5), mu = (1,0,3,-1), sigma = 2, rho = -7: mu.A = 3 - 0 + 6 + 5 = 14 in (+,-,-,-)
    s1, m1, r1 = slots(comm(theta(vec([3, 1, -2, 5]), smap(P1)), tractor(F(2), vec([1, 0, 3, -1]), F(-7))))
    ok = ok and s1 == -14
    GA.check("tractor gauge field reproduces the stored connection and preserves Q", ok)
    assert ok


def check_scale_tractor_parallel_iff_einstein():
    _premises()
    lam = F(9, 7)
    rho = lam / 6
    I = tractor(F(1), {}, rho)
    ok = dot(I, I) == lam / 3
    Pe = lambda A: GA.scal(rho, A)                            # P = rho id: the Einstein case
    for _, a, _ in CASES:
        A = vec(a)
        ok = ok and GA.is_zero(comm(theta(A, Pe), I))
        ok = ok and GA.eq(comm(theta(A, smap(P1)), I), GA.sub(GA.scal(rho, A), smap(P1)(A)))
    ok = ok and not GA.is_zero(comm(theta(vec([1, 0, 0, 0]), smap(P1)), I))
    ok = ok and dot(I, I) == F(3, 7) and rho == F(3, 14)
    GA.check("scale tractor parallel iff Einstein, Q(I) = Lambda/3", ok)
    assert ok


def check_flat_de_sitter_scale_tractor_is_parallel_frozen_point():
    _premises()
    lam = F(6, 5)

    def V(x):
        sig = 1 - lam * dot(x, x) / 12
        return tractor(sig, GA.scal(-lam / 6, x), lam / 6)

    zero = lambda A: {}
    ok = GA.eq(V(vec([0, 0, 0, 0])), GA.add(NI, GA.scal(lam / 6, N0)))
    for x in ([1, 2, 0, -1], [F(1, 2), 0, 3, 1], [0, -2, 1, 4]):
        X = vec(x)
        ok = ok and dot(V(X), V(X)) == lam / 3
        for _, a, _ in CASES:
            A = vec(a)
            t = F(1)
            dirV = GA.scal(F(1, 2) / t, GA.sub(V(GA.add(X, GA.scal(t, A))), V(GA.sub(X, GA.scal(t, A)))))
            ok = ok and GA.is_zero(GA.add(dirV, comm(theta(A, zero), V(X))))
    ok = ok and dot(V(vec([1, 2, 0, -1])), V(vec([1, 2, 0, -1]))) == F(2, 5)
    ok = ok and GA.eq(V(vec([0, 0, 0, 0])), GA.add(NI, GA.scal(F(1, 5), N0)))
    GA.check("flat de Sitter scale tractor is parallel with Q = Lambda/3 and V(0) = I_Lambda", ok)
    assert ok


def check_field_strength_spacetime_block_is_weyl():
    _premises()
    sig_r = wedge(E[1], E[0])

    def R_kn(M, c):
        T = smap(M)

        def R(B):
            out = GA.scal(c, GA.add(B, GA.scal(3, GA.mul(GA.mul(sig_r, B, S), sig_r, S))))
            for m in range(4):
                for n in range(m + 1, 4):
                    k = GA.mul(B, wedge(ER[n], ER[m]), S).get((), F(0))
                    if k:
                        out = GA.add(out, GA.scal(k, GA.add(wedge(T(E[m]), E[n]), wedge(E[m], T(E[n])))))
            return out
        return R

    def ricci(R, b):
        return GA.add(*[grade(comm(ER[m], R(wedge(E[m], b))), 1) for m in range(4)])

    def schouten(R):
        sc = sum(GA.mul(ER[m], ricci(R, E[m]), S).get((), F(0)) for m in range(4))
        return lambda a: GA.scal(F(1, 2), GA.sub(ricci(R, a), GA.scal(sc / 6, a)))

    lam = F(3, 2)
    ops = [lambda B: GA.scal(lam / 3, B), R_kn(P1, F(1, 2)), R_kn(P2, F(-2))]
    ok = True
    for idx, R in enumerate(ops):
        P = schouten(R)
        for m in range(4):
            for n in range(m + 1, 4):
                A, B = E[m], E[n]
                Fab = GA.add(GA.neg(R(wedge(A, B))), comm(theta(A, P), theta(B, P)))
                W = GA.sub(R(wedge(A, B)), GA.add(wedge(P(A), B), wedge(A, P(B))))
                spacetime = {b: c for b, c in Fab.items() if max(b) < 4}
                rest = {b: c for b, c in Fab.items() if max(b) >= 4}
                ok = ok and GA.eq(spacetime, GA.neg(W)) and GA.is_zero(rest)
                if idx == 0:
                    ok = ok and GA.is_zero(Fab)
    # the data are not degenerate: hand values of the operators used
    ok = ok and GA.eq(ops[0](wedge(E[0], E[1])), GA.scal(F(1, 2), wedge(E[0], E[1])))
    ok = ok and ops[1](wedge(E[0], E[2])) == {(0, 2): F(-4), (1, 2): F(-1), (2, 3): F(-3), (0, 1): F(-4), (0, 3): F(-2)}
    GA.check("algebraic field strength of the tractor gauge field is minus the Weyl curvature", ok)
    assert ok


def check_stelle_west_reduction_is_macdowell_mansouri_connection():
    """(v) With P = (Lambda/6) id, Theta(A) = A ^ W, W = ninf - (Lambda/6) n0 = V/Q(V) for the
    Stelle-West vector V = n0 - (3/Lambda) I: Theta(A) x V = A (D_a V is the soldering form),
    Theta(A) x I = 0, and Theta(A) x Theta(B) = (Lambda/3) A ^ B = (A ^ B)/l^2."""
    _premises()
    lam = F(3, 4)
    I = GA.add(NI, GA.scal(lam / 6, N0))
    V = GA.sub(N0, GA.scal(3 / lam, I))
    W = GA.scal(1 / dot(V, V), V)
    ok = dot(V, V) == -4 and dot(V, I) == 0 and GA.eq(W, GA.sub(NI, GA.scal(F(1, 8), N0)))
    Pe = lambda A: GA.scal(lam / 6, A)
    for m in range(4):
        A = E[m]
        ok = ok and GA.eq(theta(A, Pe), wedge(A, W))
        ok = ok and GA.eq(comm(theta(A, Pe), V), A)
        ok = ok and GA.is_zero(comm(theta(A, Pe), I))
        for n in range(4):
            ok = ok and GA.eq(comm(theta(A, Pe), theta(E[n], Pe)), GA.scal(F(1, 4), wedge(A, E[n])))
    GA.check("Stelle-West reduction of the tractor gauge field is the MacDowell-Mansouri connection", ok)
    assert ok
