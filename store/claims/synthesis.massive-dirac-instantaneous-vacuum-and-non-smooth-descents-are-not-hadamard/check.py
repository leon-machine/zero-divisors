"""synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard: exact checks.

One momentum-helicity sector of the Dirac field on a spatially flat Robertson-Walker field, in conformal
time, is the two-level system i u' = H u with H = M s3 + k s1, M = m a(eta) (s_j the Pauli vectors, i the
Pauli pseudoscalar I = s1 s2 s3). For a pure state rho = (1 + s)/2 with Bloch vector s this is
s' = 2 h x s, h = (k, 0, M).

Jets: M_j = d^j M / d eta^j are independent polynomial variables; D(M_j) = M_{j+1}; eps = 1/k.
(1) Pauli algebra: H^2 = k^2 + M^2, I^2 = -1, I central, (a b - b a)/2 = I (a x b) on all basis pairs.
(2) The all-order adiabatic Bloch series s_ad = sum_j eps^j c_j: recursion e1 x c_{n+1} = (D c_n - 2 M e3 x c_n)/2
    with the e1-part fixed by |s| = 1; solvability, unit norm, the equation residual and weight homogeneity
    (weight(M_j) = j + 1, c_j of weight j) are checked to order NMAX; c_1 = M e3, c_2 = -M^2/2 e1 + M_1/2 e2.
(3) The instantaneous eigenvector h/|h| as a series; 1 - s_ad . h/|h| = M_1^2/8 eps^4 + c6 eps^6 + ...,
    odd orders zero; |beta|^2 = (1 - s.s')/2 = M_1^2/(16 k^4) + O(k^-6).
(3b) A gauge-invariant deposit diagonal over the instantaneous vacuum has one-particle Bloch part t h/|h|; its
    sigma_2 gap to the adiabatic state's density (1 - s_ad)/2 is s_ad.s2/2 = M_1/(4 k^2) + O(k^-4) for every t.
(4) Jump law: the only monomial of c_{n+1} containing M_n is lambda_n M_n v_n, lambda_n v_n = -(1/2) lambda_{n-1}
    e1 x v_{n-1}, |lambda_n| = 2^-n; M_n is absent from c_j for j <= n; shifting M_n by D changes s through
    order n + 1 only by D lambda_n v_n eps^(n+1), and 1 - s_L . s_R = D^2 4^-n / 2 eps^(2n+2) + O(eps^(2n+3)).
"""
from fractions import Fraction as Fr
import GA
from tp_premise import premise

NMAX = 9          # series order computed
NJ = NMAX + 3     # jet variables M_0 .. M_{NJ-2}, plus the shift variable D in the last slot
DSLOT = NJ - 1


# ---- polynomials in the jet variables: {exponent tuple: Fraction} ----
def padd(p, q, c=1):
    out = dict(p)
    for m, v in q.items():
        out[m] = out.get(m, 0) + c * v
        if out[m] == 0:
            del out[m]
    return out


def pmul(p, q):
    out = {}
    for a, x in p.items():
        for b, y in q.items():
            m = tuple(i + j for i, j in zip(a, b))
            out[m] = out.get(m, 0) + x * y
            if out[m] == 0:
                del out[m]
    return out


def pscale(p, c):
    return {m: v * c for m, v in p.items() if v * c != 0}


def mono(j, e=1):
    t = [0] * NJ
    t[j] = e
    return {tuple(t): Fr(1)}


ONE = {tuple([0] * NJ): Fr(1)}
M = mono(0)


def pder(p):
    """Total eta-derivative: D M_j = M_{j+1}; the shift variable D is a constant."""
    out = {}
    for m, v in p.items():
        for j, e in enumerate(m[:DSLOT]):
            if e:
                t = list(m)
                t[j] -= 1
                t[j + 1] += 1
                assert j + 1 < DSLOT
                t = tuple(t)
                out[t] = out.get(t, 0) + v * e
                if out[t] == 0:
                    del out[t]
    return out


def subst(p, j, q):
    """Substitute M_j -> q in p."""
    out = {}
    for m, v in p.items():
        e = m[j]
        base = list(m)
        base[j] = 0
        term = {tuple(base): v}
        for _ in range(e):
            term = pmul(term, q)
        out = padd(out, term)
    return out


# ---- 3-vectors of polynomials ----
def vadd(a, b, c=1):
    return [padd(a[i], b[i], c) for i in range(3)]


def vder(a):
    return [pder(x) for x in a]


