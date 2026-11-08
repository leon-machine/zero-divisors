---
id: std-algebra.vector-squares
kind: claim
version: 1
title: The product of two vectors
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- classical-theorem
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
  - std-algebra.polarisation@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_anticommutator_is_twice_the_polar_form
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
In $\Cl(V, Q)$, for all $u, v \in V$,
\begin{equation}
v^{2} = Q(v), \qquad u v + v u = 2 B(u, v).
\end{equation}
In particular $u v = B(u, v) + \tfrac12(u v - v u)$, the sum of a scalar and an antisymmetric part.

## technical
A vector squares to its quadratic form, and the symmetrised product of two vectors is twice their polar form: $uv + vu = 2B(u, v)$. So the product of two vectors splits into the scalar $B(u, v)$ and the antisymmetric part $\tfrac12(uv - vu)$.

## lay
Multiplying two arrows gives a number plus something new. The number is their ordinary dot product. The new part changes sign when the order is swapped, and turns out to be the oriented plane the two arrows span.

## one-liner
$v^{2} = Q(v)$ and $uv + vu = 2B(u, v)$, so $uv = B(u, v) + \tfrac12(uv - vu)$.
