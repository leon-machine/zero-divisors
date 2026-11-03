---
id: quantity.boltzmann-constant
kind: quantity
version: 1
title: The Boltzmann constant in GeV per kelvin
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
  symbol: k_{B}
  value: '8.617333262e-14'
  units: GeV/K
  dimension: energy per temperature
  source:
    citation: BIPM, The International System of Units (SI Brochure), 9th edition (2019)
    url: https://www.bipm.org/en/publications/si-brochure
    locator: defining constants (k = 1.380649e-23 J/K, e = 1.602176634e-19 C)
  date: '2019'
  note: k/e is exact in the SI but its decimal does not terminate; the store writes it to ten figures
    (synthesis.finite-range-descent-deposit-cannot-seed-cmb).
---

## formal
$k_{B} = 8.617333262 \times 10^{-14}$ GeV/K, the Boltzmann constant in GeV per kelvin, from the exact SI values of $k$ and $e$, to ten figures.

## technical
pending

## lay
The constant that converts a temperature into an energy.

## one-liner
$k_{B} = 8.617333262 \times 10^{-14}$ GeV/K.
