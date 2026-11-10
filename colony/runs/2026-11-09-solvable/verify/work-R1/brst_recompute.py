"""R1 recomputations for the two Higgs-sector BRST proposals (exact arithmetic, GA)."""
import sys
import itertools
import random
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, sc, reverse

E3 = (1, 1, 1)
EVEN = [(), (1, 2), (0, 2), (0, 1)]   # basis 1, e12, e02, e01 (0-based labels e0, e1, e2)


def ev(cs):
    return {b: F(c) for b, c in zip(EVEN, cs) if c != 0}


def coords(x):
    return [x.get(b, F(0)) for b in EVEN]


def inner(a, b):
    return mul(reverse(a), b, E3).get((), F(0))


T = [scal(F(1, 2), {(1, 2): F(1)}), scal(F(1, 2), {(0, 2): F(-1)}), scal(F(1, 2), {(0, 1): F(1)})]  # 1/2 e12, 1/2 e20, 1/2 e01
E12 = {(1, 2): F(1)}


def rho(a, phi, y):
    if a < 3:
        return mul(T[a], phi, E3)
    return scal(y, mul(phi, E12, E3))


def goldstone_vectors(Phi, y):
    return [[rho(a, p, y) for p in Phi] for a in range(4)]


def rank(rows):
    M = [list(r) for r in rows]
    rk = 0
    ncol = len(M[0]) if M else 0
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / M[rk][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk


def flat(Wa):
    return [c for x in Wa for c in coords(x)]


def part_rank_census():
    counts = {}
    agree = True
    for vals in itertools.product((-1, 0, 1), repeat=8):
        Phi = [ev(vals[:4]), ev(vals[4:])]
        r = rank([flat(Wa) for Wa in goldstone_vectors(Phi, F(1, 2))])
        counts[r] = counts.get(r, 0) + 1
        psi = mul(reverse(Phi[0]), Phi[1], E3)
        Kp = psi.get((0, 2), F(0)) ** 2 + psi.get((0, 1), F(0)) ** 2
        nz = any(vals)
        pred = 0 if not nz else (3 if Kp == 0 else 4)
        agree = agree and pred == r
    return counts, agree


def charpoly_eigs_2x2_and_spectrum(v1, v2, y, k12):
    Phi = [ev((v1, 0, 0, 0)), ev((v2, 0, 0, 0))]
    W = goldstone_vectors(Phi, y)
    Gam = [[sum(inner(W[a][k], W[b][k]) for k in range(2)) for b in range(4)] for a in range(4)]
    kap = [F(1, 4), F(1, 4), F(1, 4), k12]
    M = [[Gam[a][b] / kap[a] for b in range(4)] for a in range(4)]
    return Gam, M


def eig_check(M, cands):
    """Return the multiset of candidate eigenvalues found via rank deficiency of M - t."""
    out = {}
    n = len(M)
    for t in cands:
        r = rank([[M[i][j] - (t if i == j else 0) for j in range(n)] for i in range(n)])
        out[t] = n - r
    return out


def part_masses():
    Gam, M = charpoly_eigs_2x2_and_spectrum(1, 2, F(1, 2), F(3, 4))
    return eig_check(M, [F(0), F(5), F(20, 3)])


def part_FF_normalisation():
    """<F^2>_0 = -(1/2) F_{mu nu} F^{mu nu} in signature (+,-,-,-): the stored density kappa <F F>_0 is twice the
    canonical -(1/4) kappa F_{mu nu} F^{mu nu}."""
    S = (1, -1, -1, -1)
    g = [1, -1, -1, -1]
    random.seed(7)
    for _ in range(5):
        Fc = {}
        for i in range(4):
            for j in range(i + 1, 4):
                Fc[(i, j)] = F(random.randint(-5, 5))
        Fb = {k: v for k, v in Fc.items() if v != 0}
        lhs = mul(Fb, Fb, S).get((), F(0))
        # tensor: F = sum_{i<j} F_ij e_i e_j with lower-index frame vectors; F^{ij} = g^ii g^jj F_ij
        ff = 2 * sum(v * v * g[i] * g[j] for (i, j), v in Fc.items())
        assert lhs == -F(1, 2) * ff, (lhs, ff)
    return True


def N(p):
    return inner(p, p)


def part_quartics():
    random.seed(3)
    ok = True
    for _ in range(40):
        Phi = [ev([F(random.randint(-6, 6), random.randint(1, 4)) for _ in range(4)]) for _ in range(2)]
        n1, n2 = N(Phi[0]), N(Phi[1])
        psi = mul(reverse(Phi[0]), Phi[1], E3)
        K = psi.get((), F(0)) ** 2 + psi.get((1, 2), F(0)) ** 2
        Kp = psi.get((0, 2), F(0)) ** 2 + psi.get((0, 1), F(0)) ** 2
        S, D = n1 + n2, n1 - n2
        ok = ok and (K + Kp == n1 * n2)
        Vm = (S - F(3, 2)) ** 2 + D ** 2 - K
        ok = ok and Vm == F(3, 4) * (S - 2) ** 2 + F(5, 4) * D ** 2 - F(3, 4) + Kp
        Vp = (S - 2) ** 2 + D ** 2 + K
        ok = ok and Vp >= 0
    return ok


if __name__ == "__main__":
    print("FF normalisation <F^2>_0 = -(1/2) F_mn F^mn:", part_FF_normalisation())
    print("kappa^{-1} Gamma at v=(1,2), y=1/2, kappa_Y=3/4: eigen-multiplicities", part_masses())
    print("quartic decompositions and K + K' = N1 N2 at 40 random rational pairs:", part_quartics())
    counts, agree = part_rank_census()
    print("Goldstone rank census on {-1,0,1}^8:", dict(sorted(counts.items())), "matches K' rule:", agree)
