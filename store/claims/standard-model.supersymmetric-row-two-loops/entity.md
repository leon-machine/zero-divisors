---
id: standard-model.supersymmetric-row-two-loops
kind: claim
version: 6
title: The supersymmetric row at two loops
status: proved
region: standard-model
subject: standard-model
tags:
- running-and-unification
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
  - standard-model.imported-two-loop-gauge-coefficients@1
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
- name: standard-route
  uses:
  - standard-model.imported-two-loop-gauge-coefficients@1
  proof: proof-standard-route.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_two_loop_matrices_from_the_formulas
- kind: check
  ref: check.py::check_integrator_against_exact_one_loop
- kind: check
  ref: check.py::check_central_meeting_point
- kind: check
  ref: check.py::check_alpha_s_range
- kind: check
  ref: check.py::check_threshold_shifts
locators:
  paper: T12
  number: Prop 8.19
  label: prop:twoloop
  line: 1476
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: two-loop matrices from the formulas, and an exact-arithmetic RK4 run bracketing M_I = 2.3 TeV, M_U = 1.1e16 GeV, alpha_U^-1 = 25.7 and the stated shifts, with a one-loop control. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.table-exact
    added:
    - standard-model.imported-two-loop-gauge-coefficients
    - standard-model.hyp-s-slot-statistics
    note: 'Removed the one-loop table, which the proof uses only as a control on the integrator; added
      a standard-route through the two-loop coefficients since the paper says the few-TeV degenerate threshold
      is a known result reproduced here. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - standard-model.hyp-s-slot-statistics
    note: Proof is an exact or record-level run with no step naming (S); stated its role, the lepton doublet
      of the derived content, from Theorem hypercharge-global-form and Proposition weak-angle, which put
      the lepton doublet under (S).
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
about:
- obj.standard-model.one-threshold-spectrum-admissible
---

## formal
Under Hypothesis (S), take the derived content with one Higgs doublet below a single threshold $M_{I}$ and the full supersymmetric content above it, run at two loops with the top Yukawa by the coefficients of Fact \claimref{standard-model.imported-two-loop-gauge-coefficients} from the record's central values. Then the three couplings meet exactly at one scale for
\[
M_{I} \;=\; 2.3 \text{ TeV}, \qquad M_{U} = 1.1 \times 10^{16}\ \text{GeV}, \qquad \alpha_{U}^{-1} = 25.7,
\]
and $M_{I}$ moves between $1.7$ and $3.0$ TeV across $\alpha_{s} = 0.1180 \pm 0.0009$, by $0.3$ TeV under the top Yukawa switched off, by $0.06$ TeV under $y_{t}(M_{Z}) = 0.99$ against $0.95$, by $0.15$ TeV under $\sin\beta = 0.9$, and by $0.27$ TeV under $\sin^{2}\theta_{W} + 0.0001$. The row that one loop could not decide is admissible at two loops, with its threshold in the low TeV range.

## technical
Under Hypothesis (S), take the derived content with one Higgs doublet below a single threshold $M_{I}$ and the full supersymmetric content above it, and integrate the two-loop gauge equations with the top Yukawa, using the imported coefficient matrices, from the record's central values. The three couplings then meet exactly at one scale for $M_{I} = 2.3$ TeV, with $M_{U} = 1.1 \times 10^{16}$ GeV and $\alpha_{U}^{-1} = 25.7$.

The threshold moves between $1.7$ and $3.0$ TeV across $\alpha_{s} = 0.1180 \pm 0.0009$, and by at most about $0.3$ TeV under the stated changes to the top Yukawa, $\sin\beta$ and $\sin^{2}\theta_{W}$. The row one loop could not decide is admissible at two loops, with its threshold in the low TeV range; this is a record-level numerical result.

## lay
At the simplest level of approximation, supersymmetric partner particles all at one mass came very close to making the three forces meet, but the calculation could not settle it. Repeating it one level more precisely shows that they do meet if the partners weigh about 2.3 TeV, with unification near ten to the sixteen GeV. This reproduces a result already known in the literature, and here it rests on the paper's hypothesis about the composite's modes.

## one-liner
Under Hypothesis (S), at two loops the full supersymmetric content above a single threshold makes the three couplings meet for $M_{I} \approx 2.3$ TeV, with $M_{U} = 1.1 \times 10^{16}$ GeV and $\alpha_{U}^{-1} = 25.7$.
