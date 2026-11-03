---
id: quantity.solar-mass
kind: quantity
version: 1
title: The mass of the Sun
status: measured
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
  symbol: M_{\odot}
  value: 1.116e57
  uncertainty: 0.001e57
  units: GeV
  dimension: mass
  source:
    citation: S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024)
      030001
    key: PDG2024
    doi: 10.1103/PhysRevD.110.030001
    locator: 'Astrophysical constants table: solar mass'
  date: '2024'
  note: The store writes 1.116e57 GeV (dark-matter.parallel-boundary-mode-spaces-one-wall). From M_sun
    = 1.98841(4)e30 kg the energy equivalent is 1.11542e57 GeV, so the stored value is 0.05 % high (rounded
    up); the uncertainty here covers that rounding. Source table from memory (source to confirm).
---

## formal
$M_{\odot} = 1.116 \times 10^{57}$ GeV, the solar mass in energy units as the store uses it (from $M_{\odot} = 1.98841 \times 10^{30}$ kg).

## technical
pending

## lay
The mass of the Sun, written as an energy.

## one-liner
$M_{\odot} = 1.116 \times 10^{57}$ GeV.
