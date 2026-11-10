# maintainer-MN: the number N and the window reading (run 2026-11-10-phase2)

Acting for Leon on decisions 1 to 3 of DECISIONS.md. Files of section MB not touched. No check.py, proof or
coverage file was changed, so no runcheck or check4 run was needed. No agent spawned, nothing committed, no
removal, no repin, lock or build.

## Validation
`tp check --store store --layers 1,2,3 --keep-going --author leon`, last run after all MN edits:
0 errors, 0 warnings, 121 information findings (119 I213, I126, I305), the same information findings as the
baseline taken before any edit. Intermediate runs showed one error on an MB file that was being edited at the
time (one-relation.measure-indifference-borns-rule-located: E206, then E202); it was gone in the last run. No
error and no warning on any MN file at any point. store/open_problems.yaml parses.

## Entities changed

| entity | version | what |
|---|---|---|
| standard-model.why-large | 3 -> 4 | N2. Restated as rule-dependent at all four levels; status conjectured kept; credit entry and `maintainer_pass_2026_11_10`. |
| refuted.the-number-n-is-a-mystery-of-largeness | 2 -> 3 | N2. Technical, lay, one-liner restated; status refuted and refuted_by kept; credit entry and `maintainer_pass_2026_11_10`. |
| synthesis.window-reading-array-killing-energy | 2 -> 3 | N3. Two scope paragraphs, "at spacing kappa" in "What it is for" (i) and refutation condition (b), one sentence in "What it costs", technical, lay, one-liner; credit entry and `maintainer_pass_2026_11_10_scopes` (the key `maintainer_pass_2026_11_10` was taken by the version 2 pass). |
| synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent | 1 (kept) | N1. "Intended citation" sentence replaced by a named comparison; claimref to the invariant-forms result in clause (iv) and the closing paragraph; lineage entry; note on the source of the bracket corrected (below). |
| synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r | 1 (kept) | N1. "Sibling / intended citation" sentences replaced by named comparisons of the twist-integral and free-spacing results; two lineage entries. |
| synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages | 1 (kept) | N1. "Intended citation" of the free-spacing result replaced by a named comparison; lineage entry. |
| synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter | 1 (kept) | N1. The open question in the note (assumes edge to (Q)?) decided: none, as R3 and the attacker recommended; the (Q) clauses are hypotheses of clause (iv) and (Q) is in the cone through the null-ordering result. |
| store/open_problems.yaml, op.residue-killing-weights | n/a | N4, N5. Attack item 4 closed; one `known` paragraph; "at the spacing kappa of (Q)" in the statement; source line. |
| store/open_problems.yaml, op.counted-mode-energy | n/a | N5. One `known` paragraph; source line. |

Each of the four version 1 entities also carries a `maintainer_pass_2026_11_10` note; layers 1-3 accept them at
version 1. Not changed: synthesis.invariant-forms-on-the-fock-module-..., synthesis.number-n-free-at-fixed-d-term-level-...
(no intended-citation sentence left in either; the invariant-forms result already cites the base by uses edge).

## N1, how the citations were turned
All four leftover sentences name a result that itself cites the entity (invariant forms -> base; twist integral and
free spacing -> window base; free spacing -> twist integral). A uses edge back would be a cycle and nothing of the
later result is used in a proof step, so each became a lineage entry (`motivated_by`, the only lineage key that
fits; the schema has no "compared with") plus plain naming in the note, and for the exponential base a claimref
at the two places of the formal level that already spoke of "a rule through an invariant form". The base's note
said the second rule reaches "the tower's own next floor"; that is the wording R2 found false as an equivariant
statement, and it now reads "a Witt index that equals the pair count of the tower's next floor as a number only".

## N2, what the two entities now say
Both: the exponential reading (3, 8, 256, 2^256) is the iterated Fock construction, exact under the rule "states
become creators", and not a step of the proved ascent (three pairs become four); it is one of at least two
counting rules (second rule 3, 4, 8, 128, 2^127, from an invariant symmetric form), nothing stored selects one
(argued, a reading of the stored tower results, not an audit); the base three is a complex count on signature
(2,4) against a real count on Cl(3,3); the horizon count is of registered units and is compared in size only
(between 2^256 and 2^(2^256) of the first rule, between 2^127 and 2^(2^127 - 1) of the second); N stays a
registered free input (Premise synthesis.number-n-registered-free-input and the N-free result are cited).
What the reading supports is now worded as conditional: given such a rule, large counts arise in three or four
steps. Withdrawn in why-large: "large counts are the generic output of a tower, so the largeness of N requires
no mechanism". The refuted entity now says the refutation "is not carried by the proved tower" and stands only
given a counting rule. The candidate selection (iii) and the residue (iv) of why-large are kept; (iv) gained
"by which counting rule if by any"; a clause (v) states that nothing there derives or bounds N. No open problem
was created. The new claimrefs are text only (neither entity has a derivation; no edge added).

Side correction found while doing this: the exponential base attributes the bracket 2^407 < |J| < 2^408 to "the
technical level" of the refuted entity, but at version 2 that level did not contain it (only its strength-pass
note did). The bracket is now stated in the technical level of version 3, with its source (proof and check of
the trichotomy result), and the base's extraction note says so. The base's formal sentence is thereby true as
it stands.

Checked for sentences that now overstate, none edited:
- standard-model.largeness-number-universes-boundary-modes: no sentence about the exponential reading or a
  counting rule. It says "its boundary modes number pi N^2/ln 2"; see "For Leon" 2.
