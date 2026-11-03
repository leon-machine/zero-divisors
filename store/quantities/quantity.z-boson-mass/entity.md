---
id: quantity.z-boson-mass
kind: quantity
version: 2
title: Mass of the Z boson
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
  symbol: M_{Z}
  value: '91.1880'
  uncertainty: '0.0020'
  units: GeV
  dimension: mass
  source:
    citation: S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024)
      030001
    key: PDG2024
    doi: 10.1103/PhysRevD.110.030001
    locator: 'Summary Tables, gauge and Higgs bosons: Z mass'
  date: '2024'
  note: 'Version 2 (maintainer pass of 2026-10-31) stores the PDG 2024 value 91.1880 +- 0.0020 GeV, checked on 2026-10-31 against the PDG 2024
    summary table of gauge and Higgs bosons (rpp2024-sum-gauge-higgs-bosons); version 1 stored 91.1876 +- 0.0021
    GeV, the LEP value carried by PDG through 2022, which some running and record computations of the store
    still use as a literal. Every store use is consistent with either at its displayed precision.'
---

## formal
$M_{Z} = 91.1880 \pm 0.0020$ GeV, the mass of the $Z$ boson, the Particle Data Group 2024 average \cite{PDG2024}.

## technical
pending

## lay
The mass of the Z boson, one of the carriers of the weak force, about 97 times the mass of a proton.

## one-liner
$M_{Z} = 91.1880$ GeV.
