---
id: sheaf.boundary-units-invert
kind: claim
version: 2
title: Boundary units invert
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
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_admissible_neumann_inverse
- kind: check
  ref: check.py::check_smooth_positive_plus_small_is_invertible
- kind: check
  ref: check.py::check_geometric_convergence_where_a_is_small
locators:
  paper: T04
  number: Lem 9.2
  label: lem:units
  line: 1184
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: admissible Neumann inverse of 1 + a modulo tau^N, inversion of c + a, and the geometric bound at sample points. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: "Self-contained lemma with no premises; no edges changed."
---

## formal
If $a \in \mathcal{A}$ has every exponent bounded below by some $\delta > 0$ on the relevant compact (so $a = O(\tau^\delta)$ locally uniformly), then $1 + a$ is invertible in $\mathcal{A}$ after shrinking $\varepsilon$: the Neumann series $\sum_{k \geq 0} (-a)^k$ has exponent families adding to $\{k\delta + \cdots\}$, admissible since only finitely many products fall below any level, and it converges locally uniformly where $|a| \leq \tfrac12$. More generally any $c + a$ with $c$ smooth, positive and bounded away from zero near $E$ is invertible in $\mathcal{A}$.

## technical
Let $a \in \mathcal{A}$ have every exponent bounded below by some $\delta > 0$ on the relevant compact, so that $a = O(\tau^\delta)$ locally uniformly. Then, after shrinking $\varepsilon$, $1 + a$ is invertible in $\mathcal{A}$, with inverse the Neumann series $\sum_{k \geq 0}(-a)^k$: its exponent family is admissible, because only finitely many products fall below any level, and it converges locally uniformly where $|a| \leq \tfrac12$. More generally $c + a$ is invertible whenever $c$ is smooth, positive and bounded away from zero near $E$.

## lay
In the algebra of functions built from varying powers of time, it matters which elements can be divided by. This result shows that a positive smooth quantity plus a correction that vanishes at the boundary can always be inverted near the boundary. The inverse is given by the usual geometric series.

## one-liner
In the variable-order algebra, $c + a$ is invertible near $E$ whenever $c$ is smooth, positive and bounded away from zero and every exponent of $a$ is bounded below by some $\delta > 0$.
