"""correspondence.imported-vacuum-equations-scale-tractor: exact checks in Cl(2,4).

Conventions as in the tractor gauge field: e0 (square +1), e1..e3 (square -1), e+ (+1), e- (-1),
n0 = (e+ + e-)/2, ninf = e+ - e-; tractors sigma ninf + mu + rho n0. The gravitational field is a sample
hb (through hb^{-1}, a linear map) and Omega (spacetime bivectors); the field strength is given as a
curvature operator R on physical bivectors in the store's sign, built as (Lambda/3) B plus a trace-free
(Weyl) part plus a Kulkarni-Nomizu part T ^ id; its Ricci map R(b) = d_a . R(a ^ b), scalar J-trace and
Schouten map P(A) = (R(A) - A R/6)/2 are computed by contraction, not assumed.
  (1) Lambda = 0: the Weyl-only operator has R(b) = 0 and P = 0, and D^T_a ninf = -P(A) = 0 for every a:
      the null scale tractor (Q(ninf) = 0) is parallel; a non-vacuum operator gives D^T_a ninf = -P(A) != 0.
  (2) Einstein (R(B) = (Lambda/3) B + Weyl): R(b) = Lambda b, P = (Lambda/6) id, rho_g = J/4 = Lambda/6
      with J the trace of P, I_g = ninf + rho_g n0 is parallel and Q(I_g) = Lambda/3.
  (3) Converse: D^T_a (ninf + rho n0) = rho A - P(A) + (a.grad rho) n0, so a non-constant rho or a non-scalar
      P is not parallel, and on an Einstein field the only rho is Lambda/6, i.e. Lambda = 6 rho.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])


def mul(*xs):
    r = GA.sc(1)
    for x in xs:
        r = GA.mul(r, x, S)
    return r


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def dot(a, b):
    return GA.dot(a, b, S)


def linmap(M):
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), E[n])
                              for n in range(4)])

def symmap(M):
    """A -> sum_n (sum_m M[m][n] A.e^m) e^n: for symmetric M a metric-symmetric map (P(e_m).e_n = M[m][n])."""
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), ER[n])
                              for n in range(4)])


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def curvature(lam, weyl, T):
    """R(B) = (lam/3) B + weyl (B + 3 s B s), s = e1 e0, + (T ^ id)(B), T a symmetric matrix."""
    s = mul(E[1], E[0])
    Tm = symmap(T) if T else None

    def R(B):
        out = GA.add(GA.scal(F(lam) / 3, B), GA.scal(F(weyl), GA.add(B, GA.scal(3, mul(s, B, s)))))
        if Tm:
            for m in range(4):
                for n in range(m + 1, 4):
                    k = mul(B, comm(ER[n], ER[m])).get((), F(0))
                    if k:
                        out = GA.add(out, GA.scal(k, GA.add(comm(Tm(E[m]), E[n]), comm(E[m], Tm(E[n])))))
        return out
    return R


def ricci(R, b):
    return GA.add(*[grade(comm(ER[m], R(comm(E[m], b))), 1) for m in range(4)])


def scalar(R):
    return sum(dot(ER[m], ricci(R, E[m])) for m in range(4))


def schouten(R):
    sc = scalar(R)
    return lambda A: GA.scal(F(1, 2), GA.sub(ricci(R, A), GA.scal(sc / 6, A)))


def tractor(sig, mu, rho):
    return GA.add(GA.scal(sig, NI), mu, GA.scal(rho, N0))


HINV = [[2, 1, 0, 0], [0, 1, 0, -1], [1, 0, 3, 0], [0, 0, 1, 1]]
OMEGA = [mul(E[0], E[1]), GA.add(mul(E[1], E[2]), mul(E[0], E[3])), mul(E[2], E[3]), mul(E[0], E[2])]
DIRS = ([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [3, 1, -2, 5])
TSYM = [[1, 0, 2, 0], [0, -1, 0, 1], [2, 0, 3, 0], [0, 1, 0, 2]]
WEYL = F(5, 4)


def omega_of(a):
    return GA.add(*[GA.scal(dot(a, ER[m]), OMEGA[m]) for m in range(4)])


def D_const(a, P, V):
    """D^T_a V for a tractor V with constant components: Omega_T(a) x V."""
    A = linmap(HINV)(vec(a))
    om = GA.add(omega_of(vec(a)), GA.neg(comm(NI, A)), comm(N0, P(A)))
    return comm(om, V)


def check_vacuum_iff_null_scale_tractor_parallel():
    premise("interior.covariant-form-vacuum-equations")
    hinv = linmap(HINV)
    Rv = curvature(0, WEYL, None)                      # Ricci-flat: Weyl part only
    ok = all(GA.is_zero(ricci(Rv, E[m])) for m in range(4))
    Pv = schouten(Rv)
    ok = ok and dot(NI, NI) == 0
    for a in DIRS:
        ok = ok and GA.is_zero(D_const(a, Pv, NI))
    Rn = curvature(0, WEYL, TSYM)                      # not vacuum
    Pn = schouten(Rn)
    moved = False
    for a in DIRS:
        d = D_const(a, Pn, NI)
        ok = ok and GA.eq(d, GA.neg(Pn(hinv(vec(a)))))
        moved = moved or not GA.is_zero(d)
    ok = ok and moved
    # by hand: the Weyl part alone, R(e0 ^ e1) = (5/4)(e0e1 + 3 s e0e1 s) = (5/4)(1 + 3) e0e1 = 5 e0e1
    ok = ok and GA.eq(Rv(mul(E[0], E[1])), GA.scal(5, mul(E[0], E[1])))
    GA.check("vacuum (Lambda = 0) iff the null scale tractor ninf is parallel", ok)
    assert ok


def check_einstein_scale_tractor_parallel_with_norm():
    premise("interior.scale-tractor-leaves-cone")
    ok = True
    for lam in (F(3, 2), F(-6, 5), F(9, 7)):
        R = curvature(lam, WEYL, None)
        ok = ok and all(GA.eq(ricci(R, E[m]), GA.scal(lam, E[m])) for m in range(4))
        P = schouten(R)
        ok = ok and all(GA.eq(P(E[m]), GA.scal(lam / 6, E[m])) for m in range(4))
        J = sum(dot(ER[m], P(E[m])) for m in range(4))
        rho_g = J / 4
        I = tractor(F(1), {}, rho_g)
        for a in DIRS:
            ok = ok and GA.is_zero(D_const(a, P, I))
        ok = ok and dot(I, I) == lam / 3
    # by hand at Lambda = 3/2: J = 4 (1/4) = 1, rho_g = 1/4, Q(I) = 2 rho_g = 1/2
    R = curvature(F(3, 2), WEYL, None)
    P = schouten(R)
    ok = ok and sum(dot(ER[m], P(E[m])) for m in range(4)) == 1 and scalar(R) == 6
    GA.check("Einstein field: I_g = ninf + (J/4) n0 is parallel with Q(I_g) = Lambda/3", ok)
    assert ok


def check_parallel_section_forces_einstein_lambda_six_rho():
    premise("interior.scale-tractor-leaves-cone")
    hinv = linmap(HINV)
    ok = True
    # derivative clause: a non-constant rho leaves (a.grad rho) n0, even on an Einstein field
    lam = F(3, 2)
    P = schouten(curvature(lam, WEYL, None))
    r = [1, 0, -2, 0]
    for a in DIRS:
        x0, xp, xm = [0, 0, 0, 0], list(a), [-c for c in a]
        rho = lambda x: lam / 6 + sum(F(r[i]) * x[i] for i in range(4))
        dI = GA.scal(F(1, 2), GA.sub(tractor(F(1), {}, rho(xp)), tractor(F(1), {}, rho(xm))))
        DI = GA.add(dI, D_const(a, P, tractor(F(1), {}, rho(x0))))
        ok = ok and GA.eq(DI, GA.scal(sum(F(r[i]) * a[i] for i in range(4)), N0))
    # algebraic clause: rho A - P(A); on an Einstein field the unique rho is Lambda/6
    for lam in (F(3, 2), F(-6, 5)):
        P = schouten(curvature(lam, WEYL, None))
        for a in DIRS:
            A = hinv(vec(a))
            for rho in (lam / 6, lam / 3, F(0)):
                d = D_const(a, P, tractor(F(1), {}, rho))
                ok = ok and GA.eq(d, GA.sub(GA.scal(rho, A), P(A)))
                ok = ok and (GA.is_zero(d) == (6 * rho == lam))
    # a non-Einstein field has no parallel (1, 0, rho): P(e0) is not a multiple of e0
    Pn = schouten(curvature(F(3, 2), WEYL, TSYM))
    ok = ok and GA.rank_of_vectors([GA.basis_vector_of(x, [(0,), (1,), (2,), (3,)]) for x in (Pn(E[0]), E[0])]) == 2
    GA.check("a parallel (1, 0, rho) forces rho constant and an Einstein field with Lambda = 6 rho", ok)
    assert ok
