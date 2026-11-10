"""synthesis.curved-field-vacuum-polarisation-freedom-is-five-local-covariant-constants-of-which-one-is-transverse: exact checks.

The local covariant freedom of the vacuum-polarisation kernel on a torsion-free gravitational field.

Conventions of the store (lib/gtg.py): spacetime algebra Cl(1,3); a field is given by its coframe, with
g^mu = hb^T(e^mu); D_mu M = d_mu M + Omega(e_mu) x M; D = g^mu D_mu; curvature operator calR(B) = -R(hb(B)),
Ricci vector calR(b) = d_a . calR(a ^ b), scalar calR = d_a . calR(a).

  (1) counting: dimensions of the spaces of Lorentz-invariant tensors that the imported form of the freedom allows
      (invariance under the three bivector generators gamma_0 gamma_1, gamma_1 gamma_2, gamma_2 gamma_3, which
      generate the Lorentz algebra), by exact rank;
  (2) the identity D.(D ^ A) = Lap A - D(D.A) + calR(A) on a torsion-free field, Lap the rough Laplacian, and
      D ^ D chi = 0; with torsion D ^ D chi is not zero;
  (3) the Ward identity K(D chi) = 0 on K = c1 Lap + c2 D(D.) + c3 m^2 + c4 calR + c5 calR(.) has the solutions
      (c, -c, 0, 0, c) only.
"""
from fractions import Fraction as F
import itertools
import GA
import gtg
from gtg import Jet
from tp_premise import premise

LC = "synthesis.imported-local-covariance-with-scaling-of-time-ordered-products"
FLAT = "synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants"

SQ = GA.sig(1, 3)
ND = len(SQ)
G = [GA.gen(i) for i in range(ND)]
GUP = [GA.scal(F(SQ[i]), G[i]) for i in range(ND)]
VB = [(i,) for i in range(ND)]
BIV = gtg.bivector_blades(ND)
GENS = [{(0, 1): F(1)}, {(1, 2): F(1)}, {(2, 3): F(1)}]
FIELD_SEED, CHI_SEEDS, VEC_SEED = 1, (3, 4), 11
LOW, HIGH = 2, 3                       # jet orders of the coframe: curvature at a point, and its use on three derivatives
MASSES_SQ = (F(7, 3), F(2))
KN_DIAGONAL = (F(3), F(1), F(1), F(1))         # Ricci-type sample: scalar 2 (d - 1) tr P = 36


# ---- (1) invariant tensors ------------------------------------------------------------------------------------

def rep_cols(J, blades):
    """Columns of M -> J x M on the span of the blades."""
    cols = []
    for b in blades:
        im = gtg.comm(J, {b: F(1)}, SQ)
        cols.append({blades.index(k): c for k, c in im.items()})
    return cols


def flat_index(idx, dims):
    n = 0
    for i, d in zip(idx, dims):
        n = n * d + i
    return n


def generator_rows(J, slots):
    """Rows of the derivation J on the tensor product of the slots."""
    mats = [rep_cols(J, s) for s in slots]
    dims = [len(s) for s in slots]
    rows = {}
    for idx in itertools.product(*[range(n) for n in dims]):
        col = flat_index(idx, dims)
        for k, m in enumerate(mats):
            for i, c in m[idx[k]].items():
                out = list(idx)
                out[k] = i
                r = rows.setdefault(flat_index(out, dims), {})
                r[col] = r.get(col, F(0)) + c
    return list(rows.values())


def sparse_rank(rows):
    piv, r = {}, 0
    for row in rows:
        row = {k: v for k, v in row.items() if v != 0}
        while row:
            k = min(row)
            if k in piv:
                f = row[k]
                for kk, vv in piv[k].items():
                    nv = row.get(kk, F(0)) - f * vv
                    if nv == 0:
                        row.pop(kk, None)
                    else:
                        row[kk] = nv
            else:
                f = row[k]
                piv[k] = {kk: vv / f for kk, vv in row.items()}
                r += 1
                break
    return r


def invariants(slots, extra=()):
    """Dimension of the space of tensors on the slots annihilated by the generators and by the extra rows."""
    rows = []
    for J in GENS:
        rows += generator_rows(J, slots)
    n = 1
    for s in slots:
        n *= len(s)
    return n - sparse_rank(rows + list(extra))


