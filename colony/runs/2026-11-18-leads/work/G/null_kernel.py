"""Leads 4 and 5: the stored first-order Einstein map at null momentum, in Cl(1,d-1), exact.

R_k[h](B) = -1/2 k ^ h(B.k);  Ric(a) = sum_b e^b . R(e_b ^ a);  G = Ric - 1/2 id tr Ric.
A symmetric map is stored as a matrix H with h(a) = sum_{mu,nu} H[mu][nu] (a.e_mu) e_nu.
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA
from GA import add, gen, mul, scal, sub


class ST:
    """Cl(1, d-1) helper."""

    def __init__(self, d):
        self.d = d
        self.S = GA.sig(1, d - 1)
        self.eta = [1] + [-1] * (d - 1)
        self.e = [gen(i) for i in range(d)]
        self.rec = [scal(self.eta[i], self.e[i]) for i in range(d)]

    def vec(self, comps):
        return {(i,): F(c) for i, c in enumerate(comps) if c}

    def dot(self, a, b):
        return GA.dot(a, b, self.S)

    def g1(self, x):
        return {b: c for b, c in x.items() if len(b) == 1}

    def wedge(self, a, b):
        return scal(F(1, 2), sub(mul(a, b, self.S), mul(b, a, self.S)))

    def vdotB(self, a, B):
        return self.g1(scal(F(1, 2), sub(mul(a, B, self.S), mul(B, a, self.S))))

    def apply(self, H, a):
        out = {}
        for m in range(self.d):
            am = self.dot(a, self.e[m])
            if am == 0:
                continue
            for n in range(self.d):
                if H[m][n]:
                    out = add(out, scal(am * H[m][n], self.e[n]))
        return out

    def mat_of(self, f):
        """matrix M with f(a) = sum M[mu][nu] (a.e_mu) e_nu, from a linear map f on vectors."""
        M = [[F(0)] * self.d for _ in range(self.d)]
        for m in range(self.d):
            img = f(self.rec[m])                  # rec[m].e_mu = delta
            for n in range(self.d):
                M[m][n] = self.dot(img, self.rec[n])
        return M

    def riem(self, H, k, B):
        # B.k = -(k.B)
        return scal(F(-1, 2), self.wedge(k, self.apply(H, GA.neg(self.vdotB(k, B)))))

    def ricci(self, H, k):
        def ric(a):
            out = {}
            for b in range(self.d):
                out = add(out, self.vdotB(self.rec[b], self.riem(H, k, self.wedge(self.e[b], a))))
            return out
        return self.mat_of(ric)

    def trace(self, M):
        # tr = sum_a e^a . M(e_a);  M(e_a) = sum M[mu][nu] (e_a.e_mu) e_nu = eta_a M[a][nu] e_nu
        return sum(self.eta[a] * M[a][a] for a in range(self.d))

    def idmat(self):
        # id(a) = sum (a.e_mu) e^mu = sum eta_mu (a.e_mu) e_mu
        return [[F(self.eta[m]) if m == n else F(0) for n in range(self.d)] for m in range(self.d)]

    def einstein(self, H, k):
        R = self.ricci(H, k)
        t = self.trace(R)
        I = self.idmat()
        return [[R[m][n] - F(1, 2) * t * I[m][n] for n in range(self.d)] for m in range(self.d)]

    def pair(self, A, B):
        # <A, B> = sum_a A(e_a) . B(e^a) = sum_{a} eta_a A[a][n] B[a][n'] ... worked in components
        tot = F(0)
        for a in range(self.d):
            for n in range(self.d):
                tot += self.eta[a] * self.eta[n] * A[a][n] * B[a][n]
        return tot

    def outer(self, x, y):
        """the symmetric map a -> (a.x) y + (a.y) x, as a matrix; x, y component lists (contravariant)."""
        d = self.d
        # (a.x) = sum_mu x^mu (a.e_mu);  so M[mu][nu] = x^mu y^nu + y^mu x^nu
        return [[F(x[m]) * F(y[n]) + F(y[m]) * F(x[n]) for n in range(d)] for m in range(d)]

    def sym_basis(self):
        d = self.d
        out = []
        for m in range(d):
            for n in range(m, d):
                H = [[F(0)] * d for _ in range(d)]
                H[m][n] = F(1)
                H[n][m] = F(1)
                out.append(H)
        return out

    def flat(self, M):
        return [M[m][n] for m in range(self.d) for n in range(self.d)]

    def Q(self, kc):
        return sum(self.eta[i] * F(kc[i]) ** 2 for i in range(self.d))

    def lower(self, x):
        return [self.eta[i] * F(x[i]) for i in range(self.d)]

    def mdot(self, x, y):
        return sum(self.eta[i] * F(x[i]) * F(y[i]) for i in range(self.d))


def madd(A, B, c=1):
    return [[A[m][n] + c * B[m][n] for n in range(len(A))] for m in range(len(A))]


def mscal(c, A):
    return [[c * x for x in row] for row in A]


def rank(rows):
    return GA.mat_rank([list(r) for r in rows]) if rows else 0


def study(d, kc, trans, label):
    """kc: components of k; trans: list of d-2 mutually orthogonal unit spacelike vectors orthogonal to k (null k)."""
    st = ST(d)
    k = st.vec(kc)
    basis = st.sym_basis()
    nsym = len(basis)
    Gimg = [st.einstein(H, k) for H in basis]
    rk = rank([st.flat(M) for M in Gimg])
    q = st.Q(kc)
    print(f"[{label}] d={d} k={kc} Q(k)={q}: dim Sym={nsym}, rank Einstein={rk}, kernel={nsym - rk}")
    # displacements a -> (a.k) xi + (a.xi) k
    gauge = [st.outer(kc, [1 if i == j else 0 for i in range(d)]) for j in range(d)]
    rg = rank([st.flat(M) for M in gauge])
    ing = all(all(x == 0 for x in st.flat(st.einstein(M, k))) for M in gauge)
    print(f"   displacements: rank {rg}, in kernel: {ing}")
    res = dict(rank=rk, kernel=nsym - rk, gauge_rank=rg, gauge_in_kernel=ing, Q=q)
    if q == 0 and trans is not None:
        # transverse trace-free maps
        tt = []
        n = len(trans)
        for i in range(n):
            for j in range(i + 1, n):
                tt.append(st.outer(trans[i], trans[j]))
        for i in range(1, n):
            tt.append(madd(mscal(F(1, 2), st.outer(trans[0], trans[0])), mscal(F(1, 2), st.outer(trans[i], trans[i])), -1))
        intt = all(all(x == 0 for x in st.flat(st.einstein(M, k))) for M in tt)
        rtot = rank([st.flat(M) for M in gauge + tt])
        print(f"   transverse trace-free maps: {len(tt)}, in kernel: {intt}, rank(displacements + tt) = {rtot}")
        res.update(tt=len(tt), tt_in_kernel=intt, rank_gauge_tt=rtot)
        # image: conserved, and pairs to zero with the tt maps
        ok_cons = True
        ok_pair = True
        for M in Gimg:
            img = st.apply(M, k)
            ok_cons = ok_cons and GA.is_zero(img)
            ok_pair = ok_pair and all(st.pair(M, T) == 0 for T in tt)
        print(f"   image conserved: {ok_cons}; image pairs to zero with tt: {ok_pair}")
        res.update(image_conserved=ok_cons, image_perp_tt=ok_pair)
        # conserved sources at k: T(k) = 0
        rows = []
        for H in basis:
            img = st.apply(H, k)
            rows.append([st.dot(img, st.rec[i]) for i in range(d)])
        # kernel of the map Sym -> V, H -> H(k): solve by rank
        rcons = nsym - rank(rows)
        print(f"   conserved sources: dimension {rcons}; expected image dimension {rcons - len(tt)} = rank {rk}")
        res.update(conserved_dim=rcons)
        res['tt_maps'] = tt
        res['gauge'] = gauge
    return res, st


if __name__ == '__main__':
    # four dimensions
    study(4, (2, 0, 0, 0), None, 'timelike')
    study(4, (0, 1, 1, 3), None, 'spacelike')
    study(4, (1, 0, 0, 1), [(0, 1, 0, 0), (0, 0, 1, 0)], 'null')
    study(4, (5, 3, 0, 4), [(0, 0, 1, 0), (0, F(4, 5), 0, F(-3, 5))], 'null')
    study(4, (-5, 3, 0, 4), [(0, 0, 1, 0), (0, F(4, 5), 0, F(-3, 5))], 'null, other sheet')
    # controls in three and five dimensions
    study(3, (2, 0, 0), None, 'timelike')
    study(3, (1, 0, 1), [(0, 1, 0)], 'null')
    study(3, (5, 3, 4), [(0, F(4, 5), F(-3, 5))], 'null')
    study(5, (2, 0, 0, 0, 0), None, 'timelike')
    study(5, (1, 0, 0, 0, 1), [(0, 1, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0)], 'null')
