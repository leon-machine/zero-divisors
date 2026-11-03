"""synthesis.boundary-mode-premises-finite-models: exact checks.

Finite boundary-mode models: n fermion modes (integer Jordan-Wigner matrices), integer
weights w_k (in units of kappa), a density matrix whose entries are exact rational functions
(GA.RF) of one symbol u standing for exp(-2 pi) = exp(-beta kappa), so a mode of weight
kappa k has Boltzmann factor u^k.  No exponential or logarithm is evaluated.

(Q)   the (Q) window k = -1, 0, 1: the product Gibbs state is even, stationary under the
      Killing flow H0 = sum k N_k, Wick-factorised, and its single-mode marginals are KMS
      at the period (full single-mode reading: <v> = 0 and <v* v> = u^k <v v*>).
odd resonance: every H0-stationary operator is even exactly when no odd signed resonance
      exists; commutant dimensions for several weight sets, and the predicate is tested
      against the commutant on all 3-element weight sets from -3..3 and 4-element sets
      from 1..6.
not-P model A on (Q) weights 0, 1 and model B on positive weights 1, 2, 3: positive,
      stationary, Gibbs marginals, odd.
not-R model: the (Q) window at the doubled period u^2.
not-L_E model: the pairing v_1 v_{-1} + h.c. and a weight-conserving quartic hop commute
      with H0 and with the (Q) state and are not number-diagonal; the quadratic stationary
      generators of the (Q) state on the window -2..2 are exactly the N_k and the +-k pairings.
not-Q model: Gibbs marginals plus a density-density correlation.
chains (2): a rational pairing rotation fixes the (Q) state and moves a member of the class C
      (even, Gibbs marginals) out of C.
"""
from fractions import Fraction as Fr
from itertools import combinations, product
from collections import defaultdict
import GA
import fock
from GA import RF
from tp_premise import premise

PREMISES = (
    "hawking.imported-quasi-free-states-car-algebra",
    "singularity.kms-uniqueness-factor",
    "singularity.chains-state-class-stability",
)

R0, R1 = RF.const(0), RF.const(1)
U = RF.var()


def upow(k):
    out = R1
    base = U if k >= 0 else R1 / U
    for _ in range(abs(k)):
        out = out * base
    return out


# ---------------- exact matrix kit over RF ----------------
def zeros(n):
    return [[R0] * n for _ in range(n)]


def eye(n):
    m = zeros(n)
    for i in range(n):
        m[i][i] = R1
    return m


def mm(a, b):
    n = len(a)
    out = zeros(n)
    for i in range(n):
        for t in range(n):
            x = a[i][t]
            if x.is_zero():
                continue
            bt = b[t]
            for j in range(n):
                y = bt[j]
                if not y.is_zero():
                    out[i][j] = out[i][j] + x * y
    return out


def madd(a, b, s=1):
    sc = RF.const(s)
    return [[a[i][j] + sc * b[i][j] for j in range(len(a))] for i in range(len(a))]


def mscal(c, a):
    return [[c * x for x in row] for row in a]


def comm(a, b):
    return madd(mm(a, b), mm(b, a), -1)


def is_zero(a):
    return all(x.is_zero() for row in a for x in row)


def tr(a):
    s = R0
    for i in range(len(a)):
        s = s + a[i][i]
    return s


def dag(a):
    # every matrix here is real
    return [list(r) for r in zip(*a)]


def kron(a, b):
    n, m = len(a), len(b)
    out = zeros(n * m)
    for i in range(n):
        for j in range(n):
            if a[i][j].is_zero():
                continue
            for k in range(m):
                for l in range(m):
                    out[i * m + k][j * m + l] = a[i][j] * b[k][l]
    return out


def small(rows):
    return [[RF.const(x) for x in r] for r in rows]


Z2 = small([[1, 0], [0, -1]])
X2 = small([[0, 1], [1, 0]])


