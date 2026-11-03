---
id: pred.boundary-mode-density
kind: prediction
version: 2
title: One boundary mode per Bekenstein-Mukhanov area quantum
status: live
subject: entropy
tags:
- live-prediction
- boundary-modes
- mode-counting
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
  source: authorship disclosure of T08, deposited version
review: typed
kill_condition:
  threshold: A derivation of the calibration residue from the boundary modes returning any other value, which refutes
    the intrinsic-clock premise (IC)
  data_source: Internal
  registered: 2026-08 (T17 stance table, row 6)
observations:
- date: 2026-10
  dataset: GW250114 area-law tests
  result: No experiment tests a discrete horizon-area spectrum. GW250114 confirms the classical area increase
    at high credibility, which does not bear on quantisation, and area-law tests turn out to be model
    dependent (horizonless mergers can pass them).
  verdict: pending
  source: LVK, PRL (2025), arXiv:2509.08054; Vangstein and Moore, arXiv:2610.36162 (2026)
- date: 2026-08
  dataset: Internal
  result: 'Internal: the geometry is closed at Schwarzschild, and the calibration residue must be produced from
    the boundary modes themselves.'
  verdict: pending
  source: T17 stance table, row 6
locators:
  paper: T08
  number: T17 stance 6
  label: tab:stances
extraction:
  env: table row
  source: T17 tab:stances
  typing:
    by: ai-typing-pass
    note: 'The single basis edge to the integer-holographic corollary is the prediction''s real premise and is kept;
      the intrinsic-clock premise enters through that corollary''s epoch theorem. Levels pass: the lay said the
      hole''s interior records the information, but the modes are boundary (horizon) modes, so it now says so, and
      it names the intrinsic-clock premise the epoch identification rests on.'
  source_formal: 'The internal prediction: $\nu = 1/16\pi$ in the 1-nat convention, equivalently one boundary-mode
    fermion per four Planck cells of horizon area per modular period ($N_{\mathrm{epoch}} = S_{\mathrm{BH}}$).'
  source_title: One boundary-mode fermion per four Planck cells
  convention_note: 'Stated in the capacity convention (ln 2 nats per fermionic mode), the one T08 Prop ''The residue
    in each convention'' (iii) shows has physical content and in which T08 declares the prediction''s form; the
    1-nat convention of T08 Thm ''epoch'' is given as the conversion. The kill condition is unchanged: the residue
    is 1/(4 ln 2) in the capacity convention, 1/4 in the 1-nat convention, the same statement.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 10
    note: Restated in the physical (capacity) convention, nu = 1/(16 pi ln 2), one mode per 4 ln 2 Planck areas,
      with the 1-nat form nu = 1/16 pi as the conversion; title and lay changed to match; basis gains the residue
      proposition. The kill condition's substance is unchanged.
derivations:
- name: basis
  uses:
  - scrambling.integer-holographic-form-identification@2
  - scrambling.residue-each-convention@4
---

## formal
The internal prediction, in the capacity convention (a fermionic mode carries at most $\ln 2$ nats): $\nu = 1/(16\pi\ln 2)$, equivalently one boundary-mode fermion per $4\ln 2$ Planck cells of horizon area, one per Bekenstein-Mukhanov area quantum, per modular period ($N_{\mathrm{epoch}}\ln 2 = S_{\mathrm{BH}}$, calibration residue $\kappa_c = 1/(4\ln 2)$, \claimref{scrambling.residue-each-convention}). In the 1-nat convention the same statement reads $\nu = 1/16\pi$, one fermion per four Planck cells ($N_{\mathrm{epoch}} = S_{\mathrm{BH}}$, $\kappa_c = \tfrac14$).

## technical
With the counted epoch fixed at the modular period $\beta = 8\pi M$, the area law requires the boundary-mode capacity registered per modular period to equal the Bekenstein-Hawking entropy: $N_{\mathrm{epoch}}\ln 2 = \SBH = A/4$, so $N_{\mathrm{epoch}} = A/(4\ln 2)$, one fermion per $4\ln 2 \approx 2.77$ Planck cells of horizon area (one per Bekenstein-Mukhanov area quantum), and the mode density per Planck cell is $\nu = 1/(16\pi\ln 2)$. This is the capacity convention, the one that compares an entropy with an entropy (\claimref{scrambling.residue-each-convention}(iii)). In the 1-nat convention, which credits each mode with one nat, the same statement reads $\nu = 1/16\pi$ and $N_{\mathrm{epoch}} = \SBH$, one fermion per four Planck cells.

The prediction is internal: a derivation of the calibration residue from the boundary modes that returned any other value would refute the intrinsic-clock premise on which the epoch identification rests.

## lay
The framework predicts how densely a black hole's horizon modes record information: one elementary fermionic mode for about every three Planck-sized patches of horizon area (exactly $4\ln 2 \approx 2.77$ of them, the area quantum Bekenstein and Mukhanov proposed), per cycle of the hole's natural clock. Each such mode can hold one bit. Given the premise that this clock sets the counting epoch, this is the counting that reproduces the Bekenstein-Hawking entropy. The test is internal to the theory: if its own calculation of this density gave a different number, a key assumption about the clock would be refuted.

## one-liner
The boundary modes register one fermion per Bekenstein-Mukhanov area quantum, $4\ln 2$ Planck cells of horizon area, per modular period: $\nu = 1/(16\pi\ln 2)$ ($1/16\pi$ in the 1-nat convention).
