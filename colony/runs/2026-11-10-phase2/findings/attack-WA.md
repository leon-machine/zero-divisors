# attack-WA: cluster W, angle A (constructive). Run 2026-11-10-phase2

Status: PRE-REGISTRATION (written before any computation of this run). Labels: proved / computed / argued / conjectured.

## Orientation (read, no computation)
Stored entities read in full (formal level, and proofs/checks where used): synthesis.window-reading-array-killing-energy v2,
synthesis.half-integer-weight-array-carries-half-ln2 v5, synthesis.counted-unit-energy-at-half-offset v3,
synthesis.null-ordering-of-counted-units-is-zeta-symmetric v4, singularity.q-joint-quasi-freeness-s-wave v3,
scrambling.residue-each-convention v4, synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping v1,
synthesis.array-ln2-is-zero-mode-doublet-one-tower v6, synthesis.imported-theta-function-identities v2,
synthesis.residue-from-mode-entropy v4, synthesis.clausius-is-window-first-law-plus-boost-charge-conservation v3,
synthesis.positive-null-energy-gives-r-premises v9, hawking.i-state-continuum v5, synthesis.n-plus-null-ground-state v12,
synthesis.quarter-from-temperature v1, synthesis.de-sitter-mode-count v3, pred.boundary-mode-density v3,
op.residue-killing-weights, op.counted-mode-energy; phase 1 bridges.md Job 1 and REPORT.md.

Notation fixed here: beta = 2 pi/kappa the thermal period; L the window length in Killing time; r = L/beta the window
length in thermal periods; delta in [0,1) the twist (offset) of an array, weights (2 pi/L)(k + delta); x = beta omega;
s(x) = ln(1 + e^{-x}) + x/(e^{x} + 1).

