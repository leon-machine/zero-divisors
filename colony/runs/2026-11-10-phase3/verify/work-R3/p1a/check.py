"""synthesis.protraction-identity-of-the-curvature-operator-from-vanishing-torsion: exact checks.

Gauge Theory Gravity on flat spacetime with the store's conventions (lib/gtg.py): a field is given by its coframe
matrix, hb^{-1}(e_mu) = g_mu, with reciprocal vectors g^mu = hb^T(e^mu); D_mu M = d_mu M + Omega(e_mu) x M;
R(e_mu ^ e_nu) the field strength; calR(B) = -R(hb(B)) the curvature operator on physical bivectors. Fields are
truncated Taylor polynomials with rational coefficients about a rational point, so every value is exact.

For a linear map M from bivectors to bivectors write
    T(c) = d_a ^ M(a ^ c)                      (the protraction, a trivector),
    C(c) = d_b ^ d_a ^ (M(a ^ b) . c)          (the cyclic trivector).

  (1) algebra, every M: C(c) = 2 T(c) - c . S with S = d_e ^ T(e), and T(c) = C(c)/2 - c . (d_e ^ C(e))/4;
  (2) every field, with torsion S^mu = D ^ g^mu:  C(g^mu)/2 = D ^ S^mu - S^nu ^ D_nu g^mu;
  (3) torsion-free fields (Omega solved from hb): T = 0;
  (4) the kernel of T: dimension d^2 (d^2 - 1)/12, inside the symmetric maps; B -> I B is symmetric and outside it;
      in Cl(1,3) the cyclic vector identity M(x ^ y) . z + M(y ^ z) . x + M(z ^ x) . y = 0 has the same solutions.
"""
from fractions import Fraction as F
import itertools
import GA
import gtg
from gtg import Jet

S13, S22, S12, S14 = GA.sig(1, 3), GA.sig(2, 2), GA.sig(1, 2), GA.sig(1, 4)
ALGEBRA_SAMPLES = ((S13, None), (S22, None), (S14, 12))      # signature, number of basis maps sampled (None: all)
MIN_NONZERO = 12
TORSION_SAMPLES = ((3, S13), (5, S12))                       # seed, signature
FREE_SEEDS = ((1, S13), (2, S13), (4, S12), (6, S22))
SCHW = (F(1), F(2), F(3, 5), F(4, 5))                        # M, r, sin, cos of the polar angle: 2M/r^3 = 1/4
DS_H, DS_E = F(1, 2), F(1)                                   # Hubble rate, value of exp(H t) at the point
KERNEL_SIGS = (S12, S13, S22, S14)


def coef(seed, k):
    return F((seed * 7919 + k * 104729) % 11 - 5)


def poly(seed, k, order, scale, d, const):
    """A polynomial with rational coefficients in the d labels, truncated at the given order, about the origin."""
    X = [Jet.var(i, F(0), d, order) for i in range(d)]
    j = Jet.const(const, d) + X[0] * 0
    for deg in range(1, order + 1):
        for combo in itertools.combinations_with_replacement(range(d), deg):
            t = Jet.const(coef(seed, k) * scale, d)
            k += 1
            for i in combo:
                t = t * X[i]
            j = j + t
    return j, k


def coframe(seed, sq, order=2):
    d = len(sq)
    TH, k = [], 0
    for a in range(d):
        row = []
        for mu in range(d):
            c0 = (F(1) if a == mu else F(0)) + coef(seed, 900 + d * a + mu) * F(1, 8)
            j, k = poly(seed, k, order, F(1, 4), d, c0)
            row.append(j)
        TH.append(row)
    return TH


def gup(fld):
    """g^mu = hb^T(e^mu) = sum_a Hi[mu][a] gamma^a, as jets."""
    HJ, sq, d = fld.hb_matrix_jet(), fld.sq, fld.d
    return [gtg.m_add(*[gtg.m_scal(HJ[mu][a] * sq[a], GA.gen(a)) for a in range(d)]) for mu in range(d)]


def cov(fld, mu, M):
    return gtg.m_add(gtg.m_d(M, mu), gtg.comm(fld.Om[mu], M, fld.sq))


