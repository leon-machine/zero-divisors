"""families.imported-tree-relations-family-no-go: exact checks.

The module (32 x 32 Jordan-Wigner operators, invariant pairing, forms, species) comes from the EXPORTS of
standard-model.family-no-go-vev-cannot-separate. Species names are Hypothesis (S)'s. The literature factor
three (Georgi-Jarlskog, record level) is not computed; the external literature entity is not touched.
(0) c = a v_4 + b w_4 at sample (a, b): symmetric form with entry magnitudes {|a|} on (L, nu^c), (Q, u^c) and
    {|b|} on (L, e^c), (Q, d^c), nothing else: m_nu = m_u, m_e = m_d.
(i) For two generic rational family matrices and every signed entry pair (y_e, y_d) of the 10 form,
    y_e F and y_d F have the same characteristic invariants of M M^T (equal singular spectra); the 126 entries
    (-1, +-1/3) give different ones (control).
(ii) I = a v_1 + b w_1, c_4 = -w_4 + lambda v_4, c_5 = -w_5 at sample values generate an 8-dimensional algebra
    (closure under right multiplication); its colour-singlet part (exact kernel of the su(3) commutators) is
    4-dimensional and its odd singlet elements lie in the span of the rung mode vectors (the 10).
(iii) Adding b = v_4 v_5 and b^dagger = w_5 w_4: the algebra is 32-dimensional, its colour-singlet part is the
    16-dimensional rung Clifford algebra (equal to the span of the 16 rung monomials); its odd elements of
    Y = -1/2, T_3 = -1/2 are spanned by w_4 and v_5 w_4 w_5 = w_4 N_5 (as operators), f(w_4 N_5) = 1/2 f(w_4),
    b^dagger v_5 = -w_4 + w_4 N_5 with form -1/2 f(w_4): every symmetric doublet form is a multiple of the 10 form.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

RUNG_PLANE = [(F(1), F(0)), (F(0), F(1)), (F(3), F(-2)), (F(-1, 4), F(5, 3))]
FAMS = [[[F(2), F(1, 3), F(-1)], [F(0), F(5, 7), F(4)], [F(-1), F(3), F(1, 2)]],
        [[F(1), F(1), F(0)], [F(-2), F(3), F(1, 5)], [F(4), F(0), F(-3)]]]
FROZEN = (F(2), F(3), F(1, 7))


def _module():
    return premise("standard-model.family-no-go-vev-cannot-separate")["module"]


class Span:
    def __init__(self, M):
        self.M, self.piv = M, []

    def reduce(self, v):
        M = self.M
        for key, pv in self.piv:
            x = v.get(key)
            if x:
                v = M["madd"](v, M["msc"](-x, pv))
        return v

    def add(self, v):
        v = self.reduce(v)
        if not v:
            return False
        key = next(iter(v))
        self.piv.append((key, self.M["msc"](1 / v[key], v)))
        return True


def closure(M, gs):
    sp = Span(M)
    sp.add(M["ONE"])
    basis = [M["ONE"]]
    i = 0
    while i < len(basis):
        for g in gs:
            Y = M["mm"](basis[i], g)
            if Y and sp.add(Y):
                basis.append(Y)
        i += 1
    return basis


def singlets(M, ops):
    imgs = []
    for X in ops:
        out = {}
        for gi, g in enumerate(M["SU3"]):
            for k, x in M["comm"](g, X).items():
                out[(gi,) + k] = x
        imgs.append(out)
    _, ker = M["kernel"](imgs)
    return [M["madd"](*[M["msc"](x, ops[i]) for i, x in c.items()]) for c in ker]


def frozen_gens(M, a, b, lam):
    I = M["madd"](M["msc"](a, M["V"][0]), M["msc"](b, M["W"][0]))
    c4 = M["madd"](M["msc"](-1, M["W"][3]), M["msc"](lam, M["V"][3]))
    return [I, c4, M["msc"](-1, M["W"][4])]


def check_rung_plane_vector_entries():
    M = _module()
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for a, b in RUNG_PLANE:
        c = M["madd"](M["msc"](a, M["V"][3]), M["msc"](b, M["W"][3]))
        f = M["form"](c)
        cl = M["clebsch"](f)
        ok = ok and M["meq"](f, M["ftr"](f))
        want = {}
        if a:
            want.update({("L", "nuc"): {abs(a)}, ("Q", "uc"): {abs(a)}})
        if b:
            want.update({("L", "ec"): {abs(b)}, ("Q", "dc"): {abs(b)}})
        ok = ok and {k: {abs(x) for x in v} for k, v in cl.items()} == want
        # one lepton pair and three colour pairs per rung vector, both orders: 8 entries per nonzero coefficient
        ok = ok and len(f) == 8 * ((a != 0) + (b != 0))
    # Signed entries by hand. v_4 e_23 (23 = slots 1, 2, 3, 5) is (-1)^3 e_31 and B(e_0, e_31) = +1, so
    # Y_{v4}(e_0, e_23) = -1 (nu^c with L); w_4 e_9 = (-1)^1 e_1 and the B-sign of e_30 is +1 (4 slots,
    # (-1)^6, and the permutation [1,2,3,4,0] has 4 inversions), so Y_{w4}(e_30, e_9) = -1 (e^c with L).
    fv, fw = M["form"](M["V"][3]), M["form"](M["W"][3])
    ok = ok and fv.get((0, 23)) == -1 and fw.get((30, 9)) == -1
    ok = ok and M["clebsch"](fv) == {("L", "nuc"): {-1}, ("Q", "uc"): {-1, 1}}
    ok = ok and M["clebsch"](fw) == {("L", "ec"): {1}, ("Q", "dc"): {-1, 1}}
    GA.check("a v4 + b w4: |a| on (L,nu^c),(Q,u^c), |b| on (L,e^c),(Q,d^c): the relations of one 10", ok)
    return ok


def check_family_matrix_cannot_split():
    M = _module()
    premise("standard-model.family-no-go-vev-cannot-separate")
    premise("standard-model.hyp-s-slot-statistics")

    def inv3(A):
        P = [[sum(A[i][k] * A[j][k] for k in range(3)) for j in range(3)] for i in range(3)]
        t = P[0][0] + P[1][1] + P[2][2]
        m2 = sum(P[i][i] * P[j][j] - P[i][j] * P[j][i] for i, j in ((0, 1), (0, 2), (1, 2)))
        d = (P[0][0] * (P[1][1] * P[2][2] - P[1][2] * P[2][1]) - P[0][1] * (P[1][0] * P[2][2] - P[1][2] * P[2][0])
             + P[0][2] * (P[1][0] * P[2][1] - P[1][1] * P[2][0]))
        return (t, m2, d)

    def sc(c, A):
        return [[c * x for x in r] for r in A]

    cl = M["clebsch"](M["form"](M["W"][3]))
    cg = M["clebsch"](M["form"](M["mm"](M["W"][3], M["BL"], M["CHI"])))
    ok = cg[("L", "ec")] == {F(-1)} and cg[("Q", "dc")] == {F(1, 3), F(-1, 3)}
    for Fm in FAMS:
        ok = ok and all(inv3(sc(ye, Fm)) == inv3(sc(yd, Fm)) for ye in cl[("L", "ec")] for yd in cl[("Q", "dc")])
        ok = ok and inv3(sc(F(-1), Fm)) != inv3(sc(F(1, 3), Fm))
    GA.check("10 vev with any family matrix: m_e and m_d spectra identical; the 126 entries would differ", ok)
    return ok


def check_frozen_point_algebra_eight():
    M = _module()
    premise("standard-model.no-go-frozen-point-lifts-do")
    gs = frozen_gens(M, *FROZEN)
    alg = closure(M, gs)
    ok = len(alg) == 8
    sing = singlets(M, alg)
    ok = ok and len(sing) == 4
    rungvec = [M["V"][3], M["V"][4], M["W"][3], M["W"][4]]
    oddpart = [{k: x for k, x in X.items() if (M["ntot"](k[0]) + M["ntot"](k[1])) % 2} for X in sing]
    ok = ok and M["rank"](oddpart) == 2 and M["rank"](oddpart + rungvec) == 4
    GA.check("frozen point and lifts: 8-dim algebra, colour singlets 4-dim, odd singlets inside the 10", ok)
    return ok


def check_bracket_algebra_thirty_two():
    M = _module()
    premise("standard-model.bracket-composite-lands")
    premise("standard-model.hyp-s-slot-statistics")
    mm, madd, msc, rank, form, sym = M["mm"], M["madd"], M["msc"], M["rank"], M["form"], M["sym"]
    V, W = M["V"], M["W"]
    gs = frozen_gens(M, *FROZEN) + [mm(V[3], V[4]), mm(W[4], W[3])]
    alg = closure(M, gs)
    ok = len(alg) == 32
    rmons = []
    for S in (s for k in range(3) for s in combinations((3, 4), k)):
        for T in (t for k in range(3) for t in combinations((3, 4), k)):
            rmons.append(mm(M["ONE"], *([V[m] for m in S] + [W[m] for m in T])))
    sing = singlets(M, alg)
    ok = ok and len(sing) == 16 and rank(rmons) == 16 and rank(sing + rmons) == 16
    dbl = [X for X in rmons if (M["ntot"](next(iter(X))[0]) + M["ntot"](next(iter(X))[1])) % 2 == 1
           and M["op_weight"](M["HYP"], X) == F(-1, 2) and M["op_weight"](M["T3"], X) == F(-1, 2)]
    w4N5 = mm(W[3], M["NUM"][4])
    ok = ok and len(dbl) == 2 and rank(dbl + [W[3], w4N5]) == 2
    f10 = sym(form(W[3]))
    ok = ok and M["meq"](sym(form(w4N5)), msc(F(1, 2), f10))
    bv5 = mm(gs[4], V[4])
    ok = ok and M["meq"](bv5, madd(msc(-1, W[3]), w4N5)) and M["meq"](sym(form(bv5)), msc(F(-1, 2), f10))
    ok = ok and all(rank([sym(form(X)), f10]) <= 1 for X in dbl)
    GA.check("with the bracket: 32-dim algebra, singlets = rung Clifford algebra, every doublet form a multiple of the 10", ok)
    return ok
