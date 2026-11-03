"""singularity.assembled-page-curve-up-typicality: exact checks of the capacity arm and the envelope.

(1) The capacity arm (Schmidt). For pure states psi in R (x) L given as rational dim R x dim L
    coefficient matrices (five shapes, one of deficient rank), rho_R = psi psi^T / tr and
    rho_L = psi^T psi / tr have characteristic polynomials with lambda^{dim L} chi_R = lambda^{dim R} chi_L
    (Faddeev-LeVerrier, exact), so the nonzero spectra coincide; the common rank is at most
    min(dim R, dim L), and the purity satisfies tr rho^2 >= 1/rank >= 1/dim L, the Renyi-2 form of
    S_R = S_L <= ln dim L. The von Neumann bound itself needs logarithms and is not evaluated.
(2) The envelope, in the maximally entangled idealisation of the eviction theorem (every h_k = ln 2),
    on an exact qubit model: r radiation qubits (thermal accumulation Sth = r ln 2) and l partner
    modes (dim L = 2^l, capacity C = l ln 2), min(r, l) Bell pairs. rho_R has rank 2^min(r,l) and
    rho_R^2 = rho_R / 2^min(r,l) (flat spectrum), so S_rad = min(r, l) ln 2 = min(Sth, C) exactly.
    Along an evaporation r = t, l = l0 - t (l0 = 6) the curve rises, turns over at t = l0/2 at half the
    initial entropy, falls, and vanishes at complete evaporation.
Not checked: saturation for Page-typical states (the imported Page theorem) and the thermal arm's
locality inputs; the subleading corrections.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

STATES = (
    [[1, 2, 0], [0, -1, 3]],
    [[2, 1, 1, 0], [1, -1, 0, 2], [0, 3, -2, 1]],
    [[1, 0], [2, 1], [-1, 1], [0, 3]],
    [[1, 2, 3], [2, 4, 6], [1, 0, -1]],
    [[F(1, 2), 1], [3, F(-2, 3)]],
)
L0 = 6


def transpose(A):
    return [list(c) for c in zip(*A)]


def scale(A, c):
    return [[c * x for x in row] for row in A]


def trace(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def charpoly(A):
    """Coefficients [c0, ..., cn] of det(lambda - A), by Faddeev-LeVerrier."""
    n = len(A)
    c = [F(0)] * (n + 1)
    c[n] = F(1)
    Mk = [[F(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        AM = GA.mat_mul(A, Mk)
        Mk = [[AM[i][j] + (c[n - k + 1] if i == j else 0) for j in range(n)] for i in range(n)]
        c[n - k] = -trace(GA.mat_mul(A, Mk)) / F(k)
    return c


def shift(p, s):
    return [F(0)] * s + p


def check_schmidt_equal_marginal_spectra():
    ok = True
    for psi in STATES:
        psi = GA.frac_matrix(psi)
        dR, dL = len(psi), len(psi[0])
        Z = trace(GA.mat_mul(psi, transpose(psi)))
        rR = scale(GA.mat_mul(psi, transpose(psi)), 1 / Z)
        rL = scale(GA.mat_mul(transpose(psi), psi), 1 / Z)
        ok = ok and trace(rR) == 1 and trace(rL) == 1
        ok = ok and shift(charpoly(rR), dL) == shift(charpoly(rL), dR)
        rk = GA.mat_rank(rR)
        ok = ok and rk == GA.mat_rank(rL) and rk <= min(dR, dL)
        pur = trace(GA.mat_mul(rR, rR))
        ok = ok and pur == trace(GA.mat_mul(rL, rL)) and pur * rk >= 1 and pur * dL >= 1
    ok = ok and GA.mat_rank(GA.frac_matrix(STATES[3])) == 2
    GA.check("pure bipartite states: equal nonzero marginal spectra, rank <= min dim, purity >= 1/dim L", ok)
    return ok


def bell_state(r, l):
    """Coefficient matrix (2^r x 2^l) of min(r, l) Bell pairs (R_j, L_j), the rest in |0>."""
    k = min(r, l)
    psi = [[F(0)] * (2 ** l) for _ in range(2 ** r)]
    for bits in range(2 ** k):
        psi[bits][bits] = F(1)
    return psi


def entropy_bits(psi):
    """For a flat-spectrum marginal returns log2 of its rank, else None."""
    Z = trace(GA.mat_mul(psi, transpose(psi)))
    rho = scale(GA.mat_mul(psi, transpose(psi)), 1 / Z)
    rk = GA.mat_rank(rho)
    if GA.mat_mul(rho, rho) != scale(rho, F(1, rk)):
        return None
    return rk.bit_length() - 1 if rk & (rk - 1) == 0 else None


def check_envelope_min_thermal_capacity():
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    premise("singularity.area-law-test")
    ok = True
    curve = []
    for t in range(L0 + 1):
        r, l = t, L0 - t
        s = entropy_bits(bell_state(r, l))
        ok = ok and s == min(r, l)
        curve.append(s)
    ok = ok and curve == [0, 1, 2, 3, 2, 1, 0]
    peak = max(curve)
    ok = ok and curve.index(peak) == 3 and 2 * peak == L0
    ok = ok and entropy_bits(bell_state(2, 5)) == 2 and entropy_bits(bell_state(4, 1)) == 1
    GA.check("maximally entangled envelope: S_rad = min(Sth, C) in units of ln 2; rises, turns over at half "
             "the initial entropy, falls, vanishes at complete evaporation", ok)
    return ok
