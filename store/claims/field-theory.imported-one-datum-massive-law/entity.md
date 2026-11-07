---
id: field-theory.imported-one-datum-massive-law
kind: claim
version: 2
title: 'Imported: one datum for the massive law'
status: proved
region: field-theory
subject: quantum-fields
tags: [mass-generation, pseudoscalar-and-centre]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
review: typed
locators:
  paper: FT
  number: Fact 2.3
  label: fact:onedatum
  line: 82
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in Cl(1,3), the pseudoscalar is even with square -1 and anticommutes with C = I u, the commutant of C in Cl+ is 4-dimensional, J^2 = -1 there is a two-sheeted hyperboloid, and J -> C J is a unit timelike vector orthogonal to u with joint commutant span{1, J}. Version 1 -> 2.'
  env: fact
  flags:
  - citation taken from inline provenance (no \cite)
  source_imported_from:
  - citation: T16, Lemma lem:onedatum
  typing:
    by: ai-typing-pass
    added:
    - one-relation.one-datum-not-two-imaginary-unit
    note: 'The fact restates the foundations paper''s one-datum lemma, which is in the store, so it was
      made a restatement (status proved, uses that lemma, as the store treats series facts), not an import.
      Levels pass: levels written from scratch, keeping every condition and level qualifier of the formal
      statement.'
derivations:
- name: main
  uses:
  - one-relation.one-datum-not-two-imaginary-unit@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pseudoscalar_excluded_and_commutant_four_dimensional
- kind: check
  ref: check.py::check_complex_structures_form_hyperboloid
- kind: check
  ref: check.py::check_imaginary_unit_and_rest_frame_one_choice
---

## formal
The massive Dirac law in the spacetime algebra needs one geometric datum beyond the field, and the pseudoscalar cannot serve as it. \emph{Provenance:} T16, Lemma lem:onedatum.

## technical
The massive Dirac law in the spacetime algebra needs one geometric datum beyond the field, and the pseudoscalar cannot serve as it: the pseudoscalar, though even and of square $-1$, anticommutes with the mass datum and is excluded from the complex structures the massive law needs.

## lay
Writing the equation of a massive electron in geometric algebra needs one extra geometric ingredient beyond the field itself, in effect a rest-frame direction. The spacetime volume element, although it squares to minus one, cannot play that role.

## one-liner
The massive Dirac law in the spacetime algebra needs one geometric datum beyond the field, and the pseudoscalar cannot serve as it.
