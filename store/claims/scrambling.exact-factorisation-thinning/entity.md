---
id: scrambling.exact-factorisation-thinning
kind: claim
version: 3
title: The exact factorisation of the thinning
status: proved
region: scrambling
subject: entropy
tags: [mode-counting, schwarzschild]
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
about:
- obj.scrambling.stretched-singularity
derivations:
- name: main
  uses:
  - scrambling.epoch-modular-period-two-unknowns-become@6
  - scrambling.slice-volume-exactly-per-unit-killing@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - num:4.8
- kind: check
  ref: check.py::check_slice_count_per_unit_time
- kind: check
  ref: check.py::check_slice_count_per_period
- kind: check
  ref: check.py::check_factorisation
locators:
  paper: T08
  number: Prop 4.8
  label: prop:factor
  line: 772
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: slice count 8 pi M = 4 pi r_h = A/r_h, N_slice = 64 pi^2 M^2 = 16 pi S_BH, and 16 pi = (beta/r_h)(A/S_BH) = 4 pi x 4 as exact monomials. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Both uses (slice volume and the epoch''s value of beta) are the factors the proof multiplies,
      and are kept. Levels pass: the lay level now keeps "per modular period" and "at leading order in
      $r_c/2M$" (review item 8).'
---

## formal
In Planck units, with $r_h = 2M$, $A = 4\pi r_h^2 = 16\pi M^2$, $\beta = 8\pi M$ and $\SBH = A/4$:
\begin{enumerate}
\item[(i)] the slice count per unit Killing time is $8\pi M = 4\pi r_h = A/r_h$, at leading order in $r_c/2M$;
\item[(ii)] the slice count per modular period is $N_{\mathrm{slice}} = 64\pi^2 M^2$ and $N_{\mathrm{slice}}/\SBH = 16\pi$, at the same order;
\item[(iii)] $16\pi = (\beta/r_h) \times (A/\SBH) = 4\pi \times 4$, and the first factor is universal for Schwarzschild, $\beta/r_h = 2\pi/(\kappa r_h) = 4\pi$ with $\kappa = 1/(2r_h)$.
\end{enumerate}

## technical
In Planck units, with $r_h = 2M$, $A = 16\pi M^2$, $\beta = 8\pi M$ and $\SBH = A/4$, the slice count per unit Killing time is $8\pi M = 4\pi r_h = A/r_h$, and per modular period it is $N_{\mathrm{slice}} = 64\pi^2M^2$, so $N_{\mathrm{slice}}/\SBH = 16\pi$, both at leading order in $r_c/2M$.

The factor splits exactly as $16\pi = (\beta/r_h)\times(A/\SBH) = 4\pi \times 4$, and the first factor, $\beta/r_h = 2\pi/(\kappa r_h) = 4\pi$ with $\kappa = 1/(2r_h)$, is universal for Schwarzschild.

## lay
Counting one mode per Planck-sized cell of the black hole's inner slice, per thermal period, overshoots the entropy by a factor of $16\pi$, at leading order in the ratio of the cutoff to the hole's size. That factor splits exactly into two pieces: $4\pi$, the ratio of the hole's thermal period to its radius, the same for every Schwarzschild black hole, and $4$, the ratio of horizon area to entropy.

## one-liner
The slice count per modular period exceeds $\SBH$ by $16\pi = (\beta/r_h)\times(A/\SBH) = 4\pi \times 4$, at leading order in $r_c/2M$.
