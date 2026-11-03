---
id: sheaf.solve-closed-radical-gauge
kind: claim
version: 3
title: The solve, closed by the radical gauge
status: proved
region: sheaf
subject: walls
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
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:10.2
- kind: check
  ref: check.py::check_musical_image_is_ker_k
- kind: check
  ref: check.py::check_solution_unique_modulo_k
- kind: check
  ref: check.py::check_normalisation_one_gauge
locators:
  paper: T04
  number: Lem 10.2
  label: lem:wallsolve
  line: 1356
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: musical image equals ker k, solutions unique modulo R k, and the normalisation met at exactly one gauge (slope 2) on all corank-one wall fibres with n <= 5 and Schwarzschild data. Version 1 -> 2. Check strengthened: the second solution (reversed-column solve) actually differs from vt, and the difference is asserted to span R k; the old reversed-row solve returned vt itself. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: "No edges: the proof is a rank count and a one-line gauge computation."
---

## formal
For every $v \in \ker k$ there is $\tilde v \in T^*M$ with $G(\alpha, \tilde v) = \alpha(v)$ for all $\alpha$, unique modulo $\R k$; and the normalisation $G(\tilde v, \tilde v) + 2\tilde v(u) = 0$ is met at exactly one gauge representative, the left side being affine in the gauge parameter with slope $2k(u) = 2$.

## technical
At the wall the cometric $G$ has radical $\R k$, so the map $\alpha \mapsto G(\alpha, \cdot)$ has image exactly $\ker k$. Hence for every $v \in \ker k$ there is a covector $\tilde v$ with $G(\alpha, \tilde v) = \alpha(v)$ for all $\alpha$, unique up to adding multiples of $k$. Under $\tilde v \mapsto \tilde v + tk$ the quantity $G(\tilde v, \tilde v) + 2\tilde v(u)$ changes by $2t\,k(u) = 2t$, so exactly one representative meets the normalisation $G(\tilde v, \tilde v) + 2\tilde v(u) = 0$.

## lay
At the wall the geometry cannot be inverted in the usual way, because one direction has no length. Still, for directions compatible with the dying one, an inverse exists up to an ambiguity along the dying direction. A single extra condition removes that ambiguity uniquely.

## one-liner
For each $v \in \ker k$ the equation $G(\alpha, \tilde v) = \alpha(v)$ has a solution unique modulo $\R k$, and the normalisation $G(\tilde v, \tilde v) + 2\tilde v(u) = 0$ selects exactly one.
