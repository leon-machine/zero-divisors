"""synthesis.uniform-pair-channel-of-a-tower-condensate-is-a-goldstone-rotor: exact checks.

The stored pairing element H_4 = sum_b K(n_a + n_c) - G P* P, P = sum_b w_a w_c, on the Fock space of its 2 n_b
tower modes, built with GA's exterior model of the CAR (creation = wedge, annihilation = contraction; the tower
planes generate the CAR). Mode 2b is a_b, mode 2b + 1 is c_b. Sectors are the joint eigenspaces of N_a, N_c; the
pair field X = P* has charge (1, 1). Lowest eigenvalues are certified exactly: M - E is positive semidefinite
(symmetric elimination over the rationals) and singular.
(i)   no order parameter in a sector: <psi, P psi> = 0 on sector vectors; at the degenerate couplings
      K/G = n_b/2 - n the ground eigenspace holds psi_n and psi_{n+1} and their sum has <P> != 0;
(ii)  the variational bounds E(s + h) - E(s) <= <X psi, [H, X] psi>/|X psi|^2 and the same for X*, on every
      sector of the n_b = 2, 3 floors for H_0 = K N + L (N_a - N_c)^2 + R D (D the number of singly occupied
      blocks), all commuting with P;
(iii) the pairing form: the two quotients are eps + G c(s) and -eps - G c(s - h), eps = 2K, c(s) = N_a + N_c - n_b,
      so the second difference is at most 2G;
(iv)  the single shell: the ground state is the band state at the integer n* nearest gamma = (n_b + 1)/2 - K/G,
      E(n* +- 1) - E(n*) = G(1 +- 2(n* - gamma)) in [0, 2G], (P + P*) psi_{n*} lies in span{psi_{n* - 1},
      psi_{n* + 1}} with the quasi-spin weights; in the symmetric phase the bound pair P* Omega sits at
      2K - G n_b below the broken-pair level 2K; the rotor over the threshold G n_b is at most 2/n_b.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

# (n_b, K, G) samples: condensed, symmetric, at the condensation threshold, K = 0
SHELL = [(2, F(1), F(3)), (2, F(3), F(1)), (2, F(1, 2), F(5, 3)), (3, F(1), F(2)), (3, F(3), F(1)),
         (3, F(0), F(1)), (3, F(1, 3), F(7, 5)), (4, F(1), F(1)), (4, F(5, 2), F(1)), (4, F(1, 2), F(3, 4)), (2, F(1), F(1))]
# H_0 extras (L, R) for the variational bound
EXTRA = [(F(0), F(0)), (F(1, 2), F(0)), (F(0), F(3, 2)), (F(-1, 3), F(2))]
BOUND = [(2, F(1), F(3)), (2, F(3), F(1)), (3, F(1), F(2)), (3, F(1, 2), F(5, 3))]
FLOORS = (2, 3)
DEGENERATE = ((2, 0), (3, 1), (4, 1))


def _add_into(out, x, c):
    for k, v in x.items():
        out[k] = out.get(k, F(0)) + c * v


def _clean(x):
    return {k: v for k, v in x.items() if v != 0}


def _ann(i, st, m):
    return GA.ext_contract([F(1) if j == i else F(0) for j in range(m)], st)


def _p(nb, st):                      # P = sum_b w_a w_c
    m = 2 * nb
    out = {}
    for b in range(nb):
        _add_into(out, _ann(2 * b, _ann(2 * b + 1, st, m), m), F(1))
    return _clean(out)


def _pstar(nb, st):                  # P* = sum_b v_c v_a
    out = {}
    for b in range(nb):
        _add_into(out, GA.ext_wedge(2 * b + 1, GA.ext_wedge(2 * b, st)), F(1))
    return _clean(out)


def _counts(S):
    na = sum(1 for j in S if j % 2 == 0)
    nc = sum(1 for j in S if j % 2 == 1)
    d = sum(1 for b in range(max([j // 2 for j in S] + [0]) + 1) if (2 * b in S) != (2 * b + 1 in S))
    return na, nc, d


def _h(nb, K, G, L, R, st):
    out = {}
    for S, c in st.items():
        na, nc, d = _counts(S)
        out[S] = out.get(S, F(0)) + c * (K * (na + nc) + L * (na - nc) ** 2 + R * d)
    _add_into(out, _pstar(nb, _p(nb, st)), -G)
    return _clean(out)


def _basis(nb, na, nc):
    m = 2 * nb
    return [frozenset(S) for k in range(m + 1) for S in combinations(range(m), k)
            if sum(1 for j in S if j % 2 == 0) == na and sum(1 for j in S if j % 2 == 1) == nc]


def _matrix(nb, K, G, L, R, na, nc):
    B = _basis(nb, na, nc)
    idx = {S: i for i, S in enumerate(B)}
    M = [[F(0)] * len(B) for _ in B]
    for j, S in enumerate(B):
        for T, v in _h(nb, K, G, L, R, {S: F(1)}).items():
            M[idx[T]][j] += v
    return B, M


def _psd(M):
    """Exact positive semidefiniteness of a symmetric rational matrix by symmetric elimination."""
    A = [list(r) for r in M]
    n = len(A)
    for k in range(n):
        if A[k][k] < 0:
            return False
        if A[k][k] == 0:
            if any(A[k][j] != 0 for j in range(k, n)):
                return False
            continue
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= f * A[k][j]
    return True


def _shift(M, e):
    return [[M[i][j] - (e if i == j else 0) for j in range(len(M))] for i in range(len(M))]


def _predicted(nb, K, G, L, R, na, nc):
    vals = set()
    for sa in range(nb + 1):
        for scc in range(nb + 1 - sa):
            p = na - sa
            if p < 0 or nc - scc != p or p > nb - sa - scc:
                continue
            om = nb - sa - scc
            for twoj in range(om, -1, -2):
                if abs(2 * p - om) > twoj:
                    continue
                j, mm = F(twoj, 2), F(2 * p - om, 2)
                vals.add(K * (2 * p + sa + scc) + L * (na - nc) ** 2 + R * (sa + scc) - G * (j + mm) * (j - mm + 1))
    return sorted(vals)


def _lowest(nb, K, G, L, R, na, nc):
    """Lowest eigenvalue (certified: PSD after the shift, singular) and one lowest eigenvector."""
    B, M = _matrix(nb, K, G, L, R, na, nc)
    e = _predicted(nb, K, G, L, R, na, nc)[0]
    Ms = _shift(M, e)
    if not _psd(Ms) or GA.mat_rank(Ms) == len(M):
        return None
    ker = GA.field_kernel(Ms)
    return e, ker, B


def _vec(B, v):
    return _clean({B[i]: v[i] for i in range(len(B))})


def _ip(x, y):
    return sum(c * y.get(S, F(0)) for S, c in x.items())


def _band(nb, n):                    # psi_n = (P*)^n Omega
    st = {frozenset(): F(1)}
    for _ in range(n):
        st = _pstar(nb, st)
    return st


def _band_energy(nb, K, G, n):
    return 2 * K * n - G * n * (nb - n + 1)


def check_no_order_parameter_in_a_sector():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("field-theory.imported-tower-limit")
    premise("field-theory.composite-scalars-mean-field-level")
    ok = True
    seen = 0
    for nb in FLOORS:
        for na in range(nb + 1):
            for nc in range(nb + 1):
                B = _basis(nb, na, nc)
                seen += len(B)
                x = _clean({S: F(i + 1, 2 + len(S)) for i, S in enumerate(B)})
                ok = ok and _ip(x, _p(nb, x)) == 0 and _ip(x, _pstar(nb, x)) == 0
    # degenerate couplings K/G = n_b/2 - n: E(n) = E(n+1) is the ground energy, and psi_n + psi_{n+1} has <P> != 0
    ok = ok and seen == 80
    for (nb, n) in DEGENERATE:
        G = F(1)
        K = G * (F(nb, 2) - n)
        en, en1 = _band_energy(nb, K, G, n), _band_energy(nb, K, G, n + 1)
        ok = ok and en == en1 and all(_band_energy(nb, K, G, k) > en for k in range(nb + 1) if k not in (n, n + 1))
        x = _clean({**_band(nb, n), **_band(nb, n + 1)})
        # <x, P x> = <psi_n, P psi_{n+1}> = |psi_{n+1}|^2 = (n+1)(n_b - n) |psi_n|^2
        nn = _ip(_band(nb, n), _band(nb, n))
        ok = ok and _ip(x, _p(nb, x)) == (n + 1) * (nb - n) * nn and nn > 0
    GA.check("a pair field has no expectation on sector vectors; at K/G = n_b/2 - n the ground band levels n, n+1 "
             "coincide and their sum has <P> = (n+1)(n_b - n)|psi_n|^2", ok)
    return ok


def check_variational_bounds_on_every_sector():
    premise("field-theory.imported-tower-limit")
    premise("synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy")
    ok = True
    hits = 0
    for (nb, K, G) in BOUND:
        for (L, R) in EXTRA:
            low = {}
            for na in range(nb + 1):
                for nc in range(nb + 1):
                    low[(na, nc)] = _lowest(nb, K, G, L, R, na, nc)
                    ok = ok and low[(na, nc)] is not None
            for (na, nc), (e, ker, B) in low.items():
                psi = _vec(B, ker[0])
                xp, xm = _pstar(nb, psi), _p(nb, psi)
                hx = _h(nb, K, G, L, R, xp)
                hxm = _h(nb, K, G, L, R, xm)
                if xp:
                    rq = _ip(xp, hx) / _ip(xp, xp) - e         # <X psi, [H, X] psi>/|X psi|^2
                    up = low[(na + 1, nc + 1)][0] - e
                    ok = ok and up <= rq and rq == 2 * K + G * (na + nc - nb)
                    hits += 1
                if xm:
                    rq = _ip(xm, hxm) / _ip(xm, xm) - e
                    dn = low[(na - 1, nc - 1)][0] - e
                    ok = ok and dn <= rq and rq == -2 * K - G * (na + nc - 2 - nb)
                    hits += 1
                if xp and xm:
                    second = low[(na + 1, nc + 1)][0] + low[(na - 1, nc - 1)][0] - 2 * e
                    ok = ok and second <= G
    ok = ok and hits == 208
    GA.check("on every sector of the n_b = 2, 3 floors, for four H_0 commuting with P: E(s +- h) - E(s) is at most "
             "the Rayleigh quotient, which is +-(2K + G c), and the second difference is at most 2G", ok)
    return ok


def check_single_shell_rotor_and_uniform_channel():
    premise("synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy")
    premise("field-theory.how-close-tower-comes-ccr")
    ok = True
    phases = [0, 0]
    for (nb, K, G) in SHELL:
        gamma = F(nb + 1, 2) - K / G
        es = [_band_energy(nb, K, G, n) for n in range(nb + 1)]
        ok = ok and all(es[n] == G * (n - gamma) ** 2 - G * gamma ** 2 for n in range(nb + 1))
        estar = min(es)
        nstar = es.index(estar)
        ok = ok and (abs(nstar - gamma) <= F(1, 2) or (nstar == 0 and gamma < F(1, 2)))
        # the band minimum is the ground energy of H_4 on the whole Fock space (every sector PSD after the shift)
        for na in range(nb + 1):
            for nc in range(nb + 1):
                _, M = _matrix(nb, K, G, F(0), F(0), na, nc)
                ok = ok and _psd(_shift(M, estar))
        psi = _band(nb, nstar)
        hp = _h(nb, K, G, F(0), F(0), psi)
        nn = _ip(psi, psi)
        ok = ok and GA.ext_state_eq(hp, {S: estar * c for S, c in psi.items()})
        if G * nb > 2 * K:
            phases[0] += 1
            up, dn = es[nstar + 1] - estar, es[nstar - 1] - estar
            ok = ok and up == G * (1 + 2 * (nstar - gamma)) and dn == G * (1 - 2 * (nstar - gamma))
            ok = ok and 0 <= up <= 2 * G and 0 <= dn <= 2 * G and up + dn == 2 * G
            # the uniform channel: (P + P*) psi = psi_{n*+1} + n*(n_b - n* + 1) psi_{n*-1}
            u = _clean({**_pstar(nb, psi)})
            _add_into(u, _p(nb, psi), F(1))
            target = dict(_band(nb, nstar + 1))
            _add_into(target, _band(nb, nstar - 1), F(nstar * (nb - nstar + 1)))
            ok = ok and GA.ext_state_eq(_clean(u), _clean(target))
            ok = ok and _ip(_pstar(nb, psi), _pstar(nb, psi)) == (nstar + 1) * (nb - nstar) * nn
            ok = ok and _ip(_p(nb, psi), _p(nb, psi)) == nstar * (nb - nstar + 1) * nn
            ok = ok and 2 * G / (G * nb) == F(2, nb) and max(up, dn) / (G * nb) <= F(2, nb)
        if G * nb < 2 * K:
            phases[1] += 1
            ok = ok and nstar == 0 and es[1] - es[0] == 2 * K - G * nb and 0 < es[1] < 2 * K
            ok = ok and 2 * K in _predicted(nb, K, G, F(0), F(0), 1, 1)
            # the ground state is unique: every other level is strictly positive
            for na in range(nb + 1):
                for nc in range(nb + 1):
                    if (na, nc) != (0, 0):
                        ok = ok and _predicted(nb, K, G, F(0), F(0), na, nc)[0] > 0
    ok = ok and phases == [7, 3]
    GA.check("single shell: the ground state is the band state nearest gamma; in the condensed phase both neighbours "
             "lie within 2G and carry all of (P + P*) psi; in the symmetric phase the bound pair sits at 2K - G n_b", ok)
    return ok


def check_collective_limit_at_fixed_gap():
    premise("synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy")
    ok = True
    E, K = F(5), F(3)                       # mean-field quasiparticle energy E = G n_b/2 > K
    prev = None
    for nb in range(4, 61):
        G = 2 * E / nb
        gamma = F(nb + 1, 2) - K / G
        es = [_band_energy(nb, K, G, n) for n in range(nb + 1)]
        nstar = es.index(min(es))
        up, dn = es[nstar + 1] - es[nstar], es[nstar - 1] - es[nstar]
        rot = max(up, dn)
        ok = ok and 0 < nstar < nb and abs(nstar - gamma) <= F(1, 2)
        ok = ok and rot <= 4 * E / nb and up + dn == 4 * E / nb and G * nb == 2 * E
        if prev is not None:
            ok = ok and 4 * E / nb < prev
        prev = 4 * E / nb
    ok = ok and prev == F(1, 3)
    GA.check("at fixed mean-field gap E = G n_b/2 the rotor splitting is at most 4E/n_b (1/3 at n_b = 60) while the "
             "pair-breaking threshold stays 2E", ok)
    return ok


if __name__ == "__main__":
    check_no_order_parameter_in_a_sector()
    check_variational_bounds_on_every_sector()
    check_single_shell_rotor_and_uniform_channel()
    check_collective_limit_at_fixed_gap()
