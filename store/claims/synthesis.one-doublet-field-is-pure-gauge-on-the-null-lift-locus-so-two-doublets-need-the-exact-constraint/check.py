"""The rung unit lies in no one-doublet field: exact checks.

The rung summand is built in GA.py as Cl(2,2), as in the stored lift-locus check: generators 0, 1
(square +1) are e+_4, e+_5 and 2, 3 (square -1) are e-_4, e-_5; v_a = (e-_a + e+_a)/2,
w_a = (e+_a - e-_a)/2. A complexified rung vector c = sum_a alpha_a v_a + beta_a w_a is stored as a
pair (x, y) of real coordinate vectors in the basis (v4, v5, w4, w5), c = x + i y. Q (complex
bilinear) and the Hermitian norm N = c* . c come from GA.dot; the slot mixing u(2) acts through the
commutators of the products v_a w_b computed with GA.mul. Everything is exact (Fractions, Gaussian
rationals).
(1) The real-linear u(2)-equivariant maps from one hypercharge-1/2 doublet into R_C form a real
    4-dimensional space, spanned by gamma -> (gamma, 0), (i gamma, 0), (0, conj gamma),
    (0, i conj gamma); so the one-doublet subspaces are {beta = 0} and the graphs
    G_a = {beta = a conj(alpha)}, a complex (a = infinity: {alpha = 0}).
(2) Q(alpha, a conj alpha) = a |alpha|^2: G_a meets L = {Q = -h} only for a = -r < 0; on G_{-r}
    the ratio m/N is the constant (1 - r^2)/(1 + r^2); c_lam lies in G_a exactly for a = -lam^2/h.
(3) At c_lam the tangent space of G_{-r} meets that of L in the gauge-orbit tangent (dimension 3):
    no physical direction; the rung unit dc_lam/dlam and the charged plane are outside it; the
    smallest u(2)-invariant subspace containing c_lam and the rung unit is all of R_C (real rank 8).
(4) Within G_{-r} the Hermitian complement of the gauge orbit at c_lam is the line of c_lam itself,
    a direction that changes Q (dQ = 2Q(c_lam) = -2h).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = GA.sig(2, 2)
EV = [GA.gen(i) for i in range(4)]
HALF = F(1, 2)
V = [GA.scal(HALF, GA.add(EV[2], EV[0])), GA.scal(HALF, GA.add(EV[3], EV[1]))]
W = [GA.scal(HALF, GA.sub(EV[0], EV[2])), GA.scal(HALF, GA.sub(EV[1], EV[3]))]
BASIS = V + W
Z4 = [[F(0)] * 4 for _ in range(4)]
ZV = [F(0)] * 4


def coords(x):
    """Coordinates of a real vector in (v4, v5, w4, w5): e+_a = v_a + w_a, e-_a = v_a - w_a."""
    c = [F(0)] * 4
    for blade, val in x.items():
        assert len(blade) == 1
        i = blade[0]
        if i < 2:
            c[i] += val
            c[2 + i] += val
        else:
            c[i - 2] += val
            c[i] -= val
    return c


def vec(c):
    return GA.add(*[GA.scal(c[i], BASIS[i]) for i in range(4)])


def bil(x, y):
    return GA.dot(vec(x), vec(y), SQ)


def theta(x):
    return [x[2], x[3], x[0], x[1]]


def ad(B):
    cols = [coords(GA.sub(GA.mul(B, x, SQ), GA.mul(x, B, SQ))) for x in BASIS]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


E = {(a, b): ad(GA.mul(V[a], W[b], SQ)) for a in range(2) for b in range(2)}


def lin(A, B, c=1):
    return [[A[i][j] + c * B[i][j] for j in range(4)] for i in range(4)]


def scm(A, c):
    return [[c * A[i][j] for j in range(4)] for i in range(4)]


def mv(A, x):
    return [sum((A[i][j] * x[j] for j in range(4)), F(0)) for i in range(4)]


T1 = (Z4, scm(lin(E[(0, 1)], E[(1, 0)]), HALF))
T2 = (scm(lin(E[(0, 1)], E[(1, 0)], -1), HALF), Z4)
T3 = (Z4, scm(lin(E[(0, 0)], E[(1, 1)], -1), HALF))
TY = (Z4, scm(lin(E[(0, 0)], E[(1, 1)]), HALF))
GENS = [T1, T2, T3, TY]


def app(op, c):
    (R, I), (x, y) = op, c
    Rx, Ry, Ix, Iy = mv(R, x), mv(R, y), mv(I, x), mv(I, y)
    return ([Rx[i] - Iy[i] for i in range(4)], [Ry[i] + Ix[i] for i in range(4)])


def Qb(c, d):
    (x, y), (u, w) = c, d
    return (bil(x, u) - bil(y, w), bil(x, w) + bil(y, u))


def Q(c):
    return Qb(c, c)


def G(c, d):
    (x, y), (u, w) = c, d
    return bil(theta(x), u) + bil(theta(y), w)


def N(c):
    return G(c, c)


def m(c):
    KB = (lin(E[(0, 0)], E[(1, 1)]), Z4)
    return G(c, app(KB, c))


def flat(c):
    return c[0] + c[1]


def unflat(u):
    return (list(u[:4]), list(u[4:]))


def clam(lam, h):
    return ([h / lam, F(0), -lam, F(0)], list(ZV))


def dclam(lam, h):
    return ([-h / (lam * lam), F(0), F(-1), F(0)], list(ZV))


def from_complex(al, be):
    return ([al[0].re, al[1].re, be[0].re, be[1].re], [al[0].im, al[1].im, be[0].im, be[1].im])


def graph(a, al):
    """The point (alpha, a conj(alpha)) of G_a, a and alpha Gaussian rationals."""
    return from_complex(al, [a * al[0].conj(), a * al[1].conj()])


# the doublet: gamma in C^2 as real coordinates (Re g1, Re g2, Im g1, Im g2); generators
# (i/2) sigma_j and (i/2) 1, the same u(2) as on the alpha-coefficients of R_C
def dbl_app(T, g):
    x, y = g[:2], g[2:]
    R = [r[:2] for r in T[0][:2]]
    I = [r[:2] for r in T[1][:2]]
    Rx = [R[i][0] * x[0] + R[i][1] * x[1] for i in range(2)]
    Ry = [R[i][0] * y[0] + R[i][1] * y[1] for i in range(2)]
    Ix = [I[i][0] * x[0] + I[i][1] * x[1] for i in range(2)]
    Iy = [I[i][0] * y[0] + I[i][1] * y[1] for i in range(2)]
    return [Rx[0] - Iy[0], Rx[1] - Iy[1], Ry[0] + Ix[0], Ry[1] + Ix[1]]


def nullspace(rows, n):
    M = [r[:] for r in rows]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    basis = []
    for fc in [c for c in range(n) if c not in piv]:
        x = [F(0)] * n
        x[fc] = F(1)
        for i, pc in enumerate(piv):
            x[pc] = -M[i][fc]
        basis.append(x)
    return basis


UNIT8 = [[F(1) if k == j else F(0) for k in range(8)] for j in range(8)]
UNIT4 = [[F(1) if k == j else F(0) for k in range(4)] for j in range(4)]
LAMS = [F(1, 5), F(1, 3), F(1), F(2), F(7)]
HS = [F(1, 3), F(1, 2), F(3)]


def check_one_doublet_subspaces_are_the_graphs():
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    premise("synthesis.rung-unit-is-frame-boost")
    # the alpha-coefficients carry the doublet: on (v4, v5) the generators act as on gamma
    for T in GENS:
        for e in UNIT4:
            c = ([e[0], e[1], F(0), F(0)], [e[2], e[3], F(0), F(0)])
            out = app(T, c)
            assert out[0][2:] == [0, 0] and out[1][2:] == [0, 0]
            assert [out[0][0], out[0][1], out[1][0], out[1][1]] == dbl_app(T, e)
    # unknown real 8x4 matrix M (column-major unknowns): M(T gamma) = T(M gamma) for all T, gamma
    def Mcol(j):
        return [[F(1) if (k == 8 * j + i) else F(0) for k in range(32)] for i in range(8)]
    rows = []
    for T in GENS:
        for e in UNIT4:
            Te = dbl_app(T, e)
            lhs = [[sum((Te[j] * Mcol(j)[i][k] for j in range(4)), F(0)) for k in range(32)]
                   for i in range(8)]
            Me = [[sum((e[j] * Mcol(j)[i][k] for j in range(4)), F(0)) for k in range(32)]
                  for i in range(8)]
            # T applied to the symbolic vector M e: linear in the unknowns, column by column
            rhs = [[F(0)] * 32 for _ in range(8)]
            for k in range(32):
                vk = unflat([Me[i][k] for i in range(8)])
                tv = flat(app(T, vk))
                for i in range(8):
                    rhs[i][k] = tv[i]
            for i in range(8):
                rows.append([lhs[i][k] - rhs[i][k] for k in range(32)])
    ker = nullspace(rows, 32)
    assert len(ker) == 4
    # the four named maps lie in it and span it
    def as_vec(fn):
        cols = [flat(fn(e)) for e in UNIT4]
        return [cols[j][i] for j in range(4) for i in range(8)]
    def mk(p, q):
        def fn(g):
            al = [GA.qi(g[0], g[2]), GA.qi(g[1], g[3])]
            return from_complex([p * al[0], p * al[1]], [q * al[0].conj(), q * al[1].conj()])
        return fn
    named = [as_vec(mk(GA.qi(1), GA.qi(0))), as_vec(mk(GA.qi(0, 1), GA.qi(0))),
             as_vec(mk(GA.qi(0), GA.qi(1))), as_vec(mk(GA.qi(0), GA.qi(0, 1)))]
    for v in named:
        assert all(sum((r[k] * v[k] for k in range(32)), F(0)) == 0 for r in rows)
    assert GA.rank_of_vectors(named) == 4
    assert GA.rank_of_vectors(named + ker) == 4
    # every nonzero equivariant map is injective (rank 4): sampled combinations p, q
    for p, q in [(GA.qi(1), GA.qi(0)), (GA.qi(0), GA.qi(1)), (GA.qi(2, 1), GA.qi(-1, 3)),
                 (GA.qi(1, -1), GA.qi(5))]:
        fn = mk(p, q)
        assert GA.rank_of_vectors([flat(fn(e)) for e in UNIT4]) == 4
    # an inequivariant map fails: gamma -> (conj gamma, 0)
    def bad(g):
        return ([g[0], g[1], F(0), F(0)], [-g[2], -g[3], F(0), F(0)])
    assert any(sum((r[k] * as_vec(bad)[k] for k in range(32)), F(0)) != 0 for r in rows)
    return True


def check_graphs_meet_the_lift_locus_in_one_frame():
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    samples = [[GA.qi(1, 2), GA.qi(0, 1)], [GA.qi(3), GA.qi(-1, 1)], [GA.qi(2, -3), GA.qi(1)]]
    for a in [GA.qi(-2), GA.qi(F(-1, 3)), GA.qi(1), GA.qi(0, 1), GA.qi(1, 1)]:
        for al in samples:
            c = graph(a, al)
            n2 = (al[0] * al[0].conj() + al[1] * al[1].conj()).re
            assert Q(c) == ((a.re * n2), (a.im * n2))
            # m / N constant on the graph: (1 - |a|^2)/(1 + |a|^2)
            aa = (a * a.conj()).re
            assert N(c) == HALF * (1 + aa) * n2
            assert m(c) * (1 + aa) == (1 - aa) * N(c)
    # the complex doublets {beta = 0}, {alpha = 0} have Q = 0 and miss L (h > 0)
    for al in samples:
        assert Q(from_complex(al, [GA.qi(0), GA.qi(0)])) == (0, 0)
        assert Q(from_complex([GA.qi(0), GA.qi(0)], al)) == (0, 0)
    # c_lam lies in G_a exactly for a = -lam^2/h (alpha = (h/lam) e_4 determines a)
    for h in HS:
        for lam in LAMS:
            c = clam(lam, h)
            a = GA.qi(-lam * lam / h)
            assert graph(a, [GA.qi(h / lam), GA.qi(0)]) == c
            assert graph(GA.qi(-lam * lam / h + 1), [GA.qi(h / lam), GA.qi(0)]) != c
            assert Q(c) == (-h, 0)
    return True


def tangent_of_graph(a):
    """Real basis of the (linear) subspace G_a."""
    out = []
    for g in UNIT4:
        al = [GA.qi(g[0], g[2]), GA.qi(g[1], g[3])]
        out.append(flat(graph(a, al)))
    return out


def check_one_doublet_field_on_the_lift_locus_is_pure_gauge():
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    for h in HS:
        for lam in LAMS:
            c = clam(lam, h)
            r = lam * lam / h
            TG = tangent_of_graph(GA.qi(-r))
            assert GA.rank_of_vectors(TG) == 4
            assert GA.rank_of_vectors(TG + [flat(c)]) == 4          # c_lam in G_{-r}
            # T G cap ker dQ: solve for coefficients s with dQ(sum s_j t_j) = 0 (two real rows)
            rows = [[Qb(c, unflat(t))[part] for t in TG] for part in range(2)]
            ker = nullspace(rows, 4)
            assert len(ker) == 3
            inter = [[sum((s[j] * TG[j][k] for j in range(4)), F(0)) for k in range(8)] for s in ker]
            orb = [flat(app(T, c)) for T in GENS]
            assert GA.rank_of_vectors(orb) == 3
            assert GA.rank_of_vectors(inter + orb) == 3              # = the gauge tangent
            # the rung unit is not in G_{-r}; nor are the charged modes of L
            dc = dclam(lam, h)
            assert GA.rank_of_vectors(TG + [flat(dc)]) == 5
            Lrows = [[Qb(c, unflat(e))[part] for e in UNIT8] for part in range(2)]
            Lrows += [[G(unflat(o), unflat(e)) for e in UNIT8] for o in orb]
            Lrows += [[G(dc, unflat(e)) for e in UNIT8]]
            charged = nullspace(Lrows, 8)
            assert len(charged) == 2
            for v in charged:
                assert GA.rank_of_vectors(TG + [v]) == 5
            # the u(2)-span of {c_lam, rung unit} is all of R_C
            span = [flat(c), flat(dc)]
            for _ in range(3):
                span = span + [flat(app(T, unflat(s))) for T in GENS for s in span]
                basis = []
                for s in span:
                    if GA.rank_of_vectors(basis + [s]) > len(basis):
                        basis.append(s)
                span = basis
            assert len(span) == 8
            # the u(2)-span of c_lam alone is G_{-r} (rank 4)
            sp = [flat(c)]
            for _ in range(3):
                sp = sp + [flat(app(T, unflat(s))) for T in GENS for s in sp]
                b2 = []
                for s in sp:
                    if GA.rank_of_vectors(b2 + [s]) > len(b2):
                        b2.append(s)
                sp = b2
            assert len(sp) == 4 and GA.rank_of_vectors(sp + TG) == 4
    return True


def check_radial_mode_of_a_one_doublet_field_changes_q():
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    for h in HS:
        for lam in LAMS:
            c = clam(lam, h)
            r = lam * lam / h
            TG = tangent_of_graph(GA.qi(-r))
            orb = [flat(app(T, c)) for T in GENS]
            rows = [[G(unflat(o), unflat(t)) for t in TG] for o in orb]
            ker = nullspace(rows, 4)
            assert len(ker) == 1
            rad = [sum((ker[0][j] * TG[j][k] for j in range(4)), F(0)) for k in range(8)]
            assert GA.rank_of_vectors([rad, flat(c)]) == 1              # the line of c_lam
            assert Qb(c, c) == (-h, 0)
            assert tuple(2 * x for x in Qb(c, c)) == (-2 * h, 0)          # dQ along c_lam
            # by contrast the rung unit keeps Q and moves m; it differs from the radial
            # direction c_lam/lam only by (2h/lam^2) e_4 in the alpha coefficient
            dc = dclam(lam, h)
            diff = [c[0][i] / lam - dc[0][i] for i in range(4)]
            assert diff == [2 * h / (lam * lam), 0, 0, 0] and c[1] == list(ZV) and dc[1] == list(ZV)
            assert Qb(c, dc) == (0, 0)
            assert G(dc, (theta_free_K(c))) != 0
    return True


def theta_free_K(c):
    """K c, K = -2i Y (the hypercharge boost): +1 on v, -1 on w."""
    x, y = c
    return ([x[0], x[1], -x[2], -x[3]], [y[0], y[1], -y[2], -y[3]])
