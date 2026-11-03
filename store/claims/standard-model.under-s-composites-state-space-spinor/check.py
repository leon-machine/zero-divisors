"""standard-model.under-s-composites-state-space-spinor: exact checks.

Components (j, k) of Lambda^*(C^2 + C^3): Lambda^j C^2 (x) Lambda^k C^3, SU(2) content 1, 2, 1 (j = 0, 1, 2), SU(3)
content 1, 3, 3bar, 1 (k = 0..3), dimension C(2,j) C(3,k); the hypercharge generator y = (3i I_2, -2i I_3) acts by
the sum of its eigenvalues over occupied modes (q = 3j - 2k, Y = q/6), computed from the generator.
(1) The even part has dimension 16 and its (SU(2), SU(3), Y) multiset is the derived generation Q, L, u^c, d^c,
    e^c, nu^c at (1,1), (1,3), (0,2), (2,2), (2,0), (0,0); the odd part's is the conjugate multiset, with
    (2,1)_{1/2} at (1,0); (2,0) carries (1,1)_1, the mass bracket's slot factor; the Hodge map (j,k) -> (2-j, 3-k)
    negates every weight.
(2) Five-mode Fock space by Jordan-Wigner (32 states, Gaussian-rational sparse matrices): gamma_{2i} = a_i + a_i^dag,
    gamma_{2i+1} = i(a_i - a_i^dag) satisfy the Cl(10) relations, the vacuum is the unique common kernel of the a_i,
    and 32 = 2^5 is the dimension of the simple module of Cl(10, C) = M_32(C); the parity (-1)^(j+k) anticommutes
    with every gamma and splits 16 + 16. Of the 45 bivectors' complex span, the part commuting with the mode
    number has dimension 25 (u(5)), and the part commuting also with the slot number 13 (u(2) + u(3)). The
    Spin(10) generator for n_i is n_i - 1/2 (in the bivector span), while n_i itself is not: the det^(-1/2) phase.
(3) (a) For alpha j + beta k on the derived generation the three linear sums are 2(2a+3b), 2(2a+3b), 8(2a+3b) on
    the integer grid [-6, 6]^2, vanishing exactly on the multiples of (3, -2); (1,1) gives (10, 10, 40, 400),
    (1,-1) gives (-2, -2, -8, -32), and the cubic sum vanishes at (3, -2). (b) With the Spin(10) shift
    alpha j + beta k - (2 alpha + 3 beta)/2 all four sums and the mixed sums Y^2 X, Y X^2 vanish on a 4 x 4 grid,
    hence identically (cubic forms). X = j + k - 5/2 = 2Y - (5/2)(B - L), B - L = 1 - 2k/3, takes -5/2, -1/2,
    3/2 as stated; the Majorana bilinear nu^c nu^c has X = -5, B - L = 2.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from pyutil import get_or_set
from tp_premise import premise

QI = GA.QI
XY = [QI(0, 3), QI(0, 3)]
YY = [QI(0, -2), QI(0, -2), QI(0, -2)]
SU2 = {0: "1", 1: "2", 2: "1"}
SU3 = {0: "1", 1: "3", 2: "3b", 3: "1"}
CONJ3 = {"1": "1", "3": "3b", "3b": "3"}
DIM = {"1": 1, "2": 2, "3": 3, "3b": 3}
GEN_AT = {"nuc": (0, 0), "uc": (0, 2), "Q": (1, 1), "L": (1, 3), "ec": (2, 0), "dc": (2, 2)}
GRID = [F(-3), F(1, 2), F(2), F(7, 3)]


def _comb(n, k):
    return len(list(combinations(range(n), k)))


def _q(j, k):
    return (sum((XY[i] for i in range(j)), QI(0)) + sum((YY[i] for i in range(k)), QI(0))).im


def _content(j, k):
    return (SU2[j], SU3[k], F(_q(j, k), 6))


def _sums(charge, comps):
    """[SU(3)]^2, [SU(2)]^2, gravitational, cubic sums of a charge over components (j, k)."""
    su3 = su2 = grav = cub = F(0)
    for (j, k) in comps:
        d2, d3 = DIM[SU2[j]], DIM[SU3[k]]
        c = charge(j, k)
        if d3 == 3:
            su3 += d2 * c
        if d2 == 2:
            su2 += d3 * c
        grav += d2 * d3 * c
        cub += d2 * d3 * c ** 3
    return (su3, su2, grav, cub)


# ---- Fock space: sparse matrices {(row, col): QI} on 32 states -----------------------------------------
NM, N32 = 5, 32


def _annih(i):
    M = {}
    for b in range(N32):
        if b >> i & 1:
            sign = -1 if bin(b & ((1 << i) - 1)).count("1") % 2 else 1
            M[(b ^ (1 << i), b)] = QI(sign)
    return M


def _dag(M):
    return {(c, r): z.conj() for (r, c), z in M.items()}


def _mul(A, B):
    byrow = {}
    for (r, c), z in B.items():
        get_or_set(byrow, r, []).append((c, z))
    out = {}
    for (r, c), z in A.items():
        for (d, w) in byrow.get(c, []):
            out[(r, d)] = out.get((r, d), QI(0)) + z * w
    return {k: v for k, v in out.items() if v}


def _add(A, B, s=1):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, QI(0)) + (v if s == 1 else QI(0) - v)
    return {k: v for k, v in out.items() if v}


def _scal(c, A):
    return {k: c * v for k, v in A.items() if c * v}


def _ident():
    return {(b, b): QI(1) for b in range(N32)}


def _flat(M):
    row = [QI(0)] * (N32 * N32)
    for (r, c), z in M.items():
        row[r * N32 + c] = z
    return row


def check_even_part_is_the_generation():
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    premise("standard-model.chirality-two-halves-spinor-module-conjugation")
    premise("standard-model.mass-bracket-charged-singlet")
    premise("standard-model.hyp-s-slot-statistics")
    even, odd, dim_even = [], [], 0
    for j in range(3):
        for k in range(4):
            (even if (j + k) % 2 == 0 else odd).append(_content(j, k))
            dim_even += _comb(2, j) * _comb(3, k) if (j + k) % 2 == 0 else 0
    derived = [("2", "3", F(1, 6)), ("2", "1", F(-1, 2)), ("1", "3b", F(-2, 3)), ("1", "3b", F(1, 3)),
               ("1", "1", F(1)), ("1", "1", F(0))]
    ok = dim_even == 16 and sorted(even) == sorted(derived)
    ok = ok and sorted(odd) == sorted((a, CONJ3[b], -c) for (a, b, c) in derived)
    ok = ok and {n: _content(*jk) for n, jk in GEN_AT.items()} == {
        "nuc": ("1", "1", F(0)), "uc": ("1", "3b", F(-2, 3)), "Q": ("2", "3", F(1, 6)),
        "L": ("2", "1", F(-1, 2)), "ec": ("1", "1", F(1)), "dc": ("1", "3b", F(1, 3))}
    ok = ok and _content(1, 0) == ("2", "1", F(1, 2)) and _content(2, 0) == ("1", "1", F(1))
    ok = ok and all(_q(2 - j, 3 - k) == -_q(j, k) for j in range(3) for k in range(4))
    GA.check("even part of Lambda(C^2 + C^3) = the derived generation (16), odd part = its conjugate", ok)
    return ok


def check_fock_space_is_the_cl10_spinor():
    premise("standard-model.imported-fock-representation-clifford-algebra-bogoliubov")
    a = [_annih(i) for i in range(NM)]
    ad = [_dag(x) for x in a]
    gam = []
    for i in range(NM):
        gam.append(_add(a[i], ad[i]))
        gam.append(_scal(QI(0, 1), _add(a[i], ad[i], -1)))
    I = _ident()
    ok = all(_add(_mul(gam[p], gam[q]), _mul(gam[q], gam[p])) == (_scal(QI(2), I) if p == q else {})
             for p in range(10) for q in range(10))
    # unique vacuum: common kernel of the a_i is spanned by the basis state 0
    killed = [b for b in range(N32) if all(not any(c == b for (r, c) in a[i]) for i in range(NM))]
    ok = ok and killed == [0] and N32 == 2 ** (10 // 2)
    G = I
    for i in range(NM):
        G = _mul(G, _add(I, _scal(QI(2), _mul(ad[i], a[i])), -1))
    ok = ok and all(G[(b, b)] == QI((-1) ** bin(b).count("1")) for b in range(N32)) and len(G) == N32
    ok = ok and all(_add(_mul(g, G), _mul(G, g)) == {} for g in gam)
    ok = ok and sum(1 for b in range(N32) if bin(b).count("1") % 2 == 0) == 16
    GA.check("Jordan-Wigner gammas satisfy Cl(10) on 32 states; unique vacuum; parity splits 16 + 16", ok)
    return ok


def check_number_and_split_preserving_bivectors():
    premise("standard-model.imported-fock-representation-clifford-algebra-bogoliubov")
    a = [_annih(i) for i in range(NM)]
    ad = [_dag(x) for x in a]
    gam = []
    for i in range(NM):
        gam.append(_add(a[i], ad[i]))
        gam.append(_scal(QI(0, 1), _add(a[i], ad[i], -1)))
    biv = [_mul(gam[p], gam[q]) for p in range(10) for q in range(p + 1, 10)]
    n = [_mul(ad[i], a[i]) for i in range(NM)]
    Ntot, Nslot = {}, {}
    for i in range(NM):
        Ntot = _add(Ntot, n[i])
        if i < 2:
            Nslot = _add(Nslot, n[i])

    def commuting_dim(ops):
        cols = []
        for B in biv:
            col = []
            for O in ops:
                col.extend(_flat(_add(_mul(B, O), _mul(O, B), -1)))
            cols.append(col)
        rows = [[cols[c][r] for c in range(len(biv))] for r in range(len(cols[0]))]
        rows = list({tuple((z.re, z.im) for z in r): r for r in rows if any(r)}.values())
        return len(GA.field_kernel(rows))
    d_num = commuting_dim([Ntot])
    d_split = commuting_dim([Ntot, Nslot])
    # coordinates restricted to the union of supports (the other entries vanish for every operator used)
    shifted = _add(n[0], _scal(QI(F(-1, 2)), _ident()))
    keys = sorted(set(k for B in biv + [shifted, n[0]] for k in B))
    vec = lambda M: [M.get(k, QI(0)) for k in keys]
    span = [vec(B) for B in biv]
    r0 = GA.field_rank(span)
    in_span = GA.field_rank(span + [vec(shifted)]) == r0
    raw_in = GA.field_rank(span + [vec(n[0])]) == r0
    ok = len(biv) == 45 and r0 == 45 and d_num == 25 and d_split == 13 and in_span and not raw_in
    GA.check("bivectors commuting with N: 25 (u(5)); also with the slot number: 13; n_i - 1/2 in Spin(10), n_i not", ok)
    return ok


def check_abelian_generators_anomalies():
    premise("standard-model.imported-anomaly-coefficients")
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    comps = list(GEN_AT.values())
    ok = True
    sols = []
    for al in range(-6, 7):
        for be in range(-6, 7):
            s = _sums(lambda j, k: al * j + be * k, comps)
            c = 2 * al + 3 * be
            ok = ok and s[:3] == (2 * c, 2 * c, 8 * c)
            if (al, be) != (0, 0) and s[:3] == (0, 0, 0):
                sols.append((al, be))
    ok = ok and sols == [(-6, 4), (-3, 2), (3, -2), (6, -4)]
    ok = ok and _sums(lambda j, k: 3 * j - 2 * k, comps) == (0, 0, 0, 0)
    ok = ok and _sums(lambda j, k: j + k, comps) == (10, 10, 40, 400)
    ok = ok and _sums(lambda j, k: j - k, comps) == (-2, -2, -8, -32)
    GA.check("untwisted action: linear sums 2(2a+3b), 2(2a+3b), 8(2a+3b), zero only along hypercharge", ok)
    return ok


def check_spin10_action_anomaly_free():
    premise("standard-model.imported-fock-representation-clifford-algebra-bogoliubov")
    premise("standard-model.imported-anomaly-coefficients")
    comps = list(GEN_AT.values())
    Yof = lambda j, k: F(_q(j, k), 6)
    ok = True
    for al in GRID:
        for be in GRID:
            ch = lambda j, k: al * j + be * k - (2 * al + 3 * be) / 2
            ok = ok and _sums(ch, comps) == (0, 0, 0, 0)
            mixed1 = sum((DIM[SU2[j]] * DIM[SU3[k]] * Yof(j, k) ** 2 * ch(j, k) for j, k in comps), F(0))
            mixed2 = sum((DIM[SU2[j]] * DIM[SU3[k]] * Yof(j, k) * ch(j, k) ** 2 for j, k in comps), F(0))
            ok = ok and mixed1 == 0 and mixed2 == 0
    X = lambda j, k: j + k - F(5, 2)
    BL = lambda j, k: 1 - F(2, 3) * k
    ok = ok and all(X(j, k) == 2 * Yof(j, k) - F(5, 2) * BL(j, k) for j, k in comps)
    vals = {n: X(*jk) for n, jk in GEN_AT.items()}
    ok = ok and vals == {"nuc": F(-5, 2), "Q": F(-1, 2), "uc": F(-1, 2), "ec": F(-1, 2), "L": F(3, 2), "dc": F(3, 2)}
    ok = ok and 2 * X(0, 0) == -5 and 2 * BL(0, 0) == 2
    GA.check("Spin(10) action: all sums and mixed sums vanish identically; X = 2Y - 5/2 (B - L)", ok)
    return ok
