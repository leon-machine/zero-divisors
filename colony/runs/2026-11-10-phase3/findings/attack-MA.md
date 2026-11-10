# attack-MA (constructive), Cluster M: dark-matter premise reduction

## The 23 postulates and the split (written first, for MB)
Selection rule: every entity under store/claims with `status: postulate` and `subject: dark-matter` (23 entities).
Not counted: dark-matter.hyp-u-equal-rank-one-eigenvalues (status postulate, id in dark-matter.*, but subject
neutrinos); I will still report where it touches the table. Order: alphabetical by id. Odd numbers are owned by MA
(MB challenges), even numbers owned by MB (MA challenges).

| # | id | owner |
|---|----|-------|
| 1 | dark-matter.d-democracy-total-mass | MA |
| 2 | dark-matter.p1-single-frozen-point | MB |
| 3 | dark-matter.p2-indifference | MA |
| 4 | dark-matter.p3-nearest-dimension-representatives | MB |
| 5 | dark-matter.p4-democracy-asymmetry-over-oriented-towers | MA |
| 6 | dark-matter.p5-boundary-modes-hold-entropy-not | MB |
| 7 | dark-matter.premise-cpt-covariance | MA |
| 8 | dark-matter.premise-flag-as-datum | MB |
| 9 | dark-matter.r1-equal-mass-per-quantum | MA |
| 10 | dark-matter.r2-one-quantum-per-unit-ball | MB |
| 11 | dark-matter.r3-one-cell-per-unshared-direction | MA |
| 12 | dark-tower-matter.h1-momentum | MB |
| 13 | dark-tower-matter.h2-identification | MA |
| 14 | dark-tower-matter.hypothesis-s-slot-statistics | MB |
| 15 | dark-tower-matter.u-transposition-rule | MA |
| 16 | simulations.c-odd-towers-collisionless | MB |
| 17 | simulations.s1-one-species-per-tower | MA |
| 18 | simulations.s2-sheet-fluid | MB |
| 19 | simulations.s3-mirror-cluster | MA |
| 20 | simulations.s4-our-matter | MB |
| 21 | simulations.s5-halos | MA |
| 22 | synthesis.common-ceiling-coupling-premise | MB |
| 23 | synthesis.matter-asymmetry-registered-free-input | MA |

Division of filing: MA builds the dependency table (M1) and files the base statement (the audited table and the
reduction that follows from it). MB: please do not file the table; cite or attack it. Anything you find on a
postulate I own goes in your findings and I will restate.


## Pre-registered kill conditions (written before the computations of M2, M3)
- K0 (cluster, from RUN.md): none of the 23 is redundant; then the count stands as the cost of the fit.
- K1 (density law). Claim: the stored total uses R1 and R2 only through the product (mass per unit ball), so for the
  ratio R1, R2 and D are one premise E. Killed if a model with unequal quantum masses and compensating number
  densities changes any stored share, or if D holds in a model whose common length differs from the de Sitter radius.
- K2 (mirror term). Claim: the mirror's share one is obtained twice, by two disjoint premise sets (R1, R2 at D = 3;
  or P1, P2, common ceiling, the copy). Killed if either stored derivation has the other's premises in its past cone.
- K3 (P4). Claim: every stored use of P4 is its mirror instance, which a stored theorem proves without P4. Killed if
  P4 is in the past cone of that theorem, or if a stored result uses P4 on the fork r = 0.
- K4 (flag from CPT). Claim: in the stored four-ways definition, CPT covariance as typed at version 3 (C acts on the
  configuration space, x and Cx kinematically isomorphic, S o C = S, C flips the bit) already gives the conclusion
  the flag premise is used for. Killed by a finite theory satisfying the typed CPT clauses in which the bit is
  kinematic or constant on a nonempty solution space.
- K5 (independence claims): each "independent" needs a model in which the one postulate fails and the other 22 hold
  as stated; otherwise the label is "argued" or "undecided".

## M1. Dependency table (read from build/graph.json of the run's baseline; script work/MA/table.py, data table.json)
Dependence edges followed: uses, assumes, founded_on, specialises, derived_from. "direct" = entities with a
dependence edge to the postulate (all are `assumes`); "cone" = claims in its forward cone; "out" = cone entities
whose subject is not dark-matter. Last three columns: is the postulate in the past cone of (a) the closed form
dark-matter.unit-ball-rule (5.36432), (b) dark-matter.total-function-thickness (T(c), mirror share taken from the
population count), (c) dark-matter.population-count-one-share-half-percent (mirror share one).

