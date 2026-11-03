---
id: synthesis.imported-invariant-cone-classification
kind: claim
version: 1
title: 'Imported: the classification of invariant convex cones in simple real Lie algebras'
status: imported
region: synthesis
subject: completion
tags: [representation-theory, classification, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'E. B. Vinberg, Invariant convex cones and orderings in Lie groups, Funct. Anal. Appl. 14 (1980), 1--10.'
  key: Vinberg1980
  doi: 10.1007/BF01078407
- citation: 'S. M. Paneitz, Invariant convex cones and causality in semisimple Lie algebras and groups, J. Funct. Anal. 43 (1981), 313--359.'
  key: Paneitz1981
  doi: 10.1016/0022-1236(81)90021-5
- citation: 'S. M. Paneitz, Determination of invariant convex cones in simple Lie algebras, Ark. Mat. 21 (1983), 217--228.'
  key: Paneitz1983
  doi: 10.1007/BF02384311
- citation: 'G. I. Ol''shanskii, Invariant cones in Lie algebras, Lie semigroups, and the holomorphic discrete series, Funct. Anal. Appl. 15 (1981), 275--285.'
  key: Olshanskii1981
  doi: 10.1007/BF01106156
- citation: 'G. I. Ol''shanskii, Invariant orderings in simple Lie groups. The solution to E. B. Vinberg''s problem, Funct. Anal. Appl. 16 (1982), 311--313.'
  key: Olshanskii1982
  doi: 10.1007/BF01077863
- citation: 'I. E. Segal, Mathematical Cosmology and Extragalactic Astronomy, Academic Press, New York (1976).'
  key: Segal1976
extraction:
  note: >-
    Imported for the result that the spectrum condition selects the sign of the Rule 2 generator,
    which uses the 'only if' direction (a nonzero proper invariant cone forces a nonzero centre of
    the maximal compact subalgebra). The bibliographic data of Vinberg, Paneitz (both papers) and
    Ol'shanskii (both papers) were checked against the Wikipedia article on invariant convex cones
    and the Math-Net.Ru records. The 'only if' direction was checked against secondary statements
    (the existence of a pointed generating invariant cone forces the algebra to be hermitian); the
    converse direction and the attribution to Kostant (through Segal 1976) are cited from memory,
    not checked against the source. The reduction to pointed generating cones in the formal level is
    the elementary argument given there.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass so that the Rule 2 sign result can pin the invariant-cone classification it cited from memory; partly verified (see note).'
---

## formal
Let $\mathfrak{g}$ be a finite-dimensional simple real Lie algebra with Cartan decomposition $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$, $\mathfrak{k}$ a maximal compact subalgebra. Then $\mathfrak{g}$ contains a closed convex cone $W$, invariant under the adjoint group ($e^{\mathrm{ad}X}W = W$ for all $X \in \mathfrak{g}$), with $W \neq \{0\}$ and $W \neq \mathfrak{g}$, if and only if the centre $\mathfrak{z}(\mathfrak{k})$ is nonzero, that is, if and only if $\mathfrak{g}$ is of hermitian type. (For simple $\mathfrak{g}$ such a cone is automatically pointed and generating: $W \cap -W$ and $W - W$ are invariant subspaces, hence ideals, so they are $\{0\}$ and $\mathfrak{g}$.) \emph{Provenance:} Kostant (reported in \cite{Segal1976}); \cite{Vinberg1980, Paneitz1981, Paneitz1983, Olshanskii1981, Olshanskii1982}.

## technical
A simple real Lie algebra admits a nontrivial closed convex cone invariant under its adjoint group exactly when it is of hermitian type, which means that the centre of its maximal compact subalgebra is nonzero (equivalently, the corresponding symmetric space is a bounded symmetric domain). For a simple algebra any nonzero proper invariant closed convex cone is pointed and spans the algebra, because its edge and its span are ideals. The theory was begun by Kostant, Segal and Vinberg; the classification is due to Vinberg, Paneitz and Ol'shanskii.

## lay
In a symmetry algebra, an invariant cone is a set of directions closed under adding and under every symmetry transformation, which picks out a consistent notion of 'positive'. A classical theorem of Lie theory says that a simple symmetry algebra has such a cone, other than the trivial ones, exactly when it contains a special rotation that commutes with all its other rotations. This is a known result taken from the literature.

## one-liner
A simple real Lie algebra contains a closed invariant convex cone other than $\{0\}$ and itself if and only if the centre of its maximal compact subalgebra is nonzero (Kostant, Vinberg, Paneitz, Ol'shanskii).
