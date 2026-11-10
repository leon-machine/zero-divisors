---
id: synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory
kind: claim
version: 1
title: 'Imported: the Atiyah-Hirzebruch filtration of complex K-theory'
status: imported
region: synthesis
subject: walls
tags: [classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-09
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: maintainer pass of 2026-11-09
review: draft
imported_from:
- citation: 'M. F. Atiyah and F. Hirzebruch, Vector bundles and homogeneous spaces, Proc. Sympos. Pure Math. 3, Amer. Math. Soc. (1961), 7--38.'
  key: AtiyahHirzebruch1961
- citation: 'M. F. Atiyah, K-Theory, W. A. Benjamin, New York (1967).'
  key: Atiyah1967
extraction:
  note: >-
    Imported, by decision of 9 November 2026, so that the K-ring clause of
    synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure can pin the general
    K-theory fact it used as the in-statement hypothesis (AH) instead of citing it from memory. Stated generally;
    clause (iv) is the form that result uses. NOT checked against the sources: the statement, the bibliographic
    data (volume, pages, publisher) and the attribution of each clause are cited from memory. Clauses (i) to (iii)
    are the literature's; clause (iv) is an immediate consequence of (ii), with the short argument given in the
    technical level. The lambda-operations of K-theory are not part of this Fact, and neither is any statement
    about lens spaces. Topological: a statement about bundles over a finite complex, written in its source's
    language.
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Created by the maintainer pass of 9 November 2026 (second pass), by decision: the Atiyah-Hirzebruch filtration imported as one general K-theory Fact, so that the K-ring of the quarter-turn lens spaces is a stored theorem given it.'
outside_ga:
  kind: imported
  why: 'A classical theorem of algebraic topology (the skeletal filtration of the ring of stable classes of complex vector bundles and its spectral sequence), taken from the literature and stated in its source''s language; it has no geometric-algebra form.'
---

## formal
Let $X$ be a finite CW complex with skeleta $X^{p}$ and $K(X)$ its complex K-theory: the ring of stable classes of complex vector bundles over $X$, commutative under the tensor product. Cited from memory and not checked against the sources:
\begin{enumerate}
\item[(i)] \emph{(The filtration.)} The subgroups $F^{p} := \ker\bigl(K(X) \to K(X^{p-1})\bigr)$, the classes that vanish on the $(p-1)$-skeleton, form a decreasing filtration of $K(X)$ by ideals, $K(X) = F^{0} \supseteq F^{1} \supseteq \cdots$, with $F^{p} = 0$ for $p > \dim X$, and it is multiplicative: $F^{p}F^{q} \subseteq F^{p+q}$.
\item[(ii)] \emph{(The spectral sequence.)} There is a spectral sequence with $E_{2}^{p,q} = H^{p}(X; K^{q}(\mathrm{pt}))$, where $K^{q}(\mathrm{pt})$ is $\Z$ for $q$ even and $0$ for $q$ odd, converging to $K^{*}(X)$, with $E_{\infty}^{p,-p} \cong F^{p}/F^{p+1}$. It is multiplicative: the product on $E_{2}$ is the cup product (up to the sign convention) and the product on $E_{\infty}$ is the one induced by $K(X)$. Every differential has finite order (the sequence collapses after tensoring with $\Q$). In particular $F^{2r-1} = F^{2r}$ and $F^{2r}/F^{2r+2}$ is a subquotient of $H^{2r}(X; \Z)$.
\item[(iii)] \emph{(Line bundles.)} For a complex line bundle $\ell$ over $X$ the class $\ell - 1$ lies in $F^{2}$, and its image in $F^{2}/F^{4}$, a subgroup of $H^{2}(X; \Z)$, is the first Chern class $c_{1}(\ell)$, which is the Euler class of the underlying oriented plane bundle.
\item[(iv)] \emph{(The form used in the store; a consequence of (ii).)} If $H^{\mathrm{odd}}(X; \Z)$ is zero, or is torsion-free and concentrated in the degree $\dim X$, then no differential enters or leaves the groups $E_{r}^{2r', -2r'}$, so $F^{2r}/F^{2r+2} \cong H^{2r}(X; \Z)$ for every $r$, compatibly with products: the product $F^{2r}/F^{2r+2} \times F^{2s}/F^{2s+2} \to F^{2r+2s}/F^{2r+2s+2}$ induced by $K(X)$ is the cup product, and for connected $X$ the order of the reduced group $F^{1}$ is the product of the orders of the groups $H^{2r}(X; \Z)$, $r \geq 1$, when these are finite.
\end{enumerate}
Topological statements about bundles over the space, flagged as such. \emph{Provenance:} \cite{AtiyahHirzebruch1961} for the filtration and the spectral sequence, \cite{Atiyah1967} for K-theory as a ring; cited from memory, section and page numbers not given because they were not verified.

## technical
Complex K-theory of a finite cell complex is filtered by how far out on the skeleta a class first becomes nonzero. The filtration is compatible with the ring structure, and its successive quotients are computed by a spectral sequence that starts from the ordinary integral cohomology of the space, placed in every even row. The differentials of this sequence are torsion operations, so they vanish wherever they would have to map into a torsion-free group. That gives clause (iv) by induction on the page. A differential leaving a group of total degree zero lands in a subgroup of an odd cohomology group, which is torsion-free by hypothesis, so it vanishes; a differential entering such a group starts from an odd cohomology group, which by hypothesis is zero unless its degree is the dimension of the space, and from there the target lies above the dimension and is zero. So the even cohomology survives unchanged, and the quotients of the filtration are the even integral cohomology groups, with the ring structure of K-theory inducing the cup product on them. A line bundle minus the trivial line sits in the second step of the filtration, with leading term its first Chern class. The store uses the statement in this form to obtain the K-ring of the quarter-turn lens spaces from their integral cohomology ring by a count of orders, with no extension problem to solve. The statement is cited from memory and has not been checked against the sources.

## lay
K-theory is a way of adding and multiplying families of planes over a space, and it sees twisting that ordinary invariants can miss. This classical theorem says how K-theory is built up from the more familiar cohomology of the space, layer by layer, as one moves outward through the cells the space is made of. When the space has no awkward odd-dimensional cohomology, the layers of K-theory are exactly the even-dimensional cohomology groups, and multiplying in K-theory matches multiplying there. The collection uses it to turn a computed cohomology ring into a K-theory ring. It is quoted from memory and has not been checked against the original papers.

## one-liner
Complex K-theory of a finite complex has a multiplicative skeletal filtration whose quotients are computed by a spectral sequence from $H^{*}(X; \Z)$ with torsion differentials; when the odd integral cohomology is zero, or torsion-free in the top degree only, $F^{2r}/F^{2r+2} \cong H^{2r}(X; \Z)$ compatibly with products, and a line bundle $\ell$ has $\ell - 1 \in F^{2}$ with leading term $c_{1}(\ell)$ (Atiyah and Hirzebruch 1961; cited from memory).
