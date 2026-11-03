---
id: scrambling.slice-volume-exactly-per-unit-killing
kind: claim
version: 4
title: The slice volume is exactly $8\pi M$ per unit Killing time, at leading order in $r_c/2M$
status: proved
region: scrambling
subject: interior
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
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:prop:volume
- kind: check
  ref: check.py::check_induced_slice_geometry_and_volume
- kind: check
  ref: check.py::check_cutoff_gives_exactly_eight_pi_m
locators:
  paper: T08
  number: Prop 3.3
  label: prop:volume
  line: 620
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the induced slice geometry from the PG gauge field and the volume 4 pi r_c^2 sqrt(f), and 8 pi M exactly at the cutoff with its M-scaling. Version 3 -> 4.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the slice is the background surface r = r_c of the Painleve-Gullstrand gauge field and the induced geometry is read from hb^{-1}; computation unchanged. Proof prefixed.'
  typing:
    by: ai-typing-pass
    note: 'Elementary computation from the static metric with no store premise; the source does not present
      it as a classical result, so no standard-route. Levels pass: conditions already kept.'
  env: proposition
---

## formal
For the Schwarzschild field in the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$, $\beta = \sqrt{2M/r}$, of Fact \claimref{sheaf.gauge-field-cometric}, the induced geometry of the background slice $r = r_c$ inside the horizon, read from $\hb^{-1}$ on its tangent vectors ($Q(\hb^{-1}(e_t)) = -f$), is $ds_3^2 = f\,dt^2 + r_c^2\,d\Omega^2$ with $f = 2M/r_c - 1$, so the three-volume per unit Killing time $t$ is $4\pi r_c^2\sqrt{f}$. With the curvature cutoff $r_c = (2M)^{1/3}$ and to leading order in $r_c/2M$ (i.e.\ $f \approx 2M/r_c$),
\[
4\pi\,r_c^2\,\sqrt{2M/r_c} \;=\; 4\pi\,\sqrt{2M}\;r_c^{3/2} \;=\; 4\pi\,\sqrt{2M}\,\sqrt{2M} \;=\; 8\pi M
\]
\emph{exactly}: the cutoff radius combines with the anisotropic stretch of the $t$-direction to give an exactly linear dependence on the mass. A cutoff radius independent of $M$ would give $M^{1/2}$ instead.

## technical
The background slice $r = r_c$ of the Painlev\'e-Gullstrand gauge field inside the horizon has induced metric $ds_3^2 = f\,dt^2 + r_c^2\,d\Omega^2$ with $f = 2M/r_c - 1$, so its three-volume per unit Killing time is $4\pi r_c^2\sqrt f$. With the curvature cutoff $r_c = (2M)^{1/3}$ and to leading order in $r_c/2M$, where $f \approx 2M/r_c$, this is $4\pi\sqrt{2M}\,r_c^{3/2} = 8\pi M$ exactly. The cutoff radius combines with the stretch of the $t$-direction to give a dependence linear in the mass; a cutoff radius independent of $M$ would give $M^{1/2}$ instead.

## lay
Inside a black hole one can look at the surface of fixed radius near the centre where the curvature reaches the Planck scale. This result computes how much volume that surface gains per unit of the black hole's outside time. At leading order the answer is exactly eight pi times the mass, so it grows in direct proportion to the mass.

## one-liner
At the curvature cutoff $r_c = (2M)^{1/3}$ the interior slice volume per unit Killing time is exactly $8\pi M$ at leading order in $r_c/2M$.
