"""synthesis.injection-freshness-is-pair-purity: exact checks.

Qubit models of one injection step: the window mode W and emitted quantum R of the k-th pair,
and X standing for everything already present.  Amplitudes are rational (c, s) = (3/5, 4/5),
so every density matrix is exact over Fractions; the zero-weight case uses the unnormalised
vector |01> + |10> with the factor 1/2 in the density matrix.

(a) purity of the pair forces freshness, for every rho on W, R, X = C^2: with P = |psi><psi|,
    psi = c|00> + s|11>, the linear identities (P (x) 1) E (P (x) 1) = P (x) <psi|E|psi>_X,
    tr_WR((P (x) 1) E (P (x) 1)) = <psi|E|psi>_X and tr((P (x) 1) E) = tr(P tr_X E) are checked on
    all 64 matrix units E, so for every operator. If rho_WR = P then tr((1 - P) (x) 1) rho) = 0, and
    for rho >= 0 (not computed: the positivity step) this gives rho = (P (x) 1) rho (P (x) 1) =
    P (x) rho_X. A sample with a mixed X confirms the marginals;
(b) counter-model: c|00>|00> + s|11>|11> on W, R and two earlier modes X is globally pure (U)
    and even (P), has the thermal marginals diag(c^2, s^2) on W and on R, and its pair state is
    mixed (tr rho_P^2 = c^4 + s^4 < 1) and correlated with X: freshness and the pair
    form both fail while (U), (C) and the marginals hold;
(c) Schmidt rigidity at c != s: a pure pair state with both marginals diag(c^2, s^2) has
    coefficient matrix diag(c e^{ia}, s e^{ib}): scanned over real amplitudes on a 17-value grid
    (four hits, diag(+-c, +-s)) and over complex amplitudes r w, r in {0, 9/25, 12/25, 3/5, 16/25,
    4/5} and w one of 12 rational unit phases (+-1, +-i, (+-3 +- 4i)/5, (+-4 +- 3i)/5): 144 hits,
    all diagonal; conversely each c|00> + w s|11> on the phase grid is pure with those marginals;
(d) zero weight: (|01> + |10>)/sqrt2 is pure with maximally mixed marginals and is not of
    the form c|00> + s|11>.
"""
from fractions import Fraction as Fr
from itertools import product
import GA
from GA import QI
from tp_premise import premise


def kron(a, b):
    return [[a[i][j] * b[k][l] for j in range(len(a)) for l in range(len(b))]
            for i in range(len(a)) for k in range(len(b))]


def outer(v):
    return [[x * y for y in v] for x in v]


mm = GA.mat_mul


def tr(a):
    return sum((a[i][i] for i in range(len(a))), Fr(0))


def ptrace(rho, dims, keep):
    """partial trace keeping the listed tensor factors (dims: list of factor dimensions)."""
    n = len(dims)
    def idx(bits):
        out = 0
        for b, d in zip(bits, dims):
            out = out * d + b
        return out
    kd = [dims[i] for i in keep]
    size = 1
    for d in kd:
        size *= d
    out = [[Fr(0)] * size for _ in range(size)]
    for bi in product(*[range(d) for d in dims]):
        for bj in product(*[range(d) for d in dims]):
            if any(bi[t] != bj[t] for t in range(n) if t not in keep):
                continue
            ri = 0
            rj = 0
            for t in keep:
                ri = ri * dims[t] + bi[t]
                rj = rj * dims[t] + bj[t]
            out[ri][rj] += rho[idx(bi)][idx(bj)]
    return out


def eq(a, b):
    return all(a[i][j] == b[i][j] for i in range(len(a)) for j in range(len(a)))


C, S = Fr(3, 5), Fr(4, 5)


def unit(n, a, b):
    m = [[Fr(0)] * n for _ in range(n)]
    m[a][b] = Fr(1)
    return m


