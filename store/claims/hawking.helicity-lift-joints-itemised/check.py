"""hawking.helicity-lift-joints-itemised: exact checks of the computable joints.

J1 (Fact hawking.imported-penrose-transform): helicity s <-> homogeneity -2s - 2; the table: photon s = +1, -1 at
    -4, 0 and graviton s = +2, -2 at -6, +2, and the map s -> -2s - 2 is injective with inverse h -> -(h + 2)/2.
J2 (Proposition hawking.homogeneity-ordering-shift with the shift of Fact
    hawking.imported-twistor-storey-ordering-shift): on polynomials in Z^0..Z^3, Zbar_a = -d/dZ^a (hbar = 1),
    q(id) = 1/2 sum_a (Z^a Zbar_a + Zbar_a Z^a) equals -(Upsilon + 2) on every monomial of degree <= 3, so a
    homogeneous function of degree h has helicity s = q(id)/2 eigenvalue -(h + 2)/2; the offset -2 is the
    ordering shift (the normal-ordered generator sum Z^a Zbar_a gives -Upsilon, no offset).
J3 (the s-wave reduction) is a modelling joint with no computable content and is not checked.
"""
import GA
from fractions import Fraction as F
from itertools import product

from tp_premise import premise

HELICITIES = [(1, "photon"), (-1, "photon"), (2, "graviton"), (-2, "graviton")]


def check_homogeneity_table():
    premise("hawking.imported-penrose-transform")
    table = {s: -2 * s - 2 for s, _ in HELICITIES}
    ok = table == {1: -4, -1: 0, 2: -6, -2: 2}
    ok = ok and all(F(-(h + 2), 2) == s for s, h in table.items())
    ok = ok and len(set(table.values())) == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_homogeneity_table"; return _tp_rv


def mono_Z(a, f):
    out = {}
    for ex, c in f.items():
        e = list(ex)
        e[a] += 1
        out[tuple(e)] = out.get(tuple(e), F(0)) + c
    return out


def mono_Zbar(a, f):
    out = {}
    for ex, c in f.items():
        if ex[a] == 0:
            continue
        e = list(ex)
        e[a] -= 1
        out[tuple(e)] = out.get(tuple(e), F(0)) - c * ex[a]
    return out


def add_into(out, f, coef):
    for ex, c in f.items():
        out[ex] = out.get(ex, F(0)) + coef * c


def check_helicity_is_the_shifted_euler_charge():
    premise("hawking.homogeneity-ordering-shift")
    premise("hawking.imported-twistor-storey-ordering-shift")
    ok = True
    count = 0
    for ex in product(range(4), repeat=4):
        deg = sum(ex)
        if deg > 3:
            continue
        f = {ex: F(1)}
        sym, normal = {}, {}
        for a in range(4):
            add_into(sym, mono_Z(a, mono_Zbar(a, f)), F(1, 2))
            add_into(sym, mono_Zbar(a, mono_Z(a, f)), F(1, 2))
            add_into(normal, mono_Z(a, mono_Zbar(a, f)), F(1))
        ok = ok and sym == {ex: F(-(deg + 2))} and normal == ({ex: F(-deg)} if deg else {})
        ok = ok and sym[ex] / 2 == F(-(deg + 2), 2)
        count += 1
    _tp_rv = (ok and count == 35); assert _tp_rv is not False, "check_helicity_is_the_shifted_euler_charge"; return _tp_rv
