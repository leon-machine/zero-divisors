"""synthesis.canonical-part-of-a-spinor-on-a-null-plane: exact checks in Cl(1,3).

Spacetime algebra Cl(1,3): gamma_0^2 = +1, gamma_i^2 = -1 (indices 0..3). Spinors are even
multivectors psi in Cl+(1,3) (real dimension 8); rotors act by left multiplication. The null plane
N_k = {x : x.k = 0} has generators along k = gamma_0 + gamma_3; m = gamma_0 - gamma_3 is the second
null direction (k.m = 2), B = gamma_3 gamma_0 (B^2 = 1), Lambda(a) = a gamma_0 / (2 a_0).

(i)   Lambda(k) = k gamma_0/2 = (1 + B)/2 = k m/4 and Lambda(m) = m gamma_0/2 = (1 - B)/2 = m k/4 are
      complementary idempotents, self-adjoint for the Dirac adjoint (gamma_0 reverse(L) gamma_0 = L),
      with images ker L_m (the (-1)-eigenspace of L_B) and ker L_k (the (+1)-eigenspace), dimension 4;
(ii)  the flux of the Dirac current J_psi = psi gamma_0 psi~ through N_k is J_psi . k = 2 |Lambda(m) psi|^2
      (Euclidean norm in the blade basis), and through N_m it is 2 |Lambda(k) psi|^2;
(iii) L_{I_4} and Hestenes' right unit R_{I_4 sigma_3} square to -1 and commute with L_B, so each image
      is a two-dimensional complex space under either unit;
(iv)  every vector is (1/2) m (k.a) + (1/2) k (m.a) + a_perp, so k nabla has no derivative off N_k;
      k Lambda(k) = 0, k anticommutes with gamma_1, gamma_2, k psi X = k Lambda(m) psi X for every right
      multiplier X, L_k is injective on the image of Lambda(m); the linear maps Cl+(1,3) -> Cl(1,3)
      commuting with every even left multiplication are exactly the 16 right multiplications.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
EVEN = [(), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2, 3)]
ODD = [(0,), (1,), (2,), (3,), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
ALL = EVEN + ODD


def g(i):
    return GA.gen(i)


def m(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def opmat(op, dom, cod):
    """Matrix of a linear map: columns are op applied to each blade of dom, rows the blades of cod."""
    cols = [op({b: F(1)}) for b in dom]
    return [[cols[j].get(c, F(0)) for j in range(len(dom))] for c in cod]


def ident(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def lin(a, A, b, Bm):
    return [[a * A[i][j] + b * Bm[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


def rank(M):
    return GA.mat_rank(GA.frac_matrix(M))


def kernel_dim(M):
    return len(M[0]) - rank(M)


K = GA.add(g(0), g(3))
M = GA.sub(g(0), g(3))
B = m(g(3), g(0))
I4 = m(g(0), g(1), g(2), g(3))
S3 = m(g(3), g(0))
IS3 = m(I4, S3)
LAMK = GA.scal(F(1, 2), GA.add(GA.sc(1), B))
LAMM = GA.scal(F(1, 2), GA.sub(GA.sc(1), B))

E8 = ident(8)
LB = opmat(lambda x: GA.mul(B, x, SQ), EVEN, EVEN)
PK = opmat(lambda x: GA.mul(LAMK, x, SQ), EVEN, EVEN)
PM = opmat(lambda x: GA.mul(LAMM, x, SQ), EVEN, EVEN)
ZERO = lin(F(0), E8, F(0), E8)


def flux_gram(a):
    """Gram matrix of the quadratic form psi -> <psi gamma_0 psi~ a>_0 on the even basis."""
    def q(psi):
        return GA.mul(GA.mul(GA.mul(psi, g(0), SQ), GA.reverse(psi), SQ), a, SQ).get((), F(0))
    bas = [{b: F(1)} for b in EVEN]
    return [[(q(GA.add(x, y)) - q(x) - q(y)) / 2 for y in bas] for x in bas]


def check_projectors_are_complementary_dirac_self_adjoint_idempotents():
    premise("field-theory.second-quantisation")
    ok = GA.eq(GA.mul(B, B, SQ), GA.sc(1))
    # Lambda(a) = a gamma_0 / (2 a_0) at a_0 = 1, and the forms k m / 4, m k / 4
    ok = ok and GA.eq(GA.scal(F(1, 2), m(K, g(0))), LAMK) and GA.eq(GA.scal(F(1, 2), m(M, g(0))), LAMM)
    ok = ok and GA.eq(GA.scal(F(1, 4), m(K, M)), LAMK) and GA.eq(GA.scal(F(1, 4), m(M, K)), LAMM)
    # idempotent, complementary, orthogonal
    ok = ok and GA.eq(m(LAMK, LAMK), LAMK) and GA.eq(m(LAMM, LAMM), LAMM)
    ok = ok and GA.eq(GA.add(LAMK, LAMM), GA.sc(1)) and GA.is_zero(m(LAMK, LAMM)) and GA.is_zero(m(LAMM, LAMK))
    # self-adjoint for the Dirac adjoint
    for L in (LAMK, LAMM):
        ok = ok and GA.eq(m(g(0), GA.reverse(L), g(0)), L)
    # images: ker L_m = (-1)-eigenspace of L_B = image of Lambda(m), dimension 4; likewise for k
    for vec_, sign, P in ((M, -1, PM), (K, 1, PK)):
        Lv = opmat(lambda x, v=vec_: GA.mul(v, x, SQ), EVEN, ODD)
        eig = lin(F(1), LB, F(-sign), E8)
        ok = ok and kernel_dim(Lv) == 4 and kernel_dim(eig) == 4
        ok = ok and kernel_dim(Lv + eig) == 4 and rank(P) == 4
        ok = ok and GA.mat_eq(GA.mat_mul(Lv, P), [[F(0)] * 8 for _ in ODD])
        ok = ok and GA.mat_eq(GA.mat_mul(eig, P), ZERO)
    GA.check("(i) Lambda(k) = k gamma_0/2 = (1 + B)/2 = k m/4, Lambda(m) = m gamma_0/2 = (1 - B)/2 = m k/4: "
             "complementary Dirac-self-adjoint idempotents onto ker L_k and ker L_m, dimension 4 each", ok)
    return ok


def check_flux_through_the_plane_is_twice_the_norm_of_the_canonical_part():
    premise("field-theory.second-quantisation")
    Gk = flux_gram(K)
    ok = GA.mat_eq(Gk, lin(F(2), GA.mat_mul(transpose(PM), PM), F(0), E8))
    ok = ok and GA.mat_eq(GA.mat_mul(GA.mat_mul(transpose(PK), Gk), PK), ZERO)
    ok = ok and rank(GA.mat_mul(GA.mat_mul(transpose(PM), Gk), PM)) == 4
    Gm = flux_gram(M)
    ok = ok and GA.mat_eq(Gm, lin(F(2), GA.mat_mul(transpose(PK), PK), F(0), E8))
    ok = ok and GA.mat_eq(GA.mat_mul(GA.mat_mul(transpose(PM), Gm), PM), ZERO)
    # contrast: the flux through a spacelike hyperplane (normal gamma_0) is not carried by one half
    G0 = flux_gram(g(0))
    ok = ok and not GA.mat_eq(GA.mat_mul(GA.mat_mul(transpose(PK), G0), PK), ZERO)
    # J_psi . k = 2 |Lambda(m) psi|^2 on one explicit spinor psi = 1 + 2 gamma_1 gamma_2 + 3 gamma_0 gamma_3
    psi = GA.add(GA.sc(1), GA.scal(2, m(g(1), g(2))), GA.scal(3, m(g(0), g(3))))
    flux = GA.mul(GA.mul(GA.mul(psi, g(0), SQ), GA.reverse(psi), SQ), K, SQ).get((), F(0))
    lm = GA.mul(LAMM, psi, SQ)
    ok = ok and flux == 2 * sum(c * c for c in lm.values()) and flux == 20
    GA.check("(ii) the flux J.k through N_k is 2|Lambda(m) psi|^2 and J.m is 2|Lambda(k) psi|^2: "
             "zero on the image of Lambda(k), positive definite on that of Lambda(m)", ok)
    return ok


def check_canonical_part_is_two_complex_channels():
    premise("field-theory.second-quantisation")
    LI = opmat(lambda x: GA.mul(I4, x, SQ), EVEN, EVEN)
    RH = opmat(lambda x: GA.mul(x, IS3, SQ), EVEN, EVEN)
    minus = lin(F(-1), E8, F(0), E8)
    ok = GA.mat_eq(GA.mat_mul(LI, LI), minus) and GA.mat_eq(GA.mat_mul(RH, RH), minus)
    for U in (LI, RH):
        ok = ok and GA.mat_eq(GA.mat_mul(U, LB), GA.mat_mul(LB, U))
        ok = ok and GA.mat_eq(GA.mat_mul(U, PM), GA.mat_mul(PM, U))
        # the image of Lambda(m) is invariant: U Lambda(m) = Lambda(m) U Lambda(m)
        ok = ok and GA.mat_eq(GA.mat_mul(U, PM), GA.mat_mul(GA.mat_mul(PM, U), PM))
    ok = ok and rank(PM) == 4 and rank(PM) // 2 == 2
    # contrast: a transverse left unit that is not central, L_{gamma_1 gamma_3}, does not preserve the image
    LX = opmat(lambda x: GA.mul(m(g(1), g(3)), x, SQ), EVEN, EVEN)
    ok = ok and not GA.mat_eq(GA.mat_mul(LX, PM), GA.mat_mul(PM, LX))
    GA.check("(iii) L_{I_4} and the right unit R_{I_4 sigma_3} square to -1, commute with L_B and preserve "
             "the image of Lambda(m): two complex channels under either unit", ok)
    return ok


def check_mass_terms_enter_only_the_constraint():
    premise("field-theory.second-quantisation")
    ok = GA.is_zero(m(K, K)) and GA.eq(m(K, M), GA.add(GA.sc(2), GA.scal(F(2), B)))
    ok = ok and GA.dot(K, M, SQ) == 2
    for a in (g(0), g(1), g(2), g(3)):
        ka = GA.dot(K, a, SQ)
        ma = GA.dot(M, a, SQ)
        perp = GA.sub(a, GA.add(GA.scal(F(ka, 2), M), GA.scal(F(ma, 2), K)))
        ok = ok and GA.dot(K, perp, SQ) == 0 and GA.dot(M, perp, SQ) == 0
        # k times the off-plane part (1/2) k (m.a) vanishes: no derivative off N_k in k nabla
        ok = ok and GA.is_zero(m(K, GA.scal(F(ma, 2), K)))
    for j in (1, 2):
        ok = ok and GA.anticommutes(K, g(j), SQ)
    # k Lambda(k) = 0 on every even blade; L_k injective on Lambda(m) (rank 4)
    LkPk = opmat(lambda x: m(K, LAMK, x), EVEN, ODD)
    LkPm = opmat(lambda x: m(K, LAMM, x), EVEN, ODD)
    ok = ok and GA.mat_rank(LkPk) == 0 and GA.mat_rank(LkPm) == 4
    # every right multiplier X enters k psi X through Lambda(m) only
    for X in [{b: F(1)} for b in ALL]:
        R = opmat(lambda x, X=X: m(K, LAMK, x, X), EVEN, ALL)
        ok = ok and GA.mat_rank(R) == 0
    # contrast: a left multiplier does not pass: k gamma_3 Lambda(k) = -2 Lambda(k) is not zero
    ok = ok and GA.eq(m(K, g(3), LAMK), GA.scal(-2, LAMK))
    GA.check("(iv) k nabla has no derivative off N_k, k Lambda(k) = 0, and k psi X = k Lambda(m) psi X for "
             "every right multiplier X: mass terms reach only the constraint", ok)
    return ok


def check_covariant_maps_are_right_multiplications():
    premise("field-theory.second-quantisation")
    # unknown F: 16 x 8 matrix (Cl+ -> Cl), entries indexed (r, c) -> r * 8 + c.
    # F L_X = L'_X F for X in the six basis bivectors (they and 1 generate Cl+ as an algebra).
    rows = []
    for X in [{b: F(1)} for b in EVEN if len(b) == 2]:
        Le = opmat(lambda x: GA.mul(X, x, SQ), EVEN, EVEN)
        La = opmat(lambda x: GA.mul(X, x, SQ), ALL, ALL)
        for r in range(16):
            for c in range(8):
                row = [F(0)] * 128
                for t in range(8):          # (F Le)[r][c] = sum_t F[r][t] Le[t][c]
                    row[r * 8 + t] += Le[t][c]
                for s in range(16):         # (La F)[r][c] = sum_s La[r][s] F[s][c]
                    row[s * 8 + c] -= La[r][s]
                rows.append(row)
    ok = 128 - rank(rows) == 16
    # the 16 right multiplications R_Y solve it and are independent
    sols = []
    for Y in [{b: F(1)} for b in ALL]:
        Fm = opmat(lambda x, Y=Y: GA.mul(x, Y, SQ), EVEN, ALL)
        sols.append([Fm[r][c] for r in range(16) for c in range(8)])
        ok = ok and all(sum(rw[i] * sols[-1][i] for i in range(128)) == 0 for rw in rows)
    ok = ok and rank(sols) == 16
    GA.check("(iv) the linear maps Cl+(1,3) -> Cl(1,3) commuting with every even left multiplication "
             "are exactly the 16 right multiplications", ok)
    return ok


def run():
    return all([check_projectors_are_complementary_dirac_self_adjoint_idempotents(),
                check_flux_through_the_plane_is_twice_the_norm_of_the_canonical_part(),
                check_canonical_part_is_two_complex_channels(),
                check_mass_terms_enter_only_the_constraint(),
                check_covariant_maps_are_right_multiplications()])


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
