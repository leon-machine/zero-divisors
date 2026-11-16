"""synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise: exact checks.

CAR Fock spaces from lib/fock.py (LSB bitmask, Jordan-Wigner); all arithmetic over Fractions.
A gauge-invariant quasi-free state with one-particle density E (<a_i^dag a_j> = E_ij, real
symmetric, 0 <= E <= 1) is built exactly as a product state of rotated modes b = O^T a with rational
orthogonal O (Cayley transform) and rational occupations nu. One-body observables
N_f = sum_ij f_ij a_i^dag a_j with f real symmetric.

(1) Wick: Var_E(N_f) = Tr(f E f (1 - E)), on the Fock space, for several E and f.
(2) The shot-noise bound: for any projector E_0 (the vacuum),
      sd_E(N_f) <= sd_0(N_f) + sqrt(2 Tr(f^2 X)),  X = (E - E_0)^2 + E(1 - E),  Tr X = N_exc,
    N_exc = Tr(E(1 - E_0)) + Tr((1 - E)E_0) (particles plus holes); square roots handled by squaring.
    The proof's steps are checked exactly: the purification
      Et = [[E, S], [S, 1 - E]], S = sqrt(E(1 - E)) (rational for nu = a^2/(a^2 + b^2)),
    is a projector restricting to E; with Et_0 = E_0 (+) (1 - E_0), ||Et - Et_0||^2 = 2 N_exc and the
    system block of (Et - Et_0)^2 is X; for a projector 2 Var = ||[f, Et]||^2.
    Control: the non-quasi-free mixture of the empty and the full state on five modes breaks the bound.
(3) Pairing included (Nambu form, alpha = (a, a^dag), Gamma_IJ = omega(alpha_J^dag alpha_I), O = alpha^dag F alpha / 2):
    Var = Tr(F Gamma F (1 - Gamma))/2 and sd <= sd_0 + sqrt(Tr(F^2 X)), X = (Gamma - Gamma_0)^2 + Gamma(1 - Gamma),
    Tr X = 2 <N_exc>, on a mixed state obtained by restricting a pure Thouless state of 5 modes to 3 (the
    purification's system block Gt_12 Gt_21 = Gamma(1 - Gamma) checked), and on the stored pure pair state
    (3/5)|00> + (4/5)|11> with the observable a^dag b + b^dag a coupling mode and partner.
(4) The descent's parity average over one mode, omega o E_desc = (omega + sigma omega sigma)/2:
      Var = Var_Gamma(F)/2 + Var_Gamma(SFS)/2 + diff^2/4,  diff = Tr((F - SFS) Gamma)/2,
      diff^2 <= 8 sum over I in the mode's Nambu pair, J outside, of F_IJ^2, on the Fock space.
(5) At the pivot: the shot term 3 c_k k_*^3/(2 pi^2 nbar) with nbar >= the comoving number of one Weyl species
    in the I-state, (3 zeta(3)/(2 pi^2)) (a_d T_d)^3, (a_d T_d)^3 >= (a_0 T_0)^3 g_s0/g_sd, g_sd <= 10^4,
    and c_k = <(omega + k)^2>/<omega>^2 < 1.31 for the Fermi-Dirac spectrum: below 1e-77, more than
    1e68 below A_s, for every T_d.
"""
from fractions import Fraction as F
import GA
import fock as fk
from tp_premise import premise


# ---------------------------------------------------------------- small exact linear algebra
def mzero(n):
    return [[F(0)] * n for _ in range(n)]


def eye(n):
    M = mzero(n)
    for i in range(n):
        M[i][i] = F(1)
    return M


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(k)), F(0)) for j in range(m)] for i in range(n)]


