"""synthesis.operator-join-has-no-zero-modes-on-positive-energy-modules: exact checks.

Positive-energy (oscillator) model of two constituents: bosonic modes a_{iA}, c_{iA} (i = constituent, A = spinor
index), unnormalised basis |n> = prod (x^dag)^{n_x}|0>, so x|n> = n_x|n - e_x>, x^dag|n> = |n + e_x>,
<n|n> = prod n_x!. Store components: omega = (Z^0, Z^1), pi = (Z^2, Z^3), pibar_A = Zbar_A, omegabar = Zbar_{2,3}.
With s^2 = sig:  Z^A = s(a_A + c_A^dag)/sqrt2,  Z^{2+A} = (a_A - c_A^dag)/(sqrt2 s),
                 Zbar_A = (Z^{2+A})^dag = (a_A^dag - c_A)/(sqrt2 s),  Zbar_{2+A} = (Z^A)^dag = s(a_A^dag + c_A)/sqrt2.
Every operator used is a sum of products of two Z or Zbar, so coefficients are rational (1/2) sig^{0, +-1}.
B = <pi^1 pi^2> + lam [omega^1 omega^2], Bdag its conjugate (store's convention), lam = Lambda/6, hbar = 1;
h_il = (Zbar_i.Z^l + Z^l.Zbar_i)/2; C = (1/2) sum h_il h_li - (1/4)(tr h)^2;
m2 = Bdag B + B Bdag + (Lambda/3) C - (2 Lambda/3) (the stored palatial form, N = 2).
Pair form (lam sig^2 = 1): B = sqrt(lam) (det a + det c^dag); K- = B/sqrt(lam), K+ = Bdag/sqrt(lam), K0 = tr h/2,
C_sl = K0^2 - K0 - K+ K-, and m2 = (Lambda/3)(K0^2 - C_sl + C - 2).
Runs at (Lambda, sig) = (6, 1) (sqrt lam = 1) and (3/2, 2) (sqrt lam = 1/2).
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

MODES = [(k, i, A) for k in "ac" for i in (0, 1) for A in (0, 1)]
IDX = {m: n for n, m in enumerate(MODES)}
NM = len(MODES)


def _fact(n):
    p = 1
    for t in range(2, n + 1):
        p *= t
    return p


def vadd(*vs):
    out = {}
    for v in vs:
        for k, x in v.items():
            out[k] = out.get(k, F(0)) + x
    return {k: x for k, x in out.items() if x != 0}


def vsc(c, v):
    return {k: c * x for k, x in v.items() if c * x != 0}


def low(m):
    j = IDX[m]

    def f(v):
        out = {}
        for k, x in v.items():
            if k[j]:
                kk = list(k)
                kk[j] -= 1
                kk = tuple(kk)
                out[kk] = out.get(kk, F(0)) + k[j] * x
        return out
    return f


def rai(m):
    j = IDX[m]

    def f(v):
        out = {}
        for k, x in v.items():
            kk = list(k)
            kk[j] += 1
            kk = tuple(kk)
            out[kk] = out.get(kk, F(0)) + x
        return out
    return f


def comp(*ops):
    def f(v):
        for o in reversed(ops):
            v = o(v)
        return v
    return f


def lin(*terms):
    return lambda v: vadd(*[vsc(c, o(v)) for c, o in terms])


def ident(v):
    return dict(v)


def inner(u, v):
    tot = F(0)
    for k, x in u.items():
        if k in v:
            w = 1
            for n in k:
                w *= _fact(n)
            tot += x * v[k] * w
    return tot


def zeta(i, al):
    """(weight exponent, [(coef, op)]) for sqrt2 Z^al_i, weight s^e."""
    A = al % 2
    a, c = ("a", i, A), ("c", i, A)
    if al < 2:
        return 1, [(F(1), low(a)), (F(1), rai(c))]
    return -1, [(F(1), low(a)), (F(-1), rai(c))]


def zetabar(i, al):
    A = al % 2
    a, c = ("a", i, A), ("c", i, A)
    if al < 2:
        return -1, [(F(1), rai(a)), (F(-1), low(c))]
    return 1, [(F(1), rai(a)), (F(1), low(c))]


class Model:
    def __init__(self, LAM, sig):
        self.LAM, self.sig = LAM, sig
        self.lam = LAM / 6

        def prod2(X, Y, extra=F(1)):
            (e1, t1), (e2, t2) = X, Y
            w = {-2: 1 / sig, 0: F(1), 2: sig}[e1 + e2]
            return lin(*[(extra * F(1, 2) * w * cx * cy, comp(ox, oy)) for cx, ox in t1 for cy, oy in t2])
        self.prod2 = prod2

        def br(Xf, i, l, a, b):
            return lin((F(1), prod2(Xf(i, a), Xf(l, b))), (F(-1), prod2(Xf(i, b), Xf(l, a))))
        self.b = br(zeta, 0, 1, 2, 3)
        self.om = br(zeta, 0, 1, 0, 1)
        self.bd = br(zetabar, 0, 1, 0, 1)
        self.omd = br(zetabar, 0, 1, 2, 3)
        self.B = lin((F(1), self.b), (self.lam, self.om))
        self.Bd = lin((F(1), self.bd), (self.lam, self.omd))

        def h(i, l):
            terms = []
            for al in range(4):
                terms.append((F(1, 2), prod2(zetabar(i, al), zeta(l, al))))
                terms.append((F(1, 2), prod2(zeta(l, al), zetabar(i, al))))
            return lin(*terms)
        self.H = [[h(i, l) for l in range(2)] for i in range(2)]
        H = self.H
        self.trh = lin((F(1), H[0][0]), (F(1), H[1][1]))
        self.C = lin(*([(F(1, 2), comp(H[i][l], H[l][i])) for i in range(2) for l in range(2)]
                       + [(F(-1, 4), comp(self.trh, self.trh))]))
        L3 = LAM / 3
        self.m2 = lin((F(1), comp(self.Bd, self.B)), (F(1), comp(self.B, self.Bd)), (L3, self.C), (-2 * L3, ident))


def det_a():
    return lin((F(1), comp(low(("a", 0, 0)), low(("a", 1, 1)))), (F(-1), comp(low(("a", 0, 1)), low(("a", 1, 0)))))


def det_cd():
    return lin((F(1), comp(rai(("c", 0, 0)), rai(("c", 1, 1)))), (F(-1), comp(rai(("c", 0, 1)), rai(("c", 1, 0)))))


def det_ad():
    return lin((F(1), comp(rai(("a", 0, 0)), rai(("a", 1, 1)))), (F(-1), comp(rai(("a", 0, 1)), rai(("a", 1, 0)))))


def Na(v):
    return vadd(*[vsc(F(sum(k[0:4])), {k: x}) for k, x in v.items()])


def Nc(v):
    return vadd(*[vsc(F(sum(k[4:8])), {k: x}) for k, x in v.items()])


def basis(maxtot):
    return [k for k in product(range(maxtot + 1), repeat=NM) if sum(k) <= maxtot]


SAMPLE = [k for n, k in enumerate(basis(2)) if n % 3 == 0] + [(1, 0, 0, 1, 0, 1, 1, 0), (0, 2, 0, 0, 1, 0, 0, 1)]


def check_positive_energy_module_is_the_stored_oscillator_model():
    premise("field-theory.twistor-attachment")
    premise("synthesis.operator-join-ordering-constants")
    ncheck = 0
    for LAM, sig in [(F(6), F(1)), (F(3, 2), F(2))]:
        M = Model(LAM, sig)
        # canonical relations [Z^al_i, Zbar_{l be}] = delta delta and [Z, Z] = 0 (via products of two)
        for k in SAMPLE[:4]:
            v = {k: F(1)}
            for i, l in [(0, 0), (0, 1)]:
                for al in range(4):
                    for be in range(4):
                        zz = lin((F(1), M.prod2(zeta(i, al), zetabar(l, be))), (F(-1), M.prod2(zetabar(l, be), zeta(i, al))))
                        want = v if (i == l and al == be) else {}
                        GA.check("[Z, Zbar] = delta delta", zz(v) == want)
                        z2 = lin((F(1), M.prod2(zeta(i, al), zeta(l, be))), (F(-1), M.prod2(zeta(l, be), zeta(i, al))))
                        GA.check("[Z, Z] = 0", z2(v) == {})
                        ncheck += 1
        # the conjugate is the Hilbert adjoint: <u, B v> = <Bdag u, v>, h_il^dag = h_li
        for k in SAMPLE[:10]:
            for k2 in SAMPLE[:10] + [(0, 0, 0, 0, 1, 0, 0, 1), (1, 0, 0, 1, 0, 0, 0, 0)]:
                u, v = {k2: F(1)}, {k: F(1)}
                GA.check("Bdag is the adjoint of B", inner(u, M.B(v)) == inner(M.Bd(u), v))
                GA.check("h_12 adjoint is h_21", inner(u, M.H[0][1](v)) == inner(M.H[1][0](u), v))
                ncheck += 1
    GA.check("number of relations checked", ncheck == 2 * (4 * 2 * 16 + 10 * 12))
    # one constituent: helicity N_a - N_c, energy levels |s| + 1 + n with multiplicity (n+1)(n+2|s|+1)
    counts = []
    for two_s in range(-3, 4):
        for n in range(3):
            cnt = 0
            for na in product(range(8), repeat=2):
                for nc in product(range(8), repeat=2):
                    if sum(na) - sum(nc) == two_s and sum(na) + sum(nc) == abs(two_s) + 2 * n:
                        cnt += 1
            counts.append(cnt)
    GA.check("helicity module multiplicities (n+1)(n+2|s|+1), tabulated",
             counts == [4, 10, 18, 3, 8, 15, 2, 6, 12, 1, 4, 9, 2, 6, 12, 3, 8, 15, 4, 10, 18])
    return True


def check_bracket_is_pair_form():
    premise("mass.exact-join")
    premise("synthesis.operator-join-ordering-constants")
    for LAM, sig, rl in [(F(6), F(1), F(1)), (F(3, 2), F(2), F(1, 2))]:
        M = Model(LAM, sig)
        Bp = lin((rl, det_a()), (rl, det_cd()))
        for k in SAMPLE:
            v = {k: F(1)}
            GA.check("B = sqrt(lam)(det a + det c^dag)", M.B(v) == Bp(v))
            GA.check("tr h = N_a - N_c", M.trh(v) == vadd(Na(v), vsc(F(-1), Nc(v))))
            GA.check("[B, Bdag] = lam tr h",
                     vadd(M.B(M.Bd(v)), vsc(F(-1), M.Bd(M.B(v)))) == vsc(LAM / 6, M.trh(v)))
    return True


def check_join_is_casimir_form():
    premise("synthesis.operator-join-ordering-constants")
    premise("synthesis.operator-join-casimir-shifts")
    for LAM, sig, rl in [(F(6), F(1), F(1)), (F(3, 2), F(2), F(1, 2))]:
        M = Model(LAM, sig)
        Km = lin((1 / rl, M.B))
        Kp = lin((1 / rl, M.Bd))
        K0 = lin((F(1, 2), M.trh))
        Csl = lin((F(1), comp(K0, K0)), (F(-1), K0), (F(-1), comp(Kp, Km)))
        L3 = LAM / 3
        form = lin((L3, comp(K0, K0)), (-L3, Csl), (L3, M.C), (-2 * L3, ident))
        for k in SAMPLE:
            v = {k: F(1)}
            GA.check("m2 = (Lambda/3)(K0^2 - C_sl + C - 2)", M.m2(v) == form(v))
            GA.check("[K-, K+] = 2 K0", vadd(Km(Kp(v)), vsc(F(-1), Kp(Km(v)))) == vsc(F(2), K0(v)))
            GA.check("[K0, K-] = -K-", vadd(K0(Km(v)), vsc(F(-1), Km(K0(v)))) == vsc(F(-1), Km(v)))
        # internal Casimir C = j(j+1): (a_{00}^dag)^d |0> has j = d/2
        cas = [M.C({(d, 0, 0, 0, 0, 0, 0, 0): F(1)})[(d, 0, 0, 0, 0, 0, 0, 0)] for d in range(1, 4)]
        GA.check("C = j(j+1) on (a00^dag)^d|0>, tabulated", cas == [F(3, 4), F(2), F(15, 4)])
        singlet = vadd({(1, 0, 0, 0, 1, 0, 0, 0): F(1)}, {(0, 0, 1, 0, 0, 0, 1, 0): F(1)})
        GA.check("internal singlet of a and c has C = 0", M.C(singlet) == {})
    return True


def _a_states(d):
    return [k + (0, 0, 0, 0) for k in product(range(d + 1), repeat=4) if sum(k) == d]


def check_lowest_weights_and_gap():
    premise("synthesis.operator-join-ordering-constants")
    premise("mass.exact-join")
    # su(1,1)_a lowest weights: ker(A) on degree-d states of the a-modes, A = det a; dims tabulated (d+1)^2
    A = det_a()
    dims = []
    for d in range(5):
        src = _a_states(d)
        tgt = _a_states(d - 2) if d >= 2 else []
        rows = [[A({k: F(1)}).get(t, F(0)) for k in src] for t in tgt]
        dims.append(len(src) - (GA.mat_rank(rows) if rows else 0))
    GA.check("dim ker A in degree d = (d+1)^2", dims == [1, 4, 9, 16, 25])
    # the gap is attained: lowest weight of D+(1) inside D+(2)_a x D-(1)_c, j = 1, K0 = 1:
    # v = sum_p beta_p (A^dag)^p (a00^dag)^2 (C^dag)^p |0>, beta_p = -beta_{p-1}/(p(p+3))
    M = Model(F(6), F(1))
    beta = [F(1)]
    for p in range(1, 6):
        beta.append(-beta[-1] / (p * (p + 3)))
    GA.check("beta tabulated", beta == [F(1), F(-1, 4), F(1, 40), F(-1, 720), F(1, 20160), F(-1, 806400)])
    term = {(2, 0, 0, 0, 0, 0, 0, 0): F(1)}
    v = {}
    Ad, Cd = det_ad(), det_cd()
    for b in beta:
        v = vadd(v, vsc(b, term))
        term = Ad(Cd(term))
    by_level = lambda w: sorted(set(sum(k[0:4]) for k in w))
    kv = M.B(v)
    GA.check("K- v vanishes except at the truncation level", by_level(kv) == [12])
    res = vadd(M.m2(v), vsc(-M.LAM / 3, v))
    GA.check("m2 v = (Lambda/3) v except at the two truncation levels", by_level(res) == [12, 14])
    GA.check("C v = 2 v (j = 1)", M.C(v) == vsc(F(2), v))
    GA.check("K0 v = v", vsc(F(1, 2), M.trh(v)) == v)
    return True


def _is_halfint(x):
    return (2 * x).denominator == 1


def check_discrete_series_in_the_product():
    premise("synthesis.operator-join-seed-has-no-diagonal-matrix-elements")
    # D+(k1) (x) D-(k2), normalised bases |p>, |q>: K- = K-^a + K+^c. A lowest weight of K0 = kap lives on
    # q = p + k1 - k2 - kap; the coefficient of |p-1, q(p)> gives |al_p|^2 (p)(p + 2k1 - 1) = |al_{p-1}|^2 (q_{p-1}+1)(q_{p-1}+2k2).
    for k1 in [F(t, 2) for t in range(2, 11)]:
        for k2 in [F(t, 2) for t in range(2, 11)]:
            for n in range(-3, 5):
                kap = k1 - k2 - n
                p0 = max(0, -n)          # q(p) = p + n >= 0
                if n < 0:
                    # boundary: the state |p0 - 1, q(p0)> = |p0 - 1, 0> receives only al_{p0} sqrt(p0 (p0 + 2k1 - 1)) != 0
                    GA.check("no lowest weight above k1 - k2", p0 * (p0 + 2 * k1 - 1) != 0)
                    continue
                for p in range(1, 40):
                    q = p - 1 + n
                    r = F((q + 1) * (q + 2 * k2)) / (p * (p + 2 * k1 - 1))
                    # exact expansion r = 1 - 2 kap/p + n(n - 1 + 2k2)/(p (p + 2k1 - 1)) + 2kap(2k1 - 1)/(p(p + 2k1 - 1))
                    rhs = 1 - 2 * kap / p + (n * (n - 1 + 2 * k2) + 2 * kap * (2 * k1 - 1)) / (p * (p + 2 * k1 - 1))
                    GA.check("ratio expansion (Gauss test exponent 2 kap)", r == rhs)
                GA.check("kap in half-integers", _is_halfint(kap))
    return True


def check_no_zero_mode_and_gap():
    premise("synthesis.operator-join-ordering-constants")
    premise("synthesis.operator-join-seed-has-no-diagonal-matrix-elements")
    vals = []
    for tja in range(0, 13):
        for tjc in range(0, 13):
            ja, jc = F(tja, 2), F(tjc, 2)
            k1, k2 = ja + 1, jc + 1
            js = [abs(ja - jc) + t for t in range(int(ja + jc - abs(ja - jc)) + 1)]
            for n in range(0, 13):
                for kap in (k1 - k2 - n, k2 - k1 - n):
                    if kap <= F(1, 2):
                        continue
                    for p in range(0, 6):
                        K0sq = (kap + p) ** 2
                        for j in js:
                            GA.check("parity K0 = j mod 1", _is_halfint(kap + p - j) and (kap + p - j).denominator == 1)
                            val = K0sq - kap * (kap - 1) + j * (j + 1) - 2     # m2 / (Lambda hbar^2 / 3)
                            vals.append(val)
                            GA.check("no zero mode", val != 0)
    GA.check("point-spectrum minimum is 1 (m2 = Lambda hbar^2/3)", min(vals) == 1)
    # the zero-mode values c = K0^2 + j(j+1) - 2 below -1/4 occur only in sectors (0,0), (+-1,0), (+-1/2,1/2)
    low_sectors = []
    for tm in range(-8, 9):
        for tj in range(0, 9):
            m, j = F(tm, 2), F(tj, 2)
            if (m - j).denominator != 1:
                continue
            if m * m + j * (j + 1) - 2 < F(-1, 4):
                low_sectors.append((m, j))
    GA.check("principal-range sectors", sorted(low_sectors) == sorted(
        [(F(0), F(0)), (F(1), F(0)), (F(-1), F(0)), (F(1, 2), F(1, 2)), (F(-1, 2), F(1, 2))]))
    # control: with the central constant -(Lambda) hbar^2 in place of -(2 Lambda/3) hbar^2 zero modes would exist
    hit = [(kap, p, j) for kap in (F(1), F(3, 2), F(2)) for p in range(3) for j in (F(1), F(3, 2), F(2))
           if j >= kap and (kap + p) ** 2 - kap * (kap - 1) + j * (j + 1) - 3 == 0]
    GA.check("control: constant -3 admits a zero mode (kap = 1, p = 0, j = 1)", (F(1), 0, F(1)) in hit)
    return True


def check_anti_de_sitter_scale_control():
    premise("synthesis.operator-join-ordering-constants")
    premise("mass.exact-join")
    # Lambda = -6, s = 1: lam s^4 = -1, the pure terms vanish and B is the N-preserving cross term
    M = Model(F(-6), F(1))
    deg2 = [k for k in product(range(3), repeat=8) if sum(k) == 2]
    GA.check("36 states at oscillator number 2", len(deg2) == 36)
    imgs = [M.m2({k: F(1)}) for k in deg2]
    GA.check("the join preserves the oscillator number", all(sum(t) == 2 for w in imgs for t in w))
    GA.check("B preserves the oscillator number", all(sum(t) == 2 for k in deg2 for t in M.B({k: F(1)})))
    mat = [[w.get(t, F(0)) for w in imgs] for t in deg2]
    rk = GA.mat_rank(mat)
    GA.check("three zero modes of finite energy content at oscillator number 2", 36 - rk == 3)
    cimgs = [vadd(M.C({k: F(1)}), {k: F(-2)}) for k in deg2]
    stacked = mat + [[w.get(t, F(0)) for w in cimgs] for t in deg2]
    GA.check("the zero modes have internal spin j = 1 (C = 2)", GA.mat_rank(stacked) == rk)
    trimgs = [M.trh({k: F(1)}) for k in deg2]
    stacked2 = mat + [[w.get(t, F(0)) for w in trimgs] for t in deg2]
    GA.check("the zero modes have s1 + s2 = 0 (tr h = 0)", GA.mat_rank(stacked2) == rk)
    return True
