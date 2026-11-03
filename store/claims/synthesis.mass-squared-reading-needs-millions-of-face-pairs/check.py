"""Pair-number bound for the mass-squared reading on the span of face words: exact checks.

By the stored Proposition synthesis.pair-singlet-mass-form-is-floor-plus-face-density, for a state on the
span S of face-word monomials Omega^{dag m}|0> (coefficients c_m, D = |m|):
norm = sum |c_m|^2 (D+1)! m!, f = 1 + <D>/2 (the floor), H = f 1 + G with
G_kl = (1/norm) sum_m conj(c_m) c_{m'} (D+1)! m_k m'_l (m - e_k)! (D + 3/2), m' = m - e_k + e_l,
and tr H = 3 + 3<D> + <D^2>. Complex coefficients are Gaussian rationals (pairs of Fractions).
(1) On random states supported on D <= 3: tr H = 3 + 3<D> + <D^2>, G >= 0 (principal minors), and
    (tr H - f)/f <= 2K + 1 + 2/(K + 2) with K the largest pair number in the support; equality on z_1^K.
(2) (2 + 5D/2 + D^2)/(1 + D/2) = 2D + 1 + 2/(D + 2), strictly increasing on D >= 0.
(3) With the stored masses (three standard deviations), (m_mu^2 + m_tau^2)/m_e^2 > 2K + 1 + 2/(K + 2)
    for every K <= 6065573, and not for K = 6065574.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise, quantity


class C(object):
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re, self.im = F(re), F(im)

    def __add__(self, o): return C(self.re + o.re, self.im + o.im)
    def __mul__(self, o): return C(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    def sc(self, t): return C(self.re * t, self.im * t)
    def conj(self): return C(self.re, -self.im)
    def n2(self): return self.re * self.re + self.im * self.im


Z = C(0)


def fact(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def mfact(m): return fact(m[0]) * fact(m[1]) * fact(m[2])


def mass_form(coef):
    norm = sum(c.n2() * fact(sum(m) + 1) * mfact(m) for m, c in coef.items())
    dmean = sum(c.n2() * fact(sum(m) + 1) * mfact(m) * sum(m) for m, c in coef.items()) / norm
    d2 = sum(c.n2() * fact(sum(m) + 1) * mfact(m) * sum(m) ** 2 for m, c in coef.items()) / norm
    G = [[Z] * 3 for _ in range(3)]
    for k in range(3):
        for l in range(3):
            s = Z
            for m, c in coef.items():
                if not m[k]:
                    continue
                mp = list(m); mp[k] -= 1; mp[l] += 1; mp = tuple(mp)
                if mp not in coef:
                    continue
                D = sum(m)
                base = list(m); base[k] -= 1
                w = fact(D + 1) * m[k] * mp[l] * mfact(base) * (F(D) + F(3, 2))
                s = s + (c.conj() * coef[mp]).sc(w)
            G[k][l] = s.sc(1 / norm)
    f = 1 + dmean / 2
    return f, G, dmean, d2


def psd3(G):
    """Hermitian 3x3 over Q(i): all principal minors >= 0."""
    d = [G[i][i].re for i in range(3)]
    m2 = [(G[i][i] * G[j][j] + (G[i][j] * G[j][i]).sc(-1)).re for i, j in [(0, 1), (0, 2), (1, 2)]]
    a, b, c = G[0][0], G[0][1], G[0][2]
    dd, e, ff = G[1][1], G[1][2], G[2][2]
    det = (a * (dd * ff + (e * G[2][1]).sc(-1)) + (b * (G[1][0] * ff + (e * G[2][0]).sc(-1))).sc(-1)
           + c * (G[1][0] * G[2][1] + (dd * G[2][0]).sc(-1))).re
    herm = all(G[i][j].re == G[j][i].re and G[i][j].im == -G[j][i].im for i in range(3) for j in range(3))
    return herm and min(d) >= 0 and min(m2) >= 0 and det >= 0


def lcg(seed):
    while True:
        seed = (1103515245 * seed + 12345) % 2147483648
        yield seed


def bound(K): return 2 * K + 1 + F(2, K + 2)


def check_ratio_bound_on_the_span_of_face_words():
    premise("synthesis.pair-singlet-mass-form-is-floor-plus-face-density")
    g = lcg(11)
    monos = [m for m in product(range(4), repeat=3) if sum(m) <= 3]
    ok_tr, ok_psd, ok_bd = True, True, True
    for trial in range(12):
        coef = {}
        for m in monos:
            if next(g) % 3 == 0:
                coef[m] = C(F(next(g) % 11 - 5, 1 + next(g) % 4), F(next(g) % 9 - 4, 1 + next(g) % 3))
        coef = {m: c for m, c in coef.items() if c.n2() != 0}
        if not coef:
            continue
        K = max(sum(m) for m in coef)
        f, G, dm, d2 = mass_form(coef)
        trH = 3 * f + sum(G[i][i].re for i in range(3))
        ok_tr &= trH == 3 + 3 * dm + d2
        ok_psd &= psd3(G)
        ok_bd &= (trH - f) / f <= bound(K)
    GA.check("(i) tr H = 3 + 3<D> + <D^2> on twelve random states supported on D <= 3", ok_tr)
    GA.check("(i) G = H - f 1 is positive semidefinite (principal minors), so every eigenvalue is >= f", ok_psd)
    GA.check("(i) (tr H - f)/f <= 2K + 1 + 2/(K + 2) on the same states", ok_bd)
    f, G, dm, d2 = mass_form({(1, 0, 0): C(1), (0, 1, 0): C(0, 1), (1, 1, 0): C(2), (0, 0, 2): C(1, -1)})
    trH = 3 * f + sum(G[i][i].re for i in range(3))
    GA.check("(i) fingerprint state: f = 51/26, <D> = 25/13, <D^2> = 49/13, G diag (89/52, 89/52, 42/13), "
             "G_12 = 5i/52, tr H = 163/13, ratio 275/51 <= 2*2 + 1 + 1/2",
             (f, dm, d2, trH, (trH - f) / f) == (F(51, 26), F(25, 13), F(49, 13), F(163, 13), F(275, 51))
             and [G[i][i].re for i in range(3)] == [F(89, 52), F(89, 52), F(42, 13)]
             and (G[0][1].re, G[0][1].im) == (F(0), F(5, 52)) and psd3(G) and F(275, 51) <= bound(2))
    f, G, dm, d2 = mass_form({(3, 0, 0): C(1)})
    trH = 3 * f + sum(G[i][i].re for i in range(3))
    GA.check("(i) equality at the word z_1^3: (tr H - f)/f = 2*3 + 1 + 2/5 = 37/5, floor attained twice",
             (trH - f) / f == bound(3) == F(37, 5) and G[1][1].re == 0 and G[2][2].re == 0)


def check_extreme_point_function_is_increasing():
    premise("synthesis.pair-singlet-mass-form-is-floor-plus-face-density")
    ok = all((2 + F(5, 2) * D + D * D) / (1 + F(D, 2)) == bound(D) for D in range(0, 60))
    ok &= all(bound(D + 1) > bound(D) for D in range(0, 60))
    GA.check("(ii) (2 + 5D/2 + D^2)/(1 + D/2) = 2D + 1 + 2/(D + 2), increasing (D = 0..60)", ok)
    GA.check("(ii) values at D = 0, 1, 2: 2, 11/3, 11/2", [bound(0), bound(1), bound(2)] == [F(2), F(11, 3), F(11, 2)])


def check_threshold_from_the_stored_masses():
    premise("synthesis.pair-singlet-mass-form-is-floor-plus-face-density")
    me = quantity("quantity.electron-mass")
    mm = quantity("quantity.muon-mass")
    mt = quantity("quantity.tau-mass")
    r_min = ((mm - 3 * F(23, 10 ** 7)) ** 2 + (mt - 3 * F(9, 100)) ** 2) / (me + F(1, 10 ** 9)) ** 2
    r_max = ((mm + 3 * F(23, 10 ** 7)) ** 2 + (mt + 3 * F(9, 100)) ** 2) / (me - F(1, 10 ** 9)) ** 2
    GA.check("(iii) (m_mu^2 + m_tau^2)/m_e^2 in (12131147, 12138498) at three standard deviations",
             F(12131147) < r_min < r_max < F(12138498))
    GA.check("(iii) every state supported on D <= 6065573 falls short; K = 6065574 is the first that can reach",
             bound(6065573) < r_min <= bound(6065574))


if __name__ == "__main__":
    for fn in [check_ratio_bound_on_the_span_of_face_words, check_extreme_point_function_is_increasing,
               check_threshold_from_the_stored_masses]:
        fn()
    print("FAILURES", GA.FAILURES)
