"""Kugo-Ojima quartets at every number of quanta for the gluons and the massive vectors: exact checks.

One-particle data (real; the Krein form is <x, y>_K = <x, J y>_+ with J a signed permutation of an orthonormal basis):
gluon at a null k: polarisation modes e_0..e_3 (Krein Gram -g, the Gupta-Bleuler form), ghost c (gh +1), antighost cb
(gh -1), <c, cb>_K = 1; Q1|u> = -(k.u)|c>, Q1|cb> = |k>. Massive vector at timelike p with a Goldstone mode phi
(Krein +1): Q1|u> = -(p.u)|c>, Q1 phi = beta c, Q1 cb = |p> + beta phi (fixed by Krein self-adjointness).
Fock space: the graded-symmetric algebra on the modes (bosons: polynomials with <z^n, z^n>_+ = n!, the palatial
form; ghosts: exterior monomials, orthonormal, the tower floor's trace form), operators second-quantised as
graded derivations dGamma, Krein form <x, Gamma(J) y>_+.
(1) One particle: Q1^2 = 0 and Q1 Krein-self-adjoint for k = (5,3,4,0) and for p = (5,4,0,0), beta = 3 (beta^2 = Q(p));
    beta = 2 is not nilpotent; an odd R1 with Q1 R1 + R1 Q1 = P exists, P the projection onto the quartet span
    (span{k, kb, c, cb}, resp. span{p, phi, c, cb}) along the physical span (transverse plane, resp. p-perp), which
    is Krein-orthogonal to the quartet span and Krein-positive (Gram 25, 1, resp. 9, 1, 1).
(2) Fock space: on every sector with T quanta (T <= 4 gluon, T <= 3 massive): Q^2 = 0, Q Krein-self-adjoint and
    Q R + R Q = dGamma(P) = N_q, the number of quartet quanta.
(3) Ghost-number-zero cohomology dimensions: gluon 1, 2, 3, 4, 5 (T = 0..4), massive 1, 3, 6, 10 (T = 0..3), two
    gluon colours 1, 4, 10, 20 (T = 0..3): the symmetric powers of the physical span; the Krein form on ker Q has
    signature (dim H, 0, rank of Q into ghost number zero).
(4) The gauge algebra broken by two hypercharge-1/2 doublets with a neutral aligned vacuum (input): the Goldstone map
    a -> (T_a phi_1, T_a phi_2) has rank 3 (computed), so nine vectors stay massless and three are massive, the unbroken
    u(1) mixing T3 and Y; the one-particle direct sum is Krein-self-adjoint with a homotopy, physical span of dimension
    9*2 + 3*3 = 27 and Krein signature (27, 0, 0); 8 - 3 = 5 physical scalars.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement

import GA
from tp_premise import premise

G4 = (1, -1, -1, -1)


def mdot(u, w):
    return sum((F(G4[m]) * u[m] * w[m] for m in range(4)), F(0))


class OneParticle(object):
    """Real one-particle space with basis modes; parity par[i]; positive form diagonal (orthonormal basis);
    fundamental symmetry J (signed permutation matrix as dict i -> (j, sign)): Krein form <x, y>_K = <x, J y>_+."""

    def __init__(self, names, par, J):
        self.names, self.par, self.J = names, par, J
        self.n = len(names)

    def krein(self):
        M = [[F(0)] * self.n for _ in range(self.n)]
        for j, (i, sg) in self.J.items():
            M[i][j] = F(sg)
        return M


def direct_sum(ops):
    names, par, J = [], [], {}
    off = 0
    for V in ops:
        names += [(off, x) for x in V.names]
        par += V.par
        for j, (i, sg) in V.J.items():
            J[j + off] = (i + off, sg)
        off += V.n
    return OneParticle(names, par, J)


def block(*Ms):
    n = sum(len(M) for M in Ms)
    out = [[F(0)] * n for _ in range(n)]
    off = 0
    for M in Ms:
        for i in range(len(M)):
            for j in range(len(M)):
                out[off + i][off + j] = M[i][j]
        off += len(M)
    return out


# ---------------------------------------------------------------- one-particle data
def gluon(k, kb):
    """Modes e_0..e_3 (polarisations, Krein Gram -g), c (gh +1), cb (gh -1) with <c, cb>_K = 1.
    Q1|u> = -(k.u)|c>, Q1|cb> = |k>; R1|k> = |cb>, R1|c> = -|kb>, zero on kb and on the transverse plane."""
    V = OneParticle(['e0', 'e1', 'e2', 'e3', 'c', 'cb'], [0, 0, 0, 0, 1, 1],
                    {0: (0, -1), 1: (1, 1), 2: (2, 1), 3: (3, 1), 4: (5, 1), 5: (4, 1)})
    n = 6
    Q = [[F(0)] * n for _ in range(n)]
    for m in range(4):
        Q[4][m] = -F(G4[m]) * k[m]          # coefficient of c in Q1 e_m = -(k . e_m)
        Q[m][5] = F(k[m])                    # Q1 cb = sum k^m e_m
    return V, Q


def massive(p, beta):
    """Modes e_0..e_3, Goldstone phi (Krein +1), c, cb.  Q1|u> = -(p.u)|c>, Q1 phi = beta c,
    Q1 cb = |p> + beta phi (fixed by Krein self-adjointness)."""
    V = OneParticle(['e0', 'e1', 'e2', 'e3', 'phi', 'c', 'cb'], [0, 0, 0, 0, 0, 1, 1],
                    {0: (0, -1), 1: (1, 1), 2: (2, 1), 3: (3, 1), 4: (4, 1), 5: (6, 1), 6: (5, 1)})
    n = 7
    Q = [[F(0)] * n for _ in range(n)]
    for m in range(4):
        Q[5][m] = -F(G4[m]) * p[m]
        Q[m][6] = F(p[m])
    Q[5][4] = F(beta)
    Q[4][6] = F(beta)
    return V, Q


def mm(A, B):
    return GA.mat_mul(A, B)


def madd(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(len(A))] for i in range(len(A))]


def solve_homotopy(V, Q, P):
    """Find an odd R with Q R + R Q = P (linear system in the odd entries of R)."""
    n = V.n
    unk = [(i, j) for i in range(n) for j in range(n) if V.par[i] != V.par[j]]
    rows = []
    for a in range(n):
        for b in range(n):
            row = []
            for (i, j) in unk:
                # (Q R)_{ab} gets Q[a][i] if j == b; (R Q)_{ab} gets Q[j][b] if i == a
                v = (Q[a][i] if j == b else F(0)) + (Q[j][b] if i == a else F(0))
                row.append(v)
            row.append(-P[a][b])
            rows.append(row)
    ker = GA.field_kernel(rows)
    pick = [v for v in ker if v[-1] != 0]
    if not pick:
        return None
    v = pick[0]
    R = [[F(0)] * n for _ in range(n)]
    for t, (i, j) in enumerate(unk):
        R[i][j] = v[t] / v[-1]
    return R


# ---------------------------------------------------------------- graded Fock space
def normal(lst, par):
    """Sort a word of modes; sign (-1)^{p_i p_j} per transposition; repeated odd mode gives 0."""
    lst = list(lst)
    sg = 1
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            if par[lst[j - 1]] and par[lst[j]]:
                sg = -sg
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1] and par[lst[i]]:
            return 0, None
    return sg, tuple(lst)


def sector(V, T):
    out = []
    for w in combinations_with_replacement(range(V.n), T):
        if any(w[i] == w[i + 1] and V.par[w[i]] for i in range(T - 1)):
            continue
        out.append(w)
    return out


def dGamma(V, X, xpar, state):
    """Second quantisation of the one-particle operator X (parity xpar) on a monomial: graded derivation."""
    out = {}
    passed = 0
    for r, j in enumerate(state):
        sg0 = -1 if (xpar and passed % 2) else 1
        for i in range(V.n):
            if X[i][j] == 0:
                continue
            w = state[:r] + (i,) + state[r + 1:]
            sg, w2 = normal(w, V.par)
            if sg == 0:
                continue
            out[w2] = out.get(w2, F(0)) + sg0 * sg * X[i][j]
        passed += V.par[j]
    return {w: c for w, c in out.items() if c != 0}


def apply(V, X, xpar, vec):
    out = {}
    for w, c in vec.items():
        for w2, c2 in dGamma(V, X, xpar, w).items():
            out[w2] = out.get(w2, F(0)) + c * c2
    return {w: c for w, c in out.items() if c != 0}


def _fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def pos_norm(w):
    out = 1
    i = 0
    while i < len(w):
        j = i
        while j < len(w) and w[j] == w[i]:
            j += 1
        out *= _fact(j - i)
        i = j
    return F(out)


def gammaJ(V, w):
    lst = []
    sg = 1
    for j in w:
        i, s = V.J[j]
        lst.append(i)
        sg *= s
    s2, w2 = normal(lst, V.par)
    return sg * s2, w2


def krein(V, u, w):
    """<u, w>_K = <u, Gamma(J) w>_+ on monomials."""
    sg, w2 = gammaJ(V, w)
    return pos_norm(u) * sg if w2 == u else F(0)


def ghost(V, w, gh):
    return sum(gh[j] for j in w)




# ---------------------------------------------------------------- data of the checks
K_NULL = (5, 3, 4, 0)
KB_NULL = (F(1, 10), F(-3, 50), F(-4, 50), F(0))
P_MASS = (5, 4, 0, 0)


def _vecs(rows):
    return [[F(x) for x in r] for r in rows]


def _proj(basisv, keep):
    n = len(basisv)
    B = [[basisv[j][i] for j in range(n)] for i in range(n)]
    cols = [GA.field_solve([r[:] for r in B], [F(int(i == e)) for i in range(n)]) for e in range(n)]
    Binv = [[cols[j][i] for j in range(n)] for i in range(n)]
    Dg = [[F(int(i == j and i in keep)) for j in range(n)] for i in range(n)]
    return mm(B, mm(Dg, Binv))


def _gluon_data():
    V, Q = gluon(K_NULL, KB_NULL)
    bv = _vecs([list(K_NULL) + [0, 0], list(KB_NULL) + [0, 0], [0, 4, -3, 0, 0, 0], [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])
    return V, Q, bv, [0, 1, 4, 5], [2, 3], [0, 0, 0, 0, 1, -1]


def _massive_data(beta):
    V, Q = massive(P_MASS, beta)
    bv = _vecs([[5, 4, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [4, 5, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]])
    return V, Q, bv, [0, 1, 5, 6], [2, 3, 4], [0, 0, 0, 0, 0, 1, -1]


def _tr(A):
    return [list(r) for r in zip(*A)]


def _one_particle(V, Q, bv, quart, phys):
    K = V.krein()
    n = V.n
    ipK = lambda u, w: sum((u[i] * K[i][j] * w[j] for i in range(n) for j in range(n)), F(0))
    ok = all(x == 0 for r in mm(Q, Q) for x in r) and GA.mat_eq(mm(K, Q), mm(_tr(Q), K))
    P = _proj(bv, quart)
    R = solve_homotopy(V, Q, P)
    ok = ok and R is not None
    ok = ok and all(ipK(bv[i], bv[j]) == 0 for i in phys for j in quart)
    ok = ok and all(not any(x != 0 for x in GA.mat_mul(Q, [[y] for y in bv[i]])[r]) for i in phys
                    for r in range(n))
    gram = [ipK(bv[i], bv[i]) for i in phys]
    return ok, P, R, gram


def _sector_ops(V, X, xpar, S):
    return {w: apply(V, X, xpar, {w: F(1)}) for w in S}


def _fock_checks(V, Q, R, P, S):
    Qs = _sector_ops(V, Q, 1, S)
    ok = True
    for w in S:
        ok = ok and not apply(V, Q, 1, Qs[w])
        lhs = apply(V, Q, 1, apply(V, R, 1, {w: F(1)}))
        for x, c in apply(V, R, 1, Qs[w]).items():
            lhs[x] = lhs.get(x, F(0)) + c
        lhs = {x: c for x, c in lhs.items() if c != 0}
        ok = ok and lhs == apply(V, P, 0, {w: F(1)})
    # Krein self-adjointness: <u, Q w>_K = <u, Gamma(J) Q w>_+ equals <Q u, w>_K = <Q u, Gamma(J) w>_+
    M1, M2 = {}, {}
    for w in S:
        for x, c in Qs[w].items():
            sg, x2 = gammaJ(V, x)
            if sg:
                M1[(x2, w)] = M1.get((x2, w), F(0)) + pos_norm(x2) * sg * c
    for u in S:
        for w in S:
            sg, w2 = gammaJ(V, w)
            c = Qs[u].get(w2, F(0)) if sg else F(0)
            if c:
                M2[(u, w)] = pos_norm(w2) * sg * c
    ok = ok and {k: v for k, v in M1.items() if v} == M2 and (len(M2) > 0 or len(S) == 1)
    return ok


def _cohomology(V, Q, gh, T):
    S = sector(V, T)
    sec = {g: [w for w in S if ghost(V, w, gh) == g] for g in (-1, 0, 1)}

    def mat(src, dst):
        di = {w: i for i, w in enumerate(dst)}
        M = [[F(0)] * len(src) for _ in dst]
        for j, w in enumerate(src):
            for w2, c in apply(V, Q, 1, {w: F(1)}).items():
                M[di[w2]][j] = c
        return M
    C0 = sec[0]
    r0 = GA.mat_rank(mat(C0, sec[1])) if sec[1] else 0
    rm = GA.mat_rank(mat(sec[-1], C0)) if sec[-1] else 0
    h = len(C0) - r0 - rm
    ker = GA.field_kernel(mat(C0, sec[1])) if sec[1] else [[F(int(i == j)) for j in range(len(C0))]
                                                           for i in range(len(C0))]
    pos = {w: i for i, w in enumerate(C0)}
    Kn = []
    for j, w in enumerate(C0):
        sg, w2 = gammaJ(V, w)
        if sg and w2 in pos:
            Kn.append((pos[w2], j, pos_norm(w2) * sg))
    Gk = [[sum((u[i] * c * v[j] for i, j, c in Kn), F(0)) for v in ker] for u in ker]
    return h, GA.congruence_signature(Gk) == (h, 0, rm)


def _explicit_gluon_R():
    # R1 k = cb, R1 kb = 0, R1 t = 0 (transverse), R1 c = -kb
    n = 6
    R = [[F(0)] * n for _ in range(n)]
    M = _vecs([list(K_NULL), list(KB_NULL), [0, 4, -3, 0], [0, 0, 0, 1]])
    x = GA.field_solve(M, [F(1), F(0), F(0), F(0)])
    for m in range(4):
        R[5][m] = x[m]
        R[m][4] = -KB_NULL[m]
    return R


def _explicit_massive_R(beta):
    # R1 c = phi / beta, R1 p = cb, R1 zero on phi, cb and p-perp
    n = 7
    R = [[F(0)] * n for _ in range(n)]
    R[4][5] = F(1) / beta
    M = _vecs([list(P_MASS), [4, 5, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    x = GA.field_solve(M, [F(1), F(0), F(0), F(0)])
    for m in range(4):
        R[6][m] = x[m]
    return R


def check_one_particle_quartets_and_homotopies():
    premise("synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts")
    ok = mdot(K_NULL, K_NULL) == 0 and mdot(KB_NULL, KB_NULL) == 0 and mdot(K_NULL, KB_NULL) == 1
    ok = ok and mdot(P_MASS, P_MASS) == 9
    V, Q, bv, quart, phys, gh = _gluon_data()
    o, P, R, gram = _one_particle(V, Q, bv, quart, phys)
    ok = ok and o and gram == [25, 1]
    Rg = _explicit_gluon_R()
    ok = ok and GA.mat_eq(madd(mm(Q, Rg), mm(Rg, Q)), P)
    V, Q, bv, quart, phys, gh = _massive_data(3)
    o, P, R, gram = _one_particle(V, Q, bv, quart, phys)
    ok = ok and o and gram == [9, 1, 1]
    Rm = _explicit_massive_R(3)
    ok = ok and GA.mat_eq(madd(mm(Q, Rm), mm(Rm, Q)), P)
    V2, Q2 = massive(P_MASS, 2)
    ok = ok and any(x != 0 for r in mm(Q2, Q2) for x in r)
    GA.check("one particle: Q1 nilpotent and Krein-self-adjoint (beta^2 = Q(p) = 9 forced), homotopy R1 with"
             " {Q1, R1} = P, physical span Krein-orthogonal and positive (25, 1; 9, 1, 1)", ok)
    return ok


def check_second_quantised_homotopy_counts_quartet_quanta():
    premise("synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts")
    premise("field-theory.imported-statistics-no-go-palatial-algebra")
    premise("field-theory.imported-tower-limit")
    ok = True
    for data, tmax in ((_gluon_data(), 4), (_massive_data(3), 3)):
        V, Q, bv, quart, phys, gh = data
        P = _proj(bv, quart)
        R = solve_homotopy(V, Q, P)
        sizes = []
        for T in range(tmax + 1):
            S = sector(V, T)
            sizes.append(len(S))
            ok = ok and _fock_checks(V, Q, R, P, S)
        ok = ok and sizes in ([1, 6, 19, 44, 85], [1, 7, 26, 70])
    GA.check("Fock space: Q^2 = 0, Q Krein-self-adjoint, Q R + R Q = N_q on every sector T <= 4 (gluon),"
             " T <= 3 (massive)", ok)
    return ok


def check_cohomology_is_the_positive_physical_fock_space():
    premise("synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts")
    V, Q, bv, quart, phys, gh = _gluon_data()
    res = [_cohomology(V, Q, gh, T) for T in range(5)]
    ok = [h for h, s in res] == [1, 2, 3, 4, 5] and all(s for h, s in res)
    V, Q, bv, quart, phys, gh = _massive_data(3)
    res = [_cohomology(V, Q, gh, T) for T in range(4)]
    ok = ok and [h for h, s in res] == [1, 3, 6, 10] and all(s for h, s in res)
    Vg, Qg, bvg, quart, phys, ghg = _gluon_data()
    V2 = direct_sum([Vg, Vg])
    Q2 = block(Qg, Qg)
    res = [_cohomology(V2, Q2, ghg + ghg, T) for T in range(4)]
    ok = ok and [h for h, s in res] == [1, 4, 10, 20] and all(s for h, s in res)
    GA.check("ghost-number-zero cohomology 1..5 (gluon), 1, 3, 6, 10 (massive), 1, 4, 10, 20 (two colours),"
             " Krein form positive on it with radical im Q", ok)
    return ok


def _doublet_generators():
    """The twelve generators acting on one hypercharge-1/2 doublet (2 x 2, Gaussian rationals): su(2) anti-Hermitian
    basis, su(3) trivially (the doublets are colour singlets), u(1) as (i/2) times the identity."""
    Z, O, I = GA.QI(0), GA.QI(1), GA.QI(0, 1)
    su2 = [[[I, Z], [Z, GA.QI(0, -1)]], [[Z, O], [GA.QI(-1), Z]], [[Z, I], [I, Z]]]
    zero = [[Z, Z], [Z, Z]]
    hyp = [[GA.QI(0, F(1, 2)), Z], [Z, GA.QI(0, F(1, 2))]]
    return su2 + [zero] * 8 + [hyp]


def _goldstone_map(gens, vevs):
    """Real matrix of a -> (T_a phi_1, T_a phi_2) in R^8 (real and imaginary parts)."""
    cols = []
    for T in gens:
        col = []
        for phi in vevs:
            for r in range(2):
                z = T[r][0] * phi[0] + T[r][1] * phi[1]
                col += [z.re, z.im]
        cols.append(col)
    return [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))]


def check_broken_gauge_algebra_one_particle_count():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    gens = _doublet_generators()
    # input: both doublets take neutral, aligned vacuum values (0, v_1), (0, v_2)
    vevs = [(GA.QI(0), GA.QI(3)), (GA.QI(0), GA.QI(4))]
    G = _goldstone_map(gens, vevs)
    n_gauge = len(gens)
    n_massive = GA.mat_rank(G)
    n_scalar_real = len(G)
    ker = GA.field_kernel(G)
    ok = n_gauge == 12 and n_massive == 3 and n_scalar_real == 8 and len(ker) == 9
    # the unbroken electroweak direction mixes the diagonal su(2) generator with hypercharge
    ew = [v for v in ker if any(v[i] != 0 for i in (0, 1, 2, 11))]
    ok = ok and len(ew) == 1 and ew[0][0] != 0 and ew[0][11] != 0
    Vg, Qg, bvg, qg, pg, ghg = _gluon_data()
    Vm, Qm, bvm, qm, pm, ghm = _massive_data(3)
    parts = [(Vg, Qg, bvg, qg, pg)] * (n_gauge - n_massive) + [(Vm, Qm, bvm, qm, pm)] * n_massive
    V = direct_sum([x[0] for x in parts])
    K = V.krein()
    # the operators are block diagonal: every identity is checked block by block
    rank_P = 0
    for x in parts:
        Kx = x[0].krein()
        Px = _proj(x[2], x[3])
        Rx = solve_homotopy(x[0], x[1], Px)
        ok = ok and Rx is not None and GA.mat_eq(mm(Kx, x[1]), mm(_tr(x[1]), Kx))
        if not ok:
            return False
        ok = ok and GA.mat_eq(madd(mm(x[1], Rx), mm(Rx, x[1])), Px)
        ok = ok and all(y == 0 for r in mm(x[1], x[1]) for y in r)
        rank_P += GA.mat_rank(Px)
    # Krein Gram of the physical span (block-embedded physical basis vectors)
    phys = []
    off = 0
    for x in parts:
        for i in x[4]:
            phys.append([F(0)] * off + x[2][i] + [F(0)] * (V.n - off - len(x[2][i])))
        off += x[0].n
    Knz = [(i, j, K[i][j]) for i in range(V.n) for j in range(V.n) if K[i][j] != 0]
    Gp = [[sum((u[i] * k * w[j] for i, j, k in Knz), F(0)) for w in phys] for u in phys]
    ok = ok and V.n == 9 * 6 + 3 * 7 and V.n - rank_P == 27 and rank_P == 48 and len(phys) == 27
    ok = ok and GA.congruence_signature(Gp) == (27, 0, 0)
    ok = ok and n_scalar_real - n_massive == 5
    GA.check("two doublets with neutral aligned vacuum: Goldstone map of rank 3 (9 massless, 3 massive vectors,"
             " unbroken u(1) mixes T3 and Y); one-particle homotopy, 27 physical polarisations of Krein signature"
             " (27, 0, 0), 5 physical scalars", ok)
    return ok


if __name__ == "__main__":
    check_one_particle_quartets_and_homotopies()
    check_second_quantised_homotopy_counts_quartet_quanta()
    check_cohomology_is_the_positive_physical_fock_space()
    check_broken_gauge_algebra_one_particle_count()
