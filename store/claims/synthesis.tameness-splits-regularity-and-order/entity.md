---
id: synthesis.tameness-splits-regularity-and-order
kind: claim
version: 3
title: Tameness splits into a regularity clause and an order clause; the one-sided completion needs no order and the wall iteration only finite order
status: proved
region: synthesis
subject: walls
tags: [degenerate-algebras, tameness]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.determinant-identity-blow-up-expansion@3
  - sheaf.invariant-form-t3@2
  - std-algebra.sylvester-inertia@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_jacobi_corank_one_simple_zero
- kind: check
  ref: check.py::check_wild_wall_completion_and_shadow
- kind: check
  ref: check.py::check_even_order_keeps_signature
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - sheaf.tameness
  - sheaf.one-sided-completion
  - sheaf.tame-wall-induction
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.sylvester-inertia where the proof uses them. Version 2 -> 3.'
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the one-liner now names the hypotheses (T1), (T2) and compactness under which the completion clause holds. Version 1 -> 2.'
  open_problem: pr.tameness
  note: >-
    Answers the premise target on tameness by splitting it. Clause (T3) is the only clause with
    content beyond the definition of a corank-one wall, and the result locates exactly which consumers
    need it: the simple pole of the inverse form and the exceptional algebra (and what is built on
    them) need first order; the one-sided completion needs no order condition at all; the wall
    iteration needs only finite order of the first wall, the shadow walls being first order
    automatically; two-sidedness needs only that the signature changes. The genericity question
    (transverse corank-two points, their three signatures and their stability) is treated in the result
    filed alongside, synthesis.transverse-corank-two-walls-are-wild, and is not repeated here. Transport-absent: symmetric bilinear algebra on bundles. The
    proof deliberately avoids citing store results that assume tameness, re-running the needed
    steps of the completion and induction proofs instead.
---

## formal
Let $G$ be a smooth symmetric form on $T^*M$ and $\Sig$ its degeneracy locus. In a local frame $(k, m_1, \dots, m_{n-1})$ along a transversal with parameter $\tau$, $\Sig = \{\tau = 0\}$, write the Gram matrix as $\begin{psmallmatrix} \lambda & b^{\mathsf T} \\ b & G_1 \end{psmallmatrix}$ with $G_1$ invertible near $\Sig$ and $k$ spanning the radical on $\Sig$ (so $\lambda = b = 0$ there), and let $S := \lambda - b^{\mathsf T} G_1^{-1} b = \det G / \det G_1$ be the Schur complement.
\begin{enumerate}
\item \emph{(Regularity.)} At a point of $\Sig$ of corank one, $d(\det G) = \det G_1 \cdot \delta(k \otimes k)$, with $\delta$ the transversality datum of Lemma \claimref{sheaf.invariant-form-t3}; at a point of corank at least two, $d(\det G) = 0$. Hence (T1)-(T3) of the tameness hypothesis hold along $\Sig$ if and only if, in some (equivalently every) local frame, $\det G$ vanishes exactly on $\Sig$ with nonzero differential there: tameness is the statement that the degeneracy locus is the regular zero set of $\det G$, and (T3) is the statement that $S$ vanishes to first order. (At a point of corank at least two the zero of $\det G$ is therefore never simple; the behaviour of transverse corank-two points is the subject of the result filed alongside, synthesis.transverse-corank-two-walls-are-wild.)
\item \emph{(Completion without (T3).)} Assume (T1) and (T2), $\Sig$ compact, $w_1(\shL) = 0$, and that $S > 0$ on the physical side $\Mp$, of signature $(p,q)$. Then for $s := G^{-1}(e,e)$ of the collar data, exactly,
\[
s \;=\; \frac{(1 - c)^2}{S} + B, \qquad c := b^{\mathsf T} G_1^{-1} e', \quad B := e'^{\mathsf T} G_1^{-1} e',
\]
with $e = (1, e')$ in the dual frame, $c$ and $B$ smooth up to the wall and $c = 0$ on $\Sig$; and the ambient form $h$ of the one-sided completion is nondegenerate of signature $(p{+}1, q{+}1)$ on all of $\Mp$, including $\Sig$. No order of vanishing of $S$ is used.
\item \emph{(Finite order.)} If moreover $S = \tau^m u$ with $m \geq 1$ finite and $u$ nowhere zero on $\Sig$, then for odd $m$ and good couplings the far-side degeneration of $h$ lies on a shadow wall $\Sig'$ across which $\det h$ has a simple zero, so $(T, h)$ is a tame corank-one degeneration along $\Sig'$ whatever $m$ is; for even $m$ the signature does not change across $\Sig$ and $h$ is nondegenerate on a whole neighbourhood of $\Sig$.
\item \emph{(Two sides.)} A wall across which the signature changes is two-sided, with or without (T3); at even order a one-sided wall carrying a corank-one degeneration exists.
\end{enumerate}
In particular the wild wall with $S = \tau^3$ violates (T3) and is completed by one rung, and its shadow wall is first order; what fails there is the simple pole of $G^{-1}$, which has order three.

## technical
Tameness is three clauses: (T1) the wall is a smooth closed hypersurface, (T2) the corank is exactly one with a smooth radical line bundle, (T3) the degeneration is first order. Write the Gram matrix along a transversal in a frame whose first vector spans the radical on the wall, and let $S$ be the Schur complement of the nondegenerate block, the dying eigenvalue up to a positive factor. By Jacobi's formula the differential of $\det G$ on the wall is the determinant of the nondegenerate block times the transversality datum at corank one, and zero at higher corank. So the three clauses together say exactly that the wall is the regular zero set of $\det G$, and (T3) says $S$ vanishes to first order. Whether tameness is generic, which turns on transverse corank-two points, is not addressed here (filed alongside, synthesis.transverse-corank-two-walls-are-wild).

The consumers use (T3) unevenly. The one-sided completion needs none of it: the exact identity $s = (1-c)^2/S + B$ replaces the expansion $s = 1/\lambda + O(1)$, and $s \to +\infty$ on the physical side whatever the order of vanishing. The wall iteration needs only finite order: the monotone zone exists because $s'$ is dominated by $-N S'/S^2$, and every shadow wall is then a simple zero of $\det h$, so the walls from the second on are tame automatically. Two-sidedness needs only that the signature changes. The canonical simple pole of $G^{-1}$, the identification of the conormal bundle with the square of the dying line, and the exceptional algebra of the normal-cone deformation do use first order in their stated proofs: at order $m$ the pole has order $m$. This consumer reading is an audit of the stated proofs, not a theorem.

## lay
The series assumes that wherever its geometry degenerates, it does so in the tamest possible way: along a smooth wall, one direction at a time, with the dying length shrinking at a steady linear rate. This result takes that assumption apart. The first part says that it is the same as asking that a single number built from the geometry crosses zero cleanly. The linear-rate part is not needed for the main repair the series performs at a wall: a wall where the length dies like the cube of the distance is repaired by the same construction, and the next walls the repair creates are clean ones. What does use the linear rate, as the series' proofs are written, is the precise form of the blow-up of the inverse metric at the wall and the limiting algebra built from it.

## one-liner
Tameness is the regularity of the zero set of $\det G$, with its first-order clause (T3) equivalent to a simple zero of the Schur complement; assuming (T1) and (T2) with a compact wall, the one-sided completion holds without (T3), the wall iteration needs only finite order (its shadow walls are first order automatically), and signature-changing walls are two-sided without (T3).
