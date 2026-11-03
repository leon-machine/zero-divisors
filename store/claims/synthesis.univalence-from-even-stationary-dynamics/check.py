"""synthesis.univalence-from-even-stationary-dynamics: exact checks.

  (1) In Cl(2n, 0) built with GA, n = 1, 2, 3, the grading is inner: conjugation by the volume
      element e_1 ... e_{2n}, which is the product of the mode-plane bivectors B_k = e_{2k-1} e_{2k}
      (the rotors of rotation by pi in every mode plane, R_k(pi) = -B_k), sends every generator to
      its negative; a single B_k negates exactly the two generators of its plane.
  (2) On the Fock space of three modes (Jordan-Wigner matrices over the integers), the parity
      Gamma = prod(1 - 2 N_k) commutes with an even Hamiltonian containing weights, hops and
      pairing terms, hence with every polynomial in it; a Gibbs state, a function of H, is even.
  (3) For H = sum w_k N_k the spectra on the even and odd sectors are disjoint exactly when no
      signed sum of an odd number of weights vanishes: disjoint for (1, 3, 5), (1, 2), (2, 2, 2);
      not for (1, 2, 3) (1 + 2 - 3 = 0) or (0, 1, 1) (a zero weight). When disjoint, Gamma is
      the Lagrange polynomial in H that takes the value of the parity on each eigenvalue.
  (4) Counter-states: for weights (1, 2, 3), rho = (1 + (x + x^*)/2)/8 with x = a_1 a_2 a_3^* commutes
      with H, is positive (x + x^* has square a projection P with (x + x^*) P = x + x^*), and does not
      commute with Gamma; for a zero-weight mode, (1 + sigma_x/2)/2 is stationary and not even.
"""
from fractions import Fraction as F
from itertools import combinations, product
import GA
import fock
from tp_premise import premise


# ---------- Clifford side ----------
def vec(i):
    return GA.gen(i)


def blade(idx):
    return {tuple(idx): F(1)}


def ad(g, x, sq):
    """g x g^{-1} for g a product of unit vectors with square +1 each (g^{-1} = reverse(g))"""
    return GA.mul(GA.mul(g, x, sq), GA.reverse(g), sq)


