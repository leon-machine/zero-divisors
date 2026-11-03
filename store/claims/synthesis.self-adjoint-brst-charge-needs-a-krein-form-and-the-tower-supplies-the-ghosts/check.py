"""synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts: exact checks.

(1) Positivity: on tower floors (one and two planes) T03's * gives <b* b>_0 = 1 for every basis blade and
    <b* c>_0 = 0 for distinct blades, so the trace form is positive definite; the palatial polynomial form
    <z^n, z^m> = n! delta is positive. The BRST charge Q of (2) satisfies Q^2 = 0, Q != 0 and is not
    self-adjoint for the positive form, as the lemma requires.
(2) Krein BRST at a null momentum k: polarisation modes a_mu = d/dz_mu, positive adjoint z_mu, Krein operator
    eta = (-1)^{n_0} x (swap of the ghost pair b, d, built as S = 1 - (b* - d*)(b - d) on two tower planes), so
    a_mu^dagger = -g_mumu z_mu and b^dagger = d*. L = k.a, Q = L^dagger b + d* L. On the space of total number
    T = deg + N_b + N_d <= 3: Q^2 = 0, Q is Krein-self-adjoint, the Krein form is symmetric; the one-particle Krein
    form -u.w is invariant under a boost rotor while the Euclidean form is not.
(3) Ghost-number-zero cohomology at T = 0, 1, 2, 3 has dimensions 1, 2, 3, 4 (the symmetric powers of a
    two-dimensional space); the Krein form on ker Q has signature (h, 0, rank of Q into ghost number zero): positive
    definite on the cohomology, with radical im Q.
(4) epsilon -> k epsilon maps k-perp into {f bivector : k f = 0} with image of rank 2 = dim{f : k f = 0}, kernel
    containing k (k k = 0): the cohomology's one-particle space is the stored photon mode space.
(5) The derived algebra su(2) + su(3) + u(1) on C^2 x C^3 (12 anti-Hermitian generators, Gaussian-rational
    entries) with ghosts c^a, antighosts cb_a on twelve tower planes: Q = c^a T_a - 1/2 f_ab^c c^a c^b cb_c has
    Q^2 = 0; without the cubic ghost term Q^2 != 0; with one structure constant perturbed Q^2 != 0.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

QI = GA.QI
G = (1, -1, -1, -1)
KS = [(1, 0, 0, 1), (5, 3, 4, 0)]
TMAX = 3


def _scl(c, x):
    out = {}
    for b, v in x.items():
        w = c * v
        if w != 0:
            out[b] = w
    return out


def _plane(q):
    e_, f_ = 2 * q, 2 * q + 1
    return (GA.add(_scl(F(1, 2), GA.gen(e_)), _scl(F(1, 2), GA.gen(f_))),
            GA.add(_scl(F(1, 2), GA.gen(e_)), _scl(F(-1, 2), GA.gen(f_))))


def _star(x, s):
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sign = -sign
        out[b] = sign * c
    return {b: c for b, c in out.items() if c != 0}


# ---------------------------------------------------------------- ghost pair on two tower planes
GS = (1, -1, 1, -1)
_gm = lambda x, y: GA.mul(x, y, GS)
(_bd, _b), (_dd, _d) = _plane(0), _plane(1)
_vac = _gm(_gm(_b, _bd), _gm(_d, _dd))
_GB = [_vac, _gm(_bd, _vac), _gm(_dd, _vac), _gm(_bd, _gm(_dd, _vac))]
_NB = [(0, 0), (1, 0), (0, 1), (1, 1)]


def _gmat(op):
    M = [[F(0)] * 4 for _ in range(4)]
    for j, g in enumerate(_GB):
        x = _gm(op, g)
        if GA.is_zero(x):
            continue
        hit = False
        for i, h in enumerate(_GB):
            for s in (1, -1):
                if GA.eq(x, _scl(F(s), h)):
                    M[i][j] = F(s)
                    hit = True
        if not hit:
            raise ValueError("ghost operator leaves the Fock basis")
    return M


_SWAP = GA.sub(GA.sc(1), _gm(GA.sub(_bd, _dd), GA.sub(_b, _d)))


def _fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def _space(tmax):
    basis = []
    for e in product(range(tmax + 1), repeat=4):
        if sum(e) > tmax:
            continue
        for gi in range(4):
            if sum(e) + sum(_NB[gi]) <= tmax:
                basis.append((e, gi))
    return basis, {s: i for i, s in enumerate(basis)}


def _zeros(D):
    return [[F(0)] * D for _ in range(D)]


def _boson(basis, idx, kind, mu):
    M = _zeros(len(basis))
    for j, (e, gi) in enumerate(basis):
        e2 = list(e)
        if kind == "c":
            e2[mu] += 1
            c = F(1)
        else:
            if e[mu] == 0:
                continue
            c = F(e[mu])
            e2[mu] -= 1
        t = (tuple(e2), gi)
        if t in idx:
            M[idx[t]][j] += c
    return M


def _ghost(basis, idx, Mg):
    M = _zeros(len(basis))
    for j, (e, gi) in enumerate(basis):
        for i in range(4):
            if Mg[i][gi] != 0 and (e, i) in idx:
                M[idx[(e, i)]][j] += Mg[i][gi]
    return M


def _madd(*As):
    D = len(As[0])
    return [[sum((A[i][j] for A in As), F(0)) for j in range(D)] for i in range(D)]


def _msc(c, A):
    return [[c * x for x in r] for r in A]


def _tr(A):
    return [list(r) for r in zip(*A)]


def _brst(k, tmax):
    basis, idx = _space(tmax)
    D = len(basis)
    L = _madd(*[_msc(F(G[m] * k[m]), _boson(basis, idx, "a", m)) for m in range(4)])
    Ld = _madd(*[_msc(F(-k[m]), _boson(basis, idx, "c", m)) for m in range(4)])
    Q = _madd(GA.mat_mul(Ld, _ghost(basis, idx, _gmat(_b))), GA.mat_mul(_ghost(basis, idx, _gmat(_dd)), L))
    P = _zeros(D)
    Eb = _zeros(D)
    for i, (e, gi) in enumerate(basis):
        P[i][i] = F(_fact(e[0]) * _fact(e[1]) * _fact(e[2]) * _fact(e[3]))
        Eb[i][i] = F((-1) ** e[0])
    K = GA.mat_mul(P, GA.mat_mul(Eb, _ghost(basis, idx, _gmat(_SWAP))))
    return basis, Q, P, K


def _nullspace(M, n):
    rows = [list(r) for r in M]
    piv = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
    out = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -rows[i][fc]
        out.append(v)
    return out


def check_positive_forms_carry_no_self_adjoint_nilpotent():
    premise("field-theory.imported-tower-limit")
    premise("field-theory.imported-statistics-no-go-palatial-algebra")
    ok = True
    for nplanes in (1, 2):
        s = tuple([1, -1] * nplanes)
        blades = GA.all_blades(2 * nplanes)
        ok = ok and len(blades) == 4 ** nplanes
        for b1 in blades:
            for b2 in blades:
                v = GA.mul(_star({b1: F(1)}, s), {b2: F(1)}, s).get((), F(0))
                ok = ok and v == (F(1) if b1 == b2 else F(0))
    basis, Q, P, K = _brst(KS[0], 2)
    ok = ok and all(P[i][i] > 0 for i in range(len(basis)))
    ok = ok and all(x == 0 for r in GA.mat_mul(Q, Q) for x in r) and any(x != 0 for r in Q for x in r)
    ok = ok and not GA.mat_eq(GA.mat_mul(P, Q), GA.mat_mul(_tr(Q), P))
    GA.check("tower trace form and palatial form positive definite; the nilpotent BRST charge is not"
             " self-adjoint for them", ok)
    return ok


def check_krein_brst_nilpotent_and_self_adjoint():
    premise("field-theory.imported-tower-limit")
    premise("field-theory.imported-statistics-no-go-palatial-algebra")
    premise("field-theory.fock-space-maxwell-modes")
    ok = GA.eq(_gm(_SWAP, _SWAP), GA.sc(1)) and GA.eq(_gm(_gm(_SWAP, _b), _SWAP), _d)
    for k in KS:
        ok = ok and k[0] * k[0] - k[1] * k[1] - k[2] * k[2] - k[3] * k[3] == 0
        basis, Q, P, K = _brst(k, TMAX)
        ok = ok and all(x == 0 for r in GA.mat_mul(Q, Q) for x in r)
        ok = ok and GA.mat_eq(GA.mat_mul(K, Q), GA.mat_mul(_tr(Q), K)) and GA.mat_eq(K, _tr(K))
    # Lorentz invariance of the one-particle Krein form -u.w under a boost rotor (5/4 + 3/4 g0 g1)
    R = GA.add(GA.sc(F(5, 4)), _scl(F(3, 4), GA.mul(GA.gen(0), GA.gen(1), G)))
    Rr = GA.reverse(R)
    ok = ok and GA.eq(GA.mul(R, Rr, G), GA.sc(1))
    vs = [GA.gen(0), GA.add(GA.gen(1), GA.gen(2))]
    bv = [GA.mul(GA.mul(R, v, G), Rr, G) for v in vs]
    kre = lambda u, w: -GA.mul(u, w, G).get((), F(0))
    euc = lambda u, w: sum((u.get((i,), F(0)) * w.get((i,), F(0)) for i in range(4)), F(0))
    ok = ok and kre(bv[0], bv[0]) == kre(vs[0], vs[0]) and kre(bv[0], bv[1]) == kre(vs[0], vs[1])
    ok = ok and euc(bv[0], bv[0]) != euc(vs[0], vs[0])
    GA.check("Krein BRST at null k: Q^2 = 0, Q Krein-self-adjoint (T <= 3); the Krein form is boost-invariant,"
             " the Euclidean form is not", ok)
    return ok


def check_cohomology_is_transverse_and_positive():
    premise("field-theory.imported-tower-limit")
    premise("field-theory.imported-statistics-no-go-palatial-algebra")
    ok = True
    for k in KS:
        basis, Q, P, K = _brst(k, TMAX)
        dims = []
        for T in range(TMAX + 1):
            sec = {gh: [i for i, (e, gi) in enumerate(basis)
                        if sum(e) + sum(_NB[gi]) == T and _NB[gi][1] - _NB[gi][0] == gh] for gh in (-1, 0, 1)}
            C0 = sec[0]
            Qm = [[Q[i][j] for j in sec[-1]] for i in C0]
            Q0 = [[Q[i][j] for j in C0] for i in sec[1]]
            rm = GA.mat_rank(Qm) if sec[-1] else 0
            r0 = GA.mat_rank(Q0) if sec[1] else 0
            h = len(C0) - r0 - rm
            dims.append(h)
            ker = _nullspace(Q0, len(C0)) if sec[1] else [[F(int(i == j)) for j in range(len(C0))]
                                                         for i in range(len(C0))]
            Kc = [[K[C0[i]][C0[j]] for j in range(len(C0))] for i in range(len(C0))]
            Gk = [[sum(u[i] * Kc[i][j] * v[j] for i in range(len(C0)) for j in range(len(C0))) for v in ker]
                  for u in ker]
            ok = ok and GA.congruence_signature(Gk) == (h, 0, rm)
        ok = ok and dims == [1, 2, 3, 4]
    GA.check("ghost-number-zero cohomology has dimensions 1, 2, 3, 4 at T = 0..3, Krein form positive on it", ok)
    return ok


def check_cohomology_matches_the_photon_modes():
    premise("field-theory.fock-space-maxwell-modes")
    ok = True
    biv = [b for b in GA.all_blades(4) if len(b) == 2]
    for k in KS + [(3, 1, 2, 2)]:
        kv = GA.add(*[_scl(F(k[m]), GA.gen(m)) for m in range(4)])
        ok = ok and GA.is_zero(GA.mul(kv, kv, G))
        perp = _nullspace([[F(G[m] * k[m]) for m in range(4)]], 4)
        ok = ok and len(perp) == 3
        imgs = [GA.mul(kv, GA.add(*[_scl(p[m], GA.gen(m)) for m in range(4)]), G) for p in perp]
        ok = ok and all(GA.is_zero(GA.mul(kv, f, G)) and set(f) <= set(biv) for f in imgs)
        ok = ok and GA.mat_rank([[f.get(b, F(0)) for b in biv] for f in imgs]) == 2
        cols = [GA.mul(kv, {b: F(1)}, G) for b in biv]
        rows = sorted({x for c in cols for x in c})
        ok = ok and 6 - GA.mat_rank([[c.get(x, F(0)) for c in cols] for x in rows]) == 2
    GA.check("epsilon -> k epsilon maps k-perp onto {f : k f = 0} (dimension 2), kernel span{k}", ok)
    return ok


# ---------------------------------------------------------------- the derived algebra and its ghost charge
_Z, _ONE, _I = QI(0), QI(1), QI(0, 1)


def _qz(n):
    return [[_Z] * n for _ in range(n)]


def _E(n, j, k):
    M = _qz(n)
    M[j][k] = _ONE
    return M


def _qadd(*As):
    n = len(As[0])
    return [[sum((A[i][j] for A in As), _Z) for j in range(n)] for i in range(n)]


def _qsc(c, A):
    return [[c * x for x in r] for r in A]


def _qmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), _Z) for j in range(n)] for i in range(n)]


def _kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def _qid(n):
    return [[_ONE if i == j else _Z for j in range(n)] for i in range(n)]


def _su(n):
    g = []
    for j in range(n - 1):
        g.append(_qsc(_I, _qadd(_E(n, j, j), _qsc(QI(-1), _E(n, j + 1, j + 1)))))
    for j in range(n):
        for k in range(j + 1, n):
            g.append(_qadd(_E(n, j, k), _qsc(QI(-1), _E(n, k, j))))
            g.append(_qsc(_I, _qadd(_E(n, j, k), _E(n, k, j))))
    return g


def _flat(A):
    out = []
    for r in A:
        for x in r:
            out += [x.re, x.im]
    return out


def _structure(gens):
    ng = len(gens)
    cols = [_flat(g) for g in gens]
    fs = {}
    for a in range(ng):
        for b in range(ng):
            Cm = _qadd(_qmul(gens[a], gens[b]), _qsc(QI(-1), _qmul(gens[b], gens[a])))
            rhs = _flat(Cm)
            M = [[cols[c][i] for c in range(ng)] + [rhs[i]] for i in range(len(rhs))]
            sol = _nullspace([row[:ng] + [row[ng]] for row in M], ng + 1)
            # the commutator lies in the span: pick the null vector with last entry -1
            pick = [v for v in sol if v[ng] != 0]
            if len(pick) != 1:
                return None
            v = pick[0]
            for c in range(ng):
                if v[c] != 0:
                    fs[(a, b, c)] = -v[c] / v[ng]
    return fs


def _q_squared_zero(gens, fs, with_ghost):
    ng = len(gens)
    s = tuple([1, -1] * ng)
    m = lambda x, y: GA.mul(x, y, s)
    pl = [_plane(a) for a in range(ng)]
    c = [p[0] for p in pl]
    cb = [p[1] for p in pl]
    terms = [_scl(F(-1, 2) * v, m(m(c[a], c[b]), cb[cc])) for (a, b, cc), v in fs.items()]
    Gt = GA.add(*terms) if (terms and with_ghost) else {}
    acc = {}

    def put(M, x):
        for bb, v in x.items():
            add = _qsc(QI(v), M)
            acc[bb] = add if bb not in acc else _qadd(acc[bb], add)
    for a in range(ng):
        for b in range(ng):
            put(_qmul(gens[a], gens[b]), m(c[a], c[b]))
    if with_ghost:
        for a in range(ng):
            put(gens[a], GA.add(m(c[a], Gt), m(Gt, c[a])))
        put(_qid(len(gens[0])), m(Gt, Gt))
    return all(all(not x for r in M for x in r) for M in acc.values())


def check_derived_algebra_ghost_charge_is_nilpotent():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("field-theory.imported-tower-limit")
    gens = [_kron(x, _qid(3)) for x in _su(2)] + [_kron(_qid(2), y) for y in _su(3)] + [_qsc(_I, _qid(6))]
    ok = len(gens) == 12 and GA.field_rank([_flat(g) for g in gens]) == 12
    fs = _structure(gens)
    ok = ok and fs is not None and len(fs) == 62
    ok = ok and _q_squared_zero(gens, fs, True)
    ok = ok and not _q_squared_zero(gens, fs, False)
    key = sorted(k for k in fs if 3 <= k[0] < 11)[0]
    bad = dict(fs)
    bad[key] = bad[key] + 1
    ok = ok and not _q_squared_zero(gens, bad, True)
    GA.check("su(2) + su(3) + u(1) on C^2 x C^3 with twelve tower ghost pairs: Q^2 = 0, needs the cubic ghost term,"
             " fails for a perturbed structure constant", ok)
    return ok


if __name__ == "__main__":
    check_positive_forms_carry_no_self_adjoint_nilpotent()
    check_krein_brst_nilpotent_and_self_adjoint()
    check_cohomology_is_transverse_and_positive()
    check_cohomology_matches_the_photon_modes()
    check_derived_algebra_ghost_charge_is_nilpotent()
