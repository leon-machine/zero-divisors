"""synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape: exact checks.

Units (cells, modes) labelled 0..N-1; a relabelling group G acts on the labels; a G-invariant state has a
covariance matrix C with C[g i][g j] = C[i][j].
(1) Orbitals.  The orbits of G on ordered pairs, symmetrised, are computed by closure for: the symmetric group on
    4 labels; the affine group x -> a x + b of the field of 5 elements (order 20); the similarity-type group
    x -> a x + b of the field of 7 elements (order 42); the cyclic group of 6 (3 off-diagonal orbitals); the
    dihedral group of 6 (3); the square-multipliers x -> a^2 x + b of 7 elements (order 21, transitive, not doubly
    transitive, 1 symmetrised off-diagonal orbital but 2 ordered ones).  A doubly transitive group has exactly one
    off-diagonal orbital, so C = (v - c) 1 + c U (U the all-ones matrix).  For such C: C f = (v - c) f on every
    sum-zero f, C 1 = (v + (N - 1) c) 1, and Var(sum f_i O_i) = (v - c) sum f_i^2 + c (sum f_i)^2 for arbitrary
    rational profiles f.  Positivity ends c = v and c = -v/(N - 1).
(2) No shape.  On a ring of 6 cells the cosine modes m = 1, 2, 3 have the same variance per unit norm under
    C = (v - c) 1 + c U, for several (v, c); under the dihedral-invariant C = 1 + (1/4) A (A the nearest-neighbour
    matrix), which is positive, they have 5/4, 3/4, 1/2: an invariant state of a group that is not doubly
    transitive carries a shape.  Walsh modes on 8 cells likewise.  A white spectrum has Delta^2 proportional to
    k^3: doubling k multiplies it by 8 (the index 3 of the stored finite-range class).
(3) CAR.  N = 4 modes as null vectors v_j = (e_j + f_j)/2, w_j = (e_j - f_j)/2 of Cl(4,4), n_j = v_j w_j, states
    as vectors of the left regular representation with <x, y> = <x* y>_0.  The state psi = (sum_j v_j) prod_j (1 -
    n_j) (one quantum in the symmetric mode) is carried to itself by the transposition of two planes; its
    one-particle matrix is E_ij = 1/4 for all i, j (n = 1/4, e = 1/4 = (1 - n)/(N - 1), the upper end); its
    pairing vanishes; Cov(n_i, n_j) = -1/16, Var(n_i) = 3/16, so v + (N - 1) c = 0 and v - c = 1/4; the stored
    quasi-free variance Tr(f E f (1 - E)) gives (n(1 - n) + e^2) sum f^2 - e^2 (sum f)^2, the same numbers, and
    for a general real symmetric one-body f, a(1 - a) Tr f^2 + e(1 - 2a) <1, f^2 1> - e^2 <1, f 1>^2 with a = n - e.
    The stored ladder states omega_k on N = 2, 3 blocks: v = (k/N)(1 - k/N), c = k(k - 1)/(N(N - 1)) - k^2/N^2,
    v + (N - 1) c = 0, v - c = k(N - k)/(N(N - 1)).  An antisymmetric matrix invariant under one transposition
    of its two labels has that entry zero.
(4) Similarities.  In Cl(3,0) a reflection is x -> -u x u^(-1); translation, reflection and dilatation carry the
    pair (x, y) to a prescribed pair (x', y') (double transitivity, on a rational sample with |y' - x'|/|y - x| =
    7/3), so an invariant kernel takes one value off the diagonal; the kernels Q(x - y)^(-D) (D = 0, 1, -1, 2)
    scale by lambda^(-2D) under the same map: one exponent, no shape beyond it.
"""
from fractions import Fraction as F
import itertools

import GA
from tp_premise import premise