# Fock operators from lib/fock.py in MSB order (mode 0 is the leftmost tensor factor, occupation
# basis |0>, |1>, Jordan-Wigner sign from the lower-labelled modes), made dense over RF.
def ann(i, n):
    return small(fock.to_dense(fock.ann(i, n, fock.MSB), 2 ** n))


def parity(n):
    return small(fock.to_dense(fock.parity(n), 2 ** n))


def bits_of(idx, n):
    return fock.occ(idx, n, fock.MSB)


def index_of(bits):
    return fock.idx(bits, fock.MSB)


def gibbs(weights, scale=1):
    n = len(weights)
    pops = [upow(scale * sum(w * b for w, b in zip(weights, bits_of(i, n)))) for i in range(2 ** n)]
    Zs = R0
    for p in pops:
        Zs = Zs + p
    rho = zeros(2 ** n)
    for i, p in enumerate(pops):
        rho[i][i] = p / Zs
    return rho


def h0(weights):
    n = len(weights)
    H = zeros(2 ** n)
    for i, w in enumerate(weights):
        a = ann(i, n)
        H = madd(H, mscal(RF.const(w), mm(dag(a), a)))
    return H


def expect(rho, X):
    return tr(mm(rho, X))


def marginal_kms(rho, i, n, w, scale=1):
    """(R) read in full on mode i: <v> = <v*> = 0 and <v* v> = u^(scale w) <v v*>."""
    a = ann(i, n)
    ad = dag(a)
    return (expect(rho, a).is_zero() and expect(rho, ad).is_zero()
            and (expect(rho, mm(ad, a)) - upow(scale * w) * expect(rho, mm(a, ad))).is_zero())


def comb(n, k):
    c = Fr(1)
    for i in range(k):
        c = c * (n - i) / (i + 1)
    return c


def poly_positive_open_unit(p):
    """sufficient certificate: the Bernstein coefficients of p on [0, 1] are all >= 0 and not
    all zero, so p > 0 on the open interval (0, 1)."""
    p = [Fr(c) for c in p]
    d = len(p) - 1
    if d < 0:
        return False
    b = [sum((comb(k, i) / comb(d, i) * p[i] for i in range(k + 1)), Fr(0)) for k in range(d + 1)]
    return all(x >= 0 for x in b) and any(x > 0 for x in b)


def positive_on_unit_interval(r):
    """r > 0 for 0 < u < 1 (u = exp(-2 pi) lies there): numerator and denominator have the
    same strict sign there, each certified by Bernstein coefficients."""
    num, den = r.num, r.den
    if not num or not den:
        return False
    if poly_positive_open_unit(num) and poly_positive_open_unit(den):
        return True
    return poly_positive_open_unit([-c for c in num]) and poly_positive_open_unit([-c for c in den])


def eigen_ok(rho, vecs):
    """each integer vector is an eigenvector with an eigenvalue positive on (0,1), and the
    vectors are as many as the dimension and linearly independent: rho is positive definite."""
    n = len(rho)
    for v in vecs:
        rv = [sum((rho[i][j] * RF.const(v[j]) for j in range(n)), R0) for i in range(n)]
        piv = next(i for i in range(n) if v[i] != 0)
        lam = rv[piv] / RF.const(v[piv])
        if not all((rv[i] - lam * RF.const(v[i])).is_zero() for i in range(n)):
            return False
        if not positive_on_unit_interval(lam):
            return False
    return len(vecs) == n and GA.rank_of_vectors([[Fr(x) for x in v] for v in vecs]) == n


# ---------------- expected values ----------------
def rf(num, den):
    return RF([Fr(x) for x in num], [Fr(x) for x in den])


def same(r, num, den):
    return (r - rf(num, den)).is_zero()


