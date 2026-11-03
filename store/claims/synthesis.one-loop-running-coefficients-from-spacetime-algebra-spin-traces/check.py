"""One-loop running coefficients from spin traces in the spacetime algebra: exact checks.

Cl(1,3), signature (+,-,-,-). A field-strength bivector F = sum_{mu<nu} F^{mu nu} g_mu g_nu; its
invariant X = F_{mu nu} F^{mu nu}. The Lorentz generator of F is a -> a . F on vectors and
psi -> F psi/2 (left multiplication) on a minimal left ideal of the even algebra, which with the unit
I4 (left multiplication, central in the even algebra) is a two-dimensional complex space: one Weyl
spinor. The spin coupling of each one-loop operator is E = 2 M(F); the spin weight is
s = 4 Re tr M(F)^2 / X.

Heat-kernel bookkeeping (Seeley-DeWitt a_2 = (1/12) Omega Omega + (1/2) E^2 on a flat background,
imported in the proof text): a field with n components, statistics sigma and determinant weight w
contributes b = (1/3) sigma w (n + 6 s) per unit index, normalised so that a complex scalar gives 1/3.

Gauge indices from explicit generators of su(2) on C^2 and su(3) on Lambda^k C^3 (Gaussian rationals),
and the content from the stored hypercharge rule Y = (3j - 2k)/6 on the (j, k) components.
Exact arithmetic only.
"""
from fractions import Fraction as Fr
from itertools import combinations

import GA
from GA import QI
from tp_premise import premise

S = (1, -1, -1, -1)
G = [GA.gen(i) for i in range(4)]
I4 = GA.mul(GA.mul(G[0], G[1], S), GA.mul(G[2], G[3], S), S)
PS = (0, 1, 2, 3)
PAIRS = list(combinations(range(4), 2))
EVEN = [b for b in GA.all_blades(4) if len(b) % 2 == 0]

F_SAMPLES = [
    {(0, 1): Fr(2), (0, 2): Fr(-1, 3), (0, 3): Fr(1, 2), (1, 2): Fr(3), (1, 3): Fr(-2, 5), (2, 3): Fr(1)},
    {(0, 1): Fr(1), (2, 3): Fr(0)},
    {(1, 2): Fr(5, 7), (0, 3): Fr(-4, 3), (1, 3): Fr(1, 9)},
]


def mul(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, S)
    return out


def sc(x):
    return x.get((), Fr(0))


def invariant_X(F):
    """F_{mu nu} F^{mu nu} = 2 sum_{mu<nu} F^{mu nu} F_{mu nu}, F_{mu nu} = S[mu] S[nu] F^{mu nu}."""
    return 2 * sum(S[a] * S[b] * c * c for (a, b), c in F.items())


def coords(x, basis_rows):
    """Coordinates of x in a basis of multivectors (exact solve on the blade components)."""
    blades = sorted({bl for v in basis_rows for bl in v} | set(x))
    n = len(basis_rows)
    rows = [[v.get(bl, Fr(0)) for v in basis_rows] for bl in blades]
    rhs = [x.get(bl, Fr(0)) for bl in blades]
    AtA = [[sum(r[i] * r[j] for r in rows) for j in range(n)] for i in range(n)]
    Atb = [sum(r[i] * b for r, b in zip(rows, rhs)) for i in range(n)]
    sol = GA.field_solve(AtA, Atb)
    recon = GA.add(*[GA.scal(c, v) for c, v in zip(sol, basis_rows)])
    if not GA.is_zero(GA.sub(recon, x)):
        raise ValueError("not in the span")
    return sol


def real_trace(op, basis_rows):
    return sum(coords(op(v), basis_rows)[i] for i, v in enumerate(basis_rows))


def weyl_ideal():
    """The minimal left ideal Cl+(1,3) P, P = (1 + g3 g0)/2: real dimension 4."""
    P = GA.scal(Fr(1, 2), GA.add({(): Fr(1)}, mul(G[3], G[0])))
    span = [mul({b: Fr(1)}, P) for b in EVEN]
    basis = []
    for v in span:
        if GA.rank_of_vectors([[w.get(bl, Fr(0)) for bl in GA.all_blades(4)] for w in basis + [v]]) > len(basis):
            basis.append(v)
    return P, basis


