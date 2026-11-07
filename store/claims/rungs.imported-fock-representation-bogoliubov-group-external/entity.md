---
id: rungs.imported-fock-representation-bogoliubov-group-external
kind: claim
version: 2
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
- name: Claude Opus 5.5
  role: 'consistency pass, citation typography in the formal level'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 2
  source: maintainer pass 2026-11-07 (decisions)
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
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version kept at 2 (already raised in this run). Decision item E9 (routine; no retirement): equivalent_to standard-model.imported-fock-representation-clifford-algebra-bogoliubov@1 added. An exact duplicate of the standard-model Fact, which is kept as the home; a later dedupe pass may retire this one under POLICIES section 4.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. The citation list in the formal level carried doubled stops before the locators; removed; no change of content.'
  env: fact
  context_refs:
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov
  flags:
  - external ingredients of rungs.imported-fock-representation-bogoliubov-group
  typing:
    by: ai-typing-pass
    note: External-ingredients record; levels only.
equivalent_to:
- standard-model.imported-fock-representation-clifford-algebra-bogoliubov@1
---

## formal
The results from outside the series on which \claimref{rungs.imported-fock-representation-bogoliubov-group} draws, as cited there: W. Fulton and J. Harris, Representation Theory: A First Course, Graduate Texts in Mathematics 129, Springer (1991), Lecture~20; H. B. Lawson and M.-L. Michelsohn, Spin Geometry, Princeton University Press (1989), Ch.~I, \S\S 2, 5.

## technical
This entry records the sources from outside the series of the Fock-representation fact: Fulton and Harris for the spinor module as an exterior algebra $\Lambda^{\bullet}E$ and its half-spin decomposition, and Lawson and Michelsohn for $\mathrm{Spin}(2n)$ as the double cover of $SO(2n)$ and its spin representation.

## lay
Part of the Fock-representation fact comes from standard textbooks outside the series, on representation theory and on spin geometry. This entry records those sources so that the dependence is visible.

## one-liner
External ingredients of the Fock-representation fact: Fulton and Harris on the spinor module as an exterior algebra, and Lawson and Michelsohn on $\mathrm{Spin}(2n)$ and its spin representation.
