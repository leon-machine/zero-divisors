"""angle.imported-singularity-papers-state-selection: exact checks of the finite cores of this imported Fact.

Horizon pair: two fermionic modes, Jordan-Wigner basis |n0 n1> (index n0 + 2 n1), boost K = w (N0 - N1) (the
number-difference boost of the vacuum form), sample w = 1.
(a) State form: the vectors invariant up to phase under e^{itK} are the eigenvectors of K; its eigenspaces are
    span{|00>, |11>} (0), |10> (w), |01> (-w), computed as kernels. Cyclic and separating for the mode-0 factor
    means Schmidt rank 2 (full-rank reduced density matrix): c|00> + s|11> has it iff c s != 0, and |10>, |01>
    and |00> do not.
(b) Marginal diag(c^2, s^2) = Gibbs diag(1, q)/(1 + q) with q = tan^2 theta = s^2/c^2; the sample point
    q = 9/16 is (c, s) = (4/5, 3/5).
(c) Automorphisms intertwining the flow act on beta through {+-1}: an inner automorphism Ad(U) of M_2 with
    U K U^{-1} = lambda K + mu has characteristic polynomial x^2 - w^2/4 = (x - mu)^2 - lambda^2 w^2/4, forcing
    mu = 0 and lambda^2 = 1; U = 1 and the particle-hole swap realise lambda = 1 and -1, and the linear system
    U K = (lambda K + mu) U has only the zero solution for lambda in {2, 1/2, -3} (any mu tested at the forced
    value 0 and at sample values).
(d) Schwarzschild f(r) = 1 - 2M/r: horizon r = 2M, kappa = f'(r_h)/2 = 1/(4M); near the horizon f = 2 kappa x
    - x^2/(4M^2) + O(x^3) in x = r - r_h, so the Euclidean section is smooth at period 2 pi/kappa = 8 pi M
    (coefficient of pi checked at several M).
(e) What imposing KMS mode by mode fixes: for one mode with Boltzmann ratio q = e^{-beta w}, the KMS relations
    phi(E_ab E_cd) = phi(E_cd alpha_{i beta}(E_ab)) on all matrix-unit pairs, solved for a general linear functional
    phi on M_2, have a one-dimensional solution space spanned by diag(1, q); normalised, the marginal is the Gibbs
    state diag(1, q)/(1 + q), at q in {9/16, 1/3, 5}. That (R) imposes KMS, and at the period 2 pi/kappa, is the
    content of the assumed premise singularity.r-regularity-fixed-locus and is not computed here.
(f) Ultralocal supplied class: on three modes every number monomial prod_{x in S} N_x (S any subset) and every
    parity section 1 - 2 N_x commutes with every N_x, while the hopping generator a_0^dag a_1 (outside the class)
    does not.
(g) Sea-level occupancies of the s-wave array: with the weights w_k = kappa k entered as premise (Q)'s convention
    (not derived here), the occupancies n_k = 1/(x^{-k} + 1), x = e^{-beta kappa}, have n_0 = 1/2 and
    n_k + n_{-k} = 1 (explicit values at x = 1/2), and the bilinear weights, computed as the eigenvalues of
    [H, a_j^dag a_i] for H = sum_k kappa k N_k on the sites -1, 0, 1, depend only on the site difference.
"""
from fractions import Fraction as F
from itertools import product

import GA
from pyutil import get_or_set
import fock
from tp_premise import premise

DIM = 4
SAMPLE_CS = [(F(4, 5), F(3, 5)), (F(5, 13), F(-12, 13)), (F(1), F(0)), (F(0), F(1))]
MASSES = [F(1, 2), F(3), F(7, 4)]
QS = [F(9, 16), F(1, 3), F(5)]


def zero(n=DIM):
    return [[F(0)] * n for _ in range(n)]


mm = GA.mat_mul                         # dense matrix product


def madd(a, b, c=1):
    return [[a[i][j] + F(c) * b[i][j] for j in range(len(a))] for i in range(len(a))]


def ident(n=DIM):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def num(k):
    return fock.to_dense(fock.num(k, 2), DIM)


def reduced(v):
    """Reduced density matrix on mode 0 of a real vector with even or odd parity (coefficients v[n0 + 2 n1])."""
    rho = zero(2)
    for a in range(2):
        for b in range(2):
            rho[a][b] = sum(v[a + 2 * n1] * v[b + 2 * n1] for n1 in range(2))
    return rho


