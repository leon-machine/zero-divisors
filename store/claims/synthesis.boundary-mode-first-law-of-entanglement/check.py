"""synthesis.boundary-mode-first-law-of-entanglement: exact checks.

Logarithms are formal symbols. A real number built from logs is a dict {symbol: Fraction}, where
the symbols are ('lnr', j) = beta omega_j (the Boltzmann exponent of mode j, r_j = e^{beta omega_j}
rational), ('ln1r', j) = ln(1 + r_j), and ('lnq', q) = ln q for a rational occupation q of a
trial state. Identities among such combinations are checked coefficient by coefficient.
The mode itself is built in GA: the ascent pair of Cl(1,1), a = (e+ + e-)/2, a* = (e+ - e-)/2.
"""
from fractions import Fraction as F
from itertools import product
import GA
from GA import mul, add, sub, scal, gen, sc
from tp_premise import premise

SQ = (1, -1)                      # e+ = gen(0), e- = gen(1)
RS = [F(2), F(1, 3), F(7, 2)]     # Boltzmann factors e^{beta omega_j} of a three-mode window


def lin(*pairs):
    out = {}
    for k, c in pairs:
        out[k] = out.get(k, F(0)) + c
    return {k: v for k, v in out.items() if v != 0}


def ladd(*xs):
    out = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def lsc(c, x):
    return {k: c * v for k, v in x.items() if c * v != 0}


def ln_gibbs(j, occ):
    # ln P_I(occupied) = -ln(1+r); ln P_I(empty) = ln r - ln(1+r)
    if occ:
        return lin((('ln1r', j), F(-1)))
    return lin((('lnr', j), F(1)), (('ln1r', j), F(-1)))


def setup():
    premise("synthesis.imported-jacobson-entanglement-equilibrium-2016")
    premise("hawking.i-state")
    premise("state-selection.partner-purification-are-canonical")
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("angle.imported-theorems-deliver-their-hypotheses")


def check_mode_algebra():
    setup()
    a = scal(F(1, 2), add(gen(0), gen(1)))
    ad = scal(F(1, 2), sub(gen(0), gen(1)))
    assert mul(a, a, SQ) == {} and mul(ad, ad, SQ) == {}
    assert add(mul(a, ad, SQ), mul(ad, a, SQ)) == sc(1)          # CAR
    N = mul(ad, a, SQ)
    assert mul(N, N, SQ) == N                                    # N is a projection: spectrum {0, 1}
    # Gibbs weights of one mode: P(n) proportional to r^{-n}; P(1) = 1/(1+r) is the Fermi-Dirac n_I
    for r in RS:
        p0, p1 = r / (1 + r), 1 / (1 + r)
        assert p0 + p1 == 1 and p1 / p0 == 1 / r                 # detailed balance n/(1-n) = e^{-beta omega}
    return True


def check_first_law():
    setup()
    k = len(RS)
    basis = list(product((0, 1), repeat=k))
    # -ln rho_I on the Fock basis equals beta H_F + ln Z_F, with beta H_F(n) = sum n_j ln r_j
    # and ln Z_F = sum (ln(1+r_j) - ln r_j)
    lnZ = ladd(*[lin((('ln1r', j), F(1)), (('lnr', j), F(-1))) for j in range(k)])
    for n in basis:
        minus_ln_rho = lsc(F(-1), ladd(*[ln_gibbs(j, n[j]) for j in range(k)]))
        betaH = ladd(*[lin((('lnr', j), F(n[j]))) for j in range(k)])
        assert minus_ln_rho == ladd(betaH, lnZ)
    # first law: for a traceless variation delta (diagonal part d(n), sum d = 0; off-diagonal parts
    # do not enter Tr(delta ln rho_I) because rho_I is diagonal), dS = -Tr(delta ln rho_I) - Tr(delta)
    # equals beta * Tr(delta H_F). Check on several traceless diagonal variations.
    deltas = []
    for s in range(1, 4):
        d = [F((i * s * 7) % 5 - 2, s) for i in range(len(basis))]
        tot = sum(d)
        d[0] -= tot
        assert sum(d) == 0
        deltas.append(d)
    for d in deltas:
        dS = ladd(*[lsc(d[i], lsc(F(-1), ladd(*[ln_gibbs(j, basis[i][j]) for j in range(k)])))
                    for i in range(len(basis))])
        dE = ladd(*[lsc(d[i], ladd(*[lin((('lnr', j), F(basis[i][j]))) for j in range(k)]))
                    for i in range(len(basis))])
        assert dS == dE                                          # dS = beta dE, the ln Z part cancels
        assert dE != {}                                          # a nontrivial variation
    return True


