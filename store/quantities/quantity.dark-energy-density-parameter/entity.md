---
id: quantity.dark-energy-density-parameter
kind: quantity
version: 1
title: The dark-energy density parameter
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
  symbol: \Omega_{\Lambda}
  value: '0.685'
  uncertainty: '0.007'
  units: '1'
  dimension: dimensionless
  source:
    citation: N. Aghanim et al. (Planck Collaboration), Planck 2018 results. VI. Cosmological parameters,
      Astron. Astrophys. 641 (2020) A6
    key: Planck2018
    doi: 10.1051/0004-6361/201833910
    locator: abstract (Omega_m = 0.315 +- 0.007, flat); Table 2 gives Omega_Lambda = 0.6847 +- 0.0073
  date: '2018'
  note: The checks use 0.685 (1 - Omega_m of the abstract, flatness); dark-matter.thickness-not-gravitational-quantity
    uses the Table 2 value 0.6847. They agree at displayed precision.
---

## formal
$\Omega_{\Lambda} = 0.685 \pm 0.007$, the dark-energy fraction of the critical density in the Planck 2018 base $\Lambda$CDM fit \cite{Planck2018}.

## technical
pending

## lay
The share of the universe's energy in dark energy, about 69 percent.

## one-liner
$\Omega_{\Lambda} = 0.685$ (Planck 2018).
