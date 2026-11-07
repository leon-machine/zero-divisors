"""synthesis.kasner-curvature-wall-is-negative-weight-helicity: exact checks (Fractions and GA).

(a) The scalar curvature of the slice metric h = sum_l a_l^2 (theta^l)^2 two ways: the coordinate Ricci
    scalar from the jets of h at a point, and the orthonormal-frame formula
    4 e_i(acc_i) - 6 acc.acc - (1/2)(2 n:n - (tr n)^2) from the structure functions; three generic coframes,
    three weight triples each. The helicities h_k (theta^k ^ d theta^k = h_k theta^1 ^ theta^2 ^ theta^3) are
    computed as GA wedges and equal -c_ij^k for (i j k) cyclic, the diagonal of n; their values are pinned.
(b) Support identity: R(a) = -(1/2) sum_k h_k^2 a_k^2/(a_i a_j)^2 + sum_m Q_m / a_m^2 with Q_m independent of
    the a's: Q fitted at three weight triples and confirmed at two more, for each coframe; dropping the
    helicity term breaks it (control).
(c) Exponent bookkeeping: with a_l = tau^(p_l), sum p = 1, tau^2 R is a sum of tau^(4 p_k) and tau^(2 - 2 p_m);
    on the open Kasner arc exactly one exponent (4 p_1) is negative, the rest exceed delta = min(4 p_2, 2 - 2 p_3)
    > 0 (pinned at sample u); at the Taub point (1, 0, 0) zero exponents occur (control); on the circle the
    residue part (tr P)^2 - tr P^2 of the Hamiltonian constraint vanishes, off it not.
(d) Bianchi II: the coordinate Ricci tensor of N^2 dT^2 - a1^2 (dx - z dy)^2 - a2^2 dy^2 - a3^2 dz^2,
    N = a1 a2 a3, vanishes at jets obeying the stated equations and not at perturbed jets.
(e) The Liouville solution, the constraint BC = v^2, the limiting epochs and the BKL transition law (and u -> u - 1),
    with the negative weight of the earlier epoch on a helicity-free axis.
(f) The GTG route (lib/gtg.py): the slice gauge field in Cl(0,3) and the Bianchi II gauge field on exact jets,
    Omega solved from the torsion equation; the slice scalar equals the frame formula, the Bianchi II Omega equals
    its closed form, and the Bianchi II Ricci map gives the stated equations.
(g) The frame formula derived from the torsion equation: for a general orthonormal frame of Cl(0,3) the store-sign
    scalar of the torsion-solved field strength equals the Ellis-MacCallum formula as an exact polynomial identity
    in the structure functions and their frame derivatives.
"""
from fractions import Fraction as F
import GA
from GA import field_solve, mul, gen, add, scal
from tp_premise import premise
import gtg

N3 = 3


