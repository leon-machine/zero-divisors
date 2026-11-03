---
id: quantity.heaviest-neutrino-mass
kind: quantity
version: 1
title: The heaviest neutrino mass (normal ordering, lightest massless)
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
  symbol: m_{3}
  value: '0.050'
  uncertainty: '0.0006'
  units: eV
  dimension: mass
  source:
    citation: S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024)
      030001
    key: PDG2024
    doi: 10.1103/PhysRevD.110.030001
    locator: 'Neutrino mixing review: Delta m^2_32 (normal ordering)'
  date: '2024'
  note: 'Derived, not measured: m_3 = sqrt(Delta m^2_31) with m_1 = 0 in the normal ordering. The store
    uses 0.050 eV with the bracket (49.4, 50.5) meV, and 0.0502 eV in standard-model.what-angle-asks-neutrino-sector;
    the uncertainty here is half that bracket. The PDG Delta m^2 value behind the bracket is not quoted
    in the store (source to confirm).'
---

## formal
$m_{3} = 0.050$ eV, the heaviest neutrino mass $\sqrt{\Delta m^{2}_{31}}$ in the normal ordering with the lightest neutrino massless, bracketed in the store as $(49.4, 50.5)$ meV.

## technical
pending

## lay
The mass of the heaviest neutrino if the lightest one weighs nothing, about a ten-millionth of the electron's mass.

## one-liner
$m_{3} \approx 0.050$ eV.
