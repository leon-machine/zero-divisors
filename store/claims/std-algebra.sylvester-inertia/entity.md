---
id: std-algebra.sylvester-inertia
kind: claim
version: 1
title: Orthogonal bases and the law of inertia
status: imported
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- classical-theorem
- clifford-classification
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
- obj.std-algebra.radical
imported_from:
- citation: T. Y. Lam, Introduction to Quadratic Forms over Fields, AMS (2005).
  key: Lam2005
  locator: the diagonalisation of forms and Sylvester's law of inertia (real case)
checked_by:
- kind: check
  ref: check.py::check_inertia_under_congruence
locators:
  sources:
  - key: Lam2005
    locator: Ch. I and II (quadratic forms; the real case)
extraction:
  by: algebra-core-2026-10-26
  note: Imported, with a check of its finite core, as Leon decided on 2026-10-26 for the long classical
    proofs.
---

## formal
Every real quadratic space $(V, Q)$ of dimension $n$ has an orthogonal basis $e_1, \dots, e_n$ with $Q(e_i) \in \{1, -1, 0\}$. The numbers $p$, $q$ and $r$ of basis vectors with $Q(e_i) = 1$, $-1$ and $0$ do not depend on the basis (Sylvester's law of inertia). Moreover $r = \dim \operatorname{rad} V$, and $p + q$ is the rank of any Gram matrix of $B$. Two real quadratic spaces are isometric if and only if they have the same $(p, q, r)$.

## technical
A real quadratic space always has an orthogonal basis in which every basis vector squares to $1$, $-1$ or $0$. How many of each, $(p, q, r)$, is the same for every such basis: this is Sylvester's law of inertia. The number of null basis vectors equals the dimension of the radical, and $p + q$ is the rank of the Gram matrix. The triple $(p, q, r)$ classifies the space up to isometry.

## lay
However you choose perpendicular unit directions in a space, you always find the same number of "space-like", "time-like" and "zero" directions. These three counts are the space's signature, and they are all there is to know about it.

## one-liner
Every real quadratic space has an orthogonal basis squaring to $1, -1, 0$, and the counts $(p, q, r)$ are invariants that classify it up to isometry.
