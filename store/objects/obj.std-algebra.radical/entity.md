---
id: obj.std-algebra.radical
kind: object
version: 1
title: Radical of a quadratic space
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
about:
- obj.std-algebra.quadratic-space
locators:
  sources:
  - key: Lam2005
    locator: Ch. I and II (quadratic forms; the real case)
extraction:
  by: algebra-core-2026-10-26
---

## formal
The \emph{radical} of a real quadratic space $(V, Q)$ with polar form $B$ is
\begin{equation}
\operatorname{rad} V = \{ a \in V : B(a, x) = 0 \ \text{for all } x \in V \}.
\end{equation}
$(V, Q)$ is \emph{nondegenerate} when $\operatorname{rad} V = 0$, and \emph{degenerate} otherwise. Every vector of the radical is null.

## technical
The radical of $(V, Q)$ is the subspace of vectors orthogonal to every vector, $\operatorname{rad} V = \{a : B(a, x) = 0 \ \forall x\}$. The space is nondegenerate exactly when the radical is zero. Radical vectors are null, since $Q(a) = B(a, a) = 0$; the converse fails, as a null vector need not be orthogonal to everything.

## lay
The radical collects the directions that the length rule cannot see at all: they have zero length and are perpendicular to every direction. A space with no such directions is called nondegenerate. Degenerate spaces, where such directions exist, are where the Transport Papers do most of their work.

## one-liner
The radical of a quadratic space is the subspace of vectors orthogonal to all vectors; the space is nondegenerate when it is zero.
