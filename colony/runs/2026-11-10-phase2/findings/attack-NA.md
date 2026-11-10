# attack-NA (cluster N, angle A constructive), run 2026-11-10-phase2

Status: COMPLETE. Two proposals registered. Kill conditions below were registered before any computation.

## Entities read
standard-model.why-large v3 (conjectured), refuted.the-number-n-is-a-mystery-of-largeness v2,
refuted.the-number-n-is-a-coincidence-dirac v2, standard-model.largeness-number-universes-boundary-modes,
standard-model.trichotomy-what-kind-number (entity, proof, check), synthesis.number-n-registered-free-input v1,
tower.fock-module-one-qubit-per-rung v6, tower.witt-index-quantum-capacity v5, tower.ladder-pairs-satisfy-car-vectors v4,
tower.answers-iteration-question v5, rungs.imported-tower-one-qubit-per-rung v4, standard-model.pair-count-dimension,
standard-model.gauge-algebra-minimal-massive-composite, synthesis.d-term-level-free-at-fixed-n (the format and method
model for N3: the 9 November independence sweep).

## N1. The exponential reading as precise claims (stated before computing)
Notation: a level with k modes is B_k = Cl(k,k) with null pairs v_i, w_i and Fock module F_k = Lambda W_k, dim 2^k.
- Reading E-asc (ascent): "the pair construction" is the stored transport ascent T_k -> T_{k+1}; claim: one ascent from
  a level with k pairs gives a level with 2^k pairs.
- Reading E-fock (states become modes): level n+1 is the Clifford algebra of the hyperbolic space F_n + F_n^*, so its
  null pairs are indexed by a basis of the Fock module of level n; k_{n+1} = dim F_{k_n} = 2^{k_n}, k_0 = 3.
- Reading E-int (internal): the 2^k "objects" of a level are fermionic pairs (any elements, not only vectors) inside
  that same level's algebra or inside a rung below 2^k.
- Reading E-pairs (literal pairs): objects of the next level are the 2-element sets (or grade-2 states) of the level.
Base "three": the pair count of standard-model.pair-count-dimension is a complex count ((n+2)/2 = 3 for V_C of
signature (2,4)); the real Witt index of Cl(2,4) is 2. Real against complex counting is NB's item; I state the
reading on Cl(3,3) (split, Witt index 3) and note the choice.

## N2. Routes, choice, kill conditions
Routes: (a) exact construction in GA.py of level one (Cl(3,3), module dimension by rank) and level two (Cl(8,8) with
pairs indexed by the 8 Fock states), and the tower's own next rung Cl(4,4); (b) a structural bound (simple algebra
dimension count) on CAR pairs of arbitrary elements; (c) from another subject: the Bogoliubov/second-quantisation lift
(rungs.imported-fock-representation-bogoliubov-group) to test whether level n sits inside level n+1 as fermions.
Choice: (a)+(b) as the decision, (c) as a secondary exact test.
Kill conditions (registered now):
- K-N2-1 (first computation, the claimed 8): E-asc is KILLED if the count of null pairs after one ascent from three
  differs from 8 (expected by the stored Witt theorem: 4). E-fock SURVIVES as arithmetic only if dim F_3 computed by
  exact rank in Cl(3,3) is 8 and the 8 state-indexed vectors of Cl(8,8) satisfy the CAR exactly; it is KILLED if either
  fails.
- K-N2-2 (256): E-fock survives at the next level only if the module of the 8 pairs has exactly 256 independent states
  (computed, not quoted); killed otherwise.
- K-N2-3: E-int is KILLED if dim counting forbids m > k CAR pairs in B_k (4^m <= 4^k); it survives if I find 4 CAR
  pairs of general elements in Cl(3,3).
- K-N2-4: E-pairs is KILLED if C(3,2), dim Lambda^2 or the even count differ from 8 at the first step.
- K-N2-5 (my own constructive claim "E-fock levels are rungs a_n of the proved tower and nothing more"): this claim is
  KILLED if a canonical CAR-preserving inclusion of level n in level n+1 comes out of the second-quantised lift
  (d Gamma(v_i) squares to zero and {d Gamma(v_i), d Gamma(w_j)} = delta_ij in Cl(4,4) for k = 2 or Cl(8,8) for k = 3).
Overall: the exponential reading as a statement about the proved tower is refuted if E-asc and E-int both die; it is
"a valid arithmetic of a different functor" if E-fock survives; I will not call it proved as a statement about the
series' tower unless a stored result selects the rungs 3, 8, 256.

