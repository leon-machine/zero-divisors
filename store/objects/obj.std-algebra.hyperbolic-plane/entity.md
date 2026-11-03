---
id: obj.std-algebra.hyperbolic-plane
kind: object
version: 1
title: Hyperbolic planes and hyperbolic pairs
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- hyperbolic-plane
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
review: typed
trust: ai-proposed
about:
- obj.std-algebra.quadratic-space
- obj.std-algebra.radical
locators:
  sources:
  - key: Lam2005
    locator: Ch. I (hyperbolic planes, the Witt decomposition, Witt's theorems)
extraction:
  by: algebra-core-2026-10-26
---

## formal
A \emph{hyperbolic plane} is a nondegenerate real quadratic space $H$ of dimension $2$ that contains a nonzero null vector. A \emph{hyperbolic pair} in a quadratic space is a pair $(u, w)$ of null vectors with $B(u, w) = \tfrac12$, equivalently
\begin{equation}
u w + w u = 1
\end{equation}
in the Clifford algebra. By \claimref{std-algebra.witt-decomposition}, every hyperbolic plane is spanned by a hyperbolic pair, and every hyperbolic plane is isometric to $\R^{1,1}$: with $e = u + w$ and $f = u - w$ one has $Q(e) = 1$, $Q(f) = -1$ and $B(e, f) = 0$.

## technical
A hyperbolic plane is a nondegenerate plane containing a null direction. Such a plane always has a basis of two null vectors $u$, $w$ normalised so that $uw + wu = 1$, a hyperbolic pair, and it is the plane $\R^{1,1}$ in disguise: $u + w$ squares to $1$ and $u - w$ to $-1$. This is the normalisation used throughout the series (for example in \claimref{primer.splitting-along-hyperbolic-plane}).

## lay
A hyperbolic plane is the simplest piece of space-time: one direction of space and one of time. Its two light-like directions, which have zero length, can be scaled so that they multiply together to give one. Every space with both space-like and time-like directions is built from such planes plus a part that is all space or all time.

## one-liner
A hyperbolic plane is a nondegenerate plane with a null vector; it is spanned by a hyperbolic pair $u, w$ of null vectors with $uw + wu = 1$, and is isometric to $\R^{1,1}$.
