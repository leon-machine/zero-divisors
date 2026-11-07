---
id: dark-matter.no-coupling-rule-odd-towers-follows
kind: claim
version: 5
title: No coupling rule for the odd towers follows from the series
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
review: typed
derivations:
- name: main
  uses:
  - dark-matter.mirror-tower-copy-one@8
  - dark-matter.residue-soldered-invariant-not-algebraic-one@3
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
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA in the proof of (a): the Yang-Mills density is det(hb)^{-1} <(hb^T F)^2>_0, and under g -> lambda^2 g (hb^{-1} -> lambda hb^{-1}) the volume factor scales as lambda^d and the outermorphism hb^T on bivectors as lambda^{-2}, so the action scales as lambda^{d-4}; the component form (the two inverse metrics in the star) stays as a labelled reading. A notation change: the scaling is immediate from the linearity of hb^T, and the existing check confirms the component scaling lambda^{d-4} in d = 3 to 6. Statement unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the scaling lambda^(d-4) of the Yang-Mills density under g -> lambda^2 g in d = 3 to 6, and the odd towers off the reversal orbit with non-isometric generating subspaces. Version 3 -> 4.'
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
No rule relating an odd tower's gauge coupling to this tower's follows from the series' premises and theorems, for three independent reasons. (a) In a tower of dimension $d \neq 4$ the gauge coupling is dimensionful, $[g^{2}] = \mathrm{mass}^{4-d}$, so a comparison with this tower's dimensionless coupling needs a length, and in five dimensions that length is the size of the fifth direction, which the sheaf paper's wall construction does not fix \cite{ButlerT4}. (b) No gauge coupling value is derived anywhere in the series (the Standard-Model paper takes $\alpha_{\mathrm{em}}$ and $\alpha_{s}$ from the record \cite[Fact 2.8, Prop.~6.1]{ButlerT12}), so a rule for a dark tower's coupling would be a rule for ours first. (c) Premise \claimref{dark-matter.p2-indifference} cannot supply democracy: the odd towers are inequivalent to this one as soldered algebras (Theorem \claimref{dark-matter.residue-soldered-invariant-not-algebraic-one}), off the reversal orbit along which alone the audit equates (Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv)). Any rule is therefore a premise, and the paper adopts none; structural level, not proved in the sense of \cite{ButlerT1}.

## technical
No rule relating an odd tower's gauge coupling to ours follows from the series, for three independent reasons. In dimension $d \neq 4$ the coupling is dimensionful, $[g^{2}] = \mathrm{mass}^{4-d}$, so a comparison with our dimensionless coupling needs a length, and in five dimensions that length, the size of the fifth direction, is not fixed by the wall construction. No gauge coupling value is derived anywhere in the series (ours are taken from the record), so a rule for a dark tower's coupling would first be a rule for ours. And indifference cannot supply equality: the odd towers are inequivalent to this one as soldered algebras and lie off the reversal orbit, along which alone the audit equates.

Any such rule is therefore a premise, and none is adopted. The result is at structural level, not proved in the series' strict sense.

## lay
Saying how strong the forces are in an odd-dimensional hidden world, compared with ours, would need an extra rule. The series supplies none: the strength there carries units, so comparing it needs a length the theory does not fix; the series does not predict our own force strengths either; and its indifference premise (P2), the assumption that treats worlds alike, only links worlds that are mirror images. Any such rule would be a new assumption. The argument is at structural level, not a proof in the series' strict sense.

## one-liner
At structural level, no rule relating an odd tower's gauge coupling to ours follows from the series' premises, since that coupling is dimensionful, no coupling value is derived anywhere, and the indifference premise P2 does not reach towers off the reversal orbit.
