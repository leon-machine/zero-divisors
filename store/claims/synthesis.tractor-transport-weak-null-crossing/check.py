"""synthesis.tractor-transport-weak-null-crossing: exact checks.

Polynomials over Fractions in the symbols S (the singular Schouten coefficient), f (the gauge function),
and, for the explicit null and timelike frames, the regular components. The transport equation along
gamma in a parallel frame, store convention of interior.imported-tractor-connection:
    sigma' = mu(X),  mu_b' = -X_b rho + P(X)_b sigma,  rho' = -eta^{bc} P(X)_c mu_b,
i.e. A = E_X + N_{P(X)} with E_X the soldering part and N_v the nilpotent map
    N_v : sigma -> (mu += v sigma),  mu -> (rho -= eta^{-1}(v, mu)).
The gauge is G = 1 + f N_n with n null (N_n^2 = 0), and Ahat = G^-1 A G - G^-1 G'.

  check_general_removal:   for fixed rational data (eta = diag(-1,1,1,1), causal X, null n with
                           nu = n(X) != 0, regular covector R), with P(X) = S nu n + R and the Riccati
                           f' = nu (S - f^2): Ahat = E_X + N_R + f [E_X, N_n] exactly; also
                           N_n E_X N_n = nu N_n, N_n N_R N_n = 0, N_n^2 = 0, and A preserves the
                           tractor metric.
  check_null_and_radial_frames: the two explicit frames of the proof (null generator with dilation,
                           radial timelike crossing with the null gauge): the gauged connection is free
                           of S and at most linear in f.
  check_model_profile:     the model y = 1 + t, t = (s_c - s)^(1/2): S = y''/(nu^2 y) is exact in t,
                           |S| ~ t^-3 (not integrable in s, ds = 2t dt) while |s - s_c||S| ~ t^-1
                           (integrable), and f = y'/(nu y) ~ t^-1 is integrable but unbounded.
"""
from fractions import Fraction as F
from itertools import product
import GA  # noqa: F401  (house rule; the computation is polynomial algebra over Fractions)
from tp_premise import premise
import gtg


class Det:
    """Deterministic integer sequence (linear congruential, exact integers only) supplying fixed
    rational test points; replaces pseudo-random sampling so the check is reproducible and exact."""

    def __init__(self, seed):
        self.x = seed

    def _next(self):
        self.x = (self.x * 1103515245 + 12345) % 2147483648
        return self.x // 65536

    def randint(self, lo, hi):
        return lo + self._next() % (hi - lo + 1)

    def choice(self, seq):
        return seq[self._next() % len(seq)]

    def sample(self, seq, k):
        pool = list(seq)
        out = []
        for _ in range(k):
            out.append(pool.pop(self._next() % len(pool)))
        return out

VARS = ("S", "f")


class P:
    def __init__(self, d=None):
        self.d = {k: F(v) for k, v in (d or {}).items() if v != 0}

    @staticmethod
    def c(x):
        return P({(0, 0): x})

    def __add__(s, o):
        o = o if isinstance(o, P) else P.c(o)
        d = dict(s.d)
        for k, v in o.d.items():
            d[k] = d.get(k, F(0)) + v
        return P(d)
    __radd__ = __add__

    def __neg__(s):
        return P({k: -v for k, v in s.d.items()})

    def __sub__(s, o):
        return s + (-(o if isinstance(o, P) else P.c(o)))

    def __mul__(s, o):
        o = o if isinstance(o, P) else P.c(o)
        d = {}
        for (k1, v1), (k2, v2) in product(s.d.items(), o.d.items()):
            k = (k1[0] + k2[0], k1[1] + k2[1])
            d[k] = d.get(k, F(0)) + v1 * v2
        return P(d)
    __rmul__ = __mul__

    def __eq__(s, o):
        return (s - o).d == {}

    def deg(s, i):
        return max((k[i] for k in s.d), default=0)

    def ddl(s, fprime):
        out = P()
        for k, c in s.d.items():
            assert k[0] == 0, "gauge must not depend on S"
            if k[1]:
                out = out + P({(0, k[1] - 1): c * k[1]}) * fprime
        return out


Sy, fy = P({(1, 0): 1}), P({(0, 1): 1})
DIM = 6           # (sigma, mu_0..mu_3, rho)
SIG, RHO = 0, 5
ETA = [F(-1), F(1), F(1), F(1)]


def zeros():
    return [[P() for _ in range(DIM)] for _ in range(DIM)]


def eye():
    M = zeros()
    for i in range(DIM):
        M[i][i] = P.c(1)
    return M


