---
id: obj.std-algebra.clifford-conjugation
kind: object
version: 1
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
review: typed
trust: ai-proposed
about:
- obj.std-algebra.grade-involution
- obj.std-algebra.reversion
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
extraction:
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