# ---------------------------------------------------------------- permutation groups and orbitals
def _closure(gens, n):
    ident = tuple(range(n))
    seen = {ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                gh = tuple(h[g[i]] for i in range(n))
                if gh not in seen:
                    seen.add(gh)
                    nxt.append(gh)
        frontier = nxt
    return seen


def _orbitals(group, n, symmetrise=True):
    """Orbits on pairs (i, j), i != j; with symmetrise, (i, j) and (j, i) are joined."""
    left = {(i, j) for i in range(n) for j in range(n) if i != j}
    orbs = []
    while left:
        p = next(iter(left))
        orb = set()
        for g in group:
            q = (g[p[0]], g[p[1]])
            orb.add(q)
            if symmetrise:
                orb.add((q[1], q[0]))
        orbs.append(orb)
        left -= orb
    return orbs


def _affine(p, mults):
    return [tuple((a * x + b) % p for x in range(p)) for a in mults for b in range(p)]


def _mat(v, c, n):
    return [[(v if i == j else c) for j in range(n)] for i in range(n)]


def _quad(C, f, g=None):
    g = f if g is None else g
    return sum((f[i] * C[i][j] * g[j] for i in range(len(f)) for j in range(len(g))), F(0))


def _apply(C, f):
    return [sum((C[i][j] * f[j] for j in range(len(f))), F(0)) for i in range(len(f))]


def check_doubly_transitive_relabelling_leaves_two_numbers():
    sym4 = _closure([(1, 0, 2, 3), (1, 2, 3, 0)], 4)
    aff5 = _closure(_affine(5, [1, 2, 3, 4]), 5)
    aff7 = _closure(_affine(7, [1, 2, 3, 4, 5, 6]), 7)
    cyc6 = _closure([(1, 2, 3, 4, 5, 0)], 6)
    dih6 = _closure([(1, 2, 3, 4, 5, 0), (0, 5, 4, 3, 2, 1)], 6)
    sq7 = _closure(_affine(7, [1, 2, 4]), 7)
    ok = (len(sym4), len(aff5), len(aff7), len(cyc6), len(dih6), len(sq7)) == (24, 20, 42, 6, 12, 21)
    counts = [len(_orbitals(g, n)) for g, n in ((sym4, 4), (aff5, 5), (aff7, 7), (cyc6, 6), (dih6, 6), (sq7, 7))]
    ok = ok and counts == [1, 1, 1, 3, 3, 1]
    ok = ok and len(_orbitals(sq7, 7, symmetrise=False)) == 2 and len(_orbitals(aff7, 7, symmetrise=False)) == 1
    # every invariant symmetric matrix of a doubly transitive group is (v - c) 1 + c U: check invariance and spectrum
    for n, group in ((4, sym4), (5, aff5), (7, aff7)):
        for v, c in ((F(3), F(1)), (F(2), F(-1, 3)), (F(5, 7), F(2, 9))):
            C = _mat(v, c, n)
            ok = ok and all(C[g[i]][g[j]] == C[i][j] for g in group for i in range(n) for j in range(n))
            ones = [F(1)] * n
            ok = ok and _apply(C, ones) == [v + (n - 1) * c] * n
            for f in ([F(1), F(-1)] + [F(0)] * (n - 2), [F(2), F(-3), F(1)] + [F(0)] * (n - 3),
                      [F(k) - F(n - 1, 2) for k in range(n)]):
                ok = ok and sum(f) == 0 and _apply(C, f) == [(v - c) * x for x in f]
            for f in ([F(k * k + 1, 3) for k in range(n)], [F((-2) ** k, 5) for k in range(n)]):
                ok = ok and _quad(C, f) == (v - c) * sum(x * x for x in f) + c * sum(f) ** 2
    # positivity ends: c = v kills the sum-zero modes, c = -v/(N - 1) kills the constant
    for n in (4, 5, 7):
        v = F(3)
        ok = ok and _apply(_mat(v, v, n), [F(1), F(-1)] + [F(0)] * (n - 2)) == [F(0)] * n
        ok = ok and _apply(_mat(v, -v / n, n), [F(1)] * n) == [F(0)] * n
        ok = ok and _quad(_mat(v, -v / (n - 1) - F(1, 100), n), [F(1)] * n) < 0
    assert ok


def check_embedding_supplies_the_only_shape():
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    ok = True
    n = 6
    cosm = {1: [F(1), F(1, 2), F(-1, 2), F(-1), F(-1, 2), F(1, 2)],
            2: [F(1), F(-1, 2), F(-1, 2), F(1), F(-1, 2), F(-1, 2)],
            3: [F(1), F(-1), F(1), F(-1), F(1), F(-1)]}
    # the three vectors are the cosines cos(2 pi m j/6): checked through the recurrence c_(j+1) + c_(j-1) = 2 c_1 c_j
    for m, cm in cosm.items():
        ok = ok and sum(cm) == 0 and all(cm[(j + 1) % n] + cm[(j - 1) % n] == 2 * cm[1] * cm[j] for j in range(n))
    for v, c in ((F(3), F(1)), (F(2), F(-2, 5)), (F(1), F(0))):
        C = _mat(v, c, n)
        per_norm = [_quad(C, cm) / sum(x * x for x in cm) for cm in cosm.values()]
        ok = ok and per_norm == [v - c] * 3
    A = [[(F(1) if (i - j) % n in (1, n - 1) else F(0)) for j in range(n)] for i in range(n)]
    Cd = [[(F(1) if i == j else F(0)) + F(1, 4) * A[i][j] for j in range(n)] for i in range(n)]
    dih6 = _closure([(1, 2, 3, 4, 5, 0), (0, 5, 4, 3, 2, 1)], 6)
    ok = ok and all(Cd[g[i]][g[j]] == Cd[i][j] for g in dih6 for i in range(n) for j in range(n))
    per_norm = [_quad(Cd, cm) / sum(x * x for x in cm) for cm in cosm.values()]
    ok = ok and per_norm == [F(5, 4), F(3, 4), F(1, 2)]
    # positive: strictly diagonally dominant (1 > 2/4)
    ok = ok and all(Cd[i][i] > sum(abs(Cd[i][j]) for j in range(n) if j != i) for i in range(n))
    # Walsh modes on 8 cells
    walsh = [[F((-1) ** bin(i & m).count("1")) for i in range(8)] for m in range(1, 8)]
    C8 = _mat(F(7, 3), F(-1, 5), 8)
    ok = ok and all(sum(w) == 0 and _quad(C8, w) == (F(7, 3) + F(1, 5)) * 8 for w in walsh)
    ok = ok and all(_quad(C8, walsh[a], walsh[b]) == 0 for a in range(7) for b in range(a))
    # white spectrum: Delta^2 = k^3 P/(2 pi^2) with P constant has index 3
    for k in (F(1), F(3, 7), F(50)):
        ok = ok and (2 * k) ** 3 == 8 * k ** 3
    assert ok


# ---------------------------------------------------------------- CAR side, in Cl(N, N)
def _dag(x, sq):
    out = {}
    for b, c in x.items():
        g = len(b)
        s = (-1) ** (g * (g - 1) // 2) * (-1) ** sum(1 for i in b if sq[i] == -1)
        out[b] = c * s
    return {b: c for b, c in out.items() if c != 0}


def _prod(xs, sq):
    r = GA.sc(1)
    for x in xs:
        r = GA.mul(r, x, sq)
    return r


def _ip(x, y):
    return sum((c * y.get(b, 0) for b, c in x.items()), F(0))


def _modes(nm):
    sq = tuple([1, -1] * nm)
    v = [GA.scal(F(1, 2), GA.add(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(nm)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(nm)]
    n = [GA.mul(v[j], w[j], sq) for j in range(nm)]
    return sq, v, w, n


def _relabel(x, perm, sq):
    """The algebra automorphism that sends plane j to plane perm[j]."""
    out = {}
    for b, c in x.items():
        img = _prod([GA.gen(2 * perm[i // 2] + i % 2) for i in b], sq)
        out = GA.add(out, GA.scal(c, img))
    return out


def check_exchangeable_fermion_states():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    premise("synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations")
    ok = True
    nm = 4
    sq, v, w, n = _modes(nm)
    for i in range(nm):
        for j in range(nm):
            anti = GA.add(GA.mul(v[i], w[j], sq), GA.mul(w[j], v[i], sq))
            ok = ok and anti == (GA.sc(1) if i == j else {})
            ok = ok and GA.anticommutes(v[i], v[j], sq) and GA.anticommutes(w[i], w[j], sq)
    vac = _prod([GA.sub(GA.sc(1), n[j]) for j in range(nm)], sq)
    psi = GA.mul(GA.add(*v), vac, sq)
    nrm = _ip(psi, psi)
    ok = ok and nrm != 0
    # exchangeable: the transposition of planes 0 and 1, and the 4-cycle, fix psi
    ok = ok and _relabel(psi, (1, 0, 2, 3), sq) == psi and _relabel(psi, (1, 2, 3, 0), sq) == psi

    def ev(X):
        return _ip(psi, GA.mul(X, psi, sq)) / nrm

    E = [[ev(GA.mul(v[j], w[i], sq)) for j in range(nm)] for i in range(nm)]
    ok = ok and all(E[i][j] == F(1, 4) for i in range(nm) for j in range(nm))
    nn, e = F(1, 4), F(1, 4)
    ok = ok and e == (1 - nn) / (nm - 1) and -nn / (nm - 1) <= e
    ok = ok and all(ev(GA.mul(w[i], w[j], sq)) == 0 and ev(GA.mul(v[i], v[j], sq)) == 0
                    for i in range(nm) for j in range(nm))
    var = ev(GA.mul(n[0], n[0], sq)) - ev(n[0]) ** 2
    cov = ev(GA.mul(n[0], n[1], sq)) - ev(n[0]) * ev(n[1])
    ok = ok and (var, cov) == (F(3, 16), F(-1, 16)) and var + (nm - 1) * cov == 0 and var - cov == F(1, 4)
    ok = ok and all(ev(GA.mul(n[i], n[j], sq)) - ev(n[i]) * ev(n[j]) == cov
                    for i in range(nm) for j in range(nm) if i != j)
    # the stored quasi-free variance Tr(f E f (1 - E)) for diagonal f: (n(1-n) + e^2) sum f^2 - e^2 (sum f)^2
    for f in ([F(1), F(-1), F(0), F(0)], [F(2), F(1, 3), F(-5), F(7, 2)], [F(1)] * 4):
        tr = sum((f[i] * E[i][j] * f[j] * ((F(1) if i == j else F(0)) - E[j][i])
                  for i in range(nm) for j in range(nm)), F(0))
        direct = ev(_prod([GA.add(*[GA.scal(f[i], n[i]) for i in range(nm)])] * 2, sq)) \
            - ev(GA.add(*[GA.scal(f[i], n[i]) for i in range(nm)])) ** 2
        formula = (nn * (1 - nn) + e * e) * sum(x * x for x in f) - e * e * sum(f) ** 2
        ok = ok and tr == direct == formula
    # general one-body f (real symmetric): Var = a(1-a) Tr f^2 + e(1-2a) <1, f^2 1> - e^2 <1, f 1>^2, a = n - e
    for fm in ([[F(1), F(2), F(0), F(-1)], [F(2), F(0), F(1, 2), F(3)], [F(0), F(1, 2), F(-2), F(1)],
                [F(-1), F(3), F(1), F(5)]],
               [[F(0), F(1), F(1), F(1)], [F(1), F(0), F(1), F(1)], [F(1), F(1), F(0), F(1)],
                [F(1), F(1), F(1), F(0)]]):
        Nf = GA.add(*[GA.scal(fm[i][j], GA.mul(v[i], w[j], sq)) for i in range(nm) for j in range(nm)])
        direct = ev(GA.mul(Nf, Nf, sq)) - ev(Nf) ** 2
        f2 = [[sum(fm[i][k] * fm[k][j] for k in range(nm)) for j in range(nm)] for i in range(nm)]
        a = nn - e
        formula = a * (1 - a) * sum(f2[i][i] for i in range(nm)) \
            + e * (1 - 2 * a) * sum(f2[i][j] for i in range(nm) for j in range(nm)) \
            - e * e * sum(fm[i][j] for i in range(nm) for j in range(nm)) ** 2
        ok = ok and direct == formula
    # an antisymmetric matrix invariant under the transposition of its two labels vanishes there
    for p in (F(3, 7), F(-2), F(0)):
        P01, P10 = p, -p            # antisymmetry
        invariant = (P10 == P01)    # invariance under (0 1)
        ok = ok and (invariant == (p == 0))
    # the stored ladder states: permutation symmetric, covariance of the upper occupations
    for Nb in (2, 3):
        sqb, vb, wb, nb = _modes(2 * Nb)
        b = [GA.mul(vb[2 * i], wb[2 * i + 1], sqb) for i in range(Nb)]
        Ks = _dag(GA.add(*b), sqb)
        P = _prod([GA.mul(nb[2 * i], GA.sub(GA.sc(1), nb[2 * i + 1]), sqb) for i in range(Nb)], sqb)
        psik = P
        for k in range(1, Nb + 1):
            psik = GA.mul(Ks, psik, sqb)
            nk = _ip(psik, psik)

            def evk(X):
                return _ip(psik, GA.mul(X, psik, sqb)) / nk

            vv = evk(GA.mul(nb[1], nb[1], sqb)) - evk(nb[1]) ** 2
            cc = evk(GA.mul(nb[1], nb[3], sqb)) - evk(nb[1]) * evk(nb[3])
            ok = ok and vv == F(k, Nb) * (1 - F(k, Nb))
            ok = ok and cc == F(k * (k - 1), Nb * (Nb - 1)) - F(k, Nb) ** 2
            ok = ok and vv + (Nb - 1) * cc == 0 and vv - cc == F(k * (Nb - k), Nb * (Nb - 1))
    assert ok


# ---------------------------------------------------------------- similarities of a Euclidean slice, in Cl(3,0)
def _vec(a):
    return GA.add(*[GA.scal(F(a[i]), GA.gen(i)) for i in range(3)]) if any(a) else {}


def _coords(x):
    return [x.get((i,), F(0)) for i in range(3)]


def _q(x, sq):
    return GA.mul(x, x, sq).get((), F(0))


def _reflect(u, x, sq):
    """x -> -u x u^(-1), the reflection in the plane orthogonal to u."""
    return GA.scal(F(-1) / _q(u, sq), GA.mul(GA.mul(u, x, sq), u, sq))


def check_similarities_are_doubly_transitive_and_leave_one_exponent():
    premise("synthesis.frozen-phase-spectrum-not-red")
    sq = GA.sig(3, 0)
    ok = True
    samples = [((1, 0, 2), (2, 2, 4), (5, -1, 0), (7, 2, 6)),      # d = (1,2,2), d' = (2,3,6): 3 -> 7
               ((0, 0, 0), (2, 3, 6), (1, 1, 1), (2, 3, 3)),       # 7 -> 3
               ((4, 4, 7), (5, 8, 15), (0, 0, 0), (6, 6, 7))]      # d = (1,4,8) norm 9, d' = (6,6,7) norm 11
    for xs, ys, xt, yt in samples:
        x, y, x2, y2 = _vec(xs), _vec(ys), _vec(xt), _vec(yt)
        d, d2 = GA.sub(y, x), GA.sub(y2, x2)
        lam2 = _q(d2, sq) / _q(d, sq)
        lam = None
        for num in range(1, 40):
            for den in range(1, 40):
                if F(num, den) ** 2 == lam2:
                    lam = F(num, den)
        ok = ok and lam is not None
        u = GA.sub(GA.scal(lam, d), d2)

        def g(p):
            z = GA.scal(lam, GA.sub(p, x))
            z = _reflect(u, z, sq) if u else z
            return GA.add(z, x2)

        ok = ok and g(x) == x2 and g(y) == y2
        # the map is a similarity of ratio lam: squared distances scale by lam^2 on further rational points
        pts = [_vec(p) for p in ((3, -2, 5), (0, 7, 1), (-4, 4, 9), (1, 1, 1))]
        for a in pts:
            for b in pts:
                ok = ok and _q(GA.sub(g(a), g(b)), sq) == lam2 * _q(GA.sub(a, b), sq)
                if a != b:
                    r2 = _q(GA.sub(a, b), sq)
                    for D in (0, 1, -1, 2):
                        ok = ok and _q(GA.sub(g(a), g(b)), sq) ** (-D) == lam2 ** (-D) * r2 ** (-D)
        # a reflection preserves the square
        ok = ok and all(_q(_reflect(_vec((1, 2, 2)), a, sq), sq) == _q(a, sq) for a in pts)
    assert ok