# ---------------- (i) (Q) contains (P) and (R); (G) gives (P) ----------------
def check_q_contains_p_and_r():
    premise("hawking.imported-quasi-free-states-car-algebra")
    premise("singularity.kms-uniqueness-factor")
    W = [-1, 0, 1]
    n = 3
    rq = gibbs(W)
    a = [ann(i, n) for i in range(n)]
    N = [mm(dag(x), x) for x in a]
    assert (tr(rq) - R1).is_zero()
    assert is_zero(comm(rq, parity(n)))                          # (P)
    assert is_zero(comm(rq, h0(W)))                              # stationary
    assert all(marginal_kms(rq, i, n, W[i]) for i in range(n))   # (R), full reading
    occ = [expect(rq, x) for x in N]
    assert same(occ[0], [1], [1, 1]) and same(occ[1], [1], [2]) and same(occ[2], [0, 1], [1, 1])
    for i, j in combinations(range(n), 2):
        assert (expect(rq, mm(N[i], N[j])) - occ[i] * occ[j]).is_zero()   # Wick
        assert expect(rq, mm(dag(a[i]), a[j])).is_zero()                  # no hopping data
        assert expect(rq, mm(a[i], a[j])).is_zero()                       # no pairing data
    # (G): the modular state is the Gibbs state of K_geo, which commutes with the grading
    for Wg in ([1, 2, 4], [2, 3, 7]):
        assert is_zero(comm(gibbs(Wg), parity(3)))


# ---------------- (ii) odd resonance ----------------
def commutant_dims(W):
    n = len(W)
    blocks = defaultdict(lambda: [0, 0])
    for idx in range(2 ** n):
        b = bits_of(idx, n)
        blocks[sum(w * x for w, x in zip(W, b))][sum(b) % 2] += 1
    full = sum((d0 + d1) ** 2 for d0, d1 in blocks.values())
    even = sum(d0 * d0 + d1 * d1 for d0, d1 in blocks.values())
    return full, even


def has_odd_resonance(W):
    n = len(W)
    for size in range(1, n + 1, 2):
        for T in combinations(range(n), size):
            for signs in product((1, -1), repeat=size):
                if sum(s * W[t] for s, t in zip(signs, T)) == 0:
                    return True
    return False


def check_odd_resonance_criterion():
    premise("singularity.kms-uniqueness-factor")
    assert commutant_dims([1, 2, 4]) == (8, 8)
    assert commutant_dims([1, 2, 3]) == (10, 8)
    assert commutant_dims([-1, 0, 1]) == (24, 12)
    assert commutant_dims([-2, -1, 0, 1, 2]) == (176, 88)
    assert commutant_dims([1, 3, 5, 7]) == (18, 18)
    assert has_odd_resonance([1, 2, 3]) and has_odd_resonance([0, 5, 9])
    assert not has_odd_resonance([1, 2, 4]) and not has_odd_resonance([1, 3, 5, 7])
    tested = resonant = 0
    for W in list(combinations(range(-3, 4), 3)) + list(combinations(range(1, 7), 4)):
        full, even = commutant_dims(list(W))
        assert (full != even) == has_odd_resonance(list(W))
        tested += 1
        resonant += full != even
    assert tested == 50 and resonant == 39


