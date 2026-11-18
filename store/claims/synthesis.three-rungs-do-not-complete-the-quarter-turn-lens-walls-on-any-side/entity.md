---
id: synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side
kind: claim
version: 1
title: 'Three rungs fail on quarter-turn lens walls from dimension five (five given spin class)'
status: proved
region: synthesis
subject: walls
tags: [degenerate-algebras, tameness, hyperbolic-plane, no-go]
proposed_by:
  kind: ai
  session: 2026-11-09-bridges
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-bridges
review: draft
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - synthesis.wall-rung-count-is-height-of-dying-line-class@2
  - synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial@2
  - synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height@2
  - synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure@1
  - synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory@1
  - synthesis.imported-whitney-product-formula-and-projective-space@2
  - sheaf.imported-real-line-bundles@1
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_dying_line_has_sign_holonomy
- kind: check
  ref: check.py::check_twisted_cochain_complex_of_lens_spaces
- kind: check
  ref: check.py::check_whitney_class_of_the_rank_two_complement
- kind: check
  ref: check.py::check_doubled_line_in_the_k_ring
- kind: check
  ref: check.py::check_gaussian_image_for_every_dimension
- kind: check
  ref: check.py::check_spin_class_in_dimension_five
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial
  - synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height
extraction:
  open_problem: op.wall-class-invariant
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Cross-references to the stored definite-side rung-count result written with its id (it cites clause (2) here for the twisted cohomology and is not a premise of this result); no change of content. Version kept: the entity was accepted in the same pass.'
  note: >-
    Attack item 1 of op.wall-class-invariant (the exact rung count between the stored lower bounds and e(L)), on
    every side, indefinite sides and the physical type (1, 2n+1) included. The stored two-rung result uses that the
    complement N of the necessity clause is a line with the class of the dying line; here N is a plane bundle, and
    the step that replaces "a line is fixed by its class" is that a plane bundle whose twisted Euler class has
    nowhere to live has a nowhere-zero section. The twisted integral cohomology of the lens spaces is computed in
    the stored cell model. For n >= 3 the conclusion needs neither the spin class nor the lambda-operations: only
    the stored K-ring (given the imported Atiyah-Hirzebruch filtration) and the fact that the complexification of
    a stably trivial bundle is stably trivial. For n = 2 it is conditional on the spin class, hypothesis (L2) of
    synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial, which is not in the store. Compared with the
    stored bounds: three at n = 2, 3, 4 becomes four; from n = 5 the stored K-theory bound already gives four or
    more. Not claimed: that four rungs suffice on any side; the definite-side count, where k = e(L) and
    stronger unstable obstructions apply
    (synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five, which cites the twisted
    cohomology of clause (2) here, supplies the upper bound 5 on the L^5(4) walls, and with the stored result on
    odd maps to four components gives k = 5 on their definite side given the imported Steenrod Fact). Background: (G+), the background (G) of the cited cohomology
    theorem extended by cohomology with local coefficients and the obstruction to a section of a circle bundle
    that need not be orientable; the extension is stated in the formal level and is not in the store. Transport-absent:
    bundle topology of the stored wall setting.
outside_ga:
  kind: other
  why: 'Clauses (1) to (3) are statements about real vector bundles over the wall, their Stiefel-Whitney classes, cohomology with twisted integer coefficients and the complex K-ring; none is a geometric-algebra identity. The algebra enters in the quarter turn v -> v . B of the stored lens walls, in the embedding of the dying line by a map that anticommutes with it, and in the ring map of the K-ring to span{1, e1e2}.'
---

