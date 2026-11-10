# Bridges and cross-pollination, run 2026-11-09-three (agent X)

Read: BRIEF.md, RUN.md, the earlier run's REPORT.md and bridges.md (L1 to L6 and its rejected list are not
repeated here), the "Unexpected links" sections of every earlier run, all 32 open problems (attack fields and
entities), attack-A.md and attack-B.md of this run as of 20:12 (routes and kill conditions only; no results yet).
Method: direct lookups on store/claims (1344 entities: 1011 proved, 218 imported, 69 postulates, 30 conjectured,
16 refuted), a cross-subject edge count over the `uses` edges, past and future cones, and four small exact
computations (work is in my scratch, not in the lab; each is restated below so it can be rerun).

Labels. "stored" = what the store says at the version quoted. "computed" = a small exact check I ran (Fractions
or integers). "argued" = my reading, for an attacker to test. "memory" = literature cited from memory, unchecked.

Connectivity facts used below (computed from `uses` edges): no edge at all between generations and any of
tower, completion, one-relation, descent, einstein, entropy, walls, dark-matter; walls to dark-matter 1 edge,
walls to descent 1, walls to one-relation 0; quantum-fields to dark-matter 1, to interior 0, to neutrinos 0;
entropy to clifford-structure 0, to conformal-spacetime 0 direct (20 of 83 entropy claims reach it through cones).

## Links bearing on T1-T3 (for relay)

### T3

R1. The two generation leads need opposite assumptions about the graviton (to A and B). computed.
Entities: synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations (einstein,
proved v3) clause (i); hawking.helicity-lift-joints-itemised (proved, v6 pinned by array-ln2); the capacity bound
of the earlier bridge L1(c). Clause (i) stores the polar part of one helicity state's character as
2 t^-3 - s^2 t^-1. So the stored quadratic coefficient is a supertrace of helicity squared over helicity states:
2 N_V (1) - 2 N_W (1/4) = 2 (N_V - N_W/4), scalars contributing 0. That is the whole content of "12 = 4 N_g".
Adding the graviton's two helicity states by the same stored rule (s = 2, the module J1 already uses) gives
2 N_V + 8 eps - N_W/2 = 0, so N_W = 64 and n_g = 4 at eps = 1. The capacity bound needs the opposite:
2 n_V + n_s + 2 eps <= 16 n_g gives n_g >= 3 only at (n_s, eps) = (8, 1); at (8, 0) it is 32 <= 32 and n_g = 2
passes; at (4, 0) and (4, 1) it is 28 and 30 and n_g = 2 passes. So lead (a) excludes n_g = 2 only with the
graviton counted, and lead (b) gives 3 only with the graviton not counted. They cannot be premises of one theorem
without a stated reason why the graviton registers on the arrays yet does not enter the supertrace (induced
gravity would be such a reason: the graviton is not a field of the content; then (a) loses its exclusion of 2).
Kill: a stored premise that fixes eps the same way in both counts.