# ---------------- (iii) not (P) ----------------
def check_not_p_models():
    premise("singularity.kms-uniqueness-factor")
    premise("hawking.imported-quasi-free-states-car-algebra")
    # model A: (Q) weights 0 and 1, odd coherence X_0 Z_1 on the Gibbs state
    n, W = 2, [0, 1]
    X = kron(X2, Z2)
    rho = madd(gibbs(W), mscal(rf([0, 1], [4, 4]), X))
    assert (tr(rho) - R1).is_zero() and is_zero(comm(rho, h0(W)))
    assert all(marginal_kms(rho, i, n, W[i]) for i in range(n))
    assert not is_zero(comm(rho, parity(n)))
    assert same(expect(rho, X), [0, 1], [1, 1])
    vecs = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, -1, 0], [0, 1, 0, -1]]
    assert eigen_ok(rho, vecs)
    lams = []
    for v in vecs:
        rv = [sum((rho[i][j] * RF.const(v[j]) for j in range(4)), R0) for i in range(4)]
        k = next(i for i in range(4) if v[i])
        lams.append(rv[k] / RF.const(v[k]))
    assert same(lams[0], [2, 1], [4, 4]) and same(lams[1], [0, 1], [4, 4])
    assert same(lams[2], [2, -1], [4, 4]) and same(lams[3], [0, 3], [4, 4])
    # model B: positive weights 1, 2, 3, coherence between |110> and |001> (energy 3 each)
    n, W = 3, [1, 2, 3]
    g = gibbs(W)
    s, t = index_of([1, 1, 0]), index_of([0, 0, 1])
    assert (s, t) == (6, 1) and (g[s][s] - g[t][t]).is_zero()
    E = zeros(8)
    E[s][t] = R1
    E[t][s] = R1
    rhoB = madd(g, mscal(g[s][s] / RF.const(2), E))
    a = [ann(i, n) for i in range(n)]
    assert (tr(rhoB) - R1).is_zero() and is_zero(comm(rhoB, h0(W)))
    assert all(marginal_kms(rhoB, i, n, W[i]) for i in range(n))
    assert not is_zero(comm(rhoB, parity(n)))
    assert same(expect(rhoB, mm(dag(a[2]), mm(a[1], a[0]))), [0, 0, 0, 1], [2, 2, 2, 4, 2, 2, 2])
    vecs = []
    for i in range(8):
        if i not in (s, t):
            v = [0] * 8
            v[i] = 1
            vecs.append(v)
    for sg in (1, -1):
        v = [0] * 8
        v[s] = 1
        v[t] = sg
        vecs.append(v)
    assert eigen_ok(rhoB, vecs)


# ---------------- (iv) not (R) ----------------
def check_not_r_model():
    premise("hawking.imported-quasi-free-states-car-algebra")
    W = [-1, 0, 1]
    n = 3
    r2 = gibbs(W, scale=2)
    a = [ann(i, n) for i in range(n)]
    assert is_zero(comm(r2, h0(W))) and is_zero(comm(r2, parity(n)))
    assert all(marginal_kms(r2, i, n, W[i], scale=2) for i in range(n))
    assert [marginal_kms(r2, i, n, W[i]) for i in range(n)] == [False, True, False]
    occ = [expect(r2, mm(dag(x), x)) for x in a]
    assert same(occ[0], [1], [1, 0, 1]) and same(occ[1], [1], [2]) and same(occ[2], [0, 0, 1], [1, 0, 1])
    for i, j in combinations(range(n), 2):
        assert expect(r2, mm(dag(a[i]), a[j])).is_zero() and expect(r2, mm(a[i], a[j])).is_zero()


# ---------------- (v) not (L_E) ----------------
def check_not_le_model():
    premise("hawking.imported-quasi-free-states-car-algebra")
    W = [-1, 0, 1]
    n = 3
    rq = gibbs(W)
    a = [ann(i, n) for i in range(n)]
    N = [mm(dag(x), x) for x in a]
    H = h0(W)
    G = madd(mm(a[2], a[0]), dag(mm(a[2], a[0])))          # pairing of k = +1 and k = -1
    assert is_zero(madd(G, dag(G), -1)) and is_zero(comm(G, H)) and is_zero(comm(G, rq))
    assert not is_zero(comm(G, N[2])) and is_zero(comm(G, parity(n)))
    hop = madd(mm(dag(a[2]), a[0]), mm(dag(a[0]), a[2]))
    assert not is_zero(comm(hop, rq))                        # quadratic hopping is not stationary
    # quartic hop on the window -1, 0, 1, 2: v_2* v_{-1}* v_1 v_0, weights 2 - 1 = 1 + 0
    W4 = [-1, 0, 1, 2]
    b = [ann(i, 4) for i in range(4)]
    q4 = mm(dag(b[3]), mm(dag(b[0]), mm(b[2], b[1])))
    Q4 = madd(q4, dag(q4))
    assert not is_zero(Q4)
    assert is_zero(comm(Q4, h0(W4))) and is_zero(comm(Q4, gibbs(W4)))
    assert not is_zero(comm(Q4, mm(dag(b[3]), b[3]))) and is_zero(comm(Q4, parity(4)))
    Ntot = zeros(16)
    for x in b:
        Ntot = madd(Ntot, mm(dag(x), x))
    assert is_zero(comm(Q4, Ntot))
    # quadratic monomials on the window -2..2 with ad(H0) eigenvalue zero
    W5 = [-2, -1, 0, 1, 2]
    zero_hops = [(i, j) for i in range(5) for j in range(5) if W5[i] - W5[j] == 0]
    zero_pairs = [(i, j) for i, j in combinations(range(5), 2) if W5[i] + W5[j] == 0]
    assert zero_hops == [(i, i) for i in range(5)] and zero_pairs == [(0, 4), (1, 3)]
    c5 = [ann(i, 5) for i in range(5)]
    H5 = h0(W5)
    for (i, j) in [(0, 4), (1, 3), (1, 2)]:
        P2 = mm(c5[i], c5[j])
        assert is_zero(madd(comm(H5, P2), mscal(RF.const(W5[i] + W5[j]), P2)))


