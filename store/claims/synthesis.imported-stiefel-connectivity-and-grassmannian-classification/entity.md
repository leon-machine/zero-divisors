---
id: synthesis.imported-stiefel-connectivity-and-grassmannian-classification
kind: claim
version: 1
title: 'Imported: the Stiefel manifold $V_{k}(\R^{m})$ is $(m - k - 1)$-connected, and over a complex of dimension less than $m - k$ rank-$k$ bundles are classified by maps into $\mathrm{Gr}_{k}(\R^{m})$ (Milnor and Stasheff; Husemoller)'
status: imported
region: synthesis
subject: walls
tags: [obstruction-types, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: J. W. Milnor and J. D. Stasheff, Characteristic Classes, Annals of Mathematics Studies 76, Princeton University Press (1974), Section 5.
  key: MilnorStasheff1974
- citation: D. Husemoller, Fibre Bundles, 3rd ed., Graduate Texts in Mathematics 20, Springer (1994), Chapters 3 and 8.
  key: Husemoller1994
- citation: A. Hatcher, Algebraic Topology, Cambridge University Press (2002), Section 4.2.
  key: Hatcher2002
extraction:
  note: >-
    Imported so that the lens-space wall result can pin the two classical inputs of its indefinite
    case, (S) and (G) of its proof, instead of citing them from memory. Cited from memory, not
    checked against the sources (section and chapter numbers included). Clause (ii) follows from (i)
    by the long exact sequences of the fibrations O(k) -> V_k(R^m) -> Gr_k(R^m) and
    O(k) -> V_k(R^infinity) -> Gr_k(R^infinity): the inclusion of Grassmannians is then an
    isomorphism on homotopy groups below degree m - k and onto in that degree, which gives the
    statement on homotopy classes by cellular approximation. Topological statements, flagged as such.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created by the maintainer pass of 2026-10-31 (literature cited from memory by an accepted result; Leon''s list of imports).'
---

## formal
Let $V_{k}(\R^{m})$ be the Stiefel manifold of orthonormal $k$-frames in $\R^{m}$ and $\mathrm{Gr}_{k}(\R^{m})$ the Grassmannian of $k$-planes, with tautological bundle $\gamma_{k}^{m}$.
\begin{enumerate}
\item[(i)] \emph{(Connectivity.)} $V_{k}(\R^{m})$ is $(m - k - 1)$-connected: $\pi_{i}V_{k}(\R^{m}) = 0$ for $i \le m - k - 1$. Hence every map from a CW complex of dimension at most $m - k - 1$ into $V_{k}(\R^{m})$ is null-homotopic.
\item[(ii)] \emph{(Classification in a range.)} If $X$ is a CW complex of dimension less than $m - k$, the map $f \mapsto f^{*}\gamma_{k}^{m}$ is a bijection from homotopy classes of maps $X \to \mathrm{Gr}_{k}(\R^{m})$ onto isomorphism classes of real vector bundles of rank $k$ over $X$ (onto, not necessarily injective, when the dimension equals $m - k$). In particular two rank-$k$ subbundles of the trivial bundle $X \times \R^{m}$ that are isomorphic as bundles are homotopic through subbundles.
\end{enumerate}
\emph{Provenance:} \cite[Section 5]{MilnorStasheff1974}; \cite[Chapters 3 and 8]{Husemoller1994}; \cite[Section 4.2]{Hatcher2002}.

## technical
Frames of $k$ orthonormal vectors in $m$ dimensions form a space with no holes of dimension below $m - k$, so on a small enough complex every family of such frames can be deformed to a constant one. The Grassmannian of $k$-planes classifies rank-$k$ bundles in the same range: over a complex of dimension below $m - k$, two $k$-plane subbundles of a trivial $m$-dimensional bundle can be deformed into each other exactly when they are isomorphic bundles. Both are standard results of bundle theory.

## lay
Two standard facts from topology: a family of frames in a space of many dimensions can always be straightened out over a small enough base, and over such a base the only thing that distinguishes two families of planes is whether they are twisted the same way. The series uses them to show that two ways of filling a wall can be deformed into one another.

## one-liner
$V_{k}(\R^{m})$ is $(m - k - 1)$-connected, and over a complex of dimension below $m - k$ maps into $\mathrm{Gr}_{k}(\R^{m})$ classify rank-$k$ bundles, so isomorphic subbundles of a trivial bundle are homotopic (Milnor and Stasheff; Husemoller).
