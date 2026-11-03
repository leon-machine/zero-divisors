"""singularity.curvature-gauge-field-exact-shape-decoupling: exact checks in Gauge Theory Gravity.

Cl(1,3) in GA.py, signature (+,-,-,-), sigma_r = e_r e_t = gamma_1 gamma_0, I = gamma_0 gamma_1 gamma_2
gamma_3. Bivectors are multivectors of grade 2; the six frame blades are a basis. Pi is the projection
onto span{sigma_r, I sigma_r} orthogonal for the scalar product <A B> (nondegenerate on bivectors).
The curvature operator is computed from the PG gauge fields (hb, Omega) by the engine exported by
singularity.solution-where-divergence-lies: calR(B) = -R(hb(B)) in the store sign, at six rational
points with the horizon included.
(1) The radial plane is hb-invariant: hb(e_t) ^ hb(e_r) = e_t ^ e_r for hb(a) = a - beta (a.e_t) e_r at
    beta = 0, 1/3, 1, 7/2.
(2) The two forms of the shape operator agree on every basis bivector: 1 - 3 Pi = B -> -(B + 3 sigma_r
    B sigma_r)/2; and calR(B) = -(M/r^3) S(B) on all six frame planes at every sample point, with
    calR(sigma_r) = +(2M/r^3) sigma_r and S(sigma_r) = -2 sigma_r.
(3) S^2 + S = 2 on every basis bivector; the eigenspace of -2 (kernel of S + 2) is exactly
    span{sigma_r, I sigma_r} (dimension 2), that of 1 has dimension 4, and the trace of S on the
    six-dimensional space is 0; tr(1 - 3 Pi') = 0 also for two other rank-two projections Pi', so
    trace-freeness alone carries no field equation; the scalar contraction of calR vanishes.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
PL = [(a, b) for a in range(4) for b in range(a + 1, 4)]


def bl(a, b):
    return GA.mul(GA.gen(a), GA.gen(b), S13)


def coords(B):
    return [B.get(p, F(0)) for p in PL]


def from_coords(v):
    return GA.add(*[GA.scal(v[i], {PL[i]: F(1)}) for i in range(6)])


def proj(basis):
    """Orthogonal projection (scalar product <AB>) onto span(basis)."""
    G = [[GA.mul(x, y, S13).get((), F(0)) for y in basis] for x in basis]
    det = G[0][0] * G[1][1] - G[0][1] * G[1][0]
    Gi = [[G[1][1] / det, -G[0][1] / det], [-G[1][0] / det, G[0][0] / det]]

    def P(B):
        s = [GA.mul(x, B, S13).get((), F(0)) for x in basis]
        return GA.add(*[GA.scal(sum(Gi[i][j] * s[j] for j in range(2)), basis[i]) for i in range(2)])
    return P


def matrix(op):
    cols = [coords(op({p: F(1)})) for p in PL]
    return [[cols[j][i] for j in range(6)] for i in range(6)]


SIG = bl(1, 0)
I4 = GA.mul(bl(0, 1), bl(2, 3), S13)
ISIG = GA.mul(I4, SIG, S13)
PI = proj([SIG, ISIG])


def S_proj(B):
    return GA.sub(B, GA.scal(3, PI(B)))


def S_conj(B):
    return GA.scal(F(-1, 2), GA.add(B, GA.scal(3, GA.mul(GA.mul(SIG, B, S13), SIG, S13))))


def check_radial_plane_is_hb_invariant():
    et, er = GA.gen(0), GA.gen(1)
    for beta in (F(0), F(1, 3), F(1), F(7, 2)):
        def hb(a):
            return GA.sub(a, GA.scal(beta * GA.dot(a, et, S13), er))
        x, y = hb(et), hb(er)
        w = GA.scal(F(1, 2), GA.sub(GA.mul(x, y, S13), GA.mul(y, x, S13)))
        assert GA.eq(w, bl(0, 1))
    assert GA.eq(SIG, GA.neg(bl(0, 1)))
    return True


def check_shape_operator_matches_gauge_curvature():
    ex = premise("singularity.solution-where-divergence-lies")
    for p in PL:
        B = {p: F(1)}
        assert GA.eq(S_proj(B), S_conj(B))
    assert GA.eq(S_conj(SIG), GA.scal(-2, SIG))
    for M, beta, s, c in ex["POINTS"]:
        fld = ex["pg_field"](M, beta, s, c)
        r = fld["r"]
        Rc = ex["curvature"](fld)
        for p in PL:
            B = {p: F(1)}
            assert GA.eq(ex["apply_op"](Rc, B), GA.scal(-M / r ** 3, S_conj(B)))
        assert GA.eq(ex["apply_op"](Rc, SIG), GA.scal(2 * M / r ** 3, SIG))
    return True


def check_shape_operator_spectrum():
    ex = premise("singularity.solution-where-divergence-lies")
    for p in PL:
        B = {p: F(1)}
        assert GA.eq(GA.add(S_conj(S_conj(B)), S_conj(B)), GA.scal(2, B))
    Sm = matrix(S_conj)
    shifted = [[Sm[i][j] + (2 if i == j else 0) for j in range(6)] for i in range(6)]
    ker = GA.field_kernel(shifted)
    assert len(ker) == 2
    span = [coords(SIG), coords(ISIG)]
    assert GA.rank_of_vectors(span) == 2 and GA.rank_of_vectors(span + ker) == 2
    ones = [[Sm[i][j] - (1 if i == j else 0) for j in range(6)] for i in range(6)]
    assert len(GA.field_kernel(ones)) == 4
    assert sum(Sm[i][i] for i in range(6)) == 0
    for other in ([bl(0, 2), bl(1, 3)], [bl(0, 3), GA.add(bl(2, 3), bl(1, 2))]):
        P2 = proj(other)
        T = matrix(lambda B: GA.sub(B, GA.scal(3, P2(B))))
        assert sum(T[i][i] for i in range(6)) == 0
    M, beta, s, c = ex["POINTS"][0]
    Rc = ex["curvature"](ex["pg_field"](M, beta, s, c))
    scal = sum(GA.mul(GA.scal(F(S13[b]), GA.gen(b)), ex["ricci"](Rc, b), S13).get((), F(0))
               for b in range(4))
    assert scal == 0
    return True
