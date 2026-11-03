"""synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations: exact checks.

The attachment's helicity-s module (field-theory.twistor-attachment): conformal energies k = |s| + 1 + n,
n >= 0, multiplicity (n + 1)(n + 2|s| + 1) = k^2 - s^2.  Its conformal-energy character is
    chi_s(t) = sum_n (n + 1)(n + 2|s| + 1) e^{-t(|s| + 1 + n)}
             = e^{-t(|s| + 1)} [2 / (1 - e^{-t})^3 + (2|s| - 1) / (1 - e^{-t})^2].
(i)   Laurent polar part of chi_s: 2 t^-3 + 0 t^-2 - s^2 t^-1 (exact truncated series in Fractions).
(ii)  Dictionary on the unit Einstein static field (R = 6): a1 per field = (c_-1(field) / 3) R, giving
      conformal scalar 0, two-component fermion -R/6, gauge vector -2R/3; cross-checked against the heat-kernel
      values computed independently: tr(E + R/6) with the Lichnerowicz E = -R/4 computed in Cl(4,0) for a
      constant-curvature field, and 4 R/6 - tr Ric - 2 R/6 for the vector with two ghosts.
(iii) Regulated zero-point energy of one helicity state, E_s(L) = sum_k (k^2 - s^2) k f(k/L), is an exact Laurent
      polynomial in L for integer L and f = (1 - x^2)^m (m = 2, 3): L^4 coefficient int x^3 f, L^2 coefficient
      -s^2 int x f, no L^3 or L term; for the exponential cut-off -chi_s'(t) has 6 t^-4 - s^2 t^-2 and no t^-3, t^-1.
(iv)  Statistics-weighted sum (1/2)(bosons) - (1/2)(fermions) over the content N_V gauge vectors (two helicity
      states each), N_S conformal scalars, N_W Weyl fermions (two helicity states each): the L^2 coefficient is
      -(N_V - N_W/4) int x f; with N_V = dim(su(3) + su(2) + u(1)) = 12 and N_W = 16 N_g it vanishes iff N_g = 3,
      for every N_S, while the L^4 coefficient (2 N_V + N_S - 2 N_W) int x^3 f / 2 does not vanish; with
      N_W = 15 N_g (no right-handed neutrino) the L^2 coefficient never vanishes (-1/8 at N_g = 3, m = 2).
(v)   A cut-off with f(1) != 0 (sharp floors, m = 0) gives L^3 and L terms whose coefficients depend on whether the
      energies are integers (bosons) or half-integers (fermions); one with f(1) = 0, f'(1) != 0 (m = 1) gives no
      odd powers but an L^2 edge term that is not -s^2 int x f and depends on the same offset.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

NSER = 8


# ---------------------------------------------------------------- helpers (no asserted values here)
def exp_series(c, n=NSER):
    out = [F(1)]
    for k in range(1, n + 1):
        out.append(out[-1] * c / k)
    return out


def u_series(n=NSER):
    """(1 - e^{-t}) / t."""
    out, fact = [], F(1)
    for j in range(n + 1):
        fact *= (j + 1)
        out.append(F((-1) ** j) / fact)
    return out


def character_laurent(s, n=NSER):
    """Laurent coefficients {p: c} of chi_s(t), p = -3 .. n - 3."""
    a = abs(F(s))
    pre = exp_series(-(a + 1), n)
    u = u_series(n)
    u3 = GA.ps_inv(GA.ps_mul(GA.ps_mul(u, u, n), u, n), n)
    u2 = GA.ps_inv(GA.ps_mul(u, u, n), n)
    tu2 = [F(0)] + u2[:n]
    br = [2 * x + (2 * a - 1) * y for x, y in zip(u3, tu2)]
    ser = GA.ps_mul(pre, br, n)
    return {j - 3: ser[j] for j in range(n + 1)}


def closed_form_q_series(s, nterms):
    """Coefficients of q^j in q^{|s|+1} [2/(1-q)^3 + (2|s|-1)/(1-q)^2], j = 0 .. nterms - 1 (shifted)."""
    a = abs(F(s))
    one_minus_q = [F(1), F(-1)]
    inv1 = GA.ps_inv(one_minus_q, nterms)
    inv2 = GA.ps_mul(inv1, inv1, nterms)
    inv3 = GA.ps_mul(inv2, inv1, nterms)
    return [2 * x + (2 * a - 1) * y for x, y in zip(inv3, inv2)][:nterms]


def mult(s, n):
    a = abs(F(s))
    return (n + 1) * (n + 2 * a + 1)


def E_state(s, L, m):
    """sum over conformal energies k < L of (k^2 - s^2) k (1 - k^2/L^2)^m."""
    a = abs(F(s))
    k, tot = a + 1, F(0)
    while k < L:
        tot += (k * k - a * a) * k * (1 - (k / L) ** 2) ** m
        k += 1
    return tot


def laurent_fit(fun, top, bottom, Ls):
    """Exact Laurent polynomial through the first points; verified at the remaining points."""
    powers = list(range(top, bottom - 1, -1))
    nP = len(powers)
    M = [[F(L) ** p for p in powers] + [fun(L)] for L in Ls[:nP]]
    for i in range(nP):
        piv = next(r for r in range(i, nP) if M[r][i] != 0)
        M[i], M[piv] = M[piv], M[i]
        for r in range(nP):
            if r != i and M[r][i] != 0:
                fct = M[r][i] / M[i][i]
                M[r] = [x - fct * y for x, y in zip(M[r], M[i])]
    co = {p: M[i][nP] / M[i][i] for i, p in enumerate(powers)}
    ok = all(sum(c * F(L) ** p for p, c in co.items()) == fun(L) for L in Ls[nP:])
    return co, ok


def fit_state(s, m):
    return laurent_fit(lambda L: E_state(s, L, m), 4, -2 * m, list(range(6, 6 + 2 * m + 9)))


def moment(m, j):
    """int_0^1 x^j (1 - x^2)^m dx for odd j, exactly (binomial expansion)."""
    tot, c = F(0), F(1)
    for i in range(m + 1):
        tot += c * F((-1) ** i, j + 1 + 2 * i)
        c = c * (m - i) / (i + 1)
    return tot


def content_sum(coeffs, NV, NS, NW):
    """(1/2) bosons - (1/2) fermions, two helicity states per vector and per Weyl field."""
    return F(1, 2) * (2 * NV * coeffs[F(1)] + NS * coeffs[F(0)]) - F(1, 2) * (2 * NW * coeffs[F(1, 2)])


def lie_dim_su(n):
    return n * n - 1


# ---------------------------------------------------------------- checks
def check_module_character_polar_part():
    premise("field-theory.twistor-attachment")
    ok = True
    # (2s numerator, expected t^-3, t^-2, t^-1 as (num, den))
    table = [(0, 2, 0, (0, 1)), (1, 2, 0, (-1, 4)), (2, 2, 0, (-1, 1)), (3, 2, 0, (-9, 4)), (4, 2, 0, (-4, 1))]
    for twos, c3, c2, (n1, d1) in table:
        s = F(twos, 2)
        # the closed form reproduces the stored multiplicities, and they equal k^2 - s^2
        qs = closed_form_q_series(s, 30)
        ok = ok and all(qs[n] == mult(s, n) for n in range(30))
        ok = ok and all(mult(s, n) == (abs(s) + 1 + n) ** 2 - s * s for n in range(30))
        lau = character_laurent(s)
        ok = ok and lau[-3] == c3 and lau[-2] == c2 and lau[-1] == F(n1, d1) and lau[-1] == -s * s
    return GA.check("character polar part 2 t^-3 - s^2 t^-1 on every helicity module", ok)


def check_dictionary_reproduces_a1():
    premise("field-theory.twistor-attachment")
    c1 = {s: character_laurent(s)[-1] for s in (F(0), F(1, 2), F(1))}
    # per field on the unit Einstein static field: a1 / R = c_-1(field) / 3, fields with 1, 2, 2 states
    a1_scalar = c1[F(0)] / 3
    a1_weyl = 2 * c1[F(1, 2)] / 3
    a1_vector = 2 * c1[F(1)] / 3
    ok = a1_scalar == 0 and a1_weyl == F(-1, 6) and a1_vector == F(-2, 3)
    # independent heat-kernel values on a constant-curvature field, Cl(4,0), R(B) = kappa B
    SQ = GA.sig(4, 0)
    for kappa in (F(1), F(-3, 7)):
        lich = GA.sc(0)
        ric_trace = F(0)
        for a in range(4):
            for b in range(4):
                if a == b:
                    continue
                eab = GA.mul(GA.gen(a), GA.gen(b), SQ)
                wedge = eab  # orthonormal: e_a ^ e_b = e_a e_b
                Rab = GA.scal(kappa, wedge)
                if a < b:
                    lich = GA.add(lich, GA.scal(F(1, 2), GA.mul(eab, Rab, SQ)))
                # Ricci scalar: sum_{a,b} (e_b ^ e_a) . R(e_a ^ e_b) with the reversed pairing
                ric_trace += GA.mul(GA.reverse(wedge), Rab, SQ).get((), F(0))
        Rs = ric_trace
        ok = ok and Rs == 12 * kappa and GA.eq(lich, GA.sc(-Rs / 4))
        E = -Rs / 4
        weyl_hk = 2 * (Rs / 6 + E)
        vec_hk = 4 * Rs / 6 - Rs - 2 * Rs / 6
        ok = ok and weyl_hk == a1_weyl * Rs and vec_hk == a1_vector * Rs and a1_scalar * Rs == Rs / 6 - Rs / 6
    return GA.check("module dictionary gives a1 = 0, -R/6, -2R/3 per conformal scalar, Weyl field, vector", ok)


def check_smooth_cutoff_vacuum_energy():
    premise("field-theory.twistor-attachment")
    ok = True
    for m in (2, 3):
        M3, M1 = moment(m, 3), moment(m, 1)
        ok = ok and M1 == F(1, 2 * (m + 1)) and M3 == F(1, 2 * (m + 1) * (m + 2))
        for twos in (0, 1, 2, 3):
            s = F(twos, 2)
            co, fit_ok = fit_state(s, m)
            ok = ok and fit_ok and co[4] == M3 and co[2] == -s * s * M1 and co[3] == 0 and co[1] == 0
    # exponential cut-off: -chi_s'(t) from the character's Laurent series
    for twos in (0, 1, 2, 3, 4):
        s = F(twos, 2)
        lau = character_laurent(s)
        dl = {p - 1: -p * c for p, c in lau.items() if p != 0}
        ok = ok and dl[-4] == 6 and dl[-3] == 0 and dl[-2] == -s * s and dl.get(-1, F(0)) == 0
    return GA.check("smooth cut-offs: L^4 int x^3 f, L^2 -s^2 int x f, no odd powers", ok)


def check_series_content_cancels():
    premise("field-theory.twistor-attachment")
    premise("standard-model.connection-forced")
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    NV = lie_dim_su(3) + lie_dim_su(2) + 1
    per_generation = 16
    ok = NV == 12
    for m in (2, 3):
        coeffs = {s: fit_state(s, m)[0] for s in (F(0), F(1, 2), F(1))}
        M1, M3 = moment(m, 1), moment(m, 3)
        for Ng in (1, 2, 3, 4, 5):
            NW = per_generation * Ng
            for NS in (0, 4, 8):
                L2 = content_sum({s: c[2] for s, c in coeffs.items()}, NV, NS, NW)
                L4 = content_sum({s: c[4] for s, c in coeffs.items()}, NV, NS, NW)
                ok = ok and L2 == -(NV - F(NW, 4)) * M1
                ok = ok and L4 == F(2 * NV + NS - 2 * NW, 2) * M3 and ((L4 == 0) == (2 * NV + NS == 2 * NW))
                ok = ok and ((L2 == 0) == (Ng == 3))
    # the exponential cut-off: t^-2 coefficient of the weighted -chi'
    c1 = {s: character_laurent(s)[-1] for s in (F(0), F(1, 2), F(1))}
    for Ng in (2, 3, 4):
        w = content_sum(c1, NV, 4, per_generation * Ng)  # t^-2 coefficient of -chi' is c_-1
        ok = ok and (w == 0) == (Ng == 3) and w == -(NV - 4 * Ng)
    # fifteen Weyl components per generation (no right-handed neutrino): never zero; -1/8 at three generations, m = 2
    co2 = {s: fit_state(s, 2)[0][2] for s in (F(0), F(1, 2), F(1))}
    no_nr = [content_sum(co2, NV, 4, 15 * Ng) for Ng in range(1, 7)]
    ok = ok and all(w != 0 for w in no_nr) and no_nr[2] == F(-1, 8)
    # a gauge algebra other than the connection-forced one does not cancel at three generations (e.g. 21 generators)
    alt = lie_dim_su(4) + 2 * lie_dim_su(2)
    coeffs2 = {s: fit_state(s, 2)[0][2] for s in (F(0), F(1, 2), F(1))}
    ok = ok and alt == 21 and content_sum(coeffs2, alt, 4, 48) != 0
    return GA.check("series content: L^2 coefficient -(N_V - N_W/4) int x f, zero iff three generations", ok)


def check_sharp_floor_cutoff_is_not_local():
    premise("field-theory.twistor-attachment")
    co0 = {s: fit_state(s, 0)[0] for s in (F(0), F(1, 2), F(1))}
    fits = all(fit_state(s, mm)[1] for s in (F(0), F(1, 2), F(1)) for mm in (0, 1))
    # sharp floors (k < L): odd powers, offset-dependent
    ok = fits and co0[F(0)][3] == F(-1, 2) and co0[F(1)][3] == F(-1, 2) and co0[F(1, 2)][3] == 0
    ok = ok and co0[F(1)][1] == F(1, 2) and co0[F(0)][1] == 0 and co0[F(1, 2)][1] == 0
    # kinked cut-off (m = 1): no odd powers, but the L^2 coefficient minus the universal -s^2/4 is offset-dependent
    co1 = {s: fit_state(s, 1)[0] for s in (F(0), F(1, 2), F(1))}
    edge = {s: co1[s][2] + s * s * moment(1, 1) for s in co1}
    ok = ok and all(co1[s][3] == 0 and co1[s][1] == 0 for s in co1)
    ok = ok and edge[F(0)] == F(-1, 6) and edge[F(1)] == F(-1, 6) and edge[F(1, 2)] == F(1, 12)
    # so with the series content the m = 1 edge term does not cancel, and m = 0 leaves a Lambda^3 term
    w1 = content_sum({s: c[2] for s, c in co1.items()}, 12, 4, 48)
    w0 = content_sum({s: c[3] for s, c in co0.items()}, 12, 4, 48)
    ok = ok and w1 != 0 and w0 == -7
    return GA.check("sharp and kinked floor cut-offs add offset-dependent terms", ok)
