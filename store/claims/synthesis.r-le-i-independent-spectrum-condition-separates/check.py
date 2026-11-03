"""synthesis.r-le-i-independent-spectrum-condition-separates: exact checks (Fractions).

Two fermionic modes by Jordan-Wigner on C^2 x C^2 (real 4x4 matrices): a0 = s- x 1, a1 = sz x s-,
basis |n0 n1>. Killing flow of mode k at imaginary period: alpha(a_k) = a_k / q_k, alpha(a_k*) = q_k a_k*,
alpha(N_k) = N_k, where q_k = e^{-p w_k} is the Boltzmann factor of the period p = 2 pi / kappa.
(R) for mode k: omega(X alpha(Y)) = omega(Y X) for X, Y in {1, a_k, a_k*, N_k}.
(L_E): the generator commutes with N_0 and N_1.  (I): the channel map sends a_k to a_k.
(S): the state is the unique ground state of the generator.
Models:
  M1  H = w0 N0 + w1 N1, product Gibbs state, T = 1           : (R), (L_E), (I) hold
  M2  same H, Boulware vacuum |00>, T = 1                     : (L_E), (I), (S) hold; (R) fails
  M3  H_t = g[A(N0 + N1) + (a0* a1* + a1 a0)], A = (1-t^2)/(2t): (R), (I), (S) hold; (L_E) fails
  M4  M1 with T a rational beam splitter of the two channels   : (R), (L_E) hold; (I) fails
and the eigen-identity of M3 is checked as an identity of rational functions of t.
"""
import GA
import fock
from fractions import Fraction as F
from tp_premise import premise

Z = F(0)


mm = GA.mat_mul


def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def add(*Ms):
    return [[sum((M[i][j] for M in Ms), Z) for j in range(len(Ms[0][0]))] for i in range(len(Ms[0]))]


def sc(c, A):
    return [[F(c) * x for x in r] for r in A]


