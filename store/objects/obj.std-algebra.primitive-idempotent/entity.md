---
id: obj.std-algebra.primitive-idempotent
kind: object
version: 1
title: Idempotents and primitive idempotents
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- idempotents
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
locators:
  sources:
  - key: Lam1999
    locator: matrix rings, idempotents and Morita theory
  - key: Lounesto2001
    locator: Ch. 17 (spin groups and spinor spaces)
extraction:
  by: algebra-core-2026-10-26
---

## formal
In a unital real algebra $A$, an \emph{idempotent} is an element $e$ with $e^{2} = e$. Idempotents $e, f$ are \emph{orthogonal} when $ef = fe = 0$; then $e + f$ is an idempotent. A nonzero idempotent is \emph{primitive} when it is not the sum of two nonzero orthogonal idempotents; equivalently, $0$ and $e$ are the only idempotents of the corner algebra $eAe$. A \emph{complete system} is a family of mutually orthogonal idempotents summing to $1$.

## technical
An idempotent is an element equal to its own square, such as a projection. Two are orthogonal when both products vanish. A primitive idempotent cannot be split further into two orthogonal nonzero pieces, which is the same as saying its corner algebra $eAe$ has no idempotents besides $0$ and $e$. In a Clifford algebra, $\tfrac12(1 + u)$ is an idempotent for every $u$ with $u^{2} = 1$.

## lay
An idempotent is an element that does nothing new when applied twice, like a projection onto a subspace. Primitive ones are the smallest such projections, and they are used to cut the algebra down to its spinors.

## one-liner
An idempotent satisfies $e^{2} = e$; it is primitive when it is nonzero and not a sum of two nonzero orthogonal idempotents.