R2. The Sakharov three is equivalent to conformal coupling of the scalars (to A and B). computed, on stored weights.
Entities: synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off (einstein, proved v2)
clause (i), weights 1 - 6 xi_R per real scalar, 1 per Weyl field, -4 per vector at alpha = 1. B = 16 n_g - 48 +
N_S (1 - 6 xi_R). With the two doublets (N_S = 8): B = 0 at n_g = 3 iff xi_R = 1/6; xi_R = -1/6 gives n_g = 2,
xi_R = 1/2 gives n_g = 4, xi_R = 0 gives 5/2 (no integer). The store calls xi_R an open datum
(op.einstein-from-the-field-theory item 3, op.qft-bosons-and-the-rung-field item 3) and the vector weight gauge
dependent (-(3 + 6 xi_R alpha)). So "N_g = 3" is a statement on the surface (xi_R, alpha) = (1/6, 1), and what it
would take to make it a theorem is a premise fixing xi_R = 1/6 (the attachment modules are conformal, which is
why clause (iv) is independent of N_S: that is a property of the attachment, not of the rung field's action).
The same datum is the free tilt coupling of
synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling (dark-energy,
proved v3): see cross-link C1. Kill: a stored derivation of xi_R for the rung field.

R3. No stored premise requires the quadratic coefficient to vanish (to A). computed by cone.
No entity in the future cone of the Sakharov claim (four entities) has synthesis.c-loc-local-horizon-premise or
synthesis.field-space-premise-parallel-frozen-point in its past cone. The only candidate requirement I can
construct is argued: (Loc) says the entropy density of a cut is independent of matter. If the one-loop area term
of the fields' entanglement across the cut is the same B Lambda^2 (Susskind and Uglum; memory), matter-independence
of eta needs either B = 0 or all of 1/G induced. That would make B = 0 a consequence of (Loc) plus an imported
identification, with xi_R = 1/6 and the gauge still to be fixed. It is a route to a conditional theorem, not a
derivation. The vector's weight -4 = 2 - 6 has a known reading as two helicities plus a contact term carried by
edge modes (Kabat; Donnelly and Wall; memory); the store has no claim on it (find: no hit for "contact term" in
this sense, none for "edge mode" outside synthesis.central-label-carries-mass-at-zero-weight).

R4. The capacity bound is not uniform in the partial wave (to B). argued, from T2's own scope.
Spin-2 channels exist for l >= 2 only and vector channels for l >= 1; the count 2 n_V + n_s + 2 eps is 34 only
for l >= 2. If the bound is read per (l, m), low l never constrains; if read per light ray, it is a large-l
statement and inherits T2's non-uniformity in l. B's T2 route R3 (l = 0, 1) supplies the fact.

R5. The number current is what the recurrence verdict uses, and the Majorana premise breaks it (to B). argued.
Entities: the earlier L4 (15 n_g = 0 mod 24 gives 8 | n_g; the 3 | n_g verdict needs the number-current sector);
neutrino.m-framework-realises-majorana-term-scale (Premise (M)); synthesis.slot-module-light-ray-arrays-are-weyl-
components (entropy, proved v3: fifteen components is not a halving). A Majorana term carries fermion number 2,
so the split H = H_so(10) + H_N is not preserved by the dynamics that gives nu_R its mass. First computation: the
commutator of the window number current with a pair term a a on the sixteenth array (exact, GA). Kill: the test
is posed on free null data, where mass terms do not enter (as the earlier L5 found for Higgs breaking).

R6. Sixteen per generation as a global anomaly condition (to B, look-elsewhere accounting). memory plus stored.
The store's Klein twist (synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-
conjugations-give-interacting-spin-statistics, quantum-fields, proved v5; Z in
synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state, thermality, proved v5) is an
order-four element whose square is the grading. A Z4 whose square is fermion parity has a mod-16 anomaly on
Weyl fields of odd charge (bordism group of five-manifolds with that structure is Z16, generated by RP^5;
Garcia-Etxebarria and Montero, Hsieh, Tachikawa and Yonekura; memory). This bears on 15 against 16 per
generation (op.hypothesis-s item 3 says the bit cannot be decided by gauge numbers, CPT or anomaly freedom), not
on n_g. The store has no entity on it (no hit for bordism, Dai-Freed, eta invariant, mod 16). See new area N1.
Correction to a tempting form: L^5(4) carries a structure of this kind with Z8, not Z4 (the rotor lift of the
quarter turn in three planes has fourth power -1), so the Z16 statement lives on RP^5 walls, where the earlier
run found ht = e.

### T1

R7. On a definite side the exact rung count is a Borsuk-Ulam index (to A and B). argued, short proof from stored
clauses. Entities: synthesis.wall-rung-count-is-height-of-dying-line-class (walls, proved v2) clause (2)
(sufficiency: L a subbundle of the trivial R^k) and synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-
height (walls, proved v1) clause (3) (definite side: k = e(L)). A line subbundle of the trivial R^k is a map to
RP^{k-1} classifying L, that is a Z2-equivariant map from the double cover of the wall defined by x to S^{k-1}
with the antipodal action. For L^{2m+1}(4) the double cover is RP^{2m+1} with the involution induced by the
quarter turn. So e(L) = 1 + the least j with an equivariant map (RP^{2m+1}, J) -> (S^j, -1): the coindex, or
"level", of projective space with that involution (Pfister and Stolz; Stolz, The level of real projective
spaces, 1989; memory: the answer is known and depends on m mod 8, values not checked). Data points: m = 0 gives
2; m = 1 gives 3 (stored: k = 3 on L(4,1) with a definite side). For L^5(4) the stored window is 3 <= k <= 6
(two-rungs clause: e(L) <= 6). First computation in A's cellular model: the primary obstruction to an
equivariant map into S^2 (a class in the twisted integral H^3 of L^5(4)); if it vanishes, the next one with
pi_3(S^2). On indefinite sides the same with the stable condition of clause (1). Kill: the stored definite-side
equality k = e(L) uses more than clause (1) and (2) (it does not, on my reading of clause (3)).
If Stolz's table is as remembered, the exact count is periodic in m mod 8 through real K-theory, which would be
a structural link to the tower clock (same Bott periodicity), unlike the 24 = 8 x 3 item rejected earlier.

