---
id: dark-energy.gravity-pre-metric-forces-degenerate-exactly
kind: claim
version: 5
title: Gravity is pre-metric; the forces degenerate exactly where the conformal class does
status: proved
region: dark-energy
subject: dark-energy
tags: [refutation, gauge-fields, curvature-and-field-equations, no-go]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - dark-energy.imported-walls-sphere-theorem@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:thm:twokinds
- kind: check
  ref: check.py::check_star_free_invariant_is_topological
- kind: check
  ref: check.py::check_hodge_star_depends_on_conformal_class_only
- kind: check
  ref: check.py::check_star_degenerates_at_corank_one_wall
locators:
  paper: T10
  number: Thm 4.3
  label: thm:twokinds
  line: 823
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The result is about the Hodge star on two-forms as a function of the metric, *alpha_{ab} = (1/2) sqrt|g| epsilon_{abcd} g^{ce} g^{df} alpha_{ef}, and its failure where the metric degenerates; on bivectors of an invertible field it is multiplication by the pseudoscalar, but the degenerate case it treats has no pseudoscalar duality, so the component form is the content.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: tr(F ^ F) = d CS and the Bianchi identity for polynomial gl(2) connections, the Hodge star depending on the conformal class only, and its degeneration at a corank-one wall. Version 2 -> 3. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    added:
    - dark-energy.frozen-point-makes-stelle-west-vector
    note: 'Added the action theorem, which clause (2) cites for gravity''s action being pre-metric; the
      refutation-record citation is context only. Levels pass: the lay level now restricts the wall to
      a tame corank-one wall, speaks of the standard actions of the other forces, and keeps the formal''s
      open question about actions of a different shape.'
  env: theorem
  context_refs:
  - dark-energy.frozen-point-makes-stelle-west-vector
  outside_pilot_cites:
  - ButlerT12
  - ButlerT17
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-energy.frozen-point-makes-stelle-west-vector
outside_ga:
  kind: other
  why: 'The result is about the Hodge star on two-forms as a function of the metric, *alpha_{ab} = (1/2) sqrt|g| epsilon_{abcd} g^{ce} g^{df} alpha_{ef}, and its failure where the metric degenerates; on bivectors of an invertible field it is multiplication by the pseudoscalar, but the degenerate case it treats has no pseudoscalar duality, so the component form is the content.'
---

## formal
(Shared with the Standard-Model paper \cite{ButlerT12}, which uses it from the internal side.)
\begin{enumerate}
\item Neither of the two routes by which the MacDowell-Mansouri mechanism could extend to an internal factor is open. Contraction with the frozen point produces nothing there: $I$ is a singlet for the internal group and an internal field strength carries no tractor index, so no invariant of the form $\epsilon(I, \cdot, F_i, F_i)$ exists. And the star-free quadratic invariants of an internal field strength, $\int\tr(F_i\wedge F_i)$ for each simple factor, are topological: a boundary term with vanishing interior variation and no field equations. The natural conjecture, that the forces are gauged polynomially as gravity is, fails along both routes: the ninth refutation in the series' record \cite[Table~1, row 9]{ButlerT17}. (Whether some polynomial functional of a different shape could serve is not decided here.)
\item What exists instead are the Yang-Mills functionals $S_i = (1/2g_i^2)\int \tr(F_i \wedge {*}F_i)$, and the Hodge star on two-forms in four dimensions depends on exactly one piece of metric data, the conformal class $[g]$, and is independent of the scale. The internal forces are therefore \emph{conformal-level} objects, defined exactly where the conformal class is nondegenerate, while gravity's action alone is \emph{pre-metric}: polynomial in the connection, the frozen point and the Stelle-West vector, defined across the singular locus (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(1)).
\item Corollary: at a tame corank-one wall the cometric acquires a radical and the metric a pole (Fact \claimref{dark-energy.imported-walls-sphere-theorem}), so the conformal class degenerates and the star on two-forms, built from two inverse metrics and the volume form, is no longer a nondegenerate map there; the internal actions degenerate with the metric, what crosses is gravity together with the topological $\theta$-terms, the part of each force that survives the singularity.
\end{enumerate}

## technical
The MacDowell-Mansouri mechanism does not extend to an internal gauge factor along either route. The frozen point is an internal singlet and an internal field strength carries no tractor index, so no invariant $\epsilon(I,\cdot,F_i,F_i)$ exists; and the star-free quadratic invariants $\int\tr(F_i\wedge F_i)$ are topological, a boundary term with no field equations. Whether a polynomial functional of some other shape could serve is not decided. What exists instead are the Yang-Mills functionals $(1/2g_i^2)\int\tr(F_i\wedge *F_i)$, and the Hodge star on two-forms in four dimensions depends on the conformal class $[g]$ alone.

So the internal forces are conformal-level objects, defined where the conformal class is nondegenerate, while gravity's action is pre-metric: polynomial in the connection, the frozen point and the Stelle-West vector. At a tame corank-one wall the cometric acquires a radical and the metric a pole, the star on two-forms is no longer a nondegenerate map, and the internal actions degenerate; what crosses is gravity together with the topological $\theta$-terms.

## lay
Gravity's action can be written without ever inverting the metric, but the standard actions of the other forces cannot: they need the Hodge star, which depends on the metric's angles though not its overall scale. The two natural ways of writing the other forces in gravity's style either give nothing or give only a term without dynamics; whether some other kind of action could work is left open. So at a mild (tame) singular wall, where the metric loses one direction and degenerates, the ordinary forces break down with it, while gravity and the topological part of each force carry on across.

## one-liner
Gravity's action is pre-metric while the internal forces' Yang-Mills actions need the conformal class, so at a tame corank-one wall the internal actions degenerate and only gravity and the topological $\theta$-terms cross.