def check_equilibrium():
    setup()
    # per mode: phi(q) = s(q) - x q with x = ln r. D(q || n_I) = phi(n_I) - phi(q), as an identity of
    # log symbols, for trial occupations q; D >= 0 is Klein's inequality, D = 0 iff q = n_I.
    for j, r in enumerate(RS):
        nI = 1 / (1 + r)
        for q in (F(1, 5), F(1, 2), F(3, 4), nI):
            # D = q ln(q/nI) + (1-q) ln((1-q)/(1-nI))
            D = ladd(lin((('lnq', q), q), (('lnq', 1 - q), 1 - q)),
                     lsc(-q, ln_gibbs(j, 1)), lsc(-(1 - q), ln_gibbs(j, 0)))
            # phi(q) = -q ln q - (1-q) ln(1-q) - q ln r
            phi_q = lin((('lnq', q), -q), (('lnq', 1 - q), -(1 - q)), (('lnr', j), -q))
            # phi(nI) = s(nI) - x nI = ln(1+r) - (r/(1+r)) ln r - (1/(1+r)) ln r = ln(1+r) - ln r
            phi_I = lin((('ln1r', j), F(1)), (('lnr', j), F(-1)))
            assert D == ladd(phi_I, lsc(F(-1), phi_q))
            if q == nI:
                # substitute ln nI = -ln(1+r), ln(1 - nI) = ln r - ln(1+r): D vanishes
                sub_map = {('lnq', q): ln_gibbs(j, 1), ('lnq', 1 - q): ln_gibbs(j, 0)}
                Ds = ladd(*[lsc(c, sub_map[key]) if key in sub_map else {key: c} for key, c in D.items()])
                assert Ds == {}
        # stationarity: phi'(q) = ln((1-q)/q) - ln r vanishes iff (1-q)/q = r, i.e. q = nI exactly
        assert (1 - nI) / nI == r
        for q in (F(1, 5), F(1, 2), F(3, 4)):
            if q != nI:
                assert (1 - q) / q != r
        # concavity: phi''(q) = -1/(q(1-q)) < 0 on (0,1)
        for q in (F(1, 5), F(1, 2), F(3, 4)):
            assert -1 / (q * (1 - q)) < 0
    return True


def check_small_ball_balance():
    setup()
    # Jacobson's balance in spacetime dimension d (space dimension m = d - 1), with Omega the area of
    # the unit (d-2)-sphere kept as a formal factor (coefficients below are per Omega l^d):
    # (a) matter: delta<K> = 2 pi * int_0^l (l^2 - r^2)/(2 l) r^{d-2} dr * delta T00 / l^d
    # (b) area at fixed volume: V = w l^m (1 - Rs l^2/(6(m+2))), A = m w l^{m-1} (1 - Rs l^2/(6m)),
    #     Rs = 2 G00 on a time-symmetric slice; to first order delta A|_V = -A Rs l^2/(2 m (m+2)).
    for d in (3, 4, 5, 6, 10):
        m = d - 1
        integral = (F(1, 2) * (F(1, d - 1) - F(1, d + 1)))      # int (l^2 - r^2)/(2l) r^{d-2} dr / l^d
        assert integral == F(1, d * d - 1)
        # fixed volume: l = l0 (1 + eps), eps = Rs l0^2/(6 m (m+2)); A/A0 - 1 = (m-1) eps - Rs l0^2/(6m)
        eps = F(1, 6 * (m + 2)) / m                              # from m eps - Rs l0^2/(6(m+2)) = 0
        assert m * eps - F(1, 6 * (m + 2)) == 0
        coeff_A = (m - 1) * eps - F(1, 6 * m)                    # coefficient of Rs l0^2 in A/A0 - 1
        assert coeff_A == F(-1, 2 * m * (m + 2))
        # A0 = m w l^{m-1} = Omega l^{d-2}, so delta A|_V = -Omega l^d Rs/(2 (d-1)(d+1)) = -Omega l^d G00/(d^2-1)
        dA_per_G00 = coeff_A * 2                                 # Rs = 2 G00, in units Omega l^d
        assert dA_per_G00 == -F(1, d * d - 1)
        # equilibrium eta delta A + 2 pi delta<K>/(2 pi) ... : eta (-G00) + 2 pi T00 = 0 after the common
        # factor Omega l^d/(d^2 - 1): G00 = (2 pi/eta) T00 = 8 pi G T00 iff eta = 1/(4G); coefficient of pi
        for eta_inv4 in (F(1), F(3, 2)):                          # eta = 1/(4 G), G = eta_inv4
            eta = 1 / (4 * eta_inv4)
            two_pi_over_eta = 2 / eta                             # coefficient of pi
            assert two_pi_over_eta == 8 * eta_inv4
    return True
