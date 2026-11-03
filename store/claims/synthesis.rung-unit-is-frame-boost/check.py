"""synthesis.rung-unit-is-frame-boost: exact checks.

The rung summand is built in GA.py as Cl(2,2) (generators 0, 1 of square +1 are e+_4, e+_5; 2, 3 of
square -1 are e-_4, e-_5). Operators on vectors are 4x4 matrices in the basis (v4, v5, w4, w5);
complex matrices use GA's Gaussian rationals. Everything is exact.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = GA.sig(2, 2)
EV = [GA.gen(i) for i in range(4)]
HALF = F(1, 2)
V = [GA.scal(HALF, GA.add(EV[2], EV[0])), GA.scal(HALF, GA.add(EV[3], EV[1]))]
W = [GA.scal(HALF, GA.sub(EV[0], EV[2])), GA.scal(HALF, GA.sub(EV[1], EV[3]))]
BASIS = V + W


def coords(x):
    """Coordinates of a vector in (v4, v5, w4, w5): e+_a = v_a + w_a, e-_a = v_a - w_a."""
    c = [F(0)] * 4
    for blade, val in x.items():
        assert len(blade) == 1
        i = blade[0]
        if i < 2:
            c[i] += val
            c[2 + i] += val
        else:
            c[i - 2] += val
            c[i] -= val
    return c


def ad(B):
    cols = [coords(GA.sub(GA.mul(B, x, SQ), GA.mul(x, B, SQ))) for x in BASIS]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def mmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), F(0) * 0) for j in range(n)] for i in range(n)]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def tp(A):
    return [list(r) for r in zip(*A)]


def lin(A, B, c):
    return [[A[i][j] + c * B[i][j] for j in range(len(A))] for i in range(len(A))]


def gram():
    return [[GA.dot(x, y, SQ) for y in BASIS] for x in BASIS]


def slot_generators():
    return {(a, b): ad(GA.mul(V[a], W[b], SQ)) for a in range(2) for b in range(2)}


def invariant_symmetric_forms(gens):
    idx = [(i, j) for i in range(4) for j in range(i, 4)]
    eqs = []
    for M in gens:
        cols = []
        for n in range(len(idx)):
            K = [[F(0)] * 4 for _ in range(4)]
            i, j = idx[n]
            K[i][j] = K[j][i] = F(1)
            Z = lin(mmul(tp(M), K), mmul(K, M), 1)
            cols.append([x for r in Z for x in r])
        for r in range(16):
            eqs.append([cols[n][r] for n in range(len(idx))])
    return len(idx) - GA.rank_of_vectors(eqs)


def qf(M, c):
    return sum((c[i] * M[i][j] * c[j] for i in range(4) for j in range(4)), F(0))


def check_rung_unit_is_frame_boost():
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    premise("standard-model.transported-frozen-point")
    G = gram()
    assert G == [[0, 0, HALF, 0], [0, 0, 0, HALF], [HALF, 0, 0, 0], [0, HALF, 0, 0]]
    assert GA.congruence_signature(G) == (2, 2, 0)
    E = slot_generators()
    # (1) E_ab: matrix unit on the v's, minus the transpose on the w's; each preserves Q
    for a in range(2):
        for b in range(2):
            M = E[(a, b)]
            want = [[F(0)] * 4 for _ in range(4)]
            want[a][b] = F(1)
            want[2 + b][2 + a] = F(-1)
            assert M == want
            Z = lin(mmul(tp(M), G), mmul(G, M), 1)
            assert all(x == 0 for r in Z for x in r)
    NR = lin(E[(0, 0)], E[(1, 1)], 1)
    assert NR == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
    # (1) the compact u(2): i(E_ab + E_ba), E_ab - E_ba, i E_aa; which real combinations are real matrices
    I = GA.qi(0, 1)

    def cm(M, c):
        return [[c * GA.qi(x) for x in r] for r in M]
    U2 = [cm(E[(0, 0)], I), cm(E[(1, 1)], I), cm(lin(E[(0, 1)], E[(1, 0)], 1), I),
          cm(lin(E[(0, 1)], E[(1, 0)], -1), GA.qi(1))]
    rows = [[U2[k][i][j].im for k in range(4)] for i in range(4) for j in range(4)]
    assert 4 - GA.rank_of_vectors(rows) == 1
    assert all(x.im == 0 for r in U2[3] for x in r)          # the survivor is E_45 - E_54
    # (2) trace form of so(2,2) on R: signature (4,2); control so(4): (0,6)
    ADS = [ad(GA.mul(EV[i], EV[j], SQ)) for i, j in combinations(range(4), 2)]
    TF = [[tr(mmul(X, Y)) for Y in ADS] for X in ADS]
    assert GA.congruence_signature(TF) == (4, 2, 0)
    SQ4 = GA.sig(4, 0)
    E4 = [GA.gen(i) for i in range(4)]

    def ad4(B):
        cols = []
        for x in E4:
            y = GA.sub(GA.mul(B, x, SQ4), GA.mul(x, B, SQ4))
            cols.append([y.get((i,), F(0)) for i in range(4)])
        return [[cols[j][i] for j in range(4)] for i in range(4)]
    A4 = [ad4(GA.mul(E4[i], E4[j], SQ4)) for i, j in combinations(range(4), 2)]
    assert GA.congruence_signature([[tr(mmul(X, Y)) for Y in A4] for X in A4]) == (0, 6, 0)
    # su(2) in its 2-dim rep: trace form negative definite on all three generators (the sign used in (2))
    s = [[[GA.qi(0, 1), GA.qi(0)], [GA.qi(0), GA.qi(0, -1)]],
         [[GA.qi(0), GA.qi(1)], [GA.qi(-1), GA.qi(0)]],
         [[GA.qi(0), GA.qi(0, 1)], [GA.qi(0, 1), GA.qi(0)]]]
    for X in s:
        t2 = sum((X[i][k] * X[k][i] for i in range(2) for k in range(2)), GA.qi(0))
        assert t2.im == 0 and t2.re == -2
    # (3) invariant symmetric forms: one-dimensional for gl(2,R), sl(2,R) and so(2,2); theta-form definite
    assert invariant_symmetric_forms(list(E.values())) == 1
    assert invariant_symmetric_forms([E[(0, 1)], E[(1, 0)], lin(E[(0, 0)], E[(1, 1)], -1)]) == 1
    assert invariant_symmetric_forms(ADS) == 1
    TH = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
    TH = [[F(x) for x in r] for r in TH]
    assert [coords(x) for x in (EV[0], EV[2])] == [[1, 0, 1, 0], [1, 0, -1, 0]]
    KS = mmul(G, TH)
    assert GA.congruence_signature(KS) == (4, 0, 0)
    assert KS == [[HALF if i == j else 0 for j in range(4)] for i in range(4)]
    # theta fixes e+ and negates e- in BOTH rung planes, checked on the frame itself
    for a in range(2):
        ep, em = coords(EV[a]), coords(EV[2 + a])
        assert [sum(TH[i][j] * ep[j] for j in range(4)) for i in range(4)] == ep
        assert [sum(TH[i][j] * em[j] for j in range(4)) for i in range(4)] == [-x for x in em]
    boosts = [ADS[k] for k in range(6) if tr(mmul(ADS[k], ADS[k])) > 0]
    assert len(boosts) == 4 and all(mmul(B, TH) != mmul(TH, B) for B in boosts)
    # (4) the lift's rung component in a boosted null pair
    pairs = [(F(1, 5), F(1)), (F(3), F(1)), (F(7, 2), F(1)), (F(3), F(1, 3)), (F(1, 5), F(2)),
             (F(7, 2), F(5, 7)), (F(4, 3), F(2, 3)), (F(12), F(2)), (F(1, 3), F(1, 3)),
             (F(5), F(3, 4)), (F(2), F(9, 4)), (F(27, 4), F(3, 2))]
    for L, lam in pairs:
        n0 = [F(0), F(0), -lam, F(0)]
        ninf = [F(2) / lam, F(0), F(0), F(0)]
        assert qf(G, n0) == 0 and qf(G, ninf) == 0
        assert sum((n0[i] * G[i][j] * ninf[j] for i in range(4) for j in range(4)), F(0)) == -1
        c = [n0[i] + (L / 6) * ninf[i] for i in range(4)]
        mu = (L / 3) / lam
        assert c == [mu, F(0), -lam, F(0)]
        assert qf(G, c) == -L / 3
        assert qf(KS, c) == (lam * lam + mu * mu) / 2
        assert qf(KS, c) - L / 3 == (lam - mu) ** 2 / 2
        balanced = lam * lam == L / 3
        assert (qf(KS, c) == L / 3) == balanced
        # (5) |a| = |b| exactly when balanced (U(2) and complex scale preserve |a|, |b| ratios)
        assert (mu * mu == lam * lam) == balanced
        if balanced:
            a, b = GA.qi(mu), GA.qi(-lam)
            ia, ib = I * a, I * b
            assert ib == ia.conj()                      # i c lies in R_1 = {a.v + conj(a).w}
    assert sum(1 for L, lam in pairs if lam * lam == L / 3) == 5
    # (5) U(2) preserves R_mu: generator X acts by (Xa, conj(X) b); test on a real basis of R_mu
    for mu in (F(1), F(-1), F(2, 5)):
        for X in U2:
            Xa = [[X[i][j] for j in range(2)] for i in range(2)]
            Xb = [[X[2 + i][2 + j] for j in range(2)] for i in range(2)]
            assert all(Xb[i][j] == Xa[i][j].conj() for i in range(2) for j in range(2))
            for a in ([GA.qi(1), GA.qi(0)], [GA.qi(0, 1), GA.qi(0)], [GA.qi(0), GA.qi(1)], [GA.qi(0), GA.qi(0, 1)]):
                b = [GA.qi(mu) * z.conj() for z in a]
                na = [sum((Xa[i][j] * a[j] for j in range(2)), GA.qi(0)) for i in range(2)]
                nb = [sum((Xb[i][j] * b[j] for j in range(2)), GA.qi(0)) for i in range(2)]
                assert all(nb[i] == GA.qi(mu) * na[i].conj() for i in range(2))
                q = sum((a[i] * b[i] for i in range(2)), GA.qi(0))     # Q = 2 * (1/2) * sum a_i b_i
                assert q.im == 0 and (q.re > 0) == (mu > 0)
    return True