def check_spin_weights_from_lorentz_generator_traces():
    """s = 4 Re tr M(F)^2 / X: 0 for a scalar, -1 for a Weyl spinor (the minimal left ideal with the unit
    I4), -2 for the whole even algebra (a Dirac field, two Weyl ideals of one chirality with i = I4),
    -4 for a vector. The I4-complex trace of the squared spin coupling on the Weyl ideal is 2 F^2, an
    element of span{1, I4}: its scalar part renormalises the coupling, its I4 part is the parity-odd F ^ F."""
    premise("field-theory.second-quantisation")
    premise("field-theory.fock-space-maxwell-modes")
    ok = True
    P, L = weyl_ideal()
    ok &= len(L) == 4
    # the ideal is I4-stable (a complex space with the unit I4)
    ok &= all(GA.rank_of_vectors([[w.get(bl, Fr(0)) for bl in GA.all_blades(4)] for w in L + [mul(I4, v)]]) == 4
              for v in L)
    for Fc in F_SAMPLES:
        F = GA.add(*[GA.scal(c, mul(G[a], G[b])) for (a, b), c in Fc.items()])
        X = invariant_X(Fc)
        F2 = mul(F, F)
        ok &= sc(F2) == -X / 2 and set(F2) <= {(), PS}
        # vectors: M(F) a = a . F = (aF - Fa)/2
        Mv = (lambda a: GA.scal(Fr(1, 2), GA.sub(mul(a, F), mul(F, a))))
        trv = real_trace(lambda a: Mv(Mv(a)), G)
        # Weyl ideal: M(F) psi = F psi/2; complex trace = Tr_R/2 - I4 Tr_R(I4 .)/2
        Ms = (lambda psi: GA.scal(Fr(1, 2), mul(F, psi)))
        tr_re = real_trace(lambda v: Ms(Ms(v)), L) / 2
        tr_im = -real_trace(lambda v: mul(I4, Ms(Ms(v))), L) / 2
        # the whole even algebra
        EV = [{b: Fr(1)} for b in EVEN]
        tr_even_re = real_trace(lambda v: Ms(Ms(v)), EV) / 2
        if X != 0:
            ok &= 4 * trv / X == -4
            ok &= 4 * tr_re / X == -1
            ok &= 4 * tr_even_re / X == -2
        # the spin coupling E = 2 M(F) = F on the ideal: tr_C(E^2) = 2 F^2 (both parts)
        ok &= 4 * tr_re == 2 * sc(F2) and 4 * tr_im == 2 * F2.get(PS, Fr(0))
        # the I4 part is nonzero exactly when F ^ F is (a parity-odd density)
        ok &= (tr_im != 0) == (F2.get(PS, Fr(0)) != 0)
    # control: the right-multiplied action psi -> psi F/2 does not preserve the ideal for generic F
    F = GA.add(*[GA.scal(c, mul(G[a], G[b])) for (a, b), c in F_SAMPLES[0].items()])
    try:
        coords(mul(L[0], F), L)
        ok = False
    except ValueError:
        pass
    GA.check("check_spin_weights_from_lorentz_generator_traces", ok)
    return ok


def b_weight(sigma, w, n, s):
    return Fr(1, 3) * sigma * w * (n + 6 * s)


def computed_spin_weights():
    """The spin weights s = 4 Re tr M(F)^2 / X computed from the Clifford traces (generic sample F):
    scalar (M = 0 on a one-dimensional space), Weyl ideal, whole even algebra (Dirac), vectors."""
    Fc = F_SAMPLES[0]
    F = GA.add(*[GA.scal(c, mul(G[a], G[b])) for (a, b), c in Fc.items()])
    X = invariant_X(Fc)
    Mv = (lambda a: GA.scal(Fr(1, 2), GA.sub(mul(a, F), mul(F, a))))
    Ms = (lambda psi: GA.scal(Fr(1, 2), mul(F, psi)))
    P, L = weyl_ideal()
    EV = [{bl: Fr(1)} for bl in EVEN]
    return {"scalar": 4 * real_trace(lambda v: GA.scal(0, v), [{(): Fr(1)}]) / X,
            "weyl": 4 * (real_trace(lambda v: Ms(Ms(v)), L) / 2) / X,
            "dirac": 4 * (real_trace(lambda v: Ms(Ms(v)), EV) / 2) / X,
            "vector": 4 * real_trace(lambda a: Mv(Mv(a)), G) / X}