| # | postulate | ver | direct | cone | out | (a) | (b) | (c) |
|---|-----------|-----|--------|------|-----|-----|-----|-----|
| 1 | d-democracy-total-mass | 1 | 2 | 2 | 0 | - | - | - |
| 2 | p1-single-frozen-point | 1 | 10 | 79 | 31 | - | Y | Y |
| 3 | p2-indifference | 2 | 8 | 145 | 92 | Y | Y | Y |
| 4 | p3-nearest-dimension-representatives | 3 | 4 | 144 | 90 | Y | Y | Y |
| 5 | p4-democracy-asymmetry | 1 | 2 | 37 | 17 | - | Y | Y |
| 6 | p5-boundary-modes-hold-entropy-not | 1 | 2 | 25 | 7 | - | - | - |
| 7 | premise-cpt-covariance | 3 | 4 | 11 | 10 | - | - | - |
| 8 | premise-flag-as-datum | 4 | 3 | 11 | 10 | - | - | - |
| 9 | r1-equal-mass-per-quantum | 1 | 6 | 47 | 27 | Y | Y | - |
| 10 | r2-one-quantum-per-unit-ball | 3 | 8 | 47 | 27 | Y | Y | - |
| 11 | r3-one-cell-per-unshared-direction | 1 | 6 | 47 | 27 | Y | - | - |
| 12 | h1-momentum | 1 | 3 | 42 | 23 | - | - | - |
| 13 | h2-identification | 1 | 3 | 19 | 3 | - | - | - |
| 14 | hypothesis-s-slot-statistics | 2 | 1 | 13 | 3 | - | - | - |
| 15 | u-transposition-rule | 2 | 5 | 19 | 3 | - | - | - |
| 16 | c-odd-towers-collisionless | 2 | 2 | 3 | 0 | - | - | - |
| 17 | s1-one-species-per-tower | 2 | 2 | 3 | 0 | - | - | - |
| 18 | s2-sheet-fluid | 2 | 2 | 3 | 0 | - | - | - |
| 19 | s3-mirror-cluster | 1 | 2 | 3 | 0 | - | - | - |
| 20 | s4-our-matter | 1 | 2 | 3 | 0 | - | - | - |
| 21 | s5-halos | 1 | 2 | 3 | 0 | - | - | - |
| 22 | common-ceiling-coupling-premise | 1 | 4 | 59 | 24 | - | Y | Y |
| 23 | matter-asymmetry-registered-free-input | 2 | 0 | 0 | 0 | - | - | - |

Direct dependants (all by `assumes`):
- 1 D: democracy-de-sitter-radius-unit-ball, two-reductions.
- 2 P1: imported-gravity-only-coupling, mirror-share-assembled, mirror-tower-copy-one, mode-counts-two-modules-which-one,
  parallel-boundary-mode-spaces-one-wall, population-count, projection-every-towers-content-dilutes-ones,
  stored-asymmetry-charge-not-number, superselected-hence-dark-exactly-stable, odd-extensions.belongs-tower.
- 3 P2: mirror-share-assembled, mirror-tower-copy-one, mode-counts-two-modules-which-one,
  no-coupling-rule-odd-towers-follows, population-count, total-function-thickness,
  towers-are-residues-single-clock-filter, one-relation.imported-indifference-instrument.
- 4 P3: flag-bit-exists-exactly-tower-dimension, population-count, towers-are-residues-single-clock-filter,
  dark-tower-matter.imported-towers-their-types.
- 5 P4: asymmetry-arrow-counted-fifteenth-refutation, population-count.
- 6 P5: parallel-boundary-mode-spaces-one-wall, stored-asymmetry-charge-not-number.
- 7 CPT: orientation-arrow-seventeenth-refutation, neutrino.imported-ceiling-under-hypothesis-u-arrow,
  one-relation.imported-flag-arrow-superselection, one-relation.record-chain-votes-measurement-without-collapse.
- 8 flag: the first, third and fourth of CPT's four (a subset of them).
- 9 R1: contact-mechanism-returns-r3, total-function-thickness, unit-ball-rule,
  dark-tower-matter.imported-unit-ball-rule, simulations.cluster-bound-two-dimensions,
  simulations.imported-unit-ball-rule-family.
