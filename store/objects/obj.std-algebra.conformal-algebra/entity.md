---
id: obj.std-algebra.conformal-algebra
kind: object
version: 1
title: The conformal algebra
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- conformal-model
- hyperbolic-plane
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
- obj.std-algebra.signature
locators:
  sources:
  - key: DoranLasenby2003
    locator: 'Ch. 10 (geometry: the conformal model)'
extraction:
  by: algebra-core-2026-10-26
---

## formal
For a nondegenerate real quadratic space $(V, Q)$ of signature $(p, q)$, the \emph{conformal space} is $V \perp H$ with $H$ a hyperbolic plane spanned by null vectors $n_0, n_\infty$ with $B(n_0, n_\infty) = -1$; it has signature $(p+1, q+1)$, and $\Cl(p+1, q+1)$ is the \emph{conformal algebra} of $V$. The \emph{conformal embedding} of points is $X(x) = n_0 + x + \tfrac12 Q(x)\, n_\infty$ for $x \in V$. The cases used in the store are $\Cl(4,1)$, the conformal algebra of Euclidean three-space, and $\Cl(2,4)$, the conformal algebra of spacetime $\R^{1,3}$.

## technical
The conformal algebra of a space adds one positive and one negative direction, written through two null vectors: the origin $n_0$ and the point at infinity $n_\infty$. A point $x$ is represented by the null vector $n_0 + x + \tfrac12 Q(x) n_\infty$. For spacetime this gives $\Cl(2,4)$, whose even part carries the twistors used in the series.

## lay
The conformal algebra adds two extra directions, one for the origin and one for "infinity". Points become special arrows of zero length, and spheres, planes and their transformations become simple elements of the algebra.

## one-liner
The conformal algebra of $\R^{p,q}$ is $\Cl(p+1,q+1)$, with null $n_0, n_\infty$ ($B(n_0,n_\infty) = -1$) and points $X(x) = n_0 + x + \tfrac12 Q(x)\,n_\infty$; $\Cl(2,4)$ for spacetime.
