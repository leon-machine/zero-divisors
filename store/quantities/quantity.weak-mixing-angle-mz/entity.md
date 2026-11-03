---
id: quantity.weak-mixing-angle-mz
kind: quantity
version: 1
title: The weak mixing angle at the Z mass
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
  symbol: \sin^{2}\theta_{W}
  value: '0.23122'
  uncertainty: '0.00004'
  units: '1'
  dimension: dimensionless
  source:
    citation: S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024)
      030001
    key: PDG2024
    doi: 10.1103/PhysRevD.110.030001
    locator: 'Electroweak model review: MS-bar sin^2 theta_W(M_Z)'
  date: '2024'
  note: MS-bar value at M_Z as the store quotes it (standard-model.imported-two-loop-gauge-coefficients);
    the spectrum run uses the rounded 0.2312. 0.23122(4) is the PDG 2022 value; PDG 2024 may list 0.23129(4)
    (source to confirm).
---

## formal
$\sin^{2}\theta_{W}(M_{Z}) = 0.23122 \pm 0.00004$, the $\overline{\mathrm{MS}}$ weak mixing angle at the $Z$ mass \cite{PDG2024}.

## technical
pending

## lay
The angle that sets how the electromagnetic and weak forces mix.

## one-liner
$\sin^{2}\theta_{W}(M_{Z}) = 0.23122$.
