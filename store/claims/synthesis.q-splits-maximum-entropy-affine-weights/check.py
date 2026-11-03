"""synthesis.q-splits-maximum-entropy-and-affine-weights: exact checks.

Everything is exact: integer Jordan-Wigner matrices and Fractions; no floating point.
Boltzmann factors are rational parameters: b stands for e^{beta c} (the slope) and D for
e^{beta d} (the sea offset), so n_k = 1/(D b^k + 1) is the Fermi symbol of the affine weight
omega_k = c k + d and no exponential is evaluated.

(i)   quasi-free part: on a 3-mode window the product sigma of Gibbs marginals is Gibbs for
      K = sum omega_k N_k, obeys Wick factorisation with diagonal two-point data, and has
      log sigma in span{1, N_k}; a correlated member rho = sigma + eps Y of the class C
      (same marginals, same diagonal two-point data, positive definite) violates Wick, is not
      Gibbs, and satisfies Tr(rho log sigma) = Tr(sigma log sigma), so that
      S(sigma) - S(rho) = D(rho || sigma).
(ii)  affine law: [diag(omega), S_m] is a multiple of the shift S_m for every m != 0 iff
      omega is affine (affine passes, three non-affine perturbations fail); the
      second-quantised commutator on a 4-mode window is the hat of the one-particle one.
(iii) Planck clause: n_{k+m}(1 - n_k) = (n_k - n_{k+m})/(b^m - 1) termwise, the finite-window
      sum telescopes to edge terms, and the edge error is bounded by a quantity that tends to
      zero, for three offsets D; the limit m/(b^m - 1) does not see D.
(iv)  particle-hole: the symbol is invariant under k -> -k at D = 1 (sea at a site) and under
      k -> -1-k at D^2 = b (sea between sites), and under neither for a generic offset; the
      one-particle generator diag(k) is mapped to itself by the reflection.
(v)   rotations: on C^W (x) C^n with the principal triple on C^n (n = 2, 3), diag(omega) (x) 1
      commutes with 1 (x) e, f, h; a diagonal generator commuting with 1 (x) e has weights
      independent of the magnetic index (solution space of dimension |W|); the placement of
      (Q) on one principal window, (kappa/2) h, does not commute with e; the second-quantised
      statement holds on a 4-mode Fock space.
"""
from fractions import Fraction as F
from itertools import product
import GA
import fock
from GA import rank_of_vectors, mat_mul, mat_eq
from tp_premise import premise

PREMISES = (
    "singularity.chains-state-class-stability",
    "singularity.deficit-carried-quanta-correlations",
    "singularity.deficit-theorem-cost-descent-exactly",
    "singularity.exact-equilibrium-over-determines-boundary-modes",
    "singularity.kms-uniqueness-factor",
    "hawking.imported-quasi-free-states-car-algebra",
    "singularity.bosonisation-bridge-s-wave-sector",
    "scrambling.boundary-mode-space-matrix",
    "scrambling.principality-indifference-sphere",
    "synthesis.residue-common-weight-particle-hole",
    "synthesis.residue-from-mode-entropy",
)


# ---------------- exact matrix kit ----------------
def zeros(r, c):
    return [[F(0)] * c for _ in range(r)]


def eye(n):
    m = zeros(n, n)
    for i in range(n):
        m[i][i] = F(1)
    return m


