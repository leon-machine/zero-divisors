---
id: singularity.cones-fold
kind: claim
version: 4
title: The cones fold
status: proved
region: singularity
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
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  uses:
  - singularity.degeneration-exactly@2
  - singularity.non-removability-invariant-argument@2
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:2.5
- kind: check
  ref: check.py::check_null_directions_of_the_physical_cone
- kind: check
  ref: check.py::check_horizon_null_pair
- kind: check
  ref: check.py::check_cones_fold_onto_e_r
- kind: check
  ref: check.py::check_limit_direction_is_null_kernel_direction
locators:
  paper: T05
  number: Prop 2.5
  label: prop:fold
  line: 1401
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.orthogonal-anticommute where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: g(e_t + lambda e_r) = 1 - (lambda + beta)^2 over Q(lambda) with roots -beta +- 1, the horizon pair 0 and -2, the folding onto e_r, and e_r as the null kernel direction. Version 2 -> 3.'
  env: proposition
  context_refs:
  - singularity.degeneration-exactly
  - singularity.non-removability-invariant-argument
  eqrefs: 1
  typing:
    by: ai-typing-pass
    added: [singularity.degeneration-exactly, singularity.non-removability-invariant-argument]
    note: 'the proof states that the two claims of the final sentence are the two cited propositions, so both were added as premises of those clauses; the limit computations themselves need neither'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - singularity.degeneration-exactly
    - singularity.non-removability-invariant-argument
---

## formal
Track the null directions of the $(t,r)$ plane in the metric \eqref{eq:metricdef}, $g(a,a) = \hb^{-1}(a)^{2}$ with $\hb^{-1} = 1 + \beta P$: for $a = \et + \lambda\,\er$,
\[
\hb^{-1}(a) = \et + (\lambda + \beta)\,\er, \qquad g(a,a) = 1 - (\lambda + \beta)^2 ,
\]
so $a$ is $g$-null exactly when $\lambda = -\beta \pm 1$: the physical cone's two null directions are $\et + (-\beta \pm 1)\er$, the radial null curves $dr/dt = -\beta \pm 1$ of the Painlev\'e-Gullstrand line element of Appendix \ref{app:metric}. At the horizon ($\beta = 1$) they are $\lambda = 0$, the hovering ray, and $\lambda = -2$, an ingoing one. Normalising each by its $\er$-coefficient and letting $r \to 0$ (so $\beta \to \infty$),
\[
\tfrac{1}{-\beta \pm 1}\,\et + \er \;\longrightarrow\; \er :
\]
both branches of the light cone collapse onto the single direction $\er$, both tipping towards $-\er$, inward, on the way. Simultaneously $g(\et, \et) = 1 - \beta^2 \to -\infty$: no rescaling of the classical field stays finite and nondegenerate. The degeneration is through a null kernel direction in the exact sense of Proposition \claimref{singularity.degeneration-exactly}, and it is not removable by gauge choice (Proposition \claimref{singularity.non-removability-invariant-argument}).

## technical
In the Painlev\'e-Gullstrand gauge the metric is $g(a,a) = Q(\hb^{-1}(a))$ with $\hb^{-1} = 1 + \beta P$. For $a = \et + \lambda\,\er$ in the $(t,r)$ plane this gives $\hb^{-1}(a) = \et + (\lambda + \beta)\er$ and $g(a,a) = 1 - (\lambda + \beta)^2$, so the two null directions are $\lambda = -\beta \pm 1$, the radial null curves $dr/dt = -\beta \pm 1$. At the horizon, $\beta = 1$, they are the hovering ray $\lambda = 0$ and an ingoing ray $\lambda = -2$.

As $r \to 0$, $\beta \to \infty$ and both branches, normalised by their $\er$-coefficient, converge to $\er$, tipping inward on the way, while $g(\et,\et) = 1 - \beta^2 \to -\infty$, so no rescaling of the classical field stays finite and nondegenerate. The degeneration is through a null kernel direction in the exact sense of the rescaled-limit result, and it is not removable by gauge choice.

## lay
Light cones record the directions in which light can travel at each point. Following the two radial light directions inward towards the centre of a black hole, both swing round to point inward and, in the limit at the centre, merge into a single direction. At the same time the time part of the metric grows without bound, so the classical field cannot be rescaled to stay finite and well behaved there, and the failure cannot be removed by a change of gauge.

## one-liner
As $r \to 0$ both radial null directions of the Painlev\'e-Gullstrand metric collapse onto $\er$ while $g(\et,\et)$ diverges, a degeneration through a null kernel direction that no gauge choice removes.
