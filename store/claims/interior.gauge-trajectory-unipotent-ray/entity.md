---
id: interior.gauge-trajectory-unipotent-ray
kind: claim
version: 9
title: The gauge trajectory is a unipotent ray
status: proved
region: interior
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
  source: authorship disclosure of T06, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, kernel direction stated as null for the limit form; garbled proof expression repaired'
  version: 9
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass, uses edges to the restated singularity results at Leon''s decisions'
  version: 9
  source: maintainer pass 2026-11-07 (decisions)
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - singularity.degeneration-exactly@2
  - singularity.type-n-only-type-n@5
  - singularity.non-removability-invariant-argument@2
  - std-algebra.orthogonal-anticommute@1
  - singularity.unipotent-ray@4
  - singularity.cones-fold@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:3.1
- kind: check
  ref: check.py::check_unipotent_group_and_history_ray
- kind: check
  ref: check.py::check_closed_form_inverse
- kind: check
  ref: check.py::check_metric_is_painleve_gullstrand
- kind: check
  ref: check.py::check_folding_onto_kernel_direction
locators:
  paper: T06
  number: Prop 3.1
  label: prop:unipotent
  line: 381
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version kept at 9 (already raised in this run). Decision items D10 and E2 (routine): clauses (1), (2) and (4) restate singularity.unipotent-ray (T05 Prop 2.2) and singularity.cones-fold (T05 Prop 2.5); uses edges to both (@4) are added and the proof says so, keeping the group law along the ray as this result''s own content; the singularity originals are the homes.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.orthogonal-anticommute where the proof uses them. Version 7 -> 8.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: P^2 = 0 and the group law over Q(s), the history ray, hb^{-1} = 1 + beta P with det 1, the PG metric entries, and the folding onto the kernel direction. Version 5 -> 6. Check strengthened: ray samples now pin s^2 r = 2M and the horizon r = 2M at |s| = 1; samples moved to module level. Version 6 -> 7.'
  typing:
    by: ai-typing-pass
    added:
    - singularity.type-n-only-type-n
    - singularity.non-removability-invariant-argument
    note: 'the proof says the type-N diagnosis and the absence of any removing gauge choice are quoted
      from the singularity paper''s Steps 1-2 rather than reproved, so the type-N and non-removability
      propositions are premises; the solution proposition (context ref) is cited but not used, and the
      cone folding is recomputed here. Levels pass: conditions already kept.'
  env: proposition
  context_refs:
  - singularity.solution-where-divergence-lies
  - singularity.type-n-only-type-n
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - singularity.non-removability-invariant-argument
    - singularity.type-n-only-type-n
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 8 -> 9. Wording and a typo only: clause (4) said the cones fold onto "the single null direction of the kernel", but e_r is null only for the rescaled limit form (singularity.degeneration-exactly(3); g(e_r, e_r) = -1 at every r > 0, as the proof already says), so the clause now says so; in the proof the expression 1 - beta^2 - 2 lambda beta - lambda^2 . 1 . (-1)(-1) is written as (e_t + (lambda + beta) e_r)^2 = 1 - (lambda + beta)^2, the same polynomial. Statement, status and links unchanged.'
---

## formal
The map $P$ is nilpotent, $P^2 = 0$, exactly and at every radius. Consequently:
\begin{enumerate}
\item the maps $\{1 + sP : s \in \R\}$ form a one-parameter unipotent group, $(1 + sP)(1 + s'P) = 1 + (s + s')P$, and the entire history of the gauge field, from spatial infinity to the singularity, is the ray $s = -\beta(r) \in (-\infty, 0]$ in this group;
\item $\hb$ is invertible at every $r > 0$ in closed form, $\hb^{-1} = 1 + \beta P$, the horizon $\beta = 1$ included: the horizon is algebraically unremarkable;
\item the metric $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$ is the Painlev\'e-Gullstrand line element: $g(\et,\et) = 1 - \beta^2 = 1 - 2M/r$, $g(\et,\er) = -\beta$, $g(\er,\er) = -1$, angular directions untouched;
\item the singularity is the divergence $s \to -\infty$ of the shear parameter: division fails nowhere at $r > 0$ and unavoidably at $r = 0$, where the light cones of $g$ fold onto the single kernel direction $\er$, null for the rescaled limit form (Proposition \claimref{singularity.degeneration-exactly}(3); $g(\er, \er) = -1$ at every $r > 0$), a type-N degeneration \cite[Props.~2.4-2.6, 3.1]{ButlerT5}.
\end{enumerate}

## technical
The map $P(a) = (a\cdot\et)\,\er$ in the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$, $\beta = \sqrt{2M/r}$, satisfies $P^2 = 0$ exactly at every radius. Hence the maps $1 + sP$ form a one-parameter unipotent group, $(1 + sP)(1 + s'P) = 1 + (s + s')P$, and the whole history of the gauge field, from spatial infinity to the singularity, is the ray $s = -\beta(r) \in (-\infty, 0]$. In particular $\hb^{-1} = 1 + \beta P$ at every $r > 0$, the horizon $\beta = 1$ included, and the metric $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$ is the Painlev\'e-Gullstrand line element, with $g(\et,\et) = 1 - 2M/r$, $g(\et,\er) = -\beta$, $g(\er,\er) = -1$.

The singularity is the divergence $s \to -\infty$ of the shear parameter. Division fails nowhere at $r > 0$ and unavoidably at $r = 0$, where the null directions $\et + \lambda\er$ of $g$, $\lambda = -\beta \pm 1$, fold onto the single kernel direction $\er$, a type-N degeneration (the type-N diagnosis and its non-removability being taken from the earlier singularity analysis).

## lay
In this formulation of gravity, the field describing a non-rotating black hole is the identity plus a shear, and the size of the shear grows steadily as one falls inward. Because the shear squared is zero, the field can be undone by an explicit formula at every radius, including at the event horizon, which is nothing special algebraically. The only place it cannot be undone is the centre, where the shear becomes infinite and the light cones collapse onto a single direction.

## one-liner
The Painlev\'e-Gullstrand Schwarzschild gauge field traces a ray in a one-parameter unipotent group, invertible in closed form at every $r > 0$ including the horizon, with the singularity at $r = 0$ as the divergence of the shear parameter.
