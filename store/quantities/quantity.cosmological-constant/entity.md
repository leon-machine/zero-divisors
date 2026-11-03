---
id: quantity.cosmological-constant
kind: quantity
version: 1
title: The cosmological constant
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
  symbol: \Lambda
  value: '1.09e-52'
  uncertainty: '0.02e-52'
  units: m^-2
  dimension: inverse area
  source:
    citation: N. Aghanim et al. (Planck Collaboration), Planck 2018 results. VI. Cosmological parameters,
      Astron. Astrophys. 641 (2020) A6
    key: Planck2018
    doi: 10.1051/0004-6361/201833910
    locator: 'derived: Lambda = 3 Omega_Lambda H_0^2/c^2'
  date: '2018'
  note: 'Derived from quantity.hubble-constant, quantity.dark-energy-density-parameter and quantity.speed-of-light:
    3 (0.685)(67.4 km/s/Mpc)^2/c^2 = 1.0909e-52 m^-2, uncertainty about 0.02e-52. The store brackets Lambda
    in (1.0, 1.2)e-52 m^-2 citing PDG 2024, and writes Lambda ~ 1e-122 in Planck units (2.85e-122 at these
    values).'
---

## formal
$\Lambda = 3\,\Omega_{\Lambda}H_{0}^{2}/c^{2} = (1.09 \pm 0.02) \times 10^{-52}$ m$^{-2}$, the cosmological constant derived from the Planck 2018 values of $H_{0}$ and $\Omega_{\Lambda}$.

## technical
pending

## lay
The cosmological constant, the steady energy of empty space that drives the accelerating expansion.

## one-liner
$\Lambda \approx 1.09 \times 10^{-52}$ m$^{-2}$.
