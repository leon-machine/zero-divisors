"""standard-model.internal-symmetry-ladder: exact checks.

A mixing Z^i -> U^i_j Z^j sends the total momentum p = sum_i pi^i pibar^i to sum_{j,k} (U^T Ubar)_{jk} pi^j pibar^k,
so it preserves p for every configuration iff N = U^T Ubar - 1 satisfies sum N_jk pi^j pibar^k = 0 for all
configurations.
(1) n = 2: for an explicit configuration the four products pi^j pibar^k are independent (rank 4 over Q(i)), so the
    linear map N -> sum N_jk pi^j pibar^k has zero kernel: momentum preservation forces U^T Ubar = 1, i.e. U unitary.
    n = 3: the nine products of a generic configuration have rank 4 only (dependent), so the proof goes through
    rank-one configurations pi^j = v_j pi: then sum N_jk v_j vbar_k = 0 for all v, and on the nine test vectors the
    functionals v -> v^dag M v have rank 9 on the nine-dimensional space of Hermitian forms, so M = 0.
(2) Exact unitaries (real and complex Gaussian-rational, n = 2 and n = 3) preserve the total momentum and the
    helicity form sum |Z^i|^2; non-unitary mixings (diag(2, 1), a shear) do not.
(3) U(n) = (SU(n) x U(1))/Z_n for n = 2, 3: in Q(zeta_6) the pairs (mu^-1 I_n, mu) with mu^n = 1 map to the identity
    under (a, mu) -> mu a, their a factors have det 1, there are exactly n of them (x^n - 1 has n distinct roots
    among the sixth roots of unity), and the other 6 - n sixth roots of unity fail mu^n = 1.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
P1 = [QI(1), QI(0)]
P2 = [QI(1, 1), QI(2)]
P3 = [QI(2, -1), QI(F(1, 3), 1)]
U2 = [[[QI(F(3, 5)), QI(F(4, 5))], [QI(F(-4, 5)), QI(F(3, 5))]],
      [[QI(F(3, 5), F(4, 5)), QI(0)], [QI(0), QI(1)]]]
U3 = [[[QI(F(1, 3)), QI(F(2, 3)), QI(F(2, 3))], [QI(F(2, 3)), QI(F(1, 3)), QI(F(-2, 3))],
       [QI(0, F(2, 3)), QI(0, F(-2, 3)), QI(0, F(1, 3))]]]
NONU = [[[QI(2), QI(0)], [QI(0), QI(1)]], [[QI(1), QI(1)], [QI(0), QI(1)]]]
I_ = QI(0, 1)
TESTV = [[QI(1), QI(0), QI(0)], [QI(0), QI(1), QI(0)], [QI(0), QI(0), QI(1)],
         [QI(1), QI(1), QI(0)], [QI(1), QI(0), QI(1)], [QI(0), QI(1), QI(1)],
         [QI(1), I_, QI(0)], [QI(1), QI(0), I_], [QI(0), QI(1), I_]]


def _outer(a, b):
    return [a[A] * b[Ap].conj() for A in range(2) for Ap in range(2)]


def _herm_basis(n):
    out = []
    for j in range(n):
        M = [[QI(0)] * n for _ in range(n)]
        M[j][j] = QI(1)
        out.append(M)
    for j in range(n):
        for k in range(j + 1, n):
            M = [[QI(0)] * n for _ in range(n)]
            M[j][k] = M[k][j] = QI(1)
            out.append(M)
            M2 = [[QI(0)] * n for _ in range(n)]
            M2[j][k], M2[k][j] = I_, QI(0, -1)
            out.append(M2)
    return out


def _quad(M, v):
    n = len(v)
    return sum((v[j].conj() * M[j][k] * v[k] for j in range(n) for k in range(n)), QI(0))


def _mix(U, sp):
    n = len(U)
    return [[sum((U[i][j] * sp[j][A] for j in range(n)), QI(0)) for A in range(2)] for i in range(n)]


def _ptot(sp):
    p = [QI(0)] * 4
    for s in sp:
        p = [x + y for x, y in zip(p, _outer(s, s))]
    return p


def _helicity(sp):
    return sum((s[A] * s[A].conj() for s in sp for A in range(2)), QI(0))


class Z6(object):
    def __init__(self, p=0, q=0):
        self.p, self.q = F(p), F(q)

    def __mul__(self, o):
        return Z6(self.p * o.p - self.q * o.q, self.p * o.q + self.q * o.p + self.q * o.q)

    def __eq__(self, o):
        return self.p == o.p and self.q == o.q

    def __hash__(self):
        return hash((self.p, self.q))

    def inv(self):
        conj = Z6(self.p + self.q, -self.q)
        nrm = (self * conj).p
        return Z6(conj.p / nrm, conj.q / nrm)

    def pw(self, n):
        out = Z6(1)
        b = self if n >= 0 else self.inv()
        for _ in range(abs(n)):
            out = out * b
        return out


def check_momentum_preservation_forces_unitarity():
    rows2 = [_outer(p, q) for p in (P1, P2) for q in (P1, P2)]
    rows3 = [_outer(p, q) for p in (P1, P2, P3) for q in (P1, P2, P3)]
    ok = GA.field_rank(rows2) == 4 and GA.field_rank(rows3) == 4
    rows = []
    allreal = True
    for v in TESTV:
        row = []
        for M in _herm_basis(3):
            z = _quad(M, v)
            allreal = allreal and z.im == 0
            row.append(z.re)
        rows.append(row)
    ok = ok and allreal and GA.mat_rank(rows) == 9 == len(_herm_basis(3))
    GA.check("n = 2: products independent (rank 4); n = 3: rank 4 of 9, polarisation rank 9 forces U^dag U = 1", ok)
    return ok


def check_unitaries_preserve_and_others_fail():
    ok = True
    for U in U2:
        sp = [P1, P2]
        ok = ok and _ptot(_mix(U, sp)) == _ptot(sp) and _helicity(_mix(U, sp)) == _helicity(sp)
    for U in U3:
        sp = [P1, P2, P3]
        ok = ok and _ptot(_mix(U, sp)) == _ptot(sp) and _helicity(_mix(U, sp)) == _helicity(sp)
    for U in NONU:
        sp = [P1, P2]
        ok = ok and _ptot(_mix(U, sp)) != _ptot(sp)
    # the helicity form of the two- and three-spinor configurations, |pi|^2 summed: 1 + 6 and 7 + 55/9
    ok = ok and _helicity([P1, P2]) == QI(7) and _helicity([P1, P2, P3]) == QI(F(118, 9))
    GA.check("unitary mixings preserve momentum and helicity; diag(2, 1) and a shear do not", ok)
    return ok


def check_un_is_sun_times_u1_mod_zn():
    zeta = Z6(0, 1)
    roots6 = [zeta.pw(j) for j in range(6)]
    ok = len(set(roots6)) == 6 and zeta.pw(6) == Z6(1)
    for n in (2, 3):
        ker = [mu for mu in roots6 if mu.pw(n) == Z6(1)]
        ok = ok and len(ker) == n
        for mu in ker:
            a = mu.pw(-1)                    # a = mu^-1 I_n, mu a = I_n, det a = mu^-n = 1
            ok = ok and mu * a == Z6(1) and a.pw(n) == Z6(1)
        others = [mu for mu in roots6 if mu.pw(n) != Z6(1)]
        ok = ok and len(others) == 6 - n
    GA.check("U(n) = (SU(n) x U(1))/Z_n: kernel of exactly n elements for n = 2, 3", ok)
    return ok
