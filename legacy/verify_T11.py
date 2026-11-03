#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T11.py: exact-arithmetic verification of the computational identities of
"The Origin of Mass: The Weight Dictionary and the Exact Join"
(Transport Papers, T11), printed version 1.1.

Imports the series' shared exact-arithmetic library GA.py (deposited alongside
this script).  Everything is exact: rationals, Gaussian rationals, rational
functions in a formal variable, and truncated power series; no floating point
anywhere.  Statement tags refer to the compiled paper.

Parts:
  A  the mass-weight dictionary (thm:dictionary, cor:series): the slot pairing
     I . D sigma is formed and the mass read off, never typed in;
  B  mass as symplectic area (prop:area);
  C  the chart, the de Sitter scale in the flat chart (lem:dsscale), the
     deformed bracket and the point-supported evaluation (thm:grip(1), (4));
  D  the grip theorem (lem:chartiso, def:grip, lem:real, thm:grip(2)-(3),
     prop:casimir, lem:five): the spin isomorphism solved exactly, the
     momentum P = M(I) built from it, its reality on the real slice, and
     m^2 = <P,P> = 2|B|^2 + <I,I> C confirmed as a polynomial identity in the
     deformation parameter on exact instances;
  E  the weight of a composite (prop:weight).
"""

from fractions import Fraction as F
from itertools import combinations

import GA as g

# ---------------------------------------------------------------------------
# small exact helper local to this script
# ---------------------------------------------------------------------------


def gsolve(rows, rhs):
    """Exact solution of a consistent linear system over the Gaussian
    rationals (possibly overdetermined; raises if inconsistent or
    underdetermined)."""
    m, n = len(rows), len(rows[0])
    A = [rows[i][:] + [rhs[i]] for i in range(m)]
    piv, r = [], 0
    zero = g.qi(0)
    for c in range(n):
        p = None
        for i in range(r, m):
            if A[i][c] != zero:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = g.qi(1) / A[r][c]
        A[r] = [x * inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != zero:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    for i in range(r, m):
        if A[i][n] != zero:
            raise ValueError("inconsistent linear system")
    if len(piv) != n:
        raise ValueError("underdetermined linear system")
    sol = [zero] * n
    for i, c in enumerate(piv):
        sol[c] = A[i][n]
    return sol


# ---------------------------------------------------------------------------
# Part A: the mass-weight dictionary (thm:dictionary, cor:series)
# ---------------------------------------------------------------------------
# Conventions of the geometry paper T6: tractor metric <(s,mu,r),(s',mu',r')>
# = s r' + r s' + g(mu,mu'); on an Einstein background P_ab = (Lambda/6) g_ab,
# J = 2 Lambda/3, frozen point I = (1, 0, rho_I) with rho_I = J/n and
# <I,I> = 2 rho_I = 2J/n; Thomas operator on a weight-w density
#   D sigma = ( w(n+2w-2) sigma, (n+2w-2) grad sigma, -(Box sigma - w J sigma) ).
# A "field" is represented by the pair of formal coordinates (sigma, Box sigma):
# the pairing I . D sigma is a linear form a * Box sigma + b * sigma, and the
# Klein-Gordon equation (Box + m^2) sigma = 0 gives m^2 = b / a.  The script
# FORMS the pairing and READS m^2 off it; nothing is typed in.


def thomas_slots(w, n, J):
    """Slots of D sigma: top and bottom as (coefficient of sigma, coefficient
    of Box sigma); the middle slot is (n+2w-2) grad sigma, carried as its
    scalar factor."""
    top = (w * (n + 2 * w - 2), 0)
    mid = (n + 2 * w - 2)
    bot = (w * J, -1)
    return top, mid, bot


def pairing_I_D(w, n, J):
    """I . D sigma with I = (1, 0, rho_I), rho_I = J/n: returns (a, b) with
    I . D sigma = a * Box sigma + b * sigma.  The middle slot pairs against
    the zero middle slot of I and drops out."""
    rho_I = J / n
    top, mid, bot = thomas_slots(w, n, J)
    a = bot[1] + rho_I * top[1]
    b = bot[0] + rho_I * top[0]
    return a, b


def mass_squared_from_pairing(w, n, J):
    a, b = pairing_I_D(w, n, J)
    # a Box sigma + b sigma = 0  <=>  Box sigma = -(b/a) sigma  <=>  m^2 = b/a
    return b / a


ok_minus = True
ok_plus_fails = True
n_nonzero = 0
for w in (F(1), F(-2), F(3, 2), F(7, 3), F(10), F(-1), F(-3), F(0), F(-1, 2)):
    for n in (F(3), F(4), F(6), F(11, 2)):
        for J in (F(1), F(-2, 3), F(5, 7), F(2)):
            ipII = 2 * J / n
            m2 = mass_squared_from_pairing(w, n, J)
            ok_minus = ok_minus and m2 == -w * (w + n - 1) * ipII
            if m2 != 0:
                n_nonzero += 1
                ok_plus_fails = ok_plus_fails and m2 != w * (w + n - 1) * ipII
ok_plus_fails = ok_plus_fails and n_nonzero > 100
g.check("thm:dictionary: forming I . D sigma slot by slot and reading the mass "
      "off the Klein-Gordon equation gives m^2 = -w(w+n-1)<I,I> on a 144-point "
      "rational (w, n, J) grid", ok_minus)
g.check("thm:dictionary: the opposite sign m^2 = +w(w+n-1)<I,I> FAILS the same "
      "pairing at every grid point where m^2 is nonzero (the sign is read off, "
      "not chosen)", ok_plus_fails)

# n = 4, J = 2 Lambda/3 (T6 convention): <I,I> = Lambda/3, rho_I = Lambda/6, and
# m^2 = -w(w+3) Lambda/3, as rational-function identities in a formal Lambda
Lam = g.RF.var()
J_rf = (g.RF.const(2) / g.RF.const(3)) * Lam
g.check("fact:frozen: <I,I> = 2J/n = Lambda/3 and rho_I = J/n = Lambda/6 with "
      "J = 2 Lambda/3, n = 4, as rational-function identities",
      (g.RF.const(2) * J_rf / g.RF.const(4)).eqrf(Lam / g.RF.const(3))
      and (J_rf / g.RF.const(4)).eqrf(Lam / g.RF.const(6)))

ok = True
for w in (F(1), F(-1), F(-3, 2), F(2), F(-3), F(0)):
    rho = J_rf / g.RF.const(4)
    a = g.RF.const(-1)
    b = g.RF.const(w) * J_rf + rho * g.RF.const(w * (4 + 2 * w - 2))
    m2_rf = b / a
    ok = ok and m2_rf.eqrf(g.RF.const(-w * (w + 3)) * Lam / g.RF.const(3))
g.check("thm:dictionary: in n = 4 the pairing gives m^2 = -w(w+3) Lambda/3 as a "
      "rational-function identity in Lambda at six rational weights", ok)

m2_cc = mass_squared_from_pairing(F(-1), F(4), F(2))     # Lambda = 3, H^2 = 1
g.check("cor:series: the conformally coupled scalar (w = -1) has m^2 = 2 Lambda/3 "
      "= 2H^2 from the pairing (instance Lambda = 3: m^2 = 2), positive",
      m2_cc == F(2))

ok = True
for n in (F(3), F(4), F(5), F(6)):
    for J in (F(2), F(-1, 2)):
        roots = [w for w in (F(0), 1 - n, F(1), F(-1), n - 1, F(1, 2))
                 if mass_squared_from_pairing(w, n, J) == 0]
        ok = ok and sorted(roots) == sorted([F(0), 1 - n])
g.check("cor:series: the massless weights are exactly w = 0 and w = 1 - n "
      "(the shadow pair), no others among the tested values", ok)

ok = True
for n in (F(3), F(4), F(5), F(6)):
    for J in (F(2), F(-1, 2)):
        ipII = 2 * J / n
        # shadow symmetry w -> 1 - n - w
        for w in (F(1), F(-2), F(1, 3), F(7, 2)):
            ok = ok and mass_squared_from_pairing(w, n, J) == \
                mass_squared_from_pairing(1 - n - w, n, J)
        # the conformally coupled weight in general dimension
        ok = ok and mass_squared_from_pairing(1 - n / 2, n, J) == n * (n - 2) / 4 * ipII
g.check("cor:series: the shadow symmetry m^2(w) = m^2(1-n-w) on instances, and "
      "m^2 = n(n-2)/4 <I,I> at w = 1 - n/2 for four dimensions", ok)

ok = True
for w in (F(0), F(-3), F(-3, 2), F(-1), F(-2), F(-1, 4)):        # inside [-3, 0]
    ok = ok and mass_squared_from_pairing(w, F(4), F(2)) >= 0
for w in (F(1), F(2), F(1, 2), F(-4), F(-5), F(-7, 2)):           # outside
    ok = ok and mass_squared_from_pairing(w, F(4), F(2)) < 0
ok = ok and mass_squared_from_pairing(F(1), F(4), F(2)) == F(-4)  # w = 1: -4 H^2
g.check("cor:series(3): at real weights m^2 >= 0 exactly inside [-3, 0] and m^2 < 0 "
      "outside (six instances each; w = 1 gives -4H^2): the complementary series "
      "and the tachyonic branch", ok)

wv = g.RF.var()
lhs = -(wv * (wv + g.RF.const(3)))
rhs = g.RF.const(F(9, 4)) - (wv + g.RF.const(F(3, 2))) * (wv + g.RF.const(F(3, 2)))
g.check("cor:series: -w(w+3) = 9/4 - (w+3/2)^2 exactly, so a real weight gives "
      "m^2 <= 9H^2/4 (the complementary series), maximal at w = -3/2",
      lhs.eqrf(rhs))

ok = True
for nu in (F(1), F(2), F(7, 3), F(100)):
    m2H2 = F(9, 4) + nu * nu
    for sgn in (1, -1):
        w = g.qi(F(-3, 2), sgn * nu)
        ok = ok and (-(w * (w + g.qi(3))) == g.qi(m2H2))
g.check("cor:series: for m > 3H/2 the weight is complex, w = -3/2 +- i nu with "
      "nu^2 = m^2/H^2 - 9/4, verified in exact Gaussian rationals (the "
      "principal series)", ok)

# ---------------------------------------------------------------------------
# Part B: mass as symplectic area (prop:area) over the Gaussian rationals
# ---------------------------------------------------------------------------


def eps2(a, b):
    """<ab> = eps^{AB} a_A b_B = a_0 b_1 - a_1 b_0."""
    return a[0] * b[1] - a[1] * b[0]


def momentum_spinor(spinors):
    """p_{AA'} = sum_i pi^i_A conj(pi^i)_{A'} as a 2x2 QI matrix."""
    p = [[g.qi(0), g.qi(0)], [g.qi(0), g.qi(0)]]
    for s in spinors:
        for A in range(2):
            for Ap in range(2):
                p[A][Ap] = p[A][Ap] + s[A] * s[Ap].conj()
    return p


def p_squared(p):
    """p^2 = eps^{AB} eps^{A'B'} p_{AA'} p_{BB'} (exact, QI)."""
    tot = g.qi(0)
    eps = ((0, 1, 1), (1, 0, -1))
    for A, B, s1 in eps:
        for Ap, Bp, s2 in eps:
            tot = tot + g.qi(s1 * s2) * p[A][Ap] * p[B][Bp]
    return tot


SPINORS = [
    [g.qi(1), g.qi(0)],
    [g.qi(0), g.qi(1)],
    [g.qi(2, 1), g.qi(1, -1)],
    [g.qi(1, 3), g.qi(-2, 1)],
    [g.qi(1, 2), g.qi(3, 5)],
]

g.check("prop:area: a single twistor's momentum is null (p^2 = 0) on all five "
      "exact Gaussian-rational spinor instances",
      all(p_squared(momentum_spinor([s])) == g.qi(0) for s in SPINORS))

ok = True
for i in range(len(SPINORS)):
    for j in range(i + 1, len(SPINORS)):
        s1, s2 = SPINORS[i], SPINORS[j]
        br = eps2(s1, s2)
        val = p_squared(momentum_spinor([s1, s2]))
        ok = ok and val == g.qi(2) * br * br.conj()
g.check("prop:area: p^2 = 2|<pi1 pi2>|^2 exactly on all ten unordered pairs "
      "(real, with the imaginary part identically zero)", ok)

g.check("prop:area: proportional (aligned) spinors give vanishing bracket and "
      "a null composite",
      eps2(SPINORS[2], [g.qi(3) * SPINORS[2][0], g.qi(3) * SPINORS[2][1]]) == g.qi(0))

# ---------------------------------------------------------------------------
# Part C: the chart, the de Sitter scale, the deformed bracket
# ---------------------------------------------------------------------------
# T = C^4 with e1, e2 the omega-plane and e3, e4 the pi-plane; n_inf = e1^e2,
# n_0 = e3^e4; ambient pairing <P,P'> = coefficient of e1^e2^e3^e4 in P^P'.
PAIRS4 = list(combinations(range(4), 2))


def wedge2(z1, z2):
    return [z1[i] * z2[j] - z1[j] * z2[i] for (i, j) in PAIRS4]


def perm_sign(perm):
    s = 1
    p = list(perm)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def amb_pair(P, Q):
    tot = g.qi(0)
    for a, (i, j) in enumerate(PAIRS4):
        for b, (k, l) in enumerate(PAIRS4):
            idx = (i, j, k, l)
            if len(set(idx)) != 4:
                continue
            tot = tot + g.qi(perm_sign(idx)) * P[a] * Q[b]
    return tot


def biv(i, j):
    out = [g.qi(0)] * 6
    for a, p in enumerate(PAIRS4):
        if p == (min(i, j), max(i, j)):
            out[a] = g.qi(1) if i < j else g.qi(-1)
    return out


def vadd(u, v):
    return [a + b for a, b in zip(u, v)]


def vscal(c, u):
    return [c * a for a in u]


n_inf, n_0 = biv(0, 1), biv(2, 3)
EAMB = [biv(i, j) for (i, j) in PAIRS4]            # ambient basis
X_SLOT = [biv(0, 2), biv(0, 3), biv(1, 2), biv(1, 3)]

g.check("fact:chart: <n_0, n_inf> = +1 and both distinguished points are null",
      amb_pair(n_0, n_inf) == g.qi(1) and amb_pair(n_inf, n_inf) == g.qi(0)
      and amb_pair(n_0, n_0) == g.qi(0))


def xslot(coeffs):
    x = [g.qi(0)] * 6
    for c_, v in zip(coeffs, X_SLOT):
        x = vadd(x, vscal(g.qi(c_), v))
    return x


def Xpoint(x, c=F(-1, 2)):
    Q = amb_pair(x, x)
    return vadd(vadd(n_0, x), vscal(g.qi(c) * Q, n_inf))


X_SAMPLES = [(F(1), F(0), F(0), F(0)), (F(1), F(2), F(-1), F(3)),
             (F(0), F(1, 2), F(1, 3), F(-2)), (F(2), F(-1), F(1, 3), F(1))]

ok = True
for co in X_SAMPLES:
    x = xslot(co)
    det = co[0] * co[3] - co[1] * co[2]
    ok = ok and amb_pair(x, x) == g.qi(-2 * det)
    ok = ok and amb_pair(x, n_0) == g.qi(0) and amb_pair(x, n_inf) == g.qi(0)
    Q = amb_pair(x, x)
    for c in (F(-1, 2), F(0), F(1, 2), F(2)):
        X = Xpoint(x, c)
        ok = ok and amb_pair(X, X) == Q * g.qi(1 + 2 * c)
    ok = ok and amb_pair(Xpoint(x), Xpoint(x)) == g.qi(0)
g.check("fact:chart / rem:nullity: <x,x> = -2 det x, the x-slot is orthogonal to "
      "n_0 and n_inf, and <X,X> = Q(x)(1+2c) with c undetermined, so nullity "
      "for all x fixes c = -1/2 once <n_0,n_inf> = 1 and Q = <x,x> are given", ok)

# lem:dsscale(1): sigma = 1 - Lambda Q/12 with Q = t^2 - x^2 - y^2 - z^2.
G4 = [F(1), F(-1), F(-1), F(-1)]
ok = True
for xs in ((F(1), F(0), F(0), F(0)), (F(1, 2), F(2), F(-1), F(3)),
           (F(0), F(1), F(1), F(-2))):
    Qv = sum(G4[a] * xs[a] * xs[a] for a in range(4))
    sigma = g.RF1 - Lam * g.RF.const(Qv) / g.RF.const(12)
    mu = [-(Lam / g.RF.const(6)) * g.RF.const(G4[a] * xs[a]) for a in range(4)]
    box = g.RF.const(0)
    for a in range(4):
        # d_a d_a sigma = -(Lambda/6) g_aa; Box = g^{aa} d_a d_a
        box = box + g.RF.const(1 / G4[a]) * (-(Lam / g.RF.const(6)) * g.RF.const(G4[a]))
    rho = -box / g.RF.const(4)
    ok = ok and box.eqrf(-(g.RF.const(2) / g.RF.const(3)) * Lam)
    ok = ok and rho.eqrf(Lam / g.RF.const(6))
    for a in range(4):
        slot2 = -(Lam / g.RF.const(6)) * g.RF.const(G4[a]) + g.RF.const(G4[a]) * rho
        ok = ok and slot2.is_zero()
    norm = g.RF.const(2) * sigma * rho
    for a in range(4):
        norm = norm + g.RF.const(1 / G4[a]) * mu[a] * mu[a]
    ok = ok and norm.eqrf(Lam / g.RF.const(3))
g.check("lem:dsscale(1): for sigma = 1 - Lambda Q/12 the scale tractor "
      "(sigma, d sigma, -Box sigma/4) = (1 - Lambda Q/12, -Lambda x/6, Lambda/6) "
      "is parallel for the flat tractor connection (every slot zero) and has "
      "norm exactly Lambda/3, as rational-function identities in Lambda", ok)

lam_rf = Lam / g.RF.const(6)
ok = True
for co in X_SAMPLES:
    x = xslot(co)
    Q = amb_pair(x, x)
    assert Q.im == 0
    val = g.RF1 - lam_rf * g.RF.const(Q.re) / g.RF.const(2)
    ok = ok and val.eqrf(g.RF1 - Lam * g.RF.const(Q.re) / g.RF.const(12))
    for lam_q in (F(1, 2), F(-1), F(3)):
        I_l = vadd(n_inf, vscal(g.qi(lam_q), n_0))
        ok = ok and amb_pair(Xpoint(x), I_l) == g.qi(1 - lam_q * Q.re / 2)
    I_o = vadd(n_0, vscal(g.qi(F(1, 2)), n_inf))
    ok = ok and amb_pair(Xpoint(x), I_o) == g.qi(-Q.re / 2 + F(1, 2))
g.check("lem:dsscale(2): <X(x), n_inf + lam n_0> = 1 - lam Q/2 exactly, equal "
      "to sigma iff lam = Lambda/6; the other order n_0 + lam n_inf has scale "
      "function lam - Q/2, the inverted chart, not sigma", ok)


ok = (g.RF.const(2) * lam_rf).eqrf(Lam / g.RF.const(3))
for lam_q in (F(1, 2), F(-1), F(3), F(1, 7)):
    I_l = vadd(n_inf, vscal(g.qi(lam_q), n_0))
    ok = ok and amb_pair(I_l, I_l) == g.qi(2 * lam_q)
    # simplicity: I ^ I is the pairing times the volume element; I is simple
    # (a wedge of two vectors) iff <I,I> = 0 iff lam = 0
    ok = ok and (amb_pair(I_l, I_l) == g.qi(0)) == (lam_q == 0)
ok = ok and amb_pair(n_inf, n_inf) == g.qi(0)
g.check("lem:dsscale(3): the ambient pairing <n_inf + lam n_0, n_inf + lam n_0> "
      "is formed and equals 2 lam at four values of lam, so with 2 lam = Lambda/3 "
      "(rational-function identity) the ambient norm is the tractor norm: two "
      "computations, one number; and the vector is null, hence simple by "
      "fact:chart, exactly at lam = 0", ok)

TWISTORS = [
    ([g.qi(1), g.qi(0)], [g.qi(0), g.qi(1)]),
    ([g.qi(2, 1), g.qi(0)], [g.qi(1), g.qi(1, -1)]),
    ([g.qi(0), g.qi(1, 1)], [g.qi(3), g.qi(2)]),
    ([g.qi(1), g.qi(2)], [g.qi(1, 2), g.qi(-1)]),
    ([g.qi(1, -1), g.qi(2, 1)], [g.qi(0, 1), g.qi(1, 1)]),
]


def twistor(om, pi):
    return [om[0], om[1], pi[0], pi[1]]


ok_pi = ok_om = ok_B = True
lam_q = F(1, 2)     # instance Lambda = 3
I_lam = vadd(n_inf, vscal(g.qi(lam_q), n_0))
for i in range(len(TWISTORS)):
    for j in range(i + 1, len(TWISTORS)):
        (o1, p1), (o2, p2) = TWISTORS[i], TWISTORS[j]
        P = wedge2(twistor(o1, p1), twistor(o2, p2))
        ok_pi = ok_pi and amb_pair(n_inf, P) == eps2(p1, p2)
        ok_om = ok_om and amb_pair(n_0, P) == eps2(o1, o2)
        ok_B = ok_B and amb_pair(I_lam, P) == eps2(p1, p2) + g.qi(lam_q) * eps2(o1, o2)
g.check("thm:grip(1): <n_inf, Z1^Z2> = <pi1 pi2> exactly on all ten twistor "
      "pairs (the flat infinity-twistor contraction)", ok_pi)
g.check("thm:grip(1): <n_0, Z1^Z2> = [omega1 omega2] exactly (the second block)",
      ok_om)
g.check("thm:grip(1): B_Lam = <pi1 pi2> + (Lambda/6)[omega1 omega2] exactly at "
      "the instance Lambda = 3 on all ten pairs", ok_B)

ok = True
for co in X_SAMPLES[:2]:
    x = xslot(co)
    Q = amb_pair(x, x).re
    for (o1, p1), (o2, p2) in ((TWISTORS[0], TWISTORS[1]), (TWISTORS[2], TWISTORS[3])):
        br = eps2(p1, p2)
        P = vscal(br, Xpoint(x))
        for lam_q2 in (F(1, 2), F(2)):
            I_l = vadd(n_inf, vscal(g.qi(lam_q2), n_0))
            ok = ok and amb_pair(I_l, P) == br * g.qi(1 - lam_q2 * Q / 2)
g.check("thm:grip(4): for the point-supported composite <pi1 pi2> X(x) the "
      "deformed bracket is sigma(x) <pi1 pi2> = (1 - Lambda Q/12) <pi1 pi2> "
      "exactly: the flat bracket read in the de Sitter scale", ok)

# thm:grip(4), the wedge identity: two twistors on the incidence line of x,
# Z = mu_x pi + pi with (mu_x pi)^a = x^{aa'} eps_{b'a'} pi^{b'} (mu_x = -b_x),
# have Z1 ^ Z2 = <pi1 pi2> X(x); built from the line, not typed in


def on_line(co, pi):
    # co = (x^{13}, x^{14}, x^{23}, x^{24}); eps_{34} = +1
    x13, x14, x23, x24 = co
    # (mu pi)^a = x^{a a'} eps_{b' a'} pi^{b'} = x^{a3} eps_{43} pi^{4} + x^{a4} eps_{34} pi^{3}
    #           = -x^{a3} pi^4 + x^{a4} pi^3
    om = [-g.qi(x13) * pi[1] + g.qi(x14) * pi[0],
          -g.qi(x23) * pi[1] + g.qi(x24) * pi[0]]
    return twistor(om, pi)


ok = True
for co in X_SAMPLES:
    x = xslot(co)
    for (o1, p1), (o2, p2) in ((TWISTORS[0], TWISTORS[1]), (TWISTORS[2], TWISTORS[4])):
        Z1, Z2 = on_line(co, p1), on_line(co, p2)
        W = wedge2(Z1, Z2)
        ok = ok and W == vscal(eps2(p1, p2), Xpoint(x))
g.check("thm:grip(4): two twistors on the incidence line of x, Z = mu_x pi + pi "
      "with mu_x = -b_x, have Z1 ^ Z2 = <pi1 pi2> X(x) exactly (four points, two "
      "spinor pairs): the wedge identity behind the point-supported evaluation", ok)

# ---------------------------------------------------------------------------
# Part D: the grip theorem
# ---------------------------------------------------------------------------


def rot(U, V, W):
    """R_{U^V}(W) = <U,W> V - <V,W> U."""
    return vadd(vscal(amb_pair(U, W), V), vscal(-amb_pair(V, W), U))


def act(A, P):
    """A.(u^v) = Au^v + u^Av, extended linearly to bivectors."""
    out = [g.qi(0)] * 6
    for a, (i, j) in enumerate(PAIRS4):
        if P[a] == g.qi(0):
            continue
        Aei = [A[r][i] for r in range(4)]
        Aej = [A[r][j] for r in range(4)]
        ei = [g.qi(1) if r == i else g.qi(0) for r in range(4)]
        ej = [g.qi(1) if r == j else g.qi(0) for r in range(4)]
        out = vadd(out, vscal(P[a], vadd(wedge2(Aei, ej), wedge2(ei, Aej))))
    return out


_UNIT = []
for r in range(4):
    for c in range(4):
        A = [[g.qi(0)] * 4 for _ in range(4)]
        A[r][c] = g.qi(1)
        _UNIT.append(A)
_UNIT_ACT = [[act(A, EAMB[b]) for b in range(6)] for A in _UNIT]


def spin_preimage(U, V):
    """The traceless A in gl(4) whose action on bivectors is R_{U^V}."""
    rows, rhs = [], []
    for b in range(6):
        target = rot(U, V, EAMB[b])
        for comp in range(6):
            rows.append([_UNIT_ACT[k][b][comp] for k in range(16)])
            rhs.append(target[comp])
    rows.append([g.qi(1) if r == c else g.qi(0) for r in range(4) for c in range(4)])
    rhs.append(g.qi(0))
    sol = gsolve(rows, rhs)
    A = [[sol[4 * r + c] for c in range(4)] for r in range(4)]
    for b in range(6):
        if act(A, EAMB[b]) != rot(U, V, EAMB[b]):
            raise ValueError("spin preimage does not reproduce the rotation")
    return A


def E44(r, c, val=1):
    A = [[g.qi(0)] * 4 for _ in range(4)]
    A[r][c] = g.qi(val)
    return A


A_grade = spin_preimage(n_inf, n_0)
ok = A_grade == [[g.qi(F(-1, 2)), g.qi(0), g.qi(0), g.qi(0)],
                 [g.qi(0), g.qi(F(-1, 2)), g.qi(0), g.qi(0)],
                 [g.qi(0), g.qi(0), g.qi(F(1, 2)), g.qi(0)],
                 [g.qi(0), g.qi(0), g.qi(0), g.qi(F(1, 2))]]
trans_expect = {(0, 2): E44(0, 3, 1), (0, 3): E44(0, 2, -1),
                (1, 2): E44(1, 3, 1), (1, 3): E44(1, 2, -1)}
sc_expect = {(0, 2): E44(2, 1, -1), (0, 3): E44(3, 1, -1),
             (1, 2): E44(2, 0, 1), (1, 3): E44(3, 0, 1)}
for (a, jp), Aexp in trans_expect.items():
    ok = ok and spin_preimage(biv(a, jp), n_inf) == Aexp
for (a, jp), Aexp in sc_expect.items():
    ok = ok and spin_preimage(biv(a, jp), n_0) == Aexp
g.check("lem:chartiso: the spin isomorphism solved exactly on the basis "
      "rotations reproduces the chart form: grading diag(-1/2,-1/2,1/2,1/2) for "
      "n_inf^n_0, the upper-right nilpotent block (pi -> omega) for x^n_inf, "
      "the lower-left block (omega -> pi) for x^n_0, with the displayed signs", ok)

SIG = [[g.qi(0)] * 4 for _ in range(4)]
for k in range(2):
    SIG[k][k + 2] = g.qi(1)
    SIG[k + 2][k] = g.qi(1)


def herm(zi, zj):
    """conj(zi)^T Sigma zj: the (2,2) Hermitian form pairing omega with conj(pi)."""
    tot = g.qi(0)
    for a in range(4):
        for b in range(4):
            tot = tot + zi[a].conj() * SIG[a][b] * zj[b]
    return tot


def moment(A, Zs):
    """M_A = i sum_i conj(Z_i)^T Sigma A Z_i."""
    tot = g.qi(0)
    for z in Zs:
        Az = [sum((A[r][c] * z[c] for c in range(4)), g.qi(0)) for r in range(4)]
        tot = tot + herm(z, Az)
    return g.qi(0, 1) * tot


GRAM = [[amb_pair(EAMB[a], EAMB[b]) for b in range(6)] for a in range(6)]
_inv_cols = [gsolve([row[:] for row in GRAM],
                    [g.qi(1) if r == c else g.qi(0) for r in range(6)]) for c in range(6)]
GRAM_INV = [[_inv_cols[c][r] for c in range(6)] for r in range(6)]
_PRE = {}


def grip(Zs, I):
    """P = M(I): the ambient vector with <P,U> = M_{A(U^I)} for all U."""
    key = tuple((c.re, c.im) for c in I)
    if key not in _PRE:
        _PRE[key] = [spin_preimage(EAMB[a], I) for a in range(6)]
    vals = [moment(_PRE[key][a], Zs) for a in range(6)]
    P = [sum((vals[a] * GRAM_INV[a][J] for a in range(6)), g.qi(0)) for J in range(6)]
    for a in range(6):
        assert amb_pair(P, EAMB[a]) == vals[a]
    return P


def internal_casimir(Z1, Z2):
    """C = (h11 - h22)^2/4 + |h12|^2 = tr(h_0^2)/2, h the Hermitian Gram matrix."""
    h11, h22, h12 = herm(Z1, Z1), herm(Z2, Z2), herm(Z1, Z2)
    return (h11 - h22) * (h11 - h22) / g.qi(4) + h12 * h12.conj()


PAIR_SAMPLES = []
for i in range(len(TWISTORS)):
    for j in range(i + 1, len(TWISTORS)):
        (o1, p1), (o2, p2) = TWISTORS[i], TWISTORS[j]
        PAIR_SAMPLES.append((twistor(o1, p1), twistor(o2, p2), o1, p1, o2, p2))

ok = True
for Z1, Z2, o1, p1, o2, p2 in PAIR_SAMPLES:
    P = grip([Z1, Z2], n_inf)
    br = eps2(p1, p2)
    ok = ok and amb_pair(P, P) == g.qi(2) * br * br.conj()
    ok = ok and amb_pair(P, n_inf) == g.qi(0)
g.check("thm:grip(3): at Lambda = 0 the grip P = M(n_inf) has <P,P> = "
      "2|<pi1 pi2>|^2 on all ten pairs (prop:area recovered from the ambient "
      "construction) and P lies in n_inf-perp", ok)

ok = True
for Z1, Z2, o1, p1, o2, p2 in PAIR_SAMPLES:
    P0 = grip([Z1, Z2], n_0)
    br = eps2(o1, o2)
    ok = ok and amb_pair(P0, P0) == g.qi(2) * br * br.conj()
g.check("thm:grip proof (ii): the grip on n_0, M(n_0), has <P_0,P_0> = "
      "2|[omega1 omega2]|^2 on all ten pairs", ok)

ok = True
for Z1, Z2, o1, p1, o2, p2 in PAIR_SAMPLES:
    Pi, P0 = grip([Z1, Z2], n_inf), grip([Z1, Z2], n_0)
    cross = amb_pair(Pi, P0)
    prod = eps2(p1, p2) * eps2(o1, o2).conj()
    ok = ok and cross == g.qi(2 * prod.re) + internal_casimir(Z1, Z2)
    t = [[sum((p_i[a].conj() * o_l[a] for a in range(2)), g.qi(0))
          for o_l in (o1, o2)] for p_i in (p1, p2)]
    pk = sum((t[i][l] * t[i][l].conj() for i in range(2) for l in range(2)), g.qi(0))
    d = g.qi((t[0][0] + t[1][1]).im)
    ok = ok and cross == pk - d * d
    dett = t[0][0] * t[1][1] - t[0][1] * t[1][0]
    ok = ok and dett == eps2(p1, p2).conj() * eps2(o1, o2)
g.check("thm:grip proof (iii): <P_inf, P_0> = p.k - d^2 with p.k = sum |t_il|^2, "
      "d = Im tr t, t_il = conj(pi_i).omega_l; det t = conj<pi1 pi2>[omega1 omega2]; "
      "and the cross term equals 2 Re(<pi1 pi2> conj[omega1 omega2]) + C exactly", ok)

ok = True
for Z1, Z2, o1, p1, o2, p2 in PAIR_SAMPLES:
    Pi, P0 = grip([Z1, Z2], n_inf), grip([Z1, Z2], n_0)
    C = internal_casimir(Z1, Z2)
    bp, bo = eps2(p1, p2), eps2(o1, o2)
    a0, a1, a2 = amb_pair(Pi, Pi), g.qi(2) * amb_pair(Pi, P0), amb_pair(P0, P0)
    b0 = g.qi(2) * bp * bp.conj()
    b1 = g.qi(2) * (bp * bo.conj() + bo * bp.conj()) + g.qi(2) * C
    b2 = g.qi(2) * bo * bo.conj()
    ok = ok and a0 == b0 and a1 == b1 and a2 == b2
    for lam_q3 in (F(1, 2), F(2), F(-1, 3)):
        I_l = vadd(n_inf, vscal(g.qi(lam_q3), n_0))
        PL = grip([Z1, Z2], I_l)
        ok = ok and PL == vadd(Pi, vscal(g.qi(lam_q3), P0))
        B = amb_pair(I_l, wedge2(Z1, Z2))
        m2 = amb_pair(PL, PL)
        ok = ok and m2 == g.qi(2) * B * B.conj() + g.qi(2 * lam_q3) * C
        ok = ok and m2.im == 0
        ok = ok and amb_pair(PL, I_l) == g.qi(0)
g.check("thm:grip(2): m^2 = <P_Lam,P_Lam> = 2|B_Lam|^2 + <I_Lam,I_Lam> C, with "
      "C = (h11-h22)^2/4 + |h12|^2, as an identity in the deformation parameter "
      "(all three lam-coefficients agree) on all ten pairs; m^2 real; P_Lam "
      "orthogonal to I_Lam; P_Lam = P_inf + lam P_0 recomputed from scratch", ok)

ok = True
for Z1, Z2, o1, p1, o2, p2 in PAIR_SAMPLES:
    h11, h22, h12 = herm(Z1, Z1), herm(Z2, Z2), herm(Z1, Z2)
    tr, det = h11 + h22, h11 * h22 - h12 * h12.conj()
    C = internal_casimir(Z1, Z2)
    ok = ok and C == (tr * tr - g.qi(4) * det) / g.qi(4)
    h0 = [[h11 - tr / g.qi(2), h12], [h12.conj(), h22 - tr / g.qi(2)]]
    trh0sq = sum((h0[i][k] * h0[k][i] for i in range(2) for k in range(2)), g.qi(0))
    ok = ok and C == trh0sq / g.qi(2)
    ok = ok and C.im == 0 and C.re >= 0
g.check("thm:grip(2): C = tr(h_0^2)/2 = ((tr h)^2 - 4 det h)/4, the internal "
      "su(2) Casimir of the Hermitian Gram matrix, real and nonnegative on all "
      "pairs", ok)

# lem:real: the real slice x = i K eps (the 1/sqrt2 dropped, harmless for
# reality), K Hermitian; for real pairs the generators lie in su(2,2), i.e.
# Sigma A is anti-Hermitian; and the grip of a composite on the frozen point
# has real pairing with every real basis vector


def xreal(t, x_, y, z):
    K = [[g.qi(t + z), g.qi(x_, -y)], [g.qi(x_, y), g.qi(t - z)]]
    eps = [[g.qi(0), g.qi(1)], [g.qi(-1), g.qi(0)]]
    X = [[sum((K[a][b] * eps[b][c] for b in range(2)), g.qi(0)) * g.qi(0, 1)
          for c in range(2)] for a in range(2)]
    co = (X[0][0], X[0][1], X[1][0], X[1][1])
    v = [g.qi(0)] * 6
    for c_, vec in zip(co, X_SLOT):
        v = vadd(v, vscal(c_, vec))
    return v


def in_su22(A):
    SA = [[sum((SIG[i][k] * A[k][j] for k in range(4)), g.qi(0)) for j in range(4)]
          for i in range(4)]
    return all(SA[i][j] + SA[j][i].conj() == g.qi(0) for i in range(4) for j in range(4))


REAL_PTS = [(3, 1, -2, 5), (1, 0, 0, 0), (2, -1, 1, 1), (0, 1, 1, -2)]
REAL_X = [xreal(*p) for p in REAL_PTS]
ok = in_su22(A_grade)
for v, p in zip(REAL_X, REAL_PTS):
    t, x_, y, z = p
    ok = ok and amb_pair(v, v) == g.qi(2 * (t * t - x_ * x_ - y * y - z * z))
    ok = ok and in_su22(spin_preimage(v, n_inf)) and in_su22(spin_preimage(v, n_0))
    for w_ in REAL_X:
        ok = ok and in_su22(spin_preimage(v, w_))
# the rotation commutator identity used in lem:real:
# [R_{x^n_inf}, R_{y^n_0}] = <x,y> R_{n_inf^n_0} + R_{x^y}, transported through
# the spin isomorphism


def comm(A, B):
    AB = [[sum((A[i][k] * B[k][j] for k in range(4)), g.qi(0)) for j in range(4)] for i in range(4)]
    BA = [[sum((B[i][k] * A[k][j] for k in range(4)), g.qi(0)) for j in range(4)] for i in range(4)]
    return [[AB[i][j] - BA[i][j] for j in range(4)] for i in range(4)]


ok_comm = True
for v in REAL_X:
    for w_ in REAL_X:
        lhs = comm(spin_preimage(v, n_inf), spin_preimage(w_, n_0))
        xy = amb_pair(v, w_)
        Axy = spin_preimage(v, w_)
        rhs = [[xy * A_grade[i][j] + Axy[i][j] for j in range(4)] for i in range(4)]
        ok_comm = ok_comm and lhs == rhs
g.check("lem:real: [A(x^n_inf), A(y^n_0)] = <x,y> A(n_inf^n_0) + A(x^y) on all "
      "sixteen pairs of the four real points (the commutator identity that puts "
      "the Lorentz generators in su(2,2))", ok_comm)

# rem:nullity: the x for which the translation block b_x = x eps is
# anti-Hermitian form a real 4-dimensional space (8 real unknowns, the
# condition x eps + (x eps)^dagger = 0 has rank 4), and it contains the slice
rows = []
for re_im in range(2):
    for a in range(2):
        for b in range(2):
            x = [[g.qi(0), g.qi(0)], [g.qi(0), g.qi(0)]]
            x[a][b] = g.qi(1) if re_im == 0 else g.qi(0, 1)
            eps = [[g.qi(0), g.qi(1)], [g.qi(-1), g.qi(0)]]
            bx = [[sum((x[i][k] * eps[k][j] for k in range(2)), g.qi(0)) for j in range(2)]
                  for i in range(2)]
            cond = [bx[i][j] + bx[j][i].conj() for i in range(2) for j in range(2)]
            # real and imaginary parts as a real row vector (8 real equations)
            rows.append([F(c.re) for c in cond] + [F(c.im) for c in cond])
g.check("rem:nullity: the real-linear condition 'x eps anti-Hermitian' on the "
      "eight real parameters of x has rank exactly 4, so its solutions are a real "
      "four-dimensional space, the slice x = i K eps (K Hermitian) and nothing "
      "else", g.rank_of_vectors(rows) == 4)

g.check("lem:real: on the real slice x = i K eps (K Hermitian) Q = det K up to the "
      "dropped normalisation, and every generator A(U ^ V) of a real pair "
      "(grading, translations, special conformal, Lorentz) has Sigma A "
      "anti-Hermitian: it lies in su(2,2)", ok)

# uniqueness in lem:dsscale(2): the six points x = 0, the four real coordinate
# unit vectors e_a (t, x, y, z), and 2 e_0 have point embeddings spanning the
# ambient space (rank 6); the chart's own basis bivectors are null and would not do
SIX = [Xpoint(xslot((F(0), F(0), F(0), F(0))))]
for p in ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (2, 0, 0, 0)):
    SIX.append(Xpoint(xreal(*p)))
g.check("lem:dsscale(2), uniqueness: the point embeddings of x = 0, the four real "
      "coordinate unit vectors, and 2 e_0 span the six-dimensional ambient space "
      "(exact rank 6), so a scale function determines its constant vector",
      g.field_rank(SIX) == 6)

ok = True
I_l = vadd(n_inf, vscal(g.qi(F(1, 2)), n_0))
for Z1, Z2, o1, p1, o2, p2 in PAIR_SAMPLES:
    PL = grip([Z1, Z2], I_l)
    for U in [n_inf, n_0] + REAL_X:
        ok = ok and amb_pair(PL, U).im == 0
g.check("lem:real: the grip on I_Lam has real pairing with n_inf, n_0 and four "
      "real x-slot vectors on all ten pairs: P is a real ambient vector", ok)

ok = True
for (o1, p1) in TWISTORS:
    Z = twistor(o1, p1)
    for lam_q3 in (F(1, 2), F(3)):
        I_l = vadd(n_inf, vscal(g.qi(lam_q3), n_0))
        PL = grip([Z, Z], I_l)
        h = herm(Z, Z)
        ok = ok and all(c == g.qi(0) for c in wedge2(Z, Z))
        ok = ok and amb_pair(PL, PL) == g.qi(2 * lam_q3) * h * h
Z1 = twistor([g.qi(1), g.qi(0)], [g.qi(0), g.qi(1)])
Z2 = twistor([g.qi(3, 1), g.qi(0)], [g.qi(0), g.qi(-2, 5)])
I_l = vadd(n_inf, vscal(g.qi(F(1, 2)), n_0))
PL = grip([Z1, Z2], I_l)
ok = ok and amb_pair(I_l, wedge2(Z1, Z2)) == g.qi(0)
ok = ok and internal_casimir(Z1, Z2) == g.qi(0)
ok = ok and amb_pair(PL, PL) == g.qi(0)
ok = ok and any(c != g.qi(0) for c in wedge2(Z1, Z2))
g.check("thm:grip(5): the doubled composite has B_Lam = 0 and m^2 = <I,I> (conj(Z).Z)^2 "
      "(pure residue) on all five twistors; and a non-doubled pair with "
      "B_Lam = 0 and h = 0 has m^2 = 0 exactly: the zero locus is not the "
      "doubled locus, and there is no mass floor", ok)


def casimir(Zs, basis):
    """C2 = (1/2) sum g^{IK} g^{JL} M_IJ M_KL over the span of `basis`."""
    n = len(basis)
    Gs = [[amb_pair(u, v) for v in basis] for u in basis]
    cols = [gsolve([row[:] for row in Gs],
                   [g.qi(1) if r == c else g.qi(0) for r in range(n)]) for c in range(n)]
    Gi = [[cols[c][r] for c in range(n)] for r in range(n)]
    Mm = [[moment(spin_preimage(u, v), Zs) for v in basis] for u in basis]
    tot = g.qi(0)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    tot = tot + Gi[a][c] * Gi[b][d] * Mm[a][b] * Mm[c][d]
    return tot / g.qi(2)


lam_q = F(1, 2)
I_l = vadd(n_inf, vscal(g.qi(lam_q), n_0))
PERP = [vadd(n_inf, vscal(g.qi(-lam_q), n_0))] + X_SLOT
ok = all(amb_pair(u, I_l) == g.qi(0) for u in PERP)
for Z1, Z2, o1, p1, o2, p2 in PAIR_SAMPLES[:4]:
    Zs = [Z1, Z2]
    PL = grip(Zs, I_l)
    C6, C5 = casimir(Zs, EAMB), casimir(Zs, PERP)
    ok = ok and amb_pair(PL, PL) == amb_pair(I_l, I_l) * (C6 - C5)
    h11, h22, h12 = herm(Z1, Z1), herm(Z2, Z2), herm(Z1, Z2)
    c1 = h11 + h22
    c2 = h11 * h11 + h22 * h22 + g.qi(2) * h12 * h12.conj()
    ok = ok and C6 == c2 - c1 * c1 / g.qi(4)
    # prop:casimir(3): the de Sitter Casimir in closed form at Lambda = 3
    B = amb_pair(I_l, wedge2(Z1, Z2))
    ok = ok and C5 == c1 * c1 / g.qi(4) + internal_casimir(Z1, Z2) - g.qi(6) * B * B.conj() / g.qi(3)
E_grade = A_grade
trE2 = sum((E_grade[i][k] * E_grade[k][i] for i in range(4) for k in range(4)), g.qi(0))
ok = ok and trE2 == g.qi(1)
g.check("prop:casimir: <P,P> = <I,I>(C2(so(2,4)) - C2(so(1,4))) on four pairs at "
      "Lambda = 3 (both Casimirs formed from the exact moment components in "
      "adapted bases), C2(so(2,4)) = tr h^2 - (tr h)^2/4, the closed form "
      "C2(so(1,4)) = (tr h)^2/4 + C - 6|B|^2/Lambda, and tr E^2 = 1 on the "
      "grading element fixing the normalisation", ok)

Om = [[amb_pair(I_l, wedge2([g.qi(1) if r == i else g.qi(0) for r in range(4)],
                             [g.qi(1) if r == j else g.qi(0) for r in range(4)]))
       for j in range(4)] for i in range(4)]


def omx(X):
    return [[sum((Om[i][k] * X[k][j] for k in range(4)), g.qi(0)) for j in range(4)]
            for i in range(4)]


def cond_rows(sym):
    rows = []
    for i in range(4):
        for j in range(4):
            if (sym and i < j) or ((not sym) and i <= j):
                row = []
                for X in _UNIT:
                    OX = omx(X)
                    row.append(OX[i][j] - OX[j][i] if sym else OX[i][j] + OX[j][i])
                rows.append(row)
    return rows


dim_stab = 16 - g.field_rank(cond_rows(True))
dim_comp = 16 - g.field_rank(cond_rows(False))
ok = dim_stab == 10 and dim_comp == 6
five = [spin_preimage(u, I_l) for u in PERP]
for A in five:
    OA = omx(A)
    ok = ok and all(OA[i][j] + OA[j][i] == g.qi(0) for i in range(4) for j in range(4))
    ok = ok and sum((A[i][i] for i in range(4)), g.qi(0)) == g.qi(0)
ok = ok and g.field_rank([[A[r][c] for r in range(4) for c in range(4)] for A in five]) == 5
g.check("lem:five: Omega A symmetric has a 10-dimensional solution space (six "
      "conditions), Omega A antisymmetric a 6-dimensional one, the trace cuts "
      "it to 5; and the five generators A(e_a ^ I_Lam), e_a in I_Lam-perp, are "
      "independent, traceless, and lie in the antisymmetric complement", ok)

# ---------------------------------------------------------------------------
# Part E: the weight of a composite (prop:weight)
# ---------------------------------------------------------------------------
ok = True
for Z1, Z2, o1, p1, o2, p2 in PAIR_SAMPLES[:3]:
    for lam_q3 in (F(1, 2), F(2)):
        I_l = vadd(n_inf, vscal(g.qi(lam_q3), n_0))
        PL = grip([Z1, Z2], I_l)
        m2H2 = amb_pair(PL, PL) / g.qi(2 * lam_q3)
        nu2 = m2H2 - g.qi(F(9, 4))
        B = amb_pair(I_l, wedge2(Z1, Z2))
        ok = ok and nu2 == B * B.conj() / g.qi(lam_q3) + internal_casimir(Z1, Z2) - g.qi(F(9, 4))
        ok = ok and nu2.im == 0 and nu2.re > 0      # principal series on these pairs
g.check("prop:weight: nu^2 = m^2/H^2 - 9/4 = 6|B_Lam|^2/Lambda + C - 9/4 exactly "
      "on three pairs at two values of Lambda, real and positive there (the "
      "principal series); that w = -3/2 +- i nu then solves -w(w+3) = m^2/H^2 "
      "is the Gaussian-rational check of Part A", ok)

N = 6
root = g.ps_pow_rat(g.ps_trunc([F(1), F(0), F(-9, 4)], N), F(1, 2), N)
g.check("prop:weight: sqrt(1 - (9/4)eps^2) = 1 - (9/8)eps^2 - (81/128)eps^4 + ... "
      "exactly (eps = H/m), so Im w = m/H - (9/8)H/m + O((H/m)^3) and Re w = -3/2 "
      "exactly", root[0] == 1 and root[1] == 0 and root[2] == F(-9, 8)
      and root[3] == 0 and root[4] == F(-81, 128))

# ---------------------------------------------------------------------------
# summary
# ---------------------------------------------------------------------------

print()
if g.FAILURES:
    print("FAILURES (%d):" % len(g.FAILURES))
    for f in g.FAILURES:
        print("  " + f)
    raise SystemExit(1)
print("All checks pass.")