def mm(A, B):
    C = zeros()
    for i in range(DIM):
        for j in range(DIM):
            s = P()
            for k in range(DIM):
                if A[i][k].d and B[k][j].d:
                    s = s + A[i][k] * B[k][j]
            C[i][j] = s
    return C


def add(A, B, cb=1):
    return [[A[i][j] + B[i][j] * cb for j in range(DIM)] for i in range(DIM)]


def scale(A, p):
    return [[A[i][j] * p for j in range(DIM)] for i in range(DIM)]


def N(v):
    """v: covector (4 entries, may be P)."""
    M = zeros()
    for b in range(4):
        M[1 + b][SIG] = v[b] if isinstance(v[b], P) else P.c(v[b])
        M[RHO][1 + b] = -(v[b] if isinstance(v[b], P) else P.c(v[b])) * ETA[b]
    return M


def E(X):
    M = zeros()
    for a in range(4):
        M[SIG][1 + a] = P.c(X[a])
        M[1 + a][RHO] = P.c(-ETA[a] * X[a])
    return M


def eta_t():
    M = zeros()
    M[SIG][RHO] = M[RHO][SIG] = P.c(1)
    for a in range(4):
        M[1 + a][1 + a] = P.c(ETA[a])     # eta^{ab} on lower-index mu (diagonal, eta^-1 = eta)
    return M


def tr(A):
    return [[A[j][i] for j in range(DIM)] for i in range(DIM)]


def same(A, B):
    return all(A[i][j] == B[i][j] for i in range(DIM) for j in range(DIM))


NULLS = [(5, 3, 4, 0), (13, 5, 12, 0), (3, 1, 2, 2), (9, 1, 4, 8), (7, 2, 3, 6)]


def check_general_removal():
    premise("interior.imported-tractor-connection")
    # explicit instance: n = (5, 3, 4, 0) null, X = (2, 1, 1, 0) timelike, nu = n(X) = 17. The commutator
    # [E_X, N_n] is the g_0 element: nu on sigma, -nu on rho, and the Lorentz generator
    # mu -> X^flat <n, mu> - n <X^flat, mu>-type block on mu.
    n0 = [F(5), F(3), F(4), F(0)]
    X0 = [F(2), F(1), F(1), F(0)]
    assert sum(ETA[a] * n0[a] * n0[a] for a in range(4)) == 0
    assert sum(ETA[a] * X0[a] * X0[a] for a in range(4)) == -2
    nu0 = sum(n0[a] * X0[a] for a in range(4))
    assert nu0 == 17
    cm0 = add(mm(E(X0), N(n0)), mm(N(n0), E(X0)), -1)
    expect = {(0, 0): 17, (5, 5): -17, (1, 2): -11, (1, 3): -13, (2, 1): -11, (2, 3): 1,
              (3, 1): -13, (3, 2): -1}
    for i in range(DIM):
        for j in range(DIM):
            assert cm0[i][j] == P.c(expect.get((i, j), 0)), (i, j)
    assert same(mm(mm(N(n0), E(X0)), N(n0)), scale(N(n0), P.c(17)))
    rng = Det(1022)
    for _ in range(25):
        nv = list(map(F, rng.choice(NULLS)))
        sgn = [rng.choice((1, -1)) for _ in range(3)]
        perm = rng.sample([1, 2, 3], 3)
        n = [nv[0]] + [sgn[i] * nv[perm[i]] for i in range(3)]          # null covector
        assert sum(ETA[a] * n[a] * n[a] for a in range(4)) == 0
        while True:
            X = [F(rng.randint(-6, 6), rng.randint(1, 3)) for _ in range(4)]
            if sum(ETA[a] * X[a] * X[a] for a in range(4)) <= 0 and sum(n[a] * X[a] for a in range(4)) != 0:
                break
        if rng.randint(0, 9) < 4:                                         # a null tangent
            X = [x for x in map(F, rng.choice(NULLS))]
            if sum(n[a] * X[a] for a in range(4)) == 0:
                continue
        nu = sum(n[a] * X[a] for a in range(4))
        R = [F(rng.randint(-5, 5), rng.randint(1, 4)) for _ in range(4)]
        PX = [Sy * (nu * n[b]) + R[b] for b in range(4)]
        A = add(E(X), N(PX))
        # A preserves the tractor metric
        H = eta_t()
        Z = add(mm(H, A), mm(tr(A), H))
        assert all(not Z[i][j].d for i in range(DIM) for j in range(DIM))
        Nn = N(n)
        assert all(not x.d for row in mm(Nn, Nn) for x in row)                # N_n^2 = 0
        assert same(mm(mm(Nn, E(X)), Nn), scale(Nn, P.c(nu)))               # N E N = nu N
        assert all(not x.d for row in mm(mm(Nn, N(R)), Nn) for x in row)      # N N_R N = 0
        G = add(eye(), scale(Nn, fy))
        Gi = add(eye(), scale(Nn, -fy))
        assert same(mm(G, Gi), eye())
        fprime = (Sy - fy * fy) * nu
        Gp = [[G[i][j].ddl(fprime) for j in range(DIM)] for i in range(DIM)]
        Ah = add(mm(mm(Gi, A), G), mm(Gi, Gp), -1)
        comm = add(mm(E(X), Nn), mm(Nn, E(X)), -1)
        target = add(add(E(X), N(R)), scale(comm, fy))
        assert same(Ah, target)
        for row in Ah:
            for x in row:
                assert x.deg(0) == 0 and x.deg(1) <= 1
    return True