def check_boost_invariant_cyclic_separating_states():
    premise("singularity.schmidt-forcing-proved-outright")
    K = madd(num(0), num(1), -1)
    ok = True
    dims = {}
    for lam in (F(0), F(1), F(-1), F(2)):
        ker = GA.field_kernel(madd(K, ident(), -lam))
        dims[lam] = len(ker)
    ok = ok and dims == {F(0): 2, F(1): 1, F(-1): 1, F(2): 0}
    full = 0
    for c, s in SAMPLE_CS:
        v = [c, F(0), F(0), s]
        ok = ok and [sum(K[i][j] * v[j] for j in range(DIM)) for i in range(DIM)] == [F(0)] * DIM
        rho = reduced(v)
        rank = GA.field_rank(rho)
        ok = ok and (rank == 2) == (c * s != 0)
        full += rank == 2
        if c * c + s * s == 1:
            ok = ok and rho == [[c * c, F(0)], [F(0), s * s]]
    for prod in ([F(0), F(1), F(0), F(0)], [F(0), F(0), F(1), F(0)]):
        ok = ok and GA.field_rank(reduced(prod)) == 1
    _tp_rv = (ok and full == 2); assert _tp_rv is not False, "check_boost_invariant_cyclic_separating_states"; return _tp_rv


def check_marginal_is_gibbs_at_the_sample_point():
    premise("singularity.modular-descent")
    c, s = F(4, 5), F(3, 5)
    q = s * s / (c * c)
    ok = q == F(9, 16) and c * c + s * s == 1
    ok = ok and (c * c, s * s) == (1 / (1 + q), q / (1 + q))
    _tp_rv = (ok); assert _tp_rv is not False, "check_marginal_is_gibbs_at_the_sample_point"; return _tp_rv


def check_intertwining_automorphisms_act_through_sign():
    premise("singularity.rate-rigidity-temperature-not-algebra-intrinsic")
    w = F(1)
    K = [[w / 2, F(0)], [F(0), -w / 2]]
    ok = True
    # characteristic polynomial coefficients: (trace, det) of K and of lambda K + mu
    for lam in (F(1), F(-1), F(2), F(1, 2), F(-3)):
        for mu in (F(0), F(1, 4), F(-1)):
            T = [[lam * K[0][0] + mu, F(0)], [F(0), lam * K[1][1] + mu]]
            same = (T[0][0] + T[1][1], T[0][0] * T[1][1]) == (K[0][0] + K[1][1], K[0][0] * K[1][1])
            ok = ok and same == (mu == 0 and lam * lam == 1)
            # solve U K = T U for U (4 unknowns): an invertible solution exists iff conjugate
            rows = []
            for i in range(2):
                for j in range(2):
                    row = [F(0)] * 4
                    for k in range(2):
                        row[2 * i + k] += K[k][j]          # (U K)_ij = sum_k U_ik K_kj
                        row[2 * k + j] -= T[i][k]          # (T U)_ij = sum_k T_ik U_kj
                    rows.append(row)
            sols = GA.field_kernel(rows)
            inv = any(u[0] * u[3] - u[1] * u[2] != 0 for u in sols) or (
                len(sols) == 2 and (sols[0][0] + sols[1][0]) * (sols[0][3] + sols[1][3])
                - (sols[0][1] + sols[1][1]) * (sols[0][2] + sols[1][2]) != 0)
            ok = ok and inv == same
    swap = [[F(0), F(1)], [F(1), F(0)]]
    ok = ok and mm(mm(swap, K), swap) == [[-w / 2, F(0)], [F(0), w / 2]]
    _tp_rv = (ok); assert _tp_rv is not False, "check_intertwining_automorphisms_act_through_sign"; return _tp_rv


def check_surface_gravity_and_euclidean_period():
    premise("singularity.computed")
    premise("singularity.euclidean-section-period")
    ok = True
    for M in MASSES:
        rh = 2 * M
        ok = ok and 1 - 2 * M / rh == 0
        fprime = 2 * M / (rh * rh)
        kappa = fprime / 2
        ok = ok and kappa == 1 / (4 * M)
        # expansion f(rh + x) = x/(rh + x) checked against 2 kappa x - x^2/(4M^2) + x^3/(8M^3) - ...
        for x in (F(1, 100), F(-1, 300)):
            exact = 1 - 2 * M / (rh + x)
            series = 2 * kappa * x - x * x / (4 * M * M) + x ** 3 / (8 * M ** 3)
            ok = ok and abs(exact - series) <= abs(x) ** 4 / M ** 4
        # period 2 pi/kappa in units of pi: 8 M
        ok = ok and 2 / kappa == 8 * M
    _tp_rv = (ok); assert _tp_rv is not False, "check_surface_gravity_and_euclidean_period"; return _tp_rv


