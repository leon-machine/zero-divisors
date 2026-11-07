---
id: sheaf.gauge-field-cometric
kind: claim
version: 3
title: The gauge field and its cometric
status: proved
region: sheaf
subject: singularity
tags: [schwarzschild, null-directions]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
derivations:
- name: main
  uses:
  - sheaf.gauge-field-cometric-external@1
  - singularity.cones-fold@4
  - singularity.degeneration-exactly@2
  - singularity.solution-where-divergence-lies@3
  - singularity.unipotent-ray@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_unipotent_gauge_field_invertible_off_zero
- kind: check
  ref: check.py::check_induced_metric_is_painleve_gullstrand
- kind: check
  ref: check.py::check_degeneration_through_a_null_kernel
locators:
  paper: T04
  number: Fact 8.1
  label: fact:pg
  line: 863
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: at three masses as identities in sqrt r, P^2 = 0, hbar^-1 = 1 + beta P with det 1, the induced metric is the Painleve-Gullstrand line element with the stated cometric, and eps hbar -> -P with the null kernel direction e_r. Version 2 -> 3.'
  env: fact
  context_refs:
  - singularity.cones-fold
  - singularity.degeneration-exactly
  - singularity.solution-where-divergence-lies
  - singularity.unipotent-ray
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'kept all five edges: the four series propositions are the restated results and the external entry carries the cited gauge-theoretic background; corrected the earlier note and levels, which called this an imported fact although its status is proved; no standard-route derivation, since the paper cites the textbook as background, not as an independent derivation, and the standard Painleve-Gullstrand result has no separate store entry.'
  repair:
    note: 'status imported -> proved: the fact restates series results cited without brackets; derivation
      assembled from them'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - singularity.unipotent-ray
    - singularity.solution-where-divergence-lies
    - singularity.cones-fold
    - singularity.degeneration-exactly
    - sheaf.gauge-field-cometric-external
---

## formal
In gauge theory gravity the Schwarzschild solution in the Newtonian (Painlev\'e-Gullstrand) gauge is carried by $\hb = 1 - \beta P$, $\beta = \sqrt{2M/r}$, $P(a) = (a \cdot e_t)\,e_r$, with $P^2 = 0$; $\hb$ is invertible in closed form at every $r > 0$, horizon included, and fails at $r = 0$ through a null kernel. The induced metric is the Painlev\'e-Gullstrand line element $ds^2 = dt^2 - (dr + \beta\,dt)^2 - r^2 d\Omega^2$. \emph{Provenance:} \cite{ButlerT5}, Props.~2.2, 2.4, 2.5 and 2.6, and Appendix A; the gauge-theoretic background is \cite{DoranLasenby2003}.

## technical
In gauge theory gravity the Schwarzschild solution in the Painlev\'e-Gullstrand gauge is carried by the gauge field $\hb = 1 - \beta P$, with $\beta = \sqrt{2M/r}$ and $P(a) = (a \cdot \et)\,\er$, where $P^2 = 0$. The field $\hb$ is invertible in closed form at every $r > 0$, the horizon included, and fails at $r = 0$ through a null kernel.

The induced metric is the Painlev\'e-Gullstrand line element $ds^2 = dt^2 - (dr + \beta\,dt)^2 - r^2\,d\Omega^2$. The fact restates results proved earlier in the series, with the gauge-theoretic background from the standard literature.

## lay
This fact, carried over from earlier in the series, describes the Schwarzschild black hole in a formulation of gravity where the gravitational field is a linear map acting on directions. In coordinates adapted to observers falling freely inward, this map can be inverted explicitly everywhere except the centre, including at the event horizon, and it breaks down only at the central singularity. It reproduces the standard Painlev\'e-Gullstrand form of the black-hole geometry.

## one-liner
In gauge theory gravity the Painlev\'e-Gullstrand Schwarzschild field $\hb = 1 - \beta P$ is invertible at every $r > 0$, fails at $r = 0$ through a null kernel, and induces the Painlev\'e-Gullstrand line element.
