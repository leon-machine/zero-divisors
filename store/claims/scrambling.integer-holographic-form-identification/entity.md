---
id: scrambling.integer-holographic-form-identification
kind: claim
version: 2
title: The integer-holographic form, and the identification of the $16\pi$
status: proved
region: scrambling
subject: entropy
tags: [live-prediction, mode-counting, boundary-modes]
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
  - scrambling.epoch-modular-period-two-unknowns-become@6
  - scrambling.mode-count@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:cor:holographic
  - num:4.4
- kind: check
  ref: check.py::check_epoch_volume_is_beta_squared
- kind: check
  ref: check.py::check_density_iff_integer_count
- kind: check
  ref: check.py::check_naive_overshoot_is_area_coefficient
locators:
  paper: T08
  number: Cor 4.4
  label: cor:holographic
  line: 708
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: V = 64 pi^2 M^2 = beta^2, nu V = S_BH exactly at nu = 1/(16 pi), overshoot V/S_BH = 16 pi = A/M^2. Version 1 -> 2.'
  env: corollary
  unresolved_refs:
  - rem:nu
  typing:
    by: ai-typing-pass
    note: 'Both uses (the count formula and the epoch value) are the inputs of the arithmetic and are
      kept. Levels pass: lay and one-liner now keep the 1-nat convention, on which the exact 16 pi depends,
      and lay states the equivalence as an if-and-only-if.'
---

## formal
With the epoch fixed at $\beta$:
\begin{enumerate}
\item the counted three-volume of one epoch is $V = (8\pi M)\cdot\beta = 64\pi^2M^2$ in Planck units; restoring the length, $V = \beta^2\lP$: the coincidence with $\beta^2$ is a consequence of the framework's units, one visible power of $\lP$ marking the volume as geometric rather than purely modular;
\item the prediction $\nu = 1/16\pi$ holds if and only if the number of boundary modes registered per modular period is
\[
N_{\mathrm{epoch}} \;=\; \nu\,V \;=\; 4\pi M^2 \;=\; \SBH
\]
exactly as arithmetic: \emph{one boundary-mode fermion per four Planck cells of horizon area, per modular period}. The transcendental density becomes an integer-holographic statement, in the 1-nat convention and inheriting the per-mode $\ln 2$ normalisation of Remark \ref{rem:nu};
\item the naive one-mode-per-volume-cell reading ($\nu = 1$) overshoots it by exactly $16\pi$, which is precisely the horizon-area coefficient $A = 16\pi M^2$: the thinning the weighted completion must produce is the area coefficient itself. (Figure \ref{fig:conveyor} draws the assembled counting geometry.)
\end{enumerate}

## technical
With the epoch fixed at $\beta = 8\pi M$, the counted three-volume of one epoch is $V = (8\pi M)\beta = 64\pi^2M^2$ in Planck units, equal to $\beta^2\lP$ once the length is restored. The prediction $\nu = 1/16\pi$ holds exactly when $N_{\mathrm{epoch}} = \nu V = 4\pi M^2 = \SBH$: one boundary-mode fermion per four Planck cells of horizon area per modular period, in the 1-nat convention.

The naive reading of one mode per volume cell, $\nu = 1$, overshoots this by exactly $16\pi$, the coefficient in $A = 16\pi M^2$: the thinning the weighted completion must produce is the area coefficient itself.

## lay
Once the counting time is fixed at one thermal cycle, and in a bookkeeping convention that credits each mode with one unit of entropy, the predicted packing density of modes holds exactly when a whole-number rule does: one elementary mode per four Planck-sized patches of horizon, per thermal cycle. In that convention, counting one mode per tiny cell of interior volume instead gives too many by a factor of $16\pi$, the same number that appears in the area of the horizon.

## one-liner
With the epoch at $\beta$ and in the 1-nat convention, $\nu = 1/16\pi$ is equivalent to $N_{\mathrm{epoch}} = \SBH$, one boundary-mode fermion per four Planck cells of horizon per modular period, and the naive count overshoots by the area coefficient $16\pi$.
