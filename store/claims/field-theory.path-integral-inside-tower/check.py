"""field-theory.path-integral-inside-tower: exact checks.

Grassmann variables: the blade engine with all squares 0 (exterior algebra); the Berezin integral
over prod_m dpsibar_m dpsi_m is (-1)^(M) times the top coefficient (int dpsibar dpsi e^{-a psibar
psi} = a). The sliced action S = sum_m psibar_m psi_m - t psibar_m psi_{m-1}, psi_0 = eta psi_M,
t = 1 - delta (H = N on one mode, delta = beta eps/M), eta = -1 (antiperiodic) or +1 (periodic).
(1) Grassmann variables are further rungs: in the tower (planes of squares +1, -1, premise
tower-limit) the creation vectors of four further rungs square to 0, anticommute pairwise and with
the physical pair, and have a nonzero top product; with the rung vectors as Grassmann generators and
the Berezin integral realised as w...w x P0 (P0 the rungs' vacuum projector), the M = 2 integrals are
the abstract ones (one overall sign fixed once).
(2) Exact slicing: Berezin(exp(-S)) = det(A) = 1 - eta t^M = Tr(1 - delta N)^M (eta = -1) and
Tr Gamma (1 - delta N)^M (eta = +1), M = 1..5, delta = 1/3, 2/7, 5/4; two modes factorise.
(3) The limit: the occupancy at slicing M is t^M/(1 + t^M); with x = beta eps = 1, e^{-1} is
bracketed by alternating partial sums and (1 - 1/M)^M lies in [lo (1 - 1/M), hi] at M = 100, 1000
(e^{-x}(1 - x^2/M) <= (1 - x/M)^M <= e^{-x}), so Tr(1 - delta N)^M -> 1 + e^{-1} = Tr e^{-beta H}
and the occupancy -> 1/(e + 1), Fermi-Dirac, with an interval of width < 1/M around it.
(4) Two-point function: <psi_m psibar_n> from the Berezin integral depends on m - n only, equals the
time-ordered operator function (Gamma inserted for the periodic closure), and G(j - M) = eta G(j):
antiperiodic for the trace, periodic for the supertrace, at every slicing M = 2, 3, 4.
The period (the identification of the Euclidean circle) is imported and not checked.
"""
from fractions import Fraction as F

import GA
from GA import mul, add, neg, sc, gen, eq, is_zero, anticommutes
from tp_premise import premise

ST = tuple([1, -1] * 5)
GR = tuple([0] * 40)
DELTAS = [F(1, 3), F(2, 7), F(5, 4)]


def scl(c, x):
    return {b: c * v for b, v in x.items() if c * v != 0}


def pair(e, f):
    return (add(scl(F(1, 2), gen(e)), scl(F(1, 2), gen(f))),
            add(scl(F(1, 2), gen(e)), scl(F(-1, 2), gen(f))))


def exp_nil(X, s, nmax):
    out, term = sc(1), sc(1)
    for n in range(1, nmax + 1):
        term = scl(F(1, n), mul(term, X, s))
        if not term:
            break
        out = add(out, term)
    return out


def action(M, t, eta, base=0):
    Sx = {}
    for m in range(1, M + 1):
        pb = base + 2 * (m - 1)
        Sx = add(Sx, {(pb, pb + 1): F(1)})
        prev, c = (pb - 1, -t) if m >= 2 else (base + 2 * (M - 1) + 1, -t * eta)
        Sx = add(Sx, scl(c, mul(gen(pb), gen(prev), GR)))
    return Sx


