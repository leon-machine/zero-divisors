# Maintainer pass M2 after run 2026-11-09-solvable (by: maintainer-2026-11-09)

Scope: the fifteen synthesis entities accepted on 9 November and store/open_problems.yaml. No other stored entity
was touched. No check.py or coverage.yaml was changed, so runcheck/check4 were not needed and not run.

Validation: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`, after my edits and M1's:
0 errors, 0 warnings (121 information findings, all I213/I126/I305). The fifteen entities therefore stay at version 1
(layers 1-3 accept the edits, which are only derivations, citations in proofs and extraction notes). open_problems.yaml
loads with yaml.safe_load; a field-by-field diff against the original shows that only the intended fields of the
thirteen problems changed. Not run: tp repin, tp lock, tp build, the full check. Nothing committed.

## Entities changed (all stay at version 1; each has a `maintainer_pass` entry, by maintainer-2026-11-09)
- synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays (1 -> 1): assumes
  singularity.q-joint-quasi-freeness-s-wave@3 and synthesis.window-reading-array-killing-energy@1; the proof's audit
  cites (Q) by \claimref; the "assumes edge for the maintainer" sentence removed.
- synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content (1 -> 1): the same two
  assumes edges; the proof cites both by \claimref (one parenthetical); the "assumes edge" sentence removed; the
  sibling's intended citation is now a plain cross-reference; the J3 sentence follows J3 v2 (the channel reduction
  narrowed to spin 2, the current-boson identification kept, so vectors and scalars stay currents under J3).
- synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping (1 -> 1): assumes (Q)@3,
  singularity.c2-cell-density@4 and the window reading @1; the proof cites (Q) by \claimref; the sentence reworded.
- synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free (1 -> 1): assumes
  dark-tower-matter.u-transposition-rule@2 (the current version); the sentence removed.
- synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge (1 -> 1): plain cross-reference to the
  breaking-pattern result.
- synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets (1 -> 1): plain cross-references to
  the field-level result ((ii) nilpotency; (iv), (v) masses).
- synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height (1 -> 1): plain cross-reference to the
  spin-class result.
- synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial (1 -> 1): plain cross-reference to the K-theory
  result.
- synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional (1 -> 1, note only): "For the
  maintainer" request replaced by the record of what was done (J3 v2 wording; op known text corrected).
- synthesis.joint-clifford-clause-is-an-instance-of-the-signed-direction-postulates (1 -> 1, note only): "the
  maintainer's decision" replaced by Leon's decision of 9 November, with the (F1) reading flagged.
- synthesis.koide-middle-mass-bound-closes-the-remaining-quark-dressing-class (1 -> 1, note only): no longer calls the
  stored theorem's sentence a misstatement; says it was corrected in its version 2 (orchestrator's request).
- Unchanged: synthesis.d-term-level-free-at-fixed-n, synthesis.gauge-factor-sugawara-parts-satisfy-virasoro-relations-on-the-band,
  synthesis.georgi-jarlskog-weight-free-on-the-stored-relations, synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3
  (no maintainer sentences in their notes).

## store/open_problems.yaml (statuses unchanged; every problem: `source` extended with "the 9 November results and
Leon's decisions", a "(9 November.)" paragraph in `known` with \claimref to the new entities, `entities` extended)
- op.wall-class-invariant (reformulated): item 1 restated as answered in the negative (k > ht from dimension five,
  unbounded excess, lens-space inputs cited from memory); the remainder is the exact count. The dim <= 3 table item
  stays, with a note on Leon's no-import decision. New item: derive the lens-space cohomology rings, q1 and the K-ring
  in the store. +2 entities.
- op.helicity-per-boundary-mode (partial): the known sentence corrected (1 - 2M/r for spins 0 and 1, sqrt(1 - 2M/r)
  for spin 1/2); paragraph on the horizon-channels result and J3 v2 (channel reduction assumed for spin 2 only, the
  current-boson identification and partial-wave lift premise for every field). Import item restated to spin 2 and the
  harmonic-analysis inputs. +1.
- op.odd-towers (partial): item 1 marked done (constituents-field, where-mass-begins, three- and five-dimensional
  content); one sentence on the Bott result. +4.
- op.qft-non-abelian-gauge-fields (partial): Virasoro item done (band domain only); Higgs-sector item restated to
  the interacting theory; paragraph on both BRST results. +3.
- op.hypothesis-s (reformulated): sign-bit item done; clause (f) restatement recorded. Also fixed a YAML defect: the
  sign-bit item was indented inside the Klein-convention item's block scalar and so was not a separate item; it is now
  one (attack count 6 -> 7).
- op.gram-square-and-face-space (partial): item 1 closed in the negative for QCD-type dressing; selectivity account
  for quarks dropped unless a dressing law favouring the heaviest quark is proposed; the known sentence saying
  D2 > D3 > D1 is "not treated" corrected. +1.
- op.counted-mode-energy and op.qft-structural-inputs (partial): the exact test (24 | n, two-model independence),
  verdicts under the two readings (relative to J3 v1, unchanged under J3 v2), Leon's "test, not a premise", the "78"
  marked a reading; the sea item and the three-generations item restated. +2 each.
- op.window-p3 (partial): split by residue (1, 7 from Premise U; 3, 5 free, window an input); the argued "every
  selector periodic mod 8" expectation revised; the pairing-reading item stays. +1.
- op.thickness-deposit-rule (partial): item 1 done on the orbit reading; the fit moves to eps (T = 1 + 4/eps = 5.364
  at eps about 0.917). +1.
- op.residue-killing-weights (reformulated): the N-copies form replaced (two sentences) by the mean-two, free-grouping
  result; light-ray count; item 1's second branch answered; count unit stays a decision. +1.
- op.pair-sector-current (partial): item 3 done; the factor 3 an input of the record. +1.
- op.rung-unit (partial): xi G free at fixed N (models on the record-excluded branch), consistent with the register. +1.

## Dependants and content to re-check
- Stale pins on my entities, for `tp repin` (M1's bumps): koide-middle-mass -> synthesis.mass-ordered-dressing-cannot-spoil-koide@1
  (now 2); lens-space-walls and two-rungs -> synthesis.lens-space-wall-rung-count-sees-the-integral-twist@5 (now 6);
  no-rule-p2 and the-residue -> dark-matter.stored-asymmetry-charge-not-number@9 (now 10). These changes are
  corrections or wording, consistent with my entities, so repinning should be a formality, with one exception:
- Content: the-residue formal (iii) says pi N^2/ln 2 counts registered units "not of light rays as
  \claimref{dark-matter.stored-asymmetry-charge-not-number} words it". After M1's v10 that entity no longer words it
  so. This needs a wording change at repin (for example "as its version 9 worded it"). It is formal-level, so I did
  not make it.
- Text-only version references in the one-window proof's audit of (v): J3@1, P3@2, R2@2 and rung-unit@3 are now at
  2, 3, 3 and 4. tp repin will not change them. The audit's per-premise readings still hold under the new versions
  (J3 v2 still covers every massless field's channels through the current-boson identification).
- joint-clifford: its extraction note quotes clause (f) in its version-4 CAR form. The result now justifies the
  restated clause (slot-module v5); the statement is unaffected.
- one-window (iv), light-ray reading (2), residue (i) and (iii): stated relative to J3 v1. Under J3 v2 the
  current-boson identification, which they use, is unchanged, so their content stands.
- New assumes edges widen these entities' declared premise sets: one-window, light-ray (+(Q), window reading),
  residue (+(Q), C2, window reading), Bott (+U). Their past cones already held these through other premises, so
  layer 3 is unchanged. check4 was not rerun, since no check changed; if layer 4 flags the new assumes as untouched
  premises (I405 or W405), coverage.yaml may need entries.

## Not done, and why
- Statuses: none changed. The brief keeps problems partial unless settled. op.pair-sector-current's success clause
  ("a no-go ... which would make the second family's factor 3 an input") is met on the stored relations. op.thickness-deposit-rule's
  ("a proof that no rule P2 licenses gives it") is met on the orbit reading. Leon may judge either settled.
- The header limits `entities` to 2-8 ids. As the brief asked, I extended the lists anyway: now 9-14 ids. The limit is
  not enforced (op.qft-non-abelian-gauge-fields already had 11). Trim if Leon wants the limit kept.
- Problem `statement` fields were not edited. op.helicity-per-boundary-mode's still calls joint J3 open in full.
- Optional overlap note from R2 (cite the Bott and no-rule-p2 results together as the two inputs of the unit-ball
  relation): done only in the open-problem text, not in the entities.
