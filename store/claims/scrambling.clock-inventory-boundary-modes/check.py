"""scrambling.clock-inventory-boundary-modes: exact checks.

Two exact models: GA.py's Cl(n,n) (real modes e_i, square +1, with adjoined partners f_i, square
-1; psi_i = (e_i + f_i)/2, psi_i^dag = (e_i - f_i)/2), and the Fock representation of n = 3 modes
as 8 x 8 rational matrices (Jordan-Wigner signs), where ad_X is computed by commutators on the
span of the 2n mode operators (coefficients by the trace pairing, span membership certified by
reassembly). Clock criterion: A = ad_X on the mode operators is nonzero and A^3 = t A with t > 0,
which is exactly "semisimple, real eigenvalues, nonzero ones of equal magnitude sqrt(t)"; unit
rapidity is t = 1.
(i)   In Cl(3,3), for every even blade of grade 2k and every vector, the commutator has grade 2k - 1
      or vanishes; for k = 2, 3 the map A_2k -> ([A_2k, e_a])_a is injective, and the even central
      elements are the scalars: only the bivector part of an even generator moves vectors.
(ii)  One completed pair, Cl(1,1): the bivector space is one-dimensional (e0 e1), its adjoint on
      vectors has eigenvalues +-2 (a boost), and sigma/2 with sigma = psi^dag psi - psi psi^dag
      gives unit rapidity; with kappa = 1/(4M) the period 2 pi/kappa is 8 pi M.
(iii) Fock, n = 3: [E_ij, psi_k^dag] = delta_jk psi_i^dag and [E_ij, psi_k] = -delta_ik psi_j for all
      i, j, k. Clocks at t = 1: E_00, E_01 + E_10, sum E_ii, E_00 - E_11, and the pairing
      2 psi_0^dag psi_1^dag + (1/2) psi_1 psi_0; the pairing with cd = 4 is a clock at t = 4. Not
      clocks: E_01 - E_10 (A^3 = -A, compact), E_01 (A^2 = 0, nilpotent), E_00 + 2 E_11 (unequal
      magnitudes), E_00 + E_01 - E_10 (complex eigenvalues), E_00 + E_01 + E_11 (not semisimple).
      Pairing trichotomy: for c, d over a grid, A^3 = (cd) A exactly; clock iff cd > 0, compact
      (t < 0) iff cd < 0, nilpotent (A^2 = 0) iff cd = 0.
      In GA (Cl(3,3)): E_ij + E_ji = n_+ - n_- with n_+- = (1/2)(psi_i +- psi_j)^dag (psi_i +- psi_j)
      for the rotated modes, which obey the CAR after normalisation ({phi, phi^dag} = 2 before it);
      sigma_i = 2 E_ii - 1 squares to 1.
      Witt step: for the clocks sum E_ii, E_01 + E_10 and the pairings (c, d) = (2, 1/2), (3, 4/3)
      in Cl(3,3), the +c and -c eigenspaces of ad_X on vectors are isotropic, of equal dimension,
      mutually dual (nondegenerate pairing) and orthogonal to the kernel, as the extension
      argument needs. The bivector algebra of Cl(n,n) (n = 2, 3) has dimension n(2n - 1): gl(n)
      (the E_ij - delta_ij/2) gives n^2, the pairing sector n(n - 1), and together they span it.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

NF = 3
DIM = 1 << NF


CRE = [fock.to_dense(fock.cre(k, NF), DIM) for k in range(NF)]
ANN = [fock.to_dense(fock.ann(k, NF), DIM) for k in range(NF)]
OPS = CRE + ANN


mm = GA.mat_mul


def lc(*terms):
    n = len(terms[0][1])
    R = [[F(0)] * n for _ in range(n)]
    for c, Mx in terms:
        for a in range(n):
            for b in range(n):
                R[a][b] += F(c) * Mx[a][b]
    return R


def comm(A, B):
    return lc((1, mm(A, B)), (-1, mm(B, A)))


def E(i, j):
    return mm(CRE[i], ANN[j])


def P(i, j, c, d):
    return lc((c, mm(CRE[i], CRE[j])), (d, mm(ANN[j], ANN[i])))


def ad(X):
    """ad_X on span(OPS) as a 2n x 2n matrix, or None if a commutator leaves the span."""
    m = len(OPS)
    A = [[F(0)] * m for _ in range(m)]
    norm = F(DIM, 2)
    for j, O in enumerate(OPS):
        Y = comm(X, O)
        for k, Ok in enumerate(OPS):
            A[k][j] = sum(Ok[a][b] * Y[a][b] for a in range(DIM) for b in range(DIM)) / norm
        if lc(*[(A[k][j], OPS[k]) for k in range(m)]) != Y:
            return None
    return A


def clock_t(A):
    """t with A^3 = t A (A != 0), else None."""
    if all(x == 0 for r in A for x in r):
        return None
    A3 = mm(mm(A, A), A)
    i, j = next((i, j) for i in range(len(A)) for j in range(len(A)) if A[i][j] != 0)
    t = A3[i][j] / A[i][j]
    if A3 != [[t * x for x in r] for r in A]:
        return None
    return t


# ---- GA model --------------------------------------------------------------------------
def ga_modes(n):
    S = GA.sig(n, n)
    psi = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(n + i))) for i in range(n)]
    psd = [GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(n + i))) for i in range(n)]
    return S, psi, psd


def ga_ad_on_vectors(X, S, n):
    cols = []
    for a in range(2 * n):
        v = GA.gen(a)
        w = GA.sub(GA.mul(X, v, S), GA.mul(v, X, S))
        assert all(len(b) == 1 for b in w)
        cols.append([w.get((b,), F(0)) for b in range(2 * n)])
    return [[cols[j][i] for j in range(2 * n)] for i in range(2 * n)]


def check_intrinsic_flows_are_bivector_flows():
    premise("scrambling.imported-modes-modular-inventory")
    n = 6
    S = GA.sig(3, 3)
    blades = GA.all_blades(n)
    for B in blades:
        if len(B) % 2 or not B:
            continue
        for a in range(n):
            c = GA.sub(GA.mul({B: F(1)}, GA.gen(a), S), GA.mul(GA.gen(a), {B: F(1)}, S))
            assert all(len(b) == len(B) - 1 for b in c)
    for k in (2, 3):
        gk = [b for b in blades if len(b) == 2 * k]
        rows = []
        for a in range(n):
            imgs = [GA.sub(GA.mul({B: F(1)}, GA.gen(a), S), GA.mul(GA.gen(a), {B: F(1)}, S)) for B in gk]
            for b in blades:
                rows.append([im.get(b, F(0)) for im in imgs])
        assert GA.field_kernel(rows) == []
    ev = [b for b in blades if len(b) % 2 == 0]
    rows = []
    for a in range(n):
        imgs = [GA.sub(GA.mul({B: F(1)}, GA.gen(a), S), GA.mul(GA.gen(a), {B: F(1)}, S)) for B in ev]
        for b in blades:
            rows.append([im.get(b, F(0)) for im in imgs])
    ker = GA.field_kernel(rows)
    assert len(ker) == 1 and ker[0][ev.index(())] != 0 and sum(1 for x in ker[0] if x) == 1
    return True


def check_single_pair_is_the_boost():
    premise("hawking.modular-structure-completed-pair")
    premise("scrambling.imported-modes-modular-inventory")
    S, psi, psd = ga_modes(1)
    blades = GA.all_blades(2)
    assert [b for b in blades if len(b) == 2] == [(0, 1)]
    A = ga_ad_on_vectors({(0, 1): F(1)}, S, 1)
    assert mm(A, A) == [[F(4), F(0)], [F(0), F(4)]]          # eigenvalues +-2, real: a boost
    sigma = GA.sub(GA.mul(psd[0], psi[0], S), GA.mul(psi[0], psd[0], S))
    assert GA.mul(sigma, sigma, S) == {(): F(1)}
    As = ga_ad_on_vectors(GA.scal(F(1, 2), sigma), S, 1)
    assert mm(As, As) == [[F(1), F(0)], [F(0), F(1)]]        # unit rapidity
    kappa_M = F(1, 4)                                         # kappa = 1/(4M)
    assert F(2) / kappa_M == 8                                # beta = 2 pi / kappa = 8 pi M
    return True


def check_inventory_by_clock_criterion():
    premise("scrambling.boundary-mode-space-matrix")
    for i in range(NF):
        for j in range(NF):
            for k in range(NF):
                assert comm(E(i, j), CRE[k]) == (CRE[i] if j == k else lc((0, CRE[0])))
                assert comm(E(i, j), ANN[k]) == (lc((-1, ANN[j])) if i == k else lc((0, ANN[0])))
    clocks = [(E(0, 0), 1), (lc((1, E(0, 1)), (1, E(1, 0))), 1),
              (lc((1, E(0, 0)), (1, E(1, 1)), (1, E(2, 2))), 1),
              (lc((1, E(0, 0)), (-1, E(1, 1))), 1),
              (P(0, 1, 2, F(1, 2)), 1), (P(0, 1, 3, F(4, 3)), 4)]
    for X, t in clocks:
        A = ad(X)
        assert A is not None and clock_t(A) == t
    A = ad(lc((1, E(0, 1)), (-1, E(1, 0))))
    assert clock_t(A) == -1                                   # compact
    A = ad(E(0, 1))
    assert mm(A, A) == [[F(0)] * 6 for _ in range(6)] and clock_t(A) == 0     # nilpotent
    for X in (lc((1, E(0, 0)), (2, E(1, 1))), lc((1, E(0, 0)), (1, E(0, 1)), (-1, E(1, 0))),
              lc((1, E(0, 0)), (1, E(0, 1)), (1, E(1, 1)))):
        A = ad(X)
        assert A is not None and clock_t(A) is None
    return True


def check_pairing_trichotomy():
    premise("scrambling.boundary-mode-space-matrix")
    grid = [F(-2), F(-1, 2), F(0), F(1, 3), F(3)]
    kinds = {}
    for c in grid:
        for d in grid:
            if c == 0 and d == 0:
                continue
            A = ad(P(0, 2, c, d))
            A3 = mm(mm(A, A), A)
            assert A3 == [[c * d * x for x in r] for r in A]
            t = clock_t(A)
            if c * d > 0:
                kind = 'clock'
                assert t == c * d and t > 0
            elif c * d < 0:
                kind = 'compact'
                assert t < 0
            else:
                kind = 'nilpotent'
                assert mm(A, A) == [[F(0)] * 6 for _ in range(6)]
            kinds[kind] = kinds.get(kind, 0) + 1
    assert kinds == {'clock': 8, 'compact': 8, 'nilpotent': 8}
    A = ad(P(0, 2, F(3), F(1, 3)))
    assert clock_t(A) == 1                                    # cd = 1: unit rapidity outright
    return True


def check_rotated_modes_atom_boosts_and_so_nn():
    premise("scrambling.boundary-mode-space-matrix")
    premise("tower.witt-index-quantum-capacity")
    n = 3
    S, psi, psd = ga_modes(n)
    Eg = {(i, j): GA.mul(psd[i], psi[j], S) for i in range(n) for j in range(n)}
    one = GA.sc(1)
    for i in range(n):
        for j in range(n):
            if i == j:
                sig = GA.sub(GA.scal(2, Eg[(i, i)]), one)
                assert GA.eq(GA.mul(sig, sig, S), one)
                continue
            phis = [(GA.add(psi[i], psi[j]), GA.add(psd[i], psd[j])),
                    (GA.sub(psi[i], psi[j]), GA.sub(psd[i], psd[j]))]
            for (a, ad_) in phis:
                assert GA.eq(GA.add(GA.mul(a, ad_, S), GA.mul(ad_, a, S)), GA.sc(2))
            a0, b0 = phis[0][0], phis[1][1]
            assert GA.is_zero(GA.add(GA.mul(a0, b0, S), GA.mul(b0, a0, S)))
            n_p = GA.scal(F(1, 2), GA.mul(phis[0][1], phis[0][0], S))
            n_m = GA.scal(F(1, 2), GA.mul(phis[1][1], phis[1][0], S))
            assert GA.eq(GA.add(Eg[(i, j)], Eg[(j, i)]), GA.sub(n_p, n_m))
    for m in (2, 3):
        S2, ps, pd = ga_modes(m)
        blades = GA.all_blades(2 * m)
        rk = lambda xs: GA.rank_of_vectors([[x.get(b, F(0)) for b in blades] for x in xs])
        biv = [{b: F(1)} for b in blades if len(b) == 2]
        gl = [GA.sub(GA.mul(pd[i], ps[j], S2), GA.sc(F(1, 2)) if i == j else {}) for i in range(m) for j in range(m)]
        pair = [GA.mul(pd[i], pd[j], S2) for i in range(m) for j in range(i + 1, m)] + \
               [GA.mul(ps[j], ps[i], S2) for i in range(m) for j in range(i + 1, m)]
        assert all(len(b) == 2 for x in gl + pair for b in x)
        assert len(biv) == m * (2 * m - 1)
        assert rk(gl) == m * m and rk(pair) == m * (m - 1) and rk(gl + pair) == m * (2 * m - 1)
    return True


def check_witt_eigenspaces_isotropic_and_dual():
    premise("tower.witt-index-quantum-capacity")
    n = 3
    S, psi, psd = ga_modes(n)
    Eg = {(i, j): GA.mul(psd[i], psi[j], S) for i in range(n) for j in range(n)}

    def pairing(i, j, c, d):
        return GA.add(GA.scal(c, GA.mul(psd[i], psd[j], S)), GA.scal(d, GA.mul(psi[j], psi[i], S)))
    cases = [(GA.add(Eg[(0, 0)], Eg[(1, 1)], Eg[(2, 2)]), 1, 3),
             (GA.add(Eg[(0, 1)], Eg[(1, 0)]), 1, 2),
             (pairing(0, 1, F(2), F(1, 2)), 1, 2),
             (pairing(0, 2, F(3), F(4, 3)), 2, 2)]
    vecs = lambda k: GA.add(*[GA.scal(k[a], GA.gen(a)) for a in range(2 * n) if k[a]])
    for X, c, dim in cases:
        A = ga_ad_on_vectors(X, S, n)
        Ep = [vecs(k) for k in GA.field_kernel([[A[i][j] - (c if i == j else 0) for j in range(2 * n)] for i in range(2 * n)])]
        Em = [vecs(k) for k in GA.field_kernel([[A[i][j] + (c if i == j else 0) for j in range(2 * n)] for i in range(2 * n)])]
        E0 = [vecs(k) for k in GA.field_kernel(A)]
        assert len(Ep) == dim and len(Em) == dim and len(E0) == 2 * n - 2 * dim
        assert all(GA.dot(x, y, S) == 0 for x in Ep for y in Ep)
        assert all(GA.dot(x, y, S) == 0 for x in Em for y in Em)
        assert all(GA.dot(x, y, S) == 0 for x in Ep + Em for y in E0)
        gram = [[GA.dot(x, y, S) for y in Em] for x in Ep]
        assert GA.rank_of_vectors(gram) == dim
    return True
