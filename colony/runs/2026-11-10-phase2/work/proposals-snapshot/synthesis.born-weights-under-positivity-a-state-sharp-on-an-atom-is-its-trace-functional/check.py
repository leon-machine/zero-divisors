"""synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional: exact checks.

Cl_Q(p,q) on blades; the dagger sends a blade to its inverse; tau is the scalar part. An atom is a
self-adjoint idempotent P whose corner P A P has only the multiples of P as self-adjoint elements.

(i)   maximal independent commuting sets of blades of square +1 give atoms in every signature with
      p + q <= 5 and in (2,4), (3,3): trace 2^-m, corner dimension 1, 2 or 4, self-adjoint corner 1.
(ii)  the orbit y P y^dagger / lambda of an atom consists of atoms of the same trace, a hermitian square
      is a non-negative combination of atoms, and the weight of one orbit atom in another is the
      squared modulus of the overlap over the product of the squared norms (real, complex-type and
      quaternion-type corners: signatures (2,2), (3,0), (1,3)).
(iii) the uniqueness step as linear algebra: N A + A N + (anti-self-adjoint elements), N = 1 - P, has
      codimension exactly one and tau(P .) vanishes on it, for blade atoms and orbit atoms.
(iv)  the three examples showing that reality, positivity and the atom condition are each needed.
The Cauchy-Schwarz step (a positive real functional with value zero on N vanishes on N A) is the proof's.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
HALF = F(1, 2)
SIGS_SMALL = [(p, n - p) for n in range(1, 6) for p in range(n + 1)] + [(2, 4), (3, 3)]
ORBIT_SIGS = [(2, 2), (3, 0), (1, 3)]
SEEDS = [[1, 2, 0, -1, 3, 0, 1, 1, -2, 1, 0, 2, 1, -1, 0, 3], [2, 0, 1, 0, 0, 1, 0, -1, 1, 1, 3, 0, 0, -2, 1, 0],
         [0, 1, -1, 2, 0, 2, 0, 1, 1, 0, 0, -1, 2, 0, 1, 1]]


def dsign(b, sq):
    g = len(b)
    s = (-1) ** (g * (g - 1) // 2)
    for i in b:
        s *= sq[i]
    return s


def dagger(x, sq):
    return {b: c * dsign(b, sq) for b, c in x.items()}


def clean(x):
    return {b: c for b, c in x.items() if c != 0}


def prod(sq, *xs):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, sq)
    return clean(r)


def lin(*terms):
    r = {}
    for c, x in terms:
        r = GA.add(r, GA.scal(F(c), x))
    return clean(r)


def tau(x):
    return x.get((), F(0))


def blade(b):
    return {tuple(b): F(1)}


def blades_commute(b1, b2):
    return (len(b1) * len(b2) - len(set(b1) & set(b2))) % 2 == 0


def maximal_set(sq, order):
    """Greedy maximal independent commuting set of blades of square +1; returns (generators, group)."""
    gens, group = [], {(): F(1)}
    for b in order:
        if not b or dsign(b, sq) != 1 or b in group:
            continue
        if any(not blades_commute(b, g) for g in gens):
            continue
        new = {}
        for t, s in group.items():
            c, bb = GA.blade_mul(t, b, sq)
            new[bb] = s * c
        group.update(new)
        gens.append(b)
    return gens, group


def idem(sq, gens, signs=None):
    P = ONE
    for i, b in enumerate(gens):
        s = 1 if signs is None else signs[i]
        P = prod(sq, P, lin((HALF, ONE), (HALF * s, blade(b))))
    return P


def vec(x, blades):
    return [x.get(b, F(0)) for b in blades]


def corner(sq, P):
    """(dimension of P A P, dimension of its self-adjoint part)."""
    blades = GA.all_blades(len(sq))
    full, sym = [], []
    for b in blades:
        y = prod(sq, P, blade(b), P)
        full.append(vec(y, blades))
        sym.append(vec(GA.add(y, dagger(y, sq)), blades))
    return GA.rank_of_vectors(full), GA.rank_of_vectors(sym)


def is_projector(sq, P):
    return dagger(P, sq) == P and prod(sq, P, P) == P and P != {}


def atom_table():
    out = {}
    for p, q in SIGS_SMALL:
        sq = GA.sig(p, q)
        blades = [b for b in GA.all_blades(p + q) if b]
        rows = set()
        for order in (blades, blades[::-1]):
            gens, group = maximal_set(sq, order)
            maximal = all(b in group for b in blades
                          if dsign(b, sq) == 1 and all(blades_commute(b, g) for g in gens))
            P = idem(sq, gens)
            ok = maximal and is_projector(sq, P) and tau(P) * 2 ** len(gens) == 1
            rows.add((len(gens),) + corner(sq, P) + (ok,))
        out[(p, q)] = sorted(rows)
    return out


def element(sq, seed, shift):
    blades = GA.all_blades(len(sq))
    return clean({b: F(seed[(i + shift) % len(seed)]) for i, b in enumerate(blades)})


def orbit_atom(sq, P, y):
    lam = tau(prod(sq, P, dagger(y, sq), y)) / tau(P)
    return GA.scal(F(1) / lam, prod(sq, y, P, dagger(y, sq))), lam


def orbit_report(p, q):
    """For one signature: orbit atoms are atoms; hermitian square = sum of atoms; weights."""
    sq = GA.sig(p, q)
    blades = [b for b in GA.all_blades(p + q) if b]
    gens, _ = maximal_set(sq, blades)
    P = idem(sq, gens)
    dims = corner(sq, P)
    ok = True
    weights = []
    for k, seed in enumerate(SEEDS):
        x, y = element(sq, seed, k), element(sq, seed, k + 5)
        Q, lx = orbit_atom(sq, P, x)
        R, ly = orbit_atom(sq, P, y)
        ok = ok and lx > 0 and ly > 0 and is_projector(sq, Q) and is_projector(sq, R)
        ok = ok and tau(Q) == tau(P) and corner(sq, Q) == dims
        z = prod(sq, P, dagger(x, sq), y, P)
        w = tau(prod(sq, Q, R)) / tau(Q)
        ok = ok and w == tau(prod(sq, z, dagger(z, sq))) / (lx * ly * tau(P)) and 0 <= w <= 1
        ok = ok and w == tau(prod(sq, R, Q)) / tau(R)
        # hermitian square as a non-negative combination of atoms
        total = {}
        n = len(gens)
        for mask in range(2 ** n):
            signs = [1 if (mask >> i) & 1 == 0 else -1 for i in range(n)]
            Pc = idem(sq, gens, signs)
            if prod(sq, x, Pc) == {}:
                continue
            Rc, lc = orbit_atom(sq, Pc, x)
            ok = ok and lc > 0 and is_projector(sq, Rc)
            total = GA.add(total, GA.scal(lc, Rc))
        ok = ok and clean(GA.sub(total, prod(sq, x, dagger(x, sq)))) == {}
        weights.append(w)
    return dims, ok, weights


def uniqueness_codimension(sq, P):
    """Dimension of N A + A N + anti-self-adjoint elements, and whether tau(P .) vanishes on it."""
    blades = GA.all_blades(len(sq))
    N = clean(GA.sub(ONE, P))
    rows, ok = [], True
    for b in blades:
        cands = [prod(sq, N, blade(b)), prod(sq, blade(b), N)]
        if dsign(b, sq) == -1:
            cands.append(blade(b))
        for y in cands:
            rows.append(vec(y, blades))
            ok = ok and tau(prod(sq, P, y)) == 0
    return GA.rank_of_vectors(rows), ok


def modes(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]
    f = [GA.gen(2 * k + 1) for k in range(m)]
    p = [prod(sq, f[k], e[k]) for k in range(m)]
    return sq, e, f, p


def check_maximal_commuting_blade_sets_give_atoms_in_every_small_signature():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    table = atom_table()
    assert all(len(rows) == 1 and rows[0][-1] for rows in table.values())
    got = {s: rows[0][:3] for s, rows in table.items()}
    # (number of blades in the set, dimension of the corner, dimension of its self-adjoint part)
    assert got[(1, 1)] == (1, 1, 1) and got[(2, 0)] == (1, 1, 1) and got[(0, 2)] == (0, 4, 1)
    assert got[(3, 0)] == (1, 2, 1) and got[(1, 3)] == (1, 4, 1) and got[(2, 2)] == (2, 1, 1)
    assert got[(0, 1)] == (0, 2, 1) and got[(0, 3)] == (1, 4, 1) and got[(3, 2)] == (3, 1, 1)
    assert got[(2, 4)] == (2, 4, 1) and got[(3, 3)] == (3, 1, 1) and got[(4, 1)] == (2, 2, 1)
    assert all(v[2] == 1 and v[1] in (1, 2, 4) for v in got.values()) and len(got) == 22


def check_orbit_atoms_hermitian_squares_and_overlap_weights():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    reports = [orbit_report(p, q) for p, q in ORBIT_SIGS]
    assert all(r[1] for r in reports)
    assert [r[0] for r in reports] == [(1, 1), (2, 1), (4, 1)]
    w = reports[0][2]
    assert w == [F(36, 85), F(0), F(11, 17)] and all(0 <= x <= 1 for r in reports for x in r[2])
    assert reports[1][2] == [F(145, 161), F(1, 2), F(1, 6)]
    assert reports[2][2] == [F(1025, 1457), F(184, 315), F(82, 273)]


def check_sharpness_on_an_atom_leaves_one_functional():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    out = []
    for p, q in ORBIT_SIGS + [(1, 1), (0, 2), (2, 1)]:
        sq = GA.sig(p, q)
        blades = [b for b in GA.all_blades(p + q) if b]
        gens, _ = maximal_set(sq, blades)
        P = idem(sq, gens)
        rank, ok = uniqueness_codimension(sq, P)
        Q, _ = orbit_atom(sq, P, element(sq, SEEDS[0], 3))
        rank2, ok2 = uniqueness_codimension(sq, Q)
        assert ok and ok2
        out.append((2 ** (p + q) - rank, 2 ** (p + q) - rank2))
    assert out == [(1, 1)] * 6
    # the vacuum projector of two modes: killed by both lowering vectors, corner of dimension one
    sq, e, f, p = modes(2)
    P0 = idem(sq, [(0, 1), (2, 3)], [-1, -1])
    v = [lin((HALF, e[k]), (HALF, f[k])) for k in range(2)]
    assert P0 == prod(sq, lin((HALF, ONE), (HALF, p[0])), lin((HALF, ONE), (HALF, p[1])))
    assert all(prod(sq, vk, P0) == {} for vk in v) and corner(sq, P0) == (1, 1) and tau(P0) == F(1, 4)
    # a projector that is not an atom leaves a family: the corner has self-adjoint dimension 2
    Pbig = lin((HALF, ONE), (HALF, p[0]))
    rank3, _ = uniqueness_codimension(sq, Pbig)
    assert corner(sq, Pbig) == (4, 3) and 16 - rank3 == 3


def check_reality_positivity_and_the_atom_condition_are_each_needed():
    premise("synthesis.premise-positivity-of-values")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    sq, e, f, p = modes(1)
    P = lin((HALF, ONE), (HALF, p[0]))
    assert is_projector(sq, P) and corner(sq, P) == (1, 1)
    born = lambda x: tau(prod(sq, P, x)) / tau(P)
    # (a) no reality: positive on hermitian squares, sharp on P, differs on the anti-self-adjoint f
    mu = lambda x: born(x) + tau(prod(sq, f[0], x))
    grid = [lin((a, ONE), (b, e[0]), (c, f[0]), (d, p[0]))
            for a in range(-2, 3) for b in range(-2, 3) for c in range(-2, 3) for d in range(-2, 3)]
    assert mu(ONE) == 1 and mu(P) == 1 and mu(f[0]) == -1 and born(f[0]) == 0
    assert all(mu(prod(sq, y, dagger(y, sq))) == born(prod(sq, y, dagger(y, sq))) >= 0 for y in grid)
    assert all(mu(lin((1, y), (1, dagger(y, sq)))) == born(lin((1, y), (1, dagger(y, sq)))) for y in grid)
    # (b) no positivity: real, normalised, sharp on P, value 1/3 on e, negative on a hermitian square
    m = lin((1, ONE), (1, p[0]), (F(1, 3), e[0]))
    lam = lambda x: tau(prod(sq, m, x))
    y = lin((-3, ONE), (3, e[0]), (-2, f[0]), (2, p[0]))
    assert dagger(m, sq) == m and lam(ONE) == 1 and lam(P) == 1 and lam(e[0]) == F(1, 3) and born(e[0]) == 0
    assert lam(prod(sq, y, dagger(y, sq))) == F(-4, 3)
    # (c) not an atom: two states sharp on (1 + p_1)/2 in two modes
    sq, e, f, p = modes(2)
    Pbig = lin((HALF, ONE), (HALF, p[0]))
    s = prod(sq, Pbig, p[1])
    for eps in (F(1), F(-1, 2)):
        rho = lin((1, Pbig), (eps, s))
        om = lambda x: tau(prod(sq, rho, x)) / tau(Pbig)
        assert om(ONE) == 1 and om(Pbig) == 1 and om(p[1]) == eps
        assert all(om(prod(sq, y, dagger(y, sq))) >= 0
                   for y in (element(sq, sd, k) for k, sd in enumerate(SEEDS)))
