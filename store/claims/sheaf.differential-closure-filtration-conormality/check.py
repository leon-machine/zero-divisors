"""sheaf.differential-closure-filtration-conormality: exact checks.

A formal calculus of locally finite sums f(x) tau^{e(x)} (log tau)^k with f, e polynomials over Q, the two
derivations acting by the formulas of sheaf.log-obstruction (tau d/dtau tau^e = e tau^e, d/dx tau^e =
e' L tau^e, tau d/dtau L = 1, d/dx L = 0) extended by Leibniz.
(1) A^log is a commutative associative algebra containing A; it is closed under tau d/dtau and d/dx;
[d/dx, tau d/dtau] = 0 and both Leibniz rules hold on products; d/dx tau^e leaves A (log degree 1) as soon as
e' != 0, so the differential closure of A is strictly larger than A.
(2) Filtration: N tangential derivatives of tau^{e} (e = 1 + 2x^2, e' = 4x) give log degree exactly N with top
coefficient (e')^N = 4^N x^N, for N = 1..4; radial derivatives never raise the log degree; along an eight-letter
word the log degree is at most the number of tangential letters.
(3) No operation lowers the exponent set (each derivative's exponents are a subset of the input's), which is the
algebraic content of the conormal bound O(tau^{e_min - eps}); the analytic estimate |log tau|^k = O(tau^-eps) is
not checked.
(4) Log-free elements with constant exponents are closed under both derivations (the Melrose polyhomogeneous
ring); A is the log-degree-zero part, a subalgebra but not stable under d/dx for nonconstant exponents.
EXPORTS the calculus for sheaf.exponent-ratios-are-invariant.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def pnorm(p):
    p = [F(c) for c in p]
    while p and p[-1] == 0:
        p.pop()
    return tuple(p)


def padd(a, b):
    n = max(len(a), len(b))
    return pnorm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def pmul(a, b):
    if not a or not b:
        return ()
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return pnorm(out)


def pdiff(a):
    return pnorm([i * a[i] for i in range(1, len(a))])


def pc(*coeffs):
    return pnorm(coeffs)


def anorm(d):
    return {ek: f for ek, f in d.items() if f}


def aterm(f, e, k=0):
    return anorm({(pnorm(e), k): pnorm(f)})


def aadd(a, b):
    out = dict(a)
    for ek, f in b.items():
        out[ek] = padd(out.get(ek, ()), f)
    return anorm(out)


def amul(a, b):
    out = {}
    for (e1, k1), f1 in a.items():
        for (e2, k2), f2 in b.items():
            ek = (padd(e1, e2), k1 + k2)
            out[ek] = padd(out.get(ek, ()), pmul(f1, f2))
    return anorm(out)


def a_tau_dtau(a):
    """tau d/dtau: f tau^e L^k -> f e tau^e L^k + k f tau^e L^(k-1)."""
    out = {}
    for (e, k), f in a.items():
        t1 = pmul(f, e)
        if t1:
            out[(e, k)] = padd(out.get((e, k), ()), t1)
        if k >= 1:
            out[(e, k - 1)] = padd(out.get((e, k - 1), ()), pnorm([k * c for c in f]))
    return anorm(out)


def a_dx(a):
    """d/dx: f tau^e L^k -> f' tau^e L^k + f e' tau^e L^(k+1)."""
    out = {}
    for (e, k), f in a.items():
        t1 = pdiff(f)
        if t1:
            out[(e, k)] = padd(out.get((e, k), ()), t1)
        t2 = pmul(f, pdiff(e))
        if t2:
            out[(e, k + 1)] = padd(out.get((e, k + 1), ()), t2)
    return anorm(out)


def logdeg(a):
    return max((k for (_, k) in a), default=-1)


def exps(a):
    return {e for (e, _) in a}


EXPORTS = {"pc": pc, "pmul": pmul, "pdiff": pdiff, "aterm": aterm, "aadd": aadd, "amul": amul,
           "a_dx": a_dx, "a_tau_dtau": a_tau_dtau, "logdeg": logdeg, "exps": exps}

# generic sample elements of A (polynomial coefficients and exponents)
E1 = pc(0, 1)                 # e = x
E2 = pc(1, 0, 2)              # e = 1 + 2x^2
A1 = aadd(aterm(pc(3, -1), E1), aterm(pc(0, 0, 5), E2))
A2 = aadd(aterm(pc(2), E2), aterm(pc(1, 1), pc(2)))
A3 = aterm(pc(1, 2), pc(0, 3))
B1 = aadd(A1, aterm(pc(0, 0, 5), E1, 1))      # an element of A^log with a log term


def check_log_completion_is_a_stable_algebra():
    premise("sheaf.log-obstruction")
    ok = True
    P = amul(A1, A2)
    ok = ok and logdeg(P) == 0 and padd(E1, E2) in exps(P)
    ok = ok and amul(A1, A2) == amul(A2, A1)
    ok = ok and amul(amul(A1, A2), A3) == amul(A1, amul(A2, A3))
    ok = ok and amul(amul(B1, A2), B1) == amul(B1, amul(A2, B1))
    ok = ok and a_dx(a_tau_dtau(B1)) == a_tau_dtau(a_dx(B1))
    ok = ok and a_dx(amul(B1, A2)) == aadd(amul(a_dx(B1), A2), amul(B1, a_dx(A2)))
    ok = ok and a_tau_dtau(amul(B1, A2)) == aadd(amul(a_tau_dtau(B1), A2), amul(B1, a_tau_dtau(A2)))
    # tau d/dtau of the log itself is 1
    ok = ok and a_tau_dtau(aterm(pc(1), pc(0), 1)) == aterm(pc(1), pc(0), 0)
    # d/dx tau^x = log(tau) tau^x: outside A, so the differential closure exceeds A
    D = a_dx(aterm(pc(1), E1))
    ok = ok and D == aterm(pc(1), E1, 1) and logdeg(D) == 1
    GA.check("A^log is a commutative algebra stable under tau d/dtau and d/dx, strictly containing A", ok)
    return ok


def check_log_filtration_by_tangential_derivatives():
    premise("sheaf.log-obstruction")
    ok = True
    T = aterm(pc(1), E2)                         # tau^{1 + 2x^2}, e' = 4x
    word = T
    for N in range(1, 5):
        word = a_dx(word)
        top = {ek: f for ek, f in word.items() if ek[1] == N}
        # (e')^N = (4x)^N, written out by hand
        want = pnorm([0] * N + [4 ** N])
        ok = ok and logdeg(word) == N and top == {(E2, N): want}
    # radial derivatives do not raise the log degree
    for el in (A1, B1, word):
        ok = ok and logdeg(a_tau_dtau(el)) == logdeg(el)
    # a mixed eight-letter word: log degree <= number of tangential letters (here 4, attained)
    w = A1
    ntang = 0
    for op in (a_dx, a_tau_dtau, a_dx, a_tau_dtau, a_dx, a_tau_dtau, a_tau_dtau, a_dx):
        w = op(w)
        if op is a_dx:
            ntang += 1
    ok = ok and ntang == 4 and logdeg(w) == 4
    GA.check("N tangential derivatives give log degree N with top coefficient (e')^N; radial ones add none", ok)
    return ok


def check_exponent_set_never_drops():
    premise("sheaf.log-obstruction")
    ok = True
    for el in (A1, A2, B1, amul(A1, B1)):
        for op in (a_tau_dtau, a_dx):
            ok = ok and exps(op(el)) <= exps(el)
    # iterated: the minimum exponent of the input bounds every term of the output, exponents x and 1 + 2x^2
    w = B1
    for op in (a_dx, a_dx, a_tau_dtau, a_dx):
        w = op(w)
    ok = ok and exps(w) == {E1, E2}
    GA.check("no derivative lowers the exponent set (the algebraic content of conormality)", ok)
    return ok


def check_constant_exponent_ring_and_degree_zero_part():
    premise("sheaf.log-obstruction")
    ok = True
    c1, c2 = pc(F(2, 3)), pc(F(-1, 5))
    R = aadd(aterm(pc(3, -1), c1), aterm(pc(0, 7), c2))
    for op in (a_dx, a_tau_dtau):
        ok = ok and logdeg(op(R)) == 0
    ok = ok and a_dx(R) == aadd(aterm(pc(-1), c1), aterm(pc(7), c2))
    ok = ok and a_tau_dtau(R) == aadd(aterm(pc(2, F(-2, 3)), c1), aterm(pc(0, F(-7, 5)), c2))
    # A is the log-degree-zero part: closed under products, not under d/dx once an exponent moves
    ok = ok and logdeg(amul(A1, A2)) == 0 and logdeg(a_dx(A1)) == 1
    GA.check("constant exponents give the log-free polyhomogeneous ring; A is the degree-zero subalgebra", ok)
    return ok
