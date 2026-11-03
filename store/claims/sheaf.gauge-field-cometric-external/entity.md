---
id: sheaf.gauge-field-cometric-external
kind: claim
version: 1
title: The gauge field and its cometric (external ingredients)
status: imported
region: sheaf
subject: singularity
tags: [classical-theorem, schwarzschild]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
imported_from:
- citation: C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003).
  key: DoranLasenby2003
locators:
  paper: T04
  number: Fact 8.1
  label: ''
  line: 863
extraction:
  typing:
    by: ai-typing-pass
    note: 'imported bookkeeping entry for the textbook background; levels describe only what the citation supplies.'
  env: fact
  context_refs:
  - singularity.cones-fold
  - singularity.degeneration-exactly
  - singularity.solution-where-divergence-lies
  - singularity.unipotent-ray
  flags:
  - external ingredients of sheaf.gauge-field-cometric
---

## formal
The results from outside the series on which \claimref{sheaf.gauge-field-cometric} draws, as cited there: C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003).

## technical
This entry records the source from outside the series on which the Painlev\'e-Gullstrand gauge-field fact draws: Doran and Lasenby's textbook treatment of gauge theory gravity. In that formalism gravity is carried by a position-dependent linear gauge field $\hb$ acting on vectors of the flat spacetime algebra, with the metric recovered as $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$.

The entry supplies the gauge-theoretic background only; the specific statements about the Schwarzschild field are carried by results within the series.

## lay
This is a bookkeeping entry naming the textbook, from outside the series, that supplies the background for the black-hole gauge-field fact. The book develops a version of gravity built from geometric algebra, in which the gravitational field is a map acting on directions in flat spacetime.

## one-liner
The external ingredient of the Painlev\'e-Gullstrand gauge-field fact is the gauge theory gravity background of Doran and Lasenby's textbook.
