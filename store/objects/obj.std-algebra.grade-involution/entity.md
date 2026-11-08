---
id: obj.std-algebra.grade-involution
kind: object
version: 2
title: The grade involution
status: defined
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
- name: Claude Opus 5.5
  role: 'maintainer pass, foundation layer'
  version: 2
  source: run 2026-11-08-foundation-layer
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-algebra
founded_on:
- synthesis.continuum-completion-premise@2
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  by: algebra-core-2026-10-26
---

## formal
The \emph{grade involution} $x \mapsto \hat{x}$ of $\Cl(V, Q)$ is $\Cl(-1_V)$, the automorphism extending the isometry $v \mapsto -v$ (\claimref{std-algebra.functoriality}).

## technical
The grade involution is the automorphism of the algebra that flips the sign of every vector. It exists and is unique because $v \mapsto -v$ preserves $Q$.

## lay
The grade involution reverses every arrow. Elements made of an even number of arrows are unchanged; those made of an odd number change sign.

## one-liner
The grade involution $\hat{\cdot}$ is the automorphism extending $v \mapsto -v$.
