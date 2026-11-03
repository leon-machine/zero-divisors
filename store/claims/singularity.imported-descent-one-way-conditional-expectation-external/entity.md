---
id: singularity.imported-descent-one-way-conditional-expectation-external
kind: claim
version: 1
title: 'Imported: the descent is a one-way conditional expectation (external ingredients)'
status: imported
region: singularity
subject: descent
tags: [classical-theorem, descent-map]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
imported_from:
- citation: M. Takesaki, Conditional expectations in von Neumann algebras, J. Funct. Anal. 9 (1972), 306--321.
  key: Takesaki1972
locators:
  paper: T05
  number: Fact 5.9
  label: ''
  line: 1605
extraction:
  env: fact
  context_refs:
  - singularity.descent-parity-average
  - transport.door-one-way
  - transport.pinching-kernel
  flags:
  - external ingredients of singularity.imported-descent-one-way-conditional-expectation
  typing:
    by: ai-typing-pass
    note: 'external import; no edges to review Levels pass: conditions already kept.'
---

## formal
The results from outside the series on which \claimref{singularity.imported-descent-one-way-conditional-expectation} draws, as cited there: M. Takesaki, Conditional expectations in von Neumann algebras, J. Funct. Anal. 9 (1972), 306--321.

## technical
The external ingredient is Takesaki's theorem on conditional expectations in von Neumann algebras: the trace-preserving conditional expectation onto a von Neumann subalgebra is unique. It supplies the uniqueness clause of the fact that the descent is a one-way conditional expectation.

## lay
A theorem of Takesaki from the theory of operator algebras says that, when an algebra carries a trace, there is only one averaging projection onto a given subalgebra that preserves the trace. The series uses it to show that the descent is the only projection of its kind.

## one-liner
External ingredient: Takesaki's theorem that the trace-preserving conditional expectation onto a von Neumann subalgebra is unique.
