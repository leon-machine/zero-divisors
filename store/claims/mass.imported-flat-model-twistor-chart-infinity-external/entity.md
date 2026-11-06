---
id: mass.imported-flat-model-twistor-chart-infinity-external
kind: claim
version: 1
title: 'Imported: flat model, conformal spinor chart and infinity bivector (external)'
status: imported
region: mass
subject: conformal-spacetime
tags: [classical-theorem, conformal-spinors, tractors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
review: typed
imported_from:
- citation: T. N. Bailey, M. G. Eastwood, and A. R. Gover, Thomas's structure bundle for conformal, projective
    and related structures, Rocky Mountain J. Math. 24 (1994), 1191--1217.
  key: BEG1994
  locator: \S2
- citation: 'R. Penrose and W. Rindler, Spinors and Space-Time, Vol. 2: Spinor and Twistor Methods in
    Space-Time Geometry, Cambridge University Press (1986).'
  key: PenroseRindler1986
- citation: L. P. Hughston, Twistors and Particles, Lecture Notes in Physics 97, Springer (1979).
  key: Hughston1979
locators:
  paper: T11
  number: Fact 2.3
  label: ''
  line: 422
extraction:
  env: fact
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  - correspondence.incidence-relation-chart
  - correspondence.one-statement-three-languages
  - correspondence.spin-representation
  - correspondence.spinor-identification
  - interior.sign-fixed-internally
  - mass.de-sitter-scale-frozen-point
  outside_pilot_cites:
  - ButlerT6
  flags:
  - external ingredients of mass.imported-flat-model-twistor-chart-infinity
  typing:
    by: ai-typing-pass
    note: External-ingredients entry; imported, no edges.
  source_title: "Imported: the flat model, the twistor chart, and the infinity twistor (external ingredients)"
  source_formal: |-
    The results from outside the series on which \claimref{mass.imported-flat-model-twistor-chart-infinity} draws, as cited there: T. N. Bailey, M. G. Eastwood, and A. R. Gover, Thomas's structure bundle for conformal, projective and related structures, Rocky Mountain J. Math. 24 (1994), 1191--1217., \S2; R. Penrose and W. Rindler, Spinors and Space-Time, Vol. 2: Spinor and Twistor Methods in Space-Time Geometry, Cambridge University Press (1986).; L. P. Hughston, Twistors and Particles, Lecture Notes in Physics 97, Springer (1979)..
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Cosmetic only: title and plain levels follow the converted flat-model fact. The formal level is a bibliography and keeps the cited titles verbatim."
---

## formal
The results from outside the series on which \claimref{mass.imported-flat-model-twistor-chart-infinity} draws, as cited there: T. N. Bailey, M. G. Eastwood, and A. R. Gover, Thomas's structure bundle for conformal, projective and related structures, Rocky Mountain J. Math. 24 (1994), 1191--1217., \S2; R. Penrose and W. Rindler, Spinors and Space-Time, Vol. 2: Spinor and Twistor Methods in Space-Time Geometry, Cambridge University Press (1986).; L. P. Hughston, Twistors and Particles, Lecture Notes in Physics 97, Springer (1979)..

## technical
The external results on which the flat-model fact draws, as cited there. From Bailey, Eastwood and Gover: the tractor dictionary on the flat model, in which parallel sections are constant vectors $V$ with $\sigma$-slot $\ip{X(x)}{V}$.

From Penrose and Rindler and from Hughston: the classical material of twistor theory, namely the spinor bracket $\br{\pi^1\pi^2} = \varepsilon^{AB}\pi^1_A\pi^2_B$, the null momentum $p_{AA'} = \pi_A\bar\pi_{A'}$ of a conformal spinor, and the conformal generators as Hermitian quadratics $\bar Z_\alpha Z^\beta$ in the conformal spinor variables.

## lay
This entry records the outside literature that the flat-model fact relies on: the standard theory of tractor bundles in conformal geometry and the classical textbooks on two-component and conformal spinors. It adds no result of the series.

## one-liner
The external ingredients of the flat-model fact: the conformal tractor dictionary of Bailey, Eastwood and Gover, and classical spinor material from Penrose and Rindler and from Hughston.
