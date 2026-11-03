---
id: std-algebra.orthogonal-anticommute
kind: claim
version: 1
title: Orthogonal vectors anticommute
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- grading-and-parity
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-algebra
derivations:
- name: main
  uses:
  - std-algebra.vector-squares@1
  - std-algebra.blade-basis@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_blade_table
- kind: check
  ref: check.py::check_anticommute_iff_orthogonal
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
For $u, v \in V$: $u v = -v u$ if and only if $B(u, v) = 0$. In an orthogonal basis $e_1, \dots, e_n$, $e_i e_j = -e_j e_i$ for $i \ne j$ and $e_i^{2} = Q(e_i)$, and the product of two basis blades is $e_I e_J = \pm \bigl(\prod_{i \in I \cap J} Q(e_i)\bigr)\, e_{I \triangle J}$, the sign being $(-1)$ to the number of pairs $(i, j) \in I \times J$ with $i > j$.

## technical
Two vectors anticommute exactly when they are orthogonal. In an orthogonal basis this gives the multiplication table of basis blades: the product $e_I e_J$ is the blade on the symmetric difference $I \triangle J$, times the squares of the shared generators, times a sign that counts how many transpositions are needed to sort the indices.

## lay
Perpendicular arrows anticommute: swapping their order flips the sign. That single fact, plus the squares of the basis arrows, gives the whole multiplication table.

## one-liner
$uv = -vu$ iff $B(u,v) = 0$; in an orthogonal basis $e_I e_J = \pm \prod_{I \cap J} Q(e_i)\; e_{I \triangle J}$ with the sorting sign.
