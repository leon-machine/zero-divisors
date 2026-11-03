"""synthesis.slot-module-light-ray-arrays-are-weyl-components: exact checks.

Part A, spacetime algebra Cl(1,3) (gamma_0^2 = +1, gamma_i^2 = -1), horizon null plane N_k with
k = gamma_0 + gamma_3, m = gamma_0 - gamma_3, B = gamma_3 gamma_0, Lambda(k) = (1 + B)/2,
Lambda(m) = (1 - B)/2 (canonical part on N_k, stored):
(i)  the Dirac operator splits as nabla = (1/2) m (k.nabla) + (1/2) k (m.nabla) + nabla_perp, so
     k nabla carries no derivative off N_k (k k = 0), k m = 2 + 2B = 4 Lambda(k), k anticommutes with
     gamma_1, gamma_2, and k Lambda(k) = 0; hence for every right multiplier X (every Lorentz-covariant
     mass term, Dirac or Majorana) k psi X = k Lambda(m) psi X: mass terms enter only the constraint
     fixing Lambda(k) psi along N_k, and L_k is injective on the canonical part (rank 4);
(i') Lambda(m) is the primitive idempotent (1 + e_t e_a)/2 of the even algebra of the (1,1) plane of
     k and m, e_t = gamma_0, e_a = gamma_3 (the residue-0 single chiral ideal).
Part B, the fermionic slot module V = Lambda(C^5) (modes 0, 1 slots; 2, 3, 4 pairs), built as
exterior states, with Y = (3n - 2k)/6, T3 = (n_0 - n_1)/2, colour weights n_{2+i} - k/3:
(ii)  every CPT halving commuting with the gauge algebra (32 sign patterns on the five conjugate
      pairs of isotypic components, times a line in the neutral block) has dim V_+ = 16 and
      V_- = conj(V_+) on weights; so a generation is 16 Weyl components, 16 arrays per light ray,
      8 registered units of ln 2 (2 arrays each), for every neutral-singlet choice;
(iii) in every such halving no non-neutral weight of V_+ has its negative in V_+: the particle half is
      chiral, vector-like only on the neutral singlet; at the anomaly-free halving (-1)^N the
      hypercharge multiset is {0:1, -2/3:3, 1/6:6, -1/2:2, 1:1, 1/3:3};
(iv)  after electroweak breaking (charge Q = T3 + Y, colour) the anomaly-free half pairs into exactly 7
      charged Dirac species plus 2 neutral components; 2*7 + 2 = 16 arrays with two Majorana
      neutrals, 2*8 = 16 with one Dirac neutrino; a generation without the neutral singlet (15) is
      not a halving and would give 15/2 units;
(v)   N_g generations: 16 N_g arrays, 8 N_g units; gauge-covariant Dirac pairs only among the
      N_g neutral singlets, at most N_g // 2.
"""
from fractions import Fraction as F
from itertools import combinations, product
import GA
from tp_premise import premise

# ---------------------------------------------------------------- Part A: Cl(1,3)
SQ = GA.sig(1, 3)
EVEN = [(), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2, 3)]
ODD = [(0,), (1,), (2,), (3,), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]


def g(i):
    return GA.gen(i)


