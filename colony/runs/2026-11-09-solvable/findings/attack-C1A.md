# Attack C1A (cluster C1, angle A constructive), run 2026-11-09-solvable

Status: attack round done. Two proposals filed (T1, T2); T3 nothing filed (answered in store). Kill conditions were
written here before any computation.

## T1 op.wall-class-invariant (attack item 1, with the dim <= 3 table as attack item 2)

Orientation. Parent claims read in full: synthesis.wall-rung-count-is-height-of-dying-line-class (clauses (1) necessity
N(Gbar) + L + N = N(Gbar) + R^k with rank N = k-1; (2) sufficiency L in R^k; (3) ht(x) <= k <= e(L) <= d+1) and
synthesis.lens-space-wall-rung-count-sees-the-integral-twist (L(4,1): indefinite k = 2, definite k = 3; T^3 comparison).
No earlier run findings on this problem exist in colony/runs/*/findings (the 31 October work has no run folder here).

Routes.
- R1 (the lead: Adams on RP^n). On RP^n the only nontrivial line is the tautological one, with x^n != 0, so
  ht(x) = n + 1 = e(L) = d + 1 and k = n + 1 is already fixed by the parent claim. RP^n walls cannot separate ht, e and k.
  Adams' order 2^phi(n) of L - 1 in KO(RP^n) gives the bound k >= 1 + phi(n) (gamma-operation argument), which is weaker
  than ht = n + 1. DROPPED for RP^n walls, reason recorded: the bounds coincide there. (Adams-type input could matter on
  other bases; see R2/R3.)
- R2 (cross-subject: K-theory of lens spaces). On L^{2m+1}(4) the class x has x^2 = 0 for every m, but L + L might be
  stably nontrivial. Complexify: L (x) C is the flat line of holonomy -1, i.e. eta^2. K(L^{2m+1}(4)) = Z[eta]/(eta^4 - 1,
  (eta - 1)^{m+1}) (Atiyah, from memory). Delivers: k >= 3 via the stable obstruction, and a gamma-operation lower bound
  growing with m. Needs: lens-space K-theory as an import. Fails if 2(eta^2 - 1) = 0 in K (it is 0 for m <= 2).
  (C1B is computing this order in work/C1B/klens.py; I leave the K-theoretic growth bound to C1B.)
- R3 (own: the spin Pontryagin class of L + L). A two-rung completion forces N = L (line with w1 = x), hence
  L + L stably trivial on ANY side. L + L is an oriented plane bundle carrying a canonical spin structure when x^2 = 0;
  its spin class q1 = p1/2 is an obstruction in ordinary integral cohomology. On L^{2m+1}(4) the plane bundle L + L is
  the square (rotor double cover) of the quarter-turn plane bundle eta, so q1(L + L) = 2 y^2, nonzero in
  H^4(L^{2m+1}(4); Z) = Z_4 for m >= 2. Delivers k >= 3 > ht = 2 on every side in dimensions 5 and 7, cohomologically.
  Needs: lens cohomology ring, q1 and p1(plane) = e^2 (Milnor-Stasheff), from memory.

Choice: R3 (with R2's complex computation as an independent cross-check in dimension 7), plus the elementary general
consequences of the parent clauses (definite side k = e(L) in every dimension; k <= 2 iff-condition on L + L stably).

Kill condition (pre-registered): R3 is dead if (a) q1(L + L) = 0 on L^5(4) and L^7(4) (e.g. y^2 = 0 in H^4, or the spin
structure of L + L is not the square of eta's), or (b) the K-theory cross-check on L^7(4) gives 2(eta^2 - 1) = 0, or
(c) the comparison wall L(4,1) x T^4 fails to have the same W(Sigma) (w = 1, x != 0 = x^2) and beta x != 0 as L^7(4).
Any of these: file nothing on T1 and record.

Outcome. Kill condition did not fire: q1(L + L) = 2y^2 != 0 for m = 2, 3 (both spin structures); 2(eta^2 - 1) reduces
to 2s^3 != 0 for m = 3 (0 for m = 1, 2); (c) see the coordination note below (the comparison clause was left to C1B).
Established:
- proved (from the parent's clause (1), elementary): on every side and in every dimension, k <= 2 forces L + L stably
  trivial (the complement line N has w1 = x, so N = L; the borrowed negative directions cancel only unstably); on a
  definite side k = e(L) exactly, in every dimension.
- proved given classical inputs cited from memory (lens cohomology, q1 = p1/2, p1 = e^2 for planes): q1 of a spin plane
  bundle whose Spin(2) bundle has Euler class a is 2a^2; L + L on L^{2m+1}(4) is the rotor square of the quarter-turn
  bundle, so q1 = 2y^2, nonzero in Z_4 for m >= 2; p1 = 4y^2 = 0 misses it. Hence k >= 3 > ht = 2 on every side,
  dimension 5 first (L^5(4) x R, physical side (1,5), explicit wall), every dimension >= 5 by products with tori.
- computed: explicit tame walls on L^{2m+1}(4) x R with physical sides (1, 2m+1) and (2m+2, 0) (c(x) embeds L in
  T*M, J-equivariant cometrics, det -t and t); e(L) <= 6 on L^7(4) (quaternionic odd map), so 3 <= k <= 6 there.
- computed (cross-check): complex K-theory sees the obstruction on L^7(4) but is blind on L^5(4); there only q1 sees it.
- argued (remark): in dimension 4 on closed walls q1 = 2a^2 = 0 whenever x^2 = 0 (and [X, BSpin] = H^4 for dim <= 7),
  so the stable obstruction never exceeds ht in dimension 4; the indefinite dimension-4 question stays open.
Proposal: synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial (title "Spin class of the doubled dying line
obstructs two rungs"). Gate: runcheck 5/5 pass; check4 exit 0, 0 errors, only I405 (two premises declared and
untouched, explained in coverage.yaml), no W413; validate_one ok, no codes; registered with propose_claim (moved aside,
files identical, coverage.yaml copied back, check4 rerun on the registered folder: exit 0). outside_ga declared
(imported: characteristic classes, K-theory cross-check). Ledger: transport-absent.
The problem stays partial: the exact count on L^5(4), L^7(4) (3 to 6), the dimension-4 indefinite case, and the
general integral datum for k >= 3 are open. Attack item 2 (the dim <= 3 table) was not attempted: it needs the
classification of bundles over 3-complexes by (w1, w2) imported as a Fact (maintainer-only), and its statement is
already recorded as argued in the problem's known text; my q1 remark is consistent with it (H^4 = 0 in dimension 3).

Coordination with C1B. C1B's findings (read midway) plan a K-theoretic proposal: k >= 1 + log2 ord(xi - 1) on every side,
k(L^7(4)) >= 3, gap unbounded in n, and the dimension-7 comparison pair L^7(4) against L(4,1) x S^4 for the success
clause's second branch. I drafted a comparison clause with L(4,1) x T^4 and removed it before filing, so as not to file
what C1B files; my proposal keeps what C1B's route does not give: the stable two-rung criterion on every side, k = e(L)
on definite sides, the integral obstruction q1 and the dimension-five case where complex K-theory is blind.

## T2 op.helicity-per-boundary-mode (J3 at the horizon, in GA)

Routes.
- R1 (problem's): import Regge-Wheeler / Teukolsky / Chandrasekhar as a Fact. Maintainer-only; not taken.
- R2 (the lead, GTG): reduce the massless and massive scalar and Dirac fields on the Schwarzschild exterior in GA in a
  GTG gauge, using the stored gauge fields (static coframe and connection, pairing.imported-schwarzschild-connection-curvature;
  PG gauge, singularity.connection-bivector-computed), to a two-dimensional equation per channel in the tortoise coordinate,
  with the coupling to the sphere and the mass carried by a factor that vanishes at the horizon.
- R3 (own): a uniform near-horizon argument (Rindler times sphere) for all spins: the angular operator always enters with
  a factor of the lapse. Delivers all spins at once but only to leading order; weaker than exact channel equations.

Choice: R2 for spin 0 and 1/2 (exact identities in Q(r)[s], s^2 = 1 - 2M/r), spin 1 if time allows.

Kill condition (pre-registered): R2 fails for a spin if, after conjugating out the measure factor, the channel operator
keeps a term not multiplied by a positive power of f = 1 - 2M/r (so the channel does not become a free two-dimensional
field at the horizon), or if the angular operator does not commute with the radial part (no separation). Prediction to
test, not to assume: for the Dirac field the coupling is proportional to sqrt(f), not f, so the potential decays as
exp(kappa r_*), not exp(2 kappa r_*), and the stored known text ("proportional to 1 - 2M/r" for all spins) is then wrong
for spin 1/2.

Outcome. Kill condition did not fire for spins 0, 1/2 or 1; the prediction was confirmed: the Dirac coupling carries
sqrt(f). Spin 1 was added (odd parity computed, even parity by duality). Established:
- proved (exact identities, derivation in the proof, verified at jet points of the stored static GTG field):
  scalar: f r (D.D phi + mu^2 phi) = (d_t^2 - d_{r*}^2 + V_l) u Y, V_l = f(l(l+1)/r^2 + 2M/r^3 + mu^2);
  Dirac: r f^{3/4} D(r^{-1} f^{-1/4} Phi) = (gamma^0 d_t + gamma^1 d_{r*}) Phi + (sqrt f / r) K Phi, the sphere operator
  T = gamma^0 gamma^1 K commutes with the radial operator, channels T Phi = lambda Phi give a 2D Dirac equation with
  coupling lambda sqrt f / r (and m sqrt f), squared potentials V_+- = lambda^2 f/r^2 +- lambda sqrt f (3M - r)/r^3;
  Maxwell: odd-parity potential psi(t,r) X_lm, D.F = (1/f)(d_t^2 psi - d_{r*}^2 psi + f l(l+1) psi/r^2) X, D(IF) = -I DF
  gives the even parity.
- proved: f = C(r) e^{2 kappa r*} with C regular; spin 0, 1 potentials decay as e^{2 kappa r*}, spin 1/2 as e^{kappa r*}
  (exact order sqrt f, coefficient +-lambda/(8M^2)); every channel tends to the free 2D equation (left/right movers).
  So J3 holds at the horizon for spins 0, 1/2, 1 (massive for 0 and 1/2). The problem's known text ("potential
  proportional to 1 - 2M/r ... e^{2 kappa r*}" for all spins) is wrong for spin 1/2.
- argued: non-uniform in l (C1B's R4 point, included in the proof as argued); the f^{-1/4} is the boost-weight-1/2
  rescaling.
- not established: spin 2 (linearised gravity), massive spin 1; completeness of the spinor harmonics is cited.
Proposal: synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional. Gate: runcheck 5/5; check4
exit 0, 0 errors, 0 findings; validate_one ok (info I213, I305 only); registered (moved aside, identical, coverage.yaml
copied back, check4 rerun on the registered folder: exit 0, 0 findings). Uses only
pairing.imported-schwarzschild-connection-curvature@7 (about: obj.synthesis.gtg-flat-spacetime-gauge-fields).
Ledger: transport-absent (recovers known physics in GA). The problem stays partial (spin 2).

## T3 op.odd-towers, attack item 1 (Fock ideals and mass formulas, dimensions 3 and 5 under P3)

Routes.
- R1: compute the minimal left ideals of Cl^0 of (2,1), (1,2), (4,1), (1,4) and their mass laws from scratch.
- R2: check whether the store already holds them (T14c entities dark-tower-matter.*), and whether they match the gauge
  algebras of synthesis.gauge-algebra-by-tower.
- R3: a pure-spinor reading of where mass begins (one constituent massless iff pure).
Choice: R2 first (do not redo settled work).

Kill condition (pre-registered): if the stored T14c results already give the ideals (S = Cl^0(V) f with commutant the
constituents' field), the mass laws in dimensions 3 and 5 at proved level, and agree with the gauge algebras, then
attack item 1 is answered in store and nothing is filed; the decision goes to Leon (update the problem record).

Outcome. Kill condition FIRED (as a "settled in store" finding): dark-tower-matter.constituents-field (proved, T14c
Thm 3.2) gives the minimal ideals S = Cl^0(V) f with commutant R (n = 3, dim S = 2) and H (n = 5, dim S = 8);
dark-tower-matter.where-mass-begins (proved, T14c Thm 3.5) gives the mass laws m^2 = 2<x x^dagger>_0, x = psi_1~ psi_2
(n = 3, mass at two constituents) and m^2 = (1/2)<x x^dagger>_0, x = psi~ psi (n = 5, one constituent), verified as
polynomial identities over Q in all six causal towers; dark-tower-matter.three-dimensional-content and
.five-dimensional-content give the Fock state spaces; synthesis.gauge-algebra-by-tower takes (a, F, b, K) from these and
gives so(2)+so(2) and u(3). Dimensions agree with std-algebra.fock-representation's odd-dimensional Fock halves
(Cl^0(2,1) = M2(R): R^2; Cl^0(4,1) = M2(H): H^2). Nothing filed; C1B reached the same verdict independently.
Proposal: none (attack item 1 is answered in store; the problem record does not cite it).

## Unexpected links
- T2 and C3 (the light-ray sea): J3 now holds at the horizon for spins 0 and 1 as well as 1/2, so integer-weight fields
  also contribute two-dimensional channels there; if the sea excludes them, that exclusion must come from statistics or
  the CAR count, not from J3 (argued).
- T2 and synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays: the Dirac channel's rescaling f^{-1/4}
  and its e^{kappa r*} rate (half the integer-spin rate) are the boost weight 1/2 of that result seen in the static frame
  (argued, cited in the T2 note, not filed).
- T1 and the stored L(4,1) result: the same rotor double cover that gave the explicit frame of R + L + L there gives
  here the canonical spin structure of L + L (its Spin(2) bundle is the quarter-turn plane bundle).
- T1 and C1B's K-theoretic proposal: complementary (q1 sees L^5(4) where complex K is blind; complex K gives the
  unbounded growth along L^{2n+1}(4)); they overlap only in k >= 3 on L^7(4).

## Decisions for Leon
1. (T1, imports) Import as one Fact the classical inputs both C1 proposals cite from memory: the integral and mod-2
   cohomology rings of L^{2m+1}(4) and T Sigma + R = (m+1) eta; the spin class q1 (2 q1 = p1, generating H^4(BSpin; Z))
   and p1 = e^2 for oriented plane bundles; the K-ring Z[eta]/(eta^4 - 1, (eta - 1)^{m+1}). Recommendation: import.
2. (T1, merge) synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial and C1B's
   synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height overlap only at L^7(4). Recommendation: keep both,
   no merge (different obstructions, different dimensions covered).
3. (T1, assumes) My T1 proposal carries assumes: sheaf.tameness@1, the same postulate edge as its parent. Recommendation:
   accept the edge (it is the setting, not a new premise).
4. (T1, wording) The lay level of synthesis.lens-space-wall-rung-count-sees-the-integral-twist says that with an
   indefinite side the price is set by the simple twist class alone; that is true in dimension three and false from
   dimension five on. Recommendation: scope the sentence to dimension three in the maintainer pass, and add to
   op.wall-class-invariant's known text that k = ht(x) on indefinite sides fails in every dimension >= 5.
5. (T2, status in a core region) hawking.joint-j3-s-wave-reduction is a modelling premise. With the T2 proposal accepted,
   J3 at the horizon is proved for spins 0, 1/2, 1 (massive 0, 1/2) from the stored static GTG field. Recommendation:
   keep J3 as a premise only for spin 2 (restate its scope), and correct op.helicity-per-boundary-mode's known text: the
   potentials are proportional to 1 - 2M/r for spins 0 and 1, to sqrt(1 - 2M/r) for spin 1/2.
6. (T2, imports) Completeness of spinor spherical harmonics (eigenvalues +-(j + 1/2)) and the exact/co-exact split of
   one-forms on the sphere are cited from memory. Recommendation: accept as cited (standard), or import one Fact.
7. (T3) Record op.odd-towers attack item 1 as answered in store: dark-tower-matter.constituents-field,
   .where-mass-begins, .three-dimensional-content, .five-dimensional-content, synthesis.gauge-algebra-by-tower; drop the
   item from the attack list and cite them in the known text. Recommendation: do so.
