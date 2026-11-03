---
id: obj.std-algebra.quadratic-space
kind: object
version: 1
title: Real quadratic space
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
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
locators:
  sources:
  - key: Lam2005
    locator: Ch. I and II (quadratic forms; the real case)
extraction:
  by: algebra-core-2026-10-26
---

## formal
A \emph{real quadratic space} $(V, Q)$ is a finite-dimensional real vector space $V$ with a map $Q : V \to \R$ such that $Q(\lambda v) = \lambda^{2} Q(v)$ for all $\lambda \in \R$, $v \in V$, and
\begin{equation}
B(u, v) = \tfrac12\bigl(Q(u + v) - Q(u) - Q(v)\bigr)
\end{equation}
is bilinear. $B$ is the \emph{polar form} of $Q$. The form is not assumed nondegenerate. Vectors $u, v$ are \emph{orthogonal} when $B(u, v) = 0$; a vector $v$ is \emph{null} when $Q(v) = 0$. An \emph{isometry} $f : (V, Q) \to (W, Q')$ is a linear map with $Q'(f v) = Q(v)$ for all $v$.

## technical
A real quadratic space is a finite-dimensional real vector space $V$ together with a quadratic form $Q$: a map with $Q(\lambda v) = \lambda^{2} Q(v)$ whose polarisation $B(u, v) = \tfrac12(Q(u+v) - Q(u) - Q(v))$ is bilinear. $B$ is the polar form. Degenerate forms are allowed: some nonzero vectors may be orthogonal to everything.

Orthogonality, null vectors and isometries are defined through $Q$ and $B$ in the usual way.

## lay
A quadratic space is a space of arrows with a rule that assigns each arrow a number, its "square length". The rule may give negative numbers, as time directions do in relativity, and it may give zero for arrows that are not zero, as light rays do. Everything else in the algebra is built from this one rule.

## one-liner
A real quadratic space is a finite-dimensional real vector space with a quadratic form $Q$, possibly degenerate, whose polar form $B(u,v) = \tfrac12(Q(u+v) - Q(u) - Q(v))$ is bilinear.
