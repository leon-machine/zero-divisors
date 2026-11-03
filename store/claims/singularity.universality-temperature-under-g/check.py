"""singularity.universality-temperature-under-g: exact checks.

Four modes with weights w = (1, 2, 3, 0) (one mode of zero weight); K_geo = sum_k w_k N_k on the 16-dim
occupation basis; y = e^{-beta} rational, so e^{-beta K_geo} has entries y^(sum w_k n_k).
(1) Forward: the Gibbs state of K_geo (built from its spectrum) is the product of the marginals, and each
    marginal (partial trace) is diag(1, y^w_k)/(1 + y^w_k) = Gibbs(beta w_k): beta_k = beta for every mode of
    nonzero weight; the zero-weight marginal is diag(1, 1)/2 for every y (beta_k is not defined there).
    Checked at y = 2/3 and y = 5/4.
(2) Converse: a product of per-mode Gibbs marginals with Boltzmann factors x_k = e^{-beta_k w_k} equals a
    Gibbs state of K_geo for some y iff x_k = y^w_k for one y on the nonzero-weight modes. Its population
    ratio p(e_1)/p(0) = x_1 forces y = x_1 (w_1 = 1), and the product state is compared entrywise with the
    K_geo Gibbs state at that y: equal for x = (y, y^2, y^3, 1) (the zero-weight factor is e^0 = 1), unequal
    for each of three single-mode deviations (one beta_k changed). Checked at y = 2/3 and y = 5/4.
"""
import GA
from fractions import Fraction as F
from itertools import product

from tp_premise import premise

W = (1, 2, 3, 0)
STATES = list(product((0, 1), repeat=4))


def kgeo_gibbs(y):
    wts = [y ** sum(w * n for w, n in zip(W, s)) for s in STATES]
    Z = sum(wts)
    return {s: wt / Z for s, wt in zip(STATES, wts)}


def product_state(xs):
    out = {}
    for s in STATES:
        p = F(1)
        for x, n in zip(xs, s):
            p *= (x if n else 1) / (1 + x)
        out[s] = p
    return out


def marginal(rho, k):
    p1 = sum(p for s, p in rho.items() if s[k] == 1)
    return (1 - p1, p1)


def check_g_gives_one_temperature():
    premise("singularity.kms-uniqueness-factor")
    ok = True
    for y in (F(2, 3), F(5, 4)):
        rho = kgeo_gibbs(y)
        ok = ok and sum(rho.values()) == 1
        margs = [marginal(rho, k) for k in range(4)]
        for k in range(4):
            xk = y ** W[k]
            ok = ok and margs[k] == (1 / (1 + xk), xk / (1 + xk))
        ok = ok and margs[3] == (F(1, 2), F(1, 2))
        ok = ok and product_state([y ** w for w in W]) == rho
        # the Boltzmann factor of each nonzero-weight marginal is y^w_k: the same beta
        for k in range(3):
            ratio = margs[k][1] / margs[k][0]
            ok = ok and ratio == y ** W[k] and ratio != y ** (W[k] + 1)
    _tp_rv = (ok); assert _tp_rv is not False, "check_g_gives_one_temperature"; return _tp_rv


def check_product_satisfies_g_only_at_equal_betas():
    premise("singularity.kms-uniqueness-factor")
    ok = True
    for y in (F(2, 3), F(5, 4)):
        good = [y, y ** 2, y ** 3, F(1)]
        rho = product_state(good)
        y_forced = rho[(1, 0, 0, 0)] / rho[(0, 0, 0, 0)]
        ok = ok and y_forced == y and rho == kgeo_gibbs(y_forced)
        bads = [[y, F(1, 2), y ** 3, F(1)], [y, y ** 2, F(7, 3), F(1)], [y, y ** 2, y ** 3, F(3)]]
        for xs in bads:
            r2 = product_state(xs)
            yf = r2[(1, 0, 0, 0)] / r2[(0, 0, 0, 0)]
            ok = ok and yf == y and r2 != kgeo_gibbs(yf)
    _tp_rv = (ok); assert _tp_rv is not False, "check_product_satisfies_g_only_at_equal_betas"; return _tp_rv
