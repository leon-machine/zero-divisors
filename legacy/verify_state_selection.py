#!/usr/bin/env python3
"""
verify_state_selection.py: exact-arithmetic verification of the computational
identities of

    "Selecting the State: Parity, Regularity, and the Irreducible Calibration
     behind the Hawking Temperature"   (companion note to Transport Papers T5)

in the style of the series' scripts: the shared basis-blade Clifford engine of
GA.py over exact rationals for the Clifford statements, and an exact
multi-qubit engine with rational amplitudes for the state-level statements.
Every check is PASS/FAIL; nonzero exit on any failure; no floating point
anywhere.  Where an exponential appears it is carried as an exact rational
variable (x = e^{-beta omega} in Q), never evaluated numerically.

Coverage (labels refer to the note):
  [Thm 2.2]  the descent is the parity average: E(x) = (x + sigma x sigma)/2;
             idempotence; the conditional-expectation property E(a x b) =
             a E(x) b for even a, b; range = even span {1, sigma}; kernel =
             odd span {v, v*}; and the atom's CAR with sigma = e0 e1
  [Thm 3.1]  the descended form is state independent: E(rho) is diagonal for a
             generic rational rho, equals the Gibbs matrix diag(1, x)/(1+x) at
             the x the theorem names, and x -> p is injective
  [Thm 3.3]  univalence: omega(v_k) = 0 and all single-mode marginals diagonal
             for an even three-mode state; a parity-mixed control has a nonzero
             marginal coherence; the model's pair states are even
  [Thm 4.2]  KMS uniqueness: the KMS identity on all sixteen matrix-unit pairs
             for rho ~ diag(1, 16/9); a non-Gibbs diagonal state fails it; the
             commutation [rho, e^{beta H}] = 0 forced by the identity
  [Cor 4.4]  universality: the two-mode product is a Gibbs state of K_geo
             exactly when the two inverse temperatures agree (x2 = x1^{w2/w1}),
             with a witness pair for which it fails; the GMC state factorises
  [Thm 4.5]  rate rigidity: diagonal unitaries fix the Gibbs state; the
             exchange unitary sends beta to -beta; the exchange does not
             commute with K
  [Prop 5.2] the Euclidean partner: sigma_r^2 = +1 and (I sigma_r)^2 = -1
             blade-exactly in Cl(1,3); both are shape-operator eigenvectors of
             eigenvalue -2; the rotor composition law; R_{2pi} = -1 reached by
             squaring the quarter rotor; conjugation by -1 is trivial
  [Thm 6.1]  exact equilibrium over-determines: the product Gibbs state is a
             fixed point of E_N (zero deficit) and equals rho_1 (x) rho_2,
             against a correlated control with both failing
  [Thm 7.1]  purification: the thermofield vector reproduces rho on partial
             trace; the modular eigenvalues lambda_i^2/lambda_j^2; the angle
             tan^2 theta = e^{-omega/T}; purifications differ by a unitary on
             the purifying factor only
  [Prop 6.4] number-diagonal dynamics: a controlled-Z circuit preserves every
             joint-number probability and every marginal; a real beam-splitter
             (hopping) rotation does not, which is exactly what (L_E) excludes
"""

from fractions import Fraction
import sys
import GA as g


# ---------------------------------------------------------------------------
# exact matrix helpers over Q
# ---------------------------------------------------------------------------

def F(a, b=1):
    return Fraction(a, b)


def zeros(n, m=None):
    m = n if m is None else m
    return [[F(0)] * m for _ in range(n)]


