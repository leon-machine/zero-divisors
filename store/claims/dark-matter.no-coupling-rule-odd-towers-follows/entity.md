---
id: dark-matter.no-coupling-rule-odd-towers-follows
kind: claim
version: 6
title: Three obstructions to a coupling rule for the odd towers
status: proved
region: dark-matter
subject: dark-matter
tags: [no-go, gauge-fields, undetermined-input]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
- name: Claude Opus 5.5
  role: GA rewrite (Hodge-star scaling as the scaling of hb^T on bivectors)
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass, restatement of the formal as its three established facts, the reading moved to a remark, at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Opus 5.5
  role: 'assumes edge to the common-ceiling-coupling premise dropped at Leon''s second-round decisions (scope kept as a text mention)'
  version: 6
  source: maintainer pass 2026-11-07 (decisions, second round)
review: typed
derivations:
- name: main
  uses:
  - dark-matter.mirror-tower-copy-one@9
  - dark-matter.residue-soldered-invariant-not-algebraic-one@5
  assumes:
  - dark-matter.p2-indifference@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_coupling_is_dimensionful_off_four
- kind: check
  ref: check.py::check_odd_towers_off_the_reversal_orbit
locators:
  paper: T14
  number: Prop A.4
  label: prop:norule
  line: 1517
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. Leon''s second-round answer 2: the assumes edge to synthesis.common-ceiling-coupling-premise@1 is dropped, since (c) cites the premise only for its scope (it equates the ceiling coupling along the reversal orbit and does not reach the odd towers) and no step rests on it; the formal, technical, lay and one-liner keep that scope as a text mention, which is part of what (c) states, not a condition. The P2 edge stays. Coverage''s untouched_premises entry for the premise removed. holds_given still lists the premise, reached through dark-matter.mirror-tower-copy-one@9 (used for (c)), which assumes it; only the direct edge goes.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version kept at 5 (already raised in this run). Leon''s answer 5 (B2): the formal level is restated as the three facts it establishes, (a) the coupling is dimensionful for d not 4 and the comparison length is not fixed, (b) no gauge coupling value is derived in the series, (c) the odd towers are off the reversal orbit and neither P2 (labels, not couplings) nor the common-ceiling-coupling premise (answer 2; assumes edge added) reaches them; the unproved conclusion that any rule is a further premise moves to a marked remark at the technical level, the structural-level disclaimer is dropped from the formal, the title follows the formal, status stays proved. The version-5 formal and title are kept under source_formal and source_title.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA in the proof of (a): the Yang-Mills density is det(hb)^{-1} <(hb^T F)^2>_0, and under g -> lambda^2 g (hb^{-1} -> lambda hb^{-1}) the volume factor scales as lambda^d and the outermorphism hb^T on bivectors as lambda^{-2}, so the action scales as lambda^{d-4}; the component form (the two inverse metrics in the star) stays as a labelled reading. A notation change: the scaling is immediate from the linearity of hb^T, and the existing check confirms the component scaling lambda^{d-4} in d = 3 to 6. Statement unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the scaling lambda^(d-4) of the Yang-Mills density under g -> lambda^2 g in d = 3 to 6, and the odd towers off the reversal orbit with non-isometric generating subspaces. Version 3 -> 4.'
  source_title: No coupling rule for the odd towers follows from the series
  source_formal: |-
    No rule relating an odd tower's gauge coupling to this tower's follows from the series' premises and theorems, for three independent reasons. (a) In a tower of dimension $d \neq 4$ the gauge coupling is dimensionful, $[g^{2}] = \mathrm{mass}^{4-d}$, so a comparison with this tower's dimensionless coupling needs a length, and in five dimensions that length is the size of the fifth direction, which the sheaf paper's wall construction does not fix \cite{ButlerT4}. (b) No gauge coupling value is derived anywhere in the series (the Standard-Model paper takes $\alpha_{\mathrm{em}}$ and $\alpha_{s}$ from the record \cite[Fact 2.8, Prop.~6.1]{ButlerT12}), so a rule for a dark tower's coupling would be a rule for ours first. (c) Premise \claimref{dark-matter.p2-indifference} cannot supply democracy: the odd towers are inequivalent to this one as soldered algebras (Theorem \claimref{dark-matter.residue-soldered-invariant-not-algebraic-one}), off the reversal orbit along which alone the audit equates (Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv)). Any rule is therefore a premise, and the paper adopts none; structural level, not proved in the sense of \cite{ButlerT1}.
  env: proposition
  context_refs:
  - dark-matter.mirror-tower-copy-one
  - dark-matter.residue-soldered-invariant-not-algebraic-one
  - standard-model.imported-one-loop-running-trace-ratio
  - standard-model.weak-angle-over-derived-generation
  outside_pilot_cites:
  - ButlerT1
  - ButlerT4
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.mirror-tower-copy-one
    - dark-matter.residue-soldered-invariant-not-algebraic-one
    note: 'Added the soldered-invariant theorem and the mirror-copy theorem, on which reason (c) rests;
      the Standard-Model citations in reason (b) document that no coupling is derived and are not premises,
      so they stay unedged. Levels pass: the lay and one-liner now name P2 as a premise and keep the structural-level
      qualifier.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.mirror-tower-copy-one
    - dark-matter.residue-soldered-invariant-not-algebraic-one
    - dark-matter.p2-indifference