def vsc(a, p):
    return [pmul(x, p) for x in a]


def cross(a, b):
    return [padd(pmul(a[1], b[2]), pmul(a[2], b[1]), -1),
            padd(pmul(a[2], b[0]), pmul(a[0], b[2]), -1),
            padd(pmul(a[0], b[1]), pmul(a[1], b[0]), -1)]


def vdot(a, b):
    return padd(padd(pmul(a[0], b[0]), pmul(a[1], b[1])), pmul(a[2], b[2]))


E1 = [ONE, {}, {}]
E2 = [{}, ONE, {}]
E3 = [{}, {}, ONE]
ZERO = [{}, {}, {}]


def adiabatic_series(N):
    c = [E1]
    for n in range(N):
        rhs = vadd(vder(c[n]), vsc(cross(E3, c[n]), pscale(M, 2)), -1)
        rhs = [pscale(x, Fr(1, 2)) for x in rhs]
        assert rhs[0] == {}, ("solvability fails", n)
        nxt = [pscale(x, -1) for x in cross(E1, rhs)]
        s = {}
        for a in range(1, n + 1):
            s = padd(s, vdot(c[a], c[n + 1 - a]))
        nxt[0] = pscale(s, Fr(-1, 2))
        c.append(nxt)
    return c


def inst_series(N):
    """h/|h| = (1, 0, eps M) (1 + eps^2 M^2)^(-1/2) via GA's exact power series."""
    coeffs = GA.ps_pow_rat([Fr(1), Fr(1)], Fr(-1, 2), N // 2 + 1)   # (1 + x)^(-1/2)
    out = [[{}, {}, {}] for _ in range(N + 1)]
    m2 = ONE
    for j, cj in enumerate(coeffs):
        if 2 * j <= N:
            out[2 * j][0] = padd(out[2 * j][0], pscale(m2, cj))
        if 2 * j + 1 <= N:
            out[2 * j + 1][2] = padd(out[2 * j + 1][2], pmul(pscale(m2, cj), M))
        m2 = pmul(m2, pmul(M, M))
    return out


def series_dot(a, b, N):
    out = []
    for n in range(N + 1):
        tot = {}
        for i in range(n + 1):
            tot = padd(tot, vdot(a[i], b[n - i]))
        out.append(tot)
    return out


C = adiabatic_series(NMAX)
CI = inst_series(NMAX)


def check_pauli_two_level_bloch_form():
    sq = (1, 1, 1)
    e = [GA.gen(i) for i in range(3)]
    I = GA.mul(GA.mul(e[0], e[1], sq), e[2], sq)
    assert GA.eq(GA.mul(I, I, sq), GA.sc(-1))
    for v in e:
        assert GA.commutes(I, v, sq)
    # (a b - b a)/2 = I (a x b) on all basis pairs, so on all vectors by bilinearity
    for i in range(3):
        for j in range(3):
            lhs = GA.scal(Fr(1, 2), GA.sub(GA.mul(e[i], e[j], sq), GA.mul(e[j], e[i], sq)))
            cr = [0, 0, 0]
            k = 3 - i - j
            if i != j:
                sgn = 1 if (i, j) in ((0, 1), (1, 2), (2, 0)) else -1
                cr[k] = sgn
            rhs = GA.mul(I, GA.add(*[GA.scal(Fr(cr[t]), e[t]) for t in range(3)]), sq)
            assert GA.eq(lhs, rhs)
    # H = M s3 + k s1 squares to k^2 + M^2 at sample rational points
    for Mv, kv in ((Fr(3, 7), Fr(5)), (Fr(-2), Fr(1, 3)), (Fr(0), Fr(11, 4))):
        H = GA.add(GA.scal(Mv, e[2]), GA.scal(kv, e[0]))
        assert GA.eq(GA.mul(H, H, sq), GA.sc(kv * kv + Mv * Mv))
    return True


def check_adiabatic_series_solves_the_bloch_equation():
    assert C[1] == [{}, {}, M]
    assert C[2] == [pscale(pmul(M, M), Fr(-1, 2)), pscale(mono(1), Fr(1, 2)), {}]
    for n in range(NMAX + 1):
        # unit norm order by order: sum_{a+b=n} c_a . c_b = delta_{n0}
        tot = {}
        for a in range(n + 1):
            tot = padd(tot, vdot(C[a], C[n - a]))
        assert tot == (ONE if n == 0 else {}), n
        # weight homogeneity
        for comp in C[n]:
            for m in comp:
                assert sum((j + 1) * e for j, e in enumerate(m)) == n
        # residual of s' = 2 h x s at order eps^n (n < NMAX): D c_n - 2 e1 x c_{n+1} - 2 M e3 x c_n = 0
        if n < NMAX:
            res = vadd(vadd(vder(C[n]), vsc(cross(E1, C[n + 1]), pscale(ONE, 2)), -1),
                       vsc(cross(E3, C[n]), pscale(M, 2)), -1)
            assert res == ZERO, n
    # parity: c_j lies along e1, e2 for even j and along e3 for odd j
    for n in range(NMAX + 1):
        if n % 2:
            assert C[n][0] == {} and C[n][1] == {}
        else:
            assert C[n][2] == {}
    return True


def check_instantaneous_vacuum_differs_at_order_k_minus_two():
    premise("synthesis.imported-microlocal-hadamard-condition")
    # the instantaneous series is a unit vector along h
    tot = series_dot(CI, CI, NMAX)
    assert tot[0] == ONE and all(t == {} for t in tot[1:])
    assert cross(E1, CI[1]) == vsc(cross(E1, E3), M)
    # agreement through order 1, first difference at order 2 along e2 with coefficient M_1/2
    for n in range(2):
        assert C[n] == CI[n]
    d2 = vadd(C[2], CI[2], -1)
    assert d2 == [{}, pscale(mono(1), Fr(1, 2)), {}]
    # 1 - s_ad . s_inst
    sd = series_dot(C, CI, NMAX)
    one_minus = [padd(ONE if n == 0 else {}, sd[n], -1) for n in range(NMAX + 1)]
    for n in range(4):
        assert one_minus[n] == {}
    assert one_minus[4] == pscale(pmul(mono(1), mono(1)), Fr(1, 8))
    assert one_minus[5] == {} and one_minus[7] == {}
    six = padd(padd(pscale(pmul(pmul(M, M), pmul(mono(1), mono(1))), Fr(-3, 8)),
                    pscale(pmul(mono(1), mono(3)), Fr(-1, 16))), pscale(pmul(mono(2), mono(2)), Fr(1, 32)))
    assert one_minus[6] == six
    # |beta|^2 = (1 - s.s')/2 at order k^-4 is M_1^2/16; the energy moment k^2 * k * |beta|^2 has
    # leading term (M_1^2/16) / k, so each dyadic shell [K, 2K] contributes at least M_1^2/32 at
    # leading order (1/k >= 1/(2K) on the shell, shell length K)
    beta2_4 = pscale(one_minus[4], Fr(1, 2))
    assert beta2_4 == pscale(pmul(mono(1), mono(1)), Fr(1, 16))
    shell = pscale(beta2_4, Fr(1, 2))          # K * (1/(2K)) * M_1^2/16
    assert shell == pscale(pmul(mono(1), mono(1)), Fr(1, 32))
    # the number moment k^2 |beta|^2 ~ k^-2 is integrable at infinity; the energy moment ~ k^-1 is not
    num_power, energy_power = 2 - 4, 2 + 1 - 4
    assert num_power < -1 and energy_power == -1
    # massless field: every correction vanishes at M = 0 (conformal vacuum exact)
    for n in range(1, NMAX + 1):
        for comp in C[n]:
            for m in comp:
                assert any(m[j] for j in range(DSLOT))
    return True


def check_deposits_diagonal_over_the_instantaneous_vacuum_keep_the_gap():
    premise("synthesis.imported-microlocal-hadamard-condition")
    # h/|h| has no sigma_2 part at any order
    for n in range(NMAX + 1):
        assert CI[n][1] == {}
    for t in (Fr(-1), Fr(-1, 3), Fr(0), Fr(1, 2), Fr(1)):
        # Bloch part of the difference of densities: (t h_hat - (-s_ad))/2
        diff = [vadd(vsc(CI[n], pscale(ONE, t)), C[n]) for n in range(NMAX + 1)]
        half2 = [pscale(diff[n][1], Fr(1, 2)) for n in range(NMAX + 1)]
        assert half2[0] == {} and half2[1] == {}
        assert half2[2] == pscale(mono(1), Fr(1, 4))
        assert half2[3] == {}
        assert half2[4] == padd(pscale(mono(3), Fr(-1, 16)), pscale(pmul(pmul(M, M), mono(1)), Fr(-3, 8)))
        # the gap does not depend on t: identical to the t = 0 value at every order
        assert half2 == [pscale(C[n][1], Fr(1, 2)) for n in range(NMAX + 1)]
    return True


def check_jump_law():
    premise("synthesis.imported-microlocal-hadamard-condition")
    lam_v = None
    for n in range(NMAX):
        key = list(mono(n))[0]
        coeff = [comp.get(key, Fr(0)) for comp in C[n + 1]]
        # only one monomial of c_{n+1} contains M_n: M_n itself
        for comp in C[n + 1]:
            for m in comp:
                if m[n]:
                    assert m == key
        # absent below
        for j in range(n + 1):
            for comp in C[j]:
                for m in comp:
                    assert m[n] == 0
        mag = sum(x * x for x in coeff)
        assert mag == Fr(1, 4 ** n)
        expected_axis = 2 if n % 2 == 0 else 1
        assert [i for i in range(3) if coeff[i] != 0] == [expected_axis]
        if lam_v is not None:
            prev = [{key0: lam_v[i]} if lam_v[i] else {} for i in range(3)]
            rec = [pscale(x, Fr(-1, 2)) for x in cross(E1, prev)]
            assert [x.get(key0, Fr(0)) for x in rec] == coeff
        lam_v = coeff
        key0 = key
        # shift M_n -> M_n + D: s changes through order n + 1 only by D lambda_n v_n
        shifted = [[subst(comp, n, padd(mono(n), mono(DSLOT))) for comp in C[j]] for j in range(NMAX + 1)]
        for j in range(n + 1):
            assert shifted[j] == C[j]
        diff = vadd(shifted[n + 1], C[n + 1], -1)
        assert diff == [{list(mono(DSLOT))[0]: coeff[i]} if coeff[i] else {} for i in range(3)]
        if 2 * n + 2 <= NMAX:
            sd = series_dot(shifted, C, NMAX)
            om = [padd(ONE if t == 0 else {}, sd[t], -1) for t in range(NMAX + 1)]
            for t in range(2 * n + 2):
                assert om[t] == {}
            assert om[2 * n + 2] == pscale(mono(DSLOT, 2), Fr(1, 2 * 4 ** n))
    return True


def check_stored_sudden_start_differs_from_bunch_davies_unboundedly():
    premise("synthesis.sudden-descent-feature-not-tilt")
    premise("synthesis.imported-microlocal-hadamard-condition")
    I = GA.QI(0, 1)
    # u = E (1 - i/z), u_z = E (-i - 1/z + i/z^2), E = e^{-iz} of modulus one; instantaneous data f = 1, f_z = -i.
    # The identities below are Laurent polynomials in 1/z of degree at most 8, so nine distinct sample
    # points determine them; eleven are used.
    samples = [Fr(-1, 3), Fr(-1, 2), Fr(-1), Fr(-3, 2), Fr(-2), Fr(-5, 2), Fr(-3), Fr(-7), Fr(-10), Fr(-40), Fr(-101, 3)]
    for z in samples:
        p = GA.QI(1) - I * GA.QI(Fr(1) / z)                       # u / E
        q = GA.QI(0, -1) - GA.QI(Fr(1) / z) + I * GA.QI(Fr(1) / (z * z))  # u_z / E
        u2 = (p * p.conj()).re
        uz2 = (q * q.conj()).re
        e_u = Fr(1, 2) * (uz2 + u2)
        e_f = Fr(1, 2) * (1 + 1)
        assert z * z * (u2 - 1) == 1                               # <chi^2> deficit 1/z^2 per mode
        assert z ** 4 * (e_u - e_f) == Fr(1, 2)                    # energy deficit 1/(2 z^4) per mode
        # Bogoliubov coefficient of the instantaneous data against u, |beta|^2 = 1/(4 z^4)
        W = GA.QI(0, 2)
        beta = GA.QI(-1) * (q + I * p) / W                       # -(u' + i u)/W up to the phase E
        assert z ** 4 * (beta * beta.conj()).re == Fr(1, 4)
    # in physical units chi = f/sqrt(2k), d/deta = k d/dz: per-mode deficits (1/(2k)) (k eta_d)^-2 and
    # (k/2) (1/2)(k eta_d)^-4; with the measure k^2 dk both are (const)/k: logarithmically divergent
    chi_power = -1 - 2 + 2      # k^-1 (1/(2k)) * k^-2 * k^2
    energy_power = 1 - 4 + 2    # k (k/2) * k^-4 * k^2
    assert chi_power == -1 and energy_power == -1
    return True
