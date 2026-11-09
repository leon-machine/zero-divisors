---
id: standard-model.grade-three-georgi-jarlskog-direction
kind: claim
version: 5
title: A grade-three Georgi-Jarlskog direction
status: proved
region: standard-model
subject: generations
tags: [flavour-and-mixing, representation-theory]
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
  - standard-model.imported-spinor-bilinears@1
  - families.doublet-direction-module-georgi-jarlskog-clebsch@6
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_one_sided_weightings_grade_three
- kind: check
  ref: check.py::check_forms_antisymmetric_ratio_three
- kind: check
  ref: check.py::check_antisymmetric_family_matrix_off_diagonal
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Prop 11.6
  label: prop:gradethree
  line: 2081
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: w4 (B-L) and v4 (B-L) pure grade three; antisymmetric forms on the stated pairs with ratio 3; antisymmetric family matrix gives a symmetric form zero on the family diagonal. Version 4 -> 5.'
  env: proposition
  context_refs:
  - families.doublet-direction-module-georgi-jarlskog-clebsch
  - standard-model.imported-spinor-bilinears
  typing:
    by: ai-typing-pass
    added:
    - standard-model.imported-spinor-bilinears
    - families.doublet-direction-module-georgi-jarlskog-clebsch
    - standard-model.hyp-s-slot-statistics
    note: 'Added the spinor-bilinear Fact and the families Proposition, which the statement names as the
      basis for placing the forms in the 120; the rest is the script computation. Hypothesis pass: assumes
      standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis (S). Levels
      pass: the lay now names Hypothesis (S).'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - families.doublet-direction-module-georgi-jarlskog-clebsch
    - standard-model.imported-spinor-bilinears
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), $w_{4}(B - L)$ and $v_{4}(B - L)$ are pure grade three, so their forms lie in the $120$ component of $16 \otimes 16$ (Fact \claimref{standard-model.imported-spinor-bilinears}, with the equivariance of Fact \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}). Their mass forms on the sixteen are antisymmetric and couple exactly $(L, e^{c})$ and $(Q, d^{c})$, respectively $(L, \nu^{c})$ and $(Q, u^{c})$, with lepton-to-quark modulus ratio $3$. With an antisymmetric family matrix the combined form is symmetric and vanishes on the family diagonal: the direction contributes only to entries between different families.

## technical
Under Hypothesis (S), the one-sided weightings $w_{4}(B - L)$ and $v_{4}(B - L)$ are pure grade three in the Clifford algebra of the ten, so their forms lie in the $120$ component of $16 \otimes 16$. Their mass forms on the sixteen are antisymmetric, couple exactly $(L, e^{c})$ and $(Q, d^{c})$, respectively $(L, \nu^{c})$ and $(Q, u^{c})$, and have lepton-to-quark modulus ratio $3$, the Georgi-Jarlskog ratio.

Combined with an antisymmetric family matrix the total form is symmetric and vanishes on the family diagonal, so this direction contributes only to entries between different families.

## lay
The factor of three that unified theories need between some lepton and quark masses can also come, assuming the slots behave like the pairs (Hypothesis (S)), from a second kind of ingredient, built here from the same charge that tells quarks from leptons. This ingredient cannot give mass within a single family; it only links different families. That makes it a candidate for supplying the factor through mixing between the second and third families.

## one-liner
Under Hypothesis (S), $w_{4}(B - L)$ and $v_{4}(B - L)$ give antisymmetric $120$ mass forms with lepton-to-quark ratio $3$ that act only between different families.