- 10 R2: R1's six, and dark-tower-matter.population, dark-tower-matter.survival-sheets.
- 11 R3: democracy-de-sitter-radius-unit-ball, unit-ball-rule, dark-tower-matter.five-dimensional-towers,
  dark-tower-matter.imported-unit-ball-rule, simulations.effective-cross-section-sheet-matter,
  simulations.imported-unit-ball-rule-family.
- 12 H1: dark-tower-matter.gauge-algebras, synthesis.gauge-algebra-by-tower,
  synthesis.lowest-causal-residues-zero-four-content.
- 13 H2: dark-tower-matter.gauge-algebras, dark-tower-matter.same-kind-matter, synthesis.gauge-algebra-by-tower.
- 14 (S): dark-tower-matter.five-dimensional-content (one result only).
- 15 U: dark-tower-matter.five-dimensional-towers, gauge-algebras, same-kind-matter, synthesis.gauge-algebra-by-tower,
  synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free.
- 16 to 21 (C, S1 to S5): simulations.halo-shapes and simulations.merger, the same two for all six.
- 22 ceiling: mirror-share-assembled, mirror-share-one-how-fragile, mirror-tower-copy-one, population-count.
- 23 epsilon: none (motivated_by only; its own text says no assumes edge is drawn).

Read-off (computed from the graph):
- Used by nothing: 23. Used by one result: 14. Used by exactly two results: 1, 5, 6 and each of 16 to 21.
- Forward cone inside the subject only: 1 and 16 to 21 (seven postulates). Used outside the subject (cone leaves
  dark-matter): 2 to 15 and 22; widest are P2 and P3 (about 90 entities outside: quantum-fields, standard-model,
  dark-energy, tower, neutrinos, einstein), through towers-are-residues-single-clock-filter.
