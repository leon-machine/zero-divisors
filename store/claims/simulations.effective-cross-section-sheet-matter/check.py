"""simulations.effective-cross-section-sheet-matter: exact checks.

(1) Number density by counting: sheets at heights z = k s (k = 0..K-1) carrying quanta on a square
    lattice of spacing a (n2 = 1/a^2 per unit area) are counted in boxes L x L x K s; the count is
    K (L/a)^2, so n3 = count / volume = n2 / s, for sample (a, s, L, K).
(2) Collision rate: a quantum moving in its sheet at speed v for time tau sweeps the area lambda v tau
    and meets n2 lambda v tau quanta; a three-dimensional gas of density n3 meets n3 sigma v tau.
    Solving for sigma gives sigma_eff = lambda s, and sigma_eff/m = lambda s/m; the rates agree at
    sample values.
(3) Spacing under compression by Delta in volume at redshift z, comoving mean spacing d_b (R3):
    a compression with normal factor alpha and in-plane factor beta (alpha beta^2 = 1/Delta,
    both <= 1) gives spacing alpha d_b/(1+z); alpha = 1/Delta (all along the normal), alpha = 1 (all
    in the plane), alpha = Delta^(-1/3) (isotropic) are the three cases, and every split lies
    between the first two. Checked at perfect-cube Delta (exact cube roots) and, for general
    Delta, through cubes: (d_b/(Delta (1+z)))^3 <= d_b^3/(Delta (1+z)^3) <= (d_b/(1+z))^3.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

LATTICE = [(F(1, 2), F(3), F(4), 3), (F(1), F(2), F(5), 4), (F(1, 3), F(1, 2), F(2), 2)]
RATES = [(F(5), F(2), F(1, 3), F(7), F(10), F(3)), (F(1, 4), F(9), F(2), F(1, 2), F(4), F(1, 10))]
DELTAS = [F(8), F(27), F(125), F(1000), F(64, 27)]
ZS = [F(0), F(1), F(3, 2), F(5)]


def check_number_density_by_counting():
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    ok = True
    expect = [(192, F(4, 3)), (100, F(1, 2)), (72, F(18))]       # counted by hand
    for (a, s, L, K), (cnt, dens) in zip(LATTICE, expect):
        # lattice points (i a, j a) with 0 <= i a < L, 0 <= j a < L in each of K sheets
        per_side = sum(1 for i in range(0, 100) if i * a < L)
        count = K * per_side * per_side
        n2 = 1 / (a * a)
        n3 = F(count) / (L * L * K * s)
        ok = ok and count == cnt and n3 == dens and n3 == n2 / s
    GA.check("counting quanta in boxes: n3 = n2 / s", ok)
    return ok


def check_collision_rate_equivalence():
    ok = True
    expect = [(F(2, 3), F(2, 9)), (F(18), F(180))]                 # (lambda s, lambda s / m) by hand
    for (n2, lam, s, v, tau, m), (sig, per_m) in zip(RATES, expect):
        hits_sheet = n2 * lam * v * tau
        n3 = n2 / s
        sigma = hits_sheet / (n3 * v * tau)            # the 3D cross-section with the same rate
        ok = ok and sigma == sig and sigma / m == per_m
        ok = ok and n3 * sigma * v == n2 * lam * v
    GA.check("collision rate n2 lambda v = n3 sigma_eff v with sigma_eff = lambda s", ok)
    return ok


def _cube_root(x):
    for k in range(1, 50):
        for d in range(1, 50):
            if F(k, d) ** 3 == x:
                return F(k, d)
    return None


def check_spacing_bounds_under_compression():
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    ok = True
    db = F(1)
    # hand values of the isotropic spacing: Delta = 8 at z = 1 gives 1/4, Delta = 1000 at z = 5 gives 1/60
    ok = ok and db / (_cube_root(F(8)) * 2) == F(1, 4) and db / (_cube_root(F(1000)) * 6) == F(1, 60)
    for D in DELTAS:
        r = _cube_root(D)
        ok = ok and r is not None
        for z in ZS:
            lo, hi, iso = db / (D * (1 + z)), db / (1 + z), db / (r * (1 + z))
            ok = ok and lo <= iso <= hi and lo < hi
            ok = ok and iso ** 3 == db ** 3 / (D * (1 + z) ** 3)
            # isotropic: each length factor 1/r, volume factor 1/D
            ok = ok and (1 / r) ** 3 == 1 / D
            # general splits: beta from Delta^(-1/2) to 1 (squares chosen exactly), alpha = 1/(Delta beta^2)
            for beta2 in (1 / D, F(1, 2) + F(1, 2) / D, F(1)):
                alpha = 1 / (D * beta2)
                ok = ok and alpha * beta2 == 1 / D and 1 / D <= alpha <= 1
                ok = ok and lo <= alpha * db / (1 + z) <= hi
    for D in (F(2), F(5), F(10)):
        for z in ZS:
            lo3 = (db / (D * (1 + z))) ** 3
            iso3 = db ** 3 / (D * (1 + z) ** 3)
            hi3 = (db / (1 + z)) ** 3
            ok = ok and lo3 < iso3 < hi3
    GA.check("spacing d_b Delta^(-1/3)/(1+z) between d_b/(Delta(1+z)) and d_b/(1+z)", ok)
    return ok
