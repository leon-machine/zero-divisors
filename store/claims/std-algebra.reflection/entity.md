---
id: std-algebra.reflection
kind: claim
version: 1
title: Reflection in a non-null vector
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- rotors-and-stabilisers
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
- obj.std-algebra.quadratic-space
derivations:
- name: main
  uses:
  - std-algebra.inverse-of-vector@1
  - std-algebra.vector-squares@1
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_sandwich_is_reflection
locators:
  sources:
  - key: DoranLasenby2003
    locator: 'Ch. 4 (foundations of geometric algebra: rotors, versors)'
  - key: HestenesSobczyk1984
    locator: Ch. 3 (versors, rotors and the bivector algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
Let $u \in V$ with $Q(u) \ne 0$. Then $V = \R u \oplus u^{\perp}$, and for $x \in V$
\begin{equation}
-\,u x u^{-1} = x - 2\,\frac{B(x, u)}{Q(u)}\, u .
\end{equation}
The map $s_u : x \mapsto -u x u^{-1}$ is an isometry of $(V, Q)$ fixing $u^{\perp}$ pointwise and sending $u$ to $-u$: the reflection in the hyperplane $u^{\perp}$. It fixes $\operatorname{rad} V$ pointwise, $s_u^{2} = 1$, $s_{\lambda u} = s_u$ for $\lambda \ne 0$, and its determinant is $-1$. If $Q(a) = Q(b) \ne 0$ and $Q(a - b) \ne 0$, then $s_{a-b}(a) = b$.

## technical
Sandwiching a vector between a non-null vector $u$ and its inverse, with a minus sign, reflects it in the hyperplane perpendicular to $u$: the component along $u$ flips and the perpendicular part is untouched. This is an isometry with determinant $-1$, an involution, and it fixes every radical vector, since radical vectors are perpendicular to $u$. Two vectors of the same nonzero square are exchanged by the reflection in their difference when that difference is not null.

## lay
Multiplying an arrow on both sides by a fixed arrow, with a sign, gives its mirror image in the plane perpendicular to the fixed arrow. This works for any fixed arrow that does not have zero length. Mirrors are the building blocks of all rotations.

## one-liner
For $Q(u) \ne 0$, $x \mapsto -uxu^{-1} = x - 2\frac{B(x,u)}{Q(u)}u$ is the reflection in $u^{\perp}$: an involutive isometry of determinant $-1$ fixing $\operatorname{rad} V$.