## formal
Let $(M, G)$ be a tame corank-one degeneration (\claimref{sheaf.tameness}) with compact wall $\Sig$, physical side $\Mp$ of any signature $(p, q)$, $p \geq 1$, dying line $\shL$, $x := w_{1}(\shL)$, and $k(\Sig)$ the least number of rungs of a completion (\claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}). Write $\Z^{x}$ for the integer coefficient system on $\Sig$ twisted by $x$ (a loop acts by $-1$ exactly when $x$ is nonzero on it). Background (G+), an extension of the background (G) of \claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure}, which has cellular cohomology and the Euler class of an oriented plane bundle only. (G+) adds, as classical facts stated here and not in the store: cellular cohomology with local (twisted integer) coefficients, computed from the equivariant cochains of the universal cover; and for a plane bundle $N$, orientable or not, over a finite complex, that the only obstruction to a nowhere-zero section is a single class in $H^{2}(\Sig; \Z^{w_{1}(N)})$ (the fibre of the circle bundle is a circle, whose higher homotopy groups vanish).
\begin{enumerate}
\item \emph{(Three rungs, every side.)} If a three-rung completion exists and $H^{2}(\Sig; \Z^{x}) = 0$, then $\shL \oplus \shL$ is stably trivial. In general a three-rung completion gives a plane bundle $N$ over $\Sig$ with $w_{1}(N) = x$ and $\shL \oplus N$ stably trivial; when $x^{2} = 0$, $w(N) = 1 + x$.
\item \emph{(Twisted cohomology of the lens spaces.)} Let $\Sig_{n} = L^{2n+1}(4) = S^{2n+1}/\langle J \rangle$, $J(v) = v \cdot B$ the quarter turn in every coordinate plane, and $\shL$ the flat line on which $J$ acts by $-1$. In the equivariant cell structure of the cited theorem, $H^{j}(\Sig_{n}; \Z^{x}) = \Z_{2}$ for $j$ odd and $0$ for $j$ even, $0 \leq j \leq 2n + 1$, for every $n$. In particular $H^{2}(\Sig_{n}; \Z^{x}) = 0$.
\item \emph{(Lens walls.)} For $n \geq 2$ every tame wall with cross-section $\Sig_{n}$ and dying line $\shL$ has
\[
k(\Sig) \geq 4 \quad \text{on every side, whatever the signature of the physical side.}
\]
For $n \geq 3$ this holds given the K-ring of clause (6) of the cited theorem (itself given the imported Atiyah-Hirzebruch filtration, \claimref{synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory}): the complexification of $\shL \oplus \shL$ is $2\chi^{2}$, and $2(1 - \chi^{2}) \neq 0$ in $\Z[\chi]/(\chi^{4} - 1, (\chi - 1)^{n+1})$ for every $n \geq 3$; neither the spin class nor the lambda-operations are used. For $n = 2$ it holds given the spin class, hypothesis (L2) of \claimref{synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial} (cited there from memory, not in the store), by its clause (3): $q_{1}(\shL \oplus \shL) = 2y^{2} \neq 0$. With the stored upper bounds, $4 \leq k(\Sig) \leq 6$ on every side of the walls on $L^{5}(4)$ and $L^{7}(4)$, the physical types $(1, 5)$ and $(1, 7)$ included, where the stored lower bound was $3$. On $L^{5}(4)$ Theorem \claimref{synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five}, clause (2), gives an explicit odd map into five dimensions, so $e(\shL) \leq 5$ and $4 \leq k(\Sig) \leq 5$ on every side there (that result is not a premise of this one; the bound $6$ is what the stored results give); on $L^{7}(4)$ the window stays $4 \leq k(\Sig) \leq 6$.
\item \emph{(Scope.)} At $n = 1$ nothing is excluded: $\shL \oplus \shL$ is stably trivial on $L(4,1)$, and the stored two-rung completion with an indefinite side exists. The argument of (1) stops at three rungs: with four rungs $N$ has rank three and is not fixed by $w_{1}$. Whether four rungs suffice on an indefinite side of $L^{5}(4)$ is not decided here.
\end{enumerate}
Clause (3) at $n = 2$ is conditional on (L2); every clause is on the background (G+), the stored (G) extended as stated above.

## technical
The stored two-rung result rests on a simple fact: with two rungs the complement $N$ produced by the necessity clause of the parent claim is a line bundle with the class of the dying line, hence the dying line itself, so the doubled dying line is stably trivial. With three rungs $N$ is a plane bundle with $w_{1}(N) = x$. A plane bundle has a nowhere-zero section exactly when its twisted Euler class vanishes, and that class lives in the second cohomology with integers twisted by $w_{1}(N)$. On the quarter-turn lens spaces this group is zero: in the stored cell structure the twisted cochain complex alternates multiplication by $2$ and by $0$, so twisted cohomology is $\Z_{2}$ in odd degrees and vanishes in even ones. So $N$ splits as a trivial line plus a line of class $x$, which is the dying line again, and three rungs force the doubled dying line to be stably trivial exactly as two rungs do.

That it is not stably trivial is read in two ways. From dimension seven on, complexify: a stably trivial real bundle has stably trivial complexification, and the complexification $2\chi^{2}$ of the doubled line differs from $2$ in the stored K-ring, because $1 - \chi^{2}$ has order four or more there (an exact lattice computation at $n = 3$, and for $n \geq 4$ the ring map $\chi \mapsto e_{1}e_{2}$, under which $2(1 - \chi^{2})$ goes to $4 = -(1 - e_{1}e_{2})^{4}$, not a multiple of $(1 - e_{1}e_{2})^{5}$). In dimension five complex K-theory is blind, and the stored spin-class argument is used, with its hypothesis. The result raises the stored lower bound from three to four at $n = 2, 3, 4$, on indefinite sides as well as definite ones, and leaves the question whether four rungs can suffice on an indefinite side.

## lay
At a wall where the geometry changes signature in the well-behaved way the series assumes, extra pairs of directions (rungs) repair the wall, and earlier results showed that on walls shaped like certain lens spaces two rungs are never enough from dimension five on. This result shows that in dimension five and above three are not enough either, whatever the signature on the physical side (on the three-dimensional wall of this family two can suffice). The reason is that with three rungs the leftover twisted piece is a plane's worth of directions, and on these walls any such plane must contain an untwisted direction, which reduces the three-rung problem to the two-rung one. In dimension five the conclusion depends on one classical fact about spin structures that the store has not derived; in dimension seven and above it does not.

## one-liner
Assuming the tameness hypotheses, a three-rung completion forces $\shL \oplus \shL$ to be stably trivial whenever $H^{2}(\Sig; \Z^{x}) = 0$; on the quarter-turn lens walls $L^{2n+1}(4)$ of dimension five and more ($n \geq 2$) that group vanishes and the doubled dying line is not stably trivial (by the stored K-ring for $n \geq 3$, given the spin class, cited from memory, for $n = 2$), so $k \geq 4$ on every side.
