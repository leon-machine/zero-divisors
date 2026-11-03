# Leon's decisions of 21 October 2026 (evening), and how to carry them out

Background: seed/CONTRADICTIONS_VALUES.md, seed/CONTRADICTIONS_STRUCTURE.md,
seed/SYNTHESIS_BRIDGES.md, seed/SYNTHESIS_GAPS.md, BUILD_REPORT.md (last
sections). Read the findings you are assigned in full before editing.

## Decisions

1. **T14 against T14c: supersede by T14c.** The T14 claims that T14c corrects
   (the mirror's temperature under P2; the mirror's helium composition at the
   floor and the 0.995 burning-branch share that relies on it; monopole
   confinement in the three-dimensional towers) are narrowed to what still
   holds, carry a caveat naming the T14c result, and the T14c result records
   `lineage.supersedes: [the T14 id]`.
2. **Euclidean partner: accept the Wick-rotor result and narrow the note.**
   The maintainer accepts `synthesis.wick-rotor-chiral-angular-rotor`. The
   state-selection note's `state-selection.euclidean-partner-curvature-selected`
   is narrowed to the action on spinors (each chiral half), and cites the
   Wick-rotor result and T05 Prop 7.21(3) (`singularity.euclidean-rotor-where-it-lies`).
3. **T12 dating: make it conditional.** `standard-model.dating-descent` states
   that Lambda and N were fixed at the origin under the Henneaux-Teitelboim
   promotion, and links the T10 result that proves "N is initial data" false
   for the action as written (`dark-energy.under-action-written-norm-parameter-laws`)
   and the T10 note that reconciles them.
4. **The two boost flows: name them distinctly.** Each result that speaks of
   "the boost flow" gets a recorded note (`extraction.flow_note`) saying
   which it means: the rotor flow exp(lambda sigma/2), which rescales the
   modes (T05 Thm 6.3, T08 Lem 4.2, T08 Asm 6.1 and their dependants), or the
   phase flow e^{-i omega t} on the modes (T05 Thm 7.16, T07 Def 2.7 and their
   dependants), which T05 Prop 7.21 identifies as the Euclidean rotation. Add
   one remark (a note, kind note, status remark, id
   `note.decisions.two-boost-flows`) that comments on the principal results of
   both and states the distinction and that the KMS analysis uses the phase
   flow while the scrambling law uses the rotor flow.
5. **Proposals: accept the eight proved ones** after an independent review;
   keep the de Sitter temperature conjecture as a proposal.
6. **Trichotomy: leave for now.**
7. **Duplicates: merge.** Keep one entity per pair, retire the other in
   store/tombstones.yaml with `replaced_by`, move every link and \claimref to
   the kept one.
8. **Small fixes, all four:** the misdirected function-linearity citations;
   the Page-curve result's status; Hypothesis (S) onto spectrum-run and (U)
   onto the ceiling proposition, P4 off the mirror-share result; the unnamed
   hypotheses (the real-breaking assumption, the trichotomy's exhaustiveness,
   CPT covariance) made store postulates and assumed where they are used.
9. **T16 and (R):** T16's modular-period result assumes (R); "unconditionally"
   goes from its levels.
10. **Boundary-mode count:** restate `pred.boundary-mode-density` in the
    physical convention, the other as a conversion; the kill condition's
    substance is unchanged.
11. **(U) against (EW):** add a `contradicts` link between
    `dark-matter.hyp-u-equal-rank-one-eigenvalues` and
    `standard-model.premise-ew-equal-weight`.
12. **Restatements:** correct T15's "grade-three state" to T14's grade zero,
    and T14a's "are populated" to "admit matter", in the store's text.

## How to edit

- Store entities are store/<kind>/<id>/entity.md (front matter, then
  `## formal`, `## technical`, `## lay`, `## one-liner`) with proofs in
  proof-<name>.tex. Read store/conventions.md.
- Before changing a formal level for the first time, if the front matter has
  no `extraction.source_formal`, copy the formal text there; before changing a
  proof, copy proof-NAME.tex to orig-proof-NAME.tex unless one exists.
- A change to the formal level, a proof, derivations (uses, assumes),
  `about`, lineage or other links is substantive: bump `version` by 1 once
  per entity. Level wording alone (technical, lay, one-liner) is not.
- Every premise in `uses` or `assumes` must be cited with \claimref in the
  proof text (W215); a \claimref must name an existing id (E214).
- Record on each entity you change, under `extraction:`, a key
  `decision_pass:` with `by: ai-decision-pass`, `date: 2026-10-21`,
  `decision: <number above>` and `note:` what changed.
- New postulates: folder store/claims/<id>/, status postulate, a formal
  statement taken from the paper's own words, levels written, subject, tags
  if apt, `proposed_by: {kind: ai, ...}`, `ai_involved: yes`, `version: 1`,
  locators to where the paper states it.
- Check after each step:  python3 -m tp check --store store --layers 1-3,5
  and fix every error and every W215 you caused. Other agents edit other
  entities at the same time; touch only what your assignment names (and the
  dependants a link move requires), re-reading each file just before you
  edit it.
- Do not edit pins in entities outside your assignment; the maintainer
  repins. Do not run verify scripts or layer 4. House style: no em dashes;
  never "honest" or "honestly"; British spelling.