def add(a, b, s=1):
    return [[a[i][j] + s * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scal(c, a):
    return [[c * x for x in row] for row in a]


def mm(a, b):
    return mat_mul(a, b)


def comm(a, b):
    return add(mm(a, b), mm(b, a), -1)


def is_zero(a):
    return all(x == 0 for row in a for x in row)


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def kron(a, b):
    ra, ca, rb, cb = len(a), len(a[0]), len(b), len(b[0])
    out = zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            if a[i][j]:
                for k in range(rb):
                    for l in range(cb):
                        out[i * rb + k][j * cb + l] = a[i][j] * b[k][l]
    return out


def dag(a):
    return [list(r) for r in zip(*a)]   # real matrices: adjoint = transpose


# ---------------- Jordan-Wigner modes ----------------
def jw(n):
    """Dense annihilators c_0..c_{n-1}, mode 0 the leading tensor factor (fock MSB order)."""
    return [fock.to_dense(fock.ann(i, n, fock.MSB), 2 ** n) for i in range(n)]


def hat(X, cs):
    d = len(cs[0])
    out = zeros(d, d)
    for i in range(len(X)):
        for j in range(len(X)):
            if X[i][j]:
                out = add(out, scal(X[i][j], mm(dag(cs[i]), cs[j])))
    return out


def occ_bits(idx, n):
    return fock.occ(idx, n, fock.MSB)


def leading_minors_positive(a):
    # Gaussian elimination without pivoting: all pivots > 0 iff positive definite
    m = [list(r) for r in a]
    n = len(m)
    for c in range(n):
        if m[c][c] <= 0:
            return False
        for r in range(c + 1, n):
            f = m[r][c] / m[c][c]
            if f:
                m[r] = [x - f * y for x, y in zip(m[r], m[c])]
    return True


# ---------------- (i) quasi-free part ----------------
def check_quasi_free_part():
    for p in ("singularity.chains-state-class-stability",
              "singularity.deficit-carried-quanta-correlations",
              "singularity.deficit-theorem-cost-descent-exactly",
              "singularity.exact-equilibrium-over-determines-boundary-modes",
              "singularity.kms-uniqueness-factor",
              "hawking.imported-quasi-free-states-car-algebra"):
        premise(p)
    n = 3
    cs = jw(n)
    d = 2 ** n
    b = F(3)                       # e^{beta c}
    ks = [-1, 0, 1]                # array labels; weights omega_k = c k
    nk = [F(1) / (b ** k + 1) for k in ks]
    Ns = [mm(dag(c), c) for c in cs]
    # sigma = product of marginals diag(1 - n_k, n_k)
    sigma = zeros(d, d)
    for idx in range(d):
        bits = occ_bits(idx, n)
        v = F(1)
        for k in range(n):
            v *= nk[k] if bits[k] else 1 - nk[k]
        sigma[idx][idx] = v
    ok = tr(sigma) == 1
    # Gibbs for K = sum omega_k N_k: sigma_idx proportional to prod b^{-k occ_k}
    g = [F(1)] * d
    for idx in range(d):
        for k in range(n):
            if occ_bits(idx, n)[k]:
                g[idx] *= b ** (-ks[k])
    Z = sum(g)
    ok = ok and all(sigma[i][i] == g[i] / Z for i in range(d))
    # two-point data diagonal with entries n_k
    for i in range(n):
        for j in range(n):
            val = tr(mm(sigma, mm(dag(cs[i]), cs[j])))
            ok = ok and val == (nk[i] if i == j else 0)
    # Wick for the four-point functions <c_i^+ c_j^+ c_l c_k>

    def two(st, i, j):
        return tr(mm(st, mm(dag(cs[i]), cs[j])))

    def four(st, i, j, l, k):
        return tr(mm(st, mm(mm(dag(cs[i]), dag(cs[j])), mm(cs[l], cs[k]))))

    wick = True
    for i, j, l, k in product(range(n), repeat=4):
        lhs = four(sigma, i, j, l, k)
        rhs = two(sigma, i, k) * two(sigma, j, l) - two(sigma, i, l) * two(sigma, j, k)
        wick = wick and lhs == rhs
    ok = ok and wick
    # correlated member of C: rho = sigma + eps (N_0 - 1/2)(N_1 - 1/2)
    half = scal(F(1, 2), eye(d))
    Y = mm(add(Ns[0], half, -1), add(Ns[1], half, -1))
    eps = F(1, 10)
    rho = add(sigma, scal(eps, Y))
    ok = ok and tr(rho) == 1 and leading_minors_positive(rho)
    # same marginals (even, diagonal: <N_k>, odd one-point functions zero) and two-point data
    for k in range(n):
        ok = ok and tr(mm(rho, Ns[k])) == nk[k] and tr(mm(rho, cs[k])) == 0
    for i in range(n):
        for j in range(n):
            ok = ok and two(rho, i, j) == two(sigma, i, j)
    # rho violates Wick at <c_0^+ c_1^+ c_1 c_0> = <N_0 N_1>
    lhs = four(rho, 0, 1, 1, 0)
    rhs = two(rho, 0, 0) * two(rho, 1, 1) - two(rho, 0, 1) * two(rho, 1, 0)
    ok = ok and lhs != rhs
    # rho is not Gibbs for K (KMS state on a matrix factor is unique: it differs from sigma)
    ok = ok and rho != sigma
    # log sigma = sum_k [log(1 - n_k) 1 + log(n_k/(1 - n_k)) N_k]: sigma's diagonal factorises
    # bit by bit, so Tr(rho log sigma) = Tr(sigma log sigma) follows from equal <1>, <N_k>
    fact = all(sigma[idx][idx] ==
               _prod([nk[k] if occ_bits(idx, n)[k] else 1 - nk[k] for k in range(n)])
               for idx in range(d))
    ok = ok and fact and tr(rho) == tr(sigma)
    ok = ok and all(tr(mm(rho, Ns[k])) == tr(mm(sigma, Ns[k])) for k in range(n))
    GA.check("(i) product of (R) marginals: Gibbs, Wick, diagonal two-point; a correlated "
             "member of C with the same two-point data violates Wick; log sigma in span{1,N_k}", ok)
    return ok


def _prod(xs):
    out = F(1)
    for x in xs:
        out *= x
    return out


# ---------------- (ii) affine law ----------------
def shift(W, m):
    s = zeros(W, W)
    for k in range(W):
        if 0 <= k + m < W:
            s[k][k + m] = F(1)
    return s


def current_eigenvalues(omega):
    # the scalars lambda_m with [diag(omega), S_m] = lambda_m S_m, or None if some fails
    W = len(omega)
    Dg = zeros(W, W)
    for k in range(W):
        Dg[k][k] = omega[k]
    out = {}
    for m in range(-(W - 1), W):
        if m == 0:
            continue
        S = shift(W, m)
        Cm = comm(Dg, S)
        lam = Cm[0][m] if m > 0 else Cm[-m][0]
        if not is_zero(add(Cm, scal(lam, S), -1)):
            return None
        out[m] = lam
    return out


def currents_are_eigen(omega):
    W = len(omega)
    Dg = zeros(W, W)
    for k in range(W):
        Dg[k][k] = omega[k]
    for m in range(-(W - 1), W):
        if m == 0:
            continue
        S = shift(W, m)
        Cm = comm(Dg, S)
        # Cm = lambda S for one scalar lambda?
        lam = None
        for k in range(W):
            if 0 <= k + m < W:
                v = Cm[k][k + m]
                lam = v if lam is None else lam
                if v != lam:
                    return False
        if not is_zero(add(Cm, scal(lam, S), -1)):
            return False
    return True


# (ii) samples: affine weights c k + d0 on a W-mode window; three non-affine controls (one weight
# bumped, quadratic, a staggered offset); a LIE_N-mode window with weights 3k + LIE_OFFSET and shifts m.
AFFINE_W, AFFINE_C, AFFINE_D0 = 8, F(2), F(-7, 3)
NON_AFFINE = [
    [AFFINE_C * k + AFFINE_D0 + (1 if k == 3 else 0) for k in range(AFFINE_W)],
    [F(k * k) for k in range(AFFINE_W)],
    [AFFINE_C * k + (F(1, 2) if k % 2 else 0) for k in range(AFFINE_W)],
]
LIE_N, LIE_OFFSET = 4, -1
LIE_SHIFTS = (1, 2, -1)


def check_affine_law():
    premise("singularity.bosonisation-bridge-s-wave-sector")
    premise("scrambling.boundary-mode-space-matrix")
    W = AFFINE_W
    c, d0 = AFFINE_C, AFFINE_D0
    affine = [c * k + d0 for k in range(W)]
    ok = currents_are_eigen(affine)
    lams = current_eigenvalues(affine)
    ok = ok and lams is not None and len(lams) == 14
    ok = ok and lams[1] == -2 and lams[-3] == 6 and all(lams[m] == -c * m for m in lams)
    ok = ok and not any(currents_are_eigen(bad) for bad in NON_AFFINE)
    # second quantisation is a Lie map on a 4-mode window: [K^, a_m^] = ([h, S_m])^
    n = LIE_N
    cs = jw(n)
    omega = [F(3) * k + LIE_OFFSET for k in range(n)]
    h = zeros(n, n)
    for k in range(n):
        h[k][k] = omega[k]
    for m in LIE_SHIFTS:
        S = shift(n, m)
        lhs = comm(hat(h, cs), hat(S, cs))
        rhs = hat(comm(h, S), cs)
        ok = ok and lhs == rhs and not is_zero(rhs)
        # and a_m^ is an eigenoperator with eigenvalue omega_k - omega_{k+m} = -3 m
        ok = ok and lhs == scal(F(-3 * m), hat(S, cs))
    GA.check("(ii) every current a_m is a normal mode of the boost flow iff the weights are "
             "affine; second-quantised commutators are hats of one-particle ones", ok)
    return ok


# ---------------- (iii) Planck clause, offset independence ----------------
def check_planck_offset_free():
    premise("singularity.bosonisation-bridge-s-wave-sector")
    premise("hawking.imported-quasi-free-states-car-algebra")
    b = F(3)
    ok = True
    for D in (F(1), F(5, 2), F(2, 7)):
        def n(k):
            return F(1) / (D * b ** k + 1)
        for m in (1, 2, 3):
            # termwise identity
            for k in range(-6, 7):
                ok = ok and n(k + m) * (1 - n(k)) == (n(k) - n(k + m)) / (b ** m - 1)
            # telescoped finite window and its edge error
            for K in (5, 10, 20):
                S = sum(n(k + m) * (1 - n(k)) for k in range(-K, K + 1))
                bottom = sum(n(k) for k in range(-K, -K + m))
                top = sum(n(k) for k in range(K + 1, K + m + 1))
                ok = ok and S == (bottom - top) / (b ** m - 1)
                limit = F(m) / (b ** m - 1)
                err = abs(S - limit)
                # 1 - n_k <= D b^k (k <= -K + m - 1) and n_k <= b^{-k}/D (k >= K + 1)
                bound = (m * D * b ** (-K + m - 1) + m * b ** (-K - 1) / D) / (b ** m - 1)
                ok = ok and err <= bound
            ok = ok and F(m) / (b ** m - 1) == F(m, 3 ** m - 1)
    GA.check("(iii) <a_{-m} a_m> telescopes to m/(b^m - 1) for every sea offset D, with "
             "explicit edge bounds", ok)
    return ok


# ---------------- (iv) particle-hole and the two offsets ----------------
def check_particle_hole_offsets():
    premise("synthesis.residue-common-weight-particle-hole")
    premise("hawking.imported-quasi-free-states-car-algebra")
    b = F(4)
    ok = True
    R = 6

    def sym(D):
        return lambda k: F(1) / (D * b ** k + 1)
    nR = sym(F(1))                 # sea level at a site: omega_0 = 0
    nNS = sym(F(2))                # D^2 = b: sea level midway between sites
    nG = sym(F(3))                 # generic offset
    ok = ok and all(nR(-k) == 1 - nR(k) for k in range(-R, R + 1))
    ok = ok and nR(0) == F(1, 2)
    ok = ok and all(nNS(-1 - k) == 1 - nNS(k) for k in range(-R, R + 1))
    ok = ok and all(nNS(k) != F(1, 2) for k in range(-R, R + 1))
    ok = ok and any(nG(-k) != 1 - nG(k) for k in range(-R, R + 1))
    ok = ok and any(nG(-1 - k) != 1 - nG(k) for k in range(-R, R + 1))
    # the reflection P: k -> -k maps h = diag(k) to -P h P^T = h on a symmetric window
    W = list(range(-3, 4))
    h = zeros(len(W), len(W))
    P = zeros(len(W), len(W))
    for i, k in enumerate(W):
        h[i][i] = F(k)
        P[i][W.index(-k)] = F(1)
    ok = ok and scal(F(-1), mm(mm(P, h), dag(P))) == h
    # NS: k -> -1-k on the window {-3..2} maps diag(k + 1/2) to minus itself under conjugation
    Wn = list(range(-3, 3))
    hn = zeros(len(Wn), len(Wn))
    Pn = zeros(len(Wn), len(Wn))
    for i, k in enumerate(Wn):
        hn[i][i] = F(k) + F(1, 2)
        Pn[i][Wn.index(-1 - k)] = F(1)
    ok = ok and scal(F(-1), mm(mm(Pn, hn), dag(Pn))) == hn
    # recurrence: in units of the slope the weights are integers (sea at a site), so the flow
    # at time 2 pi / c is the identity, or odd half-integers (sea between sites), so it is
    # the parity automorphism psi -> -psi
    ok = ok and all((F(k) * 2) % 2 == 0 for k in W)
    ok = ok and all(((F(k) + F(1, 2)) * 2) % 2 == 1 for k in Wn)
    GA.check("(iv) the symbol is particle-hole invariant exactly for the two symmetric "
             "offsets (sea at a site, sea between sites)", ok)
    return ok


# ---------------- (v) rotations: the tensor placement ----------------
def principal_triple(n):
    e, f, h = zeros(n, n), zeros(n, n), zeros(n, n)
    for i in range(n):
        h[i][i] = F(n - 1 - 2 * i)
    for i in range(n - 1):
        e[i][i + 1] = F((i + 1) * (n - 1 - i))
        f[i + 1][i] = F(1)
    return e, f, h


def check_tensor_placement():
    premise("scrambling.principality-indifference-sphere")
    premise("synthesis.residue-common-weight-particle-hole")
    premise("synthesis.residue-from-mode-entropy")
    premise("scrambling.boundary-mode-space-matrix")
    ok = True
    for n in (2, 3):
        e, f, h = principal_triple(n)
        ok = ok and comm(e, f) == h and comm(h, e) == scal(F(2), e)
        W = 3
        om = zeros(W, W)
        for i, k in enumerate((-1, 0, 1)):
            om[i][i] = F(k)
        Htot = kron(om, eye(n))
        ok = ok and sorted(Htot[i][i] for i in range(W * n)) == [F(-1)] * n + [F(0)] * n + [F(1)] * n
        for X in (e, f, h):
            ok = ok and is_zero(comm(Htot, kron(eye(W), X)))
        # diagonal generators commuting with 1 (x) e: solution space has dimension W
        N = W * n
        rows = []
        for r in range(N):
            for s in range(N):
                # [diag(d), E]_{rs} = (d_r - d_s) E_rs ; collect linear conditions on d
                Ers = kron(eye(W), e)[r][s]
                if Ers:
                    v = [F(0)] * N
                    v[r] += Ers
                    v[s] -= Ers
                    rows.append(v)
        rk = rank_of_vectors(rows) if rows else 0
        ok = ok and N - rk == W and rk == W * (n - 1)
        # the (Q) placement on one principal window: weights kappa k = (kappa/2) h
        ok = ok and comm(scal(F(1, 2), h), e) == e and not is_zero(e)
    # second quantised: 2 levels x spin 1/2 = 4 modes, K^ commutes with the rotation hats
    e, f, h = principal_triple(2)
    om = [[F(-1), F(0)], [F(0), F(1)]]
    cs = jw(4)
    Kh = hat(kron(om, eye(2)), cs)
    ok = ok and tr(Kh) == 0 and tr(mm(Kh, Kh)) == 16
    for X in (e, f, h):
        ok = ok and is_zero(comm(Kh, hat(kron(eye(2), X), cs)))
    ok = ok and not is_zero(comm(hat(kron(eye(2), scal(F(1, 2), h)), cs), hat(kron(eye(2), e), cs)))
    GA.check("(v) weights on the array index commute with the principal rotations on the "
             "channel index; equivariance forces weights constant on each multiplet; the "
             "single-window placement of (Q) does not commute", ok)
    return ok


def run():
    results = [check_quasi_free_part(), check_affine_law(), check_planck_offset_free(),
               check_particle_hole_offsets(), check_tensor_placement()]
    return all(results)


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