def check_pure_pair_is_fresh():
    premise("singularity.modular-descent")
    psi = [C, Fr(0), Fr(0), S]                         # c|00> + s|11> on (W, R)
    rP = outer(psi)
    assert tr(rP) == 1 and tr(mm(rP, rP)) == 1          # pure
    PX = kron(rP, unit(2, 0, 0))
    PX = [[PX[i][j] + kron(rP, unit(2, 1, 1))[i][j] for j in range(8)] for i in range(8)]   # P (x) 1
    # the three linear identities, on all 64 matrix units of W (x) R (x) X: hence for every operator
    n_units = 0
    for a in range(8):
        for b in range(8):
            E = unit(8, a, b)
            sand = mm(mm(PX, E), PX)
            # <psi|E|psi>_X: the 2 x 2 matrix x, y -> sum psi_i psi_j E[(i, x)][(j, y)]
            ex = [[sum(psi[i] * psi[j] * E[2 * i + x][2 * j + y] for i in range(4) for j in range(4))
                   for y in range(2)] for x in range(2)]
            assert eq(sand, kron(rP, ex))
            assert eq(ptrace(sand, [2, 2, 2], [2]), ex)
            assert tr(mm(PX, E)) == tr(mm(rP, ptrace(E, [2, 2, 2], [0, 1])))
            n_units += 1
    assert n_units == 64
    # rho_WR = P gives tr((1 - P) (x) 1 rho) = 1 - tr(P P) = 0
    assert 1 - tr(mm(rP, rP)) == 0
    # a sample: any state of X
    rX = [[Fr(1, 3), Fr(1, 6)], [Fr(1, 6), Fr(2, 3)]]
    full = kron(rP, rX)
    assert eq(ptrace(full, [2, 2, 2], [0, 1]), rP) and eq(ptrace(full, [2, 2, 2], [2]), rX)
    assert eq(mm(mm(PX, full), PX), full)
    assert eq(ptrace(full, [2, 2, 2], [0]), [[C * C, Fr(0)], [Fr(0), S * S]])


def check_ghz_counter_model():
    premise("singularity.chains-state-class-stability")
    # c|00>|00> + s|11>|11> on (W, R) and X = two earlier modes: globally pure and even
    g = [Fr(0)] * 16
    g[0], g[15] = C, S
    full = outer(g)
    dims = [2, 2, 2, 2]
    assert tr(full) == 1 and tr(mm(full, full)) == 1    # (U): globally pure
    parity = [(-1) ** bin(i).count("1") for i in range(16)]
    assert all(full[i][j] == 0 for i in range(16) for j in range(16) if parity[i] != parity[j])  # (P)
    thermal = [[C * C, Fr(0)], [Fr(0), S * S]]
    assert eq(ptrace(full, dims, [0]), thermal) and eq(ptrace(full, dims, [1]), thermal)
    rP = ptrace(full, dims, [0, 1])
    assert tr(mm(rP, rP)) == C ** 4 + S ** 4 == Fr(337, 625)     # pair mixed: no thermofield vector
    rX = ptrace(full, dims, [2, 3])
    assert not eq(full, kron(rP, rX))                    # correlated with X: not fresh
    # the pair state is even and diagonal in the number basis, as the marginal data allow
    par2 = [1, -1, -1, 1]
    assert all(rP[i][j] == 0 for i in range(4) for j in range(4) if i != j)
    assert rP[0][0] == C * C and rP[3][3] == S * S and par2[0] == par2[3]