def check_null_and_radial_frames():
    premise("interior.imported-tractor-connection")
    # n = (1, 1, 0, 0) is a null covector (the conormal of the crossed null hypersurface); the
    # transverse null generator k^a = (1, 1, 0, 0) has nu = n(k) = 2; X_t is a radial unit timelike vector.
    n = [F(1), F(1), F(0), F(0)]
    k = [F(1), F(1), F(0), F(0)]
    assert sum(ETA[a] * n[a] * n[a] for a in range(4)) == 0
    nu = sum(n[a] * k[a] for a in range(4))
    assert nu == 2 and sum(ETA[a] * k[a] * k[a] for a in range(4)) == 0
    X_t = [F(5, 4), F(3, 4), F(0), F(0)]             # radial timelike, eta(X,X) = -1
    assert sum(ETA[a] * X_t[a] * X_t[a] for a in range(4)) == -1
    for X in (k, X_t):
        nuX = sum(n[a] * X[a] for a in range(4))
        R = [F(1, 3), F(-2, 5), F(0), F(0)]          # radial regular part (no angular flux)
        PX = [Sy * (nuX * n[b]) + R[b] for b in range(4)]
        A = add(E(X), N(PX))
        G = add(eye(), scale(N(n), fy))
        Gi = add(eye(), scale(N(n), -fy))
        Gp = [[G[i][j].ddl((Sy - fy * fy) * nuX) for j in range(DIM)] for i in range(DIM)]
        Ah = add(mm(mm(Gi, A), G), mm(Gi, Gp), -1)
        for row in Ah:
            for x in row:
                assert x.deg(0) == 0 and x.deg(1) <= 1
    return True


def check_model_profile():
    premise("interior.imported-tractor-connection")
    # y(s) = 1 + t with t = sqrt(s_c - s): dy/ds = -1/(2t), d2y/ds2 = -1/(4 t^3).
    # With nu = 1: S = y''/y = -1/(4 t^3 (1 + t)); f = y'/y = -1/(2 t (1 + t)).
    # Verify the Riccati f' = S - f^2 exactly at rational t (d/ds = -(1/(2t)) d/dt).
    for t in (F(1, 2), F(1, 3), F(2, 7), F(1, 10), F(5, 9), F(1, 1000)):
        y = 1 + t
        f = -1 / (2 * t * (1 + t))
        S = -1 / (4 * t ** 3 * (1 + t))
        dfdt = (2 * (1 + t) + 2 * t) / (2 * t * (1 + t)) ** 2          # d/dt of -1/(2t(1+t))
        fprime = -dfdt / (2 * t)
        assert fprime == S - f * f
        assert S * y == -1 / (4 * t ** 3)                               # y'' = S y
        # measures in s: ds = 2t dt. |S| ds = |S| 2t dt ~ t^-2 dt (divergent);
        # |s - s_c||S| ds = t^2 |S| 2t dt = 1/(2(1+t)) dt (bounded integrand); |f| ds = 1/(1+t) dt.
        assert abs(S) * 2 * t * t * t * (1 + t) * 2 == 1                 # |S| 2t = 1/(2 t^2 (1+t))
        assert t * t * abs(S) * 2 * t == 1 / (2 * (1 + t))
        assert abs(f) * 2 * t == 1 / (1 + t)
    return True


# ---- (GTG) the same algebra in Cl(2,4): tractors V = sigma ninf + mu + rho n0, bivectors acting by x ----
SQC = gtg.S24
N0C, NIC = gtg.null_pair(SQC)


def _v(c):
    return {(i,): F(x) for i, x in enumerate(c) if x}


