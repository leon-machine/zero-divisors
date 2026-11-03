---
id: quantity.fermi-scale
kind: quantity
version: 1
title: The Fermi scale, the vacuum value of the Higgs field
status: derived
subject: standard-quantities
programme: standard
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
quantity:
  symbol: v
  value: '246.22'
  units: GeV
  dimension: mass
  source:
    citation: 'J. Erler and A. Freitas, Electroweak model and constraints on new physics, Section 10 of S. Navas
      et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024) 030001'
    key: PDG2024
    doi: 10.1103/PhysRevD.110.030001
    locator: 'Review 10, Section 10.1: v = 246.22 GeV; G_F/sqrt2 = 1/(2 v^2) = g^2/(8 M_W^2) after equation
      (10.6); equation (10.5b), M_W = g v/2; G_F = 1.1663788(6) x 10^-5 GeV^-2, equation (10.8)'
  date: '2024'
  note: 'Derived from the Fermi constant by the tree relation v = (sqrt2 G_F)^(-1/2): with G_F = 1.1663788(6)
    x 10^-5 GeV^-2 this is 246.2196 GeV, uncertainty about 6 x 10^-5 GeV from G_F, quoted by the Particle Data
    Group as 246.22 GeV. Checked on 2026-11-01 against the PDG 2024 review "Electroweak model and constraints
    on new physics" (rpp2024-rev-standard-model), Sections 10.1 and 10.2.1. The tree relations v = 2M_W/g =
    (sqrt2 G_F)^(-1/2) hold at tree level; the tree value from the stored M_W, sin^2 theta_W(M_Z) and
    alpha(M_Z), about 246.6 GeV, differs from it by radiative corrections. The store reads v^2 = 2N for the rung
    field.'
---

## formal
$v = (\sqrt{2}\,G_{F})^{-1/2} = 246.22$ GeV, the vacuum value of the Higgs field (the Fermi scale), from the Fermi constant $G_{F} = 1.1663788(6) \times 10^{-5}$ GeV$^{-2}$ by the tree relation $G_{F}/\sqrt{2} = 1/(2v^{2}) = g^{2}/(8M_{W}^{2})$, with $M_{W} = gv/2$ at tree level \cite{PDG2024}.

## technical
pending

## lay
The size of the Higgs field's background value, about 246 GeV, read off the strength of the weak interaction in muon decay; it sets the masses of the W and Z bosons and of the quarks and leptons.

## one-liner
$v = (\sqrt{2}\,G_{F})^{-1/2} = 246.22$ GeV.
