---
id: pred.neutrino-mass-sum-floor
kind: prediction
version: 3
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
- name: Claude Fable 5.2
  role: 'kill condition names the cosmological model in which the bound is read (w = -1, the series'' own); note on the opposite exposure of the two cosmological predictions'
  version: 3
  source: maintainer pass of 2026-11-10
review: typed
kill_condition:
  threshold: 'Below: a physical-prior cosmological bound, read in the cosmological model with w = -1
    (the series'' own), confirmed below the floor, or confirmed inverted
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
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 2 -> 3: the kill condition did not name the cosmological model in which a cosmological bound is derived; it now says the bound is read in the model with w = -1, the series'' own by its registered dark-energy prediction, and a note labelled argued records that the two cosmological predictions are exposed in opposite senses (the same data give a bound below the floor with w = -1 held and above it with the dark-energy parameters free, as the stored observation rows show). The prediction is unchanged.'
  env: table row
  source: T17 tab:stances
  typing:
    by: ai-typing-pass
    note: 'basis edges unchanged (rank-one seesaw, assuming (H)). Levels pass: the lay dropped Premise
      (H), on which the formal says the sum is a prediction; it now names it.'
derivations:
- name: basis
  uses:
  - neutrino.rank-one-seesaw-ordering-sum-double@9
  assumes:
  - neutrino.h-second-stage-hierarchical@1
lineage:
  derived_from:
  - neutrino.double-prediction-sum-predicted-floor
---

## formal
The neutrino mass sum lies at the oscillation floor, approximately $0.059$ eV, with normal ordering; the sum is a prediction under the hierarchy premise (H).

\emph{Note (the cosmological model of the bound).} The cosmological bound of the kill condition is read in the cosmological model with $w = -1$, the series' own (\claimref{pred.dark-energy-w-minus-one}): while that prediction stands by its registered rule, a bound obtained with $(w_{0}, w_{a})$ free does not count for or against the floor. The two predictions are exposed in opposite senses (argued): in the stored observations the same data give a bound below the floor with $w = -1$ held and bounds above it with $(w_{0}, w_{a})$ free, so if $w = -1$ falls by its rule the floor is relieved, not refuted, and while $w = -1$ stands the floor is the prediction under pressure.

## technical
From the rank-one seesaw the ordering is normal, with $m_{1} = m_{2} = 0$ at leading order. The second-stage breaking lifts $m_{2}$ to $\sqrt{\Delta m^{2}_{21}}$ and, under Premise (H), lifts $m_{1}$ by far less ($m_{1} \lesssim 0.1$ meV), so the sum sits at the kinematic floor of normal ordering, $\mnu = \sqrt{\Delta m^{2}_{21}} + \sqrt{\Delta m^{2}_{31}} \approx 0.059$ eV, within about $0.1$ meV of it. The prediction fails below if a physical-prior cosmological bound is confirmed under the floor or inverted ordering is confirmed, and above if the sum is determined meaningfully above the floor or $m_{1}$ is measured above a few meV. The cosmological bound is read in the model with $w = -1$, the series' own; bounds with the dark-energy parameters free do not count while that prediction stands, and the two predictions are exposed in opposite senses (argued).

## lay
If the second stage of the framework's family symmetry breaking is hierarchical (Premise (H)), the framework predicts that the three neutrino masses add up to the smallest total that oscillation experiments allow, about 0.059 eV, with the normal ordering. Cosmological surveys are now close to this value, so it is a near-term test. The surveys' limit depends on what is assumed about dark energy; the limit that counts here is the one obtained with unchanging dark energy, which the framework itself predicts.

## one-liner
Under Premise (H) the neutrino mass sum lies at the normal-ordering floor, $\mnu \approx 0.059$ eV; the cosmological bound that tests it is read in the model with $w = -1$.
