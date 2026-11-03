"""dark-matter.type-residue-what-each-tower-can: exact checks.

Everything is computed in GA.py (exact Fractions). For a diagonal signature (p,q):
- the centre is the span of the central basis blades (commutation with a generator acts on a blade by a
  sign, so the centre is spanned by blades); its dimension and omega^2 give the component count;
- a primitive idempotent f = prod (1 + e_T)/2 is built greedily from commuting blades of square +1 that
  lower dim Cl f, and primitivity is then certified independently: the corner f Cl f is a division
  algebra, read off from the signature of its regular trace form tr(L_xy) ((1,0) = R, (1,1) = C,
  (1,3) = H; any other signature is not a division algebra);
- the irreducible module is Cl f, of real dimension m d, and m^2 d (components) = 2^n is checked.
Checked: the type table D and the component count on the P3 representatives (premise: the census and
sort of towers-are-residues), and residue invariance on all twenty signatures with n <= 5, including
along every rung (p,q) -> (p+1,q+1) (premise: the eight-towers fact). (i)-(iii): the intrinsic group is
the unit group of D; its Lie algebra is the trace-free (pure) part of f Cl f, of dimension 0, 1, 3, on
which x^2 = -N(x) f with N positive definite (so the complex structures are +-J for C and the unit
sphere S^2 of pure quaternions for H). (iv): at r = 1, 5 the central idempotents (1 +- omega)/2 give two
modules on which omega acts as +1 and -1 (inequivalent: omega is central); at r = 3, 7 omega f lies in
f Cl f, is pure and squares to -f: the volume element is the complex unit.
The literature classification (rule2.imported-classification-centre-type-c-external) is recomputed,
not relied on, so it gets no premise() call.
EXPORTS["clifford_type"](p, q) returns the dict computed here, for dependent checks.
"""
from fractions import Fraction as F
import GA
from pyutil import get_or_set
from tp_premise import premise

P3_REPS = {6: (1, 3), 2: (3, 1), 0: (2, 2), 4: (4, 0), 1: (2, 1), 7: (1, 2), 3: (4, 1), 5: (1, 4)}
_CACHE = {}


def _coords(x, blades):
    return [x.get(b, F(0)) for b in blades]


def _blade_sq(b, sq):
    return GA.mul({b: F(1)}, {b: F(1)}, sq).get((), F(0))


def _solve_in(basis_rows, v):
    """Coordinates of v in the span of the independent rows (exact), or None."""
    d = len(basis_rows)
    M = [[basis_rows[i][k] for i in range(d)] + [v[k]] for k in range(len(v))]
    ker = GA.field_kernel(M)
    for kv in ker:
        if kv[d] != 0:
            return [-kv[i] / kv[d] for i in range(d)]
    return None


def clifford_type(p, q):
    if (p, q) in _CACHE:
        return _CACHE[(p, q)]
    n = p + q
    sq = GA.sig(p, q)
    blades = GA.all_blades(n)
    central = [b for b in blades if all(GA.commutes({b: F(1)}, GA.gen(i), sq) for i in range(n))]
    om = tuple(range(n))
    w2 = _blade_sq(om, sq)

    def dim_left(f):
        return GA.rank_of_vectors([_coords(GA.mul({b: F(1)}, f, sq), blades) for b in blades])
    f, dim, chosen = GA.sc(1), 2 ** n, []
    for b in blades:
        if b == () or _blade_sq(b, sq) != 1:
            continue
        if not all(GA.commutes({b: F(1)}, {c: F(1)}, sq) for c in chosen):
            continue
        f2 = GA.mul(f, GA.scal(F(1, 2), GA.add(GA.sc(1), {b: F(1)})), sq)
        d2 = dim_left(f2)
        if 0 < d2 < dim:
            f, dim, chosen = f2, d2, chosen + [b]
    # corner algebra f A f
    rows, corner = [], []
    for b in blades:
        y = GA.mul(GA.mul(f, {b: F(1)}, sq), f, sq)
        c = _coords(y, blades)
        if any(c) and GA.rank_of_vectors(rows + [c]) > len(rows):
            rows.append(c)
            corner.append(y)
    d = len(corner)
    # regular representation L_x on the corner and the trace form
    L = []
    for x in corner:
        L.append([_solve_in(rows, _coords(GA.mul(x, y, sq), blades)) for y in corner])

    def lmat(cx):
        return [[sum((cx[a] * L[a][j][i] for a in range(d)), F(0)) for j in range(d)] for i in range(d)]
    prods = [[_solve_in(rows, _coords(GA.mul(x, y, sq), blades)) for y in corner] for x in corner]
    T = [[sum(lmat(prods[i][j])[k][k] for k in range(d)) for j in range(d)] for i in range(d)]
    tsig = GA.congruence_signature(T)
    D = {(1, 0, 0): "R", (1, 1, 0): "C", (1, 3, 0): "H"}.get(tuple(tsig))
    comps = 2 if (len(central) == 2 and w2 == 1) else 1
    m = dim // d if D else None
    out = dict(sig=(p, q), r=(p - q) % 8, centre=len(central), omega2=w2, D=D, d=d, comps=comps,
               m=m, dimS=dim, f=f, corner=corner, rows=rows, sq=sq, trace=T, tsig=tsig)
    _CACHE[(p, q)] = out
    return out


def _pure_part(t):
    """Trace-free part of the corner, as coordinate vectors: kernel of x -> tr(L_x) = T[x][unit]."""
    d = t["d"]
    unit = _solve_in(t["rows"], _coords(t["f"], GA.all_blades(sum(t["sig"]))))
    row = [sum(t["trace"][i][j] * unit[j] for j in range(d)) for i in range(d)]
    return GA.field_kernel([row]), unit


