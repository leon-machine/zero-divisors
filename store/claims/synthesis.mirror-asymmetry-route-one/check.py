"""synthesis.mirror-asymmetry-route-one: the canonical reversal keeps the Witt pair and the
Fock grading; composed with the flag conjugate it exchanges them.

One split Witt pair W = <n_a, p1, p2>, W' = <n_b, q1, q2> of the 6-dimensional fibre in a fixed basis: Phi is
an anti-isometry h -> h' (real forms of signature (2,4) and (4,2)); on Lambda W' it intertwines creation,
annihilation up to -1 and every mode number operator; Phi o C is a second anti-isometry carrying W onto W';
the families of W, W', Phi W, Phi W', (Phi o C) W are computed from dim(X cap Y) mod 2. Not computed: every
Witt pair of V_C, the asymmetry per mode and its signs, and clauses (ii), (iii).
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from tp_premise import premise


def check_reversal_keeps_flag():
    premise("odd-extensions.two-towers-one-curved-universe")
    premise("dark-matter.orientation-arrow-seventeenth-refutation")
    premise("dark-matter.flag-bit-exists-exactly-tower-dimension")
    premise("dark-matter.mirror-tower-copy-one")
    premise("dark-tower-matter.mirrors-temperature-p2")
    N = 6   # order: W = [0: n_a, 1: p1, 2: p2], W' = [3: n_b, 4: q1, 5: q2]; pair j = (j, j+3)
    def gram(sig_ab, sig_mu):
        G = [[F(0)] * N for _ in range(N)]
        for j, s in zip(range(3), [sig_ab, sig_mu, sig_mu]):
            G[j][j + 3] = G[j + 3][j] = F(s)
        return G
    h, hp = gram(1, 1), gram(1, -1)
    Phi = [[F(0)] * N for _ in range(N)]
    for i in range(N): Phi[i][i] = F(-1) if i == 3 else F(1)
    T = lambda A: [list(r) for r in zip(*A)]
    GA.check("Phi is an anti-isometry: Phi^T h' Phi = -h", GA.mat_mul(GA.mat_mul(T(Phi), hp), Phi) == [[-x for x in r] for r in h])

    # the actual real forms: h on R^{2,4}, h' on R^{4,2} in a real basis (n_a, n_b, gamma_0..gamma_3)
    def real_gram(mu_sign):
        G = [[F(0)] * 6 for _ in range(6)]; G[0][1] = G[1][0] = F(1)
        for i, s in enumerate([1, -1, -1, -1]): G[2 + i][2 + i] = F(mu_sign * s)
        return G
    GA.check("real forms: this tower's tractor fibre has signature (2,4), the mirror's (4,2)",
             GA.congruence_signature(real_gram(1))[:2] == (2, 4) and GA.congruence_signature(real_gram(-1))[:2] == (4, 2))

    def isotropic(idx, G): return all(G[a][b] == 0 for a in idx for b in idx)
    Wi, Wpi = [0, 1, 2], [3, 4, 5]
    GA.check("Witt pair: W = <n_a, p1, p2> and W' = <n_b, q1, q2> are maximal isotropic for h and for h', "
             "and Phi maps each to itself (Phi is diagonal in this basis)",
             isotropic(Wi, h) and isotropic(Wpi, h) and isotropic(Wi, hp) and isotropic(Wpi, hp))

    # Fock module Lambda(W'): basis = subsets S of {0,1,2} (pair labels); c(x) = wedge(x_W') + iota(x_W),
    # iota(w) the contraction with 2 G(w, .).  Matrices 8 x 8 over Q.
    subsets = [S for k in range(4) for S in combinations(range(3), k)]
    idx = {S: i for i, S in enumerate(subsets)}
    def zero(): return [[F(0)] * 8 for _ in range(8)]
    def wedge(j):
        M = zero()
        for S in subsets:
            if j in S: continue
            Tn = tuple(sorted(S + (j,))); sign = (-1) ** sum(1 for s in S if s < j)
            M[idx[Tn]][idx[S]] = F(sign)
        return M
    def contract(j, G):
        """iota of the annihilator w_j (basis index j of W) against creation v_j (index j+3)."""
        M = zero(); c = 2 * G[j][j + 3]
        for S in subsets:
            if j not in S: continue
            Tn = tuple(s for s in S if s != j); sign = (-1) ** sum(1 for s in S if s < j)
            M[idx[Tn]][idx[S]] = c * sign
        return M
    mmul = GA.mat_mul
    def sc(c, M): return [[c * x for x in r] for r in M]
    def addm(A, B): return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]
    # LambdaPhi derived from Phi: Phi must carry W' onto an h'-isotropic subspace of W', and on the
    # basis v_S = v_{s1} ^ ... ^ v_{sk} (s1 < ... < sk) it acts by the k x k minors of Phi's W' block
    GA.check("Phi maps W' into W', onto a subspace isotropic for the mirror form h'",
             all(Phi[i][j] == 0 for j in Wpi for i in Wi)
             and all(sum(Phi[a][x] * hp[a][b] * Phi[b][y] for a in range(N) for b in range(N)) == 0
                     for x in Wpi for y in Wpi))
    def det(M):
        if not M: return F(1)
        return sum((-1) ** c * M[0][c] * det([r[:c] + r[c + 1:] for r in M[1:]]) for c in range(len(M)))
    LPhi = zero()
    for S in subsets:
        for Tn in subsets:
            if len(Tn) == len(S):
                LPhi[idx[Tn]][idx[S]] = det([[Phi[t + 3][s + 3] for s in S] for t in Tn])

    ok = True
    for j in range(3):
        cre, cre_p = wedge(j), wedge(j)
        ann, ann_p = contract(j, h), contract(j, hp)
        # Clifford relations of each form
        ok = ok and addm(mmul(cre, ann), mmul(ann, cre)) == sc(2 * h[j][j + 3], [[F(int(a == b)) for b in range(8)] for a in range(8)])
        ok = ok and addm(mmul(cre_p, ann_p), mmul(ann_p, cre_p)) == sc(2 * hp[j][j + 3], [[F(int(a == b)) for b in range(8)] for a in range(8)])
        # images under the theorem's Phi (rho -> -rho, n_b the rho-direction): Phi(v_j) = -v_0 for j = 0
        # else v_j; Phi(w_j) = w_j.  LambdaPhi above is derived from the matrix Phi, so a Phi whose
        # sign sits elsewhere fails the intertwining checks below
        sv = F(-1) if j == 0 else F(1)
        ok = ok and mmul(sc(sv, cre_p), LPhi) == mmul(LPhi, cre)                 # creation intertwined
        ok = ok and mmul(ann_p, LPhi) == sc(F(-1), mmul(LPhi, ann))              # annihilation: sign -1 (Phi w_j = w_j)
        # number operators N_j = c(v_j) c(w_j) / (2 G(w_j, v_j)), each form with its own Phi-images
        Nj = sc(1 / (2 * h[j][j + 3]), mmul(cre, ann))
        hpv = hp[j][j + 3] * sv                     # h'(Phi w_j, Phi v_j)
        Njp = sc(1 / (2 * hpv), mmul(sc(sv, cre_p), ann_p))
        ok = ok and mmul(Njp, LPhi) == mmul(LPhi, Nj)
        ok = ok and hpv == -h[j][j + 3]             # the reversal flips every pairing
    GA.check("Fock: LambdaPhi intertwines creation, intertwines annihilation up to the sign -1, flips the sign of every pairing h'(Phi w, Phi v) = -h(w, v), "
             "and intertwines every mode number operator exactly (the two signs cancel)", ok)
    G = zero()
    for j in range(3): G = addm(G, sc(1 / (2 * h[j][j + 3]), mmul(wedge(j), contract(j, h))))
    GA.check("Fock: the grade operator is diagonal with the subset sizes, so Phi carries grade k to grade k "
             "(particles to particles)", all(G[idx[S]][idx[S]] == len(S) for S in subsets))

    # the flag conjugate C: v_j <-> w_j (an isometry of h and of h'), and Phi o C
    C = [[F(0)] * N for _ in range(N)]
    for j in range(3): C[j][j + 3] = C[j + 3][j] = F(1)
    PC = GA.mat_mul(Phi, C)
    GA.check("conjugate: C is an isometry of h; Phi o C is a second anti-isometry h -> h', and it carries "
             "W onto W' (columns of W map into span W')",
             GA.mat_mul(GA.mat_mul(T(C), h), C) == h
             and GA.mat_mul(GA.mat_mul(T(PC), hp), PC) == [[-x for x in r] for r in h]
             and all(PC[i][j] == 0 for j in Wi for i in Wi))
    # families: two maximal isotropic subspaces X, Y (dimension m = 3) of one split form lie in the same family
    # iff dim(X cap Y) = m mod 2; dim(X cap Y) = dim X + dim Y - rank(X + Y)
    def image(A, cols):
        return [[A[i][j] for i in range(N)] for j in cols]

    def meet(X, Y):
        return len(X) + len(Y) - GA.rank_of_vectors(X + Y)

    def is_maximal_isotropic(X, G):
        return GA.rank_of_vectors(X) == 3 and all(
            sum(x[a] * G[a][b] * y[b] for a in range(N) for b in range(N)) == 0 for x in X for y in X)
    W = [[F(int(i == j)) for i in range(N)] for j in Wi]
    Wp = [[F(int(i == j)) for i in range(N)] for j in Wpi]
    PW, PWp, PCW = image(Phi, Wi), image(Phi, Wpi), image(PC, Wi)
    fam_ok = is_maximal_isotropic(W, h) and is_maximal_isotropic(Wp, h)
    fam_ok = fam_ok and all(is_maximal_isotropic(X, hp) for X in (PW, PWp, PCW))
    fam_ok = fam_ok and meet(W, Wp) == 0 and (3 - meet(W, Wp)) % 2 == 1        # W, W' opposite families of h
    fam_ok = fam_ok and meet(PW, W) == 3                                       # Phi W = W
    fam_ok = fam_ok and meet(PCW, PWp) == 3                                    # (Phi o C) W = Phi W'
    fam_ok = fam_ok and meet(PCW, PW) == 0 and (3 - meet(PCW, PW)) % 2 == 1    # opposite family to Phi W
    GA.check("families (computed by dim(X cap Y) mod 2): W and W' meet in 0, m = 3 odd, so they lie in opposite "
             "families of h; Phi W = W, and (Phi o C) W = Phi W' meets Phi W in 0, so it lies in the other family "
             "of h': the two anti-isometries differ by the flag bit", fam_ok)
    assert fam_ok
