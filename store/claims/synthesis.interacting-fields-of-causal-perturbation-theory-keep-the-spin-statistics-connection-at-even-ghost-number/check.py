"""Interacting fields of causal perturbation theory keep the spin-statistics connection of the
attached free fields: exact checks.

Spacetime algebra Cl(1,3), g0^2 = +1, gi^2 = -1, I4 = g0 g1 g2 g3. A Lorentz rotor R acts on a
spinor value by psi -> R psi, on vector and bivector values by x -> R x R~, and fixes scalar values
(the scalar fields and the Faddeev-Popov ghosts). The rotation by 2 pi is the end point of the loop
of four quarter turns in the plane g1 g2, computed as the normalised product of (1 + g1 g2)^4.

(1) The 2 pi rotor is -1: it fixes every vector and bivector value and negates every spinor value.
(2) Every monomial of the series' interaction density (vector and axial vertices, Yukawa and mass
    insertions with the doublet scalars, scalar gauge couplings, quartics, non-abelian cubic and
    quartic terms, gauge fixing, ghost terms) is a Lorentz scalar (exact rational rotors: rotations,
    boosts and a product), has an even number of spinor factors (2 pi eigenvalue +1, computed from
    the rotor action) and equal numbers of ghost and antighost factors; the counts are computed as
    homogeneity degrees, not labelled.
(2') The free Feynman-gauge potential: the Gupta-Bleuler polarisation sum is -a.b on test vectors,
    independent of k (degree 0) and indefinite; the bracket factor 1 + eta c (-1)^d of the stored
    locality result vanishes for the CCR (eta = -1) at c = 1, so the potential is local in the Krein form.
(3) Fermionic factors are tower modes v = (e + f)/2 on distinct tower planes of Cl(m, m) (CAR).
    For every Wick monomial with n_psi spinor and n_c + n_cbar ghost factors (n_psi <= 3,
    n_c, n_cbar <= 2) the Grassmann parity (grade involution) and the 2 pi eigenvalue (spinor modes
    computed in Cl(1,3) from the 2 pi rotor acting on a product of n_psi spinors) agree exactly when n_c + n_cbar is even, in
    particular at ghost number zero; among ghost-even monomials on disjoint modes two anticommute
    exactly when both have 2 pi eigenvalue -1.
(4) First order of the interacting field: for an even interaction element L the graded Jacobi
    identity [L, [A, B]] = [[L, A], B] + [A, [L, B]] holds for homogeneous A, B (supercommutators);
    an odd L needs the sign (-1)^{|L||A|} and violates the even form; [L, A] keeps the parity and the 2 pi eigenvalue of A; and the
    light-cone lemma of the locality step holds on a rational sample: if x and z are spacelike
    separated and y lies in the causal past of x with y0 > z0, then y and z are spacelike separated.
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
MET = [1, -1, -1, -1]


def g(i):
    return GA.gen(i)


def mm(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def vec(c):
    return {(i,): F(x) for i, x in enumerate(c) if x != 0}


def wedge(a, b):
    return GA.scal(F(1, 2), GA.sub(mm(a, b), mm(b, a)))


def s0(x):
    return x.get((), F(0))


def sandwich(R, x):
    return mm(R, x, GA.reverse(R))


I4 = mm(g(0), g(1), g(2), g(3))

# ---------------------------------------------------------------- sample values (inputs)
SPINORS = [
    GA.add(GA.sc(2), GA.scal(3, mm(g(0), g(1))), GA.scal(-1, mm(g(2), g(3))), GA.scal(5, I4)),
    GA.add(GA.sc(F(1, 2)), GA.scal(4, mm(g(1), g(2))), GA.scal(7, mm(g(0), g(3))), GA.scal(-3, I4),
           GA.scal(2, mm(g(0), g(2)))),
    GA.add(GA.sc(-3), GA.scal(F(5, 3), mm(g(1), g(3))), GA.scal(6, mm(g(0), g(2)))),
]
VECTORS = [vec((2, 1, -3, 5)), vec((F(1, 2), 4, 0, -1)), vec((-1, 2, 7, 3)), vec((3, -5, 1, 2)),
           vec((6, 1, 1, -2))]
BIVECTORS = [wedge(VECTORS[0], VECTORS[1]), wedge(VECTORS[2], VECTORS[3])]
SCALARS = [F(3), F(-2, 5), F(7, 2), F(4)]
ROT = GA.scal(F(1, 5), GA.add(GA.sc(3), GA.scal(4, mm(g(1), g(2)))))      # rotation, R R~ = 1
BOOST = GA.scal(F(1, 3), GA.add(GA.sc(5), GA.scal(4, mm(g(0), g(1)))))     # boost, R R~ = 1
TILT = GA.scal(F(1, 13), GA.add(GA.sc(5), GA.scal(12, mm(g(2), g(3)))))   # rotation, R R~ = 1
ROTORS = [ROT, BOOST, TILT, mm(BOOST, TILT, ROT)]
# light-cone lemma sample: pairs of spacelike-separated points and a grid of trial points y
LC_PAIRS = [((2, 0, 0, 0), (0, 3, 0, 0)), ((2, 2, 0, 1), (1, -1, 1, 1)), ((F(3, 2), 0, 0, 0), (0, 2, 0, 0))]
LC_GRID = [(F(a, 2), F(b, 2), F(c, 2), 0) for a in range(-8, 5) for b in range(-6, 9)
           for c in range(-4, 7)]


def Q(x):
    return sum(MET[m] * F(x[m]) ** 2 for m in range(4))


def diff(x, y):
    return tuple(F(x[m]) - F(y[m]) for m in range(4))


def in_causal_past(y, x):
    d = diff(x, y)
    return Q(d) >= 0 and d[0] >= 0


def two_pi_rotor():
    quarter = GA.add(GA.sc(1), mm(g(1), g(2)))
    loop = mm(quarter, quarter, quarter, quarter)
    norm = s0(mm(quarter, GA.reverse(quarter))) ** 4
    root = F(4) if norm == 16 else None
    return GA.scal(F(1) / root, loop)


# ---------------------------------------------------------------- (1)
def check_rotation_by_two_pi_is_minus_one_on_spinor_values_and_one_on_tensor_values():
    premise("field-theory.second-quantisation")
    U = two_pi_rotor()
    ok = GA.eq(U, GA.sc(-1)) and GA.eq(mm(U, GA.reverse(U)), GA.sc(1))
    half = mm(GA.add(GA.sc(1), mm(g(1), g(2))), GA.add(GA.sc(1), mm(g(1), g(2))))
    ok = ok and GA.eq(sandwich(GA.scal(F(1, 2), half), g(1)), GA.neg(g(1)))      # half the loop turns by pi
    ok = ok and all(GA.eq(sandwich(U, v), v) for v in VECTORS + BIVECTORS)
    ok = ok and all(GA.eq(mm(U, p), GA.neg(p)) for p in SPINORS)
    GA.check("the loop of four quarter turns is the rotor -1: tensors fixed, spinors negated", ok)
    return ok


# ---------------------------------------------------------------- (2)
def _monomials():
    """name -> value(fields); fields = dict of sample values (ghost values as scalar placeholders)."""
    J = lambda f: mm(f["psi"], g(0), GA.reverse(f["psi"]))           # vector current
    K = lambda f: mm(f["psi"], g(3), GA.reverse(f["psi"]))           # axial current
    return {
        "vector vertex <J A>": lambda f: s0(mm(J(f), f["A1"])),
        "axial vertex <K A>": lambda f: s0(mm(K(f), f["A2"])),
        "Yukawa <psi psi~> phi": lambda f: s0(mm(f["psi"], GA.reverse(f["psi"]))) * f["phi1"],
        "pseudoscalar Yukawa": lambda f: s0(mm(f["psi"], GA.reverse(f["psi"]), I4)) * f["phi2"],
        "scalar current <A d> phi phi": lambda f: s0(mm(f["A1"], f["d1"])) * f["phi1"] * f["phi2"],
        "seagull <A A> phi phi": lambda f: s0(mm(f["A1"], f["A2"])) * f["phi3"] * f["phi4"],
        "quartic phi^4": lambda f: f["phi1"] * f["phi2"] * f["phi3"] * f["phi4"],
        "cubic gauge <(d^A)(A^A)>": lambda f: s0(mm(wedge(f["d1"], f["A1"]), wedge(f["A2"], f["A3"]))),
        "quartic gauge <(A^A)(A^A)>": lambda f: s0(mm(wedge(f["A1"], f["A2"]), wedge(f["A3"], f["A1"]))),
        "gauge fixing <d A>^2": lambda f: s0(mm(f["d1"], f["A1"])) ** 2,
        "ghost kinetic <d d> cbar c": lambda f: s0(mm(f["d1"], f["d2"])) * f["cbar"] * f["c"],
        "ghost gauge <d A> cbar c": lambda f: s0(mm(f["d2"], f["A3"])) * f["cbar"] * f["c"],
    }


def _degree(val, f, key, lam):
    """homogeneity degree of val in the field f[key]: val(lam f) = lam^n val(f), n found by search."""
    g2 = dict(f)
    g2[key] = GA.scal(lam, f[key]) if isinstance(f[key], dict) else lam * f[key]
    ratio = val(g2) / val(f)
    for n in range(6):
        if ratio == F(lam) ** n:
            return n
    return None


def _fields(psi):
    return {"psi": psi, "A1": VECTORS[0], "A2": VECTORS[1], "A3": VECTORS[2], "d1": VECTORS[3],
            "d2": VECTORS[4], "phi1": SCALARS[0], "phi2": SCALARS[1], "phi3": SCALARS[2],
            "phi4": SCALARS[3], "c": F(2), "cbar": F(5)}


def _transform(f, R):
    out = dict(f)
    out["psi"] = mm(R, f["psi"])
    for k in ("A1", "A2", "A3", "d1", "d2"):
        out[k] = sandwich(R, f[k])
    return out


def check_interaction_monomials_are_lorentz_scalars_even_in_spinors_and_ghosts():
    premise("synthesis.one-loop-qed-in-the-spacetime-algebra")
    premise("synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts")
    premise("field-theory.second-quantisation")
    U = two_pi_rotor()
    ok = all(GA.eq(mm(R, GA.reverse(R)), GA.sc(1)) for R in ROTORS)
    for name, val in _monomials().items():
        for psi in SPINORS:
            f = _fields(psi)
            v0 = val(f)
            # counts computed from homogeneity, not labelled: spinor degree, ghost and antighost degrees
            npsi = _degree(val, f, "psi", 2)
            nc, ncb = _degree(val, f, "c", 3), _degree(val, f, "cbar", 5)
            inv = all(val(_transform(f, R)) == v0 for R in ROTORS)
            eig = v0 != 0 and val(_transform(f, U)) == (-1) ** npsi * v0
            parity = npsi in (0, 2) and nc == ncb and (nc + ncb) % 2 == 0
            if not (inv and eig and parity):
                GA.check("monomial " + name, False)
                ok = False
    # control: a one-spinor scalar changes sign under the 2 pi rotor and has spinor degree 1
    f = _fields(SPINORS[0])
    odd = lambda h: s0(mm(h["psi"], g(0), h["A1"]))
    ok = ok and odd(f) != 0 and odd(_transform(f, U)) == -odd(f) and _degree(odd, f, "psi", 2) == 1
    GA.check("the interaction monomials are Lorentz scalars with even spinor and ghost counts", ok)
    return ok


def check_feynman_gauge_potential_is_local_only_in_the_krein_form():
    premise("synthesis.locality-of-the-attached-free-fields-fixes-their-statistics")
    premise("synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields")  # (K1): the Gupta-Bleuler form of the potential
    premise("synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts")
    # Gupta-Bleuler: [a_mu, a_nu^dagger] = -g_mu nu; polarisation sum on test vectors a, b is
    # sum_mu (-g_mu mu)(a.g_mu)(g_mu.b) / g_mu mu^2 = -a.b, independent of k: degree 0
    ok = True
    for a in VECTORS:
        for b in VECTORS:
            P = sum(-MET[m] * s0(mm(a, g(m))) * s0(mm(g(m), b)) for m in range(4))
            ok = ok and P == -s0(mm(a, b))
    # the form is indefinite: a timelike test vector has negative weight, a spacelike one positive
    ok = ok and -Q((1, 0, 0, 0)) < 0 and -Q((0, 1, 0, 0)) > 0
    # bracket factor 1 + eta c (-1)^d of the stored locality result at d = 0, c = 1:
    d, c = 0, 1
    ok = ok and 1 + (-1) * c * (-1) ** d == 0 and 1 + (+1) * c * (-1) ** d != 0
    GA.check("Feynman-gauge potential: polarisation sum -a.b of degree 0, indefinite, local as a CCR field", ok)
    return ok


# ---------------------------------------------------------------- (3) tower model of the grading
def _tower_modes(m):
    sq = GA.sig(m, m)
    modes = [GA.scal(F(1, 2), GA.add(GA.gen(j), GA.gen(m + j))) for j in range(m)]
    return sq, modes


def _wick(sq, modes, npsi, nc, ncb, spin_factor):
    X = GA.sc(1)
    for j in range(npsi):
        X = GA.mul(X, GA.scal(spin_factor, modes[j]), sq)
    for j in range(nc + ncb):
        X = GA.mul(X, modes[3 + j], sq)
    return X


def _sign(Y, X):
    if GA.eq(Y, X):
        return 1
    if GA.eq(Y, GA.neg(X)):
        return -1
    return 0


def _spinor_product(n, U=None):
    """psi_1 g0 psi_2 g0 ... psi_n in Cl(1,3), each spinor optionally rotated by U."""
    X = GA.sc(1)
    for j in range(n):
        p = SPINORS[j % len(SPINORS)]
        X = mm(X, mm(U, p) if U is not None else p)
        if j < n - 1:
            X = mm(X, g(0))
    return X


def check_rotation_by_two_pi_equals_the_grading_exactly_at_even_ghost_count():
    premise("synthesis.locality-of-the-attached-free-fields-fixes-their-statistics")
    premise("field-theory.imported-tower-limit")
    U = two_pi_rotor()
    sq, modes = _tower_modes(7)
    # the modes are a CAR system: v_j^2 = 0, {v_j, v_k} = 0 on distinct planes
    ok = all(GA.is_zero(GA.mul(v, v, sq)) for v in modes)
    ok = ok and GA.anticommutes(modes[0], modes[4], sq)
    table = {}
    for npsi, nc, ncb in product(range(4), range(3), range(3)):
        X = _wick(sq, modes, npsi, nc, ncb, 1)
        grading = _sign(GA.grade_inv(X), X)                       # tower model: Grassmann parity
        S = _spinor_product(npsi)
        rot = _sign(_spinor_product(npsi, U), S)                   # spacetime algebra: 2 pi rotor
        table[(npsi, nc, ncb)] = (grading, rot, X)
        if grading == 0 or rot == 0 or GA.is_zero(X) or GA.is_zero(S):
            ok = False
        if (grading == rot) != ((nc + ncb) % 2 == 0):
            ok = False
        if nc == ncb and grading != rot:
            ok = False
    mismatches = sum(1 for k, (a, b, _) in table.items() if a != b)
    odd_pairs = sum(1 for p, q in product(range(3), range(3)) if (p + q) % 2 == 1)
    ok = ok and mismatches == len(range(4)) * odd_pairs
    # on disjoint modes, ghost-even monomials anticommute exactly when both rotate by -1
    sq2, modes2 = _tower_modes(12)
    for (a, b) in [((1, 0, 0), (1, 1, 1)), ((1, 0, 0), (2, 0, 0)), ((3, 1, 1), (1, 0, 0)),
                   ((2, 1, 1), (2, 0, 0)), ((0, 1, 1), (3, 0, 0))]:
        XA = GA.sc(1)
        for j in range(sum(a)):
            XA = GA.mul(XA, modes2[j], sq2)
        XB = GA.sc(1)
        for j in range(sum(b)):
            XB = GA.mul(XB, modes2[6 + j], sq2)
        rA, rB = table[a][1], table[b][1]
        anti = GA.anticommutes(XA, XB, sq2)
        comm = GA.commutes(XA, XB, sq2)
        if anti != (rA == -1 and rB == -1) or comm == anti:
            ok = False
    GA.check("grading = rotation by 2 pi exactly on ghost-even Wick monomials", ok)
    return ok


# ---------------------------------------------------------------- (4) first order
def _scomm(X, Y, px, py, sq):
    s = -1 if (px * py) % 2 == 1 else 1
    return GA.sub(GA.mul(X, Y, sq), GA.scal(s, GA.mul(Y, X, sq)))


SQ6, V6 = _tower_modes(6)
W6 = [GA.scal(F(1, 2), GA.sub(GA.gen(j), GA.gen(6 + j))) for j in range(6)]       # adjoint modes
# an even interaction element: spinor bilinears and a ghost bilinear (modes 0..3 spinor, 4..5 ghost)
L_EVEN = GA.add(GA.mul(W6[0], V6[1], SQ6), GA.scal(3, GA.mul(W6[1], V6[0], SQ6)), GA.mul(W6[4], V6[5], SQ6))
L_ODD = GA.add(V6[0], GA.scal(2, W6[1]))
HOMOG = [(V6[0], 1), (GA.mul(V6[1], W6[0], SQ6), 0), (GA.mul(V6[0], GA.mul(V6[1], W6[2], SQ6), SQ6), 1),
         (GA.add(W6[1], GA.scal(2, V6[2])), 1), (GA.mul(W6[5], V6[4], SQ6), 0)]


def _spin_flip(X):
    """the 2 pi rotor on the tower model: sign (-1) per spinor mode (generators j and 6 + j, j < 4)"""
    return {b: (c if sum(1 for i in b if i % 6 < 4) % 2 == 0 else -c) for b, c in X.items()}


def check_first_order_interacting_fields_keep_parity_spin_and_graded_locality():
    premise("synthesis.locality-of-the-attached-free-fields-fixes-their-statistics")
    premise("synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products")  # Bogoliubov's interacting fields of causal perturbation theory
    sq = SQ6
    ok = _sign(GA.grade_inv(L_EVEN), L_EVEN) == 1 and GA.eq(_spin_flip(L_EVEN), L_EVEN)
    ok = ok and _sign(GA.grade_inv(L_ODD), L_ODD) == -1
    nonzero, even_form_fails = 0, 0
    for (A, pa), (B, pb) in product(HOMOG, HOMOG):
        ok = ok and _sign(GA.grade_inv(A), A) == (-1) ** pa
        lhs = _scomm(L_EVEN, _scomm(A, B, pa, pb, sq), 0, (pa + pb) % 2, sq)
        rhs = GA.add(_scomm(_scomm(L_EVEN, A, 0, pa, sq), B, pa, pb, sq),
                     _scomm(A, _scomm(L_EVEN, B, 0, pb, sq), pa, pb, sq))
        ok = ok and GA.eq(lhs, rhs)
        nonzero += 0 if GA.is_zero(lhs) else 1
        # odd L: the graded Jacobi identity needs the sign (-1)^{|L||A|} on the second term
        lo = _scomm(L_ODD, _scomm(A, B, pa, pb, sq), 1, (pa + pb) % 2, sq)
        t1 = _scomm(_scomm(L_ODD, A, 1, pa, sq), B, (pa + 1) % 2, pb, sq)
        t2 = _scomm(A, _scomm(L_ODD, B, 1, pb, sq), pa, (pb + 1) % 2, sq)
        ok = ok and GA.eq(lo, GA.add(t1, GA.scal((-1) ** pa, t2)))
        even_form_fails += 0 if GA.eq(lo, GA.add(t1, t2)) else 1
    ok = ok and nonzero > 0 and even_form_fails > 0
    kept = 0
    for A, pa in HOMOG:
        C = GA.sub(GA.mul(L_EVEN, A, sq), GA.mul(A, L_EVEN, sq))
        if GA.is_zero(C):
            continue
        kept += 1
        ok = ok and _sign(GA.grade_inv(C), C) == (-1) ** pa and _sign(_spin_flip(C), C) == _sign(_spin_flip(A), A)
    ok = ok and kept > 0
    # light-cone lemma, with a control showing the hypothesis y0 > z0 is needed
    hits, control = 0, 0
    for x, z in LC_PAIRS:
        ok = ok and Q(diff(x, z)) < 0
        for y in LC_GRID:
            if in_causal_past(y, x):
                if F(y[0]) > F(z[0]):
                    hits += 1
                    ok = ok and Q(diff(y, z)) < 0
                elif in_causal_past(y, z):
                    control += 1
    ok = ok and hits > 0 and control > 0
    GA.check("first order: graded Jacobi for even L, parity and spin kept, light-cone lemma", ok)
    return ok


if __name__ == "__main__":
    for fn in [check_rotation_by_two_pi_is_minus_one_on_spinor_values_and_one_on_tensor_values,
               check_interaction_monomials_are_lorentz_scalars_even_in_spinors_and_ghosts,
               check_feynman_gauge_potential_is_local_only_in_the_krein_form,
               check_rotation_by_two_pi_equals_the_grading_exactly_at_even_ghost_count,
               check_first_order_interacting_fields_keep_parity_spin_and_graded_locality]:
        print(fn.__name__, fn())
