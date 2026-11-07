---
id: singularity.euclidean-section-period
kind: claim
version: 5
title: The Euclidean section, and its period
status: proved
region: singularity
subject: thermality
tags: [hawking-temperature, schwarzschild, recovers-known-physics]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
outside_ga:
  kind: complex-analysis
  why: 't_s = -i tau is the Wick rotation of the static Killing time coordinate, an analytic continuation of a scalar coordinate to a Riemannian section, not a unit acting on multivector values'
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - singularity.computed@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.18
- kind: check
  ref: check.py::check_wick_rotated_derived_metric
- kind: check
  ref: check.py::check_slope_is_half_f_prime
- kind: check
  ref: check.py::check_tip_expansion
- kind: check
  ref: check.py::check_regular_tip_iff_period_eight_pi_m
locators:
  paper: T05
  number: Prop 7.18
  label: prop:section
  line: 1852
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: t_s = -i tau is the Wick rotation of a coordinate; the formal-level "i.e." is a false positive. Declared complex-analysis.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Wick-rotated static gauge derived metric in GA, dF/drho = f''/2 as a rational-function identity, the tip expansion F = kappa rho + O(rho^3) by exact series reversion, and the torsion-free Omega of the (rho, tau) block matching the flat polar field exactly when kappa p = 2 pi. Version 3 -> 4. Check strengthened: exactly p = 8 pi M among the sample periods gives the smooth tip; samples moved to module level. Version 4 -> 5.'
  env: proposition
  context_refs:
  - singularity.plane-rate
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: Removed the mechanical transport-algorithm edge (the proof is metric geometry plus the surface-gravity
      value, kept); the paper says the Euclidean-regularity reading is Gibbons-Hawking, but no imported
      Gibbons-Hawking claim is in the store, so no standard route was added.
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$t_s = -i\tau$: Wick rotation (analytic continuation)'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Euclidean section is the Wick-rotated static gauge of the Schwarzschild field on the flat Euclidean background; rho = 0 named as the tip of the section (the Euclidean counterpart of the bifurcation sphere), and the regularity condition noted as local (DICTIONARY 14 item 5). Same period 8 pi M.'
---

## formal
Let $t_s = -i\tau$ in the static gauge of the Schwarzschild gravitational field on flat spacetime (Appendix \ref{app:metric}; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). The Wick-rotated field lives on the flat Euclidean background, and its derived metric is the Riemannian metric $f\,d\tau^{2} + f^{-1}dr^{2} + r^{2}d\Omega^{2}$ on $r > 2M$; let $\varrho(r) := \int_{2M}^{r} f^{-1/2}\,dr'$ be proper radial distance from the horizon locus. Then, with $F := \sqrt f$ regarded as a function of $\varrho$,
\[
f\,d\tau^{2} + f^{-1}dr^{2} \;=\; d\varrho^{2} + F(\varrho)^{2}\,d\tau^{2}, \qquad F(0) = 0, \qquad \frac{dF}{d\varrho}\Big|_{\varrho = 0} \;=\; \frac{f'(2M)}{2} \;=\; \kappa \;=\; \frac{1}{4M} ,
\]
so that near $\varrho = 0$ the $(\varrho, \tau)$ plane carries the metric $d\varrho^{2} + \kappa^{2}\varrho^{2}d\tau^{2} + O(\varrho^{4})\,d\tau^{2}$. If $\tau$ is periodic with period $p$, the section is a smooth Riemannian manifold at $\varrho = 0$ (the tip of the section, the two-sphere where the Euclidean Killing flow has its fixed points, the Euclidean counterpart of the bifurcation sphere) if and only if
\[
\kappa\,p \;=\; 2\pi, \qquad \text{i.e.} \qquad p \;=\; \frac{2\pi}{\kappa} \;=\; 8\pi M ;
\]
for any other period the origin of the $(\varrho, \tau)$ plane is a conical point of total angle $\kappa p$. The period of imaginary Killing time is therefore fixed by the gravitational field, at the horizon locus, and it is the conversion factor of Proposition \claimref{singularity.plane-rate} read in imaginary time. The regularity condition is local: it lives in a polar chart about the tip of the Wick-rotated flat background; the Lorentzian bifurcation surface itself lies beyond one flat chart and is not used.

## technical
Setting $t_s = -i\tau$ in the static gauge of the Schwarzschild field gives a field on the flat Euclidean background whose derived metric is the Riemannian $f\,d\tau^2 + f^{-1}dr^2 + r^2 d\Omega^2$ on $r > 2M$. With proper radial distance $\varrho(r) = \int_{2M}^{r} f^{-1/2}\,dr'$ and $F = \sqrt f$ regarded as a function of $\varrho$, the $(\varrho, \tau)$ part is $d\varrho^2 + F(\varrho)^2\,d\tau^2$, with $F(0) = 0$ and $dF/d\varrho$ at $\varrho = 0$ equal to $f'(2M)/2 = \kappa = 1/4M$; so near $\varrho = 0$ it is $d\varrho^2 + \kappa^2\varrho^2\,d\tau^2 + O(\varrho^4)\,d\tau^2$.

If $\tau$ has period $p$, the section is smooth at its tip $\varrho = 0$, the Euclidean counterpart of the bifurcation sphere, if and only if $\kappa p = 2\pi$, that is $p = 2\pi/\kappa = 8\pi M$; for any other period the origin of the $(\varrho, \tau)$ plane is a conical point of total angle $\kappa p$. The period of imaginary Killing time is therefore fixed by the field at the horizon locus, and it is the rapidity-to-time conversion factor read in imaginary time. The condition is local, in a polar chart about the tip.

## lay
Replacing time by an imaginary variable turns the gravitational field outside a black hole into a field on a flat four-dimensional space without time, in which the time direction closes into a circle. Near the horizon the geometry this field describes looks like a flat plane in polar coordinates, but only if the circle has exactly the right length, $8\pi$ times the mass in natural units; any other length leaves a cone point. So the period is fixed by the gravitational field rather than chosen.

## one-liner
The Euclidean section of the Schwarzschild field is smooth at its tip, the Euclidean counterpart of the bifurcation sphere, if and only if imaginary Killing time has period $p = 2\pi/\kappa = 8\pi M$; any other period leaves a conical point of total angle $\kappa p$.
