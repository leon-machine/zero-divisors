"""synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays: exact checks in Cl(1,3).

Spacetime algebra Cl(1,3): gamma_0^2 = +1, gamma_i^2 = -1 (indices 0..3). Spinors are even
multivectors psi in Cl+(1,3) (real dimension 8); rotors act by left multiplication. The horizon's
null plane is N_k = {x : x.k = 0}, generators along k = gamma_0 + gamma_3, with the second null
direction m = gamma_0 - gamma_3 (k.m = 2), boost bivector B = gamma_3 gamma_0 (B^2 = 1,
e^{B l/2} k e^{-B l/2} = e^l k) and transverse rotation bivector J = gamma_1 gamma_2 = -I B.
Lambda(a) = a gamma_0 / (2 a_0): Lambda(k) = (1 + B)/2, Lambda(m) = (1 - B)/2.

(i)   the flux of the Dirac current J_psi = psi gamma_0 psi~ through N_k is
      J_psi . k = 2 |Lambda(m) psi|^2 (Euclidean norm in the blade basis): it vanishes identically on
      the image of Lambda(k) and is positive definite on the image of Lambda(m) = ker L_m, the
      (-1)-eigenspace of L_B, real dimension 4: the canonical part on N_k (and symmetrically the
      flux through N_m is carried by Lambda(k));
(i')  the covariant boost B_l = cosh(l/2) + sinh(l/2) B acts on the values of the canonical part by
      e^{-l/2}, and the transport u -> e^{-l} u of the affine parameter multiplies the delta kernel
      by e^l: the anticommutator factor is 1 on Lambda(m) (the unitary dilation of weight 1/2, the
      carrier's boost at l = -kappa t) and e^{2l} on Lambda(k);
(ii)  chirality G psi = I psi I sigma_3 squares to 1, commutes with every left multiplication and
      with both units, and splits the canonical part 2 + 2: one complex channel per chirality;
(iii) on the canonical part L_J = -G i_H (Hestenes' unit i_H = R_{I sigma_3}) and L_J = +L_I: helicity
      about the generator direction k is minus the chirality (chirality about m); the opposite
      signs hold on the image of Lambda(k), and neither identity holds on all of Cl+(1,3);
(iv)  a Weyl spinor meets the canonical part in one complex channel, a Dirac (Hestenes) spinor in two;
(v)   vector and bivector fields carry integer boost weights under conjugation;
(vi)  count: two canonical arrays per Dirac species, one per Weyl field, (1/2) ln 2 each at (Q) v3.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
EVEN = [(), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2, 3)]


def g(i):
    return GA.gen(i)


def m(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def vec(x):
    return [x.get(b, F(0)) for b in EVEN]


def unvec(v):
    return {b: F(c) for b, c in zip(EVEN, v) if c != 0}


def matrix(op):
    """Columns: op applied to each even basis blade."""
    cols = [vec(op({b: F(1)})) for b in EVEN]
    return [[cols[j][i] for j in range(8)] for i in range(8)]


def ident():
    return [[F(1) if i == j else F(0) for j in range(8)] for i in range(8)]


def lin(a, A, b, Bm):
    return [[a * A[i][j] + b * Bm[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def rank(M):
    return GA.mat_rank(GA.frac_matrix(M))


K = GA.add(g(0), g(3))
B = m(g(3), g(0))
J = m(g(1), g(2))
I4 = m(g(0), g(1), g(2), g(3))
S3 = m(g(3), g(0))
IS3 = m(I4, S3)

LB = matrix(lambda x: GA.mul(B, x, SQ))
LJ = matrix(lambda x: GA.mul(J, x, SQ))
LI = matrix(lambda x: GA.mul(I4, x, SQ))
RI = matrix(lambda x: GA.mul(x, IS3, SQ))
G5 = matrix(lambda x: GA.mul(GA.mul(I4, x, SQ), IS3, SQ))


def lk_full():
    """L_k maps even to odd: matrix with rows over all 16 blades."""
    blades = GA.all_blades(4)
    cols = []
    for b in EVEN:
        y = GA.mul(K, {b: F(1)}, SQ)
        cols.append([y.get(bb, F(0)) for bb in blades])
    return [[cols[j][i] for j in range(8)] for i in range(len(blades))]


def kernel_dim(M):
    return len(M[0]) - rank(M)


def stack(*Ms):
    out = []
    for M in Ms:
        out.extend(M)
    return out


M = GA.sub(g(0), g(3))
E8 = ident()
PK = lin(F(1, 2), E8, F(1, 2), LB)          # Lambda(k) = (1 + B)/2, image ker L_k
PM = lin(F(1, 2), E8, F(-1, 2), LB)         # Lambda(m) = (1 - B)/2, image ker L_m: canonical on N_k
ZERO = lin(F(0), E8, F(0), E8)


def transpose(A):
    return [list(r) for r in zip(*A)]


def flux_gram(a):
    """Gram matrix of the quadratic form psi -> <psi gamma_0 psi~ a>_0 on the even basis."""
    def q(psi):
        return GA.mul(GA.mul(GA.mul(psi, g(0), SQ), GA.reverse(psi), SQ), a, SQ).get((), F(0))
    bas = [{b: F(1)} for b in EVEN]
    return [[(q(GA.add(x, y)) - q(x) - q(y)) / 2 for y in bas] for x in bas]


def canonical():
    """Kernel equations of the canonical part on N_k: (L_B + 1) psi = 0."""
    return lin(F(1), LB, F(1), E8)


def check_canonical_part_is_lambda_m():
    premise("field-theory.second-quantisation")
    premise("synthesis.canonical-part-of-a-spinor-on-a-null-plane")
    ok = GA.mat_eq(GA.mat_mul(LB, LB), E8)
    # projectors: Lambda(k) = k gamma_0 / 2 = (1 + B)/2, Lambda(m) = m gamma_0 / 2 = (1 - B)/2
    ok = ok and GA.eq(GA.scal(F(1, 2), m(K, g(0))), GA.scal(F(1, 2), GA.add(GA.sc(1), B)))
    ok = ok and GA.eq(GA.scal(F(1, 2), m(M, g(0))), GA.scal(F(1, 2), GA.sub(GA.sc(1), B)))
    # flux through N_k: J.k = 2 |Lambda(m) psi|^2, so zero on Lambda(k) and rank 4 on Lambda(m)
    Gk = flux_gram(K)
    ok = ok and GA.mat_eq(Gk, lin(F(2), GA.mat_mul(transpose(PM), PM), F(0), E8))
    ok = ok and GA.mat_eq(GA.mat_mul(GA.mat_mul(transpose(PK), Gk), PK), ZERO)
    ok = ok and rank(GA.mat_mul(GA.mat_mul(transpose(PM), Gk), PM)) == 4
    # and symmetrically the flux through N_m is carried by Lambda(k)
    Gm = flux_gram(M)
    ok = ok and GA.mat_eq(Gm, lin(F(2), GA.mat_mul(transpose(PK), PK), F(0), E8))
    # the canonical part is ker L_m, the (-1)-eigenspace of L_B, real dimension 4
    ok = ok and kernel_dim(canonical()) == 4
    LM = []
    for b in EVEN:
        y = GA.mul(M, {b: F(1)}, SQ)
        LM.append([y.get(bb, F(0)) for bb in GA.all_blades(4)])
    LM = transpose(LM)
    ok = ok and kernel_dim(LM) == 4 and kernel_dim(stack(LM, canonical())) == 4
    GA.check("(i) the flux J.k through N_k is 2|Lambda(m) psi|^2: the canonical part on N_k is the "
             "image of Lambda(m) = (1 - B)/2, real dimension 4; Lambda(k) carries no flux there", ok)
    return ok


def check_boost_weight_of_canonical_part():
    premise("synthesis.positive-null-energy-gives-r-premises")
    premise("field-theory.second-quantisation")
    c, s = F(5, 4), F(3, 4)                     # e^{l/2} = c + s = 2
    R = GA.add(GA.sc(c), GA.scal(s, B))
    ok = GA.eq(GA.mul(R, GA.reverse(R), SQ), GA.sc(1))
    ok = ok and GA.eq(GA.mul(GA.mul(R, K, SQ), GA.reverse(R), SQ), GA.scal(4, K))   # e^l k
    LR = matrix(lambda x: GA.mul(R, x, SQ))
    # value factors: e^{-l/2} = 1/2 on Lambda(m), e^{l/2} = 2 on Lambda(k)
    ok = ok and GA.mat_eq(GA.mat_mul(LR, PM), lin(F(1, 2), PM, F(0), E8))
    ok = ok and GA.mat_eq(GA.mat_mul(LR, PK), lin(F(2), PK, F(0), E8))
    # transport u -> e^{-l} u of the affine parameter: delta kernel times e^{l}
    transport = (c + s) ** 2
    ok = ok and transport == 4
    # anticommutator factor = (value factor)^2 * transport: 1 on Lambda(m), e^{2l} = 16 on Lambda(k)
    ok = ok and (c - s) ** 2 * transport == 1 and (c + s) ** 2 * transport == 16
    # the carrier's boost beta_t is this flow at l = -kappa t: inverse rotor, factor e^{+l/2} on values
    LRinv = matrix(lambda x: GA.mul(GA.reverse(R), x, SQ))
    ok = ok and GA.mat_eq(GA.mat_mul(LRinv, PM), lin(F(2), PM, F(0), E8))
    GA.check("(i') the covariant boost scales canonical values by e^{-l/2}; with the transport the "
             "anticommutator is preserved on Lambda(m) (weight 1/2) and scaled by e^{2l} on Lambda(k)", ok)
    return ok


def check_chirality_splits_canonical_part():
    premise("field-theory.where-each-lives")
    premise("field-theory.second-quantisation")
    ok = GA.mat_eq(GA.mat_mul(G5, G5), E8)
    for b in EVEN:
        Lb = matrix(lambda x, b=b: GA.mul({b: F(1)}, x, SQ))
        ok = ok and GA.mat_eq(GA.mat_mul(G5, Lb), GA.mat_mul(Lb, G5))
    ok = ok and GA.mat_eq(GA.mat_mul(G5, RI), GA.mat_mul(RI, G5))
    ok = ok and GA.mat_eq(GA.mat_mul(RI, RI), lin(F(-1), E8, F(0), E8))
    ok = ok and GA.mat_eq(GA.mat_mul(LI, LI), lin(F(-1), E8, F(0), E8))
    for sgn in (1, -1):
        W = lin(F(1), G5, F(-sgn), E8)
        ok = ok and kernel_dim(W) == 4                              # a Weyl half
        ok = ok and kernel_dim(stack(canonical(), W)) == 2          # one complex channel
    GA.check("(ii), (iv) chirality is Lorentz invariant and splits the canonical part 2 + 2: a Weyl "
             "spinor has one complex canonical channel on N_k, a Hestenes (Dirac) spinor two", ok)
    return ok


def check_helicity_on_canonical_part():
    premise("field-theory.second-quantisation")
    premise("field-theory.where-each-lives")
    GR = GA.mat_mul(G5, RI)
    # on the canonical part Lambda(m): L_J = -G i_H and L_J = +L_I
    ok = GA.mat_eq(GA.mat_mul(lin(F(1), LJ, F(1), GR), PM), ZERO)
    ok = ok and GA.mat_eq(GA.mat_mul(lin(F(1), LJ, F(-1), LI), PM), ZERO)
    # the opposite signs hold on Lambda(k), and the canonical identities fail there
    ok = ok and GA.mat_eq(GA.mat_mul(lin(F(1), LJ, F(-1), GR), PK), ZERO)
    ok = ok and not GA.mat_eq(GA.mat_mul(lin(F(1), LJ, F(1), GR), PK), ZERO)
    ok = ok and GA.eq(J, GA.neg(m(I4, B)))
    ok = ok and not GA.mat_eq(LJ, LI) and not GA.mat_eq(LJ, lin(F(-1), LI, F(0), E8))
    GA.check("(iii) on the canonical part L_J = -(chirality) i_H: helicity about the generator "
             "direction k is minus the chirality; with the unit I_4, L_J = L_I there", ok)
    return ok


def check_vector_channels_have_integer_weight():
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    premise("field-theory.second-quantisation")
    c, s = F(5, 4), F(3, 4)
    R = GA.add(GA.sc(c), GA.scal(s, B))
    Rr = GA.reverse(R)

    def conj(x):
        return GA.mul(GA.mul(R, x, SQ), Rr, SQ)
    ok = GA.eq(conj(g(1)), g(1)) and GA.eq(conj(g(2)), g(2))
    ok = ok and GA.eq(conj(K), GA.scal(4, K)) and GA.eq(conj(M), GA.scal(F(1, 4), M))
    for t in (g(1), g(2)):
        kt = GA.scal(F(1, 2), GA.sub(m(K, t), m(t, K)))
        ok = ok and GA.eq(conj(kt), GA.scal(4, kt))
    # spinors: the one-sided action gives the square root on the canonical part
    psi = GA.scal(F(1, 2), GA.sub(GA.sc(1), B))
    ok = ok and GA.eq(GA.mul(R, psi, SQ), GA.scal(F(1, 2), psi))
    # one full turn in the transverse plane: rotor -1 on spinors, identity on vectors
    Rt = J
    ok = ok and GA.eq(GA.mul(Rt, Rt, SQ), GA.sc(-1))
    ok = ok and GA.eq(GA.mul(GA.mul(m(Rt, Rt), g(1), SQ), GA.reverse(m(Rt, Rt)), SQ), g(1))
    GA.check("(v) vector and bivector channels carry integer boost weights under conjugation; "
             "canonical spinor values carry the square root under the one-sided action", ok)
    return ok


def check_count_per_species():
    premise("synthesis.residue-from-mode-entropy")
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    # channels counted by the flux through N_k, the form that carries the anticommutator
    Gk = flux_gram(K)
    PW = lin(F(1, 2), E8, F(1, 2), G5)                  # one Weyl half
    dirac = rank(Gk) // 2
    weyl = rank(GA.mat_mul(GA.mat_mul(transpose(PW), Gk), PW)) // 2
    ok0 = dirac == kernel_dim(canonical()) // 2         # agrees with the canonical eigenspace
    half = F(1, 2)                                      # array entropy in units of ln 2 at (Q) v3
    ok = ok0 and dirac == 2 and weyl == 1
    ok = ok and dirac * half == 1 and weyl * half == F(1, 2)
    # per-light-ray total over fields (n_D Dirac, n_W Weyl): arrays 2 n_D + n_W, units of ln 2 half that
    for nD, nW in ((1, 0), (0, 1), (3, 2), (45, 3)):
        arrays = dirac * nD + weyl * nW
        ok = ok and arrays * half == nD + F(nW, 2)
    # residue per counted unit under the area law, in units of 1/(4 ln 2): 1/<s>
    ok = ok and 1 / (dirac * half) == 1 and 1 / (weyl * half) == 2
    GA.check("(vi) per light ray: two canonical arrays per Dirac species, one per Weyl field; "
             "(1/2) ln 2 each, so a registered unit of ln 2 is two arrays of the total", ok)
    return ok


def run():
    return all([check_canonical_part_is_lambda_m(), check_boost_weight_of_canonical_part(),
                check_chirality_splits_canonical_part(), check_helicity_on_canonical_part(),
                check_vector_channels_have_integer_weight(), check_count_per_species()])


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
