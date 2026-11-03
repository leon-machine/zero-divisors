---
id: quantity.reduced-planck-mass
kind: quantity
version: 1
title: The reduced Planck mass
status: derived
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
  symbol: \bar{M}_{P}
  value: 2.435e18
  uncertainty: 0.001e18
  units: GeV
  dimension: mass
  source:
    citation: S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024)
      030001
    key: PDG2024
    doi: 10.1103/PhysRevD.110.030001
    locator: 'Physical constants table: reduced Planck mass'
  date: '2024'
  note: 'Derived: M_P/sqrt(8 pi) = 2.43532e18 GeV from quantity.planck-mass; the store uses the rounded
    2.435e18 GeV and writes it as M_P in the graviton-rate Fact, the same letter as the non-reduced mass.
    The uncertainty here is the rounding of the stored value.'
---

## formal
$\bar{M}_{P} = M_{P}/\sqrt{8\pi} = 2.435 \times 10^{18}$ GeV, the reduced Planck mass, derived from the Planck mass and rounded as the store uses it.

## technical
pending

## lay
The Planck mass divided by the square root of eight pi, the form in which it enters cosmology formulas.

## one-liner
$\bar{M}_{P} = 2.435 \times 10^{18}$ GeV.
