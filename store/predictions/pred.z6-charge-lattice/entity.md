---
id: pred.z6-charge-lattice
kind: prediction
version: 1
title: No fractionally charged colour singlet
status: live
subject: standard-model
tags: [live-prediction, hypercharge-and-anomalies, gauge-fields]
region: programme
proposed_by:
  kind: extraction
  session: full-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
kill_condition:
  threshold: One confirmed fractionally charged colour-singlet particle
  data_source: PDG exotic-particle searches
  registered: 2026-08 (T17 stance table, row 3)
observations:
- date: 2025-08
  dataset: milliQan Run 3; CMS fractional charge
  result: No fractionally charged or millicharged particle seen. milliQan sets the strongest limits for
    charges up to 0.24e above 0.45 GeV; CMS excludes charges e/3 to 0.9e up to 640 GeV. Nothing newer
    as of November 2026.
  verdict: consistent
  source: milliQan, arXiv:2506.02251 (2025); CMS, PRL 134, 131802 (2025)
- date: 2026-08
  dataset: PDG exotic-particle searches
  result: 'PDG exotic-particle searches: consistent to date.'
  verdict: consistent
  source: T17 stance table, row 3
locators:
  paper: T12
  number: T17 stance 3
  label: tab:stances
extraction:
  typing:
    by: ai-typing-pass
    note: 'Kept the global-form basis; the source says the stance inherits the gauge-algebra theorem''s premise, carried through the global-form result, and gives no standard-physics route.'
  env: table row
  source: T17 tab:stances
derivations:
- name: basis
  uses:
  - standard-model.global-form-quotient-determined@3
---

## formal
The $\mathbb{Z}_{6}$ charge lattice: no fractionally charged colour singlet exists.

## technical
The global form of the gauge group derived in the series is $S(U(2) \times U(3))$, the full $\mathbb{Z}_{6}$ quotient. Its representations satisfy $2t + 3\delta + q \equiv 0 \pmod 6$, equivalently $t/3 + \delta/2 + Y \in \mathbb{Z}$, for colour triality $t$, weak parity $\delta$ and hypercharge $Y = q/6$, so a colour singlet cannot carry fractional electric charge.

One confirmed fractionally charged colour-singlet particle would refute the identification of the gauge group with the automorphism group of minimal massive compositeness.

## lay
The series derives not only the Standard Model's symmetries but the precise way they fit together, and that restricts the charges particles can have. In particular, a particle that feels no strong force must have a whole-number electric charge. Finding even one such particle with a fractional charge would refute this part of the framework; searches so far have found none.

## one-liner
The $\mathbb{Z}_{6}$ charge lattice of the derived gauge group forbids any fractionally charged colour singlet.