def check_b_weights_per_field_and_ghost_cancellation():
    """b-weights (1/3) sigma w (n + 6 s): complex scalar 1/3, Weyl 2/3, Dirac 4/3, real vector in the
    background Feynman gauge -10/3, Faddeev-Popov ghost pair -1/3, gauge field total -11/3, with the spin
    weights taken from the Clifford traces. The orbital part of vector plus ghosts is +1/3 (the vector alone
    +2/3, the ghosts -1/3) and the spin part -4 (Nielsen-Hughes: -(-1)^{2j}((2j)^2 - 1/3) per helicity pair)."""
    premise("field-theory.second-quantisation")
    premise("field-theory.fock-space-maxwell-modes")
    SPIN_WEIGHTS = computed_spin_weights()
    ok = SPIN_WEIGHTS == {"scalar": 0, "weyl": -1, "dirac": -2, "vector": -4}
    ok &= b_weight(1, 1, 1, SPIN_WEIGHTS["scalar"]) == Fr(1, 3)
    ok &= b_weight(-1, Fr(1, 2), 2, SPIN_WEIGHTS["weyl"]) == Fr(2, 3)
    ok &= b_weight(-1, Fr(1, 2), 4, SPIN_WEIGHTS["dirac"]) == Fr(4, 3)
    vec = b_weight(1, Fr(1, 2), 4, SPIN_WEIGHTS["vector"])
    ghost = b_weight(-1, 1, 1, SPIN_WEIGHTS["scalar"])
    ok &= vec == Fr(-10, 3) and ghost == Fr(-1, 3) and vec + ghost == Fr(-11, 3)
    # orbital part of vector plus ghosts: 4 real components (w = 1/2) minus 2 real ghost components
    orbital = Fr(1, 3) * (Fr(1, 2) * 4 - 1)
    para = Fr(1, 3) * Fr(1, 2) * 6 * SPIN_WEIGHTS["vector"]
    ok &= orbital == Fr(1, 3) and para == -4 and orbital + para == Fr(-11, 3)
    # Nielsen-Hughes: per helicity pair, -( (-1)^{2j} ((2j)^2 - 1/3) ) for j = 0, 1/2, 1
    nh = {0: Fr(1, 3), 1: Fr(2, 3), 2: Fr(-11, 3)}    # key 2j
    for twoj, val in nh.items():
        ok &= -((-1) ** twoj) * (Fr(twoj * twoj) - Fr(1, 3)) == val
    # a Dirac field is two Weyl fields
    ok &= b_weight(-1, Fr(1, 2), 4, SPIN_WEIGHTS["dirac"]) == 2 * b_weight(-1, Fr(1, 2), 2, SPIN_WEIGHTS["weyl"])
    GA.check("check_b_weights_per_field_and_ghost_cancellation", ok)
    return ok


# ---------------------------------------------------------------- gauge indices
Z, ONE = QI(0), QI(1)


def mzero(n):
    return [[Z] * n for _ in range(n)]


def mmul(A, B):
    n = len(A)
    return [[sum((A[r][t] * B[t][c] for t in range(n)), Z) for c in range(n)] for r in range(n)]


def msub(A, B):
    return [[A[r][c] - B[r][c] for c in range(len(A))] for r in range(len(A))]


def mtr(A):
    return sum((A[r][r] for r in range(len(A))), Z)


def gellmann(N):
    """Hermitian generators t^a of su(N), tr(t^a t^b) = delta/2, as matrices over Q(i) (diagonal ones
    with rational entries scaled to the same norm)."""
    gens = []
    for i, j in combinations(range(N), 2):
        A = mzero(N)
        A[i][j], A[j][i] = QI(Fr(1, 2)), QI(Fr(1, 2))
        gens.append(A)
        B = mzero(N)
        B[i][j], B[j][i] = QI(0, Fr(-1, 2)), QI(0, Fr(1, 2))
        gens.append(B)
    diags = []
    for k in range(1, N):
        D = mzero(N)
        for r in range(k):
            D[r][r] = QI(1)
        D[k][k] = QI(-k)
        diags.append(D)
    return gens, diags


def index_of(gens, diags, rep):
    """T(rep) from tr(rep(t)^2)/tr(t^2) * 1/2 on off-diagonal generators, and the same ratio on the
    (unnormalised) diagonal ones: returns the set of ratios (one value if the rep is irreducible)."""
    vals = set()
    for t in gens + diags:
        ratio = mtr(mmul(rep(t), rep(t))) / mtr(mmul(t, t)) * QI(Fr(1, 2))
        vals.add((ratio.re, ratio.im))
    return vals