def madd(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def tp(A):
    return [list(r) for r in zip(*A)]


def inv(A):
    n = len(A)
    M = [list(A[i]) + eye(n)[i] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                fac = M[r][c]
                M[r] = [M[r][j] - fac * M[c][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def cayley(K):
    n = len(K)
    return mmul(madd(eye(n), K, -1), inv(madd(eye(n), K)))


def diag(v):
    M = mzero(len(v))
    for i, x in enumerate(v):
        M[i][i] = F(x)
    return M


def hs2(A):
    return sum((A[i][j] * A[i][j] for i in range(len(A)) for j in range(len(A[0]))), F(0))


def block(A, B, C, D):
    return [ra + rb for ra, rb in zip(A, B)] + [rc + rd for rc, rd in zip(C, D)]


def antisym(m, vals):
    K = mzero(m)
    t = 0
    for i in range(m):
        for j in range(i + 1, m):
            K[i][j] = F(vals[t % len(vals)])
            K[j][i] = -K[i][j]
            t += 1
    return K


# ---------------------------------------------------------------- Fock-space realisation
def rotated_ann(O, m):
    """b_i = sum_j O_ji a_j as sparse Fock operators."""
    A = [fk.ann(j, m) for j in range(m)]
    out = []
    for i in range(m):
        op = {}
        for j in range(m):
            if O[j][i] != 0:
                op = fk.madd(op, fk.msc(O[j][i], A[j]))
        out.append(op)
    return out


def quasi_free_rho(O, nus, m):
    dim = 2 ** m
    B = rotated_ann(O, m)
    rho = fk.eye(dim)
    for i in range(m):
        bd = fk.dag(B[i])
        fac = fk.madd(fk.msc(nus[i], fk.mm(bd, B[i])), fk.msc(1 - nus[i], fk.mm(B[i], bd)))
        rho = fk.mm(rho, fac)
    return rho


def one_body(f, m):
    op = {}
    for i in range(m):
        for j in range(m):
            if f[i][j] != 0:
                op = fk.madd(op, fk.msc(f[i][j], fk.mm(fk.cre(i, m), fk.ann(j, m))))
    return op


def fock_var(rho, Nf):
    mean = fk.trace(fk.mm(rho, Nf))
    return fk.trace(fk.mm(rho, fk.mm(Nf, Nf))) - mean * mean


def wick_var(f, E):
    n = len(E)
    return tr(mmul(mmul(mmul(f, E), f), madd(eye(n), E, -1)))


# ---------------------------------------------------------------- shared data
M = 4
O1 = cayley(antisym(M, [F(1, 2), F(-1, 3), F(1, 5), F(2, 7), F(-1, 4), F(1, 6)]))
O0 = cayley(antisym(M, [F(1, 3), F(1, 4), F(-2, 5), F(1, 7), F(1, 2), F(-1, 5)]))
# occupations nu = a^2/(a^2 + b^2): nu (1 - nu) is a rational square
PAIRS = [(1, 2), (3, 1), (2, 3), (1, 4)]
NUS = [F(a * a, a * a + b * b) for a, b in PAIRS]
ROOTS = [F(a * b, a * a + b * b) for a, b in PAIRS]
E1 = mmul(mmul(O1, diag(NUS)), tp(O1))
S1 = mmul(mmul(O1, diag(ROOTS)), tp(O1))
E0 = mmul(mmul(O0, diag([1, 1, 0, 0])), tp(O0))
FS = [
    [[F(1), F(1, 2), F(0), F(-1, 3)], [F(1, 2), F(-1), F(1, 4), F(0)], [F(0), F(1, 4), F(2), F(1)],
     [F(-1, 3), F(0), F(1), F(1, 2)]],
    [[F(0), F(1), F(0), F(0)], [F(1), F(0), F(1), F(0)], [F(0), F(1), F(0), F(1)], [F(0), F(0), F(1), F(0)]],
    diag([1, -1, 1, -1]),
    diag([1, 1, 0, 0]),
]


def bound_holds(var, var0, t):
    """sd <= sd0 + sqrt(2 t) <=> var - var0 - 2t <= 2 sqrt(2 var0 t)."""
    d = var - var0 - 2 * t
    return d <= 0 or d * d <= 8 * var0 * t


def check_wick_variance_on_fock_space():
    premise("hawking.imported-quasi-free-states-car-algebra")
    premise("hawking.i-state")
    ok = True
    rho = quasi_free_rho(O1, NUS, M)
    ok &= fk.trace(rho) == 1
    for i in range(M):
        for j in range(M):
            ok &= fk.trace(fk.mm(rho, fk.mm(fk.cre(i, M), fk.ann(j, M)))) == E1[i][j]
    for f in FS:
        ok &= fock_var(rho, one_body(f, M)) == wick_var(f, E1)
    # a second state: the vacuum projector itself (pure)
    rho0 = quasi_free_rho(O0, [1, 1, 0, 0], M)
    for f in FS:
        ok &= fock_var(rho0, one_body(f, M)) == wick_var(f, E0)
    GA.check("Wick: Var(N_f) = Tr(f E f (1 - E)) on the Fock space for mixed and pure quasi-free states", ok)
    return ok


def check_shot_noise_bound_and_its_proof_steps():
    premise("hawking.imported-quasi-free-states-car-algebra")
    premise("hawking.i-state")
    ok = True
    n = M
    one = eye(n)
    D = madd(E1, E0, -1)
    X = madd(mmul(D, D), mmul(E1, madd(one, E1, -1)))
    nexc = tr(mmul(E1, madd(one, E0, -1))) + tr(mmul(madd(one, E1, -1), E0))
    ok &= tr(X) == nexc and nexc > 0
    # purification: Et projector, restricts to E, distance to Et_0 is 2 N_exc, system block of Delta^2 is X
    Et = block(E1, S1, S1, madd(one, E1, -1))
    ok &= mmul(Et, Et) == Et
    ok &= mmul(S1, S1) == mmul(E1, madd(one, E1, -1))
    Et0 = block(E0, mzero(n), mzero(n), madd(one, E0, -1))
    Dt = madd(Et, Et0, -1)
    ok &= hs2(Dt) == 2 * nexc
    Dt2 = mmul(Dt, Dt)
    ok &= [row[:n] for row in Dt2[:n]] == X
    for f in FS:
        ft = block(f, mzero(n), mzero(n), mzero(n))
        com = madd(mmul(ft, Et), mmul(Et, ft), -1)
        var = wick_var(f, E1)
        ok &= 2 * var == hs2(com)                                   # pure: 2 Var = ||[f, Et]||^2
        ok &= wick_var(ft, Et) == var                                # same variance after purifying
        var0 = wick_var(f, E0)
        t = tr(mmul(mmul(f, f), X))
        ok &= t >= 0 and bound_holds(var, var0, t)
        ok &= hs2(mmul(ft, Dt)) == t                                 # ||f Dt||^2 = Tr(f^2 X)
    # control: a non-quasi-free mixture (empty + full on five modes) breaks the bound
    m5 = 5
    dim = 2 ** m5
    rho = fk.madd(fk.msc(F(1, 2), {(0, 0): F(1)}), fk.msc(F(1, 2), {(dim - 1, dim - 1): F(1)}))
    Ntot = fk.num_total(m5)
    var_cat = fock_var(rho, Ntot)
    Ecat = diag([F(1, 2)] * m5)
    Xcat = madd(mmul(Ecat, Ecat), mmul(Ecat, madd(eye(m5), Ecat, -1)))   # E_0 = 0, the empty state
    t_cat = tr(Xcat)
    ok &= var_cat == F(25, 4) and t_cat == F(5, 2) and not bound_holds(var_cat, F(0), t_cat)
    GA.check("shot-noise bound sd <= sd_0 + sqrt(2 Tr(f^2 X)) with its purification steps; a cat mixture breaks it", ok)
    return ok


# ---------------------------------------------------------------- Nambu (pairing) form
def thouless(Z, m):
    """exp(sum_{i<j} Z_ij a_i^dag a_j^dag)|0> as a normalised density matrix (a pure quasi-free state)."""
    K = {}
    for i in range(m):
        for j in range(i + 1, m):
            if Z[i][j] != 0:
                K = fk.madd(K, fk.msc(Z[i][j], fk.mm(fk.cre(i, m), fk.cre(j, m))))
    v, term, k = {0: F(1)}, {0: F(1)}, 1
    while True:
        term = {s: c / k for s, c in fk.apply(K, term).items()}
        if not term:
            break
        v = fk.vadd(v, term)
        k += 1
    return fk.msc(1 / fk.braket(v, v), fk.outer(v, v))


def nambu_ops(m):
    A = [fk.ann(i, m) for i in range(m)]
    Ad = [fk.cre(i, m) for i in range(m)]
    return A + Ad, Ad + A                      # alpha = (a, a^dag), alpha^dag = (a^dag, a)


def nambu_gamma(rho, m):
    """Gamma_IJ = omega(alpha_J^dag alpha_I): [[E, kappa], [kappa^dag, 1 - E^T]]."""
    al, ald = nambu_ops(m)
    return [[fk.trace(fk.mm(rho, fk.mm(ald[J], al[I]))) for J in range(2 * m)] for I in range(2 * m)]


def nambu_F(h, D):
    """Hermitian Nambu matrix of O = sum h_ij a_i^dag a_j + (1/2) sum D_ij (a_i^dag a_j^dag + h.c.) - Tr(h)/2."""
    m = len(h)
    return block(h, D, [[D[j][i] for j in range(m)] for i in range(m)], [[-h[j][i] for j in range(m)] for i in range(m)])


def nambu_obs(Fm, m):
    al, ald = nambu_ops(m)
    O = {}
    for I in range(2 * m):
        for J in range(2 * m):
            if Fm[I][J] != 0:
                O = fk.madd(O, fk.msc(Fm[I][J] / 2, fk.mm(ald[I], al[J])))
    return O


def nambu_var(Fm, G):
    one = eye(len(G))
    return tr(mmul(mmul(mmul(Fm, G), Fm), madd(one, G, -1))) / 2


def sym(m, vals):
    S = mzero(m)
    t = 0
    for i in range(m):
        for j in range(i, m):
            S[i][j] = S[j][i] = F(vals[t % len(vals)])
            t += 1
    return S


def bound_holds_nambu(var, var0, t):
    """sd <= sd0 + sqrt(t) <=> var - var0 - t <= 2 sqrt(var0 t)."""
    d = var - var0 - t
    return d <= 0 or d * d <= 4 * var0 * t


MT, MS = 5, 3                                   # a pure Thouless state on 5 modes, restricted to 3
ZT = antisym(MT, [F(1, 2), F(-3, 2), F(2, 3), F(1), F(-1, 3), F(3, 4), F(-2), F(1, 5), F(5, 4), F(-1, 2)])
Z0 = antisym(MS, [F(-1, 3), F(2), F(1, 2)])
HS = [sym(MS, [F(1), F(-1, 2), F(2, 3), F(3, 2), F(0), F(-1)]), sym(MS, [F(0), F(1), F(0), F(0), F(1), F(0)]),
      sym(MS, [F(2), F(0), F(0), F(-1), F(0), F(1, 2)])]
DS = [antisym(MS, [F(1, 2), F(0), F(-1)]), antisym(MS, [F(0), F(0), F(0)]), antisym(MS, [F(2), F(1, 3), F(1)])]


def check_bound_with_pairing_and_the_pure_pair_states():
    premise("hawking.imported-quasi-free-states-car-algebra")
    premise("synthesis.quadratic-flows-cannot-thermalise-descent")
    ok = True
    pure = thouless(ZT, MT)
    rho = fk.ptrace(pure, MT, [3, 4])
    rho0 = thouless(Z0, MS)
    G, G0, GT = nambu_gamma(rho, MS), nambu_gamma(rho0, MS), nambu_gamma(pure, MT)
    one = eye(2 * MS)
    ok &= mmul(G0, G0) == G0 and mmul(GT, GT) == GT and mmul(G, G) != G      # pure, pure, mixed
    # the system block of the purification: Gt_12 Gt_21 = Gamma (1 - Gamma), whatever the partner
    sysI = [0, 1, 2, 5, 6, 7]
    parI = [3, 4, 8, 9]
    ok &= [[GT[i][j] for j in sysI] for i in sysI] == G
    G12G21 = [[sum((GT[i][p] * GT[p][j] for p in parI), F(0)) for j in sysI] for i in sysI]
    ok &= G12G21 == mmul(G, madd(one, G, -1))
    Dl = madd(G, G0, -1)
    X = madd(mmul(Dl, Dl), mmul(G, madd(one, G, -1)))
    # Tr X = 2 <N_exc>, N_exc the quasi-particle number of the reference: (1/2) alpha^dag (1 - 2 Gamma_0) alpha + n/2
    Nexc = fk.madd(nambu_obs(madd(one, G0, -2), MS), fk.msc(F(MS, 2), fk.eye(2 ** MS)))
    ok &= fk.trace(fk.mm(rho0, Nexc)) == 0 and tr(X) == 2 * fk.trace(fk.mm(rho, Nexc))
    for h, D in zip(HS, DS):
        Fm = nambu_F(h, D)
        O = nambu_obs(Fm, MS)
        v, v0 = fock_var(rho, O), fock_var(rho0, O)
        ok &= v == nambu_var(Fm, G) and v0 == nambu_var(Fm, G0)
        t = tr(mmul(mmul(Fm, Fm), X))
        ok &= t >= 0 and bound_holds_nambu(v, v0, t)
    # the stored pure pair state c|00> + s|11> (c, s) = (3/5, 4/5), with the observable a^dag b + b^dag a
    # that couples mode and partner wherever the partner is placed, against the empty reference
    pair = thouless([[F(0), F(4, 3)], [F(-4, 3), F(0)]], 2)
    ok &= pair[(0, 0)] == F(9, 25) and pair[(3, 3)] == F(16, 25)
    Gp, Ge = nambu_gamma(pair, 2), nambu_gamma({(0, 0): F(1)}, 2)
    Fh = nambu_F([[F(0), F(1)], [F(1), F(0)]], [[F(0), F(0)], [F(0), F(0)]])
    Dp = madd(Gp, Ge, -1)
    one2 = eye(4)
    Xp = madd(mmul(Dp, Dp), mmul(Gp, madd(one2, Gp, -1)))
    vp, ve = fock_var(pair, nambu_obs(Fh, 2)), fock_var({(0, 0): F(1)}, nambu_obs(Fh, 2))
    tp_ = tr(mmul(mmul(Fh, Fh), Xp))
    ok &= vp == nambu_var(Fh, Gp) and bound_holds_nambu(vp, ve, tp_) and tr(Xp) == 2 * F(32, 25)
    GA.check("Nambu form with pairing: Var = Tr(F G F (1 - G))/2, sd <= sd_0 + sqrt(Tr(F^2 X)), pair states included", ok)
    return ok


def check_descent_parity_average():
    premise("singularity.descent-parity-average")
    premise("singularity.imported-descent-one-way-conditional-expectation")
    premise("hawking.imported-quasi-free-states-car-algebra")
    ok = True
    rho = fk.ptrace(thouless(ZT, MT), MT, [3, 4])
    G = nambu_gamma(rho, MS)
    sig = fk.mode_parity(0, MS)
    rhoE = fk.msc(F(1, 2), fk.madd(rho, fk.mm(fk.mm(sig, rho), sig)))
    Sm = diag([-1, 1, 1, -1, 1, 1])                 # the flip a_0 -> -a_0 in Nambu form
    K = [0, MS]
    for h, D in zip(HS, DS):
        Fm = nambu_F(h, D)
        O = nambu_obs(Fm, MS)
        SFS = mmul(mmul(Sm, Fm), Sm)
        ok &= fk.meq(fk.mm(fk.mm(sig, O), sig), nambu_obs(SFS, MS))
        diff = tr(mmul(madd(Fm, SFS, -1), G)) / 2
        lhs = fock_var(rhoE, O)
        ok &= lhs == nambu_var(Fm, G) / 2 + nambu_var(SFS, G) / 2 + diff * diff / 4
        r2 = sum((Fm[i][j] * Fm[i][j] for i in K for j in range(2 * MS) if j not in K), F(0))
        ok &= diff * diff <= 8 * r2
    GA.check("descent parity average: Var = (Var_F + Var_SFS)/2 + diff^2/4, diff^2 <= 8 sum |F_(K, not K)|^2", ok)
    return ok


def check_shot_term_at_the_pivot():
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    premise("hawking.i-state")
    ok = True
    PI_LO, PI_HI = F(333, 106), F(355, 113)
    Z3_LO, Z3_HI = F(6, 5), F(1203, 1000)            # 1.2 < zeta(3) = 1.2020569... < 1.203
    Z5_HI = F(104, 100)                               # zeta(5) = 1.0369... < 1.04
    Z4_LO = PI_LO ** 4 / 90                           # zeta(4) = pi^4/90
    # <omega^2>/<omega>^2 of the massless Fermi-Dirac spectrum = (4/3) eta(5) eta(3)/eta(4)^2
    eta3_hi, eta5_hi, eta4_lo = F(3, 4) * Z3_HI, F(15, 16) * Z5_HI, F(7, 8) * Z4_LO
    c_hi = F(4, 3) * eta5_hi * eta3_hi / (eta4_lo * eta4_lo)
    ok &= F(1307, 1000) < c_hi < F(1309, 1000)
    # k_*/(a_0 T_0): k_* = 0.05 / Mpc, T_0 = 2.7255 K
    kB = F("8.617333262e-5")                          # eV/K
    hbarc = F("1.973269804e-7")                       # eV m
    mpc = F("3.0856775814913673e22")                  # m
    T0_inv_mpc = F("2.7255") * kB / hbarc * mpc       # a_0 T_0 in Mpc^-1
    ratio = F("0.05") / T0_inv_mpc
    ok &= F("1.3613e-27") < ratio < F("1.3615e-27")
    gs0, gsd = F(43, 11), F(10) ** 4
    nbar_lo = 3 * Z3_LO / (2 * PI_HI ** 2) * gs0 / gsd           # in units of (a_0 T_0)^3
    # c_k = <(omega + k)^2>/<omega>^2 <= c (1 + k/<omega>)^2, <omega> > 3 a_d T_d, a_d T_d >= a_0 T_0 (g_s0/g_sd)^(1/3)
    k_over_adTd = ratio * 14                          # 14^3 > g_sd/g_s0 = 10^4 * 11/43
    ok &= 14 ** 3 * gs0 > gsd
    ck_hi = c_hi * (1 + k_over_adTd / 3) ** 2
    ok &= ck_hi < F(131, 100)
    shot_hi = 3 * ck_hi * ratio ** 3 / (2 * PI_LO ** 2 * nbar_lo)
    As_lo = F("2.07e-9")
    ok &= 7 * F(10) ** -78 < shot_hi < F(10) ** -77
    ok &= F(7, 1) * F(10) ** -80 < shot_hi * F(10675, 100) / gsd < 8 * F(10) ** -80
    ok &= shot_hi * F(10) ** 68 < As_lo
    # the amplitude of the shot term is independent of T_d: only the comoving number enters
    GA.check("shot term 3 c_k k_*^3/(2 pi^2 nbar) at the pivot below 1e-77 (g_sd <= 1e4), more than 1e68 below A_s", ok)
    return ok


if __name__ == "__main__":
    for fn in (check_wick_variance_on_fock_space, check_shot_noise_bound_and_its_proof_steps,
               check_bound_with_pairing_and_the_pure_pair_states, check_descent_parity_average,
               check_shot_term_at_the_pivot):
        print(fn.__name__, fn())

def _ls_add(a, b, s=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + s * v
    return {k: v for k, v in r.items() if v != 0}


def _ls_mul(a, b, cut):
    r = {}
    for i, u in a.items():
        for j, v in b.items():
            if i + j <= cut:
                r[i + j] = r.get(i + j, 0) + u * v
    return {k: v for k, v in r.items() if v != 0}


def _radiation_projection():
    """Frobenius series of Phi'' + (4/x) Phi' + Phi/3 = 0 (growing sum a_n x^(2n), decaying sum b_n x^(2n-3)),
    R = Phi + (x Phi' + Phi)/2, Delta = -(2/3) x^2 Phi, and the projection of data (R, Delta) on the growing
    solution: R_inf = R cR(x) + Delta cD(x).  Returns the pieces the check asserts on."""
    nterms = 7
    g, d = {0: F(1)}, {-3: F(1)}
    a = b = F(1)
    for n in range(1, nterms):
        a = -a / (3 * (2 * n) * (2 * n + 3))
        g[2 * n] = a
        b = -b / (3 * (2 * n - 3) * (2 * n))
        d[2 * n - 3] = b
    xd = lambda p: {k: v * k for k, v in p.items() if k != 0}
    residual_ok = True
    for p in (g, d):
        xdp = xd(p)
        res = _ls_add(_ls_add(_ls_add(xd(xdp), xdp, -1), {k: 4 * v for k, v in xdp.items()}),
                      _ls_mul({2: F(1, 3)}, p, 99))
        residual_ok = residual_ok and all(v == 0 for k, v in res.items() if k < max(p))
    R = lambda p: _ls_add(p, {k: v / 2 for k, v in _ls_add(xd(p), p).items()})
    D = lambda p: _ls_mul({2: F(-2, 3)}, p, 99)
    Rg, Dg, Rd, Dd = R(g), D(g), R(d), D(d)
    det = _ls_add(_ls_mul(Rg, Dd, 5), _ls_mul(Dg, Rd, 5), -1)
    cR = {k + 1: -F(3, 2) * v for k, v in Dd.items()}       # R_inf = (3/2) A, A = -x (R D_d - Delta R_d)
    cD = {k + 1: F(3, 2) * v for k, v in Rd.items()}
    dec = _ls_add(Rd, {k: v / 4 for k, v in Dd.items()})
    return dict(residual_ok=residual_ok, g=g, d=d, Rg=Rg, Rd=Rd, Dd=Dd, det=det, cR=cR, cD=cD, dec=dec)


def check_conversion_readings_of_the_shot_term():
    premise("synthesis.imported-large-scale-potential-and-sachs-wolfe-relations")
    premise("synthesis.imported-superhorizon-zeta-conservation")
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    S = _radiation_projection()
    ok = S["residual_ok"]
    ok &= S["g"][2] == F(-1, 30) and S["d"][-1] == F(1, 6)
    # growing solution: R = (3w + 5)/(3(w + 1)) Phi at w = 1/3, the stored relation
    w = F(1, 3)
    ok &= S["Rg"][0] == (3 * w + 5) / (3 * (w + 1)) == F(3, 2)
    ok &= S["det"] == {-1: F(-1)}
    cR, cD = S["cR"], S["cD"]
    ok &= (cR[0], cR[2], cD[0], cD[2]) == (F(1), F(1, 6), F(1, 4), F(-1, 24))
    # the decaying solution has R + Delta/4 = 0 to the two leading orders
    ok &= min(S["dec"]) == 1 and S["Rd"][-1] == F(1, 6) and S["Dd"][-1] == F(-2, 3)
    # slice data in the radiation era: R = psi + r, Delta_c = delta + 4 r, r = -H q/(rho + p); x = 1/X
    delta, r, X = F(2, 3), F(-5), F(10)

    def r_inf(psi):
        return (psi + r) * (cR[0] + cR[2] / X ** 2) + (delta + 4 * r) * (cD[0] + cD[2] / X ** 2)

    fm = r_inf(F(0))                                    # (FM): delta/4 + 2 r - delta/(24 X^2)
    ok &= fm == F(-35401, 3600) and fm == delta / 4 + 2 * r - delta / (24 * X ** 2)
    ue = r_inf(-F(3, 2) * X ** 2 * delta)               # (UE): the terms of order delta cancel
    ok &= ue == F(-396001, 3600) and ue == -F(3, 2) * X ** 2 * delta + 2 * r - delta / (24 * X ** 2)
    fr = delta * (cD[0] + cD[2] / X ** 2)               # (FR): r = 0, psi = 0
    ok &= fr == F(599, 3600)
    # under (FR) the uniform-density variable R - Delta_c/4 on the slice is -delta/4: opposite sign, same size
    ok &= (F(0) - delta / 4) * fr < 0 and abs(fr + (F(0) - delta / 4)) == delta / (24 * X ** 2)
    # thermal ratio: P_delta = 4T/rho, P_u = T/(rho + p) with p = rho/3
    T, rho = F(3, 7), F(11)
    Pd, Pu = 4 * T / rho, T / (rho + rho / 3)
    ok &= (Pd, Pu) == (F(12, 77), F(9, 308)) and Pu == F(3, 16) * Pd and 4 * Pu == 12 * Pd / 16
    # numbers.  (FM) at the pivot, Standard Model count: shot < 8e-80, X < 7.63e22/222
    X_hi = F(763, 100) * 10 ** 22 / 222
    ok &= F(343, 100) * 10 ** 20 < X_hi < F(344, 100) * 10 ** 20
    fm_hi = 8 * F(10) ** -80 * (1 + 12 * X_hi ** 2) / 16
    ok &= F(70, 10) * F(10) ** -39 < fm_hi < F(71, 10) * F(10) ** -39
    # (UE), thermal: amplitude^2 = (135 f)^2 g (T/M)^6 X^2/(90^3 pi^2), M the reduced Planck mass 2.435e18 GeV
    gst, f, M = F(10675, 100), F(1, 2), F(2435, 1000) * 10 ** 18
    X_lo = F(32, 10) * 10 ** 20
    amp2_top = (135 * f) ** 2 * gst * (10 ** 12 / M) ** 6 * X_lo ** 2 / (90 ** 3 * F(22, 7) ** 2)
    amp2_top_hi = (135 * f) ** 2 * gst * (10 ** 12 / M) ** 6 * X_lo ** 2 / (90 ** 3 * F(333, 106) ** 2)
    ok &= F(57, 10) ** 2 < amp2_top < amp2_top_hi < F(58, 10) ** 2
    amp2_1e10 = amp2_top / 10 ** 16                      # T_d and X each a hundred times smaller: T^6 X^2
    ok &= amp2_1e10 * 10 ** 16 == amp2_top and (26 * F("2.13e-9")) ** 2 < amp2_1e10 < (28 * F("2.13e-9")) ** 2
    GA.check("conversion: R_inf = psi + delta/4 + 2 r; readings (FR), (FM), (UE); thermal numbers", ok)
    assert ok
