"""synthesis.continued-wedge-boost-over-one-modular-period-is-the-dual-plane-turn: exact checks.

Cl(1,3), signature (+, -, -, -), generators 0..3, I4 = e0 e1 e2 e3, the field theory's unit i = I4
(field-theory.second-quantisation), central in the even subalgebra (field-theory.where-each-lives).
For a unit timelike plane B (B^2 = 1) the boost rotor is S(lambda) = exp(-lambda B/2); continued to complex
rapidity lambda + I4 theta it is S(lambda) R(theta), R(theta) = exp(-theta B*/2), B* = I4 B.
R at theta = m pi uses the exact half-angle table cos(m pi/2), sin(m pi/2).
(1) Duality: B* = I4 B is a unit spacelike blade (B*^2 = -1), commutes with B and with I4, commutes with the
    vectors of B and anticommutes with those of B*; powers of I4 B cycle 1, B*, -1, -B*, 1 (so the exponential
    series of -theta I4 B/2 is cos(theta/2) - B* sin(theta/2)).
(2) Sign table: R(2 pi) = -1 and R(4 pi) = 1; on every even element (spinor, left action) one modular period
    gives -psi, on every bivector and scalar (conjugation) +; a bivector built from a spinor, psi e1e2 psi~,
    returns to itself; R(pi) = -B*, whose conjugation reverses the vectors of B* and fixes those of B; on vector
    arguments the boost at rapidity i pi (cos pi, sin pi) is the dual turn composed with the total inversion.
(3) KMS at period 2 pi is blind to statistics: a CAR mode (the completed pair of Cl(1,1),
    hawking.modular-structure-completed-pair) and a CCR mode in their Gibbs states at x = e^{-2 pi w}
    both satisfy omega(a tau_{2 pi i}(a*)) = omega(a* a) (the form of (R_loc) on one mode).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S4 = (1, -1, -1, -1)
I4 = {(0, 1, 2, 3): F(1)}
COS_HALF = [F(1), F(0), F(-1), F(0)]       # cos(m pi/2), m mod 4
SIN_HALF = [F(0), F(1), F(0), F(-1)]       # sin(m pi/2), m mod 4
PERIOD = 2                                 # one modular period: theta = 2 pi


def _vec(c):
    return GA.add(*[GA.scal(F(c[i]), GA.gen(i)) for i in range(4) if c[i] != 0])


def _mul(*xs):
    out = {(): F(1)}
    for x in xs:
        out = GA.mul(out, x, S4)
    return out


def _planes():
    """Unit timelike 2-blades B = t ^ u (t timelike unit, u spacelike unit, t . u = 0) with the vectors spanning B."""
    out = []
    for (t, u) in [((1, 0, 0, 0), (0, 1, 0, 0)), ((1, 0, 0, 0), (0, 0, 1, 0)), ((1, 0, 0, 0), (0, 0, 0, 1)),
                   ((1, 0, 0, 0), (0, F(3, 5), F(4, 5), 0)),
                   ((F(5, 4), F(3, 4), 0, 0), (0, 0, 1, 0)),
                   ((F(5, 4), F(3, 4), 0, 0), (F(3, 4), F(5, 4), 0, 0))]:
        tv, uv = _vec(t), _vec(u)
        out.append((GA.mul(tv, uv, S4), tv, uv))
    return out


def _rotor(Bs, m):
    """R(m pi) = cos(m pi/2) - B* sin(m pi/2)."""
    return GA.sub(GA.sc(COS_HALF[m % 4]), GA.scal(SIN_HALF[m % 4], Bs))


def check_dual_plane_identity():
    premise("field-theory.second-quantisation")
    premise("field-theory.where-each-lives")
    ok = True
    for (B, t, u) in _planes():
        Bs = GA.mul(I4, B, S4)
        ok = ok and GA.eq(GA.mul(B, B, S4), GA.sc(1)) and GA.eq(GA.mul(Bs, Bs, S4), GA.sc(-1))
        ok = ok and all(len(k) == 2 for k in Bs) and GA.commutes(B, Bs, S4) and GA.commutes(I4, Bs, S4)
        ok = ok and GA.commutes(I4, B, S4) and GA.commutes(t, Bs, S4) and GA.commutes(u, Bs, S4)
        # a vector of the dual plane: n = B* . w for a vector w outside B
        for w in (GA.gen(1), GA.gen(2), GA.gen(3)):
            n = GA.sub(GA.mul(Bs, w, S4), GA.mul(w, Bs, S4))
            if not GA.is_zero(n):
                ok = ok and all(len(k) == 1 for k in n) and GA.anticommutes(n, Bs, S4)
        powers, p = [], GA.sc(1)
        for _ in range(5):
            powers.append(p)
            p = GA.mul(p, Bs, S4)
        ok = ok and GA.eq(powers[2], GA.sc(-1)) and GA.eq(powers[3], GA.neg(Bs)) and GA.eq(powers[4], GA.sc(1))
        # the continued exponent: (I4 B)^k = (B*)^k, since I4 commutes with B
        ok = ok and all(GA.eq(_mul(*([I4] * k + [B] * k)), powers[k]) for k in range(5))
    GA.check("I4 B is the unit dual plane B*, commuting with B; powers of I4 B cycle 1, B*, -1, -B*", ok)
    return ok


def check_sign_over_one_modular_period():
    premise("field-theory.second-quantisation")
    premise("field-theory.where-each-lives")
    premise("field-theory.boost-modes")
    premise("synthesis.boost-evolution-on-generators-is-one-unitary-group")
    premise("singularity.euclidean-rotor-where-it-lies")
    e01 = {(0, 1): F(1)}
    e10 = GA.neg(e01)
    e23 = {(2, 3): F(1)}
    # the stored continued rotor cos + i e1e0 sin, read with i = I4, is cos - e2e3 sin; and I sigma_r = e2e3
    ok = GA.eq(GA.mul(I4, e10, S4), GA.neg(e23)) and GA.eq(GA.mul(I4, e01, S4), e23)
    ms = list(range(8))
    ok = ok and len(ms) == 2 * 4                # two full rotor periods (4 pi each) of half-turn steps
    for m in ms:
        stored = GA.add(GA.sc(COS_HALF[m % 4]), GA.scal(SIN_HALF[m % 4], GA.mul(I4, e10, S4)))
        ok = ok and GA.eq(stored, _rotor(e23, m))
    evens = [{b: F(1)} for b in GA.all_blades(4) if len(b) % 2 == 0]
    bivs = [{b: F(1)} for b in GA.all_blades(4) if len(b) == 2]
    # the even subalgebra of Cl(1,3) has 8 unit basis blades, 6 of them bivectors
    ok = ok and len(evens) == 8 and len(bivs) == 6
    ok = ok and all(list(x.values()) == [F(1)] for x in evens + bivs)
    ok = ok and all(GA.commutes(I4, x, S4) for x in evens)   # even blades are exactly those commuting with I4
    ok = ok and all(len(k) == 2 for x in bivs for k in x)
    for (B, t, u) in _planes():
        Bs = GA.mul(I4, B, S4)
        R = _rotor(Bs, PERIOD)
        Rr = GA.reverse(R)
        ok = ok and GA.eq(R, GA.sc(-1)) and GA.eq(_rotor(Bs, 2 * PERIOD), GA.sc(1))
        ok = ok and GA.eq(GA.mul(R, Rr, S4), GA.sc(1))
        ok = ok and all(GA.eq(GA.mul(R, psi, S4), GA.neg(psi)) for psi in evens)
        ok = ok and all(GA.eq(_mul(R, F_, Rr), F_) for F_ in bivs)
        psi = GA.add(GA.sc(2), GA.scal(F(3), {(0, 1): F(1)}), GA.scal(F(-1), {(1, 3): F(1)}), GA.scal(F(5), I4))
        Fb = _mul(psi, {(1, 2): F(1)}, GA.reverse(psi))
        # the sample bilinear is pinned exactly, so its literals enter the asserted statement
        ok = ok and GA.eq(Fb, {(0, 1): F(-10), (0, 2): F(-12), (0, 3): F(-20), (1, 2): F(-13), (1, 3): F(30),
                               (2, 3): F(4)})
        Rpsi = GA.mul(R, psi, S4)
        ok = ok and GA.eq(_mul(Rpsi, {(1, 2): F(1)}, GA.reverse(Rpsi)), Fb) and not GA.is_zero(Fb)
        # half period: R(pi) = -B*, conjugation turns the dual plane by pi and fixes B
        H = _rotor(Bs, PERIOD // 2)
        Hr = GA.reverse(H)
        ok = ok and GA.eq(H, GA.neg(Bs))
        ok = ok and GA.eq(_mul(H, t, Hr), t) and GA.eq(_mul(H, u, Hr), u)
        # vectors of the dual plane: the commutators B* w - w B* over the four generators span exactly B*
        ns = [n for n in (GA.sub(GA.mul(Bs, w, S4), GA.mul(w, Bs, S4)) for w in map(GA.gen, range(len(S4))))
              if not GA.is_zero(n)]
        ok = ok and all(len(k) == 1 for n in ns for k in n)
        ok = ok and GA.rank_of_vectors([[n.get((k,), F(0)) for k in range(len(S4))] for n in ns]) == 2
        ok = ok and all(GA.eq(_mul(H, n, Hr), GA.neg(n)) for n in ns)
        # on vector arguments: the boost matrix continued to rapidity i pi has cosh = cos(pi) = -1 and
        # sinh = i sin(pi) = 0 on the plane B and is the identity on B*; it equals the dual turn composed with
        # the total inversion x -> -x
        ch, sh = COS_HALF[PERIOD], SIN_HALF[PERIOD]   # cos(pi), sin(pi)
        bt = GA.add(GA.scal(ch, t), GA.scal(sh, u))
        bu = GA.add(GA.scal(sh, t), GA.scal(ch, u))
        ok = ok and GA.eq(bt, GA.neg(_mul(H, t, Hr))) and GA.eq(bu, GA.neg(_mul(H, u, Hr)))
        ok = ok and GA.eq(bt, GA.neg(t)) and GA.eq(bu, GA.neg(u))
        ok = ok and all(GA.eq(n, GA.neg(_mul(H, n, Hr))) for n in ns)
    GA.check("one modular period continued with i = I4: -1 on spinors, +1 on bivectors and scalars; half period = -B*", ok)
    return ok


def check_kms_period_is_statistics_blind():
    premise("hawking.modular-structure-completed-pair")
    premise("synthesis.local-boost-temperature-is-local-regularity")
    S2 = (1, -1)
    v = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(1)))
    vs = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(1)))
    ok = GA.eq(GA.add(GA.mul(v, vs, S2), GA.mul(vs, v, S2)), GA.sc(1)) and GA.is_zero(GA.mul(v, v, S2))
    for x in (F(1, 3), F(2, 7), F(5, 11)):
        # CAR: occupied projector v* v, vacuum v v*; omega(X) = 2 <rho X>_0 (the trace of M_2(R))
        rho = GA.scal(1 / (1 + x), GA.add(GA.mul(v, vs, S2), GA.scal(x, GA.mul(vs, v, S2))))

        def om(X):
            return 2 * GA.mul(rho, X, S2).get((), F(0))
        ok = ok and om(GA.sc(1)) == 1
        # KMS at period 2 pi for the phase flow at weight w, on the monomials, is omega(v* v) = x omega(v v*)
        ok = ok and om(GA.mul(vs, v, S2)) == x * om(GA.mul(v, vs, S2))
        ok = ok and om(GA.mul(vs, v, S2)) == x / (1 + x)
        # CCR: Gibbs occupation n = x/(1 - x) (geometric series); KMS with [b, b*] = 1 is n = x(n + 1)
        n_ccr = x / (1 - x)
        ok = ok and n_ccr == x * (n_ccr + 1)
        # with the CAR, omega(v v*) = 1 - n gives n = x(1 - n); with the CCR, n = x(1 + n): both consistent
        ok = ok and (x / (1 + x)) == x * (1 - x / (1 + x)) and x / (1 + x) != n_ccr
    GA.check("one-mode Gibbs states at period 2 pi satisfy KMS for both CAR and CCR: the period does not fix statistics", ok)
    return ok
