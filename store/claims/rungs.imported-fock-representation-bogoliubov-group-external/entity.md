---
id: rungs.imported-fock-representation-bogoliubov-group-external
kind: claim
version: 1
title: 'Imported: the Fock representation and its Bogoliubov group (external ingredients)'
status: imported
region: rungs
subject: one-relation
tags: [spinor-modules, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
imported_from:
- citation: 'W. Fulton and J. Harris, Representation Theory: A First Course, Graduate Texts in Mathematics
    129, Springer (1991).'
  key: FultonHarris1991
  locator: Lecture~20
- citation: H. B. Lawson and M.-L. Michelsohn, Spin Geometry, Princeton University Press (1989).
  key: LawsonMichelsohn1989
  locator: Ch.~I, \S\S 2, 5
locators:
  paper: T12-rungs
  number: Fact 1.6
  label: ''
  line: 221
extraction:
  env: fact
  context_refs:
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov
  flags:
  - external ingredients of rungs.imported-fock-representation-bogoliubov-group
  typing:
    by: ai-typing-pass
    note: External-ingredients record; levels only.
---

## formal
The results from outside the series on which \claimref{rungs.imported-fock-representation-bogoliubov-group} draws, as cited there: W. Fulton and J. Harris, Representation Theory: A First Course, Graduate Texts in Mathematics 129, Springer (1991)., Lecture~20; H. B. Lawson and M.-L. Michelsohn, Spin Geometry, Princeton University Press (1989)., Ch.~I, \S\S 2, 5.

## technical
This entry records the sources from outside the series of the Fock-representation fact: Fulton and Harris for the spinor module as an exterior algebra $\Lambda^{\bullet}E$ and its half-spin decomposition, and Lawson and Michelsohn for $\mathrm{Spin}(2n)$ as the double cover of $SO(2n)$ and its spin representation.

## lay
Part of the Fock-representation fact comes from standard textbooks outside the series, on representation theory and on spin geometry. This entry records those sources so that the dependence is visible.

## one-liner
External ingredients of the Fock-representation fact: Fulton and Harris on the spinor module as an exterior algebra, and Lawson and Michelsohn on $\mathrm{Spin}(2n)$ and its spin representation.
