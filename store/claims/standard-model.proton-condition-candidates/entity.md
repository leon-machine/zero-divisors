---
id: standard-model.proton-condition-candidates
kind: claim
version: 5
title: The proton condition on the candidates
status: proved
region: standard-model
subject: standard-model
tags: [running-and-unification, confronted-with-data]
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
  - standard-model.imported-proton-condition@1
  - standard-model.one-threshold-exact-criterion@3
  - standard-model.two-threshold-criterion@4
  - standard-model.four-supersymmetric-splits@5
  - standard-model.supersymmetric-row-two-loops@6
  - standard-model.spectrum-run@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_three_admissible_rows_fail
- kind: check
  ref: check.py::check_segment_crossing
- kind: check
  ref: check.py::check_two_loop_row_meets
locators:
  paper: T12
  number: Prop 8.22
  label: prop:proton
  line: 1509
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: lifetimes and scales of the three admissible rows, the crossing on the segment of split (d), and the two-loop row, with rigorous rational bounds on pi and exp. Version 4 -> 5.'
  env: proposition
  context_refs:
  - standard-model.four-supersymmetric-splits
  - standard-model.spectrum-run
  - standard-model.supersymmetric-row-two-loops
  - standard-model.table-exact
  typing:
    by: ai-typing-pass
    added:
    - standard-model.four-supersymmetric-splits
    - standard-model.supersymmetric-row-two-loops
    - standard-model.hyp-s-slot-statistics
    note: 'Added the two-loop row and the four-splits segment, whose values clauses (3) and (2) take as
      input; did not add the table, since the proof recomputes the rows from the threshold criteria and
      the table itself cites this claim for its clause (e). Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.four-supersymmetric-splits
    - standard-model.supersymmetric-row-two-loops
    stated_role:
    - standard-model.hyp-s-slot-statistics
    note: "Proof is an exact or record-level run with no step naming (S); stated its role, the lepton doublet of the derived content, from Theorem hypercharge-global-form and Proposition weak-angle, which put the lepton doublet under (S)."
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: "Direct assumes of Hypothesis (S) removed and standard-model.spectrum-run added to uses (the statement is taken at that proposition's inputs; cited in the proof): the proof uses no slot statistics of its own, and (S) reaches it through spectrum-run, four-supersymmetric-splits and supersymmetric-row-two-loops, so it stays in holds_given and the statement keeps 'Under Hypothesis (S)'."
---

## formal
Under Hypothesis (S), at the inputs of Proposition \claimref{standard-model.spectrum-run}:
\begin{enumerate}
\item[(1)] the three rows that Proposition \claimref{standard-model.table-exact} finds admissible, the wino, the wino with the bino and the higgsinos, and the supersymmetric content without the gluino, have $M_{U} = 2.5$, $1.6$ and $1.5 \times 10^{14}$ GeV and lifetimes of about $2 \times 10^{29}$, $3 \times 10^{28}$ and $2 \times 10^{28}$ yr, short of the limit by five to six orders of magnitude: none meets the proton condition;
\item[(2)] the segment of Proposition \claimref{standard-model.four-supersymmetric-splits}(d) meets the condition from its near-degenerate end down to $(f, f') = (0.868, 0.759)$, where the light set sits at $6 \times 10^{3}$ GeV, the heavy set at $1.9 \times 10^{5}$ GeV and $M_{U} = 5.6 \times 10^{15}$ GeV, and fails it beyond, so that the end with the electroweak-inos at $7 \times 10^{8}$ GeV is excluded;
\item[(3)] the supersymmetric row at two loops (Proposition \claimref{standard-model.supersymmetric-row-two-loops}), with $M_{U} = 1.1 \times 10^{16}$ GeV and $\alpha_{U}^{-1} = 25.7$, has a lifetime of about $3 \times 10^{35}$ yr and meets the condition.
\end{enumerate}

## technical
Under Hypothesis (S), at the record inputs, the meeting scales and unified couplings of the candidate spectra are the exact rationals of the one- and two-threshold criteria converted to GeV, and the lifetime is the imported estimate $\tau_{p} \propto \bigl(\alpha_{U}^{-1}M_{U}^{2}\bigr)^{2}$ set against the Super-Kamiokande limit. The three rows admissible at one loop meet at $M_{U} = 1.5$ to $2.5 \times 10^{14}$ GeV with lifetimes of about $2 \times 10^{28}$ to $2 \times 10^{29}$ yr, five to six orders of magnitude short: none meets the proton condition.

On the supersymmetric two-threshold segment the condition holds from the near-degenerate end down to $(f, f') = (0.868, 0.759)$, where $M_{U} = 5.6 \times 10^{15}$ GeV, and fails beyond it. The supersymmetric row at two loops, with $M_{U} = 1.1 \times 10^{16}$ GeV and $\alpha_{U}^{-1} = 25.7$, has $\tau_{p} \approx 3 \times 10^{35}$ yr and meets it.

## lay
If the forces unify, the heavy particles of the unified theory let protons decay, and experiments show that protons live longer than about ten to the thirty-four years. This result applies that test to the candidate particle spectra. The three that work at the simplest level of approximation make protons decay far too quickly, while part of a supersymmetric family of spectra, and the supersymmetric case treated more precisely, survive. All of it assumes the paper's hypothesis about the composite's modes.

## one-liner
Under Hypothesis (S), none of the three spectra admissible at one loop meets the proton-decay limit, while the near-degenerate part of the two-threshold supersymmetric segment and the two-loop supersymmetric row do.
