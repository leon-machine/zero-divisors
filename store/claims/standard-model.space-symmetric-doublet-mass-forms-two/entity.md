---
id: standard-model.space-symmetric-doublet-mass-forms-two
kind: claim
version: 5
title: The space of symmetric doublet mass forms is two-dimensional
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
  - standard-model.ten-transported-ambient-space-doublets-are@2
  - families.doublet-direction-module-georgi-jarlskog-clebsch@6
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_two_dimensional_space
- kind: check
  ref: check.py::check_ratio_is_free
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Prop 9.32
  label: prop:twodim
  line: 1815
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: enumeration of the 512 odd monomials: the symmetric colour-singlet doublet forms span two dimensions (the 10 and T_GJ) and every ratio y_e/y_d is reached. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - families.doublet-direction-module-georgi-jarlskog-clebsch
    - standard-model.hyp-s-slot-statistics
    note: 'Added the families Proposition for the form of T_GJ and its ratio 3, one of the two spanning
      forms; the representation-theory route in the proof is not marked as standard by the paper, so no
      standard-route was added. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because
      its statement holds under Hypothesis (S). Levels pass: lay now keeps Hypothesis (S).'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - families.doublet-direction-module-georgi-jarlskog-clebsch
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), on the sixteen of one generation, the symmetric bilinear forms $Y_{T}(\psi, \varphi) = B(\psi, T\varphi)$ with $T$ an odd colour-singlet element of the Clifford algebra of the ten carrying hypercharge $-\tfrac12$ and $T_{3} = -\tfrac12$ span exactly a two-dimensional space, spanned by the form of the $10$ direction $w_{4}$ (Clebsch ratio $|y_{e}/y_{d}| = 1$) and the form of $T_{\mathrm{GJ}}$ (ratio $3$). Every form in the space couples only $(L, e^{c})$ and $(Q, d^{c})$, and the ratio $y_{e}/y_{d}$ takes every value as the two coefficients vary: the representation theory fixes the two directions and not the ratio.

## technical
Under Hypothesis (S), consider the symmetric forms $Y_{T}(\psi, \varphi) = B(\psi, T\varphi)$ on the sixteen of one generation, with $T$ an odd colour-singlet element of the Clifford algebra of the ten carrying hypercharge $-\tfrac12$ and $T_{3} = -\tfrac12$. They span exactly a two-dimensional space, with basis the $10$ form of $w_{4}$ (ratio $|y_{e}/y_{d}| = 1$) and the $126$ form of $T_{\mathrm{GJ}}$ (ratio $3$).

Every form in the space couples only $(L, e^{c})$ and $(Q, d^{c})$, and the ratio $y_{e}/y_{d}$ takes every value as the two coefficients vary: representation theory fixes the two directions but not the ratio.

## lay
Under the slot hypothesis (S), for one family of quarks and leptons, the paper counts every way a Higgs-like field of the right charges can give mass to electrons and down quarks together. There are exactly two independent ways, the ordinary one giving equal masses and the Georgi-Jarlskog one giving a factor of three. Mixing them can produce any ratio, so the symmetry alone does not pick the observed one.

## one-liner
Under Hypothesis (S), the symmetric doublet mass forms on one generation span a two-dimensional space, with basis the $10$ and $T_{\mathrm{GJ}}$ forms, leaving the ratio $y_{e}/y_{d}$ free.