def tp(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def comm(A, B):
    return add(mm(A, B), sc(-1, mm(B, A)))


def tr(A):
    return sum((A[i][i] for i in range(len(A))), Z)


E4 = fock.to_dense(fock.eye(4), 4)
a = [fock.to_dense(fock.ann(k, 2, fock.MSB), 4) for k in range(2)]   # Jordan-Wigner, basis |n0 n1>, |1> -> |0>
ad = [tp(x) for x in a]
N = [mm(ad[k], a[k]) for k in range(2)]
ZERO4 = [[Z] * 4 for _ in range(4)]


def car_ok():
    ok = True
    for j in range(2):
        for k in range(2):
            ok &= eq(add(mm(a[j], ad[k]), mm(ad[k], a[j])), E4 if j == k else ZERO4)
            ok &= eq(add(mm(a[j], a[k]), mm(a[k], a[j])), ZERO4)
    return ok


def omega(rho, X):
    return tr(mm(rho, X))


def kms_mode(rho, k, q):
    """(R) for mode k at Boltzmann factor q, tested on all pairs from {1, a, a*, N}"""
    ops = [(E4, E4), (a[k], sc(1 / q, a[k])), (ad[k], sc(q, ad[k])), (N[k], N[k])]
    for X, _ in ops:
        for Y, aY in ops:
            if omega(rho, mm(X, aY)) != omega(rho, mm(Y, X)):
                return False
    return True


def le_holds(H):
    return all(eq(comm(H, N[k]), ZERO4) for k in range(2))


def gibbs_product(q0, q1):
    r0 = [[1 / (1 + q0), Z], [Z, q0 / (1 + q0)]]
    r1 = [[1 / (1 + q1), Z], [Z, q1 / (1 + q1)]]
    return kron(r0, r1)                    # diagonal: JW signs do not enter


def projector(v):
    n = sum((x * x for x in v), Z)
    return [[v[i] * v[j] / n for j in range(4)] for i in range(4)]


def unique_ground(H, v, E0):
    """H v = E0 v, and every eigenvalue on the orthogonal complement exceeds E0: (H - E0) is positive on
    v-perp, checked by an exact LDL^T (Sylvester) test of the compressed form"""
    if any(x != E0 * y for x, y in zip([sum((H[i][j] * v[j] for j in range(4)), Z) for i in range(4)], v)):
        return False
    # basis of v-perp by Gram-Schmidt over Q
    basis = []
    for e in [[F(int(i == j)) for j in range(4)] for i in range(4)]:
        w = list(e)
        for b in [v] + basis:
            c = sum((w[i] * b[i] for i in range(4)), Z) / sum((b[i] * b[i] for i in range(4)), Z)
            w = [w[i] - c * b[i] for i in range(4)]
        if any(x != 0 for x in w):
            basis.append(w)
    assert len(basis) == 3
    Hs = add(H, sc(-E0, E4))
    G = [[sum((basis[i][p] * Hs[p][q2] * basis[j][q2] for p in range(4) for q2 in range(4)), Z)
          for j in range(3)] for i in range(3)]
    sig = GA.congruence_signature(G)
    return tuple(sig)[:2] == (3, 0) if isinstance(sig, tuple) else sig == (3, 0, 0)


def check_four_models_independence():
    premise("angle.within-supplied-class-spectrum-condition-selects")
    assert car_ok()
    w0, w1 = F(1), F(2)
    H = add(sc(w0, N[0]), sc(w1, N[1]))
    for (q0, q1) in [(F(1, 4), F(1, 9)), (F(2, 3), F(1, 7))]:
        # M1: all three hold, and the state is stationary
        rho = gibbs_product(q0, q1)
        assert tr(rho) == 1 and le_holds(H) and eq(comm(H, rho), ZERO4)
        assert kms_mode(rho, 0, q0) and kms_mode(rho, 1, q1)
        # M4: same state and dynamics; a rational beam splitter as exterior propagation
        c, s = F(3, 5), F(4, 5)
        out = [add(sc(c, a[0]), sc(s, a[1])), add(sc(-s, a[0]), sc(c, a[1]))]
        n_in = [omega(rho, N[k]) for k in range(2)]
        n_out = [omega(rho, mm(tp(o), o)) for o in out]
        assert n_out[0] == c * c * n_in[0] + s * s * n_in[1] != n_in[0]   # (I) fails
        assert n_out[0] + n_out[1] == n_in[0] + n_in[1]                     # occupation conserved
    assert n_out[0] == F(2, 5) * F(9, 25) + F(1, 8) * F(16, 25)          # pinned: q0 = 2/3, q1 = 1/7
    # M2: Boulware vacuum, unique ground state of H (w_k > 0), (R) fails at every q in (0,1)
    vac = [F(1), Z, Z, Z]
    rho2 = projector(vac)
    assert unique_ground(H, vac, Z)
    for q in [F(1, 2), F(1, 1000), F(999, 1000)]:
        assert not kms_mode(rho2, 0, q) and not kms_mode(rho2, 1, q)
        # the violation is on the pair (a, a*): q versus 0
        assert omega(rho2, mm(a[0], sc(q, ad[0]))) == q and omega(rho2, mm(ad[0], a[0])) == 0
    GA.check("M1 (R, L_E, I), M2 (not R; L_E, I, S), M4 (not I; R, L_E) realised exactly", True)


def check_pairing_ground_state_is_thermal_at_every_q():
    premise("angle.within-supplied-class-spectrum-condition-selects")
    premise("angle.hop-sea-filled-pairing")
    assert car_ok()
    P = add(mm(ad[0], ad[1]), mm(a[1], a[0]))           # pairing a0* a1* + a1 a0
    v11 = [sum((mm(ad[0], ad[1])[i][0],), Z) for i in range(4)]   # a0* a1* |00>
    assert v11 == [Z, Z, Z, F(1)]                          # |11> with this sign convention
    for (t, g, pinE) in [(F(1, 2), F(1), F(-1, 2)), (F(1, 3), F(3), F(-1)), (F(4, 5), F(5, 2), F(-2)),
                         (F(1, 10), F(1, 4), F(-1, 40))]:
        A = (1 - t * t) / (2 * t)
        Ht = sc(g, add(sc(A, add(N[0], N[1])), P))
        psi = [F(1), Z, Z, -t]                             # |00> - t |11>
        E0 = -g * t
        assert E0 == pinE
        assert unique_ground(Ht, psi, E0)                  # (S): unique ground state, with a gap
        assert not le_holds(Ht)                            # pairing: (L_E) fails
        rho = projector(psi)
        q = t * t
        assert kms_mode(rho, 0, q) and kms_mode(rho, 1, q)  # (R) at Boltzmann factor t^2
        assert omega(rho, N[0]) == q / (1 + q)
    # the eigen-identity for all t, as rational functions: even block [[0, g],[g, 2gA]] on (1, -t)
    t = GA.RF([0, 1])
    one = GA.RF([1])
    A = (one - t * t) / (GA.RF([0, 2]))
    row1 = t * GA.RF([-1])                                 # 0*1 + 1*(-t)
    row2 = one + GA.RF([2]) * A * (t * GA.RF([-1]))        # 1*1 + 2A*(-t)
    assert (row1 * GA.RF([-1]) - t).is_zero()                # first row: (-t) * 1, as computed above
    assert (row2 - t * t).is_zero()                        # = (-t) * (-t)
    # without uniqueness the exclusion fails: (N0 - N1)^2 is number-diagonal, its ground space holds
    # (4/5)|00> + (3/5)|11>, whose marginals are thermal (Boltzmann factor 9/16)
    Hd = mm(add(N[0], sc(-1, N[1])), add(N[0], sc(-1, N[1])))
    assert le_holds(Hd)
    psi_d = [F(4, 5), Z, Z, F(3, 5)]
    assert all(x == 0 for x in [sum((Hd[i][j] * psi_d[j] for j in range(4)), Z) for i in range(4)])
    assert not unique_ground(Hd, psi_d, Z)
    rho_d = projector(psi_d)
    assert kms_mode(rho_d, 0, F(9, 16)) and kms_mode(rho_d, 1, F(9, 16))
    # (I) with greybody loss: a vacuum-fed loss gives n0 -> |T00|^2 n0; the beam splitter's c^2 n0 + s^2 n1
    # is not of that form for any |T00| <= 1 when n1 > n0 (M4 pinned values below)
    n0, n1 = F(1, 5), F(1, 10)
    assert F(9, 25) * n0 + F(16, 25) * n1 != F(9, 25) * n0
    GA.check("for every t in (0,1) the pairing generator has the unique ground state |00> - t|11>, "
             "whose single-mode marginals are KMS at Boltzmann factor t^2: (R) and (S) without (L_E)", True)