R8. The presented K-ring gives ord(1 - xi) = 2^{ceil(n/2)} for n = 1 to 9 (to A and B). computed.
Integer lattice arithmetic in Z[chi]/(chi^4 - 1, (chi - 1)^{n+1}) (Hermite reduction of the ideal's four
generators chi^j (chi - 1)^{n+1}, membership of m (1 - chi^2)): orders 2, 2, 4, 4, 8, 8, 16, 16, 32 for
n = 1..9, and ord(1 - chi) = 2^{n+1}. This reproduces the stored clause k >= 1 + floor((n+1)/2) for
1 <= n <= 8 and extends it to n = 9; the pattern suggests the all-n bound can be raised from 1 + floor(n/2) to
1 + ceil(n/2) (a 2-adic valuation argument through chi -> the unit bivector of a plane, where (1 - chi)^2 is
2 up to a unit). B's audit point stands: the lower bound needs the presented ring to inject into K(Sigma); the
computation above is inside the presentation only.

R9. Hand check for n = 1, 2 (to A, as a test vector). computed by hand. With u = chi - 1: chi^4 - 1 =
4u + 6u^2 + 4u^3 + u^4. At n = 1: 4u = 0, 1 - chi^2 = -2u, order 2. At n = 2: 4u + 6u^2 = 0 and 4u^2 = 0, so
2(chi^2 - 1) = 4u + 2u^2 = -4u^2 = 0, order 2. This is why complex K is blind at L^5(4) and q_1 is needed there.

### T2

R10. One superpotential gives both spin-2 potentials and the horizon factor at once (to A; B's kill (b)). computed.
With mu^2 = (l - 1)(l + 2) and F = f / (r (mu^2 r + 6M)):
V_minus = -6M dF/dr_* + 36 M^2 F^2 + mu^2 (mu^2 + 2) F equals f (l(l+1)/r^2 - 6M/r^3) (Regge-Wheeler) and
V_plus = +6M dF/dr_* + 36 M^2 F^2 + mu^2 (mu^2 + 2) F equals the Zerilli potential
2 f [lam^2 (lam+1) r^3 + 3 lam^2 M r^2 + 9 lam M^2 r + 9 M^3] / (r^3 (lam r + 3M)^2), lam = mu^2/2:
exact at 36 rational points (M in {1, 3/7, 5/2}, l in {2, 3, 4, 7}, three radii), with the swapped assignment
false at every point. Since F = f times a function regular and positive at r = 2M for l >= 2, and
dF/dr_* = f dF/dr, both potentials are f times a regular function with no further work, and the intertwiner is
d/dr_* + (kappa_l/(12M) + 6M F) with kappa_l = mu^2 (mu^2 + 2). Its kernel solves the equations only at
omega^2 = -(kappa_l/12M)^2 < 0, so B's kill (a) (a real-frequency kernel) should not fire (argued from the
standard form; B to confirm exactly). The form is Chandrasekhar's (memory); the identity itself is checked.

R11. The stored Dirac channel is the same Darboux structure (to A, one sentence in the proposal). argued.
synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional (thermality, proved v1) clause
(2) has the first-order pair A Phi + W K Phi with W = sqrt(f)/r, whose square gives partner potentials
W^2 k^2 -/+ k dW/dr_*. Spin 2 has the same shape with superpotential 6M F plus a constant. The three integer
spins fit f [l(l+1)/r^2 + (1 - s^2) 2M/r^3]: stored scalar clause has +2M/r^3 (s = 0), the target has -6M/r^3
(s = 2), and (1 - s^2) is zero at s = 1 (check against the stored Maxwell clause). Note 1 - s^2 against the
-s^2 of the Sakharov character in R1: the same helicity-squared weight enters both, through the Weyl
eigenvalue 2M/r^3 here; argued, not a derivation.

