---
id: std-algebra.cl11-matrix
kind: claim
version: 1
title: Cl(1,1) and Cl(2,0) are the real 2x2 matrices
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- hyperbolic-plane
- clifford-classification
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
- obj.std-algebra.hyperbolic-plane
- obj.std-algebra.clifford-algebra
derivations:
- name: main
  uses:
  - std-algebra.existence-uniqueness@1
  - std-algebra.blade-basis@1
  - std-algebra.witt-decomposition@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_hyperbolic_plane_is_m2r
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 16 (matrix representations and periodicity of 8)
  - key: Lam2005
    locator: 'Ch. V (Clifford algebras: the tensor product rules)'
extraction:
  by: algebra-core-2026-10-26
---

## formal
The Clifford algebra of any hyperbolic plane $H$ is isomorphic to $\Mat_2(\R)$: if $(u, w)$ is a hyperbolic pair spanning $H$, the assignment
\begin{equation}
u \mapsto \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad w \mapsto \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}
\end{equation}
extends to an isomorphism $\Cl(H) \to \Mat_2(\R)$, under which $uw$ and $wu$ are the complementary idempotents $\operatorname{diag}(1, 0)$ and $\operatorname{diag}(0, 1)$. In particular $\Cl(1,1) \cong \Mat_2(\R)$. Also $\Cl(2,0) \cong \Mat_2(\R)$, by $e_1 \mapsto \operatorname{diag}(1, -1)$, $e_2 \mapsto \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}$.

## technical
The algebra of a hyperbolic plane is the algebra of real $2 \times 2$ matrices. The two null vectors of a hyperbolic pair become the two off-diagonal matrix units, and their two products become the two diagonal idempotents. The Euclidean plane algebra $\Cl(2,0)$ is the same matrix algebra by a different choice of generators. These are the base cases of the periodicity theorem.

## lay
The algebra of one space and one time direction is exactly the familiar algebra of two-by-two real matrices. The light-like directions become the matrices that move one coordinate into the other.

## one-liner
$\Cl(H) \cong \Mat_2(\R)$ for a hyperbolic plane, with a hyperbolic pair going to the off-diagonal matrix units; also $\Cl(2,0) \cong \Mat_2(\R)$.