## N3. Independence of N: routes, choice, kill conditions
Routes: (a) the 9 November method: two exact models of the stored premise set at the same G, the same D-term level
xi G and couplings, with different Lambda (so different N), and a table of every stored relation that contains N
evaluated in both; (b) a symmetry proof: the homothety (dilation rotor of the trichotomy check plus rescaling of I)
maps the model at Lambda to the model at s^2 Lambda and every stored structure is covariant; (c) the promoted action:
N constant on each solution and taking every value (synthesis.promoted-norm-one-global-pair), which is already stored
for the gravitational sector.
Choice: (a) with (b) as the proof of clause "kinematic", citing (c) and not re-proving it.
Kill conditions (registered now):
- K-N3-1: independence is KILLED if any stored relation at its pinned version contains N together with N-free
  quantities whose values the premises fix (a relation, not an identity or a definition of an N-dependent quantity).
  Candidates to audit: the mode count pi N^2/ln 2 (integrality would quantise N), the lift locus and D-term vacuum
  (H enters the tree masses), the smallness monomials, the Majorana-scale results, the dating observation, the entropic
  weight, the tower reading (N2).
- K-N3-2: the two-model construction is KILLED if at fixed (G, xi, g, g', kappa) no vacuum exists for a second value
  of H, or a dimensionless N-free stored number differs between the two models (then N is tied to it).
- K-N3-3: the upgrade of the trichotomy's observation-level reading to "proved" is KILLED (stays "argued") unless the
  audit covers the full joint cone of the results mentioning N; I will label by what the audit covers.

## N4. Findings (no kill condition: reporting)
Where 4.8 x 10^122 falls under each surviving reading; what to restate in why-large and the two refuted.* entities.

## Results

### N1 + N2. Proposal synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent
Gate: check4 0 errors (2 I405 notes, expected untouched premises), validate ok with no E/W findings, registered,
coverage.yaml added. After registration the entity text was revised in place for the coordinator's points (base
count, scope of clause (iv), sibling named as intended citation); check.py unchanged since the check4 run; validate
rerun ok. Premises: tower.fock-module-one-qubit-per-rung@6, tower.witt-index-quantum-capacity@5,
tower.ladder-pairs-satisfy-car-vectors@4, tower.commuting-copies@5, tower.matrix-amplification-structural-properties@3,
tower.answers-iteration-question@5, std-algebra.existence-uniqueness@1, standard-model.trichotomy-what-kind-number@11
(the last only for the bracket 2^407 < C < 2^408).
- PROVED (i): read as "states become creators, as many annihilators adjoined" (Clifford algebra of F_k + F_k^*) the
  counts 3, 8, 256, 2^256 are exact; 2^256 is the number of pairs of the third level above the base. COMPUTED: rank 8
  in Cl(3,3); CAR of 8 state-indexed pairs in Cl(8,8); module dimension 256 by the vacuum idempotent's scalar part
  1/256 and by the Fock criterion. The level with 256 pairs is not constructed (not feasible, not needed).
- PROVED (ii): as the ascent it fails at the first step: 4 pairs and 16 states, not 8 (K-N2-1 fired on E-asc).
- PROVED (iii): 4^m <= dim A for m CAR pairs of ANY elements (simplicity of Cl(m,m)); B_j holds at most j pairs;
  the reading's levels are floors 3, 8, 256 of the proved tower, 4 and 247 floors passed over (K-N2-3 fired on
  E-int). ARGUED: "no stored tower result selects those floors" (read of tower.* and rungs.* statements, not a cone
  audit).
