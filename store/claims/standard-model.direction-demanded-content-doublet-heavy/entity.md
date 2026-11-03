---
id: standard-model.direction-demanded-content-doublet-heavy
kind: claim
version: 7
title: 'The direction: the demanded content is doublet-heavy'
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
  - standard-model.one-threshold-exact-criterion@3
  - standard-model.spectrum-run@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_record_ratio_below_r0
- kind: check
  ref: check.py::check_direction_criterion
- kind: check
  ref: check.py::check_gluino_worsens
locators:
  paper: T12
  number: Cor 8.10
  label: cor:direction
  line: 1367
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: R = 1357472/973455 < r_0 = 218/115, the sign criterion for f and the admissibility criterion on a grid of shifts, and the gluino. Version 4 -> 5. The formal level restated: scope: ''Delta_2 = 0 and Delta_3 > 0 has f < 0'' needs Delta_1 >= 0 (the criterion gives f > 0 when Delta_1 < -R Delta_3, e.g. (-2, 0, 1/6)) (fix round 2026-10-23). Version 5 -> 6. The technical level restated: scope: add Delta_1 >= 0 to the gluino sentence, as in formal (fix round 2026-10-23). check_gluino_worsens: scope control (-2, 0, 1/6) has f > 0; docstring (3) notes it (fix round 2026-10-23). Decimal display corrected to the truncation 1.39448 before an ellipsis (exact 1.3944887...). Check strengthened: both outcomes of each grid criterion asserted to occur (was existence of f > 0 and f <= 1 only); b_12 = 109/15 and b_23 = 23/6 pinned by hand; b moved to module level. Version 6 -> 7.'
  env: corollary
  typing:
    by: ai-typing-pass
    note: 'Kept both edges, the criterion and the record inputs the proof uses. Hypothesis pass: assumes
      standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis (S). Levels
      pass: lay now keeps Hypothesis (S), the record inputs, the one-threshold setting, the weighted comparison
      and the admissibility condition; one-liner adds one-threshold.'
    added:
    - standard-model.hyp-s-slot-statistics
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - standard-model.hyp-s-slot-statistics
    note: Proof is an exact or record-level run with no step naming (S); stated its role, the lepton doublet
      of the derived content, from Theorem hypercharge-global-form and Proposition weak-angle, which put
      the lepton doublet under (S).
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: "Direct assumes of Hypothesis (S) removed: the proof uses no slot statistics of its own; (S) enters only through the coefficients and inputs of standard-model.spectrum-run, which this result already uses and which now assumes (S), so (S) stays in holds_given and the statement keeps 'Under Hypothesis (S)'. The proof's closing sentence now routes (S) through that proposition."
about:
- obj.standard-model.one-threshold-spectrum-admissible
---

## formal
Under Hypothesis (S), at the record, $R < r_{0}$: with the inputs of Proposition \claimref{standard-model.spectrum-run}, $R = 1357472/973455 = 1.39448\ldots$ and $r_{0} = 218/115 = 1.89565\ldots$. Hence a spectrum has $f > 0$ if and only if
\[
(1 + R)\,\Dl_{2} \;>\; \Dl_{1} + R\,\Dl_{3},
\]
and is admissible only if in addition $r_{\Dl} \le R$: the content must lower the ratio all the way to the record's when placed at $M_{Z}$. In words, the $SU(2)$ shift must exceed the $R$-weighted mean of the abelian and colour shifts, with $R \approx 1.39$ weighting colour: content that is heavy in $SU(2)$ doublets and triplets relative to colour and hypercharge. Content with $\Dl_{2} = 0$, $\Dl_{3} > 0$ and $\Dl_{1} \ge 0$, a gluino for instance, has $f < 0$ and worsens the miss.

## technical
Under (S), with the record inputs, the measured ratio $R = 1357472/973455 \approx 1.3945$ lies below the Standard Model's coefficient ratio $r_{0} = 218/115 \approx 1.8957$. So a one-threshold spectrum with shift $\Dl$ has threshold fraction $f > 0$ exactly when $(1 + R)\,\Dl_{2} > \Dl_{1} + R\,\Dl_{3}$, and is admissible only if in addition $r_{\Dl} \le R$.

In words, the $SU(2)$ shift must exceed the $R$-weighted mean of the abelian and colour shifts: the added content must be heavy in $SU(2)$ doublets and triplets relative to colour and hypercharge. Content with $\Dl_{2} = 0$, $\Dl_{3} > 0$ and $\Dl_{1} \ge 0$, such as a gluino, has $f < 0$ and worsens the miss.

## lay
Without new particles, the three force strengths of the Standard Model fail to meet at a single energy. Assuming Hypothesis (S) and taking the measured inputs, this result says which way a single threshold of new particles must tilt the running to fix that: they must add more to the weak force than a weighted average of what they add to the strong and hypercharge forces, and even then the content is acceptable only if it closes the whole gap. Particles that feel only the strong force, such as a gluino, make the miss worse.

## one-liner
Under (S), at the record $R < r_{0}$, so one-threshold content moves the couplings towards meeting only if $(1 + R)\,\Dl_{2} > \Dl_{1} + R\,\Dl_{3}$: the demanded content is doublet-heavy.
