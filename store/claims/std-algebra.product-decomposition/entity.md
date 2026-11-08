---
id: std-algebra.product-decomposition
kind: claim
version: 1
title: A vector times a multivector
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
- obj.std-algebra.outer-product
- obj.std-algebra.left-contraction
derivations:
- name: main
  uses:
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.grade-decomposition@2
  - std-algebra.involution-properties@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_vector_times_multivector
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
  - key: HestenesSobczyk1984
    locator: Ch. 1 (geometric algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
For a vector $a \in V$ and any $X \in \Cl(V, Q)$,
\begin{equation}
a X = a \rfloor X + a \wedge X, \qquad a \rfloor X = \tfrac12\bigl(a X - \hat{X} a\bigr), \qquad a \wedge X = \tfrac12\bigl(a X + \hat{X} a\bigr).
\end{equation}
For $X = X_k \in \Cl^{k}$, $a \rfloor X_k \in \Cl^{k-1}$ and $a \wedge X_k \in \Cl^{k+1}$, so $a X_k$ has only these two grades. In particular $a b = B(a, b) + a \wedge b$ for vectors.

## technical
The geometric product of a vector with a multivector splits into a contraction, which lowers grade by one, and an outer product, which raises it by one; nothing else occurs. Both parts are given by symmetrising or antisymmetrising the product against the grade involution. For two vectors this is $ab = a \cdot b + a \wedge b$.

## lay
Multiplying an arrow into any element does two things at once: it removes the arrow's direction where it is already present, and adds it where it is not. The full product is just the sum of the two.

## one-liner
$aX = a \rfloor X + a \wedge X$ with $a \rfloor X = \tfrac12(aX - \hat{X}a)$ and $a \wedge X = \tfrac12(aX + \hat{X}a)$.
