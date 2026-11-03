"""three-routes.support-preserving-families-quantise-without-hopping: exact checks.

Finite truncations F = {x_1, ..., x_N} with r fermionic modes per point ((N, r) = (2, 1), (3, 1), (4, 1),
(2, 2)): Jordan-Wigner annihilators psi_m as exact integer matrices on the 2^(N r) Fock states (CAR checked),
N_x = sum of psi^dag psi over the modes of x, and dGamma(a) = sum_ij a_ij psi_i^dag psi_j.
(1) For a bundle map a (block diagonal over the points, the form a C^infty-linear map takes by the
    support lemma; general integer blocks), dGamma(a) is the sum of the single-point bilinears
    dGamma(a_x) and commutes with every N_x.
(2) Exhaustively over matrix units: dGamma(E_ij) commutes with every occupation number iff modes i and j
    sit at the same point; for i at x != y at j, psi_i^dag psi_j fails to commute with N_x and maps the
    state with only mode j occupied (sector (N_x, N_y) = (0, 1)) to plus or minus the state with only mode i
    occupied (sector (1, 0)).
(3) Cross-point diagonal products: sigma_x sigma_y (sigma = psi^dag psi - psi psi^dag at a point, r = 1)
    commutes with every N_z: it conserves occupations and is not hopping.
"""
from fractions import Fraction as F  # noqa: F401

import GA  # noqa: F401
from tp_premise import premise

CASES = [(2, 1), (3, 1), (4, 1), (2, 2)]


def _zeros(d):
    return [[0] * d for _ in range(d)]


def _eye_i(d):
    return [[1 if i == j else 0 for j in range(d)] for i in range(d)]


def _imm(A, B):
    d = len(A)
    out = _zeros(d)
    for i in range(d):
        Ai = A[i]
        Oi = out[i]
        for t in range(d):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(d):
                    if Bt[j]:
                        Oi[j] += a * Bt[j]
    return out


def _iadd(*Ms):
    d = len(Ms[0])
    return [[sum(M[i][j] for M in Ms) for j in range(d)] for i in range(d)]


def _iscal(c, A):
    return [[c * x for x in row] for row in A]


def _itr(A):
    return [list(r) for r in zip(*A)]


def _comm(A, B):
    return _iadd(_imm(A, B), _iscal(-1, _imm(B, A)))


def _is_zero(A):
    return all(x == 0 for row in A for x in row)


def annihilators(nmodes):
    """Jordan-Wigner annihilators on 2^nmodes states; bit i of a basis index = occupation of mode i."""
    d = 2 ** nmodes
    out = []
    for i in range(nmodes):
        M = _zeros(d)
        for b in range(d):
            if b >> i & 1:
                M[b ^ (1 << i)][b] = (-1) ** bin(b & ((1 << i) - 1)).count("1")
        out.append(M)
    return out


def setup(N, r):
    nm = N * r
    a = annihilators(nm)
    ad = [_itr(x) for x in a]
    occ = [_iadd(*[_imm(ad[x * r + t], a[x * r + t]) for t in range(r)]) for x in range(N)]
    return nm, a, ad, occ


def dgamma(A, a, ad):
    nm = len(a)
    terms = [_iscal(A[i][j], _imm(ad[i], a[j])) for i in range(nm) for j in range(nm) if A[i][j]]
    return _iadd(*terms) if terms else _zeros(len(a[0]))


def check_bundle_maps_conserve_every_occupation():
    premise("three-routes.function-linear-maps-preserve-supports")
    ok = True
    for N, r in CASES:
        nm, a, ad, occ = setup(N, r)
        d = 2 ** nm
        ok = ok and all(_iadd(_imm(a[i], ad[j]), _imm(ad[j], a[i])) == (_eye_i(d) if i == j else _zeros(d))
                        for i in range(nm) for j in range(nm))
        A = [[(i + 2 * j + 1) if i // r == j // r else 0 for j in range(nm)] for i in range(nm)]
        D = dgamma(A, a, ad)
        parts = [dgamma([[A[i][j] if i // r == x == j // r else 0 for j in range(nm)] for i in range(nm)], a, ad)
                 for x in range(N)]
        ok = ok and D == _iadd(*parts) and not _is_zero(D)
        ok = ok and all(_is_zero(_comm(D, Nx)) for Nx in occ)
        ok = ok and all(_is_zero(_comm(P, Nx)) for P in parts for Nx in occ)
    _tp_rv = (ok); assert _tp_rv is not False, "check_bundle_maps_conserve_every_occupation"; return _tp_rv


def check_cross_components_hop():
    ok = True
    hops = 0
    for N, r in CASES:
        nm, a, ad, occ = setup(N, r)
        for i in range(nm):
            for j in range(nm):
                E = _imm(ad[i], a[j])
                conserves = all(_is_zero(_comm(E, Nx)) for Nx in occ)
                ok = ok and conserves == (i // r == j // r)
                if i // r != j // r:
                    ok = ok and not _is_zero(_comm(E, occ[i // r]))
                    src = 1 << j
                    col = [E[b][src] for b in range(2 ** nm)]
                    ok = ok and [b for b in range(2 ** nm) if col[b]] == [1 << i] and abs(col[1 << i]) == 1
                    hops += 1
    _tp_rv = (ok and hops == 2 + 6 + 12 + 8); assert _tp_rv is not False, "check_cross_components_hop"; return _tp_rv


def check_cross_point_diagonal_products_are_not_hopping():
    ok = True
    for N, r in CASES:
        if r != 1:
            continue
        nm, a, ad, occ = setup(N, r)
        sig = [_iadd(_imm(ad[x], a[x]), _iscal(-1, _imm(a[x], ad[x]))) for x in range(N)]
        for x in range(N):
            for y in range(x + 1, N):
                cz = _imm(sig[x], sig[y])
                ok = ok and all(_is_zero(_comm(cz, Nz)) for Nz in occ)
                ok = ok and all(cz[b][c] == 0 for b in range(2 ** nm) for c in range(2 ** nm) if b != c)
                ok = ok and sorted({cz[b][b] for b in range(2 ** nm)}) == [-1, 1]
    _tp_rv = (ok); assert _tp_rv is not False, "check_cross_point_diagonal_products_are_not_hopping"; return _tp_rv