R12. Stored negative-weight helicity at Kasner walls has no edge to the helicity lift (to A or B, low priority).
synthesis.kasner-curvature-wall-is-negative-weight-helicity (interior, proved v2) and
hawking.helicity-lift-joints-itemised: neither is in the other's cone (computed). Both read helicity as a boost
weight. If A's spin-2 channel is stated at boost weight zero (as the Dirac clause is, by f^{-1/4}), the Kasner
result is the interior counterpart: the growing term there is the weight the horizon rescaling removes.

## Cross-links between subjects (ranked)

C1. One free datum xi_R sits under three results in three subjects. einstein, dark-energy, quantum-fields.
Entities: series-content-induces-a-newton-coupling (einstein v2), krein-quartet-drops-from-the-induced-einstein-
hilbert-coefficient (einstein v3: zero at xi_R = 1/6, alpha = 1), kasner-approach-coupled-modes-reach-measured-
tilt-only-by-a-fitted-curvature-coupling (dark-energy v3) with synthesis.tree-level-curvature-couplings-stay-
blue-at-the-isotropic-kasner-point; op.rung-unit, op.qft-bosons item 3, op.descent-state-and-spectrum item 2.
Why: the Sakharov cancellation needs xi_R = 1/6 (R2); the red tilt needs a fitted xi_R that the series does not
fix. Status: argued link, computed arithmetic. First computation: read off the fitted xi_R of the tilt result and
evaluate B at that value on the stored content; if the tilt value is not 1/6 the two uses exclude each other
for the same scalar. Kill: the two results concern different scalar fields with independent couplings.

C2. The Hadamard scaling results supply the curved-field clause of extension of distributions.
thermality to quantum-fields. Entities: synthesis.hadamard-scaling-limit-premise (thermality, proved v8),
synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel
(proved v4), against synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-... (quantum-fields,
proved v4) and synthesis.imported-epstein-glaser-extension-theorem-... (imported v1). Computed: no path in
either direction between the two groups. op.qft-loops item 3 says the curved-field clause is "argued: the
Hadamard scaling degree gives the flat counting"; the store has proved scaling-degree statements for exactly
these parametrices. First computation: the scaling degree at the diagonal of the square of the stored Dirac
parametrix (the vacuum-polarisation kernel) on a Weyl-curved field, from the stored bound "null vacuum plus a
kernel of generator scaling degree at most 0". Kill: the stored bounds are on generators (one null direction)
and do not give the four-dimensional degree at the diagonal.

C3. Finite averages over the store's own extraspecial group could replace the Haar imports.
clifford-structure to entropy (0 edges). Entities: synthesis.signed-directions-and-the-integer-clifford-algebra
(clifford-structure, proved v2: G extraspecial of order 2^{1+n}; its future cone is in standard-model only)
against synthesis.imported-haar-average-purity and synthesis.imported-haar-moments-of-random-pure-state (entropy,
imported; used only by eviction-keeps-one-of-catalan-many-replica-saddles). Why: the normaliser of an
extraspecial 2-group in the unitary group is a unitary 2-design (memory), so second moments (purity, the Page
deficit at second order) are exact finite sums in the integer Clifford algebra. Test vector: the 60 two-qubit
stabiliser states are 36 products and 24 maximally entangled, mean purity (36 + 12)/60 = 4/5 = (2+2)/(4+1), the
imported Haar value (memory for the count; arithmetic exact). Status: argued. First computation: the mean purity
over the parity-preserving normaliser (quarter-turn rotors exp(pi/4 e_i e_j) and their quartic partners) on the
even sector for n = 4 generators. Kill: parity superselection breaks the design property on the even sector at
n = 4.

C4. The one-loop running coefficients have never been applied to the dark towers' gauge algebras.
quantum-fields to dark-matter (1 edge). Entities: synthesis.one-loop-running-coefficients-from-spacetime-algebra-
spin-traces (quantum-fields, proved v3; users: two entities, none in dark-matter) and
synthesis.gauge-algebra-by-tower (dark-matter, proved v1), dark-tower-matter.three-dimensional-content,
dark-tower-matter.five-dimensional-content. Status: computed absence of the edge; the link is argued. First
computation: b coefficients for each tower's algebra on its stored content; sign and the ratio of confinement
scales to the visible one at equal coupling at the descent. Feeds op.odd-towers items 2 and 3 and
op.thickness-deposit-rule item 2 (a correlation length of the deposit). Kill: the towers' gauge fields are not
dynamical in the store's reading (then record that).

