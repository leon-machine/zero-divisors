---
id: standard-model.four-supersymmetric-splits
kind: claim
version: 5
title: Four supersymmetric splits
status: proved
region: standard-model
subject: standard-model
tags: [running-and-unification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - standard-model.spectrum-run@6
  - standard-model.two-threshold-criterion@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - num:8.16
- kind: check
  ref: check.py::check_coefficients_and_level_line
- kind: check
  ref: check.py::check_three_splits_miss_one_has_segment
- kind: check
  ref: check.py::check_scales_at_the_endpoints
locators:
  paper: T12
  number: Prop 8.16
  label: prop:splits
  line: 1452
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the species-level coefficients, the two-threshold level line, the three missing splits and the segment of split (d), and its endpoint scales by rigorous exp and pi bounds. Version 4 -> 5.'
  env: proposition
  context_refs:
  - standard-model.spectrum-run
  typing:
    by: ai-typing-pass
    added:
    - standard-model.spectrum-run
    - standard-model.hyp-s-slot-statistics
    note: 'Added the spectrum-run proposition, whose inputs the statement takes; kept the two-threshold
      criterion. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because its statement
      holds under Hypothesis (S). Levels pass: lay now keeps Hypothesis (S) and the record inputs.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.spectrum-run
    stated_role:
    - standard-model.hyp-s-slot-statistics
    note: "Proof is an exact or record-level run with no step naming (S); stated its role, the lepton doublet of the derived content, from Theorem hypercharge-global-form and Proposition weak-angle, which put the lepton doublet under (S)."
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: "Direct assumes of Hypothesis (S) removed: the proof uses no slot statistics of its own; (S) enters only through the inputs and content of standard-model.spectrum-run, which this result already uses and which now assumes (S), so (S) stays in holds_given and the statement keeps 'Under Hypothesis (S)'."
---

## formal
Under Hypothesis (S), at the inputs of Proposition \claimref{standard-model.spectrum-run}, split the supersymmetric content into a light set at $M_{I}$ and a heavy set at $M_{I}'$ in four ways: (a) gauginos and higgsinos light, sfermions and the second doublet heavy; (b) higgsinos light, the rest heavy; (c) both doublets light, the rest heavy; (d) wino, bino and higgsinos light, the gluino, sfermions and the second doublet heavy. In (a), (b) and (c) the line misses the triangle: no admissible pair at one loop. In (d) the admissible set is the segment from $(f, f') = (1, 0.991)$, every partner within a factor $1.34$ of $M_{Z}$ and $M_{U} = 2.0 \times 10^{16}$ GeV, to $(0.438, 0)$, the electroweak-inos at $7 \times 10^{8}$ GeV, everything else at $M_{U} = 1.6 \times 10^{14}$ GeV.

## technical
Under (S), at the record inputs, split the supersymmetric partner content into a light set at $M_{I}$ and a heavy set at $M_{I}' \ge M_{I}$ and apply the two-threshold criterion. With gauginos and higgsinos light, with the higgsinos alone light, or with both doublets light, the line misses the triangle $0 \le f' \le f \le 1$: no admissible pair at one loop.

With wino, bino and higgsinos light and the gluino, sfermions and second doublet heavy, the admissible set is the segment from $(f, f') = (1, 0.991)$, every partner within a factor $1.34$ of $M_{Z}$ and $M_{U} = 2.0 \times 10^{16}$ GeV, to $(0.438, 0)$, the electroweak-inos at $7 \times 10^{8}$ GeV and everything else at $M_{U} = 1.6 \times 10^{14}$ GeV.

## lay
Supersymmetry adds partner particles that change how the force strengths run, and these partners could sit at two different energy scales. Under the slot hypothesis (S) and the paper's input values, of four natural ways to divide them into a lighter and a heavier group, three fail to bring the forces together at one loop. The one that works keeps the gluino in the heavier group, and allows a range from nearly degenerate partners near the weak scale to a split spectrum with the electroweak partners near $10^{9}$ GeV.

## one-liner
Under (S), of four two-threshold splits of the supersymmetric content only the one with wino, bino and higgsinos light and the gluino heavy admits unification at one loop, along a segment with exact endpoints.