def berezin(x, ngen):
    return F((-1) ** (ngen // 2)) * x.get(tuple(range(ngen)), F(0))


def mid(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def mmul(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(len(B))), F(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def mtrace(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def mdet(A):
    M = [list(r) for r in A]
    n, det = len(M), F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return F(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det
        det *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return det


def diff_matrix(M, t, eta):
    A = mid(M)
    for m in range(1, M):
        A[m][m - 1] = -t
    A[0][M - 1] += -t * eta
    return A


def tmat_power(t, M):
    T, out = [[F(1), F(0)], [F(0), t]], mid(2)
    for _ in range(M):
        out = mmul(out, T)
    return out


def check_grassmann_variables_are_rungs():
    premise("field-theory.imported-tower-limit")
    vp, wp = pair(0, 1)
    rungs = [pair(2 * j, 2 * j + 1) for j in range(1, 5)]
    us = [r[0] for r in rungs]
    ws = [r[1] for r in rungs]
    assert all(is_zero(mul(u, u, ST)) for u in us)
    assert all(anticommutes(us[i], us[j], ST) for i in range(4) for j in range(i + 1, 4))
    assert all(anticommutes(u, x, ST) for u in us for x in (vp, wp))
    top = sc(1)
    for u in us:
        top = mul(top, u, ST)
    assert not is_zero(top) and len(next(iter(top))) >= 4
    P0 = sc(1)
    for j in range(4):
        P0 = mul(P0, mul(ws[j], us[j], ST), ST)

    def tower_berezin(x):
        y = x
        for j in range(4):
            y = mul(ws[j], y, ST)
        y = mul(y, P0, ST)
        b0, c0 = next(iter(P0.items()))
        c = y.get(b0, F(0)) / c0
        assert eq(y, scl(c, P0))
        return c

    def to_tower(x):
        out = {}
        for b, c in x.items():
            term = sc(c)
            for g in b:
                term = mul(term, us[g], ST)
            out = add(out, term)
        return out

    sgn = tower_berezin(to_tower(exp_nil(neg(action(2, F(1, 2), 0)), GR, 4)))
    sgn = sgn / berezin(exp_nil(neg(action(2, F(1, 2), 0)), GR, 4), 4)
    assert sgn in (F(1), F(-1))
    for t in (F(2, 3), F(-1, 4)):
        for eta in (-1, 1):
            xx = exp_nil(neg(action(2, t, eta)), GR, 4)
            assert tower_berezin(to_tower(xx)) == sgn * (1 - eta * t ** 2)


def check_exact_slicing_is_trace():
    Gam = [[F(1), F(0)], [F(0), F(-1)]]
    cases = 0
    for M in range(1, 6):
        for delta in DELTAS:
            t = 1 - delta
            for eta in (-1, 1):
                Z = berezin(exp_nil(neg(action(M, t, eta)), GR, 2 * M), 2 * M)
                TM = tmat_power(t, M)
                trace = mtrace(TM) if eta == -1 else mtrace(mmul(Gam, TM))
                assert Z == mdet(diff_matrix(M, t, eta)) == 1 - eta * t ** M == trace
                cases += 1
    assert cases == 30
    for M in (2, 3):
        t1, t2 = F(2, 3), F(5, 7)
        S12 = add(action(M, t1, -1, 0), action(M, t2, -1, 2 * M))
        assert berezin(exp_nil(neg(S12), GR, 4 * M), 4 * M) == (1 + t1 ** M) * (1 + t2 ** M)


def check_continuum_limit_gibbs_and_fermi_dirac():
    fact = [1]
    for k in range(1, 20):
        fact.append(fact[-1] * k)
    lo = sum((F((-1) ** k, fact[k]) for k in range(0, 14)), F(0))       # ends on a negative term
    hi = sum((F((-1) ** k, fact[k]) for k in range(0, 13)), F(0))
    assert lo < hi and hi - lo < F(1, 10 ** 9)
    Nn = [[F(0), F(0)], [F(0), F(1)]]
    for M in (1, 2, 5, 10):
        t = 1 - F(1, M)
        TM = tmat_power(t, M)
        assert mtrace(mmul(Nn, TM)) / mtrace(TM) == t ** M / (1 + t ** M)
    fd = lambda y: y / (1 + y)
    for M in (100, 1000):
        tM = (1 - F(1, M)) ** M
        assert lo * (1 - F(1, M)) <= tM <= hi
        # Tr(1 - delta N)^M = 1 + t^M within [1 + lo(1 - 1/M), 1 + hi] around 1 + e^{-1}
        nM = fd(tM)
        assert fd(lo * (1 - F(1, M))) <= nM <= fd(hi) and fd(hi) - fd(lo * (1 - F(1, M))) < F(1, M)
    # the Fermi-Dirac value 1/(e + 1) = e^{-1}/(1 + e^{-1}) lies in [fd(lo), fd(hi)]
    assert fd(lo) < fd(hi) and fd(lo) > F(26, 100) and fd(hi) < F(27, 100)


def check_two_point_function_matsubara():
    a = [[F(0), F(1)], [F(0), F(0)]]
    ad = [[F(0), F(0)], [F(1), F(0)]]
    for M in (2, 3, 4):
        for t in (F(2, 3), F(-1, 4)):
            for eta in (-1, 1):
                ex = exp_nil(neg(action(M, t, eta)), GR, 2 * M)
                Z = berezin(ex, 2 * M)
                Gam = [[F(1), F(0)], [F(0), F(-1)]] if eta == 1 else mid(2)
                Tp = [tmat_power(t, j) for j in range(M + 1)]
                Zop = mtrace(mmul(Gam, Tp[M]))
                Gby = {}
                for m in range(1, M + 1):
                    for n in range(1, M + 1):
                        ins = mul(gen(2 * (m - 1) + 1), gen(2 * (n - 1)), GR)
                        G = berezin(mul(ins, ex, GR), 2 * M) / Z
                        j = m - n
                        if j >= 0:
                            op = mtrace(mmul(Gam, mmul(Tp[M - j], mmul(a, mmul(Tp[j], ad))))) / Zop
                        else:
                            op = -mtrace(mmul(Gam, mmul(Tp[M + j], mmul(ad, mmul(Tp[-j], a))))) / Zop
                        assert G == op
                        if j in Gby:
                            assert Gby[j] == G
                        Gby[j] = G
                for j in range(1, M):
                    assert Gby[j - M] == eta * Gby[j] and Gby[j] != 0