C5. Wall rungs and descent rungs are counted by two unlinked results. walls to descent (1 edge).
Entities: synthesis.wall-rung-count-is-height-of-dying-line-class (walls, proved v2) and
descent-lift.lift-costs-one-rung-per-mode (descent, proved v4). Both count adjoined hyperbolic planes. Argued:
a k-rung completion of a wall carries k ladder pairs, so the Witt-index capacity of the completed collar is k
qubits, and on lens walls the capacity exceeds the mod-2 height for a K-theoretic reason. First computation:
on the stored L(4,1) completions, the ladder pairs of the rung summand and the parity operator of
descent-lift; whether the capacity is k or k - 1 once the wall form is imposed. Kill: the rung summand is a
trivial bundle with no state attached, so "capacity" has no meaning without a stored state on the collar. The
earlier run rejected "wall rungs against Higgs rungs"; this is a different pair and makes no claim about n_h.

C6. Majorana pairing and the tower's pairing results. neutrinos to one-relation and tower.
Entities: pairing.* (19 claims; pairing.imported-stabiliser-tangent-external describes the Bogoliubov-rotated
vacuum exp(sum A a* a*)|0>), synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy,
against standard-model.majorana-element and neutrino.m-framework-realises-majorana-term-scale. Computed: no
neutrino claim uses any pairing.* claim. Argued: a Majorana mass is a pairing term on the neutral singlet, the
seesaw is the Bogoliubov diagonalisation, and the stored gap formula is the heavy mass in that reading. First
computation: the stored pairing gap on a two-mode block (nu_L, nu_R) with Dirac hopping m and pairing M on one
mode; it should return eigenvalues M and m^2/M at leading order, exactly as a quadratic. Kill: the pairing
results are at fixed charges, where a number-violating term has no matrix elements.

C7. The so(10) window energy is a conformal embedding with matching weights. quantum-fields to entropy.
Entities: synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy (quantum-fields, proved
v1) and the recurrence results. Computed: c(so(10) at level 4) = 4 x 45/12 = 15, and the weight of the 16 is
(45/8)/12 = 15/32, equal to the su(16) level-one fundamental weight (255/32)/17 = 15/32, as a conformal embedding
requires. This takes the earlier L4 one step further and opens N4.

C8. Kasner helicity and the helicity lift (R12), interior to thermality: argued, unlinked (computed).

C9. The parallel-tractor curved orbits and the wall sheaf, einstein to walls: see N5 (computed: the future cone
of synthesis.imported-holonomy-reductions-of-cartan-geometries lies in einstein only).

## New areas to investigate (ranked by expected yield against cost)

N1. Global (bordism) anomalies of the store's own order-four elements. Cost low to moderate; yield: a possible
decision of the neutral-singlet bit. Maps to: the Klein twist entities of R6, standard-model.slot-module-
hypothesis, synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5, and the RP^n walls of
op.wall-class-invariant. First computations: (a) the charges of the sixteen arrays under the store's order-four
element (all odd or not); (b) the fixed-point contribution on RP^5: one nontrivial deck element, weight
(1/2)(1/2^3) = 1/16 per Weyl field (argued arithmetic; the index theorem behind it would be an import, a
decision for Leon). Suggested open problem: "Is there an order-four symmetry of the slot module whose square is
the grading and which the descent preserves; if so, does consistency on RP^5 walls force sixteen components per
generation?" Feeds op.hypothesis-s item 3 and op.qft-structural-inputs. Prior art, memory: Garcia-Etxebarria and
Montero 2018; Hsieh 2018; Wang's mod-24 work already cited in the store.

N2. Equivariant index (level) theory for exact rung counts. Cost low for L^5(4) (one obstruction class in A's
cellular model), moderate in general. Maps to R7. Suggested open problem: "On a definite side the rung count of
a wall is one plus the coindex of the double cover defined by the dying line; compute it for L^{2m+1}(4) and
decide whether it is periodic in m mod 8." Feeds op.wall-class-invariant item 1.

N3. Dark-sector running and confinement (C4). Cost low (stored coefficients, stored content). Suggested open
problem: "Which dark towers' gauge algebras are asymptotically free on their stored content, and what scale
ratio to the visible sector follows at equal coupling at the descent?"

