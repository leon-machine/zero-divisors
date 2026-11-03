#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T00.py: exact-arithmetic verification of the worked examples of
"An Introduction to Geometric Algebra: A Primer for the Transport Papers"
(Transport Papers, T0).

The primer proves nothing new, but its worked examples are computations, and
the series' standard (house rule 4) is that computations are machine-checked.
Since v1.1 the primer also carries the toolkit (Section 9 as of v1.2), the
classical structural lemmas T1 imports; the computational ones are checked
here too.  (The zero-divisor lemmas returned to T1 in v1.2, and their checks
live in verify_T01.py.)
Imports the series' shared exact-arithmetic library GA.py (house rule 12);
exact rationals throughout, no floating point anywhere.  Sixteen checks.
"""

from fractions import Fraction
from itertools import combinations
import sys

import GA as g

# ---------------------------------------------------------------------------
# Section 2: the geometric product (Example 2.1, the Euclidean plane)
# ---------------------------------------------------------------------------

SQ2 = g.sig(2, 0)
e1, e2 = g.gen(0), g.gen(1)

ok = True
for (a1, a2, b1, b2) in [(1, 2, 3, -1), (Fraction(1, 2), -3, 5, Fraction(2, 7)),
                         (0, 1, 1, 0)]:
    a = g.add(g.scal(a1, e1), g.scal(a2, e2))
    b = g.add(g.scal(b1, e1), g.scal(b2, e2))
    prod = g.mul(a, b, SQ2)
    want = g.add(g.sc(Fraction(a1) * b1 + Fraction(a2) * b2),
               g.scal(Fraction(a1) * b2 - Fraction(a2) * b1, g.mul(e1, e2, SQ2)))
    ok = ok and g.eq(prod, want)
g.check("Ex 2.1: ab = (a.b) + (signed area) e1e2 in the Euclidean plane", ok)

I2 = g.mul(e1, e2, SQ2)
g.check("Ex 2.1: the unit bivector squares to -1", g.eq(g.mul(I2, I2, SQ2), g.sc(-1)))

ok = True
for (a1, b1) in [(2, 3), (Fraction(1, 3), -1)]:
    for (a2, b2) in [(1, -2), (Fraction(5, 2), 4)]:
        za = g.add(g.sc(a1), g.scal(b1, I2))
        zb = g.add(g.sc(a2), g.scal(b2, I2))
        prod = g.mul(za, zb, SQ2)
        want = g.add(g.sc(Fraction(a1) * a2 - Fraction(b1) * b2),
                   g.scal(Fraction(a1) * b2 + Fraction(b1) * a2, I2))
        ok = ok and g.eq(prod, want)
g.check("Ex 2.1: the even subalgebra multiplies exactly like C", ok)

# ---------------------------------------------------------------------------
# Section 3: blades and grades
# ---------------------------------------------------------------------------

g.check("Sec 3: the blade count is 2^n for n <= 6",
      all(len(g.all_blades(n)) == 2 ** n for n in range(7)))

# ---------------------------------------------------------------------------
# Section 4: signature and null vectors (Example 4.1, the hyperbolic plane)
# ---------------------------------------------------------------------------

SQ11 = g.sig(1, 1)
v = g.scal(Fraction(1, 2), g.add(g.gen(0), g.gen(1)))
w = g.scal(Fraction(1, 2), g.sub(g.gen(0), g.gen(1)))

g.check("Ex 4.1: v and w are null and vw + wv = 1 (hyperbolic pair)",
      g.is_zero(g.mul(v, v, SQ11)) and g.is_zero(g.mul(w, w, SQ11))
      and g.eq(g.add(g.mul(v, w, SQ11), g.mul(w, v, SQ11)), g.sc(1)))

g.check("Ex 4.1: the identity v w v = v (T1 opens with what it means)",
      g.eq(g.mul(g.mul(v, w, SQ11), v, SQ11), v))

ok = True
for (p, q) in [(2, 0), (0, 2), (3, 0)]:
    squares = g.sig(p, q)
    n = p + q
    for coeffs in [(1, 1), (2, -3), (1, 0)]:
        x = g.add(*[g.scal(c, g.gen(i)) for i, c in enumerate(coeffs[:n]) if c])
        if x and g.is_zero(g.mul(x, x, squares)):
            ok = False
g.check("Sec 4: definite signatures have no null vectors (rational net)", ok)

# ---------------------------------------------------------------------------
# Section 5: the two involutions, and the commutation rule
# ---------------------------------------------------------------------------

ok = True
for n in range(1, 6):
    squares = g.sig(n, 0)
    for b in g.all_blades(n):
        x = {b: Fraction(1)}
        k = len(b)
        ok = ok and g.eq(g.grade_inv(x), g.scal((-1) ** k, x))
        ok = ok and g.eq(g.reverse(x), g.scal((-1) ** (k * (k - 1) // 2), x))
g.check("Sec 5: involution signs (-1)^k and (-1)^{k(k-1)/2} on all blades, n <= 5", ok)

SQ13 = g.sig(1, 3)
vv = g.add(g.gen(0), g.gen(1))                     # null in Cl(1,3)
ok = g.is_zero(g.mul(vv, vv, SQ13))
for b in [(2,), (3,), (2, 3)]:               # elements orthogonal to vv
    x = {b: Fraction(1)}
    ok = ok and g.eq(g.mul(vv, x, SQ13), g.mul(g.grade_inv(x), vv, SQ13))
g.check("Sec 5: the commutation rule v x = xhat v for x orthogonal to v", ok)

# ---------------------------------------------------------------------------
# Section 6: reflections, rotors, and the boost (Examples 6.1, 6.2)
# ---------------------------------------------------------------------------

ok = True
for u_i in range(2):                          # reflect in e1, then in e2
    u = g.gen(u_i)
    for x in (e1, e2, g.add(e1, g.scal(2, e2))):
        refl = g.scal(-1, g.mul(g.mul(u, x, SQ2), u, SQ2))   # u^{-1} = u here
        # reflection fixes the orthogonal part, negates the parallel part
        par = g.scal(g.dot(x, u, SQ2), u)
        perp = g.sub(x, par)
        ok = ok and g.eq(refl, g.sub(perp, par))
g.check("Sec 6: -uxu^{-1} is the reflection in the hyperplane orthogonal to u", ok)

ok = True
for (a, b) in [(1, 1), (3, 1), (Fraction(1, 2), Fraction(1, 3))]:
    R = g.add(g.sc(a), g.scal(-b, I2))              # R = a - b e1e2 (half-angle)
    nrm = Fraction(a) ** 2 + Fraction(b) ** 2
    Rinv = g.scal(Fraction(1, 1) / nrm, g.add(g.sc(a), g.scal(b, I2)))
    got = g.mul(g.mul(R, e1, SQ2), Rinv, SQ2)
    want = g.add(g.scal((Fraction(a) ** 2 - Fraction(b) ** 2) / nrm, e1),
               g.scal(2 * Fraction(a) * b / nrm, e2))
    ok = ok and g.eq(got, want)
    # rotations preserve the quadratic form
    y = g.add(g.scal(3, e1), g.scal(-2, e2))
    ok = ok and g.eq(g.mul(g.mul(g.mul(R, y, SQ2), Rinv, SQ2),
                       g.mul(g.mul(R, y, SQ2), Rinv, SQ2), SQ2), g.mul(y, y, SQ2))
g.check("Ex 6.1: the rotor R = a - b e1e2 rotates e1 towards e2, exactly", ok)

ok = True
for (a, b) in [(Fraction(5, 4), Fraction(3, 4)), (Fraction(13, 12), Fraction(5, 12))]:
    assert Fraction(a) ** 2 - Fraction(b) ** 2 == 1
    B = g.mul(g.gen(0), g.gen(1), SQ11)
    R = g.add(g.sc(a), g.scal(b, B))
    Rinv = g.add(g.sc(a), g.scal(-b, B))            # since a^2 - b^2 = 1
    got = g.mul(g.mul(R, v, SQ11), Rinv, SQ11)
    ok = ok and g.eq(got, g.scal((Fraction(a) - b) ** 2, v))
    got_w = g.mul(g.mul(R, w, SQ11), Rinv, SQ11)
    ok = ok and g.eq(got_w, g.scal((Fraction(a) + b) ** 2, w))
g.check("Ex 6.2: a boost rescales the null directions by (a -+ b)^2", ok)

# ---------------------------------------------------------------------------
# Section 7: the mod-8 table's inputs (pseudoscalar squares, centres)
# ---------------------------------------------------------------------------

ok = True
for n in range(1, 7):
    for p in range(n + 1):
        q = n - p
        squares = g.sig(p, q)
        omega = {tuple(range(n)): Fraction(1)}
        m = p - q
        want = Fraction((-1) ** ((m * (m - 1) // 2) % 2))
        ok = ok and g.eq(g.mul(omega, omega, squares), g.sc(want))
        central = [b for b in g.all_blades(n)
                   if all(g.commutes({b: Fraction(1)}, g.gen(i), squares)
                          for i in range(n))]
        expect = [()] if n % 2 == 0 else [(), tuple(range(n))]
        ok = ok and central == expect
g.check("Sec 7: omega^2 = (-1)^{m(m-1)/2} and the centre, all (p,q) with n <= 6", ok)

# ---------------------------------------------------------------------------
# Section 8: the conformal model over the real line (the oldest 1/0)
# ---------------------------------------------------------------------------

SQC = g.sig(2, 1)                                # base (1,0) + e+ (+1) + e- (-1)
g0, ep, em = g.gen(0), g.gen(1), g.gen(2)
n0 = g.scal(Fraction(1, 2), g.sub(em, ep))
ninf = g.add(em, ep)


def lift(x):
    x = Fraction(x)
    return g.add(n0, g.scal(x, g0), g.scal(x * x / 2, ninf))


ok = g.is_zero(g.mul(n0, n0, SQC)) and g.is_zero(g.mul(ninf, ninf, SQC)) \
    and g.dot(n0, ninf, SQC) == -1
for x in (Fraction(3), Fraction(-2), Fraction(1, 4), Fraction(0)):
    X = lift(x)
    ok = ok and g.is_zero(g.mul(X, X, SQC))
    for y in (Fraction(1), Fraction(-1, 3)):
        ok = ok and g.dot(lift(x), lift(y), SQC) == -((x - y) ** 2) / 2
swap = lambda N: g.mul(g.mul(ep, N, SQC), ep, SQC)
for x in (Fraction(3), Fraction(-2), Fraction(1, 4)):
    ok = ok and g.eq(g.scal(-1 / (x * x), swap(lift(x))), lift(1 / x))
ok = ok and g.eq(swap(lift(0)), g.scal(Fraction(-1, 2), ninf))     # 1/0 = infinity
ok = ok and g.eq(swap(ninf), g.scal(-2, n0))                       # 1/infinity = 0
g.check("Sec 8: the conformal lift is null and faithful, and 1/0 = infinity "
      "on the projective line, exactly", ok)

# ---------------------------------------------------------------------------
# Section 9: the toolkit (the computational structural lemmas T1 imports)
# ---------------------------------------------------------------------------

# Lemma 9.6 (splitting along a hyperbolic plane), in Cl(2,1):
# V' = H0 perp U' with H0 spanned by the hyperbolic pair (v, w0) built from
# e1, e3 and U' = span(e2).  The eight products {1, v, w0, v w0} x {1, e2}
# must be linearly independent (unique expansion), and left multiplication
# by v must be injective on Cl(U').
SQ21 = g.sig(2, 1)
hv = g.scal(Fraction(1, 2), g.add(g.gen(0), g.gen(2)))
hw = g.scal(Fraction(1, 2), g.sub(g.gen(0), g.gen(2)))
ok = g.is_zero(g.mul(hv, hv, SQ21)) and g.is_zero(g.mul(hw, hw, SQ21)) \
    and g.eq(g.add(g.mul(hv, hw, SQ21), g.mul(hw, hv, SQ21)), g.sc(1))
h_basis = [g.sc(1), hv, hw, g.mul(hv, hw, SQ21)]
u_basis = [g.sc(1), g.gen(1)]
prods = [g.mul(h, u, SQ21) for h in h_basis for u in u_basis]
blades3 = g.all_blades(3)
rows = [[x.get(b, Fraction(0)) for b in blades3] for x in prods]
rank, m = 0, [r[:] for r in rows]
for col in range(len(blades3)):
    piv = next((i for i in range(rank, len(m)) if m[i][col]), None)
    if piv is None:
        continue
    m[rank], m[piv] = m[piv], m[rank]
    for i in range(len(m)):
        if i != rank and m[i][col]:
            f = m[i][col] / m[rank][col]
            m[i] = [a - f * b for a, b in zip(m[i], m[rank])]
    rank += 1
ok = ok and rank == 8
for x in (g.sc(1), g.gen(1), g.add(g.sc(1), g.scal(2, g.gen(1)))):
    ok = ok and not g.is_zero(g.mul(hv, x, SQ21))
g.check("Lem 9.6: the split expansion is unique (rank 8) and v-mult is "
      "injective on Cl(U'), in Cl(2,1)", ok)

# Lemma 9.2 (twisted adjoint): for the odd versor g = e1 in Cl(1,3),
# tau_g(x) = g xhat g^{-1} is multiplicative, and on vectors it is the
# reflection x - 2 (x.u / Q(u)) u.
u = g.gen(0)                                    # Q(u) = +1, so u^{-1} = u
tau = lambda z: g.mul(g.mul(u, g.grade_inv(z), SQ13), u, SQ13)
samples = [g.gen(1), g.mul(g.gen(0), g.gen(1), SQ13), g.add(g.sc(1), g.mul(g.gen(1), g.gen(2), SQ13)), g.gen(3)]
ok = True
for za in samples:
    for zb in samples:
        ok = ok and g.eq(tau(g.mul(za, zb, SQ13)), g.mul(tau(za), tau(zb), SQ13))
for vec in (g.gen(0), g.gen(1), g.add(g.gen(0), g.scal(3, g.gen(2)))):
    want = g.sub(vec, g.scal(2 * g.dot(vec, u, SQ13), u))
    ok = ok and g.eq(tau(vec), want)
g.check("Lem 9.2: tau_g is an algebra automorphism restricting to the "
      "reflection on vectors, for the odd versor g = e1 in Cl(1,3)", ok)

# ---------------------------------------------------------------------------

print()
if g.FAILURES:
    print("FAILURES (%d):" % len(g.FAILURES))
    for f in g.FAILURES:
        print("  " + f)
    sys.exit(1)
print("All checks pass.")