def check_schmidt_rigidity():
    premise("singularity.modular-descent")
    # pure pair states a00|00> + a01|01> + a10|10> + a11|11> with real rational amplitudes from a
    # grid; both marginals diag(c^2, s^2) occur only on the thermofield diagonal
    grid = sorted({Fr(k, 5) for k in range(-5, 6)} | {Fr(k, 25) for k in (-24, -12, -7, 7, 12, 24)})
    hits = []
    for a in product(grid, repeat=4):
        a00, a01, a10, a11 = a
        if a00 * a00 + a01 * a01 + a10 * a10 + a11 * a11 != 1:
            continue
        rw = [[a00 * a00 + a01 * a01, a00 * a10 + a01 * a11], [a00 * a10 + a01 * a11, a10 * a10 + a11 * a11]]
        rr = [[a00 * a00 + a10 * a10, a00 * a01 + a10 * a11], [a00 * a01 + a10 * a11, a01 * a01 + a11 * a11]]
        thermal = [[C * C, Fr(0)], [Fr(0), S * S]]
        if eq(rw, thermal) and eq(rr, thermal):
            hits.append(a)
    assert len(hits) == 4
    assert all(h[1] == 0 and h[2] == 0 and abs(h[0]) == C and abs(h[3]) == S for h in hits)
    # complex amplitudes r w on a Pythagorean-phase grid; rows of the coefficient matrix M (W index
    # first) with |row 0|^2 = c^2 and |row 1|^2 = s^2, then the rest of rho_W and rho_R
    phases = [QI(1), QI(-1), QI(0, 1), QI(0, -1)] + [QI(Fr(x, 5), Fr(y, 5)) for x, y in product(
        (3, -3, 4, -4), repeat=2) if abs(x) != abs(y)]
    assert len(phases) == 12 and all(w * w.conj() == QI(1) for w in phases)
    mags = [Fr(9, 25), Fr(12, 25), Fr(3, 5), Fr(16, 25), Fr(4, 5)]
    vals = [QI(0)] + [w * QI(r) for r in mags for w in phases]

    def n2(z):
        return (z * z.conj()).re
    tv = [(z, z.conj(), n2(z)) for z in vals]
    row0 = [(x, y) for x in tv for y in tv if x[2] + y[2] == C * C]
    row1 = [(x, y) for x in tv for y in tv if x[2] + y[2] == S * S]
    chits = []
    for (a00, c00, m00), (a01, c01, m01) in row0:
        for (a10, c10, m10), (a11, c11, m11) in row1:
            if m00 + m10 != C * C:                                      # rho_R diagonal
                continue
            if a00 * c10 + a01 * c11 != QI(0):                          # rho_W off-diagonal
                continue
            if a00 * c01 + a10 * c11 != QI(0):                          # rho_R off-diagonal
                continue
            chits.append((a00, a01, a10, a11))
    assert len(chits) == 144
    assert all(h[1] == QI(0) and h[2] == QI(0) and n2(h[0]) == C * C and n2(h[3]) == S * S for h in chits)
    # (TF) implies (Pure) with the marginals: c|00> + w s|11> on the phase grid
    for w in phases:
        v = [QI(C), QI(0), QI(0), w * QI(S)]
        rho = [[x * y.conj() for y in v] for x in v]
        assert sum((rho[i][i] for i in range(4)), QI(0)) == QI(1)
        assert sum((rho[i][j] * rho[j][i] for i in range(4) for j in range(4)), QI(0)) == QI(1)
        assert rho[0][0] == QI(C * C) and rho[3][3] == QI(S * S) and rho[1][1] == QI(0) == rho[2][2]


def check_zero_weight_form_not_forced():
    premise("singularity.modular-descent")
    v = [Fr(0), Fr(1), Fr(1), Fr(0)]                   # |01> + |10>, norm^2 = 2
    rP = [[x * y / 2 for y in v] for x in v]
    assert tr(rP) == 1 and tr(mm(rP, rP)) == 1
    half = [[Fr(1, 2), Fr(0)], [Fr(0), Fr(1, 2)]]
    assert eq(ptrace(rP, [2, 2], [0]), half) and eq(ptrace(rP, [2, 2], [1]), half)
    assert rP[0][0] == 0 and rP[3][3] == 0              # no |00>, |11> component
    assert GA.rank_of_vectors([[Fr(x) for x in v], [Fr(1), Fr(0), Fr(0), Fr(1)]]) == 2
