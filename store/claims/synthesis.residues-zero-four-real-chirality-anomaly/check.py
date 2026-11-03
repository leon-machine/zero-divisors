"""synthesis.residues-zero-four-single-ideal-anomalous: exact checks.

Signatures (p, q): p generators of square +1, q of square -1; causal means min(p, q) = 1, the
time being the minority-sign generator. T14c's spinor ideal S = Cl0(V) f with f = (1 + e_t e_a)/2,
times the chiral factor (1 + c I)/2 in dimension six (c = +1 or -1), as in
synthesis.lowest-causal-residues-zero-four-content.

check_real_chirality_window_free:
  (a) for every causal signature with n <= 14, n even: I^2 = +1 iff n = 2 mod 4 iff r in {0, 4};
      for odd n, r is odd; for n = 0 mod 4, I^2 = -1 and r in {2, 6};
  (b) at (1,1), (1,5), (5,1) every element of S is an eigenvector of left multiplication by I with
      one real eigenvalue (+1, or c), and the two chiral factors give opposite eigenvalues, so
      the two ideals are non-isomorphic Cl0-modules (I is central in Cl0); at (1,3), (3,1)
      I^2 = -1, so no real eigenvector exists;
  (c) at (1,1) the pseudoscalar is the product e_t e_a of the tower's own two directions, both
      shared with this tower; at (1,5) and (5,1), with shared directions {time, three space} and
      J the unit bivector of the two unshared ones, J^2 = -1, J commutes with every shared
      generator, and on S the shared pseudoscalar I4 equals -c J.
check_anomaly_polynomials:
  (d) A-hat = prod (x/2)/sinh(x/2), expanded exactly in the Pontryagin classes: the degree-4j
      parts for j = 1..4 are the standard ones and are nonzero; Pontryagin classes have degree
      4j only, so the degree-(n+2) part vanishes for n = 0 mod 4 and is nonzero for
      n = 2, 6, 10, 14;
  (e) the pure-gauge part of the degree-(n+2) anomaly form is tr(F^((n+2)/2)) / ((n+2)/2)!; its
      exponent is even exactly for n = 2 mod 4, where a representation and its conjugate add
      (sum of even powers of real weights, positive on every nonzero Cartan element tested in
      the u(1) and su(4) fundamental cases), and odd for n = 0 mod 4, where they can cancel.
check_two_dimensional_fields:
  (f) the scalar curvature of the plane field -a^2 deta^2 + a^2 dx^2 is R = 2 (a a'' - a'^2) / a^4:
      for a = eta (radiation) R = -2 eta^-4, for a = eta^2 (matter) R = -4 eta^-6, both with
      nonzero derivative; for de Sitter a = -1/(H eta) it is the constant 2 H^2; on the t-r plane
      of the Schwarzschild field, -f dt^2 + dr^2/f, R = -f'' = 4M/r^3 with nonzero derivative.
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from GA import mul, add, scal, sc, gen, all_blades, rank_of_vectors, ps_inv
from GA import padd, pmul, pneg, pderiv, peval, pconst
from tp_premise import premise


def squares(p, q):
    return tuple([1] * p + [-1] * q)


def vol(idx):
    return {tuple(sorted(idx)): F(1)}


def time_index(p, q):
    return 0 if p == 1 else p


def ideal(p, q, c=0):
    n = p + q
    s = squares(p, q)
    t = time_index(p, q)
    a = 1 if t == 0 else 0
    f = scal(F(1, 2), add(sc(1), mul(gen(t), gen(a), s)))
    if c:
        f = mul(f, scal(F(1, 2), add(sc(1), scal(c, vol(range(n))))), s)
    assert mul(f, f, s) == f
    blades = all_blades(n)
    rows, S = [], []
    for B in blades:
        if len(B) % 2:
            continue
        g = mul({B: F(1)}, f, s)
        cand = rows + [[g.get(C, F(0)) for C in blades]]
        if g and rank_of_vectors(cand) == len(cand):
            rows, S = cand, S + [g]
    return n, s, t, S


def check_real_chirality_window_free():
    premise("synthesis.oriented-causal-towers-mirror-pair-every-window")
    premise("transport.sign")
    premise("dark-tower-matter.constituents-field")
    premise("dark-matter.projection-every-towers-content-dilutes-ones")
    premise("dark-matter.thickness-not-gravitational-quantity")
    # (a)
    for n in range(2, 15):
        for (p, q) in sorted({(1, n - 1), (n - 1, 1)}):
            r = (p - q) % 8
            I2 = mul(vol(range(n)), vol(range(n)), squares(p, q))
            if n % 2:
                assert r % 2 == 1
            elif n % 4 == 2:
                assert I2 == sc(1) and r in (0, 4)
            else:
                assert I2 == sc(-1) and r in (2, 6)
            assert (n % 2 == 0 and I2 == sc(1)) == (r in (0, 4))
    GA.check("(a) causal, n even: I^2 = +1 iff n = 2 mod 4 iff r in {0, 4} (n <= 14)", True)
    # (b)
    for (p, q, c) in [(1, 1, 0), (1, 5, 1), (1, 5, -1), (5, 1, 1), (5, 1, -1)]:
        n, s, t, S = ideal(p, q, c)
        ev = c if c else 1
        assert len(S) == (1 if n == 2 else 8)
        for psi in S:
            assert mul(vol(range(n)), psi, s) == scal(ev, psi)
        for i in range(n):
            for j in range(i + 1, n):
                biv = mul(gen(i), gen(j), s)
                assert mul(biv, vol(range(n)), s) == mul(vol(range(n)), biv, s)
    for (p, q) in [(1, 3), (3, 1)]:
        assert mul(vol(range(4)), vol(range(4)), squares(p, q)) == sc(-1)
    GA.check("(b) T14c's single ideal at (1,1), (1,5), (5,1) has real chirality; none at (1,3), (3,1)", True)
    # (c)
    n, s, t, S = ideal(1, 1, 0)
    assert vol(range(2)) == mul(gen(0), gen(1), s)
    for (p, q) in [(1, 5), (5, 1)]:
        for c in (1, -1):
            n, s, t, S = ideal(p, q, c)
            space = [i for i in range(n) if i != t]
            shared = [t] + space[:3]
            uns = space[3:]
            assert len(shared) == 4 and len(uns) == 2
            I4 = vol(shared)
            J = mul(gen(uns[0]), gen(uns[1]), s)
            assert mul(I4, I4, s) == sc(-1) and mul(J, J, s) == sc(-1)
            assert all(mul(J, gen(i), s) == mul(gen(i), J, s) for i in shared)
            for psi in S:
                assert mul(I4, psi, s) == scal(-c, mul(J, psi, s))
    GA.check("(c) at (1,5), (5,1) the shared pseudoscalar acts on S as -c J, J the unshared plane", True)
    return True


def partitions(m, mx=None):
    mx = m if mx is None else mx
    if m == 0:
        yield ()
        return
    for k in range(min(m, mx), 0, -1):
        for rest in partitions(m - k, k):
            yield (k,) + rest


def check_anomaly_polynomials():
    premise("standard-model.imported-anomaly-coefficients")
    N = 4
    fact = [1]
    for k in range(1, 2 * N + 2):
        fact.append(fact[-1] * k)
    g = ps_inv([F(1, 4 ** k * fact[2 * k + 1]) for k in range(N + 1)], N)
    assert g == [F(1), F(-1, 24), F(7, 5760), F(-31, 967680), F(127, 154828800)]
    K = N

    def pm(A, B):
        out = {}
        for ea, ca in A.items():
            for eb, cb in B.items():
                e = tuple(x + y for x, y in zip(ea, eb))
                if sum(e) <= N:
                    out[e] = out.get(e, F(0)) + ca * cb
        return {e: v for e, v in out.items() if v != 0}

    P = {tuple([0] * K): F(1)}
    for i in range(K):
        P = pm(P, {tuple(k if m == i else 0 for m in range(K)): g[k] for k in range(N + 1)})
    E = {}
    for j in range(1, K + 1):
        E[j] = {tuple(1 if m in cmb else 0 for m in range(K)): F(1) for cmb in combinations(range(K), j)}
    expected = {
        1: {(1,): F(-1, 24)},
        2: {(1, 1): F(7, 5760), (2,): F(-4, 5760)},
        3: {(1, 1, 1): F(-31, 967680), (2, 1): F(44, 967680), (3,): F(-16, 967680)},
        4: {(1, 1, 1, 1): F(381, 464486400), (2, 1, 1): F(-904, 464486400), (2, 2): F(208, 464486400),
            (3, 1): F(512, 464486400), (4,): F(-192, 464486400)},
    }
    for j in range(1, N + 1):
        acc = {}
        for lam, coef in expected[j].items():
            m = {tuple([0] * K): F(1)}
            for part in lam:
                m = pm(m, E[part])
            for e, v in m.items():
                acc[e] = acc.get(e, F(0)) + coef * v
        acc = {e: v for e, v in acc.items() if v != 0}
        target = {e: v for e, v in P.items() if sum(e) == j}
        assert acc == target and target
        assert all(v != 0 for v in expected[j].values())
    for n in range(2, 15, 2):
        deg = n + 2
        has_pont = deg % 4 == 0
        assert has_pont == (n % 4 == 2)
    GA.check("(d) A-hat degree-4j parts j = 1..4 exact and nonzero; degree n+2 nonzero iff n = 2 mod 4", True)
    # (e) pure-gauge exponent (n+2)/2: even iff n = 2 mod 4
    for n in range(2, 15, 2):
        k = (n + 2) // 2
        assert (k % 2 == 0) == (n % 4 == 2)
    samples = [[F(1), F(-1), F(0), F(0)], [F(3), F(-1), F(-1), F(-1)], [F(1, 2), F(1, 3), F(-5, 6), F(0)]]
    for X in samples:
        for k in (2, 4, 6):
            rep = sum(x ** k for x in X)
            conj = sum((-x) ** k for x in X)
            assert rep > 0 and conj == rep and rep + conj > 0
        for k in (3,):
            assert sum(x ** k for x in X) + sum((-x) ** k for x in X) == 0
    for charges in ([F(1)], [F(2, 3), F(-1, 3)], [F(1), F(-1), F(1, 2)]):
        assert sum(qq ** 4 for qq in charges) > 0 and sum(qq ** 2 for qq in charges) > 0
    GA.check("(e) n = 2 mod 4: pure-gauge exponent even, conjugates add, positive on nonzero weights", True)
    return True


def check_two_dimensional_fields():
    premise("dark-matter.sourcing-rule-forced-not-chosen")

    def R_conformal(a):
        a1 = pderiv(a)
        a2 = pderiv(a1)
        num = pmul(pconst(2), padd(pmul(a, a2), pneg(pmul(a1, a1))))
        return num, pmul(pmul(a, a), pmul(a, a))

    # a = eta^k in conformal time: (k, eta, R, dR/deta)
    table = [(1, F(1), F(-2), F(8)), (1, F(2), F(-1, 8), F(1, 4)),
             (2, F(1), F(-4), F(24)), (2, F(2), F(-1, 16), F(3, 16))]
    for k, eta, Rx, dRx in table:
        a = [F(0)] * k + [F(1)]
        num, den = R_conformal(a)
        dnum = padd(pmul(pderiv(num), den), pneg(pmul(num, pderiv(den))))
        dden = pmul(den, den)
        assert peval(num, eta) / peval(den, eta) == Rx
        assert peval(dnum, eta) / peval(dden, eta) == dRx
    # de Sitter, a = -1/(H eta): R = 2 H^2 at every eta
    for H, Rx in ((F(1), F(2)), (F(3), F(18))):
        vals = set()
        for eta in (F(-1), F(-2), F(-7, 3)):
            a = -1 / (H * eta)
            ap = 1 / (H * eta ** 2)
            app = -2 / (H * eta ** 3)
            vals.add(2 * (a * app - ap * ap) / a ** 4)
        assert vals == {Rx}
    # Schwarzschild t-r plane: f = 1 - 2 M u, u = 1/r, d/dr = -u^2 d/du; R = -f''
    for M, r, Rx, dRx in ((F(1), F(2), F(1, 2), F(-3, 4)), (F(3, 2), F(3), F(2, 9), F(-2, 9))):
        f = [F(1), -2 * M]
        u2 = [F(0), F(0), F(1)]
        fr = pneg(pmul(u2, pderiv(f)))
        frr = pneg(pmul(u2, pderiv(fr)))
        R = pneg(frr)
        dR = pneg(pmul(u2, pderiv(R)))
        assert peval(R, 1 / r) == Rx and peval(dR, 1 / r) == dRx
    GA.check("(f) induced plane fields: radiation and matter eras and the Schwarzschild t-r plane have "
             "non-constant R; de Sitter has constant R = 2 H^2", True)
    return True
