"""synthesis.pair-singlet-mass-form-is-floor-plus-face-density: exact checks.

Exact arithmetic over Q(i) (GA.QI) in the six-mode bosonic Fock space of the skeleton theorem, in
the unnormalised occupation basis (|m> = prod (a_p^dag)^{m_p} |0>, norm prod m_p!). Face operators
Omega_k = (1/2) eps_kij eps_AB a_iA a_jB, family density rho_lk = sum_A a^dag_lA a_kA, number N, and the
mass form H_kl = (1/2) <Omega_k^dag Omega_l + Omega_l Omega_k^dag> of the stored mass-form result.
  (1) the face-word monomials Om^{dag m}|0> (D = |m| <= 3) are orthogonal with norm (D+1)! m!, and
      Omega_l, rho_lk and V = sum_k Omega_k^dag Omega_k act on them by the stated formulas;
  (2) on five non-Gaussian superpositions with complex rational coefficients H equals
      (1 + <D>/2) 1 + G, G_kl = sum (D + 3/2) <z_k psi_D, z_l psi_D> in the auxiliary boson picture;
  (3) in the normal frame of the stored Z2 result (c = (1, a, ia), a = 1 and a = 2/3) every tested state
      built from Omega(c)^dag, Omega(cbar)^dag and V is annihilated by Omega(n), n = c_R x c_I, has
      H n = (1 + <D>/2) n, and has n strictly lowest when the light pair is split; the stored values
      h_n = 32/17, 145/77, 505/257, 55/32 are reproduced as 1 + <D>/2;
  (4) the trace identity tr H = 3 + 3<D> + <D^2> on the singlet span, hence the heavy-pair sum rule.
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

QI = GA.QI
MODES = [(i, A) for i in range(3) for A in range(2)]
IDX = {m: p for p, m in enumerate(MODES)}
Z = QI(0)
ONE = QI(1)


def eps3(k, i, j):
    if len({k, i, j}) < 3:
        return 0
    return 1 if (k, i, j) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)] else -1


def eps2(A, B):
    return 0 if A == B else (1 if (A, B) == (0, 1) else -1)


THETA = [[[F(1, 2) * eps3(k, p[0], q[0]) * eps2(p[1], q[1]) for q in MODES] for p in MODES] for k in range(3)]


def fact(n):
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out


def iszero(x):
    return x.re == 0 and x.im == 0


def qeq(x, y):
    return x.re == y.re and x.im == y.im


def sadd(s, m, co):
    v = s.get(m, Z) + co
    if iszero(v):
        s.pop(m, None)
    else:
        s[m] = v


def ann(p, st):
    out = {}
    for m, co in st.items():
        if m[p]:
            mm = list(m)
            mm[p] -= 1
            sadd(out, tuple(mm), co * m[p])
    return out


def cre(p, st):
    out = {}
    for m, co in st.items():
        mm = list(m)
        mm[p] += 1
        sadd(out, tuple(mm), co)
    return out


def lin(terms):
    out = {}
    for coef, st in terms:
        for m, co in st.items():
            sadd(out, m, coef * co)
    return out


def inner(s, t):
    tot = Z
    for m, co in s.items():
        if m in t:
            w = 1
            for x in m:
                w *= fact(x)
            tot = tot + co.conj() * t[m] * w
    return tot


def omega(k, st):
    return lin([(QI(THETA[k][p][q]), ann(p, ann(q, st))) for p in range(6) for q in range(6) if THETA[k][p][q]])


def omega_dag(k, st):
    return lin([(QI(THETA[k][p][q]), cre(q, cre(p, st))) for p in range(6) for q in range(6) if THETA[k][p][q]])


def omega_vec(cv, st):
    """Omega(c) = sum_k c_k Omega_k."""
    return lin([(cv[k], omega(k, st)) for k in range(3) if not iszero(cv[k])])


def omega_vec_dag(cv, st):
    """Omega(c)^dag = sum_k conj(c_k) Omega_k^dag."""
    return lin([(cv[k].conj(), omega_dag(k, st)) for k in range(3) if not iszero(cv[k])])


def rho(l, k, st):
    return lin([(ONE, cre(IDX[(l, A)], ann(IDX[(k, A)], st))) for A in range(2)])


def vac():
    return {tuple([0] * 6): ONE}


def V(st):
    return lin([(ONE, omega_dag(k, omega(k, st))) for k in range(3)])


def mono(m):
    st = vac()
    for k in range(3):
        for _ in range(m[k]):
            st = omega_dag(k, st)
    return st


def steq(a, b):
    return not lin([(ONE, a), (QI(-1), b)])


def mass_form(psi):
    Om = [omega(k, psi) for k in range(3)]
    Od = [omega_dag(k, psi) for k in range(3)]
    H = [[(inner(Om[k], Om[l]) + inner(Od[l], Od[k])) * F(1, 2) for l in range(3)] for k in range(3)]
    return H, inner(psi, psi)


def mfact(m):
    return fact(m[0]) * fact(m[1]) * fact(m[2])


def predicted(coef):
    """Norm, <D> (unnormalised), and G (unnormalised) from the monomial coefficients."""
    norm = Z
    dsum = Z
    d2sum = Z
    for m, c in coef.items():
        D = sum(m)
        w = c.conj() * c * (fact(D + 1) * mfact(m))
        norm = norm + w
        dsum = dsum + w * D
        d2sum = d2sum + w * (D * D)
    G = [[Z] * 3 for _ in range(3)]
    for k in range(3):
        for l in range(3):
            s = Z
            for m, c in coef.items():
                if not m[k]:
                    continue
                mp = list(m)
                mp[k] -= 1
                mp[l] += 1
                mp = tuple(mp)
                if mp not in coef:
                    continue
                D = sum(m)
                base = list(m)
                base[k] -= 1
                w = fact(D + 1) * m[k] * mp[l] * mfact(base)
                s = s + c.conj() * coef[mp] * w * (F(D) + F(3, 2))
            G[k][l] = s
    return norm, dsum, d2sum, G


MONOS = [m for m in product(range(4), repeat=3) if sum(m) <= 3]


def check_face_word_monomial_algebra():
    premise("families.skeleton-rank-one-plus-ordering-shift")
    premise("families.imported-squeezed-vacuum-bosonic-pairing")
    ok = True
    st = {m: mono(m) for m in MONOS}
    for m in MONOS:
        D = sum(m)
        for m2 in MONOS:
            ip = inner(st[m], st[m2])
            exp = fact(D + 1) * mfact(m) if m == m2 else 0
            ok = ok and ip.re == exp and ip.im == 0
        for l in range(3):
            if m[l]:
                mm = list(m)
                mm[l] -= 1
                rhs = lin([(QI((D + 1) * m[l]), mono(tuple(mm)))])
            else:
                rhs = {}
            ok = ok and steq(omega(l, st[m]), rhs)
            for k in range(3):
                terms = []
                if k == l:
                    terms.append((QI(D), st[m]))
                if m[l]:
                    mm = list(m)
                    mm[l] -= 1
                    mm[k] += 1
                    terms.append((QI(-m[l]), mono(tuple(mm))))
                ok = ok and steq(rho(l, k, st[m]), lin(terms))
        ok = ok and steq(V(st[m]), lin([(QI(D * (D + 1)), st[m])]))
    GA.check("face-word monomials: norms (D+1)! m!, Omega_l, rho_lk and V act by the stated formulas", ok)
    return ok


SAMPLES = [
    {(0, 0, 0): QI(1), (1, 0, 0): QI(2, 1), (0, 1, 1): QI(F(1, 3), -1), (2, 1, 0): QI(0, F(1, 2))},
    {(1, 1, 0): QI(1), (0, 0, 2): QI(-1, 3), (1, 1, 1): QI(F(2, 5), 1), (3, 0, 0): QI(1, 1), (0, 1, 0): QI(F(-1, 2))},
    {(0, 0, 0): QI(1), (0, 1, 0): QI(1), (1, 0, 0): QI(0, 1), (0, 2, 0): QI(F(1, 2)), (1, 1, 0): QI(F(2, 3)), (2, 0, 0): QI(F(-1, 2))},
    {(2, 0, 1): QI(1, -2), (0, 2, 1): QI(3), (1, 0, 2): QI(F(1, 7), 1)},
    {(0, 0, 0): QI(F(1, 2)), (1, 1, 1): QI(1), (0, 3, 0): QI(0, -1), (0, 0, 3): QI(2, F(1, 3))},
]


def check_mass_form_is_floor_plus_weighted_density():
    premise("synthesis.face-mass-form-unit-plus-gram")
    premise("families.skeleton-rank-one-plus-ordering-shift")
    premise("synthesis.cumulants-at-fixed-second-moments-keep-the-floor")
    ok = True
    for coef in SAMPLES:
        psi = lin([(c, mono(m)) for m, c in coef.items()])
        H, n = mass_form(psi)
        norm, dsum, d2sum, G = predicted(coef)
        ok = ok and qeq(n, norm)
        trH = Z
        for k in range(3):
            trH = trH + H[k][k]
            for l in range(3):
                exp = G[k][l] + (norm + dsum * F(1, 2) if k == l else Z)
                ok = ok and qeq(H[k][l], exp)
                # G is Hermitian
                ok = ok and qeq(G[k][l], G[l][k].conj())
        # trace identity tr H = 3 + 3<D> + <D^2> (unnormalised)
        ok = ok and qeq(trH, norm * 3 + dsum * 3 + d2sum)
        # leading principal minors of G are nonnegative (G is a Gram matrix)
        g11 = G[0][0]
        g2 = G[0][0] * G[1][1] - G[0][1] * G[1][0]
        ok = ok and g11.im == 0 and g11.re >= 0 and g2.im == 0 and g2.re >= 0
    GA.check("H = (1 + <D>/2) 1 + G on five non-Gaussian singlet states, entrywise; tr H = 3 + 3<D> + <D^2>", ok)
    return ok


def poly_state(words):
    """words: list of (coefficient, list of face vectors y, power of V): coef * V^p prod Omega(y)^dag |0>."""
    out = {}
    for coef, ys, p in words:
        st = vac()
        for y in ys:
            st = omega_vec_dag(y, st)
        for _ in range(p):
            st = V(st)
        out = lin([(ONE, out), (coef, st)])
    return out


def mat_apply(H, v):
    return [sum((H[k][l] * v[l] for l in range(3)), Z) for k in range(3)]


def check_forced_eigenvector_is_lowest_in_source_built_states():
    premise("synthesis.real-structure-breaks-source-stabiliser-to-z2")
    premise("synthesis.face-mass-form-unit-plus-gram")
    ok = True
    results = []
    for a in (F(1), F(2, 3)):
        c = [QI(1), QI(a), QI(0, a)]
        cb = [x.conj() for x in c]
        n = [QI(a), QI(-1), QI(0)]          # proportional to c_R x c_I = (a^2, -a, 0)
        cR = [QI(1), QI(a), QI(0)]
        cI = [QI(0), QI(0), QI(a)]
        states = [
            ("single", [(ONE, [], 0), (ONE, [c], 0), (QI(F(1, 2)), [c, c], 0)]),
            ("real1", [(ONE, [], 0), (ONE, [c], 0), (ONE, [cb], 0), (QI(1), [c, cb], 0)]),
            ("real2", [(ONE, [], 0), (ONE, [c], 0), (ONE, [cb], 0), (QI(2), [c, cb], 0)]),
            ("realm", [(ONE, [], 0), (ONE, [c], 0), (ONE, [cb], 0), (QI(F(-1, 2)), [c, cb], 0)]),
            ("two", [(ONE, [], 0), (ONE, [c], 0), (QI(F(2, 3)), [c, cb], 0)]),
            ("mixV", [(QI(1, 1), [c], 0), (QI(F(1, 3), -1), [cb, cb], 1), (QI(0, 2), [c, cb, c], 0)]),
            ("deg3", [(QI(2), [cb], 0), (QI(-1, F(1, 2)), [c, c, cb], 0), (QI(F(1, 5)), [cb, cb, cb], 1)]),
        ]
        for name, words in states:
            psi = poly_state(words)
            ok = ok and not omega_vec(n, psi)          # Omega(n) psi = 0
            H, nn = mass_form(psi)
            # <D> from the number operator: N = 2D on the singlet span
            num = lin([(ONE, cre(p, ann(p, psi))) for p in range(6)])
            Dbar = inner(psi, num) * F(1, 2)
            hn = nn + Dbar * F(1, 2)                   # unnormalised floor
            Hn = mat_apply(H, n)
            ok = ok and all(qeq(Hn[k], n[k] * hn) for k in range(3))
            # block on n-perp in the real basis cR, cI (not orthonormal): compare via B - h_n Gram
            basis = [cR, cI]
            Bm = [[sum((basis[i][k].conj() * mat_apply(H, basis[j])[k] for k in range(3)), Z) for j in range(2)] for i in range(2)]
            Gm = [[sum((basis[i][k].conj() * basis[j][k] for k in range(3)), Z) for j in range(2)] for i in range(2)]
            X = [[Bm[i][j] - Gm[i][j] * hn for j in range(2)] for i in range(2)]   # PSD exactly when n is lowest
            det = X[0][0] * X[1][1] - X[0][1] * X[1][0]
            tr = X[0][0] + X[1][1]
            ok = ok and det.im == 0 and tr.im == 0 and det.re >= 0 and tr.re > 0
            results.append((a, name, hn.re / nn.re, det.re == 0))
    by = {(a, nm): (h, deg) for a, nm, h, deg in results}
    ok = ok and by[(F(1), "single")] == (F(32, 17), True)
    ok = ok and by[(F(1), "real1")] == (F(145, 77), False)
    ok = ok and by[(F(1), "real2")][0] == F(505, 257) and by[(F(1), "realm")][0] == F(55, 32)
    ok = ok and by[(F(1), "two")] == (F(190, 101), False)
    ok = ok and not by[(F(2, 3), "mixV")][1] and not by[(F(1), "deg3")][1]
    # a word in the forced direction itself moves n off the floor (stored instance: h_n = 1738/199, on top)
    c = [QI(1), QI(1), QI(0, 1)]
    n = [QI(1), QI(-1), QI(0)]
    psi = poly_state([(ONE, [], 0), (ONE, [c], 0), (QI(2), [n, n], 0)])
    H, nn = mass_form(psi)
    Hn = mat_apply(H, n)
    hn_val = Hn[0].re / n[0].re / nn.re
    num = lin([(ONE, cre(p, ann(p, psi))) for p in range(6)])
    floor = 1 + inner(psi, num).re / nn.re / 4
    ok = ok and hn_val == F(1738, 199) and hn_val > floor and bool(omega_vec(n, psi))
    GA.check("source-built states: Omega(n) psi = 0, H n = (1 + <D>/2) n at the floor, n lowest, stored h_n reproduced", ok)
    return ok