def inv(M):
    n = len(M)
    cols = [field_solve(M, [F(int(i == j)) for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def eps(i, j, k):
    return F((i - j) * (j - k) * (k - i), 2)


def ricci(g, dg, ddg):
    n = len(g)
    gi = inv(g)
    dgi = [[[-sum(gi[a][e] * dg[c][e][f] * gi[f][b] for e in range(n) for f in range(n))
             for b in range(n)] for a in range(n)] for c in range(n)]
    G1 = [[[(dg[a][l][b] + dg[b][l][a] - dg[l][a][b]) / 2 for b in range(n)] for a in range(n)] for l in range(n)]
    dG1 = [[[[(ddg[c][a][l][b] + ddg[c][b][l][a] - ddg[c][l][a][b]) / 2 for b in range(n)]
             for a in range(n)] for l in range(n)] for c in range(n)]
    Gam = [[[sum(gi[k][l] * G1[l][a][b] for l in range(n)) for b in range(n)] for a in range(n)] for k in range(n)]
    dGam = [[[[sum(dgi[c][k][l] * G1[l][a][b] + gi[k][l] * dG1[c][l][a][b] for l in range(n))
               for b in range(n)] for a in range(n)] for k in range(n)] for c in range(n)]
    Ric = [[sum(dGam[k][k][a][b] - dGam[b][k][a][k] for k in range(n))
            + sum(Gam[k][k][l] * Gam[l][a][b] - Gam[k][b][l] * Gam[l][a][k] for k in range(n) for l in range(n))
            for b in range(n)] for a in range(n)]
    return gi, Ric


# ---------------------------------------------------------------- slices: coframe theta^l = A^l_i(x) dx^i
def coframe(seed):
    """Deterministic generic rational coframe jets at x = 0 (value, first and second derivatives)."""
    s = seed

    def nxt():
        nonlocal s
        s = (s * 1103515245 + 12345) % 2147483648
        return F(s % 11 - 5, 1 + s % 3)
    A0 = [[nxt() for _ in range(N3)] for _ in range(N3)]
    for i in range(N3):
        A0[i][i] += 6
    A1 = [[[nxt() for _ in range(N3)] for _ in range(N3)] for _ in range(N3)]
    A2 = [[[[F(0)] * N3 for _ in range(N3)] for _ in range(N3)] for _ in range(N3)]
    for k in range(N3):
        for m in range(k, N3):
            blk = [[nxt() for _ in range(N3)] for _ in range(N3)]
            A2[k][m] = blk
            A2[m][k] = blk
    return A0, A1, A2


def scalar_coord(a, A0, A1, A2):
    h = [[sum(a[l] ** 2 * A0[l][i] * A0[l][j] for l in range(N3)) for j in range(N3)] for i in range(N3)]
    dh = [[[sum(a[l] ** 2 * (A1[k][l][i] * A0[l][j] + A0[l][i] * A1[k][l][j]) for l in range(N3))
            for j in range(N3)] for i in range(N3)] for k in range(N3)]
    ddh = [[[[sum(a[l] ** 2 * (A2[k][m][l][i] * A0[l][j] + A0[l][i] * A2[k][m][l][j]
                              + A1[k][l][i] * A1[m][l][j] + A1[m][l][i] * A1[k][l][j]) for l in range(N3))
              for j in range(N3)] for i in range(N3)] for m in range(N3)] for k in range(N3)]
    gi, Ric = ricci(h, dh, ddh)
    return sum(gi[i][j] * Ric[i][j] for i in range(N3) for j in range(N3))


def structure(A0, A1, A2):
    """[E_m, E_n] = c[m][n][l] E_l at x = 0 and the coordinate derivatives dc[k][m][n][l]."""
    E0 = inv(A0)
    dE = [[[-sum(E0[i][p] * A1[k][p][q] * E0[q][m] for p in range(N3) for q in range(N3))
            for m in range(N3)] for i in range(N3)] for k in range(N3)]
    c = [[[-sum((A1[j][l][i] - A1[i][l][j]) * E0[j][m] * E0[i][n] for i in range(N3) for j in range(N3))
           for l in range(N3)] for n in range(N3)] for m in range(N3)]
    dc = [[[[-sum((A2[k][j][l][i] - A2[k][i][l][j]) * E0[j][m] * E0[i][n]
                  + (A1[j][l][i] - A1[i][l][j]) * (dE[k][j][m] * E0[i][n] + E0[j][m] * dE[k][i][n])
                  for i in range(N3) for j in range(N3))
             for l in range(N3)] for n in range(N3)] for m in range(N3)] for k in range(N3)]
    return E0, c, dc


def scalar_frame(a, A0, A1, A2):
    E0, c, dc = structure(A0, A1, A2)
    ch = [[[a[l] * c[m][n][l] / (a[m] * a[n]) for l in range(N3)] for n in range(N3)] for m in range(N3)]
    acc = [sum(ch[i][j][j] for j in range(N3)) / 2 for i in range(N3)]
    dacc = [[sum(dc[x][i][j][j] / a[i] for j in range(N3)) / 2 for x in range(N3)] for i in range(N3)]
    div = sum(sum(E0[x][i] * dacc[i][x] for x in range(N3)) / a[i] for i in range(N3))
    nn = [[sum(eps(l, i, j) * ch[i][j][k] for i in range(N3) for j in range(N3)) / 2
           - sum(eps(l, i, k) * acc[i] for i in range(N3)) for k in range(N3)] for l in range(N3)]
    sym = all(nn[l][k] == nn[k][l] for l in range(N3) for k in range(N3))
    nsq = sum(nn[i][j] ** 2 for i in range(N3) for j in range(N3))
    tr = sum(nn[i][i] for i in range(N3))
    return 4 * div - 6 * sum(x * x for x in acc) - (2 * nsq - tr * tr) / 2, nn, c, sym


E3 = [F(1)] * 3


def vec(cs):
    return add(*[scal(cs[i], gen(i)) for i in range(N3)])


def helicities_ga(A0, A1):
    """theta^k ^ d theta^k over theta^1 ^ theta^2 ^ theta^3, as GA wedges in Cl(3,0)."""
    vol = mul(mul(vec(A0[0]), vec(A0[1]), E3), vec(A0[2]), E3).get((0, 1, 2), F(0))
    out = []
    for k in range(N3):
        dth = add(*[scal((A1[j][k][m] - A1[m][k][j]) / 2, mul(gen(j), gen(m), E3))
                    for j in range(N3) for m in range(N3) if j != m])
        out.append(mul(vec(A0[k]), dth, E3).get((0, 1, 2), F(0)) / vol)
    return out


SEEDS = (3, 17, 29)
WEIGHTS = ([F(1), F(1), F(1)], [F(2), F(1, 3), F(5, 2)], [F(1, 7), F(3), F(4, 5)],
           [F(3, 2), F(2, 9), F(7)], [F(5), F(6), F(1, 4)])
PIN_H = {3: [F(-9, 37), F(31, 185), F(19, 185)], 17: [F(5, 43), F(29, 172), F(-187, 1376)],
         29: [F(17, 106), F(9, 742), F(-11, 212)]}
PIN_R = {3: F(-136235043529, 6791951250), 17: F(-715114665428189, 21542453452800),
         29: F(54398801461, 91916659800)}
CYC = [(1, 2, 0), (2, 0, 1), (0, 1, 2)]


def check_frame_formula_and_helicities():
    ok = True
    for seed in SEEDS:
        A0, A1, A2 = coframe(seed)
        hel = helicities_ga(A0, A1)
        E0, c, _ = structure(A0, A1, A2)
        ok &= hel == PIN_H[seed]
        ok &= all(hel[k] == -c[i][j][k] for (i, j, k) in CYC)
        for a in WEIGHTS[:3]:
            Rc = scalar_coord(a, A0, A1, A2)
            Rf, nn, _, sym = scalar_frame(a, A0, A1, A2)
            ok &= sym and Rc == Rf
            ok &= all(nn[k][k] * a[i] * a[j] == -hel[k] * a[k] for (i, j, k) in CYC)
        ok &= scalar_coord(WEIGHTS[2], A0, A1, A2) == PIN_R[seed]
    GA.check("frame formula = coordinate scalar curvature; helicities = -c_ij^k (pinned)", ok)
    return ok


def check_support_identity():
    ok = True
    for seed in SEEDS:
        A0, A1, A2 = coframe(seed)
        hel = helicities_ga(A0, A1)

        def resid(a, drop=False):
            R = scalar_coord(a, A0, A1, A2)
            diag = -sum(hel[k] ** 2 * a[k] ** 2 / (a[(k + 1) % 3] * a[(k + 2) % 3]) ** 2 for k in range(3)) / 2
            return R if drop else R - diag
        M = [[1 / a[m] ** 2 for m in range(3)] for a in WEIGHTS[:3]]
        Q = field_solve(M, [resid(a) for a in WEIGHTS[:3]])
        ok &= all(resid(a) == sum(Q[m] / a[m] ** 2 for m in range(3)) for a in WEIGHTS[3:])
        Qd = field_solve(M, [resid(a, True) for a in WEIGHTS[:3]])
        ok &= not all(resid(a, True) == sum(Qd[m] / a[m] ** 2 for m in range(3)) for a in WEIGHTS[3:])
    GA.check("tau^2 R3 = -(1/2) sum h_k^2 tau^(4p_k) + sum Q_m tau^(2-2p_m), Q weight-free (control fails)", ok)
    return ok


def kasner(u):
    d = 1 + u + u * u
    return [-u / d, (1 + u) / d, u * (1 + u) / d]


def check_exponents_on_open_arc():
    premise("synthesis.nondiagonal-kasner-residue-weighted-shear")
    premise("synthesis.unit-boost-residue-needs-nonpositive-exponent")
    ok = True
    pins = {F(1): F(2, 3), F(3, 2): F(8, 19), F(2): F(2, 7), F(7, 2): F(8, 67)}
    for u, dpin in pins.items():
        p = kasner(u)
        ok &= sum(p) == 1 and sum(x * x for x in p) == 1
        exps = [4 * x for x in p] + [2 - 2 * x for x in p]
        neg = [e for e in exps if e <= 0]
        ok &= neg == [4 * p[0]] and p[0] < 0
        delta = min(e for e in exps if e > 0)
        ok &= delta == min(4 * p[1], 2 - 2 * p[2]) == dpin
        # residue part of the Hamiltonian constraint at order tau^-2: (tr P)^2 - tr P^2
        ok &= sum(p) ** 2 - sum(x * x for x in p) == 0
    # part of the scalar disk where every p is in (0, 1): every exponent positive (condition vacuous);
    # the disk point (-1/6, 5/6, 1/3) has a negative weight (the restriction is needed)
    for disk in ([F(1, 3), F(1, 3), F(1, 3)], [F(1, 5), F(3, 10), F(1, 2)]):
        dex = [4 * x for x in disk] + [2 - 2 * x for x in disk]
        ok &= sum(disk) == 1 and sum(x * x for x in disk) < 1 and min(dex) > 0
    ok &= min([4 * x for x in [F(1, 5), F(3, 10), F(1, 2)]] + [2 - 2 * x for x in [F(1, 5), F(3, 10), F(1, 2)]]) == F(4, 5)
    neg_disk = [F(-1, 6), F(5, 6), F(1, 3)]
    ok &= sum(neg_disk) == 1 and sum(x * x for x in neg_disk) == F(5, 6) and 4 * neg_disk[0] < 0
    taub = [F(1), F(0), F(0)]
    ok &= any(e == 0 for e in [4 * x for x in taub] + [2 - 2 * x for x in taub])
    off = [F(-1, 5), F(2, 5), F(4, 5)]
    ok &= sum(off) == 1 and sum(off) ** 2 - sum(x * x for x in off) != 0
    GA.check("open arc: only 4 p_1 < 0; delta pinned; Taub point degenerate; residue part zero on the circle", ok)
    return ok


class J:
    """Second-order jet in (T, z): value, d_T, d_z, d_TT, d_Tz, d_zz."""
    def __init__(self, v, t=0, z=0, tt=0, tz=0, zz=0):
        self.c = [F(v), F(t), F(z), F(tt), F(tz), F(zz)]

    def __add__(self, o):
        o = o if isinstance(o, J) else J(o)
        r = J(0)
        r.c = [x + y for x, y in zip(self.c, o.c)]
        return r

    def __neg__(self):
        r = J(0)
        r.c = [-x for x in self.c]
        return r

    def __sub__(self, o):
        return self + (-(o if isinstance(o, J) else J(o)))

    def __mul__(self, o):
        o = o if isinstance(o, J) else J(o)
        a, b = self.c, o.c
        r = J(0)
        r.c = [a[0] * b[0], a[1] * b[0] + a[0] * b[1], a[2] * b[0] + a[0] * b[2],
               a[3] * b[0] + 2 * a[1] * b[1] + a[0] * b[3],
               a[4] * b[0] + a[1] * b[2] + a[2] * b[1] + a[0] * b[4],
               a[5] * b[0] + 2 * a[2] * b[2] + a[0] * b[5]]
        return r


def bianchi2_ricci(a, da, dda):
    """a_i(T) with a_i' = a_i alpha_i', a_i'' = a_i (alpha_i'' + alpha_i'^2); Ricci at z = 0."""
    a1, a2, a3 = [J(a[i], a[i] * da[i], 0, a[i] * (dda[i] + da[i] * da[i])) for i in range(3)]
    z = J(0, 0, 1)
    Nj = a1 * a2 * a3
    gj = [[J(0) for _ in range(4)] for _ in range(4)]
    gj[0][0] = Nj * Nj
    gj[1][1] = -(a1 * a1)
    gj[1][2] = gj[2][1] = a1 * a1 * z
    gj[2][2] = -(a2 * a2) - a1 * a1 * z * z
    gj[3][3] = -(a3 * a3)
    first = {0: 1, 3: 2}
    second = {(0, 0): 3, (0, 3): 4, (3, 0): 4, (3, 3): 5}
    g = [[gj[i][j].c[0] for j in range(4)] for i in range(4)]
    dg = [[[gj[i][j].c[first[c]] if c in first else F(0) for j in range(4)] for i in range(4)] for c in range(4)]
    ddg = [[[[gj[i][j].c[second[(c, d)]] if (c, d) in second else F(0) for j in range(4)] for i in range(4)]
            for d in range(4)] for c in range(4)]
    return ricci(g, dg, ddg)[1]


def check_bianchi_ii_vacuum_equations():
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    gpins = iter([F(74, 189), F(2341, 1856)])
    for a, al, be in (([F(2, 3), F(5, 4), F(3, 7)], F(-1, 5), F(2, 3)),
                      ([F(3, 2), F(1, 2), F(4)], F(-2, 7), F(5, 3))):
        q = a[0] ** 4
        ga = (q / 4 - al * be) / (al + be)
        ok &= ga == next(gpins)
        da = [al, be, ga]
        dda = [-q / 2, q / 2, q / 2]
        ok &= all(x == 0 for row in bianchi2_ricci(a, da, dda) for x in row)
        ok &= 4 * (al * be + be * ga + ga * al) == q
        ok &= any(x != 0 for row in bianchi2_ricci(a, da, [-q / 2 + F(1, 10), q / 2, q / 2]) for x in row)
        ok &= any(x != 0 for row in bianchi2_ricci(a, [al, be, ga + F(1, 9)], dda) for x in row)
        ok &= any(x != 0 for row in bianchi2_ricci(a, da, [-q / 2, q / 2, q / 2 + F(1, 3)]) for x in row)
    # at generic jets: N^2 R(e0,e0) = -(E1+E2+E3)/2 + C/2, N^2 R(el,el) = El/2, off-diagonal zero
    rpins = iter([(F(229, 105), F(-107, 405)), (F(2, 3), F(-17, 16))])
    for a, da, dda in (([F(2, 3), F(5, 4), F(3, 7)], [F(-1, 5), F(2, 3), F(1, 4)], [F(1, 2), F(-3), F(2, 7)]),
                       ([F(3, 2), F(1, 2), F(4)], [F(1), F(-2, 3), F(5)], [F(-1), F(1, 3), F(2)])):
        R = bianchi2_ricci(a, da, dda)
        rp, cp = next(rpins)
        ok &= R[0][0] == rp and 4 * (da[0] * da[1] + da[1] * da[2] + da[2] * da[0]) - a[0] ** 4 == cp
        q = a[0] ** 4
        N2 = (a[0] * a[1] * a[2]) ** 2
        E = [2 * dda[0] + q, 2 * dda[1] - q, 2 * dda[2] - q]
        C = 4 * (da[0] * da[1] + da[1] * da[2] + da[2] * da[0]) - q
        ok &= R[0][0] == -sum(E) / 2 + C / 2
        ok &= all(N2 * R[l + 1][l + 1] / a[l] ** 2 == E[l] / 2 for l in range(3))
        ok &= all(R[i][j] == 0 for i in range(4) for j in range(4) if i != j)
    GA.check("Bianchi II: Ricci = 0 exactly on 2a1''=-a1^4, 2a2''=2a3''=a1^4, 4 sum a'a' = a1^4; not off them", ok)
    return ok


def bkl(p):
    a = 0
    return [-p[a] / (1 + 2 * p[a])] + [(p[b] + 2 * p[a]) / (1 + 2 * p[a]) for b in (1, 2)]


def check_liouville_bounce_is_bkl_law():
    premise("synthesis.bkl-bounces-no-framewise-invariant")
    ok = True
    # alpha_1 = log(2v)/2 - log cosh(2vT)/2: with s = tanh(2vT), alpha_1' = -v s, alpha_1'' = -2 v^2 (1 - s^2),
    # a_1^4 = 4 v^2 (1 - s^2); alpha_2' = -alpha_1' + B, alpha_3' = -alpha_1' + C
    for v, B in ((F(1, 2), F(3, 4)), (F(2, 3), F(5)), (F(1), F(7, 3))):
        C = v * v / B
        for s in (F(-9, 10), F(-1, 3), F(0), F(1, 2), F(7, 8)):
            d1, dd1, q = -v * s, -2 * v * v * (1 - s * s), 4 * v * v * (1 - s * s)
            d2, d3 = -d1 + B, -d1 + C
            ok &= 2 * dd1 == -q and 2 * (-dd1) == q
            ok &= 4 * (d1 * d2 + d2 * d3 + d3 * d1) == q
            ok &= d1 * d1 + q / 4 == v * v
        late = [-v, B + v, C + v]
        early = [v, B - v, C - v]
        Sp, Sm = sum(late), sum(early)
        ok &= Sp > 0 and Sm > 0
        p, pe = [x / Sp for x in late], [x / Sm for x in early]
        ok &= sum(p) == 1 and sum(x * x for x in p) == 1 and p[0] < 0
        ok &= sum(x * x for x in pe) == 1 and pe == bkl(p)
        ok &= Sm == Sp * (1 + 2 * p[0])
        ok &= pe[0] > 0 and min(pe[1], pe[2]) <= 0
    for u in (F(3, 2), F(2), F(5), F(13, 4)):
        p = kasner(u)
        q = bkl(p)
        ok &= sorted(q) == sorted(kasner(u - 1) if u >= 2 else kasner(1 / (u - 1)))
    GA.check("Liouville wall: late epoch p_1<0 -> earlier epoch = BKL law (u -> u-1); new negative weight on a free axis", ok)
    return ok


# ---------------------------------------------------------------- the GTG route (lib/gtg.py)
SQ_SLICE = GA.sig(0, 3)            # the slice's physical vectors: the spacetime vectors orthogonal to gamma_0


def slice_field(a, A0, A1, A2):
    """The slice gauge field hb^{-1}(e_i) = sum_l a_l theta^l_i(x) gamma_l (Cl(0,3)) on exact second-order jets."""
    X = [gtg.Jet.var(i, F(0), N3, 2) for i in range(N3)]
    TH = [[None] * N3 for _ in range(N3)]
    for l in range(N3):
        for i in range(N3):
            j = gtg.Jet.const(A0[l][i], N3)
            for k in range(N3):
                j = j + A1[k][l][i] * X[k]
                for m in range(N3):
                    j = j + (A2[k][m][l][i] / 2) * X[k] * X[m]
            TH[l][i] = a[l] * j
    return gtg.Field(TH, sq=SQ_SLICE)


def bianchi2_field(a, da, dda):
    """N gamma0, a1 (dx - z dy) gamma1, a2 dy gamma2, a3 dz gamma3 on jets in (T, z) about T = 0, z = 0."""
    T = gtg.Jet.var(0, F(0), 4, 2)
    z = gtg.Jet.var(3, F(0), 4, 2)
    aj = [a[i] + a[i] * da[i] * T + (a[i] * (dda[i] + da[i] * da[i]) / 2) * T * T for i in range(3)]
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0] = aj[0] * aj[1] * aj[2]
    TH[1][1] = aj[0]
    TH[1][2] = F(0) - aj[0] * z
    TH[2][2] = aj[1]
    TH[3][3] = aj[2]
    return gtg.Field(TH)


B2_GENERIC = (([F(2, 3), F(5, 4), F(3, 7)], [F(-1, 5), F(2, 3), F(1, 4)], [F(1, 2), F(-3), F(2, 7)]),
              ([F(3, 2), F(1, 2), F(4)], [F(1), F(-2, 3), F(5)], [F(-1), F(1, 3), F(2)]))
B2_SOLUTIONS = (([F(2, 3), F(5, 4), F(3, 7)], F(-1, 5), F(2, 3)), ([F(3, 2), F(1, 2), F(4)], F(-2, 7), F(5, 3)))
B2_KICK = F(1, 7)


def bianchi2_omega_closed(a, da, dda):
    """The closed form of Omega(e_mu) for the Bianchi II field, as jets in (T, z):
    Omega(e_T) = 0, Omega(e_x) = -(alpha1'/(a2 a3)) e01 + (a1^2/(2 a2 a3)) e23,
    Omega(e_y) = z (alpha1'/(a2 a3)) e01 - (alpha2'/(a1 a3)) e02 + (a1/(2 a3)) e13 - z (a1^2/(2 a2 a3)) e23,
    Omega(e_z) = -(alpha3'/(a1 a2)) e03 - (a1/(2 a2)) e12."""
    T = gtg.Jet.var(0, F(0), 4, 2)
    z = gtg.Jet.var(3, F(0), 4, 2)
    aj = [a[i] + a[i] * da[i] * T + (a[i] * (dda[i] + da[i] * da[i]) / 2) * T * T for i in range(3)]
    al = [aj[i].d(0) / aj[i] for i in range(3)]
    a1, a2, a3 = aj
    u = al[0] / (a2 * a3)
    w = a1 * a1 / (a2 * a3 * 2)
    return [{}, {(0, 1): F(0) - u, (2, 3): w},
            {(0, 1): z * u, (0, 2): F(0) - al[1] / (a1 * a3), (1, 3): a1 / (a3 * 2), (2, 3): F(0) - z * w},
            {(0, 3): F(0) - al[2] / (a1 * a2), (1, 2): F(0) - a1 / (a2 * 2)}]


def check_gtg_slice_and_bianchi_ii_field_strength():
    """(i) R^(3) is the store-sign scalar of the slice gauge field (Omega solved from the torsion equation,
    physical vectors in Cl(0,3)); it equals the frame formula and the coordinate scalar at the sample coframes
    and weights. (iv) The Bianchi II gauge field: the torsion-solved Omega equals the closed form
    bianchi2_omega_closed (value and first derivatives in T and z); its Ricci map: R^o_{mu nu} = -g_mu . calR(g_nu) gives
    R^o_TT = N^2 R^o(e0, e0) = -(E1 + E2 + E3)/2 + C/2, N^2 R^o(e_l, e_l) = E_l/2, off-diagonal zero; calR(a) = 0
    on the stated solution jets and not on perturbed ones."""
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for seed in SEEDS:
        A0, A1, A2 = coframe(seed)
        for a in WEIGHTS[:3]:
            fld = slice_field(a, A0, A1, A2)
            ok &= fld.torsion_free()
            R3 = gtg.ricci_scalar(fld.curvature(), SQ_SLICE)
            ok &= R3 == scalar_frame(a, A0, A1, A2)[0] and R3 == scalar_coord(a, A0, A1, A2)
    for a, da, dda in B2_GENERIC:
        fld = bianchi2_field(a, da, dda)
        ok &= fld.torsion_free()
        cf = bianchi2_omega_closed(a, da, dda)
        for mu in range(4):
            diff = gtg.m_sub(fld.Om[mu], cf[mu])
            ok &= not gtg.m_val(diff) and not gtg.m_val(gtg.m_d(diff, 0)) and not gtg.m_val(gtg.m_d(diff, 3))
        Rc = fld.curvature()
        g = [fld.hb_inv(GA.gen(m)) for m in range(4)]
        Ro = [[F(0) - gtg.vdot(g[m], gtg.ricci(Rc, g[n]), gtg.S13) for n in range(4)] for m in range(4)]
        q = a[0] ** 4
        N2 = (a[0] * a[1] * a[2]) ** 2
        E = [2 * dda[0] + q, 2 * dda[1] - q, 2 * dda[2] - q]
        Cc = 4 * (da[0] * da[1] + da[1] * da[2] + da[2] * da[0]) - q
        ok &= Ro[0][0] == -sum(E) / 2 + Cc / 2          # coordinate R_TT = N^2 R(e0, e0)
        ok &= all(N2 * Ro[l + 1][l + 1] / a[l] ** 2 == E[l] / 2 for l in range(3))
        ok &= all(Ro[i][j] == 0 for i in range(4) for j in range(4) if i != j)
        ok &= Ro == bianchi2_ricci(a, da, dda)
    for a, al, be in B2_SOLUTIONS:
        q = a[0] ** 4
        ga = (q / 4 - al * be) / (al + be)
        Rc = bianchi2_field(a, [al, be, ga], [-q / 2, q / 2, q / 2]).curvature()
        ok &= all(gtg.ricci(Rc, GA.gen(m)) == {} for m in range(4))
        Rp = bianchi2_field(a, [al, be, ga], [-q / 2, q / 2 + B2_KICK, q / 2]).curvature()
        ok &= any(gtg.ricci(Rp, GA.gen(m)) != {} for m in range(4))
    GA.check("GTG: slice scalar = frame formula = coordinate scalar; Bianchi II Ricci map gives E_l, C", ok)
    return ok


# ---- (i) the Ellis-MacCallum frame formula derived from the torsion equation (exact polynomial identity) ----
EM_NV = 36                                  # nine c^_mn^l (m < n) and their 27 frame derivatives e^_k(c^_mn^l)
EM_PAIRS = [(0, 1), (0, 2), (1, 2)]


def _em_var(i):
    return gtg.Jet.var(i, F(0), EM_NV, None)


EM_ZERO = gtg.Jet.const(F(0), EM_NV)


def _em_idx(i, j, k):
    if i == j:
        return None, 0
    s = 1
    if i > j:
        i, j, s = j, i, -1
    return EM_PAIRS.index((i, j)) * 3 + k, s


def _em_c(i, j, k):
    """The structure function c^_ij^k of the orthonormal frame, as a polynomial variable."""
    idx, s = _em_idx(i, j, k)
    return EM_ZERO if idx is None else _em_var(idx) * s


def _em_dc(m, i, j, k):
    """Its frame derivative e^_m(c^_ij^k), an independent variable."""
    idx, s = _em_idx(i, j, k)
    return EM_ZERO if idx is None else _em_var(9 + 9 * m + idx) * s


def _em_frame_derivative(m, x):
    """e^_m of a multivector whose coefficients are linear in the c^ (constant coefficients)."""
    out = {}
    for b, j in x.items():
        t = EM_ZERO
        for e, v in j.c.items():
            if sum(e):
                t = t + _em_var(9 + 9 * m + e.index(1)) * v
        if t:
            out[b] = t
    return out


def _em_omega():
    """omega_m = Omega(e^_m) from the torsion equation omega_m x e_n - omega_n x e_m = c^_mn^l e_l (Cl(0,3))."""
    E3 = [GA.gen(i) for i in range(N3)]
    cols = [(m, b) for m in range(N3) for b in EM_PAIRS]
    rows = []
    for (m, n) in EM_PAIRS:
        for comp in range(N3):
            row = []
            for (mm, b) in cols:
                B = {b: F(1)}
                v = F(0)
                if mm == m:
                    v += gtg.comm(B, E3[n], SQ_SLICE).get((comp,), F(0))
                if mm == n:
                    v -= gtg.comm(B, E3[m], SQ_SLICE).get((comp,), F(0))
                row.append(v)
            rows.append(row)
    Minv = gtg.mat_inv(rows)
    rhs = [_em_c(m, n, comp) for (m, n) in EM_PAIRS for comp in range(N3)]
    w = [sum((Minv[r][s] * rhs[s] for s in range(9)), EM_ZERO) for r in range(9)]
    om = [{b: w[3 * m + k] for k, b in enumerate(EM_PAIRS) if w[3 * m + k]} for m in range(N3)]
    ok = True
    for (m, n) in EM_PAIRS:
        lhs = gtg.m_sub(gtg.comm(om[m], E3[n], SQ_SLICE), gtg.comm(om[n], E3[m], SQ_SLICE))
        ok = ok and not gtg.m_sub(lhs, gtg.m_add(*[gtg.m_scal(_em_c(m, n, l), E3[l]) for l in range(N3)]))
    return om, ok


def _em_formula():
    """4 e_i(acc_i) - 6 acc.acc - (1/2)(2 n:n - (tr n)^2), with acc_i = c_ij^j/2 and
    n^lk = (1/2) eps^lij c_ij^k - eps^lik acc_i; returns the polynomial and whether the decomposition holds."""
    acc = [sum((_em_c(i, j, j) for j in range(N3)), EM_ZERO) * F(1, 2) for i in range(N3)]
    n = [[sum((_em_c(i, j, k) * (eps(l, i, j) / 2) for i in range(N3) for j in range(N3)), EM_ZERO)
          - sum((acc[i] * eps(l, i, k) for i in range(N3)), EM_ZERO) for k in range(N3)] for l in range(N3)]
    ok = all(not (n[l][k] - n[k][l]) for l in range(N3) for k in range(N3))
    ok = ok and all(not (_em_c(i, j, k) - sum((n[l][k] * eps(i, j, l) for l in range(N3)), EM_ZERO)
                         - (acc[i] if j == k else EM_ZERO) + (acc[j] if i == k else EM_ZERO))
                    for i in range(N3) for j in range(N3) for k in range(N3))
    ea = sum((_em_dc(i, i, j, j) for i in range(N3) for j in range(N3)), EM_ZERO) * F(1, 2)
    nn = sum((n[k][l] * n[k][l] for k in range(N3) for l in range(N3)), EM_ZERO)
    tr = sum((n[k][k] for k in range(N3)), EM_ZERO)
    return ea * 4 - sum((acc[i] * acc[i] for i in range(N3)), EM_ZERO) * 6 - (nn * 2 - tr * tr) * F(1, 2), ok


def _em_eval(j, vals):
    tot = F(0)
    for e, v in j.c.items():
        t = v
        for i, p in enumerate(e):
            if p:
                t *= vals[i] ** p
        tot += t
    return tot


def check_gtg_ellis_maccallum_frame_formula():
    """(i) The frame formula is a consequence of the torsion equation: for an orthonormal frame e_l of Cl(0,3) with
    background fields e^_l = hb(e_l), [e^_m, e^_n] = c^_mn^l e^_l, omega_m = Omega(e^_m) solves
    omega_m x e_n - omega_n x e_m = c^_mn^l e_l, and calR(e_m ^ e_n) = -(e^_m(omega_n) - e^_n(omega_m)
    + omega_m x omega_n - c^_mn^l omega_l); its scalar d_a . calR(a), with the c^ and their frame derivatives as
    independent variables, equals the Ellis-MacCallum formula as a polynomial (21 monomials, six of them the
    derivatives e^_i(c^_ij^j)); n^ is symmetric and the decomposition reproduces c^; the unit three-sphere's
    left-invariant frame (c^_ij^k = +-2 eps_ijk) gives 6 both ways."""
    premise("synthesis.imported-gtg-dictionary")
    om, ok = _em_omega()
    Rc = {}
    for (m, n) in EM_PAIRS:
        Rmn = gtg.m_add(_em_frame_derivative(m, om[n]), gtg.m_neg(_em_frame_derivative(n, om[m])),
                        gtg.comm(om[m], om[n], SQ_SLICE),
                        *[gtg.m_scal(_em_c(m, n, l) * -1, om[l]) for l in range(N3)])
        Rc[(m, n)] = gtg.m_neg(Rmn)
    Rs = gtg.ricci_scalar(Rc, SQ_SLICE)
    REM, dec = _em_formula()
    ok = ok and dec and not (Rs - REM)
    ok = ok and len(Rs.c) == 21 and sum(1 for e in Rs.c if any(e[9:])) == 6
    for sgn in (2, -2):
        vals = [F(0)] * EM_NV
        for (i, j) in EM_PAIRS:
            vals[_em_idx(i, j, 3 - i - j)[0]] = sgn * eps(i, j, 3 - i - j)
        ok = ok and _em_eval(Rs, vals) == 6 and _em_eval(REM, vals) == 6
    GA.check("GTG: the Ellis-MacCallum frame formula is the torsion-solved slice scalar, as a polynomial identity", ok)
    _tp_rv = (ok); assert _tp_rv is not False, "check_gtg_ellis_maccallum_frame_formula"; return _tp_rv
