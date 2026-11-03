"""synthesis.crossing-transport-tipler-threshold-sharp: exact checks.

Tractor x = (sigma, mu_0..mu_3, rho) in a parallel frame, eta = diag(-1, 1, 1, 1); along a causal geodesic
with tangent X the transport is x' = A x, A = E_X + N_{P(X)} (store convention of
interior.imported-tractor-connection, as in synthesis.tractor-transport-weak-null-crossing), with
P(X) = S nu n, n null, nu = n(X).
  check_subsystem:   w := <n, mu> and rho obey w' = -nu rho, rho' = -nu S w (row-vector identities
                     w A = -nu rho, rho A = -nu S w, for several (X, n) and rational S), so w'' = nu^2 S w.
  check_commutator:  D = [E_X, N_n] satisfies D^3 = nu^2 D, D != 0, and has eigenvalues 0, nu, -nu with
                     kernel dimension 2 (so the residue (k/nu) D has eigenvalues 0, +-k); the gauge identity
                     (1 - f N_n) A (1 + f N_n) - f' N_n = E_X + f D when f' = nu (S - f^2).
  check_euler:       generalised polynomials sum c_e t^e (rational exponents e): for S = C t^-2 with
                     nu^2 C = k (k - 1), y = t^k and t^(1-k) solve y'' = nu^2 S y; f = -k/(nu t) solves the
                     Riccati in s (d/ds = -d/dt); t S is homogeneous of degree -1, so every dyadic shell
                     [2^-(m+1), 2^-m] carries the same Tipler integral (unbounded sum).
  check_power_profiles: S = C t^(2 beta - 2): the Frobenius series y = sum a_j t^(2 beta j) solves
                     y'' = nu^2 S y up to its top term, exactly; y' leads with nu^2 C t^(2beta-1)/(2beta-1);
                     Tipler integral int_0^1 t S dt = C/(2 beta); partial L^1 integrals at eps = 8^-m for
                     beta = 1/3 grow like 2^m (not integrable), and are bounded for beta = 2/3.
"""
from fractions import Fraction as F
import GA  # noqa: F401  (house rule; the computation is exact matrix and exponent arithmetic)
from tp_premise import premise

ETA = [F(-1), F(1), F(1), F(1)]


def zeros():
    return [[F(0)] * 6 for _ in range(6)]


def E(X):
    M = zeros()
    for a in range(4):
        M[0][1 + a] = F(X[a])
        M[1 + a][5] = -ETA[a] * X[a]
    return M


def N(v):
    M = zeros()
    for b in range(4):
        M[1 + b][0] = F(v[b])
        M[5][1 + b] = -F(v[b]) * ETA[b]
    return M


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(6)) for j in range(6)] for i in range(6)]


def lin(A, B, c=1):
    return [[A[i][j] + c * B[i][j] for j in range(6)] for i in range(6)]


def vm(v, A):
    return [sum(v[k] * A[k][j] for k in range(6)) for j in range(6)]


