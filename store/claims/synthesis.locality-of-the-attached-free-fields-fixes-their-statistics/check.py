"""Locality of the attached free fields fixes their statistics: exact checks.

Spacetime algebra Cl(1,3), gamma_0^2 = +1, gamma_i^2 = -1, I4 = gamma_0 gamma_1 gamma_2 gamma_3.
Polarisation sums (the numerators of the positive-energy two-point functions), on rational null k:
  scalar   P_0(k) = 1                                   (degree 0)
  spinor   P_1(k) = k gamma_0 = 2 k_0 Lambda(k)          (degree 1; Lambda the stored projector)
  photon   P_2(k)[A, B] = sum over transverse eps of <A, k^eps><B, k^eps>, <X, Y> = <XY>_0 for
           bivectors; equal on the cone to the polynomial -<A, k^g_0><B, k^g_0> + sum_i <A, k^g_i><B, k^g_i>
           (degree 2), with k^eps in the stored mode space {f : k f = 0}.
Locality: with D_+ the massless Wightman function, equal on the open spacelike set to -1/(4 pi^2 Q(xi))
(imported, standard; the constant is kept symbolic), the bracket of a free field whose particle and
antiparticle parts carry the polarisation sum P with weights 1 and c > 0 is, at spacelike xi,
  i^d (-1/(4 pi^2)) [ P(d) f (xi) + eta c P(-d)[f(-.)](xi) ],   f = 1/Q,
eta = +1 for the CAR (anticommutator), -1 for the CCR (commutator).  The script evaluates both terms
from exact derivatives of 1/Q at rational spacelike points and finds the bracket zero exactly when
c = 1 and eta = -(-1)^d (positive norm), and P(d) f nonzero (so the other choice is non-local); with a
negative-norm antiparticle term, c = -1 (indefinite form), exactly when eta = (-1)^d (ghosts).
Storeys: a tower plane (Q(v) = Q(w) = 0, {v, w} = 1) has eta = +1; the palatial polynomial pair
(a = d/dz, a* = z) has [a, a*] = 1, eta = -1.
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
G = [1, -1, -1, -1]  # diagonal metric


def g(i):
    return GA.gen(i)


def mm(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def vec(c):
    return {(i,): F(x) for i, x in enumerate(c) if x != 0}


def wedge(a, b):
    return GA.scal(F(1, 2), GA.sub(mm(a, b), mm(b, a)))


def sp(x, y):
    return mm(x, y).get((), F(0))


I4 = mm(g(0), g(1), g(2), g(3))
NULLS = [(5, 3, 4, 0), (3, 1, 2, 2), (9, 4, 4, 7), (7, 2, 3, 6), (-5, 3, 0, 4)]
SPACELIKE = [(0, 1, 2, 3), (1, 3, 1, 2), (F(1, 2), 2, -1, F(3, 2)), (-2, 1, 4, -3)]
BIV = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def Q(x):
    return sum(G[m] * F(x[m]) ** 2 for m in range(4))


# ---------------------------------------------------------------- polarisation sums
def P1(k):
    return mm(vec(k), g(0))


def P2(k, A, B):
    kv = vec(k)
    out = -sp(A, wedge(kv, g(0))) * sp(B, wedge(kv, g(0)))
    for i in (1, 2, 3):
        out += sp(A, wedge(kv, g(i))) * sp(B, wedge(kv, g(i)))
    return out


def P2_phys(k, A, B):
    """Sum over the transverse spatial polarisations: projector delta_ij - k_i k_j / |k|^2."""
    kv = vec(k)
    kk = sum(F(k[i]) ** 2 for i in (1, 2, 3))
    out = F(0)
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            T = (F(1) if i == j else F(0)) - F(k[i]) * F(k[j]) / kk
            out += T * sp(A, wedge(kv, g(i))) * sp(B, wedge(kv, g(j)))
    return out


def blade(b):
    return {b: F(1)}


def check_polarisation_sums_have_degree_two_s():
    premise("field-theory.second-quantisation")
    premise("field-theory.fock-space-maxwell-modes")
    ok = True
    for k in NULLS:
        kv = vec(k)
        ok = ok and Q(k) == 0
        lam = GA.scal(F(1, 2 * k[0]), P1(k))
        ok = ok and GA.eq(mm(lam, lam), lam) and GA.is_zero(mm(kv, lam))
        mk = tuple(-x for x in k)
        k2 = tuple(2 * x for x in k)
        ok = ok and GA.eq(P1(mk), GA.neg(P1(k))) and GA.eq(P1(k2), GA.scal(2, P1(k)))
        # transverse polarisations give modes of the stored space {f : k f = 0}
        eps1 = vec((0, k[2], -k[1], 0))
        eps2 = vec((0, k[3] * k[1], k[3] * k[2], -(k[1] ** 2 + k[2] ** 2)))
        for eps in (eps1, eps2):
            if eps:
                f = wedge(kv, eps)
                ok = ok and GA.dot(kv, eps, SQ) == 0 and GA.is_zero(mm(kv, f)) and not GA.is_zero(f)
        for a, b in product(BIV, BIV):
            A, B = blade(a), blade(b)
            ok = ok and P2(k, A, B) == P2_phys(k, A, B)
            ok = ok and P2(mk, A, B) == P2(k, A, B) and P2(k2, A, B) == 4 * P2(k, A, B)
    # the photon sum is not identically zero and not odd
    ok = ok and any(P2(NULLS[0], blade(a), blade(b)) != 0 for a, b in product(BIV, BIV))
    GA.check("polarisation sums: spinor odd of degree 1 (2 k0 Lambda), photon even of degree 2", ok)
    return ok


# ---------------------------------------------------------------- derivatives of f = 1/Q
def d0(x):
    return F(1) / Q(x)


def d1(x, m):  # d f / d x^m
    return F(-2 * G[m]) * F(x[m]) / Q(x) ** 2


def d2(x, m, n):
    return F(-2 * (G[m] if m == n else 0)) / Q(x) ** 2 + F(8 * G[m] * G[n]) * F(x[m]) * F(x[n]) / Q(x) ** 3


def up(m):  # raising: d^m = g^{mm} d_m on the diagonal metric
    return G[m]


def quad_coeffs(A, B):
    """Coefficients M[m][n] of the quadratic polynomial P2(k) = sum M k^m k^n."""
    def P(k):
        return P2(k, A, B)
    e = [tuple(1 if i == m else 0 for i in range(4)) for m in range(4)]
    M = [[F(0)] * 4 for _ in range(4)]
    for m in range(4):
        M[m][m] = P(e[m])
    for m in range(4):
        for n in range(m + 1, 4):
            s = tuple(e[m][i] + e[n][i] for i in range(4))
            M[m][n] = M[n][m] = F(1, 2) * (P(s) - P(e[m]) - P(e[n]))
    return M


def Pd_f(d, x, sign, extra=None):
    """P(sign * d) applied to f at x, by degree d (0 scalar, 1 spinor, 2 photon component)."""
    if d == 0:
        return GA.sc(d0(x))
    if d == 1:
        out = {}
        for m in range(4):
            out = GA.add(out, GA.scal(sign * up(m) * d1(x, m), mm(g(m), g(0))))
        return out
    M = extra
    tot = F(0)
    for m in range(4):
        for n in range(4):
            tot += M[m][n] * up(m) * up(n) * d2(x, m, n)
    return GA.sc(sign * sign * tot)


def reflected(d, x, M):
    """P(-d)[f(-.)](x): derivatives of y -> f(-y) are (-1)^order f-derivatives at -x."""
    mx = tuple(-F(c) for c in x)
    if d == 0:
        return GA.sc(d0(mx))
    if d == 1:
        out = {}
        for m in range(4):
            out = GA.add(out, GA.scal(-1 * up(m) * (-1) * d1(mx, m), mm(g(m), g(0))))
        return out
    tot = F(0)
    for m in range(4):
        for n in range(4):
            tot += M[m][n] * up(m) * up(n) * d2(mx, m, n)  # (-1)^2 from P(-d), (-1)^2 from f(-.)
    return GA.sc(tot)


def check_locality_selects_the_statistics():
    premise("field-theory.second-quantisation")
    premise("field-theory.fock-space-maxwell-modes")
    premise("field-theory.twistor-attachment")
    A, B = blade((0, 1)), blade((0, 1))
    M = quad_coeffs(A, B)
    ok = True
    for x in SPACELIKE:
        ok = ok and Q(x) < 0
        # box (1/Q) = 0 off the cone: the quadratic extension is unique up to Q(k) R, R constant
        ok = ok and sum(up(m) * d2(x, m, m) for m in range(4)) == 0
        # spinor term is -2 xi gamma_0 / Q^2, nonzero
        ok = ok and GA.eq(Pd_f(1, x, 1), GA.scal(F(-2) / Q(x) ** 2, mm(vec(x), g(0))))
        for d in (0, 1, 2):
            t1 = Pd_f(d, x, 1, M)
            t2 = reflected(d, x, M)
            ok = ok and not GA.is_zero(t1)
            for eta, c in product((1, -1), (F(1), F(2), F(1, 2))):
                bracket = GA.add(t1, GA.scal(eta * c, t2))
                local = GA.is_zero(bracket)
                ok = ok and local == (c == 1 and eta == -(-1) ** d)
            # indefinite (Krein) form, negative-norm antiparticle term c = -1: the condition flips,
            # so the anticommuting scalar (d = 0, eta = +1) is local, the Faddeev-Popov ghost case
            for eta in (1, -1):
                bracket = GA.add(t1, GA.scal(-eta, t2))
                ok = ok and GA.is_zero(bracket) == (eta == (-1) ** d)
            ok = ok and (d != 0 or GA.is_zero(GA.sub(t1, t2)))
    GA.check("spacelike bracket: c > 0 local iff c = 1, eta = -(-1)^d; c = -1 local iff eta = (-1)^d", ok)
    return ok


def check_storeys_carry_opposite_brackets():
    premise("field-theory.imported-tower-limit")
    premise("field-theory.imported-statistics-no-go-palatial-algebra")
    premise("field-theory.no-canonical-commutation-relations-tower")
    premise("field-theory.how-close-tower-comes-ccr")
    sq = GA.sig(1, 1)
    e, f = GA.gen(0), GA.gen(1)
    v = GA.scal(F(1, 2), GA.add(e, f))
    w = GA.scal(F(1, 2), GA.sub(e, f))
    ok = GA.is_zero(GA.mul(v, v, sq)) and GA.is_zero(GA.mul(w, w, sq))
    ok = ok and GA.eq(GA.add(GA.mul(v, w, sq), GA.mul(w, v, sq)), GA.sc(1))       # eta = +1
    ok = ok and not GA.eq(GA.sub(GA.mul(v, w, sq), GA.mul(w, v, sq)), GA.sc(1))   # not CCR
    # palatial pair on polynomials: a = d/dz, a* = z; [a, a*] z^n = z^n
    for n in range(6):
        p = [F(0)] * n + [F(1)]
        a_astar = GA.pderiv(GA.pmul([F(0), F(1)], p))
        astar_a = GA.pmul([F(0), F(1)], GA.pderiv(p))
        ok = ok and GA.padd(a_astar, GA.pneg(astar_a)) == p                       # eta = -1
        # the anticommutator is (2n + 1) z^n, not z^n, for n >= 1
        anti = GA.padd(a_astar, astar_a)
        ok = ok and anti == [F(0)] * n + [F(2 * n + 1)]
    GA.check("tower plane: anticommutator 1 (eta = +1); palatial pair: commutator 1 (eta = -1)", ok)
    return ok




if __name__ == "__main__":
    check_polarisation_sums_have_degree_two_s()
    check_locality_selects_the_statistics()
    check_storeys_carry_opposite_brackets()
