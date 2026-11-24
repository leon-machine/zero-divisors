"""A periodic lattice model of the first-order gravitational field with its four constraints.

Field: the symmetric first-order field h in the gauge h(e_0) = 0 of a frame, on a periodic cubic lattice. The three
diagonal components h_ii sit on sites, the three off-diagonal ones h_ij on plaquettes (labelled by their base site);
s_i is the forward difference and b_i the backward one. The conjugate variable is pi, with h' = 2 p, p = pi - (1/2)
delta tr pi, and pi' = -G[h], G the first-order Einstein operator of the three space directions. Constraints:
C_0 = D h - g rho at each site (D h = 2 sum_{i<j} b_i b_j h_ij - sum_i sum_{k != i} b_k s_k h_ii) and
C_i = s_i pi_ii + sum_{j != i} b_j pi_ij on each link. W(f) = exp(I <f, pi>) shifts h by f, the unit I written as
in the field theory. Matter: a pair of equal masses about a centre, in one of two arrangements (wide, narrow), in the
algebra of a completed pair Cl(1,1): P1 = vw (wide), P2 = wv (narrow), v = P1 v P2. Operators of the model are sums
of (matter element) x W(f), held as dictionaries {f: matter element}.

(1) the lattice operators are the stored first-order Einstein map in the gauge h(e_0) = 0;
(2) displacement invariance, the contracted identity, the commuting constraints and the count of free pairs;
(3) one mass on two sites has no dressing of compact support; the pair of arrangements with one centre has;
(4) the bare recombiner breaks the constraint, the dressed one keeps it, and the dressed detection commutes with the
    field off the string;
(5) the static slaved field (no transverse trace-free part) fails; the constrained part and the transverse
    trace-free part fail by opposite amounts; a string-shaped slaved field is not static;
(6) dynamics with an exact cone: the dressed detection commutes with the field at every event outside its cone;
    the retarded slaved field does not;
(7) the signal of a coupled classical device: of first order for the slaved field, absent with the field's own
    variables at every event outside the cone;
(8) in two space dimensions the constraint leaves no free part.
"""
from fractions import Fraction as F

import GA
from GA import add, gen, mul, scal, sc, sub
from tp_premise import premise

S11 = GA.sig(1, 1)
S12 = GA.sig(1, 2)

# ---------------------------------------------------------------------------------------------------------
# sample geometry and constants (module level)
# ---------------------------------------------------------------------------------------------------------
SAMPLES = [(3, (1, 2, -2)), (-2, (3, 0, 4)), (5, (1, 1, 7))]      # (frequency, spatial momentum)
HSAMPLE = [[2, -1, 3], [-1, 5, 7], [3, 7, -4]]
FLAT_SAMPLES = [([[2, -1], [-1, 5]], (3, 4)), ([[1, 0], [0, 0]], (1, -2)), ([[0, 1], [1, 0]], (2, 7))]
LID, LRANK, LFLAT = 4, 3, 4          # tori of the identities, of the rank count, and of two dimensions
KL = 9                                # torus of the equal-time clauses
KC = (4, 4, 4)
DL = 17                               # torus of the dynamics
DC = (8, 8, 8)
STEP = F(1, 2)
ND, NMAX, ND_OTHER = 3, 6, 5
COUPLING = F(2, 3)
PQ = (F(3, 5), F(4, 5))
ANGLES = [(F(3, 5), F(4, 5)), (F(5, 13), F(-12, 13))]             # rational points (cos, sin)
STATE = (F(8, 17), F(15, 17))                                      # (a, b) of the matter state
K_AXIS, K_OFF = (0, (7, 4, 4)), (5, (1, 2, 6))                     # sampled curvature components, torus KL
D_AXIS = (0, (11, 8, 8))                                           # a curvature component of the torus DL
ZERO, ONE_, TWO = 0, 1, 2


# ---------------------------------------------------------------------------------------------------------
# stencils: (O f)(x) = sum_o c_o f(x + o)
# ---------------------------------------------------------------------------------------------------------
def unit(i, d, sign=1):
    return tuple(sign if j == i else 0 for j in range(d))


def st_mul(a, b):
    out = {}
    for o1, c1 in a.items():
        for o2, c2 in b.items():
            o = tuple(p + q for p, q in zip(o1, o2))
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


class Stencils:
    """components: i < d the diagonal ones, then the pairs (i, j), i < j, in lexicographic order."""

    def __init__(self, d):
        self.d = d
        zero = tuple([0] * d)
        self.S = [{unit(i, d): F(1), zero: F(-1)} for i in range(d)]
        self.B = [{zero: F(1), unit(i, d, -1): F(-1)} for i in range(d)]
        self.L1 = [st_mul(self.B[i], self.S[i]) for i in range(d)]
        self.pairs = [(i, j) for i in range(d) for j in range(i + 1, d)]
        self.cidx = {}
        for i in range(d):
            self.cidx[(i, i)] = i
        for n, (i, j) in enumerate(self.pairs):
            self.cidx[(i, j)] = d + n
            self.cidx[(j, i)] = d + n
        self.ncomp = d + len(self.pairs)
        self.weight = [1] * d + [2] * len(self.pairs)
        # the Hamiltonian constraint
        self.D = {}
        for i in range(d):
            self.D[i] = st_scal(-1, st_add(*[self.L1[k] for k in range(d) if k != i]))
        for (i, j) in self.pairs:
            self.D[self.cidx[(i, j)]] = st_scal(2, st_mul(self.B[i], self.B[j]))
        # the momentum constraints (on links)
        self.C = {i: {} for i in range(d)}
        for i in range(d):
            self.C[i][i] = dict(self.S[i])
            for j in range(d):
                if j != i:
                    self.C[i][self.cidx[(i, j)]] = dict(self.B[j])
        # the displacements
        self.GA = {t: {} for t in range(self.ncomp)}
        for i in range(d):
            self.GA[i][i] = st_scal(2, self.B[i])
        for (i, j) in self.pairs:
            self.GA[self.cidx[(i, j)]][j] = dict(self.S[i])
            self.GA[self.cidx[(i, j)]][i] = dict(self.S[j])
        # the Einstein operator of three space directions
        self.G = {t: {} for t in range(self.ncomp)}
        if d == 3:
            half = F(1, 2)
            for i in range(3):
                j, k = [m for m in range(3) if m != i]
                self.G[i][j] = st_scal(half, self.L1[k])
                self.G[i][k] = st_scal(half, self.L1[j])
                self.G[i][self.cidx[(j, k)]] = st_scal(-1, st_mul(self.B[j], self.B[k]))
            for (i, j) in self.pairs:
                k = 3 - i - j
                c = self.cidx[(i, j)]
                self.G[c][c] = st_scal(-half, self.L1[k])
                self.G[c][self.cidx[(j, k)]] = st_scal(half, st_mul(self.S[i], self.B[k]))
                self.G[c][self.cidx[(i, k)]] = st_scal(half, st_mul(self.S[j], self.B[k]))
                self.G[c][k] = st_scal(-half, st_mul(self.S[i], self.S[j]))


