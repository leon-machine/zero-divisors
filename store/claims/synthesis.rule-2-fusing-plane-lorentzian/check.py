"""synthesis.rule-2-fusing-plane-lorentzian: exact checks.

A = Cl(1,4) on e0 (square +1), e1..e4 (square -1), omega = e0 e1 e2 e3 e4 (central in A,
omega^2 = +1), eps_pm = (1 pm omega)/2. The two Rule 2 repairs adjoin nu = e5 with
nu^2 = +1 (B_plus = Cl(2,4)) or nu^2 = -1 (B_minus = Cl(1,5)). Checks:
  (a) in each repair the elements anticommuting with e0..e4 are exactly span{nu, Omega},
      Omega = omega nu the volume element; x -> x^2 is a real quadratic form on that plane
      of signature (1,1) in both repairs; its null lines are nu eps_+ and nu eps_-, the
      off-diagonal Rule 2 matrix units (zero divisors);
  (b) e_i -> e_i, nu_plus -> nu_minus omega respects every relation of Cl(2,4), is onto
      (images span 64 dimensions), fixes A pointwise and sends Omega_plus to -nu_minus:
      vector and volume element exchange roles;
  (c) every unit x of the plane completes e0..e4 to a Clifford generating set of the whole
      algebra, of signature (2,4) if x^2 = +1 and (1,5) if x^2 = -1, and the completion's
      volume element omega x lies in the plane, orthogonal to x, with square -x^2;
  (d) conjugation by u = a eps_+ + b eps_- (a, b nonzero) fixes A pointwise and scales the
      null lines by b/a and a/b: it preserves x^2 and acts transitively on each level set.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, sc, gen, all_blades, rank_of_vectors
from tp_premise import premise

N = 6
BASE = [0, 1, 2, 3, 4]


def sq(nu_sq):
    return (1, -1, -1, -1, -1, nu_sq)


def blade(*idx):
    return {tuple(idx): F(1)}


def anticomm(x, y, s):
    return add(mul(x, y, s), mul(y, x, s)) == {}


def comm(x, y, s):
    return sub(mul(x, y, s), mul(y, x, s)) == {}


OMEGA_A = blade(0, 1, 2, 3, 4)


def eps(sign):
    return scal(F(1, 2), add(sc(1), scal(sign, OMEGA_A)))


def as_vec(x):
    return [x.get(b, F(0)) for b in all_blades(N)]


def check_fusing_plane_lorentzian():
    premise("rule2.rule-2-kaluza-klein-algebra")
    premise("rule2.imported-rule-2-matrix-units-forgotten")
    for nu_sq in (1, -1):
        s = sq(nu_sq)
        nu = gen(5)
        # omega is central in A with square +1
        assert mul(OMEGA_A, OMEGA_A, s) == sc(1)
        assert all(comm(OMEGA_A, gen(i), s) for i in BASE)
        plane = [b for b in all_blades(N)
                 if all(anticomm({b: F(1)}, gen(i), s) for i in BASE)]
        assert sorted(plane) == sorted([(5,), (0, 1, 2, 3, 4, 5)]), plane
        Om = mul(OMEGA_A, nu, s)
        assert Om == {(0, 1, 2, 3, 4, 5): F(1)}
        n2 = mul(nu, nu, s)[()]
        o2 = mul(Om, Om, s)[()]
        assert n2 == nu_sq and o2 == -nu_sq          # one positive, one negative axis
        assert anticomm(nu, Om, s)                    # orthogonal axes
        for a, b in [(F(1), F(1)), (F(1), F(-1)), (F(3), F(2)), (F(-5), F(7))]:
            x = add(scal(a, nu), scal(b, Om))
            x2 = mul(x, x, s)
            assert x2 == sc(a * a * n2 + b * b * o2)
        # null lines: nu -+ Omega = 2 nu eps_pm, squares zero, nonzero (zero divisors)
        for sign in (1, -1):
            line = mul(nu, eps(sign), s)
            assert line != {} and mul(line, line, s) == {}
            assert scal(2, line) == sub(nu, scal(sign, Om))      # 2 nu eps_pm = nu -+ Omega
        E12 = mul(eps(1), nu, s)
        E21 = mul(eps(-1), nu, s)
        assert E12 == mul(nu, eps(-1), s)
        assert mul(E12, E21, s) == scal(nu_sq, eps(1))
        assert mul(E21, E12, s) == scal(nu_sq, eps(-1))


def check_isomorphism_exchanges_vector_and_volume():
    premise("rule2.imported-rule-2-matrix-units-forgotten")
    premise("rule2.rule-2-kaluza-klein-algebra")
    sp, sm = sq(1), sq(-1)
    image = {i: gen(i) for i in BASE}
    image[5] = mul(gen(5), OMEGA_A, sm)              # phi(nu_plus) = nu_minus omega
    for i in range(N):
        for j in range(N):
            lhs = add(mul(image[i], image[j], sm), mul(image[j], image[i], sm))
            rhs = sc(2 * sp[i]) if i == j else {}
            assert lhs == rhs, (i, j)
    # phi of every basis blade, span is 64-dimensional (phi onto, hence an isomorphism)
    def phi(b):
        out = sc(1)
        for k in b:
            out = mul(out, image[k], sm)
        return out
    vecs = [as_vec(phi(b)) for b in all_blades(N)]
    assert rank_of_vectors(vecs) == 64
    assert phi((0, 1, 2, 3, 4, 5)) == scal(-1, gen(5))     # Omega_plus -> -nu_minus
    assert list(image[5].keys()) == [(0, 1, 2, 3, 4, 5)]    # nu_plus -> a grade-6 element


def check_units_complete_generating_sets():
    premise("rule2.rule-2-kaluza-klein-algebra")
    premise("synthesis.plane-commutant-even-ground")
    premise("odd-extensions.twistor-algebra")
    for nu_sq in (1, -1):
        s = sq(nu_sq)
        nu = gen(5)
        Om = mul(OMEGA_A, nu, s)
        # rational units on both level sets: (5/4, 3/4) and (3/4, 5/4) in (nu, Omega)
        for (a, b) in [(F(5, 4), F(3, 4)), (F(3, 4), F(5, 4)), (F(1), F(0)), (F(0), F(1)),
                       (F(-13, 12), F(5, 12))]:
            x = add(scal(a, nu), scal(b, Om))
            x2 = mul(x, x, s).get((), F(0))
            assert x2 in (F(1), F(-1)) and mul(x, x, s) == sc(x2)
            assert all(anticomm(x, gen(i), s) for i in BASE)
            gens = [gen(i) for i in BASE] + [x]
            prods = []
            for bl in all_blades(N):
                out = sc(1)
                for k in bl:
                    out = mul(out, gens[k], s)
                prods.append(as_vec(out))
            assert rank_of_vectors(prods) == 64
            p = sum(1 for g in gens if mul(g, g, s) == sc(1))
            assert (p, N - p) == ((2, 4) if x2 == 1 else (1, 5))
            vol = mul(OMEGA_A, x, s)
            assert all(anticomm(vol, gen(i), s) for i in BASE)
            assert anticomm(vol, x, s)
            assert mul(vol, vol, s) == sc(-x2)
            # the volume element is central in the even part of the completion
            for i in range(5):
                for j in range(i + 1, 6):
                    biv = mul(gens[i], gens[j], s)
                    assert comm(vol, biv, s)


def check_fixing_automorphisms_are_plane_boosts():
    premise("rule2.imported-rule-2-matrix-units-forgotten")
    premise("rule2.rule-2-kaluza-klein-algebra")
    for nu_sq in (1, -1):
        s = sq(nu_sq)
        nu = gen(5)
        Ep, Em = mul(nu, eps(1), s), mul(nu, eps(-1), s)
        for a, b in [(F(2), F(3)), (F(-1), F(4)), (F(5), F(-7, 2))]:
            u = add(scal(a, eps(1)), scal(b, eps(-1)))
            ui = add(scal(F(1) / a, eps(1)), scal(F(1) / b, eps(-1)))
            assert mul(u, ui, s) == sc(1)
            assert all(comm(u, gen(i), s) for i in BASE)
            assert mul(mul(u, Ep, s), ui, s) == scal(b / a, Ep)
            assert mul(mul(u, Em, s), ui, s) == scal(a / b, Em)
        # transitivity on a level set: x = p Ep + q Em has x^2 = p q c, c = nu_sq (Ep Em + Em Ep = nu_sq)
        c = add(mul(Ep, Em, s), mul(Em, Ep, s))
        assert c == sc(nu_sq)
        x = add(scal(F(2), Ep), scal(F(1, 2), Em))
        y = add(scal(F(-1, 3), Ep), scal(F(-3), Em))
        assert mul(x, x, s) == mul(y, y, s)
        t = F(-1, 6)                                    # u with b/a = t sends x to y
        u = add(eps(1), scal(t, eps(-1)))
        ui = add(eps(1), scal(F(1) / t, eps(-1)))
        assert mul(mul(u, x, s), ui, s) == y


EXPORTS = {}