def op_of_field(fld):
    Rc = fld.curvature()
    return lambda a, b: plane(Rc, a, b)


def plane(Rc, a, b):
    if a == b:
        return {}
    return Rc[(a, b)] if a < b else gtg.m_neg(Rc[(b, a)])


def protraction(M, c, sq):
    """T(c) = d_a ^ M(a ^ c) for c a frame index: sum_a gamma^a ^ M(gamma_a ^ gamma_c)."""
    d = len(sq)
    return gtg.m_add(*[gtg.outer(gtg.er(a, sq), M(a, c), sq) for a in range(d)])


def protraction_vec(M, c, sq):
    d = len(sq)
    out = {}
    for k in range(d):
        ck = c.get((k,), F(0))
        if ck:
            out = gtg.m_add(out, gtg.m_scal(ck, protraction(M, k, sq)))
    return out


def cyclic(M, c, sq):
    """C(c) = d_b ^ d_a ^ (M(a ^ b) . c) for a vector c."""
    d = len(sq)
    out = {}
    for a in range(d):
        for b in range(d):
            if a == b:
                continue
            v = gtg.bdot(M(a, b), c, sq)
            if v:
                out = gtg.m_add(out, gtg.outer(gtg.outer(gtg.er(b, sq), gtg.er(a, sq), sq), v, sq))
    return out


def contract(c, X, sq):
    """c . X for a vector c and a multivector X of one grade: the grade-lowering part of c X."""
    k = max(len(b) for b in X) if X else 0
    return gtg.grade(gtg.m_mul(c, X, sq), k - 1)


def basis_map(i, j, blades):
    """The map taking the blade j to the blade i and the other basis blades to zero."""
    def M(a, b):
        if a == b:
            return {}
        key, s = ((a, b), 1) if a < b else ((b, a), -1)
        return {blades[i]: F(s)} if key == blades[j] else {}
    return M


