"""field-theory.ground-does-not-attach-modes: exact checks.

Ground Cl(2,4) on generators 0..5 (0, 1 square +1, 2..5 square -1), three higher planes (6,7), (8,9), (10,11)
(e^2 = 1, f^2 = -1), mode operators v = (e + f)/2, w = (e - f)/2.
(1) Every one of the 32 even ground blades commutes with all six mode operators; every ground vector anticommutes
    with them (the odd part acts by a sign), so the even ground acts trivially on the modes.
(2) In particular: the 15 conformal bivectors; chart translations 1 + n_inf a/2 for n_inf = e0 + e2 (null) and
    a = e1, e3, e4 + e5 (each a rotor, T T~ = 1); boost and rotation rotors with rational rapidity and angle
    (and their product): Ad of each fixes every mode operator.
(3) Covariance then forces constant mode functions: with Ad(T_a) the identity on the modes, psi(x + a) =
    Ad(T_a) psi(x) reads sum_j u_j(x + a) a_j = sum_j u_j(x) a_j, and the mode operators are linearly independent
    (rank 6), so u_j(x + a) = u_j(x). The finite-floor obstruction for noncompact groups is not computed.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

S = (1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1)
PLANES = [(6, 7), (8, 9), (10, 11)]
TRANS_DIRS = [{(1,): F(1)}, {(3,): F(1)}, {(4,): F(1), (5,): F(1)}]
# Covariance sample: the chart translation T = 1 + n_inf a/2 with n_inf = e0 + e2 and a = e1, and
# sample constant coefficients u_j of a field psi = sum_j u_j a_j.
COV_NINF = GA.add(GA.gen(0), GA.gen(2))
COV_DIR = GA.gen(1)
COV_COEFFS = [F(3), F(-1, 2), F(2), F(0), F(5, 7), F(1)]


def _scl(c, x):
    return {b: c * v for b, v in x.items() if c * v != 0}


def _mul(x, y):
    return GA.mul(x, y, S)


def _modes():
    out = []
    for e, f in PLANES:
        out.append(GA.add(_scl(F(1, 2), GA.gen(e)), _scl(F(1, 2), GA.gen(f))))
        out.append(GA.add(_scl(F(1, 2), GA.gen(e)), _scl(F(-1, 2), GA.gen(f))))
    return out


def _coords(x, blades):
    """Coordinates of the multivector x on the listed blades."""
    return [x.get(b, F(0)) for b in blades]


def _translation(ninf, a):
    """The translation rotor T = 1 + n_inf a/2 and its inverse 1 - n_inf a/2."""
    X = _scl(F(1, 2), _mul(ninf, a))
    return GA.add(GA.sc(1), X), GA.sub(GA.sc(1), X)


def _fixes(R, Ri, modes):
    return GA.eq(_mul(R, Ri), GA.sc(1)) and all(GA.eq(_mul(_mul(R, m), Ri), m) for m in modes)


def check_even_ground_commutes_with_modes():
    premise("tower.volume-elements-planes")
    premise("tower.commuting-copies")
    modes = _modes()
    even = [{b: F(1)} for k in range(0, 7, 2) for b in combinations(range(6), k)]
    ok = len(even) == 32 and all(GA.commutes(B, m, S) for B in even for m in modes)
    ok = ok and all(GA.anticommutes(GA.gen(i), m, S) for i in range(6) for m in modes)
    biv = [_mul(GA.gen(i), GA.gen(j)) for i, j in combinations(range(6), 2)]
    ok = ok and len(biv) == 15 and all(GA.commutes(B, m, S) for B in biv for m in modes)
    GA.check("all 32 even ground blades commute with every mode operator; ground vectors anticommute", ok)
    return ok


def check_translations_and_lorentz_rotors_act_trivially():
    premise("tower.volume-elements-planes")
    modes = _modes()
    ninf = GA.add(GA.gen(0), GA.gen(2))
    ok = GA.is_zero(_mul(ninf, ninf))
    for a in TRANS_DIRS:
        X = _scl(F(1, 2), _mul(ninf, a))
        T, Ti = GA.add(GA.sc(1), X), GA.sub(GA.sc(1), X)
        ok = ok and GA.eq(_mul(T, GA.reverse(T)), GA.sc(1)) and _fixes(T, Ti, modes)
    Bb = _mul(GA.gen(1), GA.gen(3))
    Br = _mul(GA.gen(3), GA.gen(4))
    Rb, Rbi = GA.add(GA.sc(F(5, 4)), _scl(F(3, 4), Bb)), GA.add(GA.sc(F(5, 4)), _scl(F(-3, 4), Bb))
    Rr, Rri = GA.add(GA.sc(F(3, 5)), _scl(F(4, 5), Br)), GA.add(GA.sc(F(3, 5)), _scl(F(-4, 5), Br))
    ok = ok and GA.eq(_mul(Bb, Bb), GA.sc(1)) and GA.eq(_mul(Br, Br), GA.sc(-1))
    ok = ok and _fixes(Rb, Rbi, modes) and _fixes(Rr, Rri, modes) and _fixes(_mul(Rb, Rr), _mul(Rri, Rbi), modes)
    GA.check("translation rotors and Lorentz rotors of the ground fix every mode operator", ok)
    return ok


def check_covariance_forces_constant_mode_functions():
    premise("tower.commuting-copies")
    modes = _modes()
    blades = sorted(set(b for m in modes for b in m))
    rows = [_coords(m, blades) for m in modes]
    rank = GA.rank_of_vectors(rows)
    T, Ti = _translation(COV_NINF, COV_DIR)
    # a field psi = sum_j u_j a_j with sample coefficients: Ad(T) psi = psi, so the shifted coefficients must agree
    u = COV_COEFFS
    psi = GA.add(*[_scl(c, m) for c, m in zip(u, modes) if c != 0])
    moved = _mul(_mul(T, psi), Ti)
    square = rank == len(modes) == len(blades)
    coeffs = GA.field_solve([list(col) for col in zip(*rows)], _coords(moved, blades)) if square else None
    ok = rank == 6 and len(blades) == 6 and coeffs == u
    GA.check("the mode operators are independent (rank 6) and Ad(translation) returns the same coefficients", ok)
    return ok
