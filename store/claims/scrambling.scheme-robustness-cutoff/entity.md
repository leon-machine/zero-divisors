---
id: scrambling.scheme-robustness-cutoff
kind: claim
version: 3
title: Scheme robustness of the cutoff
status: proved
region: scrambling
subject: singularity
tags: [schwarzschild]
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
  - interior.kasner-form-interior@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:lem:scheme
- kind: check
  ref: check.py::check_three_cutoffs_solve_exactly
- kind: check
  ref: check.py::check_proper_time_leading_term
- kind: check
  ref: check.py::check_constants_order_one
locators:
  paper: T08
  number: Lem 3.2
  label: lem:scheme
  line: 612
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the three cutoffs solved exactly as monomials, the proper-time leading term from the interior series, and the order-one constants. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    added:
    - obj.scrambling.stretched-singularity
    note: 'kept the Kasner-form lemma, which supplies the proper-time series; the three criteria are stated as explicit equations and solved directly, so the imported curvature spectrum behind the Kretschmann value was not added as a premise; the stretched-singularity definition added under about.'
  env: lemma
---

## formal
The stretched singularity is robust at order one against the choice of Planck criterion: the curvature-eigenvalue condition $2M/r^3 = 1$, the Kretschmann condition $48M^2/r^6 = 1$, and the unit-proper-time condition $\tau(r) = 1$ (with $\tau = \tfrac23 r^{3/2}(2M)^{-1/2}(1 + O(r/2M))$ the proper time to the singularity) all yield $r_c = c_0\,M^{1/3}\lP^{2/3}$ with order-one constants: $c_0 = 2^{1/3}$, $48^{1/6}$, and $(3/2)^{2/3}\,2^{1/3}$ respectively. The surface where the algebra requires completion is, at this order, unambiguous.

## technical
Three choices of Planck criterion are compared for where the classical interior description gives way: the curvature-eigenvalue condition $2M/r^3 = 1$, the Kretschmann condition $48M^2/r^6 = 1$, and unit proper time to the singularity, $\tau(r) = 1$ with $\tau = \tfrac23\,r^{3/2}(2M)^{-1/2}(1 + O(r/2M))$. Each yields a cutoff radius $r_c = c_0\,M^{1/3}\lP^{2/3}$, with $c_0 = 2^{1/3}$, $48^{1/6}$ and $(3/2)^{2/3}\,2^{1/3}$ respectively, all of order one.

So, at this order, the surface on which the completion is required, the stretched singularity, is the same whichever of the three criteria is used.

## lay
Inside a black hole one has to decide where ordinary geometry stops being trusted, and there are several reasonable ways to set that threshold. This result checks three of them and finds that they all put the boundary at essentially the same radius, which grows as the cube root of the mass, differing only by factors between about 1.3 and 1.9. The location is therefore not an artefact of the choice.

## one-liner
The curvature, Kretschmann and proper-time Planck criteria all place the stretched singularity at $r_c = c_0\,M^{1/3}\lP^{2/3}$ with order-one constants $c_0$.