def check_type_table_on_p3_representatives():
    premise("dark-matter.towers-are-residues-single-clock-filter")
    want_D = {0: "R", 1: "R", 2: "R", 3: "C", 4: "H", 5: "H", 6: "H", 7: "C"}
    want_comps = {0: 1, 1: 2, 2: 1, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1}
    ok = True
    for r, (p, q) in P3_REPS.items():
        t = clifford_type(p, q)
        ok = ok and t["r"] == r and t["D"] == want_D[r] and t["comps"] == want_comps[r]
        ok = ok and t["comps"] * t["m"] * t["m"] * t["d"] == 2 ** (p + q)
        ok = ok and (t["centre"] == 2) == (r % 2 == 1)
    ok = ok and clifford_type(0, 4)["D"] == "H" and clifford_type(0, 4)["comps"] == 1
    GA.check("thm:types: D = R (r = 0, 1, 2), C (3, 7), H (4, 5, 6); two components exactly at r = 1, 5", ok)
    return ok


def check_type_is_a_residue_invariant():
    premise("dark-matter.imported-eight-towers-mod-8-clock")
    by_res = {}
    ok = True
    count = 0
    for n in range(1, 6):
        for p in range(n + 1):
            t = clifford_type(p, n - p)
            ok = ok and t["D"] is not None
            ok = ok and t["comps"] * t["m"] * t["m"] * t["d"] == 2 ** n
            get_or_set(by_res, t["r"], set()).add((t["D"], t["comps"]))
            if p >= 1 and n - p >= 1:
                lower = clifford_type(p - 1, n - p - 1) if n >= 3 else None
                if lower is not None:
                    ok = ok and (lower["D"], lower["comps"]) == (t["D"], t["comps"])
            count += 1
    ok = ok and count == 20 and len(by_res) == 8 and all(len(v) == 1 for v in by_res.values())
    GA.check("thm:types: on all 20 signatures with n <= 5 (D, components) depends on p - q mod 8 only, "
             "and is unchanged along each rung (p,q) -> (p+1,q+1)", ok)
    return ok


def _scalar_multiple(s, f):
    """lam with s = lam f (f nonzero), or None."""
    b0 = next(iter(f))
    lam = s.get(b0, F(0)) / f[b0]
    return lam if GA.eq(s, GA.scal(lam, f)) else None


def check_intrinsic_groups():
    premise("dark-matter.towers-are-residues-single-clock-filter")
    want_pure = {0: 0, 2: 0, 3: 1, 7: 1, 4: 3, 5: 3, 6: 3}
    ok = True
    for r, dim_pure in want_pure.items():
        t = clifford_type(*P3_REPS[r])
        pure, unit = _pure_part(t)
        ok = ok and len(pure) == dim_pure and len(pure) == t["d"] - 1
        sq = t["sq"]
        X = [GA.add(*[GA.scal(c[i], t["corner"][i]) for i in range(t["d"]) if c[i] != 0]) for c in pure]
        G = []
        for a in X:
            row = []
            for b in X:
                s = GA.scal(F(-1, 2), GA.add(GA.mul(a, b, sq), GA.mul(b, a, sq)))
                lam = _scalar_multiple(s, t["f"])
                ok = ok and lam is not None
                row.append(lam if lam is not None else F(0))
            G.append(row)
        if dim_pure:
            ok = ok and tuple(GA.congruence_signature(G)) == (dim_pure, 0, 0)
    GA.check("intrinsic groups: the pure part of D has dimension 0 (Z2 at r = 0, 2), 1 (U(1) at r = 3, 7), "
             "3 (Sp(1) at r = 4, 5, 6), with x^2 = -N(x) f, N positive definite", ok)
    return ok


def check_volume_element_on_the_odd_residues():
    premise("dark-matter.towers-are-residues-single-clock-filter")
    ok = True
    for r in (1, 5):
        p, q = P3_REPS[r]
        n = p + q
        sq = GA.sig(p, q)
        om = {tuple(range(n)): F(1)}
        t = clifford_type(p, q)
        ok = ok and GA.eq(GA.mul(om, om, sq), GA.sc(1)) and t["comps"] == 2
        # f and its grade involute lie in the two components; omega is central
        signs = []
        for g in (t["f"], GA.grade_inv(t["f"])):
            lam = _scalar_multiple(GA.mul(om, g, sq), g)
            ok = ok and lam is not None and GA.eq(GA.mul(g, g, sq), g)
            signs.append(lam)
        ok = ok and sorted(signs) == [-1, 1]
        for s in (1, -1):
            P = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(s, om)))
            ok = ok and GA.eq(GA.mul(P, P, sq), P) and all(GA.commutes(P, GA.gen(i), sq) for i in range(n))
    for r in (3, 7):
        p, q = P3_REPS[r]
        n = p + q
        sq = GA.sig(p, q)
        om = {tuple(range(n)): F(1)}
        t = clifford_type(p, q)
        ok = ok and GA.eq(GA.mul(om, om, sq), GA.sc(-1)) and t["comps"] == 1
        J = GA.mul(om, t["f"], sq)
        ok = ok and GA.eq(GA.mul(GA.mul(t["f"], om, sq), t["f"], sq), J)
        ok = ok and GA.eq(GA.mul(J, J, sq), GA.scal(-1, t["f"]))
        ok = ok and _solve_in(t["rows"], _coords(J, GA.all_blades(n))) is not None and t["D"] == "C"
    GA.check("(iv): r = 1, 5: omega^2 = 1, two modules with omega = +1 and -1; r = 3, 7: omega f is the "
             "complex unit of f Cl f (square -f)", ok)
    return ok


EXPORTS = {"clifford_type": clifford_type, "P3_REPS": P3_REPS}
