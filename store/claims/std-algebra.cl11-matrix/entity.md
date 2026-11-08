---
id: std-algebra.cl11-matrix
kind: claim
version: 2
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
- name: Claude Opus 5.5
  role: 'GA rewrite (the isomorphism stated by matrix units inside the algebra)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
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
  - std-algebra.witt-decomposition@2
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
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. The formal level now states the isomorphism inside the algebra: uw, u, w, wu (and 1/2(1 +- e_1), 1/2(e_2 +- e_1e_2) for Cl(2,0)) are a complete set of 2 x 2 matrix units of the Clifford algebra; the matrices stay as a labelled reading. Both matrix-unit tables were verified exactly with lib/GA.py (Cl(1,1) with u = (e + f)/2, w = (e - f)/2, and Cl(2,0)). Declared outside_ga (bridge): the result identifies the Clifford algebra with a matrix algebra.'
  by: algebra-core-2026-10-26
outside_ga:
  kind: bridge
  why: 'the result identifies the Clifford algebra of a hyperbolic plane (and of the Euclidean plane) with the matrix algebra Mat_2(R); the geometric-algebra side is stated by the matrix units uw, u, w, wu inside the algebra, and the matrices are their labelled reading'
---

## formal
The Clifford algebra of any hyperbolic plane $H$ is isomorphic to $\Mat_2(\R)$: if $(u, w)$ is a hyperbolic pair spanning $H$ ($Q(u) = Q(w) = 0$, $uw + wu = 1$), the four elements
\[
\epsilon_{11} = uw, \qquad \epsilon_{12} = u, \qquad \epsilon_{21} = w, \qquad \epsilon_{22} = wu
\]
of $\Cl(H)$ are a complete set of $2 \times 2$ matrix units, $\epsilon_{ij}\epsilon_{kl} = \delta_{jk}\,\epsilon_{il}$ and $\epsilon_{11} + \epsilon_{22} = 1$, and they span $\Cl(H)$; so $x = \sum_{ij} x_{ij}\,\epsilon_{ij} \mapsto (x_{ij})$ is an isomorphism $\Cl(H) \to \Mat_2(\R)$, under which (as a labelled reading)
\begin{equation}
u \mapsto \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad w \mapsto \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix},
\end{equation}
and the complementary idempotents $uw$, $wu$ are $\operatorname{diag}(1, 0)$ and $\operatorname{diag}(0, 1)$. In particular $\Cl(1,1) \cong \Mat_2(\R)$. Also $\Cl(2,0) \cong \Mat_2(\R)$: the elements $\tfrac12(1 + e_1)$, $\tfrac12(e_2 + e_1e_2)$, $\tfrac12(e_2 - e_1e_2)$, $\tfrac12(1 - e_1)$ are matrix units in the same sense, under which $e_1 \mapsto \operatorname{diag}(1, -1)$ and $e_2 \mapsto \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}$.

## technical
The algebra of a hyperbolic plane is the algebra of real $2 \times 2$ matrices, because it contains its own matrix units: the two null vectors of a hyperbolic pair are the two off-diagonal units, and their two products are the two diagonal idempotents, summing to $1$. The Euclidean plane algebra $\Cl(2,0)$ is the same matrix algebra by a different choice of generators. These are the base cases of the periodicity theorem.

## lay
The algebra of one space and one time direction is exactly the familiar algebra of two-by-two real matrices. The light-like directions become the matrices that move one coordinate into the other.

## one-liner
$\Cl(H) \cong \Mat_2(\R)$ for a hyperbolic plane, since $uw, u, w, wu$ are matrix units of $\Cl(H)$ for a hyperbolic pair $(u, w)$; also $\Cl(2,0) \cong \Mat_2(\R)$.
