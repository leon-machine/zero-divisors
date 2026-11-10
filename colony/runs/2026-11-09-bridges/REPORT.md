# Run 2026-11-09-bridges: report

Leon asked for all the cross-pollination items of run 2026-11-09-three to be worked ("do them all"), and during the run
for two more targets: the classical topology behind a rung-count lower bound to be derived, and the tensor product in
the eviction comparisons to be replaced by geometric algebra. Method: three clusters, six attackers (two pairs and two
single constructive attackers), a bridge-hunter, three blind referees, one fix round, two maintainer agents, close-out.
Thirteen proposals accepted: eleven SOUND WITH FIXES, two restated after OVERSTATED verdicts (one with a wrong
coefficient, corrected) and accepted by Leon individually. One open problem settled, two reformulated.

## Accepted
Lens-space walls (op.wall-class-invariant)
- synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five: on a definite side the rung count
  is the least k with an odd map of the double cover into R^k minus 0 (proved from stored clauses); an explicit
  five-component odd map in Cl(6,0), so k <= 5 on L^5(4) and k <= ceil(3(n+1)/2) on L^{2n+1}(4) (likely classical);
  k = 5 on the definite side given the next result. Agrees with Stolz 1989 as quoted in secondary sources.
- synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components: no odd map S^5 -> R^4 minus 0 under the
  quarter turn, by an exact cup-one computation on a 48-orbit complex built from the stored cell model with an explicit
  higher diagonal; given the stored cellular background, the product complex, and Steenrod's theorem (now an imported
  Fact). The referee reproduced the class with independently solved higher diagonals. The higher-diagonal identity is
  verified for the degrees and orders used, not proved for general order.
- synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side: k >= 4 on every side from dimension
  five; from dimension seven on the stored K-ring alone, in dimension five given the spin class (not imported).
  Jointly: L^5(4): 4 <= k <= 5 on every side, 5 on the definite side; L^7(4): 4 <= k <= 6, definite side 5 or 6.
