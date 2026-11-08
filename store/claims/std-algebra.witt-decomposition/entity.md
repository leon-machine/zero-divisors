---
id: std-algebra.witt-decomposition
kind: claim
version: 2
title: Hyperbolic pairs and the Witt decomposition
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- hyperbolic-plane
- witt-index
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
- name: Claude Opus 5.5
  role: 'maintainer pass, citation of the retired imported Fact repointed to its derivation in geometric algebra'
  version: 2
  source: run 2026-11-07-bit-root
review: typed
trust: ai-proposed
about:
- obj.std-algebra.hyperbolic-plane
- obj.std-algebra.radical
derivations:
- name: main
  uses:
  - synthesis.completion-recovers-the-real-clifford-algebras@1
  - std-algebra.polarisation@1
  - std-algebra.vector-squares@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_hyperbolic_partner_in_a_plane
- kind: check
  ref: check.py::check_witt_decomposition_and_maximal_null_subspace
locators:
  sources:
  - key: Lam2005
    locator: Ch. I (hyperbolic planes, the Witt decomposition, Witt's theorems)
extraction:
  maintainer_pass_2026_11_08:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 7 November 2026: the imported Fact std-algebra.sylvester-inertia is retired, replaced by synthesis.completion-recovers-the-real-clifford-algebras, whose clause (iii) derives Sylvester's law of inertia in geometric algebra over any Euclidean field, the reals included; the citation and edge now point there. The check's premise() call names the new result; nothing else changed.
  by: algebra-core-2026-10-26
---

## formal
Let $(V, Q)$ be a real quadratic space of signature $(p, q, r)$ and let $m = \min(p, q)$.
\begin{enumerate}
\item[(i)] If $P \subseteq V$ is a nondegenerate plane and $u \in P$ is a nonzero null vector, there is a unique $w \in P$ such that $(u, w)$ is a hyperbolic pair; $P$ is a hyperbolic plane.
\item[(ii)] (Witt decomposition) There is an orthogonal decomposition
\begin{equation}
V = H_1 \perp \dots \perp H_m \perp A \perp \operatorname{rad} V
\end{equation}
with each $H_i$ a hyperbolic plane and $A$ anisotropic ($Q(a) \ne 0$ for $a \ne 0$, hence definite, of signature $(p - m, q - m, 0)$).
\item[(iii)] If $(u_i, w_i)$ is a hyperbolic pair spanning $H_i$, then $N = \operatorname{span}(u_1, \dots, u_m) \oplus \operatorname{rad} V$ is a maximal totally null subspace, and every totally null subspace has dimension at most $m + r$.
\end{enumerate}

## technical
In a nondegenerate plane, a null vector $u$ has exactly one partner $w$ with $uw + wu = 1$, so the plane is hyperbolic. Globally, a real quadratic space splits orthogonally into $\min(p, q)$ hyperbolic planes, a definite remainder and the radical. Taking one null vector from each hyperbolic plane, together with the radical, gives a totally null subspace of the largest possible dimension, $\min(p, q) + r$.

## lay
Any space with both space-like and time-like directions can be cut into perpendicular copies of the simplest space-time plane, plus a leftover piece that is purely space-like or purely time-like, plus the directions the length rule cannot see. The number of space-time planes, the smaller of the two counts, is the largest number of independent mutually perpendicular light-like directions the space can hold.

## one-liner
A null vector in a nondegenerate plane has a unique hyperbolic partner, and $V = H_1 \perp \dots \perp H_{\min(p,q)} \perp A \perp \operatorname{rad} V$ with $A$ definite; maximal totally null subspaces have dimension $\min(p,q) + r$.