def mm(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


K = GA.add(g(0), g(3))
M = GA.sub(g(0), g(3))
B = mm(g(3), g(0))


def opmat(op, dom, cod):
    cols = [op({b: F(1)}) for b in dom]
    return [[cols[j].get(c, F(0)) for j in range(len(dom))] for c in cod]


def lam_k(x):
    return GA.scal(F(1, 2), GA.add(x, mm(B, x)))


def lam_m(x):
    return GA.scal(F(1, 2), GA.sub(x, mm(B, x)))


def check_mass_terms_enter_only_the_constraint():
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    premise("field-theory.second-quantisation")
    ok = GA.is_zero(mm(K, K)) and GA.eq(mm(K, M), GA.add(GA.sc(2), GA.scal(F(2), B)))
    # reciprocal frame of the (k, m) plane: k.m = 2, so a = (1/2) m (k.a) + (1/2) k (m.a) + a_perp
    ok = ok and GA.dot(K, M, SQ) == 2
    for a in (g(0), g(1), g(2), g(3)):
        ka = GA.dot(K, a, SQ)
        ma = GA.dot(M, a, SQ)
        perp = GA.sub(a, GA.add(GA.scal(F(ka, 2), M), GA.scal(F(ma, 2), K)))
        ok = ok and GA.dot(K, perp, SQ) == 0 and GA.dot(M, perp, SQ) == 0
        # k times the off-plane part (1/2) k (m.a) vanishes: no derivative off N_k in k nabla
        ok = ok and GA.is_zero(mm(K, GA.scal(F(ma, 2), K)))
    for j in (1, 2):
        ok = ok and GA.anticommutes(K, g(j), SQ)
    # k Lambda(k) = 0 on every even blade; L_k injective on Lambda(m) (rank 4)
    LkPk = opmat(lambda x: mm(K, lam_k(x)), EVEN, ODD)
    LkPm = opmat(lambda x: mm(K, lam_m(x)), EVEN, ODD)
    ok = ok and GA.mat_rank(LkPk) == 0 and GA.mat_rank(LkPm) == 4
    # every right multiplier X (mass terms, Dirac or Majorana type) enters k psi X through Lambda(m) only
    for X in [{b: F(1)} for b in EVEN + ODD]:
        R = opmat(lambda x: mm(K, mm(lam_k(x), X)), EVEN, EVEN + ODD)
        ok = ok and GA.mat_rank(R) == 0
    # contrast: a left multiplier other than the rotor action does not pass (B on Lambda(k) is +1, not 0)
    ok = ok and GA.mat_rank(opmat(lambda x: lam_k(x), EVEN, EVEN)) == 4
    assert ok, "check_mass_terms_enter_only_the_constraint"
    return ok


def check_canonical_projector_is_residue_zero_ideal():
    premise("synthesis.lowest-causal-residues-zero-four-content")
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    f = GA.scal(F(1, 2), GA.add(GA.sc(1), mm(g(0), g(3))))
    lm = GA.scal(F(1, 2), GA.sub(GA.sc(1), B))
    ok = GA.eq(f, lm) and GA.eq(mm(f, f), f)
    fc = GA.sub(GA.sc(1), f)
    ok = ok and GA.is_zero(mm(f, fc)) and not GA.is_zero(fc)
    # the even algebra of the (k, m) plane is span{1, gamma_0 gamma_3}: two primitive idempotents
    ok = ok and GA.eq(mm(mm(g(0), g(3)), mm(g(0), g(3))), GA.sc(1))
    # f carries the null ray m: m f = ... f annihilated by L_m (canonical part = ker L_m)
    ok = ok and GA.is_zero(mm(M, f)) and not GA.is_zero(mm(K, f))
    assert ok, "check_canonical_projector_is_residue_zero_ideal"
    return ok


# ---------------------------------------------------------------- Part B: slot module
NM = 5
SLOTS, PAIRS = (0, 1), (2, 3, 4)


def basis_states():
    out = []
    for r in range(NM + 1):
        for S in combinations(range(NM), r):
            st = {frozenset(): F(1)}
            for i in reversed(S):
                st = GA.ext_wedge(i, st)
            out.append((S, st))
    return out


def number(i, st):
    e = [F(1) if j == i else F(0) for j in range(NM)]
    return GA.ext_wedge(i, GA.ext_contract(e, st))


def weights(S, st):
    occ = []
    for i in range(NM):
        ni = number(i, st)
        if GA.ext_state_eq(ni, st):
            occ.append(1)
        elif not ni:
            occ.append(0)
        else:
            raise ValueError("not a number eigenstate")
    n = occ[0] + occ[1]
    k = occ[2] + occ[3] + occ[4]
    Y = F(3 * n - 2 * k, 6)
    t3 = F(occ[0] - occ[1], 2)
    col = tuple(F(occ[2 + i]) - F(k, 3) for i in range(3))
    return dict(n=n, k=k, Y=Y, t3=t3, col=col, w=(t3, col, Y))


STATES = [(S, weights(S, st)) for S, st in basis_states()]


def neg(w):
    return (-w[0], tuple(-c for c in w[1]), -w[2])


def isotypic():
    """Isotypic components of V under the gauge algebra, labelled (n, k)."""
    comps = {}
    for S, d in STATES:
        comps.setdefault((d['n'], d['k']), []).append(d)
    return comps


def halvings():
    """All CPT halvings commuting with the gauge algebra: one of each conjugate pair of
    non-neutral components, and one of the two neutral lines (the neutral block is two-dimensional;
    any line in it gives the same weights)."""
    comps = isotypic()
    neutral = [(0, 0), (2, 3)]
    rest = [c for c in comps if c not in neutral]
    pairs = []
    for c in rest:
        rep = sorted(d['w'] for d in comps[c])
        for c2 in rest:
            if c2 > c and sorted(neg(d['w']) for d in comps[c2]) == rep:
                pairs.append((c, c2))
    out = []
    for signs in product((0, 1), repeat=len(pairs)):
        for nl in (0, 1):
            plus = [pairs[i][s] for i, s in enumerate(signs)] + [neutral[nl]]
            Vp = [d['w'] for c in plus for d in comps[c]]
            Vm = [d['w'] for c in comps if c not in plus for d in comps[c]]
            out.append((plus, Vp, Vm))
    return pairs, out


def check_sixteen_weyl_components_every_halving():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("synthesis.spin10-clause-content-is-the-neutral-singlet-choice")
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    ok = len(STATES) == 32
    pairs, hs = halvings()
    ok = ok and len(pairs) == 5 and len(hs) == 64
    for plus, Vp, Vm in hs:
        ok = ok and len(Vp) == 16 and len(Vm) == 16
        ok = ok and sorted(neg(w) for w in Vp) == sorted(Vm)       # V_- = conj(V_+)
        arrays = len(Vp)                                           # one array per Weyl component
        entropy_ln2 = F(arrays, 2)                                 # (1/2) ln 2 per array at (Q) v3
        units = F(arrays, 2)                                       # registered unit = two arrays
        ok = ok and entropy_ln2 == 8 and units.denominator == 1 and units == 8
    assert ok, "check_sixteen_weyl_components_every_halving"
    return ok


def check_particle_half_is_chiral():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("synthesis.spin10-clause-content-is-the-neutral-singlet-choice")
    zero = (F(0), (F(0), F(0), F(0)), F(0))
    _, hs = halvings()
    ok = True
    for plus, Vp, Vm in hs:
        vl = [w for w in Vp if w != zero and neg(w) in Vp]
        ok = ok and vl == [] and Vp.count(zero) == 1
    # contrast: the whole module is vector-like (every weight paired), so the test can fail
    allw = [d['w'] for S, d in STATES]
    ok = ok and all(neg(w) in allw for w in allw)
    # the anomaly-free halving (-1)^(n+k), particle half containing (2,3)_{1/6}
    Vp = [d for S, d in STATES if (d['n'] + d['k']) % 2 == 0]
    hist = {}
    for d in Vp:
        hist[d['Y']] = hist.get(d['Y'], 0) + 1
    ok = ok and hist == {F(0): 1, F(-2, 3): 3, F(1, 6): 6, F(-1, 2): 2, F(1): 1, F(1, 3): 3}
    ok = ok and all(-y not in hist for y in hist if y != 0)
    ok = ok and sum(y * c for y, c in hist.items()) == 0
    assert ok, "check_particle_half_is_chiral"
    return ok


def em_pairing(Vp_ws):
    """Maximal number of charge-conjugate (Dirac) pairs among weights labelled by (Q, colour)."""
    lab = {}
    for w in Vp_ws:
        key = (w[0] + w[2], w[1])
        lab[key] = lab.get(key, 0) + 1
    negk = lambda key: (-key[0], tuple(-c for c in key[1]))
    charged = sum(min(c, lab.get(negk(key), 0)) for key, c in lab.items() if key != negk(key)) // 2
    neutral = sum(c for key, c in lab.items() if key == negk(key))
    return charged, neutral


def check_electroweak_pairing_and_neutrino_cases():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("standard-model.majorana-element")
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    Vp = [d['w'] for S, d in STATES if (d['n'] + d['k']) % 2 == 0]
    charged, neutral = em_pairing(Vp)
    ok = charged == 7 and neutral == 2
    # with a nonzero Majorana term: n_D = 7, n_W = 2; with none (Dirac neutrino): n_D = 8, n_W = 0
    for nD, nW in ((charged, neutral), (charged + neutral // 2, 0)):
        arrays = 2 * nD + nW
        ok = ok and arrays == 16 and F(arrays, 2) == F(nD) + F(nW, 2) == 8
    # a generation without the neutral singlet: 15 components, not a halving, 15/2 units
    Vp15 = [w for w in Vp if w != (F(0), (F(0), F(0), F(0)), F(0))]
    c15, n15 = em_pairing(Vp15)
    ok = ok and len(Vp15) == 15 and (c15, n15) == (7, 1) and F(2 * c15 + n15, 2) == F(15, 2)
    ok = ok and F(2 * c15 + n15, 2).denominator == 2
    assert ok, "check_electroweak_pairing_and_neutrino_cases"
    return ok


def check_generations():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    zero = (F(0), (F(0), F(0), F(0)), F(0))
    gen = [d['w'] for S, d in STATES if (d['n'] + d['k']) % 2 == 0]
    ok = True
    for ng in range(1, 5):
        content = gen * ng
        arrays = len(content)
        ok = ok and arrays == 16 * ng and F(arrays, 2) == 8 * ng
        # gauge-covariant Dirac pairs: a weight w != 0 pairs only with -w; zero weights pair among themselves
        nonzero_pairs = sum(min(content.count(w), content.count(neg(w))) for w in set(content) if w != zero)
        zeros = content.count(zero)
        ok = ok and nonzero_pairs == 0 and zeros == ng and zeros // 2 == ng // 2
    assert ok, "check_generations"
    return ok


if __name__ == "__main__":
    for fn in [check_mass_terms_enter_only_the_constraint, check_canonical_projector_is_residue_zero_ideal,
               check_sixteen_weyl_components_every_halving, check_particle_half_is_chiral,
               check_electroweak_pairing_and_neutrino_cases, check_generations]:
        print(fn.__name__, fn())
