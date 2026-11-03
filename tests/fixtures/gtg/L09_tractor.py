# ---- the conformal model Cl(2,4): W = span(g0, g2, g3, g4) of signature (1,3), hyperbolic plane (g1, g5) ----
S24 = GA.sig(2, 4)
W_IDX = (0, 2, 3, 4)
N0 = GA.scal(F(1, 2), GA.add(GA.gen(1), GA.gen(5)))        # null, n0 . ninf = 1
NINF = GA.sub(GA.gen(1), GA.gen(5))
BLADES2 = [(a, b) for a in range(6) for b in range(a + 1, 6)]


def t_comm(x, y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(x, y, S24), GA.mul(y, x, S24)))


def t_coords(x):
    return [x.get(bl, F(0)) for bl in BLADES2]


def t_rank(xs):
    return GA.rank_of_vectors([t_coords(x) for x in xs]) if xs else 0


def t_wbiv(i, j):
    """The bivector W_i ^ W_j of the mu-slot (i < j indices into W_IDX)."""
    return GA.mul(GA.gen(W_IDX[i]), GA.gen(W_IDX[j]), S24)


def scale_tractor(lam):
    """I_g = (1, 0, Lambda/6) in the splitting: n0 + (Lambda/6) ninf, norm I^2 = Lambda/3."""
    return GA.add(N0, GA.scal(F(lam) / 6, NINF))


def annihilates(B, I):
    """B . I = 0 for a bivector B and a vector I."""
    return GA.is_zero(GA.scal(F(1, 2), GA.sub(GA.mul(B, I, S24), GA.mul(I, B, S24))))


def lie_closure(gens):
    basis = []
    for x in gens:
        if t_rank(basis + [x]) > len(basis):
            basis.append(x)
    while True:
        grown = False
        for a in list(basis):
            for b in list(basis):
                c = t_comm(a, b)
                if c and t_rank(basis + [c]) > len(basis):
                    basis.append(c)
                    grown = True
        if not grown:
            return basis


def stabiliser(I):
    """Basis of {X bivector : X . I = 0} (kernel of the linear map on the 15 basis bivectors)."""
    cols = []
    for bl in BLADES2:
        v = GA.scal(F(1, 2), GA.sub(GA.mul({bl: F(1)}, I, S24), GA.mul(I, {bl: F(1)}, S24)))
        cols.append([v.get((a,), F(0)) for a in range(6)])
    M = [list(r) for r in zip(*cols)]
    ker = GA.field_kernel(M)
    return [{bl: c for bl, c in zip(BLADES2, k) if c != 0} for k in ker]


def killing_rank(L):
    """Rank of the intrinsic Killing form tr(ad_X ad_Y) of the Lie algebra spanned by the basis L."""
    k = len(L)
    mat = [t_coords(x) for x in L]
    piv = []
    for c in range(len(BLADES2)):
        trial = [[row[j] for j in piv + [c]] for row in mat]
        if GA.rank_of_vectors(trial) > len(piv):
            piv.append(c)
        if len(piv) == k:
            break
    sq = [[mat[j][piv[i]] for j in range(k)] for i in range(k)]

    def coords(v):
        cv = t_coords(v)
        return GA.field_solve(sq, [cv[p] for p in piv])

    ad = []
    for X in L:
        cols = [coords(t_comm(X, Y)) for Y in L]
        ad.append([[cols[j][i] for j in range(k)] for i in range(k)])
    kil = [[sum(ad[a][i][j] * ad[b][j][i] for i in range(k) for j in range(k)) for b in range(k)] for a in range(k)]
    return GA.mat_rank(kil)
# ---- end of the conformal model ----