ST3, ST2 = Stencils(3), Stencils(2)


def moments(stn):
    """(sum of coefficients, first moments, second moments) of a stencil."""
    d = len(next(iter(stn)))
    m0 = sum(stn.values())
    m1 = [sum(c * o[i] for o, c in stn.items()) for i in range(d)]
    m2 = [[sum(c * o[i] * o[j] for o, c in stn.items()) for j in range(d)] for i in range(d)]
    return m0, m1, m2


def symbol2(stn, kap):
    """the symbol of a second-order stencil at momentum kap: -(1/2) sum_o c_o (kap . o)^2."""
    return -F(1, 2) * sum(c * sum(F(k) * o[i] for i, k in enumerate(kap)) ** 2 for o, c in stn.items())


def symbol1(stn, kap):
    return sum(c * sum(F(k) * o[i] for i, k in enumerate(kap)) for o, c in stn.items())


class Torus:
    def __init__(self, L, st=ST3):
        self.L, self.st, self.d = L, st, st.d
        self.sites = [()]
        for _ in range(st.d):
            self.sites = [s + (x,) for s in self.sites for x in range(L)]

    def sh(self, x, o, sign=1):
        return tuple((a + sign * b) % self.L for a, b in zip(x, o))

    def apply(self, sten, f):
        """sten[target][source] stencils; f = {(source, site): value}."""
        bysrc = {}
        for t, row in sten.items():
            for s, stn in row.items():
                bysrc.setdefault(s, []).append((t, stn))
        out = {}
        for (s, x), v in f.items():
            for t, stn in bysrc.get(s, ()):
                for o, c in stn.items():
                    key = (t, self.sh(x, o, -1))
                    out[key] = out.get(key, 0) + c * v
        return {k: v for k, v in out.items() if v != 0}

    def einstein(self, h):
        return self.apply(self.st.G, h)

    def ham(self, h):
        return {k[1]: v for k, v in self.apply({0: self.st.D}, h).items()}

    def mom(self, pi):
        return self.apply(self.st.C, pi)

    def gauge(self, xi):
        return self.apply(self.st.GA, xi)

    def trace(self, f):
        tr = {}
        for (c, x), v in f.items():
            if c < self.d:
                tr[x] = tr.get(x, 0) + v
        return tr

    def pmap(self, pi):
        """p = pi - (1/2) delta tr pi."""
        out = dict(pi)
        for x, t in self.trace(pi).items():
            for c in range(self.d):
                out[(c, x)] = out.get((c, x), 0) - t / 2
        return {k: v for k, v in out.items() if v != 0}

    def pair(self, a, b):
        return sum(self.st.weight[c] * v * b[(c, x)] for (c, x), v in a.items() if (c, x) in b)

    def lap(self, u):
        out = {}
        for x, v in u.items():
            out[x] = out.get(x, 0) - 2 * self.d * v
            for i in range(self.d):
                for s in (1, -1):
                    y = self.sh(x, unit(i, self.d), s)
                    out[y] = out.get(y, 0) + v
        return {x: v for x, v in out.items() if v != 0}

    def lap_comp(self, f):
        """the lattice Laplacian applied to each component."""
        out = {}
        for c in range(self.st.ncomp):
            for x, v in self.lap({x: v for (cc, x), v in f.items() if cc == c}).items():
                out[(c, x)] = v
        return out

    def solve_poisson(self, rho):
        """u with lap u = rho, from the first linear relation among rho, lap rho, lap^2 rho, ...; exact, and
        verified by the caller. rho must sum to zero."""
        vs = [dict(rho)]
        basis = []
        while True:
            j = len(vs) - 1
            r, comb = dict(vs[j]), {j: F(1)}
            for piv, bv, bc in basis:
                c = r.get(piv, 0)
                if c != 0:
                    for x, v in bv.items():
                        nv = r.get(x, 0) - c * v
                        if nv == 0:
                            r.pop(x, None)
                        else:
                            r[x] = nv
                    for k, v in bc.items():
                        comb[k] = comb.get(k, 0) - c * v
            if not r:
                break
            piv = min(r)
            pv = r[piv]
            basis.append((piv, {x: v / pv for x, v in r.items()}, {k: v / pv for k, v in comb.items()}))
            vs.append(self.lap(vs[j]))
        u = {}
        for k, c in comb.items():
            if k >= 1:
                for x, v in vs[k - 1].items():
                    u[x] = u.get(x, 0) - (c / comb[0]) * v
        return {x: v for x, v in u.items() if v != 0}

    # one step of the first-order field equations in the gauge h(e_0) = 0, and its inverse
    def step(self, h, pi, tau):
        pi2 = fadd(pi, self.einstein(h), -tau)
        return fadd(h, self.pmap(pi2), 2 * tau), pi2

    def unstep(self, h2, pi2, tau):
        h = fadd(h2, self.pmap(pi2), -2 * tau)
        return h, fadd(pi2, self.einstein(h), tau)

    # the cone of the step: which components a step can reach
    def reach(self, S):
        out = set()
        for (s, x) in S:
            for t, row in self.st.G.items():
                for o in row.get(s, ()):
                    out.add((t, self.sh(x, o, -1)))
        mixed = set(out)
        for (c, x) in out:
            if c < self.d:
                mixed.update((cc, x) for cc in range(self.d))
        return mixed

    def cone_depth(self, S0, m):
        """depth[component] = the first step at which the component can differ from zero, for data h on S0."""
        Sh, Sp = set(S0), set()
        depth = {k: 0 for k in Sh}
        for n in range(1, m + 1):
            Sp |= self.reach(Sh)
            for k in Sp - Sh:
                depth[k] = n
            Sh |= Sp
        return depth

    def curvature_depth(self, depth, big):
        """for each curvature component, the least depth of the components of h that enter it."""
        out = {}
        for c in range(self.st.ncomp):
            cells = [(s, o) for s, stn in self.st.G[c].items() for o in stn]
            for x in self.sites:
                out[(c, x)] = min(depth.get((s, self.sh(x, o)), big) for s, o in cells)
        return out


