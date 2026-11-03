---
id: obj.std-algebra.spacetime-algebra
kind: object
version: 1
title: The spacetime algebra
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- dictionaries
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
    locator: Ch. 5 (relativity and spacetime)
extraction:
  by: algebra-core-2026-10-26
---

## formal
The \emph{spacetime algebra} is $\Cl(1,3)$, the Clifford algebra of Minkowski space in signature $(+,-,-,-)$, with orthonormal basis $\gamma_0, \gamma_1, \gamma_2, \gamma_3$: $\gamma_0^{2} = 1$, $\gamma_k^{2} = -1$ for $k = 1, 2, 3$. Its pseudoscalar is $I = \gamma_0 \gamma_1 \gamma_2 \gamma_3$. For the observer with velocity $\gamma_0$, the \emph{spacetime split} assigns to $\gamma_k$ the \emph{relative vector} $\sigma_k = \gamma_k \gamma_0$, a bivector of $\Cl(1,3)$.

## technical
The spacetime algebra is the Clifford algebra of Minkowski space with one positive and three negative directions, the store's convention. A frame $\gamma_\mu$ is the GA form of the Dirac matrices, but here the $\gamma_\mu$ are vectors, not matrices. An observer's time direction $\gamma_0$ turns each spatial vector into the bivector $\gamma_k \gamma_0$, which behaves as a vector of that observer's space.

## lay
The spacetime algebra is the algebra of arrows in spacetime, one time direction and three space directions. An observer moving along the time direction sees space as the planes made by space directions with their own time direction.

## one-liner
The spacetime algebra is $\Cl(1,3)$ with frame $\gamma_\mu$ ($\gamma_0^{2} = 1$, $\gamma_k^{2} = -1$), pseudoscalar $I = \gamma_0\gamma_1\gamma_2\gamma_3$ and relative vectors $\sigma_k = \gamma_k\gamma_0$.
