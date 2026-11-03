"""dark-energy.lift-inherits-no-go-steps-itemised: exact checks of the computable cores of steps (1) and (4).

Steps (2) (near-horizon reduction, assembly level) and (3) (the imported gauge-theory-gravity exactness) have no
finite core here and are not computed; their premises are not touched.
(1) Partial waves: the harmonic homogeneous polynomials of degree l = 0..4 in (x, y, z) (exact kernel of the
    Laplacian, dimension 2l + 1) are orthogonal across different l under the sphere average, computed exactly
    from <x^a y^b z^c> = (a-1)!!(b-1)!!(c-1)!!/(a+b+c+1)!! (all exponents even, else 0); within each l the Gram
    matrix is positive definite.
(4) Spin orthogonality: su(2) in the spin-1/2, 1, 3/2 irreps and in V_{1/2} (x) V_{1/2} (unnormalised basis,
    J_+ e_m = e_{m+1}, J_- e_{m+1} = (j - m)(j + m + 1) e_m, all rational). The adjoint Casimir splits End(V) into
    eigenspaces with eigenvalues l(l+1) and the hand-counted multiplicities; the invariant operators (the
    su(2)-invariant states and the singlets T) are the l = 0 space; for every invariant rho, singlet T and
    operator O of spin l >= 1, tr(rho T O) = 0, while tr(rho T) != 0 for rho = T = 1; operators of different spin
    are trace-orthogonal.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

DEGREES = range(5)


def dfact(n):
    out = 1
    while n > 1:
        out *= n
        n -= 2
    return out


def avg(mono):
    if any(e % 2 for e in mono):
        return F(0)
    a, b, c = mono
    return F(dfact(a - 1) * dfact(b - 1) * dfact(c - 1), dfact(a + b + c + 1))


def monos(l):
    return [(a, b, l - a - b) for a in range(l + 1) for b in range(l + 1 - a)]


def laplacian_matrix(l):
    src, dst = monos(l), monos(l - 2) if l >= 2 else []
    M = [[F(0)] * len(src) for _ in dst]
    for j, (a, b, c) in enumerate(src):
        for k, e in ((0, a), (1, b), (2, c)):
            if e >= 2:
                t = [a, b, c]
                t[k] -= 2
                M[dst.index(tuple(t))][j] += e * (e - 1)
    return src, M


def harmonics(l):
    src, M = laplacian_matrix(l)
    if not M:
        return [dict(zip(src, [F(1) if i == j else F(0) for i in range(len(src))])) for j in range(len(src))]
    return [dict(zip(src, v)) for v in GA.field_kernel(M)]


def inner(P, Q):
    tot = F(0)
    for m1, x in P.items():
        for m2, y in Q.items():
            if x and y:
                tot += x * y * avg(tuple(i + j for i, j in zip(m1, m2)))
    return tot


def spin_rep(two_j):
    d = two_j + 1
    ms = [F(-two_j, 2) + k for k in range(d)]
    jj = F(two_j, 2)
    Jp = [[F(1) if r == c + 1 else F(0) for c in range(d)] for r in range(d)]
    Jm = [[(jj - ms[c - 1]) * (jj + ms[c - 1] + 1) if r == c - 1 else F(0) for c in range(d)] for r in range(d)]
    Jz = [[ms[r] if r == c else F(0) for c in range(d)] for r in range(d)]
    return Jp, Jm, Jz


def mat(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def madd(A, B, c=1):
    return [[a + c * b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def br(A, B):
    return madd(mat(A, B), mat(B, A), -1)


def tensor_rep():
    a, b = spin_rep(1), spin_rep(1)
    return tuple(madd(kron(x, eye(2)), kron(eye(2), y)) for x, y in zip(a, b))


def casimir_spaces(J, lvals):
    Jp, Jm, Jz = J
    d = len(Jz)
    basis = []
    for i, j in product(range(d), range(d)):
        E = [[F(0)] * d for _ in range(d)]
        E[i][j] = F(1)
        basis.append(E)

    def cas(O):
        t1 = br(Jz, br(Jz, O))
        t2 = madd(br(Jp, br(Jm, O)), br(Jm, br(Jp, O)))
        return madd(t1, [[x / 2 for x in r] for r in t2])

    cols = [[x for r in cas(E) for x in r] for E in basis]
    spaces = {}
    for l2 in lvals:      # l2 = 2l
        ev = F(l2 * (l2 + 2), 4)
        M = [[cols[k][i] - (ev if i == k else 0) for k in range(d * d)] for i in range(d * d)]
        spaces[l2] = [[[v[i * d + j] for j in range(d)] for i in range(d)] for v in GA.field_kernel(M)]
    return spaces


def tr(A):
    return sum(A[i][i] for i in range(len(A)))


def check_partial_waves_diagonal():
    ok = True
    H = {l: harmonics(l) for l in DEGREES}
    ok = ok and all(len(H[l]) == 2 * l + 1 for l in DEGREES)
    for l1 in DEGREES:
        for l2 in DEGREES:
            G = [[inner(P, Q) for Q in H[l2]] for P in H[l1]]
            if l1 != l2:
                ok = ok and all(x == 0 for r in G for x in r)
            else:
                ok = ok and GA.congruence_signature(G) == (2 * l1 + 1, 0, 0)
    ok = ok and avg((2, 0, 0)) == F(1, 3) and avg((2, 2, 0)) == F(1, 15)
    GA.check("harmonics of different degree are orthogonal on the sphere: the angular integral is diagonal in l", ok)
    return ok


def check_spin_separates_from_singlet():
    premise("dark-energy.acoustic-no-go-one-way-grip")
    premise("dark-energy.imported-walls-sphere-theorem")
    cases = [(spin_rep(1), {0: 1, 2: 3}), (spin_rep(2), {0: 1, 2: 3, 4: 5}),
             (spin_rep(3), {0: 1, 2: 3, 4: 5, 6: 7}), (tensor_rep(), {0: 2, 2: 9, 4: 5})]
    ok = True
    for J, dims in cases:
        d = len(J[2])
        ok = ok and br(J[2], J[0]) == J[0] and br(J[0], J[1]) == [[2 * x for x in r] for r in J[2]]
        spaces = casimir_spaces(J, sorted(dims))
        ok = ok and {k: len(v) for k, v in spaces.items()} == dims and sum(dims.values()) == d * d
        inv = spaces[0]
        ok = ok and all(br(X, g) == [[F(0)] * d for _ in range(d)] for X in inv for g in J)
        for l2, ops in spaces.items():
            if l2 == 0:
                continue
            ok = ok and all(tr(mat(mat(rho, T), O)) == 0 for rho in inv for T in inv for O in ops)
            for l3, ops3 in spaces.items():
                if l3 != l2:
                    ok = ok and all(tr(mat(A, B)) == 0 for A in ops for B in ops3)
        ok = ok and tr(eye(d)) == d != 0
    GA.check("in an su(2)-invariant state a spin-l >= 1 operator has zero overlap with every singlet", ok)
    return ok
