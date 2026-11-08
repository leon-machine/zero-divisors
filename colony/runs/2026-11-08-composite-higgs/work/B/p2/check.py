"""synthesis.even-composite-doublet-needs-a-singlet-constituent-and-its-pair-modes-are-quasi-spins: exact checks.

(i)  Selection rule, in the full Clifford algebra of the tower planes (GA's blade engine): plane j has generators
     e_j, f_j (squares +1, -1), v_j = (e_j + f_j)/2 = a_j*, w_j = (e_j - f_j)/2 = a_j. Planes 0, 1 are a doublet
     (up, down), the rest singlets. Isospin T_+ = v_0 w_1, T_- = v_1 w_0, T_3 = (v_0 w_0 - v_1 w_1)/2; the Casimir
     of ad is C = ad(T_3)^2 + (ad T_+ ad T_- + ad T_- ad T_+)/2. On the span A^(pD, pS) of the blades with doublet
     parity pD and singlet parity pS: C = 3/4 exactly when pD = 1, and C(C - 2) = 0 with the eigenvalue 2 of fixed
     multiplicity when pD = 0. One and two singlet planes; with no singlet plane every even element has integer
     isospin (the stored rung case). Hypercharge weights of the doublet-singlet bilinears.
(ii) Charged pair modes on a window k in {-2, -1, 0, 1} with channels (up, down, s), each mode a tower plane in GA's
     exterior model of the CAR: hypercharge weights (Y_d, Y_d, Y_s), M_up = E_{up, s}; [W, M] = (Y_d - Y_s) M, M^2 = 0,
     M not normal; the commutator on edge-clean vectors takes the two values q + 1 and q - 1; on the chiral sea
     B = rho_q(M)* has |B^p Omega|^2 = (p!)^2 C(q, p), B^(q+1) Omega = 0; the mutual commutator of the two components
     on an edge-clean vector is the isospin raising density.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

YD, YS = F(1, 6), F(-1, 3)          # sample weights with Y_d - Y_s = 1/2


def _squares(m):
    return [F(1), F(-1)] * m           # generator 2j = e_j, 2j + 1 = f_j


def _v(j):
    return {(2 * j,): F(1, 2), (2 * j + 1,): F(1, 2)}


def _w(j):
    return {(2 * j,): F(1, 2), (2 * j + 1,): F(-1, 2)}


def _comm(x, y, sq):
    return GA.sub(GA.mul(x, y, sq), GA.mul(y, x, sq))


def _iso(sq):
    tp = GA.mul(_v(0), _w(1), sq)
    tm = GA.mul(_v(1), _w(0), sq)
    t3 = GA.scal(F(1, 2), GA.sub(GA.mul(_v(0), _w(0), sq), GA.mul(_v(1), _w(1), sq)))
    return tp, tm, t3


def _casimir_on(blade, ops, sq):
    tp, tm, t3 = ops
    x = {blade: F(1)}
    a = _comm(t3, _comm(t3, x, sq), sq)
    b = _comm(tp, _comm(tm, x, sq), sq)
    c = _comm(tm, _comm(tp, x, sq), sq)
    return GA.add(a, GA.scal(F(1, 2), GA.add(b, c)))


def _blocks(m):
    """Casimir matrices of ad on the spans A^(pD, pS) of blades, m planes (planes 0, 1 doublet)."""
    sq = _squares(m)
    ops = _iso(sq)
    blades = GA.all_blades(2 * m)
    out = {}
    for pd in (0, 1):
        for ps in (0, 1):
            sub = [b for b in blades if sum(1 for g in b if g < 4) % 2 == pd and sum(1 for g in b if g >= 4) % 2 == ps]
            idx = {b: i for i, b in enumerate(sub)}
            M = [[F(0)] * len(sub) for _ in sub]
            closed = True
            for j, b in enumerate(sub):
                for t, cf in _casimir_on(b, ops, sq).items():
                    if t not in idx:
                        closed = closed and cf == 0
                        continue
                    M[idx[t]][j] += cf
            out[(pd, ps)] = (M, closed)
    return out


def _shift(M, e):
    return [[M[i][j] - (e if i == j else 0) for j in range(len(M))] for i in range(len(M))]


def _zero(M):
    return all(x == 0 for r in M for x in r)


def check_doublets_are_odd_in_the_doublet_modes():
    premise("synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    ok = True
    found = []
    for m in (2, 3, 4):
        for (pd, ps), (M, closed) in _blocks(m).items():
            n = len(M)
            ok = ok and closed
            if pd == 1:
                ok = ok and _zero(_shift(M, F(3, 4)))
                found.append((m, pd, ps, n, n))
            else:
                ok = ok and (n == 0 or _zero(GA.mat_mul(M, _shift(M, F(2)))))
                found.append((m, pd, ps, n, n - GA.mat_rank(_shift(M, F(2)))))
    # (planes, pD, pS, dimension, multiplicity of the eigenvalue 3/4 (pD = 1) or 2 (pD = 0))
    ok = ok and found[:4] == [(2, 0, 0, 8, 3), (2, 0, 1, 0, 0), (2, 1, 0, 8, 8), (2, 1, 1, 0, 0)]
    ok = ok and found[4:] == [(3, 0, 0, 16, 6), (3, 0, 1, 16, 6), (3, 1, 0, 16, 16), (3, 1, 1, 16, 16),
                          (4, 0, 0, 64, 24), (4, 0, 1, 64, 24), (4, 1, 0, 64, 64), (4, 1, 1, 64, 64)]
    GA.check("ad-isospin on one or two singlet planes beside a doublet: C = 3/4 on the doublet-odd part, C in {0, 2} "
             "on the doublet-even part; with no singlet plane no even doublet; the even doublets are A^(1,1), of dimension 16 and 64", ok)
    return ok


def check_bilinear_doublets_and_their_hypercharge():
    premise("synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet")
    ok = True
    sq = _squares(3)
    tp, tm, t3 = _iso(sq)
    y = GA.add(GA.scal(YD, GA.add(GA.mul(_v(0), _w(0), sq), GA.mul(_v(1), _w(1), sq))),
               GA.scal(YS, GA.mul(_v(2), _w(2), sq)))
    # the four bilinear doublets (upper component, lower component, expected hypercharge)
    cases = [(GA.mul(_v(0), _w(2), sq), GA.mul(_v(1), _w(2), sq), YD - YS),
             (GA.mul(_v(2), _w(1), sq), GA.neg(GA.mul(_v(2), _w(0), sq)), YS - YD),
             (GA.mul(_w(1), _w(2), sq), GA.neg(GA.mul(_w(0), _w(2), sq)), -YD - YS),
             (GA.mul(_v(2), _v(0), sq), GA.mul(_v(2), _v(1), sq), YD + YS)]
    for (up, dn, h) in cases:
        ok = ok and GA.is_zero(_comm(tp, up, sq)) and GA.eq(_comm(tm, up, sq), dn) and GA.eq(_comm(tp, dn, sq), up)
        ok = ok and GA.eq(_comm(t3, up, sq), GA.scal(F(1, 2), up)) and GA.eq(_comm(t3, dn, sq), GA.scal(F(-1, 2), dn))
        ok = ok and GA.eq(_comm(y, up, sq), GA.scal(h, up)) and GA.eq(_comm(y, dn, sq), GA.scal(h, dn))
    ok = ok and [h for (_, _, h) in cases] == [F(1, 2), F(-1, 2), F(1, 6), F(-1, 6)]
    GA.check("the doublet-singlet bilinears are even doublets; with Y_d - Y_s = 1/2 the hoppings carry +-1/2, the "
             "pairs -+(Y_d + Y_s)", ok)
    return ok


# ---------- (ii) window, exterior model ----------
KS = (-2, -1, 0, 1)
CH = 3                                  # channels 0 = up, 1 = down, 2 = s
WEIGHTS = (YD, YD, YS)


def _mode(k, a):
    return (k + 2) * CH + a


def _ann(i, st):
    return GA.ext_contract([F(1) if j == i else F(0) for j in range(len(KS) * CH)], st)


def _cre(i, st):
    return GA.ext_wedge(i, st)


def _acc(out, x, c):
    for k, v in x.items():
        out[k] = out.get(k, F(0)) + c * v


def _clean(x):
    return {k: v for k, v in x.items() if v != 0}


def _rho(q, M, st):
    """rho_q(M) = sum_{k, k+q} sum_{a, b} M_ab a*_{k,a} a_{k+q,b}."""
    out = {}
    for k in KS:
        if k + q not in KS:
            continue
        for a in range(CH):
            for b in range(CH):
                if M[a][b] != 0:
                    _acc(out, _cre(_mode(k, a), _ann(_mode(k + q, b), st)), M[a][b])
    return _clean(out)


def _rho_star(q, M, st):
    Ms = [[M[b][a] for b in range(CH)] for a in range(CH)]
    out = {}
    for k in KS:
        if k + q not in KS:
            continue
        for a in range(CH):
            for b in range(CH):
                if Ms[a][b] != 0:
                    _acc(out, _cre(_mode(k + q, a), _ann(_mode(k, b), st)), Ms[a][b])
    return _clean(out)


def _unit(a, b):
    return [[F(1) if (i, j) == (a, b) else F(0) for j in range(CH)] for i in range(CH)]


def _matmul(A, B):
    return [[sum(A[i][l] * B[l][j] for l in range(CH)) for j in range(CH)] for i in range(CH)]


def _ip(x, y):
    return sum(c * y.get(S, F(0)) for S, c in x.items())


def _sea():
    return {frozenset(_mode(k, a) for k in KS if k < 0 for a in range(CH)): F(1)}


def check_charged_pair_modes_are_quasi_spins():
    premise("synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    ok = True
    W = [[WEIGHTS[i] if i == j else F(0) for j in range(CH)] for i in range(CH)]
    M = _unit(0, 2)
    Md = _unit(1, 2)
    WM = _matmul(W, M)
    MW = _matmul(M, W)
    ok = ok and all(WM[i][j] - MW[i][j] == F(1, 2) * M[i][j] for i in range(CH) for j in range(CH))
    ok = ok and all(x == 0 for r in _matmul(M, M) for x in r)
    # the same components are charged under the channel isospin weights (1/2, -1/2, 0), whatever the hypercharge
    W3 = [[F(1, 2), F(0), F(0)], [F(0), F(-1, 2), F(0)], [F(0), F(0), F(0)]]
    for (X, t) in ((M, F(1, 2)), (Md, F(-1, 2))):
        A, B = _matmul(W3, X), _matmul(X, W3)
        ok = ok and all(A[i][j] - B[i][j] == t * X[i][j] for i in range(CH) for j in range(CH))
    MMs = _matmul(M, [[M[j][i] for j in range(CH)] for i in range(CH)])
    MsM = _matmul([[M[j][i] for j in range(CH)] for i in range(CH)], M)
    ok = ok and MMs != MsM
    q = 1
    # edge-clean vectors at depth 1: k = -2 filled in every channel, k = 1 empty; one extra particle at k = -1
    base = frozenset(_mode(-2, a) for a in range(CH))
    vals = []
    for a in (0, 2):
        x = {base | {_mode(-1, a)}: F(1)}
        c = dict(_rho(q, M, _rho_star(q, M, x)))
        _acc(c, _rho_star(q, M, _rho(q, M, x)), F(-1))
        c = _clean(c)
        vals.append(_ip(x, c))
        ok = ok and GA.ext_state_eq(c, {S: vals[-1] * v for S, v in x.items()})
    ok = ok and vals == [q + 1, q - 1]
    # mutual commutator of the two components on the edge-clean vector with a bulk down particle: the raising density
    x = {base | {_mode(-1, 1)}: F(1)}
    c = dict(_rho(q, M, _rho_star(q, Md, x)))
    _acc(c, _rho_star(q, Md, _rho(q, M, x)), F(-1))
    ok = ok and GA.ext_state_eq(_clean(c), {base | {_mode(-1, 0)}: F(1)})
    # quasi-spin on the chiral sea: |B^p Omega|^2 = (p!)^2 C(q, p), B = rho_q(M)*, for q = 1, 2
    norms = []
    for qq in (1, 2):
        st = _sea()
        row = []
        for p in range(qq + 2):
            row.append(_ip(st, st))
            st = _rho_star(qq, M, st)
        norms.append(row)
        ok = ok and _rho(qq, M, _sea()) == {}
    ok = ok and norms == [[1, 1, 0], [1, 2, 4, 0]]
    GA.check("a doublet-singlet hopping of hypercharge 1/2 is nilpotent and not normal: commutator q +- 1 on two "
             "edge-clean vectors, quasi-spin norms 1, 1, 0 (q = 1) and 1, 2, 4, 0 (q = 2) on the sea", ok)
    return ok


if __name__ == "__main__":
    check_doublets_are_odd_in_the_doublet_modes()
    check_bilinear_doublets_and_their_hypercharge()
    check_charged_pair_modes_are_quasi_spins()
