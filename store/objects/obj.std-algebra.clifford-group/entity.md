---
id: obj.std-algebra.clifford-group
kind: object
version: 1
title: Versors and the Clifford group
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
- obj.std-algebra.clifford-algebra
- obj.std-algebra.grade-involution
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 17 (spin groups and spinor spaces)
  - key: Porteous1995
    locator: the Clifford group, Pin and Spin
extraction:
  by: algebra-core-2026-10-26
---

## formal
The \emph{twisted adjoint action} of an invertible $g \in \Cl(V, Q)$ is $\Ad_g(x) = \hat{g}\, x\, g^{-1}$. The \emph{Clifford group} is
\begin{equation}
\Gamma(V, Q) = \{ g \in \Cl(V, Q) \text{ invertible} : \Ad_g(V) = V \}.
\end{equation}
A \emph{versor} is a product $u_1 \cdots u_k$ of invertible vectors (\claimref{std-algebra.inverse-of-vector}); it is even or odd with $k$. Versors form a subgroup of $\Gamma(V, Q)$, and for a single vector $\Ad_u = s_u$ is the reflection of \claimref{std-algebra.reflection}.

## technical
The twisted adjoint action sends $x$ to $\hat{g} x g^{-1}$; the grade involution on $g$ is what makes a single vector act as a reflection rather than as minus a reflection. The Clifford group consists of the invertible elements whose twisted adjoint action maps vectors to vectors. Products of invertible vectors, the versors, belong to it.

## lay
A versor is a product of invertible arrows. Each such product acts on arrows by sandwiching, and the action is a sequence of mirror reflections, one per factor.

## one-liner
$\Ad_g(x) = \hat{g}xg^{-1}$; the Clifford group is the invertible $g$ with $\Ad_g(V) = V$, and versors (products of invertible vectors) lie in it.