def norm(b):
    return gtg.sp(gtg.m_mul({b: F(1)}, {b: F(1)}, SQ))


OPDIMS = [len(BIV), len(BIV), ND, ND]
# a tensor w[i, j, p, q] stands for the bilinear form beta(a, b) = sum w[i, j, p, q] <B_i M(B_j)>-coordinates:
# M = sum w[i, j] B_i (x) B_j acts as M(B) = sum w[i, j] B_i <B_j B>, so M is symmetric exactly when w is.


def symmetric_rows():
    out = []
    for i in range(len(BIV)):
        for j in range(i + 1, len(BIV)):
            for p in range(ND):
                for q in range(ND):
                    out.append({flat_index((i, j, p, q), OPDIMS): F(1), flat_index((j, i, p, q), OPDIMS): F(-1)})
    return out


def linear_rows(functional):
    """Rows saying that functional(M) = 0, for a linear multivector-valued functional given on the maps
    M_ij: B_j -> B_i <B_j B_j> (the coordinates w[i, j])."""
    acc = {}
    for i in range(len(BIV)):
        for j in range(len(BIV)):
            def M(a, b, i=i, j=j):
                if a == b:
                    return {}
                key, s = ((a, b), 1) if a < b else ((b, a), -1)
                return {BIV[i]: s * norm(BIV[j])} if key == BIV[j] else {}
            for tag, val in functional(M).items():
                acc.setdefault(tag, {})[(i, j)] = val
    out = []
    for d in acc.values():
        for p in range(ND):
            for q in range(ND):
                out.append({flat_index((i, j, p, q), OPDIMS): c for (i, j), c in d.items()})
    return out


def protraction_functional(M):
    out = {}
    for c in range(ND):
        T = gtg.m_add(*[gtg.outer(GUP[a], M(a, c), SQ) for a in range(ND)])
        for bl, v in T.items():
            out[(c, bl)] = v
    return out


def ricci_functional(M):
    out = {}
    for c in range(ND):
        r = gtg.m_add(*[gtg.inner_vb(GUP[a], M(a, c), SQ) for a in range(ND)])
        for bl, v in r.items():
            out[(c, bl)] = v
    return out


def pair_rows(dims, i, j, sign):
    """Rows w[..., x at i, y at j, ...] + sign w[..., y, x, ...] = 0."""
    out = []
    for idx in itertools.product(*[range(n) for n in dims]):
        if idx[i] <= idx[j]:
            sw = list(idx)
            sw[i], sw[j] = idx[j], idx[i]
            row = {flat_index(idx, dims): F(1)}
            row[flat_index(sw, dims)] = row.get(flat_index(sw, dims), F(0)) + sign
            out.append(row)
    return out


def check_invariant_local_terms_of_dimension_two_for_two_vector_slots():
    """(i): no invariant with three vector slots (no term m D); four with four vector slots, two of them symmetric
    in the derivative pair and two antisymmetric (commutators, which are curvature terms); bilinear forms linear in
    a bivector map: 6 for all maps, 3 on symmetric maps, 2 on maps obeying the protraction identity, 0 on those
    that are also Ricci-free (Weyl type)."""
    premise(LC)
    v4 = [ND, ND, ND, ND]
    GA.check("three vector slots: no invariant", invariants([VB, VB, VB]) == 0)
    GA.check("four vector slots: four invariants", invariants([VB, VB, VB, VB]) == 4)
    GA.check("symmetric in the derivative pair: two", invariants([VB, VB, VB, VB], pair_rows(v4, 2, 3, F(-1))) == 2)
    GA.check("antisymmetric in the derivative pair: two", invariants([VB, VB, VB, VB], pair_rows(v4, 2, 3, F(1))) == 2)
    slots = [BIV, BIV, VB, VB]
    prot = linear_rows(protraction_functional)
    GA.check("all bivector maps: six", invariants(slots) == 6)
    GA.check("symmetric maps: three", invariants(slots, symmetric_rows()) == 3)
    GA.check("maps obeying the protraction identity: two", invariants(slots, prot) == 2)
    GA.check("Weyl type: none", invariants(slots, prot + linear_rows(ricci_functional)) == 0)
    GA.check("two vector slots: one invariant (the term m^2 a.b)", invariants([VB, VB]) == 1)
    # the two invariants on curvature maps are a.M(b) and (a.b) M: independent on a map of Ricci type
    M = kulkarni_nomizu(KN_DIAGONAL)
    ric = [gtg.vdot(G[a], ricci_of(M, a), SQ) for a in range(ND)]
    scal = sum((SQ[a] * ric[a] for a in range(ND)), F(0))
    GA.check("a.M(b) and (a.b) M are independent", ric[0] * scal * SQ[1] != ric[1] * scal * SQ[0] and scal == 36)
    return True


