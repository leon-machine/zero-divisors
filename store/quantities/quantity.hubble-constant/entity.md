---
id: quantity.hubble-constant
kind: quantity
version: 1
title: The Hubble constant
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
  symbol: H_{0}
  value: '67.4'
  uncertainty: '0.5'
  units: km/s/Mpc
  dimension: inverse time
  source:
    citation: N. Aghanim et al. (Planck Collaboration), Planck 2018 results. VI. Cosmological parameters,
      Astron. Astrophys. 641 (2020) A6
    key: Planck2018
    doi: 10.1051/0004-6361/201833910
    locator: abstract (base LambdaCDM, TT,TE,EE+lowE+lensing); Table 2 gives 67.36 +- 0.54
  date: '2018'
  note: 'The checks use the abstract''s 67.4 +- 0.5 (standard-model.imported-frozen-point-dictionary,
    synthesis.finite-range-descent-deposit-cannot-seed-cmb); dark-matter.thickness-not-gravitational-quantity
    uses the Table 2 value 67.36 +- 0.54. Both agree at their displayed precision. Planck 2018 is not
    the only record: distance-ladder values near 73 disagree (the Hubble tension).'
---

## formal
$H_{0} = 67.4 \pm 0.5$ km s$^{-1}$ Mpc$^{-1}$, the Hubble constant of the Planck 2018 base $\Lambda$CDM fit \cite{Planck2018}.

## technical
pending

## lay
How fast the universe is expanding today: about 67 kilometres per second faster for every megaparsec of distance.

## one-liner
$H_{0} = 67.4 \pm 0.5$ km s$^{-1}$ Mpc$^{-1}$ (Planck 2018).