# ---------------- (vi) not (Q) ----------------
def check_not_q_model():
    premise("singularity.chains-state-class-stability")
    n, W = 2, [1, 2]
    g = gibbs(W)
    cQ = g[3][3] / RF.const(2)
    rho = madd(g, mscal(cQ, kron(Z2, Z2)))
    a = [ann(i, n) for i in range(n)]
    N = [mm(dag(x), x) for x in a]
    assert (tr(rho) - R1).is_zero() and is_zero(comm(rho, parity(n)))
    assert all(marginal_kms(rho, i, n, W[i]) for i in range(n))
    assert is_zero(comm(rho, mm(N[0], N[1]))) and is_zero(comm(rho, h0(W)))
    conn = expect(rho, mm(N[0], N[1])) - expect(rho, N[0]) * expect(rho, N[1])
    assert same(conn, [0, 0, 0, 1], [2, 2, 2, 2])
    assert all(positive_on_unit_interval(rho[i][i]) for i in range(4))


# ---------------- (vii) chains (2) needs the pairing clause ----------------
def check_chains_needs_pairing_clause():
    premise("singularity.chains-state-class-stability")
    W = [-1, 0, 1]
    n = 3
    rq = gibbs(W)
    a = [ann(i, n) for i in range(n)]
    N = [mm(dag(x), x) for x in a]
    A = mm(dag(a[2]), dag(a[0]))
    Gen = madd(A, dag(A), -1)
    G2 = mm(Gen, Gen)
    assert is_zero(madd(mm(G2, Gen), Gen))                     # Gen^3 = -Gen
    cs, sn = rf([3], [5]), rf([4], [5])
    Urot = madd(madd(eye(8), mscal(sn, Gen)), mscal(R1 - cs, G2))
    assert is_zero(madd(mm(Urot, dag(Urot)), eye(8), -1))
    assert is_zero(comm(Urot, rq))
    # a member of C: the (Q) state plus a pairing coherence |1 0 1><0 0 0| (zero mode empty)
    s, t = index_of([1, 0, 1]), index_of([0, 0, 0])
    assert (rq[s][s] - rq[t][t]).is_zero()
    rc = [row[:] for row in rq]
    cpl = rq[s][s] / RF.const(2)
    rc[s][t] = rc[s][t] + cpl
    rc[t][s] = rc[t][s] + cpl
    assert is_zero(comm(rc, parity(n)))
    assert all(marginal_kms(rc, i, n, W[i]) for i in range(n))
    moved = mm(Urot, mm(rc, dag(Urot)))
    assert not marginal_kms(moved, 2, n, W[2])
    shift = expect(moved, N[2]) - expect(rc, N[2])
    assert same(shift, [0, -6], [25, 50, 25])


if __name__ == "__main__":
    for f in (check_q_contains_p_and_r, check_odd_resonance_criterion, check_not_p_models,
              check_not_r_model, check_not_le_model, check_not_q_model,
              check_chains_needs_pairing_clause):
        f()
        print("ok", f.__name__)