def wedge_rep(N, k):
    """The derivation action of an N x N matrix on Lambda^k C^N."""
    basis = list(combinations(range(N), k))
    pos = {b: i for i, b in enumerate(basis)}

    def rep(t):
        R = mzero(len(basis))
        for col, b in enumerate(basis):
            for slot, i in enumerate(b):
                for j in range(N):
                    if t[j][i] == Z:
                        continue
                    nb = list(b)
                    nb[slot] = j
                    if len(set(nb)) < k:
                        continue
                    srt = sorted(nb)
                    sign = 1
                    for a in range(k):
                        for c in range(a + 1, k):
                            if nb[a] > nb[c]:
                                sign = -sign
                    R[pos[tuple(srt)]][col] = R[pos[tuple(srt)]][col] + QI(sign) * t[j][i]
        return R
    return rep


def adjoint_index(N):
    gens, diags = gellmann(N)
    # orthonormalise the diagonal generators against tr(t t') = delta/2 is not needed for the Casimir:
    # C2(adj) delta^{ab} = sum_{c,d} f^{acd} f^{bcd} with f from [t^a, t^b] = i f^{abc} t^c on the
    # off-diagonal generators and the Killing form: tr_adj(ad t ad t) = 2 N tr(t t) for hermitian t.
    out = set()
    allg = gens + diags
    for t in allg:
        # ad t on the span of all generators, in coordinates: tr(ad_t^2) = sum over a basis of tr(...)
        def ad(x):
            return msub(mmul(t, x), mmul(x, t))
        # coordinates via the trace form on the (non-orthonormal) basis: Gram matrix
        n = len(allg)
        gram = [[mtr(mmul(allg[a], allg[b])) for b in range(n)] for a in range(n)]
        trace = Z
        for a in range(n):
            y = ad(ad(allg[a]))
            rhs = [mtr(mmul(allg[b], y)) for b in range(n)]
            coeffs = GA.field_solve(gram, rhs)
            trace = trace + coeffs[a]
        val = trace / mtr(mmul(t, t)) * QI(Fr(1, 2))
        out.add((val.re, val.im))
    return out


def check_gauge_indices_of_the_derived_algebra():
    """T = 1/2 for su(2) on C^2 and for su(3) on C^3 and Lambda^2 C^3, T = 0 on Lambda^0 and Lambda^3;
    C2(adj) = 2 for su(2) and 3 for su(3) (ad^2 traced against the trace form)."""
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    ok = True
    for N in (2, 3):
        gens, diags = gellmann(N)
        for k in range(N + 1):
            vals = index_of(gens, diags, wedge_rep(N, k))
            expect = {(Fr(0), Fr(0))} if k in (0, N) else {(Fr(1, 2), Fr(0))}
            ok &= vals == expect
        ok &= adjoint_index(N) == {(Fr(N), Fr(0))}
    # su(2) in Cl(3,0): bivectors B act on the even algebra (with the central unit e1e2e3, a doublet) by
    # left multiplication and on the bivectors by commutators; tr_adj(ad_B^2)/tr_C(L_B^2) = C2/T = 2/(1/2)
    s3 = (1, 1, 1)
    E3 = [GA.gen(i) for i in range(3)]
    I3 = GA.mul(GA.mul(E3[0], E3[1], s3), E3[2], s3)
    ok &= GA.eq(GA.mul(I3, I3, s3), {(): Fr(-1)}) and all(GA.commutes(I3, e, s3) for e in E3)
    biv = [GA.mul(E3[a], E3[b], s3) for a, b in combinations(range(3), 2)]
    even3 = [{(): Fr(1)}] + biv
    for B in biv + [GA.add(biv[0], GA.scal(Fr(2), biv[2]))]:
        left = sum(GA.mul(B, GA.mul(B, v, s3), s3).get(next(iter(v)), Fr(0)) for v in even3)
        ad = (lambda X: GA.sub(GA.mul(B, X, s3), GA.mul(X, B, s3)))
        adj = sum(ad(ad(v)).get(next(iter(v)), Fr(0)) for v in biv)
        ok &= left != 0 and adj / (left / 2) == 4
    GA.check("check_gauge_indices_of_the_derived_algebra", ok)
    return ok


