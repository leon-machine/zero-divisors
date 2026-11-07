---
id: scrambling.epoch-modular-period-two-unknowns-become
kind: claim
version: 5
title: The epoch is the modular period; two unknowns become one
status: proved
region: scrambling
subject: entropy
tags: [live-prediction, entropy-premises, modular-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
derivations:
- name: main
  uses:
  - scrambling.area-law-test@4
  - scrambling.clock-inventory-boundary-modes@6
  - singularity.euclidean-rotor-where-it-lies@5
  assumes:
  - scrambling.intrinsic-clock-ic-flagged-premise@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:thm:epoch
- kind: check
  ref: check.py::check_epoch_is_the_modular_period
- kind: check
  ref: check.py::check_density_prediction_both_directions
locators:
  paper: T08
  number: Thm 4.3
  label: thm:epoch
  line: 692
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: beta = 2 pi/kappa = 8 pi M with unit-rapidity block from GA; nu = 1/(16 pi) iff N = S_BH over beta, capacity form 1/(16 pi ln 2). Version 4 -> 5.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES L6
    open_problem: op.small-findings
    note: 'The technical level now says how (IC) stands to T05''s counted-epoch postulate (C3): the causal epoch 2M(ln(1/eps) - 8/3 + 2 ln 2) equals 8 pi M only at eps = exp(-(4 pi + 8/3 - 2 ln 2)), about 9.7 x 10^-7, so the two premises fix the epoch differently and results resting on (C3) are not thereby results under (IC). A lineage.supersedes link between the two postulates is left to the maintainer.'
  env: theorem
  context_refs:
  - scrambling.mode-count
  - tower.witt-index-quantum-capacity
  unresolved_refs:
  - rem:nu
  typing:
    by: ai-typing-pass
    added:
    - scrambling.intrinsic-clock-ic-flagged-premise
    note: 'Added the intrinsic-clock premise, which the theorem assumes outright (it would go in assumes
      if it were a postulate), and repinned the Euclidean rotor to version 2; the mode-count and capacity
      context refs are coherence and pointer citations, not premises. Hypothesis pass: moved scrambling.intrinsic-clock-ic-flagged-premise
      from uses to assumes, now that it is a postulate. Levels pass: conditions already kept.'
---

## formal
Assume (IC). Then the counted epoch is the modular period:
\[
\Delta t \;=\; \beta \;=\; \frac{2\pi}{\kappa} \;=\; 8\pi M \qquad \text{(Schwarzschild)}.
\]
The conversion is exact and holds in both directions: with the epoch fixed, the area-law condition $\nu\,\Delta t = M/2$ of Proposition \claimref{scrambling.area-law-test} becomes a prediction for the density factor,
\[
\nu \;=\; \frac{M/2}{8\pi M} \;=\; \frac{1}{16\pi}
\]
in the 1-nat convention ($\nu = 1/(16\pi\ln 2)$ in T5's capacity convention, Remark \ref{rem:nu}; Section \ref{subsec:calibration} shows the capacity convention is the one with physical content and restates the prediction there), and a calibration principle for the exceptional set (Fact \claimref{tower.witt-index-quantum-capacity}; Section \ref{subsec:calibration} says what it must produce) must return that number \emph{or refute the premise (IC)}. Two unknowns have become one equation and one falsifiable identification; the count's remaining condition is a single dimensionless number with a named derivation route and a named failure mode. The scale $\Delta t \sim M$ is thereby derived rather than imported, cohering with Theorem \claimref{scrambling.mode-count}'s own observation that the accrual rate is set by the horizon's temperature: the singularity keeps the horizon's scale.

## technical
Under the intrinsic-clock premise (IC), the counted epoch is the modular period, $\Delta t = \beta = 2\pi/\kappa = 8\pi M$ for Schwarzschild, because every clock of the boundary modes has that period. Substituting into the area-law condition $\nu\,\Delta t = M/2$ gives $\nu = 1/16\pi$ in the 1-nat convention, and $\nu = 1/(16\pi\ln 2)$ in the capacity convention.

The two unknowns $(\Delta t, \nu)$ thus become one number: a calibration principle for the exceptional set must return this value or refute (IC). The epoch of order $M$ is then derived rather than imported, consistent with the accrual rate being set by the Hawking temperature. This is a different fixing from the singularity paper's counted-epoch postulate (C3), whose causal epoch $\Delta t(\varepsilon) = 2M(\ln(1/\varepsilon) - \tfrac83 + 2\ln 2)$ equals $8\pi M$ only at $\varepsilon = e^{-(4\pi + 8/3 - 2\ln 2)} \approx 9.7 \times 10^{-7}$; results that rest on (C3) are not thereby results under (IC).

## lay
The entropy count needed two unknown inputs: how long to count for, and how densely modes are packed. Assuming the counting time is set by the modes' own clock, it must be one thermal cycle of the black hole. That leaves a single number, the packing density, which the theory must reproduce or else the assumption fails.

## one-liner
Under the intrinsic-clock premise the counted epoch is the modular period $\beta = 8\pi M$, turning the area law into the prediction $\nu = 1/16\pi$ in the 1-nat convention.
