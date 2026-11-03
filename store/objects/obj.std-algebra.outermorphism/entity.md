---
id: obj.std-algebra.outermorphism
kind: object
version: 1
title: The outermorphism of a linear map
status: defined
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
- obj.std-algebra.outer-product
locators:
  sources:
  - key: HestenesSobczyk1984
    locator: Ch. 3 (linear and multilinear functions)
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
For a linear map $f : V \to W$ between real quadratic spaces, its \emph{outermorphism} $\underline{f} : \Cl(V, Q) \to \Cl(W, Q')$ is the unique linear map with $\underline{f}(1) = 1$, $\underline{f}(v) = f(v)$ and $\underline{f}(X \wedge Y) = \underline{f}(X) \wedge \underline{f}(Y)$; through \claimref{std-algebra.exterior-isomorphism} it is $\Lambda f$. So $\underline{f}(v_1 \wedge \dots \wedge v_k) = f(v_1) \wedge \dots \wedge f(v_k)$, and $\underline{f}$ preserves grade. $f$ need not be an isometry.

## technical
Any linear map of vectors extends uniquely to a grade-preserving map of the whole algebra that respects the outer product: apply it to each factor of a blade. This is the outermorphism. Unlike the algebra homomorphism of an isometry, it is defined for every linear map, and it ignores the geometric product.

## lay
A linear map moves arrows. Its outermorphism moves planes, volumes and every other blade along with them, by moving each spanning arrow.

## one-liner
The outermorphism $\underline{f}$ of a linear map $f$ is the grade-preserving extension respecting $\wedge$: $\underline{f}(v_1 \wedge \dots \wedge v_k) = f v_1 \wedge \dots \wedge f v_k$.