- standard-model.trichotomy-what-kind-number: no sentence about the exponential reading. Its units sentence
  ("qubits, one per rung of the Fock module") is flagged in the text as a statement of units only; see "For
  Leon" 2. Not edited also because it is at version 11 with a proof and check, the three N results pin it @11,
  and a claimref to the two-arrays result there would need a uses edge that pulls the thermal premises into its
  cone.
- refuted.the-number-n-is-a-coincidence-dirac: nothing about the reading; unchanged.

## N3, the window reading at version 3
Added: "Scope (one thermal period, spacing kappa)" and "Scope (a fibre, not a subsystem)", citing the three window
results and q-splits (iv); "at spacing kappa" in "What it is for" (i) and refutation condition (b), as R3 asked.
The reading itself, consequences (ii) to (iv) and refutation conditions (a), (c) are unchanged.

Dependants (forward cone through uses and assumes), content check:
- synthesis.null-ordering-of-counted-units-is-zeta-symmetric@4 (assumes the reading @2): its "only offset" is
  stated for arrays defined with weights kappa(k + delta), so it is already at spacing kappa. Not affected.
- synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays@1,
  synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content@1,
  synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping@1 (assume it @2): use only
  the value -kappa/24 per array at the stored array, or name the reading's scope. Not affected.
- Further down: the three window results, synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free,
  synthesis.mass-terms-are-pair-terms-of-the-arrays-..., synthesis.no-single-curvature-coupling-...,
  and (through the two-arrays result) the exponential base and the invariant-forms result. Not affected.
- Pins only: the four assumes edges `synthesis.window-reading-array-killing-energy@2` are now one version behind
  (for the orchestrator's repin).
- Outside the cone, content affected and NOT edited: note.programme.setting-seventeen-refutations (version 3,
  the T17 refutation table, rows 10 to 12) still says "largeness is generic for a tower and the question is why
  so small". It transcribes the paper's table; see "For Leon" 3.

## N4, N5
Attack item 4 of op.residue-killing-weights is closed in the file's form ("Closed by Leon's decision of 10
November (claimrefs). The item asked ..."): the count compares the array's own Gibbs entropy with A/4; the
continuum's entropy never enters; 3/(4 pi) per unit of two components (3/(2 pi) per component) is recorded as NOT
adopted, citing clause (v) of the window base. Status of the problem unchanged (reformulated, open). The
computed evidence that stood in the item is now carried by the three stored results and was cut to what they
state. One `known` paragraph was added to each of the two problems.

pred.boundary-mode-density (version 3) is not changed. Its kill condition, "A derivation of the calibration
residue from the boundary modes returning any other value", is not met: 3/(4 pi) comes from inserting the
area-law hypothesis and a counterfactual entropy, not from a derivation, and base clause (v) says so (R3 reached
the same reading).

## Instructions not carried out to the letter
None was false to the stored mathematics. Two places where the edit is narrower than a reader might expect:
1. N1 produced no new uses edge (see above: all four are comparisons, and a uses edge would be circular).
2. N2: the three entities to be "checked" were left unedited (reasons above).

## For Leon
1. Window reading, the words "in every state". The first paragraph still says an array's Killing energy "in
   every state" is the continuum's over the window. Base clause (ii) shows that at spacing kappa and any
   temperature other than the Hawking temperature the array's symmetric-ordered energy differs from the
   continuum's comparison value. Version 3 records this in the scope paragraph ("verified at the sea and at the
   Hawking state") but keeps the words, since decision 2 did not cover them. Both attackers recommended
   restricting the clause to the two states. Decide: restrict, or keep as the reading's stipulation.
2. The units sentence of standard-model.trichotomy-what-kind-number ("qubits, one per rung") and "its boundary
   modes number pi N^2/ln 2" in standard-model.largeness-number-universes-boundary-modes predate the stored
   statement that the count is of registered units averaging two arrays, not of ladder pairs. The bridge note
   (L3 (c)) and attacker NB (decision 2) put a qualifier ("units of capacity ln 2; not an integrality claim") to
   you; it was not among the four decisions, so nothing was changed.
3. note.programme.setting-seventeen-refutations still carries "largeness is generic for a tower" in the T17
   table. Either leave it as a transcript of the paper or add a pointer to version 3 of the refuted entity.
4. The window reading (a postulate) now names by claimref three results whose cones contain it. This is a record
   of scope, not a dependence, and the pass note says so; say if you would rather have plain text there.
5. The N-free result's extraction note points to colony/runs/2026-11-10-phase2/findings/audit-NA-number-n.md for
   the audit lists. The house rule keeps run and agent names out of store text; two older entities also cite
   colony paths. Left as is: removing it would lose the only pointer to the lists. Moving the lists into the
   store (or docs/) would settle it.
6. Status of refuted.the-number-n-is-a-mystery-of-largeness: kept "refuted" as instructed; its text now says the
   refutation is not carried by the proved tower. Attacker NA's alternative (return it to open) remains yours.

## For the orchestrator
- Repin: the four assumes edges to the window reading (@2 -> @3). Nothing pins why-large or the refuted entity
  by version (lineage and refuted_by are unpinned).
- No folder removal, no retirement, no tombstone in MN.
- Layers 1-3 should be rerun once MB has finished, since its files were still changing during this pass.