- PROVED (iv), scope the second-quantised lift only: Lie homomorphism, not a CAR family (K-N2-5 did not fire).
  NB's point stands and is recorded in the entity: the module carries an invariant symmetric form giving FOUR pairs
  at three (NB's proposal), so "no inherited fermionic structure" is true of the lift only.
- COMPUTED (v): the horizon count lies between 2^256 and 2^(2^256) like any number with log2 between 256 and 2^256;
  on the proved tower C states need 408 floors, C pairs need C floors.
- K-N2-4 (literal pairs): C(3,2) = 3, not 8; killed (arithmetic; NB records the stationary sequence 3, 3, 3).
- Base count: stated on Cl(3,3), three real pairs. The stored base three is the complex count on the (2,4) space
  (real Witt index 2); from two real pairs the recursion is 2, 4, 16, 65536. Said in the formal statement.
Verdict: the reading is not refuted as arithmetic and is refuted as a statement about the proved tower's ascent.
Transport-essential only in (ii), (iii); (i), (iv) are textbook second quantisation (cited from memory).

### N3. Proposal synthesis.number-n-free-at-fixed-d-term-level-on-the-stored-relations
Gate: check4 0 errors (3 I405), validate ok with no E/W, registered, coverage.yaml added. Premises:
synthesis.d-term-level-free-at-fixed-n@1, synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@6,
synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion@3,
synthesis.smallness-monomials-exact-hierarchy-casimir@3, synthesis.de-sitter-entropy-pi-n-squared@6,
synthesis.de-sitter-mode-count@3, standard-model.trichotomy-what-kind-number@11,
standard-model.imported-frozen-point-dictionary@9, synthesis.promoted-norm-one-global-pair@5,
synthesis.einstein-route-makes-n-initial-data@4, dark-energy.under-action-written-norm-parameter-laws@4.
- PROVED (i): at fixed G, xi G, g, g', kappa there is a vacuum for every H (frame with m = m*), same tree mass
  ratios; every (N, xi G) is realised. Rests on the stored d-term theorem's part (i) for criticality off the family.
- COMPUTED (ii): models A (H = 48, lambda = 32) and B (H = 63, lambda = 49), m* = 2080, N = 21 and 16, N* = 3104
  and 4481; realistic sizes: (v/M_P)^4 moves by about 2.3e-177 between N = 1e61 and 2e61.
- COMPUTED (iii): G Lambda = 3/N^2, S = pi N^2, the count, the Casimir identity, G v^2 N^2 = (v/H)^2, N*^2 = m*^2 +
  H^4 hold in both. K-N3-1 did not fire; K-N3-2 did not fire.
- PROVED (iv), under a stated definition: a function of the frozen point invariant under isometries and positive
  rescaling is constant on positive-norm frozen points (two reflections), so it cannot be N. This is the upgrade of
  the trichotomy's observation-level reading; it is close to a tautology made exact and covers only constructions
  without G. The change of N is a change of datum, not a symmetry (NB's test).
- ARGUED: "no other stored relation contains N". Audit actually done: pattern search of all 1371 formal texts (45
  entities, one-liners read, formulas at formal level), a second search for cosmological-with-gravitational symbols
  (77 entities, titles read, 12 one-liners), joint past cone of the 45 (519 entities, 40 postulates, postulate
  texts searched). K-N3-3: not a formal audit, so this clause stays argued, and the entity says so.
- What is fixed is xi G, not v/M_P (NB's formula (v/M_P)^4 = 4c^2 (xi G)^2 + 4 N^-4 agrees with N*^2 = m*^2 + H^4).
- Integrality: no stored statement makes the count an integer; said in the formal statement, not a result.
- Models are of the premises, not of the record (W = kappa N*^2 has an excluded charged pair), as in the mirror result.

### N4 (findings)
- 4.8e122 falls between the third and fourth levels of reading (i), as does everything from 1.2e77 to 2^(2^256);
  nothing stored selects it; log2 is about 407.4, no level. The reading has no contact with the value of N.
- Suggested restatements (maintainer, Leon to decide): standard-model.why-large (i): replace "a reading of the tower
  that no paper proves" by "the iterated Fock functor (states become modes), which is not the tower's ascent: the
  ascent gives 3, 4, 5"; drop or qualify "enormous state-counts are the default output of the framework's central
  structure" (true of state counts 2^j, false of mode counts j, and the horizon number is a mode count); (ii)-(iv)
  "close to the base case" has no content on the proved tower (floor 408 for states, floor 4.8e122 for modes).
  refuted.the-number-n-is-a-mystery-of-largeness: its refuter now rests on a reading decided against the tower;
  status "refuted" is hard to keep; its own technical text already carries both limits. The Dirac entity is
  unaffected by N2; N3 supports its "second modulus" sentence with the caveat that v/M_P is N-independent only to
  relative order (H/v)^4 at fixed xi G.

### What failed or was not done
- No rational model pair with H ratio 4 and rational frames exists in the small range searched; the pair used has
  H ratio 21/16.
- First validate of proposal 2 timed out under machine load; rerun passed.
- 256-pair level and anything beyond: not constructed. No power above 2^256 is formed in any check.
- No full-cone formal audit of N relations.

## Unexpected links
- The exponential reading's first two counts (3, 8) are the numbers 2^k of states, and NB's invariant-form rule gives
  4 at three, which is the proved tower's own next floor: the only rule agreeing with the proved ascent at the base.
- (i) of the N3 result gives joint freedom of (N, xi G), slightly more than the two one-sided statements.
- Cluster W link (not tested): the mode count is kappa_c times area, so a change of the residue (1/(4 ln 2) against
  3/(4 pi)) changes the count for given N and leaves N3 untouched, since the count is defined from N.

## Decisions for Leon
1. Restate standard-model.why-large and decide the status of refuted.the-number-n-is-a-mystery-of-largeness (keep
   "refuted" with a weaker refuter, or return it to open): recommendation, restate why-large as above and mark the
   refutation as not carried by the tower.
2. Whether to open an open problem for N (none exists; proposal 1 has no open_problem field, proposal 2 names
   op.rung-unit as the nearest).
3. Which base the reading intends (three complex pairs or two real ones), if the reading is kept at all.
4. Whether the units statement "qubits, one per rung" is to be read as an integrality condition on pi N^2/ln 2.
5. Literature in proposal 1 (second quantisation, Bratteli-Robinson) is cited from memory, as prior art only.
