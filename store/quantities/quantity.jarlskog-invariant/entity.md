---
id: quantity.jarlskog-invariant
kind: quantity
version: 1
title: The Jarlskog invariant of quark mixing
status: measured
subject: standard-quantities
programme: standard
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
quantity:
  symbol: J
  value: '0.0000312'
  uncertainty: '0.0000013'
  units: '1'
  dimension: dimensionless
  source:
    citation: S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024)
      030001
    key: PDG2024
    doi: 10.1103/PhysRevD.110.030001
    locator: 'Review 12, CKM quark-mixing matrix (A. Ceccucci, Z. Ligeti and Y. Sakai), Sec. 12.4, global fit'
  date: '2024'
  note: 'Global-fit value J = (3.12 +0.13 -0.12) x 10^-5; the larger side of the asymmetric interval is recorded as the uncertainty. Definition Im[V_ij V_kl V_il* V_kj*] = J sum_{m,n} eps_ikm eps_jln, as in the review. Checked against the PDG 2024 CKM review on 2026-10-26.'
---

## formal
$J = (3.12^{+0.13}_{-0.12}) \times 10^{-5}$, the rephasing-invariant measure of CP violation in quark mixing, $\mathrm{Im}[V_{ij}V_{kl}V_{il}^{*}V_{kj}^{*}] = J\sum_{m,n}\epsilon_{ikm}\epsilon_{jln}$, from the global fit \cite{PDG2024}.

## technical
pending

## lay
A single number measuring how much the quark mixing matrix violates the symmetry between matter and antimatter.

## one-liner
$J = 3.12 \times 10^{-5}$.
