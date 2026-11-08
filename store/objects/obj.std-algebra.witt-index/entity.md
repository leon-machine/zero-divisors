---
id: obj.std-algebra.witt-index
kind: object
version: 2
title: The Witt index
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- witt-index
- null-directions
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
- name: Claude Opus 5.5
  role: 'maintainer pass, foundation layer'
  version: 2
  source: run 2026-11-08-foundation-layer
review: typed
trust: ai-proposed
about:
- obj.std-algebra.signature
founded_on:
- synthesis.continuum-completion-premise@2
locators:
  sources:
  - key: Lam2005
    locator: Ch. I (hyperbolic planes, the Witt decomposition, Witt's theorems)
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  by: algebra-core-2026-10-26
---

## formal
The \emph{Witt index} of a real quadratic space of signature $(p, q, r)$ is $m = \min(p, q)$, the number of hyperbolic planes in a Witt decomposition (\claimref{std-algebra.witt-decomposition}); it is the Witt index of the nondegenerate quotient $V / \operatorname{rad} V$. For nondegenerate $V$ it is the dimension of every maximal totally null subspace; in general maximal totally null subspaces have dimension $m + r$.

## technical
The Witt index counts the hyperbolic planes in a Witt decomposition, $\min(p, q)$. In a nondegenerate space it is the largest dimension of a subspace on which the form vanishes identically; a radical adds its own dimension to that.

## lay
The Witt index is the number of independent, mutually perpendicular light-like directions a space can hold. Ordinary space-time has Witt index one.

## one-liner
The Witt index of signature $(p, q, r)$ is $\min(p, q)$, the number of hyperbolic planes in a Witt decomposition.