def check_kms_relations_fix_each_mode_marginal():
    premise("singularity.r-regularity-fixed-locus")
    ok = True
    for q in QS:
        w = [F(1), q]                                           # e^{-beta K} eigenvalues, N = diag(0, 1)
        rows = []                                               # unknowns phi(E_ij) at index 2 i + j
        for a, b, c, d in product(range(2), repeat=4):
            # phi(E_ab E_cd) - (w_a/w_b) phi(E_cd E_ab) = 0, E_ab E_cd = delta_bc E_ad
            row = [F(0)] * 4
            if b == c:
                row[2 * a + d] += 1
            if d == a:
                row[2 * c + b] -= w[a] / w[b]
            rows.append(row)
        ker = GA.field_kernel(rows)
        ok = ok and len(ker) == 1
        v = ker[0]
        ok = ok and v[1] == 0 and v[2] == 0 and v[0] != 0 and v[3] == q * v[0]
        ok = ok and [v[0] / (v[0] + v[3]), v[3] / (v[0] + v[3])] == [1 / (1 + q), q / (1 + q)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_kms_relations_fix_each_mode_marginal"; return _tp_rv


def check_supplied_class_ultralocal_and_sea_level_occupancies():
    premise("singularity.l-boundary-mode-locality")
    premise("singularity.class-relative-no-go-no-supplied")
    premise("singularity.q-joint-quasi-freeness-s-wave")
    m = 3
    nums = [fock.num(k, m) for k in range(m)]
    ok = True
    count = 0
    for S in product(range(2), repeat=m):
        mono = fock.eye(2 ** m)
        for k in range(m):
            if S[k]:
                mono = fock.mm(mono, nums[k])
        ok = ok and all(fock.is_zero(fock.comm(mono, N)) for N in nums)
        count += 1
    for k in range(m):
        sigma = fock.msub(fock.eye(2 ** m), fock.msc(2, nums[k]))
        ok = ok and all(fock.is_zero(fock.comm(sigma, N)) for N in nums)
    hop = fock.mm(fock.cre(0, m), fock.ann(1, m))           # a_0^dag a_1, outside the class
    ok = ok and fock.comm(nums[0], hop) == hop and fock.comm(nums[1], hop) == fock.msc(-1, hop)
    ok = ok and fock.is_zero(fock.comm(nums[2], hop)) and count == 8
    for x in (F(1, 2), F(1, 3)):
        def n(k):
            return 1 / (x ** (-k) + 1)
        ok = ok and n(0) == F(1, 2)
        ok = ok and all(n(k) + n(-k) == 1 for k in range(1, 5))
        ok = ok and n(1) == x / (1 + x)
    x = F(1, 2)
    ok = ok and [1 / (x ** (-k) + 1) for k in (-2, -1, 1, 2)] == [F(4, 5), F(2, 3), F(1, 3), F(1, 5)]
    # bilinear weights from the flow: H = sum_k kappa k N_k on sites k = -1, 0, 1 (modes 0, 1, 2), kappa = 1/4;
    # [H, a_j^dag a_i] = (w_j - w_i) a_j^dag a_i, and the weight depends only on the site difference
    kappa = F(1, 4)
    H = fock.madd(*[fock.msc(kappa * (i - 1), nums[i]) for i in range(m)])
    weights = {}
    for j in range(m):
        for i in range(m):
            if i != j:
                b = fock.mm(fock.cre(j, m), fock.ann(i, m))
                c = fock.comm(H, b)
                lam = c[next(iter(b))] / b[next(iter(b))]
                ok = ok and c == fock.msc(lam, b)
                get_or_set(weights, j - i, set()).add(lam)
    ok = ok and weights == {1: {F(1, 4)}, 2: {F(1, 2)}, -1: {F(-1, 4)}, -2: {F(-1, 2)}}
    _tp_rv = (ok); assert _tp_rv is not False, "check_supplied_class_ultralocal_and_sea_level_occupancies"; return _tp_rv
