---
id: singularity.non-removability-invariant-argument
kind: claim
version: 2
title: 'Non-removability: the invariant argument'
status: proved
region: singularity
subject: singularity
tags: [schwarzschild, no-go, curvature-and-field-equations]
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
  - singularity.solution-where-divergence-lies@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:2.7
- kind: check
  ref: check.py::check_kretschmann_from_gauge_curvature
- kind: check
  ref: check.py::check_rotation_gauge_invariance
locators:
  paper: T05
  number: Prop 2.7
  label: prop:invariant
  line: 1436
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: K = 48 M^2/r^6 from the gauge-field curvature and as an identity, its growth, and its invariance under rotation-gauge transformations. Version 1 -> 2.'
  env: proposition
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'Kept the edge to the solution proposition, whose curvature spectrum is the premise of the evaluation
      of the invariant. Levels pass: conditions already kept.'
---

## formal
The curvature scalar
\[
K \;:=\; R_{abcd}R^{abcd} \;=\; 4\Bigl(2\,\bigl(\tfrac{2M}{r^3}\bigr)^2 + 4\,\bigl(\tfrac{M}{r^3}\bigr)^2\Bigr) \;=\; \frac{48\,M^2}{r^6}
\;\longrightarrow\; \infty \quad (r \to 0),
\]
and $K$ is invariant under every gauge transformation of the theory, $r$-dependent transformations of arbitrary size included. Hence no gauge choice removes the degeneration at $r = 0$: the division-by-zero locus is a property of the solution, not of its presentation.

## technical
The curvature scalar of the solution is $K := R_{abcd}R^{abcd} = 48M^2/r^6$, assembled from the curvature eigenvalue spectrum (each frame plane contributes four times its eigenvalue squared), and it diverges as $r \to 0$. Under the rotation-gauge law the curvature transforms by conjugation, $\mathcal{R}(B) \mapsto R\,\mathcal{R}(B)\tilde R$, which preserves every scalar contraction, and under position-gauge displacements it transforms by pullback, which relocates the function but cannot remove its unbounded range near the singular locus.

Hence $K$ is invariant under every gauge transformation of the theory, $r$-dependent transformations of arbitrary size included, and no gauge choice removes the degeneration at $r = 0$: the division-by-zero locus is a property of the solution, not of its presentation.

## lay
At the centre of a non-rotating black hole, a measure of curvature that does not depend on how the description is set up grows without bound. Because every change of description allowed in the theory leaves this quantity unchanged, no choice of description can make the blow-up disappear. The breakdown at the centre is therefore a feature of the solution itself rather than an artefact of how it is written down.

## one-liner
The curvature invariant $R_{abcd}R^{abcd} = 48M^2/r^6$ is gauge invariant and diverges at $r = 0$, so no gauge choice removes the degeneration there.
