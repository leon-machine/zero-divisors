---
id: singularity.unipotent-ray
kind: claim
version: 4
title: The unipotent ray
status: proved
region: singularity
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
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: strengthened check
  version: 4
  source: maintainer pass of 7 November 2026
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:2.2
- kind: check
  ref: check.py::check_p_squares_to_zero
- kind: check
  ref: check.py::check_closed_form_inverse_horizon_included
- kind: check
  ref: check.py::check_trajectory_is_unipotent_ray
locators:
  paper: T05
  number: Prop 2.2
  label: prop:unipotent
  line: 1333
extraction:
  maintainer_pass_warnings:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4: check_p_squares_to_zero now also asserts that P is a single elementary nilpotent (one nonzero entry in its 4 x 4 matrix), so the mutation test has literals to perturb.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: P^2 = 0, hb^{-1} = 1 + beta P over Q(beta) with det 1 and the horizon included, and the unipotent ray. Version 1 -> 2. Sample inputs moved to module level; the presence of the horizon sample beta = 1 is now asserted; no other change to what is tested. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    note: 'self-contained two-line computation, no premises; the paper does not present the result as a standard-physics recovery.'
  env: proposition
---

## formal
$P^2 = 0$ exactly, at every radius; consequently $\hb$ is invertible at every $r > 0$, in closed form,
\[
\hb^{-1} \;=\; 1 + \beta P ,
\]
horizon included. The Schwarzschild gauge trajectory $\{1 - \beta P : \beta \geq 0\}$ is a ray of unipotent maps, and the horizon ($\beta = 1$) is algebraically unremarkable: division does not fail there.

## technical
In the Painlev\'e-Gullstrand gauge the Schwarzschild gauge field is $\hb = 1 - \beta P$, with $\beta = \sqrt{2M/r}$ and $P(a) = (a\cdot\et)\,\er$. Since $\er \cdot \et = 0$, $P^2 = 0$ exactly at every radius, so $\hb$ is invertible at every $r > 0$ in closed form, $\hb^{-1} = 1 + \beta P$, horizon included.

The gauge trajectory $\{1 - \beta P : \beta \geq 0\}$ is therefore a ray of unipotent maps, and the horizon $\beta = 1$ is algebraically unremarkable: division does not fail there.

## lay
In this formulation of gravity, the field describing a non-rotating black hole is the identity plus a shear whose square is zero. That makes it reversible at every radius, with an explicit formula for the inverse. In particular nothing goes wrong algebraically at the event horizon.

## one-liner
The Painlev\'e-Gullstrand Schwarzschild gauge field $\hb = 1 - \beta P$ has $P^2 = 0$, so $\hb^{-1} = 1 + \beta P$ at every $r > 0$, horizon included.
