"""dark-matter.mirror-tower-copy-one: exact checks.

Reversal invariance of the inputs (premise: the Standard-Model chain's list of inputs):
- (c) the even subalgebras of a reversal pair are isomorphic: flipping every square changes the product
  of two even blades by (-1)^(number of contracted indices), which the bijection
  phi(e_K) = (-1)^(|K|/2) e'_K (e_i e_j -> -e'_i e'_j, the map induced by x -> i x) compensates;
  phi is multiplicative, checked on every pair of even blades for (2,4)/(4,2) (the ambients) and (1,3)/(3,1).
  Cl^0(2,4) = Cl(2,3) and Cl^0(4,2) = Cl(4,1) through the generators e_i e_n, and both have type C,
  one component, module dimension 8 (type computation exported by type-residue-what-each-tower-can):
  Spin(2,4) = Spin(4,2) = SU(2,2); likewise Cl^0(1,3) = Cl(1,2) and Cl^0(3,1) = Cl(3,0), type C, module 4.
- (b) the complexified fibres agree: x -> (i x_0, ..., i x_n) with the reversed signs is an isometry
  C^(2,4) -> C^(4,2) (Gaussian rationals), so maximal isotropic subspaces and pair counts are the same.
- (ii) the ground types differ (H for (1,3), R for (3,1)) while the even subalgebras agree, so the
  derivation, which runs on the conformal spin group, does not see the ground type.
- (iii) one-loop coefficients of this tower's content (three generations, one Higgs doublet), computed from
  the hypercharges and multiplets: b = (41/10, -19/6, -7). That the mirror's content, and so its b, is the
  same is the copy of (i), carried by the even-subalgebra and fibre checks above and not recomputed from an
  independent mirror listing; Lambda_2 = Lambda_6 then follows from Lambda = M exp(-2 pi/(b alpha(M))) and is
  not separately tested. Mean mass per baryon: ours 0.75 m_p + 0.25 m_He/4 lies in (936.5, 937.0) MeV, a helium mirror's
  m_He/4 = 931.8; the ratio lies in (0.994, 0.996), within half a percent of one.
- Caveat: P2 with this reach gives xi = 1, Delta N_eff = (8/7)(11/4)^(4/3) + 3.044 in (7.44, 7.45),
  from an exact cube-root bracket.
(iv), (v) (the audit's verdicts and inheritance of epsilon) are readings, not computations.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

GEN = [(3, 2, F(1, 6)), (3, 1, F(-2, 3)), (3, 1, F(1, 3)), (1, 2, F(-1, 2)), (1, 1, F(1)), (1, 1, F(0))]
HIGGS = (1, 2, F(1, 2))
M_P, M_HE = F(938272, 1000), F(3727379, 1000)
# resolution of the cube-root bracket of 11/4 (a precision choice, not a datum)
ROOT_DENOM = 10 ** 6
# the statement's quoted window for Delta N_eff at xi = 1, and the check's own cap on Delta N_eff
QUOTED_DNEFF = (F(744, 100), F(745, 100))
DNEFF_CAP = F(3, 10)


def iroot_bracket(x, k, denom):
    """(lo, hi) multiples of 1/denom with lo^k <= x < hi^k (integer bisection)."""
    n = x * denom ** k
    t = n.numerator // n.denominator
    lo, hi = 0, 1
    while hi ** k <= t:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** k <= t:
            lo = mid
        else:
            hi = mid
    return F(lo, denom), F(lo + 1, denom)


def even_tables_agree(p, q):
    sq = GA.sig(p, q)
    sqr = tuple(-s for s in sq)
    ev = [b for b in GA.all_blades(p + q) if len(b) % 2 == 0]
    ok = True
    for a in ev:
        for b in ev:
            c1, k1 = GA.blade_mul(a, b, sq)
            c2, k2 = GA.blade_mul(a, b, sqr)
            # phi(e_K) = (-1)^(|K|/2) e'_K: phi(a) phi(b) = phi(ab)
            ok = ok and k1 == k2 and c2 * (-1) ** ((len(a) + len(b)) // 2) == c1 * (-1) ** (len(k1) // 2)
    return ok, len(ev)


def even_generators_ok(p, q):
    n = p + q
    sq = GA.sig(p, q)
    en = GA.gen(n - 1)
    fs = [GA.mul(GA.gen(i), en, sq) for i in range(n - 1)]
    ok = sq[n - 1] == -1
    for i, fi in enumerate(fs):
        ok = ok and GA.eq(GA.mul(fi, fi, sq), GA.sc(sq[i]))
        ok = ok and all(GA.anticommutes(fi, fs[j], sq) for j in range(i + 1, n - 1))
    return ok


def check_even_subalgebras_and_spin_groups_agree():
    premise("dark-matter.imported-inputs-standard-model-chain")
    ct = premise("dark-matter.type-residue-what-each-tower-can")["clifford_type"]
    ok = True
    sizes = []
    for p, q in ((2, 4), (1, 3)):
        same, k = even_tables_agree(p, q)
        ok = ok and same
        sizes.append(k)
    ok = ok and sizes == [32, 8]
    ok = ok and all(even_generators_ok(p, q) for p, q in ((2, 4), (4, 2), (1, 3), (3, 1)))
    a, b = ct(2, 3), ct(4, 1)
    ok = ok and (a["D"], a["comps"], a["dimS"]) == (b["D"], b["comps"], b["dimS"]) == ("C", 1, 8)
    c, d = ct(1, 2), ct(3, 0)
    ok = ok and (c["D"], c["comps"], c["dimS"]) == (d["D"], d["comps"], d["dimS"]) == ("C", 1, 4)
    GA.check("thm:mirror: even subalgebras of (2,4)/(4,2) and (1,3)/(3,1) have equal structure constants; "
             "Cl(2,3), Cl(4,1) both M(4,C); Cl(1,2), Cl(3,0) both M(2,C)", ok)
    return ok


def check_complexified_fibres_and_ground_types():
    premise("dark-matter.imported-inputs-standard-model-chain")
    ct = premise("dark-matter.type-residue-what-each-tower-can")["clifford_type"]
    sq = GA.sig(2, 4)
    sqr = tuple(-x for x in sq)
    i_ = GA.QI_I
    E = [[GA.qi(int(j == k)) for k in range(6)] for j in range(6)]
    phi = lambda x: [i_ * xk for xk in x]
    bil = lambda s, x, y: sum((x[k] * y[k] * s[k] for k in range(6)), GA.qi(0))
    ok = all(bil(sqr, phi(a), phi(b)) == bil(sq, a, b) for a in E for b in E)
    ok = ok and ct(1, 3)["D"] == "H" and ct(3, 1)["D"] == "R" and ct(1, 3)["dimS"] == 8 and ct(3, 1)["dimS"] == 4
    GA.check("thm:mirror(ii): x -> i x is an isometry C^(2,4) -> C^(4,2); ground types H (this tower) and R "
             "(mirror) differ", ok)
    return ok


def b_coeffs(gens):
    content = gens * 3
    b1 = F(2, 3) * F(3, 5) * sum(c * w * y * y for c, w, y in content) \
        + F(1, 3) * F(3, 5) * 2 * HIGGS[2] ** 2
    b2 = F(-22, 3) + F(2, 3) * sum(F(c, 2) for c, w, y in content if w == 2) + F(1, 3) * F(1, 2)
    b3 = -11 + F(2, 3) * sum(F(w, 2) for c, w, y in content if c == 3)
    return b1, b2, b3


def check_standard_model_running_and_mean_mass_ratio():
    premise("dark-matter.imported-inputs-standard-model-chain")
    ours = b_coeffs(GEN)
    ok = ours == (F(41, 10), F(-19, 6), F(-7))
    ours_m = F(3, 4) * M_P + F(1, 4) * M_HE / 4
    ratio = (M_HE / 4) / ours_m
    ok = ok and F(9365, 10) < ours_m < F(937) and F(9318, 10) < M_HE / 4 < F(9319, 10)
    ok = ok and F(994, 1000) < ratio < F(996, 1000) and F(514, 10 ** 5) < 1 - ratio < F(516, 10 ** 5)
    GA.check("thm:mirror(iii): b = (41/10, -19/6, -7) for the Standard Model content; mean mass per baryon 936.7 vs 931.8 MeV, "
             "ratio in (0.994, 0.996)", ok)
    return ok


def check_p2_caveat_mirror_at_our_temperature():
    premise("dark-matter.p2-indifference")
    lo, hi = iroot_bracket(F(11, 4), 3, ROOT_DENOM)
    ok = lo ** 3 <= F(11, 4) < hi ** 3
    # (11/4)^(1/3) = 1.4010196..., by hand to seven figures
    ok = ok and lo == F(1401019, 10 ** 6) and hi == F(1401020, 10 ** 6)
    dn_lo = F(8, 7) * F(11, 4) * lo + F(3044, 1000)
    dn_hi = F(8, 7) * F(11, 4) * hi + F(3044, 1000)
    ok = ok and QUOTED_DNEFF[0] < dn_lo and dn_hi < QUOTED_DNEFF[1]
    # by hand: (8/7)(11/4)^(4/3) + 3.044 = 7.447204..., so the bracket sits in (7.44720, 7.44721)
    ok = ok and all(F(744720, 10 ** 5) < d < F(744721, 10 ** 5) for d in (dn_lo, dn_hi))
    # far above the cap: 7.4472/0.3 = 24.82, so the integer part of the ratio is 24
    ok = ok and (dn_lo / DNEFF_CAP) // 1 == 24 and (dn_hi / DNEFF_CAP) // 1 == 24
    GA.check("caveat: xi = 1 under P2 gives Delta N_eff = (8/7)(11/4)^(4/3) + 3.044 in (7.44, 7.45), far above "
             "the cap", ok)
    return ok
