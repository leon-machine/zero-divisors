---
id: pred.neutrino-mass-sum-floor
kind: prediction
version: 2
title: Neutrino mass sum at the oscillation floor
status: live
subject: neutrinos
tags:
- live-prediction
- seesaw-and-majorana
region: programme
proposed_by:
  kind: extraction
  session: full-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
review: typed
kill_condition:
  threshold: 'Below: a physical-prior cosmological bound confirmed below the floor, or confirmed inverted
    ordering. Above: a sum determined meaningfully above the floor (near 0.075 eV), or m1 measured above
    a few meV'
  data_source: Cosmological combinations
  registered: 2026-08 (T17 stance table, row 4)
observations:
- date: 2026-09
  dataset: Cosmological combinations
  result: Planck with Planck and ACT lensing and DESI BAO gives a sum below 0.069 eV (95%), above the
    0.059 eV floor. The DESI DR1 full-shape reanalysis gives below 0.049 eV in LCDM (below the floor;
    the authors attribute its sharpness to the CMB-BAO tension) and below 0.077 eV in w0waCDM, and disfavours
    inverted ordering at about 3.5 sigma in LCDM. No physical-prior bound is confirmed below the floor.
    KATRIN, below 0.45 eV, does not reach it.
  verdict: tension
  source: Figueroa, Sobotka and Erickcek, arXiv:2609.15970 (2026); Ivanov et al., arXiv:2601.16165 (2026,
    PRD)
- date: 2026-08
  dataset: Cosmological combinations
  result: 'Cosmological combinations: DESI DR2 with the CMB gives < 0.064 eV in LCDM; the tightest current
    bound, < 0.052 eV at 95% with a prior extending to zero, is read by its authors as a prior artefact,
    and gives < 0.092 eV with the physical floor imposed.'
  verdict: tension
  source: T17 stance table, row 4
locators:
  paper: T15
  number: T17 stance 4
  label: tab:stances
extraction:
  env: table row
  source: T17 tab:stances
  typing:
    by: ai-typing-pass
    note: 'basis edges unchanged (rank-one seesaw, assuming (H)). Levels pass: the lay dropped Premise
      (H), on which the formal says the sum is a prediction; it now names it.'
derivations:
- name: basis
  uses:
  - neutrino.rank-one-seesaw-ordering-sum-double@8
  assumes:
  - neutrino.h-second-stage-hierarchical@1
lineage:
  derived_from:
  - neutrino.double-prediction-sum-predicted-floor
---

## formal
The neutrino mass sum lies at the oscillation floor, approximately $0.059$ eV, with normal ordering; the sum is a prediction under the hierarchy premise (H).

## technical
From the rank-one seesaw the ordering is normal, with $m_{1} = m_{2} = 0$ at leading order. The second-stage breaking lifts $m_{2}$ to $\sqrt{\Delta m^{2}_{21}}$ and, under Premise (H), lifts $m_{1}$ by far less ($m_{1} \lesssim 0.1$ meV), so the sum sits at the kinematic floor of normal ordering, $\mnu = \sqrt{\Delta m^{2}_{21}} + \sqrt{\Delta m^{2}_{31}} \approx 0.059$ eV, within about $0.1$ meV of it. The prediction fails below if a physical-prior cosmological bound is confirmed under the floor or inverted ordering is confirmed, and above if the sum is determined meaningfully above the floor or $m_{1}$ is measured above a few meV.

## lay
If the second stage of the framework's family symmetry breaking is hierarchical (Premise (H)), the framework predicts that the three neutrino masses add up to the smallest total that oscillation experiments allow, about 0.059 eV, with the normal ordering. Cosmological surveys are now close to this value, so it is a near-term test.

## one-liner
Under Premise (H) the neutrino mass sum lies at the normal-ordering floor, $\mnu \approx 0.059$ eV.
