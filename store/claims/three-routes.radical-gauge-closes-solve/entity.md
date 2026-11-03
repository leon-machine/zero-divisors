---
id: three-routes.radical-gauge-closes-solve
kind: claim
version: 5
title: The radical gauge closes the solve
status: proved
region: three-routes
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
  source: 'authorship disclosure of T05-three-routes, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - three-routes.imported-boundary-gram-ladder@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_three_routes.py
  tags:
  - num:3.3
- kind: check
  ref: check.py::check_image_is_ker_k
- kind: check
  ref: check.py::check_unique_modulo_radical
- kind: check
  ref: check.py::check_normalisation_fixes_the_gauge
locators:
  paper: T05-three-routes
  number: Lem 3.3
  label: lem:solve
  line: 188
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: musical image equals ker k, uniqueness modulo R k and the one-gauge normalisation on Schwarzschild boundary data at five masses. Version 3 -> 4. Check strengthened: uniqueness modulo Rk checked from both transversals; probe covectors moved to module level. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    added:
    - three-routes.imported-boundary-gram-ladder
    note: 'Added the boundary Gram fact, since solvability uses that G has corank one with radical R k.
      Linked equivalent_to sheaf.solve-closed-radical-gauge: the companion note restates it. Levels pass:
      the lay now keeps the condition v in ker k under which solutions exist.'
  env: lemma
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - three-routes.imported-boundary-gram-ladder
equivalent_to:
- sheaf.solve-closed-radical-gauge@3
---

## formal
For every $v \in \ker k$ there is a covector $\tilde v \in W$ with $G(\alpha, \tilde v) = \alpha(v)$ for all $\alpha$, unique modulo the radical $\R k$; and the normalisation
\[
G(\tilde v, \tilde v) + 2\,\tilde v(u) \;=\; 0
\]
fixes it uniquely, the left side being affine in the gauge parameter with slope $2\,k(u) = 2 \neq 0$.

## technical
At a boundary point the map $\alpha \mapsto G(\alpha, \cdot)$ has kernel $\R k$ and image exactly $\ker k$, so for each $v \in \ker k$ there is a covector $\tilde v$ with $G(\alpha, \tilde v) = \alpha(v)$ for all $\alpha$, unique up to adding a multiple of $k$.

The normalisation $G(\tilde v, \tilde v) + 2\,\tilde v(u) = 0$ removes that gauge freedom: shifting $\tilde v$ by $tk$ leaves $G(\tilde v, \tilde v)$ unchanged and moves $\tilde v(u)$ by $t\,k(u) = t$, so the left side is affine in $t$ with slope $2$ and vanishes at exactly one value.

## lay
Because the boundary geometry is degenerate, a certain linear equation has solutions only for directions compatible with the collapse, and for each of those it has many, differing by multiples of the collapsing direction. A single extra condition picks out exactly one of them. This removes the ambiguity completely.

## one-liner
For each $v \in \ker k$ the solution $\tilde v$ of $G(\alpha, \tilde v) = \alpha(v)$ exists modulo $\R k$ and is fixed uniquely by $G(\tilde v, \tilde v) + 2\tilde v(u) = 0$.
