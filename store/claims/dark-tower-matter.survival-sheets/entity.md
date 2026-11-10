---
id: dark-tower-matter.survival-sheets
kind: claim
version: 5
title: Survival of sheet relics against annihilation
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [matter-asymmetry]
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
review: typed
derivations:
- name: main
  uses:
  - dark-tower-matter.imported-unit-ball-rule@4
  - dark-tower-matter.three-dimensional-phases@4
  - simulations.cluster-bound-two-dimensions@4
  assumes:
  - dark-matter.r2-one-quantum-per-unit-ball@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:K3
  - id:K4
- kind: check
  ref: check.py::check_logarithmic_depletion_law
- kind: check
  ref: check.py::check_survival_numbers
- kind: check
  ref: check.py::check_phase_t_threshold_and_collisionless
locators:
  paper: T14c
  number: Prop 9.2
  label: prop:sheetsurvival
  line: 817
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: logarithmic depletion law as an RF identity and its reduction from the sheet rate equation; exact interval redo of K3 (P bound 1.2e-16 to 2.2e-16, survival 1e-14 to 2.5e-14) and K4 thresholds. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  env: proposition
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    removed:
    - simulations.c-odd-towers-collisionless
    added:
    - dark-matter.r2-one-quantum-per-unit-ball
    - dark-tower-matter.imported-unit-ball-rule
    - dark-tower-matter.three-dimensional-phases
    - simulations.cluster-bound-two-dimensions
    note: 'E107 fix: the decimal proposition has no proof environment; its stated inputs (R2''s density,
      the two phases, the simulations companion''s phase-shift bound of 1.7e-7) were made its edges with
      a cites-only proof file. Removed the companion''s Premise C (odd towers collisionless) from assumes:
      the proposition derives that the relic meets C''s threshold, it does not assume it. Check K3 prints
      about 2e-14 surviving at P = 1 against the stated 10^-14. Levels pass: levels written from scratch,
      keeping every condition and level qualifier of the formal statement.'
---

## formal
Decimal. On a sheet the comoving number per unit area and the expansion rate both fall as $a^{-2}$ in radiation domination, so two-dimensional s-wave annihilation with $\sigma_{1}v = 2P/m$ ($P$ the absorption probability per encounter) depletes a symmetric population logarithmically, $1/N_{f} = 1/N_{0} + (2P/m)\ln(a_{f}/a_{i})/(a^{2}H)$. At R2's density a symmetric sheet relic keeps $99$ percent of its number only for $P \lesssim 2 \times 10^{-16}$; at $P = 1$ about $10^{-14}$ survives (K3). In phase (T) this needs $e^{2}/m > 7 \times 10^{7}$, which also makes the relic collisionless in clusters (threshold $5.9 \times 10^{6}$, from the in-sheet phase-shift bound $1.7 \times 10^{-7}$ of T14b's cluster computation \cite[Comp.~3.3, Prem.~2.12]{ButlerT14b}) (K4). Phase (C) fails R2 by itself.

## technical
Decimal, assuming R2's density. On a sheet the comoving number per unit area and the expansion rate both fall as $a^{-2}$ in radiation domination, so two-dimensional s-wave annihilation with $\sigma_1 v = 2P/m$, $P$ the absorption probability per encounter, depletes a symmetric population only logarithmically, $1/N_f = 1/N_0 + (2P/m)\ln(a_f/a_i)/(a^2H)$. At R2's density a symmetric sheet relic keeps $99$ percent of its number only for $P \lesssim 2 \times 10^{-16}$, and at $P = 1$ about $10^{-14}$ survives.

In phase (T) this needs $e^2/m > 7 \times 10^7$, which also makes the relic collisionless in clusters (threshold $5.9 \times 10^6$, from the in-sheet phase-shift bound $1.7 \times 10^{-7}$ of the cluster computation). Phase (C) fails R2 by itself.

## lay
Matter and antimatter on the dark sheets annihilate when they meet, and in two dimensions this erodes them slowly but steadily. In these decimal estimates, assuming the unit-ball density premise R2, a symmetric population survives only if annihilation per encounter is almost impossible, which in the topologically massive phase needs a coupling far stronger than the mass; that also lets the matter pass through itself when clusters collide. The confining phase cannot keep the required density.

## one-liner
Assuming R2's density, in decimal estimates a symmetric sheet relic survives only for $P \lesssim 2 \times 10^{-16}$, which needs $e^2/m > 7 \times 10^7$ in phase (T), while phase (C) fails R2.
