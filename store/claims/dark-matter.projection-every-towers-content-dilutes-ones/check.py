"""dark-matter.projection-every-towers-content-dilutes-ones: exact checks.

The sourcing rule of P1, modelled directly at exact sample scale factors a: a tower with D spatial
directions shares min(D,3) of them (proper length a per comoving unit); its D - 3 extra directions (if
any) have proper extent a (co-expanding) or 1 (static); a missing shared direction (D = 2) is filled by
sheets one per unit comoving length (proper spacing a), or, in the reading the lemma excludes, by a
single sheet of fixed thickness. N quanta in a comoving cell have tower number density
N/(a^shared ext^extra); integrating over the extra directions multiplies by ext^extra and the sheets
contribute 1/(spacing) per missing direction, giving the density per unit shared three-volume. Each
quantum carries m (non-relativistic) or a momentum redshifting as 1/a (radiation, the zero modes).
Checked for D = 2, 3, 4, co-expanding and static, at a = 2, 3/2, 7/3, 5: rho_matter(a)/rho_matter(1)
= a^-3 and rho_rad(a)/rho_rad(1) = a^-4 in every case (no tower diluted away or into prominence),
while the single-sheet reading gives a^-2 and a^-3 for D = 2.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SAMPLES = [F(2), F(3, 2), F(7, 3), F(5)]
N_QUANTA, MASS, P0, THICK = F(17), F(3), F(5), F(1, 4)


def projected(D, coexpand, a, sheets=True):
    shared = min(D, 3)
    extra = max(D - 3, 0)
    missing = max(3 - D, 0)
    ext = a if coexpand else F(1)
    n_tower = N_QUANTA / (a ** shared * ext ** extra)
    n_proj = n_tower * ext ** extra
    spacing = a if sheets else THICK
    n_proj = n_proj / spacing ** missing
    return n_proj * MASS, n_proj * P0 / a


def check_projected_dilution_matches_this_tower():
    premise("dark-matter.p1-single-frozen-point")
    ok = True
    cases = 0
    for D in (2, 3, 4):
        for co in (True, False):
            m1, r1 = projected(D, co, F(1))
            for a in SAMPLES:
                m, r = projected(D, co, a)
                ok = ok and m / m1 == a ** -3 and r / r1 == a ** -4
                cases += 1
    ok = ok and cases == 24
    GA.check("lem:projection: matter a^-3 and radiation a^-4 for D = 2, 3, 4, co-expanding or static (24 cases)", ok)
    return ok


def check_single_sheet_reading_is_excluded():
    premise("dark-matter.p1-single-frozen-point")
    ok = True
    for co in (True, False):
        m1, r1 = projected(2, co, F(1), sheets=False)
        for a in SAMPLES:
            m, r = projected(2, co, a, sheets=False)
            ok = ok and m / m1 == a ** -2 and r / r1 == a ** -3
            ok = ok and m / m1 != a ** -3
    GA.check("lem:projection: a single fixed sheet for the missing direction would give a^-2 and a^-3 (excluded)", ok)
    return ok
