# attack-C4B (cluster C4, independence sweep): op.pair-sector-current item 3, op.rung-unit (xi G)

Status: done (two proposals filed). Kill conditions below were written before the computations they govern.

## op.pair-sector-current: the 126 coefficient relative to the 10

Orientation. Premise set at pinned versions (cone of the problem's eight entities, 126 entities):
(F1)-(F4), standard-model.slot-module-hypothesis, scrambling.indifference-structural-premise-series, and
imported Facts (Clebsch structure and seesaw, spinor bilinears, Pati-Salam branching and survival, grade
dictionary, anomaly coefficients, Fock representation, Cauchy decomposition, Chevalley/Witt, tractor and
GTG imports). None names a coupling weight. The Pati-Salam route adds, by the stored relations that mention
couplings: Premise (EW) (heavy direction only, Y_33 = 3 f_33 in its basis), the Majorana-scale premise,
Hypothesis (U) (not in the cone; optional), the chain and v_R, (H) and the real-breaking assumption.
Earlier work: g_lambda (f -> lambda f, w -> w/lambda) frees the Majorana scale and keeps w_d f fixed, so it
does not free the 126 coefficient (problem text). Stored fits (fits-record-level) already show rows where the
126's second-family entry supplies a tenth of m_s and rows where it supplies the factor 3.

Routes.
1. (Problem's own, attack item 1) a canonical weighting along the Majorana element. Delivers a derivation if a
   stored premise singles out one element E built from T and the stored structure. Needs that selection.
   Fails if every premise is satisfied by a two-parameter space of weightings.
2. (Other subject: the Majorana-scale theorem's method) a one-parameter group on the Pati-Salam data that fixes
   every stored relation and moves w_d f against the 10. Delivers independence. Fails if some stored relation
   ties w_d to w_u, f or the gauge data.
3. (Own) the indifference premise read as "equal weights on Pati-Salam components". Would fix the weight
   (the unsplit square, whose rung form is zero). Fails because the Pati-Salam split is determined by the
   derived algebra, so a separate weight is not an undetermined distinction, and the premise fixes no real
   number (argued).

Kill condition, constructive (registered before computing): the derivation succeeds only if some element E,
fixed by the stored structure with no free coefficient, is selected by a stored premise and w_4 E has
|y_e/y_d| = 3 on the family it acts on. If no stored premise selects E (the candidate rung forms span the
(10, GJ) plane), the derivation is killed and the problem goes to the independence route.

Computed (exact, explore_r1.py, module of the stored check): rung forms x(10) + y(GJ) of w_4 E:
E = 1: (1, 0); T T^dag, T^dag T, their sum and commutator: (0, 0); degree parts G_0, G_2: (1/32, 0);
G_4, G_6: (0, 0); G_8, G_10: (-1/32, 0); P_4: (0, -3/32); X_4: (0, 3/32) plus a 120; (B - L)^2: (1/3, -2/3);
the u(3) Casimir of the pair modes: (3, 3/2) plus a 120. Normalisation: on the sixteen the 10 form has entries
+-1 on quark and lepton pairings, the GJ form +-1/3 on quark and -+1 on lepton pairings relative to the 10, so
x(10) + y(GJ) has quark entry x + y/3 and lepton entry x - y; for w_4(a + b P_4), quark a - b/32, lepton
a + 3b/32, ratio (32a + 3b)/(32a - b): -3 exactly at a = 0, +3 exactly at b/a = 32/3.
Kill condition fired: canonical elements give every kind of ratio (pure 10, pure GJ, zero, mixed) and no stored
premise selects one. The derivation fails; independence route chosen (route 2 plus the module reading).

Kill condition, independence (registered before the checks): the independence claim dies if some stored relation
ties w_d (or the module weight b) to w_u, f, the gauge data or the Majorana scale, or if a premise of the cone
fails in one of the models.

Independence (established, proposal synthesis.georgi-jarlskog-weight-free-on-the-stored-relations, filed; check4
exit 0, validate ok): h_mu: w_d -> mu w_d (mu nonzero, real), all else fixed (composed with a rescaling of
a 10's vevs against its coupling when the electroweak normalisation is imposed). Fixes M_u, M_nu, M_R, m_nu,
(EW), the Majorana-scale premise, f-hat = f/f_33 and so (U) in the form the stored theorem reads it, the chain
and v_R, S_3 and S_2 invariance statements, (H), real breaking; moves Sym(M_d - M_e) = 4 w_d f by mu. On the
module the down-type rung coupling w_4(A + B P_4) realises M_d = A - B/32, M_e = A + 3B/32 (v_d Y = A,
w_d f = -B/32), and h_mu is B -> mu B.

Established (proved, exact checks): (i) T^2 = (T^dag)^2 = 0, T T^dag T = T, so 1, T, T^dag, T T^dag, T^dag T span
the algebra of T; w_4 times any element gives a multiple of the 10 (only 1 contributes); v_4 T^dag T gives half
the 10's neutrino entry plus an antisymmetric part. So attack item 1's "one potential along the Majorana element"
cannot give the down-type GJ term through operator functions of T: it needs the (15,1,1) projection of the
monomial expansion. (ii) w_4(a + b P_4): quark a - b/32, lepton a + 3b/32, ratio (32a+3b)/(32a-b), a Moebius
bijection; (a, b) = (v_d Y, -32 w_d f) is the Clebsch structure. (iii) h_mu fixes every stored relation (exact on a
diagonal model and an off-diagonal model with a 120, four mu). (iv) models with factor 3, 2 and 37/19 (the last at
the same sigma_1(M_d), so the bottom reading of (U) on the model's own m_b does not separate them).
Not filed / not established: whether a relation outside the store (a doublet-mixing potential at M_I) fixes w_d.
Cost: the second family's factor 3 (and m_b/m_tau at M_I) is an input of the record; the Clebsch -3 stays derived.
Filing note: postulates ((EW), (U), the Majorana-scale premise, indifference) are mentioned, not in uses (E203:
taking them is an assumes edge, maintainer-only; E307: (U) and (EW) are recorded as contradicting).

## op.rung-unit: xi G (v/M_P)

Orientation. Cone of the problem's eight entities: 248 entities; premises (F1)-(F4), slot-module, indifference,
(C_loc), sheaf tameness, P2/P3 (towers), the rung-unit premise itself, imports (Henneaux-Teitelboim promotion,
Fayet-Iliopoulos level only abelian, left-right bidoublet, Coleman-Weinberg/Gildener-Weinberg, B-mixing inputs,
two-doublet scalon sum, de Sitter representations, frozen-point and tractor imports, PDG M_P/H, ...).
Relations in the store that contain G or M_P together with a particle-sector scale: Gv^2N^2 = (v/H)^2,
Im w = N m/M_P, -w(w+3) = (m/M_P)^2 N^2 (identities); the trichotomy rescaling (Lambda -> s^2 Lambda at fixed
M_P, v/M_P invariant as a reading); no relation of the form v/M_P = function(N, gauge data).

Routes.
1. (Problem's own, attack item 2) xi as an su(2)_R-breaking remnant of the Pati-Salam stage, xi = c v_R^2.
   Fails: the chain fixes v_R/M_Z from the gauge data; a remnant relation is G-free, so it can fix v/v_R and
   never xi G (argued).
2. (Other subject) a level proportional to Lambda, xi = k H^2: then v/H is the law and xi G = 3k N^{-2};
   needs k ~ 10^88, a new constant; the register already records this branch as the alternative.
3. (Own) two exact models of the premise set at equal G, Lambda (so equal N), equal gauge couplings and W,
   differing in xi, with the lift locus exact (Pythagorean rational frames), every tree mass ratio equal, and
   the three identities above checked in both.

Kill condition, constructive (registered before computing): a derivation of xi G exists in the store only if
some stored relation containing both G (or M_P) and a particle-sector scale is not satisfied by both models of
route 3; if all such relations hold in both, the stored structure does not fix xi G and the derivation is
killed.

Kill condition, independence (registered before the checks): the claim dies if a stored relation containing G or
M_P and a weak-sector scale fails in one of the two models, or if a premise of the cone speaks of the level.

Result. Constructive kill condition fired: every stored relation mixing the two scales is an identity
(Gv^2N^2 = (v/H)^2, (m/M_P)^2 N^2 = m^2/H^2), reaches G only through a free cut-off (induced gravity), relates
models at different N (trichotomy rescaling), or is a reading/conjecture; all hold in both models. Routes 1 and 2
fail as stated above (argued). Independence established (proposal synthesis.d-term-level-free-at-fixed-n;
check4 exit 0, validate ok):
(i) proved: with W = kappa N^2, every lift-family frame c_lambda (lambda != H) is a charge-preserving, locally
stable vacuum at xi = m (g^2 + g'^2 + 8 kappa)/g'^2, xi/m > 1, with m_h^2 = M_Z^2 + 4 kappa N and m_pm^2 = M_W^2 +
4 kappa N: every tree mass squared an exact multiple of N, so the dimensionless spectrum is frame independent
(Hessian on L computed exactly in two frames with the stored check's machinery);
(ii) proved: two frames at equal G, Lambda (so N), g, g', kappa: N* = 41/9 and 313/25, xi G = 826/2025 and
10738/9375, (v/M_P)^2 = 41/450 and 313/1250 at N = 10; at N = 10^61 frames 10^-44 H and 2 10^-44 H give
(v/H)^2 > 10^87 and (v/M_P)^2 in a ratio near 4;
(iii) computed/argued: the identities and the H-free boundary D-term hold in both; induced gravity matches in
each with its own cut-off (argued); the store search for M_P/Planck with weak-sector quantities found no other
relation (argued, listed in the extraction note).
Cost: none beyond the register's (xi G is already a recorded input); every value of v in Planck or Hubble units is
from the record. Not established: that no completion outside the store fixes xi G; the toy W = kappa N^2 branch
is excluded by the record (charged pair), which independence does not need.

## Unexpected links
- (P1, argued from the Clebsch structure, not filed) On the Majorana route with one rung weighting shared by the
  up-type and down-type rung components (w_d/v_d = w_u/v_u), Premise (EW) forces (M_e)_33 = 0 in the (EW) basis:
  v_u Y_33 = 3 w_u f_33 gives v_d Y_33 - 3 w_d f_33 = (v_d/v_u)(v_u Y_33 - 3 w_u f_33) = 0. So a single shared
  (15,1,1) weight is incompatible with (EW) and a heavy tau at the leading order; the covariant completion's two
  couplings (Y on c, Y-tilde on c*) or a separate w_d are needed. Relevant to op.rung-unit attack item 3 and to
  the per-sector c* reading (synthesis.conjugate-reading-up-down-split-is-t3r-odd-or-cp-odd).
- (P1) The up-type rung vector picks up one extra form from operator functions of T: v_4 T^dag T, half the 10's
  neutrino Dirac entry (nu^c with the neutral lepton), no quark entry. A Majorana-element coupling can thus shift
  the neutrino Dirac entry alone, a lead for synthesis.hypothesis-u-* and (EW) (not pursued).
- (P2) The two independence results have the same shape as the stored Majorana-scale theorem: each register
  input (N, xi G, the Majorana scale, and now the down-type 126 weight) is moved by a group or a model pair that
  fixes every stored relation. A sweep could state the register's free inputs as one list of independent moduli.
- C4A's window-p3 independence (beta shift by 8) and these share the method: model pair plus premise-cone audit.

## Decisions for Leon
1. (P1) Whether to register the down-type 126 weight (equivalently w_d against v_d, or the second family's factor
   3 at M_I) as an input of the record beside the Majorana scale, as synthesis.majorana-scale-free-input does for
   w_u. Recommendation: no new premise; record it in op.pair-sector-current's known text as an input of the fit
   (the factor 3 and m_b/m_tau at M_I are data on the stored relations), since no result uses a value of it.
2. (P1) Whether op.pair-sector-current can be marked settled on item 3: the success clause accepts "a no-go
   showing the series' structures cannot"; the proposal shows the stored relations cannot (not that no future
   dynamics can). Recommendation: mark item 3 done, keep the problem partial for items 1-2 (a dynamics weighting
   the (15,1,1) projection; the S_2-odd second stage).
3. (P2) The rung-unit premise's refutation condition could cite the new model pair as the evidence that nothing
   stored fixes xi G. Recommendation: add a note on version 3 (no version bump of content).
4. (Filing, both) The proposals mention but do not take the postulates (EW), (U), the Majorana-scale premise, (N)
   and the rung-unit premise (E203: taking a postulate is an assumes edge; E307: (U) and (EW) are recorded as
   contradicting). No assumes edge is requested.