## W1. Exact array-against-continuum comparison
Routes.
1. (the problem's own) theta/eta at tau = I_4/r with the stored theta Fact: ln Z(r) = ln(theta_3/eta)(I_4 r), self-dual
   under r -> 1/r; energy, entropy, variance by differentiating in beta. Delivers closed forms and the fixed-point
   reading. Needs only clauses (a), (b) of the Fact for the duality; derivative formulas of theta functions are NOT in
   the Fact, so anything using them is flagged.
2. (another subject) Poisson/Euler-Maclaurin: the array sum is the midpoint rule for the continuum integral; the dual
   channel is the Poisson remainder. Delivers the sign and size of the entropy difference with elementary bounds, no
   modularity.
3. (own) monotonicity: E(beta) strictly decreasing in beta (variance positive), so the zero of the symmetric energy at
   r = 1 is the only one. Delivers uniqueness of the fixed point.
Choice: route 1 for the identities, route 3 for uniqueness, route 2's elementary bounds for the sign of the entropy
difference at every r. Reason: route 1 is what the stored proofs already use, so the new result composes with them.
Kill condition (pre-registered): the "fixed-point identity" reading is dead if (a) the symmetric-ordered energy of the
antiperiodic circle vanishes at some r != 1, or the above-sea energy equals the continuum's pi r/12 at some r != 1
(then the match is not tied to r = 1); or (b) the entropy difference Delta(r) = S_array(r) - pi r/6 is not
2 sum_n [ln(1 + e^{-y_n}) - y_n/(e^{y_n} + 1)], y_n = 2 pi r (n - 1/2), or its values at r = 1, 2 are not
(1/2) ln 2 - pi/6 = -0.1770 and about -0.0197 (the bridge-hunter's numbers; if my exact bounds exclude them the
phase 1 evidence paragraph on op.residue-killing-weights is wrong and I say so); or (c) the stored variance
0.798 per array is not reproduced. Expectation written before computing: Delta(r) < 0 for every r > 0 and
Delta(r) ~ -2 (pi r - 1) e^{-pi r}.

## W2. Construction of the array from a light ray's continuum over one window
Routes.
1. Restriction: the subalgebra of the continuum on an interval of Killing time with the restricted I-state. Delivers
   an entropy if the restricted state has one. Fails if the restricted algebra is type III (expected; then the entropy
   is infinite and only a vacuum-subtracted number, from the literature, is available).
2. Compression: the one-particle Killing generator -I_4 d/dtau on L^2(window) and its self-adjoint realisations.
   Delivers the list of boundary conditions and whether the antiperiodic one is singled out. Needs elementary operator
   theory (deficiency indices of the first-order operator on an interval).
3. (own) Floquet decomposition of the continuum under the one-window Killing translation: L^2(R) as a direct integral
   over the twist delta of the twisted windows. Delivers the array as a fibre and the continuum's extensive values as
   twist averages. Fails if the twist average of the array's entropy is not the continuum's entropy rate times the
   window.
Choice: route 3 as the main construction, with route 2 as its boundary-condition statement and route 1 reported
(argued, literature from memory) for comparison.
Kill condition (pre-registered): the phase 1 verdict "different objects, the reading equates mean energy only" is
dead if some natural construction (restriction, compression, fibre) yields, WITHOUT inserting the antiperiodic
condition and the Gibbs state by hand, the product Gibbs state of (Q) version 3 on a subalgebra of the continuum in
the I-state (then the array is a subsystem and its (1/2) ln 2 is a continuum entropy). My own conjecture to be killed:
"the twist average over delta in [0,1) of S_delta(r) equals pi r/6 exactly, and likewise for ln Z, energy above the
sea and variance"; it dies if the exact computation gives any other value, or if S_{1/2} is not the minimum over the
twist. Second pre-registered test: if the antiperiodic condition follows from (N+) or (Q)'s KMS clause by a
derivation in the store, the "put in by hand" verdict is dead (stored text to check: (N+) "Not part of this premise:
the weight clause"; positive-null-energy (iii) "its weight clause ... is not given").

## W3. Absolute entropy or differences
Route: direct audit of stored statements (which results use sum s = A/4 or N ln 2 = S_BH; which use only
delta S = eta delta A), with `cone` over the count results; then the conditional arithmetic.
Kill condition (pre-registered): the claim "only the count uses the absolute value" is dead if a stored result on the
Clausius/Einstein route uses an absolute window entropy, or if a count result is derivable from differences alone.
The number in RUN.md, 3/(4 pi) "per component", is to be checked: my expectation before computing is that 3/(4 pi) is
per two-component unit and 3/(2 pi) per component; if the arithmetic gives otherwise I record it.
pred.boundary-mode-density kill condition (quoted from the store): "A derivation of the calibration residue from the
boundary modes returning any other value, which refutes the intrinsic-clock premise (IC)". Test: is any construction
of W2 such a derivation.

## W4 (findings). The premise that would equate entropies; who silently assumes it
Route: `cone` (future) of synthesis.window-reading-array-killing-energy; read each dependant for use of entropy or
variance of the continuum. Kill condition: the finding "no stored result silently assumes entropy equality" is dead
if one dependant uses the continuum's entropy over a window or equates the array's variance with the continuum's.

## RESULTS (after computing; the pre-registration above is unchanged)

Sibling: attack-WB.md read twice (midway and after WB finished). WB filed
synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter; not duplicated. The coordinator's
four exposures (twist one half at every level of P1; clause (v) counterfactual; the ordering sentence and the
"arrays that fail the energy tests" sentence in P2; the temperature and Clausius forms) are applied.

### W1. Kill conditions (a), (b), (c): none met. Proposal P1.
- proved (given the imported theta Fact, clauses (a), (b) only): ln Z(r) = ln Z(1/r) for the antiperiodic array on r
  thermal periods; dual form ln Z = pi r/12 + c(r), c > 0.
- proved: beta E_sym(r) = e_sym(r) is odd under r -> 1/r, negative for r < 1, positive for r > 1 (thermodynamic
  monotonicity). The three stored energy equalities (sea against boost ground state; energy above the sea against
  pi r/12; symmetric energy against 0) each hold only at r = 1, and are the one identity
  sum (2n-1)/(e^{(2n-1) pi} + 1) = 1/24, i.e. f'(1) = 0. Temperature form: array of spacing kappa at temperature
  r kappa/2 pi against the continuum over the window 2 pi/kappa in the null ordering: mismatch (kappa/2 pi) r D(r),
  zero only at the Hawking temperature (and in the zero-temperature limit). All at twist one half.
- proved: S(r) = pi r/6 + Delta(r), Delta(r) = 2 sum [ln(1 + e^{-y}) - y/(e^{y} + 1)], y = 2 pi r (n - 1/2);
  Delta < 0 for EVERY r > 0 (termwise for r >= 1/2, direct bound for r < 1/2);
  Delta = -2 (pi r - 1) e^{-pi r} + rho, |rho| <= 3 pi r e^{-2 pi r} for r >= 1; Clausius form
  Delta(r) = int_0^r (1/rho) d(rho D(rho)).
- computed (certified rational intervals): Delta(1) = (1/2) ln 2 - pi/6 in (-0.17703, -0.17702);
  Delta(2) in (-0.019693, -0.019692); Delta(4) = -8.067e-5; Delta(8) = -5.87e-10; Delta(1/2) = -0.23464;
  Delta(1/4) = -0.13080 (Delta is not monotone below r = 1). The bridge-hunter's values stand.
- proved + computed: variance v(r) = pi r/6 + 2 sum y n [y (1 - n) - 2] > pi r/6 for r >= 1; v(1) in
  (0.79821, 0.79822), 0.2746 above pi/6; v(2) - pi/3 = 0.100.
- computed, NOT claimed: v(1) = pi^4/(24 Gamma(3/4)^8) = (pi^2/24) theta_3(I)^8 and
  beta E_sym(r) = (pi r/12)(theta_4^4 - theta_2^4)(I r) (floating agreement to 12 digits; need Jacobi's derivative
  formulas and the lemniscatic constant, which are not in the stored Fact).
- Premises used: synthesis.imported-theta-function-identities@2 (imported); stored theorems half-ln2@5,
  counted-unit-energy@3, null-ordering@4 clauses (i) to (iii) only, boundary-mode-thermal-entropy@2. No postulate is
  assumed by the statement, but null-ordering@4 carries an assumes edge to the window reading (for its clause (iv)),
  so the graph will show the reading in P1's cone.
- Transport-absent.

### W2. My conjecture (twist average) survived; the kill condition on the phase 1 verdict is NOT met. Proposal P2.
- proved (elementary): splitting each Killing frequency as (kappa/r)(k + delta) is a unitary of the continuum's
  one-particle space onto L^2([0,1), d delta; l^2(Z)); it carries the I-state to the Gibbs arrays A(delta, r) fibre
  by fibre and the one-window flow to the phase e^{2 pi I delta}. The array of (Q) v3 is the fibre delta = 1/2
  (flow -1), (Q) v2 the fibre delta = 0. No vector of the continuum lies in one fibre: the array is a fibre (a
  quotient of Killing time with a sign), not a subsystem. This is stored clause (iv) ("vanishing Mellin width") in
  exact form.
- classical, boundary form computed: self-adjoint realisations of the Killing generator on one window are exactly
  the twists; none preferred. KMS and quasi-freeness hold in every fibre, so the antiperiodic condition is an input
  ((Q)'s weight clause, a decision by the stored text), not derived from (N+) (stored: "is not given").
- proved: A(delta, M r) is exactly the product of A((j + delta)/M, r), j < M; S, e, v and the zeta sea add. So the
  (Q) array is A(1/4, 1/2) x A(3/4, 1/2), two particle-hole conjugate arrays of spacing 2 kappa with (1/4) ln 2 each.
- proved (identity elementary; values given the theta Fact): twist averages of S, e, v are pi r/6, pi r/12, pi r/6;
  of the zeta sea 0 (boost ordering), not the null-ordered -pi r/12.
- computed (certified): at r = 1, S_{1/2} = 0.3466 < S_{1/4} = 0.51375 < pi/6 < S_{6/25} < S_0 = 0.72039;
  S = pi/6 at a twist in (6/25, 1/4) (float: 0.24158), not particle-hole symmetric. NOT claimed: that 1/2 and 0 are
  the extremes over the whole circle (sampled only).
- argued (literature from memory: Powers-Stormer; Calabrese-Cardy, Casini-Huerta): restricting the I-state to a
  window gives no array state (occupations 0.165, 0.036, 0.021 against Gibbs 0.041, 8e-5, 1.5e-7; n_k x_k -> 1/pi,
  float quadrature in work/WA/explore2.py), entropy infinite; finite subtracted part 0.217 at r = 1.
- Answer to the RUN.md question: no natural construction gives (1/2) ln 2 unless the fibre 1/2 and its Gibbs state
  are put in; pi/6 is the uniform twist average (and the value at one non-symmetric twist); restriction gives
  neither. Boundary condition: put in by hand through (Q), not derived from (Q)'s KMS clause or (N+).
- Does it meet refutation condition (a) of the window reading? No: the fibre's energy above its sea is
  unambiguous (pi/12 at r = 1, equal to the continuum's boost-ordered value), but no ordering of the sea is derived.
- Premises used: hawking.i-state-continuum@5, positive-null-energy@9 (spectral form; clause (iii), (iv)),
  theta Fact@2 (values only), half-ln2@5, boundary-mode-thermal-entropy@2, null-ordering@4 (i), (ii),
  residue-from-mode-entropy@4 (the value S_0). Transport-absent.

### W3. Kill condition not met (agrees with WB's audit, done independently on the formal texts).
- argued (text audit, not a full-cone proof): absolute entropy is used by the count only:
  synthesis.residue-from-mode-entropy (hypothesis sum s = A/4), half-ln2 (iii), counted-unit-energy (iii),
  the-residue-requires, scrambling.residue-each-convention (N_epoch ln 2 = S_BH), synthesis.de-sitter-mode-count,
  pred.boundary-mode-density. The absolute A/4 itself comes from differences plus a zero point
  (synthesis.quarter-from-temperature: dS = dM/T and S -> 0 as M -> 0). Differences only:
  synthesis.clausius-is-window-first-law (clause 2 on point-spectrum windows; clause 7 on the continuum as relative
  entropy), synthesis.einstein-equations-from-c-loc-and-clausius (delta S = eta delta A, G = 1/(4 eta)).
- Consequence, stated precisely: with the counted entropy the array's Gibbs entropy, the count is internally
  consistent and the continuum enters no entropy statement. Counterfactually, with pi/6 per component per modular
  period: 3/(4 pi) = 0.23873 units OF TWO COMPONENTS per Planck area per period (RUN.md's "per component" should
  read "per two-component unit"), 3/(2 pi) = 0.47746 components; ratio 3 ln 2/pi = 0.66190 for every grouping;
  the registered value would need a mean of 6 ln 2/pi = 1.3238 components per unit; de Sitter count 3 N^2 in place
  of pi N^2/ln 2 = 4.5324 N^2. (computed, P1 clause (v).) New: for arrays of window r the count per modular period
  is r/(4 S(r)), 0.7213 at r = 1, 0.4866 at r = 2, -> 3/(2 pi): the capacity value ln 2 for two arrays exists only
  at r = 1.
- pred.boundary-mode-density, kill condition quoted: "A derivation of the calibration residue from the boundary
  modes returning any other value, which refutes the intrinsic-clock premise (IC)". Not met and not probed: every
  number above uses the area-law hypothesis (the stored circularity fence: residue-from-mode-entropy calls such a
  statement "a conditional reformulation, not an admissible derivation"), and P2 derives no residue.

### W4 (findings).
- The premise that would equate entropies: "the counted object on a light ray is the continuum per modular period"
  (uniform weight on all twists) in place of "the fibre of twist 1/2". It is not an extension of the window
  reading: by P1 (ii), (iii) equal entropies at fixed window need equal energies along the Gibbs family, which fail
  off one temperature (WB's W4; my Clausius form proves the integral identity).
- argued (word-level audit of the 7 entities in the future cone of the window reading, listed by `cone`:
  null-ordering, one-window-parity-recurrence, light-ray-recurrence-test, capacity-and-sakharov, mass-terms,
  no-single-curvature-coupling, the-residue-requires): none uses a continuum window entropy or compares variances;
  they use the sea constant -kappa/24 and the Hawking state's energy 0.

## Proposals
1. synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r (P1, base statement of W1; W3
   arithmetic as clause (v)). Gate: see the last lines of this file.
2. synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages (P2, W2).
   Gate: see the last lines of this file.

## What failed or was not done
- No proof that S_delta(1) is extremal at twists 1/2 and 0 (needs the Jacobi transformation with a second argument,
  not in the stored Fact).
- No closed form for the variance or for e_sym in theta constants inside the store's Fact.
- The restriction statement (type of the window algebra, infinite entropy) is argued from literature, not proved.
- The audits (W3, W4) are text audits of formal levels and proofs by search, not clause-by-clause proofs over the
  full joint cone.

## Unexpected links
- WB's second fixed point (r, delta) = (1/2, 1/4) is not independent of (1, 1/2): by P2 (iii) the (Q) array is
  A(1/4, 1/2) x A(3/4, 1/2), two particle-hole conjugate halves, so each half inherits half of every energy and of
  the entropy, (1/4) ln 2. WB's third point (sqrt(2/3), 1/3) is not of this kind.
- The above-sea match e = pi/12 at r = 1 is not unique in the twist: e_delta(1) crosses pi/12 again near
  delta = 0.12 (float scan; e_0 = 0.0235, e_{0.1} = 0.245, e_{0.2} = 0.315). Only the sea condition (double root) or
  particle-hole symmetry singles out 1/2. Consistent with WB's conic.
- pi/6 per channel per thermal period is the entropy FLUX of a chiral complex fermion at temperature T (energy
  flux (pi/12) T^2, entropy flux twice that over T; from memory, the single-channel bound of Pendry 1983). So the
  two numbers are "entropy of the fibre of twist 1/2" and "entropy flowing through the generator per modular
  period". Any future stored statement of the entropy radiated per period per channel has to choose (WB's
  evaporation-ledger remark is the same point).
- Bridge to cluster N: under the counterfactual the de Sitter count is exactly 3 N^2, with no ln 2.
- The M-fold decomposition says the twists of a window of M periods are the M-th roots of -1 in the plane of the
  unit; twist 1/4 is the quarter turn J itself.

## Decisions for Leon
1. Scope sentence of the window reading (v3?): add "at twist one half the three energy equalities hold only at
   window length one thermal period and are one identity (the self-dual point)", citing P1 if accepted.
   Recommendation: yes. Related (WB's item): the clause "in every state" is true only at the sea and the Hawking
   state under equal-temperature matching; recommend restricting it.
2. Whether to record on (Q) v3 / (N+) that the array is a fibre of the continuum (twist 1/2 of the one-window flow)
   and not a subsystem, citing P2. Recommendation: yes, one sentence in the window reading's cost paragraph.
3. Which entropy the count uses (attack item 4 of op.residue-killing-weights): my recommendation is to close the
   item with "the array's, by decision; the continuum's value is the twist average and the per-period flux, and
   counting it is not a consistent extension of the energy reading", and to keep 3/(4 pi) as a recorded
   counterfactual only.
4. RUN.md / op text: "3/(4 pi) units per Planck area per component" should read "per unit of two components"
   (3/(2 pi) per component).
5. Maintainer-only imports if wanted: Jacobi's derivative formulas and theta_3(I) = pi^{1/4}/Gamma(3/4) (would make
   the variance pi^4/(24 Gamma(3/4)^8) exact); the Jacobi transformation with a second argument (would prove the
   extremal twists); von Neumann's extension theorem, Powers-Stormer, the interval entropy formula (P2 (ii) and its
   Remark cite them from memory).
6. P1 and P2 cite null-ordering@4, which assumes the window reading, only for its clauses (i) to (iii). If Leon
   prefers the two results to sit outside the reading's cone, the density kappa^2/(48 pi) can be cited from
   synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit instead (maintainer edit).

## Gate status
P1 synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r: runcheck 5/5 pass; check4 exit 0,
0 errors, 0 warnings (check.py unchanged since); validate_one ok after the final wording edits (first run: W215,
fixed by citing three premises in the proof); registered with propose_claim (accepted_for_review true, I305 only);
coverage.yaml copied back.
P2 synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages: runcheck 4/4
pass; check4 exit 0, 0 errors, 0 warnings (first run: W413 on the frequency check, fixed by pinning its literals);
validate_one ok; registered with propose_claim (accepted_for_review true, I305 only); coverage.yaml copied back.
Working copies in work/WA/<id>/; pre-registration folders moved to work/WA/aside/. Total proposals from WA: 2.
