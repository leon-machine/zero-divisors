# Findings, cluster L1 (horizons), run 2026-11-18-leads

Problems: op.which-capacity (leads 1 and 2), op.helicity-per-boundary-mode (lead 3), and the cross-link to
op.gravitational-field-at-null-momentum (cluster G). One attacker, both angles. Labels: proved / computed /
argued / conjectured. Work files: colony/runs/2026-11-18-leads/work/L1/.

## Orientation (lookups made)
- op.which-capacity and its eight entities; in full: synthesis.de-sitter-field-fixes-the-observer-tube-point (v4),
  synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries (v2, postulate),
  synthesis.wick-rotated-boost-selects-observer-tube-point.
- op.helicity-per-boundary-mode and its ten entities; in full:
  synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional (statement, check engine).
- Leads of 16 November: which-capacity "two finite computations posed", helicity "the even-parity Zerilli converse;
  a contained piece of analysis" (so lead 3 is the Zerilli converse, not the fuzzy sphere).
- op.gravitational-field-at-null-momentum and clause (i) of
  synthesis.gravitational-pair-production-from-the-operator-source-at-first-order (kernel of dimension six at
  Q(k) = 0: four displacements and two more).

## Leads 1 and 2: op.which-capacity

### Routes
R1 (the problem's own). Put the Schwarzschild and Schwarzschild-de Sitter fields in a gauge in which the horizon's
   Killing flow is the chart boost K = e1 e2 and the rotations act by conformal maps of the background, list the
   bivectors commuting with K that are symmetries, and compute the compatible tube points they fix. Delivers the
   clause's verdict. Needs: a classification of the so(3) subalgebras of the centraliser of K in the bivectors of
   Cl(2,4). Fails if adapted gauges do not exist or if the fixed set depends on the gauge in an uncontrolled way.
R2 (from the de Sitter theorem's other candidates). Compute the Killing-norm, free-fall and Tolman candidates in
   the static frame (lapse f): where the normalised norm sqrt(f)/kappa_h is stationary, for each horizon. Delivers
   what the unadopted candidates say; cannot decide what the clause says.
R3 (own; adversarial). A structural shortcut: a compatible tube point and its observer are related by the quarter
   turn of the Wick-rotated boost, which commutes with everything commuting with K; so "tube point fixed" is
   "observer fixed", and a region whose rotation orbits are spheres has no fixed observer. If right this decides
   both leads at once without choosing a gauge; if wrong (the quarter turn does not carry fixed points to fixed
   points) R1 has to be done gauge by gauge.

Choice: R3 with R1's classification as its algebraic content, then R2 for what the candidates give. Reason: R3
is gauge-independent within the class of gauges in which the clause can be read at all.

### Kill conditions (written before computing, 18 November)
K1 (classification). The claim "every so(3) in the centraliser of K is the transverse so(3) of one de Sitter
   tractor I with Q(I) > 0, and the compatible tube points it fixes are exactly x_perp = centre, rho^2 = 12/Lambda"
   dies if the exact computation finds, in the centraliser of K (dimension expected 7 = 1 + 6), a compact
   three-dimensional subalgebra whose invariant vector in span(e3, e4, e+, e-) has Q <= 0, or a fixed compatible
   tube point off that one orbit.
K2 (quarter turn). "A compatible tube point is fixed by a bivector commuting with K if and only if its observer
   x(m) is" dies if at any sample the two conditions differ.
K3 (the clause decides after all). The negative result for lead 1 dies if, in an adapted gauge of either horizon,
   some observer of the static region has an invariant tube point; for lead 2 likewise on the Schwarzschild
   exterior. (Then the clause does select, and the selected rho is to be computed.)
K4 (candidates, lead 1). "The norm, free-fall and Tolman candidates pick one observer for both horizons" dies if
   the stationary points of sqrt(f)/kappa_b and sqrt(f)/kappa_c differ or are not unique in (r_b, r_c).
   "Neither horizon has unit normalised norm there" dies if f(r_0) = 1.
K5 (Schwarzschild, lead 2). "No finite rho" dies if sqrt(f)/kappa has an interior stationary point on r > 2M.

Outcomes (work/L1/P1/check.py, exact, all five functions pass):
- K1 not triggered. Computed: the centraliser of K in the bivectors is 7-dimensional, K plus the six bivectors of
  T = span(e3, e4, e+, e-), signature (1,3). For six vectors I = alpha nO + c3 e3 + c4 e4 + beta ninf with Q(I) > 0
  the stabiliser is three-dimensional with negative definite Killing form and fixes exactly the compatible tube
  points x_perp = (c3, c4)/alpha, rho^2 = Q(I)/alpha^2 (the stored 12/Lambda at alpha = Lambda/6, beta = 1); for
  five vectors with Q(I) <= 0 the stabiliser is not compact and fixes none. The statement that every so(3) in the
  centraliser is such a stabiliser is proved by representation theory in the proof text, not by the check.
- K2 not triggered. Proved (two lines) and computed on a grid: for B in the bivectors of T, [B, X(m)] =
  [B, Re X(m)] = [B, X(x(m))], because Re X(m) and X(x(m)) differ by a vector of span(e1, e2).
- K3 not triggered. In the static chart of the wedge (Lambda = 3) the rotations move every point with s > 0 and
  fix exactly the hyperbola s = 0, Q(x) = -12/Lambda. A region whose rotation orbits are two-spheres maps into
  s > 0 under any equivariant displacement. So the clause's condition is met by no observer of the Schwarzschild
  exterior and by no observer of the static region of Schwarzschild-de Sitter, for either horizon's wedge.
- K4 not triggered. One stationary radius for both horizons, r_0^3 = 3M/Lambda (= 3 at the stored sample,
  r_0 between 36/25 and 13/9), f(r_0) = 1 - (9 Lambda M^2)^(1/3), between 3/28 and 10/91 at the sample, so
  kappa_h N_h(r_0) = sqrt(f(r_0)) < 1 for both horizons and N_c/N_b = kappa_b/kappa_c = 8/5.
- K5 not triggered. On Schwarzschild r^2 f' = 2M > 0: no stationary radius; sup sqrt(f)/kappa = 4M, not attained.

### What is established (leads 1 and 2)
- Proved (given the definition of an adapted gauge, which is the class of gauges in which the clause can be read):
  the clause's condition selects no observer and no finite rho on the Schwarzschild exterior, and none in the
  static region of Schwarzschild-de Sitter for either horizon. The chart scale of the one fixed orbit,
  rho_g^2 = 12/Lambda_g, is a parameter of the gauge (moved to any positive value by the dilation, which
  commutes with K), not of the field.
- Proved: the unadopted candidates (maximal normalised Killing norm, free fall, and, cited from memory, the
  Tolman-coldest observer) are one condition, f' = 0. Schwarzschild: no solution (asymptotic observer only, as
  the store had argued). Schwarzschild-de Sitter: one observer for both horizons, two scales in the ratio of the
  surface gravities, neither with unit normalised norm.
- So for lead 1: the clause does not decide between per observer and per horizon, and for a sharper reason than
  the stored one (it fixes nothing for either horizon, it is not merely silent on which). The norm candidate, if
  adopted, would give "foot per observer, scale per horizon". Lead 2: no finite rho.
- Transport-convenient: the content is conformal group theory plus static-patch geometry; what is specific to the
  series is the reading of the clause on compatible tube points.
- Caveat, a decision for Leon: read strictly ("m is invariant under every symmetry commuting with K") the clause
  cannot be met by any state of an exterior observer in these fields; the store reads the same situation for
  Lambda <= 0 as "rho stays free". The proposal states both readings and adopts neither.


## Lead 3: op.helicity-per-boundary-mode, the even-parity converse

### Routes
R1 (the problem's own). Closed forms for the even-parity linearised vacuum equations in the Regge-Wheeler gauge
   from the stored engine, then explicit reconstruction operators Psi -> (H0, H1, H2, K) with every vacuum
   equation of the reconstructed field a differential multiple of the Zerilli operator, identically in r and L.
   Needs: closed forms identically in radius and angle (the stored odd case has a grid and an argued degree
   bound); exact polynomial algebra in r, L and the jets, without sympy.
R2 (from the stored superpotential). Use the proved intertwiner d/dr_* + W between the odd and even operators and
   the proved odd equivalence: an even solution is (d/dr_* + W) of an odd one, whose field is a vacuum solution.
   Fails: the intertwiner relates master functions, not fields; an odd vacuum field is not an even one, so this
   gives no even-parity vacuum solution. It would need the Chandrasekhar transformation at the level of the field,
   which is not stored.
R3 (own; adversarial). Dimension count on a channel: on functions with d_t^2 = -omega^2 the even-parity vacuum
   system in the gauge reduces to a first-order system in r; if its solution space has dimension 2 per time phase
   and Psi is injective on it, the converse follows by counting. Needs the same closed forms; gives no explicit
   reconstruction.

Choice: R1, because it gives formulas a referee can perturb, and R3's count falls out of it.

### Kill conditions (written before computing, 18 November)
Z1 (closed forms). The engine's first-order Ricci vectors of the even-parity field must equal the closed forms on
   every second-order jet of (H0, H1, H2, K) and every 2-jet of the angular function, as an identity in sqrt f and
   in the polar angle together. Any component that differs kills the closed forms (and the route until repaired).
Z2 (converse). With the reconstruction operators fixed, each vacuum equation of the reconstructed field must be a
   differential multiple of the Zerilli operator applied to Psi, identically in r and L (M = 1 by homogeneity).
   A nonzero remainder after reduction by the Zerilli equation kills the converse as formulated.
Z3 (master function). The Zerilli-Moncrief function of the reconstructed field must be Psi plus a multiple of the
   Zerilli operator; a nonzero remainder kills "is the master function of".
Z4 (injectivity). On an oscillating channel a vacuum solution with Psi = 0 must vanish; if the difference
   H - Rec(Psi[H]) is not a combination of the vacuum equations and their derivatives (with 1/omega^2 allowed),
   the clause "the Zerilli function carries the whole even-parity channel" is not established.
Z5 (bonus, odd parity). If the two-variable exact engine runs, the stored odd-parity closed forms are tested as
   identities in radius and angle together; a failure would be a defect of the stored entity.

Outcomes (work/L1/P2/check.py, exact; scratch in work/L1/zer/):
- Tooling. Two exact rings with division by units only: U = Q[z, 1/z, 1/(1 - z^2), s, 1/s, c]/(c^2 = 1 - s^2)
  (z = sqrt f at M = 1, s and c the sine and cosine of the polar angle), carried by the stored jet engine, and
  A = Q[r, lam, w][1/r, 1/(r - 2), 1/(lam r + 3), 1/w] with linear forms in jet symbols. A first try with a
  gcd-reduced field Q(z)(w) was too slow (no case in 100 s) and was dropped; the unit ring runs a case in 0.08 s
  and never met a non-unit divisor.
- Z1 not triggered. Computed, as identities in radius and angle together: all sixteen components of the
  first-order Ricci vectors of the even-parity field equal the closed forms, on 24 basis jets times the 3 basis
  2-jets (P, P', P'') of the angular function (72 cases, 72 nonzero components). The 2-jet of P is free data, so
  no separation constant enters and no degree bound is needed.
- Z5 not triggered, and the stored weak spot is closed: the stored odd-parity closed forms hold as identities in
  radius and angle together (48 cases at L = 7/2 and 6; both sides are of degree one in L through S'' alone).
  The stored entity's "degree bound (argued)" can be replaced by this computation.
- Z2 not triggered. With K = a(r) Phi + f Phi', H0 = H2 = b(r) Phi + c(r) Phi' + (r - 2M) Phi'',
  H1 = d_t(r Phi' + e(r) Phi) (coefficients in the check; first written from memory of the Zerilli and
  Lousto-Price formulas, then verified, so nothing rests on the memory), every radial vacuum equation of the
  reconstructed field is a differential operator applied to the Zerilli operator on Phi: three vanish for every
  Phi, E4 = -(r d_r + e) Z, E7 = -(1/2) Z' + b' Z, E1 and E5 second order with leading coefficient -r/2.
- Z3 not triggered, with a normalisation found: the stored Zerilli-Moncrief function of the reconstructed field
  is (lam + 1) Phi, identically and without the Zerilli equation. So a solution Psi is the master function of the
  reconstruction of Psi/(lam + 1).
- Z4 not triggered, and more than asked: on an oscillating channel E2, E3, E4 are a first-order system in r;
  under it E1, E5, E7 are multiples of one algebraic relation (Zerilli's), which the system preserves; the Zerilli
  operator on the master function is a multiple of that relation; and (lam + 1)(K, H, H1) minus the reconstruction
  of the master function reduces to zero under the first-order system alone. So a vacuum solution with Psi = 0
  vanishes, and Psi is a bijection from even-parity vacuum solutions of the channel onto Zerilli solutions.

### What is established (lead 3)
- Proved (exact identities; M = 1 with the stored homogeneity; smooth fields; L > 2): the even-parity
  channel-reduction, both directions, identically. The cited fact (C3) of the stored entity is no longer needed;
  the sample-point rank computation of its clause (3) is superseded.
- Still cited from memory and not derived: (C1) completeness of tensor harmonics, (C2) reachability of the
  Regge-Wheeler gauge. Still open in the problem: l = 0, 1; charts regular across the horizon; the fuzzy-sphere
  identification (not attempted: the leads of 16 November name the converse as nearest); the current-boson
  identification and the partial-wave lift, which stay premise.
- Transport-absent: this is the classical Zerilli reduction, re-derived in the gauge-field formalism with every
  step exact. Its use to the series is that the even-parity clause of J3 need not be assumed.

### The other half of lead 3: the partial-wave identification from the fuzzy sphere (not taken)
The brief says to take the item the leads of 16 November call nearest; that is the converse above. Recorded so
that it is not skipped silently: out of reach in this run, because the identification asks for a map from the
bilinear sector of the boundary modes (Madore's fuzzy sphere under the indifference principle,
scrambling.principality-indifference-sphere, with scrambling.imported-kostant-madore-partition-data: Mat_n is
the sum of the su(2) representations l = 0, ..., n - 1, each once) to the partial-wave channels (omega, l, m, s)
of the fields, and the store holds no statement tying a field's harmonic of degree l to the fuzzy harmonic of
degree l. Two obstacles seen in the lookups: (i) the fuzzy sphere carries each l once, while a field of
helicity s has channels only for l >= |s| and the gravitational field has two per (l, m); (ii) the count is
per light ray by Leon's decision of 26 October, and the per-shell reading is recorded but not adopted. First
step someone would need: state the map as a premise or a theorem for spin 0, where l runs from 0 and there is
one channel per (l, m), and test it against the stored s-wave reduction at l = 0.

## Cross-link: two undetermined components at null momentum against the two-dimensional horizon channels
Question from the brief: the operator-source result counts two undetermined components at null momentum (clause
(i) of synthesis.gravitational-pair-production-from-the-operator-source-at-first-order); the horizon channels of
the linearised field are stored as two-dimensional. Same two, or a coincidence?

Kill condition (written before the lookups): "same two" dies if the stored "two-dimensional" counts components
of the field (then the comparison is of like with like and must match channel by channel), or if the two free
directions at null momentum are not split one and one by the reflection that separates the parities.

Answer (argued, with two small exact facts; no proposal):
- The "two-dimensional" of the stored titles is not that two. It is the dimension of the reduced equation: each
  channel is one function of (t, r_*). Read literally, the coincidence of the word is a coincidence.
- The count that does correspond is the other one in the stored result: two channels, the two parities, for each
  (omega, l, m). That is the same two as the null-momentum count, in this sense. Cluster G's findings of this run
  identify the two free directions at null k as the transverse trace-free maps n_+ and n_x (kernel of the
  Einstein map = displacements + these two). For a radial null momentum k = gamma_0 +- gamma_1 and the transverse
  frame (gamma_2, gamma_3), the reflection gamma_3 -> -gamma_3 (phi -> -phi) fixes k, commutes with the Einstein
  map, and has n_+ = gamma_2 gamma_2 - gamma_3 gamma_3 even and n_x odd (computed, trivially). The same reflection
  fixes the even-parity field of the Regge-Wheeler gauge (no gamma_3 mixing; its first-order Ricci vector along
  gamma_3 is a multiple of gamma_3, clause (1) of this run's proposal) and reverses the odd-parity one
  (k_phi along gamma_0, gamma_1). So per mode: one even and one odd free direction on both sides.
- Flat limit (computed): at M = 0 both stored potentials are L/r^2, so the two parities obey one and the same
  radial equation, the spherical-wave form of the two free directions of the flat first-order field.
- What is not shown: a map from the flat kernel at each null k to the pair (Q, Psi) of master functions (a
  partial-wave expansion of n_+, n_x in tensor harmonics; it needs the completeness fact (C1), cited from memory).
  And the link says nothing about whether those directions carry states: both sides are source-free solutions
  of the first-order equation, which is what op.gravitational-field-at-null-momentum asks about.
- Use for cluster G: the solutions counted by the two null-momentum directions are, around a static hole, exactly
  the pairs (Q, Psi) of solutions of the Regge-Wheeler and Zerilli equations (odd part stored; even part this
  run's proposal). Any statement G makes about "the free part" on a black-hole background can be phrased on those
  two functions per (omega, l, m); near the horizon each is a free wave in (t, r_*).

## Unexpected links
- To cluster G (op.gravitational-field-at-null-momentum): above.
- Within L1: the adopted tube-point clause and the horizon channels share the static frame's limitation. The
  clause can be read only in a gauge adapted to one horizon; the channel statement "free at the horizon" holds in
  the static frame of one horizon. In Schwarzschild-de Sitter each horizon has its own adapted gauge (the Killing
  flow is the chart boost of one bifurcation plane only: the fixed set of K in the conformal completion is one
  two-sphere), so no single gauge reads the clause for both horizons at once. Argued, not filed.
- To op.null-positivity-curved-horizons and the stored Kay-Wald Fact
  (synthesis.imported-kay-wald-uniqueness-and-no-go: no stationary Hadamard state on extended Schwarzschild-de
  Sitter): the clause's support was the uniqueness of the symmetric Hadamard state on de Sitter. On
  Schwarzschild-de Sitter no such state exists at all, which fits the clause having nothing to say there. Noted
  only; not computed.
- The ring trick (jets over a ring in which only units are inverted) turns any of the store's "grid plus argued
  degree bound" checks on the static field into identities. Candidates: the stored scalar, Dirac and Maxwell
  horizon-channel result, if its checks are sampled in the angle.

## Proposals filed
1. synthesis.tube-point-clause-fixes-no-observer-where-rotations-have-no-fixed-point (restated in the fix round, see below; op.which-capacity, leads 1
   and 2). validate_draft ok; check4: 0 errors, 0 other findings (after two weak-mutation warnings were removed
   by tightening two check functions; one run of check4 overlapped another agent's by mistake, about 17 s).
2. synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations
   (op.helicity-per-boundary-mode, lead 3). validate_draft ok; check4: 0 errors, 0 other findings (82 s).
Third slot not used.

## Decisions for Leon
1. The tube-point clause where no observer meets its condition (Schwarzschild, Schwarzschild-de Sitter): read it
   as silent, so that rho is a free datum of the state there (the stored reading for Lambda <= 0; then
   op.which-capacity is answered by its last alternative for both fields), or as excluding such states, or add a
   premise. Recommendation: silent, and say so in the clause's text; the alternative that excludes every
   black-hole exterior state cannot be meant.
2. Whether to adopt the norm rule as the further premise for two horizons. What it would cost and give: foot per
   observer (the free-fall radius r_0^3 = 3M/Lambda), scale per horizon (ratio kappa_b/kappa_c), no observer on
   Schwarzschild at finite radius (scale 1/kappa only as a supremum), and it loses the de Sitter property that
   the normalised norm is exactly one. No recommendation; it is a new premise with no support beyond the de
   Sitter coincidence.
3. Joint J3 (postulate): narrow it again (its version 4), dropping the channel reduction for even-parity spin 2,
   which now follows given (C1) and (C2); and decide whether (C1), (C2) are imported as Facts (they are textbook:
   completeness of tensor harmonics, reachability of the Regge-Wheeler gauge for l >= 2).
4. The stored result synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional: its
   title ("even one way"), clause (1) ("degree bound (argued)"), clause (3) and clause (5) can be restated to cite
   the new result. Maintainer wording, no change of mathematics.
5. op.helicity-per-boundary-mode after this: what is left of the spin-2 item is l = 0, 1, charts regular across
   the horizon, and the harmonic-analysis inputs; the fuzzy-sphere identification is untouched.

## Fix round (referee report verify/R-B.md)

### B1, the referee's counterexample to clause (iv): test before restating
Claim under test: from a gauge adapted in my sense, with chart (eta, sigma, n), displace by
psi(eta, sigma, n) = (eta, sigma, R_J(-c eta) n), J in so(3)_I, c != 0. Then K generates the symmetry
xi/kappa + cJ, the symmetries commuting with K are spanned by K and J and are bivectors, and the observers on
the axis of J meet the clause's condition at every sigma.
Kill conditions for the counterexample (written before computing): it dies if (a) the chart boost conjugated
back by psi is not the old boost composed with a rotation about J (then K is not a symmetry in the new gauge);
(b) J does not commute with psi, or a symmetry commuting with K fails to be a bivector; (c) the axis points
X(eta, sigma, +-n_J), sigma > 0, are not fixed by J, or their compatible tube points are not; (d) the axis points
lie outside the region (they do not: the poles of each sphere of the region). If none fires, clause (iv) as filed
is overstated and is restated.
Outcome (work/L1/fix/helical.py, exact; now check_twisted_gauge_selects_the_observers_on_the_rotation_axis in the
proposal): none of (a) to (d) fired. The conjugated boost equals the boost times a rotation about J on 72 points;
J commutes with K and with I; J fixes the axis points at every sigma > 0 (18 samples) and their compatible tube
points, with foot the centre and rho = 2 sqrt(1 - sigma^2)/(1 -+ sigma) = 2/3, 1, 4/3, 3, 4, 6 at Lambda = 3;
the whole so(3) fixes none of them. The referee is right and my clause (iv) was overstated: "every gauge in
which the clause can be read" was false; the proof needs K to generate the horizon's own flow.

### B1, what changed (verdict OVERSTATED, accepted)
- Conclusion reversed: "in every gauge where the clause can be read no observer meets it" is withdrawn. True
  statement: in gauges where K generates a positive multiple of the horizon's Killing field and the rotations
  act by bivectors, no observer of the region meets the condition (Schwarzschild; either horizon of
  Schwarzschild-de Sitter). In the twisted gauge, where K generates the horizon flow plus a rotation, the
  observers on the axis meet it at every scale. New clause (vii) states this; it is conditional on the two
  fields having no symmetries beyond the Killing flow and the rotations (standard, cited from memory).
- Restated at every level: title ("Tube-point clause on black-hole fields: empty for the horizon flow,
  reading-dependent"), one-liner, lay, technical, formal (iv), (v), (vi) wording, closing paragraph (three
  readings (a), (b), (c); (c) argued), extraction note and decisions. The id's slug no longer describes the
  result; proposed slug: synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-
  reading-dependent (renaming is the orchestrator's).
- Referee's wording fixes applied: "symmetries commuting with K other than K" throughout, with the proof that K
  fixes no compatible tube point in any field; the surface-gravity normalisation dropped from the definition;
  the sentence "these are the gauges ... the hypotheses of the clause" deleted; the chart-dependence of Lambda_I
  said to hold in de Sitter too (the difference is that the fixed orbit lies in the region there); the
  positivity line in (iii); the general-lapse connection form derived in the proof; the two representation-
  theory facts labelled standard; the stored clause's and the open problem's "decides one-horizon fields"
  flagged as inaccurate in the decisions.
- Check: new function for (vii); the complex-multiple branch of fixes_tube, which the referee found dead, is now
  exercised (the bivector Im X ^ Re X fixes the tube point with multiplier -+ I7 rho^2). runcheck: six PASS.
- Nothing declined.

### B2, what changed (verdict SOUND WITH FIXES, all four applied)
1. Clause (6), proof, technical, one-liner, extraction note: the stored clause (3) is superseded on oscillating
   channels only; without a condition on the time dependence the forward implication stays as stored, at samples.
2. Homogeneity: omega has weight -1 (w weight -2), with the weights of a, b, Z, Rel listed in the proof.
3. (C3) described as stored (surjectivity alone, clause (4) here); the forward implication and injectivity are
   what the stored clause (5) needs beyond it; "given (C1) and (C2)" moved inside clause (6).
4. "real" dropped where it is not used: the identities of (5) need only omega^2 != 0.
No conclusion reversed. Nothing declined. runcheck: five PASS. check4: pending (orchestrator), both proposals.

### Decisions for Leon, as changed by the fix round
Decision 1 above becomes a decision about the clause's wording: (a) K is the horizon's Killing flow (then no
observer on these fields, and rho free or the state excluded, as before); (b) K any symmetry, as worded (gauge
dependent; an axis in the twisted gauge); (c) only bivector-acting symmetries count (can be made empty).
Recommendation: (a), written into the clause, with "other than K" and "silent where nothing is fixed"; and
reword "decides fields with one horizon only" in the clause and in op.which-capacity, since Schwarzschild has one
horizon and is not decided.

### Second pass on B1 (verify/R2-ABC.md): two statements tested before writing them
Kill conditions (written before computing): (1) "read as every symmetry commuting with K that is not a multiple
of K, the condition is met in no field with such a symmetry, de Sitter included" dies if some a K + B, a != 0,
B a bivector of T, fixes a compatible tube point, in particular a point that B fixes. (2) "in the de Sitter field
the symmetries commuting with K + cJ are spanned by K and J" dies if the kernel of B -> ([B, I], [B, K + cJ]) on
bivectors has dimension other than 2 at the sample values of c and Lambda.
Outcome (work/L1/fix/second.py, exact; both now in the proposal's check): neither fired. (1) a K + B fixes no
compatible tube point on the grid (3024 cases; proved in general in the proof: the span(e1, e2) component cannot
be a complex multiple of u). (2) The de Sitter symmetry algebra has dimension 10 and the centraliser of K + cJ in
it has dimension 2, at Lambda = 3, 12, 4/3 and c = 1, 3/7, -2. So the twisted gauge exists in de Sitter, and the
stored clause's claim to fix rho there rests on reading (a) too.
Applied: the preamble states the reading used (the rotations among the symmetries commuting with K) and the wider
reading's outcome; clause (vii)'s condition weakened to "the symmetries commuting with a xi + cJ are spanned by xi
and J"; the de Sitter remark in the closing paragraph, the technical level and decision (1); the id in check.py
line 1. The stored entities are not edited. runcheck: six PASS.