---

## formal
Three facts bear on a rule relating an odd tower's gauge coupling to this tower's. (a) In a tower of dimension $d \neq 4$ the gauge coupling is dimensionful, $[g^{2}] = \mathrm{mass}^{4-d}$, so a comparison with this tower's dimensionless coupling needs a length, and in five dimensions that length is the size of the fifth direction, which the sheaf paper's wall construction does not fix \cite{ButlerT4}. (b) No gauge coupling value is derived anywhere in the series: the Standard-Model paper takes $\alpha_{\mathrm{em}}$ and $\alpha_{s}$ from the record \cite[Fact 2.8, Prop.~6.1]{ButlerT12}. (c) The odd towers are inequivalent to this one as soldered algebras (Theorem \claimref{dark-matter.residue-soldered-invariant-not-algebraic-one}) and lie off the reversal orbit, and neither premise that equates across towers reaches them: Premise \claimref{dark-matter.p2-indifference} equates sector labels, not couplings, and only along that orbit, and Premise \claimref{synthesis.common-ceiling-coupling-premise} equates the ceiling couplings of the two members of that orbit only (Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv)).

## technical
Three facts bear on a rule relating an odd tower's gauge coupling to ours. In dimension $d \neq 4$ the coupling is dimensionful, $[g^{2}] = \mathrm{mass}^{4-d}$, so a comparison with our dimensionless coupling needs a length, and in five dimensions that length, the size of the fifth direction, is not fixed by the wall construction. No gauge coupling value is derived anywhere in the series; ours are taken from the record. And neither premise that equates across towers reaches the odd towers, which are inequivalent to this one as soldered algebras and lie off the reversal orbit: indifference equates sector labels, not couplings, along that orbit only, and the common-ceiling-coupling premise equates the couplings of the mirror and this tower only.

\emph{Remark (a reading, not proved).} Taken together, the three facts say that any rule relating an odd tower's coupling to ours would be a further premise, and the paper adopts none. This reading is an inventory of what the stored results supply, at structural level, not a theorem in the series' strict sense: a rule could still follow from a result the series does not yet contain.

## lay
Saying how strong the forces are in an odd-dimensional hidden world, compared with ours, would need an extra rule, and three facts stand in the way of getting one from the series: the strength there carries units, so comparing it needs a length the theory does not fix; the series does not predict our own force strengths either; and the assumptions that treat worlds alike (indifference, P2, and the equal starting strengths of the mirror world) only link our world with its mirror image. The natural reading, that any such rule would be a new assumption, is stated as a remark, not proved.

## one-liner
Three facts block a rule relating an odd tower's gauge coupling to ours: off dimension four the coupling is dimensionful with no fixed comparison length, no coupling value is derived anywhere in the series, and neither indifference nor the common ceiling coupling reaches towers off the reversal orbit; that any such rule is a further premise is a remark, not a theorem.