- The fitted number. The closed form 5.36432 (unit-ball-rule) has in its past cone FIVE of the 23: P2, P3, R1, R2, R3
  (with four foundation-level postulates of the clifford-structure subject). With the mirror's share taken from the
  population count instead (total-function-thickness) the set is P1, P2, P3, P4, R1, R2, common ceiling, and R3 as
  the choice c = 1: EIGHT of the 23. The other fifteen (D, P5, CPT, flag, H1, H2, (S), U, C, S1 to S5, epsilon) are
  in the past cone of no result that states the total. So "23 postulates for one number" overstates the cost of the
  fit as the graph records it: 5 (or 8) support the number; 15 support other results of the subject (the arrow
  refutation, the odd towers' content, the cluster simulations, the wall) or nothing.
- Not in the graph but in the text: the costed single-ideal clause of dark-matter.status-rule (vi) and the inference
  that all six towers are populated (dark-matter.which-towers-are-populated, conjectured) are conditions of the
  total with no postulate entity; dark-matter.hyp-u (subject neutrinos) is in cone (b), (c) through the mirror share.

Correction to the read-off above (found when auditing the proposal): besides the statements of the total, three stored
results that VARY its conditions mention 5.364 and have further postulates in their cones: P5 under
synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3; H1 under synthesis.lowest-causal-residues-zero-four-content;
H1, H2, U under synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free. So: 8 under the statements of the
total; 4 more (P5, H1, H2, U) under results about its conditions; D under the de Sitter reading (other totals); 10
(CPT, flag, (S) carried, C, S1 to S5, epsilon) under no result whose text contains 5.364 or the closed form.

## M2 and M3. Verdict per postulate
Labels: PROVED (exact, in the proposal), AUDITED (read from the graph), ARGUED (read from stored texts), UNDECIDED.
MB owns the even numbers; my lines on them are challenges for MB to test, not verdicts.

### Proposal filed (base statement of the topic; MB cites or attacks, does not refile)
synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball (proposals/, check4 0 errors 0 warnings,
validate ok, registered, coverage.yaml added). Clauses: (i) every share depends on R1 and R2 only through (E), equal
mass per unit ball; model with both violated and every share kept (PROVED). (ii) the democracy premise D is (E) in
the unit of the de Sitter radius, given the stored sphere reading; D and R1+R2 do not imply each other (PROVED given
the reading). (iii) the mirror's term is obtained twice, by derivations sharing only P2 and P3 among the 23; they differ by 1/200
on the burning branch (AUDITED + computed). (iv) R3, the cell shape and P3's dimensions each move the total (PROVED).
(v) the count 5 / 8 / 15 of the table (AUDITED). K1 did not fire (shares kept under rescaling; D fails at
ell != d). K2 did not fire (cones disjoint in dark-matter premises apart from P2, P3 via the census).
Transport-absent: this is bookkeeping of the fit, no transport structure enters.

### Mine (odd)
1. D, democracy of the total mass. Not derivable from the others (it fixes the unit to the de Sitter radius, which
   R1, R2 do not: model d != ell, total masses in ratio (ell/d)^D, exact). Not independent in content for the total:
   it is (E) at unit ell. EQUIVALENCE (M3): D = (R1 and R2 through their product) + (unit = de Sitter radius).
   Used by two results only, both about the de Sitter reading, whose totals (5.000, 5.667, 4.333) miss the record.
   Recommendation: keep as the premise of that costed alternative but stop counting it among the premises of the
   fit; or merge R1, R2, D for the total into one premise (E) with the unit a separate clause.
3. P2, indifference. ARGUED: it is the programme's indifference premise
   (scrambling.indifference-structural-premise-series, which P2's own first sentence cites as T8 Principle 5.4)
   applied to the towers with a scope restriction (labels, not states; finite mode set; indexical labelling). The
   stored theorem synthesis.indifference-is-curie-plus-single-valuedness (4) shows each P2 equality is the general
   premise for one datum; "never equates inequivalent components" is its clause (2), a theorem. So P2 is a
   SPECIALISATION, not a second premise: derivable from the programme premise in that formalisation, with the scope
   clause a restriction (the unrestricted premise gives xi = 1, which the record excludes, so the restriction is
   what is postulated). No edge joins the two entities, and both sit in the cone of the population count, so the
   graph counts one premise twice. Model separating them in the other direction (P2 holds, the programme premise
   fails elsewhere) is trivial. Recommendation: a `specialises` edge P2 -> scrambling premise (maintainer), and
   count them once. Also: dark-matter.total-function-thickness cites P2 for "equal shares within each odd pair";
   under R1, R2 that equality is automatic (same dimension, same V_D), so that `assumes` edge is not needed there
   (PROVED in effect by clause (i) of the proposal: the share is a function of D_r alone).
5. P4, democracy of the asymmetry. Its own text: a theorem for the mirror, void for the odd residues, a premise
   only on the fork r = 0. AUDITED: its two dependants (population count; fifteenth refutation (iii)) use the mirror
   instance only; the theorem that proves the mirror instance (dark-matter.mirror-tower-copy-one (v), by P2's audit
   of the stored charge, or more weakly by P1's orientation clause) does not have P4 in its past cone, so there is
   no circle (K3 did not fire). The fork r = 0 is sterile under P3 and closed by the two-time import; no stored
   result uses P4 there (dark-matter.which-towers-can-carry-arrow mentions it counterfactually, no edge).
   Verdict: REDUNDANT as a postulate on the stored population: a theorem where used, unused where a premise.
   Recommendation: retire P4 as a postulate (repoint the two `assumes` edges to mirror-tower-copy-one, keep the
   fork clause as a remark or a conjectured statement). Leon's decision.
7. CPT covariance. Not in any cone of the total; four dependants, all the orientation-arrow argument and its
   restatements. Independent of the other 22 (ARGUED): none of them mentions an action or a conjugation; a model
   with a CPT-odd term in an action (the stored convention's own counter-case: a real-linear flag conjugate flips
   the frozen point's integrand, synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation (5)) breaks
   it and touches nothing else. Part of it is checked, not premised (metric, completion, pairing, frozen-point
   action); the premised part is the gauge sector, spinors and later structures. See 8 for its relation to the flag.
9. R1, equal mass per quantum. For the total it acts only through (E) (proposal (i)). On the reversal pair it is a
   theorem of the common ceiling and the copy (m_2 = m_6, exact on the proton-only branch, 0.995 on the burning
   branch, where R1 as "mean mass per baryon" is false by half a percent). On the odd towers: independent
   (ARGUED; the series derives no mass or coupling for them, dark-matter.no-coupling-rule-odd-towers-follows, and
   the stored note on R1 against the mass formulas says "not in conflict, not derived"). Separately used (mass
   value) by simulations.cluster-bound-two-dimensions only.
11. R3. Independence is already stored and proved: synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3 (i).
   The contact mechanism (dark-matter.contact-mechanism-returns-r3) returns R3 from R1, R2 plus four clauses
   (C, I, S, O) that are not store entities: four unregistered clauses for one premise, not a reduction.
   Nothing to add; cited in the proposal.
13. H2. A reading (which algebra is called the gauge algebra), ARGUED independent of U and H1: the column g_r of
   synthesis.gauge-algebra-by-tower is "exact linear algebra on the hierarchy" with or without H2. In dimension four
   it is the Standard-Model paper's identification at observation level; H2 is that identification asserted for
   every tower. No derivation found. Three dependants; under no statement of the total.
15. U, the transposition rule. Three clauses that DEFINE the constituent, its field, the slot and pair groups, and
   forbid an adjoined imaginary unit: a definition in disguise (M3), in the store's own words "the definition of a
   constituent, its field and the two factors' groups is Premise U". As a definition it cannot be derived or
   refuted, only replaced (the stored note branches-break-u lists what other choices give). It does have content
   through what it excludes: with U, P3's choice at residues 1 and 7 follows (stored in P3 v3's note), so U makes
   part of P3 a theorem. Recommendation: type U as a definition (object) and keep the dependants' edges.
17. S1, one species per tower. Second clause (towers interact only through gravity) is the stored theorem
   dark-matter.superselected-hence-dark-exactly-stable (cited in S1 itself): derivable, not a premise. First clause
   is a modelling simplification in tension with the stored content of the five-dimensional towers under (S) (four
   Dirac species U, D, E, N: dark-tower-matter.five-dimensional-content); as "one fluid component" it is a
   specification of the simulation. ARGUED.
19. S3, the mirror in a cluster (ionised helium, bremsstrahlung only). Not independent of the store: the stored
   decimal estimate dark-tower-matter.mirrors-composition has the mirror helium only for xi between about 3e-3 and
   2e-2, neutron-rich at the gravitational floor and hydrogen-rich towards the N_eff cap. So S3 is a choice of a
   window of the free ratio xi, UNDECIDED in-store (decided by xi, which nothing stored fixes).
21. S5, halos (Hernquist matched to NFW, all species sharing the profile). A numerical set-up; nothing in the series
   bears on it. Convention of the simulation.
17, 19, 21 with MB's 16, 18, 20: all six have the same two dependants (simulations.halo-shapes, simulations.merger)
   and nothing else; none is under the total. M3: they are the specification of one numerical model, six clauses of
   one modelling premise. Recommendation: merge into one entity (or type them as model specification, not
   postulates), which takes the subject's count from 23 to 18.
23. epsilon as a registered free input. Used by nothing (its own text draws no assumes edge). It is a register entry:
   the statement "epsilon is not computed from anything stored" is about the theory, not a premise any derivation
   can use; the total uses only the equality of epsilon across the reversal pair, not its value. M3: bookkeeping in
   disguise. Recommendation: keep it (it is the count of free numbers) but in a class of its own with the
   other registered inputs (N, the rung unit, the Majorana scale, the 126 weight), not among the 23 "postulates
   supporting the ratio".

### Challenges to MB's (even) postulates
2. P1. Its orientation clause is used for the mirror's epsilon only as the weaker of two routes
   (mirror-tower-copy-one (v)); the first route is P2 alone. So for the share the orientation clause is redundant
   given P2. The one-metric clause is the widely used part.
4. P3. Partly a theorem already: at residues 1, 7 it follows from U (stored); at 3, 5 it is independent (stored
   Bott-shifted model). So the postulate content of P3 is residues 3, 5 and the even residues' window.
6. P5. Two dependants; under no statement of the total (only under the no-rule result through the wall).
8. Flag as datum. CHALLENGE (K4): in the stored four-ways definition, the stored proof of the seventeenth refutation
   uses the flag premise for one thing: that the bit q is a function on the configuration space with q(Cx) = -q(x).
   But the CPT premise at version 3 already types C as acting on fields with S_mu o C = S_mu on the configuration
   space of each S_mu, and names the flag conjugate as a factor of C. If C is an automorphism of ONE theory (acts on
   its configuration space and exchanges the flag's orientations), then both orientations are configurations of that
   theory with isomorphic kinematics: that IS the flag premise. If instead C is an isomorphism between TWO theories
   (one per sign), the CPT text still reads true and the flag premise is false; two-point model: theories T+ = {x},
   T- = {Cx}, q constant on each. So the flag premise is not derivable from the CPT text as it stands, but the pair
   is one premise plus a typing clause: "C is a symmetry of one theory, not an isomorphism of two". K4 as
   registered did not fire (no finite theory with the typed clauses has q kinematic; the stored check of the
   refutation already enumerates this), but the derivation is conditional on the typing, so I do NOT file it:
   verdict "equivalent to a clause of CPT covariance under the automorphism reading; independent under the other".
   All three dependants of the flag premise also assume CPT. Recommendation: merge the flag premise into the CPT
   premise as its typing clause (one postulate fewer), or keep both and say in each that they are one assumption
   read at two places. Both entities were added to the store on 21 and 22 October, after T14, by maintainer
   passes; T14 names only CPT.
10. R2. As R1: only through (E) for the total; on the reversal pair a theorem (equal stored charge and equal mode
   count). Used separately (number density) by dark-tower-matter.population and survival-sheets.
12. H1. In dimension four a stored Fact, a premise in dimensions three and five only.
14. (S) carried to every tower. One dependant. In dimension four the Standard-Model (S) is no longer a postulate
   (standard-model.hyp-s-slot-statistics, proved from the slot-module hypothesis). Question for MB: does the same
   derivation run in dimension five from a transposed slot-module hypothesis? Then (S) carried is that hypothesis
   carried, and the count does not drop but the premise moves to one shared with the Standard Model.
16, 18, 20. See 17 to 21.
22. Common ceiling. Its conclusion for the total (m_2 = m_6) is R1 on the reversal pair: given R1 it is not needed
   for the total; given it, R1 is not needed on the pair. One of the two is redundant for the mirror's term.

### Result against the pre-registered cluster kill (K0)
K0 does not fire. For the total: R1, R2, D collapse to one premise (PROVED); P4 has no premise content on the stored
population (AUDITED); the mirror's term has two disjoint derivations, so either (E) on the pair or {P1's orientation
clause, common ceiling} is spare for the number (AUDITED). Outside the total: P2 is a specialisation of a programme
premise (ARGUED); the flag premise is a typing clause of CPT (ARGUED); U is a definition; six simulation premises
are one model specification; epsilon is a register entry. No postulate was DERIVED outright from the other 22 plus
the foundation with an exact proof: the reductions are merges, restrictions and re-typings. Counting generously the
23 become about 13 distinct assumptions: P1, P2 (shared with the programme), P3, P5, CPT (with the flag clause),
(E) with its unit, R3, H1, H2, (S) carried, C-and-S (one model), common ceiling, plus U as a definition and epsilon
as a registered number.

### Midway read of attack-MB.md (done)
MB's table and split agree with mine. MB's leads (b) "D, R1, R2 jointly force the cell radius to the de Sitter
radius" and (e) "a two-presentation toy separates the flag premise from CPT" agree with clause (ii) of the proposal
and with my verdict on 8; I filed neither the flag statement nor anything on H1 (MB's candidate). MB's lead (a),
that S2 and C are premises of two exclusive readings assumed by the same two results, bears on the merge proposed
for 16 to 21: the merged model premise would have to carry the two readings (W) and (C) as alternatives.

### Proposals filed
1. synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball (base statement of the cluster).
   Final gate: check4 0 errors, 0 other findings; validate ok (I305 only). One proposal; nothing else rose above
   "argued", and a statement of exposure is not a derivation.

### Not filed, and why
- Flag premise from CPT: conditional on a typing of CPT; the finite logical step is already in the stored check of
  the seventeenth refutation. Finding only.
- P4 redundant, P2 a specialisation, U a definition, the simulation premises one model: audits and readings with no
  exact content to check; they are decisions, listed below.

## Unexpected links
- The mirror's share of one is over-determined: (E) at dimension three, and the population count, give it by
  derivations sharing only P2 and P3. On the burning branch they differ by exactly 1/200. If Leon keeps R1 as
  stated, the burning branch contradicts it at half a percent; if he keeps the burning branch, R1 must be "equal
  mass per unit ball" or restricted to the odd towers.
- Dark-energy exposure (cluster D): D (democracy) is the only dark-matter postulate that uses the de Sitter radius,
  so it is the only one of the 23 tied to Lambda > 0 being a constant of the laws; R1 to R3 with the cell radius d
  do not see Lambda. If w = -1 fell, D's unit would move with time and the two results under D would go with it;
  the fitted total would not (it does not use D).
- P2 and the programme's indifference premise are one assumption held twice in the cone of the population count;
  the same may be true elsewhere in the graph (families.* and one-relation.* carry "imported indifference
  instrument" Facts): a graph-wide audit of the indifference premise would likely remove more double counting.
- Premise U makes part of P3 a theorem (residues 1, 7; stored). A definition (U) is doing premise work for the
  window: op.window-p3 could be attacked through U at residues 3, 5 (which element of U fails for (12,1)? the
  stored Bott-shifted model says none, so there U cannot help).
- The CPT premise and the flag premise entered the store on 21 and 22 October by maintainer passes, after T14;
  T14 names only CPT. The pair is in no cone of the total but is counted among the subject's 23.

## Decisions for Leon
All are maintainer-only actions; none was taken. Recommendation first.
1. (E) as the premise of the total. Recommend: add one premise "(E): equal mass per unit ball, in a common unit" and
   have dark-matter.unit-ball-rule and dark-matter.total-function-thickness assume (E) and R3 in place of R1 and R2;
   keep R1 and R2 as premises of the four results that use the mass and the number density separately
   (simulations.cluster-bound-two-dimensions, dark-tower-matter.population, dark-tower-matter.survival-sheets,
   dark-matter.contact-mechanism-returns-r3). Alternative: leave the edges and record on R1, R2, D that the total
   uses only their product.
2. D (democracy of the total mass). Recommend: keep, labelled as (E) in the unit of the de Sitter radius and as the
   premise of the costed de Sitter reading only; do not count it among the premises of the fit.
3. P4. Recommend: retire as a postulate; repoint its two `assumes` edges (population count, fifteenth refutation)
   to dark-matter.mirror-tower-copy-one (v); keep the fork clause as a remark. MB should confirm no circle (my cone
   check found none).
4. P2. Recommend: a `specialises` edge from dark-matter.p2-indifference to
   scrambling.indifference-structural-premise-series, so the two count as one premise with a scope clause; and drop
   the `assumes` P2 edge of dark-matter.total-function-thickness if (1) is adopted (equal shares within an odd pair
   follow from the dimension).
5. Flag as datum and CPT covariance. Recommend: merge the flag premise into the CPT premise as its typing clause
   ("C is a symmetry of one theory whose configurations include the flag's sign, not an isomorphism between two
   theories"); the three dependants already assume both. Alternative: keep both and cross-reference. MB owns the
   flag premise and may recommend otherwise.
6. The six simulation premises (C, S1 to S5). Recommend: merge into one modelling premise of the cluster
   simulations with six clauses and the two readings (W), (C) as alternatives, or re-type them as model
   specification; they have the same two dependants and none is under the total. S1's second clause is a stored
   theorem and should cite it as such; S3 should say it holds on the window of xi where the stored composition
   estimate gives helium.
7. Premise U. Recommend: re-type as a definition (it defines the constituent, its field and the two groups), keeping
   the dependants' edges as `uses`.
8. epsilon (registered free input). Recommend: keep, in a class "registered free inputs" with N, the rung unit, the
   Majorana scale and the 126 weight, not counted as a postulate of the dark-matter fit.
9. R1 against the burning branch. Decide which stands: R1 exact for the mirror (then the proton-only branch), or the
   burning branch (then R1 holds for the mirror to half a percent only). Recommend: restrict R1 and R2 (or (E)) to
   the odd towers, where they are premises; on the reversal pair they are consequences of the population count.
10. The count to state in the series. Recommend the sentence: "the fitted total rests on eight of the subject's
   postulates, which reduce to P3, (E) on the odd towers, R3 and the mirror's premises; it fixes two shares against
   one measured number", in place of "23 postulates support one ratio".
11. Two conditions of the total have no postulate entity: the costed single-ideal clause (status-rule (vi)) and the
   inference that all six towers are populated (which-towers-are-populated, conjectured). Recommend registering both
   as postulates so that the total's `holds_given` shows them; this RAISES the count by two and is the truthful
   direction.
