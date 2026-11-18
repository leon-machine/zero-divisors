# Maintainer report M1: store entities (run 2026-11-18-leads)

After Leon's decisions D1 to D4 of 18 November 2026. Eleven entities and store/conventions.md were edited in place.
Nothing was committed or pushed, no agent was spawned, no process was killed; layer 4, check4, validate_draft and
repin were not run. No check.py was touched, so runcheck was not needed. Not touched: store/open_problems.yaml, the
thirteen newly accepted entities.

Bookkeeping on every changed entity: version + 1; a credit entry (Claude Fable 5.2, the role, the new version,
source 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'); an amendments entry (kind, defect); an extraction
entry maintainer_pass_2026_11_18_leads with a note. Every stored file kept. Copies of the entities as they were
before this pass are in /tmp/m1/backup/ (scratch, not in the repository).

## Check

`python -m tp check --store store --layers 1-3 --keep-going --author leon`, run once after the last edit and after
store/claims held all thirteen new ids (proposals/ empty, no accept running): 0 errors, 0 warnings, 121 information
findings (119 I213 subject notes, I126, and I305: the working tree touches 38 entities, 58 claims and 15 documents
depend on them). Log: /tmp/m1/check_l13.log. Layers 1 to 3 do not report stale pins; they are listed below.

## Changes, item by item

| item | entity | version | kind |
|---|---|---|---|
| 1 | sheaf.wall-class | 3 -> 4 | restatement |
| 2 | synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries | 2 -> 3 | restatement (D3) |
| 2 | synthesis.de-sitter-field-fixes-the-observer-tube-point | 4 -> 5 | correction |
| 3 | synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional | 1 -> 2 | restatement (dated note) |
| 3 | hawking.joint-j3-s-wave-reduction | 3 -> 4 | restatement (dated note; premise not narrowed) |
| 3 | hawking.helicity-lift-joints-itemised | 7 -> 8 | restatement (dated sentence) |
| 4 | synthesis.imported-whitney-product-formula-and-projective-space | 1 -> 2 | restatement (clause added) |
| 5 | interior.duality-monodromy-fibration-over-ring | 5 -> 6 | restatement (dated note) |
| 6 | scrambling.return-delay-scrambling-log-recovered | 3 -> 4 | restatement (dated note) |
| 7 | synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records | 1 -> 2 | restatement |
| 8 | synthesis.gravitational-pair-production-from-the-operator-source-at-first-order | 1 -> 2 | correction |
| 9 | store/conventions.md | (no version) | paragraph added |

"Restatement" is declared wherever the formal level's text changed, because the validator's rule E607 ties the kind
to whether the formal level changed; where only a dated note was added the amendment's defect and note say that no
clause was reworded.

### 1. sheaf.wall-class (D4)

The draft was checked against synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line as accepted
(version 1). Applied at all four levels; status stays conjectured; clause (b) untouched.

- (a), old: "its coarse part, the clock mismatch of Theorem sheaf.conservation-degeneracy-absolute-form, obstructs
  the strict two-sided completion". New: "its coarse part, the signature jump across the wall ((1,-1) on a wall
  whose sides have signatures (p,q) and (p-1,q+1)), whose residue is the clock mismatch 2 of clause (1) of Theorem
  synthesis.wall-class-one-rung-obstruction, obstructs the strict two-sided completion (Theorem
  sheaf.conservation-degeneracy-absolute-form)".
- (c), old: "it refines, at sheaf level, the conservation-of-obstruction conjecture of [T1, Conj. 7.9], whose
  fibre-level content is the mod-8 obstruction of the transport rules". New: the wall's instance of the eigenbundle
  class of clause (4) of the strict-completions theorem, whose opposite every completion nondegenerate everywhere
  carries on its exterior forms; the first form is named as replaced, the first paper's conjecture being refuted
  as stated; then the sheaf-level sentence.
- Closing sentence extended with "Towards (c): ..." and "Not shown: ...".
- Technical, lay and one-liner to match ("the clock mismatch with a torsion part" -> "the signature jump with a
  torsion part").
- lineage.motivated_by gains the strict-completions theorem, the rung-count theorem and the new result.

Where the draft said more than the stored result, the stored result was followed:
1. The draft cited the clock mismatch 2 from sheaf.conservation-degeneracy-absolute-form, whose statement does not
   contain it. It is cited from clause (1) of the one-rung theorem, as the accepted result does.
2. The draft gave the signature jump (1,-1) for every tame wall. The side signatures are hypotheses of the one-rung
   theorem, not of tameness (the accepted result says so), so (1,-1) is stated for those signatures.
3. The draft's "Towards (c)" sentence gave the collar comparison for "a compact wall with a product collar". The
   hypotheses of the accepted result are added (corank one; side signatures; completions standard outside the
   interior of the collar; nondegenerate at every point).
4. The draft said "so the class refines the sheaf-level jump". Clause (4) of the rung-count theorem says that the
   pair determines the jump and is strictly finer on the torus wall; that is what is now quoted.
5. The draft's lay sentence "survives in that form" is worded "this is the form in which it is conjectured to
   survive".

### 2. The tube-point clause (D3)

synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries, status postulate, restated at every level
by Leon's decision D3; the amendment and the extraction note say so.

- Clause, old: "In a gravitational field of which K generates a symmetry, m is invariant under every symmetry of
  the field that commutes with K, acting on tube points complex-linearly." New: the field has a Killing horizon; the
  gauge is adapted to the horizon's flow (the flow of K is the flow of a positive multiple of the horizon's Killing
  field; the rotations among the symmetries commuting with K, those generating a compact group, act on tube points
  by bivectors); m is fixed by every such rotation; where no observer of the region meets the condition the clause
  is silent: no tube point selected, no state excluded, rho free. A sentence says the boost is not among the
  symmetries asked to fix m (cited from the new result's opening paragraph). The version-2 wording is kept in the
  extraction note.
- "What it is for", old: "It decides fields with one horizon only: ... for the Schwarzschild field it is not
  computed." New: the de Sitter selection in the gauge hb = sigma with K the horizon's flow; Lambda <= 0 as before;
  on the Schwarzschild exterior and the static region of Schwarzschild-de Sitter (either horizon) no observer meets
  the condition, the clause is silent, rho free (new result, (iv) to (vi)); the norm and free-fall candidates
  (none at finite distance on Schwarzschild; r_0^3 = 3M/Lambda with one scale per horizon, ratio 8/5 in the sample)
  are stated as not adopted.
- "What it costs": the restriction to rotations and to the horizon's flow is named as adopted, not derived, with
  what was wrong with the first wording (nothing fixed if the boost is counted; gauge dependence; the twisted
  gauge, in de Sitter too). Old last sentence "Fields with more than one horizon need a further premise assigning
  an observer's tube point to one horizon" -> "On the Schwarzschild and Schwarzschild-de Sitter fields the clause
  fixes nothing, and the question whether a tube point is assigned per observer or per horizon is not reached; a
  scale there needs a further premise, which is open (op.which-capacity)."
- Refutation condition: (a) unchanged; (b) "on a field with one horizon" -> "on a field where the clause decides
  (of the fields computed, the de Sitter field)"; (c) "the field's symmetries commuting with the boost" -> "the
  rotations of the field commuting with the boost".
- Title: "invariance under boost-commuting symmetries" -> "invariance under the rotations commuting with the
  horizon's boost". The id is unchanged.
- The new black-hole result is cited in the text and added to lineage.motivated_by (a postulate has no uses edge).

synthesis.de-sitter-field-fixes-the-observer-tube-point: the formal level and clauses (i) to (viii) are unchanged.
- Technical level and the proof's reading: "which carries that hypothesis gap and decides fields with one horizon
  only" -> the hypothesis gap, then a dated sentence: the clause as restated; clause (ii) is a computation in the
  gauge hb = sigma with K the horizon's flow, so the selection stands on that reading; silent on the black-hole
  fields, citing the new result in the text (not a uses edge: that result uses this one).
- One-liner: "the field's symmetries commuting with a wedge's boost fix exactly" -> "the rotations among the
  field's symmetries commuting with a wedge's boost fix exactly" (clause (ii) proves it for the three transverse
  symmetries); the closing words name the clause as restated. Lay: one clause added.
- The assumes pin on the clause moved 2 -> 3, since the use was read against the restated clause in this edit.

Looked at and left unchanged:
- synthesis.wick-rotated-boost-selects-observer-tube-point (named in the brief): it predates the clause, does not
  cite it, does not say it decides fields with one horizon and does not quote its wording; it says the scale is
  left free by the boost data and is a premise not derived there, which is still true. A version bump would also
  make the new black-hole result's pin on it stale for no change of content.
- synthesis.stelle-west-norm-is-no-local-output: cites the clause in lineage only.
- The other entities matching "tube point" (std-algebra.complexification-is-the-odd-extension,
  synthesis.frozen-point-datum-is-h, synthesis.operator-join-point-spectrum-on-positive-energy-modules,
  synthesis.operator-join-positive-energy-no-finite-energy-zero-modes,
  synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale,
  synthesis.positive-structure-is-twistor-form-at-imaginary-time,
  synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them) speak of tube points, not of
  the clause.

### 3. The even-parity channels

synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional: no clause reworded. A
"Note (18 November 2026)" after the list of cited facts: (C3) is clause (4) of the new even-parity result; what
clause (5) needs beyond (C3) is that result's clause (5); (C1) and (C2) are still cited from memory; clause (3) is
superseded on oscillating channels only; and (added beyond the brief, from the accepted result's clause (2))
clause (1) no longer depends on the argued degree bound. Matching sentences in the technical level, the lay level
and the one-liner. Cited in the text only (the new result uses this theorem). The title still reads "even one
way": left, since the theorem's own clauses are unchanged.

hawking.joint-j3-s-wave-reduction (postulate) and hawking.helicity-lift-joints-itemised: neither lists the
even-parity reduction as open; both list it as premise, and J3 gives as the reason that the store shows one
direction only, at sample points. That reason is no longer true of the store, so a dated note is added to each
(J3: formal, technical, lay, one-liner; helicity-lift: joint J3 in the formal level and in the proof, technical,
lay, one-liner): the reduction for even-parity spin 2 is now derived on channels with l >= 2 and real nonzero
frequency, in the static frame, given (C1) and (C2). The premise is NOT narrowed: its even-parity clause stays as
stated (see "Needs Leon", 1). In helicity-lift the assumes pin on J3 moved 3 -> 4 with the edit.

### 4. The Whitney Fact

synthesis.imported-whitney-product-formula-and-projective-space: clause (iv) added, "(Dimension axiom.) For a real
vector bundle E of rank k, w_0(E) = 1 and w_j(E) = 0 for every j > k", at all four levels. Provenance: Milnor and
Stasheff, section 4, the Fact's existing source (key MilnorStasheff1974 in store/references.yaml); the axiom's
wording and its place there (the first axiom) are marked in the provenance and in the note as recalled from
memory, not checked against the book. Clauses (i) to (iii) unchanged.

### 5. interior.duality-monodromy-fibration-over-ring

A dated note at the formal, technical and lay levels, labelled in the text "a reading, computed in a working file
and not refereed, with no stored result behind it"; the conjecture's wording and the one-liner are unchanged.
Content from findings/attack-W.md, lead 3, written in the stored Kerr theorem's notation (w = z^2, z = r - I a
cos theta): the plane family of clause (5) of the strict-completions theorem in the coordinate w has positive
eigenline R z; H = M Re(z)/|z|^2 is linear in the unit eigenvector, odd under the deck map, H^2 a function of w
(computed); so the forced cover is the orientation cover of that eigenline, an identification forced by parity
alone; the winding three is the degree of -M z^-3 in z and only its parity, the stored holonomy -1, is a class of
a degenerating form (argued); the Kerr-Schild cometric does not degenerate at the ring, so no stored completion
statement applies (computed at sample points); the rescaled cometric on the cover was not treated.

### 6. scrambling.return-delay-scrambling-log-recovered

A dated note in the formal level, with matching sentences at the other levels: as a statement about the return of
information the estimate has no proved core; clauses (a) to (d) of the spreading law as restated do not reach it
(what they prove of the count is the doubling arithmetic on one generator, the law's clause (a)); the exponent's
account is the law's clause (b), a count in rapidity; the law itself, clause (e), is an estimate; the delay stays
conjectured and is pointed to op.island-dictionary. Status unchanged. The uses pin on the spreading law moved
6 -> 7 with this reading.

### 7. The stored Pell theorem

synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records, last sentence of clause (v), old:
"the running maxima by increasing denominator are exactly 2, 14/5, 82/29, 478/169 for denominators up to 400
(computed, not proved beyond that range)". New: they are exactly the S_n for every denominator (for every D the
largest pure-state value of denominator at most D is S_n with n the largest index with Q_n <= D, attained only
there); the sentence is stated as not proved in this theorem but in clause (iii) of the new Pell result, which
uses clauses (ii) and (v) here without that sentence; the check's enumeration up to 400 is kept as such. Clause
heading, one technical sentence and the last sentence of the proof of (v) to match. Evidence named in the
amendment: check.py::check_denominator_law_and_the_pell_records. Text citation only (a uses edge would be a
cycle).

### 8. The pair-production theorem

One remark of two dated sentences appended to proof-main.tex: the channel weights of (iv) are rederived without
angular integration by the rotation-weights result, clause (iv); on the chain's bath (188, 48, 21) the
coefficients of (v) are those of the heating result, clause (iii) (a produced vector's is 2.19 times its value
from the Standard Model's bath). The remark says the two results are used nowhere in the proof; no uses edge. It
is in the proof file, not the formal level, so that the statement is unchanged and the amendment is a correction:
the theorem has seven direct users and a restatement would ask for each to be re-read against a statement that
has not changed. The validator did not object.

### 9. store/conventions.md, "Gravity and the graviton"

Two paragraphs added after "Scope of that position". "Requirement (18 November 2026)": the series requires that
no signal pass outside the light cone; so a gravitational field with no variables of its own, a field slaved to
its source, is not the full account of the field; how the requirement is met stays
op.gravitational-field-at-null-momentum; no stored result is to be read as saying that the two null-momentum
components carry states or variables, that the field has a quantum, or that they carry none. Then the three
results, each with its label (proved; proved in a lattice Maxwell model, the step to gravity by analogy; proved
under hypothesis (D), the size argued: about 1.3e-13 in the proposed experiments, of order one near 190 kg at a
metre against 1e-14 kg). The earlier paragraph is left as dated text; the new one says it replaces that
paragraph's clause leaving the requirement undecided.

## Declined, and why

- J3 was not narrowed (premise decisions are Leon's, POLICIES 4; the narrowing is item 3 of the attack's
  "Decisions for Leon" and is not among D1 to D4).
- The Wick-rotated tube-point result was not amended (above).
- No stale pin on a dependant was moved, except the three pins inside entities this pass edited and read against
  the new versions (de Sitter -> clause@3, helicity-lift -> J3@4, return delay -> spreading law@7).

## Stale pins left for the repin (computed from the front matter; 20)

- hawking.helicity-lift-joints-itemised (now 8): scrambling.imported-collars-coframe-exceptional-set-helicity,
  synthesis.array-ln2-is-zero-mode-doublet-one-tower, synthesis.attachment-conformal-energy-is-generated-by-z,
  synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free (all @7).
- hawking.joint-j3-s-wave-reduction (now 4):
  synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature,
  synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet (both @3).
- synthesis.chsh-over-the-rationals-...-pell-records (now 2): the new Pell result (@1).
- synthesis.de-sitter-field-fixes-the-observer-tube-point (now 5): the new black-hole tube-point result (@4).
- synthesis.gravitational-pair-production-from-the-operator-source-at-first-order (now 2):
  dark-matter.coefficients-floors-they-give-what-gravity, dark-matter.seeding-gravity-floor-dark-towers-temperature,
  synthesis.seeding-remainder-excludes-perturbative-pati-salam, synthesis.untuned-fit-caps-lightest-heavy-neutrino,
  and the new two-free-directions, heating and rotation-weights results (all @1). Content of the theorem
  unchanged: a formality.
- synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional (now 2): the new
  even-parity result (@1).
- synthesis.imported-whitney-product-formula-and-projective-space (now 2): the new eigenbundle result,
  synthesis.order-four-structure-on-real-projective-walls-and-the-signed-count-modulo-sixteen,
  synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side,
  synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial (all @1). Clauses (i) to (iii) unchanged.

## Needs Leon

1. J3: drop the even-parity clause of the channel reduction (premise version 5), and import (C1), (C2)
   (completeness of the tensor harmonics; reachability of the Regge-Wheeler gauge for l >= 2) as Facts? Until then
   J3 and the helicity-lift result say that the clause is kept and that on oscillating channels it adds only (C1)
   and (C2).
2. The tube-point clause as restated, three points beyond D3's sentence: (i) its hypothesis includes that the
   rotations act on tube points by bivectors (the new result's reading (a)); a gauge in which K is the horizon's
   flow and no rotation acts by a bivector (reading (c), argued only) is outside the clause as now worded;
   (ii) refutation condition (b) is narrowed to fields where the clause decides; (iii) the title is changed.
3. The dimension axiom's provenance is from memory; a look at Milnor and Stasheff, section 4, would close it.
4. The title of the horizon-channels theorem still says "even one way".
5. op.kerr-ring and op.which-capacity carry the matching statements (the other maintainer's file); the Kerr note
   here is labelled computed and not refereed.

## For the orchestrator

- accept.log, entry for synthesis.additive-weights-...: its E206 on hawking.helicity-lift-joints-itemised
  ("substantive fields changed without a version bump") was caused by this pass. The entity's text was edited in
  one step and its version bumped in the next, a few minutes later, and the accept validated the store in between.
  The entity has been at version 8 since, and the proposal is now in store/claims (proposals/ is empty). The E122 lines in the
  same entries are the proposals' own.
- Two accepted entities (not mine to edit) now carry a sentence overtaken by this pass:
  synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line says the dimension axiom is "not stated in
  the text of that Fact" (it is, from the Fact's version 2);
  synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent discusses "the
  clause as worded" and ends "which reading is the series' ... is not decided here" (D3 decided: its reading (a),
  silent where unmet). Both are true of the versions they pin.
- The dated notes in the store name the date and the cited result, not the run.