N4. Modular data of the light-ray current algebra. Cost moderate. Maps to C7, synthesis.gauge-factor-sugawara-
parts-satisfy-virasoro-relations-on-the-band, synthesis.one-window-parity-recurrence-..., and the remark on the
self-dual point in synthesis.counted-unit-energy-at-half-offset. First computation: the T-phases
exp(2 pi J (h - c/24)) of the so(10) level-4 sectors occurring in the su(16) level-1 vacuum and fundamental
sectors, for n_g copies, and whether the recurrence condition is triviality of T on the vacuum sector; then
whether invariance at the self-dual point adds a condition beyond 24 | c. Feeds op.counted-mode-energy item 3.
Kill: no Virasoro algebra on a finite window (stored), so the modular data exist only on the band domain.

N5. Walls by parallel-tractor type. Cost moderate. Maps: synthesis.imported-holonomy-reductions-of-cartan-
geometries (c) (M = M+ u M0 u M-), dark-energy.imported-frozen-point-geometry, interior.covariant-form-vacuum-
equations (the scale's zero set may be non-empty), against sheaf.tameness and sheaf.one-sided-completion. The
stored walls are corank-one degenerations of the form on T*M; the zero set of an almost-Einstein scale is a
locus where that form vanishes entirely to second order. Suggested open problem: "Extend the wall sheaf to
total-radical walls of scale type and decide whether the completion there is the tractor bundle itself (one
rung, the scale tractor's plane)." First computation: on the stored de Sitter frozen point, the collar form
sigma^2 times the conformal inverse metric and its minimal nondegenerate completion.

N6. Recovery maps for the descent's conditional expectation. Cost low. Maps:
singularity.imported-descent-one-way-conditional-expectation (descent, proved v7, Takesaki cited) and the
eviction results (singularity.eviction-window-thermal-product-radiation-entropy). The store has no entity on
recovery or error correction (no hits). First computation: the Petz map of the order-two expectation on a
matrix factor and the exact condition for an evicted window to be recoverable from the radiation. Feeds
op.island-dictionary item 3 (which quantity plays the area term).

N7. An edge-mode reading of the vector's Sakharov weight (R3). Cost moderate; yield uncertain. Maps: the
character clause (i) of the Sakharov claim, hawking.current-commutator-exactly-edge-split, J3 version 2. First
computation: split the stored vector weight into the two helicity modules' -s^2 terms and the remainder, and
compare the remainder with the edge term of the stored current commutator. Feeds op.einstein-from-the-field-
theory item 3 and the one-coupling clause of op.derive-loc-and-r-loc.

## Rejected

- Lens-space walls as Taub-NUT or Misner quotients (walls against synthesis.taub-nut-cauchy-horizon-is-taub-point-
  with-complex-residue, which has no sheaf edge): the radical direction on that horizon is the null generator,
  an orientable line, so x = 0 and one rung suffices. No realisation of the torsion walls.
- L^5(4) as the generator of the mod-16 anomaly: wrong structure (Z8 there; see R6). The correct wall is RP^5.
- Kerr's winding number three (interior.duality-monodromy-fibration-over-ring) against three generations: no
  shared structure; the Kerr three is the inverse-cube power of the complex scale.
- The 24 Hurwitz units of the weak rotor lattice against the 24 arrays of the recurrence: one is the binary
  tetrahedral group as a 5-design, the other is c = 16 n_g at n_g = 3 against the vacuum phase; nothing produces
  both. What would distinguish structure from coincidence: a derivation of the recurrence period from the
  unit group of the integer algebra.
- Koide's null condition (families.koide-nullity-condition-one-member-invariant) against the null structure of
  the completion or the (2,1) tower: generations has no edge to completion, one-relation or tower, and the Koide
  form lives on face space with its own real structure. A link would need the face form to be induced from the
  completion's form; op.gram-square-and-face-space item 2 already says the selection must come from outside
  face space, and no candidate is stored.
- An eta-invariant derivation of the K-theory order for T1: it trades the K-ring for the
  Atiyah-Patodi-Singer theorem, a heavier import. (I ran an ad hoc character sum; it did not reproduce the ring
  orders at n = 2 and is discarded.)
- BKL chaos against the scrambling bound: the store's boost dynamics has Lyapunov exponent 0 (stored, two
  entities); the billiard is a different flow on a different space.
- A Cardy count of the horizon entropy from c = 16 n_g: no Virasoro algebra on a window (stored), and the
  store's count is calibrated, not derived from c.
