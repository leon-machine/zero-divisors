---
id: quantity.reduced-planck-constant-times-c
kind: quantity
version: 1
title: The conversion constant hbar c
status: defined
subject: standard-quantities
programme: standard
proposed_by:
  kind: ai
  session: roadmap-2026-10-23
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
quantity:
  symbol: \hbar c
  value: '197.3269804'
  units: MeV fm
  dimension: energy times length
  source:
    citation: CODATA 2022 recommended values of the fundamental physical constants (NIST)
    url: https://physics.nist.gov/cuu/Constants/
    locator: reduced Planck constant times c in MeV fm
  date: '2019'
  note: Fixed by the SI definitions but irrational (a factor 1/(2 pi)); written to ten figures as the
    store uses it (simulations.cluster-bound-two-dimensions).
---

## formal
$\hbar c = 197.3269804$ MeV fm, the conversion between energy and inverse length, to ten figures.

## technical
pending

## lay
The number that converts between energies and distances in particle physics.

## one-liner
$\hbar c = 197.3269804$ MeV fm.
