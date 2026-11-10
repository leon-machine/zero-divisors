# Run 2026-11-09-three: report

Leon asked for a look over the physics graph, a choice of three problems where an advance can be made, and an attack on
them; and for cross-pollination: links between subjects and new areas to investigate. The three targets were the strongest
leads the earlier run of the day left unexecuted. Method: one cluster, two attackers (constructive and adversarial), one
cross-pollination agent, one blind referee, one fix round, one maintainer agent, close-out. Three results accepted, all
SOUND WITH FIXES; no problem changed status; two partial advances and one negative.

## Accepted
- synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure (op.wall-class-invariant):
  the Z4 cell complex of the sphere with an explicit equivariant diagonal (a chain map for every n by four parity cases,
  four group-ring identities); cup coefficient 6 for two odd degrees, so H^even(Z) = Z[y]/(4y, y^{n+1}) and x^2 = 0 mod 2;
  beta x = 2y; the Bockstein of Z2 -> Z4 -> Z2 vanishes; T Sigma + R = (n+1) eta; the K-ring
  Z[chi]/(chi^4 - 1, (chi-1)^{n+1}), both halves, given the Atiyah-Hirzebruch filtration (now an imported Fact);
  ord(1 - chi^2) = 2^{floor((n+1)/2)} computed to n = 14. Given standard cellular cohomology and obstruction theory as
  stated background. Not derived: the spin class q1, the lambda-operations. Transport-absent.
- synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional (op.helicity-per-boundary-mode):
  first-order perturbation of the static GTG field; the odd-parity first-order Ricci vector on a 144-case grid with a
  degree bound (argued); the Regge-Wheeler equation equivalent to the vacuum equations on a channel of nonzero frequency,
  l >= 2; even parity one way (the Zerilli equation in the span of the linearised equations, sampled), converse cited;
  one superpotential for both potentials, intertwiner invertible at real frequency; V/f at r = 2M is (L-3)/(4M^2) odd,
  (4 lam^2 + 4 lam + 3)/(4M^2(2 lam + 3)) even; rate e^{2 kappa r_*}. A static (Killing) frame statement. The referee
  confirmed the odd-parity identity jointly by an independent symbolic metric computation (outside GA, not part of the
  entity). Transport-absent.
- synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free (op.qft-structural-inputs; titled "Capacity
  and induced-gravity readings do not fix the generation number"): pair currents of the arrays have helicity -1, 0, +1,
  never 2, and those of helicity one are not canonical, so one array tower per helicity channel cannot be met for a
  vector or graviton at any n_g; as arithmetic the capacity bound gives n_g >= 3 only with the graviton and both
  doublets; the Sakharov zero sits at xi_R = 1/6 + (n_g - 3)/3 and moves with the gauge parameter and the graviton
  (n_g = 4 with it); the quartic coefficient vanishes at n_g = 1; of eleven rule variants two single out 3. Independence
  argued (2 of the cone's 24 postulates audited), labelled so at every level.

## Not reached
The exact rung count on L^5(4); the even-parity converse and the tensor-harmonic inputs; l = 0, 1 and regular charts;
a derivation of q1; a two-model proof for the generation number over the full joint cone; bridge lead R5 (the number
current against the Majorana premise).

## Leon's decisions (DECISIONS.md)
Import the Atiyah-Hirzebruch filtration as one Fact; q1 not imported; J3 narrowed to even-parity spin 2, reworded to
"each partial-wave channel, l >= |s|", and recorded as not injective; Killing-frame scope on both horizon-channel
results; three new open problems and one new attack item from the cross-pollination read; the success clause of
op.wall-class-invariant sharpened.

## Maintainer pass (maintainer-M.md)
New: synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory (cited from memory, not checked against the
sources). Versions raised: J3 2 -> 3; helicity-lift joints 6 -> 7; the two collapse results; array-ln2 5 -> 6; the
lower-spin horizon result 1 -> 2; the two lens-space wall results 1 -> 2 (the first now conditional on q1 alone, the
second on the lambda-operations alone). Open problems: three updated, three new (op.order-four-anomaly-and-sixteen,
op.dark-tower-running, op.curvature-coupling-across-subjects); 35 in all. Ten edges repinned.
Left for Leon: synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping says J3 "puts one
array in each helicity channel" and should be re-read against J3 version 3; the name "the s-wave reduction J3" remains in
(N+), the Hadamard deposit premise, op.derive-loc-and-r-loc, tags.yaml and two notes; the lens K-theory check's
docstring still says its K-ring is cited from memory; the Killing-frame sentence is not machine-checked and the Kruskal
coupling is computed for the scalar and Maxwell channels only.

## Cross-pollination (findings/bridges.md)
Links: xi_R under three results; Hadamard scaling as the curved-field clause of extension of distributions; finite
Clifford-group averages in place of the Haar imports; the running coefficients never applied to the dark towers; wall
rungs against descent rungs; the Majorana mass as tower pairing; so(10) level 4 inside su(16) level 1; helicity as boost
weight in the Kasner wall and helicity-lift results. New areas: order-four anomalies; equivariant level theory for rung
counts; dark-sector running; modular data of the light-ray current algebra; walls by parallel-tractor type; recovery maps
for the descent's conditional expectation; an edge-mode reading of the vector's Sakharov weight.

## Checks
Baseline 0 errors 0 warnings. Final gate: three check4 exit 0, no findings; validate ok; style clean. Final tp check
0 errors 0 warnings; build 0 errors; layout, site, lock; 394 tests OK (1 skipped).

## Costs (approximate subagent tokens)
Attackers with fixes about 0.58M, cross-pollination 0.21M, referee 0.26M, maintainer 0.38M: about 1.4M.
