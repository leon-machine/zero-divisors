---
id: quantity.reduced-planck-constant
kind: quantity
version: 1
title: The reduced Planck constant in GeV s
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
  symbol: \hbar
  value: '6.582119569e-25'
  units: GeV s
  dimension: action
  source:
    citation: CODATA 2022 recommended values of the fundamental physical constants (NIST)
    url: https://physics.nist.gov/cuu/Constants/
    locator: reduced Planck constant in eV s
  date: '2019'
  note: 'Fixed by the SI definitions of h and e, but hbar = h/(2 pi) is irrational, so no decimal is exact:
    the store writes it to ten figures (also as 6.582119569e-16 eV s). Not marked exact for that reason.'
---

## formal
$\hbar = 6.582119569 \times 10^{-25}$ GeV s, the reduced Planck constant $h/2\pi$ in GeV s to ten figures; $h$ and $e$ are exact in the SI.

## technical
pending

## lay
The quantum of action, which sets the scale of quantum effects.

## one-liner
$\hbar = 6.582119569 \times 10^{-25}$ GeV s.