Field theory
- synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
  (OVERSTATED with one coefficient WRONG; restated; titled "One-loop parametrix trace on a torsion-free field: rotors
  cancel, first order is Ricci"): the transport rotors cancel exactly from the leading kernel (proved); D_x U =
  +(1/12) Ric(xi) R at first order, given the stored Taylor data and the protraction identity (a stated hypothesis,
  not stored); degree counting and the extension count argued; the freedom is a function space of x' unless local
  covariance with scaling is used. The filed sign was wrong against the store's curvature convention; the check now
  tests the stored sign and a de Sitter case.
- synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element: the Klein twist is not a candidate;
  the pseudoscalar of the ten Majoranas (omega = -I(-1)^N, the classical centre of Spin(10)) acts by one unit on the
  sixteen; every mass form anticommutes with it; Dirac terms keep it modulo the Standard Model group; the Majorana
  element breaks it to the grading. Readings (argued): no stage where it is an unbroken non-gauge symmetry.
- synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac (titled "Mass
  terms as pair terms on four tower modes: the charge separating Majorana from Dirac"): every mass term of the stored
  block is a pair term; Majorana and Dirac differ by a charge 2 and by rank; the seesaw quadratic x^2 - Mx - m^2 for
  every K; the 3 | n_g verdict is unchanged (argued).
Finite averages and the eviction comparisons (op.island-dictionary)
- synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three (titled without "rotors"):
  quarter turns about blades of square -1, for I^2 = -1, form a state design of order three for every N; the average
  is state independent, so the Haar moments to order three are derived at dimensions that are powers of two; from
  eight generators most generating elements are not rotors and bivector turns alone are not transitive.
- synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector: the fourth moment
  exceeds Haar (computed, up to eight modes); crossing coefficients tend to the binary subspace counts for every order
  (proved); on a parity sector the mean purity is (dA + dB)/(dA dB + 2) and the third moment has a closed form (proved).
- synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product: a subsystem is a sub-Clifford
  algebra, reduction is the blade projection, a Klein twist gives the ordinary tensor product; for even states both
  reductions are the tensor-product ones; genus weights 4^g on a sector; the sector mean entropy is the two-block case
  of a published formula (Bianchi et al. 2022); the fate of each stored eviction result.
- synthesis.eviction-keeps-one-replica-saddle v4 and synthesis.eviction-keeps-one-of-catalan-many-replica-saddles v4:
  restated on the split; sector column first, abstract tensor-product values kept; leading terms unchanged. The stored
  Catalan upper bound was verified in a range, not proved: the entity now says so.
Other
- synthesis.field-strength-heat-kernel-coefficients-of-the-dark-towers-fix-no-scale-ratio (titled "Spin-trace rule in
  dimensions three and five: heat-kernel numbers, running only in four"): the coefficient table; no scale ratio for
  the odd towers follows from the store (argued, consistent with three stored results).
- synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt (OVERSTATED; restated; titled "At
  gauge parameter one no curvature coupling gives the Sakharov zero and the Kasner tilt"): with the gauge parameter
  free both are met at alpha = 1/3 + 4 xi; under clause K1 of the Krein premise the gauge parameter is one.

## Findings without a proposal
Killed links: the Kasner "helicity" is a coframe twist, not spin helicity; no state is stored on a collar for the
wall-rung against descent-rung comparison; recovery maps restate a stored property; the vector's Sakharov weight is a
pure helicity count with no edge term; so(10) level 4 inside su(16) level 1 gives no new condition; walls of
parallel-tractor (total-radical) type would need at least three rungs and are outside the tame theory. The order-four
anomaly question separates fifteen from sixteen by parity alone. Bridges (findings/bridges.md): the order-four charge
and the mass-terms charge table are one structure; P^2 = (-1)^m is one sign with four readings (design hypothesis,
slot-module pseudoscalar, twisted spin structure, lens deck rotor); bivector turns on ten generators have orbits
45 + 210, the so(10) currents and the 210.

## Leon's decisions (DECISIONS.md, items 1 to 13)
Imports: the scaling-degree rules (in the Epstein-Glaser Fact), local covariance with scaling, Steenrod's theorem.
Retired: the Haar mean-purity import. Not imported: the classical topology (T) (derived instead as far as one
theorem), the mod-16 anomaly statement. Readings: gauge parameter one by K1 for every statement about B; xi = 0 at
tree level for the rung doublets; the random-state column on a parity sector. Problems: op.dark-tower-running closed;
op.order-four-anomaly-and-sixteen restated; tameness edges added; both restated results accepted.

## Maintainer pass (maintainer-M1.md, maintainer-M2.md)
New Facts: synthesis.imported-steenrod-cup-one-square-is-a-natural-cohomology-operation,
synthesis.imported-local-covariance-with-scaling-of-time-ordered-products (its sources prove it for a scalar field;
the use for the Dirac current is flagged); the Epstein-Glaser Fact v2 with (SD1)-(SD4). None checked against a source.
Retired: synthesis.imported-haar-average-purity (tombstone, references repointed, powers-of-two caveat). Versions
raised: the all-moment Haar Fact 2 -> 3; the capacity result 1 -> 2 (K1); the Sakharov attachment-modules result
3 -> 4 (scope: modules, not content); the eviction deficit result 4 -> 5 (sector value; the lower bound (m-1)/(2n)
fails on a sector at m = 2). Notes on seven stored entities. Open problems: 34 open, 27 settled;
op.dark-tower-running settled; op.order-four-anomaly-and-sixteen and op.curvature-coupling-across-subjects
reformulated (their statements rewritten: the originals are in git history); six others updated. Nine edges repinned;
four plain-level condition sentences added at close-out (W503).
Left for Leon: the Krein-quartet result and the series-content Newton-coupling result still present the gauge
parameter and the doublets' curvature coupling as free (a note on each would match decisions 7 and 10); the Krein
premise's list of results that use it does not name the curvature-coupling result; the protraction identity is not
stored (attack item added to derive it in the algebra core); ids containing "rotors" and "no weyl term of degree
four" are unchanged, with notes stating the scope; the finite-averages entity no longer lists the three eviction
results under uses (they were comparison targets and would have made a cycle).

## Checks
Baseline 0 errors 0 warnings. Final gate: thirteen check4 exit 0, no findings (one weak-check warning tightened);
validate ok; style clean. Final tp check 0 errors 0 warnings; build 0 errors; layout, site, lock; 394 tests OK
(1 skipped).

## Costs (approximate subagent tokens)
Attackers with fixes about 2.0M, bridge-hunter 0.17M, referees 0.9M, maintainers 0.7M: about 3.8M.