# ---------------------------------------------------------------- the derived content
def content_one_generation():
    """Left-handed Weyl multiplets (dim2, k, Y) from the stored rule: component (j, k) has
    Y = (3j - 2k)/6; the doublets are the even components (1, 1), (1, 3); the singlets are (0, k), the
    odd k conjugated (Y -> -Y, Lambda^k -> Lambda^{3-k})."""
    out = []
    for k in (1, 3):
        out.append((2, k, Fr(3 - 2 * k, 6)))
    for k in range(4):
        Y = Fr(-2 * k, 6)
        if k % 2:
            out.append((1, 3 - k, -Y))
        else:
            out.append((1, k, Y))
    return out


def colour_index(k):
    gens, diags = gellmann(3)
    v = index_of(gens, diags, wedge_rep(3, k))
    return next(iter(v))[0]


def colour_dim(k):
    return [1, 3, 3, 1][k]


def b_coefficients(n_g, n_h, sw):
    weyl, scal = b_weight(-1, Fr(1, 2), 2, sw["weyl"]), b_weight(1, 1, 1, sw["scalar"])
    gauge = b_weight(1, Fr(1, 2), 4, sw["vector"]) + b_weight(-1, 1, 1, sw["scalar"])
    gen = content_one_generation()
    b3 = gauge * 3 + weyl * n_g * sum(d2 * colour_index(k) for d2, k, Y in gen)
    b2 = gauge * 2 + weyl * n_g * sum(colour_dim(k) * Fr(1, 2) for d2, k, Y in gen if d2 == 2) \
        + scal * n_h * Fr(1, 2)
    b1 = Fr(3, 5) * (weyl * n_g * sum(d2 * colour_dim(k) * Y * Y for d2, k, Y in gen)
                     + scal * n_h * 2 * Fr(1, 2) ** 2)
    return b1, b2, b3


def check_running_coefficients_of_the_derived_content():
    """With n_g generations of the derived content and n_h complex doublets of hypercharge 1/2:
    b1 = 4 n_g/3 + n_h/10, b2 = -22/3 + 4 n_g/3 + n_h/6, b3 = -11 + 4 n_g/3; at (3, 1) this is
    (41/10, -19/6, -7), the imported values; b2 < 0 iff 8 n_g + n_h < 44 and b3 < 0 iff n_g <= 8."""
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("standard-model.imported-one-loop-running-trace-ratio")
    premise("field-theory.second-quantisation")
    premise("field-theory.fock-space-maxwell-modes")
    sw = computed_spin_weights()
    gen = content_one_generation()
    ok = sorted(gen) == sorted([(2, 1, Fr(1, 6)), (2, 3, Fr(-1, 2)), (1, 0, Fr(0)), (1, 2, Fr(1, 3)),
                                (1, 2, Fr(-2, 3)), (1, 0, Fr(1))])
    # anomaly-free (cubic and mixed gravitational) as a consistency control on the listing
    ok &= sum(d2 * colour_dim(k) * Y ** 3 for d2, k, Y in gen) == 0
    ok &= sum(d2 * colour_dim(k) * Y for d2, k, Y in gen) == 0
    ok &= b_coefficients(3, 1, sw) == (Fr(41, 10), Fr(-19, 6), Fr(-7))
    ok &= b_coefficients(3, 2, sw) == (Fr(21, 5), Fr(-3), Fr(-7))
    for n_g in range(0, 10):
        for n_h in range(0, 5):
            b1, b2, b3 = b_coefficients(n_g, n_h, sw)
            ok &= b1 == Fr(4 * n_g, 3) + Fr(n_h, 10)
            ok &= b2 == Fr(-22, 3) + Fr(4 * n_g, 3) + Fr(n_h, 6)
            ok &= b3 == -11 + Fr(4 * n_g, 3)
            ok &= (b2 < 0) == (8 * n_g + n_h < 44) and (b3 < 0) == (n_g <= 8)
    # the minimal supersymmetric listing is not reproduced by this content (control)
    ok &= b_coefficients(3, 2, sw) != (Fr(33, 5), Fr(1), Fr(-3))
    # at three generations both non-abelian factors are asymptotically free exactly for n_h <= 19
    ok &= [n for n in range(0, 30) if b_coefficients(3, n, sw)[1] < 0] == list(range(0, 20))
    GA.check("check_running_coefficients_of_the_derived_content", ok)
    return ok