def rank(A):
    M = [row[:] for row in A]
    r = 0
    for c in range(6):
        p = next((i for i in range(r, 6) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        for i in range(6):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
    return r


FRAMES = [((5, 3, 4, 0), (2, 1, 1, 0)), ((13, 5, 12, 0), (3, 0, 1, 1)), ((3, 1, 2, 2), (1, 0, 0, 0)),
          ((9, 1, 4, 8), (5, 1, 2, 3)), ((1, 1, 0, 0), (1, 1, 0, 0))]


def frames():
    out = []
    for n, X in FRAMES:
        assert sum(ETA[a] * n[a] * n[a] for a in range(4)) == 0                      # n null
        assert sum(ETA[a] * X[a] * X[a] for a in range(4)) <= 0                      # X causal
        nu = sum(n[a] * X[a] for a in range(4))
        assert nu != 0
        out.append((n, X, nu))
    return out


def check_subsystem():
    premise("interior.imported-tractor-connection")
    premise("synthesis.tractor-transport-weak-null-crossing")
    for n, X, nu in frames():
        for S in (F(0), F(1), F(-3, 7), F(11, 2), F(250)):
            A = lin(E(X), N(n), S * nu)
            w = [F(0)] + [ETA[b] * n[b] for b in range(4)] + [F(0)]
            rho = [F(0)] * 5 + [F(1)]
            assert vm(w, A) == [-nu * r for r in rho]                 # w' = -nu rho
            assert vm(rho, A) == [-nu * S * x for x in w]             # rho' = -nu S w
            # second derivative of the functional w along x' = A x (A constant in s here, S frozen):
            assert vm(vm(w, A), A) == [nu * nu * S * x for x in w]    # w'' = nu^2 S w
    return True


def check_commutator():
    premise("interior.imported-tractor-connection")
    premise("synthesis.tractor-transport-weak-null-crossing")
    for n, X, nu in frames():
        D = lin(mm(E(X), N(n)), mm(N(n), E(X)), -1)
        assert D != zeros()
        D3 = mm(D, mm(D, D))
        assert D3 == [[nu * nu * x for x in row] for row in D]       # D^3 = nu^2 D
        assert rank(D) == 4                                          # kernel of dimension 2
        I = [[F(int(i == j)) for j in range(6)] for i in range(6)]
        assert rank(lin(D, I, -nu)) == 4 and rank(lin(D, I, nu)) == 4  # eigenvalues +-nu, each twice
        # D acts by nu on sigma and by -nu on rho
        assert D[0][0] == nu and D[5][5] == -nu
        # gauge identity at rational values, f' fixed by the Riccati
        for S, f in ((F(2), F(1, 3)), (F(-1), F(5)), (F(7, 4), F(-2))):
            A = lin(E(X), N(n), S * nu)
            G = lin(I, N(n), f)
            Gi = lin(I, N(n), -f)
            fp = nu * (S - f * f)
            lhs = lin(mm(Gi, mm(A, G)), N(n), -fp)
            assert lhs == lin(E(X), D, f)
            assert lhs[0][0] == f * nu                               # the sigma entry of f D
            # with a wrong f' the S-term survives: the Riccati is needed
            bad = lin(mm(Gi, mm(A, G)), N(n), -(fp + 1))
            assert bad != lin(E(X), D, f)
    # worked frame n = (5, 3, 4, 0), X = (2, 1, 1, 0): nu = 17, Riccati values f' = 289/9, -442, -153/4
    n0, X0, nu0 = frames()[0]
    assert nu0 == 17
    assert [nu0 * (S - f * f) for S, f in ((F(2), F(1, 3)), (F(-1), F(5)), (F(7, 4), F(-2)))] == \
        [F(289, 9), F(-442), F(-153, 4)]
    return True


# generalised polynomials: dict exponent (Fraction) -> coefficient (Fraction)
def gp_mul(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            out[e1 + e2] = out.get(e1 + e2, F(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def gp_d(p):
    return {e - 1: c * e for e, c in p.items() if c * e != 0}


def gp_sub(p, q):
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, F(0)) - c
    return {e: c for e, c in out.items() if c != 0}


def check_euler():
    premise("synthesis.tractor-transport-weak-null-crossing")
    premise("interior.sign-fixed-internally")
    for k, nu in ((F(2), F(17)), (F(3), F(1)), (F(5, 2), F(3))):
        C = k * (k - 1) / (nu * nu)
        S = {F(-2): C}
        for y in ({k: F(1)}, {1 - k: F(1)}):
            assert gp_sub(gp_d(gp_d(y)), gp_mul({F(0): nu * nu}, gp_mul(S, y))) == {}
        assert 1 - k < 0 < k - 1                                     # t^(1-k) unbounded, t^k -> 0
        # Riccati in s (d/ds = -d/dt) for f = y'/(nu y) with y = t^k: f = -k/(nu t)
        f = {F(-1): -k / nu}
        fs = {e: -c for e, c in gp_d(f).items()}                     # df/ds
        assert gp_sub(fs, gp_mul({F(0): nu}, gp_sub(S, gp_mul(f, f)))) == {}
        # homogeneity: t S(t) = C t^-1; under t -> t/2 the measure t S dt is invariant
        tS = gp_mul({F(1): F(1)}, S)
        assert tS == {F(-1): C}
        assert all(c * F(1, 2) ** (e + 1) == c for e, c in tS.items())  # (t/2) S(t/2) d(t/2) = t S dt
    # focusing sign (S <= 0 in the store convention): S = -C t^-2 with nu^2 C = e(1 - e), real e in (0, 1)
    for e, nu in ((F(1, 3), F(3)), (F(1, 4), F(2)), (F(1, 2), F(1))):
        C = e * (1 - e) / (nu * nu)
        S = {F(-2): -C}
        for y in ({e: F(1)}, {1 - e: F(1)}):
            assert gp_sub(gp_d(gp_d(y)), gp_mul({F(0): nu * nu}, gp_mul(S, y))) == {}
        assert 0 < e <= 1 - e < 1                                    # both solutions tend to 0: crush
        assert min(gp_d({e: F(1)})) == e - 1 and -1 < e - 1 < 0      # rho ~ t^(e-1): unbounded, integrable
    # complex case nu^2 C = 1/4 + omega^2: exponents 1/2 +- I omega (Gaussian rationals), real part 1/2 > 0
    for om in (F(1), F(3, 2)):
        re, im = F(1, 2), om
        # e (e - 1) = (re^2 - im^2 - re) + I (2 re im - im)
        assert (re * re - im * im - re, 2 * re * im - im) == (-(F(1, 4) + om * om), F(0))
    return True


def check_power_profiles():
    premise("synthesis.tractor-transport-weak-null-crossing")
    for beta, C, nu in ((F(1, 3), F(2), F(3)), (F(2, 3), F(1), F(1)), (F(1, 5), F(5), F(2))):
        J = 6
        a = [F(1)]
        for j in range(1, J + 1):
            e = 2 * beta * j
            assert e != 1
            a.append(nu * nu * C * a[-1] / (e * (e - 1)))
        y = {2 * beta * j: a[j] for j in range(J + 1)}
        S = {2 * beta - 2: C}
        res = gp_sub(gp_d(gp_d(y)), gp_mul({F(0): nu * nu}, gp_mul(S, y)))
        assert res == {2 * beta * (J + 1) - 2: -nu * nu * C * a[J]}   # only the truncation term
        yp = gp_d(y)
        lead = min(yp)
        assert lead == 2 * beta - 1 and yp[lead] == nu * nu * C / (2 * beta - 1)
        # Tipler: antiderivative of t S = C t^(2 beta - 1) is C t^(2 beta)/(2 beta), finite at 0 for beta > 0
        assert gp_d({2 * beta: C / (2 * beta)}) == {2 * beta - 1: C}
    # L^1: int_eps^1 t^(2beta-2) dt = (1 - eps^(2beta-1))/(2beta-1); beta = 1/3, eps = 8^-m: eps^(-1/3) = 2^m
    vals = [(1 - F(2) ** m) / (F(2, 3) - 1) for m in range(1, 8)]
    assert all(vals[j + 1] > vals[j] for j in range(6)) and vals[6] == 381
    # beta = 2/3: eps^(1/3) = 2^-m, integral (1 - 2^-m)/(1/3) < 3 for all m
    assert all((1 - F(1, 2 ** m)) * 3 < 3 for m in range(1, 30))
    return True
