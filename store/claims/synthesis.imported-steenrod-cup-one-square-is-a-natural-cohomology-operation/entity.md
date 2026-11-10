---
id: synthesis.imported-steenrod-cup-one-square-is-a-natural-cohomology-operation
kind: claim
version: 1
title: 'Imported: the cup-one square is a natural cohomology operation (Steenrod)'
status: imported
region: synthesis
subject: walls
tags: [classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-10
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: maintainer pass of 2026-11-10
review: draft
imported_from:
- citation: 'N. E. Steenrod, Products of cocycles and extensions of mappings, Ann. of Math. (2) 48 (1947), 290--320.'
  key: Steenrod1947
  locator: 'the cup-i products and the squaring operations on ordered simplicial complexes; cited from memory, not read'
- citation: 'N. E. Steenrod and D. B. A. Epstein, Cohomology Operations, Annals of Mathematics Studies 50, Princeton University Press, Princeton (1962).'
  key: SteenrodEpstein1962
  locator: 'the construction of the squares on regular cell complexes by equivariant acyclic carriers; cited from memory, not read'
extraction:
  note: >-
    Imported, by decision of 9 November 2026 (decision 6), so that clause (5) of
    synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components can pin the one classical theorem it
    used as the in-statement hypothesis (S) instead of citing it from memory. Clause (iii) is that hypothesis in
    the form the result uses, word for word in its mathematical content; clauses (i) and (ii) are the same
    statement in every degree. NOT checked against the sources: the primary texts were not read, and the
    statement, the bibliographic data (volume, year, pages, series number) and the attribution of each clause are
    cited from memory; the journal, volume and year of the 1947 paper agree with a bibliographic record consulted
    on 9 November 2026. The form stated is not verbatim in either source: the 1947 paper works on ordered
    simplicial complexes, and the 1962 book on regular cell complexes without a deck group. The equivariant form
    follows from the acyclic-carrier construction on regular complexes by carrying the deck group along (closed
    product cells are acyclic and the action is free, so any two carried equivariant systems are equivariantly
    homotopic, and one such system comes from an invariant ordered subdivision); that passage is part of this
    Fact and is not derived in the store. Not part of this Fact: the Cartan formula, the Adem relations, the
    stability of the squares, the cup-i products for i at least two, the classification of maps to a sphere by
    the square of degree two, and any statement about lens spaces. Topological: a statement about cochains of a
    finite cell complex, written in its source's language.
  maintainer_pass:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Created by the maintainer pass of 10 November 2026, by decision 6 of 9 November 2026: Steenrod''s theorem on the cup-one square imported as one Fact, so that the lower bound of five rungs on the definite side of the quarter-turn lens wall of dimension five is a stored theorem given it.'
outside_ga:
  kind: imported
  why: 'A classical theorem of algebraic topology (the cup-one square of a mod-2 cocycle is a natural cohomology operation, computable on a regular cell complex with a free cellular group action), taken from the literature and stated in its source''s language; it has no geometric-algebra form.'
---

## formal
Cohomology is cellular, with coefficients $\Z_{2}$. For a chain complex $C$ write $t$ for the exchange of the two factors of $C \otimes C$. Cited from memory and not checked against the sources:
\begin{enumerate}
\item[(i)] \emph{(The operation.)} For every $k \geq 1$ there is a map $Sq^{k-1} : H^{k}(X; \Z_{2}) \to H^{2k-1}(X; \Z_{2})$, defined for cell complexes $X$ and natural for continuous maps: $f^{*}Sq^{k-1} = Sq^{k-1}f^{*}$ for every continuous $f : X \to X'$.
\item[(ii)] \emph{(Computation from carried equivariant diagonals.)} Let $X = Y/G$ for a finite regular cell complex $Y$ with a free cellular action of a finite group $G$, and let $\Delta_{0}, \Delta_{1}$ be $G$-equivariant maps from the cellular chains of $Y$ to their tensor square, of degrees $0$ and $+1$, carried by closed cells (the value on a cell lies in the tensor square of the chains of its closure), with $\Delta_{0}$ a chain map preserving the augmentation and
\[
\partial\Delta_{1} + \Delta_{1}\partial = \Delta_{0} + t\Delta_{0} \pmod 2 .
\]
For a $G$-invariant mod-2 cochain $a$ put $a \cup_{1} a := (a \otimes a)\Delta_{1}$. Then for every invariant mod-2 cocycle $a$ of degree $k$, $a \cup_{1} a$ is an invariant cocycle and
\[
Sq^{k-1}[a] = [a \cup_{1} a]
\]
in $H^{2k-1}(X; \Z_{2})$, the invariant cochains of $Y$ being the cochains of $X$. In particular the class of $a \cup_{1} a$ does not depend on the choice of the pair $\Delta_{0}, \Delta_{1}$ with these properties.
\item[(iii)] \emph{(The form used in the store; the case $k = 3$ of (i) and (ii), the hypothesis (S).)} There is a map $Sq^{2} : H^{3}(X; \Z_{2}) \to H^{5}(X; \Z_{2})$, defined for cell complexes $X$ and natural for continuous maps, such that when $X = Y/G$ for a finite regular cell complex $Y$ with a free cellular action of a finite group $G$, and $\Delta_{0}, \Delta_{1}$ are $G$-equivariant maps from the cellular chains of $Y$ to their tensor square, carried by closed cells, with $\Delta_{0}$ a chain map preserving the augmentation and $\partial\Delta_{1} + \Delta_{1}\partial = \Delta_{0} + t\Delta_{0}$ modulo $2$, then $Sq^{2}[a] = [a \cup_{1} a]$ for every invariant mod-2 cocycle $a$ of degree $3$.
\end{enumerate}
This is Steenrod's theorem in the form obtained from the acyclic-carrier construction on regular complexes by carrying the deck group along; that passage is part of this Fact and is not derived in the store. Topological statements about a cell complex, flagged as such. \emph{Provenance:} \cite{Steenrod1947} for the cup-one product and the squaring operations; \cite{SteenrodEpstein1962} for the construction on regular cell complexes by acyclic carriers; cited from memory, primary texts not read, section and page numbers not given because they were not verified.

## technical
On the chains of a cell complex the diagonal map is not symmetric: it differs from its transpose by a chain homotopy $\Delta_{1}$, and that homotopy turns a mod-2 cocycle $a$ of degree $k$ into a cocycle $a \cup_{1} a$ of degree $2k - 1$. Steenrod's theorem is that the class of this cocycle depends only on the class of $a$, not on the cell structure or on the choice of diagonal and homotopy, and that it is respected by every continuous map: it is a cohomology operation, the square $Sq^{k-1}$ on classes of degree $k$. The form stated here lets the diagonal and the homotopy be chosen on a covering complex, equivariantly for a free cellular action and carried by closed cells, and then computes the operation on the quotient from invariant cochains. That form is what a finite computation on a cell model of a quotient needs: the quotient of a regular complex is in general not regular, so the classical construction on regular complexes is applied upstairs and the deck group is carried along. The sources state the theorem for ordered simplicial complexes and for regular complexes without a group; the equivariant form follows by the acyclic-carrier argument, since closed product cells are acyclic and the action is free, and that passage is included in the Fact. The store uses the case $k = 3$ on the sphere bundle over the lens space $L^{5}(4)$, where naturality is the step that compares an arbitrary continuous section with a chain-level computation. The statement is cited from memory and has not been checked against the sources.

## lay
When a space is cut into cells, classes of cohomology can be multiplied, and the multiplication is symmetric only up to a correction. In 1947 Steenrod showed that this correction is itself meaningful: applied to a class and itself it gives a new class, the same whichever way the space is cut into cells, and every continuous map between spaces respects it. This is the first of the operations now called Steenrod squares. The collection uses one instance of it, computed on an explicit cell decomposition, to show that a certain map of spheres cannot exist. The theorem is quoted from memory, in a form adapted to spaces obtained by folding a cell complex under a symmetry, and has not been checked against the original texts.

## one-liner
The cup-one square $[a] \mapsto [a \cup_{1} a]$ of a mod-2 class of degree $k$ is a cohomology operation $Sq^{k-1}$, natural for continuous maps, and on a quotient $Y/G$ of a finite regular cell complex by a free cellular action it is computed from any $G$-equivariant diagonal and first higher diagonal carried by closed cells (Steenrod 1947; Steenrod and Epstein 1962; cited from memory, primary texts not read).