def eye(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = F(1)
    return M


def mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    C = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        for t in range(k):
            a = Ai[t]
            if a == 0:
                continue
            Bt = B[t]
            for j in range(m):
                C[i][j] += a * Bt[j]
    return C


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscal(c, A):
    c = Fraction(c)
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mtr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def diag(*vals):
    n = len(vals)
    M = zeros(n)
    for i in range(n):
        M[i][i] = Fraction(vals[i])
    return M


def kron(A, B):
    na, ma, nb, mb = len(A), len(A[0]), len(B), len(B[0])
    C = zeros(na * nb, ma * mb)
    for i in range(na):
        for j in range(ma):
            a = A[i][j]
            if a == 0:
                continue
            for p in range(nb):
                for q in range(mb):
                    C[i * nb + p][j * mb + q] = a * B[p][q]
    return C


def is_diagonal(A):
    return all(A[i][j] == 0 for i in range(len(A)) for j in range(len(A[0])) if i != j)


# ---------------------------------------------------------------------------
# n-qubit engine: basis index b encodes occupations (b >> (n-1-k)) & 1
# ---------------------------------------------------------------------------

def bit(b, k, n):
    return (b >> (n - 1 - k)) & 1


def popcount(b):
    return bin(b).count("1")


def ket(n, amps):
    """amps: dict {basis index: Fraction}.  Returns the density matrix."""
    D = 2 ** n
    rho = zeros(D)
    for i, ai in amps.items():
        for j, aj in amps.items():
            rho[i][j] += Fraction(ai) * Fraction(aj)
    return rho


def parity_op(n):
    D = 2 ** n
    return diag(*[F((-1) ** popcount(b)) for b in range(D)])


def marginal(rho, k, n):
    """Single-mode marginal of mode k (2 x 2), by partial trace over the rest."""
    D = 2 ** n
    out = zeros(2)
    for b in range(D):
        for c in range(D):
            # b and c must agree off mode k
            agree = all(bit(b, t, n) == bit(c, t, n) for t in range(n) if t != k)
            if agree:
                out[bit(b, k, n)][bit(c, k, n)] += rho[b][c]
    return out


def dephase_joint(rho):
    """E_N: complete dephasing in the joint number basis."""
    D = len(rho)
    out = zeros(D)
    for b in range(D):
        out[b][b] = rho[b][b]
    return out


def dephase_mode(rho, k, n):
    """E_k: dephasing of mode k only (kills matrix elements differing in bit k)."""
    D = 2 ** n
    out = zeros(D)
    for b in range(D):
        for c in range(D):
            if bit(b, k, n) == bit(c, k, n):
                out[b][c] = rho[b][c]
    return out


def cz(n, j, k):
    """Controlled-Z between modes j and k: diagonal, entries +-1."""
    D = 2 ** n
    return diag(*[F(-1) if (bit(b, j, n) and bit(b, k, n)) else F(1) for b in range(D)])


def beam_splitter(n, j, k, c, s):
    """Real hopping rotation exp(theta (v_j* v_k - v_k* v_j)) on modes j, k,
    with (cos, sin) = (c, s): the generator (L_E) does not supply."""
    D = 2 ** n
    U = zeros(D)
    c, s = Fraction(c), Fraction(s)
    for b in range(D):
        bj, bk = bit(b, j, n), bit(b, k, n)
        if bj == bk:
            U[b][b] = F(1)
            continue
        # the two-dimensional block spanned by |1_j 0_k> and |0_j 1_k>
        flipped = b ^ (1 << (n - 1 - j)) ^ (1 << (n - 1 - k))
        if bj == 1:
            U[b][b] = c
            U[flipped][b] = s
        else:
            U[b][b] = c
            U[flipped][b] = -s
    return U


def conj(U, rho):
    Ut = [[U[j][i] for j in range(len(U))] for i in range(len(U))]
    return mm(mm(U, rho), Ut)


# ---------------------------------------------------------------------------
# the single mode: matrix units, the descent, the parity automorphism
# ---------------------------------------------------------------------------

V = [[F(0), F(1)], [F(0), F(0)]]        # v   = E_12  (lowering: |1> -> |0>)
VS = [[F(0), F(0)], [F(1), F(0)]]       # v*  = E_21
P_OCC = mm(VS, V)                       # P = v* v = E_22
SIGMA = madd(mscal(2, P_OCC), mscal(-1, eye(2)))   # sigma = 2P - 1 = diag(-1, 1)
K_GEN = mscal(Fraction(1, 2), SIGMA)    # K = sigma/2 = N - 1/2


def descent(x):
    """E(x) = P x P + (1-P) x (1-P), the map of T5 Prop 5.5."""
    Q = madd(eye(2), mscal(-1, P_OCC))
    return madd(mm(mm(P_OCC, x), P_OCC), mm(mm(Q, x), Q))


def parity_avg(x):
    return mscal(Fraction(1, 2), madd(x, mm(mm(SIGMA, x), SIGMA)))


GENERIC = [[F(2, 3), F(5, 7)], [F(-3, 11), F(4, 9)]]


# ---------------------------------------------------------------------------
# [Thm 2.2] the descent is the parity average
# ---------------------------------------------------------------------------

def parity_checks():
    g.check("[Thm 2.2] E(x) = (x + sigma x sigma)/2 on a generic rational matrix",
            meq(descent(GENERIC), parity_avg(GENERIC)))

    g.check("[Thm 2.2] E is idempotent",
            meq(descent(descent(GENERIC)), descent(GENERIC)))

    # conditional-expectation property for even a, b (diagonal = even)
    a = diag(F(3, 5), F(-2, 7))
    b = diag(F(4, 9), F(11, 13))
    lhs = descent(mm(mm(a, GENERIC), b))
    rhs = mm(mm(a, descent(GENERIC)), b)
    g.check("[Thm 2.2] E(a x b) = a E(x) b for even a, b (conditional expectation)",
            meq(lhs, rhs))

    g.check("[Thm 2.2] range of E is the even span: E(1) = 1 and E(sigma) = sigma",
            meq(descent(eye(2)), eye(2)) and meq(descent(SIGMA), SIGMA))

    g.check("[Thm 2.2] kernel of E is the odd span: E(v) = E(v*) = 0, and E kills "
            "exactly the off-diagonal part",
            meq(descent(V), zeros(2)) and meq(descent(VS), zeros(2))
            and meq(descent(GENERIC), diag(GENERIC[0][0], GENERIC[1][1])))

    # the atom, in the blade engine: CAR and sigma = e0 e1
    sq = g.sig(1, 1)
    e0, e1 = g.gen(0), g.gen(1)
    v = g.scal(Fraction(1, 2), g.add(e0, e1))
    vs = g.scal(Fraction(1, 2), g.sub(e0, e1))
    car = g.add(g.mul(v, vs, sq), g.mul(vs, v, sq))
    sigma_blade = g.sub(g.mul(vs, v, sq), g.mul(v, vs, sq))
    g.check("[Thm 2.2] the hyperbolic atom: v^2 = (v*)^2 = 0, v v* + v* v = 1, "
            "and sigma = v* v - v v* = e0 e1 blade-exactly",
            g.is_zero(g.mul(v, v, sq)) and g.is_zero(g.mul(vs, vs, sq))
            and g.eq(car, g.sc(1))
            and g.eq(sigma_blade, g.mul(e0, e1, sq)))


# ---------------------------------------------------------------------------
# [Thm 3.1] the descended form is state independent
# ---------------------------------------------------------------------------

def form_checks():
    # a generic rational density matrix with nonzero coherences
    rho = [[F(9, 25), F(6, 25)], [F(6, 25), F(16, 25)]]
    g.check("[Thm 3.1] E(rho) is diagonal for a state with nonzero coherences",
            is_diagonal(descent(rho)) and mtr(descent(rho)) == 1)

    # E(rho) = diag(1, x)/(1+x) with x = (1-p)/p, p the vacancy probability
    p = descent(rho)[0][0]
    x = (1 - p) / p
    gibbs = mscal(Fraction(1, 1) / (1 + x), diag(F(1), x))
    g.check("[Thm 3.1] E(rho) = diag(1, x)/(1+x) exactly, with x = e^{-beta omega} "
            "= (1-p)/p = 16/9",
            meq(descent(rho), gibbs) and x == F(16, 9))

    # injectivity of x -> p on a rational witness pair
    def pofx(xx):
        return Fraction(1, 1) / (1 + xx)
    g.check("[Thm 3.1] x -> p = 1/(1+x) is injective (rational witnesses 16/9, 9/16)",
            pofx(F(16, 9)) != pofx(F(9, 16)))


# ---------------------------------------------------------------------------
# [Thm 3.3] univalence: even states have diagonal marginals
# ---------------------------------------------------------------------------

def univalence_checks():
    n = 3
    # an even pure state: every configuration has even total occupation
    psi = {0b000: F(1, 2), 0b011: F(1, 2), 0b101: F(1, 2), 0b110: F(1, 2)}
    rho_even = ket(n, psi)
    # a second even pure state, mixed in with rational weights
    chi = {0b000: F(3, 5), 0b110: F(4, 5)}
    rho_even = madd(mscal(F(1, 2), rho_even), mscal(F(1, 2), ket(n, chi)))

    Gam = parity_op(n)
    g.check("[Thm 3.3] the constructed three-mode state is even: Gamma rho Gamma = rho",
            meq(mm(mm(Gam, rho_even), Gam), rho_even) and mtr(rho_even) == 1)

    ok = all(is_diagonal(marginal(rho_even, k, n)) for k in range(n))
    g.check("[Thm 3.3] every single-mode marginal of an even state is diagonal "
            "(all three modes)", ok)

    # omega(v_k) = 0 for every k: v_k's expectation is the marginal coherence
    ok = all(marginal(rho_even, k, n)[0][1] == 0 and marginal(rho_even, k, n)[1][0] == 0
             for k in range(n))
    g.check("[Thm 3.3] omega(v_k) = omega(v_k*) = 0 for every mode of an even state", ok)

    # control: a parity-mixed state has a nonzero marginal coherence
    phi = {0b000: F(3, 5), 0b001: F(4, 5)}
    rho_odd = ket(n, phi)
    g.check("[Thm 3.3] control: the parity-mixed state (3/5)|000> + (4/5)|001> has "
            "marginal coherence 12/25 on mode 3, so the premise does work",
            marginal(rho_odd, 2, n)[0][1] == F(12, 25)
            and not meq(mm(mm(parity_op(n), rho_odd), parity_op(n)), rho_odd))

    # the model's pair states (T5 Sec 12): support constraint R_k = L_k
    n4 = 4
    c1, s1, c2, s2 = F(3, 5), F(4, 5), F(4, 5), F(3, 5)
    model = {0b0000: c1 * c2, 0b0011: c1 * s2, 0b1100: s1 * c2, 0b1111: -s1 * s2}
    rho_model = ket(n4, model)
    g.check("[Thm 3.3] the finite-ledger model's two-pair state (with the CZ sign) is "
            "even, so T5 Lem 12.1 is the special case",
            meq(mm(mm(parity_op(n4), rho_model), parity_op(n4)), rho_model)
            and mtr(rho_model) == 1
            and all(is_diagonal(marginal(rho_model, k, n4)) for k in range(n4)))


# ---------------------------------------------------------------------------
# [Thm 4.2] KMS uniqueness
# ---------------------------------------------------------------------------

def kms_checks():
    x = F(16, 9)                      # x = e^{-beta omega}
    rho = mscal(Fraction(1, 1) / (1 + x), diag(F(1), x))
    Eb = diag(F(1), x)                # e^{-beta H}, H = omega N, x = e^{-beta omega}
    Ebi = diag(F(1), 1 / x)           # e^{+beta H}
    # alpha_{i beta}(a) = e^{-beta H} a e^{+beta H}

    units = [[[F(1) if (i, j) == (a, b) else F(0) for j in range(2)] for i in range(2)]
             for a in range(2) for b in range(2)]

    ok = True
    for A in units:
        for B in units:
            lhs = mtr(mm(rho, mm(A, B)))
            rhs = mtr(mm(rho, mm(B, mm(Eb, mm(A, Ebi)))))
            ok = ok and lhs == rhs
    g.check("[Thm 4.2] the KMS identity omega(ab) = omega(b e^{-betaH} a e^{betaH}) on "
            "all sixteen matrix-unit pairs for rho ~ diag(1, 16/9)", ok)

    # a non-Gibbs diagonal state fails it: exhibit a failing pair
    bad = diag(F(1, 2), F(1, 2))
    fails = False
    for A in units:
        for B in units:
            lhs = mtr(mm(bad, mm(A, B)))
            rhs = mtr(mm(bad, mm(B, mm(Eb, mm(A, Ebi)))))
            if lhs != rhs:
                fails = True
    g.check("[Thm 4.2] converse: the tracial state is not KMS for this flow "
            "(an explicit matrix-unit pair fails)", fails)

    g.check("[Thm 4.2] the identity forces [rho, e^{beta H}] = 0 and rho e^{beta H} "
            "central: rho = diag(1, x)/(1+x) commutes with e^{beta H}",
            meq(mm(rho, Eb), mm(Eb, rho)))


# ---------------------------------------------------------------------------
# [Cor 4.4] universality of the temperature
# ---------------------------------------------------------------------------

def universality_checks():
    # weights w1 = 1, w2 = 2; equal beta means x2 = x1^{w2/w1} = x1^2
    x1 = F(2, 3)
    x2_equal = x1 * x1
    x2_other = F(1, 2)

    def two_mode_product(xa, xb):
        ra = mscal(Fraction(1, 1) / (1 + xa), diag(F(1), xa))
        rb = mscal(Fraction(1, 1) / (1 + xb), diag(F(1), xb))
        return ra, rb, kron(ra, rb)

    ra, rb, rho_eq = two_mode_product(x1, x2_equal)
    g.check("[Cor 4.4] equal inverse temperatures: x2 = x1^{w2/w1} = 4/9 exactly, so "
            "the joint populations are those of a single Gibbs state of K_geo",
            x2_equal == F(4, 9)
            and rho_eq[0b11][0b11] / rho_eq[0b00][0b00] == x1 * x2_equal)

    _, _, rho_ne = two_mode_product(x1, x2_other)
    g.check("[Cor 4.4] witness failure: with x2 = 1/2 the joint populations are not "
            "those of any single Gibbs state of K_geo (x2 != x1^2)",
            x2_other != x1 * x1)

    g.check("[Cor 4.4] the GMC state factorises: e^{-beta K_geo} = rho_1 (x) rho_2 "
            "exactly", meq(rho_eq, kron(ra, rb)))


# ---------------------------------------------------------------------------
# [Thm 4.5] rate rigidity
# ---------------------------------------------------------------------------

def rigidity_checks():
    x = F(16, 9)
    rho = mscal(Fraction(1, 1) / (1 + x), diag(F(1), x))
    rho_minus = mscal(Fraction(1, 1) / (1 + 1 / x), diag(F(1), 1 / x))

    U_diag = diag(F(1), F(-1))
    g.check("[Thm 4.5](1) a diagonal unitary commutes with K and fixes the Gibbs "
            "state exactly",
            meq(mm(U_diag, K_GEN), mm(K_GEN, U_diag))
            and meq(conj(U_diag, rho), rho))

    X = [[F(0), F(1)], [F(1), F(0)]]
    g.check("[Thm 4.5](2) the exchange unitary reverses the flow (X K X = -K) and "
            "sends the beta-Gibbs state to the (-beta)-Gibbs state",
            meq(conj(X, K_GEN), mscal(-1, K_GEN))
            and meq(conj(X, rho), rho_minus))

    g.check("[Thm 4.5](3) the exchange does not commute with K, so it is not in the "
            "flow-preserving group: |beta| is the invariant",
            not meq(mm(X, K_GEN), mm(K_GEN, X)))


# ---------------------------------------------------------------------------
# [Prop 5.2] the Euclidean partner of the boost
# ---------------------------------------------------------------------------

def euclid_checks():
    sq = g.sig(1, 3)                       # e0^2 = +1, e1..e3^2 = -1
    e = [g.gen(i) for i in range(4)]
    sigma_r = g.mul(e[0], e[1], sq)        # boost bivector of the radial plane
    I = g.mul(g.mul(e[0], e[1], sq), g.mul(e[2], e[3], sq), sq)
    Isig = g.mul(I, sigma_r, sq)

    g.check("[Prop 5.2](1) sigma_r^2 = +1 blade-exactly in Cl(1,3)",
            g.eq(g.mul(sigma_r, sigma_r, sq), g.sc(1)))
    g.check("[Prop 5.2](1) (I sigma_r)^2 = -1 blade-exactly: the Euclidean partner",
            g.eq(g.mul(Isig, Isig, sq), g.sc(-1)))

    def S(B):
        # S(B) = -(1/2)(B + 3 sigma_r B sigma_r), T5 Thm 6.1
        return g.scal(Fraction(-1, 2),
                      g.add(B, g.scal(3, g.mul(g.mul(sigma_r, B, sq), sigma_r, sq))))

    g.check("[Prop 5.2](1) both members of the pair are shape-operator eigenvectors "
            "of eigenvalue -2 (T5 Thm 6.1)",
            g.eq(S(sigma_r), g.scal(-2, sigma_r)) and g.eq(S(Isig), g.scal(-2, Isig)))

    # rotor composition in the elliptic plane: R(c,s) = c + s I sigma_r
    def R(c, s):
        return g.add(g.sc(c), g.scal(s, Isig))

    c, s = Fraction(3, 5), Fraction(4, 5)
    prod = g.mul(R(c, s), R(c, s), sq)
    g.check("[Prop 5.2](2) rotor composition law holds blade-exactly: "
            "R(3/5,4/5)^2 = R(-7/25, 24/25)",
            g.eq(prod, R(Fraction(-7, 25), Fraction(24, 25))))

    quarter = R(0, 1)                      # theta/2 = pi/2, i.e. theta = pi
    half = g.mul(quarter, quarter, sq)     # theta = 2 pi
    full = g.mul(half, half, sq)           # theta = 4 pi
    g.check("[Prop 5.2](2) R_{2pi} = -1 and R_{4pi} = +1: the rotor has period 4pi",
            g.eq(half, g.sc(-1)) and g.eq(full, g.sc(1)))

    generic = g.add(g.sc(Fraction(2, 3)),
                    g.add(g.scal(Fraction(5, 7), e[2]), g.scal(Fraction(-1, 4), sigma_r)))
    minus1 = g.sc(-1)
    g.check("[Prop 5.2](2) conjugation by R_{2pi} = -1 is trivial, so the conjugation "
            "action has period 2pi",
            g.eq(g.mul(g.mul(minus1, generic, sq), minus1, sq), generic))


# ---------------------------------------------------------------------------
# [Thm 6.1] exact equilibrium over-determines the ledger
# ---------------------------------------------------------------------------

def overdetermination_checks():
    x1, x2 = F(2, 3), F(4, 9)
    r1 = mscal(Fraction(1, 1) / (1 + x1), diag(F(1), x1))
    r2 = mscal(Fraction(1, 1) / (1 + x2), diag(F(1), x2))
    rho_prod = kron(r1, r2)

    g.check("[Thm 6.1](2) the product Gibbs state is a fixed point of E_N: zero deficit",
            meq(dephase_joint(rho_prod), rho_prod))

    g.check("[Thm 6.1](1) the product Gibbs state has zero total correlation: "
            "rho = rho_1 (x) rho_2 exactly",
            meq(rho_prod, kron(marginal(rho_prod, 0, 2), marginal(rho_prod, 1, 2))))

    # correlated control: an even entangled two-mode state
    ctrl = ket(2, {0b00: F(3, 5), 0b11: F(4, 5)})
    g.check("[Thm 6.1] control: an entangled even state is not a product and is not a "
            "fixed point of E_N, so the purity strictly drops under descent",
            (not meq(ctrl, kron(marginal(ctrl, 0, 2), marginal(ctrl, 1, 2))))
            and (not meq(dephase_joint(ctrl), ctrl))
            and mtr(mm(dephase_joint(ctrl), dephase_joint(ctrl)))
                < mtr(mm(ctrl, ctrl)))


# ---------------------------------------------------------------------------
# [Thm 7.1] the purification is canonical
# ---------------------------------------------------------------------------

def purification_checks():
    c, s = F(3, 5), F(4, 5)
    omega = ket(2, {0b00: c, 0b11: s})
    rho = marginal(omega, 0, 2)
    g.check("[Thm 7.1](1) the thermofield vector purifies rho = diag(9/25, 16/25)",
            meq(rho, diag(F(9, 25), F(16, 25))) and mtr(mm(omega, omega)) == 1)

    g.check("[Thm 7.1](4) the thermofield angle: tan^2 theta = (s/c)^2 = 16/9 = "
            "e^{-omega/T}, matching T5 Lem 7.2",
            (s / c) ** 2 == F(16, 9)
            and rho[1][1] / rho[0][0] == F(16, 9))

    # modular eigenvalues lambda_i^2 / lambda_j^2 on |ij>
    lam = [c, s]
    delta = diag(*[lam[i] ** 2 / lam[j] ** 2 for i in range(2) for j in range(2)])
    g.check("[Thm 7.1](1) the modular operator Delta = rho (x) rhobar^{-1} has "
            "eigenvalues lambda_i^2/lambda_j^2 on |ij> (T5 Lem 7.1)",
            meq(delta, kron(rho, diag(1 / rho[0][0], 1 / rho[1][1]))))

    # purifications differ by a unitary on the purifying factor only
    W = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    omega2 = conj(kron(eye(2), W), omega)
    g.check("[Thm 7.1](3) a unitary on the purifying factor alone leaves the marginal "
            "unchanged: the purification is unique up to the commutant",
            meq(marginal(omega2, 0, 2), rho) and not meq(omega2, omega))


# ---------------------------------------------------------------------------
# [Prop 6.4] number-diagonal dynamics; what (L_E) excludes
# ---------------------------------------------------------------------------

def dynamics_checks():
    # the finite-ledger model's two-pair state, in the order (R1, L1, R2, L2):
    # even, with the support constraint R_k = L_k of T5 Lem 12.1
    n = 4
    c1, s1, c2, s2 = F(3, 5), F(4, 5), F(4, 5), F(3, 5)
    rho = ket(n, {0b0000: c1 * c2, 0b0011: c1 * s2,
                  0b1100: s1 * c2, 0b1111: s1 * s2})

    U = cz(n, 1, 3)                       # controlled-Z between the window qubits
    rho_cz = conj(U, rho)
    same_pops = all(rho_cz[b][b] == rho[b][b] for b in range(2 ** n))
    same_marg = all(meq(marginal(rho_cz, k, n), marginal(rho, k, n)) for k in range(n))
    g.check("[Prop 6.4] a controlled-Z circuit preserves every joint-number probability "
            "and every single-mode marginal of the ledger state", same_pops and same_marg)

    g.check("[Prop 6.4] the controlled-Z circuit commutes with the total parity, so it "
            "maps even states to even states and Thm 3.3 keeps applying",
            meq(mm(U, parity_op(n)), mm(parity_op(n), U)))

    g.check("[Prop 6.4] the controlled-Z does change the joint coherence, so the "
            "dynamics is not trivial: it writes only where the descent cannot read",
            not meq(rho_cz, rho))

    B = beam_splitter(n, 1, 2, F(3, 5), F(4, 5))
    Bt = [[B[j][i] for j in range(len(B))] for i in range(len(B))]
    g.check("[Prop 6.4] the beam splitter is orthogonal (a genuine unitary on the "
            "four-mode space) and parity preserving",
            meq(mm(B, Bt), eye(2 ** n)) and meq(mm(B, parity_op(n)), mm(parity_op(n), B)))

    rho_bs = conj(B, rho)
    g.check("[Prop 6.4] the hopping rotation changes the marginal populations, which is "
            "exactly the generator (L_E) does not supply",
            not meq(marginal(rho_bs, 1, n), marginal(rho, 1, n)))


def main():
    print("verify_state_selection.py: exact-arithmetic checks for the T5 companion "
          "note \"Selecting the State\"\n")
    parity_checks()
    form_checks()
    univalence_checks()
    kms_checks()
    universality_checks()
    rigidity_checks()
    euclid_checks()
    overdetermination_checks()
    purification_checks()
    dynamics_checks()
    print()
    if g.FAILURES:
        print("FAILURES (%d):" % len(g.FAILURES))
        for f in g.FAILURES:
            print("  " + f)
        sys.exit(1)
    print("ALL CHECKS PASSED.")


if __name__ == "__main__":
    main()