# ---------- Fock side ----------
def mm(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def madd(*Ms):
    n = len(Ms[0])
    return [[sum(M[i][j] for M in Ms) for j in range(n)] for i in range(n)]


def msc(c, A):
    return [[c * x for x in row] for row in A]


def tr(A):
    return [list(r) for r in zip(*A)]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def annihilators(n):
    """Jordan-Wigner: a_k = Z x ... x Z x s x 1 x ... x 1, s = [[0,1],[0,0]] on basis (|0>, |1>)"""
    return [fock.to_dense(fock.ann(k, n, fock.MSB), 2 ** n) for k in range(n)]


def comm(A, B):
    return madd(mm(A, B), msc(-1, mm(B, A)))


def is_zero(A):
    return all(x == 0 for row in A for x in row)


def parity(n):
    return fock.to_dense(fock.parity(n), 2 ** n)


def number_h(w):
    n = len(w)
    return fock.to_dense(fock.madd(*[fock.msc(wk, fock.num(k, n, fock.MSB)) for k, wk in enumerate(w)]), 2 ** n)


def sector_spectra(w):
    ev, od = set(), set()
    for r in range(len(w) + 1):
        for T in combinations(range(len(w)), r):
            (ev if r % 2 == 0 else od).add(sum(w[k] for k in T))
    return ev, od


def odd_signed_sum_vanishes(w):
    for r in range(1, len(w) + 1, 2):
        for S in combinations(range(len(w)), r):
            for eps in product((1, -1), repeat=r):
                if sum(e * w[k] for e, k in zip(eps, S)) == 0:
                    return True
    return False


def lagrange(H, values):
    """sum over eigenvalues lam of val(lam) prod_{mu != lam} (H - mu)/(lam - mu)"""
    n = len(H)
    out = [[F(0)] * n for _ in range(n)]
    for lam, val in values.items():
        P = eye(n)
        for mu in values:
            if mu != lam:
                P = mm(P, msc(F(1) / (lam - mu), madd(H, msc(-mu, eye(n)))))
        out = madd(out, msc(val, P))
    return out


# ---------- checks ----------
def check_grading_is_rotation_by_pi_in_every_mode_plane():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    for n in (1, 2, 3):
        sq = GA.sig(2 * n, 0)
        vol = blade(range(2 * n))
        prod_planes = {(): F(1)}
        for k in range(n):
            prod_planes = GA.mul(prod_planes, blade((2 * k, 2 * k + 1)), sq)
        assert GA.eq(prod_planes, vol)
        for i in range(2 * n):
            assert GA.eq(ad(vol, vec(i), sq), GA.neg(vec(i)))
        for k in range(n):
            Bk = blade((2 * k, 2 * k + 1))
            Rk = GA.neg(Bk)
            for i in range(2 * n):
                img = ad(Rk, vec(i), sq)
                assert GA.eq(img, GA.neg(vec(i)) if i // 2 == k else vec(i))
    # the even subalgebra is fixed: e_1 e_2 commutes with the volume element in Cl(4, 0)
    sq = GA.sig(4, 0)
    assert GA.eq(ad(blade(range(4)), blade((0, 2)), sq), blade((0, 2)))


def check_even_hamiltonian_commutes_with_parity():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    a = annihilators(3)
    ad_ = [tr(x) for x in a]
    for x, y in combinations(range(3), 2):
        assert is_zero(madd(mm(a[x], ad_[y]), mm(ad_[y], a[x])))
        assert is_zero(madd(mm(a[x], a[y]), mm(a[y], a[x])))
    G = parity(3)
    H = madd(number_h([F(2), F(-1, 3), F(5, 2)]),
             msc(F(3, 4), madd(mm(ad_[0], a[1]), mm(ad_[1], a[0]))),
             msc(F(-2, 7), madd(mm(ad_[1], ad_[2]), mm(a[2], a[1]))))
    assert is_zero(comm(G, H))
    # the generator is the one intended: pinned traces (hops and pairings are traceless)
    assert sum(H[i][i] for i in range(8)) == F(50, 3)
    assert sum(mm(H, H)[i][i] for i in range(8)) == F(102349, 1764)
    Hk = eye(8)
    for _ in range(4):
        Hk = mm(Hk, H)
        assert is_zero(comm(G, Hk))
    # an odd term breaks it
    Hodd = madd(H, msc(F(1, 2), madd(a[0], ad_[0])))
    assert not is_zero(comm(G, Hodd))


def check_stationary_states_even_iff_no_odd_resonance():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    cases = {(1, 3, 5): False, (1, 2): False, (2, 2, 2): False, (1, 2, 3): True, (0, 1, 1): True}
    for w, resonant in cases.items():
        ev, od = sector_spectra(w)
        assert odd_signed_sum_vanishes(w) == resonant
        assert (len(ev & od) > 0) == resonant
    for w in ((1, 3, 5), (1, 2)):
        wf = [F(x) for x in w]
        H = number_h(wf)
        ev, od = sector_spectra(w)
        values = {F(v): F(1) for v in ev}
        values.update({F(v): F(-1) for v in od})
        assert lagrange(H, values) == parity(len(w))


def check_counter_states_at_resonance_and_zero_weight():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    a = annihilators(3)
    H = number_h([F(1), F(2), F(3)])
    x = mm(mm(a[0], a[1]), tr(a[2]))
    X = madd(x, tr(x))
    assert not is_zero(X)
    P = mm(X, X)
    assert mm(P, P) == P and mm(X, P) == X
    rho = msc(F(1, 8), madd(eye(8), msc(F(1, 2), X)))
    assert is_zero(comm(rho, H))
    assert not is_zero(comm(rho, parity(3)))
    assert sum(rho[i][i] for i in range(8)) == 1
    # one mode of zero weight
    sx = [[F(0), F(1)], [F(1), F(0)]]
    rho1 = msc(F(1, 2), madd(eye(2), msc(F(1, 2), sx)))
    H1 = number_h([F(0)])
    G1 = parity(1)
    assert is_zero(comm(rho1, H1)) and not is_zero(comm(rho1, G1))
    assert rho1[0][1] == F(1, 4)
