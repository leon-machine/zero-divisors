---
id: obj.std-algebra.clifford-conjugation
kind: object
version: 2
title: Clifford conjugation
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
- obj.std-algebra.grade-involution
- obj.std-algebra.reversion
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
\emph{Clifford conjugation} is $\bar{x} = \hat{\tilde{x}}$, the anti-automorphism with $\bar{v} = -v$ for $v \in V$.

## technical
Clifford conjugation composes reversion with the grade involution. It is an anti-automorphism that negates vectors.

## lay
Clifford conjugation reverses the order of products and also reverses every arrow, in the way that complex conjugation reverses the imaginary unit.

## one-liner
Clifford conjugation $\bar{x} = \hat{\tilde{x}}$ is the anti-automorphism negating vectors.
