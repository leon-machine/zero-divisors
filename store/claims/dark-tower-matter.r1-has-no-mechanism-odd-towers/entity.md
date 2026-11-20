---
id: dark-tower-matter.r1-has-no-mechanism-odd-towers
kind: claim
version: 4
title: Neither E nor the particle model has a mechanism in the odd towers
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [counting-rules, mass-generation, no-go]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'restated to the deposited text of T14c version 1.0 (10.5281/zenodo.24403592)'
  version: 4
  source: maintainer pass of 2026-11-20
review: typed
derivations:
- name: main
  uses:
  - dark-matter.mirror-share-one-how-fragile@10
  - dark-tower-matter.gauge-algebras@5
  - dark-tower-matter.three-dimensional-content@4
  - dark-tower-matter.anomalies@4
  - dark-tower-matter.survival-sheets@6
  - dark-tower-matter.five-dimensional-towers@6
  - dark-tower-matter.imported-unit-ball-rule@5
  - dark-tower-matter.population@3
  assumes:
  - dark-matter.e-equal-mass-per-unit-ball@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:K1
  - id:K4
- kind: check
  ref: check.py::check_share_without_mechanism
- kind: check
  ref: check.py::check_viable_phase_bound
- kind: check
  ref: check.py::check_coupling_dimension
locators:
  paper: T14c
  number: Obs 9.4
  label: prop:R1
  line: 799
extraction:
  maintainer_pass:
    by: maintainer-2026-11-20
    date: '2026-11-20'
    note: 'Title restated: T14c deposited as version 1.0 on 20 November 2026 (10.5281/zenodo.24403592), after an independent review: the result reaches premise E as well as the particle model, so the title names both; renumbered Observation 9.4. Version 3 -> 4. The formal level restated: as the title: nothing in the content fixes the masses or densities E equates; the bound on m/e^2 given as the range 1.1 to 1.5e-8; the correction to T14 Section 8 (its odd-tower quanta read as confined composites) stated. The technical level restated: as the title: nothing in the content fixes the masses or densities E equates; the bound on m/e^2 given as the range 1.1 to 1.5e-8; the correction to T14 Section 8 (its odd-tower quanta read as confined composites) stated. The lay level restated: as the title: nothing in the content fixes the masses or densities E equates; the bound on m/e^2 given as the range 1.1 to 1.5e-8; the correction to T14 Section 8 (its odd-tower quanta read as confined composites) stated. The one-liner level restated: as the title: nothing in the content fixes the masses or densities E equates; the bound on m/e^2 given as the range 1.1 to 1.5e-8; the correction to T14 Section 8 (its odd-tower quanta read as confined composites) stated.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.mirror-share-one-how-fragile repinned 6 -> 7 after reviewing its C1 restatement ((i) now rests on the common-ceiling-coupling premise, with an assumes edge, where it said P2-protected; the values are unchanged); the use here holds as cited.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: share of the odd towers (8 pi + 16)/(11 pi + 16) bracketed at 81 percent with the individual shares; m/e^2 bound 1.4e-8; coupling dimension 4 - d. Version 1 -> 2. The formal level restated: rounding: the computed bound is m/e^2 <= sqrt(2) x 10^-8 = 1.414 x 10^-8, so the strict ''< 1.4 x 10^-8'' was tighter than what follows; now ''\lesssim 1.4 x 10^-8'' (coverage judge C03). Version 2 -> 3. The technical level restated: rounding: same fix as the formal level, ''< 1.4 x 10^-8'' to ''\lesssim 1.4 x 10^-8'' (coverage judge C03). check_viable_phase_bound: docstring states the rounding (\lesssim), new assert that the reciprocal exceeds the survival-sheets 7e7.'
  env: proposition
  context_refs:
  - dark-matter.mirror-share-one-how-fragile
  - dark-tower-matter.five-dimensional-towers
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.mirror-share-one-how-fragile
    - dark-tower-matter.anomalies
    - dark-tower-matter.five-dimensional-towers
    - dark-tower-matter.gauge-algebras
    - dark-tower-matter.imported-unit-ball-rule
    - dark-tower-matter.survival-sheets
    - dark-tower-matter.three-dimensional-content
    note: 'E107 fix: the assembly-level proposition has no proof environment and cites its inputs inline;
      those were made its edges with a cites-only proof file. The 81 percent is the two three- and two
      five-dimensional shares (check K1); m/e^2 < 1.4e-8 is the inverse of the survival bound (check K4).
      R1 is the subject of the claim, not a premise, so it was not assumed. Levels pass: levels written
      from scratch, keeping every condition and level qualifier of the formal statement.'
---

## formal
In this tower and the mirror a quantum's mass is a confinement scale, $m = c\Lambda$ \cite[Prop.~4.7]{ButlerT14}. In the three-dimensional towers the gauge algebra is abelian and the coupling dimensionful, so there is no dimensional transmutation and the cells' masses are bare parameters; the viable phase needs $m/e^{2}$ below $1.1$ to $1.5 \times 10^{-8}$, which nothing in the content protects (no chirality; parity broken by the forced Chern-Simons level). In the five-dimensional towers nothing confines (Computation \claimref{dark-tower-matter.five-dimensional-towers}(ii)) and the quanta are elementary with bare masses. The odd towers carry no asymmetry, so nothing fixes their number either (Observation \claimref{dark-tower-matter.population}). So nothing in the content fixes the masses or the densities that E equates across towers, for about $81$ percent of the dark matter; still less does it supply the particle model's equal masses. T14 already concedes that nothing sets an odd tower's quanta's mass to ours \cite[Rem.~7.8, Sec.~8]{ButlerT14}. What this note adds is the reason, and one correction: T14's Section 8 reads the odd towers' quanta as composites of sectors whose confinement scales the series does not derive, whereas here they are elementary in five dimensions and unconfined in the viable three-dimensional phase. Assembly level.

## technical
At assembly level. In this tower and the mirror a quantum's mass is a confinement scale, $m = c\Lambda$. In the three-dimensional towers the gauge algebra is abelian and the coupling dimensionful, so there is no dimensional transmutation and the cells' masses are bare parameters; the viable phase needs $m/e^{2}$ below $1.1$ to $1.5 \times 10^{-8}$, which nothing in the content protects (no chirality, and parity broken by the forced Chern-Simons level). In the five-dimensional towers nothing confines and the quanta are elementary with bare masses. The odd towers carry no asymmetry, so nothing fixes their number either.

So nothing in the content fixes the masses or densities that premise E equates across towers, for about $81$ percent of the dark matter, and still less the particle model's equal masses. This also corrects the dark-matter paper's reading of the odd towers' quanta as confined composites: they are elementary in five dimensions and unconfined in the viable three-dimensional phase.

## lay
The dark-matter paper's rule assumes every populated tower holds the same mass per unit ball, and its older particle picture assumes every dark particle has the same mass. In our tower and the mirror a particle's mass comes from a strong force, but this assembly-level argument shows that in the odd-dimensional towers, which hold about four fifths of the dark matter, masses are free parameters and nothing fixes how many particles there are. There, both assumptions are choices rather than consequences.

## one-liner
At assembly level nothing in the odd towers' content fixes the masses or densities that premise E equates, for about $81$ percent of the dark matter, still less the particle model's equal masses; their quanta are elementary, not confined composites.