def fadd(a, b, cb=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + cb * v
    return {k: v for k, v in out.items() if v != 0}


def fscal(c, a):
    return {k: c * v for k, v in a.items() if c != 0}


def sample_field(T, ncomp, seed):
    """integer sample values on every component, from a fixed linear recurrence."""
    out, s = {}, seed
    for c in range(ncomp):
        for x in T.sites:
            s = (s * 1103515245 + 12345) % 2147483648
            out[(c, x)] = F((s // 256) % 11 - 5)
    return out


def rank(rows):
    rows = [r[:] for r in rows]
    rk = 0
    for c in range(len(rows[0])):
        piv = next((r for r in range(rk, len(rows)) if rows[r][c] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        pv = rows[rk][c]
        rows[rk] = [x / pv for x in rows[rk]]
        for r in range(len(rows)):
            if r != rk and rows[r][c] != 0:
                fac = rows[r][c]
                rows[r] = [x - fac * y for x, y in zip(rows[r], rows[rk])]
        rk += 1
    return rk


def ranks(T):
    """(number of components, rank of the displacements, rank of D) on the torus T."""
    comps = [(c, x) for c in range(T.st.ncomp) for x in T.sites]
    idx = {k: n for n, k in enumerate(comps)}
    sidx = {x: n for n, x in enumerate(T.sites)}
    grows = []
    for i in range(T.d):
        for x in T.sites:
            row = [F(0)] * len(comps)
            for k, v in T.gauge({(i, x): F(1)}).items():
                row[idx[k]] = v
            grows.append(row)
    drows = [[F(0)] * len(comps) for _ in T.sites]
    for k, n in idx.items():
        for x, v in T.ham({k: F(1)}).items():
            drows[sidx[x]][n] = v
    return len(comps), rank(grows), rank(drows)


# ---- the two arrangements and the dressing -------------------------------------------------------------------
def geometry(T, centre):
    """string: the three sites about the centre along the first axis; wide masses at distance two, narrow at one."""
    ax = unit(0, T.d)
    string = [T.sh(centre, ax, k) for k in (-1, 0, 1)]
    wide = {T.sh(centre, ax, -2): F(1), T.sh(centre, ax, 2): F(1)}
    narrow = {T.sh(centre, ax, -1): F(1), T.sh(centre, ax, 1): F(1)}
    f = {}
    for x in string:
        f[(0, x)] = F(1, 2)
        f[(1, x)] = F(-1, 2)
        f[(2, x)] = F(-1, 2)
    return string, wide, narrow, f


def moments_of(T, rho, centre):
    """monopole, dipole and second moments of a function on the sites, in coordinates centred on `centre`
    (the function must be supported within less than half the period of the centre)."""
    def rel(x):
        return [((a - b + T.L // 2) % T.L) - T.L // 2 for a, b in zip(x, centre)]
    mono = sum(rho.values())
    dip = [sum(v * rel(x)[i] for x, v in rho.items()) for i in range(T.d)]
    quad = [sum(v * rel(x)[i] ** 2 for x, v in rho.items()) for i in range(T.d)]
    return mono, dip, quad


# ---- matter: Cl(1,1) --------------------------------------------------------------------------------------------
E1, E2 = gen(0), gen(1)
V = scal(F(1, 2), add(E1, E2))
W_ = scal(F(1, 2), sub(E1, E2))
P1, P2 = mul(V, W_, S11), mul(W_, V, S11)


# ---- operators: sums of (matter) x W(f) ---------------------------------------------------------------------------
def key(f):
    return tuple(sorted((k, c) for k, c in f.items() if c != 0))


def op(m, f=None):
    return {key(f or {}): m}


def oadd(*xs):
    out = {}
    for x in xs:
        for k, m in x.items():
            out[k] = add(out.get(k, {}), m)
    return {k: m for k, m in out.items() if not GA.is_zero(m)}


def oscal(c, x):
    return {k: scal(c, m) for k, m in x.items() if c != 0}


def omul(x, y):
    out = {}
    for kf, m in x.items():
        for kg, n in y.items():
            k = key(fadd(dict(kf), dict(kg)))
            out[k] = add(out.get(k, {}), mul(m, n, S11))
    return {k: m for k, m in out.items() if not GA.is_zero(m)}


def oeq(x, y):
    return oadd(x, oscal(-1, y)) == {}


def comm_field(lam, x):
    """[sum_k lam_k h_k, x]: each term (matter) x W(f) is multiplied by sum_k lam_k f_k."""
    out = {}
    for kf, m in x.items():
        c = sum(lam.get(k, 0) * val for k, val in kf)
        if c != 0:
            out[kf] = scal(c, m)
    return out


def comm_curv(T, comp, x):
    """[G_c(y)[h], x] for the curvature component comp = (c, y)."""
    out = {}
    for kf, m in x.items():
        c = T.einstein(dict(kf)).get(comp, 0)
        if c != 0:
            out[kf] = scal(c, m)
    return out


def comm_ham(T, s, rho, g, x):
    """[C_0(s), x], C_0(s) = (D h)(s) - g rho_s, rho a dictionary site -> matter element."""
    out = {}
    for kf, m in x.items():
        term = scal(T.ham(dict(kf)).get(s, 0), m)
        if s in rho:
            term = sub(term, scal(g, sub(mul(rho[s], m, S11), mul(m, rho[s], S11))))
        if not GA.is_zero(term):
            out[kf] = term
    return out


def recombiner(f, p, q):
    """U = p + q (v W(f) - w W(-f)) and its inverse; f = {} is the bare recombiner p + q e2."""
    X = oadd(op(V, f), oscal(-1, op(W_, fscal(-1, f))))
    return oadd(op(sc(p)), oscal(q, X)), oadd(op(sc(p)), oscal(-q, X)), X


def detection(f, p, q):
    U, Uinv, X = recombiner(f, p, q)
    return omul(omul(Uinv, op(P1)), U), U, Uinv, X


def charge(wide, narrow):
    rho = {}
    for s in set(wide) | set(narrow):
        rho[s] = add(scal(wide.get(s, 0), P1), scal(narrow.get(s, 0), P2))
    return rho


# ---- the stored first-order Einstein map in Cl(1,3) ----------------------------------------------------------------
class Spacetime:
    """Cl(1, d-1): the stored first-order curvature, its Einstein map, and the Einstein map of the space directions."""

    def __init__(self, d=4):
        self.d = d
        self.S = GA.sig(1, d - 1)
        self.eta = [1] + [-1] * (d - 1)
        self.e = [gen(i) for i in range(d)]
        self.rec = [scal(self.eta[i], self.e[i]) for i in range(d)]

    def dot(self, a, b):
        return GA.dot(a, b, self.S)

    def wedge(self, a, b):
        return scal(F(1, 2), sub(mul(a, b, self.S), mul(b, a, self.S)))

    def vdotB(self, a, B):
        x = scal(F(1, 2), sub(mul(a, B, self.S), mul(B, a, self.S)))
        return {b: c for b, c in x.items() if len(b) == 1}

    def apply(self, H, a):
        out = {}
        for m in range(self.d):
            am = self.dot(a, self.e[m])
            for n in range(self.d):
                if am != 0 and H[m][n] != 0:
                    out = add(out, scal(am * H[m][n], self.e[n]))
        return out

    def trace(self, H):
        return sum(self.eta[a] * self.dot(self.e[a], self.apply(H, self.e[a])) for a in range(self.d))

    def embed(self, Hs):
        """a symmetric matrix of the space directions as a map with h(e_0) = 0."""
        H = [[F(0)] * self.d for _ in range(self.d)]
        for i in range(self.d - 1):
            for j in range(self.d - 1):
                H[i + 1][j + 1] = F(Hs[i][j])
        return H

    def space_vec(self, comps):
        return {(i + 1,): F(c) for i, c in enumerate(comps) if c}

    def riem(self, H, k, B):
        return scal(F(-1, 2), self.wedge(k, self.apply(H, GA.neg(self.vdotB(k, B)))))

    def einstein(self, H, kc):
        """the matrix E[m][n] = e^n . G_k[h](e^m)."""
        k = {(i,): F(c) for i, c in enumerate(kc) if c}
        R = [[F(0)] * self.d for _ in range(self.d)]
        for m in range(self.d):
            img = {}
            for b in range(self.d):
                img = add(img, self.vdotB(self.rec[b], self.riem(H, k, self.wedge(self.e[b], self.rec[m]))))
            for n in range(self.d):
                R[m][n] = self.dot(img, self.rec[n])
        t = sum(self.eta[a] * R[a][a] for a in range(self.d))
        return [[R[m][n] - (F(1, 2) * t * self.eta[m] if m == n else 0) for n in range(self.d)]
                for m in range(self.d)]

    def pi_map(self, H, a):
        """pi(a) = (1/2)(h(a) - a tr h)."""
        return scal(F(1, 2), sub(self.apply(H, a), scal(self.trace(H), a)))

    def space_einstein(self, H, kap, a):
        """G_kappa[h](a) = (1/2)[(a.kap)(h(kap) - kap tr h) - Q(kap) h(a) + (a.h(kap)) kap
        - (kap.h(kap) - Q(kap) tr h) a]."""
        hk, t, Qk = self.apply(H, kap), self.trace(H), self.dot(kap, kap)
        return scal(F(1, 2), add(scal(self.dot(a, kap), sub(hk, scal(t, kap))), scal(-Qk, self.apply(H, a)),
                                 scal(self.dot(a, hk), kap), scal(-(self.dot(kap, hk) - Qk * t), a)))


# ---------------------------------------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------------------------------------
def check_lattice_operators_are_the_stored_first_order_map_in_the_frame_gauge():
    premise("synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints")
    st, sp = ST3, Spacetime()
    ok = True
    # every stencil of G and D kills constants and linear functions; those of C kill constants
    for row in list(st.G.values()) + [st.D]:
        for stn in row.values():
            m0, m1, _ = moments(stn)
            ok = ok and m0 == 0 and m1 == [0, 0, 0]
    ok = ok and all(moments(stn)[0] == 0 for row in st.C.values() for stn in row.values())
    for w, kap in SAMPLES:
        Hs = [[F(x) for x in r] for r in HSAMPLE]
        hcomp = {st.cidx[(i, j)]: Hs[i][j] for i in range(3) for j in range(i, 3)}
        tr = sum(Hs[i][i] for i in range(3))
        Pi = [[(Hs[i][j] - (tr if i == j else 0)) / 2 for j in range(3)] for i in range(3)]
        picomp = {st.cidx[(i, j)]: Pi[i][j] for i in range(3) for j in range(i, 3)}
        H = sp.embed(Hs)
        E = sp.einstein(H, (w,) + kap)
        # the same three statements for vectors: time-time (1/2)(kap.h(kap) - Q(kap) tr h), the space part of
        # G(e_0) is -w pi(kap), the space part of G(a) is w^2 pi(a) - G_kappa[h](a)
        kv = sp.space_vec(kap)
        ok = ok and E[0][0] == (sp.dot(kv, sp.apply(H, kv)) - sp.dot(kv, kv) * sp.trace(H)) / 2
        ok = ok and GA.eq(add(*[scal(E[0][n + 1], sp.e[n + 1]) for n in range(3)]), scal(-w, sp.pi_map(H, kv)))
        for i in range(3):
            Ga = add(*[scal(-E[i + 1][n + 1], sp.e[n + 1]) for n in range(3)])
            a = sp.e[i + 1]
            ok = ok and GA.eq(Ga, sub(scal(w * w, sp.pi_map(H, a)), sp.space_einstein(H, kv, a)))
        # e_0 . G(e_0) = -(1/2) D h, with no frequency
        Dsym = sum(symbol2(stn, kap) * hcomp[c] for c, stn in st.D.items())
        ok = ok and E[0][0] == -Dsym / 2 and E[0][0] == sp.einstein(H, (w + 1,) + kap)[0][0]
        # e_0 . G(e_i) = frequency times the momentum constraint of pi = (1/2)(h - delta tr h)
        for i in range(3):
            Csym = sum(symbol1(stn, kap) * picomp[c] for c, stn in st.C[i].items())
            ok = ok and E[0][i + 1] == w * Csym
        # e_i . G(e_j) = frequency^2 pi - G^(3)[h]
        for i in range(3):
            for j in range(i, 3):
                c = st.cidx[(i, j)]
                Gsym = sum(symbol2(stn, kap) * hcomp[s] for s, stn in st.G[c].items())
                ok = ok and E[i + 1][j + 1] == w * w * Pi[i][j] - Gsym
    GA.check("in the gauge h(e_0) = 0 the stored first-order Einstein map at k = w e_0 + kappa has time-time "
             "component -(1/2) D h, time-space components w C[pi] and space-space components w^2 pi - G[h], with D, "
             "C, G the symbols of the lattice stencils and pi = (1/2)(h - delta tr h), at three sampled momenta", ok)
    return ok


def check_displacement_invariance_commuting_constraints_and_two_free_pairs_per_momentum():
    premise("synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints")
    premise("field-theory.fock-space-maxwell-modes")
    T = Torus(LID)
    h, h2, pi = sample_field(T, 6, 1), sample_field(T, 6, 2), sample_field(T, 6, 3)
    xi = sample_field(T, 3, 4)
    ok = len(T.sites) == 64
    dh = T.gauge(xi)
    Gh = T.einstein(h)
    # displacements: G and D do not see them; [C_0, C_i] is D applied to a displacement
    ok = ok and dh != {} and Gh != {} and T.einstein(dh) == {} and T.ham(dh) == {}
    # the displacement map is the adjoint of the momentum constraints: <pi, disp xi> = -2 sum xi . C[pi]
    Cpi = T.mom(pi)
    ok = ok and T.pair(pi, dh) == -2 * sum(v * Cpi.get(k, 0) for k, v in xi.items())
    # contracted identity, symmetry, trace
    ok = ok and T.mom(Gh) == {} and T.pair(h2, Gh) == T.pair(T.einstein(h2), h)
    trG, Dh = T.trace(Gh), T.ham(h)
    ok = ok and all(trG.get(x, 0) == -Dh.get(x, 0) / 2 for x in T.sites)
    # the constraints are kept by a step: D p = sum_i b_i C_i[pi]
    Dp, bC = T.ham(T.pmap(pi)), {}
    for (i, x), v in Cpi.items():
        for o, c in ST3.B[i].items():
            y = T.sh(x, o, -1)
            bC[y] = bC.get(y, 0) + c * v
    ok = ok and all(Dp.get(x, 0) == bC.get(x, 0) for x in T.sites)
    # G h = -(1/2) lap h + (1/2) disp(V) - (1/2) delta D h, V = div h - (1/2) grad tr h
    Vf = T.mom(h)
    for x, t in T.trace(h).items():
        for i in range(3):
            y = T.sh(x, unit(i, 3), -1)
            Vf[(i, x)] = Vf.get((i, x), 0) + t / 2
            Vf[(i, y)] = Vf.get((i, y), 0) - t / 2
    gV, Lh = T.gauge(Vf), T.lap_comp(h)
    for c in range(6):
        for x in T.sites:
            rhs = -Lh.get((c, x), 0) / 2 + gV.get((c, x), 0) / 2 - (Dh.get(x, 0) / 2 if c < 3 else 0)
            ok = ok and rhs == Gh.get((c, x), 0)
    # count on the torus of 27 sites: 162 components, 78 displacement directions, 26 constraints: 58 = 2 * 26 + 6
    n, rg, rd = ranks(Torus(LRANK))
    ok = ok and (n, rg, rd) == (162, 78, 26) and n - rg - rd == 2 * 26 + 6
    GA.check("on the torus of 64 sites G and D vanish on displacements, the momentum constraints of G[h] vanish, G "
             "is symmetric with trace -(1/2) D, D p is the divergence of the momentum constraints and G is "
             "-(1/2) lap plus a displacement plus a multiple of D; on the torus of 27 sites the fields with D h = 0 "
             "modulo displacements have dimension 58, two for each of the 26 nonzero momenta and six at zero", ok)
    return ok


def check_one_mass_on_two_sites_has_no_dressing_of_compact_support_and_the_pair_has_one():
    premise("synthesis.two-dimensional-lattice-maxwell-coulomb-slaved-field-fails-and-string-dressed-detection-commutes")
    T = Torus(KL)
    string, wide, narrow, f = geometry(T, KC)
    ok = len(T.sites) == 729 and len(string) == 3
    # D of any field supported near the centre has no monopole and no dipole (sampled on a field filling the
    # cube of 27 sites about the centre); its second moments need not vanish
    cube = [x for x in T.sites if max(abs(((a - b + 4) % 9) - 4) for a, b in zip(x, KC)) <= 1]
    samp = sample_field(T, 6, 5)
    g_ = {(c, x): samp[(c, x)] for c in range(6) for x in cube}
    mono, dip, quad = moments_of(T, T.ham(g_), KC)
    ok = ok and len(cube) == 27 and T.ham(g_) != {} and mono == 0 and dip == [0, 0, 0] and quad != [0, 0, 0]
    # one mass on two sites: dipole one, so no field supported within less than half the period has this D
    a, b = T.sh(KC, unit(0, 3), 1), KC
    mono, dip, _ = moments_of(T, {a: F(1), b: F(-1)}, KC)
    ok = ok and mono == 0 and dip == [1, 0, 0]
    # the two arrangements of the pair: same mass, same centre, second moments 8 and 2
    diff = fadd(wide, narrow, -1)
    mono, dip, quad = moments_of(T, diff, KC)
    ok = ok and mono == 0 and dip == [0, 0, 0] and quad == [6, 0, 0]
    ok = ok and moments_of(T, wide, KC)[2] == [8, 0, 0] and moments_of(T, narrow, KC)[2] == [2, 0, 0]
    # the dressing: f = (1/2, -1/2, -1/2) on the diagonal at the three sites of the string, D f = wide - narrow
    ok = ok and T.ham(f) == diff and len(f) == 9 and f[(0, KC)] == F(1, 2) and f[(2, KC)] == F(-1, 2)
    # f = 2 p for the momentum pi_11 = 1/2 on the string; its momentum constraint is nonzero on exactly the two
    # links that the masses cross, +1/2 on the link from -2 to -1 and -1/2 on the link from 1 to 2
    pi_f = {(0, x): F(1, 2) for x in string}
    ok = ok and T.pmap(pi_f) == fscal(F(1, 2), f)
    ok = ok and T.mom(pi_f) == {(0, T.sh(KC, unit(0, 3), -2)): F(1, 2), (0, T.sh(KC, unit(0, 3), 1)): F(-1, 2)}
    GA.check("on the torus of 729 sites D of a field supported on the 27 sites about the centre has no monopole and "
             "no dipole; one mass on two neighbouring sites has dipole 1; the wide and narrow arrangements of the "
             "pair differ by a function with no monopole, no dipole and second moment 6, equal to D f for the "
             "field f on the three sites of the string", ok)
    return ok


def check_bare_recombiner_breaks_the_constraint_and_the_dressed_detection_commutes_off_the_string():
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    premise("field-theory.no-canonical-commutation-relations-tower")
    T = Torus(KL)
    string, wide, narrow, f = geometry(T, KC)
    rho = charge(wide, narrow)
    g, (p, q) = COUPLING, PQ
    Ub, Ubinv, _ = recombiner({}, p, q)
    Ud, Udinv, X = recombiner(fscal(g, f), p, q)
    one = op(sc(1))
    ok = oeq(omul(Ub, Ubinv), one) and oeq(omul(Ud, Udinv), one) and oeq(omul(X, X), oscal(-1, one))
    # bare: [C_0(s), U] = -g q (wide - narrow)(s) e1, nonzero at the four sites of the masses and nowhere else
    bad = [s for s in T.sites if comm_ham(T, s, rho, g, Ub) != {}]
    ok = ok and len(bad) == 4 and sorted(bad) == sorted(rho)
    ok = ok and oeq(comm_ham(T, T.sh(KC, unit(0, 3), 2), rho, g, Ub), op(scal(-g * q, E1)))
    ok = ok and oeq(comm_ham(T, T.sh(KC, unit(0, 3), 1), rho, g, Ub), op(scal(g * q, E1)))
    # dressed: commutes with C_0 at all 729 sites, and so does the detection built from it
    Od, _, _, _ = detection(fscal(g, f), p, q)
    ok = ok and all(comm_ham(T, s, rho, g, Ud) == {} for s in T.sites)
    ok = ok and all(comm_ham(T, s, rho, g, Od) == {} for s in T.sites)
    ok = ok and oeq(omul(Od, Od), Od)
    ok = ok and oeq(Od, oadd(op(scal(p * p, P1)), op(scal(q * q, P2)),
                             oscal(p * q, oadd(op(V, fscal(g, f)), op(W_, fscal(-g, f))))))
    # [h_k, O] = g p q f_k X: zero on the 4365 components off the string
    comps = [(c, x) for c in range(6) for x in T.sites]
    off = [k for k in comps if k not in f]
    ok = ok and len(comps) == 4374 and len(off) == 4365
    ok = ok and all(comm_field({k: 1}, Od) == {} for k in off)
    ok = ok and all(oeq(comm_field({k: 1}, Od), oscal(g * p * q * f[k], X)) for k in f)
    # curvature: [G_c(y), O] = g p q G[f]_c(y) X, nonzero on 57 components at 22 sites and zero on the other 4317
    Gf = T.einstein(f)
    ok = ok and len(Gf) == 57 and len({x for (_, x) in Gf}) == 22
    for k in list(Gf)[:6] + [K_AXIS, K_OFF]:
        ok = ok and oeq(comm_curv(T, k, Od), oscal(g * p * q * Gf.get(k, 0), X))
    ok = ok and K_AXIS not in Gf and K_OFF not in Gf and len(comps) - len(Gf) == 4317
    GA.check("the bare recombiner fails to commute with the Hamiltonian constraint at the four sites of the masses; "
             "the dressed recombiner and its detection commute with it at all 729 sites; the dressed detection "
             "commutes with h on the 4365 components off the string and with the curvature on the 4317 components "
             "off the 57 where the curvature of the dressing is nonzero", ok)
    return ok


def check_newtonian_slaved_field_fails_and_the_transverse_part_cancels_the_constrained_part():
    premise("synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation")
    premise("field-theory.operator-newtonian-coupling")
    premise("synthesis.two-dimensional-lattice-maxwell-coulomb-slaved-field-fails-and-string-dressed-detection-commutes")
    T = Torus(KL)
    string, wide, narrow, f = geometry(T, KC)
    g, (p, q) = COUPLING, PQ
    diff = fadd(wide, narrow, -1)
    # the field with D = wide - narrow and no transverse trace-free part: h = phi delta, -2 lap phi = wide - narrow
    phi = T.solve_poisson(fscal(F(-1, 2), diff))
    ok = T.lap(phi) == fscal(F(-1, 2), diff)
    newt = {(c, x): v for x, v in phi.items() for c in range(3)}
    ok = ok and T.ham(newt) == diff
    kap, Gf = T.einstein(newt), T.einstein(f)
    comps = [(c, x) for c in range(6) for x in T.sites]
    off = [k for k in comps if k not in Gf]
    fail = [k for k in off if kap.get(k, 0) != 0]
    ok = ok and len(off) == 4317 and len(fail) == 3858
    ok = ok and kap[K_AXIS] == F(-107604096374, 4507875455157) and kap[K_OFF] == F(519559, 1494901494)
    # static: two steps change h (by a displacement) and leave every component of the curvature unchanged;
    # the string-shaped field has changed its curvature on 499 components
    hN, piN, hS, piS = dict(newt), {}, dict(f), {}
    for _ in range(TWO):
        hN, piN = T.step(hN, piN, STEP)
        hS, piS = T.step(hS, piS, STEP)
    ok = ok and hN != newt and T.einstein(hN) == kap
    GS2 = T.einstein(hS)
    ok = ok and sum(1 for k in comps if GS2.get(k, 0) != Gf.get(k, 0)) == 499 and T.ham(hS) == diff
    # the slaved field with no transverse trace-free part: G = g kap P1 + number; with the bare detection
    Ob, _, _, _ = detection({}, p, q)
    for k in [K_AXIS, K_OFF]:
        ES = op(scal(g * kap[k], P1))
        c = oadd(omul(ES, Ob), oscal(-1, omul(Ob, ES)))
        ok = ok and c != {} and oeq(c, op(scal(g * kap[k] * p * q, E2)))
    # the constrained part of the curvature as a function of D h: G^L_c(y) = (1/(4 w_c)) sum_s u(s) (D h)(s),
    # lap u = D e_(c,y); its commutator with the dressed detection is g p q kap X, the transverse trace-free part's
    # is g p q (G[f] - kap) X, and off the support of G[f] the two cancel
    Od, _, _, X = detection(fscal(g, f), p, q)
    for k in [K_AXIS, K_OFF]:
        u = T.solve_poisson(T.ham({k: F(1)}))
        ok = ok and T.lap(u) == T.ham({k: F(1)})
        coef = sum(u.get(s, 0) * v for s, v in diff.items()) / (4 * ST3.weight[k[0]])
        ok = ok and coef == kap[k]
        cL = oscal(g * p * q * coef, X)
        cT = oadd(comm_curv(T, k, Od), oscal(-1, cL))
        ok = ok and cL != {} and oeq(cT, oscal(-g * p * q * kap[k], X)) and comm_curv(T, k, Od) == {}
    GA.check("torus of 729 sites: the curvature of the slaved field with no transverse trace-free part differs "
             "between the two arrangements on 3858 of the 4317 components off the support of the dressing's "
             "curvature, is unchanged by the field equation, and fails to commute with the bare detection there; "
             "the constrained part and the transverse trace-free part of the curvature fail to commute with the "
             "dressed detection by opposite amounts; the string-shaped slaved field is not static", ok)
    return ok


def dynamics():
    """the solutions used by the two dynamics checks, on the torus DL."""
    T = Torus(DL)
    string, wide, narrow, f = geometry(T, DC)
    depth = T.cone_depth(set(f), NMAX)
    cd = T.curvature_depth(depth, NMAX + 1)
    S = {ND: (dict(f), {})}
    h, pi = dict(f), {}
    for n in range(ND, NMAX):
        h, pi = T.step(h, pi, STEP)
        S[n + 1] = (h, pi)
    h, pi = dict(f), {}
    for n in range(ND, 0, -1):
        h, pi = T.unstep(h, pi, STEP)
        S[n - 1] = (h, pi)
    R = {0: (dict(f), {})}
    h, pi = dict(f), {}
    for n in range(NMAX):
        h, pi = T.step(h, pi, STEP)
        R[n + 1] = (h, pi)
    return T, f, fadd(wide, narrow, -1), depth, cd, S, R


def check_dynamics_dressed_detection_commutes_outside_its_cone_and_the_retarded_slaved_field_does_not():
    premise("synthesis.two-dimensional-lattice-maxwell-coulomb-slaved-field-fails-and-string-dressed-detection-commutes")
    premise("synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation")
    T, f, diff, depth, cd, S, R = dynamics()
    ok = len(T.sites) == 4913 and len(S) == 7 and len(R) == 7
    # the constraints hold at every step of both solutions
    ok = ok and all(T.ham(S[n][0]) == diff and T.mom(S[n][1]) == {} for n in S)
    ok = ok and all(T.ham(R[n][0]) == diff and T.mom(R[n][1]) == {} for n in R)
    # (a) the field's own variables: the commutator of h, pi at step n with the dressed detection at step ND is the
    # solution S; it vanishes on every component outside the cone of the string
    big = NMAX + 1
    ok = ok and all(depth.get(k, big) <= abs(n - ND) for n in S for fld in S[n] for k in fld)
    GS_ = {n: T.einstein(S[n][0]) for n in S}
    GR_ = {n: T.einstein(R[n][0]) for n in R}
    space = [(k, n) for n in S for k, dpt in cd.items() if dpt > abs(n - ND)]
    ok = ok and len(space) == 202171 and 6 * 4913 * 7 == 206346
    ok = ok and all(GS_[n].get(k, 0) == 0 for (k, n) in space)
    ok = ok and sum(1 for n in S for k, v in GS_[n].items() if 0 < cd[k] <= abs(n - ND)) == 2164
    # (b) the retarded slaved field: its curvature differs between the arrangements by GR_
    bad = [(k, n) for (k, n) in space if GR_[n].get(k, 0) != 0]
    ok = ok and len(bad) == 8736 and not any(n < 2 for (k, n) in bad)
    ok = ok and sum(1 for (k, n) in bad if n <= ND) == 1304
    # every failing event is inside the cone of the source event (the string at step 0) and outside the detection's
    ok = ok and all(cd[k] <= n and cd[k] > abs(n - ND) for (k, n) in bad)
    fwd = [(k, n) for (k, n) in space if cd[k] <= n]
    ok = ok and len(fwd) == 9310
    ok = ok and GR_[ND][D_AXIS] == F(-5, 64) and (D_AXIS, ND) in bad and cd[D_AXIS] == 2
    # a slaved field fitted to the detection at step ND fails for a detection at step ND_OTHER
    other = [(k, n) for n in S for k, dpt in cd.items() if dpt > abs(n - ND_OTHER)]
    ok = ok and len(other) == 198771 and sum(1 for (k, n) in other if GS_[n].get(k, 0) != 0) == 1252
    # the step is a canonical map and unstep inverts it: <h1', pi2'> - <pi1', h2'> is kept, on two sampled data
    z1, z2 = ({D_AXIS: F(1)}, {(5, DC): F(2)}), ({(3, DC): F(1)}, {D_AXIS: F(-3)})
    w1, w2 = T.step(z1[0], z1[1], STEP), T.step(z2[0], z2[1], STEP)
    ok = ok and T.pair(w1[0], w2[1]) - T.pair(w1[1], w2[0]) == T.pair(z1[0], z2[1]) - T.pair(z1[1], z2[0]) == -3
    ok = ok and T.unstep(w1[0], w1[1], STEP) == z1
    GA.check("torus of 4913 sites, step 1/2, detection at step 3: the dressed detection commutes with the curvature "
             "at all 202171 events outside its cone; the retarded slaved field fails at 8736 of them, 1304 not "
             "later than the detection, all inside the cone of the source event, while satisfying the constraints "
             "at every step", ok)
    return ok


def check_device_signal_is_of_first_order_for_the_slaved_field_and_absent_with_the_free_part():
    premise("synthesis.with-a-coupled-device-the-slaved-field-failure-is-a-first-order-signal-and-a-survey-finds-no-stored-bound")
    T, f, diff, depth, cd, S, R = dynamics()
    g, (p, q), (a, b) = COUPLING, PQ, STATE
    ok = a * a + b * b == 1 and p * p + q * q == 1
    # Cl(1,1) inside Cl(1,2): I = e1 e2 e3 central, I^2 = -1; state rho = (1/2)(1 + a e1 + b I e2)
    e1, e2, e3 = gen(0), gen(1), gen(2)
    I = mul(mul(e1, e2, S12), e3, S12)
    v, w = scal(F(1, 2), add(e1, e2)), scal(F(1, 2), sub(e1, e2))
    p1, p2 = mul(v, w, S12), mul(w, v, S12)
    Ie2 = mul(I, e2, S12)
    rho = scal(F(1, 2), add(sc(1), add(scal(a, e1), scal(b, Ie2))))
    U, Ui = add(sc(p), scal(q, e2)), add(sc(p), scal(-q, e2))
    O = mul(mul(Ui, p1, S12), U, S12)

    def ev(x):
        return 2 * mul(rho, x, S12).get((), 0)

    ok = ok and GA.eq(mul(I, I, S12), sc(-1)) and GA.eq(mul(rho, rho, S12), rho)
    # slaved field: the device acts by Vd = exp(-I theta P1) up to a phase; the change of the detection probability
    for (c, s) in ANGLES:
        Vd = add(mul(add(sc(c), scal(-s, I)), p1, S12), p2)
        Vdi = add(mul(add(sc(c), scal(s, I)), p1, S12), p2)
        ok = ok and GA.eq(mul(Vd, Vdi, S12), sc(1))
        ok = ok and ev(mul(mul(Vdi, O, S12), Vd, S12)) - ev(O) == p * q * (a * (c - 1) + b * s)
    # its first-order coefficient per unit strength at the event (component k, step n): g G[R(n)]_k p q b
    GR_ = {n: T.einstein(R[n][0]) for n in R}
    GS_ = {n: T.einstein(S[n][0]) for n in S}
    comm = sub(mul(p1, O, S12), mul(O, p1, S12))
    ok = ok and ev(mul(I, comm, S12)) == p * q * b and p * q * b == F(180, 425)
    early = [(k, n) for n in range(ND + 1) for k, dpt in cd.items() if dpt > abs(n - ND)]
    sig = [(k, n) for (k, n) in early if g * GR_[n].get(k, 0) * p * q * b != 0]
    ok = ok and len(early) == 115792 and len(sig) == 1304
    ok = ok and g * GR_[ND][D_AXIS] * p * q * b == F(-3, 136)
    # with the field's own variables the device multiplies W(g f) by the phase exp(I strength g G[S(n)]_k):
    # the angle per unit strength vanishes at every event outside the cone, at every order in the strength
    ok = ok and all(g * GS_[n].get(k, 0) == 0 for (k, n) in early)
    ok = ok and sum(1 for n in range(ND + 1) for k, val in GS_[n].items() if val != 0) == 814
    GA.check("the slaved field with a coupled device changes the detection probability by p q [a (cos - 1) + b sin] "
             "of the angle strength g G[R]: nonzero at 1304 of the 115792 events outside the cone and not later "
             "than the detection; with the field's own variables the angle is strength g G[S], zero at all of them", ok)
    return ok


def check_in_two_space_dimensions_the_constraint_leaves_no_free_part():
    premise("synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints")
    T = Torus(LFLAT, ST2)
    n, rg, rd = ranks(T)
    # 48 components, 30 displacement directions, 15 constraints: what is left is the 3 constant fields
    ok = len(T.sites) == 16 and (n, rg, rd) == (48, 30, 15) and n - rg - rd == 3
    xi = sample_field(T, 2, 6)
    ok = ok and T.gauge(xi) != {} and T.ham(T.gauge(xi)) == {}
    # in Cl(1,2) the Einstein map of the two space directions vanishes on every symmetric map
    sp = Spacetime(3)
    for Hs, kap in FLAT_SAMPLES:
        H, kv = sp.embed(Hs), sp.space_vec(kap)
        ok = ok and sp.trace(H) == -(Hs[0][0] + Hs[1][1]) and not GA.is_zero(sp.apply(H, kv))
        ok = ok and all(GA.is_zero(sp.space_einstein(H, kv, sp.e[i])) for i in (1, 2))
    GA.check("on the periodic square lattice of 16 sites the fields with D h = 0 modulo displacements are the three "
             "constant ones: no free part at nonzero momentum, and the invariant content of h is D h; in Cl(1,2) the "
             "Einstein map of the two space directions vanishes on the sampled symmetric maps", ok)
    return ok
