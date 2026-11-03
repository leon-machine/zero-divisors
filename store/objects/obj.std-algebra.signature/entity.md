---
id: obj.std-algebra.signature
kind: object
version: 1
title: Signature, and the spaces R^{p,q,r}
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- clifford-classification
- degenerate-algebras
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
locators:
  sources:
  - key: Lam2005
    locator: Ch. I and II (quadratic forms; the real case)
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
The \emph{signature} of a real quadratic space is the triple $(p, q, r)$ of the law of inertia, \claimref{std-algebra.sylvester-inertia}. $\R^{p,q,r}$ denotes $\R^{p+q+r}$ with the standard basis orthogonal and $Q(e_i) = 1$ for $i \le p$, $Q(e_i) = -1$ for $p < i \le p+q$, and $Q(e_i) = 0$ for the last $r$. We write $\R^{p,q} = \R^{p,q,0}$ and $n = p + q + r$. Every real quadratic space of signature $(p, q, r)$ is isometric to $\R^{p,q,r}$.

## technical
The signature $(p, q, r)$ counts the basis vectors squaring to $+1$, $-1$ and $0$ in any orthogonal basis; it is well defined by the law of inertia. The model space $\R^{p,q,r}$ has an orthonormal standard basis with $p$ positive, $q$ negative and $r$ null generators, in that order, and represents every space of that signature.

## lay
The signature is the triple of counts: how many directions square to plus one, to minus one, and to zero. Ordinary space is $(3, 0, 0)$; spacetime in the convention used here is $(1, 3, 0)$.

## one-liner
The signature $(p, q, r)$ counts positive, negative and null directions in an orthogonal basis; $\R^{p,q,r}$ is the standard model of each signature.
