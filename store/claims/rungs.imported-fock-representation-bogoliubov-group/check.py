"""rungs.imported-fock-representation-bogoliubov-group: exact checks of the finite core.

This Fact restates an imported literature fact (its two uses are the T12 Fact and the external
literature entity); the check verifies the content directly and relies on neither, so it makes no
premise() call. The infinite-dimensional and topological parts (compactness of O(2n), the covering
Pin -> O) are not checked; the finite core is, for n = 1, 2, 3 modes.

Fock space Lambda(C^n) has basis |S> (S a subset of the modes), a_i the Jordan-Wigner annihilators,
matrices over the Gaussian rationals (GA.QI). Majorana generators g_{2i} = a_i + a_i^dag and
g_{2i+1} = i (a_i^dag - a_i).
(1) Spinor module: the CAR hold; the 2n Majorana generators satisfy g_j g_k + g_k g_j = 2 delta_jk
(the complex Clifford algebra on 2n generators); their 4^n ordered monomials have rank 4^n, so they
span all of End(C^(2^n)) and the module is irreducible; the vacuum is the unique state killed by
every a_i; the grades have dimensions C(n, k).
(2) Chirality: Gamma = prod (1 - 2 a_i^dag a_i) is diagonal with entry (-1)^|S|, squares to 1,
anticommutes with every g_j, and equals c g_0 g_1 ... g_{2n-1} with c = (-i)^n (the chirality element; g_{2i} g_{2i+1} = i (1 - 2 a_i^dag a_i)).
(3) Bogoliubov group: for rational orthogonal R in O(2n) (Cayley transforms of antisymmetric
matrices, and a reflection), g'_j = sum_k R_jk g_k satisfy the Clifford relations, while a
non-orthogonal R breaks them. Pin implements O: for a unit vector u, x -> -g_u x g_u^-1 sends
g_j to the reflection of g_j in u; a product of two such (Spin) implements the rotation
refl_u refl_w; the reflection is odd and reverses Gamma, the rotation even and keeps it.
(4) The number-preserving part: for g in U(n) with Gaussian-rational entries (n = 2, 3), the
operator Lambda(g), defined by Lambda(g)|S> = (g a^dag_{s1}) ... (g a^dag_{sk}) |0>, is unitary,
commutes with the number operator, satisfies Lambda(g) a_i^dag = (sum_j g_ji a_j^dag) Lambda(g),
multiplies the top state by det g; the induced real 2n x 2n matrix on the Majorana generators is
orthogonal and commutes with the complex structure.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
import fock
from GA import QI

ZERO, ONE, I = QI(0), QI(1), QI(0, 1)
G2 = [[QI(F(3, 5)), QI(0, F(4, 5))], [QI(0, F(4, 5)), QI(F(3, 5))]]
R3A = [[QI(F(3, 5)), QI(F(-4, 5)), ZERO], [QI(F(4, 5)), QI(F(3, 5)), ZERO], [ZERO, ZERO, ONE]]
P3 = [[QI(F(3, 5), F(4, 5)), ZERO, ZERO], [ZERO, QI(F(5, 13), F(-12, 13)), QI(0)], [ZERO, ZERO, ONE]]
B3 = [[ONE, ZERO, ZERO], [ZERO, QI(F(8, 17)), QI(0, F(15, 17))], [ZERO, QI(0, F(15, 17)), QI(F(8, 17))]]
ANTISYM = ([[0, 1, -2, 0], [-1, 0, 3, 1], [2, -3, 0, -1], [0, -1, 1, 0]],
           [[0, F(1, 2), 0, 2], [F(-1, 2), 0, 1, 0], [0, -1, 0, 3], [-2, 0, -3, 0]])
UNIT_U = (F(3, 5), F(4, 5), F(0), F(0))
UNIT_W = (F(0), F(5, 13), F(0), F(12, 13))


def zeros(d):
    return [[ZERO] * d for _ in range(d)]


def eye(d):
    return [[ONE if i == j else ZERO for j in range(d)] for i in range(d)]


def mm(A, B):
    d = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(d) if A[i][k] and B[k][j]), ZERO)
              for j in range(d)] for i in range(d)]


def add(A, B, c=ONE):
    return [[A[i][j] + c * B[i][j] for j in range(len(A))] for i in range(len(A))]


def sc(c, A):
    return [[c * x for x in row] for row in A]


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))


def anti(A, B):
    return add(mm(A, B), mm(B, A))


def annih(n):
    """a_0..a_{n-1} on n Jordan-Wigner modes, dense over GA.QI (LSB bitmask basis)."""
    return [fock.to_dense(fock.msc(ONE, fock.ann(i, n)), 2 ** n, ZERO) for i in range(n)]


def majoranas(a):
    out = []
    for ai in a:
        ad = dag(ai)
        out.append(add(ai, ad))
        out.append(sc(I, add(ad, ai, QI(-1))))
    return out


def flat(A):
    return [x for row in A for x in row]


def check_car_and_irreducible_spinor_module():
    ok = True
    for n in (1, 2, 3):
        d = 2 ** n
        a = annih(n)
        ok = ok and all(meq(anti(a[i], dag(a[j])), eye(d) if i == j else zeros(d))
                        and meq(anti(a[i], a[j]), zeros(d)) for i in range(n) for j in range(n))
        g = majoranas(a)
        ok = ok and len(g) == 2 * n
        ok = ok and all(meq(anti(g[j], g[k]), sc(QI(2 * int(j == k)), eye(d)))
                        for j in range(2 * n) for k in range(2 * n))
        mons = []
        for k in range(2 * n + 1):
            for S in combinations(range(2 * n), k):
                X = eye(d)
                for s in S:
                    X = mm(X, g[s])
                mons.append(flat(X))
        ok = ok and len(mons) == 4 ** n and GA.field_rank(mons) == 4 ** n
        stack = [row for ai in a for row in ai]
        ok = ok and d - GA.field_rank(stack) == 1
        grade_dims = [sum(1 for b in range(d) if bin(b).count("1") == k) for k in range(n + 1)]
        binom = [len(list(combinations(range(n), k))) for k in range(n + 1)]
        ok = ok and grade_dims == binom and sum(grade_dims) == d
    GA.check("Fock space of n <= 3 modes: CAR, Clifford relations on 2n Majoranas, irreducible (rank 4^n)", ok)
    return ok


def check_parity_grading_is_chirality():
    ok = True
    for n in (1, 2, 3):
        d = 2 ** n
        a = annih(n)
        g = majoranas(a)
        Gam = eye(d)
        for ai in a:
            Gam = mm(Gam, add(eye(d), mm(dag(ai), ai), QI(-2)))
        ok = ok and all(Gam[b][c] == (QI((-1) ** bin(b).count("1")) if b == c else ZERO)
                        for b in range(d) for c in range(d))
        ok = ok and meq(mm(Gam, Gam), eye(d)) and all(meq(anti(Gam, x), zeros(d)) for x in g)
        top = eye(d)
        for x in g:
            top = mm(top, x)
        c = ONE
        for _ in range(n):
            c = c * QI(0, -1)
        ok = ok and meq(sc(c, top), Gam)
    GA.check("parity (-1)^|S| = (-i)^n g_0 ... g_{2n-1}: the chirality element, anticommuting with each g_j", ok)
    return ok


def rat_inverse(M):
    k = len(M)
    cols = [GA.field_solve([[F(x) for x in r] for r in M], [F(int(i == c)) for i in range(k)]) for c in range(k)]
    return [[cols[c][r] for c in range(k)] for r in range(k)]


def cayley(K):
    k = len(K)
    Id = [[F(int(i == j)) for j in range(k)] for i in range(k)]
    minus = [[Id[i][j] - F(K[i][j]) for j in range(k)] for i in range(k)]
    plus = [[Id[i][j] + F(K[i][j]) for j in range(k)] for i in range(k)]
    return GA.mat_mul(minus, rat_inverse(plus))


def combo(coeffs, g):
    out = zeros(len(g[0]))
    for c, x in zip(coeffs, g):
        if c:
            out = add(out, x, QI(c))
    return out


def clifford_ok(gs, d):
    m = len(gs)
    return all(meq(anti(gs[j], gs[k]), sc(QI(2 * int(j == k)), eye(d))) for j in range(m) for k in range(m))


def check_orthogonal_group_preserves_car_and_pin_implements_it():
    ok = True
    n, d = 2, 4
    g = majoranas(annih(n))
    for K in ANTISYM:
        R = cayley(K)
        ok = ok and GA.mat_mul(R, [list(r) for r in zip(*R)]) == [[F(int(i == j)) for j in range(4)] for i in range(4)]
        ok = ok and clifford_ok([combo(R[j], g) for j in range(4)], d)
    bad = [[F(2), F(0), F(0), F(0)], [F(0), F(1), F(0), F(0)], [F(0), F(0), F(1), F(0)], [F(0), F(1), F(0), F(1)]]
    ok = ok and not clifford_ok([combo(bad[j], g) for j in range(4)], d)

    def refl(u):
        return [[F(int(i == j)) - 2 * u[i] * u[j] for j in range(4)] for i in range(4)]

    gu, gw = combo(UNIT_U, g), combo(UNIT_W, g)
    ok = ok and meq(mm(gu, gu), eye(d)) and meq(mm(gw, gw), eye(d))
    Ru = refl(UNIT_U)
    for j in range(4):
        image = sc(QI(-1), mm(mm(gu, g[j]), gu))          # gu^-1 = gu
        ok = ok and meq(image, combo([Ru[k][j] for k in range(4)], g))
    S = mm(gu, gw)
    Sinv = mm(gw, gu)
    ok = ok and meq(mm(S, Sinv), eye(d))
    Rot = GA.mat_mul(Ru, refl(UNIT_W))
    for j in range(4):
        ok = ok and meq(mm(mm(S, g[j]), Sinv), combo([Rot[k][j] for k in range(4)], g))
    Gam = mm(mm(g[0], g[1]), mm(g[2], g[3]))
    ok = ok and meq(mm(gu, Gam), sc(QI(-1), mm(Gam, gu))) and meq(mm(S, Gam), mm(Gam, S))
    GA.check("O(2n) preserves the CAR; Pin implements reflections, Spin the rotations (n = 2)", ok)
    return ok


def det(M):
    k = len(M)
    if k == 1:
        return M[0][0]
    out = ZERO
    for j in range(k):
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        term = M[0][j] * det(minor)
        out = out + term if j % 2 == 0 else out - term
    return out


def lam(gm, a):
    """Lambda(g) on Fock space, column |S> = (g a^dag_{s1}) ... (g a^dag_{sk}) |0>."""
    n = len(gm)
    d = 2 ** n
    ad = [dag(x) for x in a]
    A = [zeros(d) for _ in range(n)]
    for s in range(n):
        for t in range(n):
            A[s] = add(A[s], ad[t], gm[t][s])
    L = zeros(d)
    for b in range(d):
        S = [i for i in range(n) if b >> i & 1]
        v = [ONE if r == 0 else ZERO for r in range(d)]
        for s in reversed(S):
            v = [sum((A[s][r][c] * v[c] for c in range(d) if v[c]), ZERO) for r in range(d)]
        for r in range(d):
            L[r][b] = v[r]
    return L


def check_unitary_group_is_number_preserving_part():
    ok = True
    gms = [G2, mm(mm(R3A, P3), B3)]
    for gm in gms:
        n = len(gm)
        d = 2 ** n
        ok = ok and meq(mm(dag(gm), gm), eye(n))
        a = annih(n)
        ad = [dag(x) for x in a]
        L = lam(gm, a)
        ok = ok and meq(mm(dag(L), L), eye(d))
        Nop = zeros(d)
        for i in range(n):
            Nop = add(Nop, mm(ad[i], a[i]))
        ok = ok and meq(mm(L, Nop), mm(Nop, L))
        for i in range(n):
            rhs = zeros(d)
            for j in range(n):
                rhs = add(rhs, ad[j], gm[j][i])
            ok = ok and meq(mm(L, ad[i]), mm(rhs, L))
        ok = ok and L[d - 1][d - 1] == det(gm) and L[0][0] == ONE
        g = majoranas(a)
        tr0 = QI(d)
        R = []
        for j in range(2 * n):
            gj_new = mm(mm(L, g[j]), dag(L))
            row = []
            for k in range(2 * n):
                t = sum((mm(gj_new, g[k])[r][r] for r in range(d)), ZERO) / tr0
                ok = ok and t.im == 0
                row.append(t.re)
            R.append(row)
        ok = ok and GA.mat_mul(R, [list(r) for r in zip(*R)]) == [[F(int(i == j)) for j in range(2 * n)] for i in range(2 * n)]
        Jc = [[F(0)] * (2 * n) for _ in range(2 * n)]
        for i in range(n):
            Jc[2 * i + 1][2 * i] = F(1)
            Jc[2 * i][2 * i + 1] = F(-1)
        ok = ok and GA.mat_mul(R, Jc) == GA.mat_mul(Jc, R)
    GA.check("U(n) acts as Lambda(g): unitary, number-preserving, implementing g, det g on the top state", ok)
    return ok
