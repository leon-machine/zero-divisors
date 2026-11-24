"""First-order gravitational field on a periodic cubic lattice, gauge h(e0) = 0 (scratch module).

Components c = 0..5: 11, 22, 33 (on sites), 12, 13, 23 (on plaquettes, labelled by their base site).
A field is a dict {(c, x, y, z): Fraction}. Stencils are 'gather' form: (O f)(x) = sum_o c_o f(x + o).
"""
from fractions import Fraction as F

DIAG = {0: 0, 1: 1, 2: 2}
PAIR = {3: (0, 1), 4: (0, 2), 5: (1, 2)}
CIDX = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (0, 1): 3, (1, 0): 3, (0, 2): 4, (2, 0): 4, (1, 2): 5, (2, 1): 5}


def e(i):
    return tuple(1 if j == i else 0 for j in range(3))


def st_mul(a, b):
    out = {}
    for o1, c1 in a.items():
        for o2, c2 in b.items():
            o = (o1[0] + o2[0], o1[1] + o2[1], o1[2] + o2[2])
            out[o] = out.get(o, 0) + c1 * c2
    return {o: c for o, c in out.items() if c != 0}


def st_scal(k, a):
    return {o: k * c for o, c in a.items()}


def st_add(*xs):
    out = {}
    for a in xs:
        for o, c in a.items():
            out[o] = out.get(o, 0) + c
    return {o: c for o, c in out.items() if c != 0}


Z3 = (0, 0, 0)
ONE = {Z3: F(1)}
S = [{e(i): F(1), Z3: F(-1)} for i in range(3)]                       # forward difference
B = [{Z3: F(1), tuple(-v for v in e(i)): F(-1)} for i in range(3)]    # backward difference
LAP1 = [st_mul(B[i], S[i]) for i in range(3)]                         # second difference along i


def einstein_stencils():
    """G[target][source] = stencil; the linearised Einstein operator of the 3-metric, self-adjoint for
    <h, h'> = sum_x (sum_i h_ii h'_ii + 2 sum_{i<j} h_ij h'_ij)."""
    G = {t: {} for t in range(6)}
    half = F(1, 2)
    for i in range(3):
        j, k = [m for m in range(3) if m != i]
        G[i][j] = st_scal(half, LAP1[k])
        G[i][k] = st_scal(half, LAP1[j])
        G[i][CIDX[(j, k)]] = st_scal(-1, st_mul(B[j], B[k]))
    for c, (i, j) in PAIR.items():
        k = 3 - i - j
        G[c][c] = st_scal(-half, LAP1[k])
        G[c][CIDX[(j, k)]] = st_scal(half, st_mul(S[i], B[k]))
        G[c][CIDX[(i, k)]] = st_scal(half, st_mul(S[j], B[k]))
        G[c][k] = st_scal(-half, st_mul(S[i], S[j]))
    return G


def hamiltonian_stencils():
    """D h = 2 sum_{i<j} b_i b_j h_ij - sum_i sum_{k != i} b_k s_k h_ii  (a scalar on sites)."""
    D = {}
    for i in range(3):
        D[i] = st_scal(-1, st_add(*[LAP1[k] for k in range(3) if k != i]))
    for c, (i, j) in PAIR.items():
        D[c] = st_scal(2, st_mul(B[i], B[j]))
    return D


def momentum_stencils():
    """C_i pi = s_i pi_ii + sum_{j != i} b_j pi_ij  (on the links of direction i)."""
    C = {i: {} for i in range(3)}
    for i in range(3):
        C[i][i] = dict(S[i])
        for j in range(3):
            if j != i:
                C[i][CIDX[(i, j)]] = dict(B[j])
    return C


def gauge_stencils():
    """(delta h)_ii = 2 b_i xi_i, (delta h)_ij = s_i xi_j + s_j xi_i: GA[target comp][xi index]."""
    GA_ = {t: {} for t in range(6)}
    for i in range(3):
        GA_[i][i] = st_scal(2, B[i])
    for c, (i, j) in PAIR.items():
        GA_[c][j] = dict(S[i])
        GA_[c][i] = dict(S[j])
    return GA_


GS, DS, CS, GAS = einstein_stencils(), hamiltonian_stencils(), momentum_stencils(), gauge_stencils()


class Torus:
    def __init__(self, L):
        self.L = L
        self.sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]

    def sh(self, x, o, sign=1):
        L = self.L
        return ((x[0] + sign * o[0]) % L, (x[1] + sign * o[1]) % L, (x[2] + sign * o[2]) % L)

    def apply(self, sten, f):
        """sten[target][source] stencils; f {(source, site): v}; scatter form."""
        out = {}
        bysrc = {}
        for t, row in sten.items():
            for s, stn in row.items():
                bysrc.setdefault(s, []).append((t, stn))
        for (s, x), v in f.items():
            for t, stn in bysrc.get(s, ()):
                for o, c in stn.items():
                    key = (t, self.sh(x, o, -1))
                    out[key] = out.get(key, 0) + c * v
        return {k: v for k, v in out.items() if v != 0}

    def einstein(self, h):
        return self.apply(GS, h)

    def ham(self, h):
        out = self.apply({0: DS}, h)
        return {k[1]: v for k, v in out.items()}

    def mom(self, pi):
        return self.apply(CS, pi)

    def gauge(self, xi):
        return self.apply(GAS, xi)

    def pmap(self, pi):
        """p = pi - (1/2) delta tr pi (the velocity h' = 2 p)."""
        out = dict(pi)
        tr = {}
        for (c, x), v in pi.items():
            if c < 3:
                tr[x] = tr.get(x, 0) + v
        for x, t in tr.items():
            for c in range(3):
                out[(c, x)] = out.get((c, x), 0) - t / 2
        return {k: v for k, v in out.items() if v != 0}

    def step(self, h, pi, tau):
        g = self.einstein(h)
        pi2 = dict(pi)
        for k, v in g.items():
            pi2[k] = pi2.get(k, 0) - tau * v
        pi2 = {k: v for k, v in pi2.items() if v != 0}
        p = self.pmap(pi2)
        h2 = dict(h)
        for k, v in p.items():
            h2[k] = h2.get(k, 0) + 2 * tau * v
        return {k: v for k, v in h2.items() if v != 0}, pi2

    def unstep(self, h2, pi2, tau):
        p = self.pmap(pi2)
        h = dict(h2)
        for k, v in p.items():
            h[k] = h.get(k, 0) - 2 * tau * v
        h = {k: v for k, v in h.items() if v != 0}
        g = self.einstein(h)
        pi = dict(pi2)
        for k, v in g.items():
            pi[k] = pi.get(k, 0) + tau * v
        return h, {k: v for k, v in pi.items() if v != 0}

    def pair(self, a, b):
        tot = 0
        for (c, x), v in a.items():
            w = b.get((c, x), 0)
            if w != 0:
                tot += (1 if c < 3 else 2) * v * w
        return tot

    def cheb(self, x, y):
        L = self.L
        return max(min((x[i] - y[i]) % L, (y[i] - x[i]) % L) for i in range(3))

    def dist_to(self, pts):
        return {x: min(self.cheb(x, y) for y in pts) for x in self.sites}


def fadd(a, b, cb=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + cb * v
    return {k: v for k, v in out.items() if v != 0}