# ---- (2), (3) differential operators on a torsion-free sample field -----------------------------------------------

def coef(seed, k):
    return F((seed * 7919 + k * 104729) % 11 - 5)


def poly(seed, k, order, scale, const, keep):
    """A polynomial in the four labels about the origin, truncated at the given order; one monomial in `keep`
    is retained (keep = 1: all)."""
    X = [Jet.var(i, F(0), ND, order) for i in range(ND)]
    j = Jet.const(const, ND) + X[0] * 0
    for deg in range(1, order + 1):
        for combo in itertools.combinations_with_replacement(range(ND), deg):
            k += 1
            if deg > 1 and (seed + k) % keep:
                continue
            t = Jet.const(coef(seed, k) * scale, ND)
            for i in combo:
                t = t * X[i]
            j = j + t
    return j, k


def sample_field(seed, order, omega_shift=None):
    TH, k = [], 0
    for a in range(ND):
        row = []
        for mu in range(ND):
            c0 = (F(1) if a == mu else F(0)) + coef(seed, 900 + ND * a + mu) * F(1, 8)
            j, k = poly(seed, k, order, F(1, 4), c0, 3)
            row.append(j)
        TH.append(row)
    fld = gtg.Field(TH, None, SQ)
    if omega_shift is None:
        return fld
    Om = [dict(x) for x in fld.Om]
    Om[1] = gtg.m_add(Om[1], omega_shift)
    return gtg.Field(TH, None, SQ, Om=Om)


class Calc(object):
    """Covariant operators on jets for one field."""

    def __init__(self, fld):
        self.f = fld
        self.HJ = fld.hb_matrix_jet()
        self.gup = [gtg.m_add(*[gtg.m_scal(self.HJ[mu][a] * SQ[a], G[a]) for a in range(ND)]) for mu in range(ND)]
        self.Rc = fld.curvature()

    def Dmu(self, mu, M):
        return gtg.m_add(gtg.m_d(M, mu), gtg.comm(self.f.Om[mu], M, SQ))

    def grad(self, chi):
        return gtg.m_add(*[gtg.m_scal(chi.d(mu), self.gup[mu]) for mu in range(ND)])

    def div(self, A):
        out = Jet.const(F(0), ND)
        for mu in range(ND):
            out = out + gtg.vdot(self.gup[mu], self.Dmu(mu, A), SQ)
        return out

    def curl(self, A):
        return gtg.m_add(*[gtg.outer(self.gup[mu], self.Dmu(mu, A), SQ) for mu in range(ND)])

    def div_bivector(self, B):
        return gtg.m_add(*[gtg.inner_vb(self.gup[mu], self.Dmu(mu, B), SQ) for mu in range(ND)])

    def along(self, a, M):
        """(gamma_a . D) M = D_{hb(gamma_a)} M."""
        return gtg.m_add(*[gtg.m_scal(self.HJ[mu][a], self.Dmu(mu, M)) for mu in range(ND)])

    def rough_laplacian(self, A):
        """sum_a Q(gamma_a) [ (gamma_a . D)(gamma_a . D) A - ((gamma_a . D) gamma_a) . D A ]."""
        out = {}
        for a in range(ND):
            t = self.along(a, self.along(a, A))
            v = self.along(a, {(a,): Jet.const(F(1), ND)})
            for b in range(ND):
                vb = v.get((b,))
                if vb:
                    t = gtg.m_sub(t, gtg.m_scal(vb, self.along(b, A)))
            out = gtg.m_add(out, gtg.m_scal(SQ[a], t))
        return out


def vector_field(seed, order):
    A, k = {}, 5000
    for a in range(ND):
        j, k = poly(seed, k, order, F(1, 2), coef(seed, 77 + a), 1)
        A[(a,)] = j
    return A