GTG_DATA = [  # (gamma' (timelike or null), n (null), R, test tractors (sigma, mu, rho))
    (_v([2, 1, 0, 0]), _v([1, 1, 0, 0]), _v([F(1, 3), -1, 2, F(1, 2)]),
     [(F(1), _v([F(1, 2), 3, -1, 2]), F(-2)), (F(-3, 4), _v([0, 1, F(2, 5), -1]), F(5))]),
    (_v([1, 0, 1, 0]), _v([3, 0, F(-9, 5), F(12, 5)]), _v([0, 2, F(-1, 7), 1]),
     [(F(2), _v([1, 1, 1, 1]), F(1, 3)), (F(0), _v([F(-1, 2), 0, 3, 1]), F(-1))]),
]


def _tr(sig, mu, rho):
    return GA.add(GA.scal(sig, NIC), mu, GA.scal(rho, N0C))


def _E(gp, V):
    return gtg.comm(gtg.wedge(NIC, gp, SQC), V, SQC)


def _N(v, V):
    return GA.neg(gtg.comm(gtg.wedge(N0C, v, SQC), V, SQC))


def check_gtg_tractor_transport_in_cl24():
    """The proof's GTG steps in Cl(2,4): in a D-parallel frame the transport generator -Omega_T(x') . V
    (Omega_T = -ninf ^ gamma' + n0 ^ p there) is E V + N_p V with E = (ninf ^ gamma') . and N_v = -(n0 ^ v) .,
    giving sigma' = gamma' . mu, mu' = -rho gamma' + sigma p, rho' = -p . mu; (a) N_v N_w V = -sigma (v . w) n0,
    N_n^2 = 0; (b) N_n E N_n = nu N_n; (c) N_n N_R N_n = 0; A preserves the tractor metric; the gauge identity
    (1 - f N_n) A (1 + f N_n) - f' N_n = E + N_R + f [E, N_n] for f' = nu (S - f^2); (4) Einstein sides have
    P = (Lambda/6) id."""
    premise("interior.imported-tractor-connection")
    ok = True
    for gp, n, R, tests in GTG_DATA:
        nu = gtg.vdot(n, gp, SQC)
        ok = ok and gtg.vdot(n, n, SQC) == 0 and nu != 0
        for S, f in ((F(2), F(1, 3)), (F(-5, 2), F(3))):
            p = GA.add(GA.scal(S * nu, n), R)
            fp = nu * (S - f * f)
            OmT = GA.add(GA.neg(gtg.wedge(NIC, gp, SQC)), gtg.wedge(N0C, p, SQC))

            def A(V):
                return GA.add(_E(gp, V), _N(p, V))
            for sig, mu, rho in tests:
                V = _tr(sig, mu, rho)
                ok = ok and GA.eq(GA.neg(gtg.comm(OmT, V, SQC)), A(V))
                slots = _tr(gtg.vdot(gp, mu, SQC), GA.add(GA.scal(-rho, gp), GA.scal(sig, p)), -gtg.vdot(p, mu, SQC))
                ok = ok and GA.eq(A(V), slots)
                ok = ok and GA.eq(_N(R, _N(n, V)), GA.scal(-sig * gtg.vdot(R, n, SQC), N0C))
                ok = ok and _N(n, _N(n, V)) == {} and _N(n, _N(R, _N(n, V))) == {}
                ok = ok and GA.eq(_N(n, _E(gp, _N(n, V))), GA.scal(nu, _N(n, V)))
                for s2, m2, r2 in tests:
                    W = _tr(s2, m2, r2)
                    ok = ok and gtg.vdot(A(V), W, SQC) + gtg.vdot(V, A(W), SQC) == 0
                lhs = GA.add(A(GA.add(V, GA.scal(f, _N(n, V)))))
                lhs = GA.sub(lhs, GA.scal(f, _N(n, lhs)))
                lhs = GA.sub(lhs, GA.scal(fp, _N(n, V)))
                rhs = GA.add(_E(gp, V), _N(R, V), GA.scal(f, GA.sub(_E(gp, _N(n, V)), _N(n, _E(gp, V)))))
                ok = ok and GA.eq(lhs, rhs)
    for lam in (F(3), F(-6, 5)):
        P = gtg.schouten(gtg.op_const(lam / 3))
        ok = ok and all(GA.eq(P(GA.gen(m)), GA.scal(lam / 6, GA.gen(m))) for m in range(4))
    _tp_rv = (ok); assert _tp_rv is not False, "check_gtg_tractor_transport_in_cl24"; return _tp_rv