def check_cyclic_trivector_determines_the_protraction_for_every_bivector_map():
    """(1): on all 36 basis maps of Cl(1,3) and all 4 frame vectors (the identities are linear in the map and in c),
    and on the 36 basis maps of signature (2,2); in five dimensions on a sample of 12 basis maps."""
    for sq, sample in ALGEBRA_SAMPLES:
        d = len(sq)
        blades = gtg.bivector_blades(d)
        pairs = [(i, j) for i in range(len(blades)) for j in range(len(blades))]
        if sample:
            pairs = pairs[::len(pairs) // sample]
        nonzero = []
        for i, j in pairs:
            M = basis_map(i, j, blades)
            T = [protraction(M, c, sq) for c in range(d)]
            S = gtg.m_add(*[gtg.outer(gtg.er(c, sq), T[c], sq) for c in range(d)])
            C = [cyclic(M, GA.gen(c), sq) for c in range(d)]
            dC = gtg.m_add(*[gtg.outer(gtg.er(c, sq), C[c], sq) for c in range(d)])
            for c in range(d):
                cS = contract(GA.gen(c), S, sq) if S else {}
                GA.check("C = 2T - c.S", gtg.m_sub(C[c], gtg.m_sub(gtg.m_scal(2, T[c]), cS)) == {})
                cdC = contract(GA.gen(c), dC, sq) if dC else {}
                GA.check("T = C/2 - c.(d^C)/4",
                         gtg.m_sub(T[c], gtg.m_sub(gtg.m_scal(F(1, 2), C[c]), gtg.m_scal(F(1, 4), cdC))) == {})
                nonzero.append(bool(T[c]))
            GA.check("d ^ C = -2 S", gtg.m_add(dC, gtg.m_scal(2, S)) == {})
        GA.check("the identities are tested on maps with nonzero protraction", sum(nonzero) >= MIN_NONZERO)
    return True


def field_with_torsion(seed, sq):
    d = len(sq)
    TH = coframe(seed, sq)
    Om, k = [], 3000
    for mu in range(d):
        B = {}
        for b in gtg.bivector_blades(d):
            j, k = poly(seed, k, 1, F(1, 3), d, coef(seed, k + 17) * F(1, 2))
            B[b] = j
        Om.append(B)
    return gtg.Field(TH, None, sq, Om=Om)


def check_cyclic_trivector_is_the_covariant_curl_of_the_torsion():
    """(2): C(g^mu)/2 = D ^ S^mu - S^nu ^ D_nu g^mu on two fields with generic polynomial hb and Omega (torsion
    present), in Cl(1,3) and in three dimensions; the protraction is then nonzero (control for (3))."""
    for seed, sq in TORSION_SAMPLES:
        d = len(sq)
        fld = field_with_torsion(seed, sq)
        GA.check("the sample has torsion", not fld.torsion_free())
        g = gup(fld)
        Dg = [[cov(fld, nu, g[mu]) for mu in range(d)] for nu in range(d)]
        S = [gtg.m_add(*[gtg.outer(g[lam], Dg[lam][mu], sq) for lam in range(d)]) for mu in range(d)]
        M = op_of_field(fld)
        tor = []
        for mu in range(d):
            DS = gtg.m_add(*[gtg.outer(g[lam], cov(fld, lam, S[mu]), sq) for lam in range(d)])
            SD = gtg.m_add(*[gtg.outer(S[nu], Dg[nu][mu], sq) for nu in range(d)])
            rhs = gtg.m_val(gtg.m_add(DS, SD))
            lhs = gtg.m_scal(F(1, 2), cyclic(M, gtg.m_val(g[mu]), sq))
            GA.check("C(g^mu)/2 = D ^ S^mu - S^nu ^ D_nu g^mu", gtg.m_sub(lhs, rhs) == {})
            tor.append(bool(lhs))
        if sq == S13:
            GA.check("with torsion the cyclic trivector is not zero", any(tor))
            GA.check("with torsion the protraction is not zero", any(protraction(M, c, sq) for c in range(d)))
    return True


def check_protraction_vanishes_on_torsion_free_fields():
    """(3): Omega solved exactly from the torsion equation for two generic polynomial coframes in Cl(1,3), one in
    signature (1,2) and one in (2,2), and the stored Schwarzschild and flat-slicing de Sitter fields: T(c) = 0 and
    C(c) = 0 for every frame vector, with nonzero curvature."""
    fields = [gtg.Field(coframe(seed, sq), None, sq) for seed, sq in FREE_SEEDS]
    schw = gtg.schwarzschild_pg(*SCHW)
    ds = gtg.de_sitter_flat(DS_H, DS_E)
    fields += [schw, ds]
    for fld in fields:
        d, sq = fld.d, fld.sq
        GA.check("the field is torsion-free", fld.torsion_free())
        M = op_of_field(fld)
        GA.check("the curvature is not zero", any(v for v in fld.curvature().values()))
        for c in range(d):
            GA.check("d_a ^ calR(a ^ c) = 0", protraction(M, c, sq) == {})
            GA.check("cyclic trivector zero", cyclic(M, GA.gen(c), sq) == {})
            full = gtg.m_add(*[gtg.m_mul(gtg.er(a, sq), M(a, c), sq) for a in range(d)])
            GA.check("d_a calR(a ^ c) is the Ricci vector", full == gtg.ricci(fld.curvature(), GA.gen(c), sq))
        Rc = fld.curvature()
        GA.check("the Ricci map is symmetric",
                 all(gtg.vdot(GA.gen(a), gtg.ricci(Rc, GA.gen(b), sq), sq) == gtg.vdot(GA.gen(b), gtg.ricci(Rc, GA.gen(a), sq), sq)
                     for a in range(d) for b in range(a)))
        for a, b, c in itertools.combinations(range(d), 3):
            cyc = gtg.m_add(gtg.bdot(M(a, b), GA.gen(c), sq), gtg.bdot(M(b, c), GA.gen(a), sq),
                            gtg.bdot(M(c, a), GA.gen(b), sq))
            GA.check("calR(a ^ b) . c + cyclic = 0", cyc == {})
    # anchors in the store's sign: de Sitter has scalar curvature 4 Lambda = 12 H^2; Schwarzschild is Ricci-flat
    GA.check("de Sitter scalar curvature 12 H^2", gtg.ricci_scalar(ds.curvature(), ds.sq) == 12 * DS_H * DS_H)
    GA.check("Schwarzschild: zero Ricci vector, radial eigenvalue 2M/r^3",
             all(gtg.ricci(schw.curvature(), GA.gen(c), schw.sq) == {} for c in range(schw.d))
             and schw.curvature()[(0, 1)] == {(0, 1): F(1, 4)})
    return True


def protraction_rows(sq):
    """Rows of the linear map M -> T on the coordinates M(B_j) = sum_i m[i][j] B_i."""
    d = len(sq)
    blades = gtg.bivector_blades(d)
    n = len(blades)
    rows = {}
    for i in range(n):
        for j in range(n):
            M = basis_map(i, j, blades)
            for c in range(d):
                for bl, v in protraction(M, c, sq).items():
                    rows.setdefault((c, bl), [F(0)] * (n * n))[i * n + j] = v
    return list(rows.values()), blades


def symmetry_rows(sq, blades):
    n = len(blades)
    nrm = [gtg.sp(gtg.m_mul({b: F(1)}, {b: F(1)}, sq)) for b in blades]
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            r = [F(0)] * (n * n)
            r[i * n + j] = nrm[i]          # <B_i M(B_j)> = m[i][j] <B_i B_i>
            r[j * n + i] = -nrm[j]
            rows.append(r)
    return rows


def cyclic_rows(sq):
    """Rows of M -> M(x ^ y) . z + M(y ^ z) . x + M(z ^ x) . y on frame triples."""
    d = len(sq)
    blades = gtg.bivector_blades(d)
    n = len(blades)
    rows = {}
    for i in range(n):
        for j in range(n):
            M = basis_map(i, j, blades)
            for x, y, z in itertools.combinations(range(d), 3):
                v = gtg.m_add(gtg.bdot(M(x, y), GA.gen(z), sq), gtg.bdot(M(y, z), GA.gen(x), sq),
                              gtg.bdot(M(z, x), GA.gen(y), sq))
                for bl, c in v.items():
                    rows.setdefault((x, y, z, bl), [F(0)] * (n * n))[i * n + j] = c
    return list(rows.values())


def check_kernel_of_the_protraction_is_the_space_of_algebraic_curvature_maps():
    """(4): rank of M -> T and the dimension d^2 (d^2 - 1)/12 of its kernel for d = 3, 4, 5; the kernel lies in the
    symmetric maps (adding the symmetry conditions does not raise the rank); B -> I B on Cl(1,3) is symmetric with
    nonzero protraction."""
    expected = ((3, 6, 0), (16, 20, 1), (16, 20, 1), (50, 50, 5))     # rank, kernel, symmetric maps outside the kernel
    for sq, (rank, ker, gap) in zip(KERNEL_SIGS, expected):
        d = len(sq)
        rows, blades = protraction_rows(sq)
        n = len(blades)
        r = GA.field_rank(rows)
        GA.check("rank of the protraction map", r == rank)
        GA.check("kernel dimension d^2 (d^2 - 1)/12", n * n - r == ker and 12 * ker == d * d * (d * d - 1))
        GA.check("the kernel consists of symmetric maps", GA.field_rank(rows + symmetry_rows(sq, blades)) == r)
        GA.check("symmetric maps outside the kernel", n * (n + 1) == 2 * (ker + gap))
    rows, blades = protraction_rows(S13)
    cyc = cyclic_rows(S13)
    GA.check("the cyclic vector identity has the same solutions as the protraction identity",
             GA.field_rank(cyc) == 16 and GA.field_rank(rows + cyc) == 16)
    sq = S13
    I4 = gtg.pseudoscalar(sq)

    def dual(a, b):
        return gtg.m_mul(I4, gtg.wedge(GA.gen(a), GA.gen(b), sq), sq) if a != b else {}
    blades = gtg.bivector_blades(len(sq))
    sym = all(gtg.sp(gtg.m_mul({x: F(1)}, dual(*y), sq)) == gtg.sp(gtg.m_mul(dual(*x), {y: F(1)}, sq))
              for x in blades for y in blades)
    GA.check("B -> I B is symmetric", sym)
    GA.check("B -> I B has protraction -3 I c",
             all(protraction(dual, c, sq) == gtg.m_scal(-3, gtg.m_mul(I4, GA.gen(c), sq)) for c in range(len(sq))))
    return True
