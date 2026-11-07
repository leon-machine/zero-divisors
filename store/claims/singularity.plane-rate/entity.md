---
id: singularity.plane-rate
kind: claim
version: 4
title: The plane and the rate
status: proved
region: singularity
subject: thermality
tags: [hawking-temperature, forcing-and-uniqueness, schwarzschild]
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
derivations:
- name: main
  uses:
  - singularity.computed@5
  - singularity.curvature-gauge-field-exact-shape-decoupling@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:6.2
- kind: check
  ref: check.py::check_pair_selected_invariantly
- kind: check
  ref: check.py::check_surface_gravity_from_the_connection
- kind: check
  ref: check.py::check_two_pi_rapidity_is_eight_pi_m
locators:
  paper: T05
  number: Prop 6.2
  label: prop:plane
  line: 1642
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the doubled eigenplane of S computed as a kernel, R(sigma_r) = +2M/r^3 sigma_r, (K.D)K = K/(4M) at the horizon from the GTG-sign Omega with the Killing bivector in the radial plane, and 2 pi of rapidity = 8 pi M of Killing time. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - singularity.computed
    note: 'Added the surface-gravity proposition: the proof takes kappa = 1/4M from the appendix computation,
      which is that proposition, though it is cited by appendix rather than by claim reference; v2 review:
      removed the mechanical transport-algorithm edge, since the proof uses only the shape theorem and
      the surface-gravity computation.'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - singularity.computed
---

## formal
The plane in which the completed pair lies is not chosen: the doubled eigenvalue of Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling} singles out the pair $\{\sigma_r, I\sigma_r\}$ invariantly at every radius, and its boost member $\sigma_r$, the member with square $+1$ up to the orientation sign, is at the horizon the boost plane of the Killing flow, with surface gravity
\[
\kappa = \frac{1}{4M} .
\]
The geometric normalisation this fixes: an interval of $2\pi$ in rapidity corresponds to $2\pi/\kappa = 8\pi M$ of Schwarzschild time. This single conversion factor is where the numerical value of the temperature enters the chain.

## technical
The doubled curvature eigenvalue singles out the pair of planes $\{\sigma_r, I\sigma_r\}$ invariantly at every radius, and its two members are separated invariantly by their squares, $\sigma_r^2 = +1$ and $(I\sigma_r)^2 = -1$ (up to the orientation sign). So the plane of the completed pair is not chosen. At the horizon the boost member $\sigma_r$ is the boost plane of the Killing flow, whose surface gravity, computed as the redshifted proper acceleration of static observers, is $\kappa = \tfrac12 f'(r_h) = 1/4M$.

This fixes the geometric normalisation: an interval of $2\pi$ in rapidity corresponds to $2\pi/\kappa = 8\pi M$ of Schwarzschild time, and this single conversion factor is where the numerical value of the temperature enters the chain.

## lay
The curvature of a non-rotating black hole picks out, at every distance from the centre, a particular pair of planes without any arbitrary choice. At the horizon one of these is the plane in which the horizon's own time symmetry acts as a boost, and the rate of that boost is the surface gravity, one over four times the mass in natural units. That rate is the single number converting the geometry's natural angle into ordinary time, and it is where the numerical value of the black hole's temperature comes from.

## one-liner
The curvature selects the boost plane of the completed pair invariantly, and at the horizon its rate is the surface gravity $\kappa = 1/4M$, so $2\pi$ of rapidity corresponds to $8\pi M$ of Schwarzschild time.
