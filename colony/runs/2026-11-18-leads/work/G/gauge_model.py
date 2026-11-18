"""Lead 3: the lattice model with a constraint. Exploration script (exact arithmetic).

Field: lattice Maxwell field on a box of sites, link variables (A, E) with [E_l, W(f)] = f_l W(f) for the Weyl
operator W(f) = exp(I sum f_l A_l); Gauss constraint G_s = (div E)_s - g rho_s.
Matter: one quantum on two sites a, b: Cl(1,1), P1 = vw (site a), P2 = wv (site b), v = P1 v P2 the hop b -> a.
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA
from GA import add, gen, mul, scal, sc, sub

S11 = GA.sig(1, 1)


class Box:
    def __init__(self, nx, ny):
        self.nx, self.ny = nx, ny
        self.sites = [(x, y) for x in range(nx) for y in range(ny)]
        self.links = [('x', x, y) for x in range(nx - 1) for y in range(ny)] + \
                     [('y', x, y) for x in range(nx) for y in range(ny - 1)]
        self.lidx = {l: i for i, l in enumerate(self.links)}
        self.plaq = [(x, y) for x in range(nx - 1) for y in range(ny - 1)]
        # boundary of each plaquette: (link, sign)
        self.pl = {p: [(('x', p[0], p[1]), 1), (('y', p[0] + 1, p[1]), 1), (('x', p[0], p[1] + 1), -1),
                       (('y', p[0], p[1]), -1)] for p in self.plaq}
        self.lp = {l: [] for l in self.links}
        for p, bd in self.pl.items():
            for l, s in bd:
                self.lp[l].append((p, s))
        # neighbours of a link: links sharing a plaquette
        self.nb = {l: sorted({m for p, _ in self.lp[l] for m, _ in self.pl[p]} - {l}) for l in self.links}

    def ends(self, l):
        k, x, y = l
        return ((x, y), (x + 1, y)) if k == 'x' else ((x, y), (x, y + 1))

    def div(self, f):
        """(div f)_s = sum of f on links leaving s minus links entering s; f a dict link -> value."""
        out = {}
        for l, val in f.items():
            if val == 0:
                continue
            s0, s1 = self.ends(l)
            out[s0] = out.get(s0, 0) + val
            out[s1] = out.get(s1, 0) - val
        return {s: c for s, c in out.items() if c != 0}

    def grad(self, u):
        """(grad u)_l = u(start) - u(end): then div grad u = (graph Laplacian) u."""
        return {l: u[self.ends(l)[0]] - u[self.ends(l)[1]] for l in self.links}

    def curl(self, A):
        return {p: sum(s * A.get(l, 0) for l, s in bd) for p, bd in self.pl.items()}

    def curlT(self, B):
        return {l: sum(s * B.get(p, 0) for p, s in self.lp[l]) for l in self.links}

    def solve_poisson(self, rho):
        """u with (graph Laplacian) u = rho, sum rho = 0, u(first site) = 0; exact."""
        n = len(self.sites)
        sidx = {s: i for i, s in enumerate(self.sites)}
        M = [[F(0)] * (n + 1) for _ in range(n)]
        for l in self.links:
            s0, s1 = self.ends(l)
            i, j = sidx[s0], sidx[s1]
            M[i][i] += 1
            M[j][j] += 1
            M[i][j] -= 1
            M[j][i] -= 1
        for s, c in rho.items():
            M[sidx[s]][n] = F(c)
        # fix u[0] = 0: replace first equation
        M[0] = [F(1)] + [F(0)] * n
        # gaussian elimination
        for c in range(n):
            piv = next(r for r in range(c, n) if M[r][c] != 0)
            M[c], M[piv] = M[piv], M[c]
            pv = M[c][c]
            M[c] = [x / pv for x in M[c]]
            for r in range(n):
                if r != c and M[r][c] != 0:
                    fac = M[r][c]
                    M[r] = [x - fac * y for x, y in zip(M[r], M[c])]
        return {s: M[sidx[s]][n] for s in self.sites}

    def longitudinal(self, f):
        """the gradient part of f: grad of the solution of Laplacian u = div f."""
        return self.grad(self.solve_poisson(self.div(f)))

    def dist_from(self, links):
        d = {l: 0 for l in links}
        frontier = list(links)
        while frontier:
            nxt = []
            for l in frontier:
                for m in self.nb[l]:
                    if m not in d:
                        d[m] = d[l] + 1
                        nxt.append(m)
            frontier = nxt
        return d

    # exact one-step maps (symplectic): E' = E + h curlT curl A ; A' = A - h E'
    def step(self, E, A, h):
        cc = self.curlT(self.curl(A))
        E2 = {l: E.get(l, 0) + h * cc[l] for l in self.links}
        A2 = {l: A.get(l, 0) - h * E2[l] for l in self.links}
        return E2, A2

    def unstep(self, E2, A2, h):
        A = {l: A2.get(l, 0) + h * E2.get(l, 0) for l in self.links}
        cc = self.curlT(self.curl(A))
        E = {l: E2.get(l, 0) - h * cc[l] for l in self.links}
        return E, A


def string_x(y, x0, x1):
    """unit flux on the x-links from (x0, y) to (x1, y), x0 < x1, oriented along +x."""
    return {('x', x, y): F(1) for x in range(x0, x1)}


def matter(p, q):
    e1, e2 = gen(0), gen(1)
    v = scal(F(1, 2), add(e1, e2))
    w = scal(F(1, 2), sub(e1, e2))
    P1, P2 = mul(v, w, S11), mul(w, v, S11)
    return dict(e1=e1, e2=e2, v=v, w=w, P1=P1, P2=P2)


if __name__ == '__main__':
    # ---- kinematics on a 9 x 9 box
    bx = Box(9, 9)
    a, b = (3, 4), (5, 4)
    # moving the quantum from b to a at fixed constraint: div of the shift must be +1 at a, -1 at b
    C = {l: -val for l, val in string_x(4, 3, 5).items()}          # flux from a ... oriented -x: leaves a towards smaller x?
    print("div of candidate string:", bx.div(C))
    kap = bx.longitudinal(C)
    off = [l for l in bx.links if l not in C]
    nz = [l for l in off if kap[l] != 0]
    print("links:", len(bx.links), " off the string:", len(off), " longitudinal part nonzero off the string:", len(nz))
    print("div of longitudinal part equals div of string:", bx.div(kap) == bx.div(C))
    print("sample values of the longitudinal part:", kap[('x', 3, 4)], kap[('x', 0, 4)], kap[('y', 4, 0)], kap[('x', 7, 7)])
    tr = {l: C.get(l, 0) - kap[l] for l in bx.links}
    print("transverse part divergence-free:", bx.div(tr) == {})
    # one space dimension
    ch = Box(13, 1)
    C1 = {l: -val for l, val in string_x(0, 4, 8).items()}
    k1 = ch.longitudinal(C1)
    print("chain: longitudinal part equals the string:", all(k1[l] == C1.get(l, 0) for l in ch.links))
    # ---- dynamics on a 21 x 21 box
    bx = Box(21, 21)
    h = F(1, 2)
    C = {l: -val for l, val in string_x(10, 9, 11).items()}
    ND, NMAX = 8, 16
    dist = bx.dist_from(list(C))
    # string inserted at step ND: forward and backward
    S = {ND: dict(C)}
    E, A = dict(C), {}
    for n in range(ND, NMAX):
        E, A = bx.step(E, A, h)
        S[n + 1] = E
    E, A = dict(C), {}
    for n in range(ND, 0, -1):
        E, A = bx.unstep(E, A, h)
        S[n - 1] = E
    spacelike = [(l, n) for n in range(NMAX + 1) for l in bx.links if dist[l] > abs(n - ND)]
    bad_full = [(l, n) for (l, n) in spacelike if S[n].get(l, 0) != 0]
    print("spacelike events:", len(spacelike), " full field, string-dressed: nonzero at", len(bad_full))
    # slaved retarded constrained field: the split at step 0 lays the same string (routes o -> a, o -> b)
    D = {0: dict(C)}
    E, A = dict(C), {}
    for n in range(0, NMAX):
        E, A = bx.step(E, A, h)
        D[n + 1] = E
    bad_slaved = [(l, n) for (l, n) in spacelike if D[n].get(l, 0) != 0]
    print("slaved retarded constrained field: nonzero at", len(bad_slaved), "of", len(spacelike))
    # instantaneous constrained part alone
    kap = bx.longitudinal(C)
    bad_inst = [(l, n) for (l, n) in spacelike if kap[l] != 0]
    print("instantaneous constrained part: nonzero at", len(bad_inst), "of", len(spacelike))
    # gauss law conserved by the dynamics
    print("div conserved along the slaved evolution:", all(bx.div(D[n]) == bx.div(C) for n in D))
    print("sample D values:", D[8].get(('x', 13, 10)), D[8].get(('y', 12, 12)), D[16].get(('x', 3, 3)))
    print("max denominators:", max(v.denominator for n in D for v in D[n].values() if v != 0))
