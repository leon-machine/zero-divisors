"""singularity.non-removability-invariant-argument: exact checks in Gauge Theory Gravity.

Cl(1,3) in GA.py, signature (+,-,-,-). The store's curvature operator calR of the Schwarzschild field
is computed from the PG gauge fields (hb, Omega) by the engine exported by
singularity.solution-where-divergence-lies, at six rational points (horizon included).
(1) K = R_abcd R^abcd, computed as 2 sum_{m,n} <calR(gamma_m ^ gamma_n) calR(gamma^n ^ gamma^m)> from
    the gauge-field curvature, equals 48 M^2/r^6 at every sample point; the eigenvalue form
    4 (2 (2M/r^3)^2 + 4 (M/r^3)^2) = 48 M^2/r^6 holds as a rational-function identity in r; and
    K r^6 = 48 M^2 is constant, so K is unbounded as r -> 0; recomputed from the gauge fields at
    r/4 (beta doubled), K is multiplied by 4^6 = 4096.
(2) Rotation-gauge invariance: for rotors R (boosts 5/4 + 3/4 B with B^2 = 1, rotations 3/5 + 4/5 B with
    B^2 = -1, and products, with R R~ = 1 checked), the transformed operator B -> R calR(R~ B R) R~ has
    the same K, with a different rotor at each sample point (an r-dependent gauge transformation is
    pointwise conjugation); the operator is moved exactly by the rotors that do not commute with
    sigma_r. Position-gauge displacements act by pullback, which relocates K and is not tested
    beyond the identity K r^6 = 48 M^2.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
ETA = [1, -1, -1, -1]


def bl(a, b):
    return GA.mul(GA.gen(a), GA.gen(b), S13)


def wedge(a, b):
    return GA.scal(F(1, 2), GA.sub(GA.mul(a, b, S13), GA.mul(b, a, S13)))


def kretschmann(op):
    tot = F(0)
    for m in range(4):
        for n in range(4):
            if m == n:
                continue
            A = op(wedge(GA.gen(m), GA.gen(n)))
            Bv = op(wedge(GA.scal(F(ETA[n]), GA.gen(n)), GA.scal(F(ETA[m]), GA.gen(m))))
            tot += GA.mul(A, Bv, S13).get((), F(0))
    return 2 * tot


ROTORS = [GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), bl(0, 1))),
          GA.add(GA.sc(F(3, 5)), GA.scal(F(4, 5), bl(2, 3))),
          GA.add(GA.sc(F(5, 3)), GA.scal(F(4, 3), bl(0, 2))),
          GA.add(GA.sc(F(12, 13)), GA.scal(F(5, 13), bl(1, 3)))]


def check_kretschmann_from_gauge_curvature():
    ex = premise("singularity.solution-where-divergence-lies")
    for M, beta, s, c in ex["POINTS"]:
        fld = ex["pg_field"](M, beta, s, c)
        r = fld["r"]
        Rc = ex["curvature"](fld)
        K = kretschmann(lambda B: ex["apply_op"](Rc, B))
        assert K == 48 * M ** 2 / r ** 6
        assert K * r ** 6 == 48 * M ** 2
        # doubling beta divides r by 4: the gauge-field curvature gives K multiplied by 4^6
        fld2 = ex["pg_field"](M, 2 * beta, s, c)
        assert fld2["r"] * 4 == r
        Rc2 = ex["curvature"](fld2)
        K2 = kretschmann(lambda B: ex["apply_op"](Rc2, B))
        assert K2 == 4096 * K
    rv = GA.RF.var()
    for M in (F(1), F(3, 2)):
        lr = GA.RF.const(2 * M) / (rv * rv * rv)
        lm = GA.RF.const(M) / (rv * rv * rv)
        Kf = GA.RF.const(4) * (GA.RF.const(2) * lr * lr + GA.RF.const(4) * lm * lm)
        assert Kf.eqrf(GA.RF.const(48 * M * M) / (rv * rv * rv * rv * rv * rv))
    return True


def check_rotation_gauge_invariance():
    ex = premise("singularity.solution-where-divergence-lies")
    rots = ROTORS + [GA.mul(ROTORS[0], ROTORS[1], S13), GA.mul(ROTORS[2], ROTORS[3], S13)]
    for R in rots:
        assert GA.eq(GA.mul(R, GA.reverse(R), S13), GA.sc(1))
    for i, (M, beta, s, c) in enumerate(ex["POINTS"]):
        fld = ex["pg_field"](M, beta, s, c)
        r = fld["r"]
        Rc = ex["curvature"](fld)
        R = rots[i % len(rots)]
        Rt = GA.reverse(R)

        def op(B):
            return GA.mul(GA.mul(R, ex["apply_op"](Rc, GA.mul(GA.mul(Rt, B, S13), R, S13)), S13), Rt, S13)
        moved = any(not GA.eq(op(bl(a, b)), ex["apply_op"](Rc, bl(a, b)))
                    for a in range(4) for b in range(a + 1, 4))
        # a rotor that does not commute with sigma_r moves the operator
        assert moved == (not GA.commutes(R, ex["SIG_R"], S13))
        assert kretschmann(op) == 48 * M ** 2 / r ** 6
    return True