def scalar_field(seed):
    """A cubic polynomial scalar."""
    return poly(seed, 9000, 3, F(1, 2), F(0), 1)[0]


def torsion_shift():
    X = [Jet.var(i, F(0), ND, LOW) for i in range(ND)]
    return {(0, 2): X[3] * F(1, 2) + F(1, 3)}


def kulkarni_nomizu(P):
    """The map a ^ b -> P(a) ^ b + a ^ P(b) on frame planes, P diagonal with entries P[a]."""
    def M(a, b):
        return gtg.m_scal(P[a] + P[b], gtg.wedge(G[a], G[b], SQ)) if a != b else {}
    return M


def ricci_of(M, b):
    return gtg.m_add(*[gtg.inner_vb(GUP[a], M(a, b), SQ) for a in range(ND)])


def check_divergence_of_the_field_strength_is_laplacian_minus_gradient_divergence_plus_ricci():
    """(ii): on a torsion-free polynomial field, D.(D ^ A) = Lap A - D(D.A) + calR(A) for a generic vector field A
    (store sign of the Ricci vector: the opposite sign fails), and D ^ D chi = 0; on a field with torsion
    D ^ D chi is not zero."""
    fld = sample_field(FIELD_SEED, LOW)
    C = Calc(fld)
    GA.check("the sample is torsion-free with nonzero Ricci vector",
             fld.torsion_free() and all(gtg.ricci(C.Rc, G[a], SQ) for a in range(ND)))
    A = vector_field(VEC_SEED, LOW)
    lhs = gtg.m_val(C.div_bivector(C.curl(A)))
    lap, gd = gtg.m_val(C.rough_laplacian(A)), gtg.m_val(C.grad(C.div(A)))
    ric = gtg.ricci(C.Rc, gtg.m_val(A), SQ)
    GA.check("D.(D ^ A) = Lap A - D(D.A) + calR(A)", gtg.m_sub(lhs, gtg.m_add(lap, gtg.m_scal(-1, gd), ric)) == {})
    GA.check("the Ricci term is needed and its sign is the store's", ric != {} and lhs != gtg.m_sub(gtg.m_sub(lap, gd), ric))
    chi = scalar_field(VEC_SEED)
    GA.check("D ^ D chi = 0 without torsion", gtg.m_val(C.curl(C.grad(chi))) == {})
    tors = sample_field(FIELD_SEED, LOW, torsion_shift())
    GA.check("with torsion D ^ D chi is not zero",
             (not tors.torsion_free()) and gtg.m_val(Calc(tors).curl(Calc(tors).grad(chi))) != {})
    return True


def check_ward_identity_leaves_one_constant_times_the_divergence_of_the_field_strength():
    """(ii): on one torsion-free polynomial field (third-order jets) and two cubic scalars chi, the equations
    c1 Lap(D chi) + c2 D(D.D chi) + c3 m^2 D chi + c4 calR D chi + c5 calR(D chi) = 0, taken at two values of
    the mass, have rank 4 and the
    one-dimensional solution space spanned by (1, -1, 0, 0, 1)."""
    premise(LC)
    premise(FLAT)
    fld = sample_field(FIELD_SEED, HIGH, {(0, 2): Jet.var(3, F(0), ND, HIGH) * F(1, 2) + F(1, 3)})
    C = Calc(fld)
    scal = gtg.ricci_scalar(C.Rc, SQ)
    rows = []
    for seed in CHI_SEEDS:
        g = C.grad(scalar_field(seed))
        gv = gtg.m_val(g)
        lap, gd, ric = gtg.m_val(C.rough_laplacian(g)), gtg.m_val(C.grad(C.div(g))), gtg.ricci(C.Rc, gv, SQ)
        for msq in MASSES_SQ:
            cols = [lap, gd, gtg.m_scal(msq, gv), gtg.m_scal(scal, gv), ric]
            for a in range(ND):
                rows.append([v.get((a,), F(0)) for v in cols])
    GA.check("four independent conditions on five constants", GA.field_rank(rows) == 4)
    ker = GA.field_kernel(rows)
    GA.check("the solutions are the multiples of (1, -1, 0, 0, 1)",
             len(ker) == 1 and ker[0][0] != 0 and [x / ker[0][0] for x in ker[0]] == [1, -1, 0, 0, 1])
    return True
